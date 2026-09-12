# 99 - Agent Improvement Protocol (A-R-C)

---
_dokument_id: DOC-99
titel: Protokoll zur kontinuierlichen Agenten-Verbesserung
version: "2.0"
status: verbindlich
owner: Dev-Ali
---

## 1. Zweck

Dieses Protokoll etabliert einen allgemeinen, fortlaufenden Mechanismus, durch den sich alle Agenten im OpenCode-System selbstständig verbessern. Das Ziel ist ein lernendes System, das aus Erfolgen und Fehlern lernt und seine eigene Effizienz und Intelligenz steigert.

## 2. Das A-R-C Protokoll mit "Self-Reporting"

Der Mechanismus basiert auf drei Schritten: **Analyse, Refine, Commit**.

### Schritt 1: Analyse (Datenerfassung & Mustererkennung)

**1.1. Self-Reporting (Verpflichtend für alle Sub-Agenten):**
Jeder Sub-Agent muss am Ende seiner Aufgabe, zusätzlich zu seinem Ergebnis, ein strukturiertes `PerformanceReview`-Objekt zurückgeben. Dieses Objekt ist Teil seines Arbeitsvertrages.

**Struktur `PerformanceReview`:**
```json
{
  "success": true, // oder false
  "duration_ms": 15000,
  "blocker_encountered": "IAM-Berechtigung 'artifactregistry.writer' fehlte.", // oder null
  "improvement_suggestion": "Das DevOps-Profil sollte einen Pre-flight-Check für alle gängigen IAM-Rollen enthalten, bevor ein Deployment gestartet wird." // oder null
}
```

**1.2. Analyse durch den `Dev-Quality-Coach`:**
Der `Dev-Quality-Coach` wird periodisch oder nach komplexen Aufgaben aufgerufen. Sein Input ist eine Sammlung dieser `PerformanceReview`-Objekte. Seine Aufgabe ist es, Muster zu erkennen:
*   Wiederkehrende Blocker.
*   Häufige Fehlertypen bei bestimmten Agenten.
*   Suboptimale Lösungswege.
*   Wertvolle Verbesserungsvorschläge von den Agenten selbst.

### Schritt 2: Refine (Anweisungen verfeinern)

Basierend auf der Analyse des Coaches wird eine konkrete Änderung für das `.md`-Profil eines Agenten formuliert. Dies ist ein hoch-priorisierter Task, der vom Lead (`Dev-Ali`) oder einem beauftragten Spezialisten durchgeführt wird.

**Beispiel:**
Der Coach meldet: "Der DevOps-Agent scheitert wiederholt an IAM-Rechten." -> Die Refine-Aktion wäre: Das Profil des `Dev-DevOps-Release-Engineer` wird um einen Abschnitt erweitert: "Prüfe vor jedem `gcloud builds` oder `gcloud run` Befehl proaktiv die notwendigen IAM-Rollen des ausführenden Service-Accounts."

### Schritt 3: Commit (Wissen verewigen)

Jede Änderung an einem Agenten-Profil wird mit einer standardisierten Commit-Nachricht auf GitHub gespeichert. Das macht das Lernen des Systems transparent und dauerhaft.

**Commit-Format:** `refactor(agent): <Agent-Name> - <Beschreibung der Verbesserung>`

**Beispiel:** `refactor(agent): Dev-DevOps-Release-Engineer - Add IAM pre-flight check to core workflow`

## 3. Implementierung

Dieser Mechanismus ist durch dieses Dokument und das Profil des `Dev-Quality-Coach` im System verankert. Die Einhaltung wird durch Code-Reviews und die Überwachung durch den `Dev-Quality-Coach` sichergestellt.
