# -*- coding: utf-8 -*-
"""Unit tests for UPUIA Universal Project & URL Intelligence Archive Engine."""
import unittest
from pathlib import Path
from forina_engine.upuia_scanner import UpuiaIntelligenceArchive, UpuiaSecurityViolation


class TestUpuiaScanner(unittest.TestCase):
    def setUp(self):
        self.archive = UpuiaIntelligenceArchive()

    def test_preflight_and_summary(self):
        preflight = self.archive.run_preflight_check()
        self.assertTrue(preflight["preflight_passed"])
        self.assertTrue(preflight["rule_1_system_immutable"])
        self.assertTrue(preflight["rule_2_local_only"])

        summary = self.archive.get_summary()
        self.assertEqual(summary["status"], "OPERATIONAL_OFFLINE")
        self.assertEqual(summary["security_directiv_compliance"], "10/10 Grundregeln verifiziert")
        self.assertTrue(summary["immutable_originals"])

    def test_secret_file_filtering(self):
        self.assertTrue(self.archive.is_secret_file("id_rsa"))
        self.assertTrue(self.archive.is_secret_file("id_ed25519.key"))
        self.assertTrue(self.archive.is_secret_file("server.pem"))
        self.assertTrue(self.archive.is_secret_file("ca.crt"))
        self.assertTrue(self.archive.is_secret_file(".env"))
        self.assertTrue(self.archive.is_secret_file("Client-Anmelde.env"))
        self.assertTrue(self.archive.is_secret_file("secrets_vault.json"))
        self.assertFalse(self.archive.is_secret_file("README.md"))
        self.assertFalse(self.archive.is_secret_file("config.json"))

    def test_sanitize_url_removes_sensitive_query_parameters(self):
        url = "https://api.example.com/v1/data?page=2&token=ghp_secretTokenHere1234567890123&view=grid"
        res = self.archive.sanitize_url(url)
        self.assertIsNotNone(res)
        clean_url, scheme, domain, path, query = res
        self.assertNotIn("token", query)
        self.assertNotIn("ghp_secretToken", clean_url)
        self.assertIn("page=2", query)
        self.assertIn("view=grid", query)

    def test_scan_text_content_extracts_and_categorizes(self):
        text = """
        Hier sind URLs:
        Besuche https://github.com/EU-UNION-AI-PACT/HCOS-FORINA-TITAN-ENGINE
        Und offizielle Normen https://www.iso.org/standard/27001.html
        Und EZB https://www.ecb.europa.eu/paym/intro/mip-online/html/2026_pontes.de.html
        """
        records = self.archive.scan_text_content(text, source_file="synthetic_doc.txt")
        self.assertEqual(len(records), 3)

        domains = {r.domain: r.category for r in records}
        self.assertIn("github.com", domains)
        self.assertEqual(domains["github.com"], "Source Code & Repositories")
        self.assertEqual(domains["www.iso.org"], "Regulatory & Norms")
        self.assertEqual(domains["www.ecb.europa.eu"], "Central Banking & Web3 Finance")


if __name__ == "__main__":
    unittest.main()
