---
dokument_id: DOC-05
titel: Bestandsaufnahme, Datenverträge und Betriebsleitfaden
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: Architektur, Integration, Freigaben, Betrieb
---

# Bestandsaufnahme, Datenverträge und Betriebsleitfaden

> **Lesart:** Operative Prozessdokumentation. Schritte nennen Zweck, technische
> Arbeit, Eingabe, Ausgabe, Fehlerpfad und Nachweis. Ist-Bestand und Zielbild
> (aeronewsfra2) bleiben getrennt. Keine Secrets oder unbewiesenen Erfolge.


## 1. Zweck

Hält den **geprüften Ist-Bestand**, Systemgrenzen, Datenverträge, Freigabematrix
und Betriebsabläufe fest. Verhindert, dass Zielbild-Funktionen als implementiert
ausgegeben werden.

## 2. Geprüfter Bestand (Stand Doku 2.0)

Geprüft wurden u. a.:

- `.opencode/docs/`, `.opencode/agent/`, `opencode.json`  
- `README.md`, Fachquellen im Projektstamm  
- erreichbare HTML unter `aeronewsfra2/` (PDFs inventarisiert; ohne verlässliche
  Textextraktion nicht als inhaltlich bestätigt)  
- lokaler Python/FastAPI-Instagram-Connector als **aktueller Kern**  

**Ist:** lokaler Connector (Formulare, SQLite, Meta-API-Anbindung, MCP).  
**Zielbild:** Website, echte Karte, ADS-B-Plattform, Redaktion, Distribution
(siehe `15`–`17`).

## 3. Vertrauenszonen

```text
[Browser/UI] --kein Secret--> [Public Pages/static]
       |
       v
[Local FastAPI 127.0.0.1] <--> [SQLite/media local]
       |
       +--> [Meta/Instagram API]   (Tokens nur Server/lokal)
       +--> [Receiver Upload]      (Zielbild; signiert, ausgehend)
       +--> [Tile/Wetter/OpenSky]  (untrusted responses)
```

Regeln:

1. Connector lokal, nicht öffentlich exponieren.  
2. Browser erhält keine Meta- oder Receiver-Secrets.  
3. Website, API, Receiver, Instagram = getrennte Zonen.  
4. Rohdaten, normalisierte Daten, Kandidaten, Entwürfe, Publiziertes = getrennte Lebenszyklen.  


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


## 4. Minimaler Datenvertrag (verbindlich)

Externe Eingaben an der Systemgrenze validieren.

```text
source: provider | own_adsb | manual | meta | other
observed_at: UTC
received_at: UTC
quality: valid | degraded | stale | rejected
confidence: low | medium | high | numeric_score
processing_status: raw|validated|candidate|review|verified|scheduled|published|archived
payload: validated, minimized fields
idempotency_key: stable
```

- unplausibel/zu alt/widersprüchlich → markieren oder verwerfen  
- öffentliche APIs: minimiert, lizenzkonform, Limit, Pagination, Datenalter  
- Zeiten intern UTC, Anzeige Europe/Berlin  

## 5. Content-/Event-Statusmodell

| Status | Bedeutung | Öffentlich? |
|---|---|---|
| detected/raw | technisch gesehen | nein |
| validated | schema-ok | nein |
| candidate | interessant | nein |
| review | Prüfung läuft | nein |
| verified | redaktionell ok | noch nicht |
| scheduled | zeitgeplant | nein |
| published | live | ja |
| corrected | korrigierte Version | ja/teilweise |
| archived | aus Listen, Historie hält | nein/ja je Policy |

## 6. Freigabematrix

| Aktion | Auto? | Freigabe |
|---|---|---|
| Isolierter Mock/Test | ja | keine Prod-Daten |
| Validierten Entwurf speichern | ja | Review-Hinweis bei Unsicherheit |
| Instagram-Entwurf vorbereiten | ja | vor Publish |
| Instagram veröffentlichen | nein | explizite Bestätigung + Statusprüfung |
| Sicherheits-/Notfallinhalt | nein | Fach- + Redaktionsprüfung |
| Produktive Migration/Löschung | nein | Change, Backup, Rückweg |
| Secret-Änderung | nein | berechtigter Betreiber |
| Deployment/Release | nein | Ali + passende Release-Freigabe |

**Unknown Publish-Status → niemals automatisch erneut posten.**  
Rollback = letzter verifizierter Zustand; Belege/Korrekturhistorie nicht löschen.

## 7. Verbindliche Prozessketten (kurz)

- Requirements → Kriterien → Vertrag → Risiken → Schnitt → Tests → Doku  
- Fehler → Repro → Beweis → Fix → Regression → Gesamttest  
- Frontend/UX → Journey → Zustände → A11y → Browser  
- Backend/DB → Vertrag → Auth → Tx/Idempotenz → Migration Testklon  
- GIS/ADS-B → Lizenz → CRS → Plausibilität → Privacy → Last/Offline  
- Content/KI → Faktenobjekt → Gegenprüfung → Review → Freigabe  
- Security/Incident → Asset → Abuse → Eindämmung → Fix → Negativtest  

## 8. Betriebsprozess

### Health vs Readiness

- Health: Prozess lebt  
- Readiness: Abhängigkeiten ok (DB, optional Meta/Receiver)  

### Ausfallanzeige

UI zeigt `offline | degraded | stale` – kein stiller Erfolgsfallback.

### Incident-Kette

```text
Zeitpunkt/Version/Fehlercode sichern
→ riskante Jobs pausieren
→ Doppelposting verhindern
→ Ursache + Datenprüfung
→ Smoke
→ kontrollierter Wiederanlauf
→ Lessons Learned (ohne Secrets)
```

### Wartung

Scope, Backup/Restore, erwartete Wirkung, Monitoring, dokumentierter Rückweg.

## 9. Instagram-Connector-Vertrag (Ist)

Typische sichere Kette:

```text
connection_status → draft speichern → preview → status
→ publish nur confirmed → status erneut
```

Fehlerklassen: 401/403 Token, 404 Media, 429 Rate, 5xx/Timeout, invalid caption/url,
duplicate confirm, unknown status.

## 10. Zielbild-Verträge (nur Planung)

Siehe `15`–`17`. Vor Umsetzung jedes Zielbild-Moduls:

```text
purpose, I/O schema, source/time semantics, error/offline,
privacy/license, tests/acceptance, rollback, owner, monitoring
```

API-Skizze Zielbild (nicht implementiert behaupten):

```text
GET  /api/v1/health
GET  /api/v1/aircraft/live?bbox=
GET  /api/v1/aircraft/{icao24}
GET  /api/v1/tracks/{flight_id}
GET  /api/v1/events
GET  /api/v1/stats/daily
GET  /api/v1/station/status
POST /api/v1/receiver/heartbeat
POST /api/v1/receiver/positions
```

## 11. Übergabeformat

```text
Auftrag, Kontext, Annahmen, Entscheidung, Dateien,
Daten-/Schnittstellenfolgen, Tests+Ergebnis, nicht verifiziert,
Risiken, Rollback, Empfehlung
```

QA-Befund: ID, Schwere, Ort, Repro, erwartet/tatsächlich, Impact, Ursache, Fix.  
Keine irreversiblen Aktionen ohne Freigabe in der Übergabe als erledigt melden.

## 12. Abschluss-Checkliste

- [ ] Ist vs Zielbild explizit  
- [ ] Trust Boundaries beachtet  
- [ ] Datenvertrag vollständig  
- [ ] Freigabematrix eingehalten  
- [ ] Betrieb/Incident-Pfade bedacht

## 13. Erweiterte Betriebs- und Vertragsprozesse

### 13.1 Vertragsänderung (Breaking vs Non-Breaking)

```text
Bedarf
→ Konsumenten listen (FE, Jobs, MCP, Docs)
→ non-breaking? Expand-Feld + Default
→ breaking? Version bump + Migrationsfenster
→ Tests beider Versionen
→ Changelog in Übergabe
```

### 13.2 Instagram-Connector – Zustandsautomat

```text
idle → drafting → draft_saved → previewed → publish_pending
→ published | failed | unknown
```

Regeln:

- `unknown` und `publish_pending` blockieren erneutes Publish
- `failed` erlaubt korrigierten Retry nur nach Status-Klarheit
- Drafts bleiben lokal nachvollziehbar

### 13.3 Datenqualitäts-Quarantäne

```text
validate fail → rejected + reason
plausible warn → degraded + reason
age > threshold → stale
source down → offline
```

Quarantäne-Datensätze nicht in public JSON mischen.

### 13.4 Backup/Restore-Prozess (lokal SQLite)

```text
1. Dienst stoppen oder read-only Fenster
2. Datei-Kopie mit Timestamp
3. Checksum notieren
4. Restore-Test in Kopie-Pfad
5. App gegen Restore starten (Smoke)
6. Ergebnis doku ohne Secret-Inhalte
```

### 13.5 Incident-Schwere

| Stufe | Beispiel | Reaktion |
|---|---|---|
| SEV1 | Secret public, Massen-PII | sofort stop + Rotation |
| SEV2 | Doppelposting, Datenkorruption | Jobs pause + Fix |
| SEV3 | degraded API | Status zeigen + beheben |
| SEV4 | kosmetisch | planen |

### 13.6 Zielbild-Vertrag vor Implementierung (Gate)

Vor Coding einer 2.0-Funktion aus Docs 15–17:

- [ ] Ist-Lücke dokumentiert
- [ ] Modulvertrag (17) ausgefüllt
- [ ] Quelle/Lizenz geklärt
- [ ] Privacy/Standort geprüft
- [ ] Testplan + Rollback
- [ ] Phase/Prio aus Roadmap
- [ ] expliziter Nutzerauftrag für Zielbild-Umsetzung

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `05-bestandsaufnahme-und-vertraege.md`
- `06-agenten.md` · `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15-zielbild-bauplan-2.0.md` · `16-zielbild-seiten-und-bedienung.md` · `17-zielbild-module-und-technik.md`

## Dokumentpflege

Bei Verhaltensänderungen Verträge, Agent-Profile, README und dieses Handbuch
gemeinsam aktualisieren. Jede Änderung: Geltungsbereich, Annahmen, Testnachweis,
offene Risiken.
