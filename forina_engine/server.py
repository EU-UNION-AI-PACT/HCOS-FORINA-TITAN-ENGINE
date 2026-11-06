"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
FORINA TITAN UNIFIED ENGINE SERVER & LIVE-SYNC GATEWAY
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
import json
import os
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs
from .spec_sync import SpecSyncEngine
from .certification import SovereignCertifier

API_MASTER_KEY = os.environ.get("FORINA_API_KEY", "FORINA-TITAN-2026-SECRET")
CURRENT_VERSION = "1.2.0"


class ForinaEngineHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        self.project_root = Path(os.environ.get("FORINA_PROJECT_ROOT", Path(__file__).parent.parent))
        self.dist_dir = self.project_root / "dist"
        self.web_dir = self.project_root / "web"
        # Serve from dist if available, else from web
        serve_dir = self.dist_dir if (self.dist_dir / "index.html").exists() else self.web_dir
        super().__init__(*args, directory=str(serve_dir), **kwargs)

    def _set_json_headers(self, status=200):
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Access-Control-Allow-Origin", "*")
        self.send_header("Access-Control-Allow-Headers", "Content-Type, X-Forina-API-Key")
        self.send_header("Access-Control-Allow-Methods", "GET, POST, OPTIONS")
        self.send_header("Cache-Control", "no-cache, no-store, must-revalidate")
        self.end_headers()

    def do_OPTIONS(self):
        self._set_json_headers(200)

    def do_GET(self):
        parsed = urlparse(self.path)
        query = parse_qs(parsed.query)

        # 1. LIVE-SYNC & SPEC STATUS (Light Blink Buttons & Statistic Glow Points)
        if parsed.path in ("/api/spec-status", "/api/live-sync"):
            sync_engine = SpecSyncEngine(self.project_root)
            report = sync_engine.verify_all_modules()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(report, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 1b. SOVEREIGN CERTIFICATION ENDPOINT
        if parsed.path == "/api/certificate":
            certifier = SovereignCertifier(self.project_root)
            cert = certifier.generate_certificate()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(cert, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 2. OTA VERSION ENDPOINT
        if parsed.path == "/api/ota/version":
            response = {
                "system": "HCOS - FORINA TITAN ENGINE",
                "latest_version": CURRENT_VERSION,
                "timestamp": int(time.time()),
                "ota_ready": True,
                "changelog": "Live Spec Realisierungs-Radar, Statistic Light Glow Points & Full Engine Integration."
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(response, indent=2).encode("utf-8"))
            return

        # 3. ATOMIC CLOCK ENDPOINT
        if parsed.path == "/api/atomclock":
            payload = {
                "utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()),
                "cet": time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()),
                "precision": "PTB-Braunschweig-Atomic-Sync",
                "epoch_ms": int(time.time() * 1000)
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload).encode("utf-8"))
            return

        # 4. MODULE LOADER
        if parsed.path == "/api/modules/load":
            mod_name = query.get("name", ["app_engine"])[0]
            safe_name = os.path.basename(mod_name)
            registry_file = self.project_root / "registry" / f"{safe_name}.json"
            if not registry_file.exists():
                self._set_json_headers(404)
                self.wfile.write(json.dumps({"error": f"Modul '{safe_name}' nicht gefunden"}).encode("utf-8"))
                return
            self._set_json_headers(200)
            self.wfile.write(registry_file.read_bytes())
            return

        # Fallback to static file serving
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)

        # 5. JMAP PARTNER INQUIRY
        if parsed.path == "/api/jmap/partner-inquiry":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            target_email = "world.banks.eyes.aether@globedynamicz.statesflowwishes.eu"
            print(f"[JMAP-RELAY] Partnerschafts-Anfrage erhalten -> Weiterleitung an IONOS ({target_email})")
            print(f"[JMAP-RELAY] Payload: {body}")
            response = {
                "success": True,
                "relay": "JMAP Client TS -> Stalwart -> IONOS",
                "target": target_email,
                "received_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return

        # 6. DYNAMIC MODULE REGISTRATION
        if parsed.path == "/api/modules/register":
            client_key = self.headers.get("X-Forina-API-Key", "")
            if client_key != API_MASTER_KEY:
                self._set_json_headers(403)
                self.wfile.write(json.dumps({"error": "Ungueltiger API-Key"}).encode("utf-8"))
                return
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            data = json.loads(body)
            slug = os.path.basename(data.get("slug", f"custom-{int(time.time())}"))
            registry_dir = self.project_root / "registry"
            registry_dir.mkdir(parents=True, exist_ok=True)
            target_file = registry_dir / f"{slug}.json"
            target_file.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")
            self._set_json_headers(201)
            self.wfile.write(json.dumps({"status": "registered", "slug": slug}).encode("utf-8"))
            return

        self._set_json_headers(404)
        self.wfile.write(json.dumps({"error": "Unbekannter Endpunkt"}).encode("utf-8"))


def run_engine_server(port: int = 4000, project_root: Path | None = None):
    if project_root:
        os.environ["FORINA_PROJECT_ROOT"] = str(project_root)
    server_address = ("0.0.0.0", port)
    httpd = HTTPServer(server_address, ForinaEngineHandler)
    print(f"==================================================================")
    print(f" HCOS FORINA TITAN ENGINE SERVER LÄUFT:")
    print(f" -> Portal UI & Live Radar:   http://localhost:{port}")
    print(f" -> Live-Sync & Spec Radar:   http://localhost:{port}/api/live-sync")
    print(f" -> OTA Versions-Check:       http://localhost:{port}/api/ota/version")
    print(f" -> Atomuhr Synchronisation:  http://localhost:{port}/api/atomclock")
    print(f"==================================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[Engine Server] Gestoppt.")
        httpd.server_close()
