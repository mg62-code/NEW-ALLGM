---
dokument_id: DOC-16
titel: Zielbild Seiten- und Bedienungsprozesse
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: Planung aus aeronewsfra2 Anlage 1 – NICHT Ist
---

# Zielbild Seiten- und Bedienungsprozesse

> **Lesart:** Operative Prozessdokumentation. Ist und Zielbild getrennt.
> Keine Secrets, keine unbewiesenen Erfolge.


## 0. Statushinweis

Übersetzung/Operationalisierung von
`aeronewsfra2/Anlage-1-Technische-Seiten-und-Bedienungsanleitung.html`.
Grundlage für Implementierung und Abnahme des **Portal-Zielbilds**.

## 1. Globale Bedienregeln (Prozess)

```text
Jede Datenfunktion definiert:
loading → success|empty → error|timeout|offline|stale
```

Regeln:

1. einheitliche Statusbegriffe und visuelle Sprache  
2. Buttons: Ladezustand + Doppelklick-Sperre  
3. externe Links: Kennzeichnung + neuer Tab + `rel=noreferrer` wo nötig  
4. jede Live-Zahl: Datenalter oder „nicht verfügbar“  
5. Filter in URL (teilbare Views)  
6. ohne JS: Grundinhalt + Rechtstexte lesbar  
7. Fokus, Statusmeldungen, Kontrast Pflicht  
8. **GitHub Pages = öffentliche Schicht; keine Secrets, keine internen Reviews dort**  

### Globale Navigation (Soll)

| Eintrag | Ziel | Funktion |
|---|---|---|
| Logo | index | Home; aktiv markieren |
| News | newsroom | Suche, Kategorien, Archiv |
| Movements | special movements | nur published Besonderheiten |
| Karte | map | Live, Layer, Tools |
| Dashboard | dashboard | Kennzahlen/Status |
| Spotting | spotting | Punkte/Wetter/Rechte |
| Quellen | sources | Methodik/Herkunft |
| Über uns/Kontakt | about/contact | Unabhängigkeit, Korrekturen |

## 2. Startseite – Prozess

```text
Static hero schnell
→ data loader news/stats
→ featured max 3 published
→ map teaser
→ bei Fehler verständliche Platzhalter (kein Weißraum-Crash)
```

CTAs (Soll): Instagram, News, alle Meldungen, Karte, Dashboard.

| Element | Funktion | Technik |
|---|---|---|
| Hero | Positionierung | statisches HTML |
| Featured News | Top-Meldungen | `data/news.json`, safe render |
| Home Stats | counts + last update | shared loader |
| Home Map | Vorschau | Karten- oder Poster-Layer |

## 3. Newsroom – Prozess

```text
Load published only
→ search title/summary/category/source
→ category buttons → URL ?category=
→ card: meta + „Mehr zur Einordnung“
→ source link only if valid HTTPS
```

Zustände:

- keine Daten: „geprüfte Meldungen werden vorbereitet“  
- Fehler: „konnten nicht geladen werden“  
- Demo: sichtbar „DEMO-INHALT“  
- draft/review: öffentlich unsichtbar  
- published: indexierbar/teilbar  

**Abnahme:** Suche ändert nur View, nicht Originaldaten; keine HTML-Injection.

## 4. Movements / Dashboard / Spotting

### special-movements

Nur published: Special Movement, Diversion, Notfall, Europa-Fokus.  
Kandidaten intern. Aktionen: News/Karte/Quelle/Einordnung.

### dashboard

Öffentliche Stats. Fallbacks: „Keine Daten“ / 0 / leeres Diagramm.  
Keine internen Scores, Privatstandorte, API-Keys.  
Links: News, Prüfprozess, Quellen.

### spotting

Regeln, Perspektive, Bildrechte; später GeoJSON-Punkte.

| Modul | Inhalt | Guardrail |
|---|---|---|
| Punkt | öffentlich, Blick, Distanz, Hinweis | keine Privatgrundstücke |
| Bild | eigene/freigegebene | EXIF strip |
| Wetter | Wind/Sicht/Wolken/Sonne | Quelle+Alter |
| Hinweis | Recht/Sicherheit | keine Nav in Sperrzonen |

Diagramme: Textzusammenfassung für A11y. Footer Rechtstexte erreichbar.

## 5. Karte – Werkzeugprozesse

### Toolbar

| Control | Aktion | Status |
|---|---|---|
| Punkt suchen | FRA/T1/T3/Cargo focus | „Punkt ausgewählt“ |
| Ansicht reset | Startview | „zurückgesetzt“ |
| Mein Standort | Geolocation lokal | found/denied/unavailable |
| Messen | Multi-Point Distanz | km + Punktzahl |
| Messung löschen | clear | 0 km |
| Koordinaten kopieren | last click clipboard | clipboard/fallback prompt |
| Kartenlink teilen | URL state | clipboard/prompt |
| Vollbild | fullscreen container | permission |
| Live-Flüge laden | Backend/OpenSky-Übergang | loaded/rate-limit/offline |
| Wetter laden | FRA weather | values/unavailable |

### Layer-Steuerung

Unabhängig schaltbar (Bereich, Punkte, Achsen, Live, …).  
Live-Layer nur nach erfolgreichem Load sichtbar.  
Marker: Alter, Richtung, optional Höhenfarbe.

### Live-Steuerung (Soll)

Callsign-Filter ohne Full-Reload; Auto-Refresh mit Cache; Pause; Detailpanel statt
Popup-Flut; stale ausgrauen.

### Karten-Zustandsprozess

```text
init map
→ load static layers
→ optional live fetch
→ on fail: map usable + status banner
→ geolocation deny: Hinweis, Rest ok
→ clipboard block: prompt fallback
```

## 6. Quellen / Über uns / Kontakt

Quellen-Flow:

```text
Suchen (Priorität) → Abgleichen → Einordnen → Freigeben
```

Über uns: Unabhängigkeit, ADS-B als Beobachtung, KI-Transparenz, Korrektur/Archiv.

Kontaktarten:

| Art | Pflicht | Workflow |
|---|---|---|
| Faktenkorrektur | Quelle, Datum, Fehler | prüfen, doku, korrigieren |
| Bildangebot | Urheber, Lizenz, Zeit | Rechte, EXIF |
| Movement-Hinweis | Flugnr, Zeit, Quelle | ADS-B nur Hinweis |

Formular: server-side spam protection, validation, Privacy-Hinweis, sichere Delivery.
Impressum/Datenschutz dauerhaft verlinkt; bei Analytics/Newsletter/Affiliate/Karten
Texte aktualisieren.

**Abnahme:** jede externe Quelle auf Quellen-Seite; Artikel verlinkt konkrete Belege.

## 7. Redaktions-/Admin-Prozess

```text
Input (RSS/ADS-B/Hinweis)
→ Candidate
→ Review (Quelle)
→ Verified
→ Published
```

Felder: title, summary, body, source_name/url, relevance, status
(draft/review/published/archived), image/alt.

Buttons: Fakten prüfen, Quelle öffnen, KI-Entwurf, verifiziert, veröffentlichen
(mit Confirm), zurückstellen, archivieren, korrigieren (neue Version, kein silent delete).

Fehlgeschlagene Publikation: **kein Auto-Retry**.

Release/Rollback (Soll): Preview → freigeben → publish artifact → bei Fehler last good.

## 8. Abnahmetests und Fehlerkatalog

| Test | Erwartet |
|---|---|
| Start ohne JS | Grundtext/Nav/Recht lesbar |
| news.json fehlt | Fehlerzustand, keine weiße Seite |
| API/OpenSky offline | Karte bedienbar, nicht live lügen |
| Geolocation denied | Hinweis, kein Abbruch |
| Clipboard blocked | Fallback |
| Mobile Touch | Zoom/Pan/Layer/Buttons ohne Overlap |
| invalid source URL | kein unsicherer Link |
| Review-Kandidat | nicht in public JSON/Newsroom |

Fehlerklassen: Daten · Quellen · Infrastruktur · Redaktion – jeweils blockieren/
review/status zeigen/entwurf sperren.

Entwickler-Abnahme: alle Buttons mit sichtbarem Ergebnis; Quelle+Zeit+Status an
Datenmodulen; keine Privatstandorte in FE/Logs/Public Data; mobile+a11y Kernpfade.

## 9. Implementierungs-Hinweis für Agents

Bei Umsetzung einzelner Seiten: dieses Doc + `10` Frontend + `13` UX + `07` QA +
`09` Security. Zielbild schrittweise hinter Feature-Flags/Phasen aus `15`.

## 10. Seitenübergreifende Datenlade-Prozesse

### 10.1 Shared News Loader

```text
fetch data/news.json
→ schema validate
→ filter status==published
→ sort by date desc
→ derive categories dynamically
→ expose to home/news/dashboard/movements
→ on fail: page-specific error copy
```

### 10.2 URL-State-Konvention

```text
?category=
&q=
&map=lat,lon,zoom
&layers=airport,live
&from=&to=
```

Regeln: shareable, back-button fähig, keine Secrets in URL, Sanitize vor Render.

### 10.3 Status-Banner-Komponente (global)

| Status | Banner-Sinn |
|---|---|
| ok | optional dezent „Stand: …“ |
| degraded | welche Teilfunktion betroffen |
| stale | Datenalter + „nicht live“ |
| offline | Retry + was noch geht |
| demo | „DEMO-INHALT“ unverkennbar |

## 11. Mobile Bedienprozess Karte

```text
Thumb-zone controls
→ large hit targets
→ bottom sheet detail statt center modal
→ pinch zoom + two-finger pan
→ layer drawer collapsible
→ list mode toggle one tap
```

## 12. Redaktionelle Tastatur-Shortcuts (Soll, intern)

Nur intern, nie public Pages: nächster Kandidat, Quelle öffnen, verifizieren,
zurückstellen – mit Confirm für Publish. Ohne Script-Doku nicht implementieren.

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `05` · `06` · `14` · `18`
- Zielbild: `15` · `16` · `17`

## Dokumentpflege

Änderungen an Verhalten erfordern synchrone Doku-/Vertrags-Updates mit
Geltungsbereich, Annahmen, Testnachweis und Risiken.
