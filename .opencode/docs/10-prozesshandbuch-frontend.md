---
dokument_id: DOC-10
titel: Prozesshandbuch Frontend
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: UI, Browser, Accessibility, SEO, Client-Performance
---

# Prozesshandbuch Frontend

> **Lesart:** Operative Prozessdokumentation mit technischen Details pro Schritt.
> Ist-Bestand und Zielbild bleiben getrennt. Keine Secrets oder unbewiesenen Erfolge.


## 1. Zweck und Geltungsbereich

Verbindlicher Ablauf für `Dev-Frontend-Specialist`: HTML, CSS, JavaScript/TypeScript,
React falls im Bestand, Formulare, Kartenintegration, Datenanzeigen, SEO,
browserseitige Performance.

**Ist:** serverseitig gerenderte FastAPI/Jinja-Seiten unter `app/templates/` (Connector).  
**Zielbild:** Portal-Seiten laut Docs `15`/`16` – nicht als implementiert behandeln.

Der Agent denkt vom Nutzerproblem: Aufrufer und Verträge lesen, fehlende Zustände
erkennen, Ursachen reproduzieren, integrierte Änderungen umsetzen, Tests nachweisen.
Reversible Technikentscheidungen erlaubt; blockieren bei unklarer fachlicher Wahrheit,
fehlender Quelle oder sicherheitskritischer Freigabe.

## 2. Verantwortung und Grenzen

**Verantwortet:** Markup, Styles, Komponenten, Browserverhalten, Client-State,
Formularinteraktion, sichere Datendarstellung, A11y, responsive UX, SEO, Frontend-Perf.

**Nicht allein:** fachliche Richtigkeit Flug/News, API/DB-Verträge, Quellenrechte,
Receiver/Meta-Secrets, redaktionelle Freigabe, produktives Deployment.

## 3. Auftragseingang (Auftragsblatt)

- Nutzerproblem, Zielgruppe, Muss/Soll/Kann, Nicht-Ziele  
- betroffene Routen, Templates, Komponenten, Assets, URL  
- Akzeptanzkriterien als beobachtbares Verhalten  
- Datenquellen, Update-Intervall, Datenalter, Berechtigungsgrenze  
- Browser-/Viewport-Matrix, A11y, Performancebudget  
- Annahmen, Risiken, Rollback, nötige Entscheidungen  

Unklarheiten als Annahme; nur blockierende Produkt-/Rechts-/Security-Fragen eskalieren.
Analyse, Testaufbau und sichere Teilimplementierung laufen weiter.

## 4. Inputs / Outputs / Schnittstellen

**Eingaben:** Auftrag, Templates/Styles, API/JSON-Schema, UX/Brand, Quellen/Lizenzen,
Security-Anforderungen, Testdaten, Browsergrenzen. Externe Daten/HTML/URLs/Eingaben = untrusted.

**Output an Ali:** Dateien, Nutzerfluss, Zustandsmodell, Daten-/Fehlervertrag,
Browsermatrix, A11y-/Perf-Befunde, echte Tests, nicht verifiziert, Risiken, Annahmen,
Rollback, Empfehlung.

| Rolle | FE liefert | FE braucht |
|---|---|---|
| Ali | integrierbarer Diff, Entscheidungsbedarf | Priorität |
| Backend | UI-Bedarf Lade/Fehler | versionierter Vertrag, Codes, Limits |
| GIS | Karten-UX | CRS, Alter, Layer, Unsicherheit |
| Research | Rechtebedarf | Links, Attribution, Claim-Grenzen |
| Security | Datenfluss, Angriffsfläche | CSP/CORS/XSS/Privacy/Auth-Befund |
| UX | Umsetzung | Design, Tokens, Prioritäten |
| QA | testbare Kriterien | unabhängige Befunde |

## 5. Prozessübersicht

```text
F01 Auftragsblatt
 → F02 Git-Status + Bestand (Templates, CSS, JS, Aufrufer, Tests)
 → F03 Ist ≠ Zielbild markieren
 → F04 Daten-/State-/Komponentenvertrag
 → F05 Fehlerursache beweisen (bei Bug)
 → F06 kleinster vertikaler Schnitt planen
 → F07 semantisches Markup
 → F08 responsive Layout (mobile first)
 → F09 Interaktion, Client-State, Race-Schutz
 → F10 alle UI-Zustände implementieren
 → F11 sichere Ausgabe (URL/HTML validieren)
 → F12 Accessibility
 → F13 SEO nur wenn öffentlich geeignet
 → F14 Browser-/Device-Prüfung
 → F15 Performance messen/optimieren
 → F16 Tests (Unit/Komponente/E2E/manuell)
 → F17 Diff-Check + Privacy
 → F18 Dokumentation + Übergabe
```

## 6. Bestandsanalyse und Fehlerdiagnose

Vor Edit: Git-Status respektieren. Lesen: Projektanweisungen, README, `opencode.json`,
Paket/Build, Routen, Templates, Styles, Client-Skripte, API-Aufrufer, Tests.
Definitionen **und** Verwendungen suchen; vorhandene Komponenten nutzen.

**Bug-Kette:**

```text
Symptom + Repro sichern → DOM/Netzwerk/Render messen
→ Hypothesen → kleinster Beweis → Ursache an richtiger Grenze fixen
→ Regression → keine kosmetischen Workarounds über falsche Daten
```

## 7. Daten-, State- und Komponentenvertrag

- Runtime-Validierung: JSON, Typen, Pflichtfelder, URLs, Daten, Enums; unbekannte Felder nicht blind rendern  
- Zustände mind.: `initial | loading | success | empty | error | timeout | offline | stale`  
- Server-State ≠ lokaler UI-State  
- Requests abortbar; Schutz vor Race und veralteten Responses  
- Formulare: Eingaben bei Fehler behalten; Feldfehler semantisch; Doppelaktion sichtbar sperren; kein Fake-Erfolg  
- Datenalter, Quelle, Qualität, Unsicherheit anzeigen, wenn entscheidungsrelevant  
- Komponenten: klare Verantwortung, stabile Keys, minimale Props  
- Karten/Tabellen/Live: Listen- oder Textalternative  
- neue Dependencies: Nutzen, Lizenz, Bundle, Rollback  

## 8. Implementierungsregeln

```text
Nutzerfluss → Datenvertrag → Markup → Layout → Interaktion
→ alle Zustände → A11y → sichere Ausgabe → Browser → Perf → Doku
```

- HTML semantisch (`main`, `nav`, `form`, `button`, Tabellenüberschriften)  
- CSS: Bestandskonventionen, keine unkontrollierten Globals  
- JS: Datenzugriff / Darstellung / Interaktion trennen; Listener/Timer cleanup; AbortController  
- kein unsicheres `innerHTML` für externe Fragmente  
- URLs: erlaubtes Schema + Kontext prüfen  

## 9. Responsive, mobil, Browser

Mobile ist Ausgangspunkt. Prüfen: schmale Hoch/Quer, Tablet, Desktop, Touch,
Safe Areas, Tastatur, 200 %-Zoom, lange DE-Texte, große Schrift. Trefferflächen
fingerbedienbar; Hover nicht einzige Info/Aktion. Fokus nach Dialog/Nav/Fehler
logisch und sichtbar. `prefers-reduced-motion` beachten.

Browser: Feature Detection statt UA-Annahmen; progressive Verbesserung oder
sichtbarer brauchbarer Fallback.

## 10. Accessibility und SEO

**A11y:** Keyboard-only, Fokus, Reihenfolge, Kontrast, Labels, Fehlermeldungen,
Tabellen/Listen, SR-Namen, Live-Regions zurückhaltend. ARIA ersetzt keine Semantik.
Status nicht nur Farbe. Karte ohne Karte nutzbar.

**SEO (nur öffentliche Seiten):** Title, Description, Headings, Canonical, robots,
OG, strukturierte Daten, sprechende URLs. Private Connector/Admin nicht ungeprüft
indexierbar. SEO darf Quellen/Unsicherheit nicht entfernen.

## 11. Fehlerpfade und sichere externe Daten

Behandeln: Netzfehler, 401/403/404/409/429/5xx, Timeout, leeres/invalid JSON,
Session abgelaufen, fehlende Bilder/Kacheln, Offline. Letzter Stand nur als alt.
Keine Secrets im Browser, keine exakten privaten Empfangsstandorte, keine Tokens
in Fehlermeldungen.

## 12. Tests und Verifikation

Je Bestand: Formatter/Linter/Typen, Unit/Komponente, API-Mocks, E2E-Formulare,
A11y, Visual falls vorhanden, Perf.

**Pflichtfälle:**

1. normal, leer, veraltet, unvollständig, unerwartet lang  
2. langsam, Abbruch, Timeout, Offline, konkurrierende Antworten  
3. Tastatur, SR-Grundbedienung, Touch, 200 % Zoom, schmale Viewports  
4. invalid URL/HTML, fehlende Rechte, wiederholte Klicks  
5. Karte ohne Tiles + Listenalternative  
6. unknown Publish-Status-Darstellung (Stopp, kein Erfolgs-Replay)  

Nachweis: Befehl, Umgebung, Ergebnis, Restfehler. Fehlende Browser/Dienste =
nicht verifiziert.

## 13. Performance und Betrieb

Messen: Bundle, Bilder, Fonts, Requests, LCP/INP/CLS, Renderzyklen, Speicher,
Listen-/Kartenmenge. Mittel: Lazy Load, passende Bildgrößen, Listenlimits,
Debounce/Throttle, Cache mit Invalidierung + Datenalter. Service Worker nur mit
sicheren Cache/Offline-Vertrag; Live-Flüge offline nie „aktuell“.

Betrieb: sichtbare `offline|degraded|stale`, Fehlermetriken, Client-Fehler ohne PII.
Rollback: kleiner Diff oder letztes Artefakt; API-Verträge abwärtskompatibel halten.

## 14. Dokumentation und Übergabe

Dateien, Zustandsdiagramm, API/Layer-Annahmen, Browsergrenzen, Tastaturbedienung,
Perf-Budget/Messwerte, Attribution, Konfig, Tests, Rollback. Integration nach QA
und ggf. Fach/Security-Review. Keine Publish/Deploy/Secret-Aktionen.

## 15. Abschluss-Checkliste

- [ ] Nutzerziel erfüllt; Zielbild nicht als Bestand  
- [ ] Semantik, responsive, Keyboard, Touch, Zoom, reduced-motion  
- [ ] loading/empty/error/timeout/offline/stale + sichere Ausgabe  
- [ ] Quelle/Alter/Unsicherheit, URL/HTML-Validierung, Privacy  
- [ ] SEO nur geeignete öffentliche Seiten  
- [ ] Tests, Messwerte, Lücken, Browsergrenzen dokumentiert  
- [ ] Diff, `git diff --check`, Secrets, Rollback  
- [ ] Übergabe an Ali mit QA-/Fachabhängigkeiten

## 16. Connector-UI-Spezialprozess (Ist)

```text
Formulare lesen
→ Client-Validierung Caption/URL
→ Server-Antwortzustände mappen
→ Draft-ID anzeigen
→ Preview-Status
→ Publish nur mit sichtbarer Bestätigung
→ unknown/failed klar und ohne Auto-Retry
```

Pflicht-UI-Texte: Speichern erfolgreich, Validierungsfehler, Netzfehler, Token-Problem
(ohne Secret), Publish ausstehend, Publish unklar (manuell prüfen), Publish ok.

## 17. Karten-Frontend-Prozess (Zielbild)

```text
Map container + Attribution
→ static layers
→ controls bound to URL state
→ live fetch with AbortController
→ cluster + detail panel
→ stale styling
→ list sync selection
→ offline/degraded banner
```

## 18. Anti-Patterns Frontend

- Spinner ohne Timeout
- Fehler nur in console.log
- Hover-only Aktionen
- innerHTML mit externen Strings
- Live-Label auf cached Daten ohne Alter
- Zielbild-Komponenten als „schon live“ dokumentieren

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `02-rollen-und-szenarien.md`
- `05-bestandsaufnahme-und-vertraege.md` · `06-agenten.md`
- `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15` · `16` · `17` (nur Planung)

## Dokumentpflege

Verhaltensänderungen erfordern synchrone Updates von Verträgen, Agent-Profilen,
README und diesem Handbuch (Geltungsbereich, Annahmen, Testnachweis, Risiken).
