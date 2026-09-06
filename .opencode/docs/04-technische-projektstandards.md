---
dokument_id: DOC-04
titel: Technische Projektstandards
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: Implementierung und Abnahme
---

# Technische Projektstandards

> **Lesart:** Operative Prozessdokumentation. Schritte nennen Zweck, technische
> Arbeit, Eingabe, Ausgabe, Fehlerpfad und Nachweis. Ist-Bestand und Zielbild
> (aeronewsfra2) bleiben getrennt. Keine Secrets oder unbewiesenen Erfolge.


## 1. Zweck

Gemeinsame Qualitätsverträge für Code, Web, Daten, Aviation/GIS, APIs, Security,
Tests, Content, Konfiguration und Performance. Abweichungen brauchen Begründung
und Ali-Entscheid.


### Lesart der Schritte

| Feld | Bedeutung |
|---|---|
| Zweck | warum der Schritt existiert |
| Arbeit | konkrete technische/fachliche Tätigkeiten |
| Eingabe | benötigte Artefakte |
| Ausgabe | erzeugte Artefakte |
| Fehler | typische Fehlschläge und Reaktion |
| Nachweis | Test, Messung, Log, Review |
| Owner | primäre Rolle |


## 2. Code-Standards

| Regel | Detail |
|---|---|
| Bestand zuerst | Sprache, Framework, Namen, Format, Module respektieren |
| Klarheit | kleine Funktionen, explizite Typen, Validierung, lesbare Namen |
| Fehler | keine still geschluckten Exceptions; nachvollziehbare Fehlerpfade |
| YAGNI/KISS | keine Abstraktion/Dependency ohne Nutzen |
| Nebenwirkungen | explizit; Idempotenz bei Writes |

**Prozess Code-Änderung**

```text
Aufrufer finden → Vertrag prüfen → minimal ändern → Validierung/Fehler
→ Test → Lint/Typ → Diff-Review
```

## 3. Web-Standards

- semantisches HTML, progressive Verbesserung  
- responsive: Smartphone/Tablet/Desktop, Touch + Keyboard  
- Pflichtzustände externer Daten: `loading | empty | success | error | timeout | offline | stale`  
- sichtbares Feedback, Fokus, Kontrast  
- externe HTML/URLs validieren; kein unsicheres `innerHTML`  
- SEO nur für öffentliche Seiten; lokale Connector-UI nicht ungeprüft indexieren  

## 4. Daten-Standards

Jedes fachlich relevante Objekt:

```text
source
observed_at   # UTC Beobachtung
received_at   # UTC Empfang
quality       # valid|degraded|stale|rejected
confidence    # low|medium|high|score
processing_status
payload       # minimiert, validiert
idempotency_key
```

- intern UTC; Anzeige `Europe/Berlin`  
- Constraints, Indizes, Transaktionen, Retention, Migration  
- Roh-/Test-/Produktionsdaten strikt trennen  

## 5. Aviation/GIS-Standards

- CRS, Projektion, Höhenreferenz, Einheiten, Quelle, Lizenz dokumentieren  
- GeoJSON: WGS84 Lon/Lat RFC 7946; Rendering oft EPSG:3857 – nicht verwechseln  
- ADS-B = Beobachtung, keine automatische Ursache/Notfall-Aussage  
- unplausible Sprünge, alte Daten, Coverage-Lücken markieren/verwerfen  
- private Empfangs-/Hausstandorte nie exakt ausgeben  
- Karte braucht Attribution + Listenalternative  

## 6. API-/Integrations-Standards

Jede API dokumentiert:

```text
version, method, auth, input limits, pagination,
response schema, status codes, timeout, retry/backoff,
rate limit, cache TTL, fallback, monitoring
```

Statuscodes mind.: 400/401/403/404/409/422/429/5xx.  
Webhooks: Signatur, Replay-Schutz, Idempotenz.  
**Unbekannter Publish-Status → kein Auto-Retry-Publish.**

## 7. Security- und Datenschutz-Standards

- Least Privilege, Secret Stores, sichere Defaults  
- Eingabevalidierung, CSP, CORS-Allowlist, TLS, Rate-Limits  
- Dependency-Prüfung vor Upgrade  
- Logs minimal, maskiert  
- Meta/Instagram-Secrets lokal, nie in Git  
- EXIF aus öffentlichen Bildern entfernen (Zielbild/Content)  
- keine privaten Kameras/Netzwerkadressen öffentlich  

## 8. Test- und Betriebs-Standards

| Ebene | Beispiele |
|---|---|
| Statisch | Lint, Typen, Format, `git diff --check` |
| Unit | pure Logik, Parser, Statusübergänge |
| Integration | API+DB, Jobs, externe Mocks |
| UI/E2E | Formulare, Karte, mobile Pfade |
| Negativ | Auth, Limits, Timeout, ungültige Payloads |
| Betrieb | Health vs Readiness, Restore-Test, Smoke |

Metriken: Latenz, Fehlerquote, Datenalter, Queue, Uptime.  
Ausfälle sichtbar als `offline|degraded|stale`.

## 9. Content-/Redaktions-Standards

```text
Recherche → Faktenobjekt → Formulierung → Review → Entwurf → Freigabe → Publish
```

- Primärquellen; keine Spekulation/Dramatisierung  
- keine erfundenen Quellen/Flugdaten  
- sicherheitsrelevante Inhalte nie auto-publish  
- Bildrechte + Attribution; Abgrenzung zu Fraport  

## 10. Konfiguration

- Env-Vars / Secret Store; `.env.example` ohne Geheimnisse  
- Dev/Test/Prod trennen  
- keine maschinenspezifischen privaten Pfade in öffentlichen Dateien  

## 11. Performance

```text
Baseline messen → Engpass beweisen → kleinste Optimierung
→ erneut messen → Budget dokumentieren
```

Begrenzen: Payloads, N+1, Renderzyklen, Bundles, Bilder, Layer, Tiles, Jobs.  
Cache nur mit TTL, Invalidierung und Datenalter-Kennzeichnung.  
Optimierung darf Korrektheit, A11y oder Privacy nicht verschlechtern.

## 12. Abnahme-Matrix (projektweit)

| Pfad | Muss geprüft |
|---|---|
| Happy Path | Kernakzeptanz |
| Leer/ungültig/veraltet | sichtbare Zustände |
| Netz/Timeout/429/5xx | kein Fake-Erfolg |
| Duplikate/Idempotenz | keine Doppelwirkung |
| AuthZ | 401/403 |
| Mobile/Keyboard | bedienbar |
| Karte | Tiles fehlen + Liste |
| Publish | unknown status stoppt |

## 13. Abschluss-Checkliste

- [ ] Standards je betroffener Domäne eingehalten  
- [ ] Verträge versioniert  
- [ ] Negativ- und Betriebsfälle bedacht  
- [ ] Privacy/Secrets geprüft  
- [ ] Messungen statt Vermutungen bei Perf

## 14. Erweiterte Standard-Prozessketten

### 14.1 Neues Datenfeld einführen

```text
Bedarf + Nutzerwert
→ Quelle und Einheit klären
→ observed_at/received_at/quality mitdenken
→ Schema + Migration Expand
→ API-Version/Kompatibilität
→ UI-Zustand für fehlend/stale
→ Tests Positiv/Negativ
→ Doku Vertrag
```

### 14.2 Externen Anbieter wechseln

```text
Research Lizenz/Limits/Kosten
→ Vertrag diff alt vs neu
→ Adapter-Schicht
→ Feature-Flag oder Fallback
→ Negativtests 401/429/5xx/Timeout
→ Privacy/Log-Review
→ Monitoring-Signal
→ Rollback = alter Adapter
```

### 14.3 Statusmodell erweitern

```text
Ist-Zustände listen
→ erlaubte Transitionen definieren
→ unerlaubte Transitionen testen
→ UI-Labels (nicht nur Farbe)
→ Audit/Historie
→ Migration bestehender Rows
```

### 14.4 Logging-Standard

```text
Zeit UTC | level | request/job id | event | status | duration_ms
```

Nie: Tokens, Passwörter, vollständige Auth-Header, exakte Privatkoordinaten,
unmaskierte E-Mails wenn nicht nötig.

### 14.5 Fehlercode-Konvention (API)

| Code | Bedeutung | Client-Verhalten |
|---|---|---|
| 400 | syntaktisch/semantisch falsch | Eingabe korrigieren |
| 401 | nicht authentifiziert | Login/Token |
| 403 | nicht autorisiert | keine Retry-Schleife |
| 404 | Ressource fehlt | leerer Zustand |
| 409 | Konflikt/Idempotenz | Status lesen |
| 422 | Validierung Fach | Feldfehler zeigen |
| 429 | Rate-Limit | Backoff |
| 5xx | Server | Retry begrenzt / degraded |

### 14.6 UTC / Europe/Berlin

- speichern und vergleichen in UTC mit Offset/Z
- anzeigen in Europe/Berlin inkl. Sommerzeit
- Datenalter aus UTC-Differenz berechnen
- Tests mit Winter- und Sommerzeit-Grenzen

### 14.7 Abnahme-Schnellcheck vor Merge

- [ ] Happy Path
- [ ] leer/invalid/stale
- [ ] 401/403/429/5xx/Timeout
- [ ] mobil + keyboard
- [ ] keine Secrets im Diff
- [ ] Vertrag/Doku aktualisiert
- [ ] Rollback benannt

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `05-bestandsaufnahme-und-vertraege.md`
- `06-agenten.md` · `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15-zielbild-bauplan-2.0.md` · `16-zielbild-seiten-und-bedienung.md` · `17-zielbild-module-und-technik.md`

## Dokumentpflege

Bei Verhaltensänderungen Verträge, Agent-Profile, README und dieses Handbuch
gemeinsam aktualisieren. Jede Änderung: Geltungsbereich, Annahmen, Testnachweis,
offene Risiken.
