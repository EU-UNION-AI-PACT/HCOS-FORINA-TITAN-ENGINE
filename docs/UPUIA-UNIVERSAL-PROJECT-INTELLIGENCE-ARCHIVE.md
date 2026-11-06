# UPUIA — Universal Project & URL Intelligence Archive

## MASTER DEVELOPMENT & SECURITY DIRECTIVE
**Target:** EndeavourOS / Arch Linux  
**Deployment:** Native Local System Platform Only (No Containers, No Host Modification)  
**Security:** Zero Trust · Offline · No Host Modifications · Fail Closed  
**Data Sovereignty:** Local Only · No Disclosure · Immutable Originals  
**Governance:** Daniel Pohl, Royal Kaiser Charter RegSys  
**Registration:** PIC: 867679357 · USt-IdNr.: DE31353063511 · Global LEI: 894500GBJSIW8L6ET310 · UNGM: 1172700

---

## Die 10 unverhandelbaren Grundregeln

| Nr. | Grundregel | Technische Durchsetzung in HCOS FORINA TITAN |
| :--- | :--- | :--- |
| **01** | **Keine Systemänderungen** | Keine Pakete, Kernel-Module, Firewall-Regeln oder Host-Dienste werden modifiziert. |
| **02** | **Ausschließlich lokal** | Vollständig autarker Offline-Betrieb. Keine Cloud-, Docker-, Podman- oder VM-Bereitstellung erforderlich. |
| **03** | **Separater Projektordner** | Alle generierten Indizes, Kataloge und Cache-Dateien verbleiben strikt in `.forina/upuia/`. |
| **04** | **Unveränderte Originale** | Quell-Dateien, Archive und Zeitstempel bleiben 100% unverändert (Strict Read-Only Access). |
| **05** | **Kein Schlüsselmaterial** | Striktes Filtern von `.key`, `.pem`, `.crt`, `.der`, `.p12`, `.env`, API-Tokens und privaten Vault-Dateien. |
| **06** | **Keine Datenlecks** | Keine Analyseinhalte in externen Chats, Telemetriediensten, Crash-Reports oder Git-Repositories. |
| **07** | **Devin ohne Echtdaten** | Subagenten und Verifikations-Engines arbeiten ausschließlich mit synthetischen Test-Fixtures. |
| **08** | **Technisch blockiertes Netzwerk** | Preflight WAN-Egress Probing (`8.8.8.8:53`, `1.1.1.1:80`, `example.com:443`) blockiert jeden Netzwerkaufruf. |
| **09** | **Unabhängige Startprüfung** | Preflight Security Gate prüft Code-Hashes, Manifest-Integrität und Dateideskriptoren vor dem Scan. |
| **10** | **Fail Closed** | Bei der geringsten Sicherheitsanomalie, Formatverletzung oder Secret-Erkennung wird der Scan verweigert. |

---

## Kernfähigkeiten

1. **Sichere URL-Normalisierung & Token-Bereinigung:**
   * Automatische Extraktion von Webadressen, Git-Repositories, Normen-Quellen und Zentralbank-Portalen.
   * Bereinigung sensibler Query-Parameter (`?token=...`, `?key=...`, `?signature=...`) vor der Persistierung.
2. **Archiv-Sicherheitsgrenzen:**
   * Verhindert *ZipSlip* / Path-Traversal durch Prüfung relativer Pfade (`..`).
   * Verhindert *ZipBombs* durch Decompressions-Budgetierung (max. 25 MB Dekomprimierungsvolumen, max. 500 Dateien).
3. **Kryptografische Evidenz:**
   * Jeder erfasste Datensatz erhält einen deterministischen SHA-256 Hashwert (`sha256_record`).
