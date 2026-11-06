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


class TestForinaTitanEngine(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).parent.parent

    def test_spec_sync_engine(self):
        sync = SpecSyncEngine(self.root)
        result = sync.verify_all_modules()
        self.assertEqual(result["total_modules"], 8)
        self.assertTrue(result["overall_realized"], "Alle 8 Module muessen als realisiert bewertet werden")
        self.assertEqual(result["overall_percentage"], 100)
        self.assertEqual(len(result["modules"]), 8)
        for mod in result["modules"]:
            self.assertEqual(mod["score"], 100)
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
