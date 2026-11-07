# Architecture 14: Automated PR Code Review, SAST/DAST & AST Security Stack

**Dokumenten-Klassifikation:** Technische Sicherheitsarchitektur & Review-Pipeline  
**Souveräner Urheber & Provenienz:** Daniel Pohl · Royal Kaiser Charter RegSys  
**Geltungsbereich:** HCOS TITAN / 20 Core Security Tools / SAST / DAST / AST Structural Refactoring / AI Code Review  
**Rechtsstatus & Identifikatoren:** PIC 867679357 & 873042778 · LEI 894500GBJSIW8L6ET310 · EORI AEOF139420 · UNGM 1172700 · USt-IdNr. DE31353063511 & DE441892129 · D-U-N-S 315676980 & 317066336 · Swiss AHV 756.6199.0539.28  

---

## 1. Motivation & Strategische Positionierung

Im Zeitalter autonomer Softwareentwicklung und KI-gestützter Codegenerierung (z.B. Devin AI, Cursor, Codex) stellt die lückenlose Verifikation von Pull Requests (PRs) das zentrale Nadelöhr für Systemstabilität und Angriffsresistenz dar.

Fehlerhafte Halluzinationen, unbemerkte Dependency-Confusion-Angriffe, versehentlich committete Geheimnisse oder architektonische Drift müssen **vor dem Merge in den Main-Branch** zuverlässig und automatisiert eliminiert werden.

Der **HCOS TITAN 20-Tool Review Stack** konsolidiert modernste statische Analyse (SAST), Container-/Infrastruktur-Sicherheit (IaC), AST-Strukturtransformation und generative KI-Reviewer zu einer geschlossenen, fail-closed Sicherheitsmauer.

---

## 2. Die Vier Säulen der Code-Review-Architektur

```
+-----------------------------------------------------------------------------------+
| 1. SEMANTISCHE & STRUKTURELLE AST-ANALYSE                                         |
|    - Semgrep (Semantische Regeln) | ast-grep & Tree-Sitter (AST-Suche)           |
|    - Joern (Code Property Graphs) | Rerast (Rust AST Transformation)              |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
| 2. SPRACH- & CONTAINER-SPEZIFISCHE LINTER                                         |
|    - Bandit (Python SAST) | Hadolint (Dockerfile AST)                             |
|    - Kube-Linter (Kubernetes/Helm) | Spectral (OpenAPI/AsyncAPI) | Buf (Protobuf) |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
| 3. VULNERABILITY- & INFRASTRUCTURE-AS-CODE SCANNER                                |
|    - Trivy (Container, SBOM, CVEs) | Checkov (IaC Policies: Terraform/K8s)       |
|    - Reviewdog (PR Feedback Bot)   | Cover-Agent (Automatische Unit-Tests)        |
+-----------------------------------------------------------------------------------+
                                         │
                                         ▼
+-----------------------------------------------------------------------------------+
| 4. GENERATIVE AI CODE REVIEW & VISUALISIERUNG                                     |
|    - PR-Agent (KI Diff-Analyse & Summaries) | Kodus-AI (Automatisierte Patches)   |
|    - Graphviz & PlantUML (Architektur- & Flussdiagramme)                          |
|    - OpenReview (Akademischer Peer-Review Standard)                               |
+-----------------------------------------------------------------------------------+
```

---

## 3. Tool-Matrix & Rollenverteilung (20 Kernwerkzeuge)

1. **Semgrep (CR-01):** Semantische Mustersuche für Sicherheitslücken ohne AST-Compiler-Overhead.
2. **Trivy (CR-02):** Tiefenscan von Dateisystemen, Container-Layern, OS-Paketen und SBOMs.
3. **Checkov (CR-03):** Durchsetzung von CIS-Benchmarks und Best Practices für Terraform und Kubernetes.
4. **ast-grep (CR-04):** Strukturierte Suche und Refactoring auf Basis konkreter Syntaxbäume.
5. **Bandit (CR-05):** Python-spezifischer Sicherheitsanalysator gegen `eval`, `shell=True`, unsichere Deserialisierung.
6. **Hadolint (CR-06):** Verhindert Root-Benutzer in Containern und unsichere Cache-Muster in Dockerfiles.
7. **Kube-Linter (CR-07):** Erzwingt Least-Privilege und Ressourcenlimits in Cloud-Native Manifesten.
8. **Spectral (CR-08):** Sichert konsistente, typensichere REST- und RPC-Schnittstellen.
9. **PR-Agent (CR-09):** KI-gestützte PR-Zusammenfassungen, Code-Smell-Erkennung und Risiko-Bewertungen.
10. **Kodus-AI (CR-10):** Generiert einsatzbereite Pull-Request-Korrekturen und Security-Fixes.
11. **Joern (CR-11):** Pfadanalyse für Taint-Tracking und Zero-Day Vulnerability Research.
12. **Cover-Agent (CR-12):** Erhöht automatisiert die Testabdeckung für geänderte Code-Bereiche.
13. **Reviewdog (CR-13):** Postet Diagnosen direkt an die betroffenen Codezeilen im GitHub-Diff.
14. **Buf (CR-14):** Verhindert Breaking Changes in gRPC- und Protocol-Buffer-Definitionen.
15. **Tree-Sitter (CR-15):** High-Speed Parsing für präzise Syntax-Hervorhebung und Navigation.
16. **PlantUML (CR-16):** Automatische Dokumentation von Sequenz- und Komponentendiagrammen.
17. **Graphviz (CR-17):** Erzeugt Abhängigkeitsgraphen und Kontrollflussdiagramme.
18. **OpenReview (CR-18):** Offene Gutachten- und Peer-Review-Strukturen für wissenschaftliche Validität.
19. **Rerast (CR-19):** Syntax-getreues Refactoring für systemnahen Rust-Code.
20. **Awesome-AI-Review (CR-20):** Wissensbasis führender KI-basierter Evaluierungsalgorithmen.

---

## 4. Integration in die 13 HCOS TITAN Assurance Gates

Die 20 Tools sind fest an die existierenden Sicherheits-Gates gekoppelt:
- **Gate G01 (License & Threat Review):** Trivy & Semgrep Lizenz- und Schwachstellenscans.
- **Gate G02 (Build Plan):** Graphviz & Buf DAG- und Schnittstellen-Validierung.
- **Gate G06 (Unit & Integration Tests):** Cover-Agent & Bandit Test- und Code-Checks.
- **Gate G07 (Adversarial Verification):** Joern Pfadanalyse gegen Injection- und Eskalations-Pfade.
- **Gate G09 (Approval):** Zusammenfassungen via PR-Agent zur finalen Genehmigung durch Daniel Pohl.
