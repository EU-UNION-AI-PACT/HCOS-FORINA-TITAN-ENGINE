"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
INSTITUTIONAL FINANCE, CENTRAL BANKING & OPEN BANKING REGISTRY
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
Sovereign Legal Provenance:
Daniel Pohl, Royal Kaiser Charter RegSys
PIC: 867679357 | USt-IdNr.: DE31353063511 | D-U-N-S: 315676980 & 317066336
Global LEI: 894500GBJSIW8L6ET310 | UNGM: 1172700
"""
from __future__ import annotations
import json
from pathlib import Path
from typing import Dict, Any, List, Optional


CENTRAL_BANKS = [
    {
        "id": "EZB",
        "name": "Europäische Zentralbank (EZB / ECB)",
        "jurisdiction": "Eurozone / EU",
        "iso_code": "EUR",
        "clearing_systems": ["TARGET2", "T2S", "TIPS (TARGET Instant Payment Settlement)"],
        "standards": ["ISO 20022", "SEPA Rulebook", "ESCB Public Key Infrastructure"],
        "status": "SOVEREIGN_MAPPED"
    },
    {
        "id": "BUNDESBANK",
        "name": "Deutsche Bundesbank",
        "jurisdiction": "Deutschland",
        "iso_code": "EUR",
        "clearing_systems": ["RCS (Retail Clearing Service)", "EMZ (Elektronischer Massenzahlungsverkehr)"],
        "standards": ["FinTS 4.0", "EBICS 3.0", "ISO 20022"],
        "status": "SOVEREIGN_MAPPED"
    },
    {
        "id": "SNB",
        "name": "Schweizerische Nationalbank (SNB)",
        "jurisdiction": "Schweiz",
        "iso_code": "CHF",
        "clearing_systems": ["SIC (Swiss Interbank Clearing)", "euroSIC"],
        "standards": ["SIC ISO 20022", "EBICS Switzerland"],
        "status": "SOVEREIGN_MAPPED"
    },
    {
        "id": "BIS",
        "name": "Bank für Internationalen Zahlungsausgleich (BIZ / BIS)",
        "jurisdiction": "International (Basel)",
        "iso_code": "SDR",
        "clearing_systems": ["Project Agora", "Project Nexus", "mBridge"],
        "standards": ["Basel III / IV", "CPMI-IOSCO Principles", "LEI ROC"],
        "status": "SOVEREIGN_MAPPED"
    },
    {
        "id": "FED",
        "name": "Federal Reserve System (Fed)",
        "jurisdiction": "USA",
        "iso_code": "USD",
        "clearing_systems": ["Fedwire", "FedNow", "CHIPS"],
        "standards": ["Fedwire ISO 20022", "NACHA ACH"],
        "status": "FEDERATION_INTEGRATION"
    },
    {
        "id": "BOE",
        "name": "Bank of England (BoE)",
        "jurisdiction": "Großbritannien",
        "iso_code": "GBP",
        "clearing_systems": ["CHAPS", "Faster Payments Service (FPS)"],
        "standards": ["CHAPS ISO 20022", "Open Banking Standard UK"],
        "status": "FEDERATION_INTEGRATION"
    }
]

OPEN_BANKING_PROVIDERS = [
    {"name": "Tink", "hq": "Stockholm, Schweden", "coverage": "Europa (3.400+ Banken)", "protocols": ["Berlin Group", "PSD2 XS2A", "Open Banking UK"], "read_only": True},
    {"name": "Plaid", "hq": "San Francisco / Amsterdam", "coverage": "USA, UK, Europa (12.000+ Institute)", "protocols": ["Open Finance API", "OAuth 2.0 FAPI"], "read_only": True},
    {"name": "finAPI", "hq": "München, Deutschland", "coverage": "DACH-Region (alle dt./österr. Banken)", "protocols": ["FinTS", "XS2A PSD2", "EBICS"], "read_only": True},
    {"name": "Klarna Open Banking", "hq": "Stockholm, Schweden", "coverage": "Europaweit (5.000+ Banken)", "protocols": ["Berlin Group NextGenPSD2"], "read_only": True},
    {"name": "Yapily", "hq": "London, UK", "coverage": "UK & Europa (2.000+ Institute)", "protocols": ["Open Banking FAPI 1.0 Advanced"], "read_only": True},
    {"name": "TrueLayer", "hq": "London / Dublin", "coverage": "UK, Irland, Europa, Australien", "protocols": ["PSD2 XS2A", "Payment Initiation API"], "read_only": True},
    {"name": "Salt Edge", "hq": "Toronto / Chișinău / London", "coverage": "Global (5.000+ Banken in 50+ Ländern)", "protocols": ["Berlin Group", "STET", "Open Banking UK"], "read_only": True},
    {"name": "Token.io", "hq": "San Francisco / London / Berlin", "coverage": "Europa (80% Kontenabdeckung)", "protocols": ["A2A Payments", "PSD2 Account Aggregation"], "read_only": True}
]


class InstitutionalFinanceRegistry:
    """Manages Central Banking integrations, ISO 20022 schemas, and Open Banking providers."""

    def __init__(self, project_root: Optional[Path] = None):
        self.root = project_root or Path(__file__).parent.parent
        self.central_banks = CENTRAL_BANKS
        self.open_banking_providers = OPEN_BANKING_PROVIDERS

    def get_central_banks(self) -> List[Dict[str, Any]]:
        return list(self.central_banks)

    def get_open_banking_providers(self) -> List[Dict[str, Any]]:
        return list(self.open_banking_providers)

    def get_iso20022_message_schemas(self) -> List[Dict[str, str]]:
        return [
            {"code": "pain.001.001.09", "name": "Customer Credit Transfer Initiation (Zahlungsauftrag)", "scope": "READ_ONLY_SIMULATION"},
            {"code": "pain.002.001.10", "name": "Payment Status Report (Zahlungsstatusmeldung)", "scope": "ACTIVE_VERIFICATION"},
            {"code": "camt.052.001.08", "name": "Bank To Customer Account Report (Intraday-Umsätze)", "scope": "OBSERVABILITY"},
            {"code": "camt.053.001.08", "name": "Bank To Customer Statement (Tagesend-Kontoauszug)", "scope": "RECONCILIATION"},
            {"code": "camt.054.001.08", "name": "Debit/Credit Notification (Einzel-Belastung/Gutschrift)", "scope": "AUDIT_PROVENANCE"}
        ]

    def get_summary(self) -> Dict[str, Any]:
        return {
            "mapped_central_banks": len(self.central_banks),
            "open_banking_providers": len(self.open_banking_providers),
            "supported_iso20022_schemas": len(self.get_iso20022_message_schemas()),
            "security_tier": "READ_ONLY_TRANSACTION_SCOPE (G05 Enforced)",
            "sovereign_governance": "Daniel Pohl, Royal Kaiser Charter RegSys"
        }
