---
dokument_id: DOC-15
titel: Zielbild Bauplan AeroNewsFRA 2.0
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: Planung – NICHT implementierter Ist-Bestand
---

# Zielbild Bauplan AeroNewsFRA 2.0

> **Lesart:** Operative Prozessdokumentation. Ist und Zielbild getrennt.
> Keine Secrets, keine unbewiesenen Erfolge.


## 0. Statushinweis (verbindlich)

Dieses Dokument übersetzt und operationalisiert `aeronewsfra2/aeronewsfra-bauplan.html`.
Es beschreibt das **Soll-System**. Der aktuelle Kern im Repo ist der lokale
Instagram/FastAPI-Connector. Kein Agent darf Inhalte hier als „bereits gebaut“
ausgeben.

## 1. Leitentscheidung

AeroNewsFRA wird **keine Flightradar24-Kopie**. Mehrwert: lokale, nachvollziehbare
Einordnung rund um Frankfurt – was ist interessant, warum, welche Daten belegen es?

Technische Grundsätze:

1. **Fakten vor KI** – KI formuliert, erfindet keine Zahlen  
2. **Live plus Historie** – getrennt behandeln  
3. **Review vor Veröffentlichung** – Automation bereitet vor  
4. Öffentliche Daten nur mit Lizenz/Genauigkeit/Zweck  
5. Empfangsstandort nicht präzise öffentlich  
6. Unabhängig – kein offizieller Fraport-Kanal  

## 2. Ist (Webseite-Zielkontext) vs Soll

| Thema | Typischer Bestand (externes Pages-Repo / Plan) | Zielbild 2.0 |
|---|---|---|
| Hosting UI | GitHub Pages statisch | bleibt öffentliche Schicht |
| News | xlsx → news.json, Actions | geprüftes Backend + Statusmodell |
| Karte | SVG/schematisch, optional OpenSky Browser | echte Tiles, eigene API |
| ADS-B | fehlend | Receiver → signierter Upload → Ingestion |
| Historie/Replay | fehlend | Flight Store + Timeline |
| KI | begrenzt/manuell | Fact-Pack → Draft → Human Review |
| Premium/Newsletter | fehlend | nach stabiler Datenbasis |

## 3. Zielarchitektur-Prozesskette

```text
Antenne ADS-B/Mode-S
→ Mini-PC readsb + lokaler Puffer
→ HTTPS Upload signiert
→ Backend Ingestion/API/DB
→ Web (Karte/News/Dashboard)
→ Distribution (Instagram/Mail) nur mit Freigabe
```

**Erfolgskriterium:** Besucher versteht in ~10s die FRA-Lage; Entwickler trace't
jede Zahl zu Quelle + Empfangszeit.

## 4. Produktseiten (Soll) – Prozess pro Seite

### 4.1 Startseite

Zweck: tagesaktuelle Lage.  
Elemente: Datenalter, Receiver-Status, interessante Movements, Top-Meldung,
„Heute rund um FRA“, Wetter/Spotting-Teaser, Links Karte/Newsroom.  
Regel: schnell und redaktionell; schwere Tools nicht auf Startseite zwingen.

### 4.2 Newsroom

Eigene URLs, Kategorien, Quellen, Timestamps, Related, SEO, Filter, Suche,
Archiv, RSS, Share. Nur `published`.

### 4.3 Special Movements

Event Engine Speisung. Status je Eintrag: beobachtet / geprüft / Quelle bestätigt.
Kandidaten intern.

### 4.4 Dashboard

Öffentliche Kennzahlen: Meldungen, Movements, Typen, Airlines, Datenalter,
Uptime, Reichweiten-Aggregate, Monatsverlauf. **Kein** exakter Hausstandort,
keine internen Scores/Keys.

### 4.5 Spotting

Öffentliche Punkte, Blickrichtung, Wetter, Sonne, rechtliche Hinweise, moderierte
Bilder. Keine Privatgrundstücke/Sicherheitszonen-Navigation.

### 4.6 Quellen / Über uns / Kontakt

Methodik, Herkunft, Lizenzen, Korrekturhistorie, Unabhängigkeit, KI-Transparenz.
Kontakt: Korrektur/Bild/Movement-Hinweis mit Spam-Schutz; keine Wohnadresse public.

### 4.7 Querschnitt Portal

Mobile-first, WCAG 2.2 AA, Breadcrumbs, Canonical, OG, JSON-LD NewsArticle/Dataset,
RSS/Atom, Sitemap, PWA-Shell, Dark/Light, DE/EN (später), Status- und Leerzustände.

## 5. Karte als Kernprodukt – Prozess

```text
Tile-Provider + Attribution wählen
→ Airport GeoJSON versionieren
→ Live-Layer an API
→ Clustering + Detailpanel
→ stale-Visualisierung
→ Historie/Replay getrennt
→ Wetter/Spotting optional
→ URL-State shareable
→ Liste als A11y-Fallback
```

Layer-Tabelle:

| Layer | Inhalt | Quelle | Verhalten |
|---|---|---|---|
| Basis | Orte/Straßen | lizenzierte Tiles | Zoom, Cache, Attribution |
| Airport | Runways/Terminals/Cargo | eigene GeoJSON | statisch versioniert |
| Live | Pos/Track/Alt/Callsign | Receiver/API | Poll/SSE, Cluster |
| Historie | Spuren/Replay | DB | Zeitregler |
| Wetter | Wind/Sicht/Wolken | Open-Meteo o.ä. | manuell/zeitgesteuert |
| Spotting | öffentliche Punkte | redaktionell | Detailpanel |

Bedienregeln: Update 10–30s mit Server-Cache; veraltete Marker ausgrauen; keine
stillen Weiterbewegungen; mobil flüssig.

**Risiko:** OSM-Tiles nicht beliebig belasten – Provider/Cache/ToS vor Live.

## 6. ADS-B-Datenplattform – Prozess

```text
SDR/Receiver → readsb → Edge-Puffer (offline-fähig)
→ signierter Batch-Upload → Ingestion validate
→ store raw short-term → normalize → aggregates/tracks
→ public API minimized
```

Entitäten (Soll): Aircraft, Position, Flight, Event, Source, Station.  
Retention: Roh kurz, Aggregate länger, Events redaktionell dauerhaft (Policy).

API-Soll (Auszug): health, aircraft/live, aircraft/{{id}}, tracks, events,
stats/daily, station/status, receiver/heartbeat, receiver/positions.

Qualität: Empfangszeit + Alter; unplausible verwerfen; confidence aus Alter,
Vollständigkeit, Plausibilität; UI aktuell/verzögert/offline.

**Abnahme:** Netz-Trennung Mini-PC → Web zeigt offline in definiertem Fenster;
Wiederkehr ohne Duplikat-/Zeitchaos.

## 7. KI/Redaktion – Prozess

```text
Quellen/Wetter/ADS-B → Validator → Event Engine
→ Fact Pack → KI Textvarianten → Review → Freigabe → Publish
```

Status: detected → candidate → review → verified → scheduled → published →
corrected/archived.

KI-Ausgaben: Artikel, Short, IG Caption/Story, Reel-Skript, SEO, DE/EN, Bildbriefing
(ohne ungeprüfte Fremdbilder).

**Verboten:** erfundene Flugnummern/Quellen/Ursachen/Security-Bewertungen/
exakte Privatpositionen; Unfälle/Security nie ohne Human Review.

## 8. Technikbetrieb Soll

| Komponente | Empfehlung | Warum |
|---|---|---|
| Frontend | GitHub Pages | statisch, CDN, günstig |
| API | Worker/VPS | Cache, Limits, sichere Endpunkte |
| DB | PostgreSQL; SQLite Edge | Historie, Indizes, Backup |
| Receiver | Mini-PC lokal | Edge, nicht exponieren |
| Bilder | Object Storage HTTPS | Meta braucht public URL |
| Automation | Actions + Backend-Jobs | Research, Build, Reports |

Security: Secret Store, HTTPS, signierte Uploads, Station-API-Keys+Rotation,
CORS, CSP, Rate-Limits, Bot-Schutz, Standort verschleiern, EXIF strip, Logs clean,
Backup+Restore-Test, Antennen-Zustimmung schriftlich.

Tests: Unit (Geo/Zeit/Status) · Integration (Receiver/API/DB/Fallback) · Browser
(Seiten/Karte/mobil/offline).

Monitoring: Pages, API-Latenz, JS-Fehler, Receiver-Uptime, Datenalter, Jobs, Build,
Uploads + sichtbare Statuspage.

Deploy-Regel: Build→Validate→Tests→Preview→Live; Rollback ein Commit/Klick.

## 9. Roadmap-Prozesse und Abnahme

| Phase | Arbeit | Abnahme |
|---|---|---|
| 0 Stabilität | Repo/Workflow, Review≠Published, Tests, Status | freigegebene Meldung erscheint zuverlässig |
| 1 Echte Karte | MapLibre/Leaflet, Provider, GeoJSON, Layer | echte Orte mobil+desktop |
| 2 Live-API | Backend, Cache, Health, OpenSky-Proxy Übergang | Rate-Limits/offline korrekt |
| 3 Eigener Receiver | SDR, readsb, Puffer, Upload, Station-Dashboard | Testbewegung in API; Outage erkannt |
| 4 Historie | Tracks, Stats, Replay, Filter | Zeitraum reproduzierbar |
| 5 Automation | Events, Quellen-Checks, KI-Drafts, IG/News-Draft | Fact→multi Draft ohne Copy-Paste |
| 6 Produkt | SEO, Affiliate, Newsletter, Premium, Analytics+Consent | messbare Aktion ohne Privacy-Bruch |

DoD je Funktion: Nutzen+Quelle doku; Desktop+Mobil; Leer/Delay/Fehler gestaltet;
Kern tests; keine Secrets/Privatstandorte/unklare Lizenzen; Preview+Live geprüft;
Rollback+Monitoring.

**MVP zuerst:** echte Basiskarte, API-Cache, Live-Layer, Status, Detailpanel,
sauberes News-Update. Replay/Monetarisierung danach.

## 10. Entwickler-Arbeitsprozess (aus Bauplan)

1. Bestand lesen  
2. Klein schneiden (1 Feature/PR)  
3. Daten zuerst (Quelle, Zeit, Schema, Fehler)  
4. Sicher (keine Creds in Chat/Code/Public)  
5. Redaktion schützen  
6. Testen (Unit/Integration/Browser/Mobil/Offline/Rate-Limit)  
7. Dokumentieren  
8. Rückwärtskompatibel bleiben  

Abschlussfragen vor Release: korrekt? verständlich? mobil? fehlende Daten? Quelle
erlaubt? Rollback?

## 11. Start-Checklisten

**Vor Live-Datenbetrieb:** Eigentümer-Zustimmung Antenne; Standort grob; Strom/ÜSS/Netz;
Lizenzen Tiles/ADS-B/Bilder; Backend nicht Heimnetz-exponiert; Secrets; Backup/Restore/Rollback.

**Vor jeder Veröffentlichung:** Fakten+Quellen; ADS-B vs Bestätigung getrennt; Datum/TZ/Alter;
keine privaten/security details; Bildrechte+Alt; Web/IG konsistent.

**90-Tage-KPIs:** Uptime sichtbar, Median Datenalter ausgewiesen, Zeit Kandidat→Draft ↓,
Korrekturen/Fehlalarme niedrig nachvollziehbar, Returning visitors/Newsletter ↑,
Einnahmen erst nach Reichweitenbasis.

## 12. Erste drei Tickets (Priorität)

1. Deployment: freigegebene Daten zuverlässig auf Pages  
2. Echte Karte vorbereiten: Lib, Provider, GeoJSON, Datenzugriff entkoppelt  
3. Receiver-Interface definieren: Format, Heartbeat, Upload-Security vor Hardware-Kauf  

## 13. Rechtlicher Vorbehalt

Vor Produktivbetrieb aktuelle Anbieterbedingungen, Datenschutz, Steuer und
lokale/luftfahrtbezogene Vorgaben gesondert prüfen.

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `05` · `06` · `14` · `18`
- Zielbild: `15` · `16` · `17`

## Dokumentpflege

Änderungen an Verhalten erfordern synchrone Doku-/Vertrags-Updates mit
Geltungsbereich, Annahmen, Testnachweis und Risiken.
