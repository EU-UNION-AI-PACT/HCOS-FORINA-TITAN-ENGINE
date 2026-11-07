# Architecture 07 — EZB Pontes & DLT Wholesale Settlement: Technische Interoperabilität und Zentralbankgeld-Finalität

**Dokument-ID:** ARCH-SPEC-07-EZB-PONTES-DLT-WHOLESALE  
**Sovereign Provenance & Urheber:** Daniel Pohl · Royal Kaiser Charter RegSys  
**Rechtliche Registrierungen & Identifikatoren:**  
- EU Transparency & Research: PIC 867679357 & 873042778  
- Steuerliche Identifikation: USt-IdNr. DE31353063511 & DE441892129  
- Unternehmensidentifikatoren: D-U-N-S 315676980 & 317066336 · Global LEI 894500GBJSIW8L6ET310  
- Internationale Register: UNGM 1172700 · EORI AEOF139420 · Swiss AHV 756.6199.0539.28  
- Akademische Register: ORCID 0009-0004-0348-9769 · Scopus EX2025D1143002  
**Lizenz:** European Union Public Licence (EUPL-1.2) · Sovereign Fail-Closed Boundary  
**Klassifizierung:** KANONISCHES INSTITUTIONELLES FINANZARCHITEKTURPAPIER (HCOS v2.16)  

---

## 1. Einordnung & Fragestellung

Die Integration von Distributed Ledger Technologie (DLT) in die europäische Finanzmarktinfrastruktur erfordert eine präzise technische und begriffliche Differenzierung:
- **Zentralbankgeld** ist eine direkte Verbindlichkeit des Eurosystems (EZB / nationale Zentralbanken) und bietet risikofreie Finalität.
- **Geschäftsbankgeld** und private Stablecoins stellen Gläubigerforderungen an private Institutionen dar und bergen Gegenparteirisiken.
- **Pontes** fungiert als konzeptionelle und technische **Interoperabilitätsbrücke** zur Koordinierung von Wertpapier-Lieferungen auf marktseitigen DLT-Netzwerken mit der Geldverrechnung in Zentralbankgeld über TARGET-Dienste.

---

## 2. Die drei Eurosystem-Erprobungslösungen (Trials 2024–2026)

Im Rahmen der EZB-Erkundungsphase für neue Technologien zur Abwicklung von Großbetragszahlungen wurden drei interoperable Lösungsansätze getestet:

```
[ Marktseitige DLT-Plattform (Asset-Leg) ]
               |
               v
+-----------------------------------------------------------+
|               INTEROPERABILITÄTS-EBENE                    |
|                                                           |
| 1. Trigger Solution (Bundesbank)                          |
|    - API / Protokoll-Trigger verbindet DLT mit T2-RTGS    |
|                                                           |
| 2. Full DLT Interoperable Ledger (Banque de France)       |
|    - DL3S Cash-Ledger erzeugt wCBDC-Token                 |
|                                                           |
| 3. TIPS Hash-Link (Banca d'Italia)                        |
|    - Kryptografischer Hash-Link verbindet Instant Payment |
+-----------------------------------------------------------+
               |
               v
[ Eurosystem TARGET Services: T2 (RTGS) / T2S / TIPS ]
```

### 1. Trigger Solution (Deutsche Bundesbank)
- **Funktionsweise:** Die Wertpapierseite (Asset Leg) verbleibt auf einer zugelassenen externen DLT-Plattform. Ein technischer Trigger initiiert die finale Geldbuchung im klassischen RTGS-System T2.
- **Vorteil:** Keine Schaffung neuer tokenisierter Geldformen; vollständige Kontinuität der bewährten Zentralbankgeld-Garantie.

### 2. DL3S Interoperable Cash Ledger (Banque de France)
- **Funktionsweise:** Bereitstellung eines eigenständigen, interoperablen DLT-Knotens, auf dem digitales Zentralbankgeld als Token (Wholesale CBDC) abgebildet wird.
- **Vorteil:** Ermöglicht atomare Abwicklungen (Atomic Settlement) direkt zwischen zwei DLT-Netzwerken via Hashed Timelock Contracts (HTLC).

### 3. TIPS Hash-Link (Banca d'Italia)
- **Funktionsweise:** Kopplung der DLT-Marktinfrastruktur an den europäischen Echtzeit-Zahlungsverkehrsdienst TIPS über kryptografische Hash-Link-Zusagen.
- **Vorteil:** 24/7/365 Verfügbarkeit und Sekunden-Finalität für Groß- und Interbankenzahlungen.

---

## 3. Globale Vergleichsprojekte & BIZ-Initiativen

Die Pontes-Architektur fügt sich nahtlos in die weltweite Forschungs- und Standardisierungslandschaft ein:
- **Project Helvetia (SNB / BIZ):** Echte Abwicklung tokenisierter Anleihen auf der SIX Digital Exchange (SDX) mit Wholesale CBDC der Schweizerischen Nationalbank.
- **Project Jura (BdF / SNB / BIZ):** Grenzüberschreitende DvP- und PvP-Abwicklung zwischen dem Eurosystem und der Schweiz.
- **Project Agorá (BIZ):** Öffentlicher-privater Verbund zur Schaffung programmierbarer Finanzinfrastrukturen mit Geschäftsbanken und Zentralbanken.
- **Project mBridge (BIZ / Asien / Nahost):** Mehrwährungs-Plattform mit eigenem Konsens-Ledger für grenzüberschreitende Außenhandelsabrechnungen.

---

## 4. Technische Implementierung in HCOS FORINA TITAN

In der HCOS-Engine wird die Pontes-Schnittstelle über das Modul `PontesDltSettlementEngine` implementiert:
1. **Rechercheregister:** 25 verifizierte DLT- und CBDC-Systeme in `docs/catalogs/EZB_PONTES_DLT_RECHERCHEMATRIX.csv`.
2. **REST API:** Endpunkte `/api/finance/pontes/matrix` und `/api/finance/pontes/summary`.
3. **CLI:** `python3 forina.py finance pontes-matrix`.
4. **Assurance Gate Alignment:** Konformität mit BSI TR-03105, ISO 20022 und BIZ DvP-Standards.
