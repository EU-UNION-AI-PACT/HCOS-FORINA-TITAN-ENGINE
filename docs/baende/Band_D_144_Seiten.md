# HCOS FORINA TITAN · Band D

## Normen, Zertifizierung, Abzeichen und Audit-Automation

34 Norm- und Regulierungs-Dossiers mit Pruefkriterien, Evidence, URLs und Zeichenpolitik

**Stand:** 06.11.2026; **Code-Referenz:** https://github.com/EU-UNION-AI-PACT/HCOS-FORINA-TITAN-ENGINE/commit/4cd1db2066237798717d201fc4a0a46759664a85

**Rechts-/Markenhinweis:** Interne Audit-Pruefung ist nicht gleich amtliche Zulassung oder externe Zertifizierung. Das Markenrecht der jeweiligen Organisation ist gesondert zu beachten. Keine personenbezogenen Geheimnisse oder Produktionsdaten.


---

## 01. EU-DSGVO / GDPR (EU) 2016/679

**Referenz:** https://eur-lex.europa.eu/eli/reg/2016/679/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** Europäische Union / Datenschutzaufsichten

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

EU-DSGVO / GDPR (EU) 2016/679 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: Europäische Union / Datenschutzaufsichten. Im HCOS-System lautet die notwendige Vorfrage: Personenbezogene Daten in Accounts, Finanzanalyse, Support und Telemetrie. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Rechtsgrundlage und Zweckbindung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Datenminimierung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Betroffenenrechte wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. TOMs wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Auftragsverarbeitung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Löschfristen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. RoPA mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Datenschutzhinweise mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. DPIA-Entscheidung mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Consent-Receipt mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Löschtest mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Zugriffsprotokoll mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Interner DSGVO-Nachweis ist kein staatliches DSGVO-Zertifikat; etwaige Zertifizierungsverfahren sind von zuständigen Stellen und Artikel 42 abhängig. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2016/679/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 02. DORA Verordnung (EU) 2022/2554

**Referenz:** https://eur-lex.europa.eu/eli/reg/2022/2554/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU / ESAs und zuständige nationale Finanzaufsicht

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

DORA Verordnung (EU) 2022/2554 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU / ESAs und zuständige nationale Finanzaufsicht. Im HCOS-System lautet die notwendige Vorfrage: Finanzunternehmen und ICT-Drittparteien je konkretem persönlichen und sachlichen Anwendungsbereich. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. ICT-Risikomanagement wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Vorfallmanagement wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Resilienztests wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Drittparteirisiko wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Governance wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Informationsaustausch wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. ICT-Asset-Register mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. kritische Dienstekette mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Vorfallplan mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Exit-Strategie mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Testprotokoll mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Dienstleisterverträge mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Keine allgemeine DORA-Zertifizierung aus Eigenprüfung; Regulierung und behördliche Aufsicht je Norm und Rolle. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2022/2554/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 03. NIS2 Richtlinie (EU) 2022/2555

**Referenz:** https://eur-lex.europa.eu/eli/dir/2022/2555/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU-Mitgliedstaaten / nationale zuständige Behörden

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

NIS2 Richtlinie (EU) 2022/2555 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU-Mitgliedstaaten / nationale zuständige Behörden. Im HCOS-System lautet die notwendige Vorfrage: Wesentliche oder wichtige Einrichtungen nach sektor- und größenbezogener nationaler Umsetzung. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Risikomanagement wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Lieferkette wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Incident Handling wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Meldewege wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Geschäftsleitung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. BCM wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Anwendbarkeitsanalyse mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Assetliste mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Meldeplan mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Lieferantenbeurteilungen mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Awareness mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Tests mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Kein offizielles EU-NIS2-Siegel durch Software; nationale Umsetzung und Fristen sind gesondert zu prüfen. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/dir/2022/2555/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 04. EU AI Act (EU) 2024/1689

**Referenz:** https://eur-lex.europa.eu/eli/reg/2024/1689

**Instrumenttyp:** GESETZ; **Zustaendig:** EU / AI Office und nationale Marktüberwachung

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

EU AI Act (EU) 2024/1689 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU / AI Office und nationale Marktüberwachung. Im HCOS-System lautet die notwendige Vorfrage: KI-Provider oder Deployer nach Rolle, Systemzweck, Risikoklasse und geltender gestaffelter Anwendungsphase. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Risikoklassifizierung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Verbotstatbestände wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Transparenz wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. High-Risk-Prozesse wo anwendbar wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. menschliche Aufsicht wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Dokumentation wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. AI-Systeminventar mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Use-Case-Factsheet mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Risikoentscheidung mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Daten-Governance mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Testfälle mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Nutzungsinformation mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Keine pauschale AI-Act-Zertifizierung; bei einschlägigen Konformitätsverfahren sind Rechtsgrundlage und Stelle nachzuweisen. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2024/1689, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 05. Cyber Resilience Act (EU) 2024/2847

**Referenz:** https://eur-lex.europa.eu/eli/reg/2024/2847/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU / Marktüberwachungs- und Konformitätsstellen

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

Cyber Resilience Act (EU) 2024/2847 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU / Marktüberwachungs- und Konformitätsstellen. Im HCOS-System lautet die notwendige Vorfrage: Produkte mit digitalen Elementen, die in Anwendungsbereich und Übergangsfristen fallen. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Secure by Design wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Schwachstellenmanagement wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Herstellerpflichten wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. technische Dokumentation wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Update- und Meldewege wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Produktklassifizierung mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. SBOM mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Schwachstellenprozess mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Sicherheitsupdates mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. technische Akte mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Risikoanalyse mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

CE-Zeichen nur bei nachweislich einschlägigem Produkt und korrekt durchlaufenem Konformitätsprozess, nicht für das Portal als Ganzes. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2024/2847/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 06. MiCA Verordnung (EU) 2023/1114

**Referenz:** https://eur-lex.europa.eu/eli/reg/2023/1114/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU / zuständige Finanzaufsicht, ESMA und EBA

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

MiCA Verordnung (EU) 2023/1114 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU / zuständige Finanzaufsicht, ESMA und EBA. Im HCOS-System lautet die notwendige Vorfrage: Crypto-Asset-Dienstleistung, Emission oder bestimmte Tokenarten nach konkreter Tätigkeit. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Token-Klassifikation wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Whitepaper wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Emittentenpflichten wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. CASP-Lizenzstatus wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Beschwerdeweg wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Marktmissbrauchsschutz wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Token-Dossier mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Registerauszug mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Whitepaper-Referenz mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Custody-Rechte mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Compliance-Mapping mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Freigabeprotokoll mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Kein MiCA-Approved-Badge ohne amtlichen Status; Selbstbewertung ist maximal eine vorbereitende Prüfdokumentation. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2023/1114/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 07. eIDAS 2 / EU Digital Identity (EU) 2024/1183

**Referenz:** https://eur-lex.europa.eu/eli/reg/2024/1183/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU-Mitgliedstaaten / Vertrauensdiensteaufsicht

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

eIDAS 2 / EU Digital Identity (EU) 2024/1183 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU-Mitgliedstaaten / Vertrauensdiensteaufsicht. Im HCOS-System lautet die notwendige Vorfrage: Digitale Identitäten, Vertrauensdienste, Wallet-Ökosystem und qualifizierte Dienste je Rolle. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Identitätsbindung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Wallet-Vertrauensmodell wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Verifizierbarkeit wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Attributfreigabe wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Widerruf wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Interoperabilität wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. DID-/VC-Profile mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Vertrauensliste mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Issuer-Evidence mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Wallet-Tests mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Signaturprüfung mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Scope mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Eine eigene Wallet oder eine Ed25519-Signatur ist nicht automatisch ein qualifizierter Vertrauensdienst. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2024/1183/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 08. PSD2 Richtlinie (EU) 2015/2366

**Referenz:** https://eur-lex.europa.eu/eli/dir/2015/2366/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU / nationale Finanzaufsichten

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

PSD2 Richtlinie (EU) 2015/2366 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU / nationale Finanzaufsichten. Im HCOS-System lautet die notwendige Vorfrage: Account Information oder Payment Initiation Services, einschlägige Zahlungsvorgänge und zugelassene Anbieter. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Starke Kundenauthentifizierung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Kundeneinwilligung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Schnittstellenrechte wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Sicherheitsmaßnahmen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Providerrolle wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Beschwerdeweg wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Consent-Scope mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. SCA-Test mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Rollen-/Lizenzanalyse mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Providervertrag mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Access Log mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Widerrufstest mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Nur Read-only-Kontodatenzugriff ist technisch und rechtlich sauber von Zahlungsauslösung zu trennen. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/dir/2015/2366/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 09. EU AML-Regelwerk / AMLR (EU) 2024/1624

**Referenz:** https://eur-lex.europa.eu/eli/reg/2024/1624/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU / AMLA, Finanzaufsichten und FIUs

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

EU AML-Regelwerk / AMLR (EU) 2024/1624 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU / AMLA, Finanzaufsichten und FIUs. Im HCOS-System lautet die notwendige Vorfrage: Verpflichtete Unternehmen und einschlägige Tätigkeiten unter abgestuften Anwendungsdaten. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Kundensorgfalt wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. wirtschaftlich Berechtigte wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Monitoring wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Verdachtsmeldungen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Aufbewahrung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Kontrollen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Produktrollenmatrix mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. AML-Policy mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. synthetische Screening-Fälle mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Eskalationsprozess mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Trainingsbeleg mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Automatisierte Analyse ersetzt nicht behördliche Anforderungen, professionelle Beurteilung oder gesetzlich gebotene Meldungen. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2024/1624/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 10. DLT-Pilotverordnung (EU) 2022/858

**Referenz:** https://eur-lex.europa.eu/eli/reg/2022/858/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU / ESMA und nationale Finanzmarktaufsichten

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

DLT-Pilotverordnung (EU) 2022/858 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU / ESMA und nationale Finanzmarktaufsichten. Im HCOS-System lautet die notwendige Vorfrage: Bestimmte DLT-Marktinfrastrukturen und Finanzinstrumente nach Ausnahme- und Zulassungsrahmen. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Rechtliche Klassifikation wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Betriebsmodell wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. DLT-Risiken wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Marktinfrastruktur-Governance wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Teilnehmerrechte wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Exit wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. DLT-Architektur mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Zulassungspfad mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Aufsichtsentscheid mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Settlement-Finality-Matrix mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Testnet-Protokoll mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Kein automatischer DLT-Pilot-Status allein aufgrund technischer Tokenisierung. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2022/858/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 11. European Accessibility Act (EU) 2019/882

**Referenz:** https://eur-lex.europa.eu/eli/dir/2019/882/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU-Mitgliedstaaten / Marktüberwachung

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

European Accessibility Act (EU) 2019/882 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU-Mitgliedstaaten / Marktüberwachung. Im HCOS-System lautet die notwendige Vorfrage: Bestimmte Produkte und Dienstleistungen mit Barrierefreiheitsanforderungen. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Bedienbarkeit wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Verständlichkeit wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Eingabehilfe wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Dokumentation wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Supportzugang wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. zugängliche Interaktion wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. WCAG-Mapping mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Tastaturtest mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Screenreader-Test mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Kontrastbericht mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Fehlerbehebungsplan mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Ein internes Accessibility-Label ist keine amtliche Marktfreigabe oder pauschale EAA-Konformität. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/dir/2019/882/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 12. EU Data Act (EU) 2023/2854

**Referenz:** https://eur-lex.europa.eu/eli/reg/2023/2854/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** Europäische Union / nationale zuständige Stellen

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

EU Data Act (EU) 2023/2854 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: Europäische Union / nationale zuständige Stellen. Im HCOS-System lautet die notwendige Vorfrage: Zugriff auf bestimmte Produkt- und Dienstdaten, Cloudwechsel und Datennutzung nach Anwendbarkeit. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Datenzugangsrechte wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Fairness wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Portabilität wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Schutz von Geschäftsgeheimnissen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Interoperabilität wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Vertragspflichten wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Data Inventory mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. API-Export-Test mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Data-Sharing-Kontrakt mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Lösch-/Wechselplan mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Jurisdiktionsanalyse mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Ein universeller Datenfreigabeanspruch folgt nicht aus dem Namen Data Act; konkrete Regeln sind zu prüfen. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2023/2854/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 13. Data Governance Act (EU) 2022/868

**Referenz:** https://eur-lex.europa.eu/eli/reg/2022/868/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU / zuständige nationale Behörden

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

Data Governance Act (EU) 2022/868 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU / zuständige nationale Behörden. Im HCOS-System lautet die notwendige Vorfrage: Besondere Datenvermittlungsdienste, geschützte öffentliche Daten und Datenaltruismus. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Intermediary-Rollen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Zwecktrennung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. organisatorische Unabhängigkeit wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Vertrauen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Transparenz wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Register wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Vermittlungsmodell mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Data-Sharing-Katalog mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Governance-Regeln mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Anbieter-Status mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Nutzungsbedingungen mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Keine amtliche Datenvermittler-Anerkennung durch selbstgeneriertes Badge. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2022/868/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 14. Digital Services Act (EU) 2022/2065

**Referenz:** https://eur-lex.europa.eu/eli/reg/2022/2065/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU / Digital Services Coordinators und Kommission

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

Digital Services Act (EU) 2022/2065 ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU / Digital Services Coordinators und Kommission. Im HCOS-System lautet die notwendige Vorfrage: Vermittlungsdienste oder Plattformdienste entsprechend ihrer tatsächlichen Funktion. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Kontaktstellen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Transparenz wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Meldungsbearbeitung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Beschwerdewege wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. ggf. zusätzliche Plattformpflichten wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Serviceklassifizierung mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Notice-and-Action-Prozess mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Moderationsaudit mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Berichtspflichtenentscheidung mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Ein internes Moderationsboard beweist keine Erfüllung aller DSA-Pflichten. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2022/2065/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 15. EU Taxonomy (EU) 2020/852 / ESG

**Referenz:** https://eur-lex.europa.eu/eli/reg/2020/852/oj

**Instrumenttyp:** GESETZ; **Zustaendig:** EU / Finanz- und Nachhaltigkeitsaufsicht

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

EU Taxonomy (EU) 2020/852 / ESG ist ein rechtlich bindendes oder national umzusetzenes Regelwerk; die Anwendbarkeit kann stark von Rolle, Sektor, Zeitpunkt und Rechtsraum abhaengen. Zuständige Quelle beziehungsweise Scheme-Halter: EU / Finanz- und Nachhaltigkeitsaufsicht. Im HCOS-System lautet die notwendige Vorfrage: Bestimmte Finanzprodukte, Unternehmen und Nachhaltigkeitsangaben nach anwendbaren Offenlegungspflichten. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Technische Bewertung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Tätigkeitsklassifikation wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. DNSH wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Mindestschutz wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Nachweise wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Datenqualität wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Asset-Taxonomy Map mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Prüfmethoden mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Quellen-Datum mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Nichtanwendbarkeitsentscheidung mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Review mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Ein grün gefärbtes ESG-Symbol ist kein geprüfter Taxonomie-Konformitätsnachweis. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://eur-lex.europa.eu/eli/reg/2020/852/oj, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 16. ISO/IEC 27001:2022 Informationssicherheitsmanagement

**Referenz:** https://www.iso.org/standard/27001

**Instrumenttyp:** NORM; **Zustaendig:** ISO/IEC / akkreditierte Zertifizierungsstelle

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

ISO/IEC 27001:2022 Informationssicherheitsmanagement ist eine technische beziehungsweise Management-Norm; nicht jede Norm ist selbst eigenstaendig zertifizierbar. Zuständige Quelle beziehungsweise Scheme-Halter: ISO/IEC / akkreditierte Zertifizierungsstelle. Im HCOS-System lautet die notwendige Vorfrage: ISMS für den festgelegten organisatorischen und technischen Geltungsbereich. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Kontext und Risiken wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. ISMS-Führung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Anwendbarkeitserklärung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Maßnahmen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Audits wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. kontinuierliche Verbesserung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Scope Statement mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Risk Register mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. SoA mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. interne Audits mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Management Review mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Wirksamkeitsbelege mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

„ISO-zertifiziert“ nur mit gültigem Zertifikat einer zuständigen Stelle im nachgewiesenen Scope; ISO-Logo nicht frei nutzbar. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.iso.org/standard/27001, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 17. ISO/IEC 27002:2022 Security Controls

**Referenz:** https://www.iso.org/standard/75652.html

**Instrumenttyp:** NORM; **Zustaendig:** ISO/IEC

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

ISO/IEC 27002:2022 Security Controls ist eine technische beziehungsweise Management-Norm; nicht jede Norm ist selbst eigenstaendig zertifizierbar. Zuständige Quelle beziehungsweise Scheme-Halter: ISO/IEC. Im HCOS-System lautet die notwendige Vorfrage: Leitfaden für Informationssicherheitsmaßnahmen und deren Umsetzung. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Organisatorische Kontrollen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. personelle Kontrollen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. physische Kontrollen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. technische Kontrollen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Wirksamkeit wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Control Catalogue mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Maßnahmenbelege mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Verantwortliche mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Audit-Proben mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Gap-Analyse mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

27002 selbst ist ein Controls-Leitfaden; daraus folgt kein eigenständiges Unternehmenszertifikat. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.iso.org/standard/75652.html, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 18. ISO/IEC 27701:2025 PIMS

**Referenz:** https://committee.iso.org/standard/27701

**Instrumenttyp:** NORM; **Zustaendig:** ISO/IEC / ggf. Zertifizierungsstelle

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

ISO/IEC 27701:2025 PIMS ist eine technische beziehungsweise Management-Norm; nicht jede Norm ist selbst eigenstaendig zertifizierbar. Zuständige Quelle beziehungsweise Scheme-Halter: ISO/IEC / ggf. Zertifizierungsstelle. Im HCOS-System lautet die notwendige Vorfrage: Privacy Information Management System für Controller und Processor nach scope. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. PII-Governance wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Rollen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Privacy Risks wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Rechteprozesse wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Datenschutzkontrollen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Verbesserung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. PIMS Scope mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Dateninventar mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Datenschutzprüfung mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Betroffenenrechte mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Prozessaudit mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

2025er Ausgabe getrennt von 2019er Ausgabe behandeln; externe Zertifizierung nur bei bestehendem Prüfweg behaupten. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://committee.iso.org/standard/27701, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 19. ISO/IEC 42001:2023 AIMS

**Referenz:** https://www.iso.org/standard/42001

**Instrumenttyp:** NORM; **Zustaendig:** ISO/IEC / Zertifizierungsstelle

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

ISO/IEC 42001:2023 AIMS ist eine technische beziehungsweise Management-Norm; nicht jede Norm ist selbst eigenstaendig zertifizierbar. Zuständige Quelle beziehungsweise Scheme-Halter: ISO/IEC / Zertifizierungsstelle. Im HCOS-System lautet die notwendige Vorfrage: AI Management System für Entwicklung oder Nutzung von KI im festgelegten Scope. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. AI-Governance wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Risiko- und Wirkungsbewertung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Systeminventar wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Prozesse wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Evaluierung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Verbesserung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. AI Policy mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Systemliste mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Risikodossier mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Modelltests mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Managementreview mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Human Oversight mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Ein KI-Projekt erhält kein ISO/IEC-42001-Siegel durch eigenen Testbericht. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.iso.org/standard/42001, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 20. ISO 9001:2026 Qualitätsmanagement

**Referenz:** https://www.iso.org/9001-2026

**Instrumenttyp:** NORM; **Zustaendig:** ISO / Zertifizierungsstelle

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

ISO 9001:2026 Qualitätsmanagement ist eine technische beziehungsweise Management-Norm; nicht jede Norm ist selbst eigenstaendig zertifizierbar. Zuständige Quelle beziehungsweise Scheme-Halter: ISO / Zertifizierungsstelle. Im HCOS-System lautet die notwendige Vorfrage: QMS mit Prozessqualität, Kundenbezug und kontinuierlicher Verbesserung. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Führung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Qualitätsziele wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Prozesssteuerung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Risiko und Chance wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Nichtkonformität wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Managementreview wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Prozesskarte mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. KPIs mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Abweichungen mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Korrekturmaßnahmen mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Auditkalender mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Managementreview mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Die 2026er Ausgabe ersetzt 2015; Übergangsbedingungen sind mit Zertifizierern zu klären. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.iso.org/9001-2026, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 21. ISO 22301:2019 Business Continuity

**Referenz:** https://www.iso.org/standard/75106.html

**Instrumenttyp:** NORM; **Zustaendig:** ISO / Zertifizierungsstelle

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

ISO 22301:2019 Business Continuity ist eine technische beziehungsweise Management-Norm; nicht jede Norm ist selbst eigenstaendig zertifizierbar. Zuständige Quelle beziehungsweise Scheme-Halter: ISO / Zertifizierungsstelle. Im HCOS-System lautet die notwendige Vorfrage: Business Continuity Management für definierte kritische Dienstleistungen. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Business Impact Analysis wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. RTO/RPO wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Fortführungsstrategien wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Übungen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Notfallkommunikation wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Verbesserungen wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. BIA mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Recovery-Pläne mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Restore-Test mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Übungsbericht mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Krisenrollen mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Recovery-KPIs mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Ein Backup allein beweist kein zertifiziertes BCMS; Geltungsbereich und Wirksamkeit zählen. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.iso.org/standard/75106.html, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 22. ISO/IEC 20000-1:2018 Service Management

**Referenz:** https://www.iso.org/standard/70636.html

**Instrumenttyp:** NORM; **Zustaendig:** ISO/IEC / Zertifizierungsstelle

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

ISO/IEC 20000-1:2018 Service Management ist eine technische beziehungsweise Management-Norm; nicht jede Norm ist selbst eigenstaendig zertifizierbar. Zuständige Quelle beziehungsweise Scheme-Halter: ISO/IEC / Zertifizierungsstelle. Im HCOS-System lautet die notwendige Vorfrage: Servicemanagementsystem für definierte IT-Dienstleistungen. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Service Design wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Incident- und Change-Management wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Supplier Control wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Service Levels wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Continual Improvement wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Service-Katalog mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. SLA/SLO mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Incident Records mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Change Freigaben mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Lieferantenreview mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Nur ein externer, scopegebundener Prüfprozess kann eine Zertifizierungsbehauptung tragen. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.iso.org/standard/70636.html, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 23. ISO/IEC 27017:2015 Cloud Controls

**Referenz:** https://www.iso.org/standard/43757.html

**Instrumenttyp:** NORM; **Zustaendig:** ISO/IEC

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

ISO/IEC 27017:2015 Cloud Controls ist eine technische beziehungsweise Management-Norm; nicht jede Norm ist selbst eigenstaendig zertifizierbar. Zuständige Quelle beziehungsweise Scheme-Halter: ISO/IEC. Im HCOS-System lautet die notwendige Vorfrage: Sicherheitsmaßnahmen für Cloud-Service-Provider und Cloud-Kunden als ergänzende Orientierung. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Shared Responsibility wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Provisioning wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Virtualization Security wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Cloud Logging wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Asset Return wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Tenant Isolation wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Responsibility Matrix mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Cloud Config mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Access Review mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Third Party Contract mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Log Hygiene mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Eine Umsetzung einzelner Cloud-Controls ist nicht automatisch ein ISO-27017-Zertifikat. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.iso.org/standard/43757.html, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 24. ISO/IEC 27018:2019 Public Cloud Privacy

**Referenz:** https://www.iso.org/standard/76559.html

**Instrumenttyp:** NORM; **Zustaendig:** ISO/IEC

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

ISO/IEC 27018:2019 Public Cloud Privacy ist eine technische beziehungsweise Management-Norm; nicht jede Norm ist selbst eigenstaendig zertifizierbar. Zuständige Quelle beziehungsweise Scheme-Halter: ISO/IEC. Im HCOS-System lautet die notwendige Vorfrage: Schutz personenbezogener Informationen bei Public-Cloud-Verarbeitung nach anwendbarer Rolle. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. PII Handling wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Löschung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Transparenz wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Subprocessing wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Zugriffskontrolle wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Auditing wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Cloud Processing Agreement mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Löschbestätigung mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. PII Inventory mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Supplier Assessment mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Cloud-Nutzung durch einzelne Funktionen wird nicht pauschal durch ein Selbstbadge datenschutzkonform. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.iso.org/standard/76559.html, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 25. ISO 31000:2018 Risikomanagement

**Referenz:** https://www.iso.org/standard/65694.html

**Instrumenttyp:** NORM; **Zustaendig:** ISO

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

ISO 31000:2018 Risikomanagement ist eine technische beziehungsweise Management-Norm; nicht jede Norm ist selbst eigenstaendig zertifizierbar. Zuständige Quelle beziehungsweise Scheme-Halter: ISO. Im HCOS-System lautet die notwendige Vorfrage: Allgemeines Management von Risiken und Chancen ohne spezialisiertes Zertifizierungsversprechen. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Risikokontext wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Identifizierung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Analyse wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Bewertung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Behandlung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Monitoring wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Risk Method mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Risk Register mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Treatments mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Monitoring Review mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Decision Minutes mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

ISO 31000 ist ein Leitfaden; es besteht keine klassische ISO-Zertifizierung nach dieser Norm. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.iso.org/standard/65694.html, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 26. NIST Cybersecurity Framework 2.0

**Referenz:** https://www.nist.gov/cyberframework

**Instrumenttyp:** FRAMEWORK; **Zustaendig:** NIST / USA

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

NIST Cybersecurity Framework 2.0 ist ein Leit- und Kontrollrahmen; Alignment ist keine automatisch erteilte Zertifizierung. Zuständige Quelle beziehungsweise Scheme-Halter: NIST / USA. Im HCOS-System lautet die notwendige Vorfrage: Cybersicherheits-Governance und Funktionsmapping für Organisationen. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Govern wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Identify wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Protect wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Detect wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Respond wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Recover wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. CSF Profile mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Gap Analysis mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Risk Register mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Control Trace mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. KPIs mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

NIST CSF Alignment ist eine interne Methodenaussage, kein NIST-Zertifikat. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.nist.gov/cyberframework, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 27. NIST SSDF SP 800-218

**Referenz:** https://csrc.nist.gov/pubs/sp/800/218/final

**Instrumenttyp:** FRAMEWORK; **Zustaendig:** NIST / USA

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

NIST SSDF SP 800-218 ist ein Leit- und Kontrollrahmen; Alignment ist keine automatisch erteilte Zertifizierung. Zuständige Quelle beziehungsweise Scheme-Halter: NIST / USA. Im HCOS-System lautet die notwendige Vorfrage: Sicherer Softwareentwicklungsprozess und Lieferkettenkontrolle. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Prepare Organization wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Protect Software wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Produce Well-Secured Software wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Respond to Vulnerabilities wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Secure SDLC mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Build Provenance mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Training mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Code Review mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Vulnerability Response mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Evidence mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Kein offizieller NIST-SSDF-Zertifikatsstatus durch selbst erstellten Bericht. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://csrc.nist.gov/pubs/sp/800/218/final, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 28. NIST SP 800-53 Rev. 5

**Referenz:** https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final

**Instrumenttyp:** FRAMEWORK; **Zustaendig:** NIST / USA

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

NIST SP 800-53 Rev. 5 ist ein Leit- und Kontrollrahmen; Alignment ist keine automatisch erteilte Zertifizierung. Zuständige Quelle beziehungsweise Scheme-Halter: NIST / USA. Im HCOS-System lautet die notwendige Vorfrage: Sicherheits- und Datenschutz-Control-Katalog für anspruchsvolle Systeme. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Access Control wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Audit wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Configuration wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Incident Response wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. System Integrity wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Privacy Controls wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. System Security Plan mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Control Assessment mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. POA&M mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Risk Evidence mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Independent Test mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Kontrollmapping ist keine staatliche NIST-Autorisierung oder Betriebsfreigabe. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://csrc.nist.gov/pubs/sp/800/53/r5/upd1/final, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 29. OWASP ASVS 5.0.0

**Referenz:** https://asvs.owasp.org/

**Instrumenttyp:** FRAMEWORK; **Zustaendig:** OWASP Foundation

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

OWASP ASVS 5.0.0 ist ein Leit- und Kontrollrahmen; Alignment ist keine automatisch erteilte Zertifizierung. Zuständige Quelle beziehungsweise Scheme-Halter: OWASP Foundation. Im HCOS-System lautet die notwendige Vorfrage: Technische Sicherheitsanforderungen für Webanwendungen und Webservices. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Authentication wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Session wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Access Control wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Input Validation wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. API Security wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Data Protection wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. ASVS Matrix mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. PenTest Results mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Source Review mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Negative API Tests mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Defect Evidence mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

OWASP ASVS 5.0 hat Referenzanforderungen; eine eigene Software kann Alignment darstellen, aber kein erfundenes OWASP-Zertifikat. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://asvs.owasp.org/, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 30. OWASP SAMM

**Referenz:** https://owaspsamm.org/

**Instrumenttyp:** FRAMEWORK; **Zustaendig:** OWASP Foundation

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

OWASP SAMM ist ein Leit- und Kontrollrahmen; Alignment ist keine automatisch erteilte Zertifizierung. Zuständige Quelle beziehungsweise Scheme-Halter: OWASP Foundation. Im HCOS-System lautet die notwendige Vorfrage: Reifegrad sicherer Softwareentwicklung mit wiederholbarer Assessment-Struktur. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Governance wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Design wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Implementation wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Verification wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Operations wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. SAMM Assessment mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Improvement Backlog mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Maturity Profile mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Sprint Evidence mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Review mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Ein SAMM-Score ist eine Bewertungsgröße, nicht automatisch eine Zertifizierung. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://owaspsamm.org/, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 31. CIS Controls v8.1

**Referenz:** https://www.cisecurity.org/controls/v8-1

**Instrumenttyp:** FRAMEWORK; **Zustaendig:** Center for Internet Security

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

CIS Controls v8.1 ist ein Leit- und Kontrollrahmen; Alignment ist keine automatisch erteilte Zertifizierung. Zuständige Quelle beziehungsweise Scheme-Halter: Center for Internet Security. Im HCOS-System lautet die notwendige Vorfrage: Priorisierte technische und organisatorische Cybersicherheitsmaßnahmen. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Asset Control wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Data Protection wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Secure Configuration wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Vulnerability Management wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Incident Response wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. PenTest wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Control-to-Safeguard Matrix mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Asset Inventory mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Scan mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Response Exercise mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. KPI mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

CIS Controls Implementierung und CIS-Akkreditierung sind unterschiedliche Dinge; kein eigenes offizielles Label erfinden. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.cisecurity.org/controls/v8-1, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 32. BSI IT-Grundschutz

**Referenz:** https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html

**Instrumenttyp:** FRAMEWORK; **Zustaendig:** Bundesamt für Sicherheit in der Informationstechnik

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

BSI IT-Grundschutz ist ein Leit- und Kontrollrahmen; Alignment ist keine automatisch erteilte Zertifizierung. Zuständige Quelle beziehungsweise Scheme-Halter: Bundesamt für Sicherheit in der Informationstechnik. Im HCOS-System lautet die notwendige Vorfrage: Deutsche Informationssicherheit und gegebenenfalls BSI-Zertifizierungsweg. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Strukturanalyse wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Schutzbedarf wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Modellierung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Basisabsicherung wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Sicherheitscheck wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Revision wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Grundschutz-Konzept mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. IT-Verbund mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. Maßnahmenliste mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Dokumentation mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. Audit-Report mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Ein BSI-Zertifikat benötigt die zuständige externe Prüfung und erteilte Zertifizierung; selbst generiertes BSI-Siegel verboten. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.bsi.bund.de/DE/Themen/Unternehmen-und-Organisationen/Standards-und-Zertifizierung/IT-Grundschutz/it-grundschutz_node.html, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 33. PCI DSS 4.0.1

**Referenz:** https://www.pcisecuritystandards.org/document_library/

**Instrumenttyp:** SCHEME; **Zustaendig:** PCI Security Standards Council

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

PCI DSS 4.0.1 ist ein formalisiertes Assessment- oder Validierungssystem mit eigenen Regeln fuer Aussteller und Marken. Zuständige Quelle beziehungsweise Scheme-Halter: PCI Security Standards Council. Im HCOS-System lautet die notwendige Vorfrage: Karteninhaberdatenumgebung nach PCI-Scope und Rollen. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. Scope Minimization wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Network Segmentation wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Encryption wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Access wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Logging wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Penetration Tests wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. Cardholder Data Flow mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. SAQ/ROC je Typ mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. AOC mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. ASV Reports mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E05. PenTest mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E06. Policies mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Validierungsart und Attestation folgen PCI-Vorgaben; interne PASS-Karte ist keine PCI-AOC. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://www.pcisecuritystandards.org/document_library/, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.


---

## 34. TISAX / VDA ISA

**Referenz:** https://portal.enx.com/en-us/TISAX/ISA/

**Instrumenttyp:** SCHEME; **Zustaendig:** ENX Association / zugelassener Prüfdienstleister

### Instrumenttyp, Anwendungsbereich und rechtliche Grenze

TISAX / VDA ISA ist ein formalisiertes Assessment- oder Validierungssystem mit eigenen Regeln fuer Aussteller und Marken. Zuständige Quelle beziehungsweise Scheme-Halter: ENX Association / zugelassener Prüfdienstleister. Im HCOS-System lautet die notwendige Vorfrage: Information Security Assessment für Automotive-Lieferketten gemäß Teilnehmeranforderungen. Die Rechts- oder Normenentscheidung wird niemals allein aus einem Domain-Suffix, einer Bibliothek oder einem groen Badge abgeleitet. Anwendbarkeit, verpflichtende Ausgabefassung und Berichtszeitpunkt sind einzeln zu dokumentieren.

### Anwendbarkeits- und Gap-Assessment

Der Prozess startet mit Rollenklassifikation (Anbieter, Nutzer, Verantwortlicher, Auftragsverarbeiter, beaufsichtigtes Institut oder Hersteller). Danach folgen Aktivitaet, Produkte, Datenkategorien und Rechtsraum. Ein GapRecord traegt requirement_id, applicability_reason, control_owner, severity, due_date, evidence_uri und review_decision. Vorhandene Module M01–M13 werden als Moeglichkeiten, nicht als automatische Erfuellung gemappt. Nicht anwendbare Regeln brauchen ebenfalls begruendete Review-Akten.

### Pruefkriterien 01 bis 06 als konkrete Kontrollen

C01. VDA ISA wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C02. Scope wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C03. Maturity wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C04. Assessment Objectives wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C05. Findings wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt. C06. Improvement Plan wird als eigene Kontrollanforderung mit Verantwortlichem und pruefbarem Sollwert gefuehrt.

### Automationsstrategie und unabhängiger Harness Loop

Ein normbezogener Harness Loop laedt die autorisierte Version der Anforderungen, markiert nur die fuer das konkrete Produkt einschlaegigen Kriterien und weist jedem Kontrollpunkt einen Testoracle zu. DISCOVER sammelt Quellen; PLAN erstellt Mapping; COLLECT liest freigegebene Evidence; VERIFY prueft Hash, Frische und Aussagekraft; REVIEW verlangt eine zweite Rolle; PUBLISH erzeugt intern nur einen Nachweisstatus. Fehlende Belege fuehren zu GAP_OPEN. Eine externe Zertifizierung oder Zulassung darf die Schleife nicht selbst ausstellen.

### Nachweisakte: zu erfassende Artefakte

E01. VDA ISA Self-assessment mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E02. Assessment Report mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E03. ENX Result Status mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren. E04. Corrective Actions mit Hash, Ausgabe, Zeit, Scope und Reviewerreferenz archivieren.

### Automatische Abnahmebedingungen und Negativtests

Eine interne Entscheidung darf PASS_INTERNAL nur erhalten, wenn alle anwendbaren Pflichtkriterien belegt, kritische Findings geschlossen und die zugehoerigen Tests reproduzierbar sind. Negativtests pruefen: manipulierte Evidence, abgelaufene Ausgabefassung, falsch deklarierter Geltungsbereich, nicht autorisierter Reviewer und eine nachtraeglich geaenderte Binary. Jeder dieser Faelle fuehrt zu BLOCKED oder REVIEW_REQUIRED. Der regelbasierte Prozess dokumentiert auch bewusst offene Ausnahmen statt diese zu verstecken.

### Abzeichen, Logo und Bannervorgaben

Nur ENX-Prozess und berechtigte Assessment-Provider können gültige TISAX-Ergebnisse erzeugen. Das Konzept liefert deshalb ein eigenes HCOS-Evidenzzeichen mit explizitem Text INTERN GEPRUEFT – KEINE EXTERNE ZERTIFIZIERUNG. Ein offizielles Logo oder eine akkreditierte Zertifizierungsmarke erscheint ausschliesslich, wenn Nutzungsrechte, Zertifikatsnummer, Aussteller, Scope, Ablaufdatum und Verifikations-URL nachweisbar sind. Keine EU-, ISO-, BSI-, ENX- oder Aufsichtsmarke wird nachgezeichnet oder als erteilt simuliert.

### Veröffentlichung und kontinuierliches Monitoring

Die Normseite zeigt stets die offizielle Referenz-URL https://portal.enx.com/en-us/TISAX/ISA/, zuletzt gepruefte Fassung, Aktualisierungsmeldungen, interne Evidence und offene Defizite. Ein Widerruf oder eine neue Gesetzesfassung setzt betroffene Assertions auf REVIEW_REQUIRED. Bei Ablauf einer fremden Zertifizierung wird deren Anzeige automatisch entzogen; dies ist ein Darstellungs- und Workflowprozess, keine Kompetenz zur amtlichen Zertifikatserteilung.

### Definition of Done für die automatische Prüfleitung

Fertig bedeutet: dokumentierte Anwendbarkeit, sechs kontrollierte Kriterien oder begruendete Nichtanwendbarkeit, sechs referenzierte Artefaktklassen, unabhängige Review-Identitaet, aktueller Versionsstand und kein ungerechtfertigtes offizielles Abzeichen. Das resultierende AuditDossier besitzt eindeutigen Record-ID, signierten Hash, nachvollziehbare Quellenkette, Gueltigkeitszeitraum und einen revisionssicheren Fehler-/Widerspruchspfad.

