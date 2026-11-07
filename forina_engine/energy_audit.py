# -*- coding: utf-8 -*-
"""
HCOS FORINA TITAN ENGINE — SCIENTIFIC ENERGY AUDIT & PONTES DLT SETTLEMENT ENGINE
Sovereign Provenance: Daniel Pohl · Royal Kaiser Charter RegSys
PIC: 867679357 & 873042778 · Global LEI: 894500GBJSIW8L6ET310 · Swiss AHV: 756.6199.0539.28
Lizenz: European Union Public Licence (EUPL-1.2)

Verbindet:
1. Top 100 Wissenschaftlicher Energie- & Extremtechnologie-Audit
2. EZB Pontes & DLT Wholesale Settlement Recherchereferenzen (25 Systeme)
"""

import csv
import json
from pathlib import Path
from typing import Any, Dict, List, Optional


class ScientificEnergyAuditEngine:
    """Verwaltet den wissenschaftlichen Top-100-Energie- und Extremtechnologiekatalog."""

    def __init__(self, project_root: Optional[Path] = None):
        self.root = Path(project_root) if project_root else Path(__file__).resolve().parent.parent
        self.csv_path = self.root / "docs" / "catalogs" / "TOP100_ENERGIE_TECHNOLOGIE_AUDIT.csv"

    def list_systems(self, group: Optional[str] = None, nachweisgrad: Optional[str] = None) -> List[Dict[str, str]]:
        """Gibt die Liste der 100 auditierten Technologiesysteme zurück."""
        if not self.csv_path.exists():
            return []
        res = []
        with open(self.csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if group and group.lower() not in row.get("Gruppe", "").lower():
                    continue
                if nachweisgrad and nachweisgrad.upper() not in row.get("Nachweisgrad", "").upper():
                    continue
                res.append(dict(row))
        return res

    def search_systems(self, query: str) -> List[Dict[str, str]]:
        """Durchsucht Systeme nach Name, Rolle, Besonderheiten oder kritischen Anmerkungen."""
        q = query.lower().strip()
        if not q:
            return self.list_systems()
        all_sys = self.list_systems()
        return [
            s for s in all_sys
            if q in s.get("System", "").lower()
            or q in s.get("Gruppe", "").lower()
            or q in s.get("Rolle", "").lower()
            or q in s.get("Besonderheit", "").lower()
            or q in s.get("kritische Anmerkung", "").lower()
        ]

    def get_system_by_nr(self, nr: int) -> Optional[Dict[str, str]]:
        """Gibt ein Einzelsystem anhand der Auswahl-Nummer zurück."""
        for s in self.list_systems():
            try:
                if int(s.get("Auswahl-Nr", -1)) == nr:
                    return s
            except ValueError:
                continue
        return None

    def get_summary(self) -> Dict[str, Any]:
        """Gibt aggregierte Kennzahlen des Energie-Audits zurück."""
        systems = self.list_systems()
        groups = {}
        grades = {}
        for s in systems:
            g = s.get("Gruppe", "Unbekannt")
            groups[g] = groups.get(g, 0) + 1
            ng = s.get("Nachweisgrad", "Unbekannt")
            key = ng[:1].upper() if ng else "U"
            grades[key] = grades.get(key, 0) + 1

        return {
            "title": "Top 100 Wissenschaftlicher Energie- & Extremtechnologie-Audit",
            "version": "2.16.0",
            "governance": "Daniel Pohl · Royal Kaiser Charter RegSys",
            "total_systems": len(systems),
            "groups_count": len(groups),
            "groups_breakdown": groups,
            "nachweisgrade": grades,
            "catalog_path": "docs/catalogs/TOP100_ENERGIE_TECHNOLOGIE_AUDIT.csv"
        }


class PontesDltSettlementEngine:
    """Verwaltet die EZB Pontes & Wholesale DLT Settlement Recherchereferenzen."""

    def __init__(self, project_root: Optional[Path] = None):
        self.root = Path(project_root) if project_root else Path(__file__).resolve().parent.parent
        self.csv_path = self.root / "docs" / "catalogs" / "EZB_PONTES_DLT_RECHERCHEMATRIX.csv"

    def list_candidates(self, category: Optional[str] = None) -> List[Dict[str, str]]:
        """Gibt die Liste der 25 untersuchten DLT- und Wholesale-Settlement-Kandidaten zurück."""
        if not self.csv_path.exists():
            return []
        res = []
        with open(self.csv_path, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                if category and category.lower() not in row.get("Kategorie", "").lower():
                    continue
                res.append(dict(row))
        return res

    def get_candidate(self, kandidat_id: str) -> Optional[Dict[str, str]]:
        """Gibt einen bestimmten Kandidaten anhand der ID zurück."""
        kid = kandidat_id.strip().upper()
        for c in self.list_candidates():
            if c.get("Kandidat_ID", "").upper() == kid:
                return c
        return None

    def get_summary(self) -> Dict[str, Any]:
        """Gibt eine aggregierte Zusammenfassung der Pontes- und DLT-Recherchedaten zurück."""
        cands = self.list_candidates()
        cats = {}
        for c in cands:
            k = c.get("Kategorie", "Sonstige")
            cats[k] = cats.get(k, 0) + 1

        return {
            "title": "EZB Pontes & Wholesale DLT Settlement Rechercheregister",
            "version": "2.16.0",
            "governance": "Daniel Pohl · Royal Kaiser Charter RegSys",
            "total_candidates": len(cands),
            "categories": cats,
            "catalog_path": "docs/catalogs/EZB_PONTES_DLT_RECHERCHEMATRIX.csv"
        }
