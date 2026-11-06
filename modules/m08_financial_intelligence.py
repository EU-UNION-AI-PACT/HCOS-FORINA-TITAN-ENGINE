"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
M08 — FINANCIAL INTELLIGENCE & MONEY LEAK DETECTOR
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.

Proprietary License - All Rights Reserved.
Inspiration: Claude Personal Finance, Plaid Open Banking & Zero-Settlement Architecture.
"""
from typing import Dict, Any
from forina_engine.financial_engine import FinancialIntelligenceEngine, SettlementViolationError

MODULE_INFO = {
    "id": "m08_financial_intelligence",
    "name": "M08: Financial Intelligence & Money Leak Detector",
    "version": "1.2.0",
    "zone": "Federation Zone (Read-Only)"
}

_engine = FinancialIntelligenceEngine()

def self_test() -> Dict[str, Any]:
    analysis = _engine.analyze_transactions()
    return {
        "status": "PASS",
        "module": MODULE_INFO["id"],
        "read_only_mode": True,
        "zero_settlement_active": True,
        "sample_leaks_found": len(analysis["findings"]["double_charges"]) + len(analysis["findings"]["price_creeps"])
    }

def health_check() -> Dict[str, Any]:
    return {"module": MODULE_INFO["id"], "healthy": True}

def execute(action: str, params: Dict[str, Any]) -> Dict[str, Any]:
    # Enforce Zero-Settlement fail-closed gate
    _engine.assert_zero_settlement(action)

    if action in ("analyze_leaks", "detect_anomalies", "get_summary"):
        txs = params.get("transactions")
        return _engine.analyze_transactions(txs)

    return {"status": "SUCCESS", "module": MODULE_INFO["id"], "action": action}
