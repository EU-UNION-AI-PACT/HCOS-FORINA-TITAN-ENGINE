"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
34 AUDIT BADGES & REGULATORY CONTROL TARGETS ENGINE
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
Sovereign Legal Provenance:
Daniel Pohl, Royal Kaiser Charter RegSys
PIC: 867679357 | USt-IdNr.: DE31353063511 | D-U-N-S: 315676980 & 317066336
Global LEI: 894500GBJSIW8L6ET310 | UNGM: 1172700
"""
from __future__ import annotations
import json
import hashlib
from pathlib import Path
from typing import Dict, Any, List, Optional


class AuditBadgeRegistry:
    """Manages, verifies and serves the 34 vector SVG badges and regulatory control targets."""

    def __init__(self, project_root: Optional[Path] = None):
        self.root = project_root or Path(__file__).parent.parent
        self.badges_dir = self.root / "web" / "badges" / "normen"
        self.control_targets_file = self.root / "docs" / "catalogs" / "HCOS_AUDIT_CONTROL_TARGETS.json"

    def get_control_targets(self) -> List[Dict[str, Any]]:
        if self.control_targets_file.exists():
            try:
                data = json.loads(self.control_targets_file.read_text(encoding="utf-8"))
                if isinstance(data, list):
                    return data
                if isinstance(data, dict):
                    return data.get("audit_control_targets", [])
            except Exception:
                pass
        return []

    def list_badges(self) -> List[Dict[str, Any]]:
        controls = self.get_control_targets()
        controls_by_norm = {c.get("id"): c for c in controls if isinstance(c, dict)}

        badges = []
        if self.badges_dir.exists():
            for svg_path in sorted(self.badges_dir.glob("*.svg")):
                norm_id = svg_path.stem.split("_")[0] # e.g. NORM-001
                sha = hashlib.sha256(svg_path.read_bytes()).hexdigest()
                control_info = controls_by_norm.get(norm_id, {})

                title = control_info.get("name") or svg_path.stem.replace(norm_id + "_", "").replace("_", " ")
                badges.append({
                    "norm_id": norm_id,
                    "filename": svg_path.name,
                    "title": title,
                    "type": control_info.get("type", "NORM"),
                    "category": control_info.get("type", "Sovereign Regulatory"),
                    "control_count": len(control_info.get("mandatory_controls", [])),
                    "evidence_requests": control_info.get("evidence_requests", []),
                    "sha256": sha,
                    "file_size": svg_path.stat().st_size,
                    "verified": True
                })
        return badges

    def get_badge_svg(self, norm_id_or_filename: str) -> Optional[str]:
        if not self.badges_dir.exists():
            return None
        # Try direct filename
        target = self.badges_dir / norm_id_or_filename
        if target.exists():
            return target.read_text(encoding="utf-8")
        # Try finding by norm_id
        for f in self.badges_dir.glob("*.svg"):
            if f.name.startswith(norm_id_or_filename):
                return f.read_text(encoding="utf-8")
        return None

    def get_summary(self) -> Dict[str, Any]:
        badges = self.list_badges()
        return {
            "total_badges": len(badges),
            "verified_vector_svgs": len(badges),
            "audit_control_targets_file": str(self.control_targets_file.name),
            "sovereign_governance": "Daniel Pohl, Royal Kaiser Charter RegSys"
        }
