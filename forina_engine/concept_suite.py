"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
34 CONCEPT PAPERS SUITE & REGULATORY COMPLIANCE CATALOG
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
from typing import Dict, Any, List, Optional
from pathlib import Path


CONCEPT_PAPERS: List[Dict[str, Any]] = [
    {
        "nr": 1,
        "title": "Executive Summary & Vision 2030",
        "code": "VIS, STR, EU",
        "category": "Strategie & Vision",
        "modules": ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12", "M13"],
        "standards": ["EU AI Act", "DSGVO"],
        "summary": "Souveräne, sichere und rechtskonforme EU-Referenzplattform für KI, Web3, Finance und öffentliche Infrastruktur."
    },
    {
        "nr": 2,
        "title": "Gesamtarchitektur HCOS FORINA TITAN",
        "code": "ARCH, M01-M13",
        "category": "Architektur",
        "modules": ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12", "M13"],
        "standards": ["ISO 27001", "BSI IT-Grundschutz"],
        "summary": "Schichtenmodell, modularer Datenfluss und strikte Trust Boundaries zwischen Offline-Core und Online-Adaptern."
    },
    {
        "nr": 3,
        "title": "Modul-Matrix M01–M13 (Funktion & DAG)",
        "code": "MOD, DAG",
        "category": "Architektur",
        "modules": ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12", "M13"],
        "standards": ["ISO 9001", "IEC 62443"],
        "summary": "Deklaratives Fähigkeitssystem, Abhängigkeits-DAG und Zyklusfreiheit für alle 13 Mastermodule."
    },
    {
        "nr": 4,
        "title": "IA – Intelligent Automation Framework",
        "code": "IA, RPA, AGT",
        "category": "Automatisierung & KI",
        "modules": ["M01", "M05"],
        "standards": ["EU AI Act", "ISO 22989"],
        "summary": "Agentische Workflow-Steuerung, semantische Reasoning-Ketten und sichere Tool-Ausführung."
    },
    {
        "nr": 5,
        "title": "XD – eXperience Design & Sovereign UI/UX",
        "code": "XD, UX, UI",
        "category": "Design & Frontend",
        "modules": ["M03"],
        "standards": ["EN 301 549", "WCAG 2.2"],
        "summary": "Souveräne Ästhetik (#121212 Dark Mode & #FFD700 Gold), responsive Layouts und Accessibility."
    },
    {
        "nr": 6,
        "title": "50-Repository Ökosystem (Zonen & Integration)",
        "code": "REPO, ZON, INT",
        "category": "Ökosystem",
        "modules": ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12", "M13"],
        "standards": ["SPDX 3.0", "Open Source Governance"],
        "summary": "Drei isolierte Zonen (Sovereign 24, Dev 15, Federation 11) und Fail-Closed Governance."
    },
    {
        "nr": 7,
        "title": "Entwicklungsumgebung & DevSecOps",
        "code": "DEV, CI/CD",
        "category": "Entwicklung & Security",
        "modules": ["M02"],
        "standards": ["SLSA Level 4", "SBOM (CycloneDX)"],
        "summary": "Deterministische Build-Pipelines, softwareseitige Materiallisten und hermetische Toolchains."
    },
    {
        "nr": 8,
        "title": "Harness-Loop: Automatischer Umsetzungs- & Audit-Loop",
        "code": "LOOP, HNL",
        "category": "Continuous Assurance",
        "modules": ["M02", "M12"],
        "standards": ["Act Pack Zero Clock", "ISO 20000-1"],
        "summary": "8-stufiger geschlossener Zyklus: Plan, Build, Test, Audit, Certify, Deploy, Monitor, Improve."
    },
    {
        "nr": 9,
        "title": "Security Architecture & Zero-Trust Model",
        "code": "SEC, ZT, IAM",
        "category": "Sicherheit",
        "modules": ["M04", "M07"],
        "standards": ["NIST SP 800-207", "BSI CS 134"],
        "summary": "Striktes Zero-Trust: Niemals vertrauen, immer verifizieren. Keine impliziten Host-Rechte."
    },
    {
        "nr": 10,
        "title": "Netzwerkisolation & Air-Gap (Sovereign Mode)",
        "code": "AIR, NET, G03",
        "category": "Sicherheit & Isolation",
        "modules": ["M07", "M10"],
        "standards": ["BSI IT-Grundschutz INF.1", "Gate G03"],
        "summary": "Fail-Closed Egress-Sperre, striktes Loopback-Binding und Unterbindung nicht-autorisierter WAN-Verbindungen."
    },
    {
        "nr": 11,
        "title": "Datenhaltung, Verschlüsselung & Schlüsselmanagement",
        "code": "ENC, KMS, HSM",
        "category": "Kryptografie & Storage",
        "modules": ["M04", "M13"],
        "standards": ["BSI TR-02102", "FIPS 140-3", "AES-256-GCM"],
        "summary": "PBKDF2 Schlüsselableitung, AES-256-GCM Vault und hardwarenahe Schlüsselverwaltung."
    },
    {
        "nr": 12,
        "title": "Blockchain-Architektur & On-/Off-Chain-Integration",
        "code": "BC, DLT, SC",
        "category": "Web3 & Blockchain",
        "modules": ["M07", "M12"],
        "standards": ["ISO 23257", "EVM"],
        "summary": "Schnittstelle zwischen manipulationssicheren On-Chain Smart Contracts und isolierten Off-Chain Berechnungen."
    },
    {
        "nr": 13,
        "title": "Crypto-Implementation (Signaturen, Wallets, ZKP)",
        "code": "CRYPTO, ED25519",
        "category": "Kryptografie",
        "modules": ["M04", "M12"],
        "standards": ["RFC 8032 (Ed25519)", "ZK-SNARKs"],
        "summary": "Asymmetrische Ed25519 Signaturen, Zero-Knowledge Proofs und kryptografische Nonce-Sicherung."
    },
    {
        "nr": 14,
        "title": "Web3-Anwendungen & Dezentralisierung",
        "code": "WEB3, DID, VC",
        "category": "Web3 & Identität",
        "modules": ["M04", "M09"],
        "standards": ["W3C DID", "Verifiable Credentials", "eIDAS 2.0"],
        "summary": "Dezentrale Identifikatoren, souveräne Berechtigungsnachweise und DAO-Governance."
    },
    {
        "nr": 15,
        "title": "Finance-Implementation (Payments, DeFi, Escrow)",
        "code": "FIN, PAY, DEFI",
        "category": "Finanzinfrastruktur",
        "modules": ["M08"],
        "standards": ["PSD2", "ISO 20022", "Zero-Settlement Policy"],
        "summary": "Read-Only Transaktionsanalyse, Abo-Erkennung und striktes Verbot unautorisierter Zahlungen."
    },
    {
        "nr": 16,
        "title": "Rechenmodelle, Tokenisierung & Asset-Management",
        "code": "RWA, TOKEN, NFT",
        "category": "Finanzinfrastruktur",
        "modules": ["M08", "M12"],
        "standards": ["MiCA", "ERC-3643"],
        "summary": "Rechtskonforme Abbildung realer Vermögenswerte (RWA) und regulatorische Token-Compliance."
    },
    {
        "nr": 17,
        "title": "Datenschutz & DSGVO-Compliance",
        "code": "DSGVO, DPA, PIA",
        "category": "Datenschutz & Recht",
        "modules": ["M04", "M10"],
        "standards": ["DSGVO Art. 25/32", "ePrivacy"],
        "summary": "Privacy by Design, Datenschutz-Folgenabschätzung (DPIA) und cookie-freie Telemetrie."
    },
    {
        "nr": 18,
        "title": "Normen & Standards (ISO, IEC, EN, BSI, NIST)",
        "code": "ISO, IEC, EN",
        "category": "Standards & Normen",
        "modules": ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12", "M13"],
        "standards": ["ISO 27001", "ISO 9001", "IEC 62443", "EN 50600"],
        "summary": "Harmonisierte Anforderungsmatrix über europäische und internationale Industriestandards."
    },
    {
        "nr": 19,
        "title": "Zertifizierungen & Abzeichen (Kriterien & Prozesse)",
        "code": "CERT, AUD, BADGE",
        "category": "Zertifizierung",
        "modules": ["M12"],
        "standards": ["TISAX", "BSI-Grundschutz", "CIS Controls"],
        "summary": "Prüfprozesse für Nachweisdokumente, Abzeichenvergabe und externe Auditbereitschaft."
    },
    {
        "nr": 20,
        "title": "Automatisierte Audit- & Abnahme-Pipeline",
        "code": "AUDIT, G00-G12",
        "category": "Continuous Assurance",
        "modules": ["M12"],
        "standards": ["13-Gate Pipeline", "Assurance Gate Engine"],
        "summary": "Reale technische Prüfungen G00–G12 ohne Mock-Pässe und mit mathematischer Signaturprüfung."
    },
    {
        "nr": 21,
        "title": "Daten-Governance & Data Lifetime Management",
        "code": "DGM, RET, ERASE",
        "category": "Datenmanagement",
        "modules": ["M06", "M10"],
        "standards": ["DIN 66399", "Recht auf Vergessenwerden"],
        "summary": "Aufbewahrungsfristen, sichere Datenlöschung und granulare RACI-Verantwortlichkeiten."
    },
    {
        "nr": 22,
        "title": "Interoperabilität & Integrationen (APIs, Protokolle)",
        "code": "API, OIDC, SSO",
        "category": "Schnittstellen",
        "modules": ["M01", "M09"],
        "standards": ["REST", "gRPC", "WebSocket", "JMAP"],
        "summary": "Standardisierte Schnittstellenadapter für E-Mail (JMAP), Kalender und Partnersysteme."
    },
    {
        "nr": 23,
        "title": "Identität, Zugriff & Föderation (SSO, OIDC, SAML)",
        "code": "IAM, OIDC, FED",
        "category": "Identität & Zugriff",
        "modules": ["M04"],
        "standards": ["OIDC", "SAML 2.0", "FIDO2 / WebAuthn"],
        "summary": "Enterprise SSO, passwortlose Passkeys und dezentrale Identitätsföderation."
    },
    {
        "nr": 24,
        "title": "Monitoring, Observability & Incident Response",
        "code": "OBS, SIEM, IR",
        "category": "Betrieb & Observability",
        "modules": ["M10", "M13"],
        "standards": ["OpenTelemetry", "SIEM Best Practice"],
        "summary": "Strukturierte Audit-Logs, Metriken, Tracing und vordefinierte Incident Response Playbooks."
    },
    {
        "nr": 25,
        "title": "Business Continuity, Backup & Disaster Recovery",
        "code": "BCP, DR, RTO/RPO",
        "category": "Resilienz & Backup",
        "modules": ["M13"],
        "standards": ["ISO 22301", "BorgBackup"],
        "summary": "Deterministische Backups, TarSlip-geschützte Wiederherstellung und 100% Hash-Parität."
    },
    {
        "nr": 26,
        "title": "Legal, Lizenzierung & Open-Source-Governance",
        "code": "LIC, SPDX, OSS",
        "category": "Recht & Governance",
        "modules": ["M01", "M02"],
        "standards": ["SPDX 3.0", "Dual-Licensing"],
        "summary": "SPDX-Lizenzprüfung, Abgrenzung proprietärer Lizenzen und urheberrechtliche Absicherung."
    },
    {
        "nr": 27,
        "title": "Risikomanagement & Threat Modeling",
        "code": "RISK, TMT, TVM",
        "category": "Sicherheit & Risiko",
        "modules": ["M07", "M13"],
        "standards": ["STRIDE", "LINDDUN", "MITRE ATT&CK"],
        "summary": "Kontinuierliche Bedrohungsanalyse, Schwachstellen-Scans und Risikomatrizen."
    },
    {
        "nr": 28,
        "title": "Performance, Skalierung & Ressourcen-Management",
        "code": "PERF, SCALE, K8S",
        "category": "Performance",
        "modules": ["M02", "M05"],
        "standards": ["WebAssembly", "Green Computing"],
        "summary": "Multi-Threaded Workflows, speichereffiziente PWA-Architektur und schnelle Kaltstarts."
    },
    {
        "nr": 29,
        "title": "KI/LLM-Integration (BOBA, Stroq, RAG, Guardrails)",
        "code": "LLM, RAG, SAFE",
        "category": "Künstliche Intelligenz",
        "modules": ["M05", "M06", "M12", "M13"],
        "standards": ["BOBA-Bench", "OWASP Top 10 for LLM"],
        "summary": "Adversarial Prompt-Abwehr, Halluzinationserkennung und Multi-Agenten-Benchmarking."
    },
    {
        "nr": 30,
        "title": "Nachhaltigkeit & Green IT (ESG, CSRD)",
        "code": "ESG, GREEN, CO2",
        "category": "Nachhaltigkeit",
        "modules": ["M02", "M08"],
        "standards": ["CSRD", "GHG Protocol", "EU Green Deal"],
        "summary": "Messung des Rechenaufwands, CO2-neutrale Workloads und ESG-Audit-Reporting."
    },
    {
        "nr": 31,
        "title": "Betrieb, Wartung & Lifecycle-Management",
        "code": "OPS, LCM, SRE",
        "category": "Betrieb",
        "modules": ["M02", "M12"],
        "standards": ["SRE Principles", "Zero-Downtime"],
        "summary": "Automatisierte Wartungspfade, unterbrechungsfreie Updates und Lifecycle-Phasen."
    },
    {
        "nr": 32,
        "title": "Roadmap, Meilensteine & Release-Strategie",
        "code": "ROAD, MILE, REL",
        "category": "Strategie & Release",
        "modules": ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12", "M13"],
        "standards": ["SemVer 2.0.0", "Release Sign & Seal"],
        "summary": "Versionierungszyklen von v1.0 bis v2.0 und Vorbereitung des 2030 Sovereign Ecosystems."
    },
    {
        "nr": 33,
        "title": "Abnahme, Zertifizierung & Continuous Compliance",
        "code": "CC, ISO, LOOP",
        "category": "Continuous Assurance",
        "modules": ["M12"],
        "standards": ["Continuous Compliance", "Act Pack Loop"],
        "summary": "Laufende Re-Zertifizierung und automatisierte Nachweiserbringung im Harness-Loop."
    },
    {
        "nr": 34,
        "title": "Anhang: Abkürzungen, Keywords & Glossar (33+)",
        "code": "A-Z, KW, DEF",
        "category": "Glossar & Referenz",
        "modules": ["M01", "M02", "M03", "M04", "M05", "M06", "M07", "M08", "M09", "M10", "M11", "M12", "M13"],
        "standards": ["ISO/IEC Directives"],
        "summary": "Vollständiges Referenzglossar für über 33 Kernbegriffe, Abkürzungen und Standards."
    }
]


STANDARDS_CATALOG: List[Dict[str, Any]] = [
    {"name": "ISO/IEC 27001", "domain": "Informationssicherheit (ISMS)", "category": "International Standard", "url": "https://www.iso.org/isoiec-27001-information-security.html"},
    {"name": "ISO 9001", "domain": "Qualitätsmanagement", "category": "International Standard", "url": "https://www.iso.org/iso-9001-quality-management.html"},
    {"name": "ISO/IEC 20000-1", "domain": "IT-Service-Management (ITSM)", "category": "International Standard", "url": "https://www.iso.org/standard/70636.html"},
    {"name": "ISO 22301", "domain": "Business Continuity Management (BCM)", "category": "International Standard", "url": "https://www.iso.org/standard/75106.html"},
    {"name": "IEC 62443", "domain": "Industrielle IT-/OT-Sicherheit", "category": "Industrial Standard", "url": "https://www.iec.ch"},
    {"name": "EN 50600", "domain": "Rechenzentren & IT-Infrastruktur", "category": "European Standard", "url": "https://www.cenelec.eu"},
    {"name": "BSI IT-Grundschutz", "domain": "Deutscher Sicherheitsstandard (BSI)", "category": "National Standard", "url": "https://www.bsi.bund.de"},
    {"name": "TISAX", "domain": "Automotive Informationssicherheit", "category": "Industry Standard", "url": "https://www.enx.com/tisax"},
    {"name": "DSGVO / GDPR", "domain": "Europäischer Datenschutz", "category": "EU Regulation", "url": "https://eur-lex.europa.eu"},
    {"name": "eIDAS 2.0", "domain": "Elektronische Identitäten & Vertrauensdienste", "category": "EU Regulation", "url": "https://eur-lex.europa.eu"},
    {"name": "NIS2", "domain": "Netz- und Informationssystemsicherheit", "category": "EU Directive", "url": "https://eur-lex.europa.eu"},
    {"name": "DORA", "domain": "Digitale operationale Resilienz im Finanzsektor", "category": "EU Regulation", "url": "https://eur-lex.europa.eu"},
    {"name": "MiCA", "domain": "Märkte für Krypto-Assets", "category": "EU Regulation", "url": "https://eur-lex.europa.eu"},
    {"name": "CSRD / ESRS", "domain": "Nachhaltigkeitsberichterstattung (ESG)", "category": "EU Directive", "url": "https://eur-lex.europa.eu"}
]


class ConceptPaperSuite:
    """Provides querying and inspection for the 34 Concept Papers and Compliance Standards."""

    def __init__(self, project_root: Optional[Path] = None):
        self.root = project_root or Path(__file__).parent.parent
        self.papers = CONCEPT_PAPERS
        self.standards = STANDARDS_CATALOG

    def list_papers(self, category_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        if not category_filter:
            return list(self.papers)
        cat_lower = category_filter.lower()
        return [p for p in self.papers if cat_lower in p["category"].lower()]

    def get_paper(self, nr: int) -> Optional[Dict[str, Any]]:
        for p in self.papers:
            if p["nr"] == nr:
                return p
        return None

    def search_papers(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower()
        results = []
        for p in self.papers:
            text = f"{p['nr']} {p['title']} {p['code']} {p['category']} {' '.join(p['standards'])} {p['summary']}".lower()
            if q in text:
                results.append(p)
        return results

    def get_summary(self) -> Dict[str, Any]:
        categories = {}
        for p in self.papers:
            c = p["category"]
            categories[c] = categories.get(c, 0) + 1

        return {
            "total_papers": len(self.papers),
            "categories_breakdown": categories,
            "total_standards": len(self.standards),
            "suite_version": "v2.0 Concept Pack (33+ A4 Masterkonzept)",
            "sovereign_governance": "Daniel Pohl, Royal Kaiser Charter RegSys"
        }
