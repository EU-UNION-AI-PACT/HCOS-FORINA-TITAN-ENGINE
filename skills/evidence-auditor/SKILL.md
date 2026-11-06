---
name: evidence-auditor
description: Fuehrt kryptografische Integritaetspruefungen, Merkle-Root-Berechnungen und Ed25519-Signatur-Validierungen durch.
version: 1.0.0
author: Daniel Pohl
frameworks: [Ed25519 RFC 8032, Merkle SHA-256, HCOS Sovereign Seal]
---

# HCOS Evidence Auditor & Cryptographic Proofs Skill

## Zweck & Kompetenzen
Verleiht dem Agenten Zugriff auf das kryptografische Zertifizierungs- und Audit-Subsystem:
- **Merkle-Root-Berechnung:** Erstellt den deterministischen SHA-256 Hashbaum ueber den gesamten Quellcode.
- **Asymmetrische Signaturpruefung:** Verifiziert die Ed25519-Signatur von Daniel Pohl gegen den oeffentlichen Schluessel (`sovereign_pubkey_ed25519.pem`).
- **Manipulationserkennung:** Schlaegt sofort Alarm, wenn auch nur ein einzelnes Byte unautorisiert geaendert wurde.

## Verfuegbare MCP-Tools
- `calculate_merkle_root`: Berechnet den Wurzel-Hash des Repositories.
- `verify_ed25519_seal`: Fuehrt die asymmetrische mathematische Signaturpruefung aus.
- `export_evidence_json`: Exportiert den fertigen Nachweis in `releases/`.
