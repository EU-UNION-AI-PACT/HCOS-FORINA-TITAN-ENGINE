# HCOS FORINA TITAN · Band A

## HCOS Architektur, IA, XD und fehlende Implementierungen

Fehlstellenanalyse, Oberflaechenentwicklung, Module, Harness Loop und Release-Governance

**Stand:** 06.11.2026; **Code-Referenz:** https://github.com/EU-UNION-AI-PACT/HCOS-FORINA-TITAN-ENGINE/commit/4cd1db2066237798717d201fc4a0a46759664a85

**Rechts-/Markenhinweis:** Interne Audit-Pruefung ist nicht gleich amtliche Zulassung oder externe Zertifizierung. Das Markenrecht der jeweiligen Organisation ist gesondert zu beachten. Keine personenbezogenen Geheimnisse oder Produktionsdaten.


---

## 01. Executive Target Architecture

### Problem und begruendete Luecke

Die bestehende Plattform besitzt viele Funktionsgruppen, jedoch fehlt ein verbindlicher Gesamtnutzen mit Grenzen je Betriebszone. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Ein öffentlich lesbares Zielbild unterscheidet Portal, Engine, offline geschützte lokale Werkzeuge und nur autorisierte Föderation. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

Capability-Karte mit Owner, Betriebszone, Datenklasse, Kritikalität, Vertrag und Systemgrenze. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Executive Target Architecture einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel ETA erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Feature-Wildwuchs, unklare Zuständigkeit und unbewiesene Produktivfreigaben. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Jede Capability hat Owner, API-Vertrag, Evidenzstatus und Rückbaupfad. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ein Dashboard-Wechsel darf niemals automatisch eine Zahlungs- oder Föderationsberechtigung erteilen. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 02. Informationsarchitektur IA

### Problem und begruendete Luecke

Verschiedene Tabs und Modulregister zeigen Fähigkeiten, aber Nutzer suchen nach Aufgaben statt Dateinamen. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Task-first-Navigation nach Prüfen, Erforschen, Bauen, Freigeben und Beobachten ersetzt ein flaches Menü. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

Navigationsschema aus Arbeitsbereich, Objekt, Aktivität, Sicherheitsstatus und zuletzt genutztem Kontext. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Informationsarchitektur IA einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel IA erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Verwechslung von Read-only- und Aktionsmodi führt zu gefährlichen Klickpfaden. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Ein neuer Benutzer findet den Prüfbericht ohne Einarbeitung und erkennt vor jeder Aktion die Folgen. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ein Prüfer sucht Belege für M07 und gelangt in höchstens drei Schritten zum passenden Evidence-Graphen. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 03. Experience Design XD

### Problem und begruendete Luecke

Das Portal wirkt technisch, aber Statusmeldungen und Aufgabenfolgen sind nicht durchgängig verständlich. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Ein konsistentes Interaktionsmodell verbindet Sprache, Feedback, Vorschau, Widerruf und sichtbare Systemgrenzen. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

Experience-Tokens für Zustände, Aufgaben, Warnungen, Eingaben, Fehler und leere Ansichten. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Experience Design XD einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel XD erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Schöne Animationen dürfen keinen falschen Sicherheitszustand visualisieren. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Jeder entscheidende Workflow besitzt Start, Vorschau, Folgenhinweis, Bestätigung, Ergebnis und Rückweg. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Bei fehlendem Evidence-Datensatz zeigt der Bildschirm neutral unbekannt statt grünes Erfolgslicht. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 04. Papier 4A: Intelligent Automation

### Problem und begruendete Luecke

Automatisierte Agenten und Prüfpipelines sind vorhanden, ihr Entscheidungsspielraum ist jedoch nicht konsequent formalisiert. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

IA bedeutet hier Intelligent Automation: Planen, Prüfen, Wiederholen mit deterministischen Freigabegrenzen. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

ActionContract mit erlaubter Aktion, Eignern, Ressourcenbudget, Testoracle und Schadensklasse. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Papier 4A: Intelligent Automation einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel 4A erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Selbstreferenzierende Aktionen oder ungeprüfte autonome Änderungen können sich hochschaukeln. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Die Automationsschleife stoppt bei unklarer Autorität oder fehlendem Beleg und verlangt Menschenentscheidung. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ein Agent schlägt einen Fix vor; nur isolierte Tests und explizite Freigabe lassen ihn in einen Release gelangen. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 05. Papier 4B: Design-System und Microinteractions

### Problem und begruendete Luecke

Leuchtende Statusanzeigen und interaktive Module benötigen gemeinsame visuelle Regeln statt Einzelgestaltung. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Eine UI-Bibliothek definiert Typografie, Kontrast, Fokus, Raster, Motion, Schrift und barrierearme Semantik. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

Design-Tokens als versionierte JSON-Schemata; Komponenten für EvidenceCard, GateStatus, ScopeBanner und SafeAction. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Papier 4B: Design-System und Microinteractions einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel 4B erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Ablenkende Daueranimation und unzureichender Kontrast beeinträchtigen Vertrauen und Barrierefreiheit. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Jedes UI-Element hat Tastaturpfad, Screenreader-Name, Disabled-Zustand und nachvollziehbare Fehlermeldung. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Eine Prüfstufe wechselt nur dann auf grün, wenn die Backend-Signatur einer gültigen Audit-Entscheidung vorliegt. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 06. Gesamtmodell der 13 Module

### Problem und begruendete Luecke

Im Registry-Modell sind 13 Kernmodule und weitere Funktionsgruppen vorhanden; die Grenzen sind teilweise implizit. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Ein Capability-Graph definiert exakt, wer Daten lesen, Mutationen ausführen oder nur Vorschläge generieren darf. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

module_id, capability_id, input_schema, output_schema, permission, zone, evidence_ref und dependency_hash. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Gesamtmodell der 13 Module einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel M01-M13 erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Import-seitige Effekte und transitive Abhängigkeiten können die Sicherheitsgrenze unterlaufen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Alle 13 Module haben maschinenlesbare Verträge mit Negativtests und signierten Versionsfreigaben. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

M08 darf Zahlungsdaten auswerten, aber keine Überweisung oder Schreibberechtigung erlangen. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 07. 50-Repository-Katalog als Source of Truth

### Problem und begruendete Luecke

Der neue Explorer listet 50 Projekte, doch Namensmapping ist kein Supply-Chain-Nachweis. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Ein verifizierter Katalog trennt Fundstelle, Lizenz-Behauptung, geprüfte Lizenz, Schwachstellen und tatsächliche Einbindung. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

Repository-URL, Commit-SHA, Tag, Lizenzbeleg, SBOM, Herkunft und Freigabeidentität je Eintrag. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer 50-Repository-Katalog als Source of Truth einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel REPO erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Namensaliase, ungesicherte Links und unbewiesene Security-Labels verwässern Aussagen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Kein Repo erhält VERIFIED ohne versionierte Primärquelle, Befund und zuständige Freigabe. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Eine neue Katalogzeile landet zunächst in Quarantäne und nicht in Sovereign. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 08. Governance und Verantwortlichkeiten

### Problem und begruendete Luecke

Technische Freigabefunktionen existieren, ohne durchgehendes Rollenmodell für Risikoakzeptanz und externe Aussagen. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

RACI und Vier-Augen-Prinzip trennen Entwickler, Prüfer, Freigebende und Betreiber. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

RoleBinding verknüpft Person oder Dienstidentität mit Scope, Zeit, Zweck und dokumentiertem Widerruf. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Governance und Verantwortlichkeiten einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel RACI erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Eine Selbstzertifizierung kann sonst unbeabsichtigt als externe Bescheinigung erscheinen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Zwei unabhängig autorisierte Rollen bestätigen kritische Produktionseingriffe und Audit-Veröffentlichungen. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ein Entwickler darf einen Kontrollbefund korrigieren, aber nicht seinen eigenen Hochrisiko-Befund abschließend abnehmen. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 09. Portal-Startseite und Nutzerführung

### Problem und begruendete Luecke

Ein Feature-Tab ist kein verlässlicher Einstieg in komplexe Prüf- und Finanzabläufe. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Eine rollenabhängige Startseite zeigt offene Aufgaben, Risiken, unabhängige Prüfnachweise und gesperrte Aktionen. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

HomeView aggregiert ReadModel statt direkte Schreibrechte aus M01 bis M13. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Portal-Startseite und Nutzerführung einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel HOME erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Echte Risiken können in dekorativen Karten verschwinden, wenn Priorität falsch gesetzt ist. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Top-Risiken, ausstehende Freigaben und Revisionsstand sind ohne Scrollen erreichbar. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Anstelle allgemeiner 100-Prozent-Balken erscheint ein überprüfbarer Status mit Erhebungszeit und Geltungsbereich. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 10. Evidenzzentriertes Statusmodell

### Problem und begruendete Luecke

Die Oberfläche kann feste PASS-Texte ausgeben, die nicht dem tatsächlichen Gate-Ergebnis entsprechen. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Der Status wird aus signierter Evaluation und Gültigkeitsfenster berechnet, nicht aus UI-Konstanten. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

EvidenceStatus: UNKNOWN, OPEN, BLOCKED, PASS_INTERNAL, REVIEWED, EXTERNAL_ATTESTED, EXPIRED. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Evidenzzentriertes Statusmodell einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel EVID erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Ein alter PASS nach neuer Codeversion ist eine Fehlfreigabe. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Statuswechsel sind transaktional und an Artifact-Hash, Signer, Scope und Zeit gebunden. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ein geänderter Build-Hash setzt zuvor erteilte Freigaben automatisch auf erneute Prüfung. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 11. Souveräner Offline-Launcher

### Problem und begruendete Luecke

Python-interne Netzwerksperren verhindern keine externen Prozess- oder Bibliothekspfade. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Ein unabhängiger Launcher validiert Dateisignaturen, genehmigte Pfade und technische Isolationsfähigkeit vor dem Start. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

LaunchManifest mit executable_hash, approved_roots, namespace_attestation, no_egress und policy_version. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Souveräner Offline-Launcher einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel LAUNCH erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Wenn keine isolierende Hostfähigkeit ohne Systemänderung verfügbar ist, muss das Programm nicht starten. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Positivtest mit synthetischer Datei und negativer Egress-Test außerhalb des Scannerprozesses bestehen. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ohne messbaren No-Egress-Nachweis wird der Start abgelehnt, nicht still auf Python-Monkeypatch reduziert. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 12. Host-Neutralität und sichere Distribution

### Problem und begruendete Luecke

Der lokale Scanner darf bestehende Arch-Konfiguration weder installieren noch verändern. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Eine rein portable Auslieferung nutzt genehmigte Ordner, prüft Bibliotheken und deklariert ihre Laufzeitanforderungen. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

Staging-Metadaten mit Hashes, Schreibpfad-Whitelist, Uninstall-Prozedur und keinerlei Hostservice. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Host-Neutralität und sichere Distribution einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel HOST erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Automatisches Paketmanagement, Cron oder Firewall-Änderungen verletzen die Betriebsbedingung. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Tests protokollieren nur Metadaten und zeigen keine Hostmutationen bei Probe und Rückbau. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Nach Ausführung unterscheiden sich System-Konfigurationsdateien und Quell-Timestamps nicht. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 13. Identität, Einwilligung und Berechtigung

### Problem und begruendete Luecke

OIDC und Consent-Komponenten bilden noch keinen einheitlichen globalen Berechtigungsentscheid. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Eine Policy Decision Point trennt Authentication, Authorization und Consent für jede sensible Operation. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

Subject, purpose, resource, action, jurisdiction, credential_age und grant_id bilden den Policy-Kontext. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Identität, Einwilligung und Berechtigung einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel IAM erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Verwechselte Nutzeridentität oder widerrufene Einwilligung ermöglichen unzulässigen Zugriff. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Jeder Zugriff ist default deny und erfordert ein aktuelles, zweckgebundenes Grant. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Bei Entzug einer Datenfreigabe verschwindet die Berechtigung aus Cache, Connector und UI. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 14. Schlüssel, Signaturen und Rotation

### Problem und begruendete Luecke

Ed25519-Bescheinigungen liefern Integrität, aber eigene Signaturen sind keine unabhängigen Zertifizierungen. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Das Key-Lifecycle-Modell trennt Signierzwecke, Verwahrung, Rotation, Sperrung und Bestätigung der Schlüsselhoheit. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

KeyRecord mit key_id, usage, custodian, created_at, expires_at, revoke_ref und verification_scope. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Schlüssel, Signaturen und Rotation einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel KMS erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Ein kompromittierter Schlüssel kann scheinbar gültige Artefakte produzieren. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Gesonderte Schlüssel für Build, Audit und Nutzer-Freigabe; keine privaten Schlüssel in ZIP oder Logs. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ein gesperrter Schlüssel macht alle davon abhängigen Statuskarten ungültig. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 15. Privacy by Design und Datenminimierung

### Problem und begruendete Luecke

Katalog, Finanzanalyse und Agentensitzungen berühren verschiedene Personen- und Geheimnisklassen. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Datentypen werden vor Verarbeitung klassifiziert; synthetische Demos und reale Daten bleiben hart getrennt. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

DataClass, purpose, lawful_basis, retention, residency, deletion_job und access_policy an jedem Datensatz. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Privacy by Design und Datenminimierung einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel PRIV erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Protokolle oder Testfixtures könnten reale Kontodaten und Zugangsgeheimnisse aufnehmen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Export und Debugger maskieren vertrauliche Felder; Lösch- und Auskunftswege sind nachweisbar. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ein Support-Report enthält niemals IBAN, Token oder Credential-Klartext. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 16. Banking Read-only und Settlement-Grenzen

### Problem und begruendete Luecke

Die Transaktionsanalyse besitzt Code-Sperren, aber Namensfilter ersetzen keine bankenrechtliche Berechtigungstrennung. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Ausschließlich getrennte Read-only-Zugangsdaten und capability-minimierte Connectoren bedienen M08. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

AccountLinkId, consent_scope, provider, expiry, read_only_assertion und audit_receipt. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Banking Read-only und Settlement-Grenzen einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel FIN erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Ein neu angeschlossener Zahlungsprovider darf keine latenten Schreibrechte übernehmen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Negative API-Tests beweisen, dass Auszahlungen und Lastschriften unabhängig von Aktionsnamen blockiert bleiben. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Die UI kann verdächtige Abos markieren, aber niemals Geld verschieben. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 17. Finanzanomalien und Erklärung

### Problem und begruendete Luecke

Doppelbelastung, Preissteigerung und Zombie-Abos können legitime Zahlungen falsch einordnen. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Ein erklärbares Regelwerk zeigt Annahmen, Vertrauenswerte, Gegenbeispiele und Nutzerfeedback. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

Finding mit rule_version, evidence_refs, confidence_band, currency, period und reversible_label. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Finanzanomalien und Erklärung einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel ANOM erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Unbegründete Ersparnisbehauptungen könnten finanzielle Entscheidungen verfälschen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Befunde gelten als Hinweise mit Rücknahmeoption und werden auf synthetischen Testfällen kalibriert. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Zwei gleiche Kaffeezahlungen bleiben zunächst Verdacht, solange keine Händler-ID oder Buchungskorrektur geklärt ist. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 18. FORINA Domain Trust

### Problem und begruendete Luecke

Technischer DNS/TLS-Erfolg ist keine Organisationsverifizierung und kein Föderationsrecht. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Eine gestufte Trust-Kette behandelt Discovery, Kontrolle, Organisation, Compliance und explizite Autorisierung getrennt. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

DomainTrustRecord mit proofs, claim_type, registrar_check, legal_entity_ref, scope und valid_until. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer FORINA Domain Trust einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel TRUST erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Einfache URL-Scans dürfen keine staatliche Zugehörigkeit oder Akkreditierung suggerieren. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Statuswerte werden nie übersprungen; Federation beginnt nur nach dokumentierter Einwilligung der Organisation. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Eine .gov-Domain ohne belegte Delegation erhält kein Organisationszertifikat. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 19. API- und Ereignisarchitektur

### Problem und begruendete Luecke

Viele Dienste lassen sich anbinden, aber undokumentierte Eventverträge verursachen verdeckte Nebenwirkungen. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Schema Registry, versionierte Events, Idempotenz und Replay-Schutz werden zum verbindlichen Integrationskern. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

OpenAPI/AsyncAPI Verträge für command_id, correlation_id, policy_ref, schema_version und idempotency_key. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer API- und Ereignisarchitektur einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel API erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Event-Duplikate, Ausführungsreihenfolge und inkonsistente Retries gefährden Datenzustände. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Contract-Tests und Dead-letter-Queues sind für jede asynchrone Verbindung definiert. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Eine doppelte Nachricht löst dieselbe fachliche Aktion höchstens einmal aus. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 20. Knowledge Graph und Provenienz

### Problem und begruendete Luecke

Dokumente, URLs, Frameworks und Repo-Evidenz bleiben sonst in mehreren Listen isoliert. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Ein gerichteter Evidence Graph verbindet Anforderungen mit Assets, Kontrollen, Tests und verantwortlichen Prüfern. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

Nodes für Source, Requirement, Control, Artifact, TestRun und Approval; Edges mit signierter Herkunft. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Knowledge Graph und Provenienz einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel GRAPH erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Automatisch abgeleitete Beziehungen könnten als offizielle Referenz durchgehen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Jeder inferierte Mapping-Edge besitzt Konfidenz, Begründung und menschliche Freigabestufe. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Eine OWASP-Prüfung führt per Klick zu Code-Test, Prüflauf und konkreter Anforderung. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 21. Agenten-Orchestrierung und Toolrechte

### Problem und begruendete Luecke

Ein Agent, der Tools frei ausführen darf, kann Sicherheitsgrenzen umgehen, auch wenn sein Text harmlos aussieht. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Capabilities werden außerhalb des Prompt-Kontexts technisch erzwungen; Agenten liefern zunächst Vorschläge. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

AgentTask mit inputs, output_schema, budget, tool_allowlist, approved_workspace und risk_class. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Agenten-Orchestrierung und Toolrechte einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel AGENT erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Prompt-Injection über Repos, Mails oder Webseiten darf keine neue Toolberechtigung erzeugen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Jede Agentenaktion ist einer expliziten Policy zugeordnet; nicht erlaubte Toolaufrufe werden abgewiesen. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ein Webseitenhinweis auf sudo-Befehle bleibt Dateninhalt und niemals Handlungsanweisung. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 22. Harness Loop und kontrollierte Autonomie

### Problem und begruendete Luecke

Eine schnelle Implementationsserie benötigt reproduzierbare Kontrollpunkte statt unendlicher Selbstbestätigung. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Plan-Build-Test-Audit-Review-Release-Monitor bildet eine begrenzte, policy-gesteuerte Verbesserungsfolge. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

LoopRecord mit iteration, task_id, state, input_hash, test_oracle, evidence_hash und stop_reason. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Harness Loop und kontrollierte Autonomie einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel LOOP erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Endlosschleifen, unsichere Selbstfreigabe und Modelldrift müssen ausdrücklich verhindert werden. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Maximale Iterationen, Budget, Freigabepflicht und negativer Test gehören in jede Arbeitsdefinition. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Wenn ein Test dreimal nicht besteht, stoppt die Schleife und erstellt ein handlungsfähiges Defect-Dossier. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 23. Evidence Bus und Audit-Pipeline

### Problem und begruendete Luecke

Ein grüner Test ist nicht automatisch beweiskräftig, wenn Ausführer und Prüfer identisch sind. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Ein Evidence Bus versieht jede Entscheidung mit Quelle, Hash, Scope, Zeit und Prüferidentität. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

EvidenceEnvelope als kanonisches JSON mit Schema-Id, input/output digest, issuer und signer_role. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Evidence Bus und Audit-Pipeline einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel AUD erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Unvollständige Logs oder nachträgliche Änderungen entwerten Revisionssicherheit. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Für jedes Gate existiert ein reproduzierbarer Datensatz mit unabhängiger Prüfroutine. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Auditoren können eine Freigabe offline anhand von Paket, Manifest und Public Key überprüfen. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 24. Audit-Cockpit und Live-Status

### Problem und begruendete Luecke

Statische PASS-Aufschriften können fail-closed Entscheidungen im Backend visuell überdecken. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Das Cockpit zeigt pro Gate Ergebnis, Beleg, Prüfer, Ausführungsdatum, Gültigkeit und Fehlergrund. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

GateView wird ausschließlich aus signierten Status-Events und nicht aus hartcodierter Farbe erzeugt. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Audit-Cockpit und Live-Status einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel GATEUI erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Ein einzelner unbekannter Gate-Status kann sonst fälschlich als Systemfreigabe erscheinen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

FAILED, UNKNOWN und EXPIRED sind sichtbar verschieden und blockieren kritische Buttons. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ein G08-Mismatch erzeugt eine rote Sperrkarte mit betroffener Datei und Recheck-Aktion. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 25. Nachweis-Abzeichen und Markenschutz

### Problem und begruendete Luecke

Ein intern erzeugtes Zertifikat kann unbeabsichtigt wie ein offizielles ISO- oder EU-Siegel wirken. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Interne Prüfmarken unterscheiden sich sichtbar von externen Zertifizierungszeichen und zeigen ihren Aussteller. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

BadgeRecord mit assertion_type, scope, issuer, issued_at, expiry, evidence_url und revocation_endpoint. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Nachweis-Abzeichen und Markenschutz einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel BADGE erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Falsche Zertifikatsbehauptungen erzeugen Rechts- und Vertrauensrisiken. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Offizielle Marken erscheinen nur mit erlaubter Nutzung und einem überprüfbaren Zertifikat. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Das Portal zeigt INTERN AUDITIERT statt ISO ZERTIFIZIERT, wenn keine akkreditierte Stelle beteiligt war. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 26. Barrierefreiheit und Performance-Budget

### Problem und begruendete Luecke

Komplexe Graphiken, animierte Dashboards und Kontrastfarben können Nutzergruppen ausschließen. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

WCAG-orientierte Komponenten mit reduzierter Bewegung, Tastaturführung und verständlichen Fehlermeldungen. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

Token für Farbkontrast, focus-visible, aria-label, reduced-motion und lokalisierte Statusnamen. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Barrierefreiheit und Performance-Budget einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel A11Y erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Screenreader erhalten möglicherweise eine falsche Reihenfolge oder rein dekorative Warnungen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Automatisierte Axe-Prüfung und manuelle Tastaturtests bestehen auf zentralen Use Cases. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Eine Warnung ist mit Text und Symbol wahrnehmbar und nicht nur rot gefärbt. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 27. Mehrsprachigkeit und Rechtsräume

### Problem und begruendete Luecke

Internationale Normen und Mandate unterscheiden sich nach Rechtsraum und Nutzerrolle. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Jurisdiction Resolver wählt Texte, Rechtsgrundlagen und Anforderungen anhand belegter Anwendbarkeit. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

LegalApplicability mit country, sector, legal_role, legal_basis, version und review_date. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Mehrsprachigkeit und Rechtsräume einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel L10N erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Eine generische EU-Regel könnte fälschlich auf USA oder CH übertragen werden. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Jede länderspezifische Aussage besitzt einen Normverweis und letzten Reviewzeitpunkt. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

DE, EN und FR zeigen dieselbe technische Prüfung, aber korrekte regionale Rechtskontexte. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 28. Observability ohne Datenleckage

### Problem und begruendete Luecke

Telemetrie ist nützlich, darf aber sensible Nutzdaten, Prompts oder Schlüssel nicht exponieren. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Metriken und strukturelle Ereignisse werden ohne Payloads, mit Sampling und striktem Redaction-Schema erhoben. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

EventSchema mit severity, request_id, elapsed_ms, control_id und secret_scrub_result. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Observability ohne Datenleckage einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel OBS erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Selbst gut gemeinte Debug-Protokolle könnten echte Bankdaten enthalten. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Redaction-Fuzzing bestätigt, dass keine Test-Token oder personenbezogenen Werte gespeichert werden. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Eine Fehlermeldung nennt einen anonymen Referenzcode statt einer IBAN. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 29. Threat Modeling und Red Team

### Problem und begruendete Luecke

Die bisherige Regex-Erkennung ist hilfreich, aber gegen Toolmissbrauch und Supply-Chain-Angriffe unvollständig. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

STRIDE, ATT&CK-Mapping und Missbrauchsszenarien werden pro Integrationsgrenze modelliert. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

ThreatRecord mit actor, trust_boundary, abuse_case, impact, mitigation, test und residual_risk. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Threat Modeling und Red Team einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel THREAT erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Insbesondere URI-Schemas, Archive, dynamische Imports und Agenten-Tools erlauben Umgehungen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Jede High-Risk-Grenze hat mindestens einen Negativtest und dokumentierte Restrestrisiken. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Eine manipulierte URL mit javascript-Schema wird im Webkatalog blockiert. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 30. Supply Chain und sichere Builds

### Problem und begruendete Luecke

Eine Liste von Projektnamen sagt nichts über den tatsächlich ausgelieferten Binärinhalt aus. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Build-Provenienz, SBOM, gepinnte Abhängigkeiten und signierte Artefakte bilden eine gemeinsame Kette. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

ReleaseManifest mit commit, dependency_lock, builder_id, SBoM_digest, build_hash und verification_method. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Supply Chain und sichere Builds einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel SLSA erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Ungeprüfte Netzwerkdownloads und Binary-Replacement gefährden die portable Distribution. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Ein externer Prüfer kann das Paket auf exakt definierte Quellen und Binärhashes zurückführen. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ein AppImage wird nur veröffentlicht, wenn Hash, Signatur und vorab geprüftes Manifest übereinstimmen. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 31. Backup und Recovery als Fertigkeit

### Problem und begruendete Luecke

Ein Backup, das sich extrahieren lässt, belegt noch nicht die vollständige Wiederanlaufbarkeit. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Restore-Drills testen Integrität, Anwendungen, Datenkonsistenz und geheimnisfreie Wiederherstellung. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

RestoreRun mit archive_digest, restoration_scope, RTO, RPO, file_parity und verified_by. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Backup und Recovery als Fertigkeit einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel BCP erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Ein Archiv kann unvollständige Tabellen oder unsichere Symlinks enthalten. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Vollständiger Hashvergleich, kontrollierte Extraktion und simuliertes Anlaufen mit synthetischen Daten. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Eine monatliche Testwiederherstellung erreicht das definierte RTO, ohne den Host zu verändern. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 32. Releasemanagement und Rollback

### Problem und begruendete Luecke

Häufige Commits und Tags brauchen klare Stufen zwischen Experiment, Pilot und Veröffentlichung. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

A signiertes Release-Promotionsmodell trennt Dev, Synthetic, Audit und Production mit Rollbackbedingungen. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

ReleaseRecord mit stage, artifact_digest, approvals, gate_results, rollback_image und change_window. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Releasemanagement und Rollback einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel REL erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Feste Produktivlabels könnten bei neuen Fehlern unverändert bestehen bleiben. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Ein neues Release ist ohne unabhängige Gate- und Policy-Nachweise nicht promotierbar. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Bei Fehlalarm wird das zuletzt freigegebene Paket ohne Neuinstallation wiederhergestellt. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 33. Finanzplanung und Betriebsmodell

### Problem und begruendete Luecke

Viele Module erhöhen den Nutzen, erzeugen aber auch laufende Wartungs- und Prüflasten. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Kosten- und Kapazitätsbudgets werden pro Service, Datenzone und externem Connector geplant. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

BudgetCard mit unit_cost, usage_cap, license_obligation, maintenance_owner und cost_ceiling. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Finanzplanung und Betriebsmodell einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel OPS erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Ein scheinbar kostenloser Dienst kann teure Nutzung, Datenabfluss oder Lizenzpflichten auslösen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

Keine Funktion verlässt die Pilotphase ohne Kostendeckel, Exit-Plan und vollständige Abhängigkeiten. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Ein neuer Open-Banking-Connector hat getrennte monatliche Kosten- und Risikoobergrenzen. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.


---

## 34. Roadmap, KPIs und Governance-Rhythmus

### Problem und begruendete Luecke

Die technische Breite verlangt eine klare Reihenfolge und messbare Qualitätsdefinitionen. Diese Beobachtung ist eine Architektur- und Produktentscheidung, keine Behauptung, dass jede vorhandene Funktion bereits produktiv abgesichert sei. Vor dem Ausbau wird deshalb eine Ist-Soll-Differenz pro M01–M13 erfasst: bestehender Endpunkt, nutzbarer Datenfluss, Sicherheitsannahmen, verantwortliche Rolle und fehlender Nachweis. Ein Bildschirm oder ein gruener Test zaehlt erst dann als Beleg, wenn er auf ein reproduzierbares Artefakt zeigt.

### Zielbild und Verantwortung

Eine priorisierte 90/180/365-Tage-Roadmap ordnet Sicherheitsgrenzen vor UI-Politur und optionalen Integrationen. Im HCOS-Kontext wird die Zielzustaendigkeit in eine klar benannte Capability mit eigenem technischen Scope uebersetzt. Der Nutzer sieht, was das Feature kann, was es ausdruecklich nicht kann und wer die Freigabe verantwortet. Lokale Offline-Funktionen, Entwicklungsdemos und autorisierte externe Federation bleiben visuell und technisch unterscheidbar.

### Datenmodell und Integrationsvertrag

RoadmapItem mit value, dependency, effort, risk_reduction, owner, milestone und evidence_target. Zusaetzlich braucht jeder Datensatz Schema-Version, Herkunfts-URI, Content-Hash, Erzeugungszeit, Freigabe-Scope und Loesch-/Ablaufregel. Lesende Abfragen und schreibende Kommandos werden unterschiedlich typisiert; diese Trennung muss auf API- und Prozess-Ebene durchgesetzt sein. Ein Frontend-Status darf diese Kontrollen nicht umgehen, weil er lediglich eine Darstellung der Backend-Evidence ist.

### Implementierung I: schneiden, spezifizieren, isolieren

1. Fachgrenze: Fuer Roadmap, KPIs und Governance-Rhythmus einen konkreten User-Flow und einen unzulaessigen Gegentest dokumentieren. 2. Vertrag: Input-, Output- und Fehler-Schema mit Version, Eigentuemer, Richtlinie und Zonenbezug definieren. 3. Isolation: Nur synthetische Testdaten verwenden und ein Nein-zu-unbekannten-Rechten als Standard festlegen. Bereits vorhandener Code wird nicht blind ueberschrieben; jede Aenderung beginnt mit Inventar und nachvollziehbarer Diff-Freigabe.

### Implementierung II: bauen, testen, nachweisen

4. Implementieren: Eine kleine, idempotente Schnittstelle mit klarer Ruecknahme und nachvollziehbarem Status einfuehren. 5. Pruefen: Unit-, Integrations-, Negativ-, Rollen- und Accessibility-Tests mit reproduzierbaren synthetischen Fixtures ausfuehren. 6. Nachweisen: Build-Hash, Testmatrix, Review-Entscheidung und offene Restrestrisiken in einer gemeinsamen Evidence-Envelope speichern. Keine externe Freigabe wird aus einer internen Testfarbe abgeleitet.

### Harness-Loop: kontrollierter Verbesserungszyklus

Die Funktion HCL (Harness Control Loop) fuehrt PLAN → DESIGN → BUILD → TEST → AUDIT → HUMAN APPROVAL → RELEASE → MONITOR aus. Jeder Lauf erhaelt eine unveraenderliche task_id, messbare Akzeptanzregeln und ein Iterationsbudget. Wenn der Testoracle einen Widerspruch zum Ziel ROAD erkennt, entsteht ein Defect-Dossier statt automatischer Selbstfreigabe. Hochrisiko-Aktionen, Secrets, Realzahlungen und Netzwerkrechte erfordern externe technische Sperren beziehungsweise manuelle, nachweisbare Entscheidung.

### Fehlermodi, Angriffe und Gegenpruefung

Arbeit an attraktiven Oberflächen kann existenzielle Sicherheitsblocker verdrängen. Daraus werden mindestens drei Negativtests abgeleitet: manipulierte Datenquelle, fehlende Berechtigung sowie eine veraltete oder widerrufene Evidenz. Die Pruefungen muessen auch dann blockieren, wenn Testdaten manipuliert sind oder ein Agent eine positive Formulierung behauptet. Ein separater Reviewer kontrolliert, ob Test und Produktivpfad denselben Kontrollpunkt durchlaufen.

### Abnahme mit messbarer Definition of Done

In jedem Sprint wird nach negativen Tests, Belegabdeckung und Nutzbarkeit statt Featurezahl priorisiert. Die Abnahmeakte dokumentiert Testdatum, Version, verantwortliche Person, Abweichungen und den Soll-Zustand nach einem Rollback. PASS_INTERNAL bedeutet einen eigenen nachgewiesenen Test; EXTERNAL_ATTESTED wird ausschliesslich nach einer passenden unabhaengigen Bescheinigung im konkreten Geltungsbereich angezeigt. Die Definition of Done verlangt gepruefte Tastaturbedienung, keine sichtbaren Secrets und wiederholbare Tests.

### Szenario, Rollout und Leitentscheidung

Sprint 1 beseitigt irreversible Risiken; Sprint 2 verbessert die Bedienung; Sprint 3 skaliert Integrationen. Zunaechst wird der Ablauf im synthetischen Demonstrationsmodus gezeigt, danach im isolierten Review-Bereich mit freigegebenen Artefakten. Erst nach erfolgreichem Vertrags-, Risiko- und Datenschutzreview wird er als Produktions-Feature sichtbar. Der Release sollte eine Klartextanzeige enthalten: welcher Commit, welches Gate, welche Rolle und welche Geltungsdauer die jeweilige Aussage tragen.

