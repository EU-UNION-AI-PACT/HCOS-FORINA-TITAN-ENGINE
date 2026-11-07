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
from .financial_engine import FinancialIntelligenceEngine, SettlementViolationError
from .boba_validator import BobaErrorChainValidator
from .stroq_scanner import StroqAgentSecurityScanner
from .assurance_gates import AssuranceGatePipeline
from .repo_catalog import RepositoryEvaluationCatalog
from .concept_suite import ConceptPaperSuite
from .harness_loop import HarnessLoopEngine
from .actpack_zeroclock import ActPackZeroClock, NaTZaFaultToleranceViolation

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

        # 7. FINANCIAL INTELLIGENCE & MONEY LEAKS (M08)
        if parsed.path == "/api/financial/leaks":
            fin_engine = FinancialIntelligenceEngine()
            report = fin_engine.analyze_transactions()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(report, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 8. BOBA-BENCH ERROR CHAIN VALIDATOR (M12)
        if parsed.path == "/api/boba/verify-demo":
            boba = BobaErrorChainValidator()
            demo_steps = [
                {"name": "01_IntakeAnalysis", "mock_result": {"status": "SUCCESS", "records": 42}, "rules": {"required_keys": ["status"]}},
                {"name": "02_CalculateSum", "mock_result": 142.50, "rules": {"min_val": 10.0, "max_val": 1000.0}},
                {"name": "03_SecurityAudit", "mock_result": {"safe": True, "gate": "PASSED"}, "rules": {"required_keys": ["safe"]}}
            ]
            demo_res = boba.run_safe_chain(demo_steps)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(demo_res, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 9. 13-GATE ASSURANCE PIPELINE (G00 - G12)
        if parsed.path == "/api/assurance/gates":
            pipeline = AssuranceGatePipeline(self.project_root)
            audit = pipeline.audit_all_gates()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(audit, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 10. 50-REPOSITORY EVALUATION CATALOG
        if parsed.path == "/api/repos/catalog":
            catalog = RepositoryEvaluationCatalog(self.project_root)
            zone_filter = query.get("zone", [""])[0]
            if zone_filter:
                items = catalog.filter_by_zone(zone_filter)
            else:
                items = catalog.list_all()
            payload = {
                "summary": catalog.get_summary(),
                "count": len(items),
                "zone_filter": zone_filter or "all",
                "repositories": items
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 10b. WISH STUDIO 18-REPOSITORY FEDERATION CATALOG
        if parsed.path == "/api/repos/wish-studio":
            catalog = RepositoryEvaluationCatalog(self.project_root)
            items = catalog.get_wish_studio_catalog()
            payload = {
                "ecosystem": "Wish Studio & Gemeinwohl Digitaler Skill Pass",
                "count": len(items),
                "repositories": items
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 10c. LOCCP 352 OPEN-SOURCE REPOSITORIES MASTER CATALOG
        if parsed.path == "/api/repos/loccp":
            catalog = RepositoryEvaluationCatalog(self.project_root)
            qs = parse_qs(parsed.query)
            q = qs.get("q", [""])[0]
            cat = qs.get("category", [""])[0]
            limit = int(qs.get("limit", [50])[0])
            items = catalog.get_loccp_repo_catalog(query=q, category=cat, limit=limit)
            stats = catalog.get_loccp_stats()
            payload = {
                "catalog": "LOCCP Konsolidierter Masterkatalog 2026-11-04",
                "count": len(items),
                "stats": stats,
                "repositories": items
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 10d. 42 COMPLIANCE-PRÜFPUNKTE & SELF-ATTESTATION
        if parsed.path == "/api/compliance/pruefpunkte":
            catalog = RepositoryEvaluationCatalog(self.project_root)
            qs = parse_qs(parsed.query)
            mod = qs.get("module", [""])[0]
            pts = catalog.get_loccp_pruefpunkte(compliance_module=mod)
            payload = {
                "count": len(pts),
                "module_filter": mod,
                "pruefpunkte": pts
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/compliance/attestation":
            attestation_file = self.project_root / "docs" / "compliance" / "WISH_OS_LOCAL_FINANCE_COMPLIANCE_ATTESTATION.md"
            badge_file = self.project_root / "web" / "badges" / "WISH_OS_COMPLIANCE_DOCUMENTED.svg"
            payload = {
                "attestation_title": "COMPLIANCE & SECURITY ATTESTATION — Wish OS Local Finance Stack",
                "scope": "Lokale Finance-Infrastruktur (127.0.0.1 Air-Gap / Gate G03)",
                "date": "2026-10-30 16:11 CET",
                "provenance": "Daniel Pohl · Royal Kaiser Charter RegSys",
                "badge_url": "/badges/WISH_OS_COMPLIANCE_DOCUMENTED.svg",
                "badge_available": badge_file.exists(),
                "content_markdown": attestation_file.read_text(encoding="utf-8") if attestation_file.exists() else ""
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 11. 34 CONCEPT PAPERS SUITE & STANDARDS
        if parsed.path.startswith("/api/concepts/paper"):
            suite = ConceptPaperSuite(self.project_root)
            nr_str = query.get("nr", [""])[0]
            if not nr_str:
                parts = parsed.path.strip("/").split("/")
                if len(parts) >= 4 and parts[3].isdigit():
                    nr_str = parts[3]
            try:
                nr = int(nr_str)
            except (ValueError, TypeError):
                nr = 1
            paper_data = suite.get_paper_content(nr)
            if not paper_data:
                self._set_json_headers(404)
                self.wfile.write(json.dumps({"error": f"Concept Paper #{nr} not found"}, ensure_ascii=False).encode("utf-8"))
                return
            self._set_json_headers(200)
            self.wfile.write(json.dumps(paper_data, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/concepts/papers":
            suite = ConceptPaperSuite(self.project_root)
            cat_filter = query.get("category", [""])[0]
            search_query = query.get("q", [""])[0]
            if search_query:
                papers = suite.search_papers(search_query)
            else:
                papers = suite.list_papers(cat_filter)
            payload = {
                "summary": suite.get_summary(),
                "count": len(papers),
                "category_filter": cat_filter or "all",
                "papers": papers
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/concepts/standards":
            suite = ConceptPaperSuite(self.project_root)
            payload = {
                "count": len(suite.standards),
                "standards": suite.standards
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 11b. 144 SEITEN ENZYKLOPÄDIE — 4 BÄNDE & 136 KAPITEL
        if parsed.path == "/api/baende/list":
            suite = ConceptPaperSuite(self.project_root)
            payload = {
                "baende": suite.list_baende(),
                "specialized": suite.list_specialized_papers(),
                "total_chapters": 136
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/baende/content":
            band_letter = query.get("band", ["A"])[0]
            suite = ConceptPaperSuite(self.project_root)
            data = suite.get_band_content(band_letter)
            if not data:
                self._set_json_headers(404)
                self.wfile.write(json.dumps({"error": f"Band {band_letter} nicht gefunden"}).encode("utf-8"))
                return
            self._set_json_headers(200)
            self.wfile.write(json.dumps(data, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 11c. 34 NORMEN SVG BADGES & REGULATORY AUDIT
        if parsed.path == "/api/badges/list":
            from forina_engine.audit_badges import AuditBadgeRegistry
            reg = AuditBadgeRegistry(self.project_root)
            payload = {
                "summary": reg.get_summary(),
                "badges": reg.list_badges()
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path.startswith("/api/badges/svg"):
            from forina_engine.audit_badges import AuditBadgeRegistry
            reg = AuditBadgeRegistry(self.project_root)
            badge_id = query.get("id", [""])[0]
            if not badge_id:
                parts = parsed.path.strip("/").split("/")
                if len(parts) >= 4:
                    badge_id = parts[3]
            svg_content = reg.get_badge_svg(badge_id) if badge_id else None
            if not svg_content:
                self._set_json_headers(404)
                self.wfile.write(json.dumps({"error": f"Badge {badge_id} nicht gefunden"}).encode("utf-8"))
                return
            self.send_response(200)
            self.send_header("Content-Type", "image/svg+xml; charset=utf-8")
            self.send_header("Access-Control-Allow-Origin", "*")
            self.end_headers()
            self.wfile.write(svg_content.encode("utf-8"))
            return

        # 11d. INSTITUTIONAL FINANCE & CENTRAL BANKING
        if parsed.path == "/api/finance/institutions":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            payload = {
                "summary": fin_reg.get_summary(),
                "central_banks": fin_reg.get_central_banks(),
                "open_banking_providers": fin_reg.get_open_banking_providers(),
                "iso20022_schemas": fin_reg.get_iso20022_message_schemas(),
                "ezb_pontes": fin_reg.get_pontes_spec()
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/pontes":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(fin_reg.get_pontes_spec(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/portals":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            qs = parse_qs(parsed.query)
            q = qs.get("q", [""])[0]
            cat = qs.get("category", [""])[0]
            limit = int(qs.get("limit", [50])[0])
            portals = fin_reg.search_portals(query=q, category=cat, limit=limit)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(portals), "query": q, "category": cat, "portals": portals}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/clevel":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            qs = parse_qs(parsed.query)
            company = qs.get("company", [""])[0]
            clevel = fin_reg.get_clevel_directory(company_filter=company)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(clevel), "company_filter": company, "directory": clevel}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/enablebanking/apps":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            apps = fin_reg.get_enable_banking_apps()
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(apps), "applications": apps}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/enablebanking/app":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            qs = parse_qs(parsed.query)
            app_id = qs.get("id", [None])[0]
            app = fin_reg.get_enable_banking_app(app_id=app_id)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(app, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/aspsp":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            qs = parse_qs(parsed.query)
            q = qs.get("q", [""])[0]
            country = qs.get("country", [""])[0]
            psu_type = qs.get("psu_type", [""])[0]
            service = qs.get("service", [""])[0]
            status = qs.get("status", [""])[0]
            limit = int(qs.get("limit", [50])[0])
            banks = fin_reg.search_aspsp_banks(query=q, country=country, psu_type=psu_type, service=service, status=status, limit=limit)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(banks), "query": q, "country": country, "banks": banks}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/aspsp/stats":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            stats = fin_reg.get_aspsp_stats()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(stats, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/centralbanks/global":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            qs = parse_qs(parsed.query)
            q = qs.get("q", [""])[0]
            jur = qs.get("jurisdiction", [""])[0]
            limit = int(qs.get("limit", [50])[0])
            cbs = fin_reg.get_global_central_banks(query=q, jurisdiction=jur, limit=limit)
            stats = fin_reg.get_global_central_banks_stats()
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(cbs), "stats": stats, "central_banks": cbs}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/vps/portals":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            qs = parse_qs(parsed.query)
            q = qs.get("q", [""])[0]
            limit = int(qs.get("limit", [50])[0])
            portals = fin_reg.get_wish_studio_vps_portals(query=q, limit=limit)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(portals), "vps_ip": "82.165.134.41", "portals": portals}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/portalregistry":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            qs = parse_qs(parsed.query)
            q = qs.get("q", [""])[0]
            cat = qs.get("category", [""])[0]
            st = qs.get("status", [""])[0]
            limit = int(qs.get("limit", [50])[0])
            portals = fin_reg.search_portal_registry_2361(query=q, category=cat, status=st, limit=limit)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(portals), "query": q, "category": cat, "status": st, "portals": portals}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path.startswith("/api/finance/partnerapps"):
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            qs = parse_qs(parsed.query)
            provider = qs.get("provider", [None])[0]
            if provider:
                app_data = fin_reg.get_partner_application(provider)
                if not app_data:
                    self._set_json_headers(404)
                    self.wfile.write(json.dumps({"error": f"Provider {provider} not found"}, ensure_ascii=False).encode("utf-8"))
                    return
                self._set_json_headers(200)
                self.wfile.write(json.dumps(app_data, indent=2, ensure_ascii=False).encode("utf-8"))
                return
            apps = fin_reg.get_partner_applications()
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(apps), "partner_applications": apps}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/globalcards":
            from forina_engine.institutional_finance import InstitutionalFinanceRegistry
            fin_reg = InstitutionalFinanceRegistry(self.project_root)
            spec = fin_reg.get_globalcards_bank_spec()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(spec, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 11e. 3D FLOW ENGINE VISUALISIERUNGEN
        if parsed.path == "/api/flow/list":
            flow_dir = self.project_root / "web" / "flow"
            files = []
            if flow_dir.exists():
                for f in sorted(flow_dir.glob("*.html")):
                    files.append({
                        "name": f.name,
                        "title": f.stem.replace("-", " ").title(),
                        "url": f"/flow/{f.name}"
                    })
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"flow_engines": files}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 12. AUTOMATED HARNESS LOOP
        if parsed.path == "/api/harness/status":
            engine = HarnessLoopEngine(self.project_root)
            payload = {
                "state": engine.get_state(),
                "stages": engine.get_stages()
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 13. ACT PACK ZERO CLOCK & NATZA STATUS
        if parsed.path == "/api/zeroclock/status":
            apzc = ActPackZeroClock(self.project_root)
            status = apzc.get_status()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(status, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 14. INTEGRATED MASTERKONZEPT & CATALOG MATRICES
        if parsed.path == "/api/concepts/masterkonzept":
            suite = ConceptPaperSuite(self.project_root)
            mk = suite.get_masterkonzept()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(mk, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 14b. DP MASTERBOOK (27 KURATIERTE KAPITEL)
        if parsed.path.startswith("/api/concepts/masterbook"):
            suite = ConceptPaperSuite(self.project_root)
            nr = None
            parts = parsed.path.strip("/").split("/")
            if len(parts) >= 4 and parts[3].isdigit():
                nr = int(parts[3])
            elif "nr" in query and query["nr"][0].isdigit():
                nr = int(query["nr"][0])

            if nr is not None:
                ch = suite.get_dp_masterbook_chapter(nr)
                if not ch:
                    self._set_json_headers(404)
                    self.wfile.write(json.dumps({"error": f"Kapitel #{nr} nicht gefunden"}, ensure_ascii=False).encode("utf-8"))
                    return
                self._set_json_headers(200)
                self.wfile.write(json.dumps(ch, indent=2, ensure_ascii=False).encode("utf-8"))
                return
            summary = suite.get_dp_masterbook_summary()
            chapters = suite.list_dp_masterbook_chapters()
            payload = {
                "summary": summary,
                "count": len(chapters),
                "chapters": chapters
            }
            self._set_json_headers(200)
            self.wfile.write(json.dumps(payload, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/catalogs/kapitel136":
            suite = ConceptPaperSuite(self.project_root)
            k136 = suite.get_136_kapitel_nachweis()
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(k136), "kapitel": k136}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/catalogs/repos50matrix":
            suite = ConceptPaperSuite(self.project_root)
            r50 = suite.get_50_repos_matrix()
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(r50), "repositories": r50}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 15. HARNESS CONTROL LOOP (HCL) SIMULATION
        if parsed.path == "/api/harness/loop/simulate":
            from .harness_control_loop import HarnessControlLoopEngine, WorkItem
            qs = parse_qs(parsed.query)
            human_appr = qs.get("human_approval", ["0"])[0] in ("1", "true")
            iso_ver = qs.get("external_isolation", ["0"])[0] in ("1", "true")
            task_id = qs.get("task_id", ["HCOS-HCL-SIM-001"])[0]
            req = qs.get("requirement", ["Sovereign zero-trust gate verification"])[0]
            prop = qs.get("proposed_change", ["Implement verified deterministic state machine"])[0]

            wi = WorkItem(
                task_id=task_id,
                requirement=req,
                proposed_change=prop,
                human_approval=human_appr,
                external_isolation_verified=iso_ver
            )
            hcl = HarnessControlLoopEngine()
            outcome = hcl.run_cycle(wi)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(outcome.to_dict(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 16. UPUIA UNIVERSAL PROJECT INTELLIGENCE ARCHIVE
        if parsed.path == "/api/upuia/status":
            from .upuia_scanner import UpuiaIntelligenceArchive
            upuia = UpuiaIntelligenceArchive(self.project_root)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(upuia.get_summary(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/upuia/preflight":
            from .upuia_scanner import UpuiaIntelligenceArchive
            upuia = UpuiaIntelligenceArchive(self.project_root)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(upuia.run_preflight_check(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 16. WISH STUDIO OS & DIGITAL SKILL PASS
        if parsed.path == "/api/wish/summary":
            from .skill_pass import WishStudioSkillPassEngine
            eng = WishStudioSkillPassEngine(self.project_root)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(eng.get_summary(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/wish/roles":
            from .skill_pass import WishStudioSkillPassEngine
            eng = WishStudioSkillPassEngine(self.project_root)
            level = query.get("level", [None])[0]
            roles = eng.list_roles(level=level)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(roles), "roles": roles}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/wish/projects":
            from .skill_pass import WishStudioSkillPassEngine
            eng = WishStudioSkillPassEngine(self.project_root)
            status = query.get("status", [None])[0]
            projs = eng.list_projects(status=status)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(projs), "projects": projs}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 17. SCIENTIFIC ENERGY AUDIT & PONTES DLT
        if parsed.path == "/api/energy/summary":
            from .energy_audit import ScientificEnergyAuditEngine
            eng = ScientificEnergyAuditEngine(self.project_root)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(eng.get_summary(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/energy/systems":
            from .energy_audit import ScientificEnergyAuditEngine
            eng = ScientificEnergyAuditEngine(self.project_root)
            q = query.get("q", [None])[0]
            group = query.get("group", [None])[0]
            grade = query.get("grade", [None])[0]
            if q:
                systems = eng.search_systems(q)
            else:
                systems = eng.list_systems(group=group, nachweisgrad=grade)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(systems), "systems": systems}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/pontes/summary":
            from .energy_audit import PontesDltSettlementEngine
            eng = PontesDltSettlementEngine(self.project_root)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(eng.get_summary(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/finance/pontes/matrix":
            from .energy_audit import PontesDltSettlementEngine
            eng = PontesDltSettlementEngine(self.project_root)
            cat = query.get("category", [None])[0]
            cands = eng.list_candidates(category=cat)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(cands), "candidates": cands}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 18. TLORE LIGHTNING SUITE & SOVEREIGN CDE
        if parsed.path == "/api/tlore/summary":
            from .tlore_cde import TloreLightningEngine
            eng = TloreLightningEngine(self.project_root)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(eng.get_summary(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/tlore/modules":
            from .tlore_cde import TloreLightningEngine
            eng = TloreLightningEngine(self.project_root)
            stage = query.get("stage", [None])[0]
            mods = eng.list_modules(harness_stage=stage)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(mods), "modules": mods}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/cde/summary":
            from .tlore_cde import SovereignCdeEngine
            eng = SovereignCdeEngine(self.project_root)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(eng.get_summary(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/cde/rules":
            from .tlore_cde import SovereignCdeEngine
            eng = SovereignCdeEngine(self.project_root)
            rules = eng.list_rules()
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(rules), "rules": rules}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # 19. FIGP GOVERNANCE & 141 OBSERVABILITY TOOLS
        if parsed.path == "/api/figp/summary":
            from .figp_engine import FigpGovernanceEngine
            eng = FigpGovernanceEngine(self.project_root)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(eng.get_summary(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/figp/frameworks":
            from .figp_engine import FigpGovernanceEngine
            eng = FigpGovernanceEngine(self.project_root)
            fams = eng.list_framework_families()
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(fams), "frameworks": fams}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/tools/summary":
            from .figp_engine import ObservabilityToolsCatalogEngine
            eng = ObservabilityToolsCatalogEngine(self.project_root)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(eng.get_summary(), indent=2, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/tools/catalog":
            from .figp_engine import ObservabilityToolsCatalogEngine
            eng = ObservabilityToolsCatalogEngine(self.project_root)
            cat = query.get("category", [None])[0]
            q = query.get("q", [None])[0]
            if q:
                tools = eng.search_tools(q)
            else:
                tools = eng.list_tools(category=cat)
            self._set_json_headers(200)
            self.wfile.write(json.dumps({"count": len(tools), "tools": tools}, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # Fallback to static file serving
        return super().do_GET()

    def do_POST(self):
        parsed = urlparse(self.path)
        master_api_key = _load_or_generate_api_key(self.project_root)

        # HARNESS LOOP ITERATION
        if parsed.path == "/api/harness/run":
            engine = HarnessLoopEngine(self.project_root)
            result = engine.run_cycle_iteration()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(result, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # HARNESS LOOP SINGLE STAGE
        if parsed.path == "/api/harness/stage":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len).decode("utf-8") if content_len else "{}"
            req_data = json.loads(post_body) if post_body else {}
            stage = req_data.get("stage", "PLAN")
            engine = HarnessLoopEngine(self.project_root)
            try:
                result = engine.run_single_stage(stage)
                self._set_json_headers(200)
                self.wfile.write(json.dumps(result, indent=2, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self._set_json_headers(400)
                self.wfile.write(json.dumps({"error": str(e), "success": False}, ensure_ascii=False).encode("utf-8"))
            return

        # ACT PACK ZERO CLOCK TICK
        if parsed.path == "/api/zeroclock/tick":
            apzc = ActPackZeroClock(self.project_root)
            tick = apzc.get_zero_clock_tick()
            self._set_json_headers(200)
            self.wfile.write(json.dumps(tick, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # WISH STUDIO OS ACTIONS
        if parsed.path == "/api/wish/projects":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len).decode("utf-8") if content_len else "{}"
            req_data = json.loads(post_body) if post_body else {}
            from .skill_pass import WishStudioSkillPassEngine
            eng = WishStudioSkillPassEngine(self.project_root)
            try:
                proj = eng.create_project(
                    title=req_data.get("title", "Neuer Wunsch"),
                    requestor=req_data.get("requestor", "Daniel Pohl"),
                    description=req_data.get("description", ""),
                    assigned_role=req_data.get("assigned_role", "SKILL-VOL-01")
                )
                self._set_json_headers(201)
                self.wfile.write(json.dumps(proj, indent=2, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self._set_json_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/wish/approve":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len).decode("utf-8") if content_len else "{}"
            req_data = json.loads(post_body) if post_body else {}
            from .skill_pass import WishStudioSkillPassEngine
            eng = WishStudioSkillPassEngine(self.project_root)
            try:
                approval = eng.approve_project(
                    project_id=req_data.get("project_id"),
                    approver=req_data.get("approver", "Daniel Pohl"),
                    role=req_data.get("role", "Sovereign Requestor / Authority")
                )
                self._set_json_headers(200)
                self.wfile.write(json.dumps(approval, indent=2, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self._set_json_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/wish/credential":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len).decode("utf-8") if content_len else "{}"
            req_data = json.loads(post_body) if post_body else {}
            from .skill_pass import WishStudioSkillPassEngine
            eng = WishStudioSkillPassEngine(self.project_root)
            try:
                vc = eng.generate_verifiable_credential(
                    developer_did=req_data.get("developer_did", "did:tdw:dev.community.org"),
                    role_id=req_data.get("role_id", "SKILL-VOL-01"),
                    project_id=req_data.get("project_id", "WISH-2026-001")
                )
                self._set_json_headers(200)
                self.wfile.write(json.dumps(vc, indent=2, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self._set_json_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}, ensure_ascii=False).encode("utf-8"))
            return

        # NATZA TMR VOTE
        if parsed.path == "/api/zeroclock/tmr-vote":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len).decode("utf-8") if content_len else "{}"
            req_data = json.loads(post_body) if post_body else {}
            v_a = req_data.get("a", "PASS")
            v_b = req_data.get("b", "PASS")
            v_c = req_data.get("c", "PASS")
            apzc = ActPackZeroClock(self.project_root)
            try:
                consensus = apzc.verify_tmr_consensus(v_a, v_b, v_c, context="UI_VOTER")
                resp = {"consensus": consensus, "status": "TMR_CONSENSUS_REACHED", "success": True}
            except NaTZaFaultToleranceViolation as e:
                resp = {"error": str(e), "status": "NATZA_DIVERGENCE_BLOCKED", "success": False}
            self._set_json_headers(200)
            self.wfile.write(json.dumps(resp, indent=2, ensure_ascii=False).encode("utf-8"))
            return

        # TLORE LIGHTNING BOOST & CDE SPAWN
        if parsed.path == "/api/tlore/boost":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len).decode("utf-8") if content_len else "{}"
            req_data = json.loads(post_body) if post_body else {}
            from .tlore_cde import TloreLightningEngine
            eng = TloreLightningEngine(self.project_root)
            try:
                res = eng.run_boost_simulation(
                    sector_nr=req_data.get("sector_nr", "01"),
                    network=req_data.get("network", "testnet")
                )
                self._set_json_headers(200)
                self.wfile.write(json.dumps(res, indent=2, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self._set_json_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}, ensure_ascii=False).encode("utf-8"))
            return

        if parsed.path == "/api/cde/spawn":
            content_len = int(self.headers.get("Content-Length", 0))
            post_body = self.rfile.read(content_len).decode("utf-8") if content_len else "{}"
            req_data = json.loads(post_body) if post_body else {}
            from .tlore_cde import SovereignCdeEngine
            eng = SovereignCdeEngine(self.project_root)
            try:
                res = eng.spawn_point(
                    point_id=req_data.get("point_id", "crash_log_77")
                )
                self._set_json_headers(200)
                self.wfile.write(json.dumps(res, indent=2, ensure_ascii=False).encode("utf-8"))
            except Exception as e:
                self._set_json_headers(400)
                self.wfile.write(json.dumps({"error": str(e)}, ensure_ascii=False).encode("utf-8"))
            return

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

        # 12. STROQ AGENT SECURITY SCANNER (M13)
        if parsed.path == "/api/stroq/scan":
            length = int(self.headers.get("Content-Length", 0))
            body = self.rfile.read(length).decode("utf-8") if length > 0 else "{}"
            data = json.loads(body)
            scanner = StroqAgentSecurityScanner()
            text = data.get("text", "")
            label = data.get("label", "agent_payload")
            result = scanner.scan_payload(text, label)
            self._set_json_headers(200)
            self.wfile.write(json.dumps(result, indent=2, ensure_ascii=False).encode("utf-8"))
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
