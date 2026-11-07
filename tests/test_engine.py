"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
AUTOMATED ENGINE & SPEC-SYNC TESTS
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
import os
import unittest
import json
from pathlib import Path
from forina_engine.spec_sync import SpecSyncEngine
from forina_engine.engine import ForinaTitanEngine
from forina_engine.certification import SovereignCertifier
from forina_engine.agent_orchestrator import AgentOrchestrator
from forina_engine.mcp_gateway import MCPGateway
from forina_engine.knowledge_base import KnowledgeBase
from forina_engine.secrets_manager import SecretsManager
from forina_engine.module_loader import ModuleLoader, ModuleSecurityViolation
from forina_engine.financial_engine import FinancialIntelligenceEngine, SettlementViolationError
from forina_engine.boba_validator import BobaErrorChainValidator, ChainStepVerificationFailed
from forina_engine.stroq_scanner import StroqAgentSecurityScanner, SecurityScannerViolation
from forina_engine.assurance_gates import AssuranceGatePipeline
from forina_engine.repo_catalog import RepositoryEvaluationCatalog
from forina_engine.network_guard import SovereignNetworkGuard, SovereignNetworkViolation
from forina_engine.concept_suite import ConceptPaperSuite
from forina_engine.harness_loop import HarnessLoopEngine
from forina_engine.actpack_zeroclock import ActPackZeroClock, NaTZaFaultToleranceViolation


class TestForinaTitanEngine(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).parent.parent

    def test_ai_agent_orchestrator_and_skills(self):
        orch = AgentOrchestrator(self.root)
        agents = orch.list_agents()
        self.assertEqual(len(agents), 5, "Muss 5 Kern-Agenten bereitstellen")
        skills = orch.list_skills()
        self.assertTrue(len(skills) >= 5, "Muss alle 5 SKILL.md Module laden")
        
        # Test Agent query
        res = orch.query_agent("evidence", "Prüfe Merkle Root")
        self.assertIn("Evidence & Cryptographic Auditor", res["response"])
        self.assertTrue(res["audit_verified"])

    def test_mcp_and_knowledge_base(self):
        mcp = MCPGateway(self.root)
        connectors = mcp.list_connectors()
        self.assertTrue(len(connectors) >= 4)
        diag = mcp.debug_connector("github")
        self.assertEqual(diag["status"], "ONLINE_DIAGNOSTIC_PASS")

        kb = KnowledgeBase(self.root)
        results = kb.search("Compliance")
        self.assertTrue(len(results) > 0)

    def test_secrets_vault_encryption(self):
        sm = SecretsManager(self.root)
        success = sm.set_secret("TEST_TOKEN", "secret-value-123")
        self.assertTrue(success)
        val = sm.get_secret("TEST_TOKEN")
        self.assertEqual(val, "secret-value-123")

    def test_sovereign_certification(self):
        certifier = SovereignCertifier(self.root)
        cert = certifier.generate_certificate(sync_dist=False)
        self.assertEqual(cert["metadata"]["author_and_creator"], "Daniel Pohl")
        self.assertEqual(cert["metadata"]["certifications"]["royal_kaiser_charter_regsys"]["pic"], "867679357")
        self.assertEqual(cert["metadata"]["certifications"]["global_lei"], "894500GBJSIW8L6ET310")
        self.assertTrue(len(cert["cryptographic_signatures"]["ed25519_signature_hex"]) >= 64)
        self.assertTrue(certifier.verify_certificate(cert), "Ed25519 Signatur muss mathematisch verifiziert werden")
        self.assertTrue((self.root / "certificates" / "CERTIFICATE.json").exists())
        self.assertTrue((self.root / "certificates" / "CERTIFICATION.md").exists())

    def test_spec_sync_engine(self):
        sync = SpecSyncEngine(self.root)
        result = sync.verify_all_modules()
        self.assertEqual(result["total_modules"], 8)
        self.assertTrue(result["overall_realized"], "Alle 8 Module muessen als realisiert bewertet werden")
        self.assertEqual(result["overall_percentage"], 100)
        self.assertEqual(len(result["modules"]), 8)
        for mod in result["modules"]:
            self.assertEqual(mod["spec_score"], 100)
            self.assertEqual(mod["light_state"], "blink-green")

    def test_module_loader_and_10_modulgruppen(self):
        loader = ModuleLoader(self.root)
        modules = loader.list_modules()
        self.assertGreaterEqual(len(modules), 10, "Muss mindestens die 10 Modulgruppen laden")

        # Verify all 10 module IDs are present
        expected_10 = [
            "01_agent_studio", "02_workflow_orchestrator", "03_connector_marketplace",
            "04_knowledge_rag", "05_web_discovery", "06_secrets_identity",
            "07_trust_compliance", "08_evidence_audit", "09_monitoring_studio",
            "10_voice_media"
        ]
        found_ids = [m["id"] for m in modules]
        for em in expected_10:
            self.assertIn(em, found_ids, f"Modul {em} muss in der Registry vorhanden sein")

        # Test verification and testing of 01_agent_studio
        v_res = loader.verify_module("01_agent_studio")
        self.assertTrue(v_res["success"])
        t_res = loader.test_module("01_agent_studio")
        self.assertTrue(t_res["success"])
        self.assertEqual(t_res["test_result"]["status"], "PASS")

        # Test execution router
        exec_res = loader.execute_module("01_agent_studio", "list_agents", {})
        self.assertEqual(exec_res["status"], "SUCCESS")
        self.assertTrue(len(exec_res["agents"]) >= 3)

        # Test promote all
        promoted = loader.promote_all_to_freigegeben()
        self.assertEqual(promoted["01_agent_studio"], "Freigegeben")
        summary = loader.get_suite_summary()
        self.assertEqual(summary["lifecycle_breakdown"]["Freigegeben"], len(modules))
        self.assertEqual(summary["production_readiness_percent"], 100.0)

    def test_financial_intelligence_and_zero_settlement(self):
        fin = FinancialIntelligenceEngine()
        analysis = fin.analyze_transactions()
        self.assertEqual(analysis["status"], "ANALYSIS_COMPLETE")
        self.assertTrue(analysis["read_only_mode"])
        self.assertGreater(analysis["estimated_monthly_leak_savings"], 0.0)
        self.assertTrue(len(analysis["findings"]["double_charges"]) > 0)
        self.assertTrue(len(analysis["findings"]["price_creeps"]) > 0)

        # Test Zero-Settlement Guardrail (fail-closed against payment/debit)
        with self.assertRaises(SettlementViolationError):
            fin.assert_zero_settlement("execute_transfer_out")
        with self.assertRaises(SettlementViolationError):
            fin.transfer("DE1234567890", 100)
        with self.assertRaises(SettlementViolationError):
            fin.debit(50)

    def test_boba_error_chain_validator(self):
        boba = BobaErrorChainValidator()
        steps = [
            {"name": "ExtractData", "mock_result": {"status": "OK", "count": 10}, "rules": {"required_keys": ["status"]}},
            {"name": "ComputeMetric", "mock_result": 42.0, "rules": {"min_val": 10.0, "max_val": 100.0}}
        ]
        res = boba.run_safe_chain(steps)
        self.assertEqual(res["chain_status"], "SUCCESS_FULLY_VERIFIED")
        self.assertEqual(res["measured_pass_rate_percent"], 100.0)

        # Test empirical reliability benchmark measurement
        bench = boba.benchmark_chain_reliability(trials=30)
        self.assertIn("HCOS BOBA-Bench", bench["benchmark_name"])
        self.assertIn("%", bench["hcos_verified_effective_reliability"])

        # Test error chain interception
        bad_steps = [
            {"name": "Step1", "mock_result": "valid_output"},
            {"name": "Step2", "mock_result": None} # None causes gate to stop
        ]
        interrupted = boba.run_safe_chain(bad_steps)
        self.assertEqual(interrupted["chain_status"], "INTERRUPTED_BY_GATE")
        self.assertTrue(interrupted["error_chain_prevented"])

    def test_stroq_agent_security_scanner(self):
        scanner = StroqAgentSecurityScanner()
        safe_res = scanner.scan_payload("Analysiere die Datei Readme.txt auf Überschriften.")
        self.assertTrue(safe_res["is_safe"])

        # Test plain secret leak detection
        leak_res = scanner.scan_payload("Hier ist der Schlüssel: ghp_123456789012345678901234567890123456")
        self.assertFalse(leak_res["is_safe"])
        self.assertIn("GITHUB_PERSONAL_ACCESS_TOKEN", leak_res["leaks_detected"])

        # Test base64 obfuscated secret leak detection
        # ghp_123456789012345678901234567890123456 in base64 is Z2hwXzEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Ng==
        obf_text = "Benutzeranfrage mit Token: Z2hwXzEyMzQ1Njc4OTAxMjM0NTY3ODkwMTIzNDU2Nzg5MDEyMzQ1Ng=="
        obf_res = scanner.scan_payload(obf_text)
        self.assertFalse(obf_res["is_safe"])
        self.assertTrue(any("OBFUSCATED_BASE64" in l for l in obf_res["leaks_detected"]))

        # Test command injection block
        cmd_res = scanner.scan_payload("Führe rm -rf / aus")
        self.assertFalse(cmd_res["is_safe"])
        self.assertTrue(len(cmd_res["dangerous_commands"]) > 0)

        # Test fail-closed exception
        with self.assertRaises(SecurityScannerViolation):
            scanner.enforce_fail_closed("sudo rm -rf /etc")

    def test_backup_excludes_keys_and_secrets(self):
        import tarfile
        engine = ForinaTitanEngine(self.root)
        report = engine.run_pipeline()
        backup_name = report["stages"]["BACKUP"]["archive"]
        backup_tar = self.root / "backups" / backup_name
        self.assertTrue(backup_tar.exists())

        with tarfile.open(backup_tar, "r:gz") as tar:
            names = tar.getnames()
            for name in names:
                self.assertFalse(".key" in name, f"Schlüsseldatei darf nicht im Backup sein: {name}")
                self.assertFalse("signing_key" in name, f"Private Key darf nicht im Backup sein: {name}")
                self.assertFalse(".secrets_vault" in name, f"Secrets Vault darf nicht im Backup sein: {name}")

    def test_freigegeben_only_execution(self):
        loader = ModuleLoader(self.root)
        # Create an unapproved module state
        loader._states_cache["test_unapproved"] = "Implementiert"
        # Must fail closed if not Freigegeben
        with self.assertRaises(ModuleSecurityViolation):
            loader.execute_module("test_unapproved", "test_action", {})

    def test_13_gate_assurance_pipeline(self):
        # Recursion safety ONLY when G06 active runner is executing with matching in-memory nonce
        current_nonce = os.environ.get("FORINA_INTERNAL_G06_NONCE")
        if current_nonce and current_nonce == getattr(AssuranceGatePipeline, "_active_g06_nonce", None):
            # Inner invocation from G06 runner: verify gate spec definitions without spawning nested runner
            from forina_engine.assurance_gates import GATES_SPEC
            self.assertEqual(len(GATES_SPEC), 13)
            return

        pipeline = AssuranceGatePipeline(self.root)
        audit = pipeline.audit_all_gates()
        self.assertEqual(audit["total_gates"], 13)
        self.assertEqual(audit["passed_gates"], 13)
        self.assertEqual(audit["overall_status"], "FULL_ASSURANCE_PASSED")

    def test_13_masterkonzept_modules(self):
        loader = ModuleLoader(self.root)
        mods = loader.list_modules()
        m_ids = [m["id"] for m in mods if m["id"].startswith("m")]
        expected_m = [
            "m01_trusted_registry", "m02_secure_builder", "m03_ui_composition",
            "m04_identity_consent", "m05_ai_cost_router", "m06_knowledge_search",
            "m07_domain_trust", "m08_financial_intelligence", "m09_communication_hub",
            "m10_privacy_monitoring", "m11_media_voice", "m12_independent_assurance",
            "m13_agent_security_scanner"
        ]
        for em in expected_m:
            self.assertIn(em, m_ids, f"Masterkonzept Modul {em} muss registriert sein")
            v = loader.verify_module(em)
            self.assertTrue(v["success"])
            t = loader.test_module(em)
            self.assertTrue(t["success"])

    def test_pipeline_build(self):
        engine = ForinaTitanEngine(self.root)
        report = engine.run_pipeline()
        self.assertEqual(report["status"], "SUCCESS")
        self.assertTrue((self.root / "dist" / "index.html").exists())
        self.assertTrue((self.root / "dist" / "styles.css").exists())
        self.assertTrue((self.root / "dist" / "app.js").exists())
        self.assertTrue((self.root / "dist" / "spec-status.json").exists())
        self.assertTrue((self.root / "dist" / "AetherTitan.AppDir" / "AppRun").exists())

    def test_50_repository_evaluation_catalog(self):
        catalog = RepositoryEvaluationCatalog(self.root)
        repos = catalog.list_all()
        self.assertEqual(len(repos), 50, "Muss exakt 50 Open-Source Repositories umfassen")
        summary = catalog.get_summary()
        self.assertEqual(summary["total_repositories"], 50)
        self.assertEqual(summary["sovereign_local_count"], 24)
        self.assertEqual(summary["development_count"], 15)
        self.assertEqual(summary["federation_count"], 11)
        # Check specific entries
        tauri = catalog.get_by_nr(1)
        self.assertEqual(tauri["repository"], "tauri-apps/tauri")
        self.assertEqual(tauri["module_id"], "M02")
        jmap = catalog.get_by_nr(28)
        self.assertEqual(jmap["repository"], "linagora/jmap-client-ts")
        self.assertEqual(jmap["zone"], "Federation & Integration Zone")
        self.assertEqual(jmap["module_id"], "M09")
        boba = catalog.get_by_nr(47)
        self.assertEqual(boba["repository"], "amazon-agi/BOBA-bench")
        self.assertEqual(boba["module_id"], "M12")
        stroq = catalog.get_by_nr(50)
        self.assertEqual(stroq["repository"], "AGGIB/Stroq")
        self.assertEqual(stroq["module_id"], "M13")

        # Validate URL containment and separation of concerns (License vs Audit)
        for r in repos:
            self.assertTrue(r["url_valid"], f"URL für {r['repository']} muss HTTPS-validiert sein")
            self.assertIn("https://", r["url"])
            self.assertIn(r["license_type"], [
                "SPDX_PERMISSIVE", "SPDX_COPYLEFT", "DUAL_SPDX",
                "PROPRIETARY_NO_CHARGE", "COMMUNITY_EVALUATION"
            ])
            self.assertEqual(r["audit_type"], "INTERNAL_ZONE_GOVERNANCE_TIER")

        # Test non-SPDX proprietary distinction (GSAP)
        gsap = catalog.get_by_nr(9)
        self.assertEqual(gsap["license_type"], "PROPRIETARY_NO_CHARGE")
        self.assertIn("Non-SPDX", gsap["license_id"])

    def test_sovereign_network_guard_probes(self):
        # 1. Negative WAN Probes within Scoped Guard
        with SovereignNetworkGuard.sovereign_airgap_scope():
            probe_res = SovereignNetworkGuard.run_airgap_probe_test()
            self.assertTrue(probe_res["passed"])
            self.assertIn("8.8.8.8:53", probe_res["blocked_targets"])
            self.assertIn("1.1.1.1:80", probe_res["blocked_targets"])
            self.assertIn("example.com:443", probe_res["blocked_targets"])

        # 2. Permanent Process-Level Guard Installation and Verification
        SovereignNetworkGuard.install_process_airgap_guard()
        self.assertTrue(SovereignNetworkGuard.is_airgap_active())
        self.assertEqual(os.environ.get("FORINA_AIRGAP_ENFORCED"), "1")
        try:
            probe_res_permanent = SovereignNetworkGuard.run_airgap_probe_test()
            self.assertTrue(probe_res_permanent["passed"])
        finally:
            SovereignNetworkGuard.uninstall_process_airgap_guard()
            self.assertFalse(SovereignNetworkGuard.is_airgap_active())

    def test_g08_strict_dist_fail_closed(self):
        # Verify that G08 fails closed if a dist/ file is missing, without falling back to root
        pipeline = AssuranceGatePipeline(self.root)
        g08_result = pipeline._check_g08_evidence_construction()
        self.assertTrue(g08_result["passed"])
        self.assertIn("0 Rogue Files", g08_result["details"])

    def test_g12_tar_safety_and_100_percent_bit_verification(self):
        import tarfile
        pipeline = AssuranceGatePipeline(self.root)
        
        # Test TarSlip containment helper
        bad_tarinfo = tarfile.TarInfo(name="../../etc/passwd")
        self.assertFalse(pipeline._is_safe_tar_member(bad_tarinfo, self.root / "dist"))
        good_tarinfo = tarfile.TarInfo(name="forina.py")
        self.assertTrue(pipeline._is_safe_tar_member(good_tarinfo, self.root))

        # Test Physical Sandbox Restore with 100% Bit-for-Bit Hash Parity
        g12_result = pipeline._check_g12_postrelease_verification()
        self.assertTrue(g12_result["passed"])
        self.assertIn("100% Bit-for-Bit Hash-Parität", g12_result["details"])
        self.assertGreaterEqual(g12_result["files_hash_verified"], 100)

    def test_34_concept_papers_suite(self):
        suite = ConceptPaperSuite(self.root)
        papers = suite.list_papers()
        self.assertEqual(len(papers), 34, "Muss exakt 34 Concept Papers umfassen")
        summary = suite.get_summary()
        self.assertEqual(summary["total_papers"], 34)
        self.assertEqual(summary["total_standards"], 14)

        # Check all 34 concept papers have verified markdown files
        for nr in range(1, 35):
            p = suite.get_paper_content(nr)
            self.assertIsNotNone(p, f"Paper #{nr} muss geladen werden können")
            self.assertTrue(p.get("file_found", False), f"Paper #{nr} Datei muss auf Disk existieren ({p.get('file')})")
            self.assertGreater(len(p.get("content", "")), 500, f"Paper #{nr} muss substantiellen Inhalt haben")

        # Check Papers #4 (IA) and #5 (XD)
        p4 = suite.get_paper(4)
        self.assertIn("Intelligent Automation", p4["title"])
        self.assertEqual(p4["code"], "IA, RPA, AGT")
        p5 = suite.get_paper(5)
        self.assertIn("eXperience Design", p5["title"])
        self.assertEqual(p5["code"], "XD, UX, UI")

        # Check Paper #34 (Anhang Glossar)
        p34 = suite.get_paper_content(34)
        self.assertIn("33+ Schlüssel-Abkürzungen", p34["content"])
        self.assertIn("33+ Kern-Keywords", p34["content"])

        # Check search functionality
        search_res = suite.search_papers("Zero-Trust")
        self.assertGreaterEqual(len(search_res), 1)
        self.assertEqual(search_res[0]["nr"], 9)

    def test_automated_harness_loop_lifecycle(self):
        harness = HarnessLoopEngine(self.root)
        stages = harness.get_stages()
        self.assertEqual(len(stages), 8, "Muss exakt 8 Harness-Loop Stufen besitzen")
        stage_ids = [s["id"] for s in stages]
        expected_ids = ["PLAN", "BUILD", "TEST", "AUDIT", "CERTIFY", "RELEASE", "MONITOR", "IMPROVE"]
        self.assertEqual(stage_ids, expected_ids)

        # Test single stage execution
        res_plan = harness.run_single_stage("PLAN")
        self.assertEqual(res_plan["stage_id"], "PLAN")
        self.assertEqual(res_plan["result"]["status"], "PASS")
        self.assertEqual(res_plan["updated_state"]["current_stage"], "BUILD")

        state = harness.get_state()
        self.assertIn("cycle_id", state)

    def test_actpack_zeroclock_and_natza_cfs(self):
        apzc = ActPackZeroClock(self.root)

        # 1. Monotonic Zero-Clock Ticks
        t1 = apzc.get_zero_clock_tick()
        t2 = apzc.get_zero_clock_tick()
        self.assertEqual(t1["tick"], 1)
        self.assertEqual(t2["tick"], 2)
        self.assertNotEqual(t1["block_hash"], t2["block_hash"])
        self.assertEqual(t1["synchronization_status"], "SYNCHRONIZED")

        # 2. NaTZa Triple Modular Redundancy (TMR) Voter Consensus
        consensus_val = apzc.verify_tmr_consensus("HASH_A", "HASH_A", "HASH_B")
        self.assertEqual(consensus_val, "HASH_A")
        
        # Test divergence fail-closed
        with self.assertRaises(NaTZaFaultToleranceViolation):
            apzc.verify_tmr_consensus("HASH_A", "HASH_B", "HASH_C")

        # 3. Devin Sub-Spawning with WhyTrace
        task = apzc.spawn_subagent_task("agent_master", "micro_audit", {"target": "m08_finance"})
        self.assertIn("whytrace_", task["trace_id"])
        self.assertEqual(task["status"], "PROVISIONED_SANDBOX")

    def test_144_seiten_enzyklopaedie_and_baende(self):
        suite = ConceptPaperSuite(self.root)
        baende = suite.list_baende()
        self.assertEqual(len(baende), 4, "Muss exakt 4 Bände (A, B, C, D) umfassen")
        for b in baende:
            self.assertTrue(b["exists"], f"Band {b['band']} muss physisch existieren")
            self.assertGreater(b["bytes"], 100000, f"Band {b['band']} muss substanziellen Volltext haben (>100KB)")

        band_a = suite.get_band_content("A")
        self.assertIsNotNone(band_a)
        self.assertIn("Band A", band_a["title"])

        themen = suite.get_136_themen()
        self.assertEqual(len(themen), 4)
        total_kap = sum(len(v) for v in themen.values())
        self.assertEqual(total_kap, 136, "Muss exakt 136 Fachkapitel umfassen")

        spec = suite.list_specialized_papers()
        self.assertGreaterEqual(len(spec), 3)

    def test_34_normen_svg_badges_registry(self):
        from forina_engine.audit_badges import AuditBadgeRegistry
        reg = AuditBadgeRegistry(self.root)
        badges = reg.list_badges()
        self.assertEqual(len(badges), 34, "Muss exakt 34 Vektor-SVG-Badges verifizieren")
        
        # Verify first badge NORM-001
        b1 = badges[0]
        self.assertEqual(b1["norm_id"], "NORM-001")
        self.assertIn("DSGVO", b1["title"])
        self.assertTrue(b1["verified"])
        self.assertEqual(len(b1["sha256"]), 64)

        svg = reg.get_badge_svg("NORM-001")
        self.assertIsNotNone(svg)
        self.assertIn("<svg", svg)

    def test_institutional_finance_registry(self):
        from forina_engine.institutional_finance import InstitutionalFinanceRegistry
        fin = InstitutionalFinanceRegistry(self.root)
        banks = fin.get_central_banks()
        self.assertGreaterEqual(len(banks), 6)
        ezb = next((b for b in banks if b["id"] == "EZB"), None)
        self.assertIsNotNone(ezb)
        self.assertIn("TARGET2", ezb["clearing_systems"])

        providers = fin.get_open_banking_providers()
        self.assertGreaterEqual(len(providers), 8)
        self.assertTrue(all(p["read_only"] for p in providers), "Open Banking muss strikt read-only sein")

        schemas = fin.get_iso20022_message_schemas()
        self.assertGreaterEqual(len(schemas), 5)

        pontes = fin.get_pontes_spec()
        self.assertIn("Pontes", pontes["protocol"])
        self.assertEqual(pontes["official_launch"], "2026-09-21 (Q3 2026)")
        self.assertTrue(len(pontes["key_capabilities"]) >= 4)

        portals = fin.search_portals(query="Aave")
        self.assertGreaterEqual(len(portals), 1)
        self.assertEqual(portals[0]["Name"], "Aave")

        clevel = fin.get_clevel_directory(company_filter="Binance")
        self.assertGreaterEqual(len(clevel), 1)
        self.assertTrue(any("Richard Teng" in c["Name"] for c in clevel))

    def test_enable_banking_and_aspsp_catalog(self):
        from forina_engine.institutional_finance import InstitutionalFinanceRegistry
        fin = InstitutionalFinanceRegistry(self.root)

        # Test Enable Banking apps
        apps = fin.get_enable_banking_apps()
        self.assertGreaterEqual(len(apps), 3)
        active_app = fin.get_enable_banking_app()
        self.assertEqual(active_app["app_name"], "aether.worldbankeyes.eu")
        self.assertEqual(active_app["app_id"], "85550b82-143d-4b06-9aa1-d33c73584984")
        self.assertEqual(active_app["environment"], "SANDBOX")
        self.assertIn("Account Information", active_app["services"])
        self.assertIn("Payment Initiation", active_app["services"])
        self.assertIn("LOCAL_CONFIG_UMASK_077", active_app["key_storage"])

        # Test ASPSP catalog stats
        stats = fin.get_aspsp_stats()
        self.assertEqual(stats["unique_brands"], 1128, "Muss exakt 1.128 unique Banken umfassen")
        self.assertEqual(stats["countries_count"], 29, "Muss 29 europäische Länder umfassen")
        self.assertIn("DE", stats["countries"])
        self.assertIn("AT", stats["countries"])
        self.assertIn("FR", stats["countries"])

        # Test Search
        sparkassen = fin.search_aspsp_banks(query="Sparkasse", country="DE", limit=10)
        self.assertGreaterEqual(len(sparkassen), 5)
        self.assertTrue(all(b["country"] == "DE" for b in sparkassen))
        self.assertTrue(any("Berliner Sparkasse" in b["brand"] for b in sparkassen))

    def test_integrated_masterkonzept_and_catalogs(self):
        suite = ConceptPaperSuite(self.root)
        mk = suite.get_masterkonzept()
        self.assertTrue(mk["size"] > 100000, "Masterkonzept muss >100KB sein")
        self.assertEqual(len(mk["sha256"]), 64)
        self.assertIn("HCOS FORINA TITAN ENGINE", mk["content"])
        self.assertIn("Integriertes Masterkonzept", mk["content"])

        k136 = suite.get_136_kapitel_nachweis()
        self.assertEqual(len(k136), 136, "Muss exakt 136 Kapitel im Nachweisregister haben")

        r50 = suite.get_50_repos_matrix()
        self.assertEqual(len(r50), 50, "Muss 50 Repositories in der Quellenmatrix haben")

        specs = suite.list_specialized_papers()
        self.assertEqual(len(specs), 26, "Muss alle 26 spezialisierten Papiere erfassen")

    def test_upuia_engine_integration(self):
        from forina_engine.upuia_scanner import UpuiaIntelligenceArchive
        upuia = UpuiaIntelligenceArchive(self.root)
        pf = upuia.run_preflight_check()
        self.assertTrue(pf["preflight_passed"])
        summ = upuia.get_summary()
        self.assertEqual(summ["status"], "OPERATIONAL_OFFLINE")
        self.assertIn("10/10 Grundregeln", summ["security_directiv_compliance"])

    def test_wish_studio_repository_catalog(self):
        from forina_engine.repo_catalog import RepositoryEvaluationCatalog
        cat = RepositoryEvaluationCatalog(self.root)
        wish = cat.get_wish_studio_catalog()
        self.assertEqual(len(wish), 18, "Muss exakt 18 Wish Studio Repositories laden")
        fider = next((r for r in wish if r["projekt"] == "Fider"), None)
        self.assertIsNotNone(fider)
        self.assertEqual(fider["repository"], "getfider/fider")
        self.assertEqual(fider["bereich"], "Wunschportal & Support")

    def test_global_central_banks_and_vps_portals(self):
        from forina_engine.institutional_finance import InstitutionalFinanceRegistry
        fin = InstitutionalFinanceRegistry(self.root)

        # Test Global Central Banks (202 sovereign entities)
        stats = fin.get_global_central_banks_stats()
        self.assertEqual(stats["total_sovereign_central_banks"], 202)
        switzerland = fin.get_global_central_banks(query="Schweiz")
        self.assertEqual(len(switzerland), 1)
        self.assertIn("Schweizerische Nationalbank", switzerland[0]["central_bank"])

        japan = fin.get_global_central_banks(jurisdiction="Japan")
        self.assertGreaterEqual(len(japan), 1)

        # Test Wish Studio 34 VPS Portals
        vps = fin.get_wish_studio_vps_portals()
        self.assertEqual(len(vps), 34, "Muss 34 VPS Portale umfassen")
        gitopia = fin.get_wish_studio_vps_portals(query="gitopia")
        self.assertGreaterEqual(len(gitopia), 5)

    def test_portal_registry_and_partner_applications(self):
        from forina_engine.institutional_finance import InstitutionalFinanceRegistry
        fin = InstitutionalFinanceRegistry(self.root)

        # 1. Master Portal Registry (2.361 Portale)
        portals = fin.search_portal_registry_2361(query="Visa")
        self.assertGreaterEqual(len(portals), 1)
        self.assertIn("Visa", portals[0]["Name"])

        # 2. Partner Application Dossiers (9 Partner)
        apps = fin.get_partner_applications()
        self.assertEqual(len(apps), 9, "Muss exakt 9 vorbereitete Partner-Anträge umfassen")
        providers = [a["provider"] for a in apps]
        self.assertIn("Mastercard", providers)
        self.assertIn("Visa", providers)
        self.assertIn("Solaris", providers)
        self.assertIn("Unit", providers)
        self.assertIn("Synctera", providers)
        self.assertIn("Highnote", providers)
        self.assertIn("Enfuce", providers)
        self.assertIn("ClearBank", providers)
        self.assertIn("EnableBanking", providers)

        # 3. Single Provider Application Check
        mc = fin.get_partner_application("Mastercard")
        self.assertIsNotNone(mc)
        self.assertEqual(mc["payload"].get("application_id"), "app_e3f999bb97")
        self.assertIn("Mastercard Engage", mc["payload"].get("program", ""))

        # 4. GlobalCards Bank Specification
        gc = fin.get_globalcards_bank_spec()
        self.assertEqual(len(gc["modules"]), 12, "Muss 12 GlobalCards Entwicklungsmodule enthalten")
        self.assertTrue(gc["spec_available"])
        self.assertGreater(gc["spec_size_bytes"], 100000)

    def test_loccp_repositories_and_compliance_pruefpunkte(self):
        from forina_engine.repo_catalog import RepositoryEvaluationCatalog
        cat = RepositoryEvaluationCatalog(self.root)

        # 1. LOCCP Masterkatalog Stats (352 Repos, 42 Prüfpunkte, 911 URLs)
        stats = cat.get_loccp_stats()
        self.assertEqual(stats["total_loccp_repositories"], 352)
        self.assertEqual(stats["total_compliance_pruefpunkte"], 42)
        self.assertEqual(stats["total_registered_urls"], 911)
        self.assertGreaterEqual(len(stats["categories"]), 30)

        # 2. Search Repos
        actual = cat.get_loccp_repo_catalog(query="actual")
        self.assertGreaterEqual(len(actual), 1)
        self.assertEqual(actual[0]["Projekt/Tool"], "Actual Budget")

        # 3. 42 Prüfpunkte
        all_pts = cat.get_loccp_pruefpunkte()
        self.assertEqual(len(all_pts), 42)
        corp_pts = cat.get_loccp_pruefpunkte(compliance_module="Corporate")
        self.assertEqual(len(corp_pts), 6)

        # 4. Wish OS Compliance Attestation & Badge
        badge = self.root / "web" / "badges" / "WISH_OS_COMPLIANCE_DOCUMENTED.svg"
        self.assertTrue(badge.exists())
        self.assertIn("<svg", badge.read_text(encoding="utf-8"))

        attestation = self.root / "docs" / "compliance" / "WISH_OS_LOCAL_FINANCE_COMPLIANCE_ATTESTATION.md"
        self.assertTrue(attestation.exists())
        self.assertIn("Wish OS Local Finance Stack", attestation.read_text(encoding="utf-8"))

    def test_dp_masterbook_integration(self):
        from forina_engine.concept_suite import ConceptPaperSuite
        suite = ConceptPaperSuite(self.root)

        # 1. Summary
        summary = suite.get_dp_masterbook_summary()
        self.assertEqual(summary["total_curated_chapters"], 27)
        self.assertGreaterEqual(summary["total_words"], 16000)
        self.assertEqual(summary["status"], "APPROVED_SOVEREIGN_META_PUBLICATION")
        self.assertEqual(summary["license"], "EUPL-1.2")
        self.assertIn("Daniel Pohl", summary["author"])

        # 2. Chapters list
        chapters = suite.list_dp_masterbook_chapters()
        self.assertEqual(len(chapters), 27)
        self.assertEqual(chapters[0]["nr"], 1)
        self.assertIn("PNIA", chapters[0]["title"])
        self.assertEqual(chapters[-1]["nr"], 27)
        self.assertIn("Resonanz-Kommunikationsprotokoll", chapters[-1]["title"])

        # 3. Chapter 1 retrieval
        ch1 = suite.get_dp_masterbook_chapter(1)
        self.assertIsNotNone(ch1)
        self.assertEqual(ch1["nr"], 1)
        self.assertIn("Production Network ID Architecture", ch1["content"])
        self.assertGreaterEqual(ch1["words"], 800)

        # 4. CSV Catalog Verification
        csv_path = self.root / "docs" / "catalogs" / "DP_MASTERBOOK_27_KAPITEL.csv"
        self.assertTrue(csv_path.exists())
        lines = [line.strip() for line in csv_path.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(lines), 28, "Header + 27 Datenzeilen")

        # 5. Core Masterbook documentation files
        self.assertTrue((self.root / "docs" / "dp_masterbook" / "INDEX.md").exists())
        self.assertTrue((self.root / "docs" / "dp_masterbook" / "MASTERPLAN.md").exists())

    def test_wish_studio_skill_pass_and_human_approval(self):
        from forina_engine.skill_pass import WishStudioSkillPassEngine
        eng = WishStudioSkillPassEngine(self.root)

        # 1. Summary
        summ = eng.get_summary()
        self.assertEqual(summ["total_defined_roles"], 10)
        self.assertGreaterEqual(summ["total_wish_projects"], 3)
        self.assertTrue(summ["gate_g09_enforced"])
        self.assertTrue(summ["w3c_did_compatible"])
        self.assertTrue(summ["swiss_swiyu_ready"])
        self.assertIn("Daniel Pohl", summ["governance"])

        # 2. Roles Catalog
        roles = eng.list_roles()
        self.assertEqual(len(roles), 10)
        titan_roles = eng.list_roles(level="Titan")
        self.assertEqual(len(titan_roles), 3)

        # 3. W3C Verifiable Credential Generation
        vc = eng.generate_verifiable_credential("did:tdw:volunteer.community.eu:pohl", "SKILL-VOL-08", "WISH-2026-001")
        self.assertIn("VerifiableCredential", vc["type"])
        self.assertIn("CivicDeveloperSkillPass", vc["type"])
        self.assertIn("Daniel Pohl", vc["issuer"]["name"])
        self.assertEqual(vc["credentialSubject"]["competenceLevel"], "TITAN")
        self.assertEqual(vc["proof"]["type"], "Ed25519Signature2020")

        # 4. Human Approval Workflow (Gate G09)
        new_proj = eng.create_project(title="Test Feature Wunsch", description="Automatischer Sandbox-Test")
        self.assertEqual(new_proj["status"], "DRAFT")
        approval = eng.approve_project(new_proj["id"], approver="Daniel Pohl", role="Sovereign Requestor / Authority")
        self.assertEqual(approval["decision"], "APPROVED")
        self.assertEqual(approval["gate_reference"], "G09_SOVEREIGN_APPROVAL")

        # 5. Architecture Paper 06 & CSV Catalog
        arch6 = self.root / "docs" / "concept_papers" / "specialized" / "Architecture_06_Wish_Studio_Skill_Pass_Human_Approval.md"
        self.assertTrue(arch6.exists())
        self.assertGreater(arch6.stat().st_size, 5000)

        csv_roles = self.root / "docs" / "catalogs" / "WISH_STUDIO_SKILL_PASS_ROLES.csv"
        self.assertTrue(csv_roles.exists())
        lines = [line.strip() for line in csv_roles.read_text(encoding="utf-8").splitlines() if line.strip()]
        self.assertEqual(len(lines), 11, "Header + 10 Rollen")

    def test_scientific_energy_audit_and_pontes_dlt(self):
        from forina_engine.energy_audit import ScientificEnergyAuditEngine, PontesDltSettlementEngine

        # 1. Energy Audit Engine
        ea = ScientificEnergyAuditEngine(self.root)
        summ = ea.get_summary()
        self.assertEqual(summ["total_systems"], 100)
        self.assertEqual(summ["groups_count"], 8)
        self.assertIn("Fusion & Plasma", summ["groups_breakdown"])
        self.assertIn("Daniel Pohl", summ["governance"])

        all_sys = ea.list_systems()
        self.assertEqual(len(all_sys), 100)

        fusion_sys = ea.list_systems(group="Fusion")
        self.assertEqual(len(fusion_sys), 15)

        tokamak_search = ea.search_systems("Tokamak")
        self.assertGreaterEqual(len(tokamak_search), 5)

        sys1 = ea.get_system_by_nr(1)
        self.assertIsNotNone(sys1)
        self.assertEqual(sys1["System"], "ITER")
        self.assertEqual(sys1["Wert"], "500")

        # 2. Pontes DLT Settlement Engine
        pont = PontesDltSettlementEngine(self.root)
        p_summ = pont.get_summary()
        self.assertEqual(p_summ["total_candidates"], 25)
        self.assertIn("Eurosystem Core", p_summ["categories"])

        cands = pont.list_candidates()
        self.assertEqual(len(cands), 25)

        c1 = pont.get_candidate("PONT-001")
        self.assertIsNotNone(c1)
        self.assertEqual(c1["Projekt"], "Pontes")
        self.assertIn("TARGET", c1["Recherchefrage"])

        c3 = pont.get_candidate("PONT-003")
        self.assertIsNotNone(c3)
        self.assertEqual(c3["Projekt"], "Trigger Solution")

        # 3. Catalog and Documentation Files Verification
        csv_energy = self.root / "docs" / "catalogs" / "TOP100_ENERGIE_TECHNOLOGIE_AUDIT.csv"
        self.assertTrue(csv_energy.exists())
        e_lines = [l.strip() for l in csv_energy.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual(len(e_lines), 101, "Header + 100 Zeilen")

        csv_pontes = self.root / "docs" / "catalogs" / "EZB_PONTES_DLT_RECHERCHEMATRIX.csv"
        self.assertTrue(csv_pontes.exists())
        p_lines = [l.strip() for l in csv_pontes.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual(len(p_lines), 26, "Header + 25 Zeilen")

        arch7 = self.root / "docs" / "concept_papers" / "specialized" / "Architecture_07_EZB_Pontes_DLT_Wholesale_Settlement.md"
        self.assertTrue(arch7.exists())
        self.assertGreater(arch7.stat().st_size, 3000)

        res1 = self.root / "docs" / "concept_papers" / "specialized" / "Research_01_Top100_Scientific_Energy_Audit_Matrix.md"
        self.assertTrue(res1.exists())
        self.assertGreater(res1.stat().st_size, 3000)

    def test_sovereign_cde_and_tlore_lightning_modules(self):
        from forina_engine.tlore_cde import SovereignCdeEngine, TloreLightningEngine

        # 1. Sovereign CDE Engine
        cde = SovereignCdeEngine(self.root)
        cde_summ = cde.get_summary()
        self.assertEqual(cde_summ["rules_count"], 4)
        self.assertTrue(cde_summ["point_start_ready"])
        self.assertTrue(cde_summ["spec_available"])
        self.assertIn("Daniel Pohl", cde_summ["governance"])

        rules = cde.list_rules()
        self.assertEqual(len(rules), 4)
        self.assertEqual(rules[0]["Regel_Nr"], "CDE-RULE-01")

        spawn = cde.spawn_point("crash_log_77")
        self.assertEqual(spawn["status"], "POINT_AWAKENED")
        self.assertLess(spawn["restore_latency_ms"], 10.0)
        self.assertTrue(spawn["vfs_streaming_active"])

        # 2. TLORE Lightning Engine
        tlore = TloreLightningEngine(self.root)
        t_summ = tlore.get_summary()
        self.assertEqual(t_summ["total_modules"], 44)
        self.assertEqual(t_summ["mode"], "SYNTHETIC_READ_ONLY")
        self.assertTrue(t_summ["spec_available"])

        mods = tlore.list_modules()
        self.assertEqual(len(mods), 44)

        m1 = tlore.get_module("01")
        self.assertIsNotNone(m1)
        self.assertEqual(m1["Name"], "Gitopia Chain Identity")

        m44 = tlore.get_module("44")
        self.assertIsNotNone(m44)
        self.assertEqual(m44["Name"], "Independent Audit and Evidence")

        boost = tlore.run_boost_simulation("01")
        self.assertEqual(boost["mode"], "synthetic_read_only")
        self.assertTrue(boost["live_trades_blocked"])
        self.assertEqual(len(boost["harness_steps"]), 8)

        # 3. File & Catalog Verifications
        csv_tlore = self.root / "docs" / "catalogs" / "TLORE_44_FINANCE_MODULES.csv"
        self.assertTrue(csv_tlore.exists())
        t_lines = [l.strip() for l in csv_tlore.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual(len(t_lines), 45, "Header + 44 Zeilen")

        csv_cde = self.root / "docs" / "catalogs" / "SOVEREIGN_CDE_RULES.csv"
        self.assertTrue(csv_cde.exists())
        c_lines = [l.strip() for l in csv_cde.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual(len(c_lines), 5, "Header + 4 Zeilen")

        arch8 = self.root / "docs" / "concept_papers" / "specialized" / "Architecture_08_Sovereign_CDE_Point_Start_Userspace.md"
        self.assertTrue(arch8.exists())
        self.assertGreater(arch8.stat().st_size, 3000)

        arch9 = self.root / "docs" / "concept_papers" / "specialized" / "Architecture_09_TLORE_44_Lightning_Power_Finance_Suite.md"
        self.assertTrue(arch9.exists())
        self.assertGreater(arch9.stat().st_size, 3000)

    def test_figp_and_observability_141_tools_catalog(self):
        from forina_engine.figp_engine import FigpGovernanceEngine, ObservabilityToolsCatalogEngine
        figp = FigpGovernanceEngine(self.root)
        summ_figp = figp.get_summary()
        self.assertEqual(summ_figp["total_framework_families"], 12)
        self.assertTrue(summ_figp["fail_closed_launcher_enforced"])
        self.assertTrue(summ_figp["schema_available"])
        self.assertTrue(summ_figp["api_spec_available"])

        frameworks = figp.list_framework_families()
        self.assertEqual(len(frameworks), 12)
        bsi = next((f for f in frameworks if "bsi" in f.get("Family_ID", "").lower()), None)
        self.assertIsNotNone(bsi)
        self.assertEqual(bsi["Family_ID"], "FIGP-BSI-01")

        tools = ObservabilityToolsCatalogEngine(self.root)
        summ_tools = tools.get_summary()
        self.assertEqual(summ_tools["total_tools"], 141)
        self.assertGreaterEqual(summ_tools["categories_count"], 14)

        all_tools = tools.list_tools()
        self.assertEqual(len(all_tools), 141)

        search_opencode = tools.search_tools("OpenCode")
        self.assertEqual(len(search_opencode), 1)
        self.assertEqual(search_opencode[0]["Name"], "OpenCode")

        # Verify files on disk
        csv_tools = self.root / "docs" / "catalogs" / "OBSERVABILITY_141_TOOLS_CATALOG.csv"
        self.assertTrue(csv_tools.exists())
        lines_tools = [l.strip() for l in csv_tools.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual(len(lines_tools), 142, "Header + 141 Tools")

        csv_figp = self.root / "docs" / "catalogs" / "FIGP_GOVERNANCE_ENTITIES.csv"
        self.assertTrue(csv_figp.exists())
        lines_figp = [l.strip() for l in csv_figp.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual(len(lines_figp), 13, "Header + 12 Frameworks")

        schema_sql = self.root / "docs" / "schemas" / "FIGP_Reference_Schema.sql"
        self.assertTrue(schema_sql.exists())
        self.assertGreater(schema_sql.stat().st_size, 1000)

        schema_yaml = self.root / "docs" / "schemas" / "FIGP_API_v1.yaml"
        self.assertTrue(schema_yaml.exists())
        self.assertGreater(schema_yaml.stat().st_size, 1000)

        arch10 = self.root / "docs" / "concept_papers" / "specialized" / "Architecture_10_FIGP_UFCIE_Framework_Intelligence_Platform.md"
        self.assertTrue(arch10.exists())
        self.assertGreater(arch10.stat().st_size, 3000)

    def test_state_sovereign_containment_and_cdp_livesync(self):
        from forina_engine.containment_pipeline import StateSovereignContainmentEngine, CdpLiveSyncAutomationEngine
        cont = StateSovereignContainmentEngine(self.root)
        summ_c = cont.get_summary()
        self.assertEqual(summ_c["total_spec_entries"], 17)
        self.assertTrue(summ_c["hardware_pipeline_verified"])
        self.assertTrue(summ_c["containment_enforced"])
        self.assertTrue(summ_c["killswitches_ready"])
        self.assertTrue(summ_c["fail_closed_active"])

        # Hardware pipeline
        hw = cont.verify_hardware_pipeline()
        self.assertEqual(hw["status"], "VERIFIED")
        self.assertEqual(hw["layers_count"], 4)
        self.assertIn("TPM 2.0", hw["root_of_trust"])

        # Containment controls
        ctrl = cont.verify_containment_controls()
        self.assertEqual(ctrl["status"], "ENFORCED")
        self.assertEqual(ctrl["controls_count"], 6)

        # Agentic loop breaker
        ok_loop = cont.evaluate_agentic_loop(iterations=5, token_count=10000, human_approved=False)
        self.assertTrue(ok_loop["allowed"])
        self.assertEqual(ok_loop["action"], "PROCEED")

        blocked_loop = cont.evaluate_agentic_loop(iterations=15, token_count=120000, human_approved=False)
        self.assertFalse(blocked_loop["allowed"])
        self.assertEqual(blocked_loop["action"], "SIGKILL_TERMINATION_AND_MEMORY_FREEZE")
        self.assertTrue(blocked_loop["fail_closed_triggered"])

        approved_loop = cont.evaluate_agentic_loop(iterations=15, token_count=120000, human_approved=True)
        self.assertTrue(approved_loop["allowed"])
        self.assertTrue(approved_loop["human_approved"])

        # Killswitch
        ks = cont.trigger_emergency_killswitch("K1-HW-KILLSWITCH")
        self.assertEqual(ks["status"], "EXECUTED_FAIL_CLOSED")
        self.assertTrue(ks["tpm_revoked"])
        self.assertTrue(ks["gpu_kernel_blocked"])

        # Audit form 99X
        form = cont.get_audit_form_99x()
        self.assertEqual(form["form_id"], "AUDITREQ-99X")
        self.assertEqual(form["certificate_id"], "#8849-AF-2026-GOV-SEC-MULTI-LAYER")

        # CDP LiveSync Engine
        cdp = CdpLiveSyncAutomationEngine(self.root)
        summ_cdp = cdp.get_summary()
        self.assertEqual(summ_cdp["total_components"], 8)
        self.assertTrue(summ_cdp["condensation_active"])
        self.assertTrue(summ_cdp["fail_closed_enforced"])

        # Livelink condensation
        sim = cdp.simulate_livelink_condensation(raw_html_size_bytes=1000000, dom_node_count=1500)
        self.assertEqual(sim["status"], "CONDENSED_SUCCESS")
        self.assertEqual(sim["compression_ratio"], "88.0%")
        self.assertLess(sim["condensed_token_estimate"], sim["raw_token_estimate"])

        # KYC prerequisites
        kyc = cdp.verify_portal_kyc_prerequisites()
        self.assertEqual(kyc["status"], "READY_FOR_PORTAL_AUTOMATION")
        self.assertEqual(kyc["cdp_port"], 9222)
        self.assertIn("867679357", kyc["sovereign_identity"]["pic_eu"])

        # File presence
        csv_cont = self.root / "docs" / "catalogs" / "KI_EINKESSELUNG_SICHERHEITS_SCHICHTEN.csv"
        self.assertTrue(csv_cont.exists())
        c_lines = [l.strip() for l in csv_cont.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual(len(c_lines), 18, "Header + 17 Kontrollen")

        csv_cdp = self.root / "docs" / "catalogs" / "CDP_MCP_PORTAL_AUTOMATION_SPECS.csv"
        self.assertTrue(csv_cdp.exists())
        cdp_lines = [l.strip() for l in csv_cdp.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual(len(cdp_lines), 9, "Header + 8 Komponenten")

        arch11 = self.root / "docs" / "concept_papers" / "specialized" / "Architecture_11_Staatliche_Sicherheits_KI_Einkesselung_Spezifikation.md"
        self.assertTrue(arch11.exists())
        self.assertGreater(arch11.stat().st_size, 3000)

        arch12 = self.root / "docs" / "concept_papers" / "specialized" / "Architecture_12_CDP_LiveSync_MCP_DevinAI_Portal_Automation.md"
        self.assertTrue(arch12.exists())
        self.assertGreater(arch12.stat().st_size, 3000)

    def test_flow_engine_and_code_review_stack(self):
        from forina_engine.flow_and_review import FlowEngineSpectralSettlement, CodeReviewSecurityStackEngine
        flow = FlowEngineSpectralSettlement(self.root)
        summ_f = flow.get_summary()
        self.assertEqual(summ_f["total_matrix_elements"], 16)
        self.assertTrue(summ_f["web_asset_available"])
        self.assertEqual(summ_f["loop_state"], "OPERATIONAL_REALTIME")
        self.assertTrue(summ_f["fail_closed_guaranteed"])

        # Simulation
        sim = flow.simulate_sensor_frame(spectral_energy=0.95, mouse_angular_speed=15.0, cpu_load=0.3)
        self.assertEqual(sim["status"], "FRAME_PROCESSED_SUCCESS")
        self.assertGreaterEqual(sim["triggered_events_count"], 3)
        self.assertGreaterEqual(sim["settlements_executed_count"], 2)
        self.assertTrue(sim["loop_closed"])

        # Web asset check
        asset_info = flow.get_visualization_asset_info()
        self.assertTrue(asset_info["available"])
        self.assertEqual(asset_info["raster_images_contained"], 0)
        self.assertTrue(asset_info["zero_image_compliant"])

        # Code Review Stack
        review = CodeReviewSecurityStackEngine(self.root)
        summ_r = review.get_summary()
        self.assertEqual(summ_r["total_tools"], 20)
        self.assertEqual(len(summ_r["assurance_gates_integrated"]), 5)

        # Policy evaluation
        pol = review.evaluate_pr_policies()
        self.assertEqual(pol["status"], "PR_REVIEW_POLICY_PASSED")
        self.assertEqual(pol["total_tools_verified"], 20)
        self.assertEqual(pol["fail_closed_policy"], "STRICT_ENFORCEMENT")
        self.assertIn("Semgrep", pol["gate_mappings"]["G01_LICENSE_AND_THREAT"])
        self.assertIn("PR-Agent", pol["gate_mappings"]["G09_SOVEREIGN_APPROVAL"])

        # File presence
        csv_flow = self.root / "docs" / "catalogs" / "FLOW_ENGINE_TRIGGER_SETTLEMENT_MATRIX.csv"
        self.assertTrue(csv_flow.exists())
        f_lines = [l.strip() for l in csv_flow.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual(len(f_lines), 17, "Header + 16 Elemente")

        csv_review = self.root / "docs" / "catalogs" / "CODE_REVIEW_20_SECURITY_TOOLS_CATALOG.csv"
        self.assertTrue(csv_review.exists())
        r_lines = [l.strip() for l in csv_review.read_text(encoding="utf-8").splitlines() if l.strip()]
        self.assertEqual(len(r_lines), 21, "Header + 20 Tools")

        arch13 = self.root / "docs" / "concept_papers" / "specialized" / "Architecture_13_Flow_Engine_Sensor_Trigger_Settlement_Spectral_Loop.md"
        self.assertTrue(arch13.exists())
        self.assertGreater(arch13.stat().st_size, 3000)

        arch14 = self.root / "docs" / "concept_papers" / "specialized" / "Architecture_14_Automated_PR_Code_Review_SAST_DAST_AST_Stack.md"
        self.assertTrue(arch14.exists())
        self.assertGreater(arch14.stat().st_size, 3000)

        web_3d = self.root / "web" / "flow-engine-3d.html"
        self.assertTrue(web_3d.exists())
        self.assertGreater(web_3d.stat().st_size, 2000)


if __name__ == "__main__":
    unittest.main()
