# Konzept 09 — DTCC: Universal Open Compliance Tech Stack

**Kurzname:** „Universal Open Compliance Tech Stack“ (Dateiname: `blank.pdf`)
**Dateien:** `blank.pdf` (1 Datei, 38 Seiten, Firefox-Druck eines Gemini-Chats)

---

## 1. Was ist das Dokument?

Ein ausgedruckter **Gemini-Chat** (URL: `gemini.google.com/app/f490a32cd2b8a7cc`), der unter dem
Titel **„Universal Open Compliance Tech Stack“** eine vertiefte Analyse der **DTCC**
(Depository Trust & Clearing Corporation) und deren Anbindungsmöglichkeiten dokumentiert.

## 2. Die DTCC — Grundlagen

- **Gründung:** 1999 · **Eigentümer:** die Finanzindustrie selbst (brancheneigen und -regiert)
- **Hauptsitz:** New York City
- **Funktion:** Automatisiert, zentralisiert und standardisiert die Abwicklung (Clearing und
  Settlement) von Finanztransaktionen

### Kernaufgaben
- **Wertpapiersammelbank (CSD):** Verwahrt den Großteil aller US-Wertpapiere, sichert Billionenwerte ab
- **Clearing und Settlement:** Wickelt täglich Transaktionen im Billionenbereich ab (Aktien, Anleihen, Derivate)
- **Risikominimierung:** Reduziert systemische Risiken im Handelsnachbereich (Post-Trade)
- **Digitale Assets:** Arbeitet an Tokenisierungsprojekten und der Verbindung traditioneller
  Märkte mit Blockchain-Infrastrukturen

### Die drei Haupttochtergesellschaften
| Tochter | Kernfunktion | Hauptaufgaben |
|---------|--------------|---------------|
| **DTC** (The Depository Trust Company) | Zentralverwahrer (CSD) | Elektronische Verwahrung, Eigentumsübertragung, Kapitalmaßnahmen (Dividenden) |
| **NSCC** (National Securities Clearing Corporation) | Zentrale Gegenpartei (CCP) für den Aktienmarkt | Clearing von Aktien/Anleihen/ETFs, Garantie der Abwicklung, multilaterales Netting |
| **FICC** (Fixed Income Clearing Corporation) | CCP für Rentenmärkte | Clearing/Netting festverzinslicher Papiere; Government Securities Division + Mortgage-Backed Securities Division |

**Zusammenspiel:** NSCC garantiert den Handel und saldiert (Netting) → weist DTC an, die
elektronischen Besitzrechte final umzubuchen (Settlement).

## 3. Tokenisierungs-Partner der DTCC

- **Chainlink:** Integration der Chainlink Runtime Environment (CRE) für die globale
  „Collateral AppChain“ (Schnittstellen-Echtzeitbepreisung)
- **Stellar Development Foundation:** Anbindung des tokenisierten DTCC-Services an das
  öffentliche Stellar-Netzwerk (liquide DTC-verwahrte Aktien und US-Treasuries)
- **Digital Asset:** Tokenisierung auf Basis des datenschutzkonformen **Canton Networks**

## 4. Technische Anbindung (Developer Lifecycle)

1. **Account erstellen:** Registrierung im DTCC API Marketplace Portal
2. **Integrations-Setup:** Dedizierter DTCC Integration Consultant; OAuth 2.0 +
   zertifikatsbasierte Authentifizierung
3. **Entwicklung & Testing (Sandbox):** Conformance Testing
4. **Go-Live:** Produktive API-Lösung mit Hypercare-Support

### Wichtige API-Kategorien
| Geschäftsbereich | API-Service | Funktion |
|------------------|-------------|----------|
| Clearing Services | Account Transfer (ACATS) API | Depotüberträge zwischen Brokern/Banken |
| Risikomanagement | Clearing Fund Management API | Margin-Anforderungen, Sicherheiten |
| Wertpapierabwicklung | ALERT API Suite | Standing Settlement Instructions (SSIs) in Echtzeit (T+1) |
| Corporate Actions | ClaimConnect API | Automatisierte Übermittlung finanzieller Ansprüche |
| Sicherheit | User Password Management API | Passwort-Überwachung/Reset via OAuth |

### Das Integrated Delivery Framework (IDF)
- **Mandatory Request Details:** Jede API-Anfrage erfordert dasselbe Set an
  Identifikations- und Validierungsdaten im Header
- **Traceability:** Daten werden unverändert durchgereicht — dieselbe Transaction-ID vom
  Clearing-Antrag bis zur finalen Depot-Umbuchung

### Vierstufiger Implementierungsfahrplan
1. **Vorbereitung:** Registrierung, Benennung eines **SAC** (Super Access Coordinator)
2. **Architektur:** DTCC Integration Consultant, Connectivity-Setup
3. **Sandbox-Test:** SDKs, JSON-Starter-Kits, EDI-Middleware (PilotFish eiConsole, Adeptia),
   Conformance Testing
4. **Go-Live & Support:** Freigabe, Produktivschaltung, Hypercare

### Zuständige Integrationsteams
| Modulgruppe | Team |
|-------------|------|
| Aktienmarkt (ACATS, UTC, Clearing) | NSCCIntegration@dtcc.com |
| Rentenmarkt (FICC Risk, Staatsanleihen) | FICC Integration Team |
| Asset Services (ClaimConnect, Dividenden) | TAServices@dtcc.com |
| Global Trade Reporting (Derivate) | GTR-Onboarding@dtcc.com |

## 5. Bedeutung für das Gesamtwerk

Das Dokument dient als **Referenz- und Vergleichsgrundlage** für die eigene
Finanzinfrastruktur-Konzepte (Konzepte 02–07): Wie baut man Clearing/Settlement-Module
industriell an? Welche APIs, Frameworks und Prozesse sind der Standard?

## 6. Querverweise

- → Konzept 02 (Finance System): Ledger-/Settlement-Prozesse
- → Konzept 05 (Blockchain): Atomic Swap vs. CCP-Netting
- → Konzept 03 (Krypto-Fiat): Tokenisierungs-Partner (Chainlink, Stellar, Canton)


---
*Kapitel 09 · ~1.6 Seiten · 569 Wörter · Beginn S. 14*
