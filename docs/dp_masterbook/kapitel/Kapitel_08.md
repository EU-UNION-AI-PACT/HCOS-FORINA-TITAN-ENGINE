# Konzept 08 — FinanceDr.Strange: Self-Hosted PaaS

**Kurzname:** „FinanceDr.Strange New Structur“ — dezentrale Self-Hosted PaaS
**Dateien:** `FinanceDr.Strange New Structur.pdf` (×2, identisch)

---

## 1. Grundidee

Aus einem Chat-Dialog: Ein Agent, der automatisch bei Hinzufügen von Repositories auf
**GitHub, Hugging Face oder GitLab** (auch Radicle, externe GitHub-B2B-Server) die Programme
und Open-Source-Connectionen durchreicht und **automatisch Bildprozesse/Deployments startet** —
ohne IDE, ohne Netlify, nur durch das reine Dasein von Forks.

> „Was du beschreibst, ist im Grunde die Architektur einer eigenen, dezentralen Self-Hosted
> PaaS (Platform as a Service) — ähnlich wie ein maßgeschneidertes, leichtgewichtiges
> Equivalent zu Vercel, Netlify oder Coolify, erweitert um Multi-Source-Quellen und
> dateibasierte oder webhook-gesteuerte Trigger.“

## 2. Die vier Komponenten

| Komponente | Beschreibung |
|------------|--------------|
| **Registry & Ingestion Layer** | Webhooks (GitHub/GitLab API) ODER eine zentral überwachte **Markdown-Datei** (`repositories.md`) auf einem großen Storage-Pool (z. B. QCOW2-VHD / ZFS, **111 TB**), in die neue Repositories eingetragen oder per Sync-Job geschrieben werden |
| **Storage & Workspace** | Massiver Storage-Bereich, in dem die Repositories als Bare-Klone oder Arbeitsverzeichnisse landen |
| **Build & Execution Engine** | Daemonisierter Agent (Python oder Go), der Änderungen erkennt, automatisch Container (Docker/Podman) oder statische Builds erzeugt |
| **Dynamic Routing & Tunneling** | Reverse Proxy (vorzugsweise **Caddy** — exzellente API, automatische TLS/Wildcard-Handhabung) + Wildcard-DNS wie **sslip.io** oder **nip.io** (z. B. `projektname.192-168-1-50.sslip.io`) — Side-by-Side-Umgebungen ohne manuelles Nginx-Reloading |

## 3. Der Deployment-Agent (Python-Prototyp)

Vollständiger Python-Prototyp im Dokument:
- Überwacht `WATCHED_MD_FILE = "/mnt/storage/repositories.md"`
- Parst Markdown-Links `[Name](URL)` per Regex
- Klont Repositories nach `WORKSPACE_DIR` (oder aktualisiert)
- Startet Docker-Container via `docker.from_env()`
- Verwaltet die Ports dynamisch

```python
def parse_repositories_md(file_path):
    """Liest Repositories aus einer Markdown-Datei (z.B. [Name](URL))."""
    matches = re.findall(r'\[(.*?)\]\((https?://[^\s]+)\)', content)
    ...
```

## 4. Deployment-Varianten

- **Fork Deployment**
- **Side-by-Side-Stellung** durch NIP oder IO
- **SSL-Lib** als Wait-Style
- Durchreichung durch **Caddy oder Nginx** als Tunnelvariante
- Automatisches Deployment

## 5. Wichtige Begriffe

| Begriff | Bedeutung |
|---------|-----------|
| Self-Hosted PaaS | Eigene Plattform-as-a-Service (Vercel/Netlify/Coolify-Äquivalent) |
| repositories.md | Markdown-Datei als Trigger-Registry |
| QCOW2-VHD / ZFS | Storage-Formate für den 111-TB-Pool |
| Caddy | Reverse Proxy mit automatischer TLS/Wildcard-Handhabung |
| sslip.io / nip.io | Wildcard-DNS-Dienste |
| Side-by-Side | Parallelbetrieb mehrerer Umgebungen |

## 6. Querverweise

- → Konzept 11 (IHoLyCLaK): Pipeline-Automatisierung aus Repos
- → Konzept 14 (Patent API Integration): MCP-Server-Architektur
- → Konzept 26 (Sonstiges): `caddy-master.zip` (Caddy-Quellcode aus vorheriger Session)


---
*Kapitel 08 · ~1.1 Seiten · 392 Wörter · Beginn S. 13*
