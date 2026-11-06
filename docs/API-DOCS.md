# HCOS FORINA TITAN · API-DOKUMENTATION

Der integrierte Engine-Server (`forina_engine/server.py`) stellt folgende REST- und Live-Sync-Endpunkte bereit:

| Endpunkt | Methode | Beschreibung |
|---|---|---|
| `/api/live-sync` | GET | Gibt den vollständigen Realisierungsstatus aller 8 Module, Light Blink Status und Statistic Glow Points zurück. |
| `/api/spec-status` | GET | Alias für `/api/live-sync`. |
| `/api/ota/version` | GET | Liefert die aktuelle OTA-Systemversion (`1.2.0`) und das Änderungsprotokoll. |
| `/api/atomclock` | GET | Hochpräzise Atomuhr-Zeitstempel (UTC/CET, Epoche in Millisekunden). |
| `/api/modules/load?name=<id>` | GET | Lädt die JSON-Definition eines Moduls aus der Registry. |
| `/api/modules/register` | POST | Registriert ein neues dynamisches Modul (erfordert `X-Forina-API-Key`). |
| `/api/jmap/partner-inquiry` | POST | JMAP-Partnerschaftsübermittlung an `world.banks.eyes.aether@globedynamicz.statesflowwishes.eu`. |
