---
dokument_id: DOC-01
titel: Prozesshandbuch – End-to-End Entwicklung und Betrieb
version: "2.1"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-09-12
geltung: alle Entwicklungs-, Content-, Betriebs- und Incident-Aufgaben
---

# Prozesshandbuch – End-to-End Entwicklung und Betrieb (v2.1)

> **Lesart:** Dieses Dokument ist operative Prozessdokumentation. Jeder Schritt
> nennt Zweck, technische Detailarbeit, Eingaben, Ausgaben, Fehlerpfade und
> Nachweis. Es enthält verbindliche Denk- und Arbeitsmechanismen für alle Agents.

## 1. Zweck und Geltungsbereich

Dieses Handbuch beschreibt den **verbindlichen Ablauf** von der Anfrage bis zum
Betrieb für alle Aufgaben. Es stellt sicher, dass Agents
wie ein professionelles, proaktives und selbst-optimierendes Team arbeiten.

## 2. Prozessübersicht

```text
P01 Auftrag schärfen
 → P02 Bestandsaufnahme
 → P02.1 Context Checksum (NEU)
 → P03 Diagnose und Design (inkl. 3-Hypothesen-Regel)
 → P04 Verträge fixieren
 → P04.1 Tool-Wheel Scan (NEU)
 → P05 Umsetzung
 → P06 Verifikation
 → P07 Security-/Fach-Gates
 → P08 Abschlussprüfung
 → P09 Dokumentation/Übergabe (inkl. Self-Reporting)
 → P10 Betrieb/Monitoring
```

## 3. Neue Denk- & Arbeitsmechanismen (v2.1)

### 3.1 Context Checksum (nach P02)

**Zweck:** Sicherstellen, dass jeder Agent mit dem vollen und aktuellen Projektwissen arbeitet.
**Arbeit:** Vor Beginn der Diagnose (P03) führt jeder Agent eine mentale Checkliste aus:
- `[ ] 00-index.md` gelesen? (Die "Landkarte" des Wissens)
- `[ ] 22-projektstatus-aktuell.md` gelesen? (Live-Status, URLs, Blocker)
- `[ ] 99-agent-improvement-protocol.md` gelesen? (Die Lern-Regeln)
- `[ ] Relevante Fach-Handbücher (07-14) für diese Aufgabe identifiziert?`

Erst wenn alle Punkte bejaht sind, wird die Arbeit fortgesetzt.

### 3.2 Die 3-Hypothesen-Regel (in P03)

**Zweck:** Kreative und systematische Lösungsfindung bei Blockern oder unerwarteten Fehlern.
**Arbeit:** Bei einem Blocker stoppt der Agent und formuliert **drei unterschiedliche Hypothesen** für die Ursache, bevor er handelt.
- **Hypothese 1 (Die wahrscheinlichste):** z.B. "Dem Nutzer fehlt eine IAM-Rolle."
- **Hypothese 2 (Eine Alternative):** z.B. "Die API ist im Projekt noch nicht aktiviert."
- **Hypothese 3 (Ein Edge Case):** z.B. "Eine übergeordnete Organisations-Policy blockiert die Aktion."

Anschließend wird die wahrscheinlichste Hypothese mit dem kleinstmöglichen Test überprüft.

### 3.3 Der Tool-Wheel Scan (vor P05)

**Zweck:** Sicherstellen, dass immer das effizienteste und spezialisierteste Werkzeug für eine Aufgabe genutzt wird.
**Arbeit:** Vor der Umsetzung (P05) führt der Agent einen mentalen "Tool-Wheel" Scan durch:
- **Dateisystem?** -> `glob`, `read`, `grep` sind `bash`-Befehlen überlegen.
- **Komplexe Aufgabe?** -> `task` mit Sub-Agenten für Parallelisierung nutzen.
- **Web-Interaktion?** -> `playwright_browser` ist das richtige Werkzeug.
- **Externes Wissen?** -> `webfetch` für Dokumentationen nutzen.

## (Rest des Dokuments bleibt erhalten, hier aus Kürze weggelassen)

< Gekürzter Inhalt des vorherigen Dokuments... >
