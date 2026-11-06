Part 2: Core Engine - Virtualization, NaTZa & Infrastructure

Die Architektur der Core Engine & System Logic

Dieses Dokument definiert das Backend, die virtuelle Infrastruktur und die orchestrierende Logik der Architektur. Die 'Core Engine' basiert auf der absoluten Determiniertheit der Act Pack Zero Clock, der fehlerfreien Logik des NaTZa Core Flight Systems und der grenzenlosen Skalierbarkeit über Hetzner QEMU/KVM Virtualisierungen. Gesteuert durch Devin AI Agentenschwärme und das Unified CLI (IHcT), setzt dieser Stack neue Standards in Datensouveränität und Web3 Compliance.

Core Konzept: NaTZa Core Flight System (CFS)

Technologische Definition

Eine hochzuverlässige, fehlerresistente Software-Architektur (ursprünglich für Raumfahrt), adaptiert für Finanz- und Backend-Systeme.

Implementation & Core Handling

Jeder Core-Prozess der Engine (z.B. Transaktions-Routing) wird im CFS-Standard in C/C++ (Clang) geschrieben, um Speicherlecks absolut auszuschließen.

Harness Loop Integration

Der Loop kompiliert den NaTZa-Code mit extrem strengen statischen Analyse-Tools (SAST). Jede Memory-Warnung führt zum sofortigen Build-Fail.

Security & Web3

Garantierte Ausfallsicherheit. Ein Crash im CEX-Anbindungs-Modul beeinträchtigt niemals den DeFi-Liquiditäts-Pool, da die CFS-Logik totale Isolierung erzwingt.

Core Konzept: UCCS (Unified Critical Coding Stack)

Technologische Definition

Ein standardisiertes Werkzeug-Set (Toolset) zum Entwickeln, Testen und Bereitstellen von sicherheitskritischer Software.

Implementation & Core Handling

Die Blaupause für alle Sub-Agenten. Wenn Devin AI neuen Code schreibt, muss dieser zwingend die UCCS-Bibliotheken (für Krypto, Logging, Memory) verwenden.

Harness Loop Integration

Automatisierte Code-Review-Pipeline im Loop verifiziert die Einhaltung der UCCS-Strukturvorgaben via AST (Abstract Syntax Tree) Analyse.

Security & Web3

Erfüllt die strengsten europäischen Normen (BSI IT-Grundschutz, DORA) by Design, da unsichere Bibliotheken auf Kernel-Ebene geblockt sind.

Core Konzept: QEMU/KVM Virtualization

Technologische Definition

Die Basis-Hypervisor-Ebene, die es erlaubt, isolierte virtuelle Maschinen mit nativer Hardware-Performance auszuführen.

Implementation & Core Handling

Jeder Teil der Architektur, von der Web Scraping-Engine bis zum DLT-Node, läuft in seiner eigenen QEMU/KVM-Umgebung auf den Hetzner Bare-Metal Servern.

Harness Loop Integration

Der Loop spawnt für jeden Test-Lauf eine frische QEMU-Instanz, spielt das Setup durch und zerstört die VM nach dem Audit spurlos (Ephemeral Environments).

Security & Web3

Extreme Sandbox-Sicherheit. Selbst wenn ein Smart Contract oder eine API eine RCE (Remote Code Execution) auslöst, ist der Angreifer im KVM-Gastsystem gefangen.

Core Konzept: VHDX Disk Image Architecture

Technologische Definition

Das dynamische Speicherformat für die virtuellen Festplatten der QEMU/KVM Maschinen, verwaltet über libyal/libvhdi.

Implementation & Core Handling

Alle Systemzustände werden als inkrementelle VHDX-Dateien gespeichert. Erlaubt Sekunden-schnelles Rollback und Klonen ganzer Server-Umgebungen.

Harness Loop Integration

Der Loop erstellt vor dem Einspielen eines Patches einen VHDX-Snapshot. Schlägt der Deployment-Test fehl, wird der Snapshot in Millisekunden wiederhergestellt.

Security & Web3

Verhindert Datenkorruption. Die VHDX-Dateien werden direkt über BorgBackup verschlüsselt und unveränderlich auf die Hetzner Storage Box gespiegelt.

Core Konzept: IHcT Unified CLI Protocol

Technologische Definition

Die zentrale Schnittstelle, die Entwickler, KI-Agenten und Systemadministratoren nutzen, um mit der Core Engine zu interagieren.

Implementation & Core Handling

Ein hochkomplexes, aber visuell simples Command-Line-Tool, das direkt mit der Act Pack Zero Clock und der DLT synchronisiert. Es steuert Ingress-Routing, FaaS und Storage.

Harness Loop Integration

Das CLI ist der Trigger für den Loop. Ein Befehl wie `ihct deploy --module finance` startet die gesamte Kaskade an QEMU-Tests, Dependency-Scans und Zertifikats-Ausstellungen.

Security & Web3

Authentifizierung via kryptografischer Signaturen (Hardware Security Modules) anstatt Passwörtern. Jeder CLI-Befehl ist eine auditable Blockchain-Transaktion.

Core Konzept: Vorta / BorgBackup Immutable Vaults

Technologische Definition

Dezentrales, dedupliziertes und stark verschlüsseltes Backup-System für die vollständige Architektur-Sicherung.

Implementation & Core Handling

Läuft als Daemon auf dem Arch Linux/EndeavourOS Host. Sichert die VHDX-Images und die DLT-State-Trees alle 12 Sekunden (Epochen-Finalität) über SSH.

Harness Loop Integration

Der Loop führt täglich automatisierte 'Disaster Recovery' Tests durch: Er lädt ein Backup herunter, bootet es in QEMU und prüft die DLT-Integrität.

Security & Web3

Ransomware-Schutz: Die Backups auf der Hetzner Storage Box sind 'append-only'. Selbst bei kompromittiertem Host-System können Angreifer alte Backups nicht löschen (Sovereign Data).

Core Konzept: AppArmor / SELinux Kernel Hardening

Technologische Definition

Sicherheitsmodule im Linux-Kernel, die Mandatory Access Control (MAC) für Programme bereitstellen.

Implementation & Core Handling

Das Host-Betriebssystem (Arch Linux) ist radikal gehärtet. Der FaaS-Daemon darf z.B. nur auf explizit freigegebene Netzwerk-Ports und VHDX-Verzeichnisse zugreifen.

Harness Loop Integration

Penetration-Tests im Loop versuchen aktiv, aus den AppArmor-Profilen auszubrechen. Erkenntnisse fließen sofort in automatische Profil-Updates ein.

Security & Web3

Blockiert Zero-Day Exploits auf Betriebssystem-Ebene. Kritisch für die Einhaltung der BSI-Vorgaben und den Betrieb von institutionellen Krypto-Bridges.

Core Konzept: Bare-Metal Provisioning (Hetzner)

Technologische Definition

Die automatisierte Skalierung und Einrichtung von physischen Servern ohne störende Cloud-Provider-Schichten (AWS/Azure).

Implementation & Core Handling

Das System skaliert sich selbst. Wenn die DLT-Last steigt, mietet die Core Engine via API vollautomatisch neue Hetzner Root-Server, installiert Arch Linux, KVM und verbindet sie.

Harness Loop Integration

Der Infrastructure-as-Code (IaC) Loop validiert die Hetzner-Boot-Scripts. Neue Server müssen innerhalb von 4 Minuten vollständig synchronisiert und audit-ready sein.

Security & Web3

Maximale Datensouveränität (EU Data Space). Die physische Kontrolle bleibt im EU-Raum, unabhängig von US-Cloud-Gesetzen (CLOUD Act).

Core Konzept: Serverless FaaS Invocation

Technologische Definition

Ausführung von kurzlebigen Code-Schnipseln (Functions) als Reaktion auf Events, ohne permanente Server-Prozesse zu betreiben.

Implementation & Core Handling

Gesteuert durch `faas-cli` und das IHcT Protokoll. Die FaaS-Container kompilieren Python/Clang-Templates in Sekundenbruchteilen.

Harness Loop Integration

Der Loop misst die 'Cold Start'-Zeiten der FaaS-Container. Sind sie zu langsam, wird das Pre-Warming-Modell des Zero-Clock-Heartbeats angepasst.

Security & Web3

Perfekte Skalierbarkeit für Off-Chain-Berechnungen (z.B. komplexe Portfolio-Risk-Auswertungen für Ghostfolio), ohne die DLT zu verstopfen.