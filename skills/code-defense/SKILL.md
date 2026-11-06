---
name: code-defense
description: Automatische Code-Analyse, AST-Syntaxcheck, Obfuskations-Validierung und Anti-Copy Feuermelder-Schutz.
version: 1.0.0
author: Daniel Pohl
frameworks: [Fail-Closed Security, Obfuscation & DRM]
---

# HCOS Code Defense & Obfuscation Guard Skill

## Zweck & Kompetenzen
Kontrolliert die physische Integritaet und den Quellcode-Schutz:
- **Obfuskations-Verifikation:** Sicherstellung, dass im Auslieferungsverzeichnis (`dist/`) kein Klartext-JavaScript sichtbar ist.
- **Fail-Closed Boundaries:** Pruefung von Pfaden auf Directory-Traversal-Angriffe (`guard_path`).
- **Feuermelder-Alarm:** Loest bei Kopiervorgaengen den Theatervorhang und die Alarmsirene aus.
