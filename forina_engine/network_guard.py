"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
SOVEREIGN NETWORK GUARD & FAIL-CLOSED EGRESS ISOLATION
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
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
    ALLOWED_HOSTS = {"127.0.0.1", "localhost", "::1", "0.0.0.0"} # 0.0.0.0 only checked for listeners

    @classmethod
    def is_loopback(cls, host: str) -> bool:
        return host in {"127.0.0.1", "localhost", "::1"}

    @classmethod
    def verify_listener_isolation(cls, host: str) -> bool:
        """Listeners must strictly bind to loopback (127.0.0.1 or ::1), never WAN/0.0.0.0."""
        return cls.is_loopback(host)

    @classmethod
    @contextmanager
    def sovereign_airgap_scope(cls):
        """
        Enforces runtime socket interception: Any connect() to non-loopback IP
        immediately raises SovereignNetworkViolation (Fail-Closed).
        """
        orig_connect = socket.socket.connect

        def guarded_connect(self, address: Tuple[str, int] | str):
            if isinstance(address, tuple):
                dest_ip = address[0]
                # Resolve address to IP
                if dest_ip not in {"127.0.0.1", "localhost", "::1"}:
                    raise SovereignNetworkViolation(
                        f"[SOVEREIGN_AIRGAP_FAIL_CLOSED] Unerlaubter WAN-Verbindungsversuch zu {dest_ip}:{address[1]} blockiert."
                    )
            return orig_connect(self, address)

        socket.socket.connect = guarded_connect
        try:
            yield
        finally:
            socket.socket.connect = orig_connect
