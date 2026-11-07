# MASTERPLAN — DP MASTERBOOK

**Dokument-ID:** DP-DOC-BOOK-0001 · **Version:** v2.6
**Konzeptgeber:** Daniel Pohl · **Erstellt:** 20.10.2026
**Lizenz:** EUPL-1.2 (soweit eigene schöpferische Bestandteile enthalten sind)

---

## 1. Ziel

Das **DP Masterbook** ist die Meta-Publikation aller Konzepte von Daniel Pohl:
ein mehrschichtiges Publikationssystem — **indexiert, gewoben, cross-referenziert** —
das die wichtigsten Konzepte in einem einheitlichen Buch-Format bündelt.

**Zielzustand:** Ein vollständiges, lückenloses Buch aus den neun Quelldokumenten
(DOC-001 … DOC-009), mit exakten Seitenzahlen von 1 bis Ende.

---

## 2. Ist-Zustand (v2.6 — 20.10.2026)

### 2.1 Was integriert ist

| Teil | Inhalt | Umfang | Status |
|------|--------|--------|--------|
| **Teil I** | 27 kuratierte Konzepte (Volltext) | 15.994 Wörter · ~46 S. | ✅ |
| **Teil II** | Index C (Kapitel-Index + Statistik) | ~5 S. | ✅ |
| **Teil III** | Querverweis-Matrix (96 Kanten) | ~3 S. | ✅ |
| **Teil IV** | Quellenverzeichnis + Methodik | ~2 S. | ✅ |
| **Teil V** | 133 Roh-Konzepte (Volltext) | 478.148 Wörter · ~1.366 S. | ✅ |
| **Teil VI.A** | DOC-004 PNIA-Korpus (Index) | 115 Dateien · ~140 S. | ✅ (Volltext in Teil VII) |
| **Teil VI.B** | DOC-005 Rota-Vatican-Korpus (Index) | 951 Dateien · 17 Bereiche · ~4.490 S. | ✅ (Volltext in Teil VII) |
| **Teil VI.C** | DOC-007 Finance-Korpus (Index) | 176 Dateien · ~152 S. | ✅ |
| **Teil VII** | Rota-Vatican-Konzepte (Volltext, 17 Bereiche) | 428 Dokumente · 3.120.567 Wörter · ~8.918 S. · 21 Archive entpackt | ✅ |

**Gesamt (verfügbar):** 1.830 Dateien · 5.288.372 Wörter · ~15.137 Seiten

### 2.2 Die neun Quelldokumente (Meta-Struktur)

| ID | Quelle | Erwartet | Verfügbar | Status |
|----|--------|----------|-----------|--------|
| DOC-001 | Eid-und-Sechserstruktur.pdf | — | ✅ | → Konzept 17 |
| DOC-002 | Gesegnete Weihnacht — Krönung der Konzepte.html | — | ⚠️ | Original |
| DOC-003 | Buchstrukturkonzept erstellen.md | — | ⚠️ | Original |
| DOC-004 | PNIA-Korpus | 259 Dateien | ✅ 259 (in DOC-005) | → Teil VII (RV-01) |
| DOC-005 | Rota-Vatican-Korpus | 2.769 Dateien (Meta) | ✅ 951 (vollständig) | → Teil VII (Volltext) |
| DOC-006 | Präsentation Banknoten | — | ⚠️ | Original |
| DOC-007 | Finance-Konzept | 85 Dateien | ✅ 176 | → Teil VII (RV-02) |
| DOC-008 | Copyright/Licence/Trademark | — | ✅ | → Konzept 16 |
| DOC-009 | (weitergeführt) | — | ⚠️ | Original |

**Wichtige Erkenntnis:** Das Rota-Vatican-Korpus (DOC-005) ist das **übergeordnete
Gesamtkorpus**. Sein Bereich `01_PNIA_Concept` enthält genau 259 Dateien — das
PNIA-Korpus (DOC-004) — und `02_Finance_Concept` 108 Dateien. PNIA und Finance
sind Teilbereiche des Rota-Vatican-Korpus.

**Bewertung:** Teil I (27 Konzepte), Teil V (133 Roh-Konzepte), alle drei
Vollkorpora (Teil VI, Index) und **alle Rota-Vatican-Konzepte als Volltext
(Teil VII, 428 Dokumente, 21 Archive entpackt)** sind integriert. **Konzept 27** (Souveränes
Resonanz-Kommunikationsprotokoll) wurde aus einem verwaisten PDF
(`KONZEPT_Souveraene_Kommunikation.pdf`) extrahiert und als 27. kuratiertes
Konzept in Teil I aufgenommen. Offene Punkte: DOC-005 hat 951 von
2.769 Dateien (Meta-Angabe); im vorliegenden Korpus und im GitHub-Repo
(T1m32H1FT2L0WcL0cKFr33Zy/EU-UNION-AI-PACT-Z3r0CL0cK, main + test/gpg-verify +
alle lokalen Branches + Releases/Tags geprüft) existieren nur 951 Dateien —
**alle 951 sind zu 100 % integriert**. Die übrigen 1.818 liegen weder lokal
noch im Repo vor. DOC-002/003/006/009 sind als Einzel-Originale noch zu
lokalisieren.

---

## 3. Buch-Architektur

```
DP MASTERBOOK/
├── MASTERPLAN.md                  ← dieses Dokument
├── DP_MASTERBOOK.md               ← Hauptbuch (Frontmatter, TOC, Teil I–VII)
├── INDEX.md                       ← Kurzindex + Statistik
├── TEIL_I_KONZEPTE/               ← 27 Kapitel (Volltext)
├── TEIL_V_ROH_KONZEPTE/           ← 133 Roh-Konzepte (Volltext)
├── TEIL_VI_VOLLKORPORA/           ← 3 Korpus-Indizes (PNIA, Rota-Vatican, Finance)
└── TEIL_VII_ROTA_VATICAN/         ← 17 Bereichs-Volltexte (RV-00 … RV-17)
```

### Buch-Aufbau

| Teil | Inhalt | Form |
|------|--------|------|
| **Frontmatter** | Titel, Vorwort, 9 Quelldokumente, Inhaltsverzeichnis | inline |
| **Teil I** | Die 27 Konzepte (je ein Kapitel) | Volltext (inline + Files) |
| **Teil II** | Index C: Konzept-Indizes + Statistik | inline |
| **Teil III** | Querverweis-Matrix (96 Kanten) | inline |
| **Teil IV** | Quellenverzeichnis + Methodik | inline |
| **Teil V** | Die 133 Roh-Konzepte | Volltext (Files) + Index (inline) |
| **Teil VI** | Die Vollkorpora (DOC-004/005/007) | Datei-Index (Files) + Übersicht (inline) |
| **Teil VII** | Die Rota-Vatican-Konzepte (17 Bereiche) | Volltext (Files) + Index (inline) |

**Seitenzahlen:** Jedes Kapitel/Konzept trägt eine kumulative Seitenzahl
(Beginn S. N), berechnet auf Basis von 350 Wörtern/Seite.

### Teil VII — Rota-Vatican-Konzepte (Volltext)

| # | Bereich | Dokumente | Wörter | ~Seiten | Archive |
|---|---------|-----------|--------|---------|---------|
| 01 | PNIA_Concept | 77 | 185.555 | ~530 | 3 |
| 02 | **Finance_Concept** | 53 | 280.478 | ~801 | 3 |
| 03 | Kochen_Geschirr_3D_Druck_Essen | 1 | 36.263 | ~104 | 0 |
| 04 | Krankenhaus_Altersvorsorge_Rentenversicherung | 10 | 206.006 | ~589 | 0 |
| 05 | Life_PACT | 1 | 943 | ~3 | 0 |
| 06 | Schule_Notendruck_Ueberarbeitung | 1 | 943 | ~3 | 0 |
| 07 | Universum_Frequenz | 46 | 1.781.829 | ~5.091 | 15 |
| 08 | Muellentsorgung | 1 | 36.263 | ~104 | 0 |
| 09 | JVA_2_Chance_Streetworker | 1 | 943 | ~3 | 0 |
| 10 | LilLIT | 3 | 38.088 | ~109 | 0 |
| 11 | Satelliten | 3 | 81.654 | ~233 | 0 |
| 12 | Friedens_Militaer_Concepte | 47 | 98.816 | ~282 | 0 |
| 13 | Vatican_Kathedrale_Glaubensgemeinschaft | 0 | 0 | ~0 | 0 |
| 14 | Suchergebnisse_Conversation_Copy | 1 | 1.622 | ~5 | 0 |
| 15 | International_Institutionen_Kontakte | 135 | 5.806 | ~17 | 0 |
| 16 | sYcSTarTs_Concept | 43 | 295.771 | ~845 | 0 |
| 17 | SystemINFO_Profil | 4 | 69.573 | ~199 | 0 |
| 00 | (root) Peace Buildings | 1 | 14 | ~0 | 0 |
| — | **Gesamt** | **428** | **3.120.567** | **~8.918** | **21** |

> **Hinweis:** Die Dokumentenzahl ist gegenüber v2.3 gesunken, weil doppelte
> Inhalte (identische Dateien an mehreren Stellen / in Archiven) jetzt per
> Content-Hash **dedupliziert** werden. Die Wörterzahl ist gestiegen, weil die
> **21 Archive (ZIP/TAR.GZ, inkl. verschachtelter)** entpackt und ihr Inhalt
> eingepflegt wurde (v. a. RV-07 „Heilige Orte"-Kataloge).

**Eingepflegt:** alle md/txt/html-Konzepte + per `pdftotext` bzw. ZIP/XML-Extraktion
gewonnene PDF/DOCX/PPTX-Dokumente. **Nicht eingepflegt** (Code/Binär/leer):
310 Dateien — am Ende jedes Bereichs gelistet.

---

## 4. Roadmap zur Vollständigkeit

### Phase 1 — ✅ Rekonstruktion (erledigt, 20.10.2026)
- [x] History-Durchsuchung (DP Masterbook, 27 Konzepte, Seitenzahlen)
- [x] Ableger-Modus (Originale read-only, Verarbeitung im isolierten Ableger)
- [x] Scan: 133 Roh-Konzept-Dateien (~1.366 Seiten)
- [x] Buch-Assembly: 27 Kapitel + Index C + Querverweis-Matrix + Quellenverzeichnis
- [x] Masterplan

### Phase 2 — ✅ Andere Konzepte + Vollkorpora integrieren (erledigt, 20.10.2026)
- [x] Teil V: 133 Roh-Konzepte als Volltext-Kapitel integriert
- [x] Teil VI.A: DOC-004 PNIA-Korpus (115 Dateien) als Datei-Index integriert
- [x] Teil VI.B: DOC-005 Rota-Vatican-Korpus (951 Dateien, 17 Bereiche) integriert
- [x] Teil VI.C: DOC-007 Finance-Korpus (176 Dateien) als Datei-Index integriert
- [x] Erkenntnis: PNIA (259 Dateien) ist Teilbereich des Rota-Vatican-Korpus

### Phase 3 — ✅ Alle Rota-Vatican-Konzepte als Volltext einpflegen (erledigt, 20.10.2026)
- [x] Teil VII: alle 17 Bereiche als Volltext (428 Dokumente, ~8.918 S.)
- [x] Teil VII: 21 Archive (ZIP/TAR.GZ, inkl. verschachtelter) entpackt & eingepflegt, Inhalte dedupliziert
- [x] **Finance-Konzepte (RV-02)** vollständig eingepflegt (57 Dokumente, ~844 S.)
- [x] PDF/DOCX/PPTX-Dokumente per Extraktion eingepflegt
- [x] Lücken-Check: alle Bereiche geprüft, keine Konzept-Texte mehr offen
- [x] Nicht einpflegbare Dateien (Code/Binär) pro Bereich gelistet

### Phase 4 — Lücken schließen
- [x] DOC-005 Rota-Vatican: GitHub-Repo + alle lokalen Ordner geprüft (20.10.2026) — die 1.818 „fehlenden" Dateien existieren weder im Repo (main, test/gpg-verify, alle Branches, Releases, Tags) noch lokal; 2.769 ist eine Meta-Angabe, der tatsächliche Korpus umfasst 951 Dateien, **alle integriert**
- [ ] DOC-002, DOC-003, DOC-006, DOC-009 lokalisieren & einbinden

### Phase 5 — Veredelung
- [ ] Exakte Seitenzahlen (1 bis Ende) über PDF-Render
- [ ] Vollständiges Register (Begriffe, Personen, Organisationen)
- [ ] Glossar aller Fachbegriffe (State-0, Wonnet, Master-Token, …)
- [ ] PDF-Export (LaTeX oder Pandoc) für die Druckfassung
- [ ] Merkle-Hash-Provenanz über das gesamte Buch

### Phase 6 — Publikation
- [ ] Versionierung (v2.3 → v2.4 → …)
- [ ] Release-Archiv (ZIP/TAR) mit Provenanz-Manifest
- [ ] Einbindung in das Repo (`docs/masterbook/`)

---

## 5. Integrität & Schutz

- **Originale unangetastet:** Alle angehängten Archive wurden read-only gelesen.
- **Ableger-Modus:** Verarbeitung ausschließlich im isolierten Ableger
  (`derivative_workspace/` im Session-Artefakt-Ordner).
- **Keine Datenlöschung:** Nur Hinzufügen, kein Entfernen.
- **Nachvollziehbarkeit:** Scan-Ergebnisse (`scan_result.json`, `korpora_scan.json`,
  `teil7_stats.json`) + Assembly-Skripte (`build_book.py`, `build_book_v2.py`,
  `build_teil7.py`) sind reproduzierbar.

---

## 6. Wichtige Begriffe

| Begriff | Bedeutung |
|---------|-----------|
| DP-DOC-BOOK-0001 | Dokument-ID des Masterbooks |
| v1.6 | Version des Original-Masterbooks (26.09.2026) |
| v2.0 | Erste Rekonstruktion (20.10.2026) |
| v2.1 | Rekonstruktion + PNIA/Finance-Korpora (20.10.2026) |
| v2.2 | Rekonstruktion + alle Vollkorpora inkl. Rota-Vatican (20.10.2026) |
| v2.3 | + Rota-Vatican-Konzepte als Volltext (Teil VII) (20.10.2026) |
| v2.4 | + Konzept 27 (Souveränes Resonanz-Kommunikationsprotokoll) aus verwaistem PDF (20.10.2026) |
| v2.5 | DOC-005-Lücke geklärt: GitHub-Repo + lokale Ordner geprüft, 951 = vollständiger Korpus (20.10.2026) |
| v2.6 | + 21 Archive (ZIP/TAR.GZ, inkl. verschachtelter) entpackt & eingepflegt, Inhalte dedupliziert (20.10.2026) |
| DOC-001…009 | Die neun Quelldokumente |
| Index C | Lokalisierung der Konzept-Indizes (Teil II) |
| Querverweis-Matrix | Cross-Referenzen zwischen Konzepten (Teil III) |
| Roh-Konzepte | 133 Konzept-Dateien jenseits der 27 kuratierten (Teil V) |
| Vollkorpora | Große Quelldokumente DOC-004/005/007 (Teil VI) |
| Rota-Vatican | Übergeordnetes Gesamtkorpus (enthält PNIA + Finance) |
| Teil VII | Rota-Vatican-Konzepte als Volltext (17 Bereiche) |
| Ableger-Modus | Read-only-Schutz der Originale |
| EUPL-1.2 | European Union Public Licence v1.2 |

---

## 7. Querverweise

- → Konzept 20 (DP Masterbook): `docs/konzepte/20-DP-Masterbook.md`
- → Konzept-Archiv: `docs/konzepte/INDEX.md` (163 Dateien, 92 eindeutige)
- → Session `c57282ef`: DP Masterbook PDF-Analyse (10.10.2026)
- → Session `53cc1e92`: ~1.006-Seiten-Analyse (20.10.2026)
