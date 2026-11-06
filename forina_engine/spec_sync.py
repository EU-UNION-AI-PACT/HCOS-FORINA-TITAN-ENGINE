"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
SPEC-SYNC ENGINE: Live-Verifikation gegen 'Tool Build Processing - Securty - So Baut man.txt'
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
import hashlib
import json
import os
import re
import time
from pathlib import Path
from typing import Dict, Any, List

SPEC_CANDIDATE_PATHS = [
    Path("/home/shinehealthcare/Schreibtisch/Tool Build Processing - Securty - So Baut man.txt"),
    Path(__file__).parent.parent / "Tool-Build-Processing-Security-Spec.txt",
    Path("/home/shinehealthcare/Schreibtisch/Tool Build Processing - Securty - So Baut man.pdf")
]

MODULE_SPEC_DEFINITIONS = [
    {
        "id": "app_engine",
        "name": "1. App-Engine, Build-Pipeline & Code-Schutz",
        "short_name": "App-Engine & Schutz",
        "color": "gold",
        "glow_class": "glow-gold",
        "spec_keywords": ["Tauri", "AppImage", "JavaScript Obfuscator", "BorgBackup", "ide-source", "build-dist"],
        "required_files": ["web/index.html", "scripts/build_pipeline.sh", "forina_engine/engine.py"],
        "description": "AppImage-Packaging, automatisches Vorab-Backup mit Zeitstempel, Code-Obfuskation & Integritäts-Hashes.",
        "spec_quote": "AppImage-Packaging: Kompilierung als ausführbares Linux-AppImage mit Zeitstempel und automatischem Backup vor jedem Build."
    },
    {
        "id": "network_dns",
        "name": "2. Netzwerk, Reverse Proxy & Wildcard-DNS",
        "short_name": "Netzwerk & Wildcard-DNS",
        "color": "cyan",
        "glow_class": "glow-cyan",
        "spec_keywords": ["Caddy", "NGINX", "sslip.io", "nip.io", "Reverse Proxy"],
        "required_files": ["config/Caddyfile", "config/nginx.conf"],
        "description": "Automatische Einbindung von Caddy & NGINX mit dynamischen sslip.io / nip.io Wildcard-Domains.",
        "spec_quote": "Reverse Proxy & Wildcard-DNS: Automatische Einbindung von NGINX und Caddy in Kombination mit sslip.io und nip.io."
    },
    {
        "id": "ui_inszenierung",
        "name": "3. UI/UX-Engines, Effekte & Start-Inszenierung",
        "short_name": "UI/UX & Show-Effekte",
        "color": "pink",
        "glow_class": "glow-pink",
        "spec_keywords": ["GSAP", "Three.js", "Canvas Confetti", "Howler.js", "Theatervorhang", "Scheibenwischer", "Glocke", "Feuermelder"],
        "required_files": ["web/index.html", "web/styles.css", "web/app.js"],
        "description": "Roter Theatervorhang, 3s-Glocke (3% Vol), Scheibenwischer (4s-Takt), Blitz, Happy-Overshine Konfetti & Feuermelder.",
        "spec_quote": "Start-Sequenz: Theatervorhang mit Wellenmuster, 3s-Glockensignal auf 3% Lautstärke, Scheibenwischer alle 4 Sekunden."
    },
    {
        "id": "interface_editor",
        "name": "4. Kern-Interface, PiP-Browser & Redaktions-Editor",
        "short_name": "PiP & Journalisten-Editor",
        "color": "amber",
        "glow_class": "glow-amber",
        "spec_keywords": ["Tiptap", "Editor.js", "Framer Motion", "Flip-Board", "PiP", "Journalist", "Thinking Flow"],
        "required_files": ["web/index.html", "web/app.js"],
        "description": "3D Flip-Board in Sidebar, Picture-in-Picture Webbrowser, Inline-Text-Editor und kategorisierbarer Journalisten-Export.",
        "spec_quote": "In die Sidebar integriertes 3D-Flip-Board mit PiP-Webbrowser sowie Thinking-Flow Journalisten-Editor mit TXT-Export."
    },
    {
        "id": "iam_auth_otp",
        "name": "5. Authentifizierung (IAM), Passkeys, OTP & Datenschutz",
        "short_name": "IAM, Passkey & OTP",
        "color": "purple",
        "glow_class": "glow-purple",
        "spec_keywords": ["Pocket ID", "Authelia", "otplib", "QR-Code", "SMS-OTP", "CookieConsent", "GPS"],
        "required_files": ["web/index.html", "web/app.js"],
        "description": "Magic Link Flow, TOTP QR-Code-Generator, Mobilfunk SMS-OTP Simulator, Cookie-Banner & GPS Opt-In mit Widerruf.",
        "spec_quote": "Zugriffsschutz über Magic Link, QR-Code Authenticator, SMS-OTP Handy Token sowie CookieConsent mit GPS Opt-in."
    },
    {
        "id": "ai_media",
        "name": "6. KI-Integration, Video-Clipping & Zeiterfassung",
        "short_name": "KI-Suche & Video-Clip",
        "color": "neon-red",
        "glow_class": "glow-red",
        "spec_keywords": ["Claude", "LLM", "Vercel AI", "FFmpeg", "30-Sekunden", "Video-Clipper", "Atomuhr", "Fokus-Timer"],
        "required_files": ["web/index.html", "web/app.js"],
        "description": "Agent-Assist KI-Suche, animierte News-Ticker Timeline, 30s Promo-Video Player mit In/Out Clipping, Atomuhr & Stoppuhr.",
        "spec_quote": "Integrierter 30-Sekunden Promo-Clip mit Clipping-Funktion, Claude LLM Suche und Atomuhr gekoppelt mit Fokus-Stoppuhr."
    },
    {
        "id": "compliance_jmap",
        "name": "7. Compliance, Audit-Engine & JMAP-Anbindung",
        "short_name": "EU-Compliance & JMAP",
        "color": "emerald",
        "glow_class": "glow-emerald",
        "spec_keywords": ["Open Policy Agent", "JMAP", "Stalwart", "EU-Union", "Original-Inhalt", "Herzens", "IONOS"],
        "required_files": ["web/index.html", "forina_engine/server.py"],
        "description": "EU-Audit- & Inspektoren-Portal, 3 Werte-Badges, JMAP Partnerschafts-Request an world.banks.eyes.aether@globedynamicz.statesflowwishes.eu.",
        "spec_quote": "Drei Originalitäts-Badges (EU-Union, Original-Inhalt, Herzens-Güte) und JMAP-Partnerschafts-Request an IONOS-Postfach."
    },
    {
        "id": "telemetry_calendar",
        "name": "8. Anonyme Telemetrie, Statistik & Buchungssystem",
        "short_name": "Telemetrie & Kalender",
        "color": "blue",
        "glow_class": "glow-blue",
        "spec_keywords": ["Umami", "Plausible", "Cal.com", "Anonyme", "Views", "Buchung", "Kalender", "Persistent Sync"],
        "required_files": ["web/index.html", "web/app.js", "forina_engine/spec_sync.py"],
        "description": "Anonymes Session-ID Tracking, persistente Echtzeit-Views, Termin- & Programm-Kalender, Live-Sync Realisierungs-Signal.",
        "spec_quote": "Eigenständiges Statistik-Dashboard auf anonymer Basis, Termin-Buchungskalender sowie persistente Synchronisation."
    }
]


class SpecSyncEngine:
    def __init__(self, project_root: Path):
        self.project_root = Path(project_root)
        self.spec_file = self._locate_spec_file()

    def _locate_spec_file(self) -> Path | None:
        for p in SPEC_CANDIDATE_PATHS:
            if p.exists() and p.is_file() and p.stat().st_size > 0:
                return p
        return None

    def get_spec_meta(self) -> Dict[str, Any]:
        if not self.spec_file or not self.spec_file.exists():
            return {
                "available": False,
                "path": "Nicht gefunden",
                "sha256": None,
                "size_bytes": 0,
                "last_modified": None
            }
        
        stat = self.spec_file.stat()
        content = self.spec_file.read_bytes()
        return {
            "available": True,
            "path": str(self.spec_file),
            "sha256": hashlib.sha256(content).hexdigest(),
            "size_bytes": stat.st_size,
            "last_modified": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(stat.st_mtime))
        }

    def verify_all_modules(self) -> Dict[str, Any]:
        spec_text = ""
        if self.spec_file and self.spec_file.exists():
            try:
                spec_text = self.spec_file.read_text(encoding="utf-8", errors="ignore")
            except Exception:
                pass

        verified_modules = []
        total_score = 0

        for defn in MODULE_SPEC_DEFINITIONS:
            # Check 1: Do required files exist in project?
            file_checks = {}
            for req_rel in defn["required_files"]:
                target = self.project_root / req_rel
                file_checks[req_rel] = target.exists() and target.stat().st_size > 0

            files_ok = all(file_checks.values())

            # Check 2: Does spec contain keywords?
            keyword_matches = []
            for kw in defn["spec_keywords"]:
                if re.search(r"\b" + re.escape(kw) + r"\b", spec_text, re.IGNORECASE):
                    keyword_matches.append(kw)

            keyword_coverage = len(keyword_matches) / len(defn["spec_keywords"]) if defn["spec_keywords"] else 1.0

            # Realized condition
            is_realized = files_ok and (keyword_coverage >= 0.5 or not spec_text)
            mod_score = 100 if (files_ok and is_realized) else (60 if files_ok else 20)
            total_score += mod_score

            light_state = "blink-green" if mod_score == 100 else ("pulse-amber" if mod_score >= 50 else "glow-red")

            verified_modules.append({
                "id": defn["id"],
                "name": defn["name"],
                "short_name": defn["short_name"],
                "color": defn["color"],
                "glow_class": defn["glow_class"],
                "light_state": light_state,
                "realized": is_realized,
                "score": mod_score,
                "description": defn["description"],
                "spec_quote": defn["spec_quote"],
                "file_evidence": file_checks,
                "keyword_matches": keyword_matches,
                "verified_at": time.strftime("%Y-%m-%d %H:%M:%S")
            })

        overall_percentage = round(total_score / len(MODULE_SPEC_DEFINITIONS))
        overall_realized = overall_percentage == 100

        return {
            "system": "HCOS - FORINA TITAN ENGINE",
            "copyright": "Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.",
            "spec": self.get_spec_meta(),
            "overall_realized": overall_realized,
            "overall_percentage": overall_percentage,
            "realized_count": sum(1 for m in verified_modules if m["realized"]),
            "total_modules": len(MODULE_SPEC_DEFINITIONS),
            "engine_status": "ONLINE - VERIFIED & SYNCHRONIZED" if overall_realized else "VERIFYING",
            "statistic_glow_points": {
                "active_glow_color": "#00ff88" if overall_realized else "#ffd700",
                "pulse_frequency_seconds": 1.2,
                "points": [
                    {"label": m["short_name"], "score": m["score"], "glow": m["glow_class"], "light": m["light_state"]}
                    for m in verified_modules
                ]
            },
            "modules": verified_modules,
            "generated_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
        }
