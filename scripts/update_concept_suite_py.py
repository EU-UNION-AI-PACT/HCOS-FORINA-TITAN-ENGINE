#!/usr/bin/env python3
import re
from pathlib import Path

ROOT = Path("/home/shinehealthcare/Schreibtisch/Creation Sites - 4 - Projects/HCOS-FORINA-TITAN-ENGINE")
CS_PATH = ROOT / "forina_engine" / "concept_suite.py"

PAPERS_MAPPING = {
    1: "01_Executive_Summary_Vision_2030.md",
    2: "02_Gesamtarchitektur_HCOS_FORINA_TITAN.md",
    3: "03_Modul_Matrix_M01_M13_DAG.md",
    4: "04_IA_Intelligent_Automation_Framework.md",
    5: "05_XD_eXperience_Design_Sovereign_UI_UX.md",
    6: "06_50_Repository_Oekosystem.md",
    7: "07_Entwicklungsumgebung_DevSecOps.md",
    8: "08_Harness_Loop_Automatischer_Zyklus.md",
    9: "09_Security_Architecture_Zero_Trust.md",
    10: "10_Netzwerkisolation_Air_Gap.md",
    11: "11_Datenhaltung_Verschluesselung_KMS.md",
    12: "12_Blockchain_Architektur_On_Off_Chain.md",
    13: "13_Crypto_Implementation_Key_Management.md",
    14: "14_Web3_Anwendungen_Dezentralisierung.md",
    15: "15_Finance_Implementation_Zahlungsinfrastruktur.md",
    16: "16_Rechenmodelle_Tokenisierung_Asset_Management.md",
    17: "17_Compliance_DSGVO_Gesetzeslage.md",
    18: "18_Normen_Standards_ISO_IEC_BSI.md",
    19: "19_Zertifizierungen_Abzeichen_Katalog.md",
    20: "20_Automatisierte_Audit_Abnahme_Pipeline.md",
    21: "21_Daten_Governance_Data_Lifetime_Management.md",
    22: "22_Interoperabilitaet_Integrationen_APIs.md",
    23: "23_Identitaet_Zugriff_Foederation.md",
    24: "24_Monitoring_Observability_Incident_Response.md",
    25: "25_Business_Continuity_Backup_Disaster_Recovery.md",
    26: "26_Legal_Lizenzierung_Open_Source_Governance.md",
    27: "27_Risikomanagement_Threat_Modeling.md",
    28: "28_Performance_Skalierung_Ressourcen_Management.md",
    29: "29_KI_LLM_Integration_BOBA_Stroq_Guardrails.md",
    30: "30_Nachhaltigkeit_Green_IT_ESG_CSRD.md",
    31: "31_Betrieb_Wartung_Lifecycle_Management.md",
    32: "32_Roadmap_Meilensteine_Release_Strategie.md",
    33: "33_Abnahme_Zertifizierung_Continuous_Compliance.md",
    34: "34_Anhang_Abkuerzungen_Keywords_Glossar.md"
}

from scripts.generate_34_concept_papers import PAPERS_META

new_content = '''"""
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
'''

for p in PAPERS_META:
    fn = p["filename"]
    rel_path = f"docs/concept_papers/{fn}"
    new_content += f"""    {{
        "nr": {p["nr"]},
        "title": "{p["title"]}",
        "code": "{p["code"]}",
        "category": "{p["category"]}",
        "modules": {p["modules"]},
        "standards": {p["standards"]},
        "file": "{rel_path}",
        "summary": "{p["mission"]}"
    }},
"""

new_content += ''']


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
        paper["content"] = f"# {paper['title']}\\n\\n{paper['summary']}"
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
'''

CS_PATH.write_text(new_content, encoding="utf-8")
print("[SUCCESS] Updated forina_engine/concept_suite.py successfully!")
