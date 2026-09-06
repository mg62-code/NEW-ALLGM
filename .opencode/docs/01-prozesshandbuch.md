---
dokument_id: DOC-01
titel: Prozesshandbuch – End-to-End Entwicklung und Betrieb
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: alle Entwicklungs-, Content-, Betriebs- und Incident-Aufgaben
---

# Prozesshandbuch – End-to-End Entwicklung und Betrieb

> **Lesart:** Dieses Dokument ist operative Prozessdokumentation. Jeder Schritt
> nennt Zweck, technische Detailarbeit, Eingaben, Ausgaben, Fehlerpfade und
> Nachweis. Ist-Bestand und Zielbild (aeronewsfra2) bleiben strikt getrennt.
> Keine Secrets, privaten Standorte oder unbewiesenen Erfolge.


## 1. Zweck und Geltungsbereich

Dieses Handbuch beschreibt den **verbindlichen Ablauf** von der Anfrage bis zum
Betrieb für Entwicklung, Fehlerbehebung, Recherche, Design, Datenarbeit,
Automatisierung, Tests, Deployment und Wartung. Es stellt sicher, dass Agents
wie ein professionelles Team arbeiten und nicht nur Codefragmente erzeugen.

**Gilt für:** Ist-System (lokaler FastAPI/Instagram-Connector) und geplante
2.0-Funktionen. Zielbild-Schritte sind als *Zielbild* markiert und erst nach
explizitem Auftrag umzusetzen.

**Gilt nicht für:** automatische Veröffentlichung, produktive Secret-Rotation
oder Live-Deployments ohne Freigabe.

## 2. Rollen und Verantwortung

Primärowner: `Dev-Ali` (Accountable). Fachrollen liefern R-Arbeit in ihrem
Bereich. Details: `02-rollen-und-szenarien.md`, `06-agenten.md`,
`14-prozesshandbuch-teamkoordination.md`.


| Aktivität | Ali | QA | Research | Frontend | Backend | GIS | Security | UX |
|---|---|---|---|---|---|---|---|---|
| Auftrag klären | A/R | C | C | C | C | C | C | C |
| Bestand prüfen | A | C | C | R | R | R | C | C |
| Vertrag definieren | A | C | C | C | R | C | C | C |
| Implementieren | A | I | I | R | R | R | I | C |
| Security-Gate | A | C | I | C | C | C | R | I |
| Unabhängige QA | A | R | I | C | C | C | C | C |
| Freigabe extern | A* | I | I | I | I | I | C | I |
| Betrieb/Rollback | A | C | I | C | R | C | C | I |

\* Externe/irreversible Freigabe nur mit ausdrücklicher Nutzer-/Betreiberbestätigung.
A=Accountable, R=Responsible, C=Consulted, I=Informed.


## 3. Eingänge, Vorbedingungen, Outputs

### Eingänge (Auftragspaket)

1. Nutzerziel und erwartetes beobachtbares Ergebnis  
2. Scope, Nicht-Ziele, Muss/Soll/Kann  
3. betroffene Systeme/Dateien/Vertrauenszonen  
4. Datenquellen, Lizenzen, Datenschutzgrenzen  
5. Akzeptanzkriterien und Risiko-/Freigabebedarf  
6. Zeit-/Umgebungsgrenzen  

### Vorbedingungen

- Arbeitsverzeichnis und Git-Status bekannt  
- keine Secrets im Chat/Commit geplant  
- Testdaten isolierbar  
- Ist vs. Zielbild geklärt  

### Outputs (Lieferpaket)

- geänderte Dateien + Diff-Kontrolle  
- Verträge (API/Daten/UI/Event) falls betroffen  
- Tests mit Befehl und echtem Ergebnis  
- nicht verifizierte Punkte, Annahmen, Risiken  
- Rollback und nächster Owner/Schritt  

## 4. Begriffe und Statusmodelle

| Begriff | Definition |
|---|---|
| Ist-Bestand | tatsächlich vorhandener Code/Betrieb |
| Zielbild | geplant in aeronewsfra2 / Bauplan 2.0 |
| Faktenobjekt | validierte Aussage mit Quelle und Zeit |
| Beobachtung | ADS-B/Signal ohne automatische Wahrheit |
| Entwurf | speicherbar, nicht öffentlich |
| Publish | freigabepflichtige öffentliche Aktion |
| stale | Daten vorhanden, aber zu alt für „live“ |
| degraded | Teilfunktion eingeschränkt |
| offline | Quelle/Dienst nicht erreichbar |

### Verarbeitungsstatus (Content/Daten)

`raw → validated → candidate → review → verified → scheduled → published → corrected|archived`

### Betriebsstatus (Anzeige)

`ok | degraded | stale | offline | unknown`

## 5. Prozessübersicht

```text
P01 Auftrag
 → P02 Bestandsaufnahme
 → P03 Diagnose/Design
 → P04 Verträge fixieren
 → P05 Umsetzung (vertikaler Schnitt)
 → P06 Verifikation
 → P07 Security-/Fach-Gates
 → P08 Abschlussprüfung
 → P09 Dokumentation/Übergabe
 → P10 Betrieb/Monitoring (falls freigegeben)
```

Parallel möglich: Research, Threat-Model, Testplanung, UX-Journey – solange
keine Dateikonflikte und Verträge stabil bleiben.


### Wie Prozessschritte zu lesen sind

Jeder nummerierte Schritt enthält:

| Feld | Bedeutung |
|---|---|
| Zweck | warum der Schritt existiert |
| Arbeit | konkrete technische oder fachliche Tätigkeiten |
| Eingabe | benötigte Artefakte/Daten |
| Ausgabe | erzeugte Artefakte/Daten |
| Fehler/Ausnahme | typische Fehlschläge und Reaktion |
| Nachweis | Test, Messung, Log oder Review |
| Owner | primär verantwortliche Rolle |


## 6. Detaillierte Prozessschritte

### P01 – Auftrag schärfen

| Feld | Inhalt |
|---|---|
| Zweck | messbare Aufgabe statt vager Wunsch |
| Arbeit | Ziel, Nutzer, Muss/Soll/Kann, Nicht-Ziele, Akzeptanzkriterien, Risiken, Freigabebedarf, Rollback skizzieren; Annahmen markieren |
| Eingabe | Nutzeranfrage, Kontext |
| Ausgabe | Auftragsblatt (kurz) |
| Fehler | unklare Sicherheitsentscheidung → gezielte Frage; sonst reversible Annahme |
| Nachweis | Akzeptanzkriterien sind beobachtbar formuliert |
| Owner | Dev-Ali |

**Technische Mindestfelder Auftragsblatt**

```text
problem:
user_value:
must/should/could/wont:
acceptance_criteria: []
systems_trust_zones: [browser, local_api, sqlite, meta, receiver, pages]
data_sources:
risks:
approval_needed: [none|publish|deploy|migration|secret]
rollback_idea:
assumptions: []
```

### P02 – Bestandsaufnahme

| Feld | Inhalt |
|---|---|
| Zweck | nichts blind neu bauen |
| Arbeit | `git status`; README; `.opencode/docs`; Agent-Profile; Konfig; Pakete; Routen; Tests; Aufrufer/Abhängigkeiten; Ist vs. Zielbild trennen |
| Eingabe | Auftragsblatt |
| Ausgabe | Ist-Karte, betroffene Dateien, vorhandene Lösungen |
| Fehler | fremde lokale Änderungen → nicht anfassen; melden |
| Nachweis | gelesene Pfade und Befunde dokumentiert |
| Owner | Dev-Ali + Fachrolle |

**Checkliste Bestand**

1. Branch, Status, Diff, letzte relevante Commits  
2. Start-/Test-/Build-Befehle  
3. Datenmodelle, APIs, Workflows, Secrets-Vorlagen (ohne Werte)  
4. UI-Zustände und Fehlertexte  
5. vorhandene Tests und Lücken  
6. aeronewsfra2 nur als Zielreferenz markieren  

### P03 – Diagnose und Design

| Feld | Inhalt |
|---|---|
| Zweck | Ursache oder Architektur vor Code |
| Arbeit | Fehler: reproduzieren, messen, Hypothesen, kleinster Ursachentest. Feature: Datenfluss, Zustände, Rechte, Migration, Testplan, Rollback |
| Eingabe | Ist-Karte, Logs (ohne Secrets), Symptom |
| Ausgabe | Ursachenbeweis oder Lösungsentwurf |
| Fehler | nur Symptom-Workaround → als Workaround kennzeichnen |
| Nachweis | Repro-Schritte oder Architekturskizze |
| Owner | Fachrolle; Ali entscheidet |

### P04 – Verträge fixieren

| Feld | Inhalt |
|---|---|
| Zweck | stabile Schnittstellen vor Implementierung |
| Arbeit | API-/Daten-/UI-/Event-/Fehlervertrag; Statuscodes; Limits; Timeout/Retry; UTC; quality/confidence; Idempotenz |
| Eingabe | Design |
| Ausgabe | versionierter Vertrag |
| Fehler | unklare Quelle/Lizenz → Research; Privacy-Risiko → Security |
| Nachweis | Vertrag im Übergabeformat referenziert |
| Owner | Backend/Frontend/GIS/UX je Schnittstelle |

**Minimaler Datenvertrag**

```text
source, observed_at(UTC), received_at(UTC), quality, confidence,
processing_status, payload(minimiert, validiert), idempotency_key
```

### P05 – Umsetzung (kleiner vertikaler Schnitt)

| Feld | Inhalt |
|---|---|
| Zweck | nutzbares Teilergebnis statt Big-Bang |
| Arbeit | Code+Tests+Doku synchron; Validierung an Grenze; Timeouts; Retries begrenzt; sichtbare Fehler; keine Fake-Erfolge |
| Eingabe | Vertrag |
| Ausgabe | Diff, lauffähiger Schnitt |
| Fehler | Blockade → unabhänge Teile fertig, Entsperrung dokumentieren |
| Nachweis | lokaler Test/Build nach Schritt |
| Owner | Implementierungsrolle |

**Umsetzungsregeln**

1. kleinste sichere Änderung  
2. bestehende Konventionen nutzen  
3. externe Eingaben untrusted  
4. Logs ohne Secrets/PII/Standorte  
5. Feature-Flag oder Reverse-Diff als Rollback  

### P06 – Verifikation

| Feld | Inhalt |
|---|---|
| Zweck | Verhalten beweisen |
| Arbeit | Syntax/Typen → Unit → Integration/API → UI/E2E → A11y/Perf/Security-Basis; Positiv+Negativ |
| Eingabe | Diff, Testplan |
| Ausgabe | Testergebnis pro Befehl |
| Fehler | rot → fix → gleiche Prüfung wiederholen |
| Nachweis | Befehl, Umgebung, Exit/Result |
| Owner | Implementierer primär; QA unabhängig danach |

**Pflicht-Negativfälle (Auszug)**

leer, ungültig, veraltet, doppelt, timeout, offline, 401/403/404/409/429/5xx,
ungültiges JSON, unbekannter Publish-Status, fehlende Kacheln, unplausible Position.

### P07 – Security- und Fach-Gates

| Feld | Inhalt |
|---|---|
| Zweck | Blocker vor öffentlicher/irreversibler Wirkung |
| Arbeit | Secrets, Auth, XSS/Injection, Standortschutz, Quellen/Lizenzen, Datenalter, Freigabepfade |
| Eingabe | Diff, Threat-Hinweise |
| Ausgabe | Gate: bestanden / mit Auflagen / blockiert |
| Fehler | Blocker stoppt Folgeaktionen |
| Nachweis | Negativtest oder Evidenz |
| Owner | Security + Fachrollen; Ali priorisiert |

### P08 – Abschlussprüfung

| Feld | Inhalt |
|---|---|
| Zweck | Lieferung übergabefähig |
| Arbeit | Funktion, Robustheit, Privacy, UX mobil, Performance, Betrieb, Wartbarkeit, Diff auf Debug/Secrets, `git diff --check` |
| Eingabe | grüne Kernprüfungen |
| Ausgabe | Go/No-Go intern |
| Fehler | Restfehler priorisieren; Kosmetik zuletzt |
| Nachweis | Checkliste abgehakt |
| Owner | Dev-Ali |

### P09 – Dokumentation und Übergabe

| Feld | Inhalt |
|---|---|
| Zweck | Nachvollziehbarkeit |
| Arbeit | README/API/Setup/Betrieb aktualisieren; nur echte Aktionen melden |
| Eingabe | Diff + Tests |
| Ausgabe | Übergabebericht |
| Fehler | „sollte funktionieren“ ohne Test → verboten |
| Nachweis | Übergabefelder vollständig |
| Owner | Dev-Ali |

### P10 – Betrieb und Monitoring (nur freigegeben)

| Feld | Inhalt |
|---|---|
| Zweck | stabiler Lauf und schnelle Eindämmung |
| Arbeit | Health/Readiness, Smoke, Logs, Metriken, Alerts, Rollback-Bereitschaft |
| Eingabe | Release-Freigabe |
| Ausgabe | Betriebsstatus, Incident-Runbook-Eintrag bei Bedarf |
| Fehler | unknown Publish → nicht wiederholen |
| Nachweis | Smoke-Ergebnis, Monitoring-Signale |
| Owner | DevOps/Backend; Ali freigibt |

## 7. Spezialprozessketten

### 7.1 Requirements

```text
Problem → Stakeholder/Nutzer → Muss/Soll/Kann → Akzeptanzkriterien
→ Daten-/Fehlervertrag → Risiken → vertikaler Schnitt → Review → Umsetzung
```

### 7.2 Fehlerdiagnose

```text
Symptom sichern → Kontext (Version, Diff, Logs) → reproduzieren
→ messen → Hypothesen → kleinster Test → Ursache beweisen → Fix
→ Regressionstest → Gesamttest → Diff → Übergabe
```

### 7.3 Frontend-Funktion

```text
Nutzerziel → Journey → Bestand → Datenvertrag → Markup/CSS/JS
→ responsive Zustände → A11y → Fehler/Offline → Tests → Perf → Doku
```

### 7.4 Backend/API

```text
Domäne → versionierter Vertrag → Auth/Limit → Validierung → Logik
→ Transaktion/Idempotenz → Cache/Event → Fehlerpfad → Migrationstest
→ Observability → Rollback
```

### 7.5 GIS/ADS-B

```text
Quelle/Lizenz → Schema/CRS/Einheiten → Zeit UTC → Plausibilität/Datenalter
→ Unsicherheit markieren → Layer/API → Standortschutz → Last/Offline-Test
→ Listenalternative
```

### 7.6 Content/KI

```text
Beobachtung → Faktenobjekt → Primärquelle/Gegenprüfung → Ereigniskandidat
→ KI-Formulierung nur aus Fakten → Review → Entwurf → Freigabe
→ Veröffentlichung → Korrekturhistorie
```

### 7.7 Instagram/MCP

```text
Verbindung status → Caption/Image validieren → Draft speichern
→ Preview/Status lesen → explizite confirmed=true → Publish einmal
→ Status erneut lesen → bei unknown STOP (kein Retry-Publish)
```

### 7.8 Release/Deployment

```text
Diff → Tests/Build → Artefakt → Zielumgebung prüfen → Test-Deploy
→ Smoke/Health/Logs → Freigabe → Prod-Deploy → Monitoring
→ Rollback-Bereitschaft dokumentieren
```

### 7.9 Incident

```text
Erkennen → Eindämmen (Jobs pausieren, Publish stoppen) → Beleg sichern
→ Impact → Ursache → Fix → Smoke → kontrollierter Wiederanlauf
→ Lessons Learned (ohne Secrets)
```

### 7.10 Datenmigration

```text
Ist-Schema → Zielmodell → Backup → idempotente Migration → Testkopie
→ Constraints/Zähler → App-Test → Freigabe → kontrolliert anwenden
→ Verify → Rollback/Roll-forward Plan
```

### 7.11 Schlechte Datenlage / leere Nachrichtentage

```text
Quellenlage prüfen → keine künstliche Story → transparent melden
→ optional immergrüne Idee als Entwurf → Review → kein Auto-Publish
```

## 8. Qualitätsgates und Definition of Done

Aufgabe fertig, wenn:

1. Akzeptanzkriterien beobachtbar erfüllt  
2. relevante Positiv- und Negativtests ausgeführt oder als nicht verifiziert benannt  
3. Fehlerpfade und Status (`offline/degraded/stale`) behandelt  
4. Security/Privacy geprüft; keine Secrets/PII/exakten Privatstandorte  
5. Dokumentation und Übergabe vollständig  
6. Commit/Push/Deploy/Publish nur bei Auftrag + Freigabe  

## 9. Negativfälle und Stop-Regeln

| Fall | Reaktion |
|---|---|
| Secret-Leak-Verdacht | stoppen, nicht kopieren, eskalieren, Rotation durch Betreiber |
| unbekannter Publish-Status | nicht erneut posten |
| widersprüchliche Flugursache | Beobachtung + Unsicherheit, kein Notfall-Claim |
| fehlende Testumgebung | Mock + Lücke dokumentieren |
| fremde Worktree-Änderungen | unangetastet lassen |
| Zielbild vs. Ist verwechselt | Korrektur in Doku/Übergabe |

## 10. Tool-Kette (Standard)

```text
git status → glob → read → grep → Plan/Vertrag → edit
→ bash Tests/Build → git diff --check → status/diff → Übergabe
```

Details: `03-opencode-und-tools.md`.

## 11. Übergabeformat

```text
Auftrag:
Nutzerwert / Akzeptanzkriterien:
Geprüfter Kontext / Ist vs Zielbild:
Entscheidung:
Annahmen:
Verträge (API/Daten/UI/Event):
Geänderte Dateien:
Tests (Befehl | Szenario | Ergebnis):
Nicht verifiziert:
Risiken / Privacy / Security:
Rollback:
Empfehlung / nächster Owner:
```

## 12. Abschluss-Checkliste

- [ ] Auftragsblatt und Akzeptanzkriterien klar  
- [ ] Bestand und Git-Status geprüft; Fremdänderungen respektiert  
- [ ] Ist/Zielbild getrennt  
- [ ] Verträge und Statusmodelle definiert  
- [ ] Implementierung klein, getestet, ohne Fake-Erfolge  
- [ ] Negativfälle und Gates erledigt  
- [ ] Diff/Secrets/Privacy sauber  
- [ ] Übergabe mit echten Testergebnissen  
- [ ] Keine externe Aktion ohne Freigabe  

## Verwandte Dokumente

- `00-index.md` – Dokumentenkarte und Lesereihenfolge
- `01-prozesshandbuch.md` – übergreifender End-to-End-Prozess
- `05-bestandsaufnahme-und-vertraege.md` – Datenverträge und Freigaben
- `06-agenten.md` – Agentenregister
- `14-prozesshandbuch-teamkoordination.md` – Rollenübergaben
- `15-zielbild-bauplan-2.0.md` – Zielarchitektur (nicht Ist)
- `16-zielbild-seiten-und-bedienung.md` – Seiten-/Bedienprozesse Zielbild
- `17-zielbild-module-und-technik.md` – Modulverträge Zielbild
- `18-prozesskatalog.md` – vollständiger Prozesskatalog

## Dokumentpflege

Bei Verhaltensänderungen: betroffene Verträge, Agent-Profile, README und dieses
Handbuch im selben Arbeitsgang aktualisieren. Jede Änderung nennt Geltungsbereich,
Annahmen, Testnachweis und offene Risiken.
