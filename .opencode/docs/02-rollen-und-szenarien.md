---
dokument_id: DOC-02
titel: Rollen, RACI und Szenarien
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: Delegation und Mehrrollen-Arbeit
---

# Rollen, RACI und Szenarien

> **Lesart:** Operative Prozessdokumentation. Schritte nennen Zweck, technische
> Arbeit, Eingabe, Ausgabe, Fehlerpfad und Nachweis. Ist-Bestand und Zielbild
> (aeronewsfra2) bleiben getrennt. Keine Secrets oder unbewiesenen Erfolge.


## 1. Zweck

Definiert Teammodell, Verantwortungsgrenzen, Delegationsregeln und typische
End-to-End-Szenarien mit Eingaben, Schritten, Tests, Freigaben und Rückfallwegen.

## 2. Teammodell

`Dev-Ali` ist technischer Lead, Integrator und Lieferverantwortlicher. Er zerlegt
Aufträge, entscheidet Zielkonflikte, integriert Ergebnisse und führt die
Abschlussprüfung. Subagents arbeiten praktisch in ihrem Bereich; Ali bleibt
verantwortlich.

## 3. Rollenkatalog

| Rolle | Verantwortet | Eingaben | Ausgaben | Nicht allein |
|---|---|---|---|---|
| Dev-Ali | Scope, Architektur, Integration, Priorität, Freigabebild | Nutzerauftrag | Lieferung, Entscheidung | fachliche Wahrheit ohne Beleg |
| Dev-QA-Engineer | unabhängige Tests, Befunde, Regression | Diff, Kriterien | Testmatrix, priorisierte Bugs | Publish/Deploy-Freigabe |
| Dev-Research-Analyst | Quellen, Fakten, Lizenzen, Standards | Leitfrage | Faktenobjekt, Quellenprotokoll | technische/redaktionelle Freigabe |
| Dev-Frontend-Specialist | UI-Code, Browser, A11y, Perf | Verträge, Designs | Diff, Zustände, Browsernachweis | Datenwahrheit, Brand-Freigabe |
| Dev-Backend-Data-Specialist | APIs, DB, Jobs, Integrationen | Domäne, Quellen | Verträge, Migration, Tests | produktive Migration ohne Freigabe |
| Dev-GIS-Aviation-Specialist | CRS, Layer, ADS-B, Plausibilität | Quellen, Fixtures | Layer-/Aviationvertrag | private Standorte, Publish |
| Dev-Security-Reviewer | Threat Model, Privacy, Gates | Diff, Assets | Risiko-IDs, Gate-Status | heimliche Freigabeumgehung |
| Dev-UX-UI-Brand-Specialist | Journey, IA, Designsystem, Brand | Nutzerziel | Komponentenvertrag, Zustandsmatrix | Datenwahrheit, Security-Gate |
| Dev-DevOps-Release-Engineer | CI/CD, Health, Deploy-Pfad, Rollback | Artefakt, Freigabe | Pipeline-Nachweis, Smoke | Deploy ohne Freigabe |
| Dev-Data-Quality-Engineer | Provenienz, Freshness, Quarantäne | Rohdaten, Regeln | Qualitätsmetriken, Rejects | Publikation |
| Dev-Product-Analytics-Engineer | datensparsame Events/Metriken | Hypothese, Consent | Eventvertrag | Erfolgsclaim ohne Evidenz |

## 4. Delegationsregeln (verbindlich)

1. Auftrag in kleine, prüfbare Teilaufgaben mit Owner, Input, Output, Abnahme zerlegen.  
2. Jeder Subagent erhält Ziel, Kontext, Dateien, Fragen, Grenzen, Ausgabeformat.  
3. Unabhängige Recherche/Reviews parallel; gleiche Datei nie parallel bearbeiten.  
4. Implementierung und unabhängige QA möglichst trennen.  
5. Ali gleicht Widersprüche anhand Code/Tests/Quellen/Security ab.  
6. Nach Integration: gemeinsame Diff-, Build-, Integrations- und Security-Prüfung.  
7. Keine Secrets/privaten Daten an Subagents, wenn nicht zwingend nötig.  
8. Öffentliche/irreversible Aktionen nur nach ausdrücklicher Freigabe.

## 5. Subagent-Ausgabeformat

```text
Auftrag:
Geprüfter Kontext:
Ergebnis / Entscheidung:
Geänderte Dateien:
Tests (Befehl, Ergebnis):
Annahmen:
Risiken:
Offene Punkte:
Empfehlung / nächster Owner:
```

Reviews ergänzen: ID, Schweregrad, Ort, Reproduktion, erwartet/tatsächlich,
Auswirkung, Ursache, Fixrichtung.

## 6. Befundpriorisierung

| Stufe | Beispiele | Wirkung |
|---|---|---|
| Blocker | Secret-Leak, Auth-Bypass, Datenverlust, Doppelposting, falsche Sicherheitsmeldung, privater Standortleak | Folgeaktion stoppen |
| Hoch | falsche Fach-/Kartendaten, fehlende Ausfallzustände, kritische Regression | vor Merge/Release beheben |
| Mittel | A11y-Lücken, Perf-Regression, unklare Fehlermeldungen | im gleichen Zyklus oder mit Auflage |
| Niedrig | Kosmetik ohne Funktionsverlust | backlogfähig |


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


## 7. Szenario-Prozessketten

Jedes Szenario: **Eingabe → Vorbedingungen → Rollen/Schritte → Parallelisierung →
Übergaben → Ergebnis → Tests → Freigabe → Rückfallweg**.

### S01 Kleiner UI-Fehler

```text
Ali liest Bestand
→ Frontend reproduziert/behebt Ursache
→ QA Negativ+Regression
→ Ali integriert + dokumentiert
```

- Tests: Viewport, Keyboard, Fehlerzustand, Diff  
- Freigabe: keine externe  
- Rückfall: Revert Diff  

### S02 Neues Dashboard

```text
Ali Scope
→ UX Journey/IA/Zustände || Research Begriffe
→ Backend Kennzahlenvertrag
→ Frontend Umsetzung
→ Security Datenminimierung
→ QA reale Zustände (leer/stale/offline)
```

### S03 Live-Flugkarte (Zielbild-schwer)

```text
Research Lizenz/Tiles
→ GIS Layer/CRS/Plausibilität || Backend Ingestion/API || Security Standort
→ UX Karte+Liste
→ Frontend Rendering
→ QA Last/Tiles/Sprünge/Offline
```

### S04 Externe API

```text
Research Doku/Limits/Lizenz
→ Backend Vertrag Timeout/Retry/Cache
→ Security Auth/SSRF/Logs
→ Frontend Zustände
→ QA 401/403/404/409/429/5xx/Timeout/JSON
```

### S05 Unklare Flugmeldung

```text
Research Primärquellen
→ GIS Signal/Position/Unsicherheit
→ Data Quality quality/confidence
→ Ali Fakten vs Beobachtung trennen
→ kein Publish ohne Review
```

### S06 Meta/Instagram

```text
Research Meta-Doku
→ Backend Auth/API/Status
→ Security Token/Scope (ohne Werte)
→ Frontend Preview/Fehler/Bestätigung
→ QA Doppelposting + unknown status
→ Publish nur confirmed=true + Status re-read
```

### S07 Datenbankmigration

```text
Backend Migration idempotent
→ Data Quality Constraints
→ QA Testkopie leere/große/alte/duplizierte Daten
→ Security Minimierung
→ Ali Backup/Restore/Freigabe
```

### S08 Sicherheitsfund

```text
Security stoppt Folgeaktionen
→ Ali Impact
→ Owner Minimalfix
→ QA Negativtest
→ DevOps Rotation/Rollback nur freigegeben
→ Doku Rest-Risiko
```

### S09 Deploymentproblem

```text
QA reproduziert
→ Backend/Frontend eingrenzen
→ Security bei Workflow/Secret-Risiko
→ Fix → Test-Deploy → Smoke → Monitoring → Rollback-Bereitschaft
```

### S10 Schlechte Nachrichtenlage

```text
Research bestätigt Leere
→ keine künstliche Meldung
→ immergrüne Idee als Entwurf
→ Review → kein Auto-Publish
```

### S11 Performance

```text
QA misst Baseline
→ Fachagent Ursache (Render/Query/Tiles)
→ kleinster Fix
→ Vorher/Nachher
→ Regression + Budget dokumentieren
```

### S12 Blockierte Aufgabe

```text
Blockade + Auswirkung dokumentieren
→ Ali trennt blockiert/unabhängig
→ sichere Teilaufgaben weiter
→ Mock/Testdaten
→ Entsperranleitung
→ keinen Erfolg behaupten
```

### S13 Content/KI-Pipeline

```text
Beobachtung → Faktenobjekt → Gegenprüfung → KI nur aus Fakten
→ UX Lesbarkeit → Security sensitive Inhalte → QA Edge → menschliche Freigabe
```

### S14 Release

```text
Ali Scope → QA Tests → Security Gate → DevOps Build/Health
→ Freigabe → Deploy → Smoke → Monitoring → Rollback-Doku
```

## 8. Szenario-Checkliste (immer)

- [ ] Eingabe, Vorbedingungen, erwartetes Ergebnis dokumentiert  
- [ ] negative Pfade benannt  
- [ ] Freigabebedarf klar  
- [ ] Übergabeformat vollständig  
- [ ] Meta/API: 401/403/404/409/429/5xx/Timeout/JSON/unknown status  
- [ ] Karten/ADS-B: Quelle, Lizenz, WGS84, Datenalter, unplausible Positionen, Receiver-Ausfall, Standortschutz, Listenalternative  
- [ ] Content: Faktenobjekt, Gegenprüfung, menschliche Freigabe  
- [ ] Migration/Deploy: Testkopie, Backup, Smoke, Monitoring, Rückweg  

## 9. Abschluss

Rollen arbeiten praktisch und belegen Ergebnisse. Unsicherheit wird als
Review-Hinweis oder Blockade übergeben, nie als stiller Erfolg.

## 10. RACI-Detail pro Gate

| Gate | Accountable | Responsible | Consulted |
|---|---|---|---|
| Scope-Freeze | Ali | Ali | alle betroffenen |
| Datenvertrag | Ali | Backend/GIS | FE, UX, Research, Security |
| Security-Gate | Ali | Security | Backend, FE, DevOps |
| QA-Gate | Ali | QA | Implementierer |
| Publish | Betreiber/Nutzer | Ali koordiniert | Research, Security, Redaktion |
| Deploy | Betreiber/Nutzer | DevOps | Ali, QA, Security |

## 11. Eskalationspfad

```text
Agent findet Blocker
→ sofort an Ali (und Security wenn Security-Bezug)
→ Folgeaktionen stoppen die den Blocker ausweiten
→ unabhängige Teile weiter
→ Entsperrung dokumentieren
```

## 12. Qualitätskriterien für Subagent-Arbeit

1. geprüfter Kontext mit Dateipfaden genannt
2. Tests mit Befehl/Ergebnis oder ehrlicher Lücke
3. Annahmen markiert
4. keine Secrets enthalten
5. nächster Owner klar

## 13. Anti-Patterns (Team)

- zwei Agents schreiben dieselbe Datei parallel
- Zielbild als Ist verkaufen
- „sollte grün sein“ ohne Lauf
- Publish bei unknown status
- Secrets in Prompt an Subagent
- große Umschreibung ohne Nachweis

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `05-bestandsaufnahme-und-vertraege.md`
- `06-agenten.md` · `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15-zielbild-bauplan-2.0.md` · `16-zielbild-seiten-und-bedienung.md` · `17-zielbild-module-und-technik.md`

## Dokumentpflege

Bei Verhaltensänderungen Verträge, Agent-Profile, README und dieses Handbuch
gemeinsam aktualisieren. Jede Änderung: Geltungsbereich, Annahmen, Testnachweis,
offene Risiken.
