---
dokument_id: DOC-12
titel: Prozesshandbuch GIS und Aviation
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: Karten, GeoJSON, ADS-B/Mode-S, FRA/EDDF, Datenqualität
---

# Prozesshandbuch GIS und Aviation

> **Lesart:** Operative Prozessdokumentation mit technischen Details pro Schritt.
> Ist-Bestand und Zielbild bleiben getrennt. Keine Secrets oder unbewiesenen Erfolge.


## 1. Zweck und Fachgrenze

Verbindlich für `Dev-GIS-Aviation-Specialist`: Karten, GeoJSON, Tiles, Layer,
Flugspuren, ADS-B/Mode-S, EDDF/FRA-Fachlogik, Datenqualität. Eigenständig:
Signale, Quellen, Projektion, Zeit, Interpretation hinterfragen; Ursachen analysieren;
reale Lösungen im zugewiesenen Bereich; prüfbare Artefakte.

**ADS-B-Signal = unvollständige Beobachtung, keine automatische Wahrheit.**

**Verantwortet:** Geometrie, Projektion, Aviation-Fachlogik, Unsicherheit, Layerverhalten.  
**Nicht:** geheime Empfangsposition, API/DB-Betriebsfreigabe allein, Quellenrechte allein,
redaktionelle Veröffentlichung, alleinige UX-Entscheidung.

**Ist:** im Connector-Kern keine produktive Live-Karte.  
**Zielbild:** Docs `15`–`17`. Keine erfundenen Flugzeug-/Flug-/Ereignisdaten.

## 2. Auftrag, Inputs, Outputs

Auftrag: Nutzerziel, Raum/Zeit, Layer, Quelle, Lizenz, Akzeptanz, Qualitätsgrenzen,
Last, Datenschutz, Offline-Fallback, Rollback.  
Eingaben: Anbieterbedingungen, Rohmeldungen/Fixtures, GeoJSON/Styles, API-Schema,
Flughafenreferenzen, UI-Vorgaben, Messwerte.

**Output an Ali:** Layer- und Datenvertrag, CRS/Einheiten, Qualitätsregeln, Dateien,
Testdaten/Ergebnisse, Perf-Grenzen, Lizenz/Attribution, Standortschutz, Unsicherheiten,
Rollback, offene Fachentscheidungen.

| Rolle | Koordination |
|---|---|
| Ali | Scope, Priorität, Integration |
| Backend | Ingestion/Query, Schema, Alter, Limits, Status |
| Frontend | Interaktion, Liste, mobile Zustände |
| Research | Primärquelle, Nutzungsgrenze, Attribution |
| Security | Standort-, Tile-, Receiver-, API-Risiko |
| UX | Legende, Detailpanel, Verständlichkeit |
| QA | Geometrie-, Daten-, UI-Befunde |
| Data Quality | Provenienz, Freshness, Rejects |

## 3. Prozessübersicht

```text
G01 Auftrag (Raum/Zeit/Layer/Lizenz/Last/Privacy)
 → G02 Bestand lesen; Ist ≠ Zielbild
 → G03 Quelle + Lizenz + Attribution klären
 → G04 CRS, Projektion, Einheiten, Höhenreferenz
 → G05 Schema- und GeoJSON-Validierung
 → G06 Aviation-Normalisierung (Roh ≠ Aussage)
 → G07 Plausibilität: Sprung, Alter, Coverage, Duplikat
 → G08 Layervertrag + Sichtbarkeits-/Zoomregeln
 → G09 Rendering: Cluster, Viewport, Generalisierung
 → G10 stale/degraded/offline Kennzeichnung
 → G11 Standortschutz vor Public Output
 → G12 Listenalternative + mobile/Keyboard
 → G13 Event-Kandidaten nur mit Evidenz+Konfidenz
 → G14 Tests + Fixtures + Perf-Messung
 → G15 Monitoring + Rollback + Übergabe
```

## 4. Bestandsanalyse und Ursachenfindung

Git-Status und Anweisungen zuerst. Dann README, Zielbild, Karten-/Frontendcode,
API/DB-Verträge, Config, Tile-Anbieter, Tests, Daten. CRS-/Koordinaten-/Höhen-/
Zeit-/Einheitenkonvertierungen und Layer-Aufrufer suchen.

**Fehler-Hypothesen trennen:** Projektion | Quelle | Empfangslücke | Parser |
Plausibilität | Cache | Rendering. Deterministische Fixtures; Roh- vs normalisierte
Werte messen; Ursache an richtiger Grenze beheben. Optischer Workaround über
falsche Daten unzulässig.

## 5. Geodaten- und Layervertrag

Jeder Layer dokumentiert: Zweck, Quelle, Lizenz, Aktualität, CRS, Geometrien,
Properties, Sichtbarkeit, Zoom/Viewport-Regel, Limit, Cache, Fallback, Zugriffsgrenze.

| Regel | Detail |
|---|---|
| GeoJSON | WGS84 Grad, RFC 7946 |
| Rendering | oft EPSG:3857 Web-Mercator – nicht mit WGS84-Metern verwechseln |
| Validierung | FeatureCollection, erlaubte Geometry-Typen, finite Zahlen |
| Bounds | Lon [-180,180], Lat [-90,90] |
| Topologie | Ring/Segment-Struktur, Payloadgröße |
| Privacy | private/sensible Koords runden, versetzen, aggregieren oder entfernen |
| Public | exakte Empfangs-/Hausposition **nie** |

Antimeridian, Achsenreihenfolge, Rundung, numerische Toleranzen bewusst behandeln.
Properties nur benötigte, typisierte Fachfelder.

## 6. Aviation-Datenvertrag und Normalisierung

**Getrennte Ebenen:**

1. Rohsignal  
2. normalisierte Beobachtung  
3. Flugsegment/Track  
4. Ereigniskandidat  
5. redaktionelle Aussage  

Mindestfelder: source, icao24 (falls), callsign, observed_at UTC, received_at UTC,
Position, Höhenreferenz, Groundspeed, Track, quality, confidence, Datenalter, Herkunft.

- Baro-Höhe ≠ geometrische Höhe  
- Einheiten (kt, ft, m/s …) explizit  
- fehlende Werte und MLAT/Coverage-Unsicherheit sichtbar  

Positionsprüfungen: Schema, Zeitfenster, Höhe/Speed, Koordinaten, Sprungweite,
zeitliche Reihenfolge. Unplausibel → `degraded`/`rejected`, nicht glätten.
Interpolation/Glättung nur als kenntlich gemachte Visualisierung; Originalpunkte bleiben.

## 7. Fachliche Plausibilität und FRA/EDDF

```text
Quelle/Lizenz → Schema/CRS → Koordinaten/Zeit → Einheiten/Höhe
→ Datenalter → Ausreißer/Sprünge → Aviation-Plausibilität
→ GeoJSON/Layer → Rendering/Cache → mobil → Attribution/Privacy → Tests
```

FRA/EDDF-Bezug, Runways, Anflugrichtungen, Korridore, Holdings, Flugphasen nur
aus belegten Referenzen oder explizit als Ableitung. Holding, Go-around, Diversion,
Erstbesuch, ungewöhnliche Route = technische Hinweise, **keine** Notfall-/Security-Claims.
Ereignisregeln → Kandidaten mit Belegen + Konfidenz; menschliche/Quellenprüfung
für Redaktion und Sicherheit Pflicht.

## 8. Implementierung Karten und Flugspuren

Layerarchitektur: Basiskarte/Tiles · Flughafenobjekte · Spotting (redaktionell) ·
Live-Flüge · Tracks · Wetter/Wind · Ereignisse.

- MapLibre oder Leaflet hinter stabilem Vertrag (austauschbar)  
- Marker-Clustering, Viewport-Queries, Zoom-Abhängigkeit, Generalisierung, Spatial Index  
- Linien mit Zeit-/Qualitätsmetadaten; Richtung nur bei belastbarem Track  
- Tile: Anbieterregeln, Cache-Header, sichtbare Attribution; kein Scraping/unlizenzierter Proxy  
- Tile-Fehler → brauchbare Listen/Textalternative + `degraded`/`offline`  
- Live vs Historie/Replay eindeutig; Interpolation nicht wie echte Messung  
- URL-State: center, zoom, filter, Zeitraum  

Live-Update typisch 10–30 s mit Server-Cache (Zielbild). Veraltete Marker ausgrauen,
nicht still weiterbewegen.

## 9. Datenalter, Empfangslücken, Unsicherheit

Schwellen fachlich festlegen und versionieren. Sichtbar: Quelle, letzte Beobachtung/
Empfangszeit, Qualität, Unsicherheit. `stale` ≠ live. Fehlende Coverage ≠ Abwesenheit
des Flugzeugs. Heartbeat, Positionszeit, Uploadzeit getrennt. Nach Ausfall kein
unkontrollierter Nachholsturm, keine vermeintlich aktuelle Animation.

Tracks bei großen Zeitlücken/Sprüngen/Coverage-Lücken segmentieren und als
unvollständig markieren. Replay: Datum/TZ, Originalzeit, Abspielstatus deutlich;
UTC intern, Europe/Berlin Anzeige.

## 10. Datenschutz, Sicherheit, Recht

- exakte Haus-/Antennen-/private Spottingpositionen nicht ausgeben  
- gesperrte/nicht öffentliche Bereiche, Kamera-, Netzwerkdaten geheim  
- Receiver nur ausgehend, authentifiziert; kein direkter Internetzugriff auf Heimnetz  
- API-Keys/Tokens/private Quellen weder Frontend noch Logs  
- vor jedem Layer: Anbieterbedingungen, Lizenz, Attribution, Cache/Tile-Regeln, Zweckbindung  
- Research bestätigt externe Fakten; Agent trennt Quelle / Beobachtung / Ableitung / Interpretation  

## 11. Tests und Verifikation

Isolierte, anonymisierte Fixtures. Pflicht:

1. ungültige/fehlende Koordinaten, NaN, Grenzwerte, falsche Achsenreihenfolge  
2. Datumsfehler, Zukunftszeit, stale, verspäteter Upload, Zeitzone  
3. unrealistischer Sprung, falsche Höhe/Speed, Duplikat, fehlende Coverage; Rohpunkt erhalten oder nachvollziehbar abgelehnt  
4. leere Layer, große Dichte, BBox, Antimeridian, fehlende Tiles  
5. Live/Replay-Verwechslung, mobile Touch/Keyboard, Listenalternative  
6. Attribution, Lizenzgrenze, Standortverschleierung, unerlaubte Payloadfelder  

Perf: realistische Punkt-/Trackzahl, Zoomstufen, langsame Verbindung – Payload,
Tile/API-Aufrufe, Renderzeit, FPS, Speicher, Clustering, Cache-Hitrate.  
Nachweis: Fixture, Befehl, Messwert, nicht verifizierte Provider-/Realweltdaten.

## 12. Betrieb, Monitoring, Rollback

Health/Readiness unterscheiden: Receiver, Ingestion, API, Tileprovider, Frontend.
Metriken: Heartbeat, Datenalter, Coverage, verworfene/markierte Meldungen, Sprünge,
Querylatenz, Tilefehler, Payload, Layer-Renderzeit. Alerts mit Runbook; bei
Qualitätsverlust Event-Jobs auf Review.

Rollback: letzter verifizierter Layer/Datenstand oder Textalternative; Regelversion
zurück, Rohdaten/Belege/Korrekturhistorie behalten. Rollback darf Standortschutz
oder Attribution nicht entfernen.

## 13. Übergabe und Checkliste

Übergabe: Auftrag, Bestand, Layer-/Aviationvertrag, CRS/Einheiten/Höhenreferenz,
Quellen/Lizenzen, Qualitätsregeln, Fixtures, Messwerte, A11y-Alternative, Privacy,
Dateien, Rollback, offene Unsicherheiten. Integration nach Backend/FE/Security/QA
soweit betroffen. Keine Public Publish/Prod-Migration/Deploy ohne Freigabe.

- [ ] Quelle, Lizenz, Attribution, Alter, CRS, Einheiten  
- [ ] WGS84/GeoJSON vs Web-Mercator sauber  
- [ ] Roh / Beobachtung / Track / Kandidat / Aussage getrennt  
- [ ] Unsicherheit, Coverage, Höhe, Sprünge, stale, Duplikate  
- [ ] Layer, Tiles, Cluster, Viewport, große Daten, Offline  
- [ ] Liste, mobil, Quellenhinweis  
- [ ] Standortschutz, Secrets, Provider, Logs  
- [ ] Monitoring, Rollback, Diff, Übergabe  

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `02-rollen-und-szenarien.md`
- `05-bestandsaufnahme-und-vertraege.md` · `06-agenten.md`
- `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15` · `16` · `17` (nur Planung)

## Dokumentpflege

Verhaltensänderungen: Verträge, Agent-Profile, README und dieses Handbuch
gemeinsam aktualisieren (Geltungsbereich, Annahmen, Testnachweis, Risiken).
