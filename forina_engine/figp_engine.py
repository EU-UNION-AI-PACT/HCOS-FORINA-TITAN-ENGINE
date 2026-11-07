# -*- coding: utf-8 -*-
"""
HCOS FORINA TITAN ENGINE — FIGP & UFCIE GOVERNANCE AND 141 OBSERVABILITY TOOLS ENGINE
Sovereign Provenance: Daniel Pohl · Royal Kaiser Charter RegSys
PIC: 867679357 & 873042778 · Global LEI: 894500GBJSIW8L6ET310 · Swiss AHV: 756.6199.0539.28
Lizenz: European Union Public Licence (EUPL-1.2)

Verbindet:
1. FIGP & UFCIE Framework Intelligence & Governance Platform (BSI, ISO, DORA, MiCA, DSGVO)
2. 141 Validierte Observability-, Monitoring- & AI-Agent-Tools über 14 Fachdomänen
"""

import csv
import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class FigpGovernanceEngine:
    """Verwaltet kanonische Framework-Familien, SQLite/PostgreSQL DDL und API-Spezifikationen."""

    def __init__(self, project_root: Optional[Path] = None):
        self.root = Path(project_root) if project_root else Path(__file__).resolve().parent.parent
        self.entities_csv = self.root / "docs" / "catalogs" / "FIGP_GOVERNANCE_ENTITIES.csv"
        self.schema_sql = self.root / "docs" / "schemas" / "FIGP_Reference_Schema.sql"
        self.api_yaml = self.root / "docs" / "schemas" / "FIGP_API_v1.yaml"
        self.arch_doc = self.root / "docs" / "concept_papers" / "specialized" / "Architecture_10_FIGP_UFCIE_Framework_Intelligence_Platform.md"

    def list_framework_families(self) -> List[Dict[str, str]]:
        """Liest die registrierten Framework-Familien aus dem Katalog."""
        if not self.entities_csv.exists():
            return []
        res = []
        with open(self.entities_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                res.append(dict(row))
        return res

    def get_schema_ddl(self) -> str:
        """Gibt das SQLite/PostgreSQL Referenzmodell als SQL-DDL zurück."""
        if self.schema_sql.exists():
            return self.schema_sql.read_text(encoding="utf-8")
        return ""

    def get_api_spec(self) -> str:
        """Gibt die OpenAPI v3.0 REST-Spezifikation zurück."""
        if self.api_yaml.exists():
            return self.api_yaml.read_text(encoding="utf-8")
        return ""

    def get_summary(self) -> Dict[str, Any]:
        """Liefert Kennzahlen zur FIGP-Governance-Architektur."""
        fams = self.list_framework_families()
        return {
            "title": "FIGP & UFCIE Framework Intelligence & Governance Platform",
            "version": "2.18.0",
            "governance": "Daniel Pohl · Royal Kaiser Charter RegSys",
            "total_framework_families": len(fams),
            "schema_available": self.schema_sql.exists(),
            "schema_size_bytes": self.schema_sql.stat().st_size if self.schema_sql.exists() else 0,
            "api_spec_available": self.api_yaml.exists(),
            "api_spec_size_bytes": self.api_yaml.stat().st_size if self.api_yaml.exists() else 0,
            "arch_paper_available": self.arch_doc.exists(),
            "fail_closed_launcher_enforced": True
        }


class ObservabilityToolsCatalogEngine:
    """Verwaltet den Katalog von 141 Monitoring-, Observability- und AI-Agent-Tools."""

    def __init__(self, project_root: Optional[Path] = None):
        self.root = Path(project_root) if project_root else Path(__file__).resolve().parent.parent
        self.tools_csv = self.root / "docs" / "catalogs" / "OBSERVABILITY_141_TOOLS_CATALOG.csv"

    def list_tools(self, category: Optional[str] = None) -> List[Dict[str, str]]:
        """Gibt alle 141 Tools zurück, optional gefiltert nach Kategorie."""
        if not self.tools_csv.exists():
            return []
        res = []
        with open(self.tools_csv, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if category and category.lower() not in row.get("Kategorie", "").lower():
                    continue
                res.append(dict(row))
        return res

    def search_tools(self, query: str) -> List[Dict[str, str]]:
        """Sucht Tools anhand von Name, Kategorie, Beschreibung oder Repository."""
        q = query.lower().strip()
        if not q:
            return self.list_tools()
        tools = self.list_tools()
        return [
            t for t in tools
            if q in t.get("Name", "").lower()
            or q in t.get("Kategorie", "").lower()
            or q in t.get("Beschreibung", "").lower()
            or q in t.get("Repo", "").lower()
        ]

    def get_summary(self) -> Dict[str, Any]:
        """Liefert Kennzahlen zum 141-Tools-Katalog."""
        tools = self.list_tools()
        categories = {}
        oss_count = 0
        for t in tools:
            cat = t.get("Kategorie", "Sonstige")
            categories[cat] = categories.get(cat, 0) + 1
            if "OSS" in t.get("Status", "").upper() or "MIT" in t.get("Lizenz", "").upper() or "APACHE" in t.get("Lizenz", "").upper():
                oss_count += 1

        return {
            "title": "Observability, Monitoring & AI-Agent Tools Stack",
            "version": "2.18.0",
            "governance": "Daniel Pohl · Royal Kaiser Charter RegSys",
            "total_tools": len(tools),
            "categories_count": len(categories),
            "categories_distribution": categories,
            "open_source_count": oss_count,
            "catalog_path": "docs/catalogs/OBSERVABILITY_141_TOOLS_CATALOG.csv"
        }
