---
dokument_id: DOC-11
titel: Prozesshandbuch Backend und Daten
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: APIs, Persistenz, Jobs, Integrationen, Migrationen
---

# Prozesshandbuch Backend und Daten

> **Lesart:** Operative Prozessdokumentation mit technischen Details pro Schritt.
> Ist-Bestand und Zielbild bleiben getrennt. Keine Secrets oder unbewiesenen Erfolge.


## 1. Zweck und Verantwortungsgrenze

Steuert `Dev-Backend-Data-Specialist` bei APIs, Services, Persistenz, Jobs,
Echtzeit, externen Integrationen und Datenqualität. Arbeit bis zu realem,
integriertem Code: Bestand prüfen, Verträge, implementieren, testen, übergeben.
Keine isolierten Beispielrouten; kein Erfolg ohne Ausführung.

**Ist:** lokaler Python/FastAPI-Instagram-Connector, SQLite, Formularrouten, Meta-API.  
**Zielbild:** Website-API, Receiver, Historie, Events – Docs `15`/`17`, nicht automatisch vorhanden.

**Verantwortet:** Backend, Datenmodell, Integrationen, Betriebsverhalten.  
**Geteilt/extern:** redaktionelle Wahrheit, Kartenfachlogik, UX, Security-Freigabe,
produktive Migration.

## 2. Auftrag, Inputs, Outputs

Auftragsblatt: Domäne, Nutzerwert, Muss/Soll/Kann, Nicht-Ziele, Module, Quellen,
Retention, Last, Rechte, Akzeptanz, Migration, Backup, Rollback.  
Eingaben: Code, Schemas, Lizenznachweise, Testdaten, Runtime/DB-Config, Incidents.  
Secrets nie lesen/kopieren/dokumentieren.

**Output an Ali:** Entscheidung, Annahmen, Dateien, OpenAPI/JSON/DB-Vertrag,
Statusmaschine, Migration/Rollback, Tests+Ergebnis, Metriken, nicht verifiziert,
Risiken, Empfehlung.

| Rolle | Vertrag/Zusammenarbeit |
|---|---|
| Ali | Priorität, Integration, Freigabe produktiver Schritte |
| Frontend | stabile Payloads, Lade/Fehler, Limits, Versionierung |
| GIS | ADS-B/GeoJSON-Schema, Alter, CRS, Qualitätsstatus |
| Research | Anbieter, Quellen, Lizenz, Limits, Belege |
| Security | Trust Boundaries, Auth, Secrets, Privacy, Abuse-Tests |
| UX | benötigte Nutzeraktionen |
| QA | unabhängige API-/Integritäts-/Ausfallabnahme |
| Data Quality | Provenienz, Freshness, Quarantäne-Regeln |

## 3. Prozessübersicht

```text
B01 Auftragsblatt
 → B02 Bestand (Routen, Services, SQL, Jobs, Config, Tests)
 → B03 Git-Status / Aufrufer / Schreibpfade
 → B04 Diagnose bei Fehler (Repro → Beweis)
 → B05 versionierter API- + Datenvertrag
 → B06 Statusmaschine + Idempotenzdesign
 → B07 Architektur-Schnitt (Trust Boundaries)
 → B08 Implementierung Validierung/Auth/Logik/Tx
 → B09 externe Calls (Timeout/Retry/Backoff/Fehlerklassen)
 → B10 Cache / Jobs / Queues
 → B11 ADS-B-Ingestion-Regeln (falls Scope)
 → B12 Migration in Testkopie
 → B13 Observability (Health≠Readiness, Logs, Metriken)
 → B14 Tests Unit/API/DB/Job/Migration/Negativ
 → B15 Security-Eskalation bei Bedarf
 → B16 Übergabe + Rollback-Plan
```

## 4. Bestandsaufnahme und Ursachenanalyse

Zuerst Git-Status und Anweisungen; dann README, `opencode.json`, requirements,
App-Start, Routen, Services, DB/SQL, Jobs, Config, Logs (ohne Sensibles), Tests.
Alle Aufrufer, Schreibpfade, Statusübergänge, externe Anbieter suchen. Ist≠Zielbild.

**Fehlerkette:**

```text
Symptom sichern → deterministisch repro
→ Request/Status/Tx/Queue/Log korrelieren
→ Hypothesen → kleinster Ursachentest → Beweis
→ Fix → Regression → Gesamttest
```

Workarounds kennzeichnen. Fremde lokale Änderungen unangetastet.

## 5. Domäne, Datenvertrag, Lebenszyklus

Vor Code – versionierter Vertrag:

- Methode, Version, Auth/Rolle  
- Eingabegrenzen, Pagination/Sort/Filter  
- Antwortschema, Einheiten  
- Statuscodes: 400/401/403/404/409/422/429/5xx  
- Timeout, Retrygrenze, Backoff, Rate-Limit, Cache-TTL, Fallback  
- `source`, `observed_at`, `received_at` UTC, `quality`, `confidence`, `processing_status`  
- validierte/minimierte Payload  
- Lebenszyklus: raw → validated → candidate/review → verified → published → archived  
- Korrektur-/Auditspur  
- Retention, Löschzweck, Indizes, Constraints, Minimierung  

Externe Responses untrusted an Grenze validieren (Schema, Typ, Größe, Encoding,
Zeit, Einheiten, erlaubte Werte). Roh/Test/Prod trennen. KI/UI bestimmen Datenmodell
nicht unkontrolliert.

## 6. Architektur und Planung

Beschreiben: Datenfluss, Trust Boundaries, Nebenwirkungen, State Machine,
Parallelität, Wiederanlauf. Kleinste stack-konforme Lösung (Bestand: Python/FastAPI/SQLite).
Neue Speicher/Queues/Dependencies begründen.

```text
Domäne → Vertrag → Auth → Validierung → Logik → Transaktion
→ Idempotenz → Event/Cache → Fehlerpfad → Tests → Migration → Betrieb
```

Writes: stabile Idempotency Keys, Duplikatregeln, Concurrent Updates, Statusübergänge.
At-least-once annehmen; Exactly-once nicht versprechen. Teilcommit, Absturz, Neustart
im Design.

## 7. Implementierung

- Requests begrenzen und validieren  
- Rechte vor Datenzugriff  
- SQL parametrisiert; Tx mit passender Isolation  
- FK, Unique/Check, Indizes, Pagination  
- keine unbounded Payloads, N+1, unkontrollierte Parallelität, silent drops  
- externe Calls: TLS, Timeouts, Retry nur transient, exp. Backoff, klare Fehlercodes  
- 401/403, 404, 409, 429, 5xx, Timeout, invalid JSON getrennt  
- **unknown Publish-Status → nicht erneut publizieren**  

## 8. Auth, Autorisierung, Security

Least Privilege; sichere Session/Token; CSRF bei Cookie-Formularen; CORS-Allowlist;
Rate- und Size-Limits. Secrets nur sichere Umgebung. Logs maskieren Token, OAuth-Code,
private Pfade, PII. Webhooks: Signatur, Herkunft, Replay, Idempotenz. Security-Befunde
an `Dev-Security-Reviewer` vor riskanter Weiterarbeit.

## 9. Transaktionen, Migrationen, Datenpflege

Migration: idempotent, versioniert, testbar, rücksetzbar oder roll-forward-plan.

```text
Ist-Schema + Backup doku
→ Expand (abwärtskompatible Spalten)
→ Code liest alt+neu
→ Backfill in Testkopie (leer/groß/alt/inkonsistent/doppelt)
→ Constraints/Zähler/Indizes/Queries prüfen
→ Freigabe
→ kontrolliert anwenden
→ Verify
→ später Contract drop
```

Produktive Migration/Löschung/Secret-Änderung brauchen explizite Freigabe.
Retention löscht nicht ungeprüft Belege/Korrekturhistorie. Backup ohne Restore-Test
≠ verifiziert.

## 10. Cache, Jobs, Echtzeit / ADS-B-Ingestion

**Cache:** Keys, TTL, Version, Invalidierung, stale-Kennzeichnung, Stampede-Schutz,
Verhalten bei Cache-Ausfall. Veraltet nie als live.

**Jobs:** Status, Lease/Lock, max Laufzeit, Retry+Backoff, Dead-Letter/manuell,
Idempotenz, graceful shutdown, Backpressure.

**ADS-B-Ingestion (Zielbild-ready):**

```text
Herkunft/Signatur → Roh speichern → Schema → UTC normalisieren
→ Qualität/Sprung/Alter → Duplikate → aktuelles Modell
→ Event-Kandidat (nicht auto-publish)
```

Receiver-Ausfall → `offline`/`stale`, keine synthetischen Live-Daten.

## 11. Tests und Verifikation

Unit, Integration, API, DB, Contract, Job, Migration – isolierte Testdaten.

**Pflicht:** Happy; leer; falsche/zu große Eingabe; bad JSON; 401/403/404/409/422/429/5xx;
Timeout; Provider-Ausfall; Retry-Limit; Duplikat; concurrent writes; Teilcommit;
Neustart; Queue-Stau; Cache-Miss; unknown external status; SQLi-Negativ; Secrets
nicht in Logs; Zeitzonen.

Nachweis: exakter Befehl, Umgebung, Ergebnis, nicht verifizierte externe Teile.
Lokaler Start ≠ Meta-Integrationstest.

## 12. Observability und Betrieb

Health ≠ Readiness. Strukturierte Logs: Zeit, korrelierbare Request/Job-ID, Status,
Dauer – keine Secrets. Metriken: Latenz, Fehlerklasse, Rate-Limits, Datenalter,
Queue, Retry/DLQ, DB-Fehler, Uptime. Alerts mit Runbook, Eindämmung, Rollback.
Graceful Shutdown, Wiederanlauf, doppelte Verarbeitung praktisch testen.

## 13. Rollback und Übergabe

Codefehler → letzter verifizierter Stand. Migration nur mit geprüftem Rückweg
oder Roll-forward. Keine Belege löschen. Externe Unsicherheit → Job pausieren,
Status prüfen, nicht wiederholen.

Übergabe: Vertrag, Statusdiagramm, Migration, Backup/Restore-Nachweis, Monitoring,
Runbook, Rollback, Dateien, QA-/Security-Befunde.

## 14. Abschluss-Checkliste

- [ ] Bestand, Aufrufer, Statusmodell, Trust Boundaries, lokale Änderungen  
- [ ] API/DB-Vertrag mit Version, Limits, Auth, Fehlern, Idempotenz  
- [ ] UTC, Quelle, Alter, Qualität, Retention, Minimierung  
- [ ] Tx, Constraint, Index, Retry, Cache, Job-Neustart, Teilfehler  
- [ ] Migration Testkopie, Backup/Restore-Pfad, Rollback  
- [ ] Security-, QA-, FE-, GIS-Abhängigkeiten  
- [ ] Logs/Metriken/Health ohne Geheimnisse; Diff sauber

## 15. Instagram/Meta-Integrationsprozess (Ist)

```text
Config laden (ohne Secret-Log)
→ connection/health
→ validate caption + image_url
→ persist draft (idempotent)
→ optional preview call
→ publish only if confirmed==true and status not pending/unknown
→ persist provider response + local status
→ on timeout: status=unknown; no auto retry publish
```

## 16. Idempotenz-Muster

| Operation | Key-Vorschlag | Bei Konflikt |
|---|---|---|
| Draft save | hash(caption+image_url+user) | update existing draft |
| Publish | draft_id | return existing publish status |
| Receiver batch | station_id+seq | ignore duplicate |
| Event create | rule_id+icao+time_bucket | merge evidence |

## 17. Anti-Patterns Backend

- Retry auf 401/403
- Publish-Retry bei unknown
- unbounded SELECT ohne Limit
- Schema-Änderung ohne Expand
- Secrets in Exception-Messages
- stille catch-all die Erfolg vortäuschen

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `02-rollen-und-szenarien.md`
- `05-bestandsaufnahme-und-vertraege.md` · `06-agenten.md`
- `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15` · `16` · `17` (nur Planung)

## Dokumentpflege

Verhaltensänderungen erfordern synchrone Updates von Verträgen, Agent-Profilen,
README und diesem Handbuch (Geltungsbereich, Annahmen, Testnachweis, Risiken).
