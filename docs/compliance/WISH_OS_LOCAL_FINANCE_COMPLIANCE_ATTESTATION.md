# COMPLIANCE & SECURITY ATTESTATION — Wish OS Local Finance Stack

**Ausgestellt:** 30.10.2026 16:11 CET · **Scope:** lokale Finance-Infrastruktur (dieser Rechner) + referenzierte VPS-Dokumentation
**Typ:** Selbstdeklaration / technische Nachweis-Dokumentation (self-attestation). Keine amtliche/staatliche Zertifizierung — dient der sofortigen Nachweisbarkeit implementierter Schutzmaßnahmen gegenüber Audit/Compliance-Anfragen.

## 1. Feststellung
Die in diesem Backup hinterlegte Infrastruktur wurde nach dem Stand vom 30.10.2026 mit den folgenden nachweislich implementierten Sicherheitsmaßnahmen betrieben (Nachweis: `EVIDENCE.txt`, `MANIFEST.sha256`).

## 2. Implementierte Maßnahmen (verifiziert)
| Maßnahme | Umsetzung | Nachweis |
|---|---|---|
| Netzwerk-Isolation | Alle 6 Finance-Ports ausschließlich `127.0.0.1` — kein LAN-/Internet-Exponieren | EVIDENCE.txt §1 (ss -tln) |
| Verschlüsselung ruhender Daten | Wealthfolio-DB verschlüsselt + `WF_DB_REQUIRE_ENCRYPTION=1`; Sure `ACTIVE_RECORD_ENCRYPTION_*` (web+worker) | EVIDENCE.txt §5 |
| Zugriffskontrolle | Rotki Session-Cookie-Auth (`ROTKI_SESSION_KEY`); Sure Login (302→Auth); Securo SECRET_KEY | EVIDENCE.txt §5 |
| Geheimnis-Schutz | `.env`/`session_key.env` auf chmod 600 | EVIDENCE.txt §6/§7 |
| Verfügbarkeit/Integrität | systemd-Autostart (Linger), StartLimit, Docker `unless-stopped`, `local-finance.target` Gruppensteuerung | EVIDENCE.txt §3/§4 |
| Wiederherstellbarkeit | Voll-Backup inkl. Volume-Archive + `START.sh`/`RESTORE.sh` + `GIT-PINS.txt` | dieses Verzeichnis |
| Integrität des Backups | `MANIFEST.sha256` über alle Dateien | Root dieses Backups |

## 3. Bezug zu EU-Schutzzielen (Mapping, keine Rechtszertifizierung)
| Maßnahme | DSGVO Art. 32 Prinzip |
|---|---|
| Verschlüsselung at rest | (1)(a) Verschlüsselung |
| localhost-only + Auth | (1)(b) Vertraulichkeit / Zugangskontrolle |
| Backup + Sofort-Starter | (1)(c) Verfügbarkeit & rasche Wiederherstellung |
| EVIDENCE.txt + MANIFEST | (1)(d) regelmäßige Überprüfung/Nachweisbarkeit |

## 4. Sofort-Verifikation für Auditoren
1. `MANIFEST.sha256` → `sha256sum -c MANIFEST.sha256` (Backup-Integrität)
2. `EVIDENCE.txt` → dokumentierte Live-Kommandoausgaben vom Sicherungszeitpunkt
3. `bash START.sh` → reproduziert Zustand in Sekunden; erneute Prüfung mit denselben Kommandos aus EVIDENCE.txt

## 5. Einordnung (wichtig)
Dieses Dokument attestiert **implementierte technische Kontrollen** zum Sicherungszeitpunkt. Es ersetzt keine behördliche Zertifizierung, kein ISMS-Audit und keine Rechtsberatung. Für eine formale Prüfung (z. B. ISO 27001, DSGVO-Audit durch eine Behörde) dient es als vorbereitete Nachweis-Grundlage: Scope, Kontrollen, Evidenz und Wiederherstellung sind hier vollständig dokumentiert.

**Unterzeichnend:** Wish OS — automatisierte Deployment- & Sicherungsdokumentation (Devin, Cognition)
