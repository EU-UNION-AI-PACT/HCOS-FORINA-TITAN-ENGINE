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
        "clearing_systems": ["TARGET2", "T2S", "TIPS (TARGET Instant Payment Settlement)", "Pontes DLT Wholesale Bridge"],
        "standards": ["ISO 20022", "SEPA Rulebook", "ESCB Public Key Infrastructure", "DLT Wholesale Interoperability"],
        "status": "SOVEREIGN_MAPPED"
    },
    {
        "id": "BUNDESBANK",
        "name": "Deutsche Bundesbank",
        "jurisdiction": "Deutschland",
        "iso_code": "EUR",
        "clearing_systems": ["RCS (Retail Clearing Service)", "EMZ (Elektronischer Massenzahlungsverkehr)", "Trigger-Lösung (DLT)"],
        "standards": ["FinTS 4.0", "EBICS 3.0", "ISO 20022"],
        "status": "SOVEREIGN_MAPPED"
    },
    {
        "id": "SNB",
        "name": "Schweizerische Nationalbank (SNB)",
        "jurisdiction": "Schweiz",
        "iso_code": "CHF",
        "clearing_systems": ["SIC (Swiss Interbank Clearing)", "euroSIC", "Project Helvetia (wCBDC)"],
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

EZB_PONTES_SPEC = {
    "protocol": "EZB Pontes DLT Wholesale Settlement Bridge",
    "lead_entity": "Europäische Zentralbank (Eurosystem)",
    "official_launch": "2026-09-21 (Q3 2026)",
    "purpose": "Verbindung privater Blockchain- und DLT-Netzwerke mit dem TARGET-Abwicklungssystem der Zentralbank zur Großbetragsabwicklung in digitalem Zentralbankgeld (wCBDC)",
    "key_capabilities": [
        "Delivery-versus-Payment (DvP) Abwicklung für tokenisierte Wertpapiere",
        "Interoperabilitätsbrücke zwischen Distributed Ledger und klassischer TARGET-Infrastruktur",
        "Wholesale-Settlement ohne Drittparteienrisiko in digitalem Zentralbankgeld",
        "Schnittstellen-Mapping zu ISO 20022 camt/pain Schemata"
    ],
    "hcos_integration": "M08 Finance Engine · ReadOnlyTransactionScope (Beobachtung, Nachweiserfassung & Zero-Settlement Schutz)"
}

OPEN_BANKING_PROVIDERS = [
    {"name": "Enable Banking (WorldBankEyes)", "hq": "Helsinki, Finnland", "coverage": "Europa (1.128+ Banken in 29 Ländern)", "protocols": ["ASPSP Open Banking", "Berlin Group", "STET", "PSD2 AISP/PISP"], "read_only": True},
    {"name": "Tink", "hq": "Stockholm, Schweden", "coverage": "Europa (3.400+ Banken)", "protocols": ["Berlin Group", "PSD2 XS2A", "Open Banking UK"], "read_only": True},
    {"name": "Plaid", "hq": "San Francisco / Amsterdam", "coverage": "USA, UK, Europa (12.000+ Institute)", "protocols": ["Open Finance API", "OAuth 2.0 FAPI"], "read_only": True},
    {"name": "finAPI", "hq": "München, Deutschland", "coverage": "DACH-Region (alle dt./österr. Banken)", "protocols": ["FinTS", "XS2A PSD2", "EBICS"], "read_only": True},
    {"name": "Klarna Open Banking", "hq": "Stockholm, Schweden", "coverage": "Europaweit (5.000+ Banken)", "protocols": ["Berlin Group NextGenPSD2"], "read_only": True},
    {"name": "Yapily", "hq": "London, UK", "coverage": "UK & Europa (2.000+ Institute)", "protocols": ["Open Banking FAPI 1.0 Advanced"], "read_only": True},
    {"name": "TrueLayer", "hq": "London / Dublin", "coverage": "UK, Irland, Europa, Australien", "protocols": ["PSD2 XS2A", "Payment Initiation API"], "read_only": True},
    {"name": "Salt Edge", "hq": "Toronto / Chișinău / London", "coverage": "Global (5.000+ Banken in 50+ Ländern)", "protocols": ["Berlin Group", "STET", "Open Banking UK"], "read_only": True},
    {"name": "Token.io", "hq": "San Francisco / London / Berlin", "coverage": "Europa (80% Kontenabdeckung)", "protocols": ["A2A Payments", "PSD2 Account Aggregation"], "read_only": True}
]

ENABLE_BANKING_APPLICATIONS = [
    {
        "app_name": "aether.worldbankeyes.eu",
        "app_id": "85550b82-143d-4b06-9aa1-d33c73584984",
        "status": "ACTIVE_SANDBOX",
        "environment": "SANDBOX",
        "services": ["Account Information", "Payment Initiation"],
        "description": "worldbankeyes enablebanking",
        "data_protection_email": "european-union@aether.worldbankeyes.eu",
        "privacy_url": "http://www.enablebanking-privacy.worldbankeyes.eu",
        "terms_url": "http://www.enablebanking-terms.worldbankeyes.eu",
        "redirect_url": "http://www.enablebanking-redirect.worldbankeyes.eu/",
        "key_storage": "LOCAL_CONFIG_UMASK_077 (No Git Storing)",
        "sovereign_governance": "Daniel Pohl · Royal Kaiser Charter RegSys"
    },
    {
        "app_name": "World BankEyes AeTHer (Production A)",
        "app_id": "b9339bba-4408-44f7-819b-92161cb7a399",
        "status": "INACTIVE_PENDING_LINKING",
        "environment": "PRODUCTION",
        "services": ["Account Information"],
        "description": "AeTHer WorldBankzEyes",
        "data_protection_email": "auroriatodaviareorgalaxylights@premiumlights.statesflowwishes.eu",
        "privacy_url": "https://privacy.SinceSgnInHolyThreeKingsTreesCrowns.know-now-no-know.EnableBanking.worldbankeyes.eu",
        "terms_url": "https://www.Terms.SinceSgnInHolyThreeKingsTreesCrowns.know-now-no-know.EnableBanking.worldbankeyes.eu.trustedorbitscodex.eu",
        "redirect_url": "https://redirect.sincesgninholythreekingstreescrowns.know-now-no-know.enablebanking.worldbankeyes.trustedorbitscodex.eu/",
        "key_storage": "LOCAL_CONFIG_UMASK_077 (No Git Storing)",
        "sovereign_governance": "Daniel Pohl · Royal Kaiser Charter RegSys"
    },
    {
        "app_name": "World BankEyes AeTHer (Production B - Germany)",
        "app_id": "d9689a63-024e-4dea-94db-b1e54fe03e69",
        "status": "INACTIVE_PENDING_LINKING",
        "environment": "PRODUCTION",
        "services": ["Account Information"],
        "description": "AeTHer WorldBankzEyes",
        "data_protection_email": "auroriatodaviareorgalaxylights@premiumlights.statesflowwishes.eu",
        "privacy_url": "https://privacy.SinceSgnInHolyThreeKingsTreesCrowns.know-now-no-know.EnableBanking.worldbankeyes.eu",
        "terms_url": "https://www.Terms.SinceSgnInHolyThreeKingsTreesCrowns.know-now-no-know.EnableBanking.worldbankeyes.eu.trustedorbitscodex.eu",
        "redirect_url": "https://redirect.sincesgninholythreekingstreescrowns.know-now-no-know.enablebanking.worldbankeyes.trustedorbitscodex.eu/",
        "key_storage": "LOCAL_CONFIG_UMASK_077 (No Git Storing)",
        "sovereign_governance": "Daniel Pohl · Royal Kaiser Charter RegSys"
    }
]

ENABLE_BANKING_APP_SPEC = ENABLE_BANKING_APPLICATIONS[0]


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

    def get_pontes_spec(self) -> Dict[str, Any]:
        return dict(EZB_PONTES_SPEC)

    def search_portals(self, query: str = "", category: str = "", limit: int = 50) -> List[Dict[str, str]]:
        csv_file = self.root / "docs" / "catalogs" / "INDEX_Finance_Portale.csv"
        if not csv_file.exists():
            return []
        import csv
        results = []
        q = query.lower().strip()
        c = category.lower().strip()
        try:
            with open(csv_file, mode="r", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f, delimiter=";")
                for row in reader:
                    name = row.get("Name", "").lower()
                    domain = row.get("Domain", "").lower()
                    cat = row.get("Kategorie", "").lower()
                    themen = row.get("Themen", "").lower()

                    if q and (q not in name and q not in domain and q not in themen):
                        continue
                    if c and c not in cat:
                        continue
                    results.append(row)
                    if len(results) >= limit:
                        break
        except Exception:
            pass
        return results

    def get_clevel_directory(self, company_filter: str = "") -> List[Dict[str, str]]:
        csv_file = self.root / "docs" / "catalogs" / "INDEX_Finance_CLevel.csv"
        if not csv_file.exists():
            return []
        import csv
        results = []
        cf = company_filter.lower().strip()
        try:
            with open(csv_file, mode="r", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f, delimiter=";")
                for row in reader:
                    unternehmensname = row.get("Unternehmen", "").lower()
                    if cf and cf not in unternehmensname:
                        continue
                    results.append(row)
        except Exception:
            pass
        return results

    def get_enable_banking_apps(self) -> List[Dict[str, Any]]:
        return list(ENABLE_BANKING_APPLICATIONS)

    def get_enable_banking_app(self, app_id: Optional[str] = None) -> Dict[str, Any]:
        if not app_id:
            return dict(ENABLE_BANKING_APP_SPEC)
        for app in ENABLE_BANKING_APPLICATIONS:
            if app["app_id"] == app_id:
                return dict(app)
        return dict(ENABLE_BANKING_APP_SPEC)

    def search_aspsp_banks(self, query: str = "", country: str = "", psu_type: str = "", service: str = "", status: str = "", limit: int = 50) -> List[Dict[str, str]]:
        csv_file = self.root / "docs" / "catalogs" / "ASPSP_1128_BANKEN_CATALOG.csv"
        if not csv_file.exists():
            return []
        import csv
        results = []
        q = query.lower().strip()
        c = country.upper().strip()
        pt = psu_type.lower().strip()
        srv = service.upper().strip()
        st = status.lower().strip()
        try:
            with open(csv_file, mode="r", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    brand = row.get("brand", "").lower()
                    country_code = row.get("country", "").upper()
                    row_psu = row.get("psu_type", "").lower()
                    row_srv = row.get("service", "").upper()
                    row_status = row.get("current_status", "").lower()

                    if q and q not in brand:
                        continue
                    if c and c != country_code:
                        continue
                    if pt and pt != row_psu:
                        continue
                    if srv and srv not in row_srv:
                        continue
                    if st and st != row_status:
                        continue
                    results.append(row)
                    if len(results) >= limit:
                        break
        except Exception:
            pass
        return results

    def get_aspsp_stats(self) -> Dict[str, Any]:
        csv_file = self.root / "docs" / "catalogs" / "ASPSP_1128_BANKEN_CATALOG.csv"
        if not csv_file.exists():
            return {"total_records": 0, "unique_brands": 0, "countries_count": 0, "countries": [], "status_distribution": {}}
        import csv
        countries = set()
        brands = set()
        total = 0
        status_counts = {"green": 0, "yellow": 0, "red": 0}
        try:
            with open(csv_file, mode="r", encoding="utf-8-sig") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    total += 1
                    b = row.get("brand", "").strip()
                    co = row.get("country", "").strip()
                    st = row.get("current_status", "").strip().lower()
                    if b:
                        brands.add(b)
                    if co:
                        countries.add(co)
                    if st in status_counts:
                        status_counts[st] += 1
                    else:
                        status_counts[st] = status_counts.get(st, 0) + 1
        except Exception:
            pass
        return {
            "total_records": total,
            "unique_brands": len(brands),
            "countries_count": len(countries),
            "countries": sorted(list(countries)),
            "status_distribution": status_counts
        }

    def get_summary(self) -> Dict[str, Any]:
        return {
            "mapped_central_banks": len(self.central_banks),
            "open_banking_providers": len(self.open_banking_providers),
            "supported_iso20022_schemas": len(self.get_iso20022_message_schemas()),
            "ezb_pontes_bridge": "INTEGRATED_SPEC_2026",
            "enable_banking_app": ENABLE_BANKING_APP_SPEC["app_name"],
            "enable_banking_status": ENABLE_BANKING_APP_SPEC["status"],
            "aspsp_eu_banks": 1128,
            "security_tier": "READ_ONLY_TRANSACTION_SCOPE (G05 Enforced)",
            "sovereign_governance": "Daniel Pohl, Royal Kaiser Charter RegSys"
        }
