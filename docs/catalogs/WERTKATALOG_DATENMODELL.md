# Wertkatalog: Datenmodell und Import-Pipeline

Dieses Modell ist ein Recherche- und Metadatenkatalog, keine Preis- oder Anlageberatung. Es trennt beobachtete Marktpreise von Schätzungen, theoretischen Produktionskosten und Fiktion. Ein Preis ohne Stichtag, Einheit, Bewertungsbasis und überprüfbare Quelle darf nicht als verifizierter Wert ausgegeben werden.

## Dateien

- `docs/catalogs/WERTKATALOG_MASTER.csv` — UTF-8-CSV mit Beispieldatensätzen und leer gelassenen, nicht belegten Preisen.
- `docs/schemas/WERTKATALOG_RECORD.schema.json` — JSON Schema für normalisierte Datensätze.
- `docs/catalogs/WERTKATALOG_QUELLEN.csv` — Quellenregister für erste offizielle bzw. primäre Rechercheportale.

## Datenebenen

1. **Raw** — unveränderte Quellantworten bzw. manuelle Notizen, Abrufzeit, Quell-URL und Lizenzhinweis; keine stillschweigende Bereinigung.
2. **Normalized** — Namen, Einheiten, ISO-4217-Währungen, Datumsformate, Kategorien und Identifikatoren vereinheitlichen. Rohwerte und Umrechnungsfaktoren erhalten.
3. **Curated** — Dubletten zusammenführen, Evidenz prüfen, Bewertung klassifizieren und Freigabestatus setzen. Für jeden Preis sind Quelle, Stichtag und Basis Pflicht.
4. **Published** — CSV/JSON-Exporte mit Quellenangaben und klarer Kennzeichnung von Unsicherheit; fiktionale und reale Einträge getrennt filterbar.

## Bewertungsregeln

- `spot_market` und `auction_sale` beschreiben beobachtete Transaktionen bzw. Marktangaben, nicht universelle intrinsische Werte.
- `production_cost_estimate`, `scenario_estimate` und `replacement_cost` sind Schätzungen und müssen als solche bezeichnet werden.
- Isotope, Antimaterie und andere nicht frei gehandelte oder kontrollierte Güter erhalten keinen erfundenen Marktpreis. Es werden hier keine Produktions-, Beschaffungs- oder Handhabungsanleitungen erfasst.
- Daten, Patente, Vertrauen, Zertifikate, Archive und Schatzreserven haben oft keine vergleichbare Einzelpreisnotierung. Bewertungsmethode und Bewertungsumfang dokumentieren.
- Fiktionale Objekte (z. B. Sternen- oder Planetenkristalle) werden als `fictional` geführt und von realen Ranglisten ausgeschlossen.
- Quellenlizenz, Nutzungsbedingungen, Abrufdatum und geografischer Geltungsbereich vor Wiederveröffentlichung prüfen.

## Import- und Qualitätschecks

1. Quelle registrieren und Nutzungsrechte prüfen.
2. Originaldatei unverändert im Raw-Bereich sichern und Hash/Erfassungszeit protokollieren.
3. Felder in das normalisierte Schema überführen; keine Schätzwerte in beobachtete Preise umwandeln.
4. Werte, Währung, Einheit und Stichtag validieren; fehlende Werte bleiben leer/null, nicht `0`.
5. Dubletten und Widersprüche markieren; Review durch Menschen.
6. Export nur aus `verified` oder ausdrücklich als Schätzung markierten Datensätzen.

Die CSV ist ein Startgerüst und keine vollständige oder bereits geprüfte 111-Quellen-Sammlung. Preise und Behauptungen müssen vor Aufnahme einzeln anhand der Originalquelle validiert werden.
