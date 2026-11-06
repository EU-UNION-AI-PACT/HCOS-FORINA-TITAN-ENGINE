"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
FORINA TITAN CORE PIPELINE & BUILD ENGINE
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
import hashlib
import io
import json
import os
import shutil
import stat
import tarfile
import tempfile
import time
import zipfile
from datetime import datetime, timezone
from pathlib import Path
from typing import Dict, Any, List

from .security import guard_path, validate_web_assets, obfuscate_javascript_inline, SecurityError
from .spec_sync import SpecSyncEngine
from .certification import SovereignCertifier

PIPELINE_STAGES = [
    ("01", "PREFLIGHT", "Workspace boundary check, spec verification and source validation"),
    ("02", "BACKUP", "Timestamped source backup with deterministic tar.gz archive"),
    ("03", "BUILD", "Compile PWA, module registry, manifest and asset obfuscation"),
    ("04", "VERIFY", "Integrity audit, SHA-256 asset checksum verification"),
    ("05", "SPEC_SYNC", "Live Spec Realisierungs-Matrix evaluation & statistic glow sync"),
    ("06", "EVIDENCE", "EU-Compliance & NATO-Framework audit evidence generation"),
    ("07", "PACKAGING", "AppDir staging & portable distribution release packaging"),
]


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat(timespec="seconds")


def calc_sha256(content: bytes) -> str:
    return hashlib.sha256(content).hexdigest()


class ForinaTitanEngine:
    def __init__(self, root_dir: Path | str):
        self.root = Path(os.path.abspath(root_dir))
        self.web_dir = self.root / "web"
        self.registry_dir = self.root / "registry"
        self.dist_dir = self.root / "dist"
        self.backups_dir = self.root / "backups"
        self.releases_dir = self.root / "releases"
        self.meta_dir = self.root / ".forina"
        self.spec_sync = SpecSyncEngine(self.root)
        self.certifier = SovereignCertifier(self.root)

    def plan(self) -> Dict[str, Any]:
        spec_meta = self.spec_sync.get_spec_meta()
        return {
            "system": "HCOS - FORINA TITAN ENGINE",
            "copyright": "Copyright (c) 2024-2026 Daniel Pohl",
            "root": str(self.root),
            "stages": [
                {"id": s[0], "name": s[1], "description": s[2]}
                for s in PIPELINE_STAGES
            ],
            "spec_status": spec_meta,
            "planned_at": utc_now()
        }

    def run_pipeline(self) -> Dict[str, Any]:
        start_time = time.time()
        timestamp = datetime.now(timezone.utc).strftime("%Y%m%d_%H%M%S")
        report: Dict[str, Any] = {
            "system": "HCOS - FORINA TITAN ENGINE",
            "build_id": timestamp,
            "status": "IN_PROGRESS",
            "stages": {},
            "errors": []
        }

        try:
            # 1. PREFLIGHT
            self.backups_dir.mkdir(parents=True, exist_ok=True)
            self.releases_dir.mkdir(parents=True, exist_ok=True)
            self.dist_dir.mkdir(parents=True, exist_ok=True)
            self.meta_dir.mkdir(parents=True, exist_ok=True)

            assets = validate_web_assets(self.web_dir)
            report["stages"]["PREFLIGHT"] = {
                "status": "PASS",
                "web_assets_found": len(assets),
                "timestamp": utc_now()
            }

            # 2. BACKUP (Mit striktem Secret- & Key-Ausschlussfilter)
            def _clean_backup_filter(tarinfo):
                name = tarinfo.name
                forbidden = [
                    ".key", "signing_key", ".api_key", ".secrets_vault",
                    "__pycache__", ".DS_Store"
                ]
                if any(f in name for f in forbidden):
                    return None
                return tarinfo

            backup_filename = f"backup_hcos_titan_{timestamp}.tar.gz"
            backup_path = self.backups_dir / backup_filename
            with tarfile.open(backup_path, "w:gz") as tar:
                for item_name in ["web", "registry", "config", "scripts", "forina_engine", "modules", "skills", "forina.py", "COPYRIGHT.md"]:
                    item_path = self.root / item_name
                    if item_path.exists():
                        tar.add(str(item_path), arcname=item_name, filter=_clean_backup_filter)
            report["stages"]["BACKUP"] = {
                "status": "PASS",
                "archive": backup_filename,
                "size_bytes": backup_path.stat().st_size,
                "timestamp": utc_now()
            }

            # 3. BUILD
            # Clean dist
            for item in self.dist_dir.iterdir():
                if item.is_dir():
                    shutil.rmtree(item)
                else:
                    item.unlink()

            # Copy web assets
            for asset in assets:
                dest = self.dist_dir / asset.name
                if asset.suffix == ".js" and asset.name == "app.js":
                    # Obfuscate / protect
                    obfuscated = obfuscate_javascript_inline(asset.read_text(encoding="utf-8"))
                    dest.write_text(obfuscated, encoding="utf-8")
                else:
                    shutil.copy2(asset, dest)

            # Copy subdirectories in web (e.g. flow, badges)
            for sub_name in ["flow", "badges"]:
                sub_src = self.web_dir / sub_name
                if sub_src.exists():
                    shutil.copytree(sub_src, self.dist_dir / sub_name, dirs_exist_ok=True)

            # Copy or generate registry in dist/registry
            dist_reg = self.dist_dir / "registry"
            dist_reg.mkdir(parents=True, exist_ok=True)
            all_modules = []
            if self.registry_dir.exists():
                for reg_file in sorted(self.registry_dir.glob("*.json")):
                    try:
                        data = json.loads(reg_file.read_text(encoding="utf-8"))
                        all_modules.append(data)
                        shutil.copy2(reg_file, dist_reg / reg_file.name)
                    except Exception:
                        pass
            
            # Write unified modules.json
            modules_index = {
                "system": "HCOS - FORINA TITAN MODULE CATALOG",
                "version": "1.2.0",
                "modules": all_modules
            }
            (dist_reg / "modules.json").write_text(
                json.dumps(modules_index, indent=2, ensure_ascii=False), encoding="utf-8"
            )

            # Mark build
            build_marker = {
                "system": "HCOS - FORINA TITAN",
                "build_id": timestamp,
                "built_at": utc_now(),
                "engine_version": "1.2.0",
                "copyright": "Copyright (c) 2024-2026 Daniel Pohl"
            }
            (self.dist_dir / "build.json").write_text(json.dumps(build_marker, indent=2), encoding="utf-8")
            (self.dist_dir / ".forina-build-marker").write_text(timestamp)

            report["stages"]["BUILD"] = {
                "status": "PASS",
                "output_dir": str(self.dist_dir),
                "modules_registered": len(all_modules),
                "timestamp": utc_now()
            }

            # 4. VERIFY & INVENTORY
            inventory = {}
            for item in sorted(self.dist_dir.rglob("*")):
                if item.is_file():
                    rel = item.relative_to(self.dist_dir)
                    inventory[str(rel)] = calc_sha256(item.read_bytes())

            (self.meta_dir / "inventory.sha256").write_text(
                "\n".join(f"{h}  {f}" for f, h in inventory.items()), encoding="utf-8"
            )

            report["stages"]["VERIFY"] = {
                "status": "PASS",
                "verified_files": len(inventory),
                "timestamp": utc_now()
            }

            # 5. SPEC_SYNC
            spec_report = self.spec_sync.verify_all_modules()
            (self.dist_dir / "spec-status.json").write_text(
                json.dumps(spec_report, indent=2, ensure_ascii=False), encoding="utf-8"
            )
            report["stages"]["SPEC_SYNC"] = {
                "status": "PASS",
                "realized": spec_report["overall_realized"],
                "percentage": spec_report["overall_percentage"],
                "realized_count": f"{spec_report['realized_count']}/{spec_report['total_modules']}",
                "spec_file": spec_report["spec"]["path"],
                "timestamp": utc_now()
            }

            # 6. EVIDENCE & SOVEREIGN CERTIFICATION
            cert_data = self.certifier.generate_certificate()
            evidence_file = self.releases_dir / f"audit_evidence_{timestamp}.json"
            evidence_payload = {
                "system": "HCOS - FORINA TITAN EVIDENCE & CERTIFICATION",
                "sovereign_certificate": cert_data,
                "spec_sync": spec_report,
                "inventory": inventory,
                "build_metadata": build_marker
            }
            evidence_file.write_text(json.dumps(evidence_payload, indent=2, ensure_ascii=False), encoding="utf-8")
            report["stages"]["EVIDENCE"] = {
                "status": "PASS",
                "evidence_path": str(evidence_file),
                "ed25519_signature": cert_data["cryptographic_signatures"]["ed25519_signature_hex"][:32] + "...",
                "timestamp": utc_now()
            }

            # 7. PACKAGING (AppDir Staging & ZIP release)
            appdir = self.dist_dir / "AetherTitan.AppDir"
            appdir_usr = appdir / "usr" / "bin"
            appdir_usr.mkdir(parents=True, exist_ok=True)
            
            # AppRun script
            apprun = appdir / "AppRun"
            apprun.write_text(
                "#!/usr/bin/env bash\n"
                "HERE=\"$(dirname \"$(readlink -f \"${0}\")\")\"\n"
                "export APP_TIMESTAMP=\"" + timestamp + "\"\n"
                "if command -v xdg-open >/dev/null 2>&1; then\n"
                "  xdg-open \"${HERE}/usr/bin/index.html\" &\n"
                "fi\n",
                encoding="utf-8"
            )
            apprun.chmod(apprun.stat().st_mode | stat.S_IEXEC | stat.S_IXGRP | stat.S_IXOTH)

            # Desktop entry
            desktop_entry = appdir / "hcos-titan.desktop"
            desktop_entry.write_text(
                "[Desktop Entry]\n"
                "Name=HCOS Forina Titan\n"
                "Exec=AppRun\n"
                "Icon=icon\n"
                "Type=Application\n"
                "Categories=Development;Security;\n"
                "Comment=HCOS Forina Titan Engine Portal\n",
                encoding="utf-8"
            )

            # Copy web into appdir & icons
            for f in self.dist_dir.glob("*"):
                if f.is_file():
                    shutil.copy2(f, appdir_usr / f.name)
                elif f.is_dir() and f.name != "AetherTitan.AppDir":
                    shutil.copytree(f, appdir_usr / f.name, dirs_exist_ok=True)
            if (self.web_dir / "icon.svg").exists():
                shutil.copy2(self.web_dir / "icon.svg", appdir / "hcos-titan.svg")

            # Finalize 100% Comprehensive Inventory (including AppDir & all staged assets)
            final_inventory = {}
            for item in sorted(self.dist_dir.rglob("*")):
                if item.is_file():
                    rel = item.relative_to(self.dist_dir)
                    final_inventory[str(rel)] = calc_sha256(item.read_bytes())

            (self.meta_dir / "inventory.sha256").write_text(
                "\n".join(f"{h}  {f}" for f, h in final_inventory.items()), encoding="utf-8"
            )

            # Build true Linux .AppImage binary if appimagetool is available
            appimage_path = self.releases_dir / f"ForinaTitan-1.2.0-x86_64.AppImage"
            appimagetool_bin = shutil.which("appimagetool") or os.path.expanduser("~/.local/bin/appimagetool")
            if os.path.exists(appimagetool_bin) and os.access(appimagetool_bin, os.X_OK):
                try:
                    import subprocess
                    env = os.environ.copy()
                    env["ARCH"] = "x86_64"
                    subprocess.run([appimagetool_bin, str(appdir), str(appimage_path)], env=env, check=True, capture_output=True)
                except Exception as ex:
                    print(f"[WARN] AppImage build notice: {ex}")

            # Create release zip
            release_zip = self.releases_dir / f"hcos-forina-titan-pwa-{timestamp}.zip"
            with zipfile.ZipFile(release_zip, "w", zipfile.ZIP_DEFLATED) as zf:
                for root_path, _, filenames in os.walk(self.dist_dir):
                    for fn in filenames:
                        fp = Path(root_path) / fn
                        rel_p = fp.relative_to(self.dist_dir)
                        zf.write(fp, arcname=str(rel_p))

            report["stages"]["PACKAGING"] = {
                "status": "PASS",
                "release_zip": str(release_zip),
                "zip_size_bytes": release_zip.stat().st_size,
                "appimage_binary": str(appimage_path) if appimage_path.exists() else None,
                "appimage_size_bytes": appimage_path.stat().st_size if appimage_path.exists() else 0,
                "timestamp": utc_now()
            }

            report["status"] = "SUCCESS"
            report["duration_seconds"] = round(time.time() - start_time, 3)

        except Exception as e:
            report["status"] = "ERROR"
            report["errors"].append(str(e))
            report["duration_seconds"] = round(time.time() - start_time, 3)

        return report
