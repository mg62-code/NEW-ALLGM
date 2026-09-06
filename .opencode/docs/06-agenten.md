---
dokument_id: DOC-06
titel: Agentenregister
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: Agent-Aufruf und Kompatibilität
---

# Agentenregister

> **Lesart:** Operative Prozessdokumentation. Schritte nennen Zweck, technische
> Arbeit, Eingabe, Ausgabe, Fehlerpfad und Nachweis. Ist-Bestand und Zielbild
> (aeronewsfra2) bleiben getrennt. Keine Secrets oder unbewiesenen Erfolge.


## 1. Zweck

Verzeichnis der sichtbaren Dev-Agenten, Schwerpunkte, Kompatibilitäts-Aliases
und Übergabestandard.

## 2. Aktive Dev-Agenten

| Agent | Schwerpunkt | Prozesshandbuch |
|---|---|---|
| `Dev-Ali` | Leitung, Architektur, Integration | `01`, `14` |
| `Dev-QA-Engineer` | Tests, Regression, Qualitätsnachweis | `07` |
| `Dev-Research-Analyst` | Quellen, Recherche, Fakten | `08` |
| `Dev-Security-Reviewer` | Security, Privacy, Compliance | `09` |
| `Dev-Frontend-Specialist` | Frontend, A11y, Performance | `10` |
| `Dev-Backend-Data-Specialist` | APIs, Daten, Persistenz | `11` |
| `Dev-GIS-Aviation-Specialist` | Karten, GIS, ADS-B | `12` |
| `Dev-UX-UI-Brand-Specialist` | UX, UI, Designsystem, Brand | `13` |
| `Dev-DevOps-Release-Engineer` | CI/CD, Release, Betrieb | `01`, `14`, `05` |
| `Dev-Data-Quality-Engineer` | Datenverträge, Provenienz, Qualität | `05`, `11`, `12` |
| `Dev-Product-Analytics-Engineer` | datensparsame Produktmessung | `04`, `13` |

Profile: `.opencode/agent/` (Dateien, nicht Inline-Konfiguration).

## 3. Kompatibilität

Frühere Kurznamen bleiben als `hidden: true`-Aliases:

`qa-engineer`, `research-analyst`, `frontend-specialist`,
`backend-data-specialist`, `gis-aviation-specialist`, `security-reviewer`,
`ux-ui-brand-specialist`.

**Neue Aufrufe und Projektverweise verwenden ausschließlich Dev-Namen.**

## 4. Aufrufprozess

```text
Bedarf aus Matrix 02/14 wählen
→ Auftrag mit Grenzen formulieren
→ keine Secrets übergeben
→ Ergebnis gegen Code/Tests prüfen
→ integrieren
→ QA unabhängig
```

## 5. Übergabestandard

Jeder Agent liefert: Auftrag, geprüfter Kontext, Entscheidung, Dateien,
Tests mit echtem Ergebnis, nicht verifiziert, Annahmen, Risiken, Rollback,
Empfehlung.

Öffentliche Aktionen, Deployments, Veröffentlichungen, Löschungen und
Secret-Änderungen bleiben freigabepflichtig.

## 6. Agent-Auswahl-Entscheidungsbaum

```text
Ist es primär Test/Abnahme? → Dev-QA-Engineer
Ist es Quelle/Fakt/Lizenz? → Dev-Research-Analyst
Ist es Threat/Privacy/Secret? → Dev-Security-Reviewer
Ist es Markup/Browser/A11y? → Dev-Frontend-Specialist
Ist es API/DB/Job? → Dev-Backend-Data-Specialist
Ist es Karte/ADS-B/CRS? → Dev-GIS-Aviation-Specialist
Ist es Journey/Brand/IA? → Dev-UX-UI-Brand-Specialist
Ist es CI/CD/Deploy-Pfad? → Dev-DevOps-Release-Engineer
Ist es Datenqualität/Provenienz? → Dev-Data-Quality-Engineer
Ist es Produktmessung/Consent-Events? → Dev-Product-Analytics-Engineer
Sonst / Integration / unklar → Dev-Ali
```

## 7. Mindestkontext im Agent-Aufruf

1. Ziel und Nicht-Ziele
2. betroffene Dateien oder Suchhinweise
3. Ist vs Zielbild
4. Akzeptanzkriterien
5. Grenzen (kein Publish/Deploy/Secret)
6. gewünschtes Ausgabeformat
7. bekannte Risiken

## 8. Qualitätsgate nach Agent-Rückkehr

- [ ] Aussagen gegen Code/Quellen geprüft
- [ ] keine Secret-Leaks in der Antwort
- [ ] Tests nachvollziehbar
- [ ] Konflikte mit anderen Rollen gelöst
- [ ] Integration durch Ali geplant

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `05-bestandsaufnahme-und-vertraege.md`
- `06-agenten.md` · `14-prozesshandbuch-teamkoordination.md` · `18-prozesskatalog.md`
- Zielbild: `15-zielbild-bauplan-2.0.md` · `16-zielbild-seiten-und-bedienung.md` · `17-zielbild-module-und-technik.md`

## Dokumentpflege

Bei Verhaltensänderungen Verträge, Agent-Profile, README und dieses Handbuch
gemeinsam aktualisieren. Jede Änderung: Geltungsbereich, Annahmen, Testnachweis,
offene Risiken.
