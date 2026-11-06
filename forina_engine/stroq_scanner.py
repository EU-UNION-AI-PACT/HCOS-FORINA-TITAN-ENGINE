"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
STROQ AGENT SESSION SECURITY & LEAK SCANNER (M13)
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.

Proprietary License - All Rights Reserved.
Inspiration: Stroq (AGGIB/Stroq) Agent Session Security & Secret Leak Prevention.
"""
from __future__ import annotations
import re
import time
from typing import Dict, Any, List


class SecurityScannerViolation(Exception):
    """Raised when an agent session contains prohibited credentials or dangerous commands."""
    pass


class StroqAgentSecurityScanner:
    """
    Session & Prompt Auditor for AI Agents.
    Scans runtime payloads before dispatching to external APIs or local executors.
    """

    SECRET_PATTERNS = [
        (re.compile(r"-----BEGIN [A-Z ]*PRIVATE KEY-----"), "ASYMMETRIC_PRIVATE_KEY"),
        (re.compile(r"ghp_[A-Za-z0-9_]{36}"), "GITHUB_PERSONAL_ACCESS_TOKEN"),
        (re.compile(r"sk-[A-Za-z0-9_-]{32,}"), "OPENAI_OR_CLAUDE_SECRET_KEY"),
        (re.compile(r"FORINA-[A-Za-z0-9_-]{20,}"), "FORINA_INTERNAL_MASTER_KEY"),
        (re.compile(r"password\s*[:=]\s*['\"][^'\"]{6,}['\"]", re.IGNORECASE), "PLAIN_PASSWORD_CONFIG")
    ]

    DANGEROUS_COMMANDS = [
        re.compile(r"\brm\s+-rf\s+[/~*]", re.IGNORECASE),
        re.compile(r"\bsudo\s+", re.IGNORECASE),
        re.compile(r"\bcurl\s+.*\|\s*(?:bash|sh)\b", re.IGNORECASE),
        re.compile(r"\bchmod\s+777\b", re.IGNORECASE),
        re.compile(r"\bmkfs\.", re.IGNORECASE),
        re.compile(r"\bdd\s+if=.*of=/dev/", re.IGNORECASE)
    ]

    INJECTION_PATTERNS = [
        re.compile(r"ignore\s+(?:all\s+)?previous\s+instructions", re.IGNORECASE),
        re.compile(r"system\s*override\s*:\s*disable\s*guardrails", re.IGNORECASE),
        re.compile(r"you\s+are\s+now\s+in\s+(?:unrestricted|dan)\s+mode", re.IGNORECASE)
    ]

    def scan_payload(self, text: str, context_label: str = "agent_prompt") -> Dict[str, Any]:
        """
        Audits a string payload for leaks, dangerous commands, or injection signatures.
        """
        leaks_found = []
        commands_found = []
        injections_found = []

        # 1. Secret scanning
        for pattern, leak_type in self.SECRET_PATTERNS:
            if pattern.search(text):
                leaks_found.append(leak_type)

        # 2. Dangerous command scanning
        for pattern in self.DANGEROUS_COMMANDS:
            if match := pattern.search(text):
                commands_found.append(match.group(0))

        # 3. Prompt injection scanning
        for pattern in self.INJECTION_PATTERNS:
            if match := pattern.search(text):
                injections_found.append(match.group(0))

        is_safe = (len(leaks_found) == 0 and len(commands_found) == 0 and len(injections_found) == 0)

        result = {
            "context_label": context_label,
            "is_safe": is_safe,
            "leaks_detected": leaks_found,
            "dangerous_commands": commands_found,
            "prompt_injections": injections_found,
            "scanned_bytes": len(text.encode("utf-8")),
            "audit_timestamp": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }

        return result

    def enforce_fail_closed(self, text: str, context_label: str = "agent_prompt") -> None:
        """
        Raises SecurityScannerViolation if any violation is detected.
        """
        audit = self.scan_payload(text, context_label)
        if not audit["is_safe"]:
            violations = []
            if audit["leaks_detected"]:
                violations.append(f"Credential-Leaks: {audit['leaks_detected']}")
            if audit["dangerous_commands"]:
                violations.append(f"Gefährliche Befehle: {audit['dangerous_commands']}")
            if audit["prompt_injections"]:
                violations.append(f"Prompt-Injektion: {audit['prompt_injections']}")
            raise SecurityScannerViolation(f"[STROQ-SCANNER ALARM] {context_label} verweigert: {'; '.join(violations)}")
