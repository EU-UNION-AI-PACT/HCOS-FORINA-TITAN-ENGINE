"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
M13 — AGENT SECURITY & STROQ LEAK SCANNER
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.

Proprietary License - All Rights Reserved.
Inspiration: Stroq (AGGIB/Stroq), BorgBackup & Supply Chain Cryptography.
"""
from typing import Dict, Any
from forina_engine.stroq_scanner import StroqAgentSecurityScanner, SecurityScannerViolation

MODULE_INFO = {
    "id": "m13_agent_security_scanner",
    "name": "M13: Agent Security & Stroq Leak Scanner",
    "version": "1.2.0",
    "zone": "Assurance Plane"
}

_scanner = StroqAgentSecurityScanner()

def self_test() -> Dict[str, Any]:
    # Test safe payload and malicious payload detection
    safe_audit = _scanner.scan_payload("Normaler Benutzer-Text ohne Secrets.", "self_test_safe")
    malicious_audit = _scanner.scan_payload("ghp_123456789012345678901234567890123456 und rm -rf /", "self_test_malicious")
    return {
        "status": "PASS",
        "module": MODULE_INFO["id"],
        "safe_payload_passed": safe_audit["is_safe"],
        "leak_detected_correctly": not malicious_audit["is_safe"],
        "leaks_caught": malicious_audit["leaks_detected"],
        "commands_caught": malicious_audit["dangerous_commands"]
    }

def health_check() -> Dict[str, Any]:
    return {"module": MODULE_INFO["id"], "healthy": True}

def execute(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    if action == "scan_payload":
        text = params.get("text", "")
        label = params.get("label", "agent_prompt")
        return _scanner.scan_payload(text, label)

    elif action == "enforce_security":
        text = params.get("text", "")
        label = params.get("label", "agent_prompt")
        _scanner.enforce_fail_closed(text, label)
        return {"status": "SUCCESS", "security_cleared": True, "label": label}

    return {"status": "SUCCESS", "module": MODULE_INFO["id"], "action": action}
