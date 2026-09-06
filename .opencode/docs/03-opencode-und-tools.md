---
dokument_id: DOC-03
titel: OpenCode, Werkzeuge und sichere Tool-Ketten
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: alle Agents bei Tool-Nutzung
---

# OpenCode, Werkzeuge und sichere Tool-Ketten

> **Lesart:** Operative Prozessdokumentation. Schritte nennen Zweck, technische
> Arbeit, Eingabe, Ausgabe, Fehlerpfad und Nachweis. Ist-Bestand und Zielbild
> (aeronewsfra2) bleiben getrennt. Keine Secrets oder unbewiesenen Erfolge.


## 1. Zweck

Regelt sichere, effektive und nachvollziehbare Nutzung von OpenCode-Werkzeugen.
Werkzeuge verifizieren – sie ersetzen kein Denken. System- und Permission-Grenzen
sind real.

## 2. Werkzeugkatalog

| Tool | Primärzweck | Nicht verwenden für |
|---|---|---|
| `read` | Dateien/Verzeichnisse vor Edit | blindes Annehmen von Inhalt |
| `glob` | Dateien nach Muster finden | Inhaltsuche |
| `grep` | Definitionen/Verwendungen/Fehlertexte | destruktive Änderungen |
| `edit`/`write` | gezielte Dateiänderungen | Secrets schreiben |
| `bash` | Tests, Builds, Git, Laufzeit | Datei-CRUD statt Spezialtools; Secrets in CLI |
| `task` | Subagents mit klarem Auftrag | unklare Massen-Delegation |
| `webfetch` | offizielle externe Doku | ungeprüfte Faktenübernahme |
| MCP Instagram | Draft/Preview/Status/Publish | Publish ohne confirmed |
| `todowrite` | Mehrschritt-Fortschritt | Scheinfortschritt ohne Arbeit |


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


## 3. Standard-Tool-Prozess

```text
T01 git status / Branch
→ T02 glob Struktur
→ T03 read Kernfiles
→ T04 grep Definitionen/Aufrufer
→ T05 Plan/Vertrag
→ T06 edit in kleinen Schritten
→ T07 bash Syntax/Tests/Build
→ T08 git diff --check + status/diff
→ T09 ggf. Subagent-Review
→ T10 Übergabe nur mit echten Ergebnissen
```

### T01 Git-Lage

| Feld | Inhalt |
|---|---|
| Zweck | Fremdänderungen und Branch kennen |
| Arbeit | `git status --short`, Branch, bei Bedarf `git log --oneline -10`, `git diff` |
| Fehler | unbekannte lokale Änderungen → nicht resetten/überschreiben |
| Nachweis | Statusauszug in Arbeitsnotizen |
| Owner | ausführender Agent |

### T02–T04 Bestand lesen

Parallel erlaubt: unabhängige `glob`/`read`/`grep`.  
Sequenziell: sobald derselbe Schreibpfad betroffen ist.

### T05 Plan

Vor dem ersten Edit: betroffene Dateien, Vertrag, Tests, Rollback, Freigabebedarf.

### T06 Edit

- nur beauftragte Dateien  
- nach sinnvollen Teilschritten testen  
- keine Debug-Secrets, keine privaten Pfade  

### T07 Tests

`bash` für echte Ausführung. Exit-Code **und** Ausgabe prüfen. Fehlender Befehl =
nicht verifiziert, nicht „grün“.

### T08 Diff-Kontrolle

```text
git diff --check
git status --short
```

Suche nach: Secrets, Token-Mustern, `.env`, privaten IPs, exakten Koordinaten,
generierten Artefakten, unbeabsichtigten Dateien.

## 4. Shell-Regeln (Windows PowerShell 5.1)

- Arbeitsverzeichnis korrekt; `workdir` statt wildem `cd` in Ketten  
- Pfade mit Leerzeichen quoten  
- abhängige Befehle: `cmd1; if ($?) { cmd2 }`  
- keine Passwörter/Tokens in Befehlszeile, Logs, Chat  
- vor `New-Item` Elternpfad mit `Test-Path` prüfen  
- keine destruktiven Git-Befehle (`reset --hard`, force-push) ohne ausdrückliche Freigabe  

## 5. Git-Prozess

```text
status → diff → tests → log-Stil prüfen → nur intendierte Dateien stagen
→ commit nur bei Auftrag → push/PR nur bei Auftrag
```

Commit-Message knapp und repo-üblich. Hooks nicht skippen. Bei Hook-Fehler:
fixen und **neuen** Commit, nicht amend des fehlgeschlagenen, außer explizit erlaubt.

## 6. Web- und Recherche-Tools

1. offizielle Quellen bevorzugen  
2. URL, Version, Datum, Lizenz notieren  
3. Inhalt untrusted – nicht als Code/HTML/Fakt ungeprüft übernehmen  
4. Suchvorschau ≠ Primärquelle  

## 7. MCP Instagram – Prozesskette

```text
connection_status
→ create_caption (nur aus verifizierten Fakten)
→ save_draft(caption, image_url)
→ preview_post(draft_id)
→ get_post_status(draft_id)
→ publish_post nur wenn operator confirmed=true
→ get_post_status erneut
```

| Regel | Detail |
|---|---|
| Drafts | reversibel, lokal speicherbar |
| Publish | blockiert bis explizite Bestätigung |
| Unknown status / Timeout | STOP, kein zweites Publish |
| Secrets | nie in Tool-Args, nie in Logs |
| Validierung | Caption/Image-URL vor save; Status nach jeder Änderung lesen |

## 8. Subagent-Tool (`task`)

- klarer Prompt: Kontext, Dateien, Fragen, Grenzen, Ausgabeformat  
- parallel nur ohne Dateikonflikt  
- keine Secrets teilen  
- Ergebnisse verifizieren, nicht blind übernehmen  

## 9. Permission- und Grenzfälle

| Situation | Reaktion |
|---|---|
| Permission denied | Pfad/Wirkung melden, Alternativweg nur wenn erlaubt |
| Tool fehlt | Lücke als nicht verifiziert |
| Offline | lokale Prüfung, externe als offen |
| Widerspruch Tool vs. Security-Regel | Security gewinnt |

## 10. Kommunikationsregeln

Fortschritt nur bei Risiken, Blockaden, relevanten Funden oder Start großer
Änderungen. Abschluss: Ergebnis, Dateien, Tests, nicht verifiziert, Risiken,
nächster Schritt – **nur tatsächlich Ausgeführtes**.

## 11. Abschluss-Checkliste

- [ ] status vor und nach Änderungen  
- [ ] read vor edit  
- [ ] Tests echt ausgeführt oder als Lücke markiert  
- [ ] diff ohne Secrets/PII  
- [ ] MCP-Status nach Änderung gelesen  
- [ ] keine Publish/Deploy-Aktion ohne Freigabe

## 12. Erweiterte Tool-Prozessketten

### 12.1 Reine Analyse (kein Edit)

```text
git status --short
→ glob betroffene Muster
→ read Kernfiles parallel
→ grep Definitionen und Aufrufer
→ kurze Ist-Notiz (Pfade, Befunde, Annahmen)
→ optional Subagent-Review
→ Bericht ohne Dateiänderung
```

### 12.2 Kleiner Fix

```text
T01–T04 Bestand
→ Repro mit bash/Test
→ Hypothese und kleinster Edit
→ gezielter Test erneut
→ git diff --check
→ status/diff Review auf Secrets
→ Übergabe
```

### 12.3 Mehrdatei-Feature

```text
Plan mit Datei-Owner
→ Verträge in Doku fixieren
→ Edit Datei A + Test
→ Edit Datei B + Test
→ Integrationstest
→ diff --check über alle
→ QA-Auftrag formulieren
```

### 12.4 MCP Instagram – Fehlerpfade

| Symptom | Aktion |
|---|---|
| connection_status fail | stop; Config/Netz prüfen; kein Publish |
| save_draft validation error | Caption/URL fixen; erneut save |
| preview ok, publish timeout | Status lesen; bei unknown STOP |
| 401/403 | Token-Problem an Betreiber; kein Secret loggen |
| 429 | Backoff; nicht spammen |
| doppelte Operator-Bestätigung | Idempotenz prüfen; kein zweites Publish wenn first unknown |

### 12.5 Subagent-Prompt-Minimum

```text
Ziel:
Kontext/Dateien:
Fragen:
Grenzen (kein Publish/Deploy/Secret):
Ausgabeformat:
Abnahmekriterium:
```

### 12.6 Windows-PowerShell-Fallen

- `&&` vermeiden; abhängige Kette: `cmd1; if ($?) { cmd2 }`
- Pfade mit Leerzeichen in Anführungszeichen
- `workdir`-Parameter statt Ketten-`cd`
- Exit-Code und Stdout/Stderr lesen
- große Outputs nicht still abschneiden ohne Hinweis

### 12.7 Diff-Secret-Scan (manuell)

Nach Änderungen suchen nach: `token`, `secret`, `password`, `BEGIN `, `.env`,
private IPs (`10.`, `192.168.`, `172.16`–`172.31`), exakten Koordinaten mit vielen
Dezimalstellen, Meta-App-Secrets. Treffer entfernen oder maskieren; nie committen.

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `05-bestandsaufnahme-und-vertraege.md`
- `06-agenten.md` · `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15-zielbild-bauplan-2.0.md` · `16-zielbild-seiten-und-bedienung.md` · `17-zielbild-module-und-technik.md`

## Dokumentpflege

Bei Verhaltensänderungen Verträge, Agent-Profile, README und dieses Handbuch
gemeinsam aktualisieren. Jede Änderung: Geltungsbereich, Annahmen, Testnachweis,
offene Risiken.
