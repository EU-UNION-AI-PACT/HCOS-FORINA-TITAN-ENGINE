---
name: forina-domain-trust
description: Analysiert und auditiert DLT- & Domain-Trust-Records, DNS-Routing, TLS-Zertifikate und sslip/nip Wildcard-Eintraege fuer HCOS FORINA TITAN.
version: 1.0.0
author: Daniel Pohl
frameworks: [NATO Strategic Defense, EU Regulatory Governance]
---

# FORINA Domain Trust & DNS Auditor Skill

## Zweck & Kompetenzen
Dieser Skill verleiht dem HCOS AI Agenten die Faehigkeit, Domaenen und Netzwerkinfrastrukturen souveraen zu auditieren:
- **Wildcard-DNS Pruefung:** Validierung von `sslip.io` und `nip.io` Domaenenaufloesungen.
- **TLS/SSL-Zertifikate:** Ueberpruefung der Verschluesselungsparameter und Header-Integritaet.
- **Fail-Closed Routing:** Sicherstellung, dass nicht autorisierte Requests vom Caddy/NGINX Reverse Proxy abgefangen werden.

## Verfuegbare MCP-Tools
- `dns_lookup`: Aufloesung von A-, AAAA- und TXT-Records.
- `tls_inspect`: Pruefung der Zertifikatslaufzeit und Cipher-Suites.
- `verify_trust_record`: Abgleich mit dem HCOS Trust Register.

## Sicherheits-Guardrails
- Keine DNS-Spoofing-Versuche.
- Zugriff ausschliesslich ueber autorisierte Proxies.
- Vollstaendiges Audit-Logging in `releases/audit_evidence_*.json`.
