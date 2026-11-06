# HCOS FORINA TITAN ENGINE
## Masterkonzept: Modular Intelligence, Trust, Compliance & Assured Delivery

**Konzeptversion:** 1.0 — 06. November 2026  
**Status:** Entwurf / Zielarchitektur; keine produktive Freigabe  
**Quellengrundlage:** hochgeladener Katalog `PDF_Sourcecode_Hyperlinks_50(1).md` (50 Einträge aus zwei PDFs)  
**Leitmotiv:** *Jede Funktion modular; jede Aktion autorisiert; jeder Nachweis überprüfbar.*

> **Trennung von Fakten und Vorschlägen:** Die Repository-Namen, URLs, PDF-Seiten und die Kennzeichnung direkter bzw. ergänzter Verweise stammen aus dem bereitgestellten Katalog. Alle Architekturentscheidungen, Modulrollen, Prioritäten, Sicherheitsrichtlinien, Datenmodelle, Entwicklungsphasen und Abnahmekriterien in diesem Dokument sind **neu erarbeitete Vorschläge**. Die Quelle belegt weder eine fertige Integration noch die Sicherheit oder Lizenzverträglichkeit der Projekte.

---

## 1. Executive Summary

HCOS FORINA TITAN ist als modularer Kontroll-, Entwicklungs- und Nachweisrahmen geplant, der auf einer vorhandenen Python-Pipeline aufbauen kann. Die 50 katalogisierten GitHub-Einträge werden **nicht** ungeprüft als Monolith übernommen. Stattdessen erhält jedes Drittprojekt genau einen der Modi **Kernbaustein**, **optional angebunden**, **Referenz/Alternative**, **zurückgestellt** oder **für den Sicherheitskern ausgeschlossen**. Die Zuordnung ist vorläufig und in der Evaluationsmatrix dokumentiert.

Die Zielplattform umfasst drei voneinander getrennte Betriebsdomänen:

1. **Sovereign Local / UPUIA:** explizit zugelassene Dateien, kein Netzwerk, keine Schlüssel/Zertifikate, kein Systemumbau, keine Container, keine ungeprüfte Fremdcode-Ausführung. Eine unabhängige Startinstanz muss Isolation *vor* der Ausführung durchsetzen bzw. nachweisen. Ist dies mit vorhandenen OS-Mitteln nicht möglich, gilt **Startverbot (fail closed)**.
2. **Development & Research:** öffentliche Quelltexte, Metadaten und synthetische Beispiele; hier können GitHub, Mistral oder weitere APIs nach expliziter Berechtigung verwendet werden. Keine produktiven Geheimnisse oder lokalen UPUIA-Daten.
3. **Federation & Services:** bewusst aktivierte Online-Adapter wie OIDC, JMAP, Finanzdaten-APIs, Domain-Discovery und Partner-Connectoren. Diese Zone kann vom Offline-Bereich keine Aufträge ziehen und keine sensitiven Daten abrufen.

**Erfolgskriterium:** Kein Modul wird als „verifiziert“, „zertifiziert“ oder „produktionsreif“ bezeichnet, nur weil Dateien vorhanden sind oder Schlüsselwörter in einer Spezifikation vorkommen.

## 2. Scope und Nicht-Ziele

**Im Scope:** Modul-Lebenszyklus, deklarative Fähigkeitssysteme, lokale Artifact-Builds, Offline-PWA, Desktop-Paketierung, Richtlinienprüfung, Security Review, Agent-Evaluation, RAG-Metadaten, föderierte Online-Adapter, Audit-Artefakte, Rollback, Release-Signaturen, optionaler Finanzanalyse-Use-Case.

**Nicht im Scope der ersten Ausbaustufe:** automatische Banktransfers, Settlement ohne separate Benutzerautorisierung, flächendeckendes Crawling fremder Sites ohne Erlaubnis und Nutzungsprüfung, eigenmächtige OIDC-Föderationsaktivierung, echte Zertifizierungsbehauptungen durch eigene Badges, weltweite institutionelle Statuszusicherungen, schlüsselloses „magisches“ Signieren oder eine garantierte Isolation ausschließlich durch Python-Logik.

## 3. Zielarchitektur und Trust Boundaries

```text
                  [ÖFFENTLICHE QUELLEN / SYNTHETISCHE DATEN]
                                  |
                        DEVELOPMENT / RESEARCH
                +-----------------+------------------+
                | Repo-Intake / BOM / License Review |
                | Sandbox-Simulator mit Fake-Daten   |
                | KI-/MCP-Adapter (opt-in)           |
                +-----------------+------------------+
                                  |
                    geprüfte, signierte Exportpakete
                                  v
                +------------------------------------+
                | HCOS TITAN CONTROL PLANE           |
                | Modulregistrierung / Policy / UI   |
                | Evidence Index / Approval Ledger   |
                +-----------------+------------------+
                                  |
              +-------------------+--------------------+
              |                                        |
      LOCAL SOVEREIGN ZONE                     ONLINE FEDERATION ZONE
      Ausführung nur, wenn                     explizite Freigaben,
      Isolation unabhängig                     API-Gateway,
      durchsetzbar ist                         egress allowlist
              |                                        |
      [UPUIA / Offline Models]                [GitHub/JMAP/OIDC/andere]
              |                                        |
              +-------------------+--------------------+
                                  |
                    [INDEPENDENT RELEASE GATE]
                 Checks -> Evidence -> Approval -> Sign
                                  |
                         [APPIMAGE / PWA / ZIP]
```

**Wichtig:** Das Diagramm ist eine logische Zielarchitektur. Die Kanten markieren **keinen automatischen bidirektionalen Datentransfer**. Ein Import in die lokale Zone ist ein separat genehmigter Vorgang nach Format- und Signaturprüfung. Ausgehende Kommunikation bleibt im UPUIA-Kontext technisch unterbunden.

### 3.1 Control Plane / Data Plane

- **Control Plane:** Modulmetadata, zulässige Aktionen, Richtlinien, Rollen, Genehmigungen, Build-Ergebnisse, Verweise auf Nachweise. Sie verarbeitet keine vertraulichen Scannerinhalte.
- **Data Plane:** Fachmodule führen nur erlaubte Aufgaben aus; Quellenzugriff und Ausgabeverzeichnisse sind pro Modul auf das Minimum begrenzt.
- **Assurance Plane:** Unabhängige Checks bewerten Artefakte, nicht bloß Statusmeldungen von Agenten. Nur diese Ebene darf den technischen Freigabestatus setzen.
- **Signierinstanz:** Ein von Scannern und Agenten getrennter Prozess; private Signierschlüssel sind **niemals** in Scanzielen, LLM-Kontext, Logs, Repository oder Testdaten enthalten.

## 4. Sicherheitsgrundregeln

1. **Deny by default / fail closed:** Jede nicht explizit zugelassene Datei, URL, Tool-Aktion, externe Verbindung oder Modul-Fähigkeit wird abgewiesen.
2. **Schlüssel-Ausschluss vor Dateizugriff:** Nicht erst nach dem Lesen nach Passwörtern suchen. Verzeichnis- und Dateitypen für Credentials, PEM, Zertifikate, Tokens sowie Schlüsselmaterial bereits bei der Dateiauswahl ausschließen; nicht öffnen, nicht hashen, nicht kopieren, nicht protokollieren.
3. **Kein stiller Egress:** Keine Telemetrie, Crashreports, Cloud-Abrufe, Modell-Downloads oder Auto-Updater im strikt lokalen Scanlauf.
4. **Unveränderliche Originale:** Der Scanner schreibt nur in ausdrücklich zugelassene neue Projekt-/Ausgabeordner und hält Quelldateien und ihre Zeitstempel unverändert.
5. **Unabhängiger Startmechanismus:** Vor dem Scanner: verifizierter Launcher prüft Binär-/Skript-Hashes, Signatur, absolute Pfade, Freigaben, Abhängigkeiten, Ausgabebereich und technisch nachgewiesene Netzwerkunterbindung. Eigene Python-Checks reichen nicht.
6. **Keine Container oder Host-Änderungen:** Der UPUIA-Pfad verwendet weder Docker, Podman, VMs noch neue Dienste, Netzwerkregeln, Pakete oder geänderte Sicherheitsrichtlinien. Wenn eine echte technische Sperre innerhalb bestehender Systemmöglichkeiten nicht verfügbar ist, wird der Lauf blockiert.
7. **KI ist nicht Prüfbehörde:** Agenten erstellen Vorschläge; OPA-/Native-Policy, reproduzierbare Tests und autorisierte Menschen treffen die Freigabeentscheidung.
8. **Kein Agent darf sein eigenes Ergebnis allein zertifizieren.** Revisionsrollen müssen getrennt sein; Testcases stammen unabhängig aus Spezifikationen und Negativszenarien.
9. **Kostenlimits:** Online-Adapter erhalten Budget, Ratenlimit und API-Scopes. Nutzungsabhängige Connectoren sind standardmäßig ausgeschaltet.
10. **Keine unbelegten institutionellen Behauptungen:** Selbst generierte Prüfnachweise = technische Integritätsnachweise, nicht EU-, NATO- oder behördliche Zertifizierungen.

## 5. Datenklassifikation und Zugriffsregeln

| Klasse | Beispiele | Offline-Modus | Cloud-/Mistral-Modus | Hinweise |
|---|---|---|---|---|
| PUBLIC | Öffentliche GitHub-Metadaten, veröffentlichte Standards, öffentliche URLs | zulässig | nach Freigabe zulässig | Urheberrecht und Nutzungsregeln beachten |
| SYNTHETIC | Fake-Konten, Fake-Token, Mock-DNS, Mock-Transaktionen | zulässig | nach Freigabe zulässig | synthetisch kennzeichnen |
| INTERNAL | Eigene unveröffentlichte Architekturentwürfe | nur zugelassene Ordner | standardmäßig gesperrt | Einzelgenehmigung nötig |
| RESTRICTED | Bankdaten, vertrauliche Mails, nichtöffentliche Organisationsdaten | nur gesondert geregelte lokale Umgebung | verboten im Konzeptstandard | minimierte Berichte |
| SECRET | API-Schlüssel, PEM, private Keys, Zertifikate, Session-Tokens | für UPUIA ausdrücklich nicht zugreifbar | verboten | getrennte Credential-Infrastruktur |

**Zusatz:** Ein Prüfer, der bekannte Secrets suchen müsste (z. B. Agent-Session-Scanner), darf im strikten UPUIA-Modus nicht auf echte Credential-Dateien zugreifen. Dafür nur synthetische Testbestände verwenden. 

---

## 6. Modulkatalog (Zielobjekte, nicht bestehende Implementierungen)

### M01 — Trusted Module Registry & Loader
**Ziel:** Erweiterungen katalogisieren, ohne ungeprüften Code automatisch nachzuladen.
- Eintrag: Modul-ID, Release, SBOM, Hash, optional echte Signatur, Herkunft, Lizenzstatus, ABI/API-Vertrag, Fähigkeiten, interne Abhängigkeiten, Zugriffsprofil.
- Loader akzeptiert nur lokale, vorab geprüfte Artefakte aus einer expliziten Allowlist. Keine dynamisch nachgeladene fremde Remote-JavaScript-Datei im sicherheitskritischen Kern.
- Lebenszyklus: `DISCOVERED -> REVIEWED -> BUILDABLE -> TESTED -> VERIFIED -> APPROVED -> ACTIVE`, plus `QUARANTINED`, `REVOKED`.
- Dependency graph mit Konflikterkennung, Version-Pinning und Rückwärtskompatibilitäts-Tests.
- **Repo-Kandidaten:** Module Federation (#37), vite-plugin-federation (#38), single-spa (#39), SystemJS (#40) als UI-Referenzen; nicht automatisch für den privilegierten Kern geeignet.
- **Abnahme:** Manipulierte Manifeste, Hashabweichungen und fehlende Genehmigungen führen nachweisbar zu keiner Aktivierung.

### M02 — Secure App Builder / Linux Delivery
**Ziel:** Desktop und Offline-PWA zuverlässig und reproduzierbar bereitstellen.
- Primärpfad: Tauri (#1), Tauri Plugins (#34), AppImageKit (#2), Workbox (#41) bzw. Vite PWA (#42).
- Electron (#36), Capacitor (#44) und Pake (#45) bleiben Plattformalternativen; nicht parallel als Pflicht-Framework einbauen.
- AppDir-Staging ist **kein** fertiges AppImage. Für Packaging ist eine gesonderte Erstellung und Validierung notwendig.
- Keine unautorisierten Update-Verbindungen. Online-Updates (#33/#35) nur in explizit aktiviertem Online-Profil; Offline-Updates per signiertem Importpaket und manueller Freigabe.
- **Abnahme:** Paket ist startbar, enthält alle Abhängigkeiten, läuft ohne Netz, lässt keine schreibenden Seiteneffekte auf nicht freigegebene Pfade zu und besteht einen Rollback-Test.

### M03 — UI/UX Composition Studio
**Ziel:** Dashboard, Redaktion, 3D-/Animationseffekte und barrierearme Bedienung.
- Quellen: GSAP (#9), Three.js (#10), Canvas Confetti (#11), Howler.js (#12), React Grid Layout (#13), Tiptap (#14), Editor.js (#15), Motion (#16).
- Animationsmodule dürfen niemals Sicherheitsergebnisse simulieren oder als Nachweis dienen. Reduzierte Bewegung, Tastaturnavigation, Sound-Opt-in und klar getrennte Statusfarben vorsehen.
- Einen Editorpfad (Tiptap **oder** Editor.js) auswählen, keine Doppelabhängigkeit ohne funktionale Begründung.
- **Abnahme:** Accessibility-Checks, UI-Tests, keine Verarbeitung sensibler Inhalte in Analytics oder Crashreports.

### M04 — Identity, Consent & Role Engine
**Ziel:** Authentifizierung und Autorisierung unabhängig von der KI durchsetzen.
- Kandidaten: Pocket ID (#17) für Passkeys/OIDC, Authelia (#18) für Zugriffsabsicherung, otplib (#19), QR-Code (#20), CookieConsent (#21).
- Authentifizierung ist nicht Autorisierung. Rollen und Datenzugriff werden separat über prüfbare Policies festgelegt.
- Lokale Offline-Werkzeuge benötigen einen eigenen minimalen Berechtigungsmodus; kein stiller Anmeldungszwang mit externem Identity Provider.
- **Abnahme:** Zugriffssperre ohne gültige Session, Replay-/CSRF-/Session-Tests für Webprofile; Consent ist widerrufbar.

### M05 — AI Model & Agent Orchestrator
**Ziel:** Austauschbare Agenten und Workflows, aber keine ungeprüften Side-Effects.
- Referenzen: Dify (#22), Vercel AI SDK (#23); Mistral ist ein **außerhalb der 50 Liste** liegender optionaler Provider.
- Agentrollen: Discovery, Classification, Security Review, Compliance Mapping, Build Planner, Evidence Analyst. Alle Aktionen als Vorschläge oder capability-beschränkte Tool-Aufrufe.
- Sensitive Daten niemals per Cloud-LLM verarbeiten. Reiner Offline-Pfad benötigt ein separat geprüftes lokales Modell bzw. eine zuvor bereitgestellte Runtime.
- **Abnahme:** Agentenvorschlag kann eine Policy nicht umgehen; unbelegte Antworten werden als Hypothesen markiert; alle Side-Effects benötigen explizite Genehmigung.

### M06 — Knowledge, Search & Local Data
**Ziel:** Quellmaterial indexieren, wiederauffindbar machen, Herkunft belegen.
- Primärer Kandidat innerhalb der 50: RxDB (#46) als Offline-/Sync-Datenhaltung. Erweiterte RAG/Embedding-Bibliotheken aus den jüngeren 50 Empfehlungen können separat evaluiert werden; sie gehören **nicht** zu den 50 PDF-Quellen.
- Indexeintrag: Quelle, Originalzeit, Ingest-Zeit, Dokument-Hash (nur freigegebene Dateien), Jurisdiktion, Kategorie, Normversion, Freigabeklasse, Indexalgorithmus.
- Keine stille Cloud-Synchronisation. Dokumentinhalt darf nur in das zu seiner Klasse passende Repository und Backend gelangen.
- **Abnahme:** Löschung/Widerruf führt zu nachvollziehbarer Indexbereinigung, Ergebnisse enthalten Quellenverweise, keine unfreigegebene Indexierung.

### M07 — FORINA Domain Trust & Compliance
**Ziel:** Domänen- und Organisationsstatus **nachweisbasiert** erfassen, nicht behaupten.
- Zustände: `DISCOVERED`, `TECHNICALLY_VERIFIED`, `DOMAIN_CONTROL_VERIFIED`, `ORGANIZATION_VERIFIED`, `COMPLIANCE_EVIDENCE_VERIFIED`, `FEDERATION_AUTHORIZED`, `ACTIVE`.
- Technische Checks je Freigabe: DNS, DNSSEC, TLS, RDAP; organisatorisch nur autoritative Register-/LEI-Daten und nachvollziehbare Belege.
- Implementierung: Quellenadapter für öffentliche Informationen, OPA (#27) für Regeln, separate Evidence Records; keine Zertifizierungsbehauptung aus einem Badge.
- Föderation wird ausschließlich auf Grundlage einer beweisbaren, expliziten Berechtigung aktiviert.
- **Abnahme:** Fehlende Nachweise führen zu `UNVERIFIED`, widersprüchliche zu `REVIEW_REQUIRED`; keine stillschweigende Hochstufung.

### M08 — Financial Intelligence (freiwillige Erweiterung)
**Ziel:** Read-only-Analyse von Kontodaten und Kostenanomalien.
- Der Claude-Newsletter beschreibt Personal-Finance-Analysen, **liefert dafür aber kein offenes Claude-Personal-Finance-Repository**. Dieses Modul ist daher ein neuer Eigenentwicklungs-Vorschlag, nicht Teil der 50 Quellcodeprojekte.
- Funktionen: Buchungskategorisierung, Doppelbuchungsverdacht, wiederkehrende Abbuchungen, Gebühren- und Abo-Abweichungen, Cashflow-Vorschau.
- Datenquelle im Online-Profil über ausdrücklich berechtigte Banking-Provider; lokal anhand synthetischer CSV-Beispiele entwickeln.
- **Keine automatische Zahlung, kein Settlement und keine Anlagenentscheidung.** Diese Aktionen wären getrennt autorisierungspflichtige Fachanwendungen mit zusätzlichen rechtlichen Pflichten.
- **Abnahme:** Beträge deterministisch nachrechnen, Buchungswährung und Valutadatum berücksichtigen, Modellfehler durch Regeltests erkennen.

### M09 — JMAP, Messaging & Calendar
**Ziel:** Partnerschaftskommunikation, Terminplanung und nachweisbare Nachrichtenprozesse.
- Kandidaten: Linagora JMAP TS (#28, **Ersatz des nicht verifizierten Originals**), Stalwart (#29), Cal.com (#32), Super Productivity (#26).
- Erst Draft/Review/Approval, dann Versand. Kein automatisches Verteilen von Partneranfragen oder vertraulichen Details.
- Online-only-Adapter, nicht als Voraussetzung für den UPUIA-Scanner.
- **Abnahme:** Authentifizierung getrennt, korrekte Empfängerfreigaben, Idempotenz und Widerruf für geplante Aktionen.

### M10 — Privacy-Respecting Monitoring
**Ziel:** Minimaler Zustand und Betriebsbeobachtung ohne Datenleck.
- Umami (#30) und Plausible (#31) sind **Alternative** für freiwillige Webstatistik, nicht erforderlich für lokale Scannerläufe.
- Keine Inhalte, Zugangsdaten, URLs aus gesperrten Scans oder Chat-Texte in Logs, Traces oder Analytics.
- Nur aggregierte, ausdrücklich konfigurierte Betriebskennzahlen für öffentliche Online-Portale.
- **Abnahme:** Netzwerksperre verhindert jede Telemetrie; Log- und Audit-Dateien enthalten ausschließlich erlaubte Metadaten.

### M11 — Media & Voice Studio
**Ziel:** Medienausgabe und sprachgestützte Bedienung.
- FFmpeg WASM (#24), Video.js (#25), Howler.js (#12), ggf. externe lokale Speech-Modelle nach neuer Evaluierung.
- Kein erzwungener Mikrofonzugriff, keine ungewollten Audio-Uploads, keine versteckte Sprachaufnahme.
- **Abnahme:** Vollständig deaktivierbar, keine Sensordaten ohne explizites Opt-in, Exportformate dokumentiert.

### M12 — Independent Assurance / Agent Chain Bench
**Ziel:** Fehlerketten erkennen, Agentenselbstauskünfte kritisch prüfen.
- BOBA-bench (#47) ist Forschungs-/Benchmarkreferenz für verkettete Aufgaben. Nicht jedes Ergebnis aus einem Paper ist auf den konkreten HCOS-Bestand übertragbar.
- Stroq (#50) ist ein Kandidat zum Analysieren von Agentensitzungen. Im strengen UPUIA-Modus **nicht auf echte Key-/Credential-Pfade ansetzen**; ausschließlich synthetische Test-Sessions außerhalb des sensitiven Laufbereichs.
- Testharness erzeugt Negativfälle, manipulierte Module, prompt-injection-artige Texte, Versionskonflikte, defekte Artefakte und fehlerhafte Signaturen.
- **Abnahme:** Unabhängiger Review stoppt Kettenfortschritt bei unbestätigten Vorgängerergebnissen, mindestens ein Negativtest pro gefährlicher Fähigkeit.

### M13 — Supply-Chain, Backup & Update Assurance
**Ziel:** Prüfbarkeit vom Fremdrepository bis zum Release-Paket.
- BorgBackup (#4) für optionales, separat freigegebenes Backup; AppImageUpdate (#33) als Online-Update-Referenz; AppImageKit (#2).
- Drittcode nur über geprüfte Tags/Commits, mit Lizenzakte, Abhängigkeiten, SBOM, Quellhashes, Build-Rezept und unabhängigen Tests.
- Backup darf keine nicht freigegebenen Quellordner oder Credentials einschließen. Updatepaket erst nach Validierung der tatsächlich signierten Bytes aktivieren.
- **Abnahme:** Reproduzierbarer Build soweit realistisch, gescheiterter Updateversuch lässt funktionsfähige Vorversion unverändert, Restore-Test erfolgreich.

---

## 7. Pipeline mit harten Freigabepunkten

| Gate | Stufe | Eingabe | Prüfergebnis | Stoppkriterium |
|---|---|---|---|---|
| G00 | Intake | Repository-URL, Commit, Herkunft | Quellakte + Hash | unbekannte Quelle / fehlende Herkunft |
| G01 | License & Threat Review | Lizenz, Abhängigkeiten, Funktionen | juristische/technische Freigabeliste | ungeklärte Lizenz bei Redistribution |
| G02 | Build Plan | Modulmanifest + Abhängigkeitsgraph | deterministischer Plan | unauflösbare Konflikte |
| G03 | Independent Preflight | Programmidentität, Pfade, Isolation | signierter Startentscheid | Netzwerk nicht nachweislich gesperrt (UPUIA) |
| G04 | Clean Snapshot | zugelassene Dateien | Snapshot-Metadaten | eingeschmuggelte Secrets / Excludes verletzt |
| G05 | Compile & Stage | freigegebener Quellstand | AppDir, Webbundle, Binärdaten | nicht gepinnte Dependency / unzulässiger Download |
| G06 | Unit & Integration Tests | Modul-Artefakte | reproduzierbare Testergebnisse | Pflichtfall rot |
| G07 | Adversarial Verification | künstlich fehlerhafte Fälle | Negativtest-Report | Umgehung von Policy / Rechteausweitung |
| G08 | Evidence Construction | Test- und Build-Belege | Prüfnachweis-Manifest | unbelegter Claim |
| G09 | Approval | unabhängiger Review | freigegebene Release-ID | fehlende menschliche Freigabe |
| G10 | Sign & Seal | Release-Bytes, Nachweishashes | echte Signatur, nicht nur Digest | ungültige/unverifizierte Signatur |
| G11 | Publish / Import | signiertes Artefakt | PWA / AppImage / Offline-Bundle | nicht autorisierte Zielumgebung |
| G12 | Postrelease Verification | ausgerolltes Paket | Install-/Start-/Rollback-Nachweise | Abweichung vom freigegebenen Artefakt |

**Zentrale Regel:** Ein Agent darf *Tests vorschlagen und ausführen*, aber nicht allein über das Bestehen des unabhängigen Verifikations-Gates entscheiden.

## 8. Statusdefinitionen für das Live-Dashboard

| Status | Bedeutung | Darf als produktiv gelten? |
|---|---|---|
| DESIGN | Konzept/Manifest vorhanden | Nein |
| IMPLEMENTED | Code vorhanden | Nein |
| TESTED | definierte Tests erfolgreich | Nein |
| VERIFIED | unabhängige Nachweise geprüft | Noch nicht automatisch |
| APPROVED | berechtigte Stelle hat Freigabe erteilt | nur für definierte Einsatzart |
| ACTIVE | konkreter, überprüfter Release ist aktiv | nur im erlaubten Geltungsbereich |
| BLOCKED | Sicherheits-/Policykonflikt | Nein |
| REVOKED | Freigabe entzogen | Nein |

Eine Prozentzahl darf nur als **Testabdeckung nach vorher definierten, gewichteten Prüfpunkten** bezeichnet werden. Sie ist keine „EU/NATO-Zertifizierungsquote“.

## 9. Normierte Datenschnittstellen (Vorschlag)

### 9.1 Modulmanifest — Schemaentwurf

```json
{
  "schema_version": "hcos.module.v1",
  "id": "forina.domain-intelligence",
  "version": "0.1.0",
  "source": {"repository": "https://example.invalid/public-repo", "commit": "<PINNED_COMMIT>"},
  "artifact": {"sha256": "<ARTIFACT_SHA256>", "signature_ref": "<VERIFIED_SIGNATURE_REFERENCE>"},
  "capabilities": ["source.read_public_metadata", "evidence.write_local"],
  "deny": ["network.unapproved", "credential.read", "host.modify"],
  "data_classes": ["PUBLIC", "SYNTHETIC"],
  "execution_profile": "OFFLINE_VERIFIED",
  "dependencies": [],
  "license_review": "PENDING",
  "security_review": "PENDING",
  "approval": {"status": "NOT_APPROVED", "reference": null}
}
```

**Validierungsnotiz:** Die Platzhalter sind keine echten Hashes, Signaturen oder Genehmigungen. Ein aktives Modul muss vor Start gegen eine lokale, unabhängig verwaltete Vertrauensliste verifiziert werden.

### 9.2 Evidence Record — Schemaentwurf

```json
{
  "schema_version": "hcos.evidence.v1",
  "subject_id": "forina.domain-intelligence@0.1.0",
  "claim": "unit_tests_passed",
  "result": "PASS",
  "method": "pytest-from-approved-test-set",
  "test_suite_hash": "<PINNED_TEST_SUITE_HASH>",
  "artifact_hash": "<ARTIFACT_HASH>",
  "source_provenance": "<SOURCE_MANIFEST_ID>",
  "independent_verifier": "<VERIFIER_ID>",
  "observed_at_utc": "<ACTUAL_TIME>",
  "limitations": ["No external conformity assessment"],
  "signature": null
}
```

**Technischer Hinweis:** Ein SHA-256-Hash ist nur ein Inhaltsfingerabdruck. Eine echte Herkunftsaussage verlangt ein Signaturverfahren mit verifizierbarem öffentlichem Schlüssel, sicherer Schlüsselhoheit und nachvollziehbarer Signiereridentität. Die Signierkomponente ist von UPUIA strikt getrennt.

### 9.3 API-Endpunkte — nur Architekturvertrag

| Endpunkt | Methode | Rechte | Nebenwirkung |
|---|---|---|---|
| `/v1/modules` | GET | registry.read | keine |
| `/v1/modules/{id}/manifest` | GET | registry.read | keine |
| `/v1/plans` | POST | plan.create | legt Plan im erlaubten Projektbereich an |
| `/v1/runs/{id}/preflight` | POST | preflight.request | unabhängiger Isolationscheck |
| `/v1/runs/{id}/start` | POST | execute.approved | nur bei gültigem Freigabe-Token |
| `/v1/evidence/{id}` | GET | evidence.read | keine |
| `/v1/releases/{id}/approve` | POST | release.approve | Vier-Augen-Freigabe |
| `/v1/releases/{id}/import` | POST | bundle.import | signierten Offline-Import validieren |

**Nicht realisiert:** Diese Endpunkte sind ein Vertrag für die künftige Implementation, keine Behauptung über den aktuellen GitHub-Stand.

## 10. Drei konkrete Ende-zu-Ende-Workflows

### 10.1 Sicherer Repository-Onboarding-Workflow
`Quelle eintragen -> Lizenz/Herkunft prüfen -> commit pinnen -> Dependency-Map -> SAST/Tests -> Sandbox-Fake-Daten -> unabhängige Prüfung -> Manifest signieren -> Modul in Registry aufnehmen`.

**Beispiel:** GSAP soll für UI-Motion genutzt werden. Vor Übernahme: Lizenz für tatsächlichen Vertriebsmodus prüfen, nur benötigte UI-Komponenten zulassen, keinen Netzwerk-/Secrets-Zugriff erteilen, Build testen.

### 10.2 FORINA Domain-Evidence-Workflow
`Autorisierte URL -> öffentliche technische Metadaten -> Quellbelege -> Evidenzschema -> Widerspruchsprüfung -> technischer Status -> getrennte Organisationsprüfung -> autorisierte Föderation`.

**Stopps:** kein Netzwerk aus Offline-UPUIA; kein Scannen fremder Systeme jenseits ausdrücklich erlaubter Prüfung; keine organisationsbezogene Identität aus einem TLS-Zertifikat allein ableiten.

### 10.3 Agent-unterstützter Code-Workflow
`Ticket -> isolierte synthetische Tests -> Agent-Vorschlag -> statischer Check -> unabhängige Regressionstests -> Negativtests -> menschliches Review -> Freigabe`.

**Schlüssellogik aus BOBA:** Fehler in einem Schritt können Folgeaufgaben verfälschen. Deshalb darf eine Kette bei `FAILED` oder `UNKNOWN` nicht ohne geregelte Reparatur und erneute Überprüfung fortsetzen.

## 11. Repository-Eignung und Architekturentscheidungen

### 11.1 Primär auswählen, aber nur nach Einzelevaluation
- **Tauri + AppImageKit + Tauri Plugins:** Desktop und Packaging. Alternativen Electron/Pake nicht ohne Bedarf parallel einbauen.
- **Vite PWA oder Workbox:** kontrollierbarer Offline-Cache, statische UI und manuelle Versionierung.
- **OPA:** prüfbare Entscheidungslogik, jedoch kein Ersatz für OS-seitig erzwungene Isolation.
- **RxDB:** lokale Datenspeicherung mit strikten Zugriffsprofilen und ohne automatische Synchronisation.
- **BOBA-bench:** Benchmarkmethodik als unabhängiges Agent Chain Testset; Übernahme der Originaltests nur nach Lizenz- und Abhängigkeitsprüfung.
- **BorgBackup:** nur für genehmigte Ausgabedaten, keine automatische Heimverzeichnissicherung.

### 11.2 Optional anbinden / gesondert bereitstellen
- **Pocket ID, Authelia:** IdP/Reverse-Proxy-Integrationen für Online-Services, nicht innerhalb des strikten Offline-Scanners.
- **Stalwart, JMAP TS, Cal.com:** Serviceintegration mit OAuth/OIDC und separater Netzfreigabe.
- **Umami oder Plausible:** nur für freiwillige Statistik im öffentlichen Portal, niemals scannerinterne Telemetrie.
- **Caddy oder NGINX:** eine Reverse-Proxy-Lösung wählen; beide sind nicht im strengen UPUIA-Pfad erforderlich.

### 11.3 Zunächst nicht als zentralen lokalen Pflichtkern übernehmen
- **Dify:** breite Plattform, deren dokumentierter Standard-Selfhosting-Pfad Docker Compose verwendet; Lizenz mit Zusatzbedingungen. Für deinen Container-freien Offline-Scanner daher nicht als Pflichtabhängigkeit übernehmen. Separat betriebener Onlinedienst nur nach Architektur- und Lizenzfreigabe.
- **SystemJS / Remote Module Federation:** kein Nachladen fremden JavaScript-Codes in sicherheitskritische Runtime.
- **AppImageUpdate/Capacitor-Updater:** automatische Netz-Updates aus dem Offline-Lauf ausschließen.
- **Off Grid AI Mobile/Desktop:** als Referenz für lokale Modellarchitektur prüfen; Plattform-/Lizenzkompatibilität verifizieren, nicht blind in deine App übernehmen.
- **Stroq:** erfüllt bestimmte Agenten-Sicherheitsanwendungsfälle, kollidiert aber bei realer Credential-/Session-Inspektion mit deiner UPUIA-Verbotsliste; deshalb im betreffenden Pfad ausschließlich auf synthetischen Daten einsetzen.

## 12. Lizenz-, Quellen- und Provenienzprüfung

**Verbindlich vor einer Integration pro Repository:** aktuelle `LICENSE`-Datei im gewünschten Commit prüfen, Autoren-/Copyright-Hinweise erhalten, Lizenz für statisches Linken, SaaS, Redistribution und Modifikation prüfen, direkte und transitive Abhängigkeiten erfassen, Drittmarken nicht unberechtigt als Partnerschaft ausgeben.

**Besondere Fälle aus einer stichprobenartigen aktuellen Recherche:**
- Dify: eigene Open-Source-Lizenz auf Apache-2.0-Basis **mit zusätzlichen Bedingungen**, unter anderem für Multi-Tenant-Betrieb und Frontend-Branding (https://github.com/langgenius/dify/blob/main/LICENSE).
- Off Grid AI Desktop: laut Repository AGPL-3.0-only und Open-Core-Aufbau; proprietäre Pro-Komponenten nicht Teil des freien Kerns (https://github.com/off-grid-ai/OGAD).
- Pocket ID: eigenständiger OIDC-/Passkey-Dienst, dessen einfache Bereitstellungsanleitung Docker verwendet; für lokale Scanner daher höchstens Entwurfsreferenz (https://github.com/pocket-id/pocket-id).
- Linagora JMAP TS: eigenständiger TypeScript-Client; seine Integrationstests verwenden Docker/Testcontainers. Der Link ist nicht das im ursprünglichen PDF genannte `audreyt/jmap-client-ts` (https://github.com/linagora/jmap-client-ts).

**Nicht behaupten:** Dass alle 50 Repositories auf aktuelle Funktionsfähigkeit, Sicherheitslage, Lizenzstatus oder Offline-Tauglichkeit geprüft seien. Die zugehörigen Prüfspalten bleiben im CSV ausdrücklich `OFFEN`.

## 13. Abnahmekriterien und Negativtests

| ID | Testfall | Erwartung |
|---|---|---|
| S01 | Modul ohne gültigen Manifest-Hash | keine Aktivierung |
| S02 | manipuliertes Update-Bundle | Import abgebrochen |
| S03 | unbekannte oder überschießende Capability | Policy-Deny |
| S04 | Credentials-/PEM-Pfad in Scanquelle | Zugriff vor Öffnen verweigert |
| S05 | Scanner versucht Netzwerk-Socket | unter der realen Laufzeitisolation technisch blockiert |
| S06 | Isolation nur als Python-Flag vorhanden | Startverbot |
| S07 | Tool erzeugt Output außerhalb genehmigten Zielordners | Aktion blockiert; keine Host-Datei verändert |
| S08 | Agent zitiert nicht existente Quelle | Claim `UNVERIFIED` |
| S09 | Self-Test sagt Pass, unabhängiger Test Fail | Release blockiert |
| S10 | Lizenz für geplanten Vertriebsfall ungeklärt | Release blockiert |
| S11 | Cloud-Agent erhält echte interne Daten | Weitergabe verhindert |
| S12 | Öffentliches Online-Portal überträgt API-Key an Browser | Regressionstest schlägt fehl |
| S13 | OIDC-Token mit falscher Audience | Auth abgelehnt |
| S14 | JMAP-Versand ohne explizite Freigabe | kein Versand |
| S15 | Auto-Update im Offline-Profil | keine Netzwerkaktivität, kein Update |
| S16 | „EU-certified“-Badge ohne externe Nachweise | Anzeige als offiziell zertifiziert blockiert |
| S17 | Backup enthält nicht genehmigte Quellen | Backup fehlgeschlagen |
| S18 | Rollback nach fehlerhaftem Build | vorherige freigegebene Version unverändert |
| S19 | Offlineruntime braucht unvorhergesehene Bibliothek | Start/Release blockiert |
| S20 | Kette von 5 Agenten-Aufgaben mit frühem Fehler | Stopp am ersten unbestätigten Übergang |

**Testdaten:** Für Cloud-Agenten und Agenten-Sicherheit ausschließlich synthetische Beispiele. Für echte lokale Daten nur in der freigegebenen, unabhängig isolierten Umgebung; die automatisierte Freigabe bleibt fail closed.

## 14. Umsetzungsfahrplan (ohne Kalender- oder Fertigstellungsgarantie)

### P0 — Repository Governance & Projektbaseline
**Lieferobjekte:** Repository-Matrix (50), Lizenzakte je Kandidat, Quelle/Commit/Hash, Architektur-Entscheidungsprotokoll (ADR), Risikoregister.  
**Gate:** Keine unbekannte Lizenz oder nicht identifizierte Hauptabhängigkeit für integrierte Komponenten.

### P1 — Trusted Core & Independent Launcher
**Lieferobjekte:** Plugin-Manifestschema, lokaler Registry-Parser, Policy-Layer, unabhängige Isolation-Attestation, synthetische Tests.  
**Gate:** Tests S01–S07 bestanden; bei fehlender OS-Isolation kein UPUIA-Start.

### P2 — Build & Artifact Delivery
**Lieferobjekte:** Tauri-/PWA-Vergleich, AppDir und vollständiges AppImage, Versionierung, Offline-Import, Rollback.  
**Gate:** prüfbares Artefakt, keine impliziten Downloads, kein Host-Umbau.

### P3 — Trust & Compliance Evidence
**Lieferobjekte:** Domain-Trust-Zustände, Evidence-Schema, Quellen-/Jurisdiktionsregister, technische und organisatorische Prüfungen getrennt.  
**Gate:** keine unberechtigte Hochstufung, reproduzierbare Nachweiskette.

### P4 — Agent & Model Intelligence
**Lieferobjekte:** synthetische Benchmark-Suite, optionale Mistral/Dify-Adapter im Onlineprofil, Agentenrollen, unabhängiger Validator.  
**Gate:** BOBA-inspirierte Fehlerketten-Tests S08–S10 und S20 bestanden.

### P5 — Optional Services & Finance
**Lieferobjekte:** opt-in OIDC, JMAP, Read-only-Finanzanalyse, Webstatistik/Calendar und sprachliche Bedienung.  
**Gate:** Benutzerfreigaben, Provider-Scopes, Budgetlimits, Datenschutz- und Vertragsprüfung.

### P6 — Production Assurance
**Lieferobjekte:** voll dokumentierte Release- und Signaturkette, SBOM, Signed Evidence Record, Wiederherstellungstest, Audit-Ausgabe.  
**Gate:** unabhängige Freigabe und nachprüfbare Grenzen des Geltungsbereichs.

## 15. Technische Betriebsstruktur — nur vorgesehener Projektordner

```text
HCOS-FORINA-TITAN/
  docs/                         # Konzepte, ADRs, Risiko- und Lizenzakten
  config/                       # signierte, geprüfte Konfigurationen
  module-registry/              # nur freigegebene Modulmanifeste
  adapters/                     # offline vs. online physisch getrennt
    offline/
    federation/
  policies/                     # OPA-Regeln + externe Enforcement-Verträge
  pipeline/                     # Plans, Build, Verify, Release
  synthetic-tests/              # künstliche Beispielbestände
  evidence/                     # zulässige Metadaten, keine sensiblen Inhalte
  release-inbox/                # offline importierte, signierte Pakete
  releases/                     # fertige AppImages, PWAs, Reports
  rollback/                     # vorherige, freigegebene Releases
```

Das ist ein **Zielverzeichnis**, keine Aussage, dass es bereits so auf deinem Rechner existiert. Keine automatischen Installationen, Änderungen an der OS-Konfiguration, Hintergrunddienste oder Container im UPUIA-Betriebsprofil.

## 16. Architektur-Risikoregister

| Risiko | Auswirkung | Gegenmaßnahme |
|---|---|---|
| ungeprüfte Dritt-Abhängigkeit | Lieferkettenangriff | Commit-Pinning, Prüfung, SBOM, Signatur |
| falsche 100%-Statusmeldung | Scheinsicherheit | messbare unabhängige Tests, Statushierarchie |
| gemeinsam genutztes Agenten-/Scanner-Privileg | Datenabfluss | strikte Trust Boundary, getrennte Prozesse |
| nicht durchsetzbare Netzsperre | Leakage | fail-closed und kein Produktivlauf |
| Dynamisches Remote-Modul | Code-Injection | lokale Allowlist, signierter Import |
| Fehlerketten von Agenten | kaputte Releases | unabhängiges Test-Gate pro Stufe |
| Secret-Scanner liest echte Schlüssel | Verbotsbruch | Synthetic-only-Scannerprofil |
| unklare Dify-/AGPL-/UI-Lizenzen | Vertriebskonflikt | commitbezogene juristische Lizenzprüfung |
| Online-Connector mit zu breitem Scope | Datenmissbrauch | Least Privilege, Zustimmung, Widerruf |
| eigene Badges als Behördenzertifikate | Falschdarstellung | ausschließlich belegte Claims |
| Update- und Backupseiteneffekte | Hoständerung / Datenkopie | getrennte Betriebsprofile und output allowlist |
| Dokumenten-Indexierung ohne Quellenkontrolle | falsche Compliance-Zuordnung | Herkunft/Datum/Version je Beleg |

## 17. Erfolgsmessung (KPIs)

- **0** akzeptierte unautorisierte Datei-, Netzwerk- und Credential-Zugriffe in Negativtests (kein absoluter Sicherheitsbeweis).
- **100 %** signaturpflichtiger Release-Artefakte mit unabhängiger, erfolgreicher Verifikation.
- **100 %** aktiver Module mit gültigem Manifest, dokumentierter Lizenzentscheidung und nachvollziehbarer Policy-Freigabe.
- **100 %** fachlicher Compliance-Behauptungen mit maschinenlesbarer Quelle, Geltungsbereich, Version, Prüfer und Datum.
- **0** Veröffentlichungen eines externen Zertifizierungsstatus ohne belegte autoritative Quelle.
- Für BOBA-/Agentenworkflows: Erfolgsquote nicht nur pro Einzelschritt, sondern *End-to-End*; Fehlerschritt führt zum Kettenstopp.
- Reproduzierbar dokumentierte Offline-Starts, Update-Imports und Restore-/Rollback-Tests.

## 18. Entscheidungsübersicht

**Sofort als Architekturkern spezifizieren:** Registry + unabhängiger Preflight, OPA/Policy, Evidence-Schema, Build-Manifest, Tauri/PWA-Releasepfad, Testkette.  
**Zweitens testen:** RxDB, JMAP, Domain-Trust-Adapter, BOBA, kontrollierte UI-Bibliotheken.  
**Drittens optional integrieren:** Online-OIDC, Calendar, Mailserver, Analytik, KI-Provider, Finance-API.  
**Explizit nicht einfach einschalten:** Remote-JavaScript-Loader, Auto-Update im Offline-Profil, Cloud-Agenten mit Originaldaten, Secret-Session-Scanner mit realem Zugangsdatenzugriff, unkontrolliertes Crawling, automatische Zahlungsaktionen.

---

## 19. Anhang A — Vollständige Repository-Zuordnung aller 50 Einträge

**Lesart:** Die Empfehlungen sind Konzeptentscheidungen, keine Aussagen über heute getestete Betriebssicherheit. `Pilot` bedeutet „für einen **isolierten** Proof-of-Concept nach Lizenz-/Sicherheitsprüfung priorisiert“, nicht „bereits geprüft oder produktionsreif“. `Reference only` bedeutet „Architektur vergleichen, nicht als Pflichtabhängigkeit“. `Deferred` bedeutet „erst später, nach ausdrücklichem Bedarf und gesonderter Prüfung“. `Online optional` ist im UPUIA-Offlinelauf **nicht erlaubt**.

| Nr. | Repository | Zweck in HCOS | Entscheidung | PDF-Seite |
|---:|---|---|---|---|
| 1 | [`tauri-apps/tauri`](https://github.com/tauri-apps/tauri) | Desktop Shell | Pilot | Tool Build Processing S. 5 |
| 2 | [`AppImage/AppImageKit`](https://github.com/AppImage/AppImageKit) | AppImage format/runtime | Pilot | Tool Build Processing S. 5 |
| 3 | [`javascript-obfuscator/javascript-obfuscator`](https://github.com/javascript-obfuscator/javascript-obfuscator) | JS-Obfuskation | Optional | Tool Build Processing S. 5 |
| 4 | [`borgbackup/borg`](https://github.com/borgbackup/borg) | Backup | Pilot | Tool Build Processing S. 5 |
| 5 | [`caddyserver/caddy`](https://github.com/caddyserver/caddy) | Reverse Proxy | Online optional | Tool Build Processing S. 5 |
| 6 | [`nginx/nginx`](https://github.com/nginx/nginx) | Reverse Proxy alternative | Online optional | Tool Build Processing S. 5 |
| 7 | [`cunnie/sslip.io`](https://github.com/cunnie/sslip.io) | DNS development routing | Reference only | Tool Build Processing S. 5 |
| 8 | [`exentriquesolutions/nip.io`](https://github.com/exentriquesolutions/nip.io) | DNS development routing alternative | Reference only | Tool Build Processing S. 5 |
| 9 | [`greensock/GSAP`](https://github.com/greensock/GSAP) | UI animation | Optional | Tool Build Processing S. 5 |
| 10 | [`mrdoob/three.js`](https://github.com/mrdoob/three.js) | 3D interface | Optional | Tool Build Processing S. 5 |
| 11 | [`catdad/canvas-confetti`](https://github.com/catdad/canvas-confetti) | Decorative effects | Optional | Tool Build Processing S. 5 |
| 12 | [`goldfire/howler.js`](https://github.com/goldfire/howler.js) | Audio UI | Optional | Tool Build Processing S. 5 |
| 13 | [`react-grid-layout/react-grid-layout`](https://github.com/react-grid-layout/react-grid-layout) | Dashboard layout | Optional | Tool Build Processing S. 5 |
| 14 | [`ueberdosis/tiptap`](https://github.com/ueberdosis/tiptap) | Rich text editor | Optional | Tool Build Processing S. 5 |
| 15 | [`codex-team/editor.js`](https://github.com/codex-team/editor.js) | Block editor alternative | Optional | Tool Build Processing S. 5 |
| 16 | [`framer/motion`](https://github.com/framer/motion) | UI motion | Optional | Tool Build Processing S. 5 |
| 17 | [`pocket-id/pocket-id`](https://github.com/pocket-id/pocket-id) | Passkey OIDC provider | Online optional | Tool Build Processing S. 5 |
| 18 | [`authelia/authelia`](https://github.com/authelia/authelia) | Access proxy/MFA | Online optional | Tool Build Processing S. 5 |
| 19 | [`yeojz/otplib`](https://github.com/yeojz/otplib) | TOTP helper | Optional | Tool Build Processing S. 6 |
| 20 | [`soldair/node-qrcode`](https://github.com/soldair/node-qrcode) | QR codes | Optional | Tool Build Processing S. 6 |
| 21 | [`orestbida/cookieconsent`](https://github.com/orestbida/cookieconsent) | Consent UI | Optional | Tool Build Processing S. 6 |
| 22 | [`langgenius/dify`](https://github.com/langgenius/dify) | Agent/RAG platform | Reference only | Tool Build Processing S. 6 |
| 23 | [`vercel/ai`](https://github.com/vercel/ai) | LLM frontend adapter | Pilot | Tool Build Processing S. 6 |
| 24 | [`ffmpegwasm/ffmpeg.wasm`](https://github.com/ffmpegwasm/ffmpeg.wasm) | Video processing in browser | Optional | Tool Build Processing S. 6 |
| 25 | [`videojs/video.js`](https://github.com/videojs/video.js) | Video player | Optional | Tool Build Processing S. 6 |
| 26 | [`johannesjo/super-productivity`](https://github.com/johannesjo/super-productivity) | Personal task management | Reference only | Tool Build Processing S. 6 |
| 27 | [`open-policy-agent/opa`](https://github.com/open-policy-agent/opa) | Policy-as-code | Pilot | Tool Build Processing S. 6 |
| 28 | [`audreyt/jmap-client-ts`](https://github.com/linagora/jmap-client-ts) | JMAP adapter | Optional | Tool Build Processing S. 6 |
| 29 | [`stalwartlabs/mail-server`](https://github.com/stalwartlabs/mail-server) | JMAP email server | Online optional | Tool Build Processing S. 6 |
| 30 | [`umami-software/umami`](https://github.com/umami-software/umami) | Web analytics | Online optional | Tool Build Processing S. 6 |
| 31 | [`plausible/analytics`](https://github.com/plausible/analytics) | Web analytics alternative | Online optional | Tool Build Processing S. 6 |
| 32 | [`calcom/cal.com`](https://github.com/calcom/cal.com) | Booking/calendar service | Online optional | Tool Build Processing S. 6 |
| 33 | [`AppImageCommunity/AppImageUpdate`](https://github.com/AppImageCommunity/AppImageUpdate) | AppImage update utility | Deferred | Tool Build Processing S. 19 |
| 34 | [`tauri-apps/plugins-workspace`](https://github.com/tauri-apps/plugins-workspace) | Tauri plugins | Pilot | Tool Build Processing S. 19 |
| 35 | [`Cap-go/capacitor-updater`](https://github.com/Cap-go/capacitor-updater) | Mobile OTA optional | Deferred | Tool Build Processing S. 19 |
| 36 | [`electron-userland/electron-builder`](https://github.com/electron-userland/electron-builder) | Electron packaging alternative | Reference only | Tool Build Processing S. 19 |
| 37 | [`module-federation/core`](https://github.com/module-federation/core) | Microfrontend federation | Deferred | Tool Build Processing S. 19 |
| 38 | [`originjs/vite-plugin-federation`](https://github.com/originjs/vite-plugin-federation) | Vite federation option | Deferred | Tool Build Processing S. 19 |
| 39 | [`single-spa/single-spa`](https://github.com/single-spa/single-spa) | Microfrontend app orchestration | Reference only | Tool Build Processing S. 19 |
| 40 | [`systemjs/systemjs`](https://github.com/systemjs/systemjs) | Dynamic JS module loader | Avoid for trusted core | Tool Build Processing S. 19 |
| 41 | [`GoogleChrome/workbox`](https://github.com/GoogleChrome/workbox) | PWA cache strategy | Pilot | Tool Build Processing S. 19 |
| 42 | [`vite-pwa/vite-plugin-pwa`](https://github.com/vite-pwa/vite-plugin-pwa) | PWA packaging | Pilot | Tool Build Processing S. 19 |
| 43 | [`pwa-builder/PWABuilder`](https://github.com/pwa-builder/PWABuilder) | PWA packaging toolkit | Reference only | Tool Build Processing S. 19 |
| 44 | [`ionic-team/capacitor`](https://github.com/ionic-team/capacitor) | Mobile bridge | Deferred | Tool Build Processing S. 19 |
| 45 | [`tw93/Pake`](https://github.com/tw93/Pake) | Desktop wrapper alternative | Reference only | Tool Build Processing S. 19 |
| 46 | [`pubkey/rxdb`](https://github.com/pubkey/rxdb) | Local-first database | Pilot | Tool Build Processing S. 19 |
| 47 | [`amazon-agi/BOBA-bench`](https://github.com/amazon-agi/BOBA-bench) | Agent-chain benchmark | Pilot | Claude Finds Your Money Leaks S. 11 |
| 48 | [`off-grid-ai/OGAM`](https://github.com/off-grid-ai/OGAM) | Offline mobile AI reference | Reference only | Claude Finds Your Money Leaks S. 12 |
| 49 | [`off-grid-ai/OGAD`](https://github.com/off-grid-ai/OGAD) | Offline desktop AI reference | Evaluate | Claude Finds Your Money Leaks S. 12 |
| 50 | [`AGGIB/Stroq`](https://github.com/AGGIB/Stroq) | Agent session security | Synthetic test only | Claude Finds Your Money Leaks S. 12 |

### Herkunft der Linkeinträge
- Nummern **1–27 und 29–46**: direkte GitHub-URLs aus dem ursprünglichen 27-seitigen PDF.
- Nummer **28**: Das Original verweist laut Katalog auf eine Google-Suche für `audreyt/jmap-client-ts`. Die angegebene Linagora-URL ist **ein separater, recherchierter Ersatz**, nicht das identische Projekt.
- Nummern **47–50**: aus dem Claude-Newsletter abgeleitete, ergänzend recherchierte GitHub-Repositories; der Newsletter enthielt keine direkte GitHub-URL dafür.
- Die Katalogzählung „50“ bedeutet **50 Datensätze**, nicht 50 auditierte oder integrierte Projekte.

## 20. Anhang B — Verifizierungsstand dieser Konzeption

**Stichprobenweise aktuelle Online-Quellen:**
- Dify Lizenz: https://github.com/langgenius/dify/blob/main/LICENSE
- Dify Selfhosting: https://github.com/langgenius/dify
- Pocket ID OIDC/Passkeys: https://github.com/pocket-id/pocket-id
- Linagora JMAP TypeScript und Testvoraussetzungen: https://github.com/linagora/jmap-client-ts
- AppImage AppDir/AppImage-Trennung: https://docs.appimage.org/introduction/concepts.html
- AppImageTool Dokumentation: https://docs.appimage.org/introduction/software-overview.html
- AppImageUpdate Stand: https://github.com/AppImageCommunity/AppImageUpdate
- Stroq sicherheitsrelevante Grenzen: https://stroq.dev/docs/
- Off Grid AI Desktop Open Core: https://github.com/off-grid-ai/OGAD

**Ausdrücklich nicht in diesem Konzept durchgeführt:** Installation, Clone, Build, ausführende Penetrationstests, vollständige Prüfung aller 50 Lizenzen, vollständige CVE/SBOM-Auswertung oder rechtliche Zertifizierung. Jeder aktivierte Kandidat benötigt eine separate, commitbezogene Evaluation.

**Schlussfolgerung:** Der belastbare Mehrwert liegt nicht in der Anzahl eingebundener Repositories, sondern in der klaren Trennung von Source-Intake, erlaubter Runtime, unabhängiger Verifikation und tatsächlicher Freigabe. So kann aus HCOS FORINA TITAN eine langfristig erweiterbare Plattform werden, ohne die strengen Datenschutz-, Integritäts- und Isolationsziele aufzugeben.
