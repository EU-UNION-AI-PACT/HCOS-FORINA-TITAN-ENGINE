"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
SOVEREIGN NETWORK GUARD & FAIL-CLOSED EGRESS ISOLATION
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
import os
import socket
from contextlib import contextmanager
from typing import Dict, Any, Tuple


class SovereignNetworkViolation(Exception):
    """Raised when any code attempts non-loopback egress or WAN connection in Sovereign Zone."""
    pass


class SovereignNetworkGuard:
    """
    Enforces the Local Sovereign Air-Gap Boundary.
    Ensures that zero unauthorized outgoing WAN connections or foreign listeners can be established.
    """
    LOOPBACK_IPS = {"127.0.0.1", "localhost", "::1"}
    ALLOWED_HOSTS = {"127.0.0.1", "localhost", "::1", "0.0.0.0"}  # 0.0.0.0 only checked for listeners
    _is_permanently_installed: bool = False
    _original_socket_connect = socket.socket.connect

    @classmethod
    def is_loopback(cls, host: str) -> bool:
        return host in cls.LOOPBACK_IPS

    @classmethod
    def verify_listener_isolation(cls, host: str) -> bool:
        """Listeners must strictly bind to loopback (127.0.0.1 or ::1), never WAN/0.0.0.0."""
        return cls.is_loopback(host)

    @staticmethod
    def _guarded_connect(sock_self: socket.socket, address: Tuple[str, int] | str):
        if isinstance(address, tuple):
            dest_host = address[0]
            # Disallow any non-loopback destination (IP or hostname)
            if dest_host not in SovereignNetworkGuard.LOOPBACK_IPS:
                raise SovereignNetworkViolation(
                    f"[SOVEREIGN_AIRGAP_FAIL_CLOSED] Unerlaubter WAN-Verbindungsversuch zu {dest_host}:{address[1]} blockiert."
                )
        elif isinstance(address, str):
            # For AF_UNIX domain sockets or path strings, verify safe local path
            if not address.startswith(("/", ".")):
                raise SovereignNetworkViolation(
                    f"[SOVEREIGN_AIRGAP_FAIL_CLOSED] Unerlaubte Adressangabe: {address}"
                )
        return SovereignNetworkGuard._original_socket_connect(sock_self, address)

    @classmethod
    def install_process_airgap_guard(cls) -> None:
        """
        Permanently hooks socket.socket.connect for the entire process lifetime.
        Sets OS process environment flag 'FORINA_AIRGAP_ENFORCED=1'.
        """
        socket.socket.connect = cls._guarded_connect
        cls._is_permanently_installed = True
        os.environ["FORINA_AIRGAP_ENFORCED"] = "1"

    @classmethod
    def uninstall_process_airgap_guard(cls) -> None:
        """Restores original socket connect (used strictly for teardown or testing scopes)."""
        socket.socket.connect = cls._original_socket_connect
        cls._is_permanently_installed = False
        os.environ.pop("FORINA_AIRGAP_ENFORCED", None)

    @classmethod
    def is_airgap_active(cls) -> bool:
        return cls._is_permanently_installed or (socket.socket.connect == cls._guarded_connect)

    @classmethod
    @contextmanager
    def sovereign_airgap_scope(cls):
        """
        Scoped airgap guard: Enforces runtime socket interception within a context.
        """
        prev_connect = socket.socket.connect
        socket.socket.connect = cls._guarded_connect
        try:
            yield
        finally:
            socket.socket.connect = prev_connect

    @classmethod
    def run_airgap_probe_test(cls) -> Dict[str, Any]:
        """
        Executes active negative verification against external WAN destinations.
        Asserts fail-closed interception of:
        - WAN IPv4 (8.8.8.8:53)
        - Cloudflare WAN IPv4 (1.1.1.1:80)
        - External Hostname (example.com:443)
        And confirms loopback calls are permitted to proceed to OS network stack.
        """
        test_probes = [
            ("8.8.8.8", 53),
            ("1.1.1.1", 80),
            ("example.com", 443),
        ]
        blocked_probes = []

        for host, port in test_probes:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            try:
                s.settimeout(0.5)
                s.connect((host, port))
                s.close()
                return {
                    "passed": False,
                    "error": f"Sicherheitsverletzung: Nicht-autorisierte WAN-Verbindung zu {host}:{port} wurde NICHT blockiert!"
                }
            except SovereignNetworkViolation:
                blocked_probes.append(f"{host}:{port}")
            except Exception as e:
                return {
                    "passed": False,
                    "error": f"Unerwarteter Fehler bei Air-Gap Negativtest für {host}:{port}: {e}"
                }
            finally:
                try:
                    s.close()
                except Exception:
                    pass

        # Loopback smoke test: Should not trigger SovereignNetworkViolation
        loopback_s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            loopback_s.settimeout(0.1)
            loopback_s.connect(("127.0.0.1", 1))
        except SovereignNetworkViolation:
            return {
                "passed": False,
                "error": "Fehlalarm: Lokale Loopback-Verbindung (127.0.0.1) wurde fälschlicherweise blockiert."
            }
        except (ConnectionRefusedError, socket.timeout, OSError):
            # Normal OS socket behavior when port is closed, NOT blocked by air-gap guard
            pass
        finally:
            try:
                loopback_s.close()
            except Exception:
                pass

        return {
            "passed": True,
            "blocked_targets": blocked_probes,
            "loopback_verified": True
        }
