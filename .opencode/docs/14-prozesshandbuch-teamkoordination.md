---
dokument_id: DOC-14
titel: Prozesshandbuch Teamkoordination
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: Mehrrollen-Arbeit, Gates, Übergaben
---

# Prozesshandbuch Teamkoordination

> **Lesart:** Operative Prozessdokumentation mit technischen Details pro Schritt.
> Ist-Bestand und Zielbild bleiben getrennt. Keine Secrets oder unbewiesenen Erfolge.


## 1. Zweck, Geltung, Leitbild

Regelt Zusammenarbeit aller Dev-Agents unter technischer Leitung von `Dev-Ali`.
Ergänzt `00`–`06` und Fachhandbücher `07`–`13`. Bei Konflikten:
System-/Sicherheitsregeln → Nutzerfreigabe → projektweite Standards → dieses Handbuch.

Teamauftrag: nachvollziehbares, getestetes, rücknehmbares Ergebnis. Jeder Agent
arbeitet praktisch in seinem Bereich; Ali bleibt für Scope, Architektur, Priorität,
Integration, Freigaben und Abschluss verantwortlich.

## 2. Unveränderliche Teamregeln

1. Vor Arbeit: Bestand, Doku, Abhängigkeiten, Git-Status. Fremde lokale Änderungen nie resetten/löschen/überschreiben.  
2. Keine Secrets, Tokens, Passwörter, privaten Netzdaten, exakten Privatstandorte teilen. Existenz/Maskierung prüfbar; Werte nie.  
3. Keine öffentliche/finanzielle/irreversible Aktion ohne ausdrückliche Freigabe (Publish, Deploy, Löschung, Prod-Migration, Secret-Änderung, externe MCP-Aktionen).  
4. Keine erfundenen Quellen, Daten, Tests, Zugriffe, Erfolge.  
5. Roh-, Test-, Mock-, Entwurf-, Prod-Daten trennen; Unsicherheit sichtbar.  
6. Blocker (Secret-Leak, Datenverlust, Auth-Bypass, Doppelposting, falsche Security-Inhalte) stoppen Folgeaktionen.  

## 3. Rollen und Grenzen

| Rolle | Verantwortet | Nicht allein |
|---|---|---|
| Dev-Ali | Auftrag, Architektur, Zerlegung, Integration, Priorität, Freigabebild | fachliche Einzelwahrheit ohne Beleg |
| UX | Journey, IA, Designsystem, Brand, Interaktion, UX-Abnahme | Datenwahrheit, Security, Publish |
| Frontend | UI-Code, Browser, A11y, Perf | fachliche Flugdaten, Markenfreigabe |
| Backend | APIs, Persistenz, Jobs, Integrationen, Migrationen | redaktionelle Aussage, Prod-Migration ohne Freigabe |
| GIS | CRS, Karten, ADS-B, Fluglogik, Unsicherheit | private Standorte, Publish |
| Research | Quellen, Standards, Fakten, Anbieter, Lizenzen | technische/redaktionelle Freigabe |
| Data Quality | Provenienz, Plausibilität, Freshness, Quarantäne | Publikation |
| Security | Threat Model, Privacy, Secrets, Security-Gate | heimliche Freigabeumgehung |
| QA | unabhängige Tests, Befunde, Regression, Abnahme | Schönreden; Prod-Reparatur ohne Auftrag |
| DevOps | Artefakt, CI/CD, Health, Monitoring, Rollback | Deploy ohne Freigabe |
| Analytics | datensparsame Events, Metriken, Experimente | Erfolgsclaim ohne Evidenz |

## 4. Intake und Zerlegung

```text
T01 Nutzerwert + Muss/Soll/Kann + Nicht-Ziele
 → T02 Trust Zones + Datenquellen + Risiken
 → T03 beobachtbare Akzeptanzkriterien
 → T04 Datei-Owner zuweisen (eine Schreibrolle pro Datei)
 → T05 Verträge vor Code (API/Daten/UI/Event/Fehler)
 → T06 Parallelplan ohne Dateikonflikt
 → T07 Gates (Security/QA/UX/Data) definieren
 → T08 Implementierung vertikaler Schnitte
 → T09 Integration + Gesamttest
 → T10 externe Freigabe falls nötig
 → T11 Betrieb / Abschluss
```

Minimaldaten: `source, observed_at, received_at, quality, confidence,
processing_status, payload`; Zeiten UTC intern, Anzeige Europe/Berlin.

Unklare Punkte = reversible Annahme; nur echte Security-/Entscheidungsblockaden
als Frage zurück.

## 5. Beauftragungsmatrix

| Auslöser | Primär | Zusätzlich / Zeitpunkt |
|---|---|---|
| UX/UI/Brand/Redesign | UX | FE danach/parallel bei Vertrag; QA danach |
| FE-Implementierung | Frontend | UX Design; Backend API; QA danach |
| API/DB/Echtzeit | Backend | Research vor Anbieter; Security vor Integration; QA danach |
| Karte/ADS-B/Spuren | GIS | Backend Datenfluss; UX/FE Darstellung; QA danach |
| Quellen/Fakten/Standards/Lizenzen | Research | Fachagent Umsetzung; Security bei Privacy |
| Datenqualität/Provenienz | Data Quality | Backend/GIS Regeln; QA Regression |
| Security/Privacy/Secrets | Security | Owner-Fix; QA Negativtest |
| Test/Regression/Abnahme | QA | unabhängig nach Implementierung; Ali Befundbehandlung |
| CI/CD/Release/Betrieb | DevOps | Security Rechte; QA Smoke |
| Metriken/Experimente | Analytics | UX Hypothese; FE/BE Instrumentierung; Security |
| Content/KI | Research + Fach | DQ, Security, QA; Human Review vor Publish |

## 6. Parallelisierung und Dateiverantwortung

**Parallel erlaubt:** getrennte Recherche, Risikoanalyse, Testplanung, Vertragsentwürfe.  
**Nicht parallel:** dieselbe Datei, widersprüchliche Datenmodelle.

Ali weist pro Datei einen Owner zu. Andere: Review-Kommentare oder Patch-Vorschläge,
keine ungefragten Writes. Nach parallelen Änderungen: gemeinsame Diff-, Build-,
Integrations- und Security-Prüfung.

Übergabepunkt erreicht wenn Input, Entscheidung, Artefakt, Tests, offene Punkte
dokumentiert. Empfänger bestätigt Annahme, weist Widersprüche aus, erfindet keine
fehlenden Infos.

## 7. Verbindliches Übergabeformat

```text
Auftrag:
Nutzerwert und Akzeptanzkriterien:
Geprüfter Kontext / Ist-Zustand:
Rolle und Verantwortungsgrenze:
Entscheidung / Ergebnis:
Annahmen und offene Fragen:
Daten-, API-, Design- oder Eventvertrag:
Geänderte Dateien und Dateiverantwortung:
Abhängigkeiten und Folgewirkungen:
Ausgeführte Tests (Befehl, Szenario, Ergebnis):
Nicht verifiziert:
Risiken und Sicherheits-/Datenschutzfolgen:
Rollback / Rückfallweg:
Empfehlung und nächster Owner:
```

QA ergänzt: ID, Schweregrad, Ort, Reproduktion, erwartet, tatsächlich, Auswirkung,
Ursache, Fixrichtung.  
Security ergänzt: Risiko-ID, Asset, Angriffsweg, Nachweis, Verifikation, Rest-Risiko.

## 8. Standardprozess und Gates (Detail)

1. **Intake** – Ali: Ziel, Scope, Nicht-Ziele, Freigabebedarf  
2. **Bestand** – Code, Doku, Config, Workflows, Status; Ist≠Zielbild  
3. **Zerlegung** – Owner, Dateien, Verträge, Abhängigkeiten, Parallelisierung  
4. **Recherche/Risiko** – Research, DQ, GIS, Security liefern Grundlagen  
5. **Design/Vertrag** – UX, API, Daten, Fehler, Event, Rollback abgestimmt  
6. **Implementierung** – kleinster vertikaler Schnitt; Defaults; Timeouts; Limits; Idempotenz; sichtbare Fehler  
7. **Review-Gates** – Security bei Risiko; UX bei Darstellung; DQ bei Daten; danach unabhängige QA  
8. **Integration** – Ali: Diff, Abhängigkeiten, Migration, Doku, Build, Gesamttests  
9. **Freigabe** – Nutzer/Betreiber für externe/irreversible Aktionen; technische Freigabe ≠ Publikationsfreigabe  
10. **Betrieb** – DevOps nur freigegeben; Health, Smoke, Logs, Metriken, Rollback  
11. **Abschluss** – Ergebnis, Version, Tests, Monitoring, offene Risiken, Rückfallweg  

## 9. Szenarien (Team-Ketten)

Jedes Szenario: Eingabe → Vorbedingungen → Rollen/Schritte → Parallelisierung →
Übergaben → Ergebnis → Tests → Freigabe → Rückfallweg. Details auch in `02`.

### 9.1 Neues Feature

Ali zerlegt → UX||Research mit Backend/GIS-Vertrag → FE/BE getrennt → Security → QA.  
Verträge vor Integration. Tests: Unit, Contract, UI, A11y, Fehler/Offline, Security.
Rückfall: Feature-Flag oder last good; keine Datenlöschung.

### 9.2 Bug

QA repro+misst → Fachagent Ursache → Ali genehmigt Minimalfix → Security bei Risiko.
Parallel: Regressionstest wenn Oracle klar. Ergebnis: Ursache behoben, Regression,
Gesamttest, Diff. Rückfall: Revert.

### 9.3 Redesign

UX Research/Journey/IA → Research Sprache/Marke → FE Komponenten → Security externe
Inhalte → QA responsive/A11y. Implementierung wartet auf Tokens/Komponentenvertrag.
Rückfall: Flag/Route zur alten Darstellung.

### 9.4 Externe API

Research Doku/Limits/Lizenz → Backend Vertrag Timeout/Retry/Cache → Security Auth/SSRF/Logs
→ FE/UX Zustände → QA 401/403/404/409/429/5xx/Timeout/JSON. Betrieb nach Ali-Entscheid.
Rückfall: Provider aus, Cache stale, kein Fake-Erfolg.

### 9.5 Live-Flugkarte

GIS Layer/CRS/Plausibilität/Unsicherheit → Backend Receiver/API/Freshness → UX/FE
Karte+Liste → Security Privacy → QA Last/Offline/Tiles/Sprünge. Roh≠Beobachtung≠Event≠Aussage.
Keine exakten Privatempfangsorte. Ausfall: stale/offline + Liste/last good.

### 9.6 Datenmigration

Backend idempotente Migration → DQ Constraints → QA Testkopie → Security Minimierung
→ Ali Anwendung. Prod erst nach allen Nachweisen + Change-Freigabe. Rückfall:
Backup-Restore oder roll-forward; Belege/Historie behalten.

### 9.7 Content/KI

Research Primärquellen → GIS/DQ Flugdaten → Ali Faktenobjekt → KI nur daraus →
UX Lesbarkeit → Security sensitive Inhalte → QA Edges. Formulierung erst nach Fakten.
Human redaktionelle Freigabe Pflicht. Rückfall: Entwurf/Review oder Evergreen; nichts künstlich aufblasen.

### 9.8 Instagram/MCP

Research Meta → Backend Auth/API/Status → UX/FE Preview/Fehler/Confirm → Security
Token/Scope (ohne Werte) → QA Doppelposting + Fehlercodes. Publish sequentiell nach
Preview + `confirmed=true` + Status re-read. Unknown → STOP, kein Retry; Draft bleibt.

### 9.9 Security-Fund

Security stoppt Folgeaktionen → Ali Impact → Owner Minimalfix → QA Negativ →
DevOps Rotation/Rollback nur freigegeben. Rückfall: isolieren, deaktivieren, last safe;
Secrets nur Betreiber.

### 9.10 Performance

QA Baseline → FE/BE/GIS Ursache → UX Nutzwert → Ali Priorität. Fix nach reproduzierbarer
Baseline; Vorher/Nachher, Budget, Regression. Rückfall: Opti aus, ohne Qualität/A11y zu opfern.

### 9.11 Schlechte Datenlage

Research Hierarchie → DQ stale/degraded/rejected → UX transparente Leere → Ali Entwurf
statt Meldung. Keine künstliche Story. Rückfall: nichts publizieren; späterer Check mit neuem UTC-Stand.

### 9.12 Agenten-Blockade

Blockade+Auswirkung doku → Ali trennt blockiert/unabhängig → Mock/Testdaten/Doku →
Security stoppt riskante Umgehungen. Sichere Teile weiter. Ergebnis: Entsperranleitung,
kein behaupteter Erfolg. Rückfall: sicherer Zwischenstand oder Abbruch ohne Prod-Nebenwirkung.

### 9.13 Release

Ali Scope → QA Tests → Security Gate → DevOps Build/Rechte/Trigger/Health/Smoke;
bei Bot/Pages auch `workflow_run`, Artefakt, echter Deploypfad. Prod wartet auf
beide Nachweise + ausdrückliche Freigabe. Rückfall: last verified Version; Migration
rückwärts oder roll-forward; keine Belege löschen.

## 10. Dokumentation, Monitoring, Betrieb

Verhaltensänderungen aktualisieren passende Doku. Dauerhafte Funktion nennt:
Health/Readiness, Fehlercodes, Datenalter, Metriken, Retention, Cache-Invalidierung,
Alert, manuellen Notfallweg. Logs ohne Secrets, Tokens, private Adressen, exakte
Standorte, unnötige PII.

Ausfall: `offline|degraded|stale` sichtbar. Meta/API/Publish-Timeout → unknown;
Wiederholung anhalten. Metriken: technische Gesundheit (Latenz, Fehler, Freshness,
Queue, Uptime) ≠ Produktnutzung. Grüner Build ≠ Smoke; Metrik ≠ Redaktionsnachweis.

## 11. Freigabematrix

| Aktion | ohne externe Freigabe? | erforderlich |
|---|---|---|
| Lesen, Analyse, lokaler Mock/Test | ja | keine Prod-Daten |
| Code/Doku im Auftrag | ja | QA/Owner vor Integration |
| Entwurf/Preview speichern | ja | Review-Hinweis bei Unsicherheit |
| Security-Fix lokal testen | ja | keine Angriffsausweitung |
| Prod-Migration oder Löschung | nein | Change, Backup, Rollback, Betreiber |
| Secret-Änderung/Rotation | nein | berechtigter Betreiber, Security |
| Instagram/Meta Publish | nein | explizite Bestätigung, Statusprüfung |
| Deployment/Release | nein | Ali + passende Release-Freigabe |
| Sicherheits-/Notfall-Content | nein | Fach-, Redaktions- und menschliche Freigabe |

## 12. Abschluss-Checkliste

- [ ] Scope, Dateien, Agenten, Entscheidungen stimmig mit Auftrag  
- [ ] Git-Diff ohne fremde, generierte oder geheime Inhalte  
- [ ] Tests mit echtem Befehl/Ergebnis oder als nicht verifiziert  
- [ ] API-, Daten-, UX-, Security-, Betriebsverträge konsistent  
- [ ] Edge Cases, Datenalter, Unsicherheit, A11y, Rollback abgedeckt  
- [ ] keine externe Aktion ohne Freigabe  
- [ ] Übergabe: Ergebnis, Dateien, Tests, offene Risiken, nächster Owner  

Aufgabe abgeschlossen erst wenn diese Prüfung erfolgt und Ali die integrierte,
dokumentierte, rücknehmbare Lieferung verantwortet.

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `02-rollen-und-szenarien.md`
- `05-bestandsaufnahme-und-vertraege.md` · `06-agenten.md`
- `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15` · `16` · `17` (nur Planung)

## Dokumentpflege

Verhaltensänderungen: Verträge, Agent-Profile, README und dieses Handbuch
gemeinsam aktualisieren (Geltungsbereich, Annahmen, Testnachweis, Risiken).
