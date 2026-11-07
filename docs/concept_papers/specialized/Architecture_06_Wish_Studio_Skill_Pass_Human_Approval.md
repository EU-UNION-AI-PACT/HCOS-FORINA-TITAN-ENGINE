# Architecture 06 — Wish Studio OS: Developer & Community Innovation Hub, Digital Skill Pass & Sovereign Human Approval Gate

**Dokument-ID:** ARCH-SPEC-06-WISH-STUDIO-SKILL-PASS-APPROVAL  
**Sovereign Provenance & Urheber:** Daniel Pohl · Royal Kaiser Charter RegSys  
**Rechtliche Registrierungen & Identifikatoren:**  
- EU Transparency & Research: PIC 867679357 & 873042778  
- Steuerliche Identifikation: USt-IdNr. DE31353063511 & DE441892129  
- Unternehmensidentifikatoren: D-U-N-S 315676980 & 317066336 · Global LEI 894500GBJSIW8L6ET310  
- Internationale Register: UNGM 1172700 · EORI AEOF139420 · Swiss AHV 756.6199.0539.28  
- Akademische Register: ORCID 0009-0004-0348-9769 · Scopus EX2025D1143002  
**Lizenz:** European Union Public Licence (EUPL-1.2) · Sovereign Fail-Closed Boundary  
**Klassifizierung:** KANONISCHES GEMEINWOHL- & INNOVATIONS-ARCHITEKTURPAPIER (WISH OS v2.15)  

---

## 1. Executive Summary & Philosophische Grundlegung

Das **Wish Studio OS** ist eine sovereign-föderierte, nutzergesteuerte Innovations- und Entwicklungsplattform.  
Im fundamentalen Gegensatz zu herkömmlichen Plattformen, die entweder bloße Feedback-Listen verwalten oder riskante, unkontrollierte Vollautomatisierung betreiben, etabliert Wish Studio ein **menschlich kontrolliertes Entwicklungs- und Freigabeparadigma mit verbindlichen Assurance-Gates**:

> **„Nicht der Nutzer muss lernen, wie eine Funktion programmiert wird. Er beschreibt, was er benötigt – und das System organisiert die strukturierte Entwicklung mit menschlicher Letztentscheidung und transparentem Kompetenznachweis.“**

Die Plattform kombiniert:
1. **Wish Portal (Wunschintegration):** Natürliche Sprachbeschreibung von Feature- und Tool-Wünschen.
2. **AI Planning & Decomposition:** KI-gestützte Architekturzerlegung, Aufgabenverteilung und Sandbox-Spezifikation.
3. **Developer Workspace:** Ehrenamtliche Entwickler, Paarprogrammierung, Git-Worktree-Isolation.
4. **Digitaler Skill Pass:** W3C Verifiable Credentials (VC) und Decentralized Identifiers (DID:tdw / DID:cheqd / swiyu Swiss e-ID kompatibel) zur manipulationssicheren Kompetenzdokumentation.
5. **Sovereign Human Approval Gate (Gate G09 Alignment):** Absolute menschliche Letztentscheidung (Daniel Pohl / autorisiertes Sovereign Team). Null autonome Produktiv-Deployments ohne explizites menschliches Sign-Off.
6. **Release & Community Distribution:** Private Sandbox-Nutzung, optionale Freigabe für Teams oder weltweite Community unter EUPL-1.2.

---

## 2. Der 6-Stufen Lebenszyklus (End-to-End Workflow)

```
[1. Wish Portal]        --> [2. AI Planning]       --> [3. Developer Workspace]
 (Nutzerwunsch)              (Spezifikation)            (Ehrenamt / Team)
                                                               |
                                                               v
[6. Community Release]  <-- [5. Human Approval]    <-- [4. Digital Skill Pass]
 (Privat / EUPL-1.2)         (Gate G09 Sign-Off)        (W3C DID / swiyu)
```

### Stufe 1: Wish Portal (Persönliche Wunschintegration)
- Nutzer formulieren Anforderungen in freier Sprache (z.B. „Exportiere Chat inklusive Tabellen und SVG-Vektoren als auditierbares ZIP-Archiv“).
- Der Intake-Validator prüft den Wunsch auf ethische und regulatorische Grundkonformität (Zero-Harassment, DSGVO Art. 25, Privacy-by-Design).
- Der Wunsch erhält eine unveränderliche UUID und einen kryptografischen Timestamp.

### Stufe 2: AI Planning & Task Decomposition
- Das AI Planning Module zerlegt den Wunsch in modulare Aufgabenpakete:
  - Frontend / UI-Komponenten (uGUI, CSS3/HTML5, Web Components).
  - Backend / Business-Logik (Python 3.11+, REST API, Dataform Pipelines).
  - Sicherheits- und Compliance-Prüfpunkte (Gate G00-G12).
- Festlegung der Sandbox-Grenzen: Welche APIs, Speicherbereiche und Berechtigungen benötigt das Tool?

### Stufe 3: Developer & Volunteer Workspace (Ehrenamtliche Zusammenarbeit)
- Registrierte Entwickler und Community-Mitglieder können Aufgabenpakete übernehmen.
- Isolierte Git-Worktree-Umgebungen verhindern Seiteneffekte auf den Hauptzweig.
- Pair-Programming-Support mit lokalen AI-Modellen (Offline / Loopback, keine Datenabflüsse).

### Stufe 4: Digitaler Skill Pass (W3C DID / VC Kompetenzmanagement)
- Jeder erfolgreich gemergte und validierte Commit fließt in den **Digitalen Skill Pass** des Entwicklers ein.
- Das Kompetenzmanagement basiert auf dem Schweizer Bundesamt für Justiz (BJ) swiyu-Standard und W3C Verifiable Credentials:
  - DID-Methoden: `did:tdw` (Trust-DID-Web) und `did:cheqd`.
  - Level-Klassifizierung: **Bronze** (Foundation), **Silver** (Intermediate), **Gold** (Advanced Core), **Titan** (Sovereign Master).
  - Kryptografisch unveränderbare Attestierungen mit Ed25519-Signaturen.

### Stufe 5: Sovereign Human Approval Gate (Gate G09 Integration)
- **Kernprinzip:** Keine autonome Bereitstellung in die Produktionsumgebung.
- Der Wunschgeber (Daniel Pohl bzw. das autorisierte Sovereign Governance Team) erhält das vollständige Audit-Dossier:
  - Quellcode-Diff, Testergebnisse, Stroq-Scanner-Audit (0 Secrets, 0 Leaks).
  - Vorschau in einer isolierten Staging-Sandbox.
- **Entscheidungsoptionen des Wunschgebers:**
  - `GENEHMIGT`: Freigabe zur lokalen Installation.
  - `AENDERUNG_GEFORDERT`: Detaillierte Rückmeldung an Entwickler / KI mit konkreten Nachbesserungsauflagen.
  - `ABGELEHNT`: Vollständiger Rollback ohne Rückstände.

### Stufe 6: Release & Community Distribution
- **Private Bereitstellung:** Tool steht exklusiv dem Wunschgeber in seiner persönlichen HCOS-Umgebung zur Verfügung.
- **Team-Freigabe:** Übertragung in geschützte Arbeitsgruppen über verschlüsselte Registrys.
- **Open-Source Community Release:** Freiwillige Veröffentlichung unter EUPL-1.2 im offiziellen HCOS-Katalog.

---

## 3. Technische Spezifikation des Digital Skill Pass

### JSON-LD Verifiable Credential Schema (swiyu / W3C Standard)
```json
{
  "@context": [
    "https://www.w3.org/2018/credentials/v1",
    "https://schema.org",
    "https://admin.ch/bj/swiyu/credentials/v1"
  ],
  "id": "urn:uuid:85550b82-143d-4b06-9aa1-d33c73584984",
  "type": ["VerifiableCredential", "CivicDeveloperSkillPass"],
  "issuer": {
    "id": "did:tdw:eu.royal-kaiser-charter:regsys",
    "name": "Daniel Pohl · Royal Kaiser Charter RegSys",
    "lei": "894500GBJSIW8L6ET310",
    "pic": "867679357"
  },
  "issuanceDate": "2026-11-07T21:00:00Z",
  "credentialSubject": {
    "id": "did:tdw:volunteer.dev:community-id",
    "competenceLevel": "TITAN",
    "verifiedSkills": [
      "Assurance Gate G00-G12 Verification",
      "Fail-Closed Security Architecture",
      "Zero-Image Compliance in Git",
      "W3C DID / VC Protocol Integration"
    ],
    "contributedProjects": 352,
    "auditHash": "cda7928fe71991870963ba0b04ed77c0..."
  },
  "proof": {
    "type": "Ed25519Signature2020",
    "created": "2026-11-07T21:00:00Z",
    "verificationMethod": "did:tdw:eu.royal-kaiser-charter:regsys#key-1",
    "proofPurpose": "assertionMethod",
    "proofValue": "z3gChV4..."
  }
}
```

---

## 4. Konformitätsmatrix & Sicherheits-Invarianten

| Invariante | Anforderung | Technische Durchsetzung |
|---|---|---|
| **INV-WISH-01** | Zero Autonomous Deployment | Hard Gate G09 in `forina_engine/assurance_gates.py` erzwingt manuelles Sign-Off |
| **INV-WISH-02** | Privacy by Design | Vollständige Trennung privater Wunschtools von öffentlichen Registries |
| **INV-WISH-03** | Zero-Leak Guarantee | Stroq-Scanner prüft jeden Pull Request vor der Zuteilung an Entwickler |
| **INV-WISH-04** | Verifiable Identity | Swiyu-kompatible W3C DID-Attestierungen mit Ed25519 (RFC 8032) |
| **INV-WISH-05** | Rollback Readiness | 1-Klick Rückbau jedes integrierten Tools ohne Datenverlust |

---

## 5. Fazit & Integrationsstatus

Das Wish Studio OS vollendet die Vision einer souveränen, demokratisierten Softwareentwicklung:
Es befähigt Menschen ohne Programmierkenntnisse zur Realisierung maßgeschneiderter Softwarewerkzeuge, belohnt ehrenamtliche Entwickler mit staatlich anschlussfähigen Kompetenznachweisen und garantiert dem Wunschgeber und Daniel Pohl die uneingeschränkte, unantastbare Kontrolle über jede Codezeile, die sein System betritt.
