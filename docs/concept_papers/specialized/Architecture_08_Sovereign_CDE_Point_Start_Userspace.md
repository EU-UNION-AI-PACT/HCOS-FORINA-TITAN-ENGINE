# Architecture 08 — Sovereign CDE & Point Start: Streaming, Time-Travel & Userspace-Checkpointing

**Dokument-ID:** ARCH-SPEC-08-SOVEREIGN-CDE-POINT-START  
**Sovereign Provenance & Urheber:** Daniel Pohl · Royal Kaiser Charter RegSys  
**Rechtliche Registrierungen & Identifikatoren:**  
- EU Transparency & Research: PIC 867679357 & 873042778  
- Steuerliche Identifikation: USt-IdNr. DE31353063511 & DE441892129  
- Unternehmensidentifikatoren: D-U-N-S 315676980 & 317066336 · Global LEI 894500GBJSIW8L6ET310  
- Internationale Register: UNGM 1172700 · EORI AEOF139420 · Swiss AHV 756.6199.0539.28  
- Akademische Register: ORCID 0009-0004-0348-9769 · Scopus EX2025D1143002  
**Lizenz:** European Union Public Licence (EUPL-1.2) · Sovereign Fail-Closed Boundary  
**Klassifizierung:** KANONISCHES SYSTEMARCHITEKTURPAPIER (HCOS v2.17)  

---

## 1. Technologische Nomenklatur & Problemstellung

Die Bereitstellung gigantischer Terabyte- und Petabyte-großer Entwicklungsumgebungen über das Internet leidet traditionell unter unerträglichen Downloadzeiten, gigantischem Speicherverbrauch und inkonsistenten Zuständen.
Die **Sovereign Cloud Development Environment (CDE)** löst dies durch die Kombination zweier bahnbrechender Kerntechnologien:

1. **Virtual File System (VFS) Streaming & Lazy Loading (Nydus / eStargz):**
   - Das Projekt wird **nicht** vollständig auf das lokale System heruntergeladen.
   - Die Entwicklungsumgebung (IDE) mountet lediglich die hierarchische Metadatenstruktur (Thin Provisioning).
   - Dateifragmente (Chunks) werden erst in der exakten Millisekunde über das Netzwerk gestreamt, in der der Compiler oder Entwickler sie referenziert. Geschlossene Ordner beanspruchen null Netzwerkbandbreite.

2. **CRIU (Checkpoint/Restore In Userspace) für den „Point Start“:**
   - Statt langwieriger Kaltstarts von Datenbanken, Compilern und API-Diensten wird der laufende RAM- und CPU-Zustand als atomarer Snapshot eingefroren.
   - Das System bootet nicht neu: Es wacht auf, indem der persistierte Speicherzustand via Memory-Mapping direkt in den Container injiziert wird.

---

## 2. Infrastruktur & Self-Hosted Sandboxing

```
[ Lokaler Thin Client (Arch Linux / EndeavourOS) ]
                       |
                  (SSH / VFS Socket)
                       v
+-----------------------------------------------------------+
|              BACKEND (Hetzner Storage & Borg)             |
|                                                           |
| 1. Read-Only Master-Layer (Petabyte VFS)                  |
| 2. Copy-on-Write Delta-Layer (OverlayFS Upperdir)         |
| 3. CRIU Checkpoint Repository ("Points")                  |
+-----------------------------------------------------------+
                       |
               (Firecracker MicroVM)
                       v
[ Isolierte Ephemere Sandbox: 0 WAN Egress / WhyTrace eBPF ]
```

- **Strikte Trennung von Darstellung und Berechnung:**
  - Der Quellcode verlässt den gesicherten Serverbereich niemals. Lokale IDEs rendern lediglich die Benutzeroberfläche über verschlüsselte Sockets.
- **Firecracker MicroVMs:**
  - Jeder Workspace läuft in einer dedizierten MicroVM nach strengen BSI IT-Grundschutz- und DORA-Vorgaben.
- **Persistenz & Versionierung:**
  - Sicherung aller Checkpoints durch BorgBackup und Vorta mit Bit-for-Bit Hash-Integrität.

---

## 3. Die vier unverhandelbaren Implementierungsregeln (Invarianten)

| Regel-ID | Bezeichnung | Technische Durchsetzung |
|---|---|---|
| **CDE-RULE-01** | Zero-Trust Egress Rule | WhyTrace / NextTrace eBPF blockiert standardmäßig jeglichen WAN-Traffic |
| **CDE-RULE-02** | Copy-on-Write (CoW) Rule | OverlayFS: Basis-Code ist Read-Only; Änderungen erfolgen im Delta Upperdir |
| **CDE-RULE-03** | Stateless Ephemeral Rule | Container werden nach Testende restlos vernichtet; nur Git-Commits und Points bleiben |
| **CDE-RULE-04** | Memory-Safety Rule | UCCS Clang ASan/UBSan Prüfung ist Voraussetzung für jede Snapshot-Freigabe |

---

## 4. Der Workflow in der Praxis (Point Start)

1. **Aktualisierung:** Die CI/CD-Pipeline generiert nach Code-Änderungen im Master-Zweig einen neuen RAM-Checkpoint (z.B. `crash_log_77`), an dem Testdatenbanken bereits migriert sind.
2. **Abruf:** Aufruf über die Engine: `python3 forina.py cde spawn --point crash_log_77`.
3. **Arbeit:** Das VFS mountet verzögerungsfrei, der RAM-Zustand wird injiziert, und der Entwickler debuggt die Anwendung ab der kritischen Zeile im Single-Step-Modus ohne Wartezeit.
