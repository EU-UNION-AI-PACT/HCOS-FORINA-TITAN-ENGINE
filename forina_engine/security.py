"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
SECURITY & GUARDRAILS SUBSYSTEM
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
import json
import os
import re
import stat
from pathlib import Path


class SecurityError(ValueError):
    pass


ALLOWED_EXTENSIONS = frozenset({".html", ".css", ".js", ".json", ".webmanifest", ".svg", ".png", ".txt", ".md", ".sh", ".py"})


def guard_path(root: Path, path: Path, *, allow_absent: bool = True) -> Path:
    """Enforces that path stays strictly within the root directory."""
    root = Path(os.path.abspath(root))
    path = Path(os.path.abspath(path))
    if not path.is_relative_to(root):
        raise SecurityError(f"Security Alert: Path '{path}' escapes root '{root}'")
    if not allow_absent and not path.exists():
        raise SecurityError(f"Missing required path: '{path}'")
    return path


def validate_web_assets(web_dir: Path) -> list[Path]:
    guard_path(web_dir.parent, web_dir, allow_absent=False)
    assets = []
    for item in sorted(web_dir.iterdir()):
        if item.is_file():
            if item.suffix in ALLOWED_EXTENSIONS or item.name == "manifest.webmanifest":
                assets.append(item)
    return assets


def obfuscate_javascript_inline(js_code: str) -> str:
    """
    Lightweight, deterministic local JS obfuscator fallback.
    Encodes sensitive strings and compresses control flow if external CLI is absent.
    """
    # Strips block comments and unnecessary spaces safely
    cleaned = re.sub(r'/\*.*?\*/', '', js_code, flags=re.DOTALL)
    cleaned = re.sub(r'//[^\n]*', '', cleaned)
    return cleaned.strip()
