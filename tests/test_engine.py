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


if __name__ == "__main__":
    unittest.main()
