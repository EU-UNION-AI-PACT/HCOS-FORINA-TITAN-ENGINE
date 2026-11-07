---
title: "GlobalCards Bank – Internationale Banking- und Karteninfrastruktur"
version: "1.0.0"
date: "2026-11-07"
author: "Daniel Pohl · Royal Kaiser Charter RegSys"
classification: "CONFIDENTIAL / SOVEREIGN ARCHITECTURE SPECIFICATION"
status: "APPROVED_SPECIFICATION"
---

# GlobalCards Bank – Internationale Banking- und Karteninfrastruktur

Dein Vier-Phasen-Konzept ist eine gute Grundlage. Ich würde daraus eine modulare, international erweiterbare Fintech-Plattform entwickeln, die zunächst als Software- und Integrationsplattform funktioniert und später über regulierte Partner Bankkonten, IBANs, Karten, Multi-Currency-Wallets und Zahlungsabwicklung bereitstellen kann.

[For years, sending money across borders was harder than it should be. From today, it isn’t.  OrbitX introduces Borderless Banking.  We began with a card. Today, the journey comes full circle.  What’s… | OrbitX | 63 comments](https://images.openai.com/static-rsc-4/ApsN9jQ77pS-wRSsBqVhTM50hNdVzggts0j9RTmTC4sx1udcWcnDmNndUR6cjtqqmOwZXnOjCZjczGbTtEAYzVtSx6Du0dOO4HTef8ymyrkFn7G12_nBEOdfaFd9DfuiNHWp_tBQLgv86Yspt_ewKgCISjmat6Isd89YXnxdRhE?purpose=inline)

[linkedin.com](https://www.linkedin.com/feed/update/urn%3Ali%3Aactivity%3A7424133503795142656/)

Visuelle Designrichtung für GlobalCards Bank – Konzeptillustration, keine bestehende Banking-App.

## 1. Die erweiterte Systemarchitektur

GlobalCards Bank Interface

Web · iOS · Android · Business Dashboard

API Gateway & Identity Layer

OAuth 2.0 · OIDC · Passkeys · Consent · RBAC

Core Banking

Konten · Ledger · IBAN

Card Engine

Visa · Mastercard · Token

Payments

SEPA · SWIFT · FX

Compliance

KYC · AML · DORA

Treasury

Liquidität · Settlement

Partner Hub

BaaS · Open Banking

Regulierte Partner & Finanznetzwerke

Lizenzierte Banken · E-Geld-Institute · Karten-Sponsoren · Prozessoren

## 2. Zwölf zentrale Entwicklungsmodule

| Modul              | Funktion                                               |
| ------------------ | ------------------------------------------------------ |
| GC-01 Identity     | KYC, KYB, Passkeys und Identitätsverwaltung            |
| GC-02 Accounts     | IBAN, virtuelle Konten und Kontoverwaltung             |
| GC-03 Ledger       | Doppelte Buchführung, Salden, Buchungsjournal          |
| GC-04 Cards        | Virtuelle und physische Debit-/Kreditkarten            |
| GC-05 Payments     | SEPA, SEPA Instant, SWIFT und internationale Transfers |
| GC-06 Currency     | Multi-Currency, Wechselkurse und FX                    |
| GC-07 Settlement   | Clearing, Abgleich und Zahlungsabschluss               |
| GC-08 Treasury     | Liquiditäts- und Reserveverwaltung                     |
| GC-09 Compliance   | AML, Sanktionsprüfung, Transaktionsmonitoring          |
| GC-10 Security     | PCI DSS, HSM, Schlüsselverwaltung, Audit               |
| GC-11 Open Banking | PSD2/Open-Banking-Konnektoren                          |
| GC-12 Governance   | DORA, DSGVO, Risiko- und Nachweismanagement            |

## 3. Technologischer Entwicklungsstack

Ich würde eine Kombination aus Open-Source-Komponenten und austauschbaren Partner-APIs vorsehen.

| Ebene              | Technologieoptionen                          |
| ------------------ | -------------------------------------------- |
| Frontend           | React, Next.js, Flutter                      |
| Backend            | Go, Rust, TypeScript                         |
| Datenbanken        | PostgreSQL, Redis                            |
| Buchhaltung        | TigerBeetle oder eigener Double-Entry-Ledger |
| IAM                | Keycloak, OpenID Connect                     |
| API                | OpenAPI, REST, gRPC                          |
| Event-Verarbeitung | NATS oder Kafka                              |
| Monitoring         | OpenTelemetry, Prometheus                    |
| Infrastruktur      | Linux, reproduzierbare Builds                |
| Compliance         | OSCAL, Policy-as-Code, Evidence Registry     |

Wichtig: Diese Technologien bilden die Softwarebasis, ersetzen aber keine Banklizenz, Kartenmitgliedschaft oder regulatorische Genehmigung.

## 4. Entwicklungs-Roadmap

01

Foundation & Compliance

Monat 1–3

Geschäftsmodell, Rechtsprüfung, Datenmodell, Bedrohungsmodell, Partneranforderungen.

02

Core Banking MVP

Monat 4–6

Testkonten, Ledger, Transaktionssimulation, APIs, Identitäts- und Rechteverwaltung.

03

Card & Payment Integration

Monat 7–10

Sandbox-Anbindung an Issuing-Prozessoren, BaaS-Partner und Zahlungsnetzwerke.

04

Security & Certification Readiness

Monat 11–14

Penetrationstests, PCI-DSS-Scope, DORA-Kontrollen, Ausfallsicherheit und Audit-Nachweise.

05

Controlled Launch

Ab Monat 15

Pilotbetrieb mit zugelassenen Partnern, anschließend schrittweise Expansion.

Die Zeitangaben sind Planungsannahmen, keine garantierten Implementierungs- oder Genehmigungsfristen.

## 5. Meine Architekturentscheidung

Für GlobalCards Bank würde ich zunächst das BaaS-/Partner-Modell mit eigenem, unabhängigem Softwarekern bevorzugen. Damit lassen sich Funktionen kontrolliert entwickeln, ohne sofort eine eigene Vollbanklizenz anzustreben.

Besonders wichtig wären:

- Ein unveränderbares, nachvollziehbares Transaktionsjournal mit idempotenter Verarbeitung.
- Eine Settlement Engine mit automatischer Abstimmung und manueller Freigabe bei Abweichungen.
- Strikte Trennung zwischen simulierten Guthaben, tatsächlichen Kundengeldern und Partnerbankkonten.
- Ein Compliance Evidence Graph für technische Prüfungen und regulatorische Nachweise.
- Keine Speicherung vollständiger Kartendaten, soweit ein tokenisiertes Modell möglich ist.
- Ein Fail-Closed-Betriebsmodell bei kritischen Sicherheits- oder Zahlungsfehlern.

Die Bezeichnung „Bank“ und die konkrete Vermarktung müssten vor einem realen Start rechtlich geprüft werden. Ein BaaS-Vertrag überträgt auch nicht automatisch sämtliche regulatorischen Pflichten auf den Partner.

## 6. Welche Ausbaurichtung soll GlobalCards Bank erhalten?

Geschäfts- und Betriebsmodell

Reine Software- und Integrationsplattform

Fintech mit Banking-as-a-Service-Partnern

Hybride internationale Banking- und Kartenplattform

Eigenständige lizenzierte Bank

Zielgruppe

Privatkunden (B2C)

Geschäftskunden (B2B)

Beide, mit separaten Funktionen

Vollständiges GlobalCards-Bank-Konzept erstellen&#x20;

Damit können wir GlobalCards Bank als tatsächlich implementierbares Projekt spezifizieren – von der ersten Testtransaktion bis zur regulierten internationalen Karten- und Zahlungsinfrastruktur.
# GlobalCards Bank

Master Implementation Blueprint · Version 1.0 · November 2026

Hybride internationale Banking-, Karten-, Zahlungs- und Finanzinfrastruktur für Privatkunden (B2C) und Geschäftskunden (B2B)

[Stripe Expands Global Money Management Tools to Boost UK Business Operations - FinTech Weekly](https://images.openai.com/static-rsc-4/aOBb1ZqNc-yiZP2T9PFY4GzIC7vN4sVt_No0UffgRPRtR7r7dHEgrwvtLBX7lod__-fVKV9thkC4liNwWf3QAnCUqhdEO2ewDuuoBlW-RdVODuXmTu3PVNOItDmnP-QxeVDL2P7wuSyLtO0ax6o6mIltAbIpuWxJTKxfTXiHLS0?purpose=inline)

[fintechweekly.com](https://www.fintechweekly.com/magazine/articles/stripe-global-money-management-uk-business-expansion)

## Executive Summary

GlobalCards Bank wird als modular aufgebaute Finanztechnologieplattform konzipiert, die eigene Softwareinfrastruktur mit den Dienstleistungen lizenzierter Banken, E-Geld-Institute, Kartenherausgeber und Zahlungsdienstleister verbindet.

Die Plattform soll langfristig Konten, IBANs, internationale Kartenzahlungen, Multi-Currency-Wallets, Open Banking, Echtzeittransaktionen, automatisiertes Settlement, Treasury-Funktionen und regulatorische Nachweisführung auf einer einheitlichen technologischen Grundlage bereitstellen.

Der entscheidende Architekturgrundsatz lautet:

GlobalCards kontrolliert die eigene Technologie, aber führt regulierte Finanzdienstleistungen nur im Rahmen der jeweils erforderlichen eigenen Zulassung oder über entsprechend berechtigte Vertragspartner aus.

Geschäftsmodell

Hybrid B2C + B2B

Startregion

Deutschland / EWR

Expansion

International, je Land

Architektur

API-First · Modular

Sieben strategische Säulen

Banking & Accounts

Card Issuing

Payments & Settlement

Multi-Currency & FX

Compliance & Security

Partner Connectivity

Data Sovereignty

## 1. Zielbild und Produktumfang

Die Plattform wird in vier Produktfamilien unterteilt.

| Produktfamilie  | B2C                                         | B2B                                       |
| --------------- | ------------------------------------------- | ----------------------------------------- |
| Konten und IBAN | Persönliche Konten, Unterkonten             | Geschäftskonten, virtuelle IBANs          |
| Karten          | Virtuelle und physische Karten              | Mitarbeiter-, Team- und Ausgabenkarten    |
| Zahlungen       | SEPA, Instant, internationale Überweisungen | Massenzahlungen, Rechnungen, Auszahlungen |
| Währungen       | Multi-Currency, FX                          | FX-Management, internationale Abrechnung  |
| Open Banking    | Kontenübersicht, Einwilligungen             | Multi-Bank-Treasury, Kontenaggregation    |
| Automatisierung | Sparregeln, Benachrichtigungen              | Freigabeketten, Zahlungsworkflows         |
| Reporting       | Umsätze, Exporte                            | Buchhaltung, Reconciliation, API-Reports  |

Kreditvergabe, Einlagengeschäft, Wertpapierhandel, Kryptoverwahrung und Investmentprodukte sind ausdrücklich separate, später zu genehmigende Produktlinien. Sie gehören nicht automatisch zum Startumfang.

## 2. Referenzarchitektur

Customer Experience Layer

GlobalCards Web · Mobile · Business Portal · Partner Portal

Identity, Consent & API Gateway

Passkeys · OAuth/OIDC · Rate Limiting · WAF · Authorization

Customer & KYB

Identität, Organisationen, Rollen

Accounts & Ledger

Konten, Salden, Journal

Card Management

Issuing, Token, Limits

Payment Orchestrator

SEPA, Instant, SWIFT

FX & Treasury

Kurse, Liquidität, Positionen

Risk & Compliance

AML, Screening, Case Management

Settlement Engine

Clearing, Abgleich, Ausnahmen

Evidence & Audit

Nachweise, Kontrollen, Prüfungen

Financial Connectivity & Partner Adapter Layer

BaaS · Issuing Processor · Payment Rails · Open Banking · FX

Regulierte externe Infrastruktur

Banken · EMI · Visa/Mastercard-Sponsoren · Zahlungsnetzwerke · Verwahrstellen

Die Architektur verwendet einen eigenen internen Ledger als Buchungs- und Abstimmungsgrundlage. Die rechtlich maßgeblichen Kontostände und Verbindlichkeiten müssen mit den Systemen der jeweiligen kontoführenden Institute übereinstimmen.

### 2.1 Technologiestack

| Komponente        | Primäre Empfehlung                          | Alternative                 |
| ----------------- | ------------------------------------------- | --------------------------- |
| Web               | Next.js, TypeScript                         | React SPA                   |
| Mobile            | Flutter                                     | Native Swift/Kotlin         |
| Backend           | Go                                          | Rust, Java                  |
| Ledger            | PostgreSQL mit Double-Entry-Engine          | TigerBeetle nach Evaluation |
| Relationale Daten | PostgreSQL                                  | CockroachDB nach Evaluation |
| Events            | NATS JetStream                              | Kafka                       |
| Identity          | Keycloak                                    | Kommerzieller IAM-Dienst    |
| Secrets/HSM       | HSM/KMS mit kontrolliertem Schlüsselzugriff | On-Premises HSM             |
| Observability     | OpenTelemetry, Prometheus                   | Kommerzielles SIEM/APM      |
| APIs              | OpenAPI 3.1, gRPC                           | AsyncAPI für Events         |
| Policy Engine     | Open Policy Agent                           | Cedar                       |

Der Start sollte mit einem modularen Monolithen für die geschäftlichen Kernfunktionen und klar isolierten Diensten für Ledger, Zahlungsabwicklung, Identität und Sicherheitsfunktionen erfolgen. Eine vollständige Microservice-Landschaft ab dem ersten Tag würde Komplexität und Betriebsrisiken unnötig erhöhen.

## 3. Regulatorische Gesamtstrategie

### 3.1 Vier rechtliche Betriebsvarianten

| Modell                            | GlobalCards übernimmt                                      | Regulierte Leistung                   |
| --------------------------------- | ---------------------------------------------------------- | ------------------------------------- |
| Technologieanbieter               | Software, UX, APIs, technische Verarbeitung                | Vertragspartner                       |
| BaaS-Programmmanager              | Kundenoberfläche, Programmsteuerung, definierte Kontrollen | Lizenzierte Bank/EMI                  |
| Eigenes Zahlungs-/E-Geld-Institut | Zugelassene Zahlungs- oder E-Geld-Dienste                  | GlobalCards innerhalb der Zulassung   |
| Vollbank                          | Bankgeschäfte nach Lizenzumfang                            | GlobalCards als zugelassenes Institut |

Für Deutschland regelt das ZAG die Zulassung von Zahlungs- und E-Geld-Instituten. Für ein CRR-Kreditinstitut liegt die Entscheidung über die Bankzulassung bei der EZB; der Antrag wird über die BaFin eingereicht.&#x20;



Deutsche Bundesbank+1



Empfohlene Rechtsstruktur:

- GlobalCards Technology GmbH: Entwicklung, IP, Softwarebetrieb und technische Dienstleistungen.
- GlobalCards Financial Services: geplante, rechtlich gesondert zu prüfende regulierte Gesellschaft.
- GlobalCards Card Program: organisatorisch abgegrenztes Kartenprogramm mit Issuer-/BIN-Sponsor.
- GlobalCards International: spätere länderspezifische Aktivitäten und Partnerbeziehungen.

Diese Einheiten sind eine Zielstruktur, keine bereits gegründeten oder zugelassenen Unternehmen.

### 3.2 Regulatorische Anforderungsmatrix

| Regelwerk           | Relevanz                                     | Umsetzung                                       |
| ------------------- | -------------------------------------------- | ----------------------------------------------- |
| KWG / CRR / CRD     | Bankgeschäft, Eigenmittel, Aufsicht          | Lizenzprüfung, Kapital- und Risikoplanung       |
| ZAG / PSD2          | Zahlungsdienste, E-Geld, Kontoinformation    | Zulassung, Safeguarding, SCA                    |
| DORA                | Digitale operationelle Resilienz             | ICT-Risikomanagement, Tests, Incident Reporting |
| DSGVO               | Personenbezogene Daten                       | Datenschutz, Löschung, Betroffenenrechte        |
| GwG / EU-AML-Regime | Geldwäsche und Terrorismusfinanzierung       | KYC, KYB, Monitoring, Meldeprozesse             |
| EU 2024/886         | Echtzeitüberweisungen                        | SEPA Instant, Empfängerüberprüfung              |
| PCI DSS             | Karteninhaberdaten                           | Segmentierung, Zugriffskontrolle, Audits        |
| eIDAS               | Elektronische Identitäten, Vertrauensdienste | Identitäts- und Signaturintegration             |
| ISO 27001           | Informationssicherheitsmanagement            | ISMS, Risiko- und Kontrollkatalog               |
| ISO 22301           | Geschäftskontinuität                         | BCP, Wiederanlauf und Notfalltests              |
| MiCAR               | Nur bei entsprechenden Kryptoaktivitäten     | Separate Produkt- und Lizenzprüfung             |

DORA ist seit dem 17. Januar 2025 anwendbar. Zu den zentralen Pflichten im jeweiligen Anwendungsbereich gehört auch die Erfassung vertraglicher ICT-Drittdienstleisterbeziehungen.&#x20;



European Banking Authority+1



Die EU-Instant-Payments-Verordnung enthält unter anderem Pflichten zur Empfängerüberprüfung, Gebührenbegrenzung und zum Angebot von Echtzeitüberweisungen. Fristen unterscheiden sich nach Institutsart und Mitgliedstaat.&#x20;



European Central Bank+1



### 3.3 Compliance-by-Design

Jede regulatorische Anforderung wird als versioniertes Kontrollobjekt geführt.

```
control_id: GC-COMP-001
domain: payment_security
requirement: strong_customer_authentication
applicability:
  jurisdiction: EU
  product: payment_account
  actor: responsible_psp
implementation:
  service: authentication-service
  enforcement: mandatory
  failure_behavior: deny
evidence:
  - policy_version
  - authentication_decision
  - test_result
  - audit_reference
review:
  owner: compliance_officer
  approval_required: true
```

Die tatsächliche Anwendbarkeit wird anhand von Rechtsraum, Dienstleistung, Institutstyp und vertraglicher Verantwortungsverteilung entschieden. Ein technischer Kontrollstatus allein ist keine behördliche Compliance-Bestätigung.

## 4. Datenmodell und Datenhoheit

GlobalCards verwendet eine mandantenfähige Datenarchitektur mit logisch und kryptografisch getrennten Kundendaten.

### 4.1 Domänenmodell

| Entität                 | Wichtige Attribute                    | Beziehungen                            |
| ----------------------- | ------------------------------------- | -------------------------------------- |
| `customer`              | ID, Typ, Status, Jurisdiktion         | Identitäten, Konten                    |
| `organization`          | ID, Rechtsform, Registerdaten         | Mitglieder, wirtschaftlich Berechtigte |
| `identity_verification` | Provider, Status, Evidenzreferenz     | Kunde                                  |
| `account`               | ID, Währung, Partner, Status          | Kunde, Ledger                          |
| `external_account_ref`  | Provider, Referenz, IBAN-Token        | Konto                                  |
| `ledger_account`        | ID, Typ, Währung, Buchungskreis       | Journal                                |
| `journal_entry`         | ID, Zeit, Referenz, Status            | Buchungszeilen                         |
| `journal_line`          | Konto, Debit, Credit, Betrag          | Journal                                |
| `payment_instruction`   | Betrag, Empfänger, Rail, Status       | Konto                                  |
| `card`                  | Token, Issuer, Status, Limit          | Kunde, Konto                           |
| `authorization`         | Kartenreferenz, Betrag, Entscheidung  | Karte                                  |
| `settlement_batch`      | Provider, Periode, Status             | Transaktionen                          |
| `fx_quote`              | Währungspaar, Kurs, Ablauf            | Zahlungsauftrag                        |
| `compliance_case`       | Typ, Risiko, Bearbeiter               | Kunde, Transaktion                     |
| `audit_event`           | Akteur, Aktion, Zeit, Integritätswert | Beliebige Domäne                       |

### 4.2 Beispiel: Ledger-Schema

```
CREATE TABLE ledger_accounts (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL,
    currency CHAR(3) NOT NULL,
    account_type TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now()
);

CREATE TABLE journal_entries (
    id UUID PRIMARY KEY,
    tenant_id UUID NOT NULL,
    external_reference TEXT,
    idempotency_key TEXT NOT NULL,
    created_at TIMESTAMPTZ NOT NULL DEFAULT now(),
    UNIQUE (tenant_id, idempotency_key)
);

CREATE TABLE journal_lines (
    id UUID PRIMARY KEY,
    entry_id UUID NOT NULL
      REFERENCES journal_entries(id),
    account_id UUID NOT NULL
      REFERENCES ledger_accounts(id),
    side TEXT NOT NULL
      CHECK (side IN ('DEBIT', 'CREDIT')),
    amount_minor BIGINT NOT NULL
      CHECK (amount_minor > 0)
);
```

Dies ist ein vereinfachtes Ausgangsschema, kein produktionsfertiger Ledger.

Produktionsanforderungen sind zusätzlich:

- Jeder Journal-Eintrag muss pro Währung ausgeglichen sein.
- Buchungen werden atomar persistiert.
- Bereits gebuchte Journale dürfen nicht verändert oder gelöscht werden.
- Korrekturen erfolgen ausschließlich durch neue Gegenbuchungen.
- Währungen mit unterschiedlichen Dezimalstellen benötigen explizite Skalierungsregeln.
- Eindeutigkeit, Mandantentrennung und Kontowährung müssen datenbankseitig erzwungen werden.
- Ledger-Einträge, externe Settlement-Datensätze und Kundenanzeigen erhalten unterschiedliche Verantwortlichkeiten.

### 4.3 Transaktionsinvarianten

Für jede vollständig gebuchte Journaltransaktion und jede einzelne Währung gilt:

\\[ \sum \mathrm{Debit}=\sum \mathrm{Credit} \\]

Eine Währungsumrechnung besteht aus nachvollziehbaren, je Währung ausgeglichenen Buchungen und dokumentierten FX-Positionen. EUR und USD dürfen nicht einfach gegeneinander saldiert werden.

Das System prüft außerdem:

\\[ \mathrm{AvailableBalance} = \mathrm{PostedBalance} - \mathrm{ActiveHolds} - \mathrm{OtherReservedFunds} \\]

Dabei müssen Kontotyp, Dispositionsregeln, Pending-Buchungen und mögliche Partnerbankabweichungen berücksichtigt werden.

## 5. API-Spezifikation

Die öffentliche API wird über `/v1` versioniert. Externe Kunden-APIs und privilegierte interne Finanzoperationen bleiben strikt getrennt.

### 5.1 Endpunktkatalog

| Methode | Endpoint                     | Zweck                     |
| ------- | ---------------------------- | ------------------------- |
| POST    | `/v1/customers`              | Kundenanlage              |
| GET     | `/v1/customers/{id}`         | Kundendaten               |
| POST    | `/v1/organizations`          | Geschäftskundenanlage     |
| POST    | `/v1/kyc/sessions`           | Identitätsprüfung starten |
| GET     | `/v1/accounts`               | Konten abrufen            |
| GET     | `/v1/accounts/{id}/balances` | Salden abrufen            |
| POST    | `/v1/payments`               | Zahlungsauftrag erstellen |
| GET     | `/v1/payments/{id}`          | Zahlungsstatus            |
| POST    | `/v1/cards`                  | Kartenantrag              |
| POST    | `/v1/cards/{id}/freeze`      | Karte sperren             |
| POST    | `/v1/cards/{id}/unfreeze`    | Karte entsperren          |
| GET     | `/v1/fx/quotes`              | Wechselkursangebot        |
| POST    | `/v1/fx/conversions`         | Umrechnung beauftragen    |
| GET     | `/v1/transactions`           | Transaktionshistorie      |
| POST    | `/v1/consents`               | Open-Banking-Einwilligung |
| GET     | `/v1/business/approvals`     | B2B-Freigaben             |

### 5.2 Beispiel einer Zahlungsanforderung

```
POST /v1/payments
Authorization: Bearer <access_token>
Idempotency-Key: 4a21d8f0-example
Content-Type: application/json
```

```
{
  "source_account_id": "acc_demo_001",
  "amount": {
    "currency": "EUR",
    "minor_units": 12500
  },
  "destination": {
    "type": "iban",
    "iban": "DE89370400440532013000",
    "name": "Demo Recipient"
  },
  "rail": "SEPA_INSTANT",
  "reference": "Demo invoice",
  "requested_execution": "IMMEDIATE"
}
```

Die Beispiel-IBAN und IDs sind ausschließlich synthetische Testdaten. Es findet keine reale Zahlungsanweisung statt.

### 5.3 Zustandsmaschine

Vereinfachte Zahlungszustandsmaschine. In Produktion werden zusätzlich Pending-, Timeout-, Return-, Recall- und Reversal-Zustände modelliert.

Eine Netzwerkauszeit bedeutet niemals automatisch, dass eine Zahlung fehlgeschlagen ist. Bei unbekanntem Status wird die Partnerreferenz abgefragt und der Auftrag nicht blind erneut eingereicht.

### 5.4 API-Sicherheitsvertrag

Jeder schreibende Endpoint benötigt eine passende Berechtigung, nachvollziehbare Identität, Mandantenprüfung, Eingabevalidierung und – bei finanziell relevanten Operationen – einen Idempotenzmechanismus.

B2B-Zahlungen können zusätzlich einem Vier-Augen-Prinzip und einem rollenbasierten Genehmigungsworkflow unterliegen.

## 6. Karteninfrastruktur und globales Issuing

Das Kartenprogramm besteht aus sechs voneinander getrennten Verantwortungsbereichen.

Issuer / BIN Sponsor

Reguliertes Karteninstitut, Netzwerkmitgliedschaft

Issuer Processor

Autorisierung, Clearing, Kartenstatus

Card Management

Kartenanträge, Limits, Lebenszyklus

Token Services

Digitale Wallets, Netzwerk-Token

Fraud & Risk

Regeln, Velocity Checks, Anomalien

Dispute Management

Chargebacks, Reklamationen, Nachweise

### 6.1 Autorisierungsablauf

1. Ein Kunde führt eine Kartenzahlung durch.
2. Das Kartennetzwerk übermittelt die Anfrage an den zuständigen Issuer-Prozessor.
3. Der Prozessor prüft Kartenstatus, Authentifizierung und weitere Netzwerkanforderungen.
4. Die GlobalCards Risk Engine prüft – sofern vertraglich und technisch eingebunden – verfügbare Mittel, Limits und Betrugsregeln.
5. Der Prozessor gibt die Autorisierungsentscheidung zurück.
6. Bei Genehmigung wird eine Vormerkung beziehungsweise Reservierung erfasst.
7. Später werden Clearing-Datensätze verarbeitet und mit tatsächlichen Buchungen abgeglichen.
8. Abweichungen, Rückerstattungen und Chargebacks werden gesondert behandelt.

Wichtig: Autorisierung, Clearing und Settlement sind verschiedene Vorgänge. Eine genehmigte Kartenzahlung ist nicht automatisch endgültig abgerechnet.

### 6.2 Kartentypen

| Kartenprodukt             | Implementierung                                               |
| ------------------------- | ------------------------------------------------------------- |
| Virtuelle Debitkarte      | Digitales Issuing über Partner                                |
| Physische Debitkarte      | Personalisierung und Versand über zertifizierte Dienstleister |
| B2B Expense Card          | Ausgabenlimits, Team- und Kostenstellenzuordnung              |
| Einmalige virtuelle Karte | Händler-/Betragsbindung, sofern Prozessor unterstützt         |
| Multi-Currency Card       | Währungsrouting, FX-Regeln, transparente Gebühren             |
| Kreditkarte               | Späteres Produkt mit gesondertem Kredit- und Risikomodell     |

Apple Pay und Google Wallet werden erst nach Bestätigung der entsprechenden Issuer-, Netzwerk- und Wallet-Integrationsvoraussetzungen freigeschaltet.

### 6.3 Karten-Datenschutz

GlobalCards soll grundsätzlich mit Netzwerk-Token, Provider-Referenzen und maskierten Kartendaten arbeiten. Vollständige PAN, CVV/CVC und PIN-Daten gehören nicht in allgemeine Anwendungsdatenbanken, Logs oder Analytics-Systeme.

Für die tatsächliche Kartenumgebung muss der PCI-DSS-Geltungsbereich gemeinsam mit den beteiligten Dienstleistern festgelegt werden. PCI DSS v4.0.1 ist in der offiziellen Dokumentenbibliothek des PCI Security Standards Council dokumentiert.&#x20;



PCI Security Standards Council+1



## 7. Zahlungsinfrastruktur und Settlement Engine

Die Payment Engine muss unterschiedliche Zahlungsnetzwerke über ein gemeinsames internes Auftragsmodell ansprechen können.

| Zahlungsweg                     | Funktion                          | Implementierungspriorität |
| ------------------------------- | --------------------------------- | ------------------------- |
| SEPA Credit Transfer            | Euro-Überweisungen                | P0                        |
| SEPA Instant                    | Euro-Echtzeitüberweisungen        | P0                        |
| SEPA Direct Debit               | Lastschriften                     | P1                        |
| Card Network Clearing           | Kartenabrechnung                  | P0                        |
| SWIFT / Korrespondenzbanken     | Internationale Überweisungen      | P2                        |
| Lokale Zahlungssysteme          | Länderabhängige Auszahlungen      | P2                        |
| Interne Umbuchungen             | Konten-/Ledgertransfers           | P0                        |
| Open-Banking-Payment Initiation | Kontobasierte Zahlungsinitiierung | P1                        |

P0 bezeichnet den ersten produktionsorientierten Umfang, P1 die erste Erweiterung und P2 den internationalen Ausbau.

### 7.1 Settlement Engine

Die Settlement Engine ist eine der kritischsten Komponenten. Sie verarbeitet eingehende Clearing-Dateien, Bankauszüge, Prozessorberichte, Gebühren und Rückbuchungen.

Bank-/Prozessorberichte + internes Ledger

Normalization → Matching → Reconciliation

Matched

Abgleich und Abschluss

Exception

Untersuchung und Freigabe

### 7.2 Reconciliation-Regeln

Die Matching Engine verwendet zunächst deterministische Kriterien:

- Externe Transaktionsreferenz
- Betrag und Währung
- Partner und Settlement-Konto
- Transaktionstyp
- Buchungs- und Valutadatum
- Gebühren- und Wechselkursinformationen

Unklare Treffer werden nicht automatisch als korrekt klassifiziert. Eine KI-basierte Vorschlagslogik darf Fälle priorisieren, aber keine ungeprüften Geldbewegungen oder Journaländerungen auslösen.

### 7.3 Kontrollierte Automatisierung

```
RECEIVE settlement_batch
    VERIFY source_signature
    VERIFY schema_and_integrity
    CHECK duplicate_batch
    NORMALIZE records
    MATCH against ledger

    IF all_records_match:
        MARK reconciled
        GENERATE evidence
    ELSE:
        CREATE exception_cases
        REQUIRE authorized_review

    ARCHIVE immutable_audit_record
END
```

## 8. Multi-Currency, FX und Treasury

GlobalCards soll Konten und Zahlungsprodukte mit mehreren Währungen unterstützen, ohne dabei interne Währungsdarstellungen mit tatsächlich verfügbaren Partnerbankguthaben zu verwechseln.

### 8.1 Währungsmodell

Jede Währung besitzt eigene Salden, Rundungsregeln, Verfügbarkeiten, Gebühren und Settlement-Verfahren.

Ein FX-Angebot enthält mindestens:

```
{
  "quote_id": "fx_demo_001",
  "source_currency": "EUR",
  "target_currency": "USD",
  "source_minor_units": 10000,
  "rate": "1.0800",
  "fee_minor_units": 50,
  "expires_at": "2026-11-07T15:10:00Z",
  "provider": "synthetic-demo"
}
```

Die Kursangabe ist rein illustrativ und kein aktueller Marktkurs. Produktionsangebote müssen zusätzlich Kursrichtung, Gebührenwährung, Rundung, garantierten Zielbetrag und rechtliche Ausführungsbedingungen eindeutig festhalten.

### 8.2 Treasury-Funktionen

- Intraday-Liquiditätsüberwachung
- Prefunding- und Settlement-Konten
- Währungspositionen und Exposures
- Mindestliquiditätsgrenzen
- Liquiditätsprognosen
- Bank- und Partnerkonzentrationsrisiken
- Liquiditätsstressszenarien
- Genehmigte Transfers zwischen Treasury-Konten

Kundengelder, Eigenmittel und operative Betriebsmittel müssen entsprechend dem anwendbaren Rechtsrahmen und dem jeweiligen Vertragsmodell getrennt behandelt werden.

## 9. KYC, KYB, AML und Fraud Management

### 9.1 Onboarding

1

Identität

Natürliche Person oder juristische Person erfassen

2

Verifikation

Identitätsprüfung, Registerprüfung, wirtschaftlich Berechtigte

3

Screening

Sanktionslisten, PEP, risikobasierte Prüfungen

4

Risikobewertung

Land, Produkt, Kundentyp, Nutzungsmuster

5

Entscheidung

Genehmigen, Nachprüfung, Ablehnung

6

Monitoring

Laufende Überwachung und periodische Aktualisierung

### 9.2 AML-Regelwerk

Das System unterstützt regelbasierte und statistische Prüfungen, beispielsweise ungewöhnliche Transaktionsmuster, auffällige Empfängerbeziehungen, Sanktionsrisiken und erhebliche Abweichungen vom bekannten Kundenprofil.

Ein Treffer erzeugt einen Compliance-Fall mit Bearbeiter, Begründung, Belegen und dokumentierter Entscheidung. Verdachtsmeldungen erfolgen ausschließlich über die dafür vorgesehenen rechtlichen und organisatorischen Verfahren.

### 9.3 KI-Governance

KI darf bei der Erkennung von Auffälligkeiten, Dokumentenklassifikation und Fallpriorisierung unterstützen. Entscheidungen mit erheblicher Wirkung auf Kunden benötigen angemessene menschliche Kontrolle, dokumentierte Regeln und rechtliche Prüfung.

Keine generative KI erhält ungefilterten Zugriff auf Produktionsschlüssel, vollständige Kartendaten oder vertrauliche Kundenunterlagen.

## 10. Sicherheitsarchitektur

GlobalCards wird nach Zero-Trust-Prinzipien und mit getrennten Sicherheitszonen entwickelt.

| Sicherheitsbereich | Maßnahme                                       |
| ------------------ | ---------------------------------------------- |
| Identität          | Phishing-resistente MFA, Passkeys, OIDC        |
| Berechtigungen     | RBAC + ABAC, Least Privilege                   |
| Datenübertragung   | TLS, mTLS für sensible Serviceverbindungen     |
| Speicherung        | Verschlüsselung, getrennte Schlüsselverwaltung |
| Secrets            | HSM/KMS, Rotation, Zugriffsnachweise           |
| Anwendungen        | SAST, DAST, SCA, Secret Scanning               |
| Lieferkette        | SBOM, signierte Artefakte, Provenance          |
| Netzwerk           | Segmentierung, Egress-Kontrollen               |
| APIs               | OAuth Scopes, Rate Limits, Abuse Detection     |
| Monitoring         | SIEM, Alarmierung, Incident Response           |
| Verfügbarkeit      | Redundanz, getestete Wiederherstellung         |
| Administration     | Just-in-Time-Zugriff, Vier-Augen-Freigaben     |

### 10.1 Datenklassifikation

| Klasse           | Beispiel                                | Schutzanforderung                |
| ---------------- | --------------------------------------- | -------------------------------- |
| Public           | Dokumentation, öffentliche Produktdaten | Integrität                       |
| Internal         | Interne Konfigurationen                 | Zugriffsbeschränkung             |
| Confidential     | Geschäftsdaten, Verträge                | Verschlüsselung, Protokollierung |
| Restricted       | KYC-Daten, Kontoinformationen           | Strenge Zugriffstrennung         |
| Critical Secrets | Schlüssel, HSM-Material, Zugangsdaten   | Isolierte Schlüsselverwaltung    |

### 10.2 Datenhoheit

Die Architektur sollte sicherstellen, dass sensible Daten nicht unkontrolliert an Drittanbieter, KI-Agenten, Telemetriedienste oder Entwicklungsplattformen übertragen werden.

Dafür werden ein Data-Flow-Register, kontrollierte ausgehende Verbindungen, Datenminimierung, regionale Speicherregeln und vertragliche Drittanbieterprüfungen eingeführt.

Eine vollständig offline betriebene Entwicklungs- und Testumgebung ist möglich. Reale internationale Zahlungen erfordern dagegen autorisierte und überwachte Verbindungen zu den zuständigen Finanzpartnern.

## 11. Module und Implementierungsreihenfolge

P0 = Fundament · P1 = Erweiterung · P2 = internationale Skalierung

| ID     | Modul                           | Priorität |
| ------ | ------------------------------- | --------- |
| GC-001 | Identity & Access               | P0        |
| GC-002 | Customer / Organization         | P0        |
| GC-003 | KYC / KYB                       | P0        |
| GC-004 | Account Registry                | P0        |
| GC-005 | Double-Entry Ledger             | P0        |
| GC-006 | Payment Orchestrator            | P0        |
| GC-007 | Card Issuing Adapter            | P0        |
| GC-008 | Card Controls                   | P0        |
| GC-009 | Settlement & Reconciliation     | P0        |
| GC-010 | Compliance Case Engine          | P0        |
| GC-011 | Audit & Evidence                | P0        |
| GC-012 | B2C Web / Mobile                | P0        |
| GC-013 | B2B Administration              | P0        |
| GC-014 | Multi-Currency & FX             | P1        |
| GC-015 | Open Banking Aggregation        | P1        |
| GC-016 | Treasury Management             | P1        |
| GC-017 | Fraud Analytics                 | P1        |
| GC-018 | Dispute & Chargeback            | P1        |
| GC-019 | Business Payments & Approvals   | P1        |
| GC-020 | Partner Developer Portal        | P1        |
| GC-021 | International Payment Rails     | P2        |
| GC-022 | Jurisdiction Policy Engine      | P2        |
| GC-023 | Multi-Entity Reporting          | P2        |
| GC-024 | Regulatory Reporting Automation | P2        |

## 12. Konkreter Entwicklungsplan – 24 Monate

Der Plan unterscheidet zwischen technischer Fertigstellung, regulatorischer Bereitschaft und tatsächlicher Genehmigung. Ein Produkt wird nicht allein deshalb freigeschaltet, weil seine Software fertig ist.

Phase 0

Rechtliche und wirtschaftliche Vorprüfung

Monat 1–2

Produkt- und Länderumfang, Erlaubnistatbestände, Partner-RFI, Finanzplanung, Risikoinventar.

Abnahmekriterium: Juristische Produktmatrix und genehmigter Projektumfang.

Phase 1

Architektur und Entwicklungsgrundlage

Monat 2–4

Repository-Struktur, CI/CD, IAM, Datenmodell, API-Verträge, Sicherheitszonen, synthetische Testdaten.

Abnahmekriterium: Abgenommene Architektur, Threat Model und automatisierte Basistests.

Phase 2

Core Banking und Ledger

Monat 4–7

Kunden, Organisationen, Konten, Double-Entry-Ledger, Reservierungen, Journale, Audit.

Abnahmekriterium: Keine unausgeglichenen Buchungen; getestete Wiederanlauf- und Idempotenzverfahren.

Phase 3

Zahlungs- und Kartenintegration

Monat 7–11

SEPA-Adapter, Issuer-Sandbox, Kartenstatus, Autorisierungen, Settlement, Reconciliation.

Abnahmekriterium: End-to-End-Sandboxtests mit nachvollziehbaren Partnerreferenzen.

Phase 4

B2C- und B2B-Anwendungen

Monat 9–13

Mobile/Web, Business Portal, Genehmigungsworkflows, Ausgabenlimits, Support.

Abnahmekriterium: Usability-, Sicherheits- und Zugriffsprüfung bestanden.

Phase 5

Compliance und Betriebsresilienz

Monat 11–16

AML-Workflows, PCI-Scope, DORA-Kontrollen, Notfallübungen, Datenschutzprüfungen.

Abnahmekriterium: Unabhängig überprüfte Kontrollen und dokumentierte Restrisiken.

Phase 6

Kontrollierter Pilotbetrieb

Monat 16–20

Regulierte Partneranbindung, begrenzte Nutzergruppen, operative Überwachung, Support und Beschwerden.

Abnahmekriterium: Rechtliche Freigabe, Partnerabnahme und Go-Live-Entscheidung.

Phase 7

Internationalisierung

Monat 20–24+

Weitere Währungen, Länder, Payment Rails, Treasury, zusätzliche Partner und Geschäftskundenprodukte.

Abnahmekriterium: Gesonderte Länder- und Produktfreigabe.

Die 24 Monate sind eine ambitionierte technische Planungsbasis. Lizenzverfahren, Partner-Onboarding und Zertifizierungen können die Markteinführung erheblich verlängern.

## 13. Automatisierte Build-, Test- und Verifikationsschleife

Damit keine Implementierungsschritte unkontrolliert ausgelassen werden, erhält GlobalCards eine kontinuierliche Build- und Evidence-Pipeline.

### 13.1 Verifikationskriterien

| Testklasse           | Mindestziel                                                     |
| -------------------- | --------------------------------------------------------------- |
| Unit Tests           | Kritische Buchungs- und Sicherheitsregeln vollständig abgedeckt |
| Property-Based Tests | Buchungsinvarianten und Zustandsübergänge                       |
| Integration Tests    | Alle wesentlichen Partner-Sandboxflüsse                         |
| Contract Tests       | Versionierte API- und Event-Schemas                             |
| Security Tests       | Keine offenen kritischen Schwachstellen                         |
| Performance Tests    | Lastprofil und definierte SLOs bestanden                        |
| Resilience Tests     | Wiederherstellung, Timeouts, Duplikate, Failover                |
| Reconciliation Tests | Keine ungeklärten Differenzen beim Testabschluss                |
| Compliance Tests     | Jede anwendbare Kontrolle mit Nachweis                          |
| UAT                  | B2C- und B2B-Geschäftsprozesse abgenommen                       |

### 13.2 Release-Entscheidung

Ein Release darf nur erfolgen, wenn alle verpflichtenden Gates erfolgreich sind:

```
function releaseGate(build):
    assert build.artifact_signature_valid
    assert build.dependencies_approved
    assert build.critical_tests_passed
    assert build.ledger_invariants_passed
    assert build.security_review_passed
    assert build.compliance_evidence_complete
    assert build.partner_contract_tests_passed
    assert build.operational_readiness_approved

    if build.enables_regulated_service:
        assert build.legal_authorization_confirmed
        assert build.partner_approval_confirmed

    return RELEASE_ELIGIBLE
```

Diese Logik ist eine fachliche Spezifikation. Die produktive Umsetzung benötigt unabhängige Prüfungen, manipulationsgeschützte Nachweise und einen separaten Freigabedienst. Ein fehlgeschlagenes Gate darf nicht durch die Build-Pipeline selbst überschrieben werden.

## 14. Betriebsmodell und Verantwortlichkeiten

Für den realen Betrieb müssen technische und regulatorische Verantwortung eindeutig zugeordnet werden.

| Rolle                  | Kernverantwortung                                     |
| ---------------------- | ----------------------------------------------------- |
| Geschäftsführung       | Strategie, Finanzierung, Gesamtverantwortung          |
| CTO                    | Architektur, Softwareentwicklung, technische Qualität |
| CISO                   | Informationssicherheit, Risiken, Incident Response    |
| Compliance Officer     | Regulatorische Kontrollen und Compliance-Überwachung  |
| Geldwäschebeauftragter | AML-Prozesse, Verdachtsfallbearbeitung                |
| DPO                    | Datenschutz und Betroffenenrechte                     |
| Head of Payments       | Zahlungsverkehr und Partnerbetrieb                    |
| Head of Cards          | Issuing-Programm, Kartenrisiken, Disputes             |
| Treasury Lead          | Liquidität, Settlement-Finanzierung                   |
| Internal Audit         | Unabhängige Kontrollprüfung                           |

Einige Funktionen können abhängig von Rechtsform, Umfang und geltendem Aufsichtsrecht ausgelagert werden. Interessenkonflikte und Unabhängigkeitsanforderungen müssen dabei berücksichtigt werden.

## 15. Wirtschaftlichkeits- und Kapazitätsplanung

Die folgenden Zahlen sind illustrative Budgetkorridore, keine geprüften Marktangebote oder Finanzierungsgarantien.

| Entwicklungsstufe                    | Grobe Budgetannahme    |
| ------------------------------------ | ---------------------- |
| Architektur, Rechtsprüfung, Prototyp | 150.000–500.000 €      |
| Sandbox-MVP mit Ledger und APIs      | 500.000–1,5 Mio. €     |
| Partnerintegrierter Pilot            | 1,5–5 Mio. €           |
| Produktionsfähige B2C-/B2B-Plattform | 5–15 Mio. €+           |
| Internationale Skalierung            | Separat zu kalkulieren |

Die Beträge sind nicht als addierbare Phasenbudgets zu verstehen. Sie beschreiben grobe Projektgrößen mit zunehmendem Umfang. Eigene regulatorische Zulassung, Eigenmittel, Sicherungsmittel, Garantien, Kartenprogrammgebühren und laufende Betriebskosten können zusätzlichen erheblichen Finanzbedarf erzeugen.

### 15.1 Wesentliche Kostenfaktoren

- Entwicklungs- und Sicherheitspersonal
- Rechtsberatung, Compliance und Prüfungen
- BaaS-, Issuer- und Payment-Processor-Verträge
- Kartenherstellung und Netzwerkgebühren
- Identitätsprüfung und Betrugsprävention
- Infrastruktur, Hochverfügbarkeit und Backups
- Kundendienst, Disputes und operative Kontrollen
- Liquiditäts- und Kapitalanforderungen

### 15.2 Technische Kapazitätsziele

Illustratives Lastszenario für die Architekturprüfung

Aktive Kunden

1.000.000

Transaktionen pro Kunde/Tag

30

Spitzenlastfaktor

50×

Transaktionen pro Tag

# 30.000.000

Spitzenlast, Transaktionen/s

# 17.361,1

Vereinfachtes Modell mit gleichmäßigem Tagesmittel und gewähltem Spitzenlastfaktor. Kein Leistungsnachweis einer bestehenden Infrastruktur.

## 16. Technische Projektstruktur

Ein Monorepository kann den ersten Implementierungsabschnitt wie folgt organisieren:

```
globalcards-bank/
├── apps/
│   ├── customer-web/
│   ├── business-web/
│   ├── mobile/
│   └── admin-console/
├── services/
│   ├── identity/
│   ├── customers/
│   ├── accounts/
│   ├── ledger/
│   ├── payments/
│   ├── cards/
│   ├── settlement/
│   ├── fx/
│   ├── treasury/
│   ├── compliance/
│   └── audit/
├── adapters/
│   ├── baas/
│   ├── card-processors/
│   ├── payment-rails/
│   ├── open-banking/
│   └── kyc-providers/
├── packages/
│   ├── api-contracts/
│   ├── domain-types/
│   ├── security-policy/
│   └── test-fixtures/
├── infrastructure/
├── governance/
│   ├── controls/
│   ├── regulatory-mappings/
│   └── evidence-schemas/
├── tests/
│   ├── integration/
│   ├── property/
│   ├── security/
│   └── resilience/
└── docs/
    ├── architecture/
    ├── adr/
    ├── api/
    └── operations/
```

Die Entwicklung beginnt mit synthetischen Daten und Mock-Adaptern. Produktive Partnerzugänge, Kundendaten und Schlüssel werden erst nach separater Sicherheits- und Rechtsfreigabe eingebunden.

## 17. Go-Live-Checkliste

Readiness Tracker

0 / 12 erledigt

Rechtsgutachten und Produkt-/Lizenzmatrix genehmigt

Regulierte Partner vertraglich und operativ freigegeben

KYC/KYB, AML und Sanktionsprozesse getestet

Ledger und Reconciliation unabhängig abgenommen

PCI-DSS-Scope und erforderliche Nachweise geklärt

Datenschutzprüfung und Auftragsverarbeitungsverträge abgeschlossen

Penetrationstest und kritische Sicherheitsbefunde bearbeitet

Incident Response, Notfallbetrieb und Wiederherstellung getestet

Kundengeldschutz und Treasury-Verantwortung dokumentiert

Beschwerde-, Betrugs- und Chargeback-Prozesse betriebsbereit

B2C-/B2B-Vertragsunterlagen und Gebühren transparent

Management- und Partner-Go-Live-Freigaben erteilt

&#x20;Checkliste kopierenDie Häkchen dienen der internen Planung und ersetzen keine dokumentierten Prüfungen oder Genehmigungen.

## 18. Offizielle regulatorische Referenzen

Für die Umsetzung sollten die jeweils aktuellen Rechtsfassungen und technischen Regelwerke direkt aus den Primärquellen in den Compliance-Katalog übernommen werden.

- [Deutsche Bundesbank – Zahlungs- und E-Geld-Institute](https://www.bundesbank.de/de/aufgaben/finanzaufsicht/einzelaspekte/zahlungsinstitute-und-e-geld-institute-598334)
- [Zahlungsdiensteaufsichtsgesetz (ZAG)](https://www.gesetze-im-internet.de/zag_2018/)
- [EBA – DORA und Informationsregister](https://www.eba.europa.eu/activities/direct-supervision-and-oversight/digital-operational-resilience-act/preparation-dora-application)
- [EZB – Instant Payments Regulation](https://www.ecb.europa.eu/paym/retail/instant_payments/html/instant_payments_regulation.tr.html)
- [PCI SSC – PCI DSS und Dokumentenbibliothek](https://www.pcisecuritystandards.org/de/document_library/)

Die BaFin bietet zudem ein Verfahren zur Prüfung der Erlaubnispflicht neuer Finanzgeschäftsmodelle an. Dies ist ein sinnvoller früher Meilenstein, bevor GlobalCards regulatorisch relevante Dienstleistungen anbietet.&#x20;



verwaltung.bund.de



## Abschließende Implementierungsentscheidung

Für GlobalCards Bank empfehle ich als ersten verbindlichen Projektumfang:

GlobalCards Core v1.0 mit Identitätsverwaltung, B2C-/B2B-Kundenmodellen, Multi-Tenant-Konten, Double-Entry-Ledger, SEPA-Sandbox, virtuellem Kartenprogramm über einen Issuer-Adapter, Settlement/Reconciliation, Compliance Engine, Audit Evidence und Web-Dashboard.

Danach werden echte Zahlungsdienste ausschließlich über bestätigte regulatorische und vertragliche Berechtigungen freigeschaltet. Der internationale Ausbau erfolgt nicht gleichzeitig in allen Ländern, sondern über ein kontrolliertes Jurisdiktions- und Partnerfreigabemodell.

Damit liegt ein vollständiger Architektur- und Implementierungsrahmen vor. Für eine tatsächliche Umsetzung müssen als nächste Artefakte insbesondere das detaillierte OpenAPI-Vertragswerk, Datenbankmigrationen, ausführbare Testfälle, Partner-RACI-Matrizen, Betriebsrunbooks und die juristische Produktklassifizierung erstellt werden.

Der wichtigste nächste Entwicklungsschritt ist die Kombination aus ausführbarem Ledger-Prototyp, synthetischer Zahlungs-Sandbox und rechtlicher Verantwortungsmatrix. Damit lassen sich die riskantesten technischen und regulatorischen Annahmen früh überprüfen, bevor erhebliche Mittel in den vollständigen Plattformaufbau fließen. # GlobalCards Bank – Internationaler Partner- & Developer-Portal-Masterkatalog

Ausgabe November 2026 · Banking-as-a-Service · Card Issuing · IBAN · SEPA · SWIFT · FX · Open Banking · KYC · Compliance · Security

Für GlobalCards Bank habe ich die Integration nach internationalen Partnerkategorien aufgeteilt. Im Mittelpunkt stehen direkte Registrierungsformulare, Corporate-Partner-Bewerbungen, Developer-Dashboards, API-Portale und Sandbox-Zugänge – ausdrücklich nicht bloß die Unternehmensstartseiten.

Die Auswahl ist auf eine hybride B2C-/B2B-Banking-Plattform ausgerichtet, mit Deutschland und dem Europäischen Wirtschaftsraum als Ausgangspunkt.

Kennzeichnung der Zugangsarten:

- Self-Service: Registrierung oder Sandbox unmittelbar erreichbar.
- Antrag: Partnerbewerbung oder Unternehmensprüfung erforderlich.
- Kontakt: Direkter Corporate-/Sales-Anfragekanal.
- Developer: Technische API-Dokumentation, gegebenenfalls mit gesonderter Zugangserteilung.

## 1. Top-Portale für den unmittelbaren Entwicklungsstart

Diese Zugänge würde ich für die ersten technischen Integrationstests priorisieren.

| Anbieter       | Direkte Registrierung / Portal-URL                                                                                                      | Funktionen                                        | Zugang           |
| -------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------- | ---------------- |
| Swan           | [swan.io/start-now](https://www.swan.io/start-now)                                                               | EU Embedded Banking, IBANs, Karten, SEPA, B2C/B2B | Self-Service     |
| Weavr          | [portal.weavr.io/solutions](https://portal.weavr.io/solutions/)                                                  | Embedded Accounts, Cards, Payments, B2B/B2C       | Self-Service     |
| Marqeta        | [auth.marqeta.com/create-account](https://auth.marqeta.com/create-account)                                       | Card Issuing, Autorisierung, Kartenkontrollen     | Self-Service\*   |
| Thredd         | [devportal.thredd.com/signup](https://devportal.thredd.com/signup)                                               | Issuing Processing, virtuelle Karten, 3DS         | Self-Service     |
| Griffin Bank   | [app.griffin.com/register](https://app.griffin.com/register)                                                     | Bankkonten, Ledger-Anbindung, Zahlungs-APIs       | Self-Service, UK |
| Monerium       | [sandbox.monerium.dev/developers](https://sandbox.monerium.dev/developers)                                       | EUR-E-Geld, SEPA, Blockchain-/Wallet-Integration  | Self-Service     |
| Visa Developer | [developer.visa.com/portal/assets/registration.html](https://developer.visa.com/portal/assets/registration.html) | Netzwerk-APIs, Zahlungen, Kartenfunktionen        | Self-Service     |
| Visa Partner   | [partner.visa.com/identity/user/register](https://partner.visa.com/identity/user/register)                       | Fintech-Programme, Sponsoren, Partnerschaften     | Registrierung    |

\*Die Marqeta-Registrierungsadresse ist in der offiziellen Dokumentation verlinkt; der direkte Seitenabruf wurde jedoch mit HTTP 403 blockiert. Dies bestätigt nicht, ob die Registrierung aus deinem Browser derzeit funktioniert.

Swan beschreibt seine Sandbox ausdrücklich für Kontoeröffnung, Karten und simulierte SEPA-Zahlungen. Griffin bietet laut eigener Dokumentation eine kostenlose Sandbox; Weavr stellt einen Embedder-Zugang mit API-Schlüsseln bereit. Visa unterscheidet zwischen einem Developer-Account und dem separaten kommerziellen Partnerprogramm.&#x20;



Swan+7



## 2. Banking-as-a-Service, IBAN und Embedded Finance

Diese Gruppe ist für die eigentliche Konten-, Bank- und Zahlungsinfrastruktur von GlobalCards besonders wichtig.

| Priorität / Partner      | Direkter Corporate-/Partner-Zugang                                                                                                               | Developer-Portal                                                                                                                  | Integration und Eignung                                                                                       |
| ------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| P0 · Solaris 🇩🇪        | [Partnerprogramm](https://www.solarisgroup.com/de/partners/)                                                              | [docs.solarisgroup.com/guides/get-started](https://docs.solarisgroup.com/guides/get-started)               | Deutsche Banking-Infrastruktur, Privat-/Geschäftskonten, IBAN, SEPA Instant, Karten; Antrag und Due Diligence |
| P0 · Treezor 🇫🇷        | [Corporate-Antragsformular](https://www.treezor.com/contact-us/contact-sales/)                                            | [docs.treezor.com](https://docs.treezor.com/guide/api-basics/environments.html)                            | EU Embedded Finance, Konten, Karten, SEPA; Sandbox nach Partner-Onboarding                                    |
| P0 · OpenPayd            | [Partnerprogramm](https://www.openpayd.com/partnership/)                                                                  | [Sandbox](https://sandbox.openpayd.com/) · [API](https://apidocs.openpayd.com/)     | Virtuelle IBANs, Multi-Currency, internationale Zahlungen und FX                                              |
| P1 · Banking Circle 🇱🇺 | [Direkte API-/Corporate-Anfrage](https://www.bankingcircle.com/api-integration/)                                          | [Banking Circle API Hub](https://www.bankingcircle.com/api/)                                               | Internationale Zahlungen, Bankkonten, FX, institutionelle Settlement-Infrastruktur                            |
| P0 · Airwallex           | [BaaS-Plattform-Onboarding](https://www.airwallex.com/docs/banking-as-a-service/get-started/set-up-your-platform-account) | [Partner-API](https://www.airwallex.com/docs/partner-api/getting_started)                                  | Geschäftskonten, Karten, globale Zahlungen, FX, verbundene Kundenkonten                                       |
| P1 · Nium                | [Corporate-Partnerbewerbung](https://www.nium.com/partners)                                                               | [app.nium.com](https://app.nium.com/) · [API-Dokumentation](https://docs.nium.com/) | Globale Auszahlungen, virtuelle Wallets, Kartenprogramme, FX                                                  |
| P1 · Wise Platform       | [Partner-Onboarding-Spezifikation](https://docs.wise.com/guides/product/account-setup)                                    | [Developer Hub](https://wise-sandbox.com/developer-hub)                                                    | Multi-Currency, internationale Transfers, Karten und Kontointegration                                         |
| P1 · Currencycloud       | [Fuse-Partnerprogramm](https://www.currencycloud.com/technology/partners)                                                 | [Direkte API-Key-Registrierung](https://developer.currencycloud.com/register-for-an-api-key/)              | FX, Währungsumrechnung, internationale Zahlungen und Kontenabstimmung                                         |

P0 = erste Anfragen, P1 = parallele oder spätere Ergänzung. Prioritäten sind meine Einschätzung für GlobalCards und keine offiziellen Anbieter-Rankings.

Wichtige Einschränkung: Banking Circle richtet sich nach eigener Aussage an bereits lizenzierte Finanzinstitute. Wise schaltet den Partner-Developer-Hub erst nach entsprechender Berechtigung frei. Treezor verlangt für Corporate-Anfragen ausdrücklich eine geschäftliche E-Mail-Adresse. Currencycloud bietet hingegen ein eigenes Demo-API-Key-Formular.&#x20;



docs.solarisgroup.com+4



Für die erste technische Partnerauswahl sind insbesondere Solaris, Treezor und Airwallex interessant, weil sie mehrere der benötigten GlobalCards-Module gleichzeitig adressieren. OpenPayd und Banking Circle sind starke Kandidaten für den internationalen Zahlungs- und Treasury-Teil.&#x20;



docs.solarisgroup.com+4



## 3. Visa, Mastercard und Karten-Netzwerkpartnerschaften

Hier geht es um den Zugang zu Kartenprogrammen, Issuer-Sponsoren, Netzwerkdiensten und qualifizierten technischen Integrationspartnern.

| Netzwerk / Programm                | Direkter Link                                                                                                                                          | Zweck                                                          | Zugang         |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------- | -------------- |
| Visa Fintech Fast Track            | [Fintech-Partnerantrag](https://partner.visa.com/site/programs/fintech-program.html)                                            | Aufbau eines Visa-Kartenprogramms, Vermittlung von Enablern    | Antrag         |
| Visa Partner Account               | [Partnerkonto registrieren](https://partner.visa.com/identity/user/register)                                                    | Corporate-Profil und Partnerprogramme                          | Self-Service   |
| Visa Technology / License Programs | [Partner- und Lizenzprogramme](https://partner.visa.com/site/programs/partner-programs.html)                                    | Technologiepartner, Lizenz- und Kartenprogrammverfahren        | Antrag         |
| Visa Partner Directory             | [Verzeichnis qualifizierter Anbieter](https://partner.visa.com/site/partner-directory.html)                                     | Issuer Processor, BIN Sponsor, Kartenproduktion suchen         | Partnerauswahl |
| Mastercard Engage                  | [Engage-Programm](https://www.mastercard.com/global/en/business/industry-segment/fintech/program/engage.html)                   | Zugang zu Netzwerk- und Implementierungspartnern               | Antrag         |
| Mastercard Engage Directory        | [Qualifiziertes Partnerverzeichnis](https://engagepartners.mastercard.com/english/directory/)                                   | Issuing-, Digital-First-, Tokenisierungs- und Zahlungsanbieter | Recherche      |
| Mastercard Developers              | [Mastercard Developer APIs](https://www.mastercard.com/content/mccom/eu/en/innovation/build-with-us/mastercard-developers.html) | API-Schlüssel, technische Integration, Netzwerkdienste         | Developer      |

Beim Mastercard-Engage-Programm ist für eine offizielle Partnerqualifikation ein Produktqualifizierungsverfahren erforderlich. Das Partnerverzeichnis kann GlobalCards aber bereits zur Suche nach bestehenden Implementierungspartnern nutzen. Visa Fast Track ist ebenfalls ein Bewerbungsverfahren mit unternehmens- und regionenabhängigen Zulassungskriterien.&#x20;



Mastercard Global+3



## 4. Internationale Zahlungen, FX und Treasury

Diese Anbieter ergänzen das Banking-Grundsystem um grenzüberschreitende Transfers und Währungsmanagement.

| Anbieter       | Direkter Zugang / Developer-Link                                                                                                             | Schwerpunkt                                                          |
| -------------- | -------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------- |
| Wise Platform  | [Partner-API-Dokumentation](https://docs.wise.com/guides/developer)                                                   | Grenzüberschreitende Zahlungen, Währungsumrechnung, Embedded Finance |
| Currencycloud  | [Demo-API-Key beantragen](https://developer.currencycloud.com/register-for-an-api-key/)                               | Wechselkurse, FX-Konvertierung, Empfängerzahlungen                   |
| Nium           | [Nium Developer & Portal](https://www.nium.com/developers)                                                            | Globale Payouts, Multi-Currency, Wallets                             |
| Airwallex      | [BaaS-Entwicklerzugang](https://www.airwallex.com/docs/banking-as-a-service/get-started/set-up-your-platform-account) | Global Treasury, Issuing und FX                                      |
| OpenPayd       | [API-Sandbox](https://sandbox.openpayd.com/)                                                                          | Virtuelle IBAN, Zahlungsein- und -ausgänge, FX                       |
| Banking Circle | [Corporate/API-Integration](https://www.bankingcircle.com/api-integration/)                                           | Institutionelle internationale Zahlungsabwicklung                    |
| Monerium       | [Whitelabel-Partnerantrag](https://monerium.com/invite/partners)                                                      | EUR-E-Geld, SEPA und optionale On-Chain-Abwicklung                   |

Diese Links enthalten sowohl unmittelbar erreichbare Testzugänge als auch Bewerbungs-/Onboarding-Strecken. Insbesondere Wise und Banking Circle sind keine offenen Produktions-APIs ohne kommerzielle und regulatorische Freigabe.&#x20;



Wise Platform+3



## 5. Open Banking, Multi-Bank-Aggregation und Payment Initiation

Diese Kategorie ist besonders wertvoll, damit GlobalCards neben eigenen Konten auch externe Bankkonten anzeigen und – bei entsprechender Berechtigung – Zahlungsinitiierungen ermöglichen kann.

| Anbieter                     | Direkte Registrierung / Partnerportal                                                             | Entwicklerdokumentation                                                                                                       | Nutzen für GlobalCards                                  |
| ---------------------------- | ------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- |
| Enable Banking 🇫🇮          | [enablebanking.com/sign-in](https://enablebanking.com/sign-in/)            | [Control-Panel-Handbuch](https://enablebanking.com/docs/api/control-panel/)                            | EU-Kontoaggregation, Bankverbindungen, API-Anwendungen  |
| Tink / Visa                  | [console.tink.com/signup](https://console.tink.com/signup)                 | [Tink-Developer-Zugang](https://tink.com/scale/)                                                       | Kontodaten, Verifizierung, Open-Banking-Payments        |
| TrueLayer                    | [console.truelayer.com](https://console.truelayer.com/)                    | [Console-Registrierungsanleitung](https://docs.truelayer.com/docs/quickstart-create-a-console-account) | Pay-by-Bank, Kontoanbindung, Zahlungen                  |
| Yapily                       | [accounts.yapily.com/register](https://accounts.yapily.com/register)       | [Yapily Console](https://console.yapily.com/)                                                          | Open-Banking-Daten und Payment Initiation               |
| Salt Edge                    | [Partner-Bewerbungsformular](https://www.saltedge.com/partnership_request) | [Partners API](https://docs.saltedge.com/partners/v1/)                                                 | PSD2-Aggregation, Kontoinformationen und Zahlungen      |
| finAPI 🇩🇪                  | [Sandbox-Testzugang beantragen](https://www.finapi.io/jetzt-testen/)       | [Technische Integrationsdokumentation](https://documentation.finapi.io/access)                         | Deutsches/EU-Multibanking, FinTS/PSD2, Datenaggregation |
| GoCardless Bank Account Data | [Bank Account Data Portal](https://bankaccountdata.gocardless.com/)        | [API-Quickstart](https://docs.gocardless.com/docs/bank-account-data/quickstart-guide)                  | Bankdatenaggregation und Transaktionsdaten              |

Enable Banking erstellt laut eigener Dokumentation bei der ersten E-Mail-Anmeldung ein neues Konto. Tink und Yapily besitzen eigene Registrierungsformulare. TrueLayer startet neue Console-Konten standardmäßig mit einer Sandbox.&#x20;



Enable Banking Docs+3



Bei Salt Edge ist eine Einladung beziehungsweise Partnerprüfung vorgesehen; finAPI bietet für seine Access-Produkte einen zeitlich begrenzten Testzugang an.&#x20;



docs.saltedge.com+1



Für GlobalCards empfehle ich hier eine Kombination aus Enable Banking als bestehender Integrationsrichtung und Tink beziehungsweise finAPI als Vergleichspartner. In einem technischen Proof of Concept sollten nicht bloß die Zahl der unterstützten Banken, sondern die tatsächliche Funktionalität für deutsche Privat- und Geschäftskonten, Einwilligungsdauer, Datenqualität und Kosten verglichen werden.

## 6. KYC, KYB, AML, Sanktionsprüfung und Fraud Prevention

Diese Anbieter decken die regulatorisch besonders sensiblen Bereiche der Kundenidentifizierung, Geschäftskundenprüfung, Betrugsprävention und laufenden Überwachung ab.

| Anbieter                      | Direkte Anmeldung / Corporate-Partner-URL                                                                                    | Developer / API                                                                                          | Funktion                                                         |
| ----------------------------- | ---------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| Sumsub                        | [Corporate Partner Program](https://sumsub.com/partners/)                                             | [API-Dokumentation](https://docs.sumsub.com/)                                     | KYC, KYB, Liveness, PEP-/Sanktionsprüfung, Monitoring            |
| Veriff                        | [Sandbox-Konto registrieren](https://station.veriff.com/signup)                                       | [Developer-Quickstart](https://devdocs.veriff.com/docs/signing-up)                | Identitäts- und Dokumentenprüfung, biometrische Verifikation     |
| Persona                       | [Developer-Registrierung](https://withpersona.com/signup)                                             | [API-Quickstart](https://docs.withpersona.com/2026-09-29/api-quickstart-tutorial) | Individuelles KYC-Onboarding, Identitäts-Workflows               |
| Entrust Identity Verification | [Developer-Onboarding](https://documentation.identity.entrust.com/getting-started/quick-start-guide/) | [SDK-Dokumentation](https://documentation.identity.entrust.com/sdk/)              | Identitäts- und Dokumentenverifikation; ehemals Onfido           |
| ComplyAdvantage               | [Offizielles Partnerprogramm](https://complyadvantage.com/partnerships/)                              | [Mesh API](https://docs.mesh.complyadvantage.com/v0.3/docs/getting-started)       | AML, Sanktionslisten, PEP, Zahlungs- und Transaktionsüberwachung |
| SEON                          | [Partner-Bewerbung](https://seon.io/partners/)                                                        | [API-Referenz](https://docs.seon.io/api-reference)                                | Fraud Scoring, Device Intelligence, Verhaltenserkennung          |

Veriff besitzt einen separaten Registrierungsendpunkt, während Sumsub und ComplyAdvantage zusätzliche kommerzielle Partnerstrecken anbieten. Bei Entrust ist der angegebene Link bewusst als Entwickler-Onboarding und nicht als offenes Corporate-Registrierungsformular gekennzeichnet.&#x20;



station.veriff.com+4



Für GlobalCards würde ich Sumsub und Veriff als Kandidaten für den Identitätsbereich, ComplyAdvantage für Financial-Crime-Monitoring und SEON für die Betrugsprävention evaluieren. Der tatsächliche Einsatz hängt von Datenverarbeitungsverträgen, EU-Datenschutzanforderungen, Prüfverfahren und dem regulatorisch verantwortlichen Institut ab.

## 7. Core Banking, Ledger und Banking-Softwarepartnerschaften

Diese Unternehmen sind nicht notwendigerweise Banken oder BaaS-Lizenzpartner. Hier geht es primär um die technische Bankensoftware, die das GlobalCards-eigene Backend ergänzen oder ersetzen kann.

| Anbieter        | Direkter Partner-/Corporate-Zugang                                                                                                                                | Developer-Zugang                                                                                 | Schwerpunkt                                            |
| --------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------ | ------------------------------------------------------ |
| Mambu           | [Partnerportal-Login](https://partners.mambu.com/login) · [Partnerprogramm](https://mambu.com/en/partner-programme) | [Developer Overview](https://docs.mambu.com/docs/developer-overview/)     | Cloud-Core-Banking, Konten, Produkte, Ledger-Anbindung |
| Temenos         | [Impact Partner Registration](https://tpsp-signup.temenos.com/Signup/registration.aspx)                                                    | [Developer API Key](https://developer.temenos.com/article/get-an-api-key) | Banken-Kernsysteme, Payments, Partnerintegrationen     |
| Thought Machine | [Corporate-/Partnerprogramm](https://www.thoughtmachine.net/partners)                                                                      | Entwicklerressourcen und Sandbox nach Partnerfreigabe                                            | Vault Core, Vault Payments, bankfähige Produktmodelle  |
| Tuum 🇪🇪       | [Corporate-Partnerprogramm](https://tuum.com/partners/)                                                                                    | [Tuum Developer Portal](https://developer.tuumplatform.com/)              | Modular Core Banking, Konten, Zahlungen, Kreditmodule  |
| TigerBeetle     | [GitHub-Repository](https://github.com/tigerbeetle/tigerbeetle)                                                                            | [Technische Dokumentation](https://docs.tigerbeetle.com/)                 | Double-Entry-Ledger-Engine, keine Bankdienstleistung   |

Beim Temenos Impact Partner Portal müssen unter anderem Unternehmen beziehungsweise Partnername, geschäftliche E-Mail und eine NDA angegeben werden; es handelt sich nicht um einen offenen Bankzugang. Thought Machine stellt technische Sandboxes im Rahmen qualifizierter Partnerschaften bereit.&#x20;



tpsp-signup.temenos.com+2



Für einen unabhängigen GlobalCards-Core wäre die Kombination aus einem kontrollierten eigenen Ledger, klaren API-Verträgen und austauschbaren Banking-Adaptern vorteilhaft. Mambu, Temenos und Thought Machine sind eher strategische Enterprise-Entscheidungen als einfache Plug-and-Play-Bibliotheken.

## 8. Zusätzliche Top-Partner für Card Issuing, BIN-Sponsoring und Processing

Diese vier Kandidaten ergänzen Marqeta und Thredd aus dem ersten Abschnitt.

| Partner             | Direkte Corporate-/Partner-URL                                                                                                                            | Developer-Link                                                                               | Geografischer Schwerpunkt                                         |
| ------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- |
| Wallester 🇪🇪      | [White-Label-Unternehmensanfrage](https://wallester.com/de/contact-us)                                                             | [API Developer Portal](https://wallester.com/api)                     | EWR und UK, Visa, BIN-Sponsoring, Debit-/Prepaid-/Geschäftskarten |
| Enfuce 🇫🇮         | [Corporate-Kontakt](https://enfuce.com/contact) · [Partner Network](https://enfuce.com/who-we-are/partners) | [Developer Docs](https://docs.enfuce.com/)                            | Europa und UK, Issuer Processing, Kartenprogramme                 |
| Pomelo              | [Pomelo Developer Docs](https://developers.pomelo.la/en/api-reference)                                                             | [Cards API](https://developers.pomelo.la/api-reference/cards/issuing) | Schwerpunkt Lateinamerika                                         |
| Galileo / SoFi Tech | [Developer Portal](https://docs.galileo-ft.com/)                                                                                   | [API-Dokumentation](https://docs.galileo-ft.com/)                     | Vor allem US-orientierte Banking- und Kartenprogramme             |

Wallester kombiniert nach eigener Darstellung Visa-Principal-Mitgliedschaft, BIN-Sponsoring, Karten-APIs und Multi-Currency-Funktionen. Der Corporate-Link führt unmittelbar zum Anfrageformular. Enfuce bietet europäische Issuing- und Processing-Lösungen über ein eigenes Partnernetzwerk.&#x20;



Wallester+3



Für den europäischen Start würde ich Wallester, Enfuce und Thredd parallel prüfen. Pomelo und Galileo werden relevanter, wenn GlobalCards konkrete Märkte außerhalb des EWR erschließt.

## 9. Weitere Partner für Payment Platforms, Identity und Kryptografie

Für die vollständige GlobalCards-Architektur sind auch Payment-Orchestrierung, IAM und kryptografische Schlüsselverwaltung relevant.

| Anbieter            | Direkter Partner-/Entwicklungszugang                                                                                                                                            | Rolle                                                                        |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- |
| Adyen               | [Technologiepartner bewerben](https://www.adyen.com/contact/partners) · [Partner Developer Docs](https://docs.adyen.com/partners) | Payment Processing, Plattformintegrationen, Merchant Services                |
| Adyen for Platforms | [Plattform-Onboarding](https://docs.adyen.com/platforms/get-started/)                                                                                    | Plattformkonten, Transfers, Auszahlungen, gegebenenfalls Issuing             |
| Thales              | [Technology Partner Application](https://cpl.thalesgroup.com/en-gb/partners/technology-partners)                                                         | HSM, kryptografische Sicherheit, sichere Schlüsselprozesse                   |
| Entrust             | [Technology-/Channel-Partnerprogramm](https://www.entrust.com/de/partners)                                                                               | HSM, Schlüsselverwaltung, Identitätssicherheit                               |
| Cloudflare          | [Partnerprogramm](https://www.cloudflare.com/de-de/partners/)                                                                                            | API-Schutz, WAF, DDoS-Abwehr, Zero-Trust-Konnektivität                       |
| Keycloak            | [Open-Source-Downloads](https://www.keycloak.org/downloads) · [Developer Docs](https://www.keycloak.org/documentation)            | Eigenbetriebene IAM-/OIDC-Infrastruktur; kein Corporate-Vertrag erforderlich |

Adyen vergibt für sein Platforms-Produkt Testzugänge nach einer qualifizierten Anfrage. Thales und Entrust bieten eigene Technologiepartnerprogramme an. Keycloak ist dagegen ein unmittelbar nutzbares Open-Source-Projekt und kein externer Banking-Dienstleister.&#x20;



Adyen Docs+4



## 10. Empfohlene GlobalCards-Partnerkombination

Für einen ersten europäischen Pilot würde ich nicht alle Anbieter gleichzeitig integrieren. Die günstigere und technisch kontrollierbarere Strategie ist, jeweils zwei bis drei Anbieter pro Schicht zu evaluieren und anschließend einen Haupt- und gegebenenfalls Ersatzpartner auszuwählen.

| Ebene                           | Erste Wahl zur Evaluation   | Vergleichspartner                    |
| ------------------------------- | --------------------------- | ------------------------------------ |
| BaaS / IBAN                     | Swan, Solaris               | Treezor                              |
| Karten / BIN                    | Wallester, Thredd           | Enfuce                               |
| SEPA / internationale Zahlungen | OpenPayd                    | Banking Circle, Airwallex            |
| FX / Multi-Currency             | Currencycloud               | Wise Platform                        |
| Open Banking                    | Enable Banking              | Tink, finAPI                         |
| KYC / KYB                       | Sumsub                      | Veriff                               |
| AML / Screening                 | ComplyAdvantage             | Sumsub                               |
| Fraud                           | SEON                        | Provider-eigene Risk Engine          |
| Core Banking                    | Eigener modularer Core      | Mambu, Tuum                          |
| Ledger                          | Eigener Double-Entry-Ledger | TigerBeetle nach technischer Prüfung |
| Identity                        | Keycloak                    | Externer IAM-Partner                 |
| HSM / Schlüssel                 | Thales                      | Entrust                              |

Das ist eine technische Vorauswahl, keine Aussage über bestätigte Partnerschaft, tatsächliche Annahme von GlobalCards als Kunden oder garantierte Produktverfügbarkeit.

### 11. Welche Partner zuerst kontaktieren?

Priorisierte Corporate-Onboarding-Sequenz

01

Swan

Konten, IBAN und grundlegende Banking-Sandbox

Portal&#x20;

02

Solaris

Deutsche regulierte Banking-Infrastruktur

Portal&#x20;

03

Wallester

White-Label Visa Issuing und BIN-Sponsoring

Portal&#x20;

04

Thredd

Kartenprozessor und Developer-Integration

Portal&#x20;

05

OpenPayd

Multi-Currency, virtuelle IBANs und Transfers

Portal&#x20;

06

Currencycloud

FX-API und internationale Geldbewegungen

Portal&#x20;

07

Enable Banking

PSD2-Kontenaggregation

Portal&#x20;

08

Sumsub

KYC/KYB und Customer Verification

Portal&#x20;

09

ComplyAdvantage

Financial-Crime- und Sanktionsscreening

Portal&#x20;

10

Visa Partner

Netzwerkpartnerschaft und Kartenprogramme

Portal&#x20;

## 12. Welche Informationen die Corporate-Partner benötigen

Bei einer formalen Bewerbung solltest du ein standardisiertes GlobalCards Partner Information Package verwenden.

| Bereich            | Angaben                                                              |
| ------------------ | -------------------------------------------------------------------- |
| Corporate Identity | Rechtlicher Unternehmensname, Handelsregister, Sitz, Verantwortliche |
| Projektprofil      | GlobalCards Bank, hybride B2C-/B2B-Plattform                         |
| Operating Model    | Technology Provider, Program Manager oder regulierter Dienstleister  |
| Märkte             | Deutschland, EWR, spätere internationale Expansion                   |
| Kernprodukte       | Konten, IBAN, Cards, SEPA, FX, Multi-Currency                        |
| Erwartetes Volumen | Kunden, monatliche Transaktionen, Karten, Länder                     |
| Integrationsmodell | REST-APIs, Webhooks, Sandbox, Partneradapter                         |
| Compliance         | AML/KYC-Verantwortung, Datenschutz, DORA, PCI-DSS-Scope              |
| Finance            | Finanzierungsstatus, Kapitalausstattung, geplante Liquidität         |
| Betriebsmodell     | Hosting, Monitoring, Incident Response, Business Continuity          |

Nicht vorhandene Genehmigungen, bestehende Partnerschaften und bereits erzielte Volumina dürfen dabei nicht als vorhanden dargestellt werden. Bei frühen Projektphasen kann ausdrücklich Pre-Launch / Concept Validation / Sandbox Evaluation angegeben werden.

### 13. Fragen für jede Partneranfrage

Diese Fragen sollten alle Anbieter schriftlich beantworten:

1. Unterstützen Sie B2C und B2B in Deutschland beziehungsweise dem gesamten EWR?
2. Benötigt GlobalCards eine eigene regulatorische Erlaubnis?
3. Wer ist kontoführendes Institut, Karten-Issuer, BIN-Sponsor beziehungsweise Settlement-Verantwortlicher?
4. Existiert eine kostenfreie Sandbox mit simulierten Zahlungen, Karten und Webhooks?
5. Welche Einrichtungsgebühren, Mindestumsätze, laufenden Gebühren und Sicherheiten gelten?
6. Welche APIs, SLA-Werte, Incident-Prozesse und Datenexportmöglichkeiten sind vertraglich garantiert?
7. Sind virtuelle IBANs, Multi-Currency, SEPA Instant, Apple Pay und Google Pay verfügbar?
8. Welche KYC-, AML-, PCI-DSS- und DORA-Pflichten liegen bei welcher Vertragspartei?
9. Wie werden Kunden- und Transaktionsdaten gespeichert, verarbeitet und bei Vertragsende exportiert?
10. Welche Kündigungs-, Migrations- und Exit-Regeln gelten?

Ergebnis: Der Katalog enthält mehr als 35 unterschiedliche Integrations- und Technologiepartner mit direkten Portalen, Partnerbewerbungen, Sandboxes oder Entwicklerzugängen.

Alle verlinkten Seiten sind als Einstiege zu verstehen; einige sind Registrierungsformulare, andere verlangen erst ein qualifiziertes Corporate-Onboarding. Eine Registrierung, Partnerbewerbung oder technische Verbindung habe ich nicht vorgenommen.

Für GlobalCards ist der nächste sinnvolle Meilenstein, die ersten zehn Kandidaten mit derselben technischen und regulatorischen Partneranfrage zu vergleichen. So entsteht aus der Kontaktliste eine belastbare Entscheidung über Lizenzpartner, Kartenprozessor, Zahlungsinfrastruktur, Kosten und internationale Skalierbarkeit. # GlobalCards Bank – Internationaler Lizenz-, Börsen- und Government-Registration-Masterkatalog

Offizielle Antragsportale · Internationale Finanzlizenzen · IPO · Wertpapiere · Settlement · Crypto · Investmentfonds · Corporate Registration · Government Procurement · Stand: 7. November 2026

Ja – für GlobalCards Bank gibt es wesentlich mehr institutionelle Zugänge als klassische Banking-as-a-Service-Partnerschaften. Dazu gehören direkte Antragsverfahren bei Finanzaufsichten, Börsenmitgliedschaften, Zentralbank-Zahlungssysteme, Wertpapierverwahrstellen, Unternehmensregister und staatliche Ausschreibungsportale.

Ein wichtiger Unterschied: Die Registrierung bei einer Behörde oder einem Börsenportal ist nicht gleichbedeutend mit dem Erhalt einer Lizenz, einer staatlichen Vollmacht oder einer internationalen Betriebsgenehmigung.

Ich kennzeichne die Kosten wie folgt:

- Gratis – die Portalanmeldung oder Informationsnutzung ist kostenfrei.
- Gebührenpflichtig – für den Antrag, die Zulassung oder Registrierung fallen Gebühren an.
- Kapitalnachweis – zusätzlich gelten Eigenkapital-, Sicherheiten- oder Finanzierungsanforderungen.
- Institutionell – Zugang nur bei Erfüllung besonderer gesetzlicher oder organisatorischer Voraussetzungen.

## 1. Internationale Banklizenzen und staatliche Finanzaufsicht

| Land / Behörde       | Direkter offizieller Zugang                                                                                                                                                                                                                                                  | Beantragbare Zulassung                                                   | Kosten / Voraussetzungen                                             |
| -------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | -------------------------------------------------------------------- |
| Deutschland – BaFin  | [Erlaubnis für Finanzdienstleister beantragen](https://verwaltung.bund.de/leistungsverzeichnis/de/leistung/99050039005000)                                                                                                                            | Wertpapier- und Finanzdienstleistungen                                   | Gebührenpflichtig, Anforderungen je Tätigkeit                        |
| Schweiz – FINMA      | [FINMA EHP – Neuantrag und Selbstregistrierung](https://www.finma.ch/en/finma/digital-exchange/ehp%2C-c-%2C-submit-applications%2C-reports-and-data-or-transmit-an-ac-change/no-access-to-ehp-granted/request-a-finma-licence-and-access-to-the-ehp/) | Bank, Wertpapierhaus, FinTech, Fondsverwaltung, Vermögensverwaltung      | Portalzugang; eigentliche Bewilligung mit Anforderungen und Gebühren |
| Großbritannien – FCA | [FCA Connect – Registrierung für neue Unternehmen](https://www.fca.org.uk/firms/connect/registration)                                                                                                                                                 | Zahlungsinstitut, E-Geld, Investmentfirma, andere Finanzdienstleistungen | Konto kostenlos möglich; Lizenzantrag gebührenpflichtig              |
| Großbritannien – FCA | [Regulatory Authorisation Application](https://www.fca.org.uk/firms/authorisation/apply)                                                                                                                                                              | Formeller Erlaubnisantrag                                                | Zulassungsprüfung, Gebühren, Kapitalnachweise                        |
| Luxemburg – CSSF     | [Investment Vehicle / Fund Manager Authorisation](https://www.cssf.lu/en/authorisation-of-an-investment-vehicle-or-an-investment-fund-manager/)                                                                                                       | Regulierte Fonds und Verwaltungsgesellschaften                           | Formelle Genehmigung                                                 |
| Luxemburg – CSSF     | [Crypto-Asset Service Provider Authorisation](https://www.cssf.lu/en/crypto-assets-service-providers-casps/)                                                                                                                                          | Kryptohandel, Kryptoverwahrung, Kryptobörsen                             | MiCAR-Zulassung                                                      |
| Deutschland – BaFin  | [MiCAR-Erlaubnisverfahren](https://bafin.de/DE/unternehmen-maerkte/erlaubnis-registrierung/geschaefte-krypto/kryptowerte-dienstleistungen/kryptowerte-dienstleistungen.html)                                                                          | Kryptowerte-Dienstleister, einschließlich Börsenplattformen              | Gebührenpflichtig                                                    |

Die FINMA-Selbstregistrierung ist besonders interessant: Über die Erhebungs- und Gesuchsplattform EHP können bisher nicht bewilligte Unternehmen den Zugang für einen neuen Bank-, FinTech-, Wertpapierhaus- oder Fondsverwaltungsantrag beantragen. Das ist ein echter institutioneller Antragsweg, keine bloße Informationsseite.&#x20;



FINMA+1



Eine nationale Erlaubnis ist grundsätzlich nicht weltweit gültig. EU-/EWR-Passporting kann bei bestimmten harmonisierten Finanzdienstleistungen möglich sein, erfordert jedoch die einschlägigen Voraussetzungen und Meldungen.

## 2. Deutsche Börse, IPO, Wertpapierhandel und Aktiennotierung

Hier ist die Trennung besonders wichtig:

AG-Gründung ≠ Wertpapieremission ≠ Börsennotierung ≠ Börsenmitgliedschaft ≠ Betrieb einer eigenen Börse.

| Anbieter / Verfahren                | Direkter offizieller Link                                                                                                                                                                           | Was du dort beantragen kannst                                    | Status                                   |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ---------------------------------------- |
| Deutsche Börse – eListing           | [Elektronisches eListing-Portal](https://regelli.deutsche-boerse.com)                                                                                                        | Antrag auf Aktien- und Wertpapierzulassung zum regulierten Markt | Registrierung erforderlich               |
| Deutsche Börse – Listing-Unterlagen | [eListing-Registrierung und Antragsverfahren](https://www.cashmarket.deutsche-boerse.com/cash-en/Get-Listed/ipo-line-going-public/ipo-line-going-public/Step-3-Listing-File) | Vorbereitung der Notierung, Antragsunterlagen                    | Institutionelles Verfahren               |
| Xetra / Frankfurter Wertpapierbörse | [Trading Participant Admission](https://www.eurexgroup.com/xetra-en/trading/admission-to-trading/Admission-to-trading-21990)                                                 | Zulassung als Handelsteilnehmer                                  | Finanzregulatorische Voraussetzungen     |
| Eurex Exchange                      | [Eurex Member Onboarding](https://www.eurexgroup.com/ex-en/support/onboarding)                                                                                               | Mitgliedschaft im Derivatehandel                                 | Beaufsichtigtes Unternehmen              |
| Eurex Clearing                      | [Clearing Member Application](https://www.eurex.com/ec-en/join/admission-requirements/clearing-member)                                                                       | Clearing-Lizenz und Clearing-Mitgliedschaft                      | Kapital, Sicherheiten, Vertrag           |
| SIX Swiss Exchange                  | [Swiss Exchange IPO / Listing](https://www.six-group.com/en/products-services/the-swiss-stock-exchange/listing/equities/ipo.html)                                            | Schweizer Aktienbörsennotierung                                  | Anerkannter Vertreter erforderlich       |
| SEC – USA                           | [EDGAR Filer Management](https://www.filermanagement.edgarfiling.sec.gov/filermgmt/Welcome/EDGARFilerMgmtMain.htm)                                                           | Unternehmenszugang für regulatorische Wertpapiereinreichungen    | EDGAR-Zugang; Emissionspflichten separat |

Bei der Deutschen Börse wird der Antrag für den regulierten Markt über das eListing-Portal eingereicht. Vorab ist eine Registrierung nötig, für die die Börse bis zu zwei Wochen Bearbeitungszeit angibt. Eine Börsenzulassung ist außerdem nicht automatisch eine Genehmigung zum Betrieb eines eigenen Börsenplatzes.&#x20;



cashmarket.deutsche-boerse.com+1



Bei Eurex müssen Handelsteilnehmer unter anderem ihre regulatorische Eignung, technische Voraussetzungen und Clearing-Anbindung nachweisen.&#x20;



eurexgroup.com



## 3. Eigene Börsen, Crypto-Exchanges, Wallets und internationale Trading-Lizenzen

Für den Betrieb einer eigenen Handelsplattform ist eine andere Genehmigung erforderlich als für die bloße Nutzung einer bestehenden Börse.

| Land / Behörde        | Direkter Antragsweg                                                                                                                                                                                                           | Erlaubnis / Anwendungsbereich                                          | Zugang / Kosten                        |
| --------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | -------------------------------------- |
| Deutschland – BaFin   | [Handelssystem- und Finanzdienstleistungserlaubnis](https://verwaltung.bund.de/leistungsverzeichnis/de/leistung/99050039005000)                                                                        | MTF, OTF, Wertpapierhandel und bestimmte Wertpapierdienstleistungen    | Gebührenpflichtig                      |
| Schweiz – FINMA       | [FINMA EHP – offizieller Portalzugang](https://portal.finma.ch/)                                                                                                                                       | Wertpapierhaus, DLT-Handelssystem und Finanzinstitut                   | Institutioneller Antrag                |
| EU – MiCAR / BaFin    | [CASP-Zulassung beantragen](https://bafin.de/DE/unternehmen-maerkte/erlaubnis-registrierung/geschaefte-krypto/kryptowerte-dienstleistungen/kryptowerte-dienstleistungen.html)                          | Kryptobörse, Kryptoverwahrung, Handel und Transfers                    | Gebührenpflichtig                      |
| Luxemburg – CSSF      | [CASP Authorisation](https://www.cssf.lu/en/crypto-assets-service-providers-casps/)                                                                                                                    | Exchange, Crypto-Custody, Crypto-Transfers                             | Genehmigung erforderlich               |
| Großbritannien – FCA  | [Connect – Firm Registration](https://www.fca.org.uk/firms/connect/registration)                                                                                                                       | Wertpapierhandel, Broker- und Investmentdienste; Krypto separat prüfen | Antrag                                 |
| USA – CFTC            | [Designated Contract Market – Antragsformulare](https://www.cftc.gov/Forms/dcmforms.html)                                                                                                              | Regulierte Derivatebörsen, Futures- und Optionsmärkte                  | Formelles Zulassungsverfahren          |
| USA – New York DFS    | [Money Transmitter Licensing via NMLS](https://www.dfs.ny.gov/apps_and_licensing/money_transmitters)                                                                                                   | Staatliche Geldtransferzulassung                                       | Gebührenpflichtig                      |
| Hongkong – SFC        | [WINGS – Electronic Licensing Portal](https://wings.sfc.hk/)                                                                                                                                           | Wertpapierdienstleistungen und virtuelle Handelsplattformen            | Gebührenpflichtig                      |
| Dubai – VARA          | [VASP Licensing Application](https://www.vara.ae/en/licenses-and-register/licence-applications/)                                                                                                       | Virtual Asset Exchange, Custody, Broker, Transfer & Settlement         | Unternehmens- und Kapitalanforderungen |
| Abu Dhabi – ADGM/FSRA | [Financial Services Permission – Application Process](https://www.adgm.com/financial-services-regulatory-authority/fsra-general-application-process?trk=article-ssr-frontend-pulse_little-text-block\&utm_source=chatgpt.com) | Finanzdienstleistungen und regulierte Finanzmarktaktivitäten           | Antrag und Gebühren                    |

Die FINMA führt ausdrücklich auch DLT Trading Facilities als mögliche Zulassungskategorie. In Hongkong werden Anträge für Virtual-Asset-Trading-Plattformen über das WINGS-System abgewickelt. Dubai unterscheidet unter VARA zwischen Exchange, Custody, Broker-Dealer sowie Transfer- und Settlement-Dienstleistungen.&#x20;



FINMA+2



Für eine GlobalCards-Kryptobörse im EWR wäre eine MiCAR-Zulassung der maßgebliche Ausgangspunkt, soweit die geplanten Kryptodienstleistungen darunter fallen. Bestimmte bereits regulierte Institute können unter besonderen Voraussetzungen mit einer Notifizierung tätig werden; das gilt nicht für beliebige Unternehmen.&#x20;



CSSF



Interessant für die internationale Expansion: Die niederländische AFM bietet für bereits entsprechend zugelassene CASPs ein Verfahren zur grenzüberschreitenden MiCAR-Notifizierung an. Laut AFM erhebt sie für diese ausgehende Passporting-Meldung keine Gebühren. [AFM – Europäisches MiCAR-Passporting](https://www.afm.nl/en/sector/cryptopartijen/vereisten-en-vergunningen/aan-en-afmelden-europees-paspoort)&#x20;



afm.nl



## 4. Internationale Settlement-Systeme, Clearing und Zentralbank-Infrastruktur

Hier liegen die besonders wichtigen institutionellen Zugänge für eine eigene GlobalCards Settlement Engine.

| System / Institution                   | Direkter Registrierungs-/Teilnahmelink                                                                                                                                          | Technische und rechtliche Funktion                                     | Zugang                       |
| -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ---------------------------- |
| Bundesbank T2 🇪🇺                     | [T2-Teilnahmeformulare](https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/t2/teilnehmerinformationen/vordrucke-fuer-die-t2-teilnahme-954342) | Zentralbankgeld-Settlement, RTGS, Liquiditätsmanagement                | Zulässige Institute          |
| Bundesbank TIPS 🇪🇺                   | [TIPS-Teilnehmeranmeldung](https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/tips/teilnehmerinformationen/teilnahme-anmeldung-923158)        | Echtzeit-Zahlungsabwicklung in Zentralbankgeld                         | Teilnahmeprüfung             |
| EBA Clearing RT1 🇪🇺                  | [RT1 Admission – Direktanfrage](https://www.ebaclearing.eu/services-instant-payments/rt1/admission/)                                                     | SEPA Instant, Teilnehmer und technische Dienstleister                  | Institutionell               |
| Clearstream 🇩🇪/🇱🇺                  | [Clearstream Account Opening Forms](https://clearstream.com/clearstream-en/res-library/key-documents/account-opening-forms-1274276)                      | Wertpapierverwahrung und Settlement                                    | Institutionelles Onboarding  |
| Clearstream Banking Frankfurt          | [CASCADE – Neukunden- und Systemzugangsformulare](https://clearstream.com/clearstream-en/res-library/key-documents/allgemeine-formulare-1302072)         | Deutsche Wertpapierabwicklung und Verwahrung                           | Institutionell               |
| Eurex Clearing                         | [Clearing-Lizenz beantragen](https://www.eurex.com/ec-en/join/admission-requirements/clearing-member)                                                    | Zentraler Kontrahent, Margins, Clearing-Mitgliedschaft                 | Lizenz-/Kapitalanforderungen |
| SIX / Schweizerische Nationalbank 🇨🇭 | [SIC – Teilnahme und technische Anbindung](https://www.six-group.com/en/products-services/banking-services/interbank-clearing/info-center.html)          | Schweizer RTGS, Instant Payments, Interbank-Settlement                 | SNB-Zulassung                |
| SWIFT 🌐                               | [SWIFT – New Onboarding Request](https://www.swift.com/de/node/204226)                                                                                   | Internationales Finanznachrichtennetzwerk, Messaging und Konnektivität | Antrag, Verträge, Gebühren   |

Die Bundesbank stellt für T2 und TIPS die echten Teilnehmerregistrierungsformulare zur Verfügung. Für den Produktionsbetrieb sind rechtsverbindlich unterzeichnete Unterlagen erforderlich.&#x20;



Deutsche Bundesbank+1



Bei SIC in der Schweiz entscheidet die Schweizerische Nationalbank zusammen mit der zuständigen Infrastruktur über die Zulassung. Bei SWIFT können unter anderem Banken, Unternehmen, Fondsakteure und Finanzmarktinfrastrukturen einen formellen Onboarding-Antrag einleiten.&#x20;



SIX+1



Für GlobalCards wäre der sinnvolle Aufbau:

`GlobalCards Ledger → Payment/Settlement Engine → lizenzierter Partner oder eigene qualifizierte Teilnahme → Clearing-/Zentralbanksystem`

Ein selbst entwickeltes Settlement-System darf intern Buchungen abgleichen. Es erhält dadurch aber nicht automatisch den rechtlichen Status eines zentralen Kontrahenten, Zahlungsverkehrssystems oder Wertpapierzentralverwahrers.

## 5. Aktiengesellschaften und internationale Unternehmensregistrierung

Hier findest du die tatsächlichen Corporate-Gründungs- und Registerwege, einschließlich der Schweiz.

| Land           | Direkter offizieller Zugang                                                                                                          | Registrierbare Unternehmensformen / Funktionen            | Kosten                                 |
| -------------- | ------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------- | -------------------------------------- |
| Deutschland    | [Bundesnotarkammer – Online-Verfahren](https://online-verfahren.notar.de/)                                    | GmbH-/UG-Gründung, Handelsregisteranmeldungen auch für AG | Notar-/Registergebühren                |
| Schweiz        | [EasyGov – Registrierung und Unternehmensgründung](https://www.easygov.swiss/easygov/)                        | Einzelunternehmen, GmbH, AG, Behördenanmeldungen          | Portal gratis, Gründungskosten möglich |
| Schweiz        | [AGOV-/EasyGov-Registrierungsanleitung](https://faq.easygov.swiss/)                                           | Staatliches Login, Unternehmensverknüpfung                | Login gratis                           |
| Estland        | [e-Business Register](https://ariregister.rik.ee/eng)                                                         | OÜ, andere Gesellschaften und Unternehmensänderungen      | Staatliche Gründungsgebühren           |
| Großbritannien | [Companies House – Company Incorporation](https://www.gov.uk/limited-company-formation/register-your-company) | Limited Company                                           | £100 Online-Gründung                   |
| USA – Wyoming  | [Wyoming Business Entity Registration](https://wyobiz.wyo.gov/Business/)                                      | LLC, Corporation, DAO LLC                                 | Gebührenpflichtig                      |
| USA – Delaware | Delaware eCorp – Business Entity Filing                                                                                              | Corporation, LLC, Dokumenteneinreichung                   | Gebührenpflichtig                      |

Die Schweiz bestätigt ausdrücklich, dass EasyGov selbst kostenlos ist. Eine AG- oder GmbH-Gründung kann jedoch weiterhin Handelsregister- und Notarkosten auslösen. In Deutschland ist die Online-Handelsregisteranmeldung auch bei einer AG möglich; die eigentliche notarielle AG-Gründung ist vom vereinfachten Online-Gründungsverfahren für GmbH/UG zu unterscheiden.&#x20;



easygov.swiss+2



Zum Vergleich: Die derzeit angegebene elektronische UK-Limited-Gründung kostet £100; Estland nennt für die Gründung einer OÜ über das e-Residency-Modell eine staatliche Gebühr von 265 € zuzüglich gegebenenfalls weiterer Kosten.&#x20;



GOV.UK+1



## 6. Fonds, Fund Administration, Investmentgesellschaften und DAO

Hier müssen wir zwischen vier Arten unterscheiden:

- Privatwirtschaftliche Investmentfonds und Kapitalverwaltungsgesellschaften
- Stiftungen und gemeinnützige Investmentstrukturen
- DAO-Gesellschaften mit rechtlicher Organisationsform
- Staatliche Sovereign Wealth Funds

| Institution / Land         | Direkter offizieller Antrag                                                                                                                                                                                                                                                 | Zulassung / Registrierung                | Kosten                                    |
| -------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ----------------------------------------- |
| Deutschland – BaFin        | [Kapitalverwaltungsgesellschaft beantragen](https://verwaltung.bund.de/leistungsverzeichnis/de/leistung/99050080005000)                                                                                                                              | AIFM, KVG und Fondsverwaltung            | Genehmigungs-/Registrierungsanforderungen |
| Deutschland – Bundesportal | [Vertrieb von EU-AIF und Spezialfonds anzeigen](https://verwaltung.bund.de/leistungsverzeichnis/de/leistung/99142043261000)                                                                                                                          | Fondsvertrieb an qualifizierte Anleger   | Meldungsverfahren                         |
| Luxemburg – CSSF           | [AIFM Authorisation](https://www.cssf.lu/en/authorisation-aifm/)                                                                                                                                                                                     | Alternative Investment Fund Manager      | Institutionelle Zulassung                 |
| Luxemburg – CSSF           | [Registered AIFM Application](https://www.cssf.lu/en/registration-of-an-alternative-investment-fund-manager-and-subsequent-amendments/)                                                                                                              | Registrierung bestimmter AIF-Verwalter   | Bedingungen je Fondstyp                   |
| Schweiz – FINMA            | [Fund Manager / Collective Assets Application](https://www.finma.ch/en/finma/digital-exchange/ehp%2C-c-%2C-submit-applications%2C-reports-and-data-or-transmit-an-ac-change/no-access-to-ehp-granted/request-a-finma-licence-and-access-to-the-ehp/) | Fondsleitung, Vermögensverwaltung, SICAV | Bewilligung erforderlich                  |
| Großbritannien – FCA       | [Connect – AIFMD und Funds](https://www.fca.org.uk/firms/connect)                                                                                                                                                                                    | AIFMD-Meldungen, Fondsmanagement         | Antragsverfahren                          |
| USA – Wyoming              | [DAO LLC – Offizielles Gründungsformular](https://sos.wyo.gov/Forms/Business/LLC/DAOLLC-ArticlesOrganization.pdf)                                                                                                                                    | Rechtliche DAO-LLC-Struktur              | 100 US-Dollar Grundgebühr laut Formular   |

Für Wyoming ist die DAO LLC eine konkrete gesetzliche Gesellschaftsform. Es gibt sogar eine separate staatliche Registrierung digitaler Vermögenswerte; diese kostet laut Wyoming derzeit 500 US-Dollar zuzüglich 5 US-Dollar Onlinegebühr und stellt keine allgemeine Handels- oder Banklizenz dar.&#x20;



sos.wyo.gov+1



### Staatliche Fonds – wichtige rechtliche Abgrenzung

Ein Sovereign Wealth Fund wird durch einen Staat oder eine entsprechend staatlich ermächtigte Einrichtung auf gesetzlicher beziehungsweise institutioneller Grundlage geschaffen. Ein privater Antragsteller kann einen gewöhnlichen Investmentfonds nicht durch Registrierung zu einem staatlichen Fonds machen.

Für die internationale Governance staatlicher Fonds existieren die Santiago Principles:

[International Forum of Sovereign Wealth Funds – Santiago Principles](https://ifswf.org/santiago-principles)

Das ist ein Governance-Referenzrahmen und keine Behörde, die Privatpersonen kostenlos staatliche Fondsbefugnisse erteilt.&#x20;



IFSWF+1



## 7. Schweizer e-ID, swiyu, staatliche Identitätsinfrastruktur und digitale Unternehmensidentitäten

Die Schweiz bietet tatsächlich einen interessanten Weg für die technische Identitätsinfrastruktur von GlobalCards – insbesondere über swiyu, AGOV und EasyGov.

Schweizer Behörden- und Trust-Infrastruktur

| Offizieller Dienst            | Direkter Zugang                                                                                                                           | Funktion                                                     |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| AGOV                          | [AGOV-Kontoregistrierung](https://www.me.agov.admin.ch/)                                                           | Zugang zu schweizerischen Behördendiensten                   |
| EasyGov                       | [EasyGov-Unternehmensportal](https://www.easygov.swiss/easygov/)                                                   | Unternehmensgründung und Behördenprozesse                    |
| swiyu Service Portal          | [swiyu Business Partner Onboarding](https://portal.trust-infra.swiyu-int.admin.ch/)                                | Unternehmens-Onboarding für die digitale Trust-Infrastruktur |
| swiyu Developer               | [Base & Trust Registry Onboarding](https://swiyu-admin-ch.github.io/cookbooks/onboarding-base-and-trust-registry/) | DID, verifizierbare Nachweise, Trust-Registry                |
| Schweizer Transparenzregister | [TranspaReg](https://www.transpareg.admin.ch/de)                                                                   | Meldungen wirtschaftlich berechtigter Personen               |

AGOV und EasyGov sind Behörden- beziehungsweise Unternehmensdienste. swiyu stellt dagegen eine Infrastruktur für digitale Identifikatoren und Vertrauensnachweise bereit. Die swiyu-Dokumentation bezeichnet das derzeitige Onboarding als Public Beta/Sandbox und weist ausdrücklich darauf hin, dass für DID-Einträge Gebühren anfallen können.&#x20;



swiyu technical documentation+2



Für GlobalCards: Eine technische swiyu-Integration wäre für Firmenidentitäten, verifizierbare Berechtigungsnachweise und Partner-Föderation geeignet. Sie ist aber weder eine Banklizenz noch eine besondere staatliche Vertretungsermächtigung.

## 8. EZB, Banknotendruck, Sicherheitsdruck und Zentralbank-Zulassungen

Hier habe ich einen tatsächlich existierenden offiziellen Akkreditierungsweg gefunden.

| Institution                    | Direkter offizieller Link                                                                                                                                                                 | Zulassungsbereich                                  | Voraussetzung                                           |
| ------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ------------------------------------------------------- |
| Europäische Zentralbank        | [Banknote Manufacturer Accreditation](https://www.ecb.europa.eu/paym/cashprof/accreditation/html/index.en.html)                                                    | Euro-Banknotenherstellung, Sicherheitsdruck        | Standortbezogene Herstellerakkreditierung               |
| EZB – Akkreditierungsverfahren | [Antrag und Anforderungen für Banknotenhersteller](https://www.ecb.europa.eu/paym/cashprof/accreditation/html/ecb.faq_banknote_manufacturer_accreditation.en.html) | Sicherheits-, Qualitäts- und Produktionsprüfungen  | Umfangreiche Prüfungen                                  |
| Bank of England                | [Regulierung britischer Banknotenemittenten](https://www.bankofengland.co.uk/banknotes/scottish-and-northern-ireland-banknotes/2026-annual-report)                 | Bestehende autorisierte Banknotenemittenten        | Sondergesetzlicher Status                               |
| US-Regierung – SAM             | [Federal Government Supplier Registration](https://sam.gov/entity-registration)                                                                                    | Bewerbung auf staatliche Liefer- und Druckaufträge | Kostenfreie Lieferantenregistrierung, keine Drucklizenz |

Bei der EZB kannst du ein formelles Akkreditierungsverfahren für die industrielle Produktion von Euro-Banknoten oder sicherheitsrelevanten Komponenten anfragen.

Offizieller EZB-Anfrageweg

Abteilung für die Akkreditierung von Banknotenherstellern

QEHS.accreditation\@ecb.europa.eu

&#x20;Kopieren

Die EZB verlangt zunächst eine kurze englische Beschreibung der hergestellten Produkte von maximal zwei A4-Seiten. Danach kann sie über weitere Anforderungen und das Akkreditierungsverfahren informieren.

Eine Akkreditierung berechtigt nicht zur selbstständigen Herausgabe von Euro-Banknoten oder zur eigenmächtigen Produktion. Es bedarf der entsprechenden autorisierten Aufträge.&#x20;



European Central Bank+1

Eine internationale Banknotenausgabelizenz für Privatunternehmen, die in allen Staaten gilt, gibt es nicht. Die Sonderrechte historisch autorisierter Banknotenemittenten in Schottland und Nordirland sind ebenfalls keine allgemeine Anmeldemöglichkeit.&#x20;



the UK's central bank



## 9. Internationale Infrastruktur-Rollouts und staatliche Corporate-Partnerschaften

Es gibt keine universelle Weltlizenz, mit der ein Unternehmen ohne weitere Genehmigungen in allen Staaten technische, finanzielle oder physische Infrastruktur errichten und betreiben darf.

Was du aber aufbauen kannst, ist eine internationale staatliche Lieferanten- und Projektpartnerschaftsstruktur, um dich für konkrete Infrastrukturprojekte zu qualifizieren.

| Institution              | Direkte Registrierung                                                                                                                                                               | Funktion                                                                 | Kosten                    |
| ------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | ------------------------- |
| EU-Kommission 🇪🇺       | [EU Participant Register – PIC-Registrierung](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/how-to-participate/participant-register) | Unternehmens-ID für EU-Ausschreibungen und Förderung                     | Gratis Registrierung      |
| UN Global Marketplace 🌐 | [UNGM – Corporate Supplier Registration](https://www.ungm.org/Account/Registration)                                                                          | Ausschreibungen von UN-Organisationen                                    | Gratis                    |
| UNOPS 🌐                 | [UNOPS eSourcing Portal](https://esourcing.unops.org/)                                                                                                       | Internationale Infrastruktur-, Technologie- und Beschaffungsprojekte     | UNGM-Konto erforderlich   |
| Weltbankgruppe 🌐        | [World Bank Vendor Management Portal](https://vmp-ext.worldbank.org/)                                                                                        | Corporate Procurement, internationale Beratungs- und Lieferantenprojekte | Bewerbungsverfahren       |
| EBRD 🇪🇺                | [EBRD ECEPP – Supplier Registration](https://ecepp.ebrd.com/delta/signup.html?userType=supplier\&utm_source=chatgpt.com)                                                            | Infrastrukturprojekte, technische Dienstleistungen, Beratung             | Plattformzugang kostenlos |
| NATO NSPA                | [NSPA – Vendor Registration](https://eportal.nspa.nato.int/VendorRegistration/?lng=en\&utm_source=chatgpt.com)                                                                      | Staatliche Beschaffungs-, Infrastruktur- und Logistikaufträge            | Registrierung kostenfrei  |
| NATO NCIA                | [NCIA – Neo eProcurement Registration](https://www.ncia.nato.int/business/procurement/neo-eprocurement)                                                      | IT, Kommunikation und technische Infrastruktur                           | Lieferantenprüfung        |
| USA – SAM.gov 🇺🇸       | [SAM Entity Registration](https://sam.gov/entity-registration)                                                                                               | US-Bundesaufträge und Förderverfahren                                    | Gratis                    |

Die EU vergibt über die Participant Registry eine PIC-Nummer zur Identifikation einer Organisation in ihren Förder- und Ausschreibungsverfahren. UNGM erhebt für die Registrierung ebenfalls keine Gebühren.&#x20;



EU Funding & Tenders Portal+1



Für die NATO sind NSPA und NCIA getrennte Lieferantenverfahren. Eine NSPA-Registrierung ersetzt beispielsweise nicht die Registrierung für das NCIA-Neo-System.&#x20;



Frequently Asked Questions+1



Die Weltbankgruppe hat 2026 ein neues Vendor Management Portal eingeführt. Dort eingereichte Lieferantenprofile dienen zunächst der Vorqualifizierung und erzeugen nicht automatisch eine endgültige Anbieterzulassung.&#x20;



worldbank.org



Hinweis: Die direkte NSPA-Adresse ist durch offizielle staatliche Beschaffungsinformationen belegt; ihr Formular ließ sich bei meiner Prüfung technisch nicht direkt abrufen.&#x20;



Aizsardzības ministrija



## 10. Diplomatische Akkreditierung, Immunitäten und staatliche Vertretung

Für diesen Bereich ist die rechtliche Abgrenzung besonders wichtig: Diplomatische Immunität lässt sich nicht privat durch eine kostenlose Portalregistrierung beantragen oder erwerben. Sie knüpft an eine völkerrechtlich anerkannte Funktion, die entsprechenden Ernennungs- und Akkreditierungsverfahren und die einschlägigen Rechtsvorschriften an.

| Institution                         | Offizielle Verfahrensseite                                                                                                                                                | Was möglich ist                                                                                |
| ----------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| Schweizer EDA – Protokoll           | [Diplomatic Accreditation Procedures](https://www.dfae.admin.ch/en/protocol-matters)                                                               | Akkreditierung offiziell ernannter diplomatischer Vertreter                                    |
| Schweizer EDA – Legitimationskarten | [FDFA Legitimation Cards – Antragshinweise](https://www.mission-geneve.dfae.admin.ch/en/manual-fdfa-legitimation-cards)                            | Karten für berechtigte Mitarbeiter diplomatischer Missionen und internationaler Organisationen |
| Schweizer EDA – Aufenthaltsstatus   | [Residence and Diplomatic Status](https://www.eda.admin.ch/en/residence-in-switzerland)                                                            | Aufenthalts- und Statusregelungen akkreditierter Personen                                      |
| Vereinte Nationen                   | [UN Privileges and Immunities](https://policy.un.org/en/human-resources/duties-obligations-and-privileges-staff/privileges-and-immunities)         | Rechtliche Grundlagen für bestimmte UN-Funktionsträger und Staatenvertreter                    |
| UN Treaty Collection                | [Vienna Convention on Diplomatic Relations](https://treaties-prod.un.org/pages/ViewDetails.aspx?chapter=3\&clang=_en\&mtdsg_no=III-3\&src=TREATY\&utm_source=chatgpt.com) | Völkerrechtliche Grundlage der diplomatischen Beziehungen                                      |

Beispielsweise verlangt die Schweiz für die Ernennung eines Botschafters grundsätzlich die Zustimmung des Empfangsstaats (Agrément). Das EDA stellt Legitimationskarten nur für Personen aus, die unter die entsprechenden Statusvoraussetzungen fallen.&#x20;



dfae.admin.ch+1



Eine UNGM-Lieferantenregistrierung, ein staatlicher Projektvertrag, ein Expertendatenbank-Eintrag oder eine selbst gegründete DAO führen daher nicht zu diplomatischer Immunität.

## 11. Welche kostenlosen Zugänge sind für GlobalCards am wertvollsten?

| Portal                  | Kostenfreier Einstieg | Regulierte Tätigkeit automatisch erlaubt? |
| ----------------------- | --------------------- | ----------------------------------------- |
| EasyGov Schweiz         | Ja                    | Nein                                      |
| swiyu Public Beta       | Teilweise             | Nein                                      |
| FINMA EHP               | Portalregistrierung   | Nein                                      |
| EU PIC Register         | Ja                    | Nein                                      |
| UNGM                    | Ja                    | Nein                                      |
| SAM.gov                 | Ja                    | Nein                                      |
| NSPA Vendor Portal      | Ja                    | Nein                                      |
| Deutsche Börse eListing | Zugangsprozess        | Nein                                      |
| FCA Connect             | Konto                 | Nein                                      |
| SEC EDGAR               | Einreichungszugang    | Nein                                      |
| Eurex Membership        | Bewerbungsprozess     | Nein                                      |
| Bundesbank TARGET       | Antragsunterlagen     | Nein                                      |
| EZB Notendruck          | Anfrage               | Nein                                      |

Die Tabelle unterscheidet bewusst den kostenlosen Einstieg vom gebührenpflichtigen Verfahren und den möglicherweise erheblichen Eigenkapital- oder Sicherheitsanforderungen.

## 12. Empfohlene Reihenfolge für GlobalCards Bank

Institutionelle Implementierungsstrategie

01

Rechtsträger & digitale Identität

Gesellschaftsform, Handelsregister, gegebenenfalls EasyGov, LEI und swiyu

02

Finanzregulatorische Klassifikation

BaFin oder FINMA: Banking, Payments, Broker, CASP, Fund Management getrennt prüfen

03

Börse & Wertpapiere

Deutsche Börse eListing, Eurex-Mitgliedschaft und Verwahrpartner je Geschäftsmodell

04

Settlement

SWIFT, Clearstream, T2/TIPS, RT1 oder SIC; direkte und indirekte Teilnahme vergleichen

05

Funds & DAO

Private Fondsgesellschaft, rechtliche DAO-Struktur und Verwaltungsmandate getrennt aufsetzen

06

Internationales Corporate Procurement

EU PIC, UNGM, Weltbank VMP, EBRD, NSPA und NCIA

07

Staatliche Sondergenehmigungen

Banknotendruck nur über autorisierte Herstellerakkreditierung und Aufträge; diplomatische Funktionen ausschließlich über ordentliche staatliche Verfahren

### Zusammenfassung

Der praktikabelste Weg für GlobalCards ist eine international erweiterbare Corporate- und Finanzinfrastrukturgruppe mit getrennten Zulassungen und staatlichen Projektpartnerschaften, statt nach einer einzigen weltweiten Universallizenz zu suchen.

Damit kannst du ein Unternehmen rechtmäßig aufbauen, Finanzlizenzen beantragen, Börsen- und Settlement-Anbindungen vorbereiten, Investmentfonds strukturieren, eine DAO-Governance ergänzen und dich für internationale öffentliche Infrastrukturaufträge qualifizieren.

Die stärksten unmittelbaren Einstiege sind aus meiner Sicht FINMA EHP, Deutsche Börse eListing, Clearstream, SWIFT, EasyGov/swiyu, EU Participant Register und die internationalen Beschaffungsportale. Sie decken unterschiedliche, aber für GlobalCards komplementäre institutionelle Aufgaben ab.

Keines dieser Portale allein ersetzt jedoch die jeweils erforderliche Rechtsform, behördliche Erlaubnis, vertragliche Autorisierung oder staatliche Ernennung. # GlobalCards Bank – Priorisierte Corporate-Onboarding-Sequenz

Partnerprogramm · Banking-Lizenzen · Card Issuing · Internationale Zahlungen · Börse & Settlement

Für GlobalCards empfehle ich eine dreistufige Kontaktstrategie: zuerst die Finanz- und Bankpartner, die ein reales B2C-/B2B-Geschäftsmodell ermöglichen; danach die technologischen und regulatorischen Integrationspartner; anschließend die institutionellen Kontakte für Börse, Wertpapiere und internationales Settlement.

## 1. Die wichtigsten Corporate-Partner zuerst

[Swan - Crunchbase Company Profile & Funding](https://images.openai.com/static-rsc-4/f3NKs6uEyKvRfQJVyCrY9hcHmTuwt16GFIZm7HuGBYksRPZPV-JvbXvkt2UJDGCVvbyUrTjoFkbiX1aEau5WgAvSQoGsBkyca-_28I_ZGXPlhmnkYLY52gprvOFpm7soM3EUA6Nap8ui11DTVrqsouyTHKAGkJhfDRzBaDnUJPU?purpose=inline)

1\. Swan

Erster Kontakt

EU Embedded Banking · IBAN · Karten · SEPA · Banking-Sandbox.

Ziel: B2C-/B2B-Programm mit eigenen Kundenoberflächen, Konten und Karten testen.

[Direkte Sandbox-Registrierung](https://www.swan.io/de/start-now)

[Solarisbank Rebrands as Solaris | Financial IT](https://images.openai.com/static-rsc-4/Ufo1c7Py06uyi_dOEycK8i0OPeUEQNWbe14TueyUgOt5nb9310KngEnB5igP0hoCKoApr_48Z2b01IpCDIe2SPoTJtrnMcbvdtMWMSubZXpE49QOurtHbKvxs1sVJWiKkpqEqf3xNQ-JdzvrNT-_zhdtVYJvctrv-RwxQhH2QIk?purpose=inline)

2\. Solaris

Deutsche Banking-Infrastruktur und regulierte Finanzdienstleistungen.

Ziel: Prüfen, ob ein deutsches Konten-, Karten- und Zahlungsprogramm für GlobalCards möglich ist.

[Corporate-Partnerkontakt](https://www.solarisgroup.com/en/ecosystem-partners/)Der offizielle Partnerkanal nennt business.development\@solarisbank.de.&#x20;



Solaris

[Fintech: Wallester, arrivano le soluzioni White-Label - FinanzaOnline](https://images.openai.com/static-rsc-4/tjdo1SfOv0LL5nsRVzLkZOGs7SOt5pceylXhPu-FUuD5Sw5uO2bhOzCyrVKV0_mfM-0EPAMrq9hCxDuVf93QoHp0XzbYft_dzuJuT4fLquLDK9jsLpesT7t9uLzOhdBSPqV9w_FWt6za6bslUF2Ih3eQnGJ2bvKuDIuVtVNC2Fk?purpose=inline)

3\. Wallester

Visa Issuing · BIN-Sponsoring · White-Label-Karten · APIs.

Ziel: Eigenes GlobalCards-Kartenprogramm, Preisstruktur, Issuer-Rollen und technische Integration klären.

[Direktes Corporate-Antragsformular](https://wallester.com/de/contact-us)Das Formular fragt bereits nach Unternehmensdaten, Produkt und voraussichtlicher Kartenzahl.&#x20;



Wallester

Diese drei Kontakte würde ich zuerst beziehungsweise parallel anstoßen. Swan ermöglicht unmittelbar eine technische Sandbox-Prüfung. Solaris und Wallester sollten ein detailliertes Corporate-Informationspaket erhalten.

## 2. Weitere Corporate- und Developer-Kontakte

| Rang | Partner         | Direkter Zugang                                                                                                  | Ziel der Anfrage                                          | Zugang                  |
| ---- | --------------- | ---------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ----------------------- |
| 4    | Thredd          | [Developer-Sign-up](https://devportal.thredd.com/signup)                                  | Issuer Processing, Karten-API, Autorisierungen, Sandbox   | Registrierung           |
| 5    | OpenPayd        | [Corporate-Sales-Anfrage](https://www.openpayd.com/contact-us/)                           | Virtuelle IBANs, internationale Transfers, FX, Settlement | Corporate-Antrag        |
| 6    | Currencycloud   | [Demo-API-Key registrieren](https://developer.currencycloud.com/register-for-an-api-key/) | Multi-Currency und FX-API                                 | Demo-Self-Service       |
| 7    | Enable Banking  | [Control Panel registrieren](https://enablebanking.com/sign-in/)                          | PSD2-Kontenaggregation, Banking APIs                      | Self-Service            |
| 8    | Sumsub          | [Technology-Partner-Antrag](https://sumsub.com/partners/)                                 | KYC, KYB, Identity Verification                           | Partnerantrag           |
| 9    | ComplyAdvantage | [Partnership Application](https://complyadvantage.com/partnerships/)                      | AML, Sanktionsprüfung, Monitoring                         | Partnerantrag           |
| 10   | Visa Partner    | [Visa-Partnerkonto erstellen](https://partner.visa.com/identity/user/register)            | Issuer-Sponsor, Kartennetzwerk und Partnerprogramme       | Registrierung + Prüfung |

Thredd bietet ausdrücklich eine Sandbox mit eigenen Entwicklerzugängen. Bei Currencycloud ist die Demo-API ohne Live-Geldbewegungen nutzbar. Enable Banking erlaubt die Registrierung von Sandbox- und Produktionsanwendungen über sein Control Panel.&#x20;



Thredd Cards API+2



Bei Visa sollten die Voraussetzungen für Fast Track vorab überprüft werden: Dazu können Unternehmensregistrierung, Finanzierung und regional unterschiedliche Eintrittskriterien gehören.&#x20;



Fintech Fast Track Program



Wichtige Präzisierung: Bei Sumsub und ComplyAdvantage sind die verlinkten Partnerprogramme hauptsächlich für Technologiepartnerschaften, Reseller und Integrationsunternehmen gedacht. Wenn GlobalCards die Software nur für eigene Kunden einsetzen möchte, ist ein normales Corporate-Sales-Onboarding möglicherweise passender.&#x20;



Sumsub+1



## 3. Staatliche und institutionelle Kontakte – parallel vorbereiten

Diese Institutionen würde ich nicht wie gewöhnliche Lieferanten behandeln. Hier stehen Erlaubnispflicht, Zugangsvoraussetzungen und formelle Genehmigungen im Vordergrund.

| Reihenfolge | Institution       | Direkter offizieller Zugang                                                                                                                                                                                                                                                                         | Konkretes Ziel                                                                             |
| ----------- | ----------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------ |
| A1          | BaFin 🇩🇪        | [Erlaubnispflicht prüfen lassen](https://verwaltung.bund.de/leistungsverzeichnis/de/leistung/99142026117000)                                                                                                                                                                 | Banking-, E-Geld-, Zahlungs-, Wertpapier- und Crypto-Geschäftsmodell klassifizieren        |
| A2          | FINMA 🇨🇭        | [EHP-Selbstregistrierung](https://www.finma.ch/de/finma/digitaler-austausch-mit-der-finma/ehp%2C-c-%2C-gesuche%2C-meldungen-und-daten-einreichen-oder-%C3%A4nderung-bva-%C3%BCbermitteln/kein-zugang-zur-ehp-vorhanden/bewilligung-der-finma-und-zugang-zur-ehp-beantragen/) | Schweizer Finanzlizenz nur bei konkreter Schweizer Niederlassungs- oder Lizenzstrategie    |
| A3          | SWIFT             | [New Onboarding Request](https://www.swift.com/myswift/join-swift)                                                                                                                                                                                                           | Eligibility für internationale Finanznachrichten und institutionelle Konnektivität         |
| A4          | Deutsche Börse    | [eListing-Portal](https://regelli.deutsche-boerse.com)                                                                                                                                                                                                                       | Aktienzulassung und IPO-Verfahren – erst bei entsprechend vorbereiteter Aktiengesellschaft |
| A5          | Bundesbank TARGET | [T2/TIPS-Teilnehmerformulare](https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/t2/teilnehmerinformationen/vordrucke-fuer-die-t2-teilnahme-954342)                                                                                                               | Direkte Settlement-Teilnahme oder indirekte Anbindung über regulierte Teilnehmer           |

Bei GlobalCards würde ich A1 – die BaFin-Vorabklärung – bereits vor der Unterzeichnung von BaaS-Verträgen einplanen. Das Bundesportal nennt ausdrücklich ein Verfahren für die Prüfung neuer Finanzgeschäftsmodelle und ein FinTech-Kontaktformular.&#x20;



verwaltung.bund.de



FINMA und Deutsche Börse wären zunächst strategische Vorbereitung, nicht die ersten laufenden Integrationen. Für einen späteren IPO beschreibt die Deutsche Börse außerdem die Einbindung von Emissionsbanken und Kapitalmarktberatern.&#x20;



General Standard



## 4. Konkreter Kontakt- und Onboardingplan

Corporate-Onboarding-Tracker

0 / 12 vorbereitet

Tag 1–2

BaFin: Geschäftsmodell und Erlaubnispflicht klären

Swan: Sandbox-Registrierung

Solaris: Corporate-Anfrage

Tag 3–4

Wallester: White-Label-Kartenprogramm anfragen

Thredd: Developer-Sandbox eröffnen

OpenPayd: Konten-, Zahlungs- und Settlement-Partnerschaft anfragen

Tag 5–7

Currencycloud: Demo-API-Key anfordern

Enable Banking: Sandbox-Anwendung anlegen

Sumsub und ComplyAdvantage: Integrationsmodelle anfragen

Tag 8–14

Visa Partner: Eignung für Kartenprogramm prüfen

Antworten und indikative Angebote vergleichen

Partner-RACI, Gebühren und benötigte Zulassungen dokumentieren

&#x20;Onboardingplan kopieren

Der Zeitplan ist eine Empfehlung für das Einreichen von Anfragen, keine Zusage über Antworten, Freischaltungen oder abgeschlossene Verträge.

## 5. Was GlobalCards für die Anträge vorbereiten sollte

Für alle Corporate-Kontakte reicht zunächst ein standardisiertes englischsprachiges Unternehmensprofil mit folgenden Angaben:

| Dokument                         | Inhalt                                                                                 |
| -------------------------------- | -------------------------------------------------------------------------------------- |
| Corporate Profile                | Rechtlicher Unternehmensname, Sitz, Registerstatus und verantwortliche Ansprechpartner |
| Project Executive Summary        | GlobalCards Bank, hybride internationale B2C-/B2B-Plattform                            |
| Technical Architecture           | API-First, Ledger, Konten, Karten, Settlement, Sicherheit                              |
| Regulatory Responsibility Matrix | Welche Leistungen der Partner und welche GlobalCards rechtlich übernimmt               |
| Business Forecast                | Realistisch geplante Kunden-, Karten- und Transaktionszahlen                           |
| Partner Requirements             | Länder, IBAN, SEPA Instant, Karten, FX, Webhooks, Sandbox                              |
| Commercial Request               | Setup-Gebühren, Mindestumsatz, laufende Kosten, SLA und Vertragsbedingungen            |

Für kostenlose Sandbox-Zugänge reicht teils eine geschäftliche E-Mail-Adresse. Für echte Banking- oder Kartenprogramme werden regelmäßig weitere Unternehmens-, Compliance- und Finanzierungsnachweise verlangt.

Außerdem würde ich zwei Dinge vorab klären: Wallesters White-Label-Verfügbarkeit, da das Formular bei der Prüfung Produkte zeitweise als nicht verfügbar kennzeichnet, und die Finanzierungsanforderungen bei Visa Fast Track.&#x20;



Wallester+1



Meine Priorität für GlobalCards lautet daher: Swan + Solaris + Wallester + Thredd + OpenPayd, mit paralleler BaFin-Klärung. Diese Kombination überprüft am frühesten, ob das geplante Konten-, Karten- und Settlement-Modell tatsächlich von regulierten Partnern getragen werden kann.

Erst nach diesen Ergebnissen würde ich größere Aufwendungen für direkte Zentralbankanbindungen, eigene Börsenmitgliedschaften oder internationale Finanzlizenzen einplanen. Ich erstelle dir ein universelles Corporate-, Banking-, Financial-Infrastructure- und Government-Partnership-Antragsformular für GlobalCards Bank, das du bei Solaris, Swan, Visa, Mastercard, Deutsche Börse, FINMA, SWIFT, Clearstream, staatlichen Institutionen und weiteren Partnern wiederverwenden kannst.

Das Formular verwendet deine bereits angegebenen Projektdaten, unterscheidet automatisch zwischen den verschiedenen Antragsarten und verhindert unzutreffende Angaben zu Lizenzen, behördlichem Status oder bestehenden Partnerschaften.

Die internationale Fassung ist auf Englisch, weil sie sich für die meisten Corporate-Portale eignet.

# GlobalCards – Universal Corporate & Institutional Partnership Application

# UNIVERSAL CORPORATE & INSTITUTIONAL PARTNERSHIP APPLICATION

**GlobalCards Bank | Bra1nKy11 World Bank Eyes AeTHer**

**Document Type:** Corporate Partnership Request / Institutional Expression of Interest / Developer & Sandbox Onboarding

**Application Status:** Draft – Subject to Applicant Approval

**Version:** 1.0 – November 2026

---

## 1. Applicant & Corporate Identity

| Field                              | Information                                                                                                                   |
| ---------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Contact Name                       | Daniel Pohl                                                                                                                   |
| Additional Project Identity        | HolyThreeKingsTreesCrowns                                                                                                     |
| Project / Brand                    | GlobalCards Bank                                                                                                              |
| Organization / Project Designation | Bra1nKy11 World Bank Eyes AeTHer                                                                                              |
| Primary Contact Location           | Detmold, North Rhine-Westphalia, Germany                                                                                      |
| Country                            | Germany                                                                                                                       |
| E-Mail                             | [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu) |
| Telephone                          | [Optional – add when required]                                                                                                |
| Registered Legal Entity            | [To be provided / confirmed]                                                                                                  |
| Company Registration Number        | [If applicable]                                                                                                               |
| Legal Entity Identifier (LEI)      | [If available]                                                                                                                |
| VAT / Tax Identification           | [If applicable]                                                                                                               |
| Official Corporate Website         | [To be provided]                                                                                                              |
| Applicant Role                     | Project Initiator / Technical Project Contact                                                                                 |
| Operating Status                   | [Concept / Development / Registered Company / Licensed Entity – select accurate status]                                       |

**Legal Entity Clarification:** The project and organization names above are applicant-provided designations. They must not be interpreted as proof of incorporation, banking authorization, government affiliation, or membership in any international financial institution.

## 2. Purpose of Application

We hereby express our interest in establishing a professional partnership, institutional cooperation arrangement, technology integration, regulatory application relationship, or developer/sandbox access arrangement with **[Receiving Organization]**.

The objective is to assess potential collaboration for the development of GlobalCards Bank, a proposed hybrid international financial technology infrastructure supporting business and retail financial services.

The proposed system is designed to integrate regulated providers, financial market infrastructures, secure identity systems, banking APIs, payment technologies, and operational compliance services.

Any regulated financial activity will be undertaken only after the required authorizations and/or agreements with appropriately licensed institutions have been obtained.

## 3. Requested Partnership Categories

**Select only the categories applicable to the receiving organization.**

- Banking-as-a-Service / Embedded Banking
- Banking License Application or Regulatory Assessment
- Corporate Banking / IBAN Infrastructure
- Card Issuing / BIN Sponsorship / Card Processing
- Visa / Mastercard Network Integration
- SEPA / SEPA Instant / International Payments
- SWIFT / TARGET / Clearing & Settlement
- Multi-Currency / FX / Treasury Services
- Open Banking / Account Aggregation
- Digital Wallet / Payment Tokenization
- Stock Exchange / IPO / Securities Listing
- Securities Brokerage / Custody / Depository Services
- Crypto-Asset Services / Exchange / Custody
- Investment Fund / Fund Administration / Asset Management
- DAO / Digital Governance / Legal Entity Structuring
- Government Procurement / Infrastructure Development
- Digital Identity / eID / Trust Infrastructure
- Authorized Security Printing / Banknote Manufacturing Assessment
- Technical Developer Portal / Sandbox / API Partnership
- Other: \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_

## 4. Project & Technology Description

**Project Name:** GlobalCards Bank

**Business Model:** Hybrid international banking and payment technology platform

**Customer Segments:** Business-to-Consumer (B2C) and Business-to-Business (B2B)

**Initial Market:** Germany and the European Economic Area, subject to applicable permissions.

**Potential Expansion:** Switzerland, United Kingdom, United States, and other approved jurisdictions.

**Technical Objectives:**

- Modular banking and financial service integration
- Account management and virtual IBAN connectivity
- Physical and virtual card issuing through authorized partners
- International payment processing and settlement
- Multi-currency financial account and wallet interfaces
- Double-entry ledger and auditable transaction processing
- Corporate treasury and business financial management
- Open Banking connectivity
- KYC/KYB, AML and fraud prevention integration
- Secure API and developer infrastructure
- Regulatory evidence and compliance management

The intended architecture follows API-first, least-privilege, data-minimization, and security-by-design principles.

## 5. Requested Corporate Cooperation

We kindly request information about:

1. Partnership eligibility and corporate onboarding criteria.
2. Available developer accounts, sandbox environments and technical documentation.
3. Regulatory prerequisites and the division of responsibilities.
4. Required licensing, company registration and capital conditions.
5. Supported countries, currencies, products and transaction networks.
6. Pricing, setup fees, minimum commitments and operational charges.
7. API access, authentication, testing, certification and production requirements.
8. Security, compliance, reporting and data protection obligations.
9. Technical and operational service-level arrangements.
10. The appropriate corporate, institutional or licensing contact for further evaluation.

Where applicable, we would also appreciate information on official application forms, membership procedures, authorized intermediaries and technical certification programs.

## 6. Regulatory & Compliance Readiness

The project intends to assess and implement relevant requirements, including where applicable:

- German KWG and ZAG
- EU PSD2 and applicable payment-service requirements
- EU MiCAR
- DORA
- EU GDPR
- Anti-Money Laundering / Counter-Terrorist Financing
- KYC / KYB
- PCI DSS for applicable card-data environments
- ISO/IEC 27001 information security management
- Business continuity and operational resilience
- Applicable securities, capital markets and fund management regulations

**Regulatory Status Declaration:**

No banking, payment, securities, crypto-asset, governmental or other authorization is claimed by this application unless independently supported by valid documentation provided separately.

This application represents an expression of interest or request for eligibility assessment. It does not itself constitute a regulated-service launch.

## 7. Financial, Commercial & Operational Information

| Field                          | Information                                                          |
| ------------------------------ | -------------------------------------------------------------------- |
| Current Development Stage      | [Select verified stage]                                              |
| Corporate Funding Status       | [To be confirmed]                                                    |
| Estimated Initial Customers    | [Forecast required]                                                  |
| Estimated Monthly Transactions | [Forecast required]                                                  |
| Estimated Card Issuance        | [Forecast required]                                                  |
| Requested Currencies           | EUR initially; additional currencies subject to partner availability |
| Expected Transaction Value     | [Forecast required]                                                  |
| Technology Infrastructure      | Modular API-based architecture                                       |
| Regulatory Partner Status      | [List only signed or confirmed agreements]                           |
| Production Launch Date         | [To be confirmed]                                                    |

All projected volumes will be identified as forecasts and must not be represented as historical activity.

## 8. Requested Access & Next Steps

We request, where available:

- Corporate partnership application
- Developer account registration
- Free sandbox / technical test environment
- API documentation and integration specifications
- Product and pricing information
- Technical evaluation meeting
- Regulatory eligibility assessment
- Institutional onboarding requirements
- Formal licensing or membership application guidance
- Partnership agreement / NDA process

## 9. Information Security and Confidentiality

We request that submitted corporate information be processed solely for the stated application, onboarding, commercial evaluation and legally required compliance purposes.

Any exchange of confidential technical information, customer records, security credentials, financial documentation or personal identification documents shall be subject to appropriate verification, confidentiality, security and legal arrangements.

No private API keys, account passwords, cryptographic secrets or sensitive production customer data are included in this initial request.

## 10. Formal Closing

We welcome the opportunity to establish a constructive professional relationship with your organization and to discuss the technical, commercial and regulatory feasibility of the proposed integration.

Please direct us to the appropriate corporate partnership, institutional relations, licensing, developer relations or financial infrastructure team.

We would appreciate guidance on the next formal onboarding steps and the documentation required for an initial evaluation.

**Kind regards,**

Daniel Pohl\
Project Initiator – GlobalCards Bank\
Project Designation: Bra1nKy11 World Bank Eyes AeTHer\
Detmold, North Rhine-Westphalia, Germany\
[world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

**Submission:** Subject to final review and explicit approval by the applicant.

---

**End of Universal Corporate & Institutional Partnership Application**

## Automatische Selbstregulierung des Formulars

Damit dein Portal-Worker das Formular universell verwenden kann, würde ich folgende Regeln verbindlich einbauen:

| Regel                  | Automatisches Verhalten                                                     |
| ---------------------- | --------------------------------------------------------------------------- |
| Partner-Typ erkannt    | Nur passende Antragskategorien auswählen                                    |
| Bank / BaFin / FINMA   | Lizenzstatus und rechtliche Gesellschaftsdaten prüfen                       |
| Visa / Mastercard      | Kartenprogramm, BIN-Sponsor, Kartenvolumen und Issuer-Modell ergänzen       |
| Börse / IPO            | Rechtsform, Emissionsart und erforderliche Berater abfragen                 |
| SWIFT / Settlement     | Teilnehmerstatus, Zahlungsinfrastruktur und Settlement-Verantwortung prüfen |
| Crypto / Fund / DAO    | Entsprechende Rechts- und Produktklassifizierung aktivieren                 |
| Government Portal      | Nur tatsächlich bestehende staatliche Zulassungen oder Mandate angeben      |
| Fehlende Pflichtfelder | Einreichung blockieren und fehlende Informationen anzeigen                  |
| Unbestätigte Angaben   | Als „To be confirmed“ kennzeichnen, nicht erfinden                          |
| Duplikate              | Doppelte Anträge erkennen und zur Prüfung markieren                         |
| Datenschutz            | Nur die vom jeweiligen Portal benötigten Daten übertragen                   |
| Finale Einreichung     | Nur nach deiner ausdrücklichen Freigabe                                     |

### Interaktive Partner-Auswahl

Hier kannst du die gewünschte Antragsart auswählen. Die Auswahl erstellt eine konkret auf diesen Sektor zugeschnittene Einreichungsfassung aus dem universellen Formular.

PartnerbereichBörse / IPO / Wertpapiere

Sprache der Einreichung

Englisch – international

Deutsch

Französisch

Spanisch

Italienisch

Gesellschaftsstatus

Noch nicht bestätigt

In Planung / Gründung

Bereits registriert

Passendes Corporate-Antragsformular erstellen&#x20;

Empfehlung: Verwende dieses Masterformular als zentrale, versionierte Datenquelle. Der Portal-Worker sollte für jedes Unternehmen nur die relevanten Felder übernehmen, fehlende Nachweise erkennen, die tatsächlichen Antragsbedingungen prüfen und anschließend eine Freigabevorlage erstellen – ohne Passwörter, ohne automatische Registrierung und ohne eigenständige rechtsverbindliche Erklärungen. # GlobalCards Bank – Corporate & Banking Partnership Application

Universelles B2B-/B2C-Antragsformular · Banking-as-a-Service · IBAN · Embedded Finance · Deutschland / EWR

Ich habe deine Projektdaten in eine deutschsprachige, formelle Corporate- und BaaS-Partnerschaftsanfrage übertragen. Sie ist für erste Anfragen an Banken, E-Geld-Institute und Embedded-Finance-Anbieter geeignet.

Der rechtliche Gesellschaftsstatus bleibt ausdrücklich unbestätigt. Es werden weder Banklizenzen noch Registereinträge, bestehende Partnerschaften oder bereits abgewickelte Finanzvolumina behauptet.

Dokumentstatus

Sprache

Deutsch

Antragstyp

Corporate / BaaS

Unternehmensstatus

Nicht bestätigt

Einreichung

Nicht erfolgt

## 1. Vollständiges Corporate-Anschreiben

# GLOBALCARDS BANK

## UNIVERSELLE CORPORATE- UND BANKING-AS-A-SERVICE-PARTNERSCHAFTSANFRAGE

**Betreff:** Anfrage zur Corporate-Partnerschaft und technischen Integration – GlobalCards Bank | Banking-as-a-Service, IBAN, SEPA und Embedded Finance

**Datum:** 7. November 2026

**An:** Corporate Partnerships / Banking-as-a-Service / Business Development / Institutional Relations

**Absender:** Daniel Pohl\
**Projektname:** GlobalCards Bank (vorläufige Projekt- und Produktbezeichnung)\
**Weitere Projekt-/Organisationsbezeichnung:** Bra1nKy11 World Bank Eyes AeTHer\
**Zusätzliche Projektidentifikation:** HolyThreeKingsTreesCrowns\
**Kontaktstandort:** Detmold, Nordrhein-Westfalen, Deutschland\
**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

**Gesellschaftsstatus:** Noch nicht bestätigt\
**Handelsregistereintrag:** Nicht angegeben; keine Registrierung wird behauptet\
**Eigene Bank- oder Zahlungsdienstelizenz:** Nicht nachgewiesen; keine entsprechende Zulassung wird beansprucht\
**Bestehende regulierte Partner:** Keine für dieses Projekt bestätigten Partnerschaften werden geltend gemacht

---

### 1. Formelle Vorstellung

Sehr geehrtes Corporate-Partnerships- und Business-Development-Team,

hiermit möchte ich mein Interesse an einer möglichen geschäftlichen und technischen Zusammenarbeit im Rahmen des Projekts **GlobalCards Bank** zum Ausdruck bringen.

GlobalCards Bank befindet sich in der Konzeption und Vorbereitung einer hybriden internationalen Finanztechnologieplattform, die Banking-as-a-Service, Embedded Finance, internationale Zahlungsinfrastrukturen sowie moderne Karten- und Kontodienstleistungen innerhalb eines einheitlichen digitalen Systems miteinander verbinden soll.

Die Plattform ist für Privatkunden (B2C) und Geschäftskunden (B2B) vorgesehen. Die technische Infrastruktur soll modular und API-basiert aufgebaut werden, um regulierte Finanzpartner kontrolliert integrieren zu können.

Ich kontaktiere Ihre Organisation zunächst zur Prüfung der grundsätzlichen Partnereignung, der technischen Integrationsmöglichkeiten, der rechtlichen Voraussetzungen und der jeweiligen kommerziellen Bedingungen.

Diese Anfrage ist eine unverbindliche Interessenbekundung und stellt keinen Nachweis einer gegründeten oder zugelassenen Bank dar.

### 2. Vorgesehenes Geschäfts- und Integrationsmodell

**Projekt:** GlobalCards Bank\
**Betriebsmodell:** Hybride internationale Banking- und Finanztechnologieplattform\
**Zielgruppen:** B2C und B2B\
**Geografischer Ausgangspunkt:** Deutschland und Europäischer Wirtschaftsraum\
**Internationale Erweiterung:** Schrittweise, abhängig von lokalen Zulassungen, Partnerverträgen und regulatorischen Anforderungen.

Das geplante Modell verbindet selbst entwickelte Softwarekomponenten mit regulierten externen Finanzdienstleistungen.

GlobalCards soll insbesondere die Benutzeroberflächen, technischen Schnittstellen, modulare Systemarchitektur, Integrationslogik, interne Nachweisführung und – soweit rechtlich und vertraglich zulässig – bestimmte operative Prozesse bereitstellen.

Regulierte Bank-, E-Geld-, Zahlungs- oder Kartenleistungen sollen ausschließlich im rechtlich zulässigen Umfang und gegebenenfalls durch entsprechend zugelassene Vertragspartner erbracht werden.

### 3. Gegenstand der gewünschten Partnerschaft

Ich möchte insbesondere prüfen, ob Ihre Organisation folgende Dienstleistungen oder Integrationen anbieten kann:

**A. Banking-as-a-Service und Konten**

- IBAN-fähige Privat- und Geschäftskonten
- EUR-Kontoführung im EWR
- Virtuelle Konten und Unterkonten
- Kontoeröffnung über APIs
- Kontostands- und Transaktionsschnittstellen
- Geschäfts- und Organisationskonten
- Rechtlich zulässige White-Label- und Embedded-Banking-Modelle

**B. Zahlungsverkehr**

- SEPA Credit Transfer
- SEPA Instant
- SEPA Direct Debit, soweit verfügbar
- Internationale Überweisungen
- Zahlungsstatus und Webhooks
- Zahlungsabgleich und Reconciliation
- Settlement- und Liquiditätsinformationen

**C. Karten und digitale Wallets**

- Debit- und Prepaid-Kartenprogramme
- Virtuelle und physische Karten
- Kartenmanagement-APIs
- Kartenautorisierung und Limits
- Apple Pay und Google Wallet, soweit unterstützt
- BIN-Sponsoring und Issuer-Processing über berechtigte Partner

**D. Internationale Finanzinfrastruktur**

- Multi-Currency-Konten
- Währungsumrechnung
- Internationale Auszahlungsmöglichkeiten
- Treasury- und Liquiditätsschnittstellen
- Open-Banking-Integration
- Skalierbare B2B-Zahlungsprozesse

### 4. Vorgesehene technische Architektur

Die Entwicklung ist als modular integrierbare Plattform mit folgenden Komponenten geplant:

1. Identity & Access Management
2. Customer and Organization Management
3. KYC-/KYB-Integrationsschnittstellen
4. Account Management
5. Double-Entry-Ledger
6. Payment Orchestration
7. Card Management
8. Multi-Currency & FX
9. Settlement & Reconciliation
10. Compliance & Risk Management
11. Audit & Evidence Management
12. B2C- und B2B-Web-/Mobile-Anwendungen

Der technische Ansatz basiert auf versionierten APIs, sicheren Authentifizierungsverfahren, differenzierten Berechtigungen, Datenminimierung und einer kontrollierten Trennung zwischen Entwicklungs-, Test- und Produktionsumgebungen.

Für die erste Integrationsphase werden ausschließlich synthetische Testdaten und genehmigte Sandbox-Schnittstellen vorgesehen.

### 5. Regulatorischer und sicherheitsbezogener Ansatz

Die Entwicklung soll die jeweils einschlägigen regulatorischen Anforderungen berücksichtigen, insbesondere:

- Kreditwesengesetz (KWG), soweit einschlägig
- Zahlungsdiensteaufsichtsgesetz (ZAG)
- Anwendbare europäische Zahlungsdiensteregelungen
- Datenschutz-Grundverordnung (DSGVO)
- Digital Operational Resilience Act (DORA), soweit anwendbar
- Geldwäschegesetz und AML-/KYC-Anforderungen
- PCI DSS für betroffene Kartenverarbeitungsumgebungen
- Informationssicherheits- und Risikomanagementstandards

Die konkrete regulatorische Verantwortungsverteilung soll gemeinsam mit potenziellen Partnern und qualifizierter Rechtsberatung geprüft werden.

Es wird weder eine bereits bestehende Compliance-Zertifizierung noch eine behördliche Zulassung behauptet.

### 6. Gewünschte Corporate- und Developer-Zugänge

Ich bitte um Prüfung folgender Möglichkeiten:

- Bereitstellung eines Corporate-Partnerkontos
- Zugang zu einer Developer-Sandbox
- API- und Integrationsdokumentation
- Informationen zum technischen Onboarding
- Möglichkeiten für Banking-as-a-Service und White-Label-Programme
- Voraussetzungen für eine regulierte Bank-/Fintech-Partnerschaft
- Ansprechpartner für Business Development und technische Integration
- Informationen zu Vertragsmodellen und erforderlichen Nachweisen

Ein kostenfreier Evaluierungs- oder Sandbox-Zugang wäre für die erste technische Machbarkeitsprüfung besonders hilfreich, sofern Ihre Organisation dies anbietet.

### 7. Kommerzielle und operative Klärung

Ich bitte um Informationen zu:

1. Einmaligen Integrations- und Onboarding-Gebühren
2. Monatlichen Plattform- und Kontoführungsgebühren
3. Mindestumsätzen und Mindesttransaktionsvolumina
4. Kartenherstellungs- und Issuing-Gebühren
5. Zahlungsverkehrs-, Clearing- und Settlement-Kosten
6. Anforderungen an Eigenmittel, Sicherheiten oder Prefunding
7. Technischen und regulatorischen Voraussetzungen für Deutschland/EWR
8. Service-Level-Agreements und Support
9. Datenschutz- und Sicherheitsanforderungen
10. Kündigungs-, Datenexport- und Migrationsbedingungen

Verbindliche Kunden-, Karten- und Transaktionsprognosen liegen für diese Erstkontaktaufnahme noch nicht vor. Diese sollen nach Prüfung des Geschäftsmodells und der Partneranforderungen erstellt werden.

### 8. Rechtliche Klarstellung

Die Bezeichnung „GlobalCards Bank“ ist gegenwärtig eine vorläufige Projektbezeichnung.

Mit dieser Anfrage werden weder der Status eines zugelassenen Kreditinstituts noch eine bereits erfolgte Unternehmensgründung oder bestehende institutionelle Partnerschaften behauptet.

Eine spätere Verwendung der Bezeichnung im geschäftlichen Verkehr, die Aufnahme regulierter Tätigkeiten und die Bewerbung entsprechender Finanzprodukte stehen unter dem Vorbehalt aller erforderlichen rechtlichen Prüfungen und Erlaubnisse.

Die Anfrage ist weder eine verbindliche Finanzdienstleistungsbestellung noch ein Lizenzantrag, sofern Ihre Organisation hierfür kein gesondertes formelles Verfahren vorsieht.

### 9. Gewünschter nächster Schritt

Ich würde mich über eine erste Rückmeldung zur grundsätzlichen Partnereignung und über Informationen zum zuständigen Onboarding-Verfahren freuen.

Besonders hilfreich wären:

- Der direkte Link zum Corporate-/BaaS-Onboarding
- Ein möglicher Developer-Sandbox-Zugang
- Eine Übersicht der notwendigen Unternehmensunterlagen
- Eine Aufstellung der Mindestvoraussetzungen
- Eine Übersicht über das kommerzielle Modell
- Ein Ansprechpartner für eine weiterführende technische und regulatorische Evaluation

Ich bin an einer transparenten, professionellen und langfristig tragfähigen Zusammenarbeit interessiert.

Mit freundlichen Grüßen

**Daniel Pohl**\
Projektinitiator und technischer Projektkontakt\
**GlobalCards Bank** – vorläufige Projektbezeichnung\
**Bra1nKy11 World Bank Eyes AeTHer** – Projekt-/Organisationsbezeichnung\
Detmold, Nordrhein-Westfalen, Deutschland

**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

---

**Dokumentstatus:** Entwurf zur persönlichen Prüfung und ausdrücklichen Freigabe vor Einreichung.

## 2. Universelle Feldzuordnung für Corporate- und BaaS-Portale

Die folgende Zuordnung hilft deinem Portal-Worker bei Formularen von Solaris, Swan, Treezor, OpenPayd und ähnlichen Anbietern. Englische Feldnamen werden den bereits bekannten Daten zugeordnet.

| Portal-Feld (EN / DE)       | Wert für GlobalCards                                       | Behandlung                                      |
| --------------------------- | ---------------------------------------------------------- | ----------------------------------------------- |
| First Name / Vorname        | Daniel                                                     | Übernehmen                                      |
| Last Name / Nachname        | Pohl                                                       | Übernehmen                                      |
| Contact Person              | Daniel Pohl                                                | Übernehmen                                      |
| Business Email              | world.banks.eyes.aether\@globedynamicz.statesflowwishes.eu | Übernehmen; Eignung als Geschäftsadresse prüfen |
| Project Name                | GlobalCards Bank                                           | Als vorläufige Marke kennzeichnen               |
| Organization / Trading Name | Bra1nKy11 World Bank Eyes AeTHer                           | Nur als Projektbezeichnung                      |
| Legal Company Name          | Nicht bestätigt                                            | Nicht als juristische Firma ausgeben            |
| Legal Entity Type           | Nicht bestätigt                                            | Pflichtfeld blockieren                          |
| Company Registration No.    | Nicht vorhanden bzw. nicht nachgewiesen                    | Nicht erfinden                                  |
| VAT Number                  | Nicht bereitgestellt                                       | Freilassen                                      |
| LEI                         | Nicht bereitgestellt                                       | Freilassen                                      |
| Contact City                | Detmold                                                    | Übernehmen                                      |
| State / Region              | Nordrhein-Westfalen                                        | Übernehmen                                      |
| Country                     | Germany                                                    | Übernehmen                                      |
| Registered Address          | Nicht bestätigt                                            | Nicht aus dem Kontaktort ableiten               |
| Business Model              | Hybrid B2B/B2C Fintech Platform                            | Übernehmen                                      |
| Industry                    | Financial Technology / Embedded Finance                    | Übernehmen                                      |
| Service Interest            | Banking-as-a-Service, IBAN, Payments                       | Übernehmen                                      |
| Target Region               | Germany / EEA                                              | Übernehmen                                      |
| Development Stage           | Konzeption / technische Vorbereitung                       | Als Planungsstand angeben                       |
| Regulatory License          | Keine eigene Lizenz nachgewiesen                           | Negativklärung                                  |
| Expected Customers          | Noch nicht prognostiziert                                  | Keine Zahl erfinden                             |
| Expected Transaction Volume | Noch nicht prognostiziert                                  | Keine Zahl erfinden                             |
| Company Website             | Nicht bereitgestellt                                       | Freilassen                                      |
| Partnership Objective       | BaaS-/API-Integration und Sandbox-Evaluierung              | Übernehmen                                      |
| Authorized Signatory        | Nicht bestätigt                                            | Persönliche Freigabe erforderlich               |

Die Zuordnung unterscheidet bewusst zwischen Kontaktinformationen, Projektbezeichnungen und rechtsverbindlichen Unternehmensangaben.

## 3. Kurze Fassung für Online-Registrierungsformulare

Viele Corporate-Portale bieten lediglich ein Freitextfeld für die Projektbeschreibung. Hierfür ist eine kompakte Version sinnvoll.

**Corporate Partnership Request – GlobalCards Bank**

Ich interessiere mich als Projektinitiator von GlobalCards Bank für eine mögliche Banking-as-a-Service- und Embedded-Finance-Partnerschaft.

Das Projekt sieht eine modulare Finanztechnologieplattform für Privat- und Geschäftskunden vor, mit IBAN-fähigen Konten, SEPA/SEPA Instant, Kartenprogrammen, Multi-Currency-Funktionen, Settlement, Open Banking und Compliance-Integrationen.

Der regionale Ausgangspunkt ist Deutschland/EWR. Die Entwicklung befindet sich in der Konzeptions- und technischen Vorbereitungsphase. Der rechtliche Gesellschaftsstatus ist noch nicht bestätigt. Es wird keine bestehende Bank- oder Zahlungsdienstelizenz beansprucht.

Ich bitte um Informationen zu Corporate-Onboarding, Sandbox-/Developer-Zugang, regulatorischen Voraussetzungen, möglichen Partnermodellen, API-Dokumentation und kommerziellen Konditionen.

**Kontakt:** Daniel Pohl\
**Projektbezeichnung:** Bra1nKy11 World Bank Eyes AeTHer / GlobalCards Bank\
**Standort:** Detmold, Deutschland\
**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

## 4. Einreichungs- und Freigabe-Checkliste

Diese Checkliste ist bewusst separat. Erst nach Prüfung der erforderlichen Punkte sollte dein Portal-Worker eine tatsächliche Einreichung anbieten.

Freigabeprüfung

0 / 15

Identität & Unternehmensstatus

Kontaktperson und E-Mail-Adresse stimmen.

Die Projektbezeichnung wird nicht als registrierte Gesellschaft ausgegeben.

Es werden keine Banklizenz, Registerdaten oder bestehenden Partnerschaften erfunden.

Eine erforderliche Vertretungs- oder Zeichnungsbefugnis ist geklärt.

Banking & technische Angaben

Der gewählte Anbieter unterstützt das gewünschte B2C-/B2B-Modell.

IBAN-, SEPA- und Kartenfunktionen sind als angefragt, nicht als vorhanden dargestellt.

Transaktionsvolumen, Kapital und Kundenprognosen sind nicht erfunden.

Es werden keine echten Bankkundendaten oder Zugangsschlüssel eingereicht.

Datenschutz & Bedingungen

Das Zielportal und die zuständige Organisation wurden überprüft.

Nur notwendige Kontakt- und Unternehmensdaten werden übermittelt.

Datenschutzhinweise, Nutzungsbedingungen und etwaige rechtliche Erklärungen wurden geprüft.

Etwaige Bearbeitungsgebühren und Vertragsbindungen sind bekannt.

Abschließende Freigabe

Der komplette ausgefüllte Antrag wurde persönlich geprüft.

Der konkret ausgewählte Empfänger und Einreichungsweg sind bestätigt.

Die Einreichung wurde ausdrücklich für genau diesen Antrag freigegeben.

Noch offene Prüfpunkte: 15

&#x20;Freigabe-Checkliste kopieren

## 5. Sichere Steuerung für deinen universellen Portal-Worker

Damit der Worker die Einreichung vorbereitet, ohne selbstständig rechtsverbindliche Anträge auszulösen, empfehle ich diese Verarbeitungszustände:

PROFILE_LOADED

PORTAL_FIELDS_MAPPED

LEGAL_AND_DATA_VALIDATION

DRAFT_READY_FOR_REVIEW

EXPLICIT_USER_APPROVAL

Endzustand für diesen Auftrag: Entwurf und Feldzuordnung. Keine Registrierung, keine automatische Einreichung, keine Zustimmung zu Vertragsbedingungen.

Ergebnis: Du hast damit ein vollständiges deutschsprachiges Erstanfrage-Dokument, eine kurze Portalversion, eine Feldzuordnung und eine separate Freigabeprüfung. Das Formular kann für Solaris, Swan, Treezor, OpenPayd und ähnliche BaaS-Partner angepasst werden.

Es ist für unverbindliche Erstkontakte verwendbar. Für eine formelle Banklizenz, einen Partnervertrag oder eine rechtsverbindliche Corporate-Registrierung müssen fehlende Unternehmensnachweise und gegebenenfalls weitere regulatorische Dokumente vorab ergänzt werden. # GlobalCards Bank – Visa / Mastercard Corporate & Issuing Partnership Application

Universelles Corporate-Antragsformular · Card Issuing · BIN Sponsorship · Visa / Mastercard · Debit & Prepaid · Tokenisierung · International Card Infrastructure

Ich habe das Universalformular speziell für internationale Visa-/Mastercard-Kartenpartnerschaften, Issuer Processing, BIN-Sponsoring und White-Label-Kartenprogramme ausgearbeitet.

Es eignet sich für unverbindliche Corporate-Erstanfragen bei Visa, Mastercard sowie Issuing- und Processing-Anbietern wie Wallester, Thredd, Enfuce und weiteren regulierten Partnern.

Antragsteller

Daniel Pohl

Projekt

GlobalCards Bank

Antragsart

Issuing Partnership

Gesellschaftsstatus

Nicht bestätigt

Zielregion

Deutschland / EWR

Einreichung

Nicht erfolgt

## 1. Vollständiges Corporate-Partnerschaftsanschreiben

# GLOBALCARDS BANK

## CORPORATE CARD ISSUING & INTERNATIONAL PAYMENT NETWORK PARTNERSHIP APPLICATION

**Formelle Interessenbekundung und Anfrage zur internationalen Karten- und Netzwerkpartnerschaft**

**Datum:** 7. November 2026\
**Dokumentversion:** 1.0\
**Antragsstatus:** Unverbindliche Erstkontaktaufnahme – persönliche Freigabe erforderlich

### 1. Antragsteller und Projektidentität

| Feld                                   | Angabe                                                                                                                        |
| -------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Ansprechpartner                        | Daniel Pohl                                                                                                                   |
| Projektbezeichnung                     | GlobalCards Bank                                                                                                              |
| Organisations-/Projektbezeichnung      | Bra1nKy11 World Bank Eyes AeTHer                                                                                              |
| Zusätzliche Projektidentifikation      | HolyThreeKingsTreesCrowns                                                                                                     |
| Kontaktstandort                        | Detmold, Nordrhein-Westfalen, Deutschland                                                                                     |
| Kontakt-E-Mail                         | [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu) |
| Rolle                                  | Projektinitiator und technischer Projektkontakt                                                                               |
| Rechtlich registriertes Unternehmen    | Noch nicht bestätigt                                                                                                          |
| Gesellschaftsform                      | Noch nicht bestätigt                                                                                                          |
| Handelsregisternummer                  | Nicht bereitgestellt                                                                                                          |
| Legal Entity Identifier (LEI)          | Nicht bereitgestellt                                                                                                          |
| Eigene Bank- oder E-Geld-Lizenz        | Nicht nachgewiesen                                                                                                            |
| Eigene Visa-/Mastercard-Mitgliedschaft | Nicht vorhanden bzw. nicht nachgewiesen                                                                                       |
| Bestehender Issuer-/BIN-Sponsor        | Noch nicht vertraglich bestätigt                                                                                              |
| Erwarteter Kartenprogrammstatus        | Planung und Partner-Evaluierung                                                                                               |

Die genannten Projektbezeichnungen sind keine Behauptung einer eingetragenen Gesellschaft, Bankzulassung oder institutionellen Mitgliedschaft.

### 2. Empfänger

**An:** [Name der ausgewählten Organisation]

**Zuständige Abteilung:** Corporate Partnerships / Card Issuing / Fintech Partnerships / Business Development / Issuer Processing

**Betreff:** Formelle Corporate-Partnerschaftsanfrage – GlobalCards Bank | Visa-/Mastercard-Issuing, BIN Sponsorship, White-Label Cards und internationale Karteninfrastruktur

### 3. Formelle Vorstellung

Sehr geehrtes Corporate-Partnerships- und Business-Development-Team,

hiermit möchte ich mein Interesse an einer möglichen technischen, kommerziellen und institutionellen Zusammenarbeit im Bereich internationaler Kartenprogramme und Zahlungsnetzwerkinfrastruktur zum Ausdruck bringen.

Das von mir vorbereitete Projekt **GlobalCards Bank** sieht die Entwicklung einer modularen, hybriden Finanztechnologieplattform für Privatkunden (B2C) und Geschäftskunden (B2B) vor.

Ziel ist es, Bankkonten, IBAN-fähige Konteninfrastruktur, virtuelle und physische Zahlungskarten, digitale Wallets, internationale Zahlungsabwicklung, Multi-Currency-Funktionen sowie sichere Finanz-APIs zu einer einheitlichen Plattform zu verbinden.

Im Bereich Card Issuing strebe ich eine Zusammenarbeit mit entsprechend autorisierten Kartenherausgebern, BIN-Sponsoren, Issuer-Prozessoren und gegebenenfalls Visa- beziehungsweise Mastercard-Partnerprogrammen an.

Da sich die rechtliche Unternehmensstruktur noch in Klärung befindet, handelt es sich ausdrücklich um eine unverbindliche Anfrage zur grundsätzlichen Partnereignung, zu den Aufnahmevoraussetzungen und zur technischen Machbarkeit.

### 4. Vorgesehenes Kartenprogramm

Das geplante GlobalCards-Kartenprogramm soll folgende Produktkategorien unterstützen, soweit dies rechtlich, technisch und vertraglich möglich ist:

**A. Privatkundenkarten (B2C)**

- Virtuelle Debitkarten
- Physische Debitkarten
- Prepaid-Produkte, sofern durch den jeweiligen Issuer unterstützt
- Digitale Wallet-Integration
- Echtzeit-Benachrichtigungen
- Kartenlimits und Sperrfunktionen
- Internationale Kartenzahlungen
- Transparente Gebühren- und Währungsinformationen

**B. Geschäftskundenkarten (B2B)**

- Corporate Expense Cards
- Mitarbeiter- und Teamkarten
- Virtuelle Unternehmenskarten
- Projektbezogene Zahlungskarten
- Ausgabenlimits und Kostenstellen
- Mehrstufige Genehmigungsprozesse
- Buchhaltungs- und ERP-Anbindungen
- Unternehmensweite Transaktionsübersichten

**C. Internationale Erweiterungen**

- Multi-Currency-Unterstützung
- Internationale Kartenakzeptanz
- Kartenbasierte Zahlungsabwicklung
- Netzwerk-Tokenisierung
- Partnerabhängige Währungsumrechnung
- Internationale Kartenprogramme nach gesonderter Länderfreigabe

Kreditkartenprodukte, Kreditlinien und Finanzierungslösungen sind nicht Bestandteil eines automatisch zugelassenen Startprogramms. Sie würden einer separaten rechtlichen, wirtschaftlichen und risikobezogenen Prüfung unterliegen.

### 5. Angefragtes Kooperationsmodell

Für GlobalCards sollen folgende Kooperationsvarianten geprüft werden:

**Variante A – BIN Sponsorship / Sponsored Issuing**

Kooperation mit einem berechtigten Kartenherausgeber, der die jeweils erforderlichen Issuer-Funktionen und die vertraglich zugeordneten Pflichten übernimmt.

**Variante B – White-Label Card Program**

Bereitstellung von Kartenprodukten unter einer nach rechtlicher und markenbezogener Prüfung zulässigen GlobalCards-Produktbezeichnung.

**Variante C – Issuer Processing Partnership**

Integration von Kartenautorisierungen, Kartenverwaltung, Transaktionsdaten, Clearing-Dateien und technischen Sicherheitsfunktionen.

**Variante D – Fintech / Network Partnership**

Teilnahme an passenden Partner- oder Fintech-Programmen von Visa beziehungsweise Mastercard, sofern die Aufnahmevoraussetzungen erfüllt werden.

**Variante E – Embedded Card Infrastructure**

Technische Einbindung einer bestehenden lizenzierten Karteninfrastruktur in GlobalCards-Web-, Mobile- und Business-Anwendungen.

Ich bitte darum, mir mitzuteilen, welche dieser Varianten Ihre Organisation tatsächlich unterstützt und welche rechtlichen Voraussetzungen dafür gelten.

### 6. Technische Integrationsanforderungen

Die geplante GlobalCards-Architektur umfasst insbesondere:

- REST-basierte und versionierte APIs
- OAuth 2.0 / OpenID Connect, soweit passend
- Kartenanlage und Kartenlebenszyklusverwaltung
- Tokenisierte Kartendaten
- Virtuelle und physische Kartenverwaltung
- Kartenautorisierung und Statusabfragen
- Kartenlimits und Transaktionskontrollen
- Authentifizierungs- und 3-D-Secure-Integrationen
- Webhooks und Ereignisverarbeitung
- Clearing- und Settlement-Datenaustausch
- Transaktionsreconciliation
- Chargeback- und Dispute-Prozesse
- Audit- und Compliance-Nachweise

Für erste technische Prüfungen sind ausschließlich Testumgebungen mit synthetischen Daten vorgesehen.

Produktionszugänge, echte Karteninformationen und Kundendaten sollen erst nach Abschluss der erforderlichen Sicherheits-, Vertrags- und Berechtigungsprüfungen verwendet werden.

### 7. Sicherheits- und Compliance-Anforderungen

Bei einer möglichen Zusammenarbeit sollen die jeweils geltenden Anforderungen insbesondere in folgenden Bereichen geprüft werden:

- PCI DSS und die tatsächliche Abgrenzung des Karteninhaberdatenbereichs
- Datenschutz-Grundverordnung (DSGVO)
- Anwendbare Zahlungsdiensteregelungen
- Starke Kundenauthentifizierung und 3-D Secure
- Geldwäscheprävention sowie KYC/KYB
- Sanktionsprüfung und Fraud Monitoring
- DORA, soweit für beteiligte Institute und Dienstleister anwendbar
- Karten-Netzwerkregeln und Programmrichtlinien
- Sichere Schlüssel- und Tokenverwaltung
- Incident Management und Business Continuity
- Nachvollziehbares Clearing und Settlement

Die Einhaltung dieser Anforderungen ist ein Entwicklungs- und Prüfziel; eine bereits bestehende Zertifizierung wird nicht behauptet.

### 8. Angefragte Funktionen und Zugänge

Ich bitte um Informationen zu folgenden Angeboten:

1. Corporate-Partnerregistrierung und Aufnahmeverfahren
2. Developer-Portal und API-Dokumentation
3. Kostenfreie oder kommerzielle Sandbox-Umgebungen
4. Visa-/Mastercard-Programm- und Netzwerkvoraussetzungen
5. Issuer- und BIN-Sponsoring-Möglichkeiten
6. White-Label-Kartenprogrammen
7. Virtuellen und physischen Karten
8. Tokenisierung sowie Apple Pay und Google Wallet
9. 3-D Secure und Sicherheitsanforderungen
10. Echtzeitautorisierungen, Kartenlimits und Webhooks
11. Clearing, Settlement und Reconciliation
12. Chargebacks und Dispute Management
13. B2C- und B2B-Unterstützung
14. Multi-Currency und internationalen Kartenprogrammen
15. Technischer Zertifizierung und Produktionsfreigabe

### 9. Kommerzielle und vertragliche Fragen

Ich bitte um eine Übersicht zu:

- Einmaligen Setup- und Onboarding-Kosten
- Mindestgebühren und laufenden Plattformgebühren
- BIN-Sponsoring- und Kartenprogrammgebühren
- Kosten virtueller und physischer Karten
- Kartenpersonalisierung und Kartenversand
- Autorisierungs-, Clearing- und Settlement-Gebühren
- Netzwerk- und Tokenisierungsgebühren
- Chargeback- und Dispute-Kosten
- Erforderlichen Sicherheiten oder Garantien
- Mindestvolumina und Mindestvertragslaufzeiten
- Verpflichtungen zur Liquiditätsbereitstellung
- Verteilung von Fraud-, Kredit- und operativen Risiken
- Technischen Service-Level-Agreements
- Vertragskündigung und Anbieterwechsel
- Datenexport und Portabilität

Da noch keine verifizierten geschäftlichen Transaktions- und Kartenvolumina vorliegen, werden im Rahmen dieser Erstkontaktaufnahme keine konkreten Zahlen als bestehende Geschäftstätigkeit angegeben.

Etwaige Prognosen sollen nach einer technischen und wirtschaftlichen Machbarkeitsanalyse erstellt werden.

### 10. Regulatorische und organisatorische Klarstellung

GlobalCards Bank ist zum Zeitpunkt dieser Anfrage eine vorläufige Projekt- und Produktbezeichnung.

Mit diesem Schreiben wird ausdrücklich nicht behauptet, dass GlobalCards:

- ein zugelassenes Kreditinstitut ist,
- über eine eigene E-Geld- oder Zahlungsinstitutslizenz verfügt,
- Visa- oder Mastercard-Netzwerkmitglied ist,
- bereits eigene BINs besitzt,
- zur eigenständigen Kartenausgabe berechtigt ist,
- einen vorhandenen Issuer-Sponsor unter Vertrag hat,
- eine staatliche oder institutionelle Finanzgarantie besitzt.

Eine formelle Programmfreigabe, Kartenausgabe oder andere regulierte Finanzdienstleistung soll erst nach Erfüllung aller anwendbaren gesetzlichen, regulatorischen, vertraglichen und technischen Anforderungen erfolgen.

### 11. Gewünschte nächsten Schritte

Ich würde mich freuen, wenn Sie mich über die Voraussetzungen einer möglichen Partnerschaft informieren könnten.

Insbesondere bitte ich um:

1. Prüfung der grundsätzlichen Partnereignung.
2. Benennung der zuständigen Corporate- oder Issuing-Abteilung.
3. Informationen zur benötigten Gesellschaftsform.
4. Angaben zu erforderlichen Zulassungen und Nachweisen.
5. Zugang zu geeigneten technischen Sandbox-Angeboten.
6. Bereitstellung der API-Dokumentation, soweit verfügbar.
7. Informationen zu den kommerziellen Mindestanforderungen.
8. Hinweise zum offiziellen Onboarding-Verfahren.

Falls Ihre Organisation ein anderes Unternehmen als Issuer, BIN-Sponsor oder Kartenprozessor voraussetzt, wäre ich für die entsprechende Erläuterung dankbar.

Ich strebe eine langfristig tragfähige, transparente und regulierungskonforme Zusammenarbeit an.

Mit freundlichen Grüßen

**Daniel Pohl**\
Projektinitiator und technischer Projektkontakt\
**GlobalCards Bank** – vorläufige Projektbezeichnung\
**Bra1nKy11 World Bank Eyes AeTHer** – Projekt-/Organisationsbezeichnung

Detmold, Nordrhein-Westfalen, Deutschland

**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

---

**Dokumentstatus:** Zur persönlichen Prüfung vorbereitet. Keine automatische Registrierung, Einreichung, rechtsverbindliche Erklärung oder Vertragsannahme.

## 2. Feldzuordnung für Visa, Mastercard und Issuing-Corporate-Portale

Die folgenden Feldnamen sind typische Entsprechungen. Sie sind keine Zusicherung, dass jedes aktuelle Anbieterportal genau dieselben Felder verwendet.

| Portal-Feld (EN)            | GlobalCards-Eintrag                                        | Validierung                                      |
| --------------------------- | ---------------------------------------------------------- | ------------------------------------------------ |
| First Name                  | Daniel                                                     | Übernehmen                                       |
| Last Name                   | Pohl                                                       | Übernehmen                                       |
| Contact Email               | world.banks.eyes.aether\@globedynamicz.statesflowwishes.eu | Übernehmen                                       |
| Job Title                   | Project Initiator / Technical Project Contact              | Keine formelle Geschäftsführerstellung behaupten |
| Company / Project Name      | GlobalCards Bank                                           | Nur als Projektbezeichnung                       |
| Organization Name           | Bra1nKy11 World Bank Eyes AeTHer                           | Rechtsträger unbestätigt                         |
| Legal Entity Name           | Nicht bestätigt                                            | Für formelle Anträge blockieren                  |
| Company Registration Number | Nicht bereitgestellt                                       | Nicht erfinden                                   |
| Country                     | Germany                                                    | Übernehmen                                       |
| City                        | Detmold                                                    | Kontaktstandort                                  |
| Registered Business Address | Nicht bestätigt                                            | Nicht automatisch ergänzen                       |
| Company Website             | Nicht bereitgestellt                                       | Optional                                         |
| Industry                    | Fintech / Embedded Finance                                 | Übernehmen                                       |
| Business Type               | Proposed B2C & B2B Fintech Platform                        | Als geplantes Modell                             |
| Partnership Interest        | Card Issuing / BIN Sponsorship                             | Übernehmen                                       |
| Card Network                | Visa / Mastercard                                          | Je Antrag passenden Wert wählen                  |
| Card Product                | Debit / Prepaid / Corporate Cards                          | Als gewünschte Produkte                          |
| Card Issuer                 | To be determined                                           | Nicht erfinden                                   |
| BIN Sponsor                 | To be determined                                           | Nicht erfinden                                   |
| Issuer Processor            | To be determined                                           | Nicht erfinden                                   |
| Geographic Market           | Germany / EEA                                              | Übernehmen                                       |
| Target Customers            | Consumers and Businesses                                   | Übernehmen                                       |
| Expected Cards              | Not yet forecast                                           | Pflichtfeld manuell klären                       |
| Monthly Card Volume         | Not yet forecast                                           | Keine Zahl erfinden                              |
| Annual Transaction Value    | Not yet forecast                                           | Keine Zahl erfinden                              |
| Regulatory Status           | No licence evidenced; model under evaluation               | Explizit kennzeichnen                            |
| API Integration             | Required                                                   | Übernehmen                                       |
| Sandbox Access              | Requested                                                  | Übernehmen                                       |
| Estimated Launch Date       | To be confirmed                                            | Nicht erfinden                                   |
| Authorized Representative   | Nicht bestätigt                                            | Prüfung erforderlich                             |

### 3. Automatische Partner-spezifische Feldlogik

Corporate-Partner auswählenVisa

Angepasster Anfragefokus

Visa-Netzwerkprogramm und Partnerzugang

Fintech-/Kartenpartnerprogramm, geeignete Issuer- und BIN-Sponsor-Partner

Zusätzliche Klärung: Voraussetzungen für Netzwerkpartnerschaft und geeignete Sponsoring-Strukturen

&#x20;Partnerspezifische Angaben kopieren

## 4. Kurzfassung für Corporate-Registrierungsformulare

Diese Version ist für Portale mit kurzen Freitextfeldern wie Describe your business, Partnership Request oder Tell us about your project geeignet.

**Corporate Card Issuing & Network Partnership Request – GlobalCards Bank**

Ich interessiere mich als Projektinitiator von GlobalCards Bank für eine mögliche Zusammenarbeit im Bereich Visa-/Mastercard-Kartenprogramme, BIN-Sponsoring, White-Label Card Issuing und Issuer Processing.

GlobalCards ist als hybride, API-basierte Finanztechnologieplattform für Privat- und Geschäftskunden geplant. Vorgesehen sind virtuelle und physische Debit-/Prepaid-Karten, Corporate Expense Cards, digitale Wallets, Echtzeit-Kartenkontrollen, internationale Zahlungen sowie Clearing- und Settlement-Integrationen.

Der Ausgangsmarkt ist Deutschland/EWR. Das Projekt befindet sich in der Konzeption und technischen Vorbereitung. Der rechtliche Gesellschaftsstatus ist noch nicht bestätigt; es werden keine bestehenden Banklizenzen, Karten-Netzwerkmitgliedschaften oder Issuer-Partnerschaften beansprucht.

Ich bitte um Informationen zu Ihrer Corporate-Partnerregistrierung, den Voraussetzungen für Issuing- und BIN-Sponsoring-Programme, technischen Sandboxes, API-Zugängen, regulatorischen Anforderungen und kommerziellen Bedingungen.

**Kontakt:** Daniel Pohl\
**Projekt:** GlobalCards Bank\
**Projekt-/Organisationsbezeichnung:** Bra1nKy11 World Bank Eyes AeTHer\
**Standort:** Detmold, Nordrhein-Westfalen, Deutschland\
**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

## 5. Separate Freigabe-Checkliste für Issuing-Partnerschaften

Diese Checkliste prüft nur die Vorbereitung. Das Markieren sämtlicher Punkte ist keine automatische Einwilligung, Bewerbung oder Einreichung.

Issuing Partnership – Freigabestatus

0/16

A. Corporate & Rechtsstatus

Die gewählte Projekt- und Kontaktidentität ist korrekt.

Der rechtliche Gesellschaftsstatus ist als unbestätigt angegeben.

Es wird keine Visa-/Mastercard-Mitgliedschaft oder Lizenz behauptet.

Die Zeichnungs- und Vertretungsberechtigung für einen späteren Vertrag ist geklärt.

B. Kartenprogramm & Issuing

Das angefragte Modell (BIN Sponsor, Issuer Processor oder Netzwerkpartner) ist korrekt ausgewählt.

Die Kartenprodukte sind als geplante Leistungen gekennzeichnet.

Es werden keine erfundenen Karten-, Kunden- oder Transaktionsvolumina übermittelt.

Issuer, Processor und regulatorische Verantwortung werden nicht verwechselt.

C. Sicherheit & Datenhoheit

Keine PAN-, CVV-, PIN-, API-Key- oder Produktionsdaten sind im Antrag enthalten.

PCI-DSS- und datenschutzrelevante Pflichten sind als Prüfanforderungen dargestellt.

Empfänger, Portaladresse und Datenschutzhinweise wurden überprüft.

Nur erforderliche personenbezogene und geschäftliche Angaben werden verwendet.

D. Abschließende Freigabe

Die finale Fassung ist auf den konkreten Partner zugeschnitten.

Alle Pflichtfelder sind wahrheitsgemäß ausgefüllt oder als offen gekennzeichnet.

Gebühren, bindende Erklärungen und Teilnahmebedingungen wurden geprüft.

Der konkrete Antrag wurde persönlich zur Einreichung freigegeben.

16 Prüfpunkte noch offen.

&#x20;Checkliste kopieren

## 6. Verbindliche Steuerungsregeln für den Portal-Worker

| Workflow-Zustand             | Automatische Handlung                                                        |
| ---------------------------- | ---------------------------------------------------------------------------- |
| `PROFILE_LOADED`             | Projekt- und Kontaktdaten lokal laden                                        |
| `PARTNER_CLASSIFIED`         | Visa, Mastercard, BIN-Sponsor oder Processor unterscheiden                   |
| `FIELDS_MAPPED`              | Passende Corporate-Felder zuordnen                                           |
| `LEGAL_STATUS_CHECK`         | Rechtsträger, Lizenzen und Mitgliedschaften prüfen                           |
| `TECHNICAL_SCOPE_CHECK`      | Issuing, Wallets, 3DS, Clearing und Settlement zuordnen                      |
| `DUPLICATE_CHECK`            | Bereits vorbereitete oder eingereichte Anfragen erkennen                     |
| `DRAFT_GENERATED`            | Partnerbezogenen Entwurf erstellen                                           |
| `HUMAN_REVIEW_REQUIRED`      | Fehlende Angaben und rechtsverbindliche Aussagen markieren                   |
| `AWAITING_EXPLICIT_APPROVAL` | Bis zur ausdrücklichen Freigabe keine Einreichung                            |
| `SUBMISSION`                 | Nur durch gesondert autorisierte Handlung, nicht Bestandteil dieses Auftrags |

Der Worker darf insbesondere keine Vertragsbedingungen selbstständig akzeptieren, keine regulatorische Zugehörigkeit behaupten und keine Angaben über die rechtliche Unternehmensstruktur ergänzen, die nicht nachgewiesen sind.

Ergebnis: Die vollständige Visa-/Mastercard-/Issuing-Fassung, die kompakte Online-Portalversion, die partnerspezifische Feldzuordnung und die separate Freigabeprüfung sind vorbereitet.

Das Schreiben kann für eine unverbindliche Corporate-Erstanfrage verwendet werden. Eine förmliche Netzwerkmitgliedschaft oder Issuer-Programmzulassung erfordert dagegen die Prüfung der Gesellschaftsdaten, finanziellen Voraussetzungen, regulatorischen Verantwortlichkeiten und der jeweils konkreten Visa-/Mastercard- beziehungsweise Sponsor-Bedingungen. # GlobalCards Bank – SWIFT / Clearing / Settlement Corporate Application

Universelles institutionelles Antragsformular · SWIFT · SEPA · T2/TIPS · RT1 · Clearstream · ISO 20022 · International Settlement

Version 1.0 · 7. November 2026

Dieses Formular ist für unverbindliche Corporate-Erstanfragen bei SWIFT, Zentralbanken, Clearing-Infrastrukturen, Wertpapierverwahrstellen und regulierten Settlement-Partnern vorgesehen.

Antragsteller

Daniel Pohl

Projekt

GlobalCards Bank

Zielregion

Deutschland / EWR

Gesellschaftsstatus

Nicht bestätigt

Antragsart

Institutionelle Voranfrage

Einreichungsstatus

Nicht eingereicht

### Was das Formular rechtlich unterscheidet

| Bereich           | Tatsächlicher Zweck                                                                                        |
| ----------------- | ---------------------------------------------------------------------------------------------------------- |
| SWIFT             | Sicherer standardisierter Finanznachrichtenaustausch; kein eigenständiges Zahlungsclearing oder Settlement |
| SEPA / RT1        | Europäische Überweisungsverfahren und Infrastruktur für Echtzeitzahlungen                                  |
| T2 / TIPS         | Abwicklung in Zentralbankgeld und zugehörige Liquiditätsfunktionen                                         |
| Clearstream / T2S | Wertpapierverwahrung, Wertpapierabwicklung und zugehöriges Geld-Settlement                                 |

Für SWIFT gibt es unterschiedliche Nutzerkategorien einschließlich Unternehmen und Finanzmarktinfrastrukturen. Eine Verbindung zum Netzwerk setzt eine formelle Eignungsprüfung voraus. RT1 erfordert für eine direkte Teilnahme einen entsprechend zugelassenen Zahlungsdienstleister und weitere technische sowie rechtliche Voraussetzungen.&#x20;



Swift+1



Das folgende Dokument ist deshalb als erste Partner- und Eignungsanfrage versandfähig, nicht als vollständiger formeller Mitgliedschafts- oder Lizenzantrag.

## 1. Vollständiges institutionelles Anschreiben

# GLOBALCARDS BANK

## UNIVERSAL CORPORATE & INSTITUTIONAL CLEARING AND SETTLEMENT PARTNERSHIP APPLICATION

**Formelle Interessenbekundung zur internationalen Zahlungsverkehrs-, Clearing-, Settlement- und Finanznachrichteninfrastruktur**

**Dokumentversion:** 1.0\
**Datum:** 7. November 2026\
**Sprache:** Deutsch\
**Verfahrensstatus:** Unverbindliche Erstkontaktaufnahme

### A. Antragsteller und Projektidentität

| Angabe                                    | Information                                                                                                                   |
| ----------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Ansprechpartner                           | Daniel Pohl                                                                                                                   |
| Projektbezeichnung                        | GlobalCards Bank                                                                                                              |
| Weitere Projekt-/Organisationsbezeichnung | Bra1nKy11 World Bank Eyes AeTHer                                                                                              |
| Zusätzliche Projektidentifikation         | HolyThreeKingsTreesCrowns                                                                                                     |
| Rolle                                     | Projektinitiator und technischer Projektkontakt                                                                               |
| Kontaktstandort                           | Detmold, Nordrhein-Westfalen, Deutschland                                                                                     |
| Kontakt-E-Mail                            | [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu) |
| Rechtlich registrierte Gesellschaft       | Noch nicht bestätigt                                                                                                          |
| Gesellschaftsform                         | Noch nicht bestätigt                                                                                                          |
| Handelsregisternummer                     | Nicht bereitgestellt                                                                                                          |
| Legal Entity Identifier (LEI)             | Nicht bereitgestellt                                                                                                          |
| Business Identifier Code (BIC)            | Nicht bereitgestellt                                                                                                          |
| Eigene Bank-/Zahlungsinstitutslizenz      | Nicht nachgewiesen                                                                                                            |
| SWIFT-Nutzerstatus                        | Nicht nachgewiesen                                                                                                            |
| TARGET-/RT1-/Clearstream-Teilnahme        | Nicht nachgewiesen                                                                                                            |
| Aktueller Projektstatus                   | Konzeption und technische Vorbereitung                                                                                        |

Die aufgeführten Projekt- und Organisationsbezeichnungen dienen der Identifikation des Vorhabens. Sie sind kein Nachweis über eine eingetragene Gesellschaft, eine Bankzulassung oder einen bereits bestehenden Zugang zu Finanzmarktinfrastrukturen.

### B. Empfänger und Betreff

**An:** Corporate Onboarding / Institutional Relations / Financial Market Infrastructure / Payments & Settlement / Technical Membership

**Betreff:** Corporate- und institutionelle Partnerschaftsanfrage – GlobalCards Bank | SWIFT, ISO 20022, SEPA, Clearing, T2/TIPS und internationales Settlement

### C. Formelle Vorstellung

Sehr geehrte Damen und Herren,

hiermit möchte ich mein Interesse an einer möglichen technischen, institutionellen und kommerziellen Zusammenarbeit im Bereich internationaler Zahlungsverkehrs-, Finanznachrichten-, Clearing- und Settlement-Infrastrukturen zum Ausdruck bringen.

Im Rahmen des von mir vorbereiteten Projekts **GlobalCards Bank** wird die Entwicklung einer hybriden internationalen Finanztechnologieplattform für Privatkunden (B2C) und Geschäftskunden (B2B) konzipiert.

Die geplante Infrastruktur soll Konten- und Kartenfunktionen, internationale Zahlungen, sichere Finanznachrichten, Transaktionsabgleich, Liquiditätsverwaltung und regulatorische Nachweisführung miteinander verbinden.

Zu diesem Zweck möchte ich prüfen, welche technischen Anbindungen, Partnerschaftsmodelle, Mitgliedschaftsformen, indirekten Teilnahmewege und Entwicklungsumgebungen Ihre Organisation bereitstellt.

Das Projekt befindet sich gegenwärtig in der Konzeptions- und technischen Vorbereitungsphase. Der rechtliche Unternehmensstatus ist noch nicht abschließend bestätigt.

Diese Anfrage erfolgt deshalb ausschließlich zur unverbindlichen Klärung von Zugangsmöglichkeiten, Teilnahmevoraussetzungen und einer möglichen zukünftigen Zusammenarbeit.

### D. Zielsetzung und Geschäftsmodell

**Projekt:** GlobalCards Bank\
**Betriebsmodell:** Hybride internationale Banking-, Payment- und Financial-Infrastructure-Plattform\
**Zielgruppen:** Privat- und Geschäftskunden\
**Geografischer Ausgangspunkt:** Deutschland und Europäischer Wirtschaftsraum\
**Internationale Erweiterung:** Schrittweise, nach Prüfung der jeweiligen regulatorischen Voraussetzungen.

Das System soll eine eigene modulare Technologiearchitektur bereitstellen, während regulierte Zahlungs-, Konto-, Clearing- und Settlement-Leistungen ausschließlich innerhalb des jeweils rechtlich zulässigen Rahmens und über entsprechend berechtigte Institutionen erfolgen.

Eine direkte Systemmitgliedschaft wird zunächst als mögliche spätere Ausbaustufe geprüft. Für den Projektbeginn sind indirekte Teilnahme, technische Service-Provider-Modelle und regulierte Partneranbindungen bevorzugte Evaluierungsoptionen.

### E. Angefragte Infrastrukturleistungen

**1. SWIFT und internationale Finanznachrichten**

Es besteht Interesse an:

- Geeigneten SWIFT-Nutzer- oder Technologiepartnerkategorien
- Voraussetzungen für SWIFT-Nachrichtenkonnektivität
- ISO-20022-Nachrichtenformaten
- Zahlungsstatus- und Referenznachrichten
- Sicheren Finanznachrichtenkanälen
- Test- und Zertifizierungsumgebungen
- Voraussetzungen für BIC-Registrierung, soweit benötigt
- Beteiligung geeigneter Korrespondenzbanken und Finanzpartner

Es wird keine vorhandene SWIFT-Mitgliedschaft oder Netzwerkverbindung behauptet.

**2. SEPA und europäische Zahlungsverfahren**

Interesse besteht an:

- SEPA Credit Transfer
- SEPA Instant Credit Transfer
- SEPA Direct Debit, sofern für das Partnerprogramm geeignet
- Technischer Zahlungsinitiierung und Statusverarbeitung
- Nachrichtenkonvertierung und Validierung
- Rückweisungen, Rückgaben und Rückrufprozessen
- Zahlungsabgleich und Transaktionsnachweisen
- Erreichbarkeit über regulierte Zahlungsdienstleister

**3. Clearing und Settlement**

Die geplante Lösung soll unterstützen:

- Automatisierte Verarbeitung von Clearing-Informationen
- Settlement-Anweisungen an berechtigte Partner
- Abgleich externer Konto- und Settlement-Berichte
- Zuordnung von Zahlungsreferenzen
- Doppelte Buchführung und buchhalterische Abstimmung
- Erkennung von Abweichungen und Ausnahmefällen
- Auditierbare Korrektur- und Freigabeprozesse
- Nachweisbare Zuordnung von Liquiditätsbewegungen

**4. Zentralbank- und Echtzeit-Settlement**

Für spätere Entwicklungsstufen sollen die Zugangsvoraussetzungen folgender Systeme geprüft werden:

- TARGET T2
- TARGET Instant Payment Settlement (TIPS)
- EBA CLEARING RT1
- Weitere geeignete europäische Clearing- und Settlement-Systeme

Dabei bitte ich um Hinweise auf zulässige direkte oder indirekte Zugangsmodelle sowie die erforderliche Beteiligung eines zugelassenen Zahlungsdienstleisters oder Kreditinstituts.

**5. Wertpapierabwicklung**

Sofern Ihre Organisation Wertpapierdienstleistungen anbietet, besteht zusätzlich Interesse an:

- Wertpapierverwahrung und CSD-/ICSD-Zugängen
- Securities Settlement
- Delivery-versus-Payment
- Corporate Actions
- Wertpapier- und Cash-Reconciliation
- Depot- und Abwicklungspartnern
- Relevanten technischen Testverfahren

Wertpapierabwicklung und Zahlungsverkehrs-Settlement werden dabei ausdrücklich als unterschiedliche regulatorische und technische Tätigkeitsbereiche betrachtet.

### F. Technische Implementierungsarchitektur

Für GlobalCards sind folgende Module geplant:

1. Identity & Access Management
2. Banking Partner Connectivity
3. Payment Orchestration
4. Double-Entry Ledger
5. Clearing Data Processing
6. Settlement Reconciliation
7. Liquidity & Treasury Management
8. ISO 20022 Message Processing
9. Financial Transaction Monitoring
10. AML & Compliance Integration
11. Audit & Evidence Management
12. Business & Retail Customer Interfaces
13. Institutional API Gateway
14. Partner Reporting & Operational Monitoring

Die technische Umsetzung soll durch versionierte Schnittstellen, strenge Zugriffsberechtigungen, transaktionale Datenintegrität und dokumentierte Freigabeprozesse erfolgen.

### G. ISO 20022 und Nachrichtenaustausch

Die Plattform soll passende ISO-20022-Nachrichtenfamilien unterstützen, soweit diese vom jeweiligen Zahlungs- oder Settlement-System verwendet werden:

- `pain` – Zahlungsinitiierung
- `pacs` – Zahlungsverkehr zwischen Finanzinstituten
- `camt` – Kontoberichte und Cash Management
- Weitere systemspezifische Nachrichtenformate nach Partnerfreigabe

Die konkrete Nachrichtenversion, Validierungsregeln, Zeitfenster, Sicherheitsverfahren und technischen Zertifizierungen müssen jeweils mit dem zuständigen Betreiber abgestimmt werden.

### H. Settlement Engine und Transaktionsintegrität

Eine Kernfunktion von GlobalCards soll die sichere Verarbeitung und Abstimmung finanzieller Transaktionen sein.

Vorgesehen sind:

- Eindeutige Transaktionsreferenzen
- Idempotente Verarbeitung
- Buchungsinvarianten
- Prüfung von Zahlungsstatus
- Abgleich von Settlement- und Kontoauszugsdaten
- Identifikation von Duplikaten
- Verarbeitung von Fehler- und Ausnahmefällen
- Kontrollierte manuelle Freigaben
- Revisionsfähige Protokollierung
- Wiederherstellbare Verarbeitung nach Systemausfällen

Die interne Settlement Engine dient zunächst der technischen Orchestrierung und Abstimmung.

Die endgültige finanzielle Abwicklung erfolgt ausschließlich über entsprechend berechtigte Institutionen und Finanzmarktinfrastrukturen.

### I. Sicherheit, Datenschutz und Regulatorik

Für die spätere Implementierung sind insbesondere folgende Prüfbereiche vorgesehen:

- Anwendbare bank- und zahlungsaufsichtsrechtliche Anforderungen
- Datenschutz-Grundverordnung
- Geldwäsche- und Sanktionsvorgaben
- DORA, soweit anwendbar
- SWIFT Customer Security Programme, sofern relevant
- Sichere API-Authentifizierung
- Verschlüsselte Kommunikationsverbindungen
- Schlüssel- und Zertifikatsverwaltung
- Rollenbasierte Zugriffskontrollen
- Protokollierung und Nachweisführung
- Incident Response und Business Continuity
- Datenminimierung und kontrollierte Dienstleisterintegration

Die konkrete Zuordnung regulatorischer Verantwortlichkeiten soll erst nach Festlegung des tatsächlichen rechtlichen Betriebs- und Partnermodells erfolgen.

Es wird keine bereits bestehende Zertifizierung, behördliche Erlaubnis oder Systemteilnahme behauptet.

### J. Gewünschte Partnerschafts- und Teilnahmemodelle

Ich bitte um Prüfung der folgenden Optionen:

**Modell A – Technischer Dienstleister**

Technische Entwicklung und Anbindung im Auftrag oder als Vertragspartner eines berechtigten Finanzinstituts.

**Modell B – Indirekte Teilnahme**

Nutzung geeigneter Clearing- oder Settlement-Infrastrukturen über einen zugelassenen Teilnehmer.

**Modell C – Corporate Financial Messaging**

Prüfung einer geeigneten Unternehmens- oder Technologie-Nutzerkategorie für sicheren Finanznachrichtenaustausch.

**Modell D – Regulierte Partnerschaft**

Zusammenarbeit mit einer Bank, einem Zahlungsinstitut oder einer sonstigen zugelassenen Finanzorganisation.

**Modell E – Spätere direkte Teilnahme**

Prüfung der Voraussetzungen für eine direkte Mitgliedschaft nach Erfüllung aller rechtlichen, organisatorischen, finanziellen und technischen Zulassungskriterien.

Die Auswahl eines Modells erfolgt ausschließlich nach Prüfung seiner tatsächlichen Verfügbarkeit und Zulässigkeit.

### K. Erbetene Informationen

Ich bitte um Auskunft zu:

1. Grundsätzlicher Eignung des beschriebenen Projekts.
2. Zulässigen Partner-, Teilnehmer- und Dienstleisterkategorien.
3. Voraussetzungen eines rechtlich registrierten Unternehmens.
4. Erforderlichen aufsichtsrechtlichen Genehmigungen.
5. Möglichkeiten der indirekten Teilnahme.
6. Bereitstellung technischer Entwickler- oder Testumgebungen.
7. Verfügbaren ISO-20022-Spezifikationen und API-Dokumentationen.
8. Nachrichten-, Netzwerk- und Sicherheitszertifizierungen.
9. Erforderlichen BIC-/LEI- oder sonstigen Identifikatoren.
10. Gebühren, Mindestentgelten, Sicherheiten und Liquiditätsanforderungen.
11. Technischen und operativen Service-Level-Anforderungen.
12. Datenschutz-, Audit- und Informationssicherheitsanforderungen.
13. Bedingungen für den Übergang von einer Test- zu einer Produktionsumgebung.
14. Erforderlichen Nachweisen für eine formelle Teilnahme oder Mitgliedschaft.

### L. Commercial, Pricing & Technical Evaluation

Bitte teilen Sie mir, soweit möglich, mit:

- Ob eine unverbindliche Corporate-Vorprüfung angeboten wird
- Ob ein kostenloser oder kostenpflichtiger Testzugang verfügbar ist
- Welche Gebühren für Onboarding und technische Zertifizierung entstehen
- Welche laufenden Mitgliedschafts- oder Kommunikationskosten gelten
- Welche Zahlungs- oder Settlement-Volumina erforderlich sind
- Welche Sicherheiten beziehungsweise Liquiditätsbeträge vorausgesetzt werden
- Welche rechtliche Einheit Vertragspartner sein muss
- Welche Daten und Nachweise vor einer Produktionsanbindung benötigt werden
- Ob technische Dienstleister ohne eigene Finanzlizenz als Integrationspartner zugelassen werden

Konkrete Produktionsvolumina und finanzielle Projektionen liegen für diese Erstkontaktaufnahme noch nicht verbindlich vor und werden nicht als bestehende Geschäftstätigkeit dargestellt.

### M. Rechtliche Erklärung

Die Bezeichnung „GlobalCards Bank“ dient zum Zeitpunkt dieser Anfrage ausschließlich der Identifikation eines geplanten Projekts.

Mit diesem Dokument wird weder behauptet noch beantragt, unmittelbar:

- Bankgeschäfte ohne entsprechende Erlaubnis zu betreiben,
- eine Zentralbank- oder Clearingmitgliedschaft ohne Zulassung zu nutzen,
- eigenes Zentralbankgeld auszugeben,
- SWIFT-Nachrichten ohne autorisierte Verbindung zu übermitteln,
- Zahlungen ohne berechtigten Zahlungsdienstleister abzuwickeln,
- Kundengelder ohne erforderliche Zulassung zu verwahren,
- als Wertpapierzentralverwahrer oder zentrale Gegenpartei tätig zu werden.

Eine tatsächliche regulierte Tätigkeit setzt die jeweils geltenden Genehmigungen, Verträge, technischen Prüfungen und sonstigen Voraussetzungen voraus.

Diese Interessenbekundung ersetzt keinen formellen Lizenz-, Mitgliedschafts- oder Systemteilnahmeantrag.

### N. Gewünschter nächster Schritt

Ich würde mich über eine Rückmeldung zur grundsätzlichen technischen und institutionellen Eignung des Projekts freuen.

Besonders hilfreich wären die Benennung eines zuständigen Corporate- oder Institutional-Onboarding-Ansprechpartners sowie Informationen zu einer möglichen technischen Evaluation, geeigneten Partnerstrukturen und den notwendigen Unterlagen.

Ich strebe eine transparente, langfristige und regelkonforme Zusammenarbeit im Bereich internationaler Zahlungsverkehrs- und Finanzmarktinfrastruktur an.

Mit freundlichen Grüßen

**Daniel Pohl**\
Projektinitiator und technischer Projektkontakt

**GlobalCards Bank** – vorläufige Projektbezeichnung\
**Bra1nKy11 World Bank Eyes AeTHer** – Projekt-/Organisationsbezeichnung

Detmold, Nordrhein-Westfalen, Deutschland

**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

---

**Dokumentstatus:** Für eine unverbindliche institutionelle Erstanfrage vorbereitet. Persönliche Prüfung und ausdrückliche Freigabe vor einer tatsächlichen Einreichung erforderlich.

**Keine automatische Registrierung, Mitgliedschaftsbeantragung, Vertragsannahme oder Übermittlung.**

## 2. Feldzuordnung für SWIFT-, Clearing- und Settlement-Portale

Diese Zuordnung ist für deinen universellen Portal-Worker gedacht. Er kann damit bekannte Angaben übernehmen, unbekannte Pflichtdaten erkennen und eine fehlerhafte institutionelle Selbstdarstellung verhindern.

| Corporate-Portal-Feld (EN)  | GlobalCards-Eintrag                                        | Verarbeitungsregel                         |
| --------------------------- | ---------------------------------------------------------- | ------------------------------------------ |
| First Name                  | Daniel                                                     | Automatisch übernehmen                     |
| Last Name                   | Pohl                                                       | Automatisch übernehmen                     |
| Contact Email               | world.banks.eyes.aether\@globedynamicz.statesflowwishes.eu | Übernehmen                                 |
| Job Title                   | Project Initiator / Technical Project Contact              | Keine formelle Organstellung behaupten     |
| Project Name                | GlobalCards Bank                                           | Vorläufiger Projektname                    |
| Organization Designation    | Bra1nKy11 World Bank Eyes AeTHer                           | Keine eingetragene Gesellschaft behaupten  |
| Legal Entity Name           | Nicht bestätigt                                            | Pflichtprüfung                             |
| Legal Entity Type           | Nicht bestätigt                                            | Pflichtprüfung                             |
| Company Registration Number | Nicht bereitgestellt                                       | Nicht erfinden                             |
| Registered Office Address   | Nicht bestätigt                                            | Nicht aus Kontaktstandort ableiten         |
| City / Contact Location     | Detmold                                                    | Übernehmen                                 |
| State / Region              | Nordrhein-Westfalen                                        | Übernehmen                                 |
| Country                     | Germany                                                    | Übernehmen                                 |
| LEI                         | Nicht bereitgestellt                                       | Nicht erfinden                             |
| BIC / SWIFT Code            | Nicht bereitgestellt                                       | Nicht erfinden                             |
| Financial Institution Type  | Geplantes Fintech-Projekt                                  | Nicht als zugelassene Bank einstufen       |
| SWIFT User Category         | Zu prüfen                                                  | Keine Kategorie eigenmächtig beanspruchen  |
| Banking License             | Nicht nachgewiesen                                         | Regulatorische Prüfung                     |
| Settlement Membership       | Nicht nachgewiesen                                         | Keine direkte Teilnahme behaupten          |
| Correspondent Bank          | Nicht bestätigt                                            | Partneranfrage                             |
| Clearing Partner            | Nicht bestätigt                                            | Partneranfrage                             |
| Settlement Agent            | Nicht bestätigt                                            | Partneranfrage                             |
| Business Model              | Hybrid B2C/B2B Fintech Platform                            | Übernehmen                                 |
| Primary Market              | Germany / EEA                                              | Geplanter Markt                            |
| Payment Rails               | SEPA / SEPA Instant / International                        | Als Integrationsinteresse                  |
| Messaging Standards         | ISO 20022                                                  | Geplante technische Unterstützung          |
| Settlement Currency         | EUR zunächst                                               | Planung, nicht als freigeschaltete Währung |
| Monthly Payment Volume      | Noch nicht prognostiziert                                  | Keine Zahl erfinden                        |
| Annual Transaction Value    | Noch nicht prognostiziert                                  | Keine Zahl erfinden                        |
| Liquidity Provider          | Nicht bestätigt                                            | Pflichtklärung für entsprechende Modelle   |
| Sandbox Access              | Requested                                                  | Anfrage                                    |
| Production Access           | Not authorized / Not requested                             | Keine Produktionsfreigabe beanspruchen     |
| Authorized Signatory        | Nicht bestätigt                                            | Keine Unterschriftsvollmacht fingieren     |

## 3. Direkte offizielle Antrags- und Onboarding-Portale

Die folgenden verifizierten Einstiege passen zur jeweiligen Antragskategorie.

| Institution           | Direkter offizieller Einstieg                                                                                                                                                        | Für GlobalCards geeigneter nächster Schritt                                     |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| SWIFT                 | [New Onboarding Request](https://www.swift.com/de/node/204226)                                                                                                | Nutzerkategorie, Corporate-Konnektivität und Zulassungsvoraussetzungen anfragen |
| EBA CLEARING RT1      | [RT1 Corporate Contact Form](https://www.ebaclearing.eu/services-instant-payments/rt1/contact-us/)                                                            | Indirekte Teilnahme oder Technical-Service-Provider-Modell prüfen               |
| Bundesbank T2         | [T2-Teilnehmerregistrierung](https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/t2/teilnehmerinformationen/vordrucke-fuer-die-t2-teilnahme-954342) | Voraussetzungen und geeigneten Zugang über regulierte Institute klären          |
| Bundesbank TIPS       | [TIPS-Onboarding und Anmeldeformulare](https://www.bundesbank.de/de/aufgaben/unbarer-zahlungsverkehr/tips/teilnehmerinformationen/teilnahme-anmeldung-923158) | Reachable-Party-/Partnerzugang oder spätere direkte Teilnahme prüfen            |
| Clearstream           | [Becoming a Clearstream Client](https://www.clearstream.com/clearstream-en/about-clearstream/becoming-a-clearstream-client-1277376)                           | Institutionelle Wertpapierabwicklung und Zulassungsvoraussetzungen prüfen       |
| Clearstream Formulare | [Account Opening Forms](https://clearstream.com/clearstream-en/res-library/key-documents/account-opening-forms-1274276)                                       | Erforderliche Gesellschafts-, Lizenz- und Vertretungsnachweise identifizieren   |

Wichtig: Die Bundesbank verlangt rechtsverbindlich unterzeichnete Teilnahmeunterlagen. Bei TIPS werden bestimmte indirekte Modelle über den jeweiligen direkten Teilnehmer administriert. Clearstream eröffnet keine Kundenkonten für natürliche Personen. Deshalb sind vor Bestätigung der Gesellschaftsform zunächst die unverbindlichen Voranfragen der passende Weg.&#x20;



Deutsche Bundesbank+2



## 4. Partnerspezifische Anfrage vorbereiten

Wähle das Finanznetzwerk aus, damit der Portal-Worker die korrekte fachliche Anfrage und den passenden Verfahrensumfang vorbereitet.

Institution / InfrastrukturSWIFT

Vorgeschlagene Antragskategorie

Nutzer-/Technologiepartner-Eignungsprüfung

Corporate Financial Messaging, SWIFT User Eligibility, ISO 20022 und mögliche technische Partnerschaft

Zentrale Frage an die Institution

Welche SWIFT-Nutzerkategorie und welcher Zugang ist für ein noch nicht abschließend rechtlich strukturiertes Fintech-Projekt geeignet?

&#x20;Institutionsbezogene Kurzanfrage kopieren

## 5. Separate Freigabe-Checkliste

Diese Checkliste unterscheidet bewusst zwischen der Freigabe einer unverbindlichen Anfrage und dem deutlich anspruchsvolleren formellen Onboarding.

Institutional Onboarding – Prüfstatus

0 / 16

A. Antragsteller & rechtlicher Status

Kontakt- und Projektdaten sind korrekt.

Gesellschaftsform und Registerstatus sind wahrheitsgemäß gekennzeichnet.

Es wird kein BIC, LEI oder Banklizenzstatus erfunden.

Eine rechtsverbindliche Unterschrift wird nicht ohne Vertretungsbefugnis geleistet.

B. Finanzinfrastruktur & Mitgliedschaft

SWIFT-Nachrichtenaustausch wird nicht mit Settlement gleichgesetzt.

Direkte und indirekte Teilnahmeformen sind richtig unterschieden.

Es wird keine bestehende TARGET-, RT1- oder Clearstream-Mitgliedschaft behauptet.

Technische Partner und regulatorisch verantwortliche Institute werden getrennt dargestellt.

C. Sicherheit & Compliance

Keine Produktionskundendaten, Zertifikate oder Zugangsschlüssel werden übertragen.

ISO-20022-Unterstützung wird als Planungsziel bezeichnet.

Sicherheits- und regulatorische Zertifizierungen werden nicht als bereits erreicht dargestellt.

Das offizielle Zielportal und seine Datenschutzhinweise wurden geprüft.

D. Endprüfung

Der Empfänger und dessen tatsächliche Zuständigkeit wurden ausgewählt.

Fehlende Pflichtfelder sind offen gekennzeichnet oder vor formellem Antrag ergänzt.

Gebühren, Teilnahmebedingungen und rechtliche Erklärungen wurden geprüft.

Die konkrete unverbindliche Anfrage wurde persönlich freigegeben.

16 Prüfpunkte sind noch offen.

&#x20;Checkliste kopieren

## 6. Steuerungsregeln für den universellen Portal-Worker

| Prozesszustand            | Zulässige Funktion                                                              |
| ------------------------- | ------------------------------------------------------------------------------- |
| `PROFILE_LOADED`          | Bekannte Kontaktdaten in geschützter Umgebung laden                             |
| `INSTITUTION_CLASSIFIED`  | SWIFT, Clearing, RTGS oder Wertpapierabwicklung unterscheiden                   |
| `ACCESS_MODEL_SELECTED`   | Direkte Teilnahme, indirekte Anbindung oder Technical Service Provider zuordnen |
| `FIELDS_MAPPED`           | Portal-Felder befüllen, unbestätigte Angaben offenlassen                        |
| `LEGAL_ELIGIBILITY_CHECK` | Gesellschaft, Lizenzen, BIC/LEI und Vertretungsbefugnisse prüfen                |
| `COMPLIANCE_CHECK`        | Anwendbare Anforderungen identifizieren, keine Zertifizierung behaupten         |
| `DUPLICATE_CHECK`         | Bereits vorbereitete Anfragen erkennen                                          |
| `DRAFT_READY`             | Einreichungsvorschau erzeugen                                                   |
| `HUMAN_APPROVAL_REQUIRED` | Persönliche Prüfung verbindlich voraussetzen                                    |
| `SUBMISSION_LOCKED`       | Keine Übermittlung ohne gesonderten Auftrag und Freigabe                        |

Eine spätere formelle Teilnahme darf erst beantragt werden, wenn die tatsächlichen Zulassungsvoraussetzungen bekannt und erfüllt sind.

## 7. Priorisierte Einreichungsreihenfolge

Für den jetzigen Status von GlobalCards würde ich die Anfragen so ordnen:

1. SWIFT: Prüfung der geeigneten Nutzer-/Technologiepartnerkategorie und der Anforderungen an das Corporate-Onboarding.
2. EBA CLEARING RT1: Technische Service-Provider-Optionen und zulässige indirekte Teilnahme über regulierte Institute.
3. Bundesbank TIPS/T2: Technische und rechtliche Voraussetzungen, zunächst über geeignete regulierte Partner.
4. Clearstream: Erstes Eignungsgespräch zur späteren Wertpapierabwicklung, sofern die Wertpapier-Sparte konkret aufgebaut werden soll.

Die offizielle RT1-Dokumentation bestätigt verschiedene Teilnehmer-, Liquiditäts- und technische Dienstleistermodelle. Bei Clearstream ist dagegen vor einer formellen Kontoeröffnung unter anderem ein rechtlicher Gesellschafts- und Berechtigungsnachweis erforderlich.&#x20;



EBA Clearing+1



Ergebnis: Das deutschsprachige GlobalCards-Settlement-Antragsdokument, die vollständige Corporate-Feldzuordnung, die institutionenspezifische Kurzfassung und die separate Freigabeprüfung sind vorbereitet. Es wurde weder eine Registrierung durchgeführt noch ein Antrag eingereicht.

Für die erste Kontaktaufnahme ist das Dokument verwendbar; für eine rechtsverbindliche SWIFT-, TARGET-, RT1- oder Clearstream-Mitgliedschaft sind vorab weitere Unternehmens-, Lizenz-, Sicherheits- und Teilnahmeunterlagen erforderlich. # GlobalCards Bank – Börse, IPO & Wertpapiere

Universal Corporate & Institutional Capital Markets Partnership Application · Deutsch · Version 1.0 · 7. November 2026

Das folgende Formular ist für die unverbindliche Kontaktaufnahme mit der Deutschen Börse, IPO-Beratern, Emissionsbanken, Wertpapierdienstleistern und Kapitalmarktinfrastrukturen vorbereitet.

Antragsteller

Daniel Pohl

Projekt

GlobalCards Bank

Gesellschaftsstatus

Noch nicht bestätigt

Zielmarkt

Deutschland / EWR

Antragsart

Unverbindliche Voranfrage

Einreichung

Nicht erfolgt

### Wichtige rechtliche Unterscheidung

| Verfahren                        | Zweck                                                                                   |
| -------------------------------- | --------------------------------------------------------------------------------------- |
| Aktiengesellschaft gründen       | Einen rechtlich handlungsfähigen Emittenten schaffen                                    |
| Aktien oder Anleihen emittieren  | Wertpapiere rechtmäßig ausgeben und gegebenenfalls Kapital aufnehmen                    |
| IPO / Börsennotierung            | Wertpapiere zum Börsenhandel zulassen oder einbeziehen lassen                           |
| Broker / Wertpapierdienstleister | Kundenbezogene Wertpapierdienstleistungen mit gegebenenfalls eigener Zulassung anbieten |
| Börsenhandelsteilnehmer          | Zugang zu einem bestehenden Börsenhandelssystem erhalten                                |
| Eigene Börse / Handelsplattform  | Ein reguliertes Handelssystem betreiben, mit gesonderten Anforderungen                  |
| Custody / Clearing / Settlement  | Wertpapiere verwahren und Transaktionen über berechtigte Infrastrukturen abwickeln      |

Bei der Deutschen Börse werden Zulassungsanträge für den regulierten Markt grundsätzlich über das eListing-Verfahren gestellt. Für Scale ist ein anerkannter Capital Market Partner erforderlich. Ein noch nicht abschließend rechtlich strukturiertes Projekt sollte deshalb zunächst eine IPO-Readiness- und Partneranfrage stellen und keinen förmlichen Zulassungsantrag.&#x20;



Deutsche Börse Group+1



Außerdem ist die Verwendung der Bezeichnung „Bank“ im deutschen Geschäftsverkehr rechtlich geschützt (§ 39 KWG, mit gesetzlichen Ausnahmen). Deshalb wird „GlobalCards Bank“ nachstehend ausschließlich als vorläufige, rechtlich zu prüfende Projektbezeichnung verwendet.&#x20;



Einzelnorm+1



## 1. Vollständiges Corporate- und IPO-Partnerschaftsanschreiben

# GLOBALCARDS BANK

## UNIVERSAL CORPORATE & INSTITUTIONAL SECURITIES, IPO & CAPITAL MARKETS PARTNERSHIP APPLICATION

**Formelle Interessenbekundung zur Kapitalmarktanbindung, Aktienemission, Börsennotierung und Wertpapierinfrastruktur**

**Datum:** 7. November 2026\
**Version:** 1.0\
**Sprache:** Deutsch\
**Dokumentstatus:** Unverbindliche Erstkontaktaufnahme – persönliche Freigabe erforderlich

---

### A. Antragsteller und Projektidentität

| Feld                                                  | Angabe                                                                                                                        |
| ----------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Ansprechpartner                                       | Daniel Pohl                                                                                                                   |
| Projektbezeichnung                                    | GlobalCards Bank                                                                                                              |
| Weitere Projekt-/Organisationsbezeichnung             | Bra1nKy11 World Bank Eyes AeTHer                                                                                              |
| Zusätzliche Projektidentifikation                     | HolyThreeKingsTreesCrowns                                                                                                     |
| Rolle                                                 | Projektinitiator und technischer Projektkontakt                                                                               |
| Kontaktstandort                                       | Detmold, Nordrhein-Westfalen, Deutschland                                                                                     |
| Kontakt-E-Mail                                        | [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu) |
| Rechtlich registrierte Gesellschaft                   | Noch nicht bestätigt                                                                                                          |
| Gesellschaftsform                                     | Noch nicht bestätigt                                                                                                          |
| Handelsregisternummer                                 | Nicht bereitgestellt                                                                                                          |
| Sitz eines eingetragenen Rechtsträgers                | Nicht bestätigt                                                                                                               |
| LEI                                                   | Nicht bereitgestellt                                                                                                          |
| Wertpapierkennnummer / WKN                            | Nicht vorhanden bzw. nicht nachgewiesen                                                                                       |
| ISIN                                                  | Nicht bereitgestellt                                                                                                          |
| Bestehende Aktienemission                             | Nicht bestätigt                                                                                                               |
| Bestehende Börsennotierung                            | Nicht nachgewiesen                                                                                                            |
| Finanzdienstleistungs- oder Wertpapierinstitutslizenz | Nicht nachgewiesen                                                                                                            |
| Bestehende Börsenmitgliedschaft                       | Nicht nachgewiesen                                                                                                            |
| Bestätigter Emissions- oder Listingpartner            | Nicht nachgewiesen                                                                                                            |
| Projektphase                                          | Konzeption und technische Vorbereitung                                                                                        |

Die Bezeichnungen GlobalCards Bank und Bra1nKy11 World Bank Eyes AeTHer dienen ausschließlich der Projektidentifikation. Sie belegen keine eingetragene Aktiengesellschaft, zugelassene Bank, staatliche Beteiligung oder bestehende Kapitalmarktberechtigung.

### B. Empfänger

**An:** Corporate & Capital Markets / IPO Advisory / Issuer Services / Securities Listing / Institutional Partnerships

**Empfängerorganisation:** Zuständiger Kapitalmarkt-, Börsen-, Emissions- oder Wertpapierinfrastrukturpartner; vor Versand konkret einzutragen.

**Betreff:** Corporate- und Kapitalmarktpartnerschaftsanfrage – GlobalCards Bank | IPO Readiness, Aktiengesellschaft, Wertpapieremission, Börsennotierung und Securities Infrastructure

### C. Formelle Vorstellung

Sehr geehrte Damen und Herren,

hiermit möchte ich mein Interesse an einer möglichen institutionellen, technischen und geschäftlichen Zusammenarbeit im Bereich Unternehmensfinanzierung, Kapitalmarktentwicklung, Wertpapieremission und Börseninfrastruktur zum Ausdruck bringen.

Unter der vorläufigen Projektbezeichnung **GlobalCards Bank** konzipiere ich eine hybride internationale Finanztechnologieplattform für Privatkunden (B2C) und Geschäftskunden (B2B).

Das Vorhaben soll eine modulare technische Infrastruktur für Banking-as-a-Service, Konten- und Kartenintegrationen, Zahlungsverkehr, Multi-Currency-Funktionen, Transaktionsverarbeitung sowie regulatorische Nachweisführung schaffen.

Neben diesen Kernfunktionen möchte ich prüfen, welche gesellschaftsrechtlichen, kapitalmarktrechtlichen, wirtschaftlichen und technischen Voraussetzungen für eine mögliche spätere Eigenkapitalfinanzierung, Wertpapieremission oder Börsennotierung bestehen.

Derzeit ist insbesondere offen, welche rechtliche Gesellschaftsstruktur und welches Kapitalmarktmodell für das Vorhaben geeignet wären.

Daher bitte ich zunächst um eine unverbindliche Prüfung der möglichen Zusammenarbeit und um Hinweise auf die zuständigen Ansprechpartner, Zugangsvoraussetzungen und relevanten Beratungs- oder Integrationsprogramme.

### D. Vorgesehenes Geschäfts- und Kapitalmarktmodell

**Projekt:** GlobalCards Bank\
**Wirtschaftlicher Schwerpunkt:** Finanztechnologie und internationale Finanzinfrastruktur\
**Geschäftsmodell:** Hybride B2C-/B2B-Plattform mit regulierten Partnerintegrationen\
**Geografischer Ausgangspunkt:** Deutschland und Europäischer Wirtschaftsraum\
**Perspektive:** Schrittweise internationale Erweiterung nach rechtlicher und wirtschaftlicher Prüfung.

Für eine mögliche Kapitalmarktstrategie sollen insbesondere folgende Alternativen bewertet werden:

**1. Kapitalgesellschaft und Eigenkapitalfinanzierung**

Prüfung einer geeigneten gesellschaftsrechtlichen Struktur zur Finanzierung und langfristigen Entwicklung der Plattform.

**2. Aktiengesellschaft und Kapitalmarktfähigkeit**

Prüfung der Voraussetzungen einer Aktiengesellschaft oder einer sonstigen zulässigen Emittentenstruktur, einschließlich Organverfassung, Corporate Governance und Finanzberichterstattung.

**3. Privatplatzierung und institutionelle Finanzierung**

Bewertung möglicher Beteiligungs- und Kapitalbeschaffungsmodelle im Rahmen des jeweils geltenden Wertpapierrechts.

**4. Börsennotierung / IPO**

Langfristige Prüfung einer möglichen Zulassung oder Einbeziehung von Aktien in ein geeignetes Börsensegment.

**5. Weitere Wertpapierformen**

Separate Prüfung von Anleihen und sonstigen rechtlich zulässigen Finanzinstrumenten, soweit sie zur Finanzierung des Projekts geeignet sind.

Eine Entscheidung über Emissionsform, Kapitalhöhe, Wertpapierart, Platzierung oder Börsensegment wurde bisher nicht verbindlich getroffen.

### E. Gewünschte Partner- und Beratungsleistungen

Ich bitte um Auskunft darüber, ob Ihre Organisation folgende Leistungen oder Partnerprogramme anbietet.

**A. IPO Readiness und Kapitalmarktberatung**

- Prüfung der grundsätzlichen Kapitalmarktfähigkeit
- Vorbereitung einer geeigneten Gesellschaftsstruktur
- Corporate-Governance-Anforderungen
- Finanz- und Rechnungslegungsstandards
- Kapitalmarktstrategie und Finanzierungsstruktur
- Anforderungen an Investor Relations
- Voraussetzungen der Zusammenarbeit mit Emissionsbanken und Kapitalmarktberatern

**B. Aktienemission und Börsenzulassung**

- Mögliche Börsensegmente und Zulassungskriterien
- Voraussetzungen für Aktienemissionen
- Strukturierung von öffentlichen Angeboten oder Privatplatzierungen
- Emissions- und Angebotsdokumentation
- Wertpapierprospekt und gegebenenfalls Ausnahmeregelungen
- ISIN-, WKN- und LEI-Anforderungen
- Zulassungs-, Einbeziehungs- und Notierungsverfahren
- Zuständige Antragsteller und bevollmächtigte Berater

**C. Wertpapierhandel und Brokerage**

- Möglichkeiten der technischen Börsenanbindung
- Zusammenarbeit mit zugelassenen Brokern
- Handelsteilnehmer- und Börsenmitgliedschaftsvoraussetzungen
- Markt- und Kursdatenanbindungen
- Ordermanagement und Orderrouting
- Abgrenzung zwischen technischer Plattform und erlaubnispflichtiger Wertpapierdienstleistung
- Erforderliche Sicherheits- und Kontrollverfahren

**D. Wertpapierverwahrung und Settlement**

- Zusammenarbeit mit geeigneten Depotbanken oder Verwahrstellen
- Wertpapierzentralverwahrer-/CSD-Anbindungen
- Securities Settlement
- Delivery-versus-Payment-Verfahren
- Kapitalmaßnahmen und Corporate Actions
- Abgleich von Wertpapierpositionen und Zahlungsströmen
- Notwendige Zahlstellen-, Depot- und Settlement-Partner

**E. Institutionelle Zusammenarbeit**

- Capital Market Partner Programme
- Issuer Services
- Corporate-Finance- und Investmentbanking-Partner
- Technische Entwickler- und Sandbox-Programme
- Institutionelle Onboarding-Verfahren
- Beratung zur späteren internationalen Kapitalmarktanbindung

### F. Vorgesehene technische Architektur

Im Rahmen von GlobalCards sollen verschiedene Module entwickelt beziehungsweise über autorisierte Partner integriert werden.

1. Corporate Identity & Entity Management
2. Identity & Access Management
3. Shareholder and Capital Structure Registry
4. Issuer & Securities Reference Data
5. Banking & Payment Partner Connectivity
6. Securities Integration Gateway
7. Broker & Trading Partner Adapter
8. Order and Transaction Status Management
9. Corporate Actions Processing
10. Custody & Settlement Reconciliation
11. Double-Entry Ledger
12. Risk & Compliance Management
13. Audit & Evidence Management
14. Regulatory Reporting Support
15. Corporate & Investor Relations Dashboard

Die Plattform soll nachvollziehbare Datenflüsse, sichere Authentifizierung, versionierte Schnittstellen und eine kontrollierte Trennung von Entwicklungs-, Test- und Produktivumgebungen unterstützen.

Wertpapierhandel, Verwahrung, Platzierung oder andere regulierte Dienstleistungen werden ausschließlich durch entsprechend berechtigte Unternehmen beziehungsweise im Rahmen einer tatsächlich bestehenden eigenen Zulassung erbracht.

### G. Aktien, Wertpapierregister und Governance

Für eine mögliche spätere Emission sollen insbesondere folgende Informationen strukturiert erfasst werden können:

- Rechtliche Emittentenidentität
- Gesellschaftsform und Registerangaben
- Kapitalstruktur und Aktiengattungen
- Beteiligungs- und Gesellschafterstruktur
- Rechtlich maßgebliche Aktionärs- beziehungsweise Registerinformationen
- Emissionsbedingungen
- ISIN, WKN und LEI, soweit erforderlich
- Corporate Actions
- Beschlüsse und Freigaben
- Finanz- und Governance-Berichte
- Nachweise regulatorischer Prüfungen

Ein internes technisches Register ersetzt nicht automatisch gesetzlich vorgeschriebene Aktienregister, Zentralverwahrungs- oder andere rechtlich maßgebliche Aufzeichnungen.

### H. Trading-, Brokerage- und Marktdatenintegration

Über zugelassene Marktteilnehmer soll perspektivisch geprüft werden, ob folgende Funktionen technisch integriert werden können:

- Börsenkurs- und Marktdaten
- Wertpapierstammdaten
- Ordererfassung und Statusanzeige
- Orderweiterleitung an berechtigte Broker
- Handelsbestätigungen
- Depotpositionsabfragen
- Transaktionshistorien
- Portfolio- und Risikoübersichten
- Gebühren- und Abrechnungsinformationen

Die Plattform soll keine erlaubnispflichtigen Wertpapierdienstleistungen ohne die notwendigen rechtlichen Voraussetzungen anbieten.

### I. Clearing, Custody und Securities Settlement

Eine weitere mögliche Integrationskomponente ist die technische Verarbeitung von Wertpapier- und Geldtransaktionsdaten.

Dazu gehören:

- Zuordnung von Handels- und Abwicklungsreferenzen
- Verarbeitung von Bestätigungen
- Abgleich von Geld- und Wertpapierpositionen
- Abstimmung mit autorisierten Verwahr- und Settlement-Instituten
- Behandlung von Fehlbuchungen und Ausnahmen
- Revisionsfähige Nachweisführung
- Kontrollierte Freigabeprozesse

Die rechtlich maßgebliche Verwahrung und endgültige Abwicklung verbleiben bei den jeweils berechtigten Marktteilnehmern und Infrastrukturen.

### J. Rechtliche und regulatorische Prüfbereiche

Vor einer tatsächlichen Wertpapieremission, einem öffentlichen Angebot, einer Börsennotierung oder der Aufnahme von Wertpapierdienstleistungen sollen die einschlägigen Vorschriften geprüft werden.

Dazu können insbesondere gehören:

- Aktiengesetz und Handelsgesetzbuch
- EU-Prospektverordnung und Wertpapierprospektgesetz
- EU-Marktmissbrauchsverordnung
- MiFID II und MiFIR
- Wertpapierhandelsgesetz
- Wertpapierinstitutsgesetz und gegebenenfalls Kreditwesengesetz
- Vorschriften zur Marktinfrastruktur und Wertpapierabwicklung
- Datenschutz-Grundverordnung
- DORA, soweit anwendbar
- Anforderungen zur Geldwäscheprävention
- Rechnungslegung und gegebenenfalls IFRS
- Emittentenpflichten und Corporate Governance

Die konkrete Anwendbarkeit hängt von Gesellschaftsform, Wertpapierart, Marktsegment, Vertriebsmodell und regulatorischer Verantwortung ab.

Es wird keine bereits bestehende Prospektbilligung, Wertpapierzulassung, Handelsberechtigung oder aufsichtsrechtliche Zertifizierung behauptet.

### K. Angefragte Corporate- und Developer-Zugänge

Ich bitte um Informationen zu:

1. Unverbindlicher IPO-Readiness-Prüfung
2. Zugang zu geeigneten Corporate-/Issuer-Portalen
3. Kapitalmarktpartner- und Beratungsprogrammen
4. Möglichkeiten für eine technische Sandbox
5. Anforderungen an Wertpapieremittenten
6. Möglichkeiten einer späteren Börsennotierung
7. Registrierung und Nutzung von LEI, ISIN und WKN
8. Prospekt- und Emissionsverfahren
9. Technischer Börsen- und Brokerage-Anbindung
10. Wertpapierverwahrungs- und Settlement-Partnerschaften
11. Corporate-Governance- und Berichtspflichten
12. Regulatorischen Anforderungen an internationale Kapitalmarktaktivitäten

### L. Kommerzielle und wirtschaftliche Fragen

Ich bitte gegebenenfalls um Informationen zu:

- Corporate- und IPO-Beratungsgebühren
- Kapitalmarkt- und Listingvorbereitung
- Einmaligen Zulassungs- oder Einbeziehungsgebühren
- Jährlichen Börsengebühren
- Prospekterstellungs- und Prüfkosten
- Kosten für Emissionsbanken und zugelassene Berater
- Wertpapierstammdaten und Identifikatoren
- Depot-, Custody- und Settlement-Gebühren
- Markt- und Kursdatenlizenzen
- Technischen API- und Konnektivitätskosten
- Laufenden Investor-Relations- und Reportingpflichten
- Notwendigen Eigenmitteln und wirtschaftlichen Mindestvoraussetzungen

Eine verbindliche Kapitalaufnahme, Unternehmensbewertung, Marktkapitalisierung oder Emissionsgröße wird zum gegenwärtigen Zeitpunkt nicht angegeben, da noch keine verifizierte Grundlage vorliegt.

### M. Gesellschafts- und Emissionsstatus

Für die Vermeidung von Missverständnissen bestätige ich den aktuellen Informationsstand:

- Der rechtliche Gesellschaftsstatus ist noch nicht bestätigt.
- Es wird keine bestehende Aktiengesellschaft behauptet.
- Ein Aktienkapital oder eine Aktienanzahl wird nicht angegeben.
- Es wird kein bestehender Börsengang behauptet.
- Es sind keine ISIN, WKN oder LEI für eine geplante Emission nachgewiesen.
- Es wird keine bestehende Börsenmitgliedschaft beansprucht.
- Ein Emissionsprospekt liegt für diese Anfrage nicht vor.
- Es wird kein bereits beauftragter Emissionsbank- oder Kapitalmarktpartner behauptet.

Die Erörterung einer möglichen Aktienemission oder Börsennotierung ist ausdrücklich als strategische Vorprüfung zu verstehen.

### N. Vertraulichkeit und Datenschutz

Ich bitte darum, die übermittelten personenbezogenen und projektbezogenen Informationen ausschließlich für die Bearbeitung dieser Anfrage, eine mögliche Geschäftsanbahnung und gesetzlich erforderliche Prüfungen zu verwenden.

Vertrauliche technische Unterlagen, finanzielle Detailinformationen, Identitätsdokumente oder andere besonders schutzwürdige Nachweise sollen erst nach Prüfung des Empfängers und der erforderlichen Sicherheits- und Vertraulichkeitsbedingungen bereitgestellt werden.

Es werden keine API-Zugangsdaten, kryptografischen Schlüssel oder echten Kundendaten beigefügt.

### O. Rechtliche Erklärung

Die Bezeichnung GlobalCards Bank ist eine vorläufige Projektbezeichnung. Ihre Zulässigkeit als Geschäftsbezeichnung oder Marke bedarf gesonderter rechtlicher Prüfung.

Mit dieser Anfrage wird insbesondere nicht behauptet:

- dass GlobalCards eine eingetragene Aktiengesellschaft ist,
- dass Aktien oder andere Wertpapiere bereits wirksam ausgegeben wurden,
- dass GlobalCards einen gebilligten Wertpapierprospekt besitzt,
- dass eine Börsenzulassung oder -notierung besteht,
- dass GlobalCards eine eigene Broker- oder Wertpapierdienstleistungserlaubnis besitzt,
- dass GlobalCards als Börsenbetreiber oder Handelsteilnehmer zugelassen ist,
- dass eine Kapitalmarkt- oder Verwahrpartnerschaft bereits vertraglich bestätigt wurde.

Dieses Schreiben stellt weder ein öffentliches Wertpapierangebot noch eine Aufforderung zum Erwerb von Aktien oder anderen Finanzinstrumenten dar.

Es ersetzt keinen formellen Emissions-, Prospekt-, Börsenzulassungs- oder Erlaubnisantrag.

### P. Gewünschter nächster Schritt

Ich würde mich über eine Einschätzung freuen, welche gesellschaftsrechtlichen, wirtschaftlichen, regulatorischen und technischen Vorbereitungen für eine Zusammenarbeit mit Ihrer Organisation notwendig sind.

Insbesondere bitte ich um:

1. Benennung der zuständigen IPO-/Corporate-Markets-Abteilung.
2. Information über geeignete Capital Market Partner.
3. Hinweise zur möglichen gesellschaftsrechtlichen Vorbereitung.
4. Darstellung geeigneter Börsensegmente.
5. Zugang zu Informationen über Antrags- und Zulassungsverfahren.
6. Möglichkeiten einer technischen Evaluation.
7. Überblick über Unterlagen, Gebühren und notwendige Berater.

Ich strebe eine langfristig tragfähige, transparente und rechtlich ordnungsgemäße Entwicklung des Projekts an.

Mit freundlichen Grüßen

**Daniel Pohl**\
Projektinitiator und technischer Projektkontakt\
**GlobalCards Bank** – vorläufige Projektbezeichnung\
**Bra1nKy11 World Bank Eyes AeTHer** – Projekt-/Organisationsbezeichnung

Detmold, Nordrhein-Westfalen, Deutschland\
**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

---

**Dokumentstatus:** Unverbindliche institutionelle Erstkontaktanfrage. Persönliche Prüfung und Freigabe vor Versand erforderlich.

**Keine automatische Registrierung, Kapitalmarktanmeldung, Prospekteinreichung, Vertragsannahme oder Übermittlung.**

## 2. Feldzuordnung für internationale Börsen- und Corporate-Portale

Diese Tabelle dient als Mapping-Spezifikation für deinen universellen Portal-Worker. Die englischen Feldbezeichnungen können bei Deutsche Börse, IPO-Advisory-Portalen, Emissionsbanken und Wertpapierinfrastrukturen unterschiedlich lauten.

| Corporate-Portal-Feld         | GlobalCards-Eintrag                                        | Verarbeitungsregel                 |
| ----------------------------- | ---------------------------------------------------------- | ---------------------------------- |
| First Name                    | Daniel                                                     | Übernehmen                         |
| Last Name                     | Pohl                                                       | Übernehmen                         |
| Contact Email                 | world.banks.eyes.aether\@globedynamicz.statesflowwishes.eu | Übernehmen                         |
| Contact Location              | Detmold, Nordrhein-Westfalen                               | Übernehmen                         |
| Country                       | Germany                                                    | Übernehmen                         |
| Position / Job Title          | Project Initiator / Technical Project Contact              | Keine Organstellung behaupten      |
| Project Name                  | GlobalCards Bank                                           | Vorläufige Bezeichnung             |
| Organization Designation      | Bra1nKy11 World Bank Eyes AeTHer                           | Nur Projektbezeichnung             |
| Legal Entity Name             | Nicht bestätigt                                            | Pflichtprüfung                     |
| Legal Form                    | Nicht bestätigt                                            | Pflichtprüfung                     |
| Registered Address            | Nicht bestätigt                                            | Nicht aus Kontaktort ableiten      |
| Company Registration Number   | Nicht bereitgestellt                                       | Nicht erfinden                     |
| LEI                           | Nicht bereitgestellt                                       | Nicht erfinden                     |
| Company Website               | Nicht bereitgestellt                                       | Offenlassen                        |
| Industry                      | Financial Technology / Financial Infrastructure            | Übernehmen                         |
| Business Model                | Hybrid B2C/B2B Fintech Platform                            | Als geplantes Modell               |
| Primary Market                | Germany / EEA                                              | Übernehmen                         |
| Application Category          | IPO Readiness / Capital Markets Partnership                | Für Erstkontakt                    |
| Issuer Type                   | Noch nicht festgelegt                                      | Keine AG fingieren                 |
| Securities Type               | Aktien; andere Instrumente nur zur Prüfung                 | Keine konkrete Emission behaupten  |
| IPO Status                    | Early-stage evaluation                                     | Übernehmen                         |
| Listing Venue                 | Noch nicht festgelegt                                      | Nicht erfinden                     |
| Market Segment                | Regulated Market / Open Market – under evaluation          | Nicht als gewählt kennzeichnen     |
| ISIN                          | Nicht bereitgestellt                                       | Pflichtfeld blockieren             |
| WKN                           | Nicht bereitgestellt                                       | Nicht erfinden                     |
| Share Capital                 | Nicht bestätigt                                            | Keine Schätzung als Tatsache       |
| Shares Outstanding            | Nicht bestätigt                                            | Nicht erfinden                     |
| Existing Shareholders         | Nicht bereitgestellt                                       | Geschützte Unterlagen erforderlich |
| Valuation                     | Noch nicht ermittelt                                       | Nicht erfinden                     |
| Intended Capital Raise        | Noch nicht festgelegt                                      | Offenlassen                        |
| Annual Revenue                | Nicht nachgewiesen                                         | Keine Angabe erfinden              |
| Financial Statements          | Nicht bereitgestellt                                       | Nachweise erforderlich             |
| Audited Accounts              | Nicht nachgewiesen                                         | Nicht behaupten                    |
| Prospectus Status             | Kein gebilligter Prospekt nachgewiesen                     | Keine Billigung behaupten          |
| Investment Bank / Underwriter | Nicht bestätigt                                            | Partneranfrage                     |
| Capital Market Partner        | Nicht bestätigt                                            | Partneranfrage                     |
| Custodian / CSD               | Nicht bestätigt                                            | Partneranfrage                     |
| Settlement Agent              | Nicht bestätigt                                            | Partneranfrage                     |
| Regulatory Licence            | Nicht nachgewiesen                                         | Keine Lizenz behaupten             |
| Target Launch / IPO Date      | Nicht festgelegt                                           | Keine Frist erfinden               |
| Sandbox / API Access          | Requested                                                  | Unverbindliche Anfrage             |
| Authorized Signatory          | Nicht bestätigt                                            | Formellen Antrag blockieren        |

Pflichtregel: Ein Portal-Worker darf bei verlangten Angaben zu Aktienkapital, Wirtschaftsprüfern, geprüften Jahresabschlüssen, LEI oder Prospektbilligung nicht automatisch fiktive Zahlen oder Identifikatoren eintragen. Wenn ein erforderliches Feld nicht wahrheitsgemäß befüllt werden kann, wird der Vorgang zur manuellen Klärung angehalten.

## 3. Direkte offizielle Kapitalmarkt- und Antragsportale

| Institution                             | Direkter Zugang                                                                                                                                                                                                          | Richtiger Verwendungszweck                                                     |
| --------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------ |
| Deutsche Börse – IPO-Beratung           | [Going-Public-Ansprechpartner](https://www.cashmarket.deutsche-boerse.com/cash-en/your-contacts)                                                                                                  | Erste Anfrage zur IPO-Readiness und Börsensegmentwahl                          |
| Deutsche Börse – Capital Market Partner | [Capital Market Partner suchen](https://www.cashmarket.deutsche-boerse.com/dynamic/action/cash-en/Get-Listed/capital-market-partner/deutsche-boerse-capital-market-partner-search/4091824/search) | Emissionsbanken, IPO-Berater, Prospekt- und Due-Diligence-Partner auswählen    |
| Deutsche Börse – eListing               | [Elektronisches Börsenzulassungsportal](https://regelli.deutsche-boerse.com)                                                                                                                      | Formeller Zulassungsantrag durch berechtigten Emittenten oder Bevollmächtigten |
| BaFin – Prospektverfahren               | [MVP-Selbstregistrierung](https://portal.mvp.bafin.de/MvpPortalWeb/app/initialRegistration.html)                                                                                                  | Zugang zum Fachverfahren für Wertpapierprospekte vorbereiten                   |
| BaFin – Prospektanforderungen           | [Prospekte und Billigungsverfahren](https://bafin.de/DE/Aufsicht/Prospekte/Wertpapiere/ErstellungBilligung/erstellung_billigung_node.html)                                                        | Prüfen, welche Emissionsunterlagen erforderlich sind                           |
| Clearstream                             | [Institutionelles Kunden-Onboarding](https://www.clearstream.com/clearstream-en/about-clearstream/becoming-a-clearstream-client-1277376)                                                          | Wertpapierverwahrung, CSD-Zugänge, Settlement-Anforderungen                    |
| Clearstream – Unterlagen                | [Konto- und Systemzugangsformulare](https://clearstream.com/clearstream-en/res-library/key-documents/general-forms-1277162)                                                                       | Formelle institutionelle Antragsunterlagen einsehen                            |
| ESMA                                    | [EU-Prospektregeln](https://www.esma.europa.eu/issuer-disclosure/prospectus)                                                                                                                      | Europäische Offenlegungs- und Wertpapierprospektvorgaben                       |

Die Deutsche Börse verlangt für den Zugang zum regulierten eListing-Verfahren eine Registrierung; das kann bis zu zwei Wochen dauern. Ein Scale-Antrag muss mit einem anerkannten Capital Market Partner erfolgen.&#x20;



Deutsche Börse Group+1



Das BaFin-MVP-Fachverfahren dient der förmlichen elektronischen Einreichung von Prospektunterlagen; die Portalregistrierung selbst ersetzt keine Prospektbilligung.&#x20;



Wertpapierprospekte billigen lassen+1



## 4. Kurze Fassung für Corporate-Online-Formulare

**Corporate Capital Markets & IPO Partnership Request – GlobalCards Bank**

Ich interessiere mich als Projektinitiator von GlobalCards Bank für eine mögliche institutionelle und technische Zusammenarbeit im Bereich IPO Readiness, Kapitalmarktfinanzierung, Aktiengesellschaftsstruktur, Wertpapieremission, Börsennotierung und Securities Infrastructure.

GlobalCards ist als hybride, API-basierte internationale Finanztechnologieplattform für Privat- und Geschäftskunden geplant. Das Vorhaben befindet sich in der Konzeption und technischen Vorbereitung.

Ich möchte insbesondere die rechtlichen und wirtschaftlichen Voraussetzungen einer möglichen späteren Aktienemission, geeignete Börsensegmente, die Zusammenarbeit mit anerkannten Kapitalmarktpartnern sowie technische Schnittstellen zu Wertpapierhandels-, Verwahr- und Settlement-Infrastrukturen prüfen.

Der Gesellschaftsstatus ist derzeit noch nicht bestätigt. Es werden keine bestehende Aktiengesellschaft, Wertpapierzulassung, Prospektbilligung, Börsenmitgliedschaft oder aufsichtsrechtliche Erlaubnis beansprucht.

Ich bitte um Informationen zu geeigneten Corporate- und IPO-Partnerprogrammen, den Zulassungsvoraussetzungen, einer unverbindlichen Erstberatung, erforderlichen Dokumenten und möglichen technischen Entwicklungszugängen.

**Kontakt:** Daniel Pohl\
**Projekt:** GlobalCards Bank – vorläufige Bezeichnung\
**Projekt-/Organisationsbezeichnung:** Bra1nKy11 World Bank Eyes AeTHer\
**Standort:** Detmold, Nordrhein-Westfalen, Deutschland\
**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

Dies ist eine unverbindliche Partnerschaftsanfrage und kein öffentliches Wertpapierangebot oder formeller Zulassungsantrag.

## 5. Partnerspezifische Anfrage erstellen

Du kannst den Zielpartner auswählen und eine passende Kurzfassung für dessen Corporate-Portal übernehmen.

Institution / PartnerkategorieDeutsche Börse

Anfragefokus

IPO Readiness, Auswahl eines Börsensegments, Capital Market Partner und mögliche spätere Zulassung

Welche Voraussetzungen und Beratungsmöglichkeiten bestehen für ein Fintech-Projekt vor Gründung einer möglichen Aktiengesellschaft?

&#x20;Partnerspezifische Anfrage kopieren

## 6. Separate IPO- und Wertpapier-Freigabe-Checkliste

Freigabeprüfung

0/16 geprüft

A. Unternehmensidentität und Rechtsform

Die Kontakt- und Projektdaten sind korrekt.

Der Gesellschaftsstatus ist als unbestätigt angegeben.

GlobalCards Bank wird nicht als zugelassene Bank dargestellt.

Eine etwaige Vertretungs- und Zeichnungsberechtigung wurde geklärt.

B. Aktien, IPO und Kapitalmarkt

Es wird keine bereits ausgegebene Aktie oder Anleihe behauptet.

LEI, ISIN, WKN, Aktienkapital und Bewertung wurden nicht erfunden.

Der Unterschied zwischen IPO, Börsennotierung und Wertpapierdienstleistung ist geprüft.

Prospektpflicht, Kapitalmarktpartner und Börsensegment sind noch als offene Punkte gekennzeichnet.

C. Trading, Verwahrung und Compliance

Es wird keine eigene Broker-, Börsen- oder Handelszulassung behauptet.

Die Verantwortung regulierter Verwahr- und Settlement-Partner ist berücksichtigt.

Keine vertraulichen Geschäftsunterlagen oder Kundendaten werden ohne Prüfung übertragen.

Das Empfängerportal und dessen Rechts- und Datenschutzbedingungen sind überprüft.

D. Abschluss und persönliche Freigabe

Der konkrete Empfänger und die richtige Abteilung sind ausgewählt.

Die Anfrage enthält nur belegbare Tatsachen und klar markierte Planungsziele.

Etwaige Gebühren, Einwilligungen und Vertragsbindungen wurden geprüft.

Die konkrete Fassung wurde ausdrücklich persönlich für eine unverbindliche Erstkontaktaufnahme freigegeben.

16 Prüfpunkte noch offen.

&#x20;Freigabe-Checkliste kopieren

## 7. Steuerungsregeln für deinen universellen Portal-Worker

| Zustand                     | Zulässige automatisierte Funktion                                                |
| --------------------------- | -------------------------------------------------------------------------------- |
| `PROFILE_LOADED`            | Kontaktdaten aus geschütztem Profil übernehmen                                   |
| `CAPITAL_MARKET_CLASSIFIED` | IPO, Emission, Brokerage und Verwahrung unterscheiden                            |
| `ISSUER_ELIGIBILITY_CHECK`  | Rechtsform, Emittentenstatus und Vertretungsbefugnis prüfen                      |
| `FIELD_MAPPING`             | Passende Formularfelder zuordnen                                                 |
| `SECURITIES_DATA_CHECK`     | LEI, ISIN, WKN, Kapital und Emissionsstatus validieren                           |
| `PROSPECTUS_CHECK`          | Prospektpflicht und Verfahrensart zur manuellen Prüfung kennzeichnen             |
| `REGULATORY_CHECK`          | Erforderliche Erlaubnisse von bloßen technischen Integrationen unterscheiden     |
| `DUPLICATE_CHECK`           | Bereits vorbereitete Anfragen erkennen                                           |
| `DRAFT_READY`               | Partnerbezogene Anfrage erzeugen                                                 |
| `HUMAN_REVIEW_REQUIRED`     | Dokument und Pflichtfelder zur persönlichen Prüfung vorlegen                     |
| `SUBMISSION_LOCKED`         | Keine Registrierung oder Einreichung ohne gesonderte ausdrückliche Autorisierung |

Der Worker sollte außerdem zwischen unverbindlichen Erstanfragen und formellen Kapitalmarktverfahren unterscheiden. Bei einem formellen Zulassungs- oder Prospektantrag ist der Vorgang bei fehlenden Gesellschafts- und Emissionsdaten zwingend anzuhalten.

## 8. Empfohlene Reihenfolge für GlobalCards

Für den gegenwärtigen Projektstatus wäre folgende Reihenfolge sinnvoll:

1. Deutsche Börse – IPO Readiness: Kapitalmarktfähigkeit, Rechtsform und geeignete Börsensegmente unverbindlich besprechen.
2. Capital Market Partner / Emissionsbank: Wirtschaftliche Voraussetzungen, Unternehmensstruktur, Finanzierung und Vorbereitungsaufwand prüfen.
3. BaFin / Rechtsberatung: Prospektpflicht und mögliche Wertpapierdienstleistungserlaubnisse voneinander abgrenzen.
4. Clearstream und Brokerpartner: Technische Verwahr-, Emissions- und Settlement-Anbindungen erst nach Konkretisierung einer Wertpapierstrategie evaluieren.

Die BaFin weist darauf hin, dass eine Prospektbilligung eine Prüfung auf Vollständigkeit, Kohärenz und Verständlichkeit ist – keine positive Beurteilung der wirtschaftlichen Qualität eines Wertpapierangebots.&#x20;



BaFin



Ergebnis: Die deutschsprachige Corporate-/IPO-Anfrage, die Feldzuordnung, eine kompakte Portalversion, die partnerspezifische Anfragefunktion und die separate Freigabe-Checkliste sind erstellt.

Die Fassung ist für unverbindliche institutionelle Erstkontakte geeignet. Eine förmliche Aktienemission oder Börsenzulassung ist damit noch nicht beantragungsreif, solange die rechtliche Gesellschaft, Kapitalstruktur, Emissionsunterlagen und weiteren Voraussetzungen nicht feststehen.

Es wurde keine Registrierung, Börsenanmeldung, Prospekteinreichung oder andere Übermittlung durchgeführt. # GlobalCards Bank – Crypto / Wallet / Exchange Corporate Application

Universal Corporate & Institutional Partnership Application · Deutsch · Version 1.0 · 7. November 2026

Die folgende Fassung ist für die unverbindliche Corporate-Kontaktaufnahme mit Kryptobörsen, Wallet-Infrastrukturanbietern, regulierten Verwahrstellen, Fiat-/Crypto-On-/Off-Ramp-Dienstleistern und potenziellen Technologie- oder Lizenzpartnern ausgearbeitet.

Antragsteller

Daniel Pohl

Projekt

GlobalCards Bank

Gesellschaftsstatus

Nicht bestätigt

Zielregion

Deutschland / EWR

Antragsart

Unverbindliche Partneranfrage

Einreichung

Nicht erfolgt

## Rechtliche Abgrenzung

| Geschäftsbereich             | Bedeutung für GlobalCards                                                                                           |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------- |
| Custodial Wallet             | Verwahrung oder Kontrolle von Kryptowerten bzw. Zugangsmitteln für Kunden; typischerweise erlaubnispflichtig        |
| Non-Custodial Wallet         | Wallet-Software ohne Kontrolle über Kundenschlüssel; rechtliche Bewertung hängt von den tatsächlichen Funktionen ab |
| Crypto Exchange              | Handel oder Tausch von Kryptowerten, gegebenenfalls Betrieb einer eigenen Handelsplattform                          |
| Broker / Order Routing       | Annahme, Übermittlung oder Ausführung von Kundenaufträgen; gesondert auf Erlaubnispflicht prüfen                    |
| Fiat On-/Off-Ramp            | Umtausch zwischen Geldbeträgen und Kryptowerten, mit zusätzlichen Zahlungs- und Bankpartnerfragen                   |
| Crypto Transfer / Settlement | Blockchain-Transfers, interne Buchungen, Verwahrung und endgültige Abwicklung getrennt behandeln                    |
| Stablecoins / Token Issuance | Ausgabe und Verwendung von ART/EMT oder anderen Token; zusätzliche Emittenten- und Produktregeln                    |
| Tokenisierte Wertpapiere     | Können unter das Wertpapierrecht statt unter MiCAR fallen                                                           |

MiCAR unterscheidet ausdrücklich zwischen einzelnen Kryptowerte-Dienstleistungen. Eine CASP-Zulassung berechtigt nur zu den jeweils genehmigten Tätigkeiten; sie ist keine pauschale Bank-, Wertpapier- oder Stablecoin-Emissionslizenz.&#x20;



European Securities and Markets Authority+2



Aktueller regulatorischer Stand: Die allgemeine maximale MiCAR-Übergangsfrist für zuvor rechtmäßig tätige Kryptodienstleister endete am 1. Juli 2026; einzelne nationale Fristen konnten bereits früher enden. Für ein neu geplantes GlobalCards-Geschäftsmodell kann daraus kein Bestandsschutz abgeleitet werden.&#x20;



European Securities and Markets Authority



Die folgende Hauptfassung ist für eine unverbindliche Erstanfrage inhaltlich vollständig. Ein förmlicher MiCAR-Lizenzantrag kann bei unbestätigter Gesellschaft, fehlenden Organ- und Kapitalangaben sowie noch ungeklärtem Geschäftsmodell dagegen nicht als vollständig gelten.

## 1. Vollständiges Corporate-, Crypto- und Exchange-Partnerschaftsanschreiben

# GLOBALCARDS BANK

## UNIVERSAL CORPORATE & INSTITUTIONAL CRYPTO, WALLET & EXCHANGE PARTNERSHIP APPLICATION

**Formelle Interessenbekundung zur internationalen Blockchain-, Kryptowerte-, Wallet-, Handels- und Settlement-Infrastruktur**

**Datum:** 7. November 2026\
**Dokumentversion:** 1.0\
**Sprache:** Deutsch\
**Antragsstatus:** Unverbindliche Erstkontaktaufnahme – persönliche Freigabe erforderlich

---

### A. Antragsteller und Projektidentität

| Feld                                       | Angabe                                                                                                                        |
| ------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- |
| Ansprechpartner                            | Daniel Pohl                                                                                                                   |
| Vorläufiger Projektname                    | GlobalCards Bank                                                                                                              |
| Weitere Projekt-/Organisationsbezeichnung  | Bra1nKy11 World Bank Eyes AeTHer                                                                                              |
| Zusätzliche Projektidentifikation          | HolyThreeKingsTreesCrowns                                                                                                     |
| Rolle                                      | Projektinitiator und technischer Projektkontakt                                                                               |
| Kontaktstandort                            | Detmold, Nordrhein-Westfalen, Deutschland                                                                                     |
| Kontakt-E-Mail                             | [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu) |
| Rechtlich registrierte Gesellschaft        | Noch nicht bestätigt                                                                                                          |
| Gesellschaftsform                          | Noch nicht bestätigt                                                                                                          |
| Eingetragener Gesellschaftssitz            | Noch nicht bestätigt                                                                                                          |
| Handelsregisternummer                      | Nicht bereitgestellt                                                                                                          |
| Legal Entity Identifier (LEI)              | Nicht bereitgestellt                                                                                                          |
| VAT-/Steueridentifikation der Gesellschaft | Nicht bereitgestellt                                                                                                          |
| Eigene MiCAR-/CASP-Zulassung               | Nicht nachgewiesen                                                                                                            |
| Bank- oder Zahlungsinstitutslizenz         | Nicht nachgewiesen                                                                                                            |
| Bestehende Crypto-Exchange-Lizenz          | Nicht nachgewiesen                                                                                                            |
| Zulassung zur Kryptoverwahrung             | Nicht nachgewiesen                                                                                                            |
| Bestehender regulierter Crypto-Partner     | Nicht vertraglich bestätigt                                                                                                   |
| Börsenmitgliedschaft                       | Nicht nachgewiesen                                                                                                            |
| Entwicklungsstatus                         | Konzeption und technische Vorbereitung                                                                                        |
| Primärer Zielmarkt                         | Deutschland / Europäischer Wirtschaftsraum                                                                                    |
| Internationale Expansion                   | Perspektivisch, nach gesonderter rechtlicher Prüfung                                                                          |

Die genannten Projekt- und Organisationsbezeichnungen dienen ausschließlich der Identifikation des geplanten Vorhabens. Sie stellen keinen Nachweis über eine eingetragene Gesellschaft, eine Banklizenz, eine regulatorische Zulassung oder eine Zugehörigkeit zu staatlichen beziehungsweise internationalen Finanzinstitutionen dar.

### B. Empfänger und Antragsgegenstand

**An:** Corporate Partnerships / Institutional Relations / Crypto Infrastructure / Exchange Partnerships / Wallet Services / Business Development

**Betreff:** Corporate- und Technologiepartnerschaftsanfrage – GlobalCards Bank | Crypto Exchange, Wallet Infrastructure, Digital Assets, Fiat On-/Off-Ramps und Blockchain Settlement

### C. Formelle Vorstellung

Sehr geehrte Damen und Herren,

hiermit möchte ich mein Interesse an einer möglichen institutionellen, technischen und kommerziellen Zusammenarbeit im Bereich digitaler Vermögenswerte, Blockchain-basierter Finanzinfrastruktur, Wallet-Technologien und regulierter Kryptowerte-Dienstleistungen zum Ausdruck bringen.

Unter der vorläufigen Projektbezeichnung **GlobalCards Bank** bereite ich die Konzeption einer modularen internationalen Finanztechnologieplattform für Privatkunden (B2C) und Geschäftskunden (B2B) vor.

Das Vorhaben soll traditionelle Bank- und Zahlungsdienstleistungen mit geeigneten digitalen Finanztechnologien verbinden. Hierzu werden insbesondere sichere Wallet-Infrastrukturen, regulierte Krypto-Handelspartner, Fiat-/Crypto-Konvertierung, Blockchain-Transfers, Settlement-Verfahren und technische Verwahrmodelle untersucht.

Ziel ist die Entwicklung einer skalierbaren, API-basierten Infrastruktur, die verschiedene regulierte Anbieter über definierte und kontrollierte Schnittstellen integrieren kann.

Da der rechtliche Gesellschaftsstatus sowie etwaige zukünftige Erlaubnisse derzeit noch nicht abschließend feststehen, erfolgt diese Kontaktaufnahme ausdrücklich als unverbindliche Anfrage zu Partnereignung, Integrationsmöglichkeiten und regulatorischen Voraussetzungen.

### D. Geschäftsmodell und strategische Zielsetzung

**Projekt:** GlobalCards Bank\
**Betriebsmodell:** Hybride internationale Finanztechnologieplattform\
**Zielgruppen:** Privat- und Geschäftskunden\
**Technisches Modell:** Modulare API-Architektur mit eigenem Integrationskern und externen regulierten Partnern\
**Ausgangsmarkt:** Deutschland und EWR

Die Plattform soll perspektivisch folgende Bereiche verbinden:

1. Banking-as-a-Service und Konteninfrastruktur
2. Fiat-Zahlungsverkehr und IBAN-Integration
3. Digitale Wallets und kryptografische Identität
4. Kryptowertetransfers
5. Regulierte Handels- und Exchange-Dienstleistungen über berechtigte Partner
6. Fiat-/Crypto-On-/Off-Ramps
7. Digital-Asset-Custody-Integration
8. Multi-Currency- und Treasury-Funktionen
9. Blockchain-Transaktionsüberwachung
10. Clearing, Ledger und Settlement-Reconciliation
11. Corporate- und institutionelle APIs
12. Regulatorische Compliance- und Nachweisführung

Nicht alle genannten Funktionen sollen zwangsläufig im ersten Produktumfang angeboten werden. Jede Dienstleistung wird vor einer möglichen Aktivierung hinsichtlich ihrer rechtlichen Zulässigkeit, wirtschaftlichen Tragfähigkeit und technischen Sicherheit geprüft.

### E. Angefragte Partnerschaftsmodelle

**Modell A – Regulierter Crypto-Asset Service Provider**

Zusammenarbeit mit einem Anbieter, der die für seine Leistungen erforderlichen Erlaubnisse besitzt und entsprechende Dienstleistungen innerhalb seines genehmigten Umfangs anbietet.

Mögliche Leistungen:

- Verwahrung und Verwaltung von Kryptowerten
- Krypto-Transfers
- Handel oder Tausch von Kryptowerten
- Ausführung beziehungsweise Weiterleitung von Orders
- Institutionelle Konten und Wallet-Infrastruktur

**Modell B – Wallet Infrastructure Provider**

Technische Integration von Wallet- und Digital-Asset-Infrastruktur, darunter:

- Kundenseitige Wallet-Oberflächen
- Blockchain-Adressen und Wallet-Referenzen
- Wallet-Lifecycle-Management
- Sichere Transaktionssignierung durch autorisierte Komponenten
- Multi-Chain-Anbindungen, soweit unterstützt
- Technische Verwaltung von Transaktionsstatus

Dabei soll zwischen selbstverwahrten Wallets und der Verwahrung von Kundenwerten durch einen Dienstleister unterschieden werden.

**Modell C – Crypto Exchange / Trading Partner**

Anbindung an geeignete regulierte Handelsplattformen oder Handelsdienstleister zur Prüfung von:

- Marktdaten und Preisabfragen
- Orderrouting
- Handelsausführung über berechtigte Partner
- Liquiditätsanbindung
- Handelsbestätigungen
- Gebühreninformationen
- Handels- und Risikoberichten

**Modell D – Fiat On-/Off-Ramp**

Zusammenarbeit mit regulierten Anbietern zur Prüfung von:

- SEPA- und Bankkontoanbindungen
- Fiat-zu-Krypto-Transaktionen
- Krypto-zu-Fiat-Transaktionen
- Auszahlungen auf berechtigte Bankkonten
- Transaktionskontrollen und Zahlungsabgleich
- Transparenter Preis- und Gebührenberechnung

**Modell E – Custody & Institutional Infrastructure**

Integration geeigneter Verwahr- und institutioneller Infrastrukturdienstleister mit besonderem Augenmerk auf sichere Schlüsselverwaltung, Zugangskontrollen, Verfügbarkeit und Nachvollziehbarkeit.

**Modell F – Technical Developer / Sandbox Partnership**

Bereitstellung von API-Dokumentation, synthetischen Testumgebungen, Integrationsunterstützung, Webhooks und technischen Zertifizierungsverfahren.

### F. Geplante Wallet-Funktionen

GlobalCards möchte unterschiedliche Wallet-Modelle technisch evaluieren.

**1. Non-Custodial Wallet**

- Kundenseitig kontrollierte Schlüssel
- Sichere Erstellung und Nutzung von Wallet-Adressen
- Lokale Signaturmechanismen
- Transaktionsvorschau
- Netzwerk- und Gebühreninformationen
- Integrationsmöglichkeiten mit Hardware-Wallets

**2. Custodial Wallet über regulierte Partner**

- Verwahrung im zulässigen Partner-Modell
- Wallet- und Bestandsreferenzen
- Transaktionsfreigaben
- Trennung von Kundengütern
- Sichere Schlüsselverwaltungsarchitektur
- Reconciliation und Reporting

**3. Business Wallet**

- Geschäftskunden- und Mandantentrennung
- Rollenbasierte Freigaben
- Transaktionslimits
- Mehrpersonen-Freigabeverfahren
- API-basierte Reporting-Funktionen
- Kontrollierte Treasury-Workflows

Die technische Gestaltung ist nicht als Festlegung der regulatorischen Einstufung zu verstehen. Insbesondere darf ein nominell selbstverwahrtes Modell nicht dazu verwendet werden, tatsächlich bestehende Verwahr- oder andere erlaubnispflichtige Dienstleistungen falsch einzuordnen.

### G. Handels- und Exchange-Funktionen

Für mögliche künftige Integrationen werden folgende Komponenten untersucht:

- Trading- und Market-Data-APIs
- Order Books und Liquiditätsinformationen
- Kauf- und Verkaufstransaktionen
- Orderverwaltung und Statusverfolgung
- Spot-Handel über berechtigte Anbieter
- Handels- und Ausführungsberichte
- Risiko- und Limitverwaltung
- Gebühren- und Spread-Transparenz
- Marktmissbrauchsprävention
- Abgleich von Handels- und Settlement-Daten

**Der eigenständige Betrieb einer Kryptohandelsplattform wird nicht als bereits genehmigt oder betriebsbereit dargestellt.**

Derivate, Margin Trading, Kreditvergabe, Anlageberatung und Portfolioverwaltung werden nicht automatisch vom angefragten Spot-/Wallet-Integrationsmodell umfasst. Sie bedürfen einer gesonderten Produkt- und Erlaubnisprüfung.

### H. Blockchain-Transfers und Settlement

Für die technische Infrastruktur ist die Entwicklung einer nachvollziehbaren Transfer- und Reconciliation-Schicht vorgesehen.

Geplante Funktionsbereiche:

1. Verwaltung von Transferanforderungen
2. Blockchain-Netzwerkauswahl
3. Berechnung beziehungsweise Anzeige anfallender Netzwerkgebühren
4. Prüfung von Empfängeradressen und Netzwerkkompatibilität
5. Einbindung erforderlicher AML- und Sanktionskontrollen
6. Autorisierung durch zuständige Personen oder Systeme
7. Verarbeitung durch einen berechtigten Transfer- oder Verwahrpartner
8. Überwachung des Blockchain-Transaktionsstatus
9. Überprüfung des erforderlichen Finalitätsniveaus
10. Buchungs- und Bestandsabgleich
11. Ausnahme- und Fehlerbearbeitung
12. Auditierbare Nachweisführung

Eine im Blockchain-Netzwerk bestätigte Transaktion wird nicht mit einer rechtswirksamen Erfüllung sämtlicher vertraglicher, finanzieller oder regulatorischer Verpflichtungen gleichgesetzt.

### I. Tokenisierung und Stablecoins

Optional sollen folgende Bereiche in einer späteren Entwicklungsphase rechtlich und technisch bewertet werden:

- Nutzung zugelassener oder anderweitig rechtmäßig angebotener Stablecoins
- Integration von E-Geld-Token-Dienstleistungen über berechtigte Partner
- Tokenisierte Zahlungs- und Settlement-Prozesse
- Tokenisierte Vermögenswerte
- Smart-Contract-basierte Verwaltungsfunktionen
- Institutionelle Wallet- und Governance-Modelle

Die eigene Emission von E-Geld-Token, vermögenswertreferenzierten Token oder tokenisierten Wertpapieren ist ausdrücklich nicht Bestandteil einer bereits genehmigten Tätigkeit.

Etwaige Tokenemissionen würden eine eigenständige rechtliche und regulatorische Prüfung erfordern.

### J. Technische Integrationsarchitektur

Für GlobalCards sind unter anderem folgende Module vorgesehen:

1. Identity & Access Management
2. Customer / Organization Management
3. KYC / KYB Integration
4. Wallet Gateway
5. Digital Asset Custody Adapter
6. Blockchain Network Connector
7. Exchange API Adapter
8. Market Data Service
9. Order Management Integration
10. Fiat On-/Off-Ramp Gateway
11. Payment & Banking Connector
12. Double-Entry Ledger
13. Crypto Transfer Orchestrator
14. Settlement & Reconciliation Engine
15. AML / Sanctions / Blockchain Monitoring
16. Compliance Evidence Registry
17. Risk & Fraud Monitoring
18. Corporate Treasury Interface
19. B2C Web / Mobile Interface
20. B2B Administration Portal

Die Architektur ist als modulare Integrationsplattform geplant und setzt auf versionierte Schnittstellen, sichere Authentifizierung, differenzierte Berechtigungen und nachvollziehbare Transaktionsprozesse.

### K. Sicherheitsanforderungen

Die technische Planung sieht insbesondere folgende Sicherheitsbereiche vor:

- Trennung von Kunden-, Geschäfts- und Administrationsbereichen
- Verschlüsselung sensibler Daten
- HSM-/MPC-gestützte Schlüsselverwaltung, soweit geeignet
- Mehrfaktor- und phishingresistente Authentifizierung
- Rollenbasierte Zugriffssteuerung
- Mehrstufige Transaktionsfreigaben
- Sichere API-Authentifizierung
- Schutz vor Replay- und Duplicate-Transaktionen
- Smart-Contract- und Dependency-Prüfungen
- Getrennte Test- und Produktivumgebungen
- Incident Response und Wiederherstellungsverfahren
- Audit-Protokollierung und technische Nachweisführung
- Lieferketten- und Softwareintegritätsprüfung

Produktive private Schlüssel, Seed-Phrasen oder andere kryptografische Geheimnisse sollen nicht in Antragsformularen, allgemeinen Logs oder ungeschützten KI-Systemen verarbeitet werden.

### L. Regulatorik und Compliance

Vor einer operativen Umsetzung sollen insbesondere folgende Rechtsbereiche geprüft werden:

- MiCAR und nationale Durchführungsvorschriften
- Erforderliche CASP-Zulassungen
- Geldwäscheprävention und KYC/KYB
- EU-Transfer-of-Funds-Regulation und Travel Rule
- Sanktions- und Embargovorschriften
- Datenschutz-Grundverordnung
- DORA, soweit anwendbar
- Marktmissbrauchs- und Handelsplattformregeln
- Verbraucherschutz und Kundeninformationen
- Steuerliche Informations- und Meldepflichten
- Wallet- und Kryptoverwahrregeln
- Gesellschafts- und Finanzdienstleistungsrecht
- Je nach Produkt MiFID II, Wertpapier- und Zahlungsdiensterecht

Die konkrete rechtliche Anwendbarkeit hängt von der tatsächlichen Art der Dienstleistung, vom Sitz des verantwortlichen Unternehmens, von der Kundenregion und von den vertraglichen Rollen der jeweiligen Partner ab.

Eine bestehende Erfüllung dieser Anforderungen oder eine bereits erteilte regulatorische Zulassung wird nicht behauptet.

### M. Gewünschte Corporate- und Developer-Zugänge

Ich bitte um Prüfung folgender Möglichkeiten:

1. Corporate-Partnerregistrierung
2. Institutional Client Onboarding
3. Developer-Portal-Zugang
4. Sandbox- und Testnet-Zugänge
5. Wallet API und Custody API
6. Exchange API und Marktdatenzugang
7. Fiat On-/Off-Ramp API
8. Bereitstellung technischer SDKs
9. Informationen zu Blockchain-Netzwerken
10. Security- und Signaturintegrationen
11. Informationen zu institutioneller Liquidität
12. Travel-Rule- und AML-Integrationsmöglichkeiten
13. Sandbox-Dokumentation für Transfers und Settlement
14. Technische Zertifizierungs- und Produktionsvoraussetzungen
15. Partner-, Reseller- und White-Label-Modelle

Ein kostenloser Entwicklungs- oder Sandbox-Zugang wäre für die erste technische Machbarkeitsprüfung besonders hilfreich, sofern dieser angeboten wird.

### N. Kommerzielle und wirtschaftliche Anforderungen

Ich bitte um Informationen zu:

- Corporate-Onboarding-Gebühren
- Mindestanforderungen an registrierte Unternehmen
- Notwendigen Genehmigungen und Zulassungen
- API-Zugangs- und Plattformgebühren
- Wallet- und Custody-Gebühren
- Handels- und Konvertierungsgebühren
- Netzwerk- und Blockchain-Transaktionsgebühren
- Mindestvolumina und Mindestumsätzen
- Liquiditäts- und Prefunding-Anforderungen
- Sicherheitsleistungen und Sicherheiten
- Versicherungs- beziehungsweise Haftungsregelungen
- Service-Level-Agreements
- Datenexport- und Migrationsverfahren
- Kündigungs- und Exit-Bedingungen

Aktuelle Kunden-, Handels-, Wallet- und Transaktionsvolumina werden nicht angegeben, da für diese Erstkontaktaufnahme keine entsprechenden verifizierten Angaben vorliegen.

### O. Verantwortlichkeiten und Partnerprüfung

Für eine mögliche Partnerschaft sollen insbesondere folgende Fragen geklärt werden:

1. Welche Gesellschaft ist regulatorischer Leistungserbringer?
2. Welche konkreten Kryptowerte-Dienstleistungen sind durch ihre Zulassung gedeckt?
3. In welchen Ländern dürfen die Dienstleistungen angeboten werden?
4. Wer ist rechtlicher Verwahrer von Kundenwerten?
5. Wer kontrolliert die für Kundentransaktionen maßgeblichen privaten Schlüssel?
6. Wie erfolgt die Trennung von Kunden- und Unternehmensvermögen?
7. Wer ist für AML, Travel Rule, Sanktionsprüfung und Transaktionsmonitoring verantwortlich?
8. Welche Haftung gilt bei Verlust, technischen Ausfällen oder Sicherheitsvorfällen?
9. Welche Funktionen darf GlobalCards als technischer Dienstleister eigenständig betreiben?
10. Welche zusätzlichen Genehmigungen wären für einen eigenen regulierten Betrieb erforderlich?

### P. Erklärung zum Gesellschafts- und Zulassungsstatus

Zum Zeitpunkt dieser Anfrage wird ausdrücklich nicht behauptet, dass GlobalCards:

- eine eingetragene oder zugelassene Bank ist,
- ein lizenzierter Crypto-Asset Service Provider ist,
- eine eigene Kryptobörse rechtmäßig betreibt,
- Kundengelder oder Kryptowerte bereits reguliert verwahrt,
- eine Fiat-/Crypto-Handelslizenz besitzt,
- eine eigene Stablecoin-Emissionsgenehmigung erhalten hat,
- über vorhandene Börsen- oder Clearing-Mitgliedschaften verfügt,
- vertraglich bestätigte Partnerschaften mit bestimmten Crypto-Dienstleistern besitzt,
- Garantien von Staaten oder internationalen Finanzinstitutionen erhalten hat.

Die vorliegende Anfrage dient ausschließlich der Prüfung einer möglichen künftigen geschäftlichen und technischen Zusammenarbeit.

Sie stellt keine Order, kein öffentliches Tokenangebot, keine Anlageempfehlung, keinen formellen Lizenzantrag und keine Beauftragung regulierter Finanzdienstleistungen dar.

### Q. Datenschutz und Vertraulichkeit

Ich bitte um eine vertrauliche und zweckgebundene Behandlung der übermittelten Kontakt- und Projektinformationen im Rahmen der geltenden Datenschutzvorschriften.

Vertrauliche Unternehmensunterlagen, Kundenidentifikationsdaten, Wallet-Geheimnisse, Produktionszugangsdaten oder technische Sicherheitsdokumentationen sollen erst nach gesonderter Prüfung und über geeignete sichere Kommunikationswege ausgetauscht werden.

### R. Gewünschter nächster Schritt

Ich würde mich freuen, wenn Ihre Organisation die grundsätzliche Eignung des Vorhabens für eine Corporate-, Wallet-, Exchange- oder Infrastrukturpartnerschaft prüfen könnte.

Besonders hilfreich wären:

- Der zuständige Corporate- oder Institutional-Onboarding-Kontakt
- Informationen zur erforderlichen Gesellschaftsform
- Eine Übersicht der regulatorischen Voraussetzungen
- Ein direkter Developer-/Sandbox-Zugang
- Angaben zu geeigneten Wallet-, Exchange- und Custody-APIs
- Eine Übersicht über unterstützte Länder und Dienstleistungen
- Kommerzielle Konditionen und erforderliche Mindestvolumina
- Informationen über die nächsten formellen Bewerbungsschritte

Ich strebe eine transparente, sichere und langfristig tragfähige Zusammenarbeit im Bereich internationaler Finanz- und Digital-Asset-Infrastruktur an.

Mit freundlichen Grüßen

**Daniel Pohl**\
Projektinitiator und technischer Projektkontakt

**GlobalCards Bank** – vorläufige Projektbezeichnung\
**Bra1nKy11 World Bank Eyes AeTHer** – Projekt-/Organisationsbezeichnung\
**HolyThreeKingsTreesCrowns** – zusätzliche Projektidentifikation

Detmold, Nordrhein-Westfalen, Deutschland

**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

---

**Dokumentstatus:** Unverbindliche Corporate-Erstanfrage, zur persönlichen Prüfung vorbereitet.

**Keine automatische Registrierung, keine Lizenzbeantragung, keine Transaktion, keine Vertragsannahme und keine Einreichung.**

## 2. Feldzuordnung für Crypto-, Wallet- und Exchange-Corporate-Portale

Die folgende Zuordnung ist für deinen universellen Portal-Worker vorgesehen. Sie unterscheidet belegbare Projektdaten, geplante Dienstleistungen und Felder, die erst nach einer rechtlichen oder geschäftlichen Klärung befüllt werden dürfen.

| Corporate-Portal-Feld (EN)     | GlobalCards-Eintrag                                        | Verarbeitungsregel                                  |
| ------------------------------ | ---------------------------------------------------------- | --------------------------------------------------- |
| First Name                     | Daniel                                                     | Übernehmen                                          |
| Last Name                      | Pohl                                                       | Übernehmen                                          |
| Contact Email                  | world.banks.eyes.aether\@globedynamicz.statesflowwishes.eu | Übernehmen                                          |
| Job Title                      | Project Initiator / Technical Project Contact              | Keine Geschäftsführerstellung behaupten             |
| Project Name                   | GlobalCards Bank                                           | Vorläufige Projektbezeichnung                       |
| Organization Designation       | Bra1nKy11 World Bank Eyes AeTHer                           | Keine registrierte Firma behaupten                  |
| Legal Company Name             | Nicht bestätigt                                            | Formellen Antrag blockieren                         |
| Legal Entity Type              | Nicht bestätigt                                            | Manuell prüfen                                      |
| Registration Number            | Nicht bereitgestellt                                       | Nicht erfinden                                      |
| Registered Office              | Nicht bestätigt                                            | Kontaktort nicht als Firmensitz übernehmen          |
| Contact City                   | Detmold                                                    | Übernehmen                                          |
| Country                        | Germany                                                    | Übernehmen                                          |
| LEI                            | Nicht bereitgestellt                                       | Nicht erfinden                                      |
| Corporate Website              | Nicht bereitgestellt                                       | Offenlassen                                         |
| Industry                       | Fintech / Digital Asset Infrastructure                     | Übernehmen                                          |
| Business Model                 | Hybrid B2C/B2B Fintech Platform                            | Als geplantes Modell                                |
| Development Stage              | Concept / Technical Preparation                            | Übernehmen                                          |
| Partnership Type               | Crypto / Wallet / Exchange Integration                     | Übernehmen                                          |
| Regulatory Jurisdiction        | Germany / EEA                                              | Geplante Zielregion                                 |
| CASP License Number            | Nicht nachgewiesen                                         | Nicht erfinden                                      |
| Regulatory Authority           | BaFin – mögliche zuständige Aufsicht                       | Nicht als bestehende Zulassungsbehörde darstellen   |
| Existing Exchange Membership   | Nicht nachgewiesen                                         | Nicht behaupten                                     |
| Custody Model                  | Noch nicht festgelegt                                      | Partnerabhängig prüfen                              |
| Wallet Type                    | Custodial / Non-Custodial – under evaluation               | Keine bestehende Bereitstellung behaupten           |
| Digital Asset Networks         | Noch nicht ausgewählt                                      | Nicht automatisch festlegen                         |
| Exchange Integration           | Requested                                                  | Anfrage                                             |
| Crypto Asset Transfer          | Planned / Under Evaluation                                 | Als geplant kennzeichnen                            |
| Fiat On-Ramp                   | Requested                                                  | Keine aktive Zahlungsdienstleistung behaupten       |
| Fiat Off-Ramp                  | Requested                                                  | Keine aktive Auszahlung behaupten                   |
| Stablecoin Integration         | Under Evaluation                                           | Keine eigene Emissionsberechtigung behaupten        |
| Trading Products               | Spot – under evaluation                                    | Derivate nicht automatisch einschließen             |
| Average Monthly Trading Volume | Nicht prognostiziert                                       | Keine Zahl erfinden                                 |
| Assets Under Custody           | Keine verifizierten Angaben                                | Nicht erfinden                                      |
| Expected Wallet Users          | Nicht prognostiziert                                       | Offenlassen                                         |
| Source of Funds                | Nicht für eine juristische Person dokumentiert             | Bei erforderlicher Prüfung echte Nachweise einholen |
| UBO / Beneficial Owners        | Nicht bereitgestellt                                       | Nicht ableiten                                      |
| AML Officer                    | Nicht bestätigt                                            | Keine Besetzung behaupten                           |
| Technical API Integration      | Requested                                                  | Übernehmen                                          |
| Sandbox / Testnet Access       | Requested                                                  | Übernehmen                                          |
| Production Access              | Nicht genehmigt                                            | Keine Produktionsfreigabe behaupten                 |
| Authorized Signatory           | Nicht bestätigt                                            | Vor verbindlichem Antrag prüfen                     |

### 3. Partnerspezifische Zusatzfelder

| Partnerkategorie      | Zusätzlich benötigte Angaben                                                                           |
| --------------------- | ------------------------------------------------------------------------------------------------------ |
| Crypto Exchange       | Handelsmodell, Spot/Derivate, Zielmärkte, Orderrouting, Kundenklassifizierung                          |
| Custody Provider      | Schlüsselkontrolle, Kundengütertrennung, Wallet-Governance, Recovery-Konzept                           |
| Wallet Infrastructure | Custodial/Non-Custodial, Chain-Unterstützung, Transaktionssignierung, technische Sicherheitsgrenzen    |
| Fiat On-/Off-Ramp     | Zahlungspartner, Kontomodell, Fiat-Währungen, Abwicklung, AML-Zuständigkeit                            |
| Liquidity Provider    | Erwartete Handelsvolumina, Ausführung, Sicherheiten, Settlement und Kreditrisiken                      |
| Stablecoin Provider   | Emittent, Tokenkategorie, rechtlicher Status, Einlösung, unterstützte Netzwerke                        |
| Regulator / BaFin     | Rechtsträger, Geschäftsleiter, Geschäftsplan, Kapitalausstattung, Organisations- und Kontrollnachweise |

Für einen förmlichen MiCAR-Antrag verlangt Artikel 62 unter anderem Angaben zu Rechtsträger, LEI, Geschäftsprogramm, Geschäftsleitern, Schutz von Kundengeldern und -kryptowerten sowie – je nach Tätigkeit – Verwahr- oder Handelsplattformregeln. Die BaFin weist ausdrücklich darauf hin, dass unvollständige Anträge abgelehnt werden können und das Verfahren gebührenpflichtig ist.&#x20;



European Securities and Markets Authority+1



## 4. Kurzfassung für Online-Corporate-Portale

**Corporate Crypto / Wallet / Exchange Partnership Request – GlobalCards Bank**

Ich interessiere mich als Projektinitiator von GlobalCards Bank für eine mögliche technische und institutionelle Zusammenarbeit im Bereich digitaler Wallets, Kryptowerte-Dienstleistungen, regulierter Exchange-Infrastruktur, Fiat-/Crypto-On-/Off-Ramps und Blockchain-basierter Zahlungs- und Settlement-Prozesse.

GlobalCards ist als hybride internationale B2C-/B2B-Finanztechnologieplattform geplant, die traditionelle Banking- und Zahlungsinfrastrukturen mit geeigneten Blockchain- und Digital-Asset-Technologien verbinden soll.

Im Vordergrund stehen die Evaluierung von Wallet- und Exchange-APIs, sichere Transaktionsverarbeitung, institutionelle Verwahrpartner, Compliance-Integrationen sowie die Möglichkeit einer technischen Sandbox-Anbindung.

Der geplante Ausgangsmarkt ist Deutschland/EWR. Das Projekt befindet sich in der Konzeption und technischen Vorbereitung. Der rechtliche Gesellschaftsstatus ist noch nicht bestätigt; es werden keine bestehenden CASP-, Banking-, Exchange- oder Custody-Lizenzen beansprucht.

Ich bitte um Informationen zu Ihren Corporate-Onboarding-Verfahren, Developer-/Sandbox-Zugängen, API-Dokumentationen, regulatorischen Voraussetzungen und kommerziellen Partnermodellen.

**Kontakt:** Daniel Pohl\
**Projekt:** GlobalCards Bank – vorläufige Projektbezeichnung\
**Weitere Projektbezeichnung:** Bra1nKy11 World Bank Eyes AeTHer\
**Standort:** Detmold, Nordrhein-Westfalen, Deutschland\
**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

Diese Anfrage ist unverbindlich und stellt weder einen formellen Lizenzantrag noch die Beauftragung einer Handels-, Verwahr- oder Zahlungsdienstleistung dar.

## 5. Separate Freigabe-Checkliste

Diese Checkliste ist für die persönliche Prüfung vor einer eventuellen Einreichung bestimmt. Das Abhaken bewirkt weder eine Registrierung noch eine rechtsverbindliche Erklärung.

Crypto Partnership – Freigabestatus

0 / 16

A. Corporate- und Rechtsstatus

Kontakt- und Projektidentität sind korrekt.

Der Gesellschaftsstatus ist als unbestätigt gekennzeichnet.

Es werden keine CASP-, Bank-, Exchange- oder Custody-Lizenzen behauptet.

Gesetzliche Vertretung und Zeichnungsberechtigung werden nicht vorausgesetzt.

B. Exchange, Wallet und Custody

Custodial und Non-Custodial Wallets sind korrekt unterschieden.

Handel, Orderrouting und Plattformbetrieb sind getrennt dargestellt.

Es werden keine tatsächlichen Handels-, Kunden- oder Verwahrvolumina erfunden.

Fiat On-/Off-Ramp und Stablecoin-Emission werden nicht als genehmigt dargestellt.

C. Compliance und Sicherheit

Die MiCAR-Einstufung des Geschäftsmodells ist als Prüfpunkt aufgenommen.

AML, Travel Rule und Sanktionsprüfung sind berücksichtigt.

Es werden keine privaten Schlüssel, Seed-Phrasen oder Produktionszugänge übermittelt.

Das konkrete Empfängerportal und seine Datenschutzbedingungen sind geprüft.

D. Einreichung und Freigabe

Der zuständige Corporate- oder Institutional-Ansprechpartner ist ausgewählt.

Alle Pflichtfelder enthalten belegbare Daten oder sind zur Klärung markiert.

Gebühren, Nutzungsbedingungen und Vertragsbindungen wurden geprüft.

Der konkrete Antrag wurde vor der Übermittlung persönlich freigegeben.

16 Prüfpunkte noch offen.

&#x20;Freigabe-Checkliste kopieren

## 6. Verbindliche Steuerungsregeln für den Portal-Worker

| Prozesszustand              | Zulässige automatische Funktion                                                                  |
| --------------------------- | ------------------------------------------------------------------------------------------------ |
| `PROFILE_LOADED`            | Bekannte Projekt- und Kontaktdaten aus geschütztem Profil laden                                  |
| `CRYPTO_PARTNER_CLASSIFIED` | Exchange, Custody, Wallet, Ramp oder Infrastrukturpartner unterscheiden                          |
| `SERVICE_SCOPE_MAPPED`      | Relevante Kryptowerte-Dienstleistungen zuordnen                                                  |
| `CASP_LICENSE_CHECK`        | Zulassung und konkrete genehmigte Dienstleistungen des Partners prüfen                           |
| `LEGAL_ENTITY_CHECK`        | Gesellschaftsdaten, UBO und Zeichnungsberechtigung validieren                                    |
| `WALLET_CUSTODY_CHECK`      | Kontrolle über Schlüssel und Kundenwerte technisch/rechtlich prüfen                              |
| `AML_TRAVEL_RULE_CHECK`     | Einzuhaltende Übermittlungs-, Prüf- und Dokumentationspflichten zuordnen                         |
| `FIELD_MAPPING`             | Freigegebene Angaben in das Zielportal übertragen                                                |
| `DUPLICATE_CHECK`           | Doppelanfragen und frühere Entwürfe erkennen                                                     |
| `DRAFT_READY`               | Antrag zur Prüfung vorbereiten                                                                   |
| `HUMAN_REVIEW_REQUIRED`     | Fehlende Nachweise, Risiken und offene Pflichtfelder anzeigen                                    |
| `SUBMISSION_LOCKED`         | Keine Registrierung, Einreichung, Vertragsannahme oder Transaktion ohne gesonderte Autorisierung |

Der Worker soll außerdem prüfen, ob die beanspruchte Dienstleistung tatsächlich von der Zulassung eines potenziellen Partners abgedeckt wird. Dafür steht das offizielle ESMA-Register zugelassener CASPs zur Verfügung.&#x20;



ESMA



## 7. Offizielle regulatorische Prüf- und Antragsressourcen

| Institution                  | Direkter Fachzugang                                                                                                                                                                                                                                                                   | Zweck                                                      |
| ---------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- |
| BaFin                        | [MiCAR-Zulassung und Antragsvoraussetzungen](https://bafin.de/DE/unternehmen-maerkte/erlaubnis-registrierung/geschaefte-krypto/kryptowerte-dienstleistungen/kryptowerte-dienstleistungen.html)                                                                 | Deutsche CASP-Zulassung, Unterlagen, Gebühren, Passporting |
| ESMA                         | [MiCAR-Register und regulatorische Informationen](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica)                                                                                            | Zugelassene CASPs und weitere Registerinformationen        |
| ESMA – Artikel 62            | [Gesetzliche Inhalte eines CASP-Antrags](https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-62-application-authorisation-crypto)                                                                                        | Nachweise und Pflichtangaben einer formellen Zulassung     |
| EBA                          | [Travel-Rule-Leitlinien](https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/anti-money-laundering-and-countering-financing-terrorism/guidelines-information-requirements-relation-transfers-funds-and-certain-crypto-assets-transfers) | Anforderungen an Angaben bei bestimmten Kryptotransfers    |
| Bundeszentralamt für Steuern | [Registrierung für bestimmte Kryptowerte-Betreiber](https://online.portal.bzst.de/SharedDocs/Leistungsbeschreibung/DE/registrierung_kryptowerte_betreiber.html)                                                                                                | DAC8/CARF-Meldeverfahren, soweit einschlägig               |

Die EBA-Leitlinien zur Travel Rule gelten seit dem 30. Dezember 2024 und behandeln unter anderem fehlende Angaben bei Kryptotransfers sowie Transfers mit selbst gehosteten Adressen. Die steuerlichen DAC8/CARF-Verfahren sind von einer aufsichtsrechtlichen CASP-Zulassung zu unterscheiden.&#x20;



European Banking Authority+1



## 8. Empfohlene erste Antragsart

Für den aktuellen Status von GlobalCards würde ich die Anfragen in dieser Reihenfolge vorbereiten:

1. Wallet- und Custody-Technologiepartner: Zugang zu Testnet, Sandbox, Wallet-APIs und technischen Sicherheitsmodellen.
2. Bereits regulierte CASP- und Exchange-Partner: Prüfung eines zulässigen Partner- oder Vermittlungsmodells, ohne automatisch anzunehmen, dass GlobalCards selbst erlaubnisfrei wäre.
3. Fiat On-/Off-Ramp-Partner: Zahlungs- und Bankkontoanbindung, EUR-Abwicklung, AML- und Travel-Rule-Verantwortung.
4. Liquiditäts- und Settlement-Partner: Preisstellung, Transaktionsabgleich, institutionelle Ausführung und Verwahrstrukturen.
5. BaFin und spezialisierte Rechtsberatung: Rechtliche Einordnung eines späteren eigenen CASP-, Handelsplattform- oder Verwahrmodells.

Ergebnis: Die deutschsprachige Corporate-Crypto-Anfrage, eine kompakte Online-Fassung, die ausführliche Portal-Feldzuordnung, die rechtliche Klassifizierungslogik und die separate Freigabe-Checkliste sind vorbereitet.

Es wurde keine Registrierung, Exchange-Anbindung, Wallet-Eröffnung, Lizenzbeantragung oder Einreichung durchgeführt. # GlobalCards Bank – Universal Crypto, Wallet & Exchange Partnership Application

Corporate Onboarding · Digital Assets · Wallet Infrastructure · Crypto Exchange · Custody · Fiat On-/Off-Ramp · Version 2.0

Antragsteller

Daniel Pohl

Projekt

GlobalCards Bank

Sprache

Deutsch

Zielmärkte

Deutschland / EWR

Gesellschaftsstatus

Nicht bestätigt

Einreichung

Nicht erfolgt

Die folgende Fassung ist für eine unverbindliche Corporate-Erstanfrage bei Kryptobörsen, Wallet-Anbietern, Custody-Dienstleistern und regulierten Finanzpartnern ausgearbeitet. Sie kann auch als Grundlage für Developer- und Sandbox-Anträge dienen.

Ein förmlicher MiCAR-Zulassungsantrag ist damit noch nicht möglich: Artikel 62 MiCAR verlangt unter anderem nachgewiesene Gesellschaftsdaten, Organisationsstrukturen, Geschäftspläne und angemessene aufsichtsrechtliche Sicherheiten.&#x20;



European Securities and Markets Authority+1



## 1. Vollständiges Corporate-Partnerschaftsanschreiben

# GLOBALCARDS BANK

## UNIVERSAL CORPORATE & INSTITUTIONAL CRYPTO, WALLET & EXCHANGE PARTNERSHIP APPLICATION

**Formelle Interessenbekundung zur Integration internationaler Kryptowerte-, Wallet-, Handels-, Verwahr- und Settlement-Infrastrukturen**

**Datum:** 7. November 2026\
**Dokumentversion:** 2.0\
**Antragsart:** Unverbindliche Corporate- und Technologiepartnerschaftsanfrage\
**Einreichungsstatus:** Entwurf zur persönlichen Freigabe

---

### A. Antragsteller und Corporate Identity

| Feld                                        | Angabe                                                                                                                        |
| ------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Ansprechpartner                             | Daniel Pohl                                                                                                                   |
| Rolle                                       | Projektinitiator und technischer Projektkontakt                                                                               |
| Projektbezeichnung                          | GlobalCards Bank                                                                                                              |
| Weitere Projekt-/Organisationsbezeichnung   | Bra1nKy11 World Bank Eyes AeTHer                                                                                              |
| Zusätzliche Projektidentifikation           | HolyThreeKingsTreesCrowns                                                                                                     |
| Kontaktstandort                             | Detmold, Nordrhein-Westfalen, Deutschland                                                                                     |
| E-Mail                                      | [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu) |
| Rechtlicher Unternehmensname                | Noch nicht bestätigt                                                                                                          |
| Gesellschaftsform                           | Noch nicht bestätigt                                                                                                          |
| Handelsregisternummer                       | Nicht bereitgestellt                                                                                                          |
| Eingetragener Gesellschaftssitz             | Noch nicht bestätigt                                                                                                          |
| Legal Entity Identifier (LEI)               | Nicht bereitgestellt                                                                                                          |
| Steuer-/Umsatzsteuer-ID der Gesellschaft    | Nicht bereitgestellt                                                                                                          |
| Eigene CASP-/MiCAR-Zulassung                | Nicht nachgewiesen; wird nicht beansprucht                                                                                    |
| Bank- oder Zahlungsinstitutslizenz          | Nicht nachgewiesen; wird nicht beansprucht                                                                                    |
| Bestehende Crypto-/Exchange-Partnerschaften | Für dieses Vorhaben nicht vertraglich bestätigt                                                                               |
| Technischer Entwicklungsstand               | Konzeption und technische Vorbereitung                                                                                        |
| Primärer Zielmarkt                          | Deutschland und Europäischer Wirtschaftsraum                                                                                  |
| Internationale Erweiterung                  | Perspektivisch, vorbehaltlich regulatorischer Freigaben                                                                       |

**Klarstellung:** Die aufgeführten Bezeichnungen sind Projektidentifikationen. Sie stellen keinen Nachweis einer eingetragenen Gesellschaft, einer staatlichen oder institutionellen Zugehörigkeit oder einer erteilten Finanzdienstleistungserlaubnis dar.

Die Verwendung des Wortes „Bank“ als spätere Geschäfts- oder Produktbezeichnung bedarf einer gesonderten rechtlichen Prüfung.

### B. Empfänger und Betreff

**An:** Corporate Partnerships / Institutional Onboarding / Digital Asset Services / Developer Relations

**Betreff:** Corporate-Partnerschaftsanfrage – GlobalCards Bank | Crypto, Wallet, Exchange, Custody, Fiat On-/Off-Ramp & Digital Asset Infrastructure

### C. Formelle Vorstellung

Sehr geehrte Damen und Herren,

hiermit bekunde ich mein Interesse an einer möglichen technischen, kommerziellen und institutionellen Zusammenarbeit mit Ihrer Organisation im Bereich digitaler Vermögenswerte, Kryptowertedienstleistungen, Wallet-Infrastruktur und internationaler Finanztechnologie.

Unter der vorläufigen Projektbezeichnung **GlobalCards Bank** bereite ich die Entwicklung einer hybriden internationalen Finanztechnologieplattform für Privatkunden (B2C) und Geschäftskunden (B2B) vor.

Das Projekt verfolgt das Ziel, klassische Finanzdienstleistungsinfrastrukturen – insbesondere Banking, Konten, Zahlungsverkehr und Kartenprogramme – mit geeigneten regulierten Digital-Asset-Dienstleistungen und Blockchain-Technologien zu verbinden.

Dabei steht die technische Integration bestehender, entsprechend berechtigter Partner im Vordergrund.

Ich möchte prüfen, welche Corporate-, Developer-, White-Label-, API- und Infrastrukturpartnerschaften Ihre Organisation für ein solches Vorhaben anbietet.

Da die endgültige Gesellschaftsstruktur und der regulatorische Betriebsumfang noch nicht feststehen, erfolgt diese Kontaktaufnahme ausdrücklich als unverbindliche Interessenbekundung und Eignungsanfrage.

### D. Geschäftsmodell und Marktstrategie

**Projekt:** GlobalCards Bank\
**Geschäftsmodell:** Hybride Banking-, Payment- und Digital-Asset-Technologieplattform\
**Kundengruppen:** Privatkunden und Geschäftskunden\
**Geografischer Start:** Deutschland / EWR\
**Langfristige Ausrichtung:** Internationale Expansion, abhängig von lokalen Genehmigungen und Partnerberechtigungen.

Das vorgesehene Modell kombiniert eigene Softwarekomponenten und standardisierte APIs mit den Dienstleistungen zugelassener Finanz- und Kryptowerte-Dienstleister.

Die geplante Plattform soll insbesondere folgende Bereiche abbilden:

1. Multi-Currency-Konten und Banking-Integration
2. Digitale Wallet-Infrastruktur
3. Kryptowerte-Verwahrung über geeignete berechtigte Partner
4. Crypto-Exchange- und Broker-Anbindungen
5. Fiat-zu-Krypto- und Krypto-zu-Fiat-Konvertierung
6. Blockchain-Transfers und Transaktionsstatus
7. Zahlungs- und Settlement-Reconciliation
8. Institutionelle Treasury- und Reporting-Funktionen
9. KYC-/KYB-, AML- und Sanktionsprüfung
10. Corporate- und Developer-APIs

Nicht alle Funktionen sind für die erste Entwicklungsphase vorgesehen. Die rechtliche Klassifizierung und Freigabe erfolgt je Produkt und Jurisdiktion gesondert.

### E. Angefragte Partnerschaftsmodelle

**1. Regulated Crypto-Asset Service Provider Partnership**

Prüfung einer Zusammenarbeit mit einem entsprechend zugelassenen Anbieter zur technischen Integration der in seiner jeweiligen Zulassung enthaltenen Kryptowerte-Dienstleistungen.

**2. Digital Wallet Infrastructure Partnership**

Integration von Wallet-Schnittstellen, Blockchain-Adressen, Transaktionsstatus, technischer Signierung und Wallet-Management.

**3. Digital Asset Custody Partnership**

Prüfung institutioneller Verwahrmodelle einschließlich sicherer Schlüsselverwaltung, Mandantentrennung, Zugriffsrechten, Recovery-Verfahren und Audit-Nachweisen.

**4. Crypto Exchange & Brokerage Integration**

Anbindung an regulierte Handelsdienstleister für Preisabfragen, Handelsinformationen, Orderübermittlung und Transaktionsstatus, soweit rechtlich und vertraglich zulässig.

**5. Fiat On-/Off-Ramp Partnership**

Integration berechtigter Zahlungs- und Konvertierungsdienstleister für den Übergang zwischen Fiatgeld und Kryptowerten, einschließlich möglicher SEPA-Anbindung.

**6. Technical Developer & Sandbox Partnership**

Zugang zu Entwicklerdokumentation, technischen Testumgebungen, SDKs, Webhooks und Integrationsunterstützung.

### F. Geplante Wallet-Funktionen

Die Plattform soll unterschiedliche technische Wallet-Modelle untersuchen:

**Non-Custodial Wallets**

- Kundenseitig kontrollierte Schlüssel
- Blockchain-Adressverwaltung
- Transaktionssignierung durch berechtigte Nutzer
- Hardware-Wallet-Kompatibilität
- Netzwerk- und Gebühreninformationen

**Custodial Wallets über berechtigte Partner**

- Sichere Verwaltung von Wallet-Referenzen
- Transaktionsfreigaben
- Trennung von Kundenvermögen
- Partnerabhängige Verwahrprozesse
- Bestands- und Transaktionsabgleich

**Corporate Wallets**

- Organisationen und Benutzerrollen
- Mehrstufige Freigaben
- Transaktionslimits
- Getrennte Mandanten- und Berechtigungsbereiche
- API-basierte Finanzübersichten

Die tatsächliche Kontrolle über private Schlüssel und Kundenwerte muss technisch und rechtlich dokumentiert werden. Eine bloße Bezeichnung als Non-Custodial Wallet ersetzt keine regulatorische Prüfung.

### G. Exchange- und Trading-Integration

Für die spätere Integration werden folgende Funktionen evaluiert:

- Marktpreis- und Kursdaten
- Spot-Handelsinformationen
- Ordermanagement
- Handelsausführung über berechtigte Dienstleister
- Orderstatus und Ausführungsnachweise
- Liquiditätsanbindung
- Risiko- und Limitkontrollen
- Gebühren- und Spread-Transparenz
- Settlement- und Bestandsabgleich
- Dokumentierte Marktmissbrauchsprävention

Der eigenständige Betrieb einer Kryptohandelsplattform wird nicht als bereits bestehende oder zugelassene Tätigkeit dargestellt.

Derivate, Hebelprodukte, Anlageberatung, Portfolioverwaltung und Wertpapierhandel sind nicht automatisch Bestandteil des angefragten Integrationsumfangs.

### H. Fiat Banking und Multi-Currency

GlobalCards soll eine klare Verbindung zwischen klassischem Zahlungsverkehr und regulierten Digital-Asset-Dienstleistungen ermöglichen.

Geplante Integrationsbereiche:

- EUR-Konten und IBAN-Anbindungen
- SEPA-/SEPA-Instant-Zahlungswege
- Konten- und Zahlungspartner
- Fiat-/Crypto-Konvertierungen
- Mehrwährungsdarstellungen
- Transparente Kursangebote
- Gebührenberechnung
- Auszahlungsstatus und Reconciliation
- Institutionelle Zahlungs- und Treasury-Workflows

Kontoführung, E-Geld-Ausgabe und Zahlungsdienstleistungen sollen ausschließlich durch entsprechend berechtigte Unternehmen beziehungsweise innerhalb einer tatsächlich erteilten eigenen Zulassung erbracht werden.

### I. Blockchain Transfer & Settlement

Für den technischen Zahlungs- und Transaktionsabgleich ist eine kontrollierte Settlement- und Reconciliation-Komponente vorgesehen.

Diese soll unterstützen:

1. Eindeutige Transaktionsreferenzen
2. Idempotente Auftragsverarbeitung
3. Autorisierte Transaktionsfreigaben
4. Überprüfung von Blockchain-Netzwerken
5. Adress- und Netzwerkvalidierung
6. Transaktionsstatus und Bestätigungen
7. Abgleich von On-Chain- und Partnerdaten
8. Interne Double-Entry-Buchungen
9. Fehler- und Ausnahmebearbeitung
10. Unveränderbare beziehungsweise manipulationsgeschützte Audit-Nachweise

Eine Blockchain-Bestätigung wird nicht automatisch mit endgültigem rechtlichem Settlement gleichgesetzt.

Die jeweilige Finalität hängt von Netzwerk, Vertrag, Asset-Typ, beteiligten Dienstleistern und einschlägigen Rechtsvorschriften ab.

### J. Technische Referenzarchitektur

Vorgesehene Komponenten:

- Identity & Access Management
- Customer / Organization Management
- Wallet API Gateway
- Blockchain Network Connectors
- Custody Provider Adapter
- Exchange & Market Data Adapter
- Order Routing Integration
- Fiat On-/Off-Ramp Connector
- Payment Orchestration
- Double-Entry Ledger
- Settlement & Reconciliation Engine
- AML / Sanctions / Travel Rule Integration
- Fraud & Transaction Monitoring
- Compliance Evidence Management
- Corporate Treasury Interface
- B2C Mobile / Web Application
- B2B Corporate Dashboard
- Partner Developer Portal

Technische Integrationen sollen durch sichere Authentifizierung, versionierte APIs, kontrollierte Berechtigungen, Testumgebungen und nachvollziehbare Änderungen abgesichert werden.

### K. Sicherheitsarchitektur und Datenschutz

Folgende Sicherheitsbereiche sind für die Umsetzung vorgesehen:

- Least-Privilege- und Zero-Trust-Zugriffsmodelle
- Starke Mehrfaktorauthentifizierung
- HSM-/MPC-Integration, soweit geeignet
- Kontrollierte Schlüsselverwaltung
- Rollenbasierte Transaktionsfreigaben
- API-Authentifizierung und Signaturprüfung
- Replay- und Duplikatschutz
- Trennung von Entwicklungs- und Produktivumgebungen
- Smart-Contract- und Software-Sicherheitsprüfungen
- Incident Management und Wiederherstellungsprozesse
- Dokumentierte Audit- und Compliance-Nachweise
- Datenschutz durch Datenminimierung und Zugriffskontrollen

Private Schlüssel, Seed-Phrasen, API-Secrets und echte Kundenproduktionsdaten werden nicht mit dieser Anfrage übermittelt.

### L. Regulatorische Anforderungen

Vor einer operativen Umsetzung sollen je nach Dienstleistung und Rechtsraum insbesondere folgende Vorschriften geprüft werden:

- EU Markets in Crypto-Assets Regulation (Mi# GlobalCards Bank – Corporate Crypto, Wallet & Exchange Partnership Application

\<text color="secondary" weight="medium">Universelles institutionelles Antragsformular · Version 2.1 · 7. November 2026\</text>

Das folgende Dokument ist eine vollständig formulierte **unverbindliche Corporate-Erstanfrage** für Crypto Exchanges, Wallet-Anbieter, Kryptoverwahrstellen, Fiat-On-/Off-Ramp-Dienstleister und regulierte Technologiepartner.

Die bereits bekannten Projekt- und Kontaktdaten sind eingetragen. Nicht bestätigte Gesellschafts- und Lizenzinformationen werden ausdrücklich als offen ausgewiesen, ohne fiktive Angaben zu ergänzen.

\<box border radius="lg" padding={3} gap={2}>\
&#x20; \<grid columns={2} gap={3}>\
&#x20;   \<grid-item>\
&#x20;     \<text color="secondary" size="xs">Antragsteller\</text>\
&#x20;     \*\*Daniel Pohl\*\*\
&#x20;   \</grid-item>\
&#x20;   \<grid-item>\
&#x20;     \<text color="secondary" size="xs">Projektbezeichnung\</text>\
&#x20;     \*\*GlobalCards Bank\*\*\
&#x20;   \</grid-item>\
&#x20;   \<grid-item>\
&#x20;     \<text color="secondary" size="xs">Sektor\</text>\
&#x20;     \*\*Crypto / Wallet / Exchange\*\*\
&#x20;   \</grid-item>\
&#x20;   \<grid-item>\
&#x20;     \<text color="secondary" size="xs">Zielmarkt\</text>\
&#x20;     \*\*Deutschland / EWR\*\*\
&#x20;   \</grid-item>\
&#x20;   \<grid-item>\
&#x20;     \<text color="secondary" size="xs">Gesellschaftsstatus\</text>\
&#x20;     \*\*Nicht bestätigt\*\*\
&#x20;   \</grid-item>\
&#x20;   \<grid-item>\
&#x20;     \<text color="secondary" size="xs">Einreichungsstatus\</text>\
&#x20;     \*\*Nicht eingereicht\*\*\
&#x20;   \</grid-item>\
&#x20; \</grid>\
\</box>

## 1. Vollständiges Corporate-Antragsformular

\<WritingBlock id="60417" variant="document"># GLOBALCARDS BANK

## UNIVERSAL CORPORATE & INSTITUTIONAL CRYPTO, WALLET & EXCHANGE PARTNERSHIP APPLICATION

**Formelle Interessenbekundung – Digital Assets, Wallet Infrastructure, Crypto Exchange, Custody, Fiat On-/Off-Ramps und Blockchain Settlement**

**Datum:** 7. November 2026\
**Version:** 2.1\
**Sprache:** Deutsch\
**Dokumentstatus:** Unverbindliche Erstanfrage, zur persönlichen Prüfung vorbereitet

---

### A. Antragsteller und Corporate Identity

| Angabe                                            | Information                                                                                                                   |
| ------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Ansprechpartner                                   | Daniel Pohl                                                                                                                   |
| Rolle                                             | Projektinitiator und technischer Projektkontakt                                                                               |
| Projektname                                       | GlobalCards Bank                                                                                                              |
| Weitere Projekt-/Organisationsbezeichnung         | Bra1nKy11 World Bank Eyes AeTHer                                                                                              |
| Zusätzliche Projektidentifikation                 | HolyThreeKingsTreesCrowns                                                                                                     |
| Kontaktstandort                                   | Detmold, Nordrhein-Westfalen, Deutschland                                                                                     |
| Kontakt-E-Mail                                    | [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu) |
| Rechtlicher Unternehmensname                      | Noch nicht bestätigt                                                                                                          |
| Gesellschaftsform                                 | Noch nicht bestätigt                                                                                                          |
| Eingetragener Unternehmenssitz                    | Noch nicht bestätigt                                                                                                          |
| Handelsregisternummer                             | Nicht bereitgestellt                                                                                                          |
| LEI                                               | Nicht bereitgestellt                                                                                                          |
| VAT-/Umsatzsteuer-ID der Gesellschaft             | Nicht bereitgestellt                                                                                                          |
| Bestehende CASP-/MiCAR-Zulassung                  | Nicht nachgewiesen                                                                                                            |
| Bestehende Bank-/Zahlungsinstitutslizenz          | Nicht nachgewiesen                                                                                                            |
| Bestehende Kryptoverwahr- oder Exchange-Zulassung | Nicht nachgewiesen                                                                                                            |
| Bestehende regulierte Partnerschaften             | Für dieses Vorhaben nicht bestätigt                                                                                           |
| Entwicklungsphase                                 | Konzeption und technische Vorbereitung                                                                                        |
| Zielregion                                        | Deutschland / Europäischer Wirtschaftsraum                                                                                    |
| Internationaler Ausbau                            | Geplant, vorbehaltlich der jeweiligen gesetzlichen Voraussetzungen                                                            |

**Statusklarstellung:** Die genannten Bezeichnungen sind Projektidentifikationen. Sie sind kein Nachweis eines eingetragenen Unternehmens, einer Bankzulassung, einer staatlichen Zugehörigkeit oder einer bestehenden regulatorischen Erlaubnis.

Die Bezeichnung „GlobalCards Bank“ wird ausschließlich als vorläufiger Projektname verwendet. Ihre spätere geschäftliche Nutzung bedarf einer gesonderten rechtlichen Prüfung.

### B. Empfänger und Betreff

**An:** Corporate Partnerships / Institutional Onboarding / Digital Asset Services / Developer Relations

**Betreff:** Corporate-Partnerschaftsanfrage – GlobalCards Bank | Crypto Exchange, Wallet, Custody, Fiat On-/Off-Ramps & Digital Asset Infrastructure

### C. Formelle Vorstellung

Sehr geehrte Damen und Herren,

hiermit möchte ich mein Interesse an einer möglichen technischen, institutionellen und kommerziellen Zusammenarbeit mit Ihrer Organisation im Bereich digitaler Vermögenswerte, Wallet-Infrastrukturen, Kryptowerte-Dienstleistungen und internationaler Finanztechnologien bekunden.

Unter der vorläufigen Projektbezeichnung **GlobalCards Bank** bereite ich die Konzeption einer modularen internationalen Finanztechnologieplattform für Privatkunden (B2C) und Geschäftskunden (B2B) vor.

Ziel ist es, traditionelle Finanzdienstleistungsinfrastrukturen, insbesondere Konten, Zahlungsverkehr, Kartenprogramme und Multi-Currency-Funktionen, mit geeigneten Blockchain- und Digital-Asset-Technologien zu verbinden.

Im Mittelpunkt steht zunächst die kontrollierte Integration bestehender, entsprechend berechtigter Technologie- und Finanzdienstleistungspartner.

Ich möchte daher prüfen, welche Corporate-, Institutional-, Developer-, Sandbox- und API-Partnerschaftsmodelle Ihre Organisation für ein derartiges Vorhaben anbietet.

Da die rechtliche Unternehmensstruktur und die regulatorische Einordnung des späteren Betriebsmodells noch nicht abschließend geklärt sind, erfolgt diese Kontaktaufnahme ausschließlich als unverbindliche Interessenbekundung und Eignungsanfrage.

### D. Geschäftsmodell und Produktumfang

**Projekt:** GlobalCards Bank\
**Modell:** Hybride internationale Banking-, Payments- und Digital-Asset-Technologieplattform\
**Zielgruppen:** Privatkunden und Geschäftskunden\
**Ausgangsmarkt:** Deutschland und Europäischer Wirtschaftsraum\
**Technische Ausrichtung:** API-First, modulare Integration und kontrollierte Datenverarbeitung.

Folgende Produktbereiche sollen hinsichtlich ihrer technischen und regulatorischen Umsetzbarkeit untersucht werden:

1. Digitale Wallets und Blockchain-Konnektivität
2. Kryptowerte-Verwahrung über geeignete regulierte Partner
3. Crypto Exchange und Brokerage-Integration
4. Fiat-zu-Krypto- und Krypto-zu-Fiat-Konvertierung
5. Zahlungsverkehr und IBAN-/SEPA-Anbindung
6. Digitale Assets und Multi-Currency-Reporting
7. Blockchain-Transfers und Transaktionsüberwachung
8. Institutionelle Liquiditäts- und Treasury-Anbindungen
9. Ledger, Clearing und Reconciliation
10. AML-, KYC-/KYB- und Sanktionsprüfung
11. Sichere Corporate- und Developer-APIs
12. Regulatorische Nachweis- und Governance-Funktionen

Die genannten Produktbereiche sind Entwicklungsziele und werden nicht als bereits angebotene Finanzdienstleistungen dargestellt.

### E. Gewünschte Partnerschaftsmodelle

**Modell 1 – Regulierter Crypto-Asset Service Provider**

Zusammenarbeit mit einem Dienstleister, dessen tatsächlich bestehende Zulassung die betreffenden Kryptowerte-Dienstleistungen abdeckt.

**Modell 2 – Wallet Infrastructure Provider**

Technische Integration von Wallets, Blockchain-Adressen, Transaktionssignierung, Wallet-Verwaltung und Netzwerkverbindungen.

**Modell 3 – Custody Provider**

Integration von Kryptoverwahrung, geeigneter Schlüsselverwaltung, Kundengütertrennung, Transaktionsfreigaben und Bestandsberichten über berechtigte Vertragspartner.

**Modell 4 – Crypto Exchange / Broker**

API-basierte Anbindung für Marktdaten, Orderstatus, zulässige Orderübermittlung, Ausführung und Abrechnung durch entsprechend berechtigte Unternehmen.

**Modell 5 – Fiat On-/Off-Ramp**

Zusammenarbeit zur Anbindung von Bankkonten, Zahlungsdiensten und regulierten Konvertierungsverfahren zwischen Fiatgeld und Kryptowerten.

**Modell 6 – Developer / Sandbox Partnership**

Bereitstellung von Testumgebungen, SDKs, technischen API-Spezifikationen, Webhooks und Integrationsunterstützung.

Die Frage, welche Tätigkeiten GlobalCards technisch erbringen darf und welche Dienstleistungen einem regulierten Partner vorbehalten bleiben, soll vor Aufnahme einer operativen Tätigkeit rechtsverbindlich geklärt werden.

### F. Wallet- und Custody-Infrastruktur

Die geplante technische Plattform soll unterschiedliche Wallet-Modelle evaluieren.

**Non-Custodial Wallets**

- Kundenseitige Schlüsselkontrolle
- Sichere lokale oder hardwaregestützte Transaktionssignierung
- Verwaltung öffentlicher Wallet-Adressen
- Transparente Netzwerk- und Gebühreninformationen
- Unterstützung ausgewählter Blockchain-Netzwerke nach technischer Prüfung

**Custodial Wallets**

- Verwahrung über einen entsprechend berechtigten Dienstleister
- Trennung von Kundengütern und Eigenvermögen
- Transaktionsfreigaben und Sicherheitsrichtlinien
- Kryptografische Schlüsselverwaltung
- Bestandsführung und Reconciliation
- Reporting und Nachweisführung

**Corporate Wallets**

- Mandanten- und Organisationsverwaltung
- Rollenbasierte Berechtigungen
- Mehrstufige Zahlungsfreigaben
- Transaktionslimits
- Treasury- und Finanzübersichten
- Sichere Entwickler- und Administrationsschnittstellen

Die tatsächliche Kontrolle über private Schlüssel, Zugangsmittel und Kundenwerte ist für die regulatorische Einordnung maßgeblich und soll gesondert dokumentiert werden.

### G. Crypto Exchange und Trading

Für mögliche Handelsintegrationen sollen folgende Funktionen evaluiert werden:

- Kurs- und Marktdaten-APIs
- Spot-Marktinformationen
- Ordererfassung und Orderstatus
- Ausführung über berechtigte Handelsdienstleister
- Liquiditäts- und Preisstellungsschnittstellen
- Handelslimits und Risikokontrollen
- Gebühren-, Spread- und Ausführungsinformationen
- Abgleich von Handel und Settlement
- Protokollierung und Marktüberwachung

Der eigenständige Betrieb einer Kryptohandelsplattform wird ausdrücklich nicht als bestehende oder bereits genehmigte Tätigkeit dargestellt.

Derivate, Hebelprodukte, Anlageberatung und weitere erlaubnispflichtige Finanzdienstleistungen werden nur nach gesonderter rechtlicher Prüfung betrachtet.

### H. Fiat Banking, Multi-Currency und Zahlungsverkehr

GlobalCards soll perspektivisch die technische Verbindung zwischen klassischen Zahlungsdiensten und Digital-Asset-Partnern ermöglichen.

Angefragte Integrationsbereiche:

- IBAN- und Bankkonto-Anbindungen
- SEPA- und SEPA-Instant-Zahlungen
- Fiat-/Crypto-Konvertierung
- Multi-Currency-Reporting
- Internationale Auszahlungen
- Zahlungsreferenzen und Statusinformationen
- Gebühren- und Wechselkursdarstellung
- Settlement und Transaktionsabgleich

Regulierte Konto-, E-Geld-, Zahlungs- und Konvertierungsdienstleistungen sollen nur innerhalb des jeweils rechtlich zulässigen Modells und durch entsprechend berechtigte Unternehmen bereitgestellt werden.

### I. Blockchain Settlement und Transaktionsintegrität

Die geplante Settlement- und Reconciliation-Schicht soll folgende technische Funktionen unterstützen:

1. Eindeutige Transaktionsreferenzen
2. Idempotente Verarbeitung
3. Berechtigungs- und Freigabekontrollen
4. Adress- und Netzwerkvalidierung
5. Erfassung von On-Chain-Transaktionsstatus
6. Abgleich mit externen Partnerdaten
7. Double-Entry-Ledger-Buchungen
8. Behandlung von Fehler- und Ausnahmefällen
9. Sichere Wiederherstellungsverfahren
10. Revisionsfähige Audit- und Evidenzdaten

Die Blockchain-Bestätigung einer Transaktion wird nicht automatisch mit rechtlich endgültigem Settlement gleichgesetzt.

Die rechtliche Finalität ist abhängig vom jeweiligen Asset, Netzwerk, Vertragsmodell und den beteiligten Finanzdienstleistern.

### J. Technische Referenzarchitektur

Für das Projekt sind folgende technische Module geplant:

| Modul                    | Funktion                                             |
| ------------------------ | ---------------------------------------------------- |
| Identity & Access        | Benutzer-, Rollen- und Zugriffsverwaltung            |
| Customer & Organization  | B2C-/B2B-Kundenverwaltung                            |
| KYC / KYB Integration    | Identitäts- und Organisationsprüfung                 |
| Wallet Gateway           | Wallet- und Blockchain-Schnittstellen                |
| Custody Adapter          | Integration regulierter Verwahrpartner               |
| Exchange Connector       | Markt- und Handels-APIs                              |
| Order Management Adapter | Orderstatus und berechtigte Ausführungspartner       |
| Fiat Gateway             | On-/Off-Ramp-Integration                             |
| Payment Orchestrator     | Zahlungsanweisungen und Partnerkommunikation         |
| Double-Entry Ledger      | Nachvollziehbare interne Buchungsführung             |
| Settlement Engine        | Clearing- und Reconciliation-Prozesse                |
| AML / Travel Rule        | Prüf- und Informationsaustauschprozesse              |
| Fraud & Risk             | Risiko- und Transaktionskontrollen                   |
| Compliance Evidence      | Regulatorische Nachweise                             |
| Corporate Treasury       | Institutionelle Bestands- und Liquiditätsübersichten |
| Developer API            | Kontrollierte externe Integrationen                  |

Die technische Umsetzung soll mit synthetischen Testdaten, versionierten Schnittstellen und kontrollierten Entwicklungsumgebungen beginnen.

### K. Sicherheit, Datenschutz und Governance

Geplant ist die Prüfung und Implementierung geeigneter Maßnahmen für:

- Zugriffskontrollen nach Least-Privilege-Prinzip
- Phishing-resistente Mehrfaktorauthentifizierung
- HSM-/MPC-gestützte Schlüsselverwaltung, soweit geeignet
- Kryptografische Integritätsprüfungen
- Transaktionslimits und Mehrpersonenfreigaben
- Schutz vor Replay- und Duplikatangriffen
- Software- und Smart-Contract-Sicherheitsprüfungen
- Netzwerksegmentierung und kontrollierte Datenflüsse
- Incident Response und Business Continuity
- Auditierbare technische Kontrollverfahren
- Datenschutz und Datensparsamkeit

Private Schlüssel, Seed-Phrasen, Zugangstoken, vertrauliche Kundendaten und Produktionsgeheimnisse werden im Rahmen dieser Erstkontaktaufnahme nicht übermittelt.

### L. Regulatorische Anforderungen

Vor einer tatsächlichen operativen Umsetzung sollen die jeweils einschlägigen Rechtsvorschriften geprüft werden, insbesondere:

- Markets in Crypto-Assets Regulation (MiCAR)
- Kryptomärkteaufsichtsgesetz
- Zulassungsvoraussetzungen für Crypto-Asset Service Provider (CASP)
- EU-Geldtransferverordnung und Travel Rule
- Geldwäscheprävention und Sanktionsvorschriften
- Datenschutz-Grundverordnung
- Digital Operational Resilience Act, soweit anwendbar
- Finanzmarkt- und Marktmissbrauchsanforderungen
- Zahlungsdiensterecht, soweit relevant
- Wertpapierrecht bei entsprechend klassifizierten Token
- Verbraucherschutz und Kundeninformationen
- Steuerliche Melde- und Dokumentationsanforderungen

Die Anwendbarkeit und Zuordnung der jeweiligen Pflichten sollen anhand des tatsächlichen Geschäftsmodells, der beteiligten Rechtsträger und der vorgesehenen Dienstleistung geprüft werden.

Eine bereits bestehende Erfüllung oder Zertifizierung wird nicht behauptet.

### M. Gewünschte Corporate- und Developer-Zugänge

Ich bitte um Informationen zu:

1. Corporate- und Institutional-Onboarding
2. Technischen Partner- und Entwicklerprogrammen
3. Kostenlosen beziehungsweise kostenpflichtigen Sandboxes
4. Wallet-, Custody- und Exchange-APIs
5. SDKs und API-Dokumentationen
6. Testnet-Zugängen und Webhook-Spezifikationen
7. Fiat-On-/Off-Ramp-Diensten
8. Geeigneten Handels- und Liquiditätspartnern
9. AML- und Travel-Rule-Integrationsmöglichkeiten
10. Sicherheits- und technischen Zertifizierungsanforderungen
11. Produkt- und Länderfreigaben
12. Voraussetzungen einer späteren Produktionsanbindung

### N. Kommerzielle und operative Fragen

Bitte informieren Sie mich gegebenenfalls über:

- Einmalige Onboarding- und Integrationskosten
- Laufende Plattform- und Servicegebühren
- Mindestumsätze und Mindestvolumina
- Trading-, Konvertierungs- und Custody-Gebühren
- Blockchain-Netzwerkgebühren
- Liquiditäts- und Prefunding-Anforderungen
- Erforderliche Eigenmittel und Sicherheiten
- Support- und Service-Level-Agreements
- Verantwortlichkeiten für Kundenvermögen und Schlüsselverwaltung
- Haftungs-, Verlust- und Sicherheitsregelungen
- Vertragskündigung, Datenexport und Exit-Verfahren

Aktuelle oder prognostizierte Kunden-, Wallet-, Handels- und Verwahrvolumina werden nicht angegeben, da keine verifizierten Zahlen für diese Anfrage vorliegen.

### O. Regulatorische Status- und Haftungsklarstellung

GlobalCards Bank ist zum Zeitpunkt dieser Anfrage eine vorläufige Projektbezeichnung.

Es wird nicht behauptet, dass GlobalCards:

- eine eingetragene und zugelassene Bank ist,
- über eine CASP-Zulassung verfügt,
- eine regulierte Kryptobörse betreibt,
- Kryptowerte bereits berechtigt für Kunden verwahrt,
- zur Ausgabe von Stablecoins zugelassen ist,
- eine bestätigte Partnerschaft mit bestimmten Exchange- oder Custody-Dienstleistern besitzt,
- eigene aufsichtsrechtliche Handels- oder Zahlungsverkehrsbefugnisse besitzt,
- bereits Kundengelder, Vermögenswerte oder Handelsaufträge verwaltet.

Diese Anfrage stellt weder einen formellen Zulassungsantrag noch ein öffentliches Angebot von Kryptowerten oder Wertpapieren dar.

Sie begründet keine Vertragsbeziehung und beinhaltet keine Beauftragung von Handels-, Verwahr- oder Zahlungsdienstleistungen.

### P. Vertraulichkeit

Ich bitte um zweckgebundene Verarbeitung der übermittelten Informationen für die Prüfung der möglichen Geschäfts- und Technologiepartnerschaft sowie für gegebenenfalls gesetzlich erforderliche Prüfungen.

Weitergehende Unternehmens-, Identitäts- oder technische Sicherheitsunterlagen sollen erst nach gesonderter Prüfung des Empfängers und über geeignete geschützte Übermittlungswege bereitgestellt werden.

### Q. Gewünschter nächster Schritt

Ich würde mich über eine Rückmeldung zur grundsätzlichen Eignung des beschriebenen Projekts freuen.

Insbesondere bitte ich um:

- Benennung der zuständigen Corporate- oder Institutional-Abteilung
- Hinweise zur erforderlichen Gesellschaftsform
- Informationen über die regulatorischen Voraussetzungen
- Developer- und Sandbox-Zugänge
- Technische API-Dokumentation
- Unterstützte Länder und Dienstleistungskategorien
- Kommerzielle Partnerbedingungen
- Weiterführende Onboarding-Verfahren

Ich strebe eine transparente, sichere und langfristig tragfähige Zusammenarbeit an.

Mit freundlichen Grüßen

**Daniel Pohl**\
Projektinitiator und technischer Projektkontakt

**GlobalCards Bank** – vorläufige Projektbezeichnung\
**Bra1nKy11 World Bank Eyes AeTHer** – Projekt-/Organisationsbezeichnung\
**HolyThreeKingsTreesCrowns** – zusätzliche Projektidentifikation

Detmold, Nordrhein-Westfalen, Deutschland

**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

---

**Dokumentstatus:** Zur persönlichen Prüfung vorbereitet.

**Keine automatische Registrierung, Einreichung, Vertragsannahme, Transaktion oder Lizenzbeantragung.**

## 2. Universelle Feldzuordnung für Corporate-Portale

Die folgende Zuordnung unterscheidet bekannte Angaben und Felder, für die weitere Nachweise erforderlich sind.

| Portal-Feld (EN)         | GlobalCards-Angabe                                         | Regel                         |
| ------------------------ | ---------------------------------------------------------- | ----------------------------- |
| First Name               | Daniel                                                     | Übernehmen                    |
| Last Name                | Pohl                                                       | Übernehmen                    |
| Contact Email            | world.banks.eyes.aether\@globedynamicz.statesflowwishes.eu | Übernehmen                    |
| Position                 | Project Initiator / Technical Project Contact              | Keine Organstellung behaupten |
| Project Name             | GlobalCards Bank                                           | Vorläufig                     |
| Organization Designation | Bra1nKy11 World Bank Eyes AeTHer                           | Nur Projektname               |
| Legal Company Name       | Nicht bestätigt                                            | Sperre bei Pflichtfeld        |
| Legal Form               | Nicht bestätigt                                            | Manuelle Prüfung              |
| Registration Number      | Nicht bereitgestellt                                       | Nicht erfinden                |
| Registered Office        | Nicht bestätigt                                            | Kontaktort nicht übernehmen   |
| Contact City             | Detmold                                                    | Übernehmen                    |
| Country                  | Germany                                                    | Übernehmen                    |
| Corporate Website        | Nicht bereitgestellt                                       | Offen                         |
| LEI / VAT                | Nicht bereitgestellt                                       | Nachweis erforderlich         |
| Business Type            | Proposed B2C/B2B Fintech Platform                          | Geplantes Modell              |
| Industry                 | Financial Technology / Digital Assets                      | Übernehmen                    |
| Development Stage        | Concept / Technical Preparation                            | Übernehmen                    |
| Target Market            | Germany / EEA                                              | Geplant                       |
| Partnership Interest     | Crypto / Wallet / Exchange                                 | Übernehmen                    |
| CASP License             | Nicht nachgewiesen                                         | Keine Zulassung behaupten     |
| Exchange License         | Nicht nachgewiesen                                         | Keine Zulassung behaupten     |
| Custody Model            | Noch nicht festgelegt                                      | Manuelle Prüfung              |
| Wallet Type              | Custodial / Non-Custodial under evaluation                 | Geplant                       |
| Trading Products         | Spot Trading under evaluation                              | Geplant                       |
| Supported Chains         | Noch nicht ausgewählt                                      | Nicht erfinden                |
| Fiat On-/Off-Ramp        | Requested                                                  | Anfrage                       |
| Stablecoin Integration   | Under Evaluation                                           | Keine Emission behaupten      |
| Trading Volume           | Nicht prognostiziert                                       | Offen                         |
| Assets Under Custody     | Keine verifizierten Angaben                                | Offen                         |
| Expected Customers       | Nicht prognostiziert                                       | Offen                         |
| UBO Details              | Nicht bereitgestellt                                       | Geschützte Prüfung            |
| Source of Funds          | Nicht dokumentiert                                         | Nachweise bei Bedarf          |
| AML Officer              | Nicht bestätigt                                            | Nicht erfinden                |
| Sandbox Access           | Requested                                                  | Übernehmen                    |
| Production Access        | Nicht genehmigt                                            | Gesperrt                      |
| Authorized Signatory     | Nicht bestätigt                                            | Vor Vertrag prüfen            |

## 3. Kompakte Version für Registrierungsportale

**Betreff: Corporate Crypto / Wallet / Exchange Partnership Request – GlobalCards Bank**

Sehr geehrte Damen und Herren,

als Projektinitiator von GlobalCards Bank interessiere ich mich für eine mögliche Corporate- und Technologiepartnerschaft zur Integration von Wallet-Infrastruktur, regulierten Kryptowerte-Dienstleistungen, Exchange-APIs, Custody, Fiat-On-/Off-Ramps und Blockchain-Settlement.

GlobalCards ist als hybride internationale B2C-/B2B-Finanztechnologieplattform mit Banking-, Zahlungs- und Digital-Asset-Schnittstellen geplant.

Der primäre Zielmarkt ist Deutschland/EWR. Das Vorhaben befindet sich in der Konzeption und technischen Vorbereitung. Der rechtliche Gesellschaftsstatus ist noch nicht bestätigt; eigene Bank-, CASP-, Exchange- oder Custody-Zulassungen werden nicht beansprucht.

Ich bitte um Informationen zu Ihren Corporate-Onboarding-Verfahren, verfügbaren Developer-Sandboxes, APIs, technischen Voraussetzungen, regulatorischen Anforderungen und kommerziellen Partnermodellen.

Mit freundlichen Grüßen

Daniel Pohl\
Projektinitiator – GlobalCards Bank\
Bra1nKy11 World Bank Eyes AeTHer\
Detmold, Nordrhein-Westfalen, Deutschland\
[world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

## 4. Separate Freigabe-Checkliste

Freigabeprüfung

0 / 16

Corporate & Identität

Kontakt- und Projektangaben sind richtig.

Der Gesellschaftsstatus wird ausdrücklich als unbestätigt bezeichnet.

Es werden keine Handelsregisterdaten, Lizenzen oder Partnerschaften erfunden.

Die Berechtigung zu einer späteren rechtsverbindlichen Erklärung wird getrennt geprüft.

Crypto / Wallet / Exchange

Gewünschte Dienstleistungen entsprechen dem ausgewählten Partner.

Custodial und Non-Custodial Wallets werden unterschieden.

Es werden keine bestehenden Trading- oder Custody-Volumina behauptet.

Eine eigene Exchange- oder Stablecoin-Emission wird nicht als genehmigt dargestellt.

Regulatorik & Sicherheit

MiCAR und die konkrete CASP-Zulassung sind als Prüfpunkt erfasst.

AML, Travel Rule und Datenschutz sind berücksichtigt.

Keine Schlüssel, Seed-Phrasen oder Produktionsdaten sind beigefügt.

Portal, Empfänger und Datenschutzhinweise sind überprüft.

Freigabe & Einreichung

Das Schreiben ist auf den tatsächlichen Partner zugeschnitten.

Fehlende Pflichtangaben sind vor einer formellen Einreichung geklärt.

Etwaige Gebühren, Vertragsbedingungen und Erklärungen sind geprüft.

Für genau diese Anfrage liegt eine ausdrückliche persönliche Versandfreigabe vor.

16 Prüfpunkte noch offen.

&#x20;Checkliste kopieren

## 5. Sichere Verarbeitungslogik für den Portal-Worker

| Status                    | Handlung                                                          |
| ------------------------- | ----------------------------------------------------------------- |
| `PROFILE_LOADED`          | Bekannte Daten aus geschütztem Profil laden                       |
| `PARTNER_CLASSIFIED`      | Exchange, Wallet, Custody, Ramp oder Technology Provider erkennen |
| `FIELD_MAPPING`           | Zutreffende Felder zuordnen                                       |
| `LEGAL_ENTITY_CHECK`      | Gesellschaft und vertretungsberechtigte Personen prüfen           |
| `CASP_SCOPE_CHECK`        | Erlaubnisumfang für die jeweilige Tätigkeit bestimmen             |
| `KYC_AML_CHECK`           | Identitäts-, AML- und Travel-Rule-Anforderungen zuordnen          |
| `SENSITIVE_DATA_FILTER`   | Schlüssel und vertrauliche Produktionsdaten ausschließen          |
| `DUPLICATE_CHECK`         | Doppelte Anfragen erkennen                                        |
| `DRAFT_READY`             | Vorschau zur persönlichen Prüfung erzeugen                        |
| `HUMAN_APPROVAL_REQUIRED` | Freigabe für konkreten Empfänger verlangen                        |
| `SUBMISSION_LOCKED`       | Keine automatische Übermittlung oder Registrierung                |

## 6. Offizielle regulatorische Referenzen

Die rechtliche Ausgestaltung muss sich am tatsächlich angebotenen Dienst orientieren. Für CASP-Zulassungen definiert MiCAR unter anderem organisatorische, technische, finanzielle und dienstleistungsspezifische Antragsvoraussetzungen.&#x20;



European Securities and Markets Authority+1



| Behörde / Regelwerk              | Direkter offizieller Link                                                                                                                                                                                                                                                                     |
| -------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| BaFin – CASP-Zulassungsverfahren | [Kryptowerte-Dienstleistungen und Antrag](https://bafin.de/DE/unternehmen-maerkte/erlaubnis-registrierung/geschaefte-krypto/kryptowerte-dienstleistungen/kryptowerte-dienstleistungen.html)                                                                            |
| ESMA – MiCAR Artikel 62          | [Antragsanforderungen für CASPs](https://www.esma.europa.eu/publications-and-data/interactive-single-rulebook/mica/article-62-application-authorisation-crypto)                                                                                                        |
| ESMA – Register                  | [MiCAR-Register und Informationen](https://www.esma.europa.eu/esmas-activities/digital-finance-and-innovation/markets-crypto-assets-regulation-mica)                                                                                                                   |
| EBA – Travel Rule                | [Leitlinien für Kryptotransfers](https://www.eba.europa.eu/activities/single-rulebook/regulatory-activities/anti-money-laundering-and-countering-financing-terrorism/guidelines-information-requirements-relation-transfers-funds-and-certain-crypto-assets-transfers) |
| EUR-Lex – MiCAR                  | [Verordnung (EU) 2023/1114](https://eur-lex.europa.eu/legal-content/DE/TXT/?uri=CELEX:32023R1114\&utm_source=chatgpt.com)                                                                                                                                                                     |

Die EBA-Travel-Rule-Leitlinien gelten seit dem 30. Dezember 2024 und legen unter anderem den Umgang mit unvollständigen Begleitinformationen zu Kryptotransfers fest.&#x20;



European Banking Authority



Ergebnis: Das vollständige deutschsprachige Corporate-Anschreiben, die internationale Feldzuordnung, die kompakte Portalversion, die Prüf- und Freigabe-Checkliste sowie die Steuerungslogik für den Portal-Worker sind vorbereitet.

Das Hauptanschreiben ist für eine unverbindliche institutionelle Erstkontaktaufnahme verwendbar. Für ein tatsächliches reguliertes Partner-Onboarding oder eine MiCAR-Zulassung müssen zuvor die noch fehlenden rechtlichen Gesellschafts-, Finanzierungs- und Verantwortlichkeitsnachweise geklärt werden.

Es wurden keine Registrierungen, Anträge, Wallet-Eröffnungen, Transaktionen oder Übermittlungen durchgeführt. # GlobalCards Bank – Funds / DAO / Asset Management

Universal Corporate & Institutional Partnership Application · Deutsche Fassung · Version 1.0 · 7. November 2026

Diese Fassung ist als unverbindliche, institutionelle Erstanfrage für Fondsadministratoren, Kapitalverwaltungsgesellschaften, Vermögensverwalter, Verwahrstellen, DAO-Infrastrukturpartner und internationale Investment-Organisationen ausgearbeitet.

Antragsteller

Daniel Pohl

Projektbezeichnung

GlobalCards Bank

Gesellschaftsstatus

Noch nicht bestätigt

Zielmarkt

Deutschland / EWR

Antragsart

Corporate-Partnerschaftsanfrage

Übermittlung

Nicht erfolgt

## 1. Rechtliche Einordnung

| Bereich                                   | Bedeutung und Voraussetzung                                                                                               |
| ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------- |
| Investmentfonds / AIF                     | Gemeinsame Kapitalanlage nach einer festgelegten Anlagestrategie; gegebenenfalls unter dem KAGB/AIFMD reguliert           |
| Kapitalverwaltungsgesellschaft (KVG/AIFM) | Verwaltung von Investmentvermögen, grundsätzlich erlaubnis- oder unter bestimmten Voraussetzungen registrierungspflichtig |
| Asset Management                          | Individuelle Finanzportfolioverwaltung oder kollektive Fondsverwaltung; regulatorisch unterschiedlich                     |
| Fund Administration                       | Fondsbuchhaltung, Anteilswertberechnung, Register, Reporting und ausgelagerte Administrationsprozesse                     |
| DAO Governance                            | Technische Abstimmungs-, Entscheidungs- und Verwaltungsstruktur, keine eigenständige universelle Rechts- oder Lizenzform  |
| Tokenisierte Fondsanteile                 | Erfordern eine eigenständige rechtliche Einordnung des Fonds und der Token                                                |
| Staatlicher Investmentfonds               | Gründung und staatliche Befugnisse setzen eine entsprechende öffentliche Rechtsgrundlage und Ermächtigung voraus          |

Nach der europäischen AIFMD kann bereits das Einsammeln von Kapital mehrerer Anleger zur Investition nach einer festgelegten Strategie die Einordnung als alternativer Investmentfonds auslösen. In Deutschland unterscheidet das KAGB zwischen erlaubnispflichtigen und bestimmten registrierungspflichtigen Kapitalverwaltungsgesellschaften.&#x20;



EUR-Lex+2



Wichtig: Eine DAO, ein Smart Contract oder eine Wallet-Struktur ersetzt keine erforderliche Fonds- oder Finanzdienstleistungslizenz. Auch eine zunächst technische DAO kann einer Regulierung unterliegen, wenn tatsächlich regulierte Finanzdienstleistungen durch identifizierbare Akteure erbracht oder kontrolliert werden.&#x20;



EUR-Lex



## 2. Vollständiges Corporate- und Institutional-Anschreiben

# GLOBALCARDS BANK

## UNIVERSAL CORPORATE & INSTITUTIONAL FUNDS, DAO & ASSET MANAGEMENT PARTNERSHIP APPLICATION

**Formelle Interessenbekundung zur Fondsstrukturierung, Fondsadministration, Vermögensverwaltung, DAO-Governance und internationalen Investmentinfrastruktur**

**Datum:** 7. November 2026\
**Dokumentversion:** 1.0\
**Sprache:** Deutsch\
**Status:** Unverbindliche Corporate-Erstanfrage – persönliche Freigabe erforderlich

---

### A. Antragsteller und Projektidentität

| Feld                                         | Angabe                                                                                                                        |
| -------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Ansprechpartner                              | Daniel Pohl                                                                                                                   |
| Funktion                                     | Projektinitiator und technischer Projektkontakt                                                                               |
| Vorläufiger Projektname                      | GlobalCards Bank                                                                                                              |
| Weitere Projekt-/Organisationsbezeichnung    | Bra1nKy11 World Bank Eyes AeTHer                                                                                              |
| Zusätzliche Projektidentifikation            | HolyThreeKingsTreesCrowns                                                                                                     |
| Kontaktstandort                              | Detmold, Nordrhein-Westfalen, Deutschland                                                                                     |
| Kontakt-E-Mail                               | [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu) |
| Rechtlich registriertes Unternehmen          | Noch nicht bestätigt                                                                                                          |
| Gesellschaftsform                            | Noch nicht bestätigt                                                                                                          |
| Eingetragener Gesellschaftssitz              | Noch nicht bestätigt                                                                                                          |
| Handelsregisternummer                        | Nicht bereitgestellt                                                                                                          |
| Legal Entity Identifier (LEI)                | Nicht bereitgestellt                                                                                                          |
| Umsatzsteuer-ID des Unternehmens             | Nicht bereitgestellt                                                                                                          |
| Bestehende KVG-/AIFM-Erlaubnis               | Nicht nachgewiesen                                                                                                            |
| Bestehende Vermögensverwaltungserlaubnis     | Nicht nachgewiesen                                                                                                            |
| Bestehende Fondsregistrierung                | Nicht nachgewiesen                                                                                                            |
| Genehmigter Investmentfonds                  | Nicht nachgewiesen                                                                                                            |
| Bestehende Fondsverwahrstelle                | Nicht bestätigt                                                                                                               |
| Bestehender Administrator oder Asset Manager | Nicht bestätigt                                                                                                               |
| Vorhandenes verwaltetes Vermögen (AuM)       | Keine verifizierten Angaben                                                                                                   |
| Staatlicher Fondsstatus                      | Nicht beansprucht                                                                                                             |
| DAO-Rechtsform / DAO-Registrierung           | Nicht bestätigt                                                                                                               |
| Projektphase                                 | Konzeption und technische Vorbereitung                                                                                        |
| Geografischer Ausgangspunkt                  | Deutschland / Europäischer Wirtschaftsraum                                                                                    |
| Internationale Erweiterung                   | Perspektivisch, nach gesonderter rechtlicher Prüfung                                                                          |

Die angegebenen Namen dienen ausschließlich der Identifikation des geplanten Vorhabens. Sie belegen weder eine eingetragene Gesellschaft noch eine bestehende aufsichtsrechtliche Zulassung, eine staatliche Vertretung oder die Berechtigung zur Verwaltung von Anlegervermögen.

Die Bezeichnung „GlobalCards Bank“ ist vorläufig und bedarf vor einer geschäftlichen Verwendung einer eigenständigen rechtlichen Prüfung.

### B. Empfänger und Betreff

**An:** Corporate Partnerships / Institutional Relations / Fund Services / Asset Management / Investment Fund Structuring / Digital Asset Governance

**Betreff:** Corporate- und institutionelle Partnerschaftsanfrage – GlobalCards Bank | Fund Structuring, Fund Administration, Asset Management, DAO Governance und Investment Infrastructure

### C. Formelle Vorstellung

Sehr geehrte Damen und Herren,

hiermit möchte ich mein Interesse an einer möglichen institutionellen, technischen und wirtschaftlichen Zusammenarbeit im Bereich Fondsstrukturierung, Investmentverwaltung, Fondsadministration und moderner digitaler Governance-Infrastrukturen zum Ausdruck bringen.

Unter der vorläufigen Projektbezeichnung **GlobalCards Bank** bereite ich die Entwicklung einer modularen internationalen Finanztechnologieplattform für Privatkunden (B2C) und Geschäftskunden (B2B) vor.

Neben Banking-, Zahlungs- und Kartenfunktionen sollen perspektivisch technische Module für die Verwaltung von Investitionsprojekten, Finanzierungsstrukturen, Vermögensbeständen, institutionellen Fondsprozessen und digitalen Entscheidungsverfahren untersucht werden.

Ein besonderer Schwerpunkt liegt auf der möglichen Verbindung traditioneller Fondsadministration mit nachvollziehbaren, transparenten und kontrollierten DAO-Governance-Mechanismen.

Ich möchte prüfen, welche Dienstleistungen, Zulassungsmodelle, rechtlichen Strukturen und technischen Integrationsmöglichkeiten Ihre Organisation für ein solches Vorhaben bereitstellen könnte.

Der rechtliche Gesellschaftsstatus sowie die konkrete rechtliche Struktur eines möglichen Investment- oder Fondsmodells sind gegenwärtig noch nicht bestätigt.

Diese Anfrage dient daher ausschließlich der unverbindlichen Prüfung einer zukünftigen Partnerschaft und der damit verbundenen Voraussetzungen.

### D. Strategisches Projekt- und Geschäftsmodell

**Projekt:** GlobalCards Bank

**Technischer Ansatz:** Modulare API-First-Finanzinfrastruktur

**Zielgruppen:** Privatkunden, Geschäftskunden, institutionelle Partner und – bei gesonderter rechtlicher Prüfung – geeignete Investoren

**Primäre Zielregion:** Deutschland und Europäischer Wirtschaftsraum

**Weitere mögliche Regionen:** Schweiz, Vereinigtes Königreich und andere Jurisdiktionen, sofern rechtlich und wirtschaftlich geeignet.

Das Vorhaben soll unterschiedliche funktionale Bereiche miteinander verbinden:

1. Corporate- und Finanzinfrastruktur
2. Banking- und Zahlungsdienstleisterintegration
3. Fondsstrukturierung und Fondsadministration
4. Asset-Management-Technologie
5. Investment- und Treasury-Reporting
6. Governance- und Genehmigungsworkflows
7. DAO-basierte Abstimmungs- und Verwaltungsprozesse
8. Digital-Asset- und Tokenisierungsintegration
9. Verwahrstellen- und Custody-Konnektivität
10. Settlement und Reconciliation
11. Risikomanagement und Compliance
12. Regulatorische Nachweisführung

Der operative Umfang soll erst nach Prüfung des jeweils anwendbaren Aufsichts-, Gesellschafts- und Investmentrechts verbindlich festgelegt werden.

### E. Angefragte Fonds- und Verwaltungsmodelle

Für die mögliche künftige Entwicklung werden folgende Modelle untersucht.

**Modell A – Alternative Investment Funds (AIF)**

Prüfung geeigneter offener oder geschlossener alternativer Investmentfonds, einschließlich der Anforderungen an Fondsstruktur, Anlegerkreis, Anlagepolitik, Verwaltung und Verwahrstelle.

**Modell B – Fund Management / KVG / AIFM**

Zusammenarbeit mit einer zugelassenen oder entsprechend registrierten Kapitalverwaltungsgesellschaft beziehungsweise einem berechtigten Fondsmanager.

**Modell C – Fund Administration**

Technische und operative Unterstützung in den Bereichen Fondsbuchhaltung, Investorenregister, Anteilswertberechnung, Reporting, Dokumentation und Transaktionsabstimmung.

**Modell D – Asset Management**

Prüfung technischer Lösungen für Portfolioanalyse, Risikomanagement, Berichterstattung und – ausschließlich über berechtigte Unternehmen – gegebenenfalls Vermögensverwaltung.

**Modell E – Corporate Investment & Treasury**

Interne Verwaltung eigener Unternehmensfinanzen, Beteiligungen, Budgets und Investitionsvorhaben unter Berücksichtigung der möglichen regulatorischen Abgrenzungen.

**Modell F – DAO Governance Infrastructure**

Einführung transparenter Abstimmungs-, Delegations-, Freigabe- und Dokumentationsmechanismen innerhalb einer geeigneten rechtlichen Organisationsstruktur.

**Modell G – Digital Asset / Tokenized Fund Services**

Prüfung möglicher technischer Schnittstellen zu rechtmäßig strukturierten tokenisierten Fondsanteilen, digitalen Wertpapieren oder anderen digitalen Vermögenspositionen.

**Modell H – Institutional or Public-Sector Fund Cooperation**

Unverbindliche Prüfung, ob öffentliche Auftraggeber oder institutionelle Fondsverwaltungen technische Dienstleistungen beziehungsweise Governance-Infrastruktur über reguläre Beschaffungs- oder Partnerschaftsverfahren beziehen.

Eine staatliche Fondseigenschaft, staatliche Trägerschaft oder Befugnis zur Verwaltung öffentlicher Gelder wird ausdrücklich nicht behauptet.

### F. Fondsstrukturierung und Investor Administration

Für eine mögliche künftige Fondsplattform sollen folgende Funktionen bewertet werden:

- Geeignete Fondsrechtsformen
- Unterscheidung zwischen Publikums- und Spezialfonds
- Festlegung des zulässigen Anlegerkreises
- Anlagepolitik und Anlagebeschränkungen
- Investoren-Onboarding
- KYC-/KYB- und wirtschaftlich-Berechtigten-Prüfung
- Zeichnungs- und Rücknahmeprozesse
- Kapitalabrufe und Ausschüttungen
- Investorenregister und Anteilsbestände
- Bewertung und Nettoinventarwert
- Gebühren- und Kostenberechnung
- Jahresabschlüsse und Berichterstattung
- Risikokontrollen und Compliance-Nachweise

Die rechtlich maßgeblichen Anlegerregister, Bewertungen, Anlageentscheidungen und Verwahrfunktionen sollen gemäß dem konkreten Betriebsmodell und den jeweils geltenden Vorschriften den hierfür verantwortlichen Institutionen zugeordnet werden.

### G. Vermögensverwaltung und Investmentprozesse

Die vorgesehene technische Plattform soll die Integration folgender Prozesse ermöglichen:

1. Portfolio- und Positionsdaten
2. Anlageklassen und Instrumentenstammdaten
3. Bewertungsdaten und Marktdaten
4. Risikokennzahlen
5. Liquiditäts- und Cash-Flow-Prognosen
6. Investmentlimits
7. Genehmigungs- und Freigabeprozesse
8. Transaktionsstatus und Brokeranbindung
9. Bestandsabgleich mit Verwahrstellen
10. Investoren- und Managementberichte
11. Performance- und Gebührenberechnung
12. Revisionsfähige Dokumentation

Die eigenständige Erbringung von Anlageberatung, Finanzportfolioverwaltung, Anlagevermittlung oder anderen regulierten Wertpapierdienstleistungen wird nicht als bereits zulässig oder bestehend dargestellt.

### H. DAO Governance und digitale Organisationsverwaltung

GlobalCards soll optional eine modulare DAO-Governance-Infrastruktur unterstützen.

Mögliche technische Funktionen:

- Mitglieder- und Rollenverwaltung
- Verwaltung definierter Stimmrechte
- Vorschlags- und Beschlussverfahren
- Delegierte Abstimmungen
- Quorum- und Mehrheitsregeln
- Zeitlich begrenzte Abstimmungsverfahren
- Kontrollierte Smart-Contract-Freigaben
- Transparente Beschluss- und Änderungsprotokolle
- Mehrstufige Treasury-Freigaben
- Konflikt- und Interessenkollisionsmanagement
- Auditierbare Governance-Nachweise
- Technische Notfall- und Wiederherstellungsverfahren

Jede DAO-Struktur muss hinsichtlich ihrer tatsächlichen Rechtsträger, wirtschaftlich Berechtigten, Leitungspersonen, Vermögenswerte und regulatorischen Tätigkeit bewertet werden.

Ein Governance-Token oder ein On-Chain-Voting-System begründet für sich allein keine rechtlich anerkannte Fondsgesellschaft, keine Finanzlizenz und keine Befugnis zur Verwaltung fremden Vermögens.

Die rechtlichen Entscheidungskompetenzen sollen ausdrücklich von technischen Abstimmungsfunktionen unterschieden werden.

### I. Fund Treasury, Wallets und Settlement

Für eine mögliche Zusammenarbeit werden außerdem folgende Integrationsbereiche untersucht:

- Fonds- und Unternehmenskonten
- IBAN- und Zahlungsdienstleisteranbindungen
- Bank- und Cash-Reconciliation
- Wertpapier- und Depotbestände
- Cash-Management und Liquiditätsübersichten
- Investment-Settlement
- Multi-Currency-Unterstützung
- Verwahrstellen- und Brokerberichte
- Dokumentierte Kapitalabrufe und Ausschüttungen
- Institutionelle Digital-Asset-Wallets
- Rollenbasierte Treasury-Freigaben
- Auditierbare Transaktionsnachweise

Kundengelder, Investmentvermögen und Fondsvermögenswerte sollen nur entsprechend der gesetzlich erforderlichen Verantwortungs- und Verwahrstruktur verarbeitet werden.

### J. Vorgesehene technische Architektur

Die mögliche technische Entwicklung umfasst folgende Module:

1. Corporate Identity & Access Management
2. Fund Entity Registry
3. Investor Onboarding & KYC/KYB
4. Beneficial Ownership Management
5. Fund Structure & Share Class Management
6. Investor Register Integration
7. Portfolio & Asset Registry
8. Fund Accounting Integration
9. NAV Calculation Support
10. Investment Risk Management
11. Asset Custody & Depositary Adapter
12. Banking & Payment Connector
13. Treasury & Liquidity Management
14. Settlement & Reconciliation Engine
15. DAO Governance Engine
16. Smart Contract Policy & Approval Layer
17. Compliance & Regulatory Mapping
18. Audit & Evidence Registry
19. Institutional Reporting
20. Developer & Partner API Gateway

Die Plattform soll modular, nachvollziehbar, sicher und möglichst unabhängig von einzelnen technischen Dienstleistern aufgebaut werden.

Für den Entwicklungsbeginn sind ausschließlich synthetische Testdaten und ausdrücklich bereitgestellte Sandbox-Umgebungen vorgesehen.

### K. Compliance, Sicherheit und Governance

Die Entwicklung soll insbesondere folgende rechtlichen und technischen Anforderungen berücksichtigen, soweit jeweils anwendbar:

- Kapitalanlagegesetzbuch (KAGB)
- Alternative Investment Fund Managers Directive (AIFMD) und geltende Änderungen
- OGAW-/UCITS-Regelungen
- Wertpapierinstitutsgesetz, MiFID II und MiFIR
- Geldwäscheprävention sowie KYC/KYB
- Datenschutz-Grundverordnung (DSGVO)
- Digital Operational Resilience Act (DORA)
- MiCAR bei entsprechenden Kryptowerte-Dienstleistungen
- Relevante Wertpapier- und Tokenisierungsvorschriften
- Verwahrstellen- und Anlegervermögensschutz
- Interessenkonfliktmanagement
- Anlegerinformationen, Vertrieb und Reporting
- Steuerliche und wirtschaftlich-Berechtigten-Meldepflichten
- Informationssicherheit und Business Continuity

Die konkrete Anwendbarkeit hängt von Rechtsform, Fondsart, Anlegerkreis, angebotenen Dienstleistungen und Rechtsraum ab.

Es wird keine bestehende Erfüllung dieser Vorschriften oder eine bereits erteilte Zertifizierung beziehungsweise Zulassung behauptet.

### L. Institutionelle Partner- und Verantwortungsstruktur

Im Rahmen eines möglichen Projekts soll geklärt werden, welche Aufgaben von welchem rechtlich verantwortlichen Unternehmen erbracht werden.

Dazu gehören:

- Fondsinitiator
- Rechtlicher Fonds- oder Investment-Rechtsträger
- Kapitalverwaltungsgesellschaft beziehungsweise AIFM
- Portfolio Manager
- Fund Administrator
- Verwahrstelle / Depositary
- Wirtschaftsprüfer
- Rechts- und Steuerberater
- Bank- und Zahlungspartner
- Transfer Agent
- Digital-Asset-Custody-Partner
- Technischer Governance-Dienstleister

GlobalCards soll nur diejenigen Aufgaben übernehmen, für die die erforderlichen rechtlichen, organisatorischen und technischen Voraussetzungen tatsächlich erfüllt sind.

### M. Gewünschte Corporate- und Developer-Zugänge

Ich bitte um Informationen zu:

1. Corporate- und Institutional-Onboarding
2. Fund Structuring und Fund Launch Services
3. Fund Administration und Transfer Agency
4. AIFM-/KVG-Partnerschaftsmodellen
5. Asset-Management- und Portfolio-APIs
6. Verwahrstellen- und Custody-Partnerschaften
7. Reporting-, NAV- und Accounting-Schnittstellen
8. DAO- und Governance-Technologien
9. Smart-Contract- und Digital-Asset-Sandboxes
10. Technischen Entwicklerprogrammen
11. Compliance-, Audit- und Reporting-Anforderungen
12. Partnerabhängigen internationalen Fondsstrukturen
13. Erforderlichen Rechtsform- und Unternehmensnachweisen
14. Möglichkeiten einer unverbindlichen Machbarkeitsprüfung

Kostenfreie Entwickler- oder Evaluierungszugänge wären für die erste technische Prüfung besonders hilfreich, sofern Ihre Organisation solche Möglichkeiten anbietet.

### N. Kommerzielle und regulatorische Fragen

Bitte informieren Sie mich nach Möglichkeit über:

- Anforderungen an einen Fondsinitiator
- Notwendige Rechtsformen und Gesellschaftsgründungen
- Zulassungs- oder Registrierungspflichten
- Mindestkapital und Eigenmittelanforderungen
- Voraussetzungen für externe Fondsmanager
- Anforderungen an die Verwahrstelle
- Mindestfondsvolumen beziehungsweise wirtschaftliche Mindestgröße
- Einmalige Strukturierungs- und Errichtungskosten
- Laufende Verwaltungs- und Administrationsgebühren
- Kosten von Wirtschaftsprüfung und Reporting
- Gebühren für Transaktions- und Depotabwicklung
- API-, Technologie- und Datenlizenzkosten
- Vertragslaufzeiten und Kündigungsbedingungen
- Verantwortlichkeiten und Haftungsregelungen
- Internationale Vertriebs- und Marketingbeschränkungen

Derzeit werden weder ein konkretes Fondsvolumen noch eine Kapitalzusage, ein Anlegerbestand, verwaltetes Vermögen oder eine Renditeprognose behauptet.

### O. Besondere Abgrenzung staatlicher und institutioneller Fonds

Falls Ihre Organisation auch mit staatlichen, kommunalen, supranationalen oder öffentlichen Investitionsfonds zusammenarbeitet, besteht Interesse an Informationen über zulässige Beschaffungs-, Technologiepartner- oder Beratungsverfahren.

Dies betrifft ausschließlich mögliche technische Dienstleistungen, Infrastrukturentwicklung und institutionelle Kooperationen.

Es wird weder die Gründung eines staatlichen Fonds beansprucht noch eine öffentlich-rechtliche Ermächtigung oder die Berechtigung zur Verwaltung staatlicher Mittel behauptet.

Entsprechende Tätigkeiten würden eine gesonderte gesetzliche oder institutionelle Grundlage und die erforderliche Beauftragung voraussetzen.

### P. Gesellschafts- und Zulassungsstatus

Zum Zeitpunkt dieser Anfrage wird ausdrücklich nicht behauptet, dass GlobalCards:

- eine eingetragene Fondsgesellschaft ist,
- eine zugelassene Kapitalverwaltungsgesellschaft ist,
- über eine Erlaubnis zur Finanzportfolioverwaltung verfügt,
- einen rechtlich genehmigten Investmentfonds betreibt,
- einen bestehenden Fondsvermögensbestand verwaltet,
- über einen bestätigten AIFM oder eine Verwahrstelle verfügt,
- Investorenkapital eingeworben hat,
- zur öffentlichen Vermarktung eines Investmentfonds berechtigt ist,
- eine rechtlich anerkannte und registrierte DAO-Fondsgesellschaft besitzt,
- eine staatliche Investmentgesellschaft oder einen Sovereign Wealth Fund betreibt,
- die Ermächtigung zur Verwaltung öffentlicher Vermögenswerte besitzt.

Diese Anfrage dient ausschließlich der Prüfung einer möglichen geschäftlichen, technischen oder institutionellen Zusammenarbeit.

Sie stellt weder ein Fondsangebot noch eine Aufforderung zur Kapitalanlage, eine Anlageberatung oder einen formellen Zulassungsantrag dar.

### Q. Vertraulichkeit und Datenverarbeitung

Ich bitte um vertrauliche und zweckgebundene Verarbeitung der übermittelten Kontakt- und Projektinformationen im Rahmen der Anfragebearbeitung und gegebenenfalls gesetzlich vorgeschriebener Prüfungen.

Vertrauliche Unternehmensunterlagen, Finanzierungsnachweise, Investorendaten, Identitätsdokumente, Zugangsdaten und kryptografische Geheimnisse sollen erst nach gesonderter Prüfung des Empfängers und über geeignete geschützte Kommunikationswege übermittelt werden.

### R. Gewünschter nächster Schritt

Ich würde mich freuen, wenn Ihre Organisation die grundsätzliche Eignung des beschriebenen Vorhabens für eine institutionelle, regulatorische oder technische Partnerschaft prüfen könnte.

Insbesondere bitte ich um:

1. Benennung der zuständigen Corporate-/Institutional-Abteilung.
2. Informationen zu geeigneten Fonds- und Verwaltungsmodellen.
3. Hinweise auf die erforderliche Gesellschaftsstruktur.
4. Angaben zu notwendigen Zulassungen und Registrierungen.
5. Informationen über externe Fondsmanager und Verwahrstellen.
6. Zugang zu technischen Entwickler- oder Testumgebungen.
7. Übersicht über Gebühren und wirtschaftliche Mindestanforderungen.
8. Hinweise zur zulässigen Integration von DAO-Governance-Funktionen.
9. Informationen zu möglichen internationalen Partnerstrukturen.

Ich strebe eine langfristig tragfähige, transparente und rechtlich ordnungsgemäße Zusammenarbeit an.

Mit freundlichen Grüßen

**Daniel Pohl**\
Projektinitiator und technischer Projektkontakt

**GlobalCards Bank** – vorläufige Projektbezeichnung\
**Bra1nKy11 World Bank Eyes AeTHer** – Projekt-/Organisationsbezeichnung\
**HolyThreeKingsTreesCrowns** – zusätzliche Projektidentifikation

Detmold, Nordrhein-Westfalen, Deutschland

**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

---

**Dokumentstatus:** Unverbindliche institutionelle Corporate-Erstanfrage.

**Keine automatische Registrierung, Fondsgründung, Kapitalaufnahme, Vertragsannahme, Lizenzbeantragung oder Einreichung.**

## 3. Feldzuordnung für Fund-, DAO- und Asset-Management-Portale

Die Feldzuordnung ist für deinen universellen Portal-Worker gedacht. Sie verwendet die vorhandenen Projektangaben, unterscheidet geplante Tätigkeiten von bestehenden Berechtigungen und stoppt verbindliche Verfahren bei fehlenden Nachweisen.

| Corporate-Portal-Feld (EN)         | GlobalCards-Angabe                                         | Verarbeitungsregel                         |
| ---------------------------------- | ---------------------------------------------------------- | ------------------------------------------ |
| First Name                         | Daniel                                                     | Übernehmen                                 |
| Last Name                          | Pohl                                                       | Übernehmen                                 |
| Contact Email                      | world.banks.eyes.aether\@globedynamicz.statesflowwishes.eu | Übernehmen                                 |
| Contact Role                       | Project Initiator / Technical Project Contact              | Keine Geschäftsführerstellung behaupten    |
| Project Name                       | GlobalCards Bank                                           | Vorläufige Bezeichnung                     |
| Organization Designation           | Bra1nKy11 World Bank Eyes AeTHer                           | Keine juristische Gesellschaft behaupten   |
| Legal Entity Name                  | Noch nicht bestätigt                                       | Pflichtprüfung                             |
| Legal Entity Type                  | Noch nicht bestätigt                                       | Manuell klären                             |
| Registration Number                | Nicht bereitgestellt                                       | Nicht erfinden                             |
| Registered Office                  | Noch nicht bestätigt                                       | Kontaktort nicht als Firmensitz verwenden  |
| Contact Location                   | Detmold, NRW                                               | Übernehmen                                 |
| Country                            | Germany                                                    | Übernehmen                                 |
| LEI                                | Nicht bereitgestellt                                       | Nachweispflichtiges Feld                   |
| Business Sector                    | Financial Technology / Fund Infrastructure                 | Übernehmen                                 |
| Partnership Interest               | Funds / DAO / Asset Management                             | Übernehmen                                 |
| Business Model                     | Proposed B2C/B2B Financial Technology Platform             | Als Planung ausweisen                      |
| Fund Type                          | AIF / Other – under evaluation                             | Nicht festgelegt                           |
| Fund Domicile                      | Nicht festgelegt                                           | Nicht aus Kontaktort ableiten              |
| Fund Legal Structure               | Nicht festgelegt                                           | Offen                                      |
| Investor Classification            | Noch nicht festgelegt                                      | Keine Anlegerberechtigung behaupten        |
| Fund Manager / AIFM                | Nicht bestätigt                                            | Partneranfrage                             |
| Fund Administrator                 | Nicht bestätigt                                            | Partneranfrage                             |
| Depositary / Custodian             | Nicht bestätigt                                            | Partneranfrage                             |
| Transfer Agent                     | Nicht bestätigt                                            | Partneranfrage                             |
| Investment Strategy                | Noch nicht festgelegt                                      | Keine Strategie fingieren                  |
| Assets Under Management            | Keine verifizierten Angaben                                | Offen                                      |
| Net Asset Value                    | Nicht vorhanden bzw. nicht nachgewiesen                    | Nicht erfinden                             |
| Committed Capital                  | Nicht bestätigt                                            | Offen                                      |
| Target Fund Size                   | Nicht prognostiziert                                       | Keine Zahlen erfinden                      |
| Existing Investors                 | Keine verifizierten Angaben                                | Nicht erfinden                             |
| Audited Financial Statements       | Nicht bereitgestellt                                       | Offen                                      |
| Regulatory License                 | Nicht nachgewiesen                                         | Keine Zulassung behaupten                  |
| AIFM / KVG Authorization           | Nicht nachgewiesen                                         | Regulatorische Klärung                     |
| DAO Legal Structure                | Noch nicht festgelegt                                      | Keine Registrierung behaupten              |
| Governance Token                   | Nicht bestätigt                                            | Keine Emission behaupten                   |
| Smart Contract Audit               | Nicht nachgewiesen                                         | Keine Prüfung behaupten                    |
| Treasury Assets                    | Keine verifizierten Angaben                                | Offen                                      |
| Sovereign / Government Fund Status | Nicht beansprucht                                          | Niemals automatisch auswählen              |
| UBO Details                        | Nicht bereitgestellt                                       | Geschützter Nachweis                       |
| Source of Funds                    | Nicht dokumentiert                                         | Individuell nachweisen, falls erforderlich |
| AML / Compliance Officer           | Nicht bestätigt                                            | Nicht erfinden                             |
| Sandbox Access                     | Requested                                                  | Übernehmen                                 |
| Developer/API Access               | Requested                                                  | Übernehmen                                 |
| Production Access                  | Nicht genehmigt                                            | Gesperrt                                   |
| Authorized Signatory               | Nicht bestätigt                                            | Vor verbindlicher Erklärung klären         |

### 3.1 Partnerabhängige Pflichtfelder

| Partnerkategorie                | Zusätzliche Informationen vor formellem Onboarding                                                                    |
| ------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| KVG / AIFM                      | Fondsrechtsform, Anlagepolitik, Geschäftsplan, Anlegerkreis, verantwortliche Geschäftsleiter, Eigenmittel             |
| Fund Administrator              | Fondsstruktur, Buchhaltung, Investorenregister, NAV-Berechnung, Reporting und Serviceumfang                           |
| Asset Manager                   | Portfolioart, Mandate, Anlageinstrumente, Entscheidungsverantwortung und erforderliche Erlaubnis                      |
| Depositary / Custodian          | Vermögensart, rechtlicher Fonds, Verwahrmodell, Settlement und Kontrollpflichten                                      |
| DAO Provider                    | Rechtsträger, Governance-Befugnisse, Tokenrechte, Schlüsselkontrolle, Beschlussverfahren                              |
| Tokenized Fund Provider         | Rechtliche Natur des Fondsanteils, Tokenstruktur, Register, Verwahrung und Anlegerrechte                              |
| Government / Institutional Fund | Offizielle Ausschreibung, institutionelle Beauftragung, Vergabevoraussetzungen; keine staatliche Stellung ohne Mandat |

## 4. Kompakte Fassung für Corporate-Online-Portale

Für kurze Textfelder wie Partnership Request, Project Description, Institutional Client Inquiry oder Fund Services Inquiry kannst du die folgende Fassung verwenden.

**Betreff: Corporate Funds / DAO / Asset Management Partnership Request – GlobalCards Bank**

Sehr geehrte Damen und Herren,

als Projektinitiator von GlobalCards Bank interessiere ich mich für eine mögliche institutionelle und technische Partnerschaft im Bereich Fondsstrukturierung, Fondsadministration, Asset Management, DAO-Governance und internationaler Investmentinfrastruktur.

GlobalCards ist als hybride, API-basierte Finanztechnologieplattform für Privat- und Geschäftskunden geplant. Perspektivisch sollen Funktionen für Fondsadministration, Portfolio-Reporting, Treasury, Verwahrstellenintegration, Investment-Settlement und transparente digitale Governance-Verfahren untersucht werden.

Ich möchte insbesondere prüfen, ob Ihre Organisation geeignete Corporate- und Institutional-Onboarding-Verfahren, AIFM-/KVG-Partnerschaftsmodelle, Fondsadministrationsleistungen, technische APIs oder Entwickler-Sandboxes anbietet.

Der rechtliche Gesellschaftsstatus ist derzeit noch nicht bestätigt. Es werden keine bestehende Fondsregistrierung, KVG-/AIFM-Erlaubnis, Vermögensverwaltungslizenz, Anlegerkapitalbestände oder staatlichen Fondsbefugnisse beansprucht.

Die Anfrage dient ausschließlich einer unverbindlichen Machbarkeits- und Partnereignungsprüfung und stellt weder ein Fondsangebot noch eine Aufforderung zur Kapitalanlage dar.

Ich bitte um Informationen zu den Voraussetzungen, den zuständigen Ansprechpartnern, den verfügbaren technischen Zugängen und den kommerziellen Bedingungen.

Mit freundlichen Grüßen

**Daniel Pohl**\
Projektinitiator – GlobalCards Bank\
Bra1nKy11 World Bank Eyes AeTHer\
Detmold, Nordrhein-Westfalen, Deutschland\
[world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

## 5. Partnerspezifisches Formular für den Portal-Worker

PartnerkategorieKVG / AIFM / Fund Manager

Anfragefokus

Fondskonzeption, externe Kapitalverwaltungsgesellschaft, AIF-Struktur und regulatorische Voraussetzungen

Konkrete Corporate-Frage

Welche Möglichkeiten bestehen für eine unverbindliche Vorprüfung eines Fondsinitiators ohne bereits bestätigte Gesellschaftsstruktur?

&#x20;Partnerspezifische Kurzanfrage kopieren

## 6. Separate Freigabe-Checkliste

Diese Checkliste ist für die persönliche Prüfung vor der Einreichung vorgesehen. Sie ersetzt keine behördliche Entscheidung und löst keine Übermittlung aus.

Corporate Funds – Freigabeprüfung

0 / 20

A. Unternehmensidentität & Rechtsstatus

Kontaktperson und Projektbezeichnungen wurden überprüft.

Der Gesellschaftsstatus ist ausdrücklich als unbestätigt angegeben.

Es werden keine KVG-/AIFM-, Asset-Management- oder sonstigen Lizenzen behauptet.

Eine rechtliche Zeichnungs- und Vertretungsberechtigung wird nicht vorausgesetzt.

B. Fonds & Asset Management

Eine mögliche Fondsstruktur wird nicht als bereits gegründet dargestellt.

Anlegergelder, Assets under Management und Renditen wurden nicht erfunden.

Fondsverwaltung, individuelle Vermögensverwaltung und Administration werden getrennt.

Die Erfordernisse für Fondsmanager, Verwahrstelle und Anlegerkreis werden geprüft.

C. DAO & Government Funds

DAO-Governance wird nicht als Ersatz einer juristischen Person oder Erlaubnis dargestellt.

Eine mögliche Tokenemission wird nicht als bereits genehmigt bezeichnet.

Es wird keine staatliche Fondsstellung oder öffentliche Vollmacht behauptet.

Smart-Contract- und Treasury-Rechte unterliegen einer klaren Verantwortlichkeitsprüfung.

D. Datenschutz & Partnerprüfung

Keine privaten Schlüssel, Kundendaten oder vertraulichen Investorendokumente werden ungeschützt beigefügt.

Der konkrete Corporate-Partner und das offizielle Zielportal wurden geprüft.

Datenschutz, Vertraulichkeit und erforderliche Verträge sind berücksichtigt.

Alle erforderlichen Pflichtangaben sind wahrheitsgemäß ausgefüllt oder als offen markiert.

E. Persönliche Freigabe

Der gewählte Empfänger und der tatsächliche Anfragezweck stimmen überein.

Gebühren, rechtliche Erklärungen und mögliche Vertragsbindungen wurden geprüft.

Das Schreiben wurde in seiner endgültigen Fassung persönlich kontrolliert.

Eine ausdrückliche Einreichungsfreigabe erfolgt ausschließlich gesondert.

20 Prüfpunkte noch offen.

&#x20;Freigabe-Checkliste kopieren

## 7. Offizielle Antragswege und regulatorische Referenzen

| Institution / Rechtsbereich | Offizieller Zugang                                                                                                                                                                                                                                                                                             | Anwendung                                                                      |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ |
| BaFin – Deutschland         | [AIF-KVG-Erlaubnisverfahren](https://bafin.de/SharedDocs/Veroeffentlichungen/DE/Merkblatt/WA/mb_130322_erlaubnisverfahren_aif-22kagb.html)                                                                                                                                              | Erlaubnis einer AIF-Kapitalverwaltungsgesellschaft nach dem KAGB               |
| Bundesportal – Deutschland  | [KVG-Erlaubnis beantragen](https://verwaltung.bund.de/leistungsverzeichnis/de/leistung/99050080005000)                                                                                                                                                                                  | Formaler Überblick über KVG-Zulassung und Registrierung                        |
| KAGB § 44                   | [Registrierung und Berichtspflichten](https://www.gesetze-im-internet.de/kagb/__44.html)                                                                                                                                                                                                | Vereinfachte Registrierung unter besonderen Voraussetzungen                    |
| CSSF – Luxemburg            | [AIFM Authorisation](https://www.cssf.lu/en/authorisation-aifm/)                                                                                                                                                                                                                        | Luxemburgisches AIFM-Verfahren, Unterlagen und eDesk-Prozess                   |
| FINMA – Schweiz             | [EHP-Zugang für Bewilligungsgesuche](https://www.finma.ch/de/finma/digitaler-austausch-mit-der-finma/ehp%2C-c-%2C-gesuche%2C-meldungen-und-daten-einreichen-oder-%C3%A4nderung-bva-%C3%BCbermitteln/kein-zugang-zur-ehp-vorhanden/bewilligung-der-finma-und-zugang-zur-ehp-beantragen/) | Selbstregistrierung für Fondsleitung, Vermögensverwalter und weitere Institute |
| FINMA – Fund Management     | [Fund Management Companies](https://www.finma.ch/en/authorisation/asset-management/fund-management-companies/)                                                                                                                                                                          | Schweizer Zulassungsanforderungen für Fondsleitungen                           |
| EU – AIFMD II               | [Richtlinie (EU) 2024/927](https://eur-lex.europa.eu/eli/dir/2024/927/oj/eng)                                                                                                                                                                                                           | Erweiterte Fondsmanageranforderungen, u. a. Delegation und Liquiditätsrisiken  |
| EU – MiCAR                  | [Verordnung (EU) 2023/1114](https://eur-lex.europa.eu/legal-content/EN/ALL/?uri=CELEX:32023R1114\&utm_source=chatgpt.com)                                                                                                                                                                                      | Zusätzliche Prüfung bei Kryptowerte- und DAO-bezogenen Dienstleistungen        |

Für den Rechtsstand November 2026 ist AIFMD II relevant: Die Umsetzungsfrist für wesentliche Änderungen war der 16. April 2026; einzelne Bestimmungen folgen später. Daher sollten die jeweils anwendbaren nationalen Umsetzungsvorschriften bei einer tatsächlichen Fondsstrukturierung berücksichtigt werden.&#x20;



EUR-Lex



## 8. Sichere Portal-Worker-Steuerung

| Workflow-Status           | Zulässige Handlung                                                  |
| ------------------------- | ------------------------------------------------------------------- |
| `PROFILE_LOADED`          | Bekannte Kontaktdaten geschützt laden                               |
| `FUND_SERVICE_CLASSIFIED` | AIF, KVG, Administration, Asset Management oder DAO unterscheiden   |
| `LEGAL_ENTITY_VALIDATION` | Rechtsträger und Vertretungsbefugnisse prüfen                       |
| `REGULATORY_SCOPE_CHECK`  | Erlaubnis-, Registrierungs- und Vertriebspflichten ermitteln        |
| `FUND_STRUCTURE_CHECK`    | Anlegerkreis, Anlagepolitik und Verantwortlichkeiten prüfen         |
| `DAO_GOVERNANCE_CHECK`    | Juristische Organisation und technische Stimmrechte unterscheiden   |
| `CUSTODY_AND_ASSET_CHECK` | Verfügungsrechte, Verwahrstellen und Kundengeldschutz kontrollieren |
| `FIELD_MAPPING`           | Belegbare Daten in die Portalvorlage zuordnen                       |
| `SENSITIVE_DATA_FILTER`   | Investorendaten, Schlüssel und vertrauliche Angaben schützen        |
| `DUPLICATE_CHECK`         | Wiederholte Anträge erkennen                                        |
| `DRAFT_READY`             | Prüfbare Anfragevorschau erstellen                                  |
| `HUMAN_REVIEW_REQUIRED`   | Persönliche Kontrolle voraussetzen                                  |
| `SUBMISSION_LOCKED`       | Keine automatische Registrierung, Fondsgründung oder Einreichung    |

## 9. Empfohlene Reihenfolge für GlobalCards

Für den derzeitigen Projektstand empfehle ich zunächst eine unverbindliche KVG-/AIFM-Strukturierungsanfrage in Deutschland, gefolgt von einem Vergleich mit Luxemburg und der Schweiz. Anschließend wären Fund Administration, Verwahrstellen- und technische DAO-Partnerschaften sinnvoll.

Der erste fachliche Meilenstein ist die Entscheidung, ob GlobalCards tatsächlich einen Investmentfonds strukturieren, eine technische Fondsadministrationsplattform anbieten oder lediglich eine Governance- und Treasury-Infrastruktur für Unternehmen entwickeln soll. Diese Entscheidung verändert das erforderliche Lizenz-, Kapital- und Organisationsmodell erheblich.

Ergebnis: Das deutschsprachige Funds-/DAO-/Asset-Management-Anschreiben, die vollständige Corporate-Feldzuordnung, die kurze Portalversion, die partnerspezifische Anfragefunktion und die separate Freigabe-Checkliste sind erstellt.

Das Dokument ist für eine unverbindliche Erstkontaktaufnahme verwendbar. Für eine tatsächliche Fondsgründung, Kapitalaufnahme, Vermögensverwaltung oder aufsichtsrechtliche Zulassung fehlen noch die gesetzlich erforderlichen Gesellschafts-, Fonds-, Kapital- und Organisationsnachweise.

Es wurde keine Registrierung, Fondsgründung, Einreichung oder Vertragsannahme durchgeführt. # GlobalCards Bank – Government / Infrastructure / Procurement

Universal Corporate & Institutional Partnership Application · Deutsch · Version 1.0 · 7. November 2026

Internationale Behördenpartnerschaften · Öffentliche Ausschreibungen · Government Technology · Finanzinfrastruktur · EU · UN · Weltbank · EBRD · NATO · Staatliche Beschaffung

Diese Fassung ist als formelle, aber unverbindliche institutionelle Erstanfrage für öffentliche Auftraggeber, internationale Organisationen, Entwicklungsbanken und staatliche Infrastrukturprogramme ausgearbeitet.

Die bekannten Projekt- und Kontaktdaten sind bereits eingetragen. Nicht bestätigte Gesellschafts-, Lizenz- und Registrierungsdaten bleiben ausdrücklich offen.

Antragsteller

Daniel Pohl

Projekt

GlobalCards Bank

Gesellschaftsstatus

Noch nicht bestätigt

Ausgangsregion

Deutschland / EWR

Antragsart

Institutionelle Voranfrage

Einreichungsstatus

Nicht eingereicht

## 1. Rechtliche Einordnung

| Verfahren                          | Bedeutung                                                                                      |
| ---------------------------------- | ---------------------------------------------------------------------------------------------- |
| Government Supplier Registration   | Registrierung als möglicher Anbieter in öffentlichen Beschaffungssystemen                      |
| RFI / EOI                          | Unverbindliche Informationsanfrage beziehungsweise Interessenbekundung                         |
| RFQ / RFP / ITB                    | Konkrete Angebots- oder Ausschreibungsverfahren mit eigenen Bedingungen                        |
| Government Technology Partnership  | Zusammenarbeit bei Software, Cybersicherheit und staatlicher Digitalisierung                   |
| Infrastructure Procurement         | Vergabe von Infrastruktur-, Entwicklungs-, Betriebs- oder Beratungsleistungen                  |
| Public-Private Partnership (PPP)   | Öffentlich-private Projektstruktur mit individuellen Verträgen und Genehmigungen               |
| Institutional Implementing Partner | Projektumsetzung im Auftrag oder Rahmen einer internationalen Organisation                     |
| Public Financial Infrastructure    | Staatliche Zahlungs- oder Finanzsysteme, deren Betrieb besondere Ermächtigungen erfordern kann |

Eine Lieferantenregistrierung verleiht keine staatliche Vertretungsbefugnis, diplomatische Immunität, allgemeine Infrastrukturlizenz oder Berechtigung zur eigenständigen Durchführung öffentlicher Projekte.

Besonders wichtig für deinen derzeitigen Gesellschaftsstatus: Das EU-Teilnehmerregister ermöglicht auch die Registrierung natürlicher Personen, soweit das jeweilige Verfahren dies zulässt. UNGM verlangt für seine reguläre Lieferantenregistrierung dagegen grundsätzlich eine entsprechend nachweisbare Unternehmensidentität.&#x20;



EU Funding & Tenders Portal+1



## 2. Vollständiges Corporate- und Government-Partnerschaftsanschreiben

# GLOBALCARDS BANK

## UNIVERSAL CORPORATE & INSTITUTIONAL GOVERNMENT, INFRASTRUCTURE & PROCUREMENT PARTNERSHIP APPLICATION

**Formelle Interessenbekundung zur öffentlichen Beschaffung, internationalen Infrastrukturentwicklung, staatlichen Digitalisierung und institutionellen Technologiepartnerschaft**

**Datum:** 7. November 2026\
**Dokumentversion:** 1.0\
**Sprache:** Deutsch\
**Antragsstatus:** Unverbindliche Erstkontaktaufnahme – persönliche Freigabe erforderlich

---

### A. Antragsteller und Projektidentität

| Feld                                          | Angabe                                                                                                                        |
| --------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Ansprechpartner                               | Daniel Pohl                                                                                                                   |
| Funktion                                      | Projektinitiator und technischer Projektkontakt                                                                               |
| Vorläufiger Projektname                       | GlobalCards Bank                                                                                                              |
| Weitere Projekt-/Organisationsbezeichnung     | Bra1nKy11 World Bank Eyes AeTHer                                                                                              |
| Zusätzliche Projektidentifikation             | HolyThreeKingsTreesCrowns                                                                                                     |
| Kontaktstandort                               | Detmold, Nordrhein-Westfalen, Deutschland                                                                                     |
| Kontakt-E-Mail                                | [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu) |
| Rechtlich registriertes Unternehmen           | Noch nicht bestätigt                                                                                                          |
| Gesellschaftsform                             | Noch nicht bestätigt                                                                                                          |
| Eingetragener Gesellschaftssitz               | Noch nicht bestätigt                                                                                                          |
| Handelsregisternummer                         | Nicht bereitgestellt                                                                                                          |
| Umsatzsteuer-ID des Unternehmens              | Nicht bereitgestellt                                                                                                          |
| Legal Entity Identifier (LEI)                 | Nicht bereitgestellt                                                                                                          |
| EU Participant Identification Code (PIC)      | Für dieses Vorhaben nicht bestätigt                                                                                           |
| UNGM Supplier Registration Number             | Für dieses Vorhaben nicht bestätigt                                                                                           |
| US Unique Entity ID (UEI)                     | Nicht bereitgestellt                                                                                                          |
| NATO CAGE / NCAGE                             | Nicht bereitgestellt                                                                                                          |
| Bestehende öffentliche Auftraggeberverträge   | Für dieses Vorhaben nicht bestätigt                                                                                           |
| Staatliches Infrastrukturmandat               | Nicht nachgewiesen                                                                                                            |
| Behördenzulassung oder Akkreditierung         | Nicht nachgewiesen                                                                                                            |
| Bestehende Bank- oder Zahlungsinstitutslizenz | Nicht nachgewiesen                                                                                                            |
| Projektstatus                                 | Konzeption und technische Vorbereitung                                                                                        |
| Ausgangsmarkt                                 | Deutschland und Europäischer Wirtschaftsraum                                                                                  |
| Internationale Zusammenarbeit                 | Geplant, abhängig von Eignung und jeweiligen Genehmigungen                                                                    |

**Rechtliche Klarstellung:** Die angegebenen Namen dienen der Projektidentifikation und stellen keine Behauptung einer bestehenden Gesellschaftsregistrierung, staatlichen Zugehörigkeit, Banklizenz, Regierungsbeauftragung oder Partnerschaft mit der Weltbank beziehungsweise einer anderen internationalen Organisation dar.

Die Projektbezeichnung „GlobalCards Bank“ wird vorläufig verwendet und bedarf vor geschäftlicher Nutzung einer gesonderten rechtlichen Prüfung.

### B. Empfänger und Betreff

**An:** Procurement Department / Government Partnerships / Institutional Relations / Infrastructure Development / Supplier Registration / Technology Partnerships

**Empfängerorganisation:** Zuständige öffentliche oder institutionelle Organisation; für jede tatsächliche Kontaktaufnahme individuell auszuwählen.

**Betreff:** Formelle Corporate- und Government-Partnerschaftsanfrage – GlobalCards Bank | Öffentliche Beschaffung, Finanzinfrastruktur, GovTech, Cybersecurity und internationale Technologieintegration

### C. Formelle Vorstellung

Sehr geehrte Damen und Herren,

hiermit möchte ich mein Interesse an einer möglichen institutionellen, technischen und geschäftlichen Zusammenarbeit mit Ihrer Organisation im Bereich öffentlicher Beschaffung, internationaler Infrastrukturentwicklung, staatlicher Digitalisierung und sicherer Finanztechnologie zum Ausdruck bringen.

Unter der vorläufigen Projektbezeichnung **GlobalCards Bank** bereite ich die Konzeption einer modularen internationalen Finanztechnologie- und Infrastrukturplattform vor.

Das Vorhaben verbindet die technische Entwicklung von Finanz-, Zahlungs-, Identitäts-, Sicherheits- und Governance-Komponenten mit dem Ziel, standardisierte und nachvollziehbare Schnittstellen für unterschiedliche öffentliche und privatwirtschaftliche Anwendungsbereiche bereitzustellen.

Im Rahmen einer möglichen institutionellen Zusammenarbeit möchte ich insbesondere prüfen, ob Ihre Organisation geeignete Lieferantenregistrierungen, Entwicklerprogramme, Technologiepartnerschaften, Ausschreibungsverfahren, Innovationsprogramme oder Möglichkeiten für eine spätere Projektbeteiligung anbietet.

Ein besonderer Schwerpunkt liegt auf der Entwicklung sicherer, interoperabler und datenschutzorientierter IT-Infrastruktur.

Die rechtliche Unternehmensstruktur und die jeweiligen Voraussetzungen einer konkreten Projektteilnahme sollen vor dem Beginn vertraglicher Verpflichtungen geklärt werden.

Diese Anfrage dient ausschließlich der unverbindlichen Prüfung möglicher Kooperationsformen.

### D. Strategisches Projekt- und Leistungsmodell

**Projektbezeichnung:** GlobalCards Bank

**Vorgesehenes Geschäftsmodell:** Hybride internationale B2C-/B2B-Finanztechnologieplattform mit möglichen institutionellen Technologie- und Infrastrukturkomponenten.

**Geografischer Ausgangspunkt:** Deutschland und Europäischer Wirtschaftsraum.

**Mögliche Erweiterung:** Weitere europäische und internationale Märkte, jeweils vorbehaltlich der rechtlichen, technischen und institutionellen Voraussetzungen.

Für die Entwicklung und mögliche Bereitstellung werden insbesondere folgende Bereiche untersucht:

1. Digitale Finanz- und Zahlungsinfrastruktur
2. Sichere API- und Systemintegration
3. Finanztransaktions- und Settlement-Technologie
4. Identitäts- und Zugriffsmanagement
5. Digitale Vertrauens- und Nachweissysteme
6. Governance-, Risiko- und Compliance-Plattformen
7. Cybersecurity und Informationssicherheit
8. Datenintegrität, Datenschutz und technische Nachweisführung
9. Interoperabilität zwischen öffentlichen und privaten Systemen
10. Digitale Unternehmens- und Verwaltungsprozesse
11. Transparente Audit- und Reporting-Verfahren
12. Modulare Infrastrukturentwicklung und technische Modernisierung

Die genannten Bereiche stellen geplante Fähigkeiten beziehungsweise Entwicklungsziele dar. Eine bestehende operative Leistungsfähigkeit in jedem einzelnen Bereich wird nicht behauptet.

### E. Angefragte institutionelle Kooperationsmodelle

**Modell A – Government Supplier / Public Procurement**

Prüfung einer möglichen Registrierung als Lieferant oder technischer Dienstleister zur Teilnahme an geeigneten öffentlichen Ausschreibungsverfahren.

Mögliche Leistungsfelder:

- Softwareentwicklung
- IT-Systemintegration
- Finanztechnologie
- Cybersecurity
- Infrastrukturmodernisierung
- Technische Beratung
- Datenmanagement und Governance
- API-Entwicklung und Interoperabilität

**Modell B – Government Technology Partnership**

Prüfung technischer Zusammenarbeit zur Entwicklung oder Integration geeigneter Komponenten für öffentliche digitale Dienste.

**Modell C – Institutional Infrastructure Development**

Prüfung möglicher Technologie- und Infrastrukturprojekte mit staatlichen, supranationalen oder öffentlich finanzierten Auftraggebern.

**Modell D – Financial Infrastructure Partnership**

Prüfung der technischen Zusammenarbeit bei Zahlungsverkehr, Finanzsystemintegration, Transaktionsabgleich, digitalen Identitäten und regulatorischen Kontrollsystemen.

**Modell E – Public-Private Partnership**

Unverbindliche Evaluierung öffentlich-privater Kooperationsmodelle, sofern ein entsprechendes Projekt, Vergabeverfahren und gesetzlich zulässiger Rahmen bestehen.

**Modell F – Institutional Research & Innovation**

Mögliche Beteiligung an Forschung, technischer Machbarkeitsprüfung, Standardisierung, Pilotprojekten und Innovationsprogrammen.

**Modell G – Developer / Technical Sandbox**

Zugang zu geeigneten öffentlichen Entwicklerressourcen, Testumgebungen, offenen Schnittstellen und technischen Dokumentationen.

Die konkrete Auswahl erfolgt ausschließlich anhand der tatsächlichen Programm- und Eignungsvoraussetzungen der jeweiligen Institution.

### F. Internationale Infrastruktur- und Rollout-Strategie

GlobalCards soll perspektivisch eine modular einsetzbare technische Architektur erhalten, die bei entsprechender Beauftragung und nach den erforderlichen Genehmigungen an unterschiedliche nationale Anforderungen angepasst werden kann.

Mögliche technische Tätigkeiten:

- Infrastruktur- und Anforderungsanalyse
- Schnittstellenentwicklung
- Systemintegration
- Technische Sicherheitsprüfung
- Pilot- und Sandbox-Implementierung
- Entwicklung von Daten- und Prozessmodellen
- Lokalisierung von Software und Verwaltungsprozessen
- Technische Dokumentation
- Implementierungs- und Migrationstests
- Schulung und Wissenstransfer
- Unterstützende Compliance-Nachweisführung
- Technische Wartung und Weiterentwicklung

Ein internationaler Rollout setzt stets die notwendigen Verträge, Zulassungen, Datenschutzprüfungen und gegebenenfalls nationalen Infrastruktur- und Sicherheitsgenehmigungen voraus.

Mit dieser Anfrage wird keine allgemeine Berechtigung zur Errichtung oder zum Betrieb öffentlicher Infrastruktur beansprucht.

### G. Government Finance & Public Payment Infrastructure

Für mögliche künftige institutionelle Technologieprojekte können folgende Bereiche fachlich geprüft werden:

- Digitale Zahlungsverkehrsinfrastruktur
- SEPA- und internationale Zahlungsintegration
- Finanztransaktionsabgleich und Reconciliation
- Buchungs- und Ledger-Technologie
- Finanzdaten-Schnittstellen
- Verwaltung technischer Zahlungsreferenzen
- Auswertungs- und Reporting-Systeme
- Kontrollierte Treasury- und Liquiditätsinformationen
- Risikomanagement- und Compliance-Werkzeuge
- Technische Nachweise und Auditprozesse

Die Bereitstellung staatlicher Zahlungsverkehrsdienste, der Zugriff auf Zentralbanksysteme, die Verwaltung öffentlicher Gelder und regulierte Finanzdienstleistungen würden gesonderte rechtliche und institutionelle Berechtigungen erfordern.

Die vorliegende Anfrage betrifft zunächst ausschließlich mögliche technische Dienstleistungen und Partnerschaften.

### H. Government Identity & Digital Trust

Für mögliche Technologiekooperationen werden außerdem folgende Bereiche untersucht:

1. Sichere digitale Identitätsverwaltung
2. Unternehmensidentitäten
3. Authentifizierungs- und Autorisierungsverfahren
4. Digitale Berechtigungsnachweise
5. Verifizierbare elektronische Nachweise
6. Organisatorische und technische Zugriffssteuerung
7. Föderierte Identitäts- und Vertrauensmodelle
8. Auditierbare Berechtigungsentscheidungen
9. Schnittstellen zu bestehenden staatlichen Identitäts- und Vertrauensdiensten
10. Technische Integritäts- und Herkunftsnachweise

Die Einbindung staatlicher Identitätsdienste würde nur über offiziell freigegebene Schnittstellen, Berechtigungen und Verträge erfolgen.

Eine staatliche Identität, Behördenrolle oder hoheitliche Befugnis wird dadurch nicht beansprucht.

### I. Cybersecurity, Compliance und Datenhoheit

Die technische Architektur soll nach einem sicherheitsorientierten Entwicklungsmodell konzipiert werden.

Geplante Prüf- und Implementierungsbereiche:

- Security by Design
- Datenschutz und Datenminimierung
- Zero-Trust-Zugriffskontrollen
- Rollen- und berechtigungsabhängige Systemzugriffe
- Sichere API-Authentifizierung
- Kryptografischer Schutz sensibler Informationen
- Trennung von Test- und Produktionsdaten
- Software-Lieferkettensicherheit
- Schwachstellen- und Risikomanagement
- Audit- und Evidenzmanagement
- Business Continuity und Incident Response
- Kontrollierte technische Änderungsverfahren
- Transparente Verantwortlichkeiten für Dienstleister

Je nach Auftraggeber, Datenkategorie und eingesetzter Infrastruktur sollen zusätzlich einschlägige nationale und internationale Vorgaben geprüft werden.

### J. Technische Referenzarchitektur

Die geplante Projektarchitektur umfasst folgende mögliche Module:

1. Institutional Identity & Access Management
2. Corporate and Organization Registry
3. Government / Enterprise API Gateway
4. Banking and Payment Connectivity
5. Financial Transaction Orchestration
6. Ledger and Reconciliation
7. Digital Trust & Credential Integration
8. Cybersecurity Control Engine
9. Regulatory & Compliance Mapping
10. Procurement Workflow Integration
11. Contract and Project Administration
12. Audit & Evidence Registry
13. Data Classification and Access Governance
14. Partner and Infrastructure Connectivity
15. Technical Reporting and Monitoring
16. International Localization Layer
17. Developer and Test Environment
18. Institutional Administration Dashboard

Die technische Realisierung soll schrittweise und anhand nachprüfbarer Anforderungen erfolgen.

Für frühe Entwicklungstests sind synthetische Daten, kontrollierte Testumgebungen und ausdrücklich freigegebene Schnittstellen vorgesehen.

### K. Öffentliche Beschaffung und Teilnahmevoraussetzungen

Ich bitte um Prüfung, welche formellen Anforderungen für eine mögliche Lieferanten- oder Projektpartnerregistrierung gelten.

Hierzu zählen gegebenenfalls:

- Registrierte juristische Person oder zulässige natürliche Person
- Handelsregister- beziehungsweise Unternehmensnachweis
- Steuerliche Identifikation
- Wirtschaftlich berechtigte Personen
- Geeignete Lieferanten- und Unternehmensidentifikatoren
- Klassifikation angebotener Waren und Dienstleistungen
- Informationen zur finanziellen und wirtschaftlichen Leistungsfähigkeit
- Referenzen und nachweisbare technische Fähigkeiten
- Ausschluss- und Sanktionsprüfungen
- Eignungs- und Zuverlässigkeitserklärungen
- Sicherheits- und Datenschutzanforderungen
- Erklärung über mögliche Interessenkonflikte
- Akzeptanz der jeweils geltenden Beschaffungsbedingungen

Nicht vorhandene Identifikatoren, Abschlüsse, Versicherungen, Zertifikate oder Referenzprojekte werden nicht durch fiktive Angaben ersetzt.

### L. Internationales Regelwerk und Governance

Für eine mögliche Zusammenarbeit sollen insbesondere die tatsächlich einschlägigen Vorgaben geprüft werden:

- Anwendbares nationales Vergaberecht
- Europäisches Vergaberecht, soweit einschlägig
- Haushalts- und Zuwendungsrecht
- Korruptionsprävention und Integritätsanforderungen
- Datenschutz-Grundverordnung
- Informationssicherheits- und Cybersicherheitsvorschriften
- Anforderungen an kritische Infrastrukturen, soweit einschlägig
- Exportkontrollen und Sanktionen
- Regeln der jeweiligen Entwicklungsbank oder internationalen Organisation
- Vorgaben zu Interessenkonflikten und Ausschlussgründen
- Anwendbare Nachhaltigkeits- und Lieferkettenpflichten
- Vertrags-, Leistungs- und Haftungsregelungen
- Relevante Finanzaufsichtsvorschriften bei regulierten Finanzsystemen

Die konkrete Anwendbarkeit soll für jedes Projekt und jede zuständige Jurisdiktion separat festgestellt werden.

Es wird nicht behauptet, dass bereits alle genannten Standards erfüllt, zertifiziert oder behördlich bestätigt sind.

### M. Gewünschte Corporate- und Government-Zugänge

Ich bitte um Informationen über:

1. Lieferantenregistrierung und Supplier Onboarding
2. Corporate- und Institutional-Partnerprogramme
3. Technische Dienstleisterregistrierung
4. Öffentliche Ausschreibungen und Procurement Portale
5. RFI-, EOI-, RFQ-, RFP- und ITB-Verfahren
6. Möglichkeiten einer unverbindlichen Interessenbekundung
7. Projekt- und Innovationspartnerschaften
8. Entwickler- und Sandbox-Programme
9. Infrastruktur- und Systemintegrationsprojekte
10. Anforderungen an internationale Lieferanten
11. Technische Qualifikations- und Sicherheitsprüfungen
12. Informationen über Partnerkonsortien
13. Anforderungen an finanzielle Leistungsfähigkeit
14. Zuständige Procurement- oder Institutional-Relations-Ansprechpartner

### N. Kommerzielle und vertragliche Fragen

Ich bitte, soweit möglich, um Auskunft zu:

- Kosten der Lieferantenregistrierung
- Kosten und Bedingungen einer Teilnahme an Ausschreibungen
- Erforderlichen Gesellschaftsnachweisen
- Wirtschaftlichen Mindestanforderungen
- Technischen Mindestqualifikationen
- Vertrags- und Vergabeverfahren
- Möglichkeiten der Beteiligung als Unterauftragnehmer
- Anforderungen an Bietergemeinschaften
- Versicherungen und Vertragssicherheiten
- Daten- und Informationssicherheitsanforderungen
- Abnahme- und Leistungskriterien
- Wartungs- und Supportanforderungen
- Zahlungs- und Rechnungsbedingungen
- Haftungs- und Gewährleistungsregelungen
- Anforderungen an internationale Niederlassungen oder lokale Vertreter

Für das Vorhaben werden derzeit keine bestätigten Auftragsumsätze, abgeschlossenen Regierungsverträge oder bereits gewonnenen Ausschreibungen geltend gemacht.

### O. Sonderfälle: Staatliche Infrastruktur und institutionelle Berechtigungen

Soweit Ihre Organisation besondere staatliche, finanzielle oder sicherheitsbezogene Infrastruktur betreibt, bitte ich um Hinweise zu den entsprechenden rechtlichen und institutionellen Verfahren.

Dies kann beispielsweise betreffen:

- Staatliche Finanzsysteme
- Öffentliche Zahlungsinfrastruktur
- Digitale Behördenidentitäten
- Sicherheitskritische Informationssysteme
- Internationale Infrastrukturprojekte
- Technische Vertrauensregister
- Institutionelle Daten- und Kommunikationssysteme

Die Durchführung entsprechender Projekte setzt eine gültige Beauftragung sowie alle erforderlichen Sicherheits-, Zugangs-, Datenschutz- und gegebenenfalls sektoralen Genehmigungen voraus.

Die bloße Lieferantenregistrierung wird nicht als entsprechende Berechtigung verstanden.

### P. Erklärung zu staatlichem und internationalem Status

Zum Zeitpunkt dieser Anfrage wird ausdrücklich nicht behauptet, dass GlobalCards:

- bereits ein rechtlich registriertes Unternehmen ist,
- ein staatlich zugelassener Infrastrukturbetreiber ist,
- eine bestehende Regierungsbeauftragung besitzt,
- ein offizieller Vertreter einer Regierung oder internationalen Organisation ist,
- eine Partnerschaft mit der Europäischen Union, den Vereinten Nationen, der Weltbank, der NATO oder anderen Institutionen nachgewiesen hat,
- eine Diplomatenakkreditierung oder Immunität besitzt,
- öffentliche Gelder verwalten darf,
- bereits als autorisierter Regierungsauftragnehmer bestätigt ist,
- Zugang zu geschützten staatlichen IT-Systemen besitzt,
- eine pauschale internationale Infrastruktur- oder Sicherheitsgenehmigung erhalten hat.

Diese Interessenbekundung ist keine Selbstzertifizierung, keine verbindliche Angebotsabgabe und kein Antrag auf staatliche Hoheitsbefugnisse.

### Q. Datenschutz, Integrität und Vertraulichkeit

Ich bitte darum, übermittelte personenbezogene und projektbezogene Informationen ausschließlich zur Bearbeitung dieser Anfrage und für gegebenenfalls rechtlich erforderliche Prüfungen zu verwenden.

Vertrauliche technische Dokumente, Identitätsnachweise, Finanzunterlagen, Zugangsdaten oder sicherheitsrelevante Informationen sollen erst nach gesonderter Prüfung der zuständigen Institution und über geeignete sichere Kommunikationswege bereitgestellt werden.

Im Rahmen dieser Erstkontaktaufnahme werden keine Produktionskundendaten, privaten Schlüssel, Passwörter oder vertraulichen Zugangsinformationen übermittelt.

### R. Gewünschter nächster Schritt

Ich würde mich über eine erste Rückmeldung zur grundsätzlichen Eignung des beschriebenen Projekts für eine Lieferanten-, Technologie- oder institutionelle Partnerschaft freuen.

Besonders hilfreich wären:

1. Der zuständige Ansprechpartner für Corporate oder Government Procurement.
2. Ein direkter Link zum offiziellen Lieferanten- oder Partnerportal.
3. Informationen zur Teilnahmeberechtigung vor und nach einer Unternehmensgründung.
4. Eine Übersicht der notwendigen Registrierungs- und Qualifikationsnachweise.
5. Hinweise auf geeignete Beschaffungs- und Innovationsprogramme.
6. Informationen über mögliche technische Test- oder Entwicklerzugänge.
7. Die Voraussetzungen für eine spätere Teilnahme an konkreten Ausschreibungen.
8. Angaben zu möglichen kommerziellen, technischen und rechtlichen Anforderungen.

Ich strebe eine transparente, regelkonforme und langfristig tragfähige Zusammenarbeit im Bereich internationaler Finanz-, Digital- und Infrastrukturtechnologien an.

Mit freundlichen Grüßen

**Daniel Pohl**\
Projektinitiator und technischer Projektkontakt

**GlobalCards Bank** – vorläufige Projektbezeichnung\
**Bra1nKy11 World Bank Eyes AeTHer** – Projekt-/Organisationsbezeichnung\
**HolyThreeKingsTreesCrowns** – zusätzliche Projektidentifikation

Detmold, Nordrhein-Westfalen, Deutschland

**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

---

**Dokumentstatus:** Unverbindliche institutionelle Erstanfrage zur persönlichen Prüfung.

**Keine automatische Registrierung, Lieferantenzulassung, Ausschreibungsabgabe, Vertragsannahme oder Übermittlung.**

## 3. Universelle Feldzuordnung für Government- und Procurement-Portale

Die Feldzuordnung ist für deinen Portal-Worker konzipiert. Sie trennt persönliche Kontaktdaten, Projektinformationen, rechtliche Gesellschaftsdaten und nachweispflichtige Eignungsangaben.

| Corporate-Portal-Feld (EN)       | GlobalCards-Eintrag                                        | Verarbeitungsregel                               |
| -------------------------------- | ---------------------------------------------------------- | ------------------------------------------------ |
| First Name                       | Daniel                                                     | Übernehmen                                       |
| Last Name                        | Pohl                                                       | Übernehmen                                       |
| Contact Email                    | world.banks.eyes.aether\@globedynamicz.statesflowwishes.eu | Übernehmen                                       |
| Job Title                        | Project Initiator / Technical Project Contact              | Keine Organstellung behaupten                    |
| Project Name                     | GlobalCards Bank                                           | Vorläufige Bezeichnung                           |
| Organization Designation         | Bra1nKy11 World Bank Eyes AeTHer                           | Nur Projektbezeichnung                           |
| Legal Entity Name                | Noch nicht bestätigt                                       | Pflichtprüfung                                   |
| Legal Entity Type                | Noch nicht bestätigt                                       | Keine Rechtsform erfinden                        |
| Certificate of Incorporation     | Nicht bereitgestellt                                       | Nachweis erforderlich                            |
| Company Registration Number      | Nicht bereitgestellt                                       | Nicht erfinden                                   |
| Registered Office Address        | Nicht bestätigt                                            | Nicht aus Kontaktort ableiten                    |
| Contact City                     | Detmold                                                    | Übernehmen                                       |
| State / Region                   | Nordrhein-Westfalen                                        | Übernehmen                                       |
| Country                          | Germany                                                    | Übernehmen                                       |
| Corporate Website                | Nicht bereitgestellt                                       | Offenlassen                                      |
| VAT / Tax Identification         | Nicht bereitgestellt                                       | Geschützte Prüfung                               |
| EU Participant PIC               | Für dieses Vorhaben nicht bestätigt                        | Bestehende Registrierung vor Neuerfassung prüfen |
| UNGM Supplier Number             | Nicht bestätigt                                            | Nicht erfinden                                   |
| Unique Entity ID (UEI)           | Nicht bereitgestellt                                       | Bei Bedarf beantragen                            |
| CAGE / NCAGE Code                | Nicht bereitgestellt                                       | Nicht erfinden                                   |
| LEI                              | Nicht bereitgestellt                                       | Nur falls erforderlich                           |
| Business Sector                  | Fintech / IT Infrastructure / GovTech                      | Als Projektgebiet                                |
| Organization Type                | Noch nicht bestätigt                                       | Keine Regierungsorganisation auswählen           |
| Company Size                     | Nicht bestätigt                                            | Offenlassen                                      |
| Number of Employees              | Nicht bereitgestellt                                       | Nicht erfinden                                   |
| Annual Revenue                   | Keine verifizierten Angaben                                | Offenlassen                                      |
| Financial Statements             | Nicht bereitgestellt                                       | Keine Abschlüsse fingieren                       |
| Government Contract History      | Für dieses Vorhaben nicht bestätigt                        | Keine Referenzen erfinden                        |
| Government Affiliation           | Keine nachgewiesene amtliche Zugehörigkeit                 | Nicht als Behördenmitglied ausgeben              |
| Procurement Interest             | Government Technology / Infrastructure / IT                | Übernehmen                                       |
| Target Regions                   | Germany / EEA / International                              | Als Interessensgebiet                            |
| Supplier Category                | Software / IT / Financial Technology                       | An tatsächliche Leistungen anpassen              |
| UNSPSC Codes                     | Noch nicht einzeln validiert                               | Passende Codes nach Tätigkeit auswählen          |
| CPV Codes                        | Noch nicht validiert                                       | EU-Ausschreibungsspezifisch zuordnen             |
| NAICS Codes                      | Noch nicht validiert                                       | Für US-Verfahren prüfen                          |
| Security Clearance               | Nicht nachgewiesen                                         | Nicht behaupten                                  |
| ISO Certification                | Keine bestätigte Zertifizierung                            | Nicht erfinden                                   |
| Professional Liability Insurance | Nicht bestätigt                                            | Nachweis prüfen                                  |
| Sanctions / Exclusions           | Keine geprüfte Eigenerklärung vorliegend                   | Nicht automatisch bescheinigen                   |
| Beneficial Owners                | Nicht bereitgestellt                                       | Geschützter Nachweis                             |
| Authorized Signatory             | Noch nicht bestätigt                                       | Formelles Verfahren blockieren                   |
| Developer Access                 | Requested                                                  | Übernehmen                                       |
| Supplier Registration            | Requested / Under Evaluation                               | Nicht als abgeschlossen darstellen               |
| Awarded Contract                 | Nicht nachgewiesen                                         | Keine Zuschlagserteilung behaupten               |
| Tender Reference                 | Noch kein konkretes Verfahren ausgewählt                   | Nicht erfinden                                   |

### 3.1 Portalabhängige Sonderfelder

| Portaltyp                     | Zusätzliche Pflichtinformationen                                                                                        |
| ----------------------------- | ----------------------------------------------------------------------------------------------------------------------- |
| EU Funding & Tenders          | EU Login, PIC, Rechtsträgerprüfung, Projekt-/Ausschreibungsreferenz, Rollen und Bevollmächtigungen                      |
| UNGM                          | Rechtsname, Unternehmensidentifikator, Länder, UNSPSC-Klassifikation, Supplier Code of Conduct, Eligibility Declaration |
| Weltbank / Entwicklungsbanken | Rechtsform, Projektreferenzen, wirtschaftliche Leistungsfähigkeit, Eigentumsverhältnisse                                |
| EBRD ECEPP                    | Kontaktrolle, Lieferantenidentität, technische Angaben und englischsprachige Registrierungsdaten                        |
| NATO Procurement              | Zulässige Lieferantenkategorie, Unternehmensnachweise, gegebenenfalls Sicherheits- und Herkunftsvoraussetzungen         |
| USA SAM.gov                   | Rechtsname, Anschrift, UEI, Steuer- und Unternehmensdaten, NAICS, representations and certifications                    |
| Government Innovation         | Projektskizze, Innovationsgrad, technische Reife, Pilotziele und gegebenenfalls Konsortialstruktur                      |
| PPP / Infrastrukturprojekt    | Auftraggeber, Rechtsraum, Machbarkeitsstudie, Finanzierungsstruktur, technische Kapazität, Genehmigungen                |

Bei UNGM sind UNSPSC-Codes, die Lieferanten-Verhaltensregeln und die Eignungserklärung Teil der Grundregistrierung. Der rechtliche Firmenname muss mit den Unternehmensnachweisen übereinstimmen.&#x20;



UNGM Help Center+1



## 4. Kompakte Version für Corporate-Registrierungsformulare

Diese Version ist für kurze Textfelder wie Describe Your Organization, Partnership Request, Supplier Introduction oder Expression of Interest geeignet.

**Betreff: Government / Infrastructure / Procurement Partnership Request – GlobalCards Bank**

Sehr geehrte Damen und Herren,

als Projektinitiator von GlobalCards Bank interessiere ich mich für eine mögliche institutionelle Zusammenarbeit im Bereich staatlicher Digitalisierung, internationaler Finanztechnologie, sicherer IT-Infrastruktur, öffentlicher Beschaffung und Government Technology.

GlobalCards ist als hybride, API-basierte Finanz- und Infrastrukturplattform für Privatkunden, Unternehmen und mögliche institutionelle Technologieanwendungen geplant.

Im Mittelpunkt stehen die Entwicklung modularer Schnittstellen, sicherer Zahlungs- und Finanzdatenintegrationen, digitaler Identitäts- und Governance-Systeme, Cybersecurity, Compliance und nachvollziehbarer technischer Infrastrukturprozesse.

Ich möchte prüfen, ob Ihre Organisation Möglichkeiten zur Lieferantenregistrierung, unverbindlichen Interessenbekundung, Technologiepartnerschaft, Beteiligung an geeigneten Ausschreibungen oder zum Zugang zu Entwickler- und Testumgebungen anbietet.

Der rechtliche Gesellschaftsstatus ist derzeit noch nicht bestätigt. Es werden keine bestehenden staatlichen Mandate, Finanzlizenzen, behördlichen Zulassungen, öffentlichen Aufträge oder institutionellen Partnerschaften beansprucht.

Ich bitte um Informationen zu den Aufnahmevoraussetzungen, erforderlichen Unternehmensnachweisen, möglichen Partnerprogrammen und zuständigen Ansprechpartnern.

Mit freundlichen Grüßen

**Daniel Pohl**\
Projektinitiator und technischer Projektkontakt\
**GlobalCards Bank** – vorläufige Projektbezeichnung\
**Bra1nKy11 World Bank Eyes AeTHer** – Projekt-/Organisationsbezeichnung

Detmold, Nordrhein-Westfalen, Deutschland\
[world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

Diese Anfrage ist unverbindlich und stellt keine formelle Angebotsabgabe oder rechtsverbindliche Lieferantenerklärung dar.

## 5. Direkte offizielle Registrierungs- und Beschaffungsportale

| Institution           | Direkter Zugang                                                                                                                                                                             | Bedeutung für GlobalCards                                                             |
| --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------- |
| EU-Kommission         | [EU Participant Register – Organisation registrieren](https://ec.europa.eu/info/funding-tenders/opportunities/portal/screen/how-to-participate/participant-register) | PIC-Registrierung und Vorbereitung von EU-Förder- und Ausschreibungsverfahren         |
| UN Global Marketplace | [UNGM – Supplier Account Registration](https://help.ungm.org/hc/en-us/articles/360012810860-How-to-create-a-supplier-account-on-UNGM)                                | Vorbereitung einer UN-Lieferantenregistrierung                                        |
| EBRD                  | [ECEPP – Direct Supplier Sign-up](https://ecepp.ebrd.com/delta/signup.html?userType=supplier\&utm_source=chatgpt.com)                                                                       | Anmeldung für öffentliche Infrastrukturprojekte, die über ECEPP ausgeschrieben werden |
| USA – SAM.gov         | [Entity Registration / UEI](https://sam.gov/entity-registration)                                                                                                     | US-Lieferantenidentifikation und staatliche Vergabeverfahren                          |

Die EU vergibt über das Participant Register eine neunstellige PIC-Kennung; die Angaben werden bei Bedarf vor Vertragsabschluss validiert. Die Registrierung allein bedeutet noch keinen öffentlichen Auftrag.&#x20;



EU Funding & Tenders Portal



UNGM ist in der Grundregistrierung kostenlos, setzt aber für reguläre Lieferanten eine entsprechende Unternehmensidentität voraus. Auch die US-Registrierung über SAM.gov ist offiziell gebührenfrei.&#x20;



UNGM Help Center+2



Die EBRD stellt ihr ECEPP-Verfahren kostenlos bereit und lässt Anbieter, Berater und Auftragnehmer für geeignete Projekte zu; die direkte Registrierungsmaske verlangt Eingaben auf Englisch.&#x20;



We invest in changing lives+1



## 6. Separate Freigabe-Checkliste

Die Checkliste dient der persönlichen Qualitäts- und Rechtsprüfung. Sie löst keine Registrierung, Übermittlung oder vertragliche Erklärung aus.

Government Procurement – Freigabestatus

0 / 20

A. Corporate & Identität

Kontaktperson, Projektname und E-Mail-Adresse sind korrekt.

Die Projektbezeichnung wird nicht als registrierter Rechtsträger dargestellt.

Es werden keine PIC-, UNGM-, UEI-, CAGE- oder anderen Nummern erfunden.

Die tatsächliche Vertretungsbefugnis wird vor verbindlichen Erklärungen geprüft.

B. Government & Procurement

Die zuständige Institution und deren Beschaffungsverfahren wurden identifiziert.

Lieferantenregistrierung, Interessenbekundung und formelles Angebot werden unterschieden.

Es werden keine bereits gewonnenen staatlichen Aufträge oder Partnerschaften behauptet.

UNSPSC-, CPV- oder NAICS-Kategorien entsprechen nachweisbaren oder geplanten Leistungen.

C. Infrastruktur & Sicherheitsstatus

Geplante IT- und Finanzinfrastrukturleistungen werden nicht als bereits produktiv dargestellt.

Es werden keine staatlichen Betriebsberechtigungen oder Sicherheitsfreigaben beansprucht.

Behördliche Identitäten und staatliche Infrastruktursysteme werden nur über autorisierte Verfahren angesprochen.

Technische und regulatorische Nachweise sind nicht erfunden.

D. Compliance & Datenschutz

Sanktions-, Ausschluss- und Interessenkonflikterklärungen werden wahrheitsgemäß geprüft.

Verhaltenskodizes und vertragliche Bedingungen wurden vor einer Zustimmung gelesen.

Keine Passwörter, Schlüssel, Produktions- oder vertraulichen Kundendaten werden übertragen.

Das offizielle Portal und der tatsächliche Datenempfänger sind verifiziert.

E. Persönliche Freigabe

Der Antrag wurde auf einen konkreten Empfänger zugeschnitten.

Alle nachweispflichtigen Pflichtfelder sind geklärt oder für das Verfahren als offen gekennzeichnet.

Gebühren, finanzielle Verpflichtungen und erforderliche Unterlagen wurden überprüft.

Eine ausdrückliche, gesonderte Versandfreigabe für genau diese Anfrage liegt vor.

20 Prüfpunkte noch offen.

&#x20;Freigabe-Checkliste kopieren

## 7. Partnerabhängige Anfrage für den Portal-Worker

Institutionelle ZielorganisationEuropäische Union / EU-Kommission

Partnerfokus

EU Participant Register, öffentliche Ausschreibungen, GovTech, Digital Infrastructure und Innovationsprogramme

Zentrale Eignungsfrage

Welche Teilnahme- und Rechtsformvoraussetzungen gelten für eine erste Interessenbekundung beziehungsweise die spätere Registrierung als zulässiger Projektteilnehmer?

&#x20;Institutionsbezogene Kurzanfrage kopieren

## 8. Sichere Automatisierungsregeln

| Workflow-Status                | Zulässige Handlung                                                                    |
| ------------------------------ | ------------------------------------------------------------------------------------- |
| `PROFILE_LOADED`               | Vorhandene Kontaktdaten geschützt übernehmen                                          |
| `GOVERNMENT_PORTAL_CLASSIFIED` | Beschaffungs-, Förder-, Partnerschafts- oder Behördenportal unterscheiden             |
| `ENTITY_ELIGIBILITY_CHECK`     | Prüfen, ob natürliche Personen oder nur registrierte Unternehmen zugelassen sind      |
| `SUPPLIER_ID_CHECK`            | PIC, UNGM, UEI und weitere IDs auf Nachweis prüfen                                    |
| `PROCUREMENT_CLASSIFICATION`   | Nur zutreffende UNSPSC-/CPV-/NAICS-Kategorien vorschlagen                             |
| `SERVICE_CAPABILITY_CHECK`     | Geplante und nachgewiesene Fähigkeiten unterscheiden                                  |
| `LEGAL_DECLARATION_CHECK`      | Ausschlussgründe, Sanktionen, Compliance und Interessenkonflikte zur Prüfung vorlegen |
| `FIELD_MAPPING`                | Erlaubte Angaben dem jeweiligen Portal zuordnen                                       |
| `SENSITIVE_DATA_FILTER`        | Zugangsdaten, Schlüssel und vertrauliche Unterlagen ausschließen                      |
| `DUPLICATE_CHECK`              | Bereits bestehende Entwürfe und Registrierungsnummern prüfen                          |
| `DRAFT_READY`                  | Vollständige Vorschau erzeugen                                                        |
| `HUMAN_REVIEW_REQUIRED`        | Persönliche Kontrolle aller verpflichtenden Erklärungen verlangen                     |
| `SUBMISSION_LOCKED`            | Keine automatische Übermittlung, Vertragsannahme oder Ausschreibungsabgabe            |

### Empfohlene Reihenfolge

Für den aktuellen Projektstand würde ich zuerst EU Participant Register und EBRD ECEPP hinsichtlich ihrer individuellen Teilnahmevoraussetzungen prüfen. Danach folgt eine UNGM-Eignungsprüfung der konkreten Rechtsträgerstruktur und anschließend die Auswahl relevanter internationaler Beschaffungsverfahren.

Der Grund: Mit einer unverbindlichen Interessenbekundung kannst du bereits institutionelle Kontakte aufbauen. Für formelle Lieferantenregistrierungen und tatsächliche Ausschreibungsangebote müssen dagegen die jeweils verlangten Identitäts-, Unternehmens- und Eignungsnachweise vorliegen.

Ergebnis: Das vollständige deutschsprachige Government-/Infrastructure-/Procurement-Anschreiben, die Corporate-Feldzuordnung, die kompakte Portalversion, die partnerabhängige Kurzanfrage, die Freigabe-Checkliste und die Steuerungslogik sind vorbereitet.

Das Hauptdokument ist für eine unverbindliche institutionelle Erstkontaktaufnahme verwendbar. Eine formelle Lieferantenregistrierung oder Angebotsabgabe kann erst erfolgen, wenn die Anforderungen des konkreten Portals erfüllt sind.

Es wurde keine Registrierung, Bewerbung, Ausschreibungseinreichung oder sonstige Übermittlung vorgenommen. # GlobalCards Bank – eID / Digital Trust / swiyu

Universal Corporate & Institutional Partnership Application · Deutsch · Version 1.0 · 7. November 2026

Schweizer digitale Identität · swiyu Trust Infrastructure · Verifiable Credentials · DID · Digital Trust · eIDAS 2.0 · EUDI Wallet · Corporate Identity

Diese Fassung ist als unverbindliche Corporate- und Technologiepartnerschaftsanfrage für die schweizerische swiyu-Vertrauensinfrastruktur, digitale Identitätsanbieter, EUDI-Wallet-Integrationspartner und institutionelle Vertrauensdienste ausgearbeitet.

Antragsteller

Daniel Pohl

Projekt

GlobalCards Bank

Gesellschaftsstatus

Noch nicht bestätigt

Ausgangsregion

Deutschland / EWR

Antragsart

Institutionelle Voranfrage

Einreichung

Nicht erfolgt

## 1. Aktuelle regulatorische und technische Einordnung

Vor der Einreichung sind drei wichtige Punkte zu berücksichtigen:

- swiyu Sandbox: Die Schweiz stellt eine öffentlich zugängliche Testumgebung bereit, deren Teilnahme kostenlos ist. Die produktive Nutzung und einzelne Registerdienste können anderen Bedingungen und Gebühren unterliegen.&#x20;

  

  Dienste und Integration vorab testen+1

- Schweizer staatliche e-ID: Nach aktuellem Stand wird ihre Einführung im ersten Halbjahr 2027 erwartet. Sie wird durch den Bund beziehungsweise fedpol ausgegeben. GlobalCards kann gegebenenfalls eigene geeignete Nachweise ausstellen oder solche prüfen, wird dadurch aber nicht selbst staatlicher e-ID-Aussteller.&#x20;

  

  fedpol.admin.ch

- AGOV Business Accounts: Diese sind für 2027 angekündigt. Ein persönliches AGOV-Konto ist keine Unternehmensgründung und keine automatische staatliche Anerkennung eines Unternehmens.&#x20;

  

  agov.admin.ch



| Rolle / Verfahren                | Bedeutung für GlobalCards                                                                           |
| -------------------------------- | --------------------------------------------------------------------------------------------------- |
| Credential Issuer                | Eigene berechtigte digitale Nachweise ausstellen                                                    |
| Credential Verifier              | Nachweise prüfen, beispielsweise Berechtigungen oder Identitätsattribute                            |
| Wallet Holder                    | Nachweise empfangen, speichern und bei Bedarf vorlegen                                              |
| DID / Base Registry              | Technische Identifikatoren und öffentliche Schlüssel veröffentlichen                                |
| Trust Registry                   | Organisationen, Vertrauensinformationen und Berechtigungen nach dem jeweiligen Verfahren überprüfen |
| AGOV                             | Schweizer Behörden-Login, nicht identisch mit einer digitalen Identitätslizenz                      |
| EUDI / eIDAS                     | Gesondertes EU-Regelwerk für digitale Identitäten und Vertrauensdienste                             |
| Qualified Trust Service Provider | Besonders regulierte Vertrauensdienste mit eigenständiger Qualifizierung und Aufsicht               |

Die Schweizer swiyu-Vertrauensinfrastruktur und das europäische EUDI-Wallet-Ökosystem sind nicht automatisch gegenseitig zugelassen. Eine spätere grenzüberschreitende Interoperabilität muss anhand geltender Standards und rechtlicher Anerkennung geprüft werden.&#x20;



swiyu technical documentation+1



## 2. Vollständiges Corporate- und Digital-Trust-Partnerschaftsanschreiben

# GLOBALCARDS BANK

## UNIVERSAL CORPORATE & INSTITUTIONAL eID, DIGITAL TRUST & SWIYU PARTNERSHIP APPLICATION

**Formelle Interessenbekundung zur Integration digitaler Identitäten, verifizierbarer Nachweise, dezentraler Identifikatoren und internationaler Vertrauensinfrastrukturen**

**Datum:** 7. November 2026\
**Dokumentversion:** 1.0\
**Sprache:** Deutsch\
**Antragstyp:** Unverbindliche Corporate-, Technologie- und institutionelle Partnerschaftsanfrage\
**Einreichungsstatus:** Entwurf – persönliche Freigabe erforderlich

---

### A. Antragsteller und Projektidentität

| Feld                                               | Angabe                                                                                                                        |
| -------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------- |
| Ansprechpartner                                    | Daniel Pohl                                                                                                                   |
| Rolle                                              | Projektinitiator und technischer Projektkontakt                                                                               |
| Vorläufiger Projektname                            | GlobalCards Bank                                                                                                              |
| Weitere Projekt-/Organisationsbezeichnung          | Bra1nKy11 World Bank Eyes AeTHer                                                                                              |
| Zusätzliche Projektidentifikation                  | HolyThreeKingsTreesCrowns                                                                                                     |
| Kontaktstandort                                    | Detmold, Nordrhein-Westfalen, Deutschland                                                                                     |
| Kontaktland                                        | Deutschland                                                                                                                   |
| Kontakt-E-Mail                                     | [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu) |
| Rechtlicher Unternehmensname                       | Noch nicht bestätigt                                                                                                          |
| Gesellschaftsform                                  | Noch nicht bestätigt                                                                                                          |
| Eingetragener Gesellschaftssitz                    | Nicht bestätigt                                                                                                               |
| Handelsregisternummer                              | Nicht bereitgestellt                                                                                                          |
| Schweizer Unternehmens-Identifikationsnummer (UID) | Nicht bereitgestellt                                                                                                          |
| Legal Entity Identifier (LEI)                      | Nicht bereitgestellt                                                                                                          |
| Schweizer AGOV-Business-Account-Status             | Nicht bestätigt                                                                                                               |
| swiyu Business Partner ID                          | Nicht bestätigt                                                                                                               |
| Registrierte swiyu-DIDs                            | Für dieses Projekt nicht nachgewiesen                                                                                         |
| Eintrag im swiyu-Basisregister                     | Nicht bestätigt                                                                                                               |
| Verifizierter Eintrag im swiyu-Vertrauensregister  | Nicht nachgewiesen                                                                                                            |
| Zugelassener Vertrauensdiensteanbieter             | Nicht nachgewiesen                                                                                                            |
| Bestehende eIDAS-Qualifizierung                    | Nicht nachgewiesen                                                                                                            |
| Behördliche oder staatliche Akkreditierung         | Nicht nachgewiesen                                                                                                            |
| Bestehende institutionelle Partnerschaften         | Für dieses Projekt nicht bestätigt                                                                                            |
| Projektstatus                                      | Konzeption und technische Vorbereitung                                                                                        |
| Ausgangsregion                                     | Deutschland / Europäischer Wirtschaftsraum                                                                                    |
| Technischer Kooperationsraum                       | Schweiz und EWR, nach Prüfung der Zugangsbedingungen                                                                          |

Die genannten Bezeichnungen dienen der Identifikation des Projekts. Sie sind keine Nachweise einer eingetragenen Gesellschaft, staatlichen Zugehörigkeit, behördlichen Autorisierung oder zertifizierten Vertrauensdienstleistung.

### B. Empfänger und Betreff

**An:** Digital Identity / Trust Infrastructure / Corporate Onboarding / Business Partner Services / Developer Relations / Institutional Partnerships

**Betreff:** Corporate- und Technologiepartnerschaftsanfrage – GlobalCards Bank | swiyu, e-ID, Digital Trust, Verifiable Credentials, DID und internationale Identitätsinfrastruktur

### C. Formelle Vorstellung

Sehr geehrte Damen und Herren,

hiermit möchte ich mein Interesse an einer möglichen technischen, institutionellen und langfristig tragfähigen Zusammenarbeit im Bereich digitaler Identitäten, dezentraler Identifikatoren, elektronischer Nachweise und sicherer Vertrauensinfrastrukturen zum Ausdruck bringen.

Unter der vorläufigen Projektbezeichnung **GlobalCards Bank** bereite ich die Konzeption einer modularen Finanztechnologie- und Infrastrukturplattform für Privatkunden (B2C) und Geschäftskunden (B2B) vor.

Ein wesentlicher Bestandteil dieser Entwicklung ist die sichere und interoperable Verwaltung digitaler Identitäten sowie die technisch nachvollziehbare Ausstellung, Prüfung und Verarbeitung elektronischer Berechtigungs- und Organisationsnachweise.

Besonderes Interesse besteht an der Schweizer swiyu-Vertrauensinfrastruktur, ihren offenen technischen Standards, den zugehörigen Registerdiensten sowie möglichen Integrationsmodellen mit europäischen digitalen Identitäts- und Vertrauensdiensten.

Ich möchte prüfen, welche Entwicklerzugänge, Testumgebungen, Organisationsregistrierungen und institutionellen Partnerschaftsverfahren für ein entsprechendes Vorhaben zur Verfügung stehen.

Der rechtliche Gesellschaftsstatus des Projekts ist noch nicht bestätigt. Daher handelt es sich zunächst ausdrücklich um eine unverbindliche Erstanfrage zur technischen und rechtlichen Machbarkeit.

### D. Vorgesehenes Geschäfts- und Integrationsmodell

**Projekt:** GlobalCards Bank

**Betriebsmodell:** Hybride internationale Finanztechnologie- und Digital-Trust-Plattform

**Zielgruppen:** Privatkunden, Geschäftskunden und mögliche institutionelle Technologiepartner

**Primärer Markt:** Deutschland und Europäischer Wirtschaftsraum

**Technischer Kooperationsfokus:** Schweizer swiyu-Vertrauensinfrastruktur und gegebenenfalls kompatible europäische Identitätsdienste

Die angestrebte Plattform soll folgende Bereiche modular miteinander verbinden:

1. Identity & Access Management
2. Digitale Personen- und Unternehmensidentitäten
3. Elektronische Berechtigungsnachweise
4. Decentralized Identifiers (DID)
5. Verifiable Credentials
6. Wallet- und Identitätsintegration
7. KYC-/KYB-Integrationsschnittstellen
8. Sichere Unternehmens- und Partner-Onboarding-Prozesse
9. Verifikation von Attributen und Berechtigungen
10. Digitale Signaturen und Vertrauensnachweise
11. Governance-, Compliance- und Audit-Funktionen
12. Interoperable Identitäts- und Vertrauensschnittstellen

Alle Module sollen zunächst als technische Entwicklungsziele verstanden werden.

### E. Angefragte swiyu-Partnerschafts- und Integrationsmodelle

**Modell A – swiyu Business Partner / Sandbox**

Prüfung der Voraussetzungen, um das Projekt nach den geltenden Bedingungen in der swiyu-Testumgebung zu evaluieren.

Gewünschte Leistungen:

- Zugang zum offiziellen Service Portal
- Informationen zur zulässigen Organisationsregistrierung
- Bereitstellung einer technischen Sandbox
- Informationen zu Base Registry und Trust Registry
- Entwicklerdokumentation und Test-APIs
- Bereitstellung der geltenden Nutzungsbedingungen

**Modell B – Credential Issuer**

Technische Prüfung der Möglichkeit, eigene geeignete digitale Nachweise auszustellen.

Mögliche Nachweisarten:

- Projektbezogene Mitgliedschaftsnachweise
- Organisatorische Rollen und Berechtigungen
- Mitarbeiter- und Partnerberechtigungen
- Technische Schulungs- oder Qualifikationsnachweise
- Nachweise für interne Unternehmensprozesse

Eine Ausstellung staatlicher Identitätsdokumente, behördlicher Berechtigungen oder amtlicher Zertifikate wird nicht beansprucht.

**Modell C – Credential Verifier**

Technische Prüfung digitaler Nachweise für geeignete und rechtmäßig definierte Geschäftsprozesse.

Dazu können gehören:

- Identitätsattribute
- Berechtigungsnachweise
- Organisationale Zuordnungen
- Authentizitäts- und Integritätsprüfung
- Prüfung des aktuellen Nachweisstatus
- Verifikation elektronischer Signaturen
- Prüfung von Ausstellerinformationen

Die Überprüfung soll auf rechtmäßig angeforderten Daten beruhen und die Zustimmung beziehungsweise andere erforderliche Rechtsgrundlagen berücksichtigen.

**Modell D – Corporate Identity & Digital Trust**

Prüfung digitaler Identitäts- und Berechtigungsmodelle für Organisationen und deren bevollmächtigte Vertreter.

**Modell E – European Digital Identity Interoperability**

Technische Bewertung möglicher Schnittstellen zwischen swiyu, eIDAS-konformen Vertrauensdiensten und EUDI-Wallet-Anwendungen.

Eine rechtliche oder technische Anerkennung zwischen den Systemen wird nicht als bereits bestehend vorausgesetzt.

**Modell F – Technology and Developer Partnership**

Mögliche Zusammenarbeit im Bereich offener Komponenten, APIs, Schnittstellen, Sicherheitsprüfungen und interoperabler Entwicklungsverfahren.

### F. Technische swiyu-Integration

Für eine mögliche Integration sollen die folgenden Elemente bewertet werden:

- swiyu Service Portal
- Business Partner Onboarding
- Base Registry
- Trust Registry
- Status Registry
- DID-Dokumente und Schlüsselverwaltung
- Proof-of-Possession-Verfahren
- Technische Registrierung von Aussteller- und Prüfdiensten
- Verifiable Credential Issuance
- Verifiable Presentation Verification
- Credential Status und Widerruf
- OpenID4VCI
- OpenID4VP
- SD-JWT VC
- API-basierte Identitäts- und Berechtigungsprüfung

Die konkret unterstützten Protokollversionen und Credential-Formate sollen aus der jeweils aktuellen offiziellen technischen Spezifikation übernommen werden.

### G. Digital Trust und Unternehmensidentitäten

Eine mögliche GlobalCards-Identitätsinfrastruktur soll zwischen folgenden Objekten unterscheiden:

**Natürliche Person**

Identitätsattribute und Berechtigungen werden ausschließlich entsprechend den anwendbaren Datenschutz- und Identitätsvorschriften verarbeitet.

**Juristische Person**

Unternehmensidentitäten beruhen auf überprüfbaren Register- und Organisationsdaten.

**Bevollmächtigte Person**

Eine Person kann nur solche Organisationsrechte geltend machen, die durch nachprüfbare Berechtigungen gedeckt sind.

**Technische Identität**

Systeme, APIs und Dienste erhalten eigenständige technische Identifikatoren, Berechtigungen und Sicherheitsrichtlinien.

**Credential Issuer**

Eine ausstellende Organisation ist für die fachliche Richtigkeit und den Lebenszyklus ihrer eigenen Nachweise verantwortlich.

**Credential Verifier**

Die prüfende Organisation bewertet Echtheit, Gültigkeit, Vertrauensinformationen und den jeweils zulässigen Verwendungszweck.

Eine technische DID beweist für sich allein weder eine staatliche Anerkennung noch die Vertretungsbefugnis einer natürlichen oder juristischen Person.

### H. Anwendung innerhalb der Finanzinfrastruktur

GlobalCards möchte insbesondere folgende Einsatzmöglichkeiten untersuchen:

1. Digitales Kunden-Onboarding
2. Organisations- und Unternehmensprüfung
3. Identifizierung bevollmächtigter Vertreter
4. Sichere Partnerregistrierung
5. Digitale Compliance-Nachweise
6. Verifizierbare technische Zertifikats- und Kompetenznachweise
7. Rollenbasierte Freigaben für Finanzprozesse
8. Dokumentierte Zustimmung und Berechtigungsverwaltung
9. Technische Verifikation bei API-Partnerschaften
10. Kontrollierte Identitätsföderation
11. Sicheres Nachweismanagement
12. Datenschutzorientierte Überprüfung von Attributen

Bei KYC-/AML-Anwendungen ist gesondert zu prüfen, welche Identitätsnachweise die jeweils zuständigen regulierten Finanzinstitute tatsächlich anerkennen und welche ergänzenden Prüfungen vorgeschrieben bleiben.

Eine erfolgreiche e-ID-Verifikation ersetzt nicht pauschal sämtliche gesetzlichen Sorgfaltspflichten.

### I. Vorgesehene technische Referenzarchitektur

Geplant sind folgende Komponenten:

| Modul                         | Funktion                                              |
| ----------------------------- | ----------------------------------------------------- |
| Corporate Identity Registry   | Organisations- und Rechtsträgerdaten                  |
| Identity & Access Management  | Authentifizierung und Berechtigungen                  |
| DID Lifecycle Service         | Erstellung und Verwaltung technischer Identifikatoren |
| Credential Issuer Adapter     | Anbindung von Nachweisausstellern                     |
| Credential Verifier Adapter   | Prüfung elektronischer Nachweise                      |
| Trust Registry Connector      | Prüfung von Vertrauensinformationen                   |
| Status Registry Connector     | Status- und Widerrufsprüfung                          |
| Wallet Integration Gateway    | Verbindung mit geeigneten digitalen Wallets           |
| Consent & Purpose Management  | Datennutzungszweck und Freigaben                      |
| KYC/KYB Connector             | Integration regulierter Identitätsprüfungen           |
| Digital Signature Integration | Signatur- und Siegelanbindung                         |
| Audit & Evidence Registry     | Integritätsgeschützte Prüfprotokolle                  |
| Governance Policy Engine      | Rechte- und Organisationsregeln                       |
| API Gateway                   | Kontrollierte technische Schnittstellen               |
| Security & Key Management     | Schlüssel, Zugriffsschutz und Rotation                |
| Partner Administration        | Technisches Partner- und Zugangsmanagement            |

Es ist vorgesehen, die technische Integration zunächst mit synthetischen Testidentitäten und Testnachweisen zu evaluieren.

### J. Sicherheit, Datenschutz und Datenhoheit

Das Projekt soll insbesondere folgende Sicherheits- und Datenschutzprinzipien berücksichtigen:

- Privacy by Design und Privacy by Default
- Datenminimierung
- Zweckbindung
- Differenzierte Zugriffskontrollen
- Sichere Schlüsselverwaltung
- HSM-Unterstützung, soweit erforderlich
- Phishing-resistente Authentifizierung
- Kontrollierte Credential-Ausstellung
- Authentizitäts- und Integritätsprüfung
- Status- und Widerrufsverwaltung
- Dokumentierte Berechtigungsentscheidungen
- Minimierung von Nachweisdaten in Protokollen
- Schutz vor unberechtigter Weitergabe
- Technische und organisatorische Notfallmaßnahmen
- Revisionsfähige Sicherheitsnachweise

Private Schlüssel, Seed-Phrasen, Client Secrets, Refresh Tokens, personenbezogene Ausweisdokumente und Produktionszugangsdaten werden im Rahmen dieser Erstanfrage nicht übermittelt.

### K. Rechtliche und regulatorische Grundlagen

Im Rahmen einer tatsächlichen Implementierung sollen unter anderem folgende Regelwerke geprüft werden, soweit sie für den konkreten Anwendungsfall einschlägig sind:

- Schweizer Bundesgesetz über den elektronischen Identitätsnachweis und andere elektronische Nachweise (BGEID)
- Schweizer Datenschutzgesetz (DSG)
- Europäische Datenschutz-Grundverordnung (DSGVO)
- eIDAS und der europäische digitale Identitätsrahmen
- EUDI-Wallet-Implementierungsvorschriften
- Vorschriften für qualifizierte elektronische Vertrauensdienste
- Anwendbare KYC-/KYB- und Geldwäschevorschriften
- Finanzaufsichtsrecht bei regulierten Finanzdienstleistungen
- Technische Sicherheitsanforderungen der jeweiligen Vertrauensinfrastruktur
- Regeln zur Unternehmensvertretung und Vertretungsbefugnis
- Gegebenenfalls DORA und andere sektorale Cybersicherheitsvorgaben

Die rechtliche Anwendbarkeit hängt insbesondere davon ab, ob GlobalCards als Technologieanbieter, Nachweisaussteller, Prüfer, Wallet-Dienstleister, regulierter Vertrauensdiensteanbieter oder Finanzdienstleister tätig wird.

Es wird keine bereits bestehende Qualifizierung oder behördliche Anerkennung behauptet.

### L. Angefragte institutionelle und technische Zugänge

Ich bitte um Auskunft zu folgenden Möglichkeiten:

1. swiyu Business Partner Onboarding
2. Zugang zur Sandbox
3. Voraussetzungen zur Eintragung im Basisregister
4. Voraussetzungen zur Eintragung und Verifikation im Vertrauensregister
5. Developer-Portal und API-Dokumentation
6. Verfügbare Credential-Issuer- und Verifier-Komponenten
7. DID- und Schlüsselverwaltungsverfahren
8. Status- und Trust-Registry-Integrationen
9. Technische Sicherheits- und Zertifizierungsanforderungen
10. Bedingungen für Test- und Produktionszugänge
11. Anerkennung ausländischer beziehungsweise noch nicht gegründeter Projektorganisationen
12. Anforderungen an verifizierte Unternehmens- und Vertretungsdaten
13. Mögliche institutionelle oder technische Partnerprogramme
14. Informationen zur Interoperabilität mit europäischen Identitätssystemen

### M. Wirtschaftliche und organisatorische Fragen

Bitte informieren Sie mich insbesondere über:

- Kostenfreie Test- und Evaluierungsmöglichkeiten
- Voraussetzungen zur Business-Partner-Registrierung
- Eventuelle Gebühren für DID- und Registerdienste
- Gebühren für produktive Nutzung
- Anforderungen an eine juristische Person
- Geeignete Identitäts- und Organisationsnachweise
- Erforderliche technische Sicherheitsnachweise
- Verantwortlichkeiten für ausgestellte Credentials
- Betriebs- und Verfügbarkeitsanforderungen
- Bedingungen für die Nutzung staatlicher Identitätsnachweise
- Datenschutzrechtliche Verantwortlichkeiten
- Technische Unterstützung und Supportmöglichkeiten
- Voraussetzungen einer späteren kommerziellen Integration

Etwaige Registrierungs- oder Nutzungsentgelte sollen vor einer kostenpflichtigen Handlung ausdrücklich offengelegt und gesondert genehmigt werden.

### N. Institutionelle und staatliche Statusklarstellung

Mit dieser Anfrage wird ausdrücklich nicht behauptet, dass GlobalCards:

- eine staatliche Identitätsbehörde ist,
- eine schweizerische e-ID ausstellen darf,
- bereits im swiyu-Vertrauensregister staatlich verifiziert ist,
- über einen bestätigten Business Partner Status verfügt,
- als qualifizierter Vertrauensdiensteanbieter zugelassen ist,
- über staatliche Unternehmens- oder Vertretungsbefugnisse verfügt,
- eine vorhandene eIDAS-Zertifizierung besitzt,
- eine offizielle Partnerschaft mit der Schweizerischen Eidgenossenschaft eingegangen ist,
- von europäischen Behörden zur Ausstellung amtlicher Identitätsnachweise ermächtigt wurde.

Eine technische Registrierung oder DID-Veröffentlichung wird nicht als staatliche Anerkennung, regulatorische Zulassung oder rechtsverbindliche Vertretungsbefugnis interpretiert.

### O. Vertraulichkeit und Datenschutz

Ich bitte darum, übermittelte Kontakt- und Projektinformationen ausschließlich zur Bearbeitung dieser unverbindlichen Anfrage und im Rahmen gegebenenfalls gesetzlich erforderlicher Prüfungen zu verwenden.

Besonders schutzwürdige Identitäts-, Organisations-, Schlüssel- oder Sicherheitsunterlagen sollen nur nach gesonderter Prüfung und über geeignete sichere Übermittlungswege bereitgestellt werden.

### P. Gewünschter nächster Schritt

Ich würde mich über eine Rückmeldung zur grundsätzlichen technischen und organisatorischen Eignung des Projekts freuen.

Besonders hilfreich wären:

1. Der zuständige Corporate- oder Technical-Onboarding-Ansprechpartner.
2. Informationen zum offiziellen swiyu-Business-Partner-Verfahren.
3. Voraussetzungen für die Sandbox-Registrierung.
4. Anforderungen an einen späteren produktiven Registerzugang.
5. Klärung der notwendigen Rechtsform und Unternehmensnachweise.
6. Informationen zu den Rollen als Issuer und Verifier.
7. Entwicklerdokumentation und technische Testmöglichkeiten.
8. Hinweise auf Gebühren und mögliche Nutzungsbeschränkungen.
9. Informationen zu europäischen Identitäts- und Vertrauensdienstintegrationen.

Ich strebe eine transparente, datenschutzorientierte und technisch interoperable Zusammenarbeit im Bereich internationaler digitaler Identitäts- und Vertrauensinfrastrukturen an.

Mit freundlichen Grüßen

**Daniel Pohl**\
Projektinitiator und technischer Projektkontakt

**GlobalCards Bank** – vorläufige Projektbezeichnung\
**Bra1nKy11 World Bank Eyes AeTHer** – Projekt-/Organisationsbezeichnung\
**HolyThreeKingsTreesCrowns** – zusätzliche Projektidentifikation

Detmold, Nordrhein-Westfalen, Deutschland

**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

---

**Dokumentstatus:** Unverbindliche Corporate- und institutionelle Erstkontaktaufnahme.

**Keine automatische Registrierung, DID-Erstellung, Vertrauensregistereintragung, Schlüsselgenerierung, kostenpflichtige Aktion, Vertragsannahme oder Einreichung.**

## 3. Universelle Feldzuordnung für eID-, swiyu- und Digital-Trust-Portale

Diese Feldzuordnung dient als Grundlage für deinen Portal-Worker. Sie vermeidet insbesondere, dass ein technischer Business-Partner-Eintrag fälschlich als amtlich bestätigte Gesellschafts- oder Vertrauensdienstzulassung dargestellt wird.

| Portal-Feld (EN)            | GlobalCards-Eintrag                                        | Verarbeitungsregel                      |
| --------------------------- | ---------------------------------------------------------- | --------------------------------------- |
| First Name                  | Daniel                                                     | Übernehmen                              |
| Last Name                   | Pohl                                                       | Übernehmen                              |
| Contact Email               | world.banks.eyes.aether\@globedynamicz.statesflowwishes.eu | Übernehmen                              |
| Contact Role                | Project Initiator / Technical Project Contact              | Keine formelle Organstellung behaupten  |
| Project Name                | GlobalCards Bank                                           | Vorläufige Projektbezeichnung           |
| Organization Designation    | Bra1nKy11 World Bank Eyes AeTHer                           | Nur Projektbezeichnung                  |
| Legal Entity Name           | Noch nicht bestätigt                                       | Pflichtprüfung                          |
| Legal Form                  | Noch nicht bestätigt                                       | Nicht erfinden                          |
| Company Registration No.    | Nicht bereitgestellt                                       | Nicht erfinden                          |
| Registered Business Address | Noch nicht bestätigt                                       | Kontaktstandort nicht übernehmen        |
| Contact City                | Detmold                                                    | Übernehmen                              |
| Region                      | Nordrhein-Westfalen                                        | Übernehmen                              |
| Country                     | Germany                                                    | Übernehmen                              |
| Company Website             | Nicht bereitgestellt                                       | Offenlassen                             |
| Swiss UID / CHE Number      | Nicht bereitgestellt                                       | Nicht erfinden                          |
| LEI                         | Nicht bereitgestellt                                       | Optional / nachweispflichtig            |
| Business Partner ID         | Nicht bestätigt                                            | Nicht erzeugen oder erfinden            |
| AGOV Account                | Nicht bestätigt                                            | Keine Kontoregistrierung behaupten      |
| Business Account Status     | Nicht bestätigt                                            | Nicht behaupten                         |
| DID                         | Nicht bestätigt                                            | Keine DID fingieren                     |
| DID Method                  | Gemäß aktueller swiyu-Spezifikation festzulegen            | Technisch prüfen                        |
| DID Space ID                | Nicht bereitgestellt                                       | Erst nach rechtmäßigem Onboarding       |
| Identifier Registry Entry   | Nicht bestätigt                                            | Offen                                   |
| Trust Registry Status       | Keine Verifizierung nachgewiesen                           | Keine staatliche Anerkennung behaupten  |
| Credential Issuer Role      | Geplante Integration                                       | Noch nicht aktiv                        |
| Credential Verifier Role    | Geplante Integration                                       | Noch nicht aktiv                        |
| Wallet Provider Role        | Noch nicht festgelegt                                      | Nicht als staatlicher Anbieter ausgeben |
| Credential Types            | Organisation, Mitgliedschaft, Berechtigung – geplant       | Keine amtlichen Nachweise fingieren     |
| Identity Proofing           | Geplante Partnerintegration                                | Nicht als abgeschlossen erklären        |
| OID4VCI / OID4VP            | Technische Evaluierung                                     | Version prüfen                          |
| Credential Format           | SD-JWT VC nach aktueller Spezifikation                     | Technisch prüfen                        |
| Trust Service Qualification | Nicht nachgewiesen                                         | Keine Qualifizierung behaupten          |
| API Access                  | Requested                                                  | Entwickleranfrage                       |
| Sandbox Access              | Requested                                                  | Keine Freischaltung behaupten           |
| Production Access           | Nicht genehmigt                                            | Gesperrt                                |
| API Client ID               | Nicht bereitgestellt                                       | Geschützter Konfigurationsbereich       |
| API Client Secret           | Nicht bereitgestellt                                       | Niemals in Erstanfrage übernehmen       |
| Public Key Material         | Noch nicht erstellt/bereitgestellt                         | Nur nach technischem Onboarding         |
| Private Keys                | Vertraulich, kein Portalformularwert                       | Strikt schützen                         |
| Authorized Signatory        | Noch nicht bestätigt                                       | Vor formeller Erklärung prüfen          |
| Compliance Certification    | Nicht nachgewiesen                                         | Nicht erfinden                          |
| Expected Credential Volume  | Noch nicht prognostiziert                                  | Keine Zahlen erfinden                   |

### Zusätzliche Felder nach Integrationsrolle

| Rolle                     | Erforderliche Zusatzinformationen                                                               |
| ------------------------- | ----------------------------------------------------------------------------------------------- |
| swiyu Business Partner    | Rechtsträger, Organisationsdaten, berechtigter Vertreter, BP-ID nach Onboarding                 |
| Credential Issuer         | Credential-Schema, rechtliche Ausstellungsbefugnis, DID, Signaturschlüssel, Statusverfahren     |
| Credential Verifier       | Prüfzweck, benötigte Attribute, Rechtsgrundlage, Vertrauensregeln, Datenlöschung                |
| Trust Registry            | Nachweise zur Organisation und gegebenenfalls staatliche Verifizierung                          |
| EUDI Wallet Relying Party | Nationale Registrierungsbedingungen, Verwendungszweck und zulässige Attribute                   |
| Qualified Trust Service   | Zuständige Aufsicht, Konformitätsbewertung, Qualifizierungsverfahren                            |
| AGOV                      | Persönliches Konto, getrennte geschäftliche Nutzung, erforderliche Verknüpfung und Berechtigung |

## 4. Direkte offizielle Portale und Developer-Zugänge

Diese Links führen zu den spezifischen Registrierungs-, Entwicklungs- und Integrationsbereichen.

| Portal                    | Direkter Zugang                                                                                                                                                         | Zweck                                                 |
| ------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- |
| swiyu Service Portal      | [Business Partner Onboarding](https://portal.trust-infra.swiyu-int.admin.ch/)                                                                    | Sandbox-Organisationsregistrierung                    |
| swiyu Onboarding Cookbook | [Base & Trust Registry Onboarding](https://swiyu-admin-ch.github.io/cookbooks/onboarding-base-and-trust-registry/)                               | DIDs, API-Subscriptions und Vertrauensregistrierung   |
| swiyu Sandbox             | [Offizielle Sandbox-Anleitung](https://www.eid.admin.ch/de/sandbox)                                                                              | Kostenfreie Testteilnahme                             |
| swiyu Issuer              | [Issuer Developer Guide](https://swiyu-admin-ch.github.io/cookbooks/getting-started-issuer/)                                                     | Elektronische Nachweise ausstellen                    |
| swiyu Verifier            | [Verifier Developer Guide](https://swiyu-admin-ch.github.io/cookbooks/getting-started-verifier/)                                                 | Nachweise prüfen                                      |
| swiyu Developer-Projekt   | [Offizielle Open-Source-Repositories](https://github.com/swiyu-admin-ch)                                                                         | Issuer, Verifier und technische Komponenten           |
| AGOV Registrierung        | [AGOV-Konto erstellen](https://www.me.agov.admin.ch/)                                                                                            | Schweizer Behörden-Login                              |
| AGOV Business Accounts    | [Business-Account-Vorbereitung](https://www.agov.admin.ch/de/business-account)                                                                   | Geschäftsbezogene Behörden-Logins                     |
| EasyGov Schweiz           | [Schweizer Unternehmensportal](https://www.easygov.swiss/easygov/)                                                                               | Unternehmens- und Behördenverfahren                   |
| EU Digital Identity       | [EUDI-Wallet-Implementierungsregeln](https://digital-strategy.ec.europa.eu/en/library/implementing-regulation-european-digital-identity-wallets) | Europäische Wallet- und Vertrauensdienstanforderungen |

Das offizielle swiyu-Service-Portal führt zur technischen Organisationsregistrierung. Ein Eintrag im Basisregister ist jedoch von einer staatlich verifizierten Vertrauensregistrierung zu unterscheiden. Die technische swiyu-Dokumentation empfiehlt außerdem getrennte API-Anwendungen für Issuer und Verifier.&#x20;



swiyu+1



Die swiyu-Sandbox ist kostenfrei nutzbar; daraus ergibt sich aber keine Garantie für kostenlose spätere Produktions-DIDs oder sonstige produktive Dienste.&#x20;



Dienste und Integration vorab testen+1



## 5. Kompakte Fassung für Corporate-Online-Portale

**Betreff: Corporate eID / Digital Trust / swiyu Partnership Request – GlobalCards Bank**

Sehr geehrte Damen und Herren,

als Projektinitiator von GlobalCards Bank interessiere ich mich für eine mögliche technische und institutionelle Zusammenarbeit im Bereich digitaler Identitäten, elektronischer Vertrauensnachweise, Decentralized Identifiers (DID), Verifiable Credentials sowie der Schweizer swiyu-Vertrauensinfrastruktur.

GlobalCards ist als hybride internationale B2C-/B2B-Finanztechnologieplattform geplant. Ein wesentlicher Entwicklungsbereich ist die sichere Integration digitaler Personen- und Unternehmensidentitäten, elektronischer Berechtigungsnachweise sowie datenschutzorientierter Issuer- und Verifier-Prozesse.

Ich möchte insbesondere die Voraussetzungen für eine technische swiyu-Sandbox-Evaluierung, Business Partner Onboarding, Base-/Trust-Registry-Integration, DID-Verwaltung und eine mögliche spätere Integration europäischer Digital-Identity-Standards prüfen.

Der rechtliche Gesellschaftsstatus ist noch nicht bestätigt. Es werden keine bestehenden staatlichen Identitätsbefugnisse, eIDAS-Zertifizierungen, swiyu-Vertrauensregistrierungen oder institutionellen Partnerschaften beansprucht.

Ich bitte um Informationen zu Ihren Corporate- und Developer-Onboarding-Verfahren, geeigneten Sandbox- und API-Zugängen, Anforderungen an die Organisation, regulatorischen Voraussetzungen und möglichen Gebühren.

**Kontakt:** Daniel Pohl\
**Projekt:** GlobalCards Bank – vorläufige Projektbezeichnung\
**Weitere Projektbezeichnung:** Bra1nKy11 World Bank Eyes AeTHer\
**Standort:** Detmold, Nordrhein-Westfalen, Deutschland\
**E-Mail:** [world.banks.eyes.aether@globedynamicz.statesflowwishes.eu](mailto:world.banks.eyes.aether@globedynamicz.statesflowwishes.eu)

Diese Anfrage ist eine unverbindliche technische und institutionelle Interessenbekundung, keine formelle Akkreditierungs- oder Vertrauensregistrierung.

Mit freundlichen Grüßen

Daniel Pohl

## 6. Partnerspezifische Antragsvorbereitung

Institution / Partnerkategorieswiyu – Business Partner / Sandbox

Ausgewählter Anfragefokus

Technisches Business Partner Onboarding, Sandbox-Zugang sowie Registrierungsvoraussetzungen für Base und Trust Registry

Zentrale Frage

Ist eine technische Sandbox-Evaluierung vor abschließender Gründung eines Rechtsträgers möglich, und welche Nachweise werden für eine formelle Registrierung verlangt?

&#x20;Partnerspezifische Anfrage kopieren

## 7. Separate Freigabe-Checkliste

Die Prüfliste ist auf eID, swiyu, DID und Trust Registry zugeschnitten. Eine Markierung gilt nur als interne Dokumentation, nicht als Freigabe gegenüber einer Behörde.

Digital Trust – Freigabeprüfung

0/20

A. Corporate Identity & Gesellschaft

Kontakt- und Projektdaten sind geprüft.

Der rechtliche Gesellschaftsstatus wird als unbestätigt angegeben.

Es werden keine Schweizer UID, BP-ID, LEI oder Registerdaten erfunden.

Die tatsächliche Organisations- und Vertretungsbefugnis ist für den gewählten Antrag geklärt.

B. swiyu & Digital Trust

Basisregister, Vertrauensregister und staatliche Verifizierung werden unterschieden.

Issuer, Verifier und Wallet-Rollen sind korrekt klassifiziert.

Es wird keine bereits bestehende staatliche e-ID-Ausstellungsberechtigung behauptet.

Die gewählte Sandbox-/Produktionsumgebung ist richtig zugeordnet.

C. Technische Integrität & Datensicherheit

Keine privaten Schlüssel, Client Secrets oder Refresh Tokens werden übermittelt.

DIDs und technische Referenzen werden nicht ohne tatsächlichen Nachweis angegeben.

Nur synthetische Testidentitäten und berechtigte Nachweisdaten sind vorgesehen.

Prüfzweck, Einwilligung oder sonstige Rechtsgrundlage sowie Datenminimierung wurden berücksichtigt.

D. Regulatorische Voraussetzungen

Schweizer BGEID/DSG und gegebenenfalls EU-DSGVO/eIDAS sind entsprechend dem Anwendungsfall geprüft.

Eine technische DID wird nicht als rechtlicher Unternehmensnachweis behandelt.

Es werden keine bestehenden Trust-Service-Zertifizierungen behauptet.

Mögliche Gebühren und produktive Registrierungsbedingungen sind vor Zustimmung geklärt.

E. Abschließende Freigabe

Der richtige institutionelle Empfänger und das offizielle Portal sind verifiziert.

Pflichtfelder und erforderliche Identitätsnachweise sind korrekt behandelt.

Die finale Anfrage wurde persönlich geprüft.

Eine gesonderte ausdrückliche Freigabe ist für die konkrete Einreichung dokumentiert.

20 Prüfpunkte noch offen.

&#x20;Freigabe-Checkliste kopieren

## 8. Verbindliche Steuerungsregeln für den Portal-Worker

| Prozesszustand           | Zulässige automatische Handlung                                                |
| ------------------------ | ------------------------------------------------------------------------------ |
| `PROFILE_LOADED`         | Freigegebene Projekt- und Kontaktdaten geschützt laden                         |
| `TRUST_ROLE_CLASSIFIED`  | Issuer, Verifier, Holder, Wallet oder Trust-Service-Provider unterscheiden     |
| `LEGAL_ENTITY_CHECK`     | Gesellschaftsstatus und Vertretungsbefugnisse prüfen                           |
| `TRUST_REGISTRY_CHECK`   | Basisregistereintrag und staatliche Vertrauensverifizierung getrennt behandeln |
| `DID_VALIDATION`         | Nur tatsächlich nachgewiesene DID-Daten verwenden                              |
| `CREDENTIAL_SCOPE_CHECK` | Nachweistypen und Ausstellungsbefugnisse prüfen                                |
| `PRIVACY_PURPOSE_CHECK`  | Zweckbindung und zulässige Attribute überprüfen                                |
| `KEY_PROTECTION_CHECK`   | Private Schlüssel und Tokens ausschließen                                      |
| `FIELD_MAPPING`          | Belegbare Angaben dem Zielportal zuordnen                                      |
| `DUPLICATE_CHECK`        | Bestehende Profile und Entwürfe auf Doppelregistrierungen prüfen               |
| `DRAFT_READY`            | Vollständige Vorschau erzeugen                                                 |
| `HUMAN_REVIEW_REQUIRED`  | Rechtliche Pflichtangaben und Freigabe überprüfen                              |
| `SUBMISSION_LOCKED`      | Keine Registrierung, DID-Veröffentlichung, Vertragsannahme oder Übermittlung   |

## 9. Empfohlene Reihenfolge für GlobalCards

01

Sandbox und technische Rolle

swiyu-Sandbox-Anforderungen lesen, Issuer- und Verifier-Anwendungsfälle festlegen.

02

Rechtsträger und Business Partner

Zulässige Organisationsform und die Voraussetzungen für einen formellen Business-Partner-Eintrag klären.

03

DID und Registerintegration

Base-, Status- und Trust-Registry-Prozesse ausschließlich mit autorisierten Sandbox-Zugängen testen.

04

Finanzidentität und Compliance

KYC/KYB, Unternehmensberechtigungen und kontrollierte Credential-Prüfung integrieren.

05

Internationale Interoperabilität

EUDI-Wallet und eIDAS-Anforderungen getrennt prüfen; später kontrolliert produktiv erweitern.

Ergebnis: Für GlobalCards Bank liegen jetzt die deutschsprachige eID-/swiyu-Corporate-Anfrage, die Portal-Feldzuordnung, die kompakte Erstkontaktversion, die partnerspezifische Anpassung und die separate Freigabeprüfung vor.

Der erste praktische Schritt ist eine unverbindliche Eignungsanfrage zur swiyu-Sandbox und zum Business Partner Onboarding. Eine formelle Unternehmensregistrierung, staatliche Verifizierung oder Produktionsfreigabe ist angesichts des noch unbestätigten Gesellschaftsstatus separat zu klären.

Es wurde keine Registrierung, DID-Erstellung, Vertrauensregistereintragung oder Einreichung durchgeführt. # GlobalCards Bank – Open Banking Multi-Bank Integration

Ja! Genau diese Infrastruktur gibt es bereits. Und das Interessante daran: Du musst nicht mit Tausenden Banken einzeln Verträge abschließen oder Tausende individuelle Schnittstellen programmieren.

Über einen entsprechend zugelassenen Open-Banking-Anbieter kannst du sehr viele Banken durch eine zentrale API, eine vorhandene Bankauswahl und einen einheitlichen Autorisierungsprozess in ein eigenes GlobalCards-Portal integrieren.

Beispiel: Enable Banking

# 2.700+

Angebundene Banken und Finanzinstitute

# 30

EWR-Länder

Eine technische Integration – sehr viele Bankverbindungen.

Diese Angaben stammen aus der aktuellen Anbieterbeschreibung von Enable Banking. Sie sind keine Garantie, dass bei jeder Bank sämtliche Privat- und Geschäftskontofunktionen verfügbar sind.&#x20;



The Connectivity Engine

## 1. Die drei Lizenzmodelle

| Modell                                            | Eigene PSD2-Zulassung?                                                                                   | Kosten                                                       |
| ------------------------------------------------- | -------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ |
| A. Open Banking unter Partnerzulassung            | Nicht zwingend, wenn der zugelassene Anbieter den regulierten Kontoinformationsdienst selbst erbringt    | Sandbox oft gratis; kommerzielle Nutzung vertraglich         |
| B. Eigener AISP                                   | Ja, in Deutschland grundsätzlich Registrierung nach § 34 ZAG für ausschließlich Kontoinformationsdienste | Registrierung, Organisation, Versicherung und Betrieb prüfen |
| C. Eigener PISP / weitergehendes Zahlungsinstitut | Grundsätzlich entsprechende Erlaubnis erforderlich                                                       | Höhere regulatorische und operative Anforderungen            |

Das heißt: GlobalCards kann unter geeigneten vertraglichen und regulatorischen Bedingungen ein eigenes Multi-Banking-Frontend entwickeln, während der zugelassene Partner die regulierte Kontoinformationsdienstleistung gegenüber dem Kunden erbringt.

Das ist keine kostenlose Übertragung einer Banklizenz. Vielmehr wird die regulierte Dienstleistung rechtlich vom zugelassenen Partner bereitgestellt. Das konkrete Rollenmodell muss im Vertrag festgelegt werden.&#x20;



Gesetze im Internet+2



## 2. Die besten Lizenz- und Integrationspartner

Ich würde insbesondere diese fünf Anbieter für GlobalCards evaluieren:

| Anbieter            | Direkter Partner- oder Developer-Zugang                                                                                                                                                                      | Lizenzmodell und Stärke                                                                                  |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------- |
| Enable Banking 🇫🇮 | [Control Panel registrieren](https://enablebanking.com/sign-in/) · [API-Anwendungen](https://enablebanking.com/cp/applications)                                | Eigene regulierte Kontoinformationsinfrastruktur, Sandbox, Multi-Bank-API, B2C/B2B                       |
| Salt Edge           | [Partnerantrag](https://www.saltedge.com/partnership_request) · [Lizenzpartnerprogramm](https://www.saltedge.com/products/account_information/partner_program) | Nutzung unter Partnerlizenz ohne eigene PSD2-AISP-Zulassung möglich; fertige Dashboards                  |
| Yapily Connect      | [Yapily Connect – Lizenzmodell](https://www.yapily.com/product/yapilyconnect/) · [Developer-Registrierung](https://accounts.yapily.com/register)               | AIS und PIS unter dem passenden regulierten Anbietermodell; API und Consent Flow                         |
| finAPI 🇩🇪         | [30-Tage-Sandbox beantragen](https://www.finapi.io/jetzt-testen/) · [Developer Docs](https://documentation.finapi.io/access)                                   | Deutsche PSD2-/FinTS-Anbindungen, Privat-/Geschäftskonten, Lizenzmodell                                  |
| Tink / Visa         | [Developer Account](https://console.tink.com/signup) · [Corporate-Onboarding](https://tink.com/get-started/)                                                   | Technische Infrastruktur und lizenzgestützte Open-Banking-Dienstleistungen für passende Geschäftspartner |

Salt Edge bietet besonders interessant ein Partnerprogramm für Unternehmen ohne eigene PSD2-Lizenz, einschließlich vorgefertigter Dashboards für Partner und Endkunden. Yapily Connect bietet ebenfalls ein Modell, in dem der regulierte Dienstleister die entsprechende Lizenzrolle übernimmt.&#x20;



Salt Edge+1



FinAPI bietet eine 30-tägige kostenlose Sandbox-Evaluation und einen separaten regulierten Lizenzservice. Tink unterscheidet ausdrücklich zwischen Kunden mit eigener Zulassung und nicht selbst zugelassenen Unternehmen, deren Endkunden die regulierte Leistung unmittelbar von Tink erhalten.&#x20;



finAPI Technical Documentation+2



Wichtig für die Kosten: Die kostenlose Nutzung von Enable Banking ist nach den Standardbedingungen auf Sandbox-Tests und bestimmte nichtkommerzielle Eigennutzungsfälle beschränkt. Für eine öffentliche GlobalCards-Plattform sind ein Vertrag, Unternehmensprüfung und kommerzielle Konditionen erforderlich.&#x20;



Enable Banking Docs+1



## 3. Es gibt sogar bereits fertige Multi-Banking-Portale!

Hier wird es für GlobalCards besonders interessant: Du musst nicht einmal das komplette Dashboard selbst entwickeln.

[Your Finances — made simple | Actual Budget](https://images.openai.com/static-rsc-4/M1EWs14hgFzK_Kqf4oAzvFS6CU6Da5ZH7hwMAvHJ2GMBAawU7ghrimm_7wC8KM1xcwwYDcYxdmygaz6VBivvYYhtplZi58QtNrGDmh7tL7GqN6U1h3mZQsIelwUTIFVuCf_HJBhXeB_FZ08VbLLi0k6PLWb2_F4v25h3bHB9osk?purpose=inline)

1\. Actual Budget

Vollständige Open-Source-Finanzanwendung mit Konten, Transaktionen, Auswertungen und Banking-Synchronisierung.

Seit Juni 2026 ist eine direkte Enable-Banking-Integration als experimentelle Funktion enthalten. Die November-Version 26.11.0 ergänzt automatische Synchronisierung in bestimmten Nutzungsszenarien.&#x20;



Actual Budget+1



Ideal als sofort vorhandene technische Referenz oder Ausgangspunkt für ein eigenes Portal; kein fertiges reguliertes White-Label-Banking-Produkt.

[GitHub – vollständiger Quellcode](https://github.com/actualbudget/actual)[Enable Banking direkt mit Actual verbinden](https://actualbudget.org/docs/advanced/bank-sync/enable-banking/)

[群晖Docker搭建开源的个人理财记账工具Firefly III | i4T](https://images.openai.com/static-rsc-4/cckNZJgTbneXL_umKlKZUmmbLf2fOMe6IjuJDB0bELUL54XbzoEZ5Vp2k5uUj1TjftLdQ5CYadcN-zmtwWyKYIhkSkM2OsSTzGOCWfNUruA9RNwP6hlistw1ulYMMhIip69ZU7XiOrl_Y7jzArZyuKX006XmO5ukaRWI5FVnvdY?purpose=inline)

2\. Firefly III

Vorhandenes Webportal mit Konten, Transaktionen, Budgets, Berichten, API und separatem Datenimporter.

Der Enable-Banking-Datenimport ist dokumentiert, der aktuelle Implementierungsstatus muss aber vor der Nutzung geprüft werden; die Importer-Dokumentation kennzeichnet ihn teilweise noch als nicht vollständig unterstützt.&#x20;



GitHub+1



[GitHub – Firefly III](https://github.com/firefly-iii/firefly-iii)[GitHub – Data Importer](https://github.com/firefly-iii/data-importer)

[Data Aggregation. Partner Program without licence | Salt Edge](https://images.openai.com/static-rsc-4/gE2k3EKFAe5xl2ti9j0IcLTZ67Ps3usuf3A3GlhVWIGU5gNtMXhVFoVDcRXNb8xea17pC36zRzXOYz3JiYFfEu1VDB79C2ypsVHCCAdAhJ1JzowrqSmcT6igPs1w2EPU3LH8RpgxwZs__-qUFGCig9EHgRFcMlFtABdeJzkFtyg?purpose=inline)

3\. Salt Edge – Partnerprogramm mit Dashboards

Von diesen Möglichkeiten kommt Salt Edge deiner Vorstellung eines fertigen kommerziellen Partnerportals besonders nahe.

Der Anbieter beschreibt bereits vorhandene Partner- und Kunden-Dashboards, eine zentrale API, Consent-Verwaltung und ein Lizenzpartnermodell ohne eigene AISP-Lizenz.&#x20;



Salt Edge



[Fertiges Open-Banking-Partnerprogramm](https://www.saltedge.com/products/account_information/partner_program)[Partner API – Developer Documentation](https://docs.saltedge.com/partners/v1/)

## 4. Enable Banking hat sogar ein fertiges Bankauswahl-Widget

Du kannst die Bankenauswahl direkt in deine eigene GlobalCards-Webseite integrieren.

Die offizielle Widget-Bibliothek unterstützt sowohl `personal` als auch `business`, Länderfilter und Bankensuche.&#x20;



Enable Banking Docs



### Beispiel: Geschäftskonten aus Deutschland auswählen

```

<!-- Enable Banking: Sandbox-Bankauswahl -->
<link
  rel="stylesheet"
  href="https://auth.enablebanking.com/lib/widgets.css"
/>

<script src="https://auth.enablebanking.com/lib/widgets.umd.min.js"></script>

<h2>GlobalCards – Geschäftskonto verbinden</h2>

<enablebanking-aspsp-list
  id="bank-selector"
  country="DE"
  psu-type="business"
  service="AIS"
  sandbox>
</enablebanking-aspsp-list>

<script>
  document
    .getElementById("bank-selector")
    .addEventListener("selected", (event) => {
      // Bank wurde ausgewählt.
      // Der Backend-Autorisierungsprozess
      // muss separat implementiert werden.
      console.log("Ausgewählte Bank:", event.detail);
    });
</script>

```

Das ist die tatsächliche Struktur des dokumentierten Anbieter-Widgets, keine eigens nachgebildete Bankliste. Der gezeigte Code wählt eine Sandbox-Bank aus; er erzeugt noch keine Kontoverbindung. Die vollständige Autorisierung benötigt einen sicheren Backend-Prozess.&#x20;



Enable Banking Docs



Für Privatkonten wird `psu-type="personal"` verwendet. Die vom jeweiligen Institut unterstützten Kontoarten können über die Anbieter-API abgefragt werden.

### So funktioniert der One-Click-Verbindungsablauf

1

Bank auswählen

GlobalCards zeigt die verfügbaren Banken des gewünschten Landes.

2

Verbindung starten

Das Backend startet über Enable Banking die Autorisierung.

3

Bei der Bank bestätigen

Der Kunde authentifiziert sich und erteilt die erforderliche Einwilligung.

4

Konten übernehmen

GlobalCards erhält über die API freigegebene Konto- und Transaktionsinformationen.

5

Multi-Banking-Dashboard

Alle verbundenen Konten werden getrennt nach Inhaber, Organisation und Währung angezeigt.

Der One-Click-Aspekt bezieht sich auf das Starten der Verbindung. Für jedes Konto beziehungsweise jede Bankenverbindung muss der berechtigte Nutzer die erforderliche Bankauthentifizierung und Zustimmung durchlaufen. Geschäftskonten können zusätzliche Zeichnungsberechtigungen oder Mehrpersonenfreigaben erfordern.

Die technische API-Sequenz ist bereits dokumentiert: `GET /aspsps` → `POST /auth` → Bankautorisierung → `POST /sessions` → Konten, Salden und Umsätze.&#x20;



Enable Banking Docs+1



## 5. Vorgefertigter Code: Direkt zu den Repositories

| Quellcode / SDK            | Direkter GitHub-Link                                                                                                                                           | Was vorhanden ist                                    |
| -------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- |
| Enable Banking API Samples | [Offizielle Code-Beispiele](https://github.com/enablebanking/enablebanking-api-samples)                                                 | Go, JavaScript, Python, Java, C#, PHP, Ruby, Postman |
| Enable Banking JS Example  | [JavaScript-Kontoinformation](https://github.com/enablebanking/enablebanking-api-samples/blob/master/js_example/accountInformation.js)  | Kontoautorisierung und AIS                           |
| Enable Banking Python      | [Python-Kontoinformation](https://github.com/enablebanking/enablebanking-api-samples/blob/master/python_example/account_information.py) | API-Integration und Kontodatenabruf                  |
| Enable Banking OpenAPI     | [Offizielle API-Referenz](https://enablebanking.com/docs/api/reference/)                                                                | Endpunkte und Datenmodelle                           |
| Actual Budget              | [Vollständiges Open-Source-Portal](https://github.com/actualbudget/actual)                                                              | Konten, Budgets, Berichte, Bank Sync                 |
| Firefly III                | [Vollständige Finanzanwendung](https://github.com/firefly-iii/firefly-iii)                                                              | Finanzdashboard und REST-API                         |

Die offiziellen Enable-Banking-Codebeispiele stehen unter Apache-2.0. Das macht den Einstieg in die Entwicklung einfacher; die Nutzung der eigentlichen Bankkonnektivität unterliegt trotzdem den separaten Anbieterbedingungen.&#x20;



GitHub



## 6. Meine Zielarchitektur für GlobalCards Multi-Banking

GlobalCards Multi-Banking Portal

B2C Personal · B2B Corporate · Multi-Currency

Personal Accounts

Eigene Konten, Transaktionen, Budget

Business Accounts

Unternehmen, Rollen, Freigaben

Open Banking Aggregation Gateway

Kontoeinwilligungen · Provider-Adapter · Synchronisation · sichere Schlüsselverwaltung

Enable Banking

Salt Edge

finAPI / Yapily

Angeschlossene Banken

Verfügbare Privat- und Geschäftskonten im jeweils unterstützten Land

Für die Speicherung würde ich fünf Hauptbereiche vorsehen: `customers`, `organizations`, `bank_connections`, `accounts` und `transactions`, ergänzt um `consents`, `sync_jobs`, `audit_events` und Zugriffsrechte.

Dabei gilt: Ein persönliches Konto darf nicht allein deshalb im Unternehmensbereich erscheinen, weil derselbe Nutzer beide Bereiche verwaltet. Umgekehrt darf ein Mitarbeiter nicht ohne entsprechende Vollmacht auf sämtliche Firmenkonten zugreifen.

## 7. Konkrete Entwicklungsreihenfolge

| Phase                  | Was du aufbauen kannst                                                                | Kostenstatus                          |
| ---------------------- | ------------------------------------------------------------------------------------- | ------------------------------------- |
| 1. Sandbox             | Enable Banking Developer Account, offizielle Beispiel-APIs, Bank-Widget               | Kostenloser Testzugang                |
| 2. Referenzportal      | Actual Budget mit experimenteller Enable-Banking-Synchronisierung evaluieren          | Open-Source-Software kostenlos        |
| 3. GlobalCards UI      | Eigene B2C-/B2B-Oberfläche, Mandantentrennung und Kontoübersicht                      | Eigene Entwicklung                    |
| 4. Lizenzpartnermodell | Enable Banking, Salt Edge, Yapily und finAPI anfragen                                 | Vertragsangebot erforderlich          |
| 5. Produktion          | Berechtigte Kundeneinwilligungen, KYB, Datenschutz, Support, laufende Synchronisation | Laufende Anbieter- und Betriebskosten |

Eine kostenlose Testumgebung ist keine kostenlose kommerzielle Lizenz. Auch ein vorhandenes Open-Source-Dashboard ersetzt nicht die rechtliche und technische Verantwortung für ein öffentliches Multi-Banking-Angebot.

## 8. Welche Kombination würde ich für GlobalCards wählen?

Für den schnellsten technischen Start: Enable Banking + Actual Budget

Hier existieren bereits die Bankkonnektivität, das UI und ein konkreter Integrationspfad. Die Enable-Banking-Anbindung in Actual ist noch experimentell und muss vor einem produktiven Einsatz geprüft werden.

Für ein kommerzielles Multi-Banking-Portal: Salt Edge oder Yapily Connect

Besonders interessant, weil beide ein reguliertes Partnermodell für Unternehmen ohne eigene AISP-Zulassung beschreiben. Salt Edge verfügt zusätzlich über vorhandene Partner- und Kunden-Dashboards.

Für den deutschen Markt: finAPI als Vergleichspartner

Insbesondere aufgrund der deutschen PSD2-Lizenzmodelle, der vorhandenen WebForms und zusätzlicher Anbindungsmöglichkeiten für weitere Kontenarten.

### Die entscheidende Corporate-Frage

Wenn du bei diesen Unternehmen anfragst, würde ich ausdrücklich nicht nach einer „kostenlosen weltweiten Banklizenz“ fragen, sondern nach:

> „White-Label Open Banking Account Aggregation under your regulated AISP authorisation, including personal and business accounts, hosted consent flows, ready-made bank selection, developer sandbox and multi-tenant portal integration.“

Das trifft wesentlich präziser auf das zu, was du entwickeln möchtest.

Fazit: Ein GlobalCards-Portal, das zahlreiche Privat- und Geschäftskonten über eine einzige technische Integrationsschicht verbindet, ist realistisch. Die Bankenauswahl, die APIs, der Autorisierungsablauf und sogar komplette Finanz-Dashboards sind bereits vorhanden. Die eigentliche Entwicklungsleistung liegt darin, diese Komponenten sicher, mandantenfähig und regulatorisch korrekt zu einem einheitlichen Produkt zu verbinden.
