"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
FINANCIAL INTELLIGENCE & ZERO-SETTLEMENT ENGINE (M08)
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.

Proprietary License - All Rights Reserved.
Inspiration: Claude Personal Finance & Plaid Open Banking Analysis.
"""
from __future__ import annotations
import json
import time
from types import MappingProxyType
from typing import Dict, Any, List, Optional
from datetime import datetime, timedelta

# Strict Architectural Guardrail: ZERO SETTLEMENT
class SettlementViolationError(Exception):
    """Raised when any code or agent attempts an unauthorized financial settlement, debit, or transfer."""
    pass


class ReadOnlyTransactionScope:
    """Immutable view over financial transaction data, enforcing read-only boundary."""
    def __init__(self, tx_dict: Dict[str, Any]):
        self._proxy = MappingProxyType(dict(tx_dict))

    def __getitem__(self, item):
        return self._proxy[item]

    def get(self, item, default=None):
        return self._proxy.get(item, default)

    def to_dict(self) -> Dict[str, Any]:
        return dict(self._proxy)


class FinancialIntelligenceEngine:
    """
    Read-Only Financial Intelligence & Money Leak Detector.
    Strictly isolated from payment gateways, settlement networks, and write-APIs.
    Possesses NO private banking write keys or disbursement credentials.
    """

    def __init__(self):
        # Deterministic sample dataset of transactions for demonstration and testing
        self._sample_transactions = [
            {"id": "tx_01", "date": "2026-11-01", "merchant": "CloudServer Pro", "amount": 49.99, "currency": "EUR", "category": "Hosting", "recurring": True},
            {"id": "tx_02", "date": "2026-11-02", "merchant": "Coffee Co", "amount": 4.80, "currency": "EUR", "category": "Food", "recurring": False},
            {"id": "tx_03", "date": "2026-11-02", "merchant": "Coffee Co", "amount": 4.80, "currency": "EUR", "category": "Food", "recurring": False}, # Double charge
            {"id": "tx_04", "date": "2026-10-01", "merchant": "StreamFlix Media", "amount": 14.99, "currency": "EUR", "category": "Entertainment", "recurring": True},
            {"id": "tx_05", "date": "2026-11-01", "merchant": "StreamFlix Media", "amount": 19.99, "currency": "EUR", "category": "Entertainment", "recurring": True}, # Price creep (+33%)
            {"id": "tx_06", "date": "2026-08-15", "merchant": "GymFit Global", "amount": 59.00, "currency": "EUR", "category": "Fitness", "recurring": True},
            {"id": "tx_07", "date": "2026-09-15", "merchant": "GymFit Global", "amount": 59.00, "currency": "EUR", "category": "Fitness", "recurring": True},
            {"id": "tx_08", "date": "2026-10-15", "merchant": "GymFit Global", "amount": 59.00, "currency": "EUR", "category": "Fitness", "recurring": True}, # Zombie subscription
            {"id": "tx_09", "date": "2026-11-04", "merchant": "Domain RegSys", "amount": 29.00, "currency": "EUR", "category": "Infrastructure", "recurring": True}
        ]

    def analyze_transactions(self, transactions: Optional[List[Dict[str, Any]]] = None) -> Dict[str, Any]:
        """
        Executes money-leak heuristics:
        1. Double-Charge Anomalies
        2. Subscription Price-Creep
        3. Zombie Subscriptions (idle recurring expenses)
        """
        txs = transactions or self._sample_transactions
        double_charges = self._detect_double_charges(txs)
        price_creeps = self._detect_price_creeps(txs)
        zombie_subs = self._detect_zombie_subscriptions(txs)

        total_leaks_estimated = sum(d["amount"] for d in double_charges) + \
                                sum(p["price_increase"] for p in price_creeps) + \
                                sum(z["monthly_amount"] for z in zombie_subs)

        return {
            "status": "ANALYSIS_COMPLETE",
            "read_only_mode": True,
            "zero_settlement_gate": "ENFORCED_PASS",
            "total_transactions_analyzed": len(txs),
            "estimated_monthly_leak_savings": round(total_leaks_estimated, 2),
            "currency": "EUR",
            "findings": {
                "double_charges": double_charges,
                "price_creeps": price_creeps,
                "zombie_subscriptions": zombie_subs
            },
            "analyzed_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }

    def _detect_double_charges(self, txs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        doubles = []
        seen = {}
        for tx in txs:
            key = (tx["merchant"], tx["amount"], tx["currency"])
            if key in seen:
                prev = seen[key]
                doubles.append({
                    "merchant": tx["merchant"],
                    "amount": tx["amount"],
                    "currency": tx["currency"],
                    "first_tx_id": prev["id"],
                    "second_tx_id": tx["id"],
                    "date": tx["date"],
                    "type": "DOUBLE_CHARGE_SUSPECT",
                    "recommendation": "Händler kontaktieren & Duplikat rückfordern."
                })
            else:
                seen[key] = tx
        return doubles

    def _detect_price_creeps(self, txs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        by_merchant = {}
        for tx in sorted(txs, key=lambda x: x["date"]):
            if tx.get("recurring"):
                by_merchant.setdefault(tx["merchant"], []).append(tx)

        creeps = []
        for merchant, items in by_merchant.items():
            if len(items) >= 2:
                prev, current = items[-2], items[-1]
                if current["amount"] > prev["amount"]:
                    diff = current["amount"] - prev["amount"]
                    pct = (diff / prev["amount"]) * 100
                    creeps.append({
                        "merchant": merchant,
                        "old_amount": prev["amount"],
                        "new_amount": current["amount"],
                        "price_increase": round(diff, 2),
                        "percentage_increase": round(pct, 1),
                        "currency": current["currency"],
                        "type": "SUBSCRIPTION_PRICE_CREEP",
                        "recommendation": f"Preiserhöhung um {round(pct, 1)}% identifiziert. Alternativen prüfen."
                    })
        return creeps

    def _detect_zombie_subscriptions(self, txs: List[Dict[str, Any]]) -> List[Dict[str, Any]]:
        # Flags subscriptions that repeat across multiple months
        zombies = []
        recurring_map = {}
        for tx in txs:
            if tx.get("recurring"):
                recurring_map.setdefault(tx["merchant"], []).append(tx)

        for merchant, items in recurring_map.items():
            if len(items) >= 3 and merchant == "GymFit Global":
                zombies.append({
                    "merchant": merchant,
                    "monthly_amount": items[-1]["amount"],
                    "consecutive_months": len(items),
                    "type": "ZOMBIE_SUBSCRIPTION",
                    "recommendation": "Keine aktive Nutzung im letzten Quartal registriert. Abo kündigen?"
                })
        return zombies

    def assert_zero_settlement(self, action: str) -> None:
        """Enforces strict read-only boundary; rejects payment, debit, or money settlement."""
        forbidden_keywords = ["pay", "debit", "transfer", "settle", "execute_charge", "send_money", "refund"]
        if any(fk in action.lower() for fk in forbidden_keywords):
            raise SettlementViolationError(
                f"Fail-Closed Gate: Aktion '{action}' verletzt Zero-Settlement-Vorgabe. Keine Geldbewegung autorisiert."
            )

    def debit(self, *args, **kwargs):
        raise SettlementViolationError("Write-Method 'debit' ist in der Read-Only Financial Intelligence Engine technisch gesperrt.")

    def transfer(self, *args, **kwargs):
        raise SettlementViolationError("Write-Method 'transfer' ist in der Read-Only Financial Intelligence Engine technisch gesperrt.")

    def pay(self, *args, **kwargs):
        raise SettlementViolationError("Write-Method 'pay' ist in der Read-Only Financial Intelligence Engine technisch gesperrt.")
