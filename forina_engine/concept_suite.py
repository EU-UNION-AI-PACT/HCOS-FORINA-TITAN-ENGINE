"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
34 CONCEPT PAPERS SUITE & REGULATORY COMPLIANCE CATALOG
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
Sovereign Legal Provenance:
Daniel Pohl, Royal Kaiser Charter RegSys
PIC: 867679357 | USt-IdNr.: DE31353063511 | D-U-N-S: 315676980 & 317066336
Global LEI: 894500GBJSIW8L6ET310 | UNGM: 1172700
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
        "modules": ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13'],
        "standards": ['EU AI Act', 'DSGVO Art. 25/32', 'BSI IT-Grundschutz', 'ISO 27001'],
        "file": "docs/concept_papers/01_Executive_Summary_Vision_2030.md",
        "summary": "Bereitstellung einer souveränen, manipulationssicheren und vollständig rechtskonformen EU-Referenzplattform für KI, Web3, Finanzen und geschäftskritische Infrastruktur."
    },
    {
        "nr": 2,
        "title": "Gesamtarchitektur HCOS FORINA TITAN",
        "code": "ARCH, M01-M13",
        "category": "Architektur",
        "modules": ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13'],
        "standards": ['ISO 27001:2022', 'BSI CS 134', 'NIST SP 800-207'],
        "file": "docs/concept_papers/02_Gesamtarchitektur_HCOS_FORINA_TITAN.md",
        "summary": "Strikte architektonische Schichtentrennung zwischen hermetischem Offline-Core, lokalen Verarbeitungsmodulen und geschützten Online-Adaptern."
    },
    {
        "nr": 3,
        "title": "Modul-Matrix M01–M13 (Funktion & DAG)",
        "code": "MOD, DAG",
        "category": "Architektur",
        "modules": ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13'],
        "standards": ['ISO 9001:2015', 'IEC 62443-4-1', 'IEEE 830'],
        "file": "docs/concept_papers/03_Modul_Matrix_M01_M13_DAG.md",
        "summary": "Mathematisch beweisbare Zyklusfreiheit (Tarjan DFS) und deterministische Initialisierungsreihenfolge aller 13 Mastermodule."
    },
    {
        "nr": 4,
        "title": "IA – Intelligent Automation Framework",
        "code": "IA, RPA, AGT",
        "category": "Automatisierung & KI",
        "modules": ['M01', 'M05'],
        "standards": ['EU AI Act (High-Risk Classification)', 'ISO/IEC 22989', 'IEEE 7000'],
        "file": "docs/concept_papers/04_IA_Intelligent_Automation_Framework.md",
        "summary": "Agentische Workflow-Steuerung mit automatisierter Tool-Synthese, semantischem Reasoning und deterministischen Guardrails."
    },
    {
        "nr": 5,
        "title": "XD – eXperience Design & Sovereign UI/UX",
        "code": "XD, UX, UI",
        "category": "Design & Frontend",
        "modules": ['M03'],
        "standards": ['EN 301 549', 'WCAG 2.2 Level AAA', 'ISO 9241-210'],
        "file": "docs/concept_papers/05_XD_eXperience_Design_Sovereign_UI_UX.md",
        "summary": "Design-Souveränität mit nativer GPU-Beschleunigung, Dark Mode (#121212) und Royal Gold (#FFD700) Akzenten bei 60+ FPS."
    },
    {
        "nr": 6,
        "title": "50-Repository Ökosystem (Zonen & Integration)",
        "code": "REPO, ZON, INT",
        "category": "Ökosystem & Integration",
        "modules": ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13'],
        "standards": ['SPDX 3.0', 'Open Source Initiative (OSI)', 'ISO/IEC 5230:2020'],
        "file": "docs/concept_papers/06_50_Repository_Oekosystem.md",
        "summary": "Strukturierte Katalogisierung und zonale Klassifizierung von 50 weltweiten Open-Source Referenzprojekten."
    },
    {
        "nr": 7,
        "title": "Entwicklungsumgebung & DevSecOps",
        "code": "DEV, CI/CD",
        "category": "DevSecOps & Toolchain",
        "modules": ['M02'],
        "standards": ['SLSA Level 4', 'NIST SSDF SP 800-218', 'BSI TR-03183'],
        "file": "docs/concept_papers/07_Entwicklungsumgebung_DevSecOps.md",
        "summary": "Hermetische, reproduzierbare Build-Pipelines mit Software Bill of Materials (SBOM) und lückenloser Supply-Chain Sicherheit."
    },
    {
        "nr": 8,
        "title": "Harness-Loop: Automatischer Umsetzungs- & Audit-Loop",
        "code": "LOOP, HNL",
        "category": "Automatisierung & KI",
        "modules": ['M02', 'M12'],
        "standards": ['ISO/IEC 20000-1', 'Continuous Assurance Framework', 'Act Pack Loop Spec'],
        "file": "docs/concept_papers/08_Harness_Loop_Automatischer_Zyklus.md",
        "summary": "Endloser, selbststeuernder 8-Stufen Zyklus (Plan -> Build -> Test -> Audit -> Certify -> Release -> Monitor -> Improve)."
    },
    {
        "nr": 9,
        "title": "Security Architecture & Zero-Trust Model",
        "code": "SEC, ZT, IAM",
        "category": "Sicherheit & Zero-Trust",
        "modules": ['M04', 'M07'],
        "standards": ['NIST SP 800-207', 'BSI IT-Grundschutz', 'Zero Trust Architecture'],
        "file": "docs/concept_papers/09_Security_Architecture_Zero_Trust.md",
        "summary": "Kein implizites Vertrauen: Jede Modul-Interaktion, jede API-Abfrage und jeder Speicherzugriff muss kryptografisch autorisiert sein."
    },
    {
        "nr": 10,
        "title": "Netzwerkisolation & Air-Gap (Sovereign Mode)",
        "code": "AIR, NET, G03",
        "category": "Sicherheit & Zero-Trust",
        "modules": ['M07', 'M10'],
        "standards": ['BSI IT-Grundschutz INF.1 / NET.3.2', 'Gate G03 Air-Gap Assurance'],
        "file": "docs/concept_papers/10_Netzwerkisolation_Air_Gap.md",
        "summary": "Garantierte physische oder logische Netzwerkisolation (Air-Gap) für den Sovereign Core mit strikter Egress-Blockade."
    },
    {
        "nr": 11,
        "title": "Datenhaltung, Verschlüsselung & Schlüsselmanagement",
        "code": "ENC, KMS, HSM",
        "category": "Kryptografie & Speicher",
        "modules": ['M04', 'M13'],
        "standards": ['BSI TR-02102-1', 'FIPS 140-3', 'NIST SP 800-57'],
        "file": "docs/concept_papers/11_Datenhaltung_Verschluesselung_KMS.md",
        "summary": "Kryptografischer Schutz ruhender und übertragener Daten mittels AES-256-GCM, PBKDF2-HMAC-SHA256 und HSM-Anbindung."
    },
    {
        "nr": 12,
        "title": "Blockchain-Architektur & On-/Off-Chain-Integration",
        "code": "BC, DLT, SC",
        "category": "Web3 & Blockchain",
        "modules": ['M07', 'M12'],
        "standards": ['ISO 23257 (Blockchain Reference Architecture)', 'EVM Standard', 'ERC-3643'],
        "file": "docs/concept_papers/12_Blockchain_Architektur_On_Off_Chain.md",
        "summary": "Souveräne Kopplung von deterministischer Off-Chain Geschäftslogik mit manipulationssicheren On-Chain DLT-Registern."
    },
    {
        "nr": 13,
        "title": "Crypto-Implementation (Signaturen, Wallets, ZKP)",
        "code": "CRYPTO, ED25519",
        "category": "Kryptografie & Speicher",
        "modules": ['M04', 'M12'],
        "standards": ['RFC 8032 (Ed25519)', 'FIPS 186-5', 'BSI TR-03111'],
        "file": "docs/concept_papers/13_Crypto_Implementation_Key_Management.md",
        "summary": "Moderne Elliptic Curve Kryptografie mit Ed25519 für hochperformante Signaturen und deterministische Schlüsselpaare."
    },
    {
        "nr": 14,
        "title": "Web3-Anwendungen & Dezentralisierung",
        "code": "WEB3, DID, VC",
        "category": "Web3 & Blockchain",
        "modules": ['M04', 'M09'],
        "standards": ['W3C Decentralized Identifiers (DID) v1.0', 'W3C Verifiable Credentials v2.0', 'eIDAS 2.0 EU Digital Identity Wallet'],
        "file": "docs/concept_papers/14_Web3_Anwendungen_Dezentralisierung.md",
        "summary": "Souveräne Identitätsverwaltung und dezentrale dApp-Konnektivität ohne Abhängigkeit von zentralen Identitätsprovidern."
    },
    {
        "nr": 15,
        "title": "Finance-Implementation (Payments, DeFi, Escrow)",
        "code": "FIN, PAY, DEFI",
        "category": "Finanzen & Zahlungsverkehr",
        "modules": ['M08'],
        "standards": ['EU Payment Services Directive 2 (PSD2)', 'ISO 20022 Financial Messaging', 'SEPA Rulebook'],
        "file": "docs/concept_papers/15_Finance_Implementation_Zahlungsinfrastruktur.md",
        "summary": "Auditsichere Finanztransaktions-Engine mit Read-Only Schutz, Betrugserkennung und optionalem DeFi-Settlement."
    },
    {
        "nr": 16,
        "title": "Rechenmodelle, Tokenisierung & Asset-Management",
        "code": "RWA, TOKEN, NFT",
        "category": "Finanzen & Zahlungsverkehr",
        "modules": ['M08', 'M12'],
        "standards": ['EU Markets in Crypto-Assets (MiCA)', 'ERC-3643 Permissioned Tokens', 'eWpG (Elektronisches Wertpapiergesetz)'],
        "file": "docs/concept_papers/16_Rechenmodelle_Tokenisierung_Asset_Management.md",
        "summary": "Rechtskonforme Tokenisierung realer Vermögenswerte (Real World Assets - RWA) und institutionelles Treasury Management."
    },
    {
        "nr": 17,
        "title": "Compliance, DSGVO & Gesetzeslage",
        "code": "DSGVO, DPA, PIA",
        "category": "Compliance & Recht",
        "modules": ['M04', 'M10'],
        "standards": ['EU Datenschutz-Grundverordnung (DSGVO)', 'EU AI Act 2024', 'NIS2 Richtlinie', 'DORA (Digital Operational Resilience Act)'],
        "file": "docs/concept_papers/17_Compliance_DSGVO_Gesetzeslage.md",
        "summary": "Vollständige, nachprüfbare Einhaltung europäischer Digital- und Datenschutzgesetze ab Werk (Privacy & Security by Design)."
    },
    {
        "nr": 18,
        "title": "Normen & Standards (ISO, IEC, EN, BSI, NIST)",
        "code": "ISO, IEC, EN",
        "category": "Compliance & Recht",
        "modules": ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13'],
        "standards": ['ISO/IEC 27001', 'ISO 9001', 'ISO/IEC 20000-1', 'ISO 22301', 'IEC 62443', 'EN 50600', 'BSI IT-Grundschutz'],
        "file": "docs/concept_papers/18_Normen_Standards_ISO_IEC_BSI.md",
        "summary": "Harmonisierte Erfüllung internationaler Sicherheits- und Qualitätsstandards über eine zentrale Kontrollmatrix."
    },
    {
        "nr": 19,
        "title": "Zertifizierungen & Abzeichen (Kriterien & Prozesse)",
        "code": "CERT, AUD, BADGE",
        "category": "Continuous Assurance",
        "modules": ['M12'],
        "standards": ['TISAX AL3', 'BSI-Zertifizierung', 'CIS Controls v8', 'EU Sovereign Ready Badge'],
        "file": "docs/concept_papers/19_Zertifizierungen_Abzeichen_Katalog.md",
        "summary": "Kryptografisch beglaubigte Abzeichen (Digital Badges) als fälschungssichere Nachweise für erreichte Prüf- und Sicherheitsstufen."
    },
    {
        "nr": 20,
        "title": "Automatisierte Audit- & Abnahme-Pipeline",
        "code": "AUDIT, G00-G12",
        "category": "Continuous Assurance",
        "modules": ['M12'],
        "standards": ['HCOS 13-Gate Assurance Specification', 'BSI CS 134', 'SLSA Level 4'],
        "file": "docs/concept_papers/20_Automatisierte_Audit_Abnahme_Pipeline.md",
        "summary": "Unabhängige, 13-stufige Fail-Closed Prüfpipeline (G00–G12) ohne Mock-Bypässe für höchste Softwareintegrität."
    },
    {
        "nr": 21,
        "title": "Daten-Governance & Data Lifetime Management",
        "code": "DGM, RET, ERASE",
        "category": "Kryptografie & Speicher",
        "modules": ['M06', 'M10'],
        "standards": ['DIN 66399 (Datenträgervernichtung)', 'ISO/IEC 2382', 'DSGVO Art. 5 (Speicherbegrenzung)'],
        "file": "docs/concept_papers/21_Daten_Governance_Data_Lifetime_Management.md",
        "summary": "Lebenszyklusverwaltung aller Datenobjekte von der Entstehung über Versionierung bis zur revisionssicheren Vernichtung."
    },
    {
        "nr": 22,
        "title": "Interoperabilität & Integrationen (APIs, Protokolle)",
        "code": "API, OIDC, FED",
        "category": "Ökosystem & Integration",
        "modules": ['M01', 'M09'],
        "standards": ['OpenAPI 3.1', 'gRPC / Protocol Buffers', 'JMAP (RFC 8620)', 'W3C WebSub'],
        "file": "docs/concept_papers/22_Interoperabilitaet_Integrationen_APIs.md",
        "summary": "Standardisierte Schnittstellen und Protokolle für reibungslose Interoperabilität bei strikter Kapselung."
    },
    {
        "nr": 23,
        "title": "Identität, Zugriff & Föderation (SSO, OIDC, SAML)",
        "code": "IAM, OIDC, FED",
        "category": "Sicherheit & Zero-Trust",
        "modules": ['M04'],
        "standards": ['OpenID Connect Core 1.0', 'SAML 2.0', 'FIDO2 / WebAuthn Passkeys', 'RFC 7519 (JWT)'],
        "file": "docs/concept_papers/23_Identitaet_Zugriff_Foederation.md",
        "summary": "Passwortlose, souveräne Identitätsverwaltung mit Passkey-Unterstützung und föderiertem Single Sign-On."
    },
    {
        "nr": 24,
        "title": "Monitoring, Observability & Incident Response",
        "code": "OBS, SIEM, IR",
        "category": "Betrieb & Wartung",
        "modules": ['M10', 'M13'],
        "standards": ['OpenTelemetry 1.0', 'ISO/IEC 27035 (Incident Management)', 'BSI CS 004'],
        "file": "docs/concept_papers/24_Monitoring_Observability_Incident_Response.md",
        "summary": "Vollständige Transparenz über Systemzustände durch strukturierte Logs, Metriken und automatisierte Notfall-Reaktionsketten."
    },
    {
        "nr": 25,
        "title": "Business Continuity, Backup & Disaster Recovery",
        "code": "BCP, DR, RTO/RPO",
        "category": "Betrieb & Wartung",
        "modules": ['M13'],
        "standards": ['ISO 22301:2019', 'BSI Standard 200-4', 'DIN EN ISO 27031'],
        "file": "docs/concept_papers/25_Business_Continuity_Backup_Disaster_Recovery.md",
        "summary": "Resiliente Geschäftskontinuität mit deterministischen, tar-basierten Offline-Backups und 100% Bit-Restorationsgarantie."
    },
    {
        "nr": 26,
        "title": "Legal, Lizenzierung & Open-Source-Governance",
        "code": "LIC, SPDX, OSS",
        "category": "Compliance & Recht",
        "modules": ['M01', 'M02'],
        "standards": ['SPDX 3.0', 'ISO/IEC 5230 (OpenChain)', 'Urheberrechtsgesetz (UrhG)'],
        "file": "docs/concept_papers/26_Legal_Lizenzierung_Open_Source_Governance.md",
        "summary": "Lückenlose rechtliche Absicherung, klare Trennung von Open-Source-Lizenzen und Schutz des geistigen Eigentums von Daniel Pohl."
    },
    {
        "nr": 27,
        "title": "Risikomanagement & Threat Modeling",
        "code": "RISK, TMT, TVM",
        "category": "Sicherheit & Zero-Trust",
        "modules": ['M07', 'M12'],
        "standards": ['ISO 31000', 'STRIDE Threat Model', 'LINDDUN Privacy Threat Model', 'CVSS v3.1'],
        "file": "docs/concept_papers/27_Risikomanagement_Threat_Modeling.md",
        "summary": "Systematische Identifikation, Bewertung und Minderung von Cyber- und Datenschutzrisiken vor der Produktivsetzung."
    },
    {
        "nr": 28,
        "title": "Performance, Skalierung & Ressourcen-Management",
        "code": "PERF, SCALE, K8S",
        "category": "Betrieb & Wartung",
        "modules": ['M01', 'M02', 'M03'],
        "standards": ['ISO/IEC 25010 (System- und Softwarequalität)', 'IEEE 1044'],
        "file": "docs/concept_papers/28_Performance_Skalierung_Ressourcen_Management.md",
        "summary": "Maximale Ressourcen-Effizienz mit Sub-Millisekunden-Reaktionszeiten und linearer Skalierbarkeit von Edge bis Cloud."
    },
    {
        "nr": 29,
        "title": "KI/LLM-Integration (BOBA, Stroq, RAG, Guardrails)",
        "code": "LLM, RAG, SAFE",
        "category": "Automatisierung & KI",
        "modules": ['M12', 'M13'],
        "standards": ['EU AI Act Art. 50 (Transparenz)', 'OWASP Top 10 for LLM Applications', 'NIST AI RMF'],
        "file": "docs/concept_papers/29_KI_LLM_Integration_BOBA_Stroq_Guardrails.md",
        "summary": "Sichere LLM-Nutzung durch physikalische Fehlerketten-Benchmarks (BOBA) und heuristische Deobfuskations-Scanner (Stroq)."
    },
    {
        "nr": 30,
        "title": "Nachhaltigkeit & Green IT (ESG, CSRD)",
        "code": "ESG, GREEN, CO2",
        "category": "Compliance & Recht",
        "modules": ['M10'],
        "standards": ['EU Corporate Sustainability Reporting Directive (CSRD)', 'European Sustainability Reporting Standards (ESRS)', 'GHG Protocol'],
        "file": "docs/concept_papers/30_Nachhaltigkeit_Green_IT_ESG_CSRD.md",
        "summary": "Ressourcenschonende Software-Architektur (Green Coding) mit messbarem CO2-Fußabdruck und ESG-Reporting."
    },
    {
        "nr": 31,
        "title": "Betrieb, Wartung & Lifecycle-Management",
        "code": "OPS, LCM, SRE",
        "category": "Betrieb & Wartung",
        "modules": ['M01', 'M02', 'M13'],
        "standards": ['ISO/IEC 20000-1', 'Site Reliability Engineering (SRE)', 'ITIL v4'],
        "file": "docs/concept_papers/31_Betrieb_Wartung_Lifecycle_Management.md",
        "summary": "Deterministisches Lifecycle-Management für unterbrechungsfreie Updates, planbare Wartungsfenster und LTS-Stabilität."
    },
    {
        "nr": 32,
        "title": "Roadmap, Meilensteine & Release-Strategie",
        "code": "ROAD, MILE, REL",
        "category": "Strategie & Vision",
        "modules": ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13'],
        "standards": ['Semantic Versioning 2.0.0', 'GitFlow / Trunk-Based Development'],
        "file": "docs/concept_papers/32_Roadmap_Meilensteine_Release_Strategie.md",
        "summary": "Strukturierter strategischer Entwicklungsplan von Version 1.0 über 2.0 bis zur finalen Vision 2030."
    },
    {
        "nr": 33,
        "title": "Abnahme, Zertifizierung & Continuous Compliance",
        "code": "CC, ISO, LOOP",
        "category": "Continuous Assurance",
        "modules": ['M12'],
        "standards": ['Continuous Compliance Framework', 'Act Pack Loop', 'ISO/IEC 17065'],
        "file": "docs/concept_papers/33_Abnahme_Zertifizierung_Continuous_Compliance.md",
        "summary": "Dauerhafte, automatisierte Re-Zertifizierung und Konformitätsbeglaubigung in jedem einzelnen Entwicklungszyklus."
    },
    {
        "nr": 34,
        "title": "Anhang: Abkürzungen, Keywords & Glossar (33+)",
        "code": "A-Z, KW, DEF",
        "category": "Glossar & Referenz",
        "modules": ['M01', 'M02', 'M03', 'M04', 'M05', 'M06', 'M07', 'M08', 'M09', 'M10', 'M11', 'M12', 'M13'],
        "standards": ['ISO/IEC Directives Part 2', 'W3C Terminology Standards'],
        "file": "docs/concept_papers/34_Anhang_Abkuerzungen_Keywords_Glossar.md",
        "summary": "Umfassendes Standardnachschlagewerk für über 33 Kernbegriffe, Abkürzungen und rechtliche Definitionen."
    },
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
    """Provides querying, inspection and full markdown content retrieval for the 34 Concept Papers."""

    def __init__(self, project_root: Optional[Path] = None):
        self.root = project_root or Path(__file__).parent.parent
        self.papers = CONCEPT_PAPERS
        self.standards = STANDARDS_CATALOG

    def list_papers(self, category_filter: Optional[str] = None) -> List[Dict[str, Any]]:
        if not category_filter or category_filter.lower() in ("all", "alle"):
            return list(self.papers)
        cat_lower = category_filter.lower()
        return [p for p in self.papers if cat_lower in p["category"].lower()]

    def get_paper(self, nr: int) -> Optional[Dict[str, Any]]:
        for p in self.papers:
            if p["nr"] == nr:
                return dict(p)
        return None

    def get_paper_content(self, nr: int) -> Optional[Dict[str, Any]]:
        """Retrieves paper metadata plus the full markdown text from disk."""
        paper = self.get_paper(nr)
        if not paper:
            return None

        file_rel = paper.get("file")
        if file_rel:
            full_path = self.root / file_rel
            if full_path.exists():
                try:
                    paper["content"] = full_path.read_text(encoding="utf-8")
                    paper["file_found"] = True
                    return paper
                except Exception as e:
                    paper["content_error"] = str(e)

        # Fallback summary content
        paper["content"] = f"# {paper['title']}\n\n{paper['summary']}"
        paper["file_found"] = False
        return paper

    def search_papers(self, query: str) -> List[Dict[str, Any]]:
        q = query.lower()
        results = []
        for p in self.papers:
            text = f"{p['nr']} {p['title']} {p['code']} {p['category']} {' '.join(p['standards'])} {p['summary']}".lower()
            if q in text:
                results.append(dict(p))
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
            "sovereign_governance": "Daniel Pohl, Royal Kaiser Charter RegSys",
            "provenance": {
                "author": "Daniel Pohl",
                "pic": "867679357",
                "vat": "DE31353063511",
                "duns": ["315676980", "317066336"],
                "lei": "894500GBJSIW8L6ET310",
                "ungm": "1172700"
            }
        }

    def list_baende(self) -> List[Dict[str, Any]]:
        """Returns the 4 Monumental Volumes (144 A4 Pages, 136 Chapters)."""
        baende_meta = [
            {"band": "A", "title": "Band A: Gesamtarchitektur, IA, XD & Modulare Plattform", "chapters": 34, "file": "docs/baende/Band_A_144_Seiten.md"},
            {"band": "B", "title": "Band B: Entwicklungssprache, 34 Glossar-Fachkapitel & API-Strategie", "chapters": 34, "file": "docs/baende/Band_B_144_Seiten.md"},
            {"band": "C", "title": "Band C: Blockchain, Crypto, Web3, Security & Finance (272 Keywords)", "chapters": 34, "file": "docs/baende/Band_C_144_Seiten.md"},
            {"band": "D", "title": "Band D: Normen, Zertifikate, Abzeichen & Automatische Abnahme", "chapters": 34, "file": "docs/baende/Band_D_144_Seiten.md"}
        ]
        res = []
        for b in baende_meta:
            path = self.root / b["file"]
            b_info = dict(b)
            b_info["exists"] = path.exists()
            b_info["bytes"] = path.stat().st_size if path.exists() else 0
            res.append(b_info)
        return res

    def get_band_content(self, band_letter: str) -> Optional[Dict[str, Any]]:
        band_letter = band_letter.upper()
        baende = {b["band"]: b for b in self.list_baende()}
        if band_letter not in baende:
            return None
        target = baende[band_letter]
        path = self.root / target["file"]
        if path.exists():
            target["content"] = path.read_text(encoding="utf-8")
        else:
            target["content"] = f"# {target['title']}\nDatei nicht gefunden."
        return target

    def get_136_themen(self) -> Dict[str, Any]:
        themen_file = self.root / "docs" / "catalogs" / "THEMEN_136_KAPITEL.json"
        if themen_file.exists():
            import json
            try:
                return json.loads(themen_file.read_text(encoding="utf-8"))
            except Exception:
                pass
        return {}

    def list_specialized_papers(self) -> List[Dict[str, Any]]:
        spec_dir = self.root / "docs" / "concept_papers" / "specialized"
        res = []
        if spec_dir.exists():
            for f in sorted(spec_dir.glob("*.md")):
                res.append({
                    "id": f.stem,
                    "title": f.stem.replace("_", " "),
                    "file": f"docs/concept_papers/specialized/{f.name}",
                    "size": f.stat().st_size
                })
        return res
