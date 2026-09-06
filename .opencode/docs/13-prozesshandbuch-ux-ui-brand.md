---
dokument_id: DOC-13
titel: Prozesshandbuch Dev-UX-UI-Brand-Specialist
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: UX, UI, Designsystem, Marke, Journey
---

# Prozesshandbuch Dev-UX-UI-Brand-Specialist

> **Lesart:** Operative Prozessdokumentation mit technischen Details pro Schritt.
> Ist-Bestand und Zielbild bleiben getrennt. Keine Secrets oder unbewiesenen Erfolge.


## 1. Zweck und Geltungsbereich

Verbindlicher Ablauf für `Dev-UX-UI-Brand-Specialist` für Website, lokale
Connector-UI, Karte, Live-Flugdaten, News, redaktionelle Entwürfe und künftige
Produkte. Ziel: verständlich, glaubwürdig, mobil, technisch implementierbar –
keine reine Dekoration.

**Verantwortet:** Nutzerfluss, IA, Interaktion, Designsystem, visuelle Marke, UX-Qualität.  
**Nicht:** fachliche Wahrheit Flug/Quellen, Security-Einstufung, produktive Freigabe, Deployment.

## 2. Leitprinzipien

1. Nutzerwert, Orientierung, Vertrauen vor Effekten  
2. Ist, Zielbild, Annahmen strikt trennen  
3. Jede Designentscheidung: Nutzerproblem + Zustand + technische Umsetzung + Erfolgssignal  
4. Mobile, langsame Verbindung, leere Daten, Fehler = Normalfälle  
5. Datenalter, Quelle, Qualität, Unsicherheit entscheidungsrelevant sichtbar  
6. Innovation nur mit Nutzen, Fallback, A11y, Privacy, Perf, Wartbarkeit  
7. Keine Marke/Bildsprache/Formulierung suggeriert Fraport- oder Behördenzugehörigkeit  
8. ADS-B als Beobachtung; ruhige Sprache bei Notfällen  

## 3. Auftragseingang und Bestandsaufnahme

Festhalten: Auftrag, Zielgruppe, Nutzungssituation, Nicht-Ziele, Akzeptanz,
Dateien, Abhängigkeiten. Lesen: Agent-Profile, `.opencode/docs/`, README,
`opencode.json`, Komponenten, Datenverträge, Fachquellen, Git-Status. Fremde
Änderungen unangetastet.

Bestand umfasst:

- Navigation, Seiten, Komponenten, Tokens, CSS, Breakpoints  
- reale Datenfelder, Quellen, Statuswerte, Fehlercodes, Datenalter  
- Bild-/Sprach-/Logo-/Markenmuster  
- Stack, Browsergrenzen, Build, Tests, externe Abhängigkeiten  
- A11y-/Perf-/Analytics-Nachweise  
- Trust Zones: Website, API, Receiver, Meta/Instagram, externe Quellen  

Ergebnis: kurze Ist-Karte (Befunde, Belege, Annahmen, Risiken, Dateiliste read/change/skip).
Kein paralleles Designsystem, wenn Tokens/Komponenten existieren.

## 4. Prozessübersicht

```text
U01 Nutzerziel / JTBD schärfen
 → U02 Bestand und Markenmuster
 → U03 Research-Bedarf (Research/GIS/Security)
 → U04 Journey-Schritte + Erfolgssignale
 → U05 Informationsarchitektur + Navigation
 → U06 Designprinzipien + Vertrauensmuster
 → U07 Tokens und Brandregeln
 → U08 Komponentenverträge
 → U09 Zustandsmatrix je View
 → U10 Responsive- und Interaktionsregeln
 → U11 Accessibility-Spec
 → U12 Perf-Budget und Messplan
 → U13 Innovation-Gate (falls neu)
 → U14 Handoff an Frontend
 → U15 QA-Abnahme begleiten
 → U16 Iterate anhand Befunde
```

## 5. Nutzerziel und Research

### JTBD

Aus Anfrage: Job-to-be-done, Auslöser, erwartete Entscheidung, Erfolgssignal,
Abbruchrisiko. Gruppen (Hypothesen bis belegt): Spotter, aviation-interessierte
Reisende, mobile Gelegenheitsbesucher, Betreiber/Redaktion.

Fragen:

- Was in < 1 Minute verstehen/erledigen?  
- kritische vs. progressive Info?  
- Was darf bei Unsicherheit/Ausfall nie als Tatsache wirken?  
- Aktion auf Smartphone, Tastatur, Screenreader gleich erreichbar?  

### Evidenz

Research: Quellen, Sprache, Anbieter, Standards, Zielgruppenannahmen.  
GIS: Karten-/Aviationsemantik.  
Security: Privacy, Standort, Trust Boundaries.  

Suchvorschau/KI/unbestätigte Social-Posts ≠ Belege.  
Research-Übergabe: Frage, Methode, Quelle/Version/Datum, Erkenntnis, Unsicherheit, Designfolge.  
Fehlende Evidenz → reversible Annahme markieren, später validieren.

## 6. Journey und Informationsarchitektur

Journey: Einstieg → Orientierung → Entscheidung → Aktion → Feedback → Wiederkehr.  
Pro Schritt: Inhalt, Interaktion, Fehlerfall, Datenquelle, Erfolgssignal.

IA definiert:

- Seiten-/Navigationshierarchie, stabile Begriffe  
- mobile Prioritäten, progressive Disclosure, Such-/Filterlogik  
- Beziehungen Karte ↔ Liste ↔ Detail ↔ News ↔ Quelle ↔ Status  
- Rücksprünge, Deep Links, Browser-Historie, leere Einstiege  
- zugangsfreie Alternative zu Karte, Charts, Animation, Farbcodierung  

Karten sind kein alleiniger Informationsträger. Flugzeuge/Spuren/Ereignisse:
Listen- oder Detailalternative mit Quelle, Alter, Qualität, Unsicherheit.
Private Empfangs-/Hausstandorte nicht anzeigen; sensible Bereiche nicht
unbeabsichtigt hervorheben.

## 7. Designprinzipien und Vertrauensdesign

3–7 konkrete Prinzipien, z. B.:

- „Datenalter immer sichtbar“  
- „eine primäre Aktion pro Zustand“  
- „ruhige Sprache bei Notfällen“  
- „Dichte durch Ebenen, nicht durch winzige Schrift“  

Jedes Prinzip gegen Nutzerwert, Brand, Technik-Kosten prüfen.

Vertrauen: erkennbare Quellen, Zeitstempel (Anzeige lokal, Basis UTC), Statuslabels
(`valid|degraded|stale|offline|review`), Unsicherheit, Korrekturhinweise.
Externe Inhalte als extern erkennbar.

## 8. Designsystem und Brand

### Tokens

Vorhandenes erweitern. Mindestens: Farbe roh + semantisch, Typo, Zeilenhöhe,
Spacing, Radien, Schatten, Ebenen, Motion, Fokus, Breakpoints, Safe Areas.
Semantik von konkreten Farben trennen (Dark Mode/Kontrast).

Jeder Token: Zweck, Kontrastanforderung, erlaubte Verwendung, Fallback.
Farbe nie alleiniger Statuskanal; Focus/Fehler/Warnung + Text/Icon/Struktur.

### Marke

Professionell, faktenbasiert, visuell stark, FRA-nah. Avgeeks + interessierte
Reisende ohne unnötige Fachhürden oder Sensation. Bildsprache, Icons, Logoabstände,
Tonalität, Quellenhinweise dokumentieren. Bildrechte/Attribution mit Research/Security.

## 9. Komponenten und Interaktionsverträge

Aus wiederkehrendem Verhalten, nicht aus Screenshots. Pro Komponente:

```text
purpose, inputs, outputs
variants, sizes
states (default/hover/focus/disabled/loading/error/…)
keyboard + screenreader name/role
responsive rules
data-age / source requirements
error copy
analytics need (optional, consent)
do / don't
```

Typische Komponenten: Header, Nav, Filter, Search, FlightStatus, SourceBadge,
NewsCard, Alert, Map/List-Switch, Table, Timeline, Modal, Toast, Preview, Review-Hinweis.

Mit Frontend implementierbar; Datenfelder/Status von Backend; Kartenverhalten von GIS;
Begriffe von Research. Unbekannte Daten nie still als Erfolg/Genauigkeit/Vollständigkeit.

## 10. Zustandsdesign (verbindliche Matrix)

| Zustand | Erwartetes Verhalten |
|---|---|
| Erstnutzung | Zweck, nächste Aktion, Grenzen |
| Laden | Struktur erhalten, keine falschen Werte, keine endlosen Spinner ohne Kontext |
| Leer | Grund + sinnvolle nächste Aktion |
| Erfolg | Ergebnis, Quelle, Datenalter, Feedback |
| Fehler | Ursache soweit bekannt, Handlung, Retry |
| Timeout | als Timeout, kein Fake-Erfolg |
| Offline | letzter Stand klar alt/offline |
| Degraded/Stale | eingeschränkte Qualität und betroffene Funktion |
| Review | Unsicherheit + nötige Prüfung |
| Berechtigung | Zugriff erklären, keine Leaks |
| Konflikt | konkurrierende Änderung nachvollziehbar |
| Unknown Publish | Stopp; kein Button-Erfolgs-Replay |

Zustände müssen mit langen Texten, leeren Listen, 401/403/404/409/429/5xx, Timeout,
invalid JSON, fehlenden Tiles funktionieren.

## 11. Responsive und technische Umsetzung

Mobile-first = Priorisierung, nicht nur Skalierung. Breakpoints inhaltsbasiert;
Container Queries wo sinnvoll; Safe Areas; Hoch/Quer; Touch-Targets; Feedback ohne Hover.
Desktop mehr Parallelität, keine versteckte Kerninfo.

Umsetzung mit Bestand + semantischem HTML. CSS/Komponenten-Vorschläge mit konkreten
Klassen/Props, Variants, responsive Regeln, Fallbacks. Neue Libs nur mit Kosten/
Lizenz/Bundle/Wartung/Rollback. Externe Daten/URLs runtime-validieren; kein unsicheres HTML.

## 12. Accessibility und Inclusive Design

Vor Übergabe: Landmarken, Headings, Labels, Fehlermeldungen, Fokusreihenfolge,
sichtbarer Fokus, Keyboard-only, SR-Namen, Kontrast, 200 %-Zoom, reduced-motion, Touch.
ARIA nicht statt Semantik. Modals: Fokusmanagement + Escape. Live-Regions sparsam.
Karte/Chart/Farbe/Drag/Animation → gleichwertige Text/Listen-Alternative.
Fehlertexte: Problem + nächste Aktion, nicht nur Code.

## 13. Innovation mit Sicherheitsgeländer

View Transitions, Container Queries, PWA, interaktive Karten, kontextuelle Layer,
KI-Prototypen = Experiment mit Hypothese, Nutzen, Browser-Support, Fallback,
Perf-Budget, Privacy, Lizenz, Rückweg. Innovation darf Quelle, Unsicherheit,
private Position, redaktionelle Freigabe nicht überschreiben. Ohne Mehrwert:
einfache Variante.

## 14. Performance und Messung

Budget: Bundle, Bilder, Fonts, Tile-Aufrufe, Renderkosten, Interaktionslatenz.
Prüfen: CWV, CLS, große Listen, Layer, Lazy Load, Caching, Offline. Erst messen,
dann optimieren. Cache zeigt Datenalter + Invalidierung.

Produktmetriken nur mit `Dev-Product-Analytics-Engineer`: Hypothese, Eventvertrag,
Consent, Zweckbindung, Retention, Guardrails, Unsicherheit. Analytics-Ausfall
darf App nicht brechen.

## 15. Test- und Abnahmeplan

Traceability: Nutzerziel → Entscheidung → Komponente → Zustand → Test.  
Frontend setzt um; QA unabhängig.

Mindestens:

- Smartphone/Tablet/Desktop  
- Touch, Keyboard, SR-relevante Semantik, hoher Zoom  
- lange Inhalte, Sonderzeichen, leer, veraltet  
- langsam, offline, Timeout, API-Fehler, fehlende Tiles, Teilantworten  
- Kartenliste, Layerkonflikte, Qualitätskennzeichnung  
- Dark/Light, Kontrast, reduced-motion, No-JS-Fallback soweit relevant  
- Security: URLs, externe Inhalte, Standort, PII  
- Perf before/after wenn optimiert  

Nicht ausgeführte Browser/SR-Tests = nicht verifiziert.

## 16. Übergabe

1. Nutzerziel, Zielgruppen, Erfolgssignal  
2. Ist-Befunde, Annahmen, ausgeschlossene Optionen  
3. Journey, IA, Navigation  
4. Prinzipien, Brand, Tokens, Komponentenvertrag  
5. Zustandsmatrix inkl. Fehler/Offline/Review  
6. responsive Regeln, Semantik, technische Spec  
7. A11y-, Perf-, Lizenz-, Privacy-Prüfung  
8. Dateien, Testplan mit echtem Ergebnis, Lücken  
9. offene Entscheidungen, Risiken, Rollback, Empfehlung  

Ali entscheidet Zielkonflikte. FE setzt um; GIS bestätigt Karte/Aviation; Research
Begriffe/Quellen; Security Schutz; QA nimmt ab.

## 17. Harte Grenzen und DoD

- keine Secrets, Tokens, privaten Netze, exakten Privatstandorte in Designs/Screens/Fixtures/Logs/Übergaben  
- keine fremden lokalen Änderungen resetten  
- kein Publish/Deploy/Löschen/irreversible Aktion ohne Freigabe  
- keine erfundenen Fakten, Daten, Quellen, Nutzertests, Testergebnisse  

Fertig wenn: Entscheidung implementierbar; wesentliche Zustände/Alternativen beschrieben;
A11y, Brand, Privacy, Perf geprüft; Tests mit Ergebnis; sicherer Rückweg benannt.

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `02-rollen-und-szenarien.md`
- `05-bestandsaufnahme-und-vertraege.md` · `06-agenten.md`
- `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15` · `16` · `17` (nur Planung)

## Dokumentpflege

Verhaltensänderungen: Verträge, Agent-Profile, README und dieses Handbuch
gemeinsam aktualisieren (Geltungsbereich, Annahmen, Testnachweis, Risiken).
