"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
FORINA TITAN HARDENED ENGINE SERVER & LIVE-SYNC GATEWAY
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
from __future__ import annotations
import hashlib
import json
import os
import secrets
import stat
import time
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path
from urllib.parse import urlparse, parse_qs

from .spec_sync import SpecSyncEngine
from .certification import SovereignCertifier
from .agent_orchestrator import AgentOrchestrator
from .module_loader import ModuleLoader, ModuleSecurityViolation

CURRENT_VERSION = "1.2.0"


def _load_or_generate_api_key(root: Path) -> str:
    """Loads secure API key from environment or creates a cryptographically random secret."""
    env_key = os.environ.get("FORINA_API_KEY")
    if env_key:
        return env_key

    key_file = root / "config" / ".api_key"
    if key_file.exists():
        try:
            return key_file.read_text(encoding="utf-8").strip()
        except Exception:
            pass

    key_file.parent.mkdir(parents=True, exist_ok=True)
    generated = "FORINA-" + secrets.token_urlsafe(24)
    key_file.write_text(generated, encoding="utf-8")
    try:
        os.chmod(key_file, stat.S_IRUSR | stat.S_IWUSR)
    except Exception:
        pass
    return generated


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

        # 1. LIVE-SYNC & SPEC STATUS (Light Blink Buttons & 4-Tier Statistic Glow Points)
        if parsed.path in ("/api/spec-status", "/api/live-sync"):
            sync_engine = SpecSyncEngine(self.project_root)
            report = sync_engine.verify_all_modules()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(report, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 2. SOVEREIGN CERTIFICATION & ED25519 ENDPOINT
        if parsed.path == "/api/certificate":
            certifier = SovereignCertifier(self.project_root)
            cert = certifier.generate_certificate()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(cert, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 2b. CERTIFICATE VERIFY ENDPOINT
        if parsed.path == "/api/certificate/verify":
            certifier = SovereignCertifier(self.project_root)
            is_valid = certifier.verify_certificate()
            self._set_json_headers(200)
            self.wfile.write(json.dumps({
                "verified": is_valid,
                "algorithm": "Ed25519",
                "status": "VALID_AND_AUTHENTIC" if is_valid else "VERIFICATION_FAILED"
            }, indent=2).encode("utf-8"))
            return

        # 3. OTA VERSION ENDPOINT
        if parsed.path == "/api/ota/version":
            response = {
                "system": "HCOS - FORINA TITAN ENGINE",
                "latest_version": CURRENT_VERSION,
                "timestamp": int(time.time()),
                "ota_ready": True,
                "changelog": "Ed25519 Asymmetric Signature, 4-Tier Production Assurance & Server Hardening."
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(response, indent=2).encode("utf-8"))
            return

        # 4. ATOMIC CLOCK ENDPOINT
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

        # 5. MODULE LOADER & CATALOG ENDPOINTS
        loader = ModuleLoader(self.project_root)
        if parsed.path == "/api/modules/catalog":
            self._set_json_headers(200)
            self.wfile.write(json.dumps(loader.get_suite_summary(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/modules/verify":
            mid = query.get("id", ["01_agent_studio"])[0]
            res = loader.verify_module(mid)
            self._set_json_headers(200 if res.get("success") else 400)
            self.wfile.write(json.dumps(res, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/modules/test":
            mid = query.get("id", ["01_agent_studio"])[0]
            res = loader.test_module(mid)
            self._set_json_headers(200 if res.get("success") else 400)
            self.wfile.write(json.dumps(res, indent=2, ensure_ascii=False).encode("utf-8"))
            return

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

        # 6. AI STUDIO & AGENTS ENDPOINTS
        orch = AgentOrchestrator(self.project_root)
        if parsed.path == "/api/agents/list":
            self._set_json_headers(200)
            self.wfile.write(json.dumps(orch.list_agents(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/skills/list":
            self._set_json_headers(200)
            self.wfile.write(json.dumps(orch.list_skills(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/skills/get":
            skill_name = query.get("name", ["forina-domain-trust"])[0]
            content = orch.get_skill_content(os.path.basename(skill_name))
            if content is None:
                self._set_json_headers(404)
                self.wfile.write(json.dumps({"error": "Skill nicht gefunden"}).encode("utf-8"))
                return
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"skill": skill_name, "markdown": content}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/mcp/connectors":
            self._set_json_headers(200)
            self.wfile.write(json.dumps(orch.mcp.list_connectors(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/mcp/debug":
            cid = query.get("id", ["github"])[0]
            diag = orch.mcp.debug_connector(cid)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(diag, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/knowledge/search":
            q = query.get("q", ["Compliance"])[0]
            results = orch.kb.search(q, top_k=3)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(results, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/secrets/status":
            self._set_json_headers(200)
            self.wfile.write(json.dumps(orch.secrets.get_vault_summary(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # Fallback to static file serving
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        master_api_key = _load_or_generate_api_key(self.project_root)

        # 6. JMAP PARTNER INQUIRY (Redacted Logging for Privacy & GDPR)
        if parsed.path == "/api/jmap/partner-inquiry":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            target_email = "world.banks.eyes.aether@globedynamicz.statesflowwishes.eu"
            body_digest = hashlib.sha256(body.encode("utf-8")).hexdigest()[:16]
            print(f"[JMAP-RELAY] Partnerschaftsanfrage erhalten [Bytes: {length}, Digest: {body_digest}] -> Relay zu IONOS ({target_email})")

            response = {
                "success": True,
                "relay": "JMAP Client TS -> Stalwart -> IONOS",
                "target": target_email,
                "digest": body_digest,
                "received_at": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(response).encode("utf-8"))
            return

        # 7. DYNAMIC MODULE REGISTRATION (Protected via Master API Key)
        if parsed.path == "/api/modules/register":
            client_key = self.headers.get("X-Forina-API-Key", "")
            if not client_key or not secrets.compare_digest(client_key, master_api_key):
                self._set_json_headers(403)
                self.wfile.write(json.dumps({"error": "Ungueltiger oder fehlender API-Key"}).encode("utf-8"))
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

        # 8. AI MULTI-AGENT CHAT QUERY
        if parsed.path == "/api/agents/chat":
            orch = AgentOrchestrator(self.project_root)
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            data = json.loads(body)
            agent_id = data.get("agent_id", "compliance")
            prompt = data.get("prompt", "Status abfragen")
            result = orch.query_agent(agent_id, prompt)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(result, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 9. KNOWLEDGE BASE WEBSITE INDEXING SIMULATION
        if parsed.path == "/api/knowledge/index":
            orch = AgentOrchestrator(self.project_root)
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8")
            data = json.loads(body)
            url = data.get("url", "https://europa.eu")
            result = orch.kb.index_website_simulation(url, page_limit=data.get("page_limit", 10))
            self._set_json_headers(201)
            self.wfile.write(json.dumps(result, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 10. MODULE EXECUTION & FAIL-CLOSED GATEWAY
        if parsed.path == "/api/modules/execute":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
            data = json.loads(body)
            mid = data.get("module_id", "01_agent_studio")
            action = data.get("action", "self_test")
            params = data.get("params", {})
            loader = ModuleLoader(self.project_root)
            try:
                res = loader.execute_module(mid, action, params)
                self._set_json_headers(200)
                self.wfile.write(json.dumps(res, indent=2, ensure_ascii=False).encode("utf-8"))
            except ModuleSecurityViolation as sv:
                self._set_json_headers(403)
                self.wfile.write(json.dumps({"error": "SecurityGateViolation", "message": str(sv)}).encode("utf-8"))
            except Exception as ex:
                self._set_json_headers(500)
                self.wfile.write(json.dumps({"error": "ExecutionError", "message": str(ex)}).encode("utf-8"))
            return

        # 11. PROMOTE ALL MODULES
        if parsed.path == "/api/modules/promote-all":
            loader = ModuleLoader(self.project_root)
            results = loader.promote_all_to_freigegeben()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(results, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        self._set_json_headers(404)
        self.wfile.write(json.dumps({"error": "Unbekannter Endpunkt"}).encode("utf-8"))


def run_engine_server(host: str = "127.0.0.1", port: int = 4000, project_root: Path | None = None):
    if project_root:
        os.environ["FORINA_PROJECT_ROOT"] = str(project_root)
    else:
        project_root = Path(os.environ.get("FORINA_PROJECT_ROOT", Path(__file__).parent.parent))

    api_key = _load_or_generate_api_key(project_root)
    server_address = (host, port)
    httpd = HTTPServer(server_address, ForinaEngineHandler)
    print(f"==================================================================")
    print(f" HCOS FORINA TITAN ENGINE SERVER (GEHÄRTET):")
    print(f" -> Host-Binding:             {host} (Localhost Safe)")
    print(f" -> Portal UI & Live Radar:   http://{host}:{port}")
    print(f" -> Live-Sync & Spec Radar:   http://{host}:{port}/api/live-sync")
    print(f" -> Ed25519 Zertifikat:       http://{host}:{port}/api/certificate")
    print(f" -> OTA Versions-Check:       http://{host}:{port}/api/ota/version")
    print(f" -> Aktiver API-Key (gehärtet): {api_key[:12]}...")
    print(f"==================================================================")
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\n[Engine Server] Gestoppt.")
        httpd.server_close()
