# HCOS FORINA TITAN · Band B

## Entwicklungssprache, Abkuerzungen und Integrationsvertraege

34 ausgearbeitete Fachbereiche mit ueber 280 Abkuerzungen, Mustern, Strategien und Tests

**Stand:** 06.11.2026; **Code-Referenz:** https://github.com/EU-UNION-AI-PACT/HCOS-FORINA-TITAN-ENGINE/commit/4cd1db2066237798717d201fc4a0a46759664a85

**Rechts-/Markenhinweis:** Interne Audit-Pruefung ist nicht gleich amtliche Zulassung oder externe Zertifizierung. Das Markenrecht der jeweiligen Organisation ist gesondert zu beachten. Keine personenbezogenen Geheimnisse oder Produktionsdaten.


---

## 01. Requirements Engineering

**Abkuerzungen:** REQ = Requirement, NFR = Nonfunctional Requirement, SLO = Service Level Objective, SLI = Service Level Indicator, DoD = Definition of Done, AC = Acceptance Criteria, RACI = Responsible Accountable Consulted Informed, ADR = Architecture Decision Record, RFC = Request for Comments

### Begriffe 1 bis 4: Bedeutung im Produkt

REQ steht fuer Requirement; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. NFR steht fuer Nonfunctional Requirement; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SLO steht fuer Service Level Objective; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SLI steht fuer Service Level Indicator; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

DoD bezeichnet Definition of Done; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. AC bezeichnet Acceptance Criteria; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. RACI bezeichnet Responsible Accountable Consulted Informed; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ADR bezeichnet Architecture Decision Record; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. RFC bezeichnet Request for Comments; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Abnahmekriterien statt Wunschlisten Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Requirements Engineering mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Zielbild als versionierte Entscheidung mit nachvollziehbaren Akzeptanztests Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe REQ, NFR, SLO, SLI, DoD als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer REQ bis RFC eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter REQ; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade AC, RACI, ADR, RFC duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 02. Information Architecture

**Abkuerzungen:** IA = Information Architecture, JTBD = Jobs To Be Done, Sitemap = Navigation Map, Taxonomy = Klassifikation, Ontology = Begriffsmodell, Facet = Suchfiltermerkmal, Breadcrumb = Navigationspfad, ContentType = Inhaltsmodell, CardSort = Karten-Sortierung

### Begriffe 1 bis 4: Bedeutung im Produkt

IA steht fuer Information Architecture; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. JTBD steht fuer Jobs To Be Done; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. Sitemap steht fuer Navigation Map; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. Taxonomy steht fuer Klassifikation; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

Ontology bezeichnet Begriffsmodell; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Facet bezeichnet Suchfiltermerkmal; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Breadcrumb bezeichnet Navigationspfad; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ContentType bezeichnet Inhaltsmodell; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. CardSort bezeichnet Karten-Sortierung; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Nutzeraufgaben über Organisationsmodule stellen Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Information Architecture mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Suche nach Auditbelegen statt Navigation nach Python-Datei Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe IA, JTBD, Sitemap, Taxonomy, Ontology als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer IA bis CardSort eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter IA; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade Facet, Breadcrumb, ContentType, CardSort duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 03. Experience Design

**Abkuerzungen:** XD = Experience Design, UX = User Experience, UI = User Interface, CX = Customer Experience, HCD = Human-Centered Design, UCD = User-Centered Design, HE = Heuristic Evaluation, SUS = System Usability Scale, UXR = User Experience Research

### Begriffe 1 bis 4: Bedeutung im Produkt

XD steht fuer Experience Design; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. UX steht fuer User Experience; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. UI steht fuer User Interface; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. CX steht fuer Customer Experience; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

HCD bezeichnet Human-Centered Design; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. UCD bezeichnet User-Centered Design; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. HE bezeichnet Heuristic Evaluation; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SUS bezeichnet System Usability Scale; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. UXR bezeichnet User Experience Research; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Konsequenzen vor attraktiven Animationen sichtbar machen Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Experience Design mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Read-only-Analyse mit sicherem Zustand und verständlicher Vorschau Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe XD, UX, UI, CX, HCD als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer XD bis UXR eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter XD; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade UCD, HE, SUS, UXR duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 04. Design Systems

**Abkuerzungen:** DT = Design Token, DS = Design System, A11Y = Accessibility, ARIA = Accessible Rich Internet Applications, RTL = Right-to-Left, WCAG = Web Content Accessibility Guidelines, L10N = Localization, I18N = Internationalization, Figma = Design Collaboration Tool

### Begriffe 1 bis 4: Bedeutung im Produkt

DT steht fuer Design Token; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. DS steht fuer Design System; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. A11Y steht fuer Accessibility; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. ARIA steht fuer Accessible Rich Internet Applications; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

RTL bezeichnet Right-to-Left; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. WCAG bezeichnet Web Content Accessibility Guidelines; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. L10N bezeichnet Localization; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. I18N bezeichnet Internationalization; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Figma bezeichnet Design Collaboration Tool; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Barrierefreie wiederverwendbare Komponenten und Tokens Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Design Systems mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Statuskarte mit Fehler- und Unbekanntzustand Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe DT, DS, A11Y, ARIA, RTL als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer DT bis Figma eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter DT; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade WCAG, L10N, I18N, Figma duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 05. Frontend Architecture

**Abkuerzungen:** SPA = Single Page Application, SSR = Server-Side Rendering, SSG = Static Site Generation, CSP = Content Security Policy, DOM = Document Object Model, XSS = Cross-Site Scripting, CSRF = Cross-Site Request Forgery, SRI = Subresource Integrity, CORS = Cross-Origin Resource Sharing

### Begriffe 1 bis 4: Bedeutung im Produkt

SPA steht fuer Single Page Application; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SSR steht fuer Server-Side Rendering; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SSG steht fuer Static Site Generation; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. CSP steht fuer Content Security Policy; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

DOM bezeichnet Document Object Model; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. XSS bezeichnet Cross-Site Scripting; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. CSRF bezeichnet Cross-Site Request Forgery; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SRI bezeichnet Subresource Integrity; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. CORS bezeichnet Cross-Origin Resource Sharing; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Sichere Rendering-Grenzen für untrusted CSV Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Frontend Architecture mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Repository-Karten ohne riskante href-Schemas Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe SPA, SSR, SSG, CSP, DOM als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer SPA bis CORS eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter SPA; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade XSS, CSRF, SRI, CORS duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 06. Backend Services

**Abkuerzungen:** REST = Representational State Transfer, RPC = Remote Procedure Call, DTO = Data Transfer Object, BFF = Backend for Frontend, CQRS = Command Query Responsibility Segregation, DDD = Domain-Driven Design, ORM = Object Relational Mapping, CRUD = Create Read Update Delete, HTTP = Hypertext Transfer Protocol

### Begriffe 1 bis 4: Bedeutung im Produkt

REST steht fuer Representational State Transfer; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. RPC steht fuer Remote Procedure Call; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. DTO steht fuer Data Transfer Object; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. BFF steht fuer Backend for Frontend; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

CQRS bezeichnet Command Query Responsibility Segregation; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. DDD bezeichnet Domain-Driven Design; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ORM bezeichnet Object Relational Mapping; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. CRUD bezeichnet Create Read Update Delete; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. HTTP bezeichnet Hypertext Transfer Protocol; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Trennung von Read Models und Befehlsausführung Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Backend Services mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Sovereign-API liefert belegte Statuswerte ohne Seiteneffekte Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe REST, RPC, DTO, BFF, CQRS als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer REST bis HTTP eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter REST; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade DDD, ORM, CRUD, HTTP duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 07. Data Contracts

**Abkuerzungen:** JSON = JavaScript Object Notation, JSONS = JSON Schema, YAML = YAML Ain't Markup Language, CSV = Comma-Separated Values, XML = Extensible Markup Language, XSD = XML Schema Definition, Protobuf = Protocol Buffers, Avro = Apache Avro, IDL = Interface Definition Language

### Begriffe 1 bis 4: Bedeutung im Produkt

JSON steht fuer JavaScript Object Notation; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. JSONS steht fuer JSON Schema; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. YAML steht fuer YAML Ain't Markup Language; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. CSV steht fuer Comma-Separated Values; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

XML bezeichnet Extensible Markup Language; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. XSD bezeichnet XML Schema Definition; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Protobuf bezeichnet Protocol Buffers; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Avro bezeichnet Apache Avro; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. IDL bezeichnet Interface Definition Language; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Versionierte JSON-Nachrichten und Validatoren Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Data Contracts mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Audit-Event bleibt bei UI-Update rückwärtskompatibel Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe JSON, JSONS, YAML, CSV, XML als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer JSON bis IDL eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter JSON; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade XSD, Protobuf, Avro, IDL duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 08. API Governance

**Abkuerzungen:** OpenAPI = OpenAPI Specification, AsyncAPI = AsyncAPI Specification, SDK = Software Development Kit, API = Application Programming Interface, SemVer = Semantic Versioning, OAuth = Open Authorization, OIDC = OpenID Connect, JWT = JSON Web Token, IdemKey = Idempotency Key

### Begriffe 1 bis 4: Bedeutung im Produkt

OpenAPI steht fuer OpenAPI Specification; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. AsyncAPI steht fuer AsyncAPI Specification; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SDK steht fuer Software Development Kit; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. API steht fuer Application Programming Interface; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

SemVer bezeichnet Semantic Versioning; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. OAuth bezeichnet Open Authorization; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. OIDC bezeichnet OpenID Connect; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. JWT bezeichnet JSON Web Token; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. IdemKey bezeichnet Idempotency Key; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Explizite Connector-Autorisierung ohne implizite Rechte Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog API Governance mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Read-only Banking Vertrag und stufenweise Versionierung Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe OpenAPI, AsyncAPI, SDK, API, SemVer als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer OpenAPI bis IdemKey eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter OpenAPI; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade OAuth, OIDC, JWT, IdemKey duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 09. Event-Driven Design

**Abkuerzungen:** EDA = Event-Driven Architecture, DLQ = Dead Letter Queue, CDC = Change Data Capture, Outbox = Transactional Outbox, Saga = Distributed Transaction Coordination, ETag = Entity Tag, TTL = Time To Live, ACK = Acknowledgment, NACK = Negative Acknowledgment

### Begriffe 1 bis 4: Bedeutung im Produkt

EDA steht fuer Event-Driven Architecture; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. DLQ steht fuer Dead Letter Queue; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. CDC steht fuer Change Data Capture; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. Outbox steht fuer Transactional Outbox; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

Saga bezeichnet Distributed Transaction Coordination; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ETag bezeichnet Entity Tag; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. TTL bezeichnet Time To Live; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ACK bezeichnet Acknowledgment; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. NACK bezeichnet Negative Acknowledgment; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Doppelte Events führen nicht zu doppelten Aktionen Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Event-Driven Design mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Signiertes Gate-Ergebnis über eine Event-Schnittstelle Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe EDA, DLQ, CDC, Outbox, Saga als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer EDA bis NACK eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter EDA; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade ETag, TTL, ACK, NACK duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 10. Identity & Access

**Abkuerzungen:** IAM = Identity and Access Management, RBAC = Role-Based Access Control, ABAC = Attribute-Based Access Control, PDP = Policy Decision Point, PEP = Policy Enforcement Point, MFA = Multi-Factor Authentication, TOTP = Time-Based One-Time Password, SSO = Single Sign-On, SCIM = System for Cross-domain Identity Management

### Begriffe 1 bis 4: Bedeutung im Produkt

IAM steht fuer Identity and Access Management; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. RBAC steht fuer Role-Based Access Control; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. ABAC steht fuer Attribute-Based Access Control; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. PDP steht fuer Policy Decision Point; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

PEP bezeichnet Policy Enforcement Point; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. MFA bezeichnet Multi-Factor Authentication; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. TOTP bezeichnet Time-Based One-Time Password; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SSO bezeichnet Single Sign-On; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SCIM bezeichnet System for Cross-domain Identity Management; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Rechte auf Session, Zweck und Ressource begrenzen Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Identity & Access mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Einwilligung wird bei Sperrung überall widerrufen Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe IAM, RBAC, ABAC, PDP, PEP als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer IAM bis SCIM eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter IAM; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade MFA, TOTP, SSO, SCIM duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 11. Secrets & Cryptography

**Abkuerzungen:** KMS = Key Management Service, HSM = Hardware Security Module, PKI = Public Key Infrastructure, KDF = Key Derivation Function, AEAD = Authenticated Encryption with Associated Data, AES = Advanced Encryption Standard, Ed25519 = Edwards-curve Digital Signature, SHA-256 = Secure Hash Algorithm 256, JWK = JSON Web Key

### Begriffe 1 bis 4: Bedeutung im Produkt

KMS steht fuer Key Management Service; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. HSM steht fuer Hardware Security Module; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. PKI steht fuer Public Key Infrastructure; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. KDF steht fuer Key Derivation Function; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

AEAD bezeichnet Authenticated Encryption with Associated Data; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. AES bezeichnet Advanced Encryption Standard; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Ed25519 bezeichnet Edwards-curve Digital Signature; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SHA-256 bezeichnet Secure Hash Algorithm 256; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. JWK bezeichnet JSON Web Key; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Schlüssel nicht in Chat, ZIP oder Telemetrie exportieren Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Secrets & Cryptography mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Trennung von Signier- und Authentifikationsschlüsseln Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe KMS, HSM, PKI, KDF, AEAD als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer KMS bis JWK eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter KMS; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade AES, Ed25519, SHA-256, JWK duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 12. Software Supply Chain

**Abkuerzungen:** SBOM = Software Bill of Materials, SLSA = Supply-chain Levels for Software Artifacts, SCA = Software Composition Analysis, SAST = Static Application Security Testing, DAST = Dynamic Application Security Testing, IAST = Interactive Application Security Testing, VEX = Vulnerability Exploitability eXchange, CVE = Common Vulnerabilities and Exposures, CWE = Common Weakness Enumeration

### Begriffe 1 bis 4: Bedeutung im Produkt

SBOM steht fuer Software Bill of Materials; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SLSA steht fuer Supply-chain Levels for Software Artifacts; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SCA steht fuer Software Composition Analysis; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SAST steht fuer Static Application Security Testing; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

DAST bezeichnet Dynamic Application Security Testing; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. IAST bezeichnet Interactive Application Security Testing; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. VEX bezeichnet Vulnerability Exploitability eXchange; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. CVE bezeichnet Common Vulnerabilities and Exposures; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. CWE bezeichnet Common Weakness Enumeration; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Quellcode- und Binary-Provenienz nachweisen Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Software Supply Chain mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

AppImage-Hash, SBOM und Repo-SHA nachvollziehbar Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe SBOM, SLSA, SCA, SAST, DAST als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer SBOM bis CWE eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter SBOM; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade IAST, VEX, CVE, CWE duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 13. Testing Strategy

**Abkuerzungen:** UT = Unit Test, IT = Integration Test, E2E = End-to-End Test, UAT = User Acceptance Test, PBT = Property-Based Testing, Fuzz = Fuzz Testing, MutTest = Mutation Testing, Snapshot = Snapshot Testing, TDD = Test-Driven Development

### Begriffe 1 bis 4: Bedeutung im Produkt

UT steht fuer Unit Test; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. IT steht fuer Integration Test; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. E2E steht fuer End-to-End Test; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. UAT steht fuer User Acceptance Test; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

PBT bezeichnet Property-Based Testing; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Fuzz bezeichnet Fuzz Testing; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. MutTest bezeichnet Mutation Testing; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Snapshot bezeichnet Snapshot Testing; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. TDD bezeichnet Test-Driven Development; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Eigenschaften und Risiken testen statt nur Demo-Erfolg Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Testing Strategy mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Manipulierter SHA oder falsche Banking-Permission muss scheitern Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe UT, IT, E2E, UAT, PBT als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer UT bis TDD eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter UT; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade Fuzz, MutTest, Snapshot, TDD duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 14. Continuous Delivery

**Abkuerzungen:** CI = Continuous Integration, CD = Continuous Delivery, GitOps = Git Operations Model, IaC = Infrastructure as Code, CICD = CI/CD Pipeline, Canary = Incremental Rollout, BlueGreen = Blue-Green Deployment, Rollback = Release Reversal, RC = Release Candidate

### Begriffe 1 bis 4: Bedeutung im Produkt

CI steht fuer Continuous Integration; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. CD steht fuer Continuous Delivery; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. GitOps steht fuer Git Operations Model; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. IaC steht fuer Infrastructure as Code; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

CICD bezeichnet CI/CD Pipeline; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Canary bezeichnet Incremental Rollout; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. BlueGreen bezeichnet Blue-Green Deployment; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Rollback bezeichnet Release Reversal; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. RC bezeichnet Release Candidate; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Releases ohne stilles Rechtewachstum freigeben Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Continuous Delivery mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Signierte Stufen Dev bis Release mit Rollback Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe CI, CD, GitOps, IaC, CICD als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer CI bis RC eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter CI; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade Canary, BlueGreen, Rollback, RC duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 15. Runtime Isolation

**Abkuerzungen:** AirGap = Physically or Technically Isolated Network, Egress = Outbound Network Traffic, Seccomp = Linux Syscall Filtering, MAC = Mandatory Access Control, DAC = Discretionary Access Control, LSM = Linux Security Module, UID = User Identifier, FUSE = Filesystem in Userspace, Rootless = Without Elevated Privileges

### Begriffe 1 bis 4: Bedeutung im Produkt

AirGap steht fuer Physically or Technically Isolated Network; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. Egress steht fuer Outbound Network Traffic; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. Seccomp steht fuer Linux Syscall Filtering; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. MAC steht fuer Mandatory Access Control; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

DAC bezeichnet Discretionary Access Control; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. LSM bezeichnet Linux Security Module; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. UID bezeichnet User Identifier; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. FUSE bezeichnet Filesystem in Userspace; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Rootless bezeichnet Without Elevated Privileges; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Air-Gap nur behaupten wenn unabhängig erzwungen Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Runtime Isolation mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Launcher lehnt fehlendes No-Egress-Evidence ab Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe AirGap, Egress, Seccomp, MAC, DAC als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer AirGap bis Rootless eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter AirGap; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade LSM, UID, FUSE, Rootless duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 16. Resilience and Backup

**Abkuerzungen:** BCP = Business Continuity Plan, DRP = Disaster Recovery Plan, RTO = Recovery Time Objective, RPO = Recovery Point Objective, MTTR = Mean Time To Recovery, MTBF = Mean Time Between Failures, HA = High Availability, PITR = Point-in-Time Recovery, 3-2-1 = Backup Copy Rule

### Begriffe 1 bis 4: Bedeutung im Produkt

BCP steht fuer Business Continuity Plan; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. DRP steht fuer Disaster Recovery Plan; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. RTO steht fuer Recovery Time Objective; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. RPO steht fuer Recovery Point Objective; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

MTTR bezeichnet Mean Time To Recovery; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. MTBF bezeichnet Mean Time Between Failures; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. HA bezeichnet High Availability; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. PITR bezeichnet Point-in-Time Recovery; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. 3-2-1 bezeichnet Backup Copy Rule; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Wiederherstellung aller kritischen Dateien nachvollziehen Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Resilience and Backup mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Borg-Archiv auf synthetischen Daten wiederherstellen Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe BCP, DRP, RTO, RPO, MTTR als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer BCP bis 3-2-1 eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter BCP; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade MTBF, HA, PITR, 3-2-1 duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 17. Observability

**Abkuerzungen:** OTel = OpenTelemetry, SIEM = Security Information and Event Management, SOAR = Security Orchestration Automation and Response, APM = Application Performance Monitoring, RUM = Real User Monitoring, P95 = 95th Percentile, RED = Rate Errors Duration, USE = Utilization Saturation Errors, SRE = Site Reliability Engineering

### Begriffe 1 bis 4: Bedeutung im Produkt

OTel steht fuer OpenTelemetry; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SIEM steht fuer Security Information and Event Management; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SOAR steht fuer Security Orchestration Automation and Response; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. APM steht fuer Application Performance Monitoring; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

RUM bezeichnet Real User Monitoring; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. P95 bezeichnet 95th Percentile; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. RED bezeichnet Rate Errors Duration; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. USE bezeichnet Utilization Saturation Errors; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SRE bezeichnet Site Reliability Engineering; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Keine personenbezogenen Zahlungsdaten in Logs Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Observability mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Request-Latenz und Gate-Fails anonym korrelieren Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe OTel, SIEM, SOAR, APM, RUM als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer OTel bis SRE eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter OTel; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade P95, RED, USE, SRE duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 18. Threat Modeling

**Abkuerzungen:** STRIDE = Spoofing Tampering Repudiation Information disclosure Denial of service Elevation of privilege, DREAD = Damage Reproducibility Exploitability Affected users Discoverability, ATTACK = MITRE ATT&CK, TTP = Tactics Techniques Procedures, KEV = Known Exploited Vulnerabilities, IOC = Indicator of Compromise, TLP = Traffic Light Protocol, STIX = Structured Threat Information Expression, TAXII = Trusted Automated Exchange of Intelligence Information

### Begriffe 1 bis 4: Bedeutung im Produkt

STRIDE steht fuer Spoofing Tampering Repudiation Information disclosure Denial of service Elevation of privilege; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. DREAD steht fuer Damage Reproducibility Exploitability Affected users Discoverability; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. ATTACK steht fuer MITRE ATT&CK; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. TTP steht fuer Tactics Techniques Procedures; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

KEV bezeichnet Known Exploited Vulnerabilities; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. IOC bezeichnet Indicator of Compromise; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. TLP bezeichnet Traffic Light Protocol; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. STIX bezeichnet Structured Threat Information Expression; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. TAXII bezeichnet Trusted Automated Exchange of Intelligence Information; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Angriffspfade als Tests statt nur Text Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Threat Modeling mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Agent-Prompt darf keine Tools freischalten Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe STRIDE, DREAD, ATTACK, TTP, KEV als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer STRIDE bis TAXII eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter STRIDE; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade IOC, TLP, STIX, TAXII duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 19. Privacy Engineering

**Abkuerzungen:** PII = Personally Identifiable Information, DPIA = Data Protection Impact Assessment, ROPA = Record of Processing Activities, DSAR = Data Subject Access Request, PET = Privacy Enhancing Technology, DLP = Data Loss Prevention, Pseudonymization = Reversible Identifier Separation, Anonymization = Non-Reidentifiable Processing, TOM = Technical and Organizational Measures

### Begriffe 1 bis 4: Bedeutung im Produkt

PII steht fuer Personally Identifiable Information; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. DPIA steht fuer Data Protection Impact Assessment; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. ROPA steht fuer Record of Processing Activities; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. DSAR steht fuer Data Subject Access Request; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

PET bezeichnet Privacy Enhancing Technology; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. DLP bezeichnet Data Loss Prevention; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Pseudonymization bezeichnet Reversible Identifier Separation; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Anonymization bezeichnet Non-Reidentifiable Processing; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. TOM bezeichnet Technical and Organizational Measures; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Datenzwecke und Retention vor Implementierung Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Privacy Engineering mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Löschauftrag propagiert in Read Models und Backups Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe PII, DPIA, ROPA, DSAR, PET als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer PII bis TOM eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter PII; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade DLP, Pseudonymization, Anonymization, TOM duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 20. GRC and Compliance

**Abkuerzungen:** GRC = Governance Risk Compliance, ISMS = Information Security Management System, AIMS = AI Management System, PIMS = Privacy Information Management System, BCMS = Business Continuity Management System, SoA = Statement of Applicability, CAPA = Corrective and Preventive Action, KRI = Key Risk Indicator, KPI = Key Performance Indicator

### Begriffe 1 bis 4: Bedeutung im Produkt

GRC steht fuer Governance Risk Compliance; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. ISMS steht fuer Information Security Management System; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. AIMS steht fuer AI Management System; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. PIMS steht fuer Privacy Information Management System; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

BCMS bezeichnet Business Continuity Management System; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SoA bezeichnet Statement of Applicability; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. CAPA bezeichnet Corrective and Preventive Action; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. KRI bezeichnet Key Risk Indicator; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. KPI bezeichnet Key Performance Indicator; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Normanforderung direkt mit Test und Beweis verbinden Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog GRC and Compliance mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

M07 Domain Trust erfordert autorisierte Herkunftsnachweise Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe GRC, ISMS, AIMS, PIMS, BCMS als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer GRC bis KPI eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter GRC; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade SoA, CAPA, KRI, KPI duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 21. Evidence Engineering

**Abkuerzungen:** Merkle = Merkle Tree, HashChain = Chained Digest Log, Attest = Signed Attestation, Provenance = Artifact Origin Proof, WORM = Write Once Read Many, Timestamp = Trusted Time Evidence, OCSP = Online Certificate Status Protocol, CRL = Certificate Revocation List, ETSI = European Telecommunications Standards Institute

### Begriffe 1 bis 4: Bedeutung im Produkt

Merkle steht fuer Merkle Tree; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. HashChain steht fuer Chained Digest Log; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. Attest steht fuer Signed Attestation; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. Provenance steht fuer Artifact Origin Proof; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

WORM bezeichnet Write Once Read Many; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Timestamp bezeichnet Trusted Time Evidence; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. OCSP bezeichnet Online Certificate Status Protocol; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. CRL bezeichnet Certificate Revocation List; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ETSI bezeichnet European Telecommunications Standards Institute; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Belege unveränderbar und scopegebunden halten Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Evidence Engineering mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Gate PASS verfällt nach geänderter Binary Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe Merkle, HashChain, Attest, Provenance, WORM als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer Merkle bis ETSI eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter Merkle; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade Timestamp, OCSP, CRL, ETSI duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 22. Agents & LLM Integration

**Abkuerzungen:** LLM = Large Language Model, RAG = Retrieval-Augmented Generation, MCP = Model Context Protocol, A2A = Agent-to-Agent Protocol, ReAct = Reasoning and Acting Pattern, RBA = Risk-Based Approval, HITL = Human in the Loop, HCL = Harness Control Loop, ToolGate = External Tool Policy Gate

### Begriffe 1 bis 4: Bedeutung im Produkt

LLM steht fuer Large Language Model; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. RAG steht fuer Retrieval-Augmented Generation; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. MCP steht fuer Model Context Protocol; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. A2A steht fuer Agent-to-Agent Protocol; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

ReAct bezeichnet Reasoning and Acting Pattern; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. RBA bezeichnet Risk-Based Approval; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. HITL bezeichnet Human in the Loop; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. HCL bezeichnet Harness Control Loop; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ToolGate bezeichnet External Tool Policy Gate; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Modellvorschläge und Rechte durch getrennte Ebenen Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Agents & LLM Integration mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Harness Loop mit unabhängigen Testorakeln Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe LLM, RAG, MCP, A2A, ReAct als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer LLM bis ToolGate eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter LLM; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade RBA, HITL, HCL, ToolGate duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 23. Model Evaluation

**Abkuerzungen:** Eval = Model Evaluation, GoldenSet = Curated Reference Dataset, Drift = Model Distribution Shift, ECE = Expected Calibration Error, FPR = False Positive Rate, FNR = False Negative Rate, TPR = True Positive Rate, Confidence = Calibrated Confidence, Oracle = Independent Test Oracle

### Begriffe 1 bis 4: Bedeutung im Produkt

Eval steht fuer Model Evaluation; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. GoldenSet steht fuer Curated Reference Dataset; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. Drift steht fuer Model Distribution Shift; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. ECE steht fuer Expected Calibration Error; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

FPR bezeichnet False Positive Rate; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. FNR bezeichnet False Negative Rate; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. TPR bezeichnet True Positive Rate; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Confidence bezeichnet Calibrated Confidence; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Oracle bezeichnet Independent Test Oracle; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Keine errechnete Modellqualität ohne Benchmark Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Model Evaluation mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

BOBA-Kette reproduzierbar mit Negativfällen messen Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe Eval, GoldenSet, Drift, ECE, FPR als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer Eval bis Oracle eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter Eval; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade FNR, TPR, Confidence, Oracle duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 24. Search and Knowledge

**Abkuerzungen:** IR = Information Retrieval, BM25 = Best Matching 25, ANN = Approximate Nearest Neighbor, RRF = Reciprocal Rank Fusion, KG = Knowledge Graph, RDF = Resource Description Framework, SPARQL = SPARQL Protocol and RDF Query Language, Rerank = Search Result Re-ranking, Citation = Source Reference

### Begriffe 1 bis 4: Bedeutung im Produkt

IR steht fuer Information Retrieval; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. BM25 steht fuer Best Matching 25; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. ANN steht fuer Approximate Nearest Neighbor; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. RRF steht fuer Reciprocal Rank Fusion; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

KG bezeichnet Knowledge Graph; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. RDF bezeichnet Resource Description Framework; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SPARQL bezeichnet SPARQL Protocol and RDF Query Language; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Rerank bezeichnet Search Result Re-ranking; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Citation bezeichnet Source Reference; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Dokumentantwort mit Quelle statt Halluzination Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Search and Knowledge mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Normen-Crosswalk mit markierten Unsicherheiten Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe IR, BM25, ANN, RRF, KG als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer IR bis Citation eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter IR; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade RDF, SPARQL, Rerank, Citation duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 25. Data Storage

**Abkuerzungen:** OLTP = Online Transaction Processing, OLAP = Online Analytical Processing, ACID = Atomicity Consistency Isolation Durability, BASE = Basically Available Soft state Eventual consistency, MVCC = Multi-Version Concurrency Control, WAL = Write-Ahead Log, ETL = Extract Transform Load, ELT = Extract Load Transform, CDC = Change Data Capture

### Begriffe 1 bis 4: Bedeutung im Produkt

OLTP steht fuer Online Transaction Processing; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. OLAP steht fuer Online Analytical Processing; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. ACID steht fuer Atomicity Consistency Isolation Durability; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. BASE steht fuer Basically Available Soft state Eventual consistency; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

MVCC bezeichnet Multi-Version Concurrency Control; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. WAL bezeichnet Write-Ahead Log; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ETL bezeichnet Extract Transform Load; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ELT bezeichnet Extract Load Transform; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. CDC bezeichnet Change Data Capture; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Souveräne lokale Daten und definierte TTL Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Data Storage mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Replikation ausschließlich nach freigegebener Zone Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe OLTP, OLAP, ACID, BASE, MVCC als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer OLTP bis CDC eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter OLTP; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade WAL, ETL, ELT, CDC duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 26. Networking & DNS

**Abkuerzungen:** DNS = Domain Name System, DNSSEC = DNS Security Extensions, TLS = Transport Layer Security, mTLS = Mutual TLS, RDAP = Registration Data Access Protocol, HSTS = HTTP Strict Transport Security, PKIX = Public Key Infrastructure X.509, CT = Certificate Transparency, ACME = Automated Certificate Management Environment

### Begriffe 1 bis 4: Bedeutung im Produkt

DNS steht fuer Domain Name System; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. DNSSEC steht fuer DNS Security Extensions; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. TLS steht fuer Transport Layer Security; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. mTLS steht fuer Mutual TLS; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

RDAP bezeichnet Registration Data Access Protocol; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. HSTS bezeichnet HTTP Strict Transport Security; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. PKIX bezeichnet Public Key Infrastructure X.509; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. CT bezeichnet Certificate Transparency; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ACME bezeichnet Automated Certificate Management Environment; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Domains verifizieren ohne Hoheitsrechte abzuleiten Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Networking & DNS mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

DNSSEC TLS RDAP werden als technische Nachweise getrennt Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe DNS, DNSSEC, TLS, mTLS, RDAP als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer DNS bis ACME eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter DNS; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade HSTS, PKIX, CT, ACME duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 27. Open Banking

**Abkuerzungen:** AIS = Account Information Service, AISP = Account Information Service Provider, PIS = Payment Initiation Service, PISP = Payment Initiation Service Provider, SCA = Strong Customer Authentication, PSD2 = Payment Services Directive 2, SEPA = Single Euro Payments Area, IBAN = International Bank Account Number, BIC = Business Identifier Code

### Begriffe 1 bis 4: Bedeutung im Produkt

AIS steht fuer Account Information Service; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. AISP steht fuer Account Information Service Provider; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. PIS steht fuer Payment Initiation Service; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. PISP steht fuer Payment Initiation Service Provider; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

SCA bezeichnet Strong Customer Authentication; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. PSD2 bezeichnet Payment Services Directive 2; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SEPA bezeichnet Single Euro Payments Area; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. IBAN bezeichnet International Bank Account Number; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. BIC bezeichnet Business Identifier Code; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Expliziter Kontozugriff ohne Zahlungsrecht Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Open Banking mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Nur lesende Transaktionen an M08 senden Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe AIS, AISP, PIS, PISP, SCA als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer AIS bis BIC eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter AIS; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade PSD2, SEPA, IBAN, BIC duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 28. Payment Integration

**Abkuerzungen:** PSP = Payment Service Provider, EMI = Electronic Money Institution, PI = Payment Institution, RTGS = Real-Time Gross Settlement, ACH = Automated Clearing House, SCT = SEPA Credit Transfer, SCTInst = SEPA Instant Credit Transfer, RTP = Real-Time Payments, SWIFT = Society for Worldwide Interbank Financial Telecommunication

### Begriffe 1 bis 4: Bedeutung im Produkt

PSP steht fuer Payment Service Provider; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. EMI steht fuer Electronic Money Institution; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. PI steht fuer Payment Institution; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. RTGS steht fuer Real-Time Gross Settlement; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

ACH bezeichnet Automated Clearing House; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SCT bezeichnet SEPA Credit Transfer; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SCTInst bezeichnet SEPA Instant Credit Transfer; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. RTP bezeichnet Real-Time Payments; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SWIFT bezeichnet Society for Worldwide Interbank Financial Telecommunication; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Transaktionszustände und Risiko sauber modellieren Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Payment Integration mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Keine Zahlungsausführung durch Analysemodul Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe PSP, EMI, PI, RTGS, ACH als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer PSP bis SWIFT eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter PSP; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade SCT, SCTInst, RTP, SWIFT duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 29. Blockchain Integration

**Abkuerzungen:** DLT = Distributed Ledger Technology, EVM = Ethereum Virtual Machine, RPC = Remote Procedure Call, ABI = Application Binary Interface, SC = Smart Contract, DID = Decentralized Identifier, VC = Verifiable Credential, ZKP = Zero-Knowledge Proof, MPC = Multi-Party Computation

### Begriffe 1 bis 4: Bedeutung im Produkt

DLT steht fuer Distributed Ledger Technology; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. EVM steht fuer Ethereum Virtual Machine; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. RPC steht fuer Remote Procedure Call; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. ABI steht fuer Application Binary Interface; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

SC bezeichnet Smart Contract; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. DID bezeichnet Decentralized Identifier; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. VC bezeichnet Verifiable Credential; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ZKP bezeichnet Zero-Knowledge Proof; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. MPC bezeichnet Multi-Party Computation; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Smart Contracts nur über genehmigte Grenzen anbinden Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Blockchain Integration mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Read-only Chain-Events getrennt von Signaturaktionen Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe DLT, EVM, RPC, ABI, SC als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer DLT bis MPC eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter DLT; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade DID, VC, ZKP, MPC duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 30. Crypto Asset Risk

**Abkuerzungen:** CASP = Crypto-Asset Service Provider, VASP = Virtual Asset Service Provider, MiCA = Markets in Crypto-Assets Regulation, AML = Anti-Money Laundering, KYC = Know Your Customer, KYB = Know Your Business, TravelRule = Crypto Transfer Information Rule, CDD = Customer Due Diligence, EDD = Enhanced Due Diligence

### Begriffe 1 bis 4: Bedeutung im Produkt

CASP steht fuer Crypto-Asset Service Provider; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. VASP steht fuer Virtual Asset Service Provider; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. MiCA steht fuer Markets in Crypto-Assets Regulation; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. AML steht fuer Anti-Money Laundering; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

KYC bezeichnet Know Your Customer; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. KYB bezeichnet Know Your Business; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. TravelRule bezeichnet Crypto Transfer Information Rule; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. CDD bezeichnet Customer Due Diligence; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. EDD bezeichnet Enhanced Due Diligence; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Tokenklassifikation vor Wallet-Verbindung prüfen Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Crypto Asset Risk mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Wallet ist nicht automatisch reguliertes Konto Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe CASP, VASP, MiCA, AML, KYC als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer CASP bis EDD eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter CASP; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade KYB, TravelRule, CDD, EDD duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 31. Smart Contract Assurance

**Abkuerzungen:** Reentrancy = Recursive Contract Entry, CEI = Checks Effects Interactions, EIP = Ethereum Improvement Proposal, ERC = Ethereum Request for Comments, Slither = Static Contract Analyzer, Foundry = EVM Testing Toolkit, Hardhat = Ethereum Development Environment, Timelock = Delayed Administrative Action, Multisig = Multi-Signature Authorization

### Begriffe 1 bis 4: Bedeutung im Produkt

Reentrancy steht fuer Recursive Contract Entry; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. CEI steht fuer Checks Effects Interactions; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. EIP steht fuer Ethereum Improvement Proposal; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. ERC steht fuer Ethereum Request for Comments; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

Slither bezeichnet Static Contract Analyzer; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Foundry bezeichnet EVM Testing Toolkit; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Hardhat bezeichnet Ethereum Development Environment; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Timelock bezeichnet Delayed Administrative Action; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Multisig bezeichnet Multi-Signature Authorization; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Unveränderliche Ausführung benötigt Extra-Vorsicht Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Smart Contract Assurance mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Simulierter Settlement-Fail-Test vor Deployment Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe Reentrancy, CEI, EIP, ERC, Slither als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer Reentrancy bis Multisig eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter Reentrancy; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade Foundry, Hardhat, Timelock, Multisig duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 32. Web3 UX

**Abkuerzungen:** SIWE = Sign-In with Ethereum, EIP712 = Typed Structured Data Signing, Nonce = Single-Use Random Value, ChainID = Blockchain Network Identifier, Gas = Transaction Execution Fee, MEV = Maximal Extractable Value, AA = Account Abstraction, Paymaster = Gas Sponsorship Contract, WalletConnect = Wallet Connection Protocol

### Begriffe 1 bis 4: Bedeutung im Produkt

SIWE steht fuer Sign-In with Ethereum; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. EIP712 steht fuer Typed Structured Data Signing; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. Nonce steht fuer Single-Use Random Value; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. ChainID steht fuer Blockchain Network Identifier; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

Gas bezeichnet Transaction Execution Fee; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. MEV bezeichnet Maximal Extractable Value; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. AA bezeichnet Account Abstraction; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Paymaster bezeichnet Gas Sponsorship Contract; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. WalletConnect bezeichnet Wallet Connection Protocol; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Transaktions- und Berechtigungsrisiken sichtbar machen Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Web3 UX mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Wallet-Bestätigung mit Kette Betrag Gebühren und Empfänger Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe SIWE, EIP712, Nonce, ChainID, Gas als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer SIWE bis WalletConnect eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter SIWE; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade MEV, AA, Paymaster, WalletConnect duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 33. Release Metadata

**Abkuerzungen:** SPDX = Software Package Data Exchange, CycloneDX = SBOM Format, OSCAL = Open Security Controls Assessment Language, SARIF = Static Analysis Results Interchange Format, JWS = JSON Web Signature, DSSE = Dead Simple Signing Envelope, Sigstore = Open Source Signing Project, Rekor = Transparency Log, SCEP = Simple Certificate Enrollment Protocol

### Begriffe 1 bis 4: Bedeutung im Produkt

SPDX steht fuer Software Package Data Exchange; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. CycloneDX steht fuer SBOM Format; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. OSCAL steht fuer Open Security Controls Assessment Language; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SARIF steht fuer Static Analysis Results Interchange Format; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

JWS bezeichnet JSON Web Signature; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. DSSE bezeichnet Dead Simple Signing Envelope; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Sigstore bezeichnet Open Source Signing Project; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Rekor bezeichnet Transparency Log; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SCEP bezeichnet Simple Certificate Enrollment Protocol; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Semantik von Zertifizierung und Label unterscheiden Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Release Metadata mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

Intern PASS ist nicht extern zertifiziert Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe SPDX, CycloneDX, OSCAL, SARIF, JWS als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer SPDX bis SCEP eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter SPDX; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade DSSE, Sigstore, Rekor, SCEP duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.


---

## 34. Operations Language

**Abkuerzungen:** P0 = Critical Incident Priority, P1 = High Incident Priority, SOP = Standard Operating Procedure, Runbook = Operational Step Guide, OnCall = Incident Response Duty, RCA = Root Cause Analysis, Postmortem = Incident Learning Review, ChangeFreeze = Temporary Release Stop, SLA = Service Level Agreement

### Begriffe 1 bis 4: Bedeutung im Produkt

P0 steht fuer Critical Incident Priority; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. P1 steht fuer High Incident Priority; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. SOP steht fuer Standard Operating Procedure; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis. Runbook steht fuer Operational Step Guide; die Bezeichnung definiert eine Rolle im technischen Vertrag und ist nicht automatisch ein Sicherheitsnachweis.

### Begriffe 5 bis 9: Integrationssprache

OnCall bezeichnet Incident Response Duty; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. RCA bezeichnet Root Cause Analysis; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. Postmortem bezeichnet Incident Learning Review; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. ChangeFreeze bezeichnet Temporary Release Stop; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet. SLA bezeichnet Service Level Agreement; im Design wird der Begriff nur mit Version, Eigentuemern und messbarem Pruefziel verwendet.

### Wozu diese Entwicklungsabkuerzungen?

Störung, Risiko und Verantwortlichkeit schnell kommunizieren Fuer HCOS muss jede Abkuerzung zweifach lesbar sein: als Kurzform fuer die Entwickler und als konkrete Konsequenz fuer Nutzer, Audit und Berechtigungsmodell. Eine Begriffsliste ohne Anwendungsbeispiel erzeugt nur Oberflaechenkomplexitaet. Deshalb verknuepft der Katalog Operations Language mit Verantwortlichkeit, Datenklasse und Abnahmeschwelle.

### Konkretes Integrationsszenario

P1-Vorfall wechselt Status aller betroffenen Belege Der Ablauf beginnt mit einem synthetischen Beispiel, in dem die Begriffe P0, P1, SOP, Runbook, OnCall als kommentierte Vertragsfelder erscheinen. Es folgen ein positiver Referenzfall und ein absichtlich fehlerhafter Gegenfall. Die UI zeigt keine nackte Akronymkette: Ein Tooltip liefert die ausgeschriebene Bezeichnung, eine knappe Aufgabe und eine Verknuepfung zur maschinenlesbaren Schnittstellendefinition.

### Implementationsstrategie in sechs Schritten

Zuerst werden die Ziele und ein unverwechselbarer Domain Name festgelegt. Anschliessend wird fuer P0 bis SLA eine kanonische Glossar-ID vergeben. Dritter Schritt ist die Validierung von Schreibweisen und Aliasen im Schema. Viertens werden OpenAPI/JSON-Schema und passende Repository-Funktionen verknuepft. Fuenftens folgen negative Contract-Tests gegen unbekannte Kurzformen. Sechstens entsteht eine signierte Glossar-Version mit Reviewdatum und Referenzen.

### Datenschnittstelle und Versionierung

Der Datensatz acronym_entry enthaelt acronym, expansion, language, type, zone, module_id, applicability, example, source_url, verified_at und deprecated_by. Ein Aenderungsvorschlag darf bestehende Bedeutungen nicht still ueberschreiben, sondern benoetigt Semantic-Versioning. Fuer kritische Fachausdruecke aus Finance und Security wird die Bedeutung durch zwei Fachrollen bestaetigt. Diese strukturierten Informationen koennen in M01, M06 und M12 wiederverwendet werden.

### Harness-Loop-Aufgabe und Stop-Bedingung

Ein PLAN-Knoten fragt nach dem Problem hinter P0; der BUILD-Knoten erzeugt nur ein lokales Schema-Artefakt. TEST kontrolliert, ob alle 9 Begriffe erklaert, verlinkt und kontraktgetestet sind. AUDIT sucht Mehrdeutigkeit, fehlerhafte URLs und unbelegte Security-Claims. Die Schleife ist durch maximal drei Korrekturrunden begrenzt; unbekannte Normausgaben oder Konflikte zwischen Teams beenden die Automatik mit REVIEW_REQUIRED statt erfundenem Ergebnis.

### Negativtests und Sicherheitskontrollen

Die Testserie injiziert einen falsch geschriebenen Acronym-Schluessel, ein nicht erlaubtes URL-Schema, eine unvollstaendige Definition und einen veralteten Standardverweis. Alle vier Faelle muessen einen erklaerbaren Fehlerstatus liefern. Gerade RCA, Postmortem, ChangeFreeze, SLA duerfen nicht als leere Platzhalter in produktive Akten gelangen. Jede aus externen Repositories gelesene Textdefinition wird vor HTML-Ausgabe sicher kodiert und als unvertrauenswuerdige Quelle behandelt.

### Abnahme, Metriken und Artefakte

Der Glossarbereich ist abgenommen, wenn alle 9 Kurzformen dieses Kapitels eine eindeutige Langform, eine technische Rolle, ein Beispiel und mindestens einen negativen Contract-Test besitzen. Die Kennzahlen sind term_coverage, ambiguous_term_count, missing_reference_count und glossary_schema_valid. Als Ergebnis werden acronym_catalog.csv, acronym_catalog.json, ein HTML-Hilfetext, ein Testreport und ein Review-Receipt freigegeben.

