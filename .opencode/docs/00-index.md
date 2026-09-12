---
dokument_id: DOC-00
titel: AeroNewsFRA Engineering Documentation – Index
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: alle Agents und Rollen
---

# AeroNewsFRA Engineering Documentation – Index

> **Lesart:** Dieses Dokument ist operative Prozessdokumentation. Jeder Schritt
> nennt Zweck, technische Detailarbeit, Eingaben, Ausgaben, Fehlerpfade und
> Nachweis. Ist-Bestand und Zielbild (aeronewsfra2) bleiben strikt getrennt.
> Keine Secrets, privaten Standorte oder unbewiesenen Erfolge.


## Zweck

Diese Dokumente sind der zentrale Arbeitskontext für `Dev-Ali` und alle
Subagents. Sie ergänzen die Agent-Profile unter `.opencode/agent/`. Bei
Widersprüchen gelten: **Systemregeln → Sicherheitsregeln → Nutzerfreigabe →
projektweite Standards → Fachquellen → Empfehlungen**.

## Dokumentenkarte

| ID | Datei | Inhalt | Wann lesen |
|---|---|---|---|
| 00 | `00-index.md` | Orientierung, Lesereihenfolge, Pflege | immer zuerst |
| 01 | `01-prozesshandbuch.md` | End-to-End-Prozess Anfrage→Betrieb | jede Aufgabe |
| 02 | `02-rollen-und-szenarien.md` | Rollen, RACI, Szenarien | Delegation |
| 03 | `03-opencode-und-tools.md` | Werkzeuge, Git, MCP, Grenzen | Tool-Nutzung |
| 04 | `04-technische-projektstandards.md` | Code-, Daten-, Web-, Security-Standards | Implementierung |
| 05 | `05-bestandsaufnahme-und-vertraege.md` | Bestand, Verträge, Freigaben, Betrieb | Architektur/Integration |
| 06 | `06-agenten.md` | Agentenregister und Aliases | Agent-Aufruf |
| 07 | `07-prozesshandbuch-qa.md` | QA-Prozesse | Tests/Abnahme |
| 08 | `08-prozesshandbuch-recherche.md` | Recherche und Fakten | Quellen/Content |
| 09 | `09-prozesshandbuch-security.md` | Security und Datenschutz | Risiko/Freigabe |
| 10 | `10-prozesshandbuch-frontend.md` | Frontend-Prozesse | UI/Browser |
| 11 | `11-prozesshandbuch-backend-daten.md` | Backend/API/Daten | Services/DB |
| 12 | `12-prozesshandbuch-gis-aviation.md` | GIS/ADS-B/Karten | Live-Flug/Karte |
| 13 | `13-prozesshandbuch-ux-ui-brand.md` | UX/UI/Brand | Journey/Design |
| 14 | `14-prozesshandbuch-teamkoordination.md` | Team-Gates und Übergaben | Mehrrollen-Arbeit |
| 15 | `15-zielbild-bauplan-2.0.md` | Bauplan 2.0 (Zielbild) | Planung 2.0 |
| 16 | `16-zielbild-seiten-und-bedienung.md` | Seiten/Bedienung Zielbild | Portal-UI |
| 17 | `17-zielbild-module-und-technik.md` | Module/Technik Zielbild | Modulbau |
| 18 | `18-prozesskatalog.md` | Prozesskatalog und Ablaufketten | Prozesssuche |
| 22 | `22-projektstatus-aktuell.md` | Live-Status, URLs, Blocker | Jede neue Session |

## Einheitliches Dokumentformat

Jedes Prozesshandbuch folgt derselben Gliederung:

1. Metadaten / Zweck / Geltung  
2. Rollen und Verantwortung (RACI)  
3. Eingänge, Vorbedingungen, Outputs  
4. Begriffe, Status- und Datenmodelle  
5. Prozessübersicht (Ablaufkette)  
6. Detaillierte Prozessschritte mit Technik  
7. Spezialprozesse und Szenarien  
8. Qualitätsgates, Negativfälle, Tools  
9. Zusammenarbeit, Übergabe, Checkliste  
10. Verwandte Dokumente und Pflege  

Technische Detailtiefe pro Schritt umfasst: **Zweck · Arbeit · Eingabe · Ausgabe ·
Fehler/Ausnahme · Nachweis/Tool · Owner**.

## Lesereihenfolge

### Neue Aufgabe (Standard)

1. `00-index.md`  
2. `01-prozesshandbuch.md`  
3. `02-rollen-und-szenarien.md` und `06-agenten.md`  
4. `03-opencode-und-tools.md` + `04-technische-projektstandards.md`  
5. `05-bestandsaufnahme-und-vertraege.md` bei Architektur/Integration  
6. Fachhandbuch `07`–`13` je Rolle  
7. `14-prozesshandbuch-teamkoordination.md` bei mehreren Rollen  
8. Zielbild `15`–`17` nur wenn 2.0-Funktionen geplant werden  
9. `18-prozesskatalog.md` zur Prozesssuche  

### Nur Fehlerbehebung

`01` → Fachhandbuch → `07` QA → Diff/Tests → Übergabe.

### Nur Zielbild-Planung

`05` (Ist) → `15`/`16`/`17` (Soll) → `01`/`14` (Umsetzungsprozess).  
**Niemals Zielbild als implementierten Bestand ausgeben.**

## Bestehende Fachquellen (Projektstamm)

| Quelle | Nutzen |
|---|---|
| `README.md` | aktueller technischer Stand, lokaler Instagram-Connector |
| `Skill Anweisung aeronewsFRA.txt` | Content-, Recherche-, Quellenregeln |
| `Anweisung Instagram OpenCode Aufbau.txt` | Meta-API, Sicherheit, Akzeptanztests |
| `Aufbau MusterVorlage automation.txt` | Content-Automationsvorlage |
| `aeronewsfra2/*.html` | Zielbild-Quellen; Markdown-Spiegel unter `15`–`17` |

## Zentraler Grundsatz

Eine Aufgabe ist erst abgeschlossen, wenn sie **funktional umgesetzt, angemessen
getestet, sicher, dokumentiert und übergabefähig** ist. Kein Agent darf fehlende
Tests, Quellen, Zugriffe oder Erfolge behaupten.

## Widerspruch und Pflege

Agent-Profile konkretisieren, schränken aber projektweite Regeln nicht ein.
Fachquellen liefern Domänenwissen; sie ersetzen keine Sicherheits-, Freigabe-
oder Verifikationsregel. Bei Verhaltensänderungen API-/Datenverträge,
Agent-Regeln, README und Fachvorlagen gemeinsam aktualisieren.

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
