# HCOS FORINA TITAN · ARCHITEKTUR & PIPELINE ENGINE

## Pipeline-Architektur

```mermaid
flowchart TD
    A["Tool Build Processing Spec\n(8 Kern-Module)"] --> B["Preflight Gate & Integrity Check"]
    B --> C["Automatisches Source-Backup\n(tar.gz Zeitstempel)"]
    C --> D["PWA & Web-Kompilierung\n(HTML5 / CSS3 / JS)"]
    D --> E["Code-Obfuskation & Kopierschutz"]
    E --> F["Live Spec-Sync Radar\n(Light Blink Buttons & Glow Points)"]
    F --> G["AppDir Staging & ZIP Release"]
    G --> H["Local Engine Web Server & OTA Gateway"]
```

## Schichtenmodell

1. **Präsentations-Ebene (`web/`):**
   - Titan-Design, metallische Farbverläufe, GSAP-Animationsabläufe, Three.js Effekte.
   - Offline-First PWA mit Service Worker (`sw.js`) und Web-Manifest.
   - Interaktive Light Blink Buttons und Statistic Glow Points.
2. **Engine & Pipeline-Ebene (`forina_engine/`):**
   - Deterministischer Build-Orchestrator (`engine.py`).
   - Spezifikations-Parser und Live-Sync Verifizierer (`spec_sync.py`).
   - Unified HTTP/API Server (`server.py`).
3. **Infrastruktur & Routing (`config/`):**
   - Caddy & NGINX Reverse Proxy Konfigurationen mit automatischer DNS-Auflösung via sslip.io / nip.io.
4. **Compliance & Nachweisführung (`releases/`, `docs/`):**
   - SHA-256 Prüfsummen-Inventar.
   - Audit Evidence JSON Berichte.
