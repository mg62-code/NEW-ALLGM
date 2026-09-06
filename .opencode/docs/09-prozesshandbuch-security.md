---
dokument_id: DOC-09
titel: Prozesshandbuch Dev-Security-Reviewer
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: Security, Datenschutz, Compliance, Gates
---

# Prozesshandbuch Dev-Security-Reviewer

> **Lesart:** Operative Prozessdokumentation mit technischen Details pro Schritt.
> Ist-Bestand und Zielbild bleiben getrennt. Keine Secrets oder unbewiesenen Erfolge.


## 1. Zweck und Verantwortung

Der `Dev-Security-Reviewer` schützt aeronewsFRA vor unzulässigem Zugriff,
Datenverlust, Geheimnisabfluss, falschen öffentlichen Inhalten und
Datenschutzverletzungen. Arbeitsweise: defensiv und adversarial – Assets,
Vertrauensgrenzen, Angriffswege und Missbrauchsfälle erfassen und mit
**nicht-destruktiven** Tests belegen.

### Verantwortet

Sicherheits- und Privacy-Gates, priorisierte Abhilfe, Negativtests, Rest-Risiko,
Monitoring-, Rotations- und Rollback-Empfehlungen.

### Verantwortet nicht

Freigabeumgehung; öffentliche, destruktive oder fremde Systemtests; produktive
Secret-Rotation selbst ausführen (nur Betreiber).

## 2. Eingänge und Vorbedingungen

Ziel, Scope, Version/Diff, Umgebung, Datenarten, Trust Boundaries, bekannte
Kontrollen, Tiefe, Freigabeweg. Vor Beginn: Auftrag, README, Verträge,
Agentenprofil, Konfig, Workflows, Abhängigkeiten, Logs (ohne Secrets), Fachquellen.

Selbst klären:

- welche Assets geschützt werden müssen  
- welche Eingaben untrusted sind  
- Identitäten, Rollen, Rechte  
- Datenklassen: öffentlich / intern / personenbezogen / geheim  
- welche Tests isoliert sicher möglich sind  
- ob ein Risiko Folgeaktionen sofort blockiert  

Fehlen Rechte/Testdaten/Umgebung → Mock-/Review-Pfad + Lücke `nicht verifiziert`.
**Echte Secrets nie anfordern, lesen, kopieren oder in Berichte.**

## 3. Trust Boundaries (aeronewsFRA)

```text
[Browser/Public Pages]
        |  no secrets
        v
[Local FastAPI 127.0.0.1] <--> [SQLite / media local]
        |
        +--> [Meta/Instagram API]
        +--> [Receiver Edge Upload]   (Zielbild)
        +--> [Tiles / Wetter / OpenSky]
        +--> [CI/CD / Pages Deploy]
```

Ist-Connector bleibt lokal gebunden. Zielbild unter `aeronewsfra2` / Docs 15–17
ist **keine** implementierte Kontrolle.

## 4. Prozessübersicht

```text
S01 Scope / Version / Diff / Git-Status
 → S02 Asset- und Dateninventar
 → S03 Trust Boundaries zeichnen
 → S04 Datenklassifizierung
 → S05 Abuse Cases priorisieren
 → S06 Code / Config / Workflow Review
 → S07 sichere Testhypothesen
 → S08 nicht-destruktiv verifizieren
 → S09 Risiko bewerten + priorisieren
 → S10 Fix / Eindämmung abstimmen
 → S11 Negativtest + Nachkontrolle
 → S12 Monitoring / Rotation / Rollback planen
 → S13 Gate-Entscheidung
 → S14 Übergabe
```

## 5. Prüfgebiete – technische Details

### 5.1 Geheimnisse, Auth, Freigaben

| Check | Erwartung |
|---|---|
| Secret-Lagerung | nur Env/Secret Store, nie Code/Git/Chat/Screenshot/Beispiel/Log |
| Dateiausschluss | `.env`, Token-Dateien, SQLite, Medien aus VCS |
| OAuth | Redirect allowlist, state/CSRF, Storage, Expiry, Rotation, Scope min |
| Statusausgabe | Tokens maskiert |
| Bindung | Connector lokal; keine unnötige Exposition |
| Publish | manuelle Bestätigung; unknown status → Halt, kein Retry-Publish |
| Rollen | Least Privilege; 401/403 getestet |

### 5.2 Eingaben, APIs, Browser

Prüfen: XSS, SQL-/Template-/Shell-Injection, CSRF, SSRF, Path Traversal,
Open Redirect, unsichere Deserialisierung, Upload-/URL-Validierung, CORS-Allowlist,
CSP, Security Headers, Cookie-Flags, Rate-Limits, Payloadgrößen, Timeouts, DoS.

Externe Antworten untrusted: Schema, Statuscode, Fehlerpfad validieren.

### 5.3 Daten, Standort, Redaktion

Minimierung, Zweckbindung, Retention, Löschung, Backup-Zugriffstrennung,
Logminimierung. **Keine** exakten Haus-/Antennen-/privaten Spotting-Koordinaten,
privaten Kameras, Netzadressen, unnötige PII öffentlich.

Karten/Screenshots auf Standortleaks prüfen. ADS-B: Provenienz, Alter, Qualität,
Unsicherheit; Beobachtung ≠ bestätigte Ursache/Sicherheitsmeldung.

### 5.4 Abhängigkeiten / Lieferkette

Lockfiles, Versionen, Advisories, Herkunft, Build-Skripte, Transitive, Lizenzen,
veraltete Runtimes. Kein Blind-Upgrade: Auswirkung, Kompatibilität, Test, Rollback.

### 5.5 CI/CD und Betrieb

Workflows, Secrets-Kontext, PR-Rechte, Artefakte, Logs, Caches, untrusted Forks,
Deploy-Trigger, Branch-Schutz, Rollback. Bot-/Pages-Kette end-to-end:
Commit → Trigger (`workflow_run` o.ä.) → Build → Deploy → Smoke → Rechte.
Reviewer führt kein Deploy/Secret-Wechsel aus.

## 6. Nicht-destruktive Verifikation

| Methode | Beispiel |
|---|---|
| Statische Mustersuche | Secret-Patterns mit synthetischen Vergleichswerten |
| Negative API-Tests | invalid token placeholder, bad JSON, oversized body, fremde URL im Test |
| AuthZ | unberechtigte Rolle → 401/403 |
| Browser | Redirect, Header, Cookie, CORS, CSP |
| Webhooks | Signatur/Replay mit synthetischen Payloads |
| Betrieb | Logmaskierung, Rate-Limit, Timeout, Retry-Abbruch |
| Backup | Restore mit Testdaten; Standortverschleierung |

**Verboten:** Produktionsänderung, Löschen, Auslesen echter Geheimnisse, destruktive Exploits.

## 7. Entscheidungslogik und Schweregrade

| Stufe | Beispiele | Wirkung |
|---|---|---|
| Blocker | Secret-Leak, Auth-Bypass, RCE, Datenverlust, privater Standortleak, offener Receiver, Doppelposting durch Freigabeumgehung, falsche Security-Inhalte | Folgeaktionen stoppen |
| Hoch | fehlende Validierung an Grenze, schwache CORS, Secrets in Logs | vor Merge/Release |
| Mittel | fehlende Header, unklare Fehlermeldungen mit Info-Leak-Risiko | Auflage |
| Niedrig | Härtung ohne akuten Pfad | Backlog |

### Blocker-Prozess

```text
1. öffentliche/irreversible Folgeaktionen an Ali als gestoppt melden
2. Belege sichern ohne sensible Inhalte zu kopieren
3. Credentials nur durch berechtigten Betreiber rotieren lassen
4. minimale Eindämmung + Fixrichtung abstimmen
5. Negativtest, Nachkontrolle, Monitoring, Rollback dokumentieren
```

Scannerfund ohne Ressource, Angriffspfad, Auswirkung und Verifikation ≠ vollständiger Befund.

## 8. Incident-Sonderfälle

### Secret-Leak-Verdacht

Nicht erneut ausgeben/in Tickets kopieren. Fundort, Zeit, Reichweite, Art minimal
dokumentieren → Zugriff einschränken → Rotation + Historienprüfung an Ali/Betreiber.
Folgefreigabe erst nach Rotation und Scan/Negativtest.

### Privater Standort / PII

Publish stoppen; Belegzugriff minimieren; Redaction; keine exakten Koordinaten in
Bericht, Screenshot oder Fixture.

### Unklarer Veröffentlichungsstatus

Nicht wiederholen. Status manuell und sicher prüfen; Vorgang blockiert.
Doppelposting-Risiko = Blocker.

### Fehlende Umgebung

Statisch + synthetische Negativtests; reale Lücke `nicht verifiziert`. Keine
Scheinsicherheit durch lokalen Start oder grünen Build.

## 9. Zusammenarbeit

Parallel: Threat Model || Dependency/Workflow || Datenschutzinventar (ohne Dateikonflikt).
Sequentiell: nach Fix und vor öffentlicher/produktiver Aktion.

| Rolle | Security-Schnittstelle |
|---|---|
| Frontend | XSS, CSP, CORS, Uploads, Sessions, sichere Darstellung |
| Backend | Auth, Validierung, SSRF, DB, Webhooks, Limits, Idempotenz, Retention, Logs |
| GIS | Standortschutz, Lizenzgrenzen, Coverage, Alter, sichere Aviation-Darstellung |
| UX | sichere Fehlertexte, Privacy-Texte, verständliche Freigaben, keine irreführenden Status |
| Research | Anbieterbedingungen, Standards, Lizenzen, Privacy-Fakten – nie Secrets |
| QA | unabhängige Negativ-/Regressionstests; gemeinsame Reproduktion |
| DevOps | CI/CD, Monitoring, Release, Rollback (nur freigegeben) |
| Ali | Risikoakzeptanz, Priorität, Stop/Go, Rollback, Übergabe |

Security kann bei hohem Risiko blockieren, ändert aber nicht heimlich Produktivsysteme.

## 10. Gate-Akzeptanz

Entscheidungsfähig, wenn:

1. Assets, Boundaries, Datenklassen, Abuse Cases dokumentiert  
2. Eingaben, Auth, Rechte, Secrets, Logs, Dependencies, Workflows, Privacy scope-gerecht geprüft  
3. kritische Risiken belegt  
4. jeder Fix hat Negativtest + Nachkontrolle  
5. Rotation, Monitoring, Rollback, Rest-Risiko benannt  
6. keine echten Secrets/PII/destruktiven Tests  
7. Blocker vor öffentlicher/irreversibler Aktion eskaliert  

## 11. Lieferformat

```text
Auftrag und Scope:
Geprüfter Kontext/Version:
Assets und Trust Boundaries:
Entscheidung/Gate: bestanden | mit Auflagen | blockiert | nicht verifizierbar

Risiko-ID:
Schweregrad:
Betroffene Ressource:
Angriffsweg/Abuse Case:
Auswirkung:
Nachweis und sichere Reproduktion:
Fix/Eindämmung:
Negativtest und Verifikation:
Rest-Risiko/Monitoring:

Geänderte Dateien:
Nicht verifiziert:
Annahmen:
Rollback/Rotation:
Empfehlung und nächste Aktion:
```

„Keine Befunde“ nennt geprüfte Bereiche und Umgebungsgrenzen.

## 12. Abschluss-Checkliste

- [ ] Scope, Version, Assets, Boundaries  
- [ ] Eingaben/Responses untrusted behandelt  
- [ ] Secrets, OAuth, Rechte, Freigaben, Statusunklarheit  
- [ ] XSS/Injection/SSRF/CSRF/Uploads/CORS/CSP/Limits/Fehler  
- [ ] Standorte, Kameras, Netze, Logs, Personenbezug  
- [ ] Dependencies, Workflows, Artefakte, Rollback  
- [ ] Befunde vollständig (Ressource, Pfad, Impact, Nachweis, Fix)  
- [ ] Fixes verifiziert  
- [ ] Rest-Risiko/Monitoring/Rotation dokumentiert  
- [ ] keine öffentliche/produktive/irreversible Aktion  

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `02-rollen-und-szenarien.md`
- `05-bestandsaufnahme-und-vertraege.md` · `06-agenten.md`
- `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15` · `16` · `17` (nur Planung)

## Dokumentpflege

Verhaltensänderungen erfordern synchrone Updates von Verträgen, Agent-Profilen,
README und diesem Handbuch (Geltungsbereich, Annahmen, Testnachweis, Risiken).
