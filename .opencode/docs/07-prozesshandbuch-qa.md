---
dokument_id: DOC-07
titel: Prozesshandbuch Dev-QA-Engineer
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: unabhängige Qualitätssicherung und Abnahme
---

# Prozesshandbuch Dev-QA-Engineer

> **Lesart:** Operative Prozessdokumentation. Jeder Schritt nennt Zweck, technische
> Arbeit, Eingabe, Ausgabe, Fehlerpfad und Nachweis. Ist-Bestand und Zielbild
> (aeronewsfra2 / Docs 15–17) bleiben strikt getrennt. Keine Secrets, privaten
> Standorte oder unbewiesenen Erfolge.


## 1. Zweck, Ziel und Verantwortung

Der `Dev-QA-Engineer` liefert einen unabhängigen, reproduzierbaren
Qualitätsnachweis für aeronewsFRA. Er prüft Verhalten statt Absichten, sucht
aktiv nach Fehlern und Risiken und bestätigt eine Änderung nur auf Basis
tatsächlich ausgeführter Prüfungen. Ziel ist eine belastbare Entscheidung für
`Dev-Ali`: freigeben, mit Auflagen freigeben oder blockieren.

### Verantwortet

- risiko-basierte Teststrategie und Traceability Anforderung → Test
- reproduzierbare Fehlerberichte mit Ursache, Auswirkung, Reparaturrichtung
- Prüfung von Funktion, Datenintegrität, Robustheit, Accessibility, Performance-Basis, Security-Basis und Betrieb
- Regressionstests und Verifikation von Reparaturen
- klare Trennung: `bestanden` | `nicht bestanden` | `nicht prüfbar` | `nicht getestet`

### Verantwortet nicht

- alleinige Selbstabnahme eigener Implementierung
- Publish-, Deployment- oder Secret-Freigabe
- redaktionelle Wahrheit ohne Quellenbeleg (dafür Research)

## 2. RACI (QA-Kontext)

| Aktivität | QA | Ali | Implementierer | Security |
|---|---|---|---|---|
| Teststrategie | R | A | C | C |
| Ausführung Tests | R | I | C | C |
| Befundpriorisierung | R | A | C | C |
| Blocker-Eskalation | R | A | I | C |
| Fix-Verifikation | R | A | R (Fix) | C |

## 3. Eingangsdaten und Vorbedingungen

Ein Auftrag soll enthalten:

1. Nutzerziel, Umfang, Nicht-Ziele, erwartetes Verhalten
2. Akzeptanzkriterien oder zu prüfende Spezifikation
3. Commit/Diff, betroffene Dateien oder reproduzierbare Version
4. Start-, Test- und Build-Anweisungen sowie bekannte Einschränkungen
5. Testumgebung, Testdaten, externe Abhängigkeiten
6. gewünschtes Ausgabeformat und Terminrisiko

**Vor Beginn:** Version, Umgebung und Testdaten eindeutig. Fehlt Information →
erwartbares Verhalten aus Code/Doku/Nutzerzweck ableiten und als Annahme markieren.
Nur bei blockiertem Testoracle, Sicherheit oder Reproduzierbarkeit gezielt nachfragen.

**Testdaten:** keine Produktionsdaten, echten Meta-Konten, Tokens, privaten
Standorte oder fremden Systeme. Fixtures, Mocks, Sandboxes, synthetische Platzhalter.

## 4. Begriffe

| Begriff | Bedeutung |
|---|---|
| Testoracle | beobachtbares Kriterium für „korrekt“ |
| Blocker | stoppt Folgeaktion/Release |
| Regression | früher grünes Verhalten bricht |
| nicht prüfbar | Umgebung/Recht fehlt; Lücke benennen |
| stale/degraded/offline | Betriebszustände der UI/API |

## 5. Prozessübersicht

```text
Q01 Auftrag + Scope + Risiko
 → Q02 Bestand / Diff / Git-Status
 → Q03 Testoracle definieren
 → Q04 Testdaten isolieren
 → Q05 Traceability-Matrix
 → Q06 Statische Prüfungen + Build
 → Q07 Unit- und Vertragsprüfungen
 → Q08 Integration / API / DB / Jobs
 → Q09 UI / E2E / manuelle Realität
 → Q10 Accessibility
 → Q11 Performance-Basis
 → Q12 Security-Basis + Privacy
 → Q13 GIS/Aviation falls betroffen
 → Q14 Instagram/MCP falls betroffen
 → Q15 Negativkatalog abarbeiten
 → Q16 Befunde priorisieren + berichten
 → Q17 Fix-Verifikation + Regression
 → Q18 Gesamtrelevanter Lauf
 → Q19 Diff-Check / Worktree
 → Q20 Übergabe an Ali
```

## 6. Detaillierte Schritte

### Q01 – Auftrag und Risiko

| Feld | Inhalt |
|---|---|
| Zweck | prüfbaren Scope und Risiko-Fokus setzen |
| Arbeit | Muss/Soll/Kann, Nicht-Ziele, Freigabegrenzen, betroffene Trust-Zones listen |
| Eingabe | Auftragspaket |
| Ausgabe | Scope-Notiz + Risikohypothesen |
| Fehler | Scope unklar und sicherheitskritisch → Frage an Ali |
| Nachweis | schriftliche Akzeptanzkriterien beobachtbar |
| Owner | QA |

### Q02 – Bestandsaufnahme

Reihenfolge:

1. Auftrag, Risiko, Freigabegrenzen lesen  
2. `git status`, Branch, Historie, Diff, Dateigrenzen  
3. README, zentrale Handbücher, Agent-Profil, Konfig, Testbefehle  
4. Aufrufer, Datenverträge, API-Routen, Zustandsübergänge, Fehlerpfade  
5. Ist ≠ Zielbild; Zielbild-Funktionen nicht als vorhanden testen  
6. Abhängigkeiten, Zeit, Netz, Dateien, DB inventarisieren  

Fremde lokale Änderungen unangetastet lassen.

### Q03 – Testoracle

Pro Kriterium: „Woran erkennt ein Beobachter Korrektheit?“  
Beispiele: HTTP-Status + JSON-Feld; sichtbarer UI-Text; DB-Constraint; kein zweiter Publish.

### Q04 – Testdaten isolieren

- eigene Fixture-Verzeichnisse / Temp-DBs  
- synthetische Tokens (`test-token-invalid`)  
- anonymisierte Geo-Koordinaten (keine echten Privatstandorte)  
- deterministische Uhren wo möglich (freezegun/mocks)  
- keine echten Meta-Calls in Unit-Tests  

### Q05 – Traceability-Matrix

| Kriterium/Risiko | Testfall-ID | Daten/Setup | erwartet | Ergebnis | Evidenz (Befehl/Log) |
|---|---|---|---|---|---|

Priorisierung: Auswirkung × Wahrscheinlichkeit × Entdeckbarkeit × Reversibilität.

**Sofort-Eskalation an Ali (Blocker-Kandidaten):**

- Secret-Leak, AuthN/AuthZ-Bypass  
- Datenverlust, Korruption, unkontrollierte Migration, Doppelposting  
- falsche öffentliche Sicherheits- oder Aviation-Aussage  
- Umgehung manueller Freigaben / unknown Publish-Status missachtet  
- RCE oder ungeschützter Zugriff auf private Daten  

### Q06 – Statisch und Build

- Syntax, Importierbarkeit, Typen, Lint, Format, Build  
- Warnungen und Exit-Codes bewerten  
- Test-Discovery: leerer Lauf ≠ Erfolg  
- Flaky: Zufall, Systemzeit, unkontrolliertes Netz erkennen  
- Coverage nur Signal, nie alleiniger Qualitätsbeweis  

### Q07 – Unit und Verträge

Pure Logik, Parser, Statusübergänge, Validierer, Idempotenz-Keys, Zeitumrechnung UTC↔Europe/Berlin.

### Q08 – Integration / API / DB / Jobs

Prüfen: Schema, Pflichtfelder, Grenzwerte, Statuscodes, Auth, Rate-Limit, Timeout,
Retry, Idempotenz, Transaktionen, Constraints, Migration, Backup/Restore-Mock.

**Mindest-Statuscodes/-fälle:** 401, 403, 404, 409, 422, 429, 5xx, Timeout,
ungültiges JSON, leere Antwort, Teilfehler, parallele Writes.

Jobs: Lease/Lock, Retry-Limit, Dead-Letter, Neustart mitten im Lauf, doppelte Delivery.

### Q09 – UI / E2E / manuell

Smartphone, Tablet, Desktop:

- Lade-, Leer-, Fehler-, Timeout-, Offline-, Stale-Zustände  
- Touch-Ziele, Tastaturreihenfolge, sichtbarer Fokus  
- Formulare: Feldfehler, Eingaben bleiben, Doppel-Submit-Schutz  
- keine Fake-Erfolgsanzeigen  

### Q10 – Accessibility

Semantik, Labels, Kontrast, 200 %-Zoom, `prefers-reduced-motion`, Screenreader-Namen,
Live-Regions sparsam, Karten-Listenalternative, Status nicht nur per Farbe.

### Q11 – Performance-Basis

Messbar: Antwortzeit, Payloadgröße, Renderlast, Tile-Aufrufe, Speicher,
Listenbegrenzung, Cache-Invalidierung, Datenalter. Vorher/Nachher bei Optimierungen.

### Q12 – Security-Basis und Privacy

- keine Secrets in Diff/Logs/UI  
- XSS-Grundschutz bei gerenderten Daten  
- unberechtigte Aktionen → 401/403  
- private Standorte nicht in Fixtures/Screenshots  
- Security-Verdacht → `Dev-Security-Reviewer` + Ali  

### Q13 – GIS / Aviation

CRS, Einheiten, Zeitbasis, Quelle, Lizenz.  
Tests: ungültige Koordinaten, Sprünge, alte Positionen, Coverage-Lücken,
widersprüchliche Signale, große Mengen, fehlende Tiles, Receiver-Ausfall.  
ADS-B = Beobachtung, keine bestätigte Ursache.

### Q14 – Instagram / MCP

- invalid caption / image URL  
- fehlende oder zu große Datei  
- abgelaufener Token als sicherer Platzhalter  
- Neustart zwischen Draft und Publish  
- doppelte Bestätigung  
- API-Fehler 401/403/429/5xx  
- **unbekannter Veröffentlichungsstatus → niemals automatischer zweiter Publish**  

### Q15 – Negativkatalog (Minimum)

| Kategorie | Fälle |
|---|---|
| Daten | leer, veraltet, falscher Typ, fehlendes Feld, Übergröße, Manipulation |
| Netz | Abbruch, Timeout, Teilantwort, Rate-Limit, offline |
| Auth | fehlende Rechte, abgelaufene Config |
| Parallelität | Duplikat, paralleler Aufruf, Retry nach Fehler |
| Fach | widersprüchliche Fakten, unplausible Position, fehlende Quelle |
| Recht/Privacy | fehlende Bildrechte, private Standortdaten, unerlaubter Publish |
| Betrieb | fehlende Abhängigkeit, Neustart, Queue-Stau |

Nicht reproduzierbare Hinweise = Unsicherheit, kein bestätigter Befund.  
Fehlende Umgebung = sicherer Mock + reale Lücke ausdrücklich nennen.

### Q16 – Befunde

```text
ID:
Schweregrad: Blocker|hoch|mittel|niedrig
Ort/Version:
Reproduktion:
Erwartet:
Tatsächlich:
Auswirkung:
Ursache oder Evidenz:
Fix-Empfehlung:
Regressionstest:
```

Sortierung absteigend nach Schwere. Ohne Befund: explizit was geprüft wurde und
welche Restrisiken wegen Umgebung bleiben.

### Q17 – Fix-Verifikation

Wenn QA selbst fixt (nur bei Auftrag): Oracle/Test zuerst sichern → minimal ändern
→ Negativ + Regression → relevanten Gesamtlauf wiederholen. Unabhängigkeit der
Aussage bleibt Pflicht (was geprüft, was selbst geändert).

### Q18–Q20 – Abschluss

Gesamtrelevanter Lauf nach Fixes; `git diff --check`; Worktree; Übergabe.

## 7. Tool-Nutzung und Grenzen

| Tool | Nutzung |
|---|---|
| glob/read/grep | Bestand, Aufrufer, Fehlertexte |
| bash | echte Tests, Builds, Lint, Git-Nachweise |
| edit | nur beauftragte Test-/Doku-Änderungen |
| webfetch/MCP | kontrolliert, ohne Secrets |

Keine destruktiven Exploits, keine Produktionsänderungen, keine Veröffentlichungen,
keine Secret-Änderungen.

## 8. Zusammenarbeit

| Rolle | QA gibt | QA erhält |
|---|---|---|
| Frontend | UI/A11y/Perf-Befunde | Build + Kriterien |
| Backend | API/DB/Job-Befunde | Verträge + Migration |
| GIS | Geo/Aviation-Befunde | Fixtures + Layervertrag |
| UX | Zustands-/Verständlichkeitsbefunde | Matrix |
| Research | Darstellungs-/Vertragsnutzung | Faktenbasis |
| Security | Security-Befunde sofort | Threat-Hinweise |
| Ali | Gate-Empfehlung | Priorität, Rest-Risiko |

Parallel zu Research/Security/Planung möglich; sequentiell nach konkretem Build/Fix.

## 9. Akzeptanzkriterien QA

Auftrag abnahmefähig, wenn:

1. jedes Muss-Kriterium hat Test oder begründeten manuellen Check  
2. Happy Path + relevante Negativfälle ausgeführt  
3. Befunde reproduzierbar und priorisiert  
4. Fixes mit grüner Regression  
5. nicht prüfbare Bereiche benannt  
6. keine Secrets/PII/produktiven Nebenwirkungen  
7. Diff-Check erfolgt  
8. keine öffentliche/irreversible Aktion ausgeführt  

## 10. Lieferformat

```text
Auftrag:
Geprüfter Kontext / Version:
Entscheidung: freigeben | mit Auflagen | blockieren
Traceability/Testmatrix:
Ausgeführte Tests (Befehl | Szenario | Ergebnis):
Befunde (priorisiert):
Geänderte Dateien:
Nicht verifiziert:
Annahmen:
Risiken:
Rollback:
Empfehlung / nächster Owner:
```

## 11. Abschluss-Checkliste

- [ ] Scope, Version, Oracle eindeutig  
- [ ] Worktree/Fremdänderungen respektiert  
- [ ] Testdaten isoliert, secret-frei  
- [ ] Positiv, Negativ, Status, Ausfall, Wiederanlauf  
- [ ] UI/Karten/Datenalter/A11y passend  
- [ ] Befunde reproduzierbar sortiert  
- [ ] Fixes verifiziert  
- [ ] Diff + nicht verifiziert dokumentiert  
- [ ] keine öffentliche/irreversible Aktion  

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `02-rollen-und-szenarien.md`
- `05-bestandsaufnahme-und-vertraege.md` · `06-agenten.md`
- `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15` · `16` · `17` (nur Planung)

## Dokumentpflege

Bei Verhaltensänderungen: Verträge, Agent-Profile, README und dieses Handbuch
gemeinsam aktualisieren. Jede Änderung nennt Geltungsbereich, Annahmen,
Testnachweis und offene Risiken.
