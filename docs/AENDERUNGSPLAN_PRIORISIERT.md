# HCOS FORINA TITAN · priorisierte Implementierungs-Roadmap

Stand 06.11.2026, Ausgangspunkt v1.7.0. Ohne Installation, Host-Aenderung oder Produktionsdaten.

## P0 · Sicherheitswahrheit (vor automatischer Freigabe)

1. G03: Unabhaengige No-Egress-Erzwingung ausserhalb der Python-Anwendung, kein Fallback ohne beweisbare Isolation.
2. G12: Archiv-Pfadvalidierung mit `is_relative_to`, deny by default, kein unsicherer `extractall`-Fallback; SHA aller extrahierten Dateien gegen vertrauenswuerdiges Manifest.
3. G08: Gegen Seiteneffekte, Ueberschreiben und Pfadtraversal abgesichertes signiertes Inventar; keine Rueckfall-Pfade.
4. Gate-Frontend: Ergebnis dynamisch aus authentisierter Backend-Evidence; UNKNOWN/EXPIRED nicht gruen darstellen.
5. Finanz-Connectoren: API-Scopes auf Providerseite read-only; echtes Payment strikt ausserhalb des Analysemoduls.

## P1 · IA/XD, Katalog und Rechte

6. Navigation nach Aufgaben statt Dateinamen; einheitliche Design-Tokens und WCAG-2.2-Pruefungen.
7. Vollstaendige URL-Validierung: nur explizit zugelassene HTTPS-Hosts, `URL`-Parser, sichere DOM-Methoden.
8. License/Security-Claims nur mit konkreter Version, Originalquelle, Reviewer und Evidenzdatum.
9. Rollen, Consent und Widerruf als zentrale Policies; getrennte Finanz-/Web3-Zonen.

## P2 · Release und Zertifizierungs-Vorbereitung

10. Signed Release Manifest mit SBOM, Provenienz, SAST/DAST und reproduzierbarem Build.
11. Normen-Mapping mit Geltungsbereich, Legal Review, internen Badges und nachweisbaren Drittzertifikaten.
12. Harness Loop mit Iterationslimit, Budget, unabh. Testoracle, Pause und expliziter Human Approval.

**Wichtig:** Kein Projekt gilt als extern zertifiziert, allein weil interne Gates gruen melden.
