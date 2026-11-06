"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
50 REPOSITORY EVALUATION CATALOG & EXPLORER
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
import csv
import json
from pathlib import Path
from typing import Dict, Any, List, Optional

ZONE_MAPPING = {
    "Local Sovereign Zone": [
        "tauri-apps/tauri", "AppImage/AppImageKit", "borgbackup/borg",
        "javascript-obfuscator/javascript-obfuscator", "mrdoob/three.js",
        "greensock/GSAP", "catdad/canvas-confetti", "goldfire/howler.js",
        "react-grid-layout/react-grid-layout", "ueberdosis/tiptap",
        "codex-team/editor.js", "framer/motion", "yeojz/otplib",
        "soldair/node-qrcode", "orestbida/cookieconsent", "ffmpegwasm/ffmpeg.wasm",
        "videojs/video.js", "johannesjo/super-productivity", "open-policy-agent/opa",
        "GoogleChrome/workbox", "vite-pwa/vite-plugin-pwa", "pubkey/rxdb",
        "off-grid-ai/OGAM", "off-grid-ai/OGAD"
    ],
    "Development & Research Zone": [
        "cunnie/sslip.io", "exentriquesolutions/nip.io", "AppImageCommunity/AppImageUpdate",
        "tauri-apps/plugins-workspace", "Cap-go/capacitor-updater",
        "electron-userland/electron-builder", "module-federation/core",
        "originjs/vite-plugin-federation", "single-spa/single-spa", "systemjs/systemjs",
        "pwa-builder/PWABuilder", "ionic-team/capacitor", "tw93/Pake",
        "amazon-agi/BOBA-bench", "AGGIB/Stroq"
    ],
    "Federation & Integration Zone": [
        "caddyserver/caddy", "nginx/nginx", "pocket-id/pocket-id",
        "authelia/authelia", "langgenius/dify", "vercel/ai",
        "linagora/jmap-client-ts", "audreyt/jmap-client-ts", "stalwartlabs/mail-server",
        "umami-software/umami", "plausible/analytics", "calcom/cal.com"
    ]
}

MODULE_MAPPING = {
    "tauri-apps/tauri": ("M02", "Secure App Builder & Packaging"),
    "AppImage/AppImageKit": ("M02", "Linux Binary AppImage Engine"),
    "javascript-obfuscator/javascript-obfuscator": ("M02", "Client Source Obfuscator"),
    "borgbackup/borg": ("M13", "Deterministic Encrypted Backup"),
    "caddyserver/caddy": ("M07", "Reverse Proxy & TLS Termination"),
    "nginx/nginx": ("M07", "High Performance Web Server"),
    "cunnie/sslip.io": ("M07", "Wildcard DNS Routing Reference"),
    "exentriquesolutions/nip.io": ("M07", "Wildcard IP DNS Reference"),
    "greensock/GSAP": ("M03", "UI Motion & Velvet Curtain Effects"),
    "mrdoob/three.js": ("M03", "3D Interactive Holographic UI"),
    "catdad/canvas-confetti": ("M03", "Verification Celebration Particles"),
    "goldfire/howler.js": ("M11", "528Hz Solfeggio Audio Engine"),
    "react-grid-layout/react-grid-layout": ("M03", "Dynamic Modular Workspace Grid"),
    "ueberdosis/tiptap": ("M03", "Headless Collaborative Editor"),
    "codex-team/editor.js": ("M03", "Clean Block-Style JSON Editor"),
    "framer/motion": ("M03", "Declarative Animation Engine"),
    "pocket-id/pocket-id": ("M04", "OIDC Passkey Identity Provider"),
    "authelia/authelia": ("M04", "Enterprise Single Sign-On Gateway"),
    "yeojz/otplib": ("M04", "RFC 6238 TOTP Two-Factor Authenticator"),
    "soldair/node-qrcode": ("M04", "Dynamic QR Authenticator Staging"),
    "orestbida/cookieconsent": ("M04", "GDPR/ePrivacy Consent Enforcer"),
    "langgenius/dify": ("M05", "Visual Agent & Workflow Orchestration"),
    "vercel/ai": ("M05", "Multi-Provider LLM Client Framework"),
    "ffmpegwasm/ffmpeg.wasm": ("M11", "In-Browser Sovereign Video Processing"),
    "videojs/video.js": ("M11", "HTML5 Universal Video Streamer"),
    "johannesjo/super-productivity": ("M09", "Time Tracking & Task Management"),
    "open-policy-agent/opa": ("M07", "Declarative Compliance & Gate Policy"),
    "linagora/jmap-client-ts": ("M09", "Modern JMAP Email Protocol Client"),
    "audreyt/jmap-client-ts": ("M09", "Modern JMAP Email Protocol Client (Linagora / Audrey Tang)"),
    "stalwartlabs/mail-server": ("M09", "All-in-One Rust Mail Gateway"),
    "umami-software/umami": ("M10", "Cookie-Free Sovereign Telemetry"),
    "plausible/analytics": ("M10", "Privacy-Preserving Web Analytics"),
    "calcom/cal.com": ("M09", "Sovereign Calendar Scheduling Engine"),
    "AppImageCommunity/AppImageUpdate": ("M02", "Delta Binary OTA Updater"),
    "tauri-apps/plugins-workspace": ("M02", "Cross-Platform System Plugin Suite"),
    "Cap-go/capacitor-updater": ("M02", "Live Background PWA Delta Updater"),
    "electron-userland/electron-builder": ("M02", "Multi-Target Application Packager"),
    "module-federation/core": ("M01", "Dynamic Microfrontend Federation Core"),
    "originjs/vite-plugin-federation": ("M01", "Vite Module Federation Pipeline"),
    "single-spa/single-spa": ("M01", "Multi-Framework Top-Level Router"),
    "systemjs/systemjs": ("M01", "Universal Dynamic Module Loader"),
    "GoogleChrome/workbox": ("M02", "PWA Cache & Offline Service Worker"),
    "vite-pwa/vite-plugin-pwa": ("M02", "Vite Progressive Web App Bundler"),
    "pwa-builder/PWABuilder": ("M02", "Store-Ready PWA Packaging Suite"),
    "ionic-team/capacitor": ("M02", "Mobile Native Runtime Bridge"),
    "tw93/Pake": ("M02", "Lightweight Rust Desktop Webview Shell"),
    "pubkey/rxdb": ("M06", "Offline-First Reactive Realtime DB"),
    "amazon-agi/BOBA-bench": ("M12", "Multi-Agent Error-Chain Benchmark"),
    "off-grid-ai/OGAM": ("M05", "Air-Gapped Mobile Offline AI Engine"),
    "off-grid-ai/OGAD": ("M05", "Air-Gapped Desktop Offline AI Engine"),
    "AGGIB/Stroq": ("M13", "Real-Time Agent Session Security Scanner")
}


class RepositoryEvaluationCatalog:
    """Manages the 50 Open-Source Repositories from the HCOS Specification and Newsletters."""

    def __init__(self, project_root: Optional[Path] = None):
        if project_root is None:
            project_root = Path(__file__).parent.parent
        self.root = Path(project_root)
        self.csv_path = self.root / "docs" / "repository_evaluation_matrix.csv"
        self._repos: List[Dict[str, Any]] = []
        self._load()

    def _load(self):
        if not self.csv_path.exists():
            return

        with open(self.csv_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                repo_name = row.get("Repository", "").strip()
                # Determine Zone (Fail-Closed: unknown repos are NEVER assigned to Sovereign Zone)
                zone = "Unassigned / Pending Review"
                for z_name, z_repos in ZONE_MAPPING.items():
                    if repo_name in z_repos:
                        zone = z_name
                        break

                mod_id, mod_role = MODULE_MAPPING.get(repo_name, ("M00", row.get("Geplante_Rolle", "")))

                self._repos.append({
                    "nr": int(row.get("Nr", 0)),
                    "repository": repo_name,
                    "url": row.get("URL", ""),
                    "pdf_source": row.get("PDF", ""),
                    "pdf_page": row.get("PDF-Seite", ""),
                    "planned_role": row.get("Geplante_Rolle", ""),
                    "module_id": mod_id,
                    "module_role": mod_role,
                    "integration_decision": row.get("Integrationsentscheid", ""),
                    "origin_note": row.get("Herkunft", ""),
                    "zone": zone,
                    "license_check": row.get("Lizenzpruefung", "OFFEN"),
                    "security_check": row.get("Sicherheitspruefung", "OFFEN")
                })

    def list_all(self) -> List[Dict[str, Any]]:
        return list(self._repos)

    def filter_by_zone(self, zone_name: str) -> List[Dict[str, Any]]:
        zone_lower = zone_name.lower()
        return [r for r in self._repos if zone_lower in r["zone"].lower()]

    def filter_by_module(self, module_id: str) -> List[Dict[str, Any]]:
        return [r for r in self._repos if r["module_id"].upper() == module_id.upper()]

    def get_by_nr(self, nr: int) -> Optional[Dict[str, Any]]:
        for r in self._repos:
            if r["nr"] == nr:
                return r
        return None

    def get_summary(self) -> Dict[str, Any]:
        zones = {}
        for r in self._repos:
            z = r["zone"]
            zones[z] = zones.get(z, 0) + 1

        decisions = {}
        for r in self._repos:
            d = r["integration_decision"]
            decisions[d] = decisions.get(d, 0) + 1

        modules = {}
        for r in self._repos:
            m = r["module_id"]
            modules[m] = modules.get(m, 0) + 1

        return {
            "total_repositories": len(self._repos),
            "zones_breakdown": zones,
            "decision_breakdown": decisions,
            "modules_breakdown": modules,
            "sovereign_local_count": zones.get("Local Sovereign Zone", 0),
            "development_count": zones.get("Development & Research Zone", 0),
            "federation_count": zones.get("Federation & Integration Zone", 0)
        }
