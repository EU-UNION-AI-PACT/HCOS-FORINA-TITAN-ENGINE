# Konzept 14 — Patent API Integration (MCP-Pipeline)

**Kurzname:** „Patent API Integration“ — MCP-Server für Patentdaten
**Dateien:** `Patent API Integration.pdf` (×6, alle identisch)

---

## 1. Grundidee

Die Integration von **offenen Patentdaten-APIs** (WIPO, EPO, EUIPO, Nationalbibliotheken)
in ein **MCP-Server-System** (Model Context Protocol), das KI-Agenten Zugriff auf
Patentdaten ermöglicht.

## 2. Die Architektur (5 Ebenen)

```
┌─────────────────────────────────────────────────────────┐
│  1. Open Data Layer                                      │
│     WIPO · EPO · EUIPO · Nationalbibliotheken            │
├─────────────────────────────────────────────────────────┤
│  2. API Connector Layer                                  │
│     Wrapper · Adapter · Normalizer · Rate Limit · Auth   │
├─────────────────────────────────────────────────────────┤
│  3. Data / Evidence Layer                                │
│     Provenienz · Hash · Unveränderbarkeit                │
├─────────────────────────────────────────────────────────┤
│  4. Registry / Pipeline Layer                            │
│     Indexierung · Verknüpfung · Historisierung           │
├─────────────────────────────────────────────────────────┤
│  5. MCP Server → Agent                                   │
│     Tool-Registry · Prompt-Integration · Agent-Aufruf    │
└─────────────────────────────────────────────────────────┘
```

### Ebene 1: Open Data Layer
- **WIPO** (World Intellectual Property Organization)
- **EPO** (European Patent Office)
- **EUIPO** (European Union Intellectual Property Office)
- **Nationalbibliotheken** (z. B. DNB, BnF)

### Ebene 2: API Connector Layer
- **Wrapper:** Einheitliche Schnittstelle über heterogene APIs
- **Adapter:** Format-Umwandlung (JSON, XML, CSV)
- **Normalizer:** Standardisierung der Datenmodelle
- **Rate Limit:** Einhaltung der API-Limits
- **Auth:** Authentifizierung (API-Keys, OAuth)

### Ebene 3: Data / Evidence Layer
- **Provenienz:** Herkunft jedes Datensatzes dokumentiert
- **Hash:** SHA-256-Hash für Unveränderbarkeit
- **Unveränderbarkeit:** Daten werden nicht verändert, nur versioniert

### Ebene 4: Registry / Pipeline Layer
- **Indexierung:** Volltext- und Metadaten-Index
- **Verknüpfung:** Cross-Referenzen zwischen Patenten
- **Historisierung:** Zeitliche Versionierung

### Ebene 5: MCP Server → Agent
- **Tool-Registry:** MCP-Tools für Patentabfragen
- **Prompt-Integration:** Patentdaten in KI-Prompts
- **Agent-Aufruf:** KI-Agenten können Patentdaten abrufen

## 3. Bedeutung im Gesamtwerk

Die Patent API Integration ist die **praktische Umsetzung** der „System Access Points“
(Konzept 13) für den Bereich **geistiges Eigentum**:
- Sie verbindet die EUIPO/EPA-Korrespondenz (Konzept 15) mit einer technischen Infrastruktur
- Sie ermöglicht KI-Agenten, Patentdaten automatisch abzufragen und zu analysieren
- Sie ist Teil der größeren „IHoLyCLaK“-Pipeline (Konzept 11)

## 4. Wichtige Begriffe

| Begriff | Bedeutung |
|---------|-----------|
| MCP | Model Context Protocol (KI-Agent-Integration) |
| WIPO | World Intellectual Property Organization |
| EPO | European Patent Office |
| EUIPO | European Union Intellectual Property Office |
| Provenienz | Herkunft/Dokumentation der Datenquelle |
| Rate Limit | Begrenzung der API-Aufrufe |

## 5. Querverweise

- → Konzept 13 (System Access Points): Föderierte Registry-Logik
- → Konzept 15 (EUIPO/EPA): Patent- und Markenkorrespondenz
- → Konzept 11 (IHoLyCLaK): Pipeline-Automatisierung
- → Konzept 26 (Sonstiges): `pasted-text-9419a806` (111+ MCP-Tools)


---
*Kapitel 14 · ~1.2 Seiten · 417 Wörter · Beginn S. 21*
