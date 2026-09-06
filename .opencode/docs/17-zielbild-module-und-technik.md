---
dokument_id: DOC-17
titel: Zielbild Module und technische Bausteine
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: Planung aus aeronewsfra2 Anlage 2 – NICHT Ist
---

# Zielbild Module und technische Bausteine

> **Lesart:** Operative Prozessdokumentation. Ist und Zielbild getrennt.
> Keine Secrets, keine unbewiesenen Erfolge.


## 0. Statushinweis

Übersetzung/Operationalisierung von
`aeronewsfra2/Anlage-2-Technische-Besonderheiten-und-Module.html`.
Modulverträge für besondere Technik. **Schnittstellen stabil halten:** Kartenwechsel
darf Receiver nicht brechen; KI darf Datenmodell nicht definieren.

## 1. Produktkern

Local Sensor + Geo Intelligence + Editorial Engine.  
Nutzer sieht nicht nur Marker, sondern **Warum FRA-relevant**, **wie sicher**, **welche Quelle**.

| Modul | Besonderheit | Prio |
|---|---|---|
| Map Core | echte Karte + Layer | P0 |
| Receiver Gateway | signierter ADS-B-Upload | P0 |
| Flight Store | Historie/Spuren | P1 |
| Event Engine | seltene/ungewöhnliche Movements | P1 |
| Replay | Zeitreise | P2 |
| AI Studio | Fact-Pack → Drafts | P2 |
| Public API | kontrollierte Daten | P2 |
| Premium Alerts | individuelle Notify | P3 |

## 2. Modulvertrag (Template für jedes Modul)

```text
purpose + user value
input/output schema
source + timestamp semantics
error + offline state
privacy + license constraints
test cases + acceptance criteria
rollback procedure
owner + monitoring signal
auth + storage + cost notes
```

## 3. Map Core – Prozess

```text
Tile Layer → GeoJSON Airport/Spotting → Flight Layer live/history
→ Interaction filter/detail → URL state → Fallback
```

Features: austauschbare MapLibre/Leaflet-Abstraktion; eigene GeoJSON Runways/
Terminals/Cargo/Spotting; Live als FeatureCollection/Vector; Clustering;
Richtungspfeile; Höhenlegende; Track LineString zeitgewichtet; Detailpanel;
URL state zoom/center/time/filter; Tile-Fallback.

| Regel | Umsetzung |
|---|---|
| Datenalter | färben/ausblenden nach Schwelle |
| Lizenz | Attribution immer sichtbar |
| Perf | viewport, cluster, throttle, cache |
| Privacy | Empfangsort runden/versetzen |
| A11y | Liste + Keyboard |

**Nicht:** reine Optik-Demo ohne Quelle/Fehlerzustand.

## 4. Receiver Gateway – Prozess

```text
Antenne 1090 → SDR → readsb JSON → Uploader Batch → API Ingestion
```

Edge:

- Config local file / protected env  
- Queue bei Offline  
- Heartbeat ≠ Positionsstream  
- Batch + retry/backoff  
- Signatur oder API-Key pro Station  
- NTP, intern UTC  
- Health: temp/disk/net/process  

Ingestion-Validierung:

| Check | Beispiel | Bei Fehler |
|---|---|---|
| Schema | lat/lon/received_at | reject+log |
| Range | coords plausible | drop |
| Jump | unrealistische Bewegung | mark degraded |
| Age | receive vs upload | mark delayed |
| Duplikat | station/seq | idempotent ignore |

Public: nur Aggregate Reichweite/Uptime/Alter. Roh geschützt, TTL/Aggregation.

**Abnahme:** nach Netzausfall keine Datenflut; Order+Duplikate korrekt.

## 5. Flight Store + Replay – Prozess

Flight-Session aus Positions; Start bei Aktivität, Ende nach Silence-Timeout.
Rohpunkte ≠ redaktionelle Summary.

Objekte: track point · flight session · track segment (simplified) · daily aggregate.

Replay:

```text
Datum/Zeitraum → Query tracks → Timeline scrub → Render markers
Controls: Live|Pause|1x|5x|20x|Share|Filter Airline/Type
```

Regeln: UTC intern / Europe/Berlin UI; Interpolation nur visuell; große Ranges
serverseitig aggregieren; abgebrochene Tracks unvollständig; Replay nie als Live;
Share-URL mit time+filter.

Besonderheit Content: „Heute vor einem Jahr“, Ereignis-Rückblick aus eigenen Daten.

## 6. Event Engine – Prozess

Erzeugt **technische Auffälligkeit**, keine Wahrheit.

| Event | Hinweis | Risiko |
|---|---|---|
| Seltenes Muster | Typ/Airline unter Schwellwert | Stammdaten lückenhaft |
| Erstbesuch | nicht in Historie | Historie unvollständig |
| Ungewöhnliche Route | Korridor-Abweichung | Route unbekannt |
| Holding | Schleifen | ≠ Notfall |
| Diversion-Hinweis | Landung ≠ erwartetes Ziel | extern bestätigen |
| Go-around-Hinweis | Sink dann Steig | Radarlücken |

Scoring (Beispielpolitik):

```text
score = rarity*0.30 + fra_relevance*0.25 + data_quality*0.20
      + source_quality*0.15 + novelty*0.10
if safety_related: require_human_review = true
```

Duplikate: gleiche Flugnr+Fenster mergen; multi-source attach; ähnliche Titel
vor Multi-Post erkennen; ein Event speist News/Movement/Story/Alert; Regeln versionieren.

Grenze: ungewöhnlich ≠ gefährlich.

## 7. AI Studio – Prozess

```text
Fact Pack → Prompt Policy → AI Draft variants → Human Review → channels
```

Kanäle: Website (Artikel/SEO/Alt) · Instagram (Caption/Story/Hashtags/Bildbriefing)
· Video 15–45s · Newsletter.

Fact-Pack-Schema (Beispiel):

```text
event_id: EVT-2026-0001
facts:
  - label: Flugzeugtyp
    value: Airbus A350-941
    source: own_adsb
    confidence: high
  - label: Beobachtungszeit
    value: 2026-08-23T14:22:00Z
    source: own_adsb
constraints:
  require_review: true
  allowed_claims: [facts_only]
```

QS: strukturierte Outputs; Zahlen/Namen gegen Fact Pack; HTTPS-Quellenpflicht;
Unsicherheit ausgeben; Prompt/Modell-Version loggen; kein Auto-Publish bei Safety.

## 8. Monitoring, PWA, Suche, Einnahmen

### Monitoring

| Signal | Alarm | UI |
|---|---|---|
| Receiver | kein Heartbeat | offline |
| API | Fehler/Latenz hoch | degraded |
| News Build | JSON fail | last good |
| Karte | Tile/API fail | fallback+hint |
| KI | Fact-Match fail | review blocked |

### PWA

App shell, manifest, SW, icon; last good news offline lesbar; Live nie offline-aktuell;
Sync nach reconnect nur unkritische Drafts.

### Suche

Index: Artikel, Airlines, Typen, Events, Reports. Volltext, Filter, Datum,
Pagination, shareable URLs.

### Einnahmen (erst nach Datenqualität + Besuchern)

Affiliate (Kontext Technik) · Newsletter · Premium-Alerts (keine Security-Promises) ·
digitale Produkte (Guide/Report). Werbung darf Karte/Trust nicht schädigen.

## 9. Abnahme pro Modul

1. Normalfall realistisch anonymisierte Daten  
2. Leer + fehlende Felder  
3. Timeout, 429, Provider down  
4. Mobil, Keyboard, SR-Basis  
5. unplausibel/verspätet  
6. keine unerlaubte Publish/Leakage  
7. messbares Monitoring-Signal  
8. Doku + Rollback  

Qualität: **Echt · Erklärbar · Robust**.

## 10. Realisierungsreihenfolge

```text
P0 Stabilität+Karte → P1 Receiver+API → P2 Historie+Events
→ P3 KI+Distribution → P4 Premium
```

**Endabnahme:** reales Flugzeug Receiver→API→Karte; daraus Content prüfbar;
riskant human-gated; rücknehmbar.

Vor Umsetzung: aktuelle ToS Karten/ADS-B/Wetter/Social/Hosting + Privacy/Steuer/Urheberrecht.

## 11. Schnittstellenmatrix zwischen Modulen

| Von → Nach | Vertrag |
|---|---|
| Receiver → Ingestion | signiertes Batch + heartbeat schema |
| Ingestion → Flight Store | normalized positions UTC |
| Flight Store → Map Core | live FC + track segments |
| Flight Store → Event Engine | sessions + features |
| Event Engine → AI Studio | Fact Pack only |
| AI Studio → Review UI | drafts + constraints |
| Public API → Pages | minimized JSON + age |
| Monitoring → alle | health/degraded/offline signals |

## 12. Modul-Lifecycle-Prozess

```text
Proposal → Vertrag (Template §2)
→ Spike/Test in Isolation
→ vertikaler Schnitt angebunden
→ Negativ+Last
→ Feature-Flag default off
→ Preview
→ Freigabe
→ on + monitor
→ iterate or rollback
```

## 13. Kosten- und Limit-Checks vor P0/P1 Go-Live

- Tile-Budget und Caching-Kosten
- API-Rate-Limits OpenSky/Wetter
- Storage-Wachstum Positionsrohdaten
- Object-Storage Bildkosten
- Meta API Call Limits
- Monitoring-Alarm-Rauschen

## 14. Sicherheitsboundary pro Modul

| Modul | Darf nie |
|---|---|
| Map Core | exakten Empfangsort zeigen |
| Receiver | inbound aus Internet öffnen |
| Public API | interne Scores/Keys liefern |
| AI Studio | Facts erfinden / auto-publish safety |
| Premium Alerts | Security-Promises senden |

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `05` · `06` · `14` · `18`
- Zielbild: `15` · `16` · `17`

## Dokumentpflege

Änderungen an Verhalten erfordern synchrone Doku-/Vertrags-Updates mit
Geltungsbereich, Annahmen, Testnachweis und Risiken.
