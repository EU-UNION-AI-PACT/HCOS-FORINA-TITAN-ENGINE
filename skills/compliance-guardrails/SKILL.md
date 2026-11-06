---
name: compliance-guardrails
description: Erzwingt EU AI Act, EUPL-1.2, DSGVO und institutionelle Governance-Vorgaben innerhalb der HCOS Engine.
version: 1.0.0
author: Daniel Pohl
frameworks: [EU AI Act, DSGVO/GDPR, EUPL-1.2, NATO Alignment]
---

# HCOS Compliance & Regulatory Guardrails Skill

## Zweck & Kompetenzen
Ermoeglicht dem Agenten die automatische Pruefung von Code, Datenfluessen und Benutzeranfragen auf EU-Konformitaet:
- **DSGVO / Anonymitaet:** Sicherstellung, dass keine PII (persönlich identifizierbaren Daten) in Telemetrie oder Logs gelangen (nur anonyme Session-IDs wie `ANON-XXXXX`).
- **EU AI Act Guardrails:** Transparenzpflichten, Risiko-Klassifizierung und unverfaelschbare Audit-Trails.
- **Werte-Badges:** Zertifizierung von Originalitaet, Zukunftssicherheit und EU-Union-Richtlinien.

## Verfuegbare MCP-Tools
- `audit_privacy`: Prueft Datenstrukturen auf unerlaubte PII.
- `verify_eu_badges`: Kontrolliert die 3 HCOS-Werte-Badges.
- `generate_compliance_report`: Erzeugt JSON- und Markdown-Nachweise fuer Inspektoren.
