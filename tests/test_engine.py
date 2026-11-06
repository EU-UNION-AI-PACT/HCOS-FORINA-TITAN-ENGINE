"""
HCOS - HNOSS CONTROL OPERATING SYSTEM
AUTOMATED ENGINE & SPEC-SYNC TESTS
Copyright (c) 2024-2026 Daniel Pohl. All Rights Reserved Worldwide.
"""
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
        cert = certifier.generate_certificate()
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

    def test_pipeline_build(self):
        engine = ForinaTitanEngine(self.root)
        report = engine.run_pipeline()
        self.assertEqual(report["status"], "SUCCESS")
        self.assertTrue((self.root / "dist" / "index.html").exists())
        self.assertTrue((self.root / "dist" / "styles.css").exists())
        self.assertTrue((self.root / "dist" / "app.js").exists())
        self.assertTrue((self.root / "dist" / "spec-status.json").exists())
        self.assertTrue((self.root / "dist" / "AetherTitan.AppDir" / "AppRun").exists())


if __name__ == "__main__":
    unittest.main()
