# UI UX – 01 UI UX Core Sliding Engine

**Autor:** Daniel Pohl | **Status:** Sovereign Specification

---

Part 1: UI/UX Core Concepts & Smooth Sliding Engine

Die Architektur der UI/UX & Module Engine

Dieses Dokument definiert die genauen Parameter, Technologien und normativen Vorgaben für das Frontend-Handling. Die 'Smooth Sliding Engine' ist nicht nur ein visuelles Gimmick, sondern das strukturierte, GPU-beschleunigte Herzstück, das entscheidet, wie Sub-Agenten, CLI-Tools (IHcT) und Web3-Transaktionen dem Nutzer präsentiert werden. Sie integriert sich lückenlos in den Act Pack Zero Clock Harness Loop und respektiert Dark Mode, Gold-Typografie und EU-Souveränität.

Konzept: Smooth Sliding Engine (Core)

Die Engine

Die Kernarchitektur der UI, die physikbasierte Animationen nutzt, um Übergänge zwischen Modulen reibungslos (60+ FPS) darzustellen.

Implementation: Modul-Handling

Umsetzung durch React Spring und Framer Motion. Jedes Modul (z.B. Finance-Dashboards) wird als Off-Canvas-Komponente geladen und gleitet GPU-beschleunigt in den Viewport.

Harness Loop Integration

Das UI-Harness misst die Frame-Drops während der Transition. Bei Frame-Drops > 5% wird automatisch das Wasm-Modul neu kompiliert.

Security & Web3

Verhindert UI-Redressing und Clickjacking durch strenge Shadow-DOM-Kapselung. Krypto-Transaktionen werden erst bei vollständig statischer UI freigegeben.

Konzept: WebGL Rendering Context

Technologie

Nutzt die Grafikkarte des Clients, um komplexe Finanzdaten, DLT-Graphen und Smart-Contract-Netzwerke in 3D zu visualisieren.

Implementation: Modul-Handling

Einbettung via Three.js. Module werden als native Canvas-Elemente über die Smooth Sliding Engine nahtlos in das 2D-DOM geblendet.

Harness Loop Integration

Automatisierte Shader-Kompilierungs-Tests im Loop. Fehlerhafte WebGL-Kontexte triggern einen Fallback auf SVG.

Security & Web3

Isolierung des WebGL-Kontexts vom Main-Thread. Schutz vor WebGL-basierten Fingerprinting-Attacken im Crypto-Umfeld.

Konzept: Hardware Acceleration (GPU)

Technologie

Auslagerung der UI-Berechnungen (Compositing, Sliding) von der CPU auf die GPU via CSS `transform` und `opacity`.

Implementation: Modul-Handling

Alle beweglichen Panels und Tools (z.B. das IHcT CLI Terminal) erzwingen GPU-Layer (`will-change: transform`).

Harness Loop Integration

Lighthouse- und Playwright-Performance-Tests im Loop verifizieren, dass das Compositing nicht durch Main-Thread-Blocking gestört wird.

Security & Web3

Verhindert Timing-Attacken auf Krypto-Wallets durch konstante Rendering-Zyklen unabhängig von der CPU-Auslastung.

Konzept: Framer Motion / Spring Physics

UI/UX Methode

Nutzung von Feder-Physik (Masse, Dämpfung, Steifigkeit) statt linearen Easing-Kurven für absolut natürliche Modul-Übergänge.

Implementation: Modul-Handling

Wenn Tools aufgerufen werden (z.B. Portfolio-Ansicht), gleiten sie mit berechneter Trägheit herein, was dem Nutzer haptisches visuelles Feedback gibt.

Harness Loop Integration

Der Loop validiert die Zustandssynchronisation zwischen React-State und Spring-Animation. Keine Hänger erlaubt.

Security & Web3

Sorgt für visuelle Eindeutigkeit bei kritischen Transaktionen (z.B. beim Signieren von Multisig-Contracts rutscht das Bestätigungs-Panel zwingend ins Zentrum).

Konzept: Virtual DOM Reconciliation

Technologie

Minimierung von direkten DOM-Manipulationen durch Berechnung von State-Diffs im Arbeitsspeicher.

Implementation: Modul-Handling

Ermöglicht das sofortige Umschalten zwischen dem Act Pack Zero Clock Dashboard und dem LEG-Nebenkosten-Modul ohne Page-Reload.

Harness Loop Integration

Automatisierter Test auf unnötige Re-Renders. Das UI-Harness bricht den Build ab, wenn ein Modul-Update das gesamte DOM invalidiert.

Security & Web3

Schützt vor DOM-basiertem XSS (Cross-Site Scripting), da Datenströme aus der Blockchain nicht direkt als HTML interpretiert werden.

Konzept: Shadow DOM Encapsulation

Technologie

Kapselung von CSS und HTML, sodass UI-Komponenten (Widgets, Tools) komplett isoliert vom Rest der App laufen.

Implementation: Modul-Handling

Drittanbieter-Tools (z.B. Enable Banking Widget) können in die Smooth Sliding Engine integriert werden, ohne das Dark Mode Gold (#FFD700) Styling zu zerstören.

Harness Loop Integration

Der Vulnerability Scan prüft, ob Shadow-Boundaries durchbrochen wurden (CSS-Leaking).

Security & Web3

Kritisch für Web3: Verhindert, dass bösartige Scripts von Dritt-Modulen auf den Speicherbereich der Crypto-Keys im Main-DOM zugreifen.

Konzept: Micro-Interactions

UI/UX Methode

Subtile, zweckgebundene Animationen (z.B. Hover-Effekte, Loading-States, Success-Ticks) zur Steuerung des Nutzerfokus.

Implementation: Modul-Handling

Jeder Klick in der Werkzeugleiste löst ein mikroskopisches physikalisches Feedback aus. Tools rasten spürbar (visuell) ein.

Harness Loop Integration

Visual Regression Tests (Cypress) vergleichen Frame-by-Frame, ob die Micro-Interactions den CI/CD-Standards entsprechen.

Security & Web3

Geben sofortiges visuelles Feedback bei der Validierung von Zero-Knowledge-Proofs (z.B. ein fließender Übergang von Rot nach Gold).

Konzept: Dark Mode (#121212) & Gold (#FFD700)

UI/UX Ästhetik

Die definierte CI/CD-Ästhetik der Plattform. Tiefes Schwarz für Kontrast und Datensouveränität, Gold für aktive, verifizierte Zustände.

Implementation: Modul-Handling

Die Smooth Sliding Engine nutzt CSS-Variablen. Beim Wechsel zwischen Modulen bleiben die Farb-Tokens global synchronisiert.

Harness Loop Integration

Color-Contrast-Automatisierung: Der Loop prüft nach WCAG 2.1 AAA, ob Gold auf Schwarz den nötigen Kontrastwert (7:1) erfüllt.

Security & Web3

Psychologische Sicherheit: Nutzer erkennen authentische System-Prompts sofort an der strengen, unveränderlichen Farb-Codierung.

Konzept: Cognitive Load Reduction

UI/UX Strategie

Design-Philosophie, die darauf abzielt, die geistige Beanspruchung des Nutzers bei komplexen Aufgaben (wie DLT-Audits) zu minimieren.

Implementation: Modul-Handling

Module öffnen sich nie überlappend im Chaos, sondern verdrängen sich sanft (Sliding Engine). Nur die akut relevanten Tools sind sichtbar.

Harness Loop Integration

KI-Agenten (Devin) analysieren die UI-Metriken im Loop und schlagen Layout-Vereinfachungen vor, falls zu viele Elemente gleichzeitig aktiv sind.

Security & Web3

Senkt die Wahrscheinlichkeit von menschlichen Fehlern (Fat-Finger-Errors) beim Routing von Millionen-Beträgen über Smart Contracts.