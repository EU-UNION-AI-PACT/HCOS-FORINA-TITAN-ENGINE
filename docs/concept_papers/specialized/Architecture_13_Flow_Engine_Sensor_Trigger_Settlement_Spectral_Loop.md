# Architecture 13: Flow-Engine: Sensor → Trigger → Settlement (Spectral Closed Loop)

**Dokumenten-Klassifikation:** Systemarchitektur & Reaktiv-Kybernetisches Referenzdokument  
**Souveräner Urheber & Provenienz:** Daniel Pohl · Royal Kaiser Charter RegSys  
**Geltungsbereich:** HCOS TITAN / Flow-Engine / Spectral Feedback / WebGL 3D Visualization / Real-Time Settlement  
**Rechtsstatus & Identifikatoren:** PIC 867679357 & 873042778 · LEI 894500GBJSIW8L6ET310 · EORI AEOF139420 · UNGM 1172700 · USt-IdNr. DE31353063511 & DE441892129 · D-U-N-S 315676980 & 317066336 · Swiss AHV 756.6199.0539.28  

---

## 1. Systemübersicht & Paradigmenwechsel

Herkömmliche Softwaresysteme und Datenverarbeitungspipelines arbeiten nach einem starren, sequentiell gestapelten Muster (*Stacking*): Input wird eingelesen, verarbeitet, gespeichert und anschließend zur Anzeige gebracht. 

Die **HCOS TITAN Flow-Engine** bricht mit dieser Starrheit und etabliert ein **fließendes kybernetisches Resonanzmodell**:
- Kontinuierliche Signalströme (Audiofrequenzen, Zeigerdynamik, CPU/GPU-Telemetrie) werden in hoher Frequenz (60 Hz) abgetastet.
- Signale transformieren sich über Schwellenwert-Muster in diskrete Ereignisse (*Trigger*).
- Trigger bewirken unumkehrbare Ausführungsaktionen (*Settlements*).
- Die Settlement-Auswirkungen koppeln direkt in das Sensorfeld zurück (*Resonance Feedback Loop*).

```
        ┌─────────────────────────────────────────────────────────┐
        │                 1. SENSOR-SCHICHT                       │
        │  * S1: Spektral (FFT, Centroid, Bass/Mid/High Energy)   │
        │  * S2: Motion (Winkelgeschwindigkeit, Scroll-Velocity)  │
        │  * S3: System Telemetrie (Load-Index, Frame-Times)      │
        └────────────────────────────┬────────────────────────────┘
                                     │ (Kontinuierlicher 60Hz Stream)
                                     ▼
        ┌─────────────────────────────────────────────────────────┐
        │                 2. TRIGGER-SCHICHT                      │
        │  * T1 Beat  * T2 Sync  * T3 Circle  * T4 Peak           │
        │  * T5 Flow-Cluster     * T6 Delay-Interpolation         │
        └────────────────────────────┬────────────────────────────┘
                                     │ (Diskrete transaktionale Events)
                                     ▼
        ┌─────────────────────────────────────────────────────────┐
        │                 3. SETTLEMENT-SCHICHT                   │
        │  * SET-01 State & Score Updates                         │
        │  * SET-02 Visual Feedback (WebGL Shader / Canvas)       │
        │  * SET-03 Token-Ledger & Punkte-Buchung                 │
        │  * SET-04 Kettenreaktionen & Stufen-Freischaltung       │
        └────────────────────────────┬────────────────────────────┘
                                     │
                                     ▼
                      [ KONTINUIERLICHE RÜCKKOPPLUNG ]
                                     │
                                     └────────────────────────────► (zurück zu Schicht 1)
```

---

## 2. Die Drei Kernschichten im Detail

### 2.1 Sensor-Schicht (Signalmessung & Normalisierung)
- **Spektral-Sensor (S1):** Analysiert Audiosignale oder Frequenzdaten in Echtzeit (0–20 kHz). Liefert normalisierte Metriken:
  - *Spectral Energy* \(E \in [0, 1]\): Gesamte Signalleistung.
  - *Spectral Centroid* \(C \in [0, 1]\): Frequenzgewichteter Schwerpunkt.
  - *Onset Strength*: Momentane Steilheit von Amplitudensprüngen.
- **Bewegungs-Sensor (S2):** Erfasst Maus-, Touch- oder Gestenvektoren. Liefert Drehwinkel (\(\theta\)), Winkelgeschwindigkeit (\(\omega\)), kumulierte Umdrehungen und Scroll-Velocity mit zeitlichem Frame-Overlap.
- **System-Sensor (S3):** Kontinuierliche Erfassung von CPU-Kernauslastung, GPU-VRAM-Allokation und Frame-Latenz.

### 2.2 Trigger-Schicht (Mustererkennung & Ereignis-Erzeugung)
Die Trigger-Schicht wandelt Fließdaten in diskrete Events um:
- **Beat-Trigger (T1):** Feuert, wenn \(E > E_{\text{dyn}}\) und ein Onset detektiert wird.
- **Sync-Trigger (T2):** Feuert, wenn mehrere heterogene Sensoren innerhalb eines definierten Toleranzfensters (\(\Delta < 5\%\)) harmonieren.
- **Kreis-Trigger (T3):** Reagiert auf vollständige \(360^\circ\)-Umdrehungen als bewusste manuelle Modulation.
- **Peak-Trigger (T4):** Prioritäts-Interrupt bei extremen Amplitudenspitzen (\(E > 0.92\)).
- **Flow-Trigger (T5):** Aggregiert Ereignis-Cluster (\(\ge 5\) Events innerhalb von 250 ms) zu einem anhaltenden Resonanzstrom.

### 2.3 Settlement-Schicht (Transaktionale Ausführung)
Jedes ankommende Event führt zu einer konkreten Zustandsänderung:
- **Zustands-Settlement (SET-01):** Historisierung im Ringpuffer, Berechnung von *Flow-Score* und *Sync-Multiplikator*.
- **Visuelles Settlement (SET-02):** Direkte Steuerung der Shader-Attribute im 3D WebGL Canvas (`flow-engine-3d.html`), Farbfeld-Shift und dynamische Partikel-Emitter.
- **Ledger-Settlement (SET-03):** Deterministische, unveränderliche Verbuchung von Aktivitäts- und Beteiligungswerten.
- **Kettenreaktionen (SET-04):** Freischaltung nachfolgender logischer Schwellenwerte.

---

## 3. WebGL 3D Live-Visualisierung

Die Engine ist nahtlos an die interaktive 3D-Präsentation `web/flow-engine-3d.html` angebunden:
- Vollständige Vektorisierung ohne Raster-Grafiken (Zero-Image-Rule).
- Mathematische Projektion des geschlossenen kybernetischen Rings im virtuellen 3D-Raum.
- Echtzeit-Modulation von Partikel-Frequenzen bei Beat- und Sync-Ereignissen.

---

## 4. Wirtschaftlich-Rechtliche Abgrenzung

Die Flow-Engine ist eine **technische Ereignis- und Resonanz-Engine**. Sie erzeugt keinen automatischen wirtschaftlichen Geldfluss. Settlement-Werte und Token stellen rein interne Verrechnungs- und Aktivitätsmetriken dar und entfalten erst in Verbindung mit externen Rechtsgeschäften (unter expliziter Freigabe durch Daniel Pohl via Gate G09) rechtlich bindende Wirkungen.
