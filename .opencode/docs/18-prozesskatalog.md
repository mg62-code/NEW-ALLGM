---
dokument_id: DOC-18
titel: Prozesskatalog AeroNewsFRA
version: "2.0"
status: verbindlich
owner: Dev-Ali
aktualisiert: 2026-08-24
geltung: Schnellfind und Ablaufketten
---

# Prozesskatalog AeroNewsFRA

> **Lesart:** Operative Prozessdokumentation. Ist und Zielbild getrennt.
> Keine Secrets, keine unbewiesenen Erfolge.


## 1. Zweck

Zentraler Katalog aller Kernprozesse mit Kurz-Kette und Verweis auf Detailhandbuch.
Für Agents: hier starten, dann Detail-Doc öffnen.

## 2. Legende

`→` sequentiell · `||` parallel erlaubt · `[Freigabe]` Stopp bis Bestätigung

## 3. Kernentwicklungsprozesse

| ID | Name | Kurz-Kette | Detail |
|---|---|---|---|
| P-ENG-01 | End-to-End Feature | Auftrag→Bestand→Design→Vertrag→Build→Test→Gate→Übergabe | `01` |
| P-ENG-02 | Bugfix | Symptom→Repro→Ursache→Fix→Regression→Gesamttest | `01`,`07` |
| P-ENG-03 | Requirements | Problem→Muss/Soll/Kann→Kriterien→Vertrag→Schnitt | `01` |
| P-ENG-04 | Code-Review/Diff | status→diff→secrets scan→tests→entscheid | `03`,`04` |
| P-ENG-05 | Tool-Kette | status→glob→read→grep→edit→test→diff-check | `03` |

## 4. Rollenprozesse

| ID | Name | Kurz-Kette | Detail |
|---|---|---|---|
| P-QA-01 | Unabhängige Abnahme | Scope→Matrix→Tests→Befunde→Gate | `07` |
| P-RES-01 | Faktenrecherche | Frage→Primär→Gegen→Konfidenz→Faktenobjekt | `08` |
| P-SEC-01 | Security-Gate | Assets→Abuse→Review→Negativ→Gate | `09` |
| P-FE-01 | Frontend Feature | Journey→State→UI→A11y→Browser→Perf | `10` |
| P-BE-01 | API/Backend | Vertrag→Auth→Tx→Idempotenz→Obs→Migration | `11` |
| P-GIS-01 | Layer/ADS-B | Lizenz→CRS→Plausibilität→Layer→Privacy→Test | `12` |
| P-UX-01 | UX Delivery | JTBD→IA→Tokens→States→Handoff | `13` |
| P-TEAM-01 | Multi-Agent | Intake→Owner→Parallel→Gates→Integration | `14` |

## 5. Daten- und Integrationsprozesse

| ID | Name | Kurz-Kette | Detail |
|---|---|---|---|
| P-DAT-01 | Datenvertrag anlegen | Felder UTC quality status idempotency | `05`,`04` |
| P-DAT-02 | Migration | Backup→Expand→Backfill→Testklon→Freigabe→Apply | `11` |
| P-DAT-03 | Cache | Key→TTL→Invalidate→stale kennzeichnen | `11` |
| P-DAT-04 | Job/Queue | Lease→Run→Retry→DLQ→Shutdown | `11` |
| P-API-01 | Externe API | Research→Vertrag→Timeout/Retry→Mock-Negativ | `02`,`11` |
| P-IG-01 | Instagram Draft→Publish | status→draft→preview→[Freigabe]→publish→re-status | `01`,`05`,`03` |
| P-IG-02 | Unknown Publish | STOP→manuell status→kein Retry | `05`,`09` |

## 6. Aviation/Kartenprozesse (Zielbild-ready)

| ID | Name | Kurz-Kette | Detail |
|---|---|---|---|
| P-AV-01 | Receiver Ingestion | Auth→Raw→Validate→Normalize→Dedupe→Store | `12`,`17` |
| P-AV-02 | Live Layer | Fetch→age check→render/cluster→stale style | `12`,`16` |
| P-AV-03 | Track/Replay | Query→timeline→visual interp only→share URL | `17` |
| P-AV-04 | Event Candidate | Rule→score→evidence→review queue | `17`,`08` |
| P-MAP-01 | Tile/Provider | ToS→Attribution→Cache→Fallback | `15`,`12` |

## 7. Content/KI-Prozesse

| ID | Name | Kurz-Kette | Detail |
|---|---|---|---|
| P-CNT-01 | News Pipeline | Beobachtung→Fakten→Gegen→Draft→Review→[Freigabe]→Publish | `01`,`08` |
| P-CNT-02 | KI nur aus Facts | Fact Pack→Prompt Policy→Draft→Match-Check→Review | `17` |
| P-CNT-03 | Leere Lage | bestätigen→transparent→Evergreen Entwurf optional | `08`,`02` |
| P-CNT-04 | Korrektur | Fehler→neue Version→Historie behalten→Hinweis | `16` |

## 8. Security/Incident/Release

| ID | Name | Kurz-Kette | Detail |
|---|---|---|---|
| P-SEC-02 | Secret-Leak | stop→minimal doku→rotate Betreiber→Negativ | `09` |
| P-SEC-03 | Privacy Standort | stop publish→redact→verify no coords | `09`,`12` |
| P-INC-01 | Incident | detect→contain→evidence→fix→smoke→restart→LL | `01`,`05` |
| P-REL-01 | Release | diff→test→build→preview smoke→[Freigabe]→deploy→monitor | `01`,`14` |
| P-REL-02 | Rollback | last good artifact/commit→verify→comms | `05` |
| P-REL-03 | Pages Bot Deploy | commit→workflow_run→build→deploy→smoke | `09`,`15` |

## 9. UX/Produktprozesse

| ID | Name | Kurz-Kette | Detail |
|---|---|---|---|
| P-UX-02 | Zustandsdesign | matrix je View inkl. offline/stale/review | `13`,`16` |
| P-UX-03 | A11y Gate | Semantik→Keyboard→Kontrast→Zoom→SR | `13`,`10` |
| P-PRD-01 | Monetarisieren | erst Qualität+Traffic→Consent→Messung→Launch | `15`,`17` |
| P-PRD-02 | Analytics | Hypothese→Eventvertrag→Consent→Instrument→Guardrail | `04`,`13` |

## 10. Zielbild-Phasenprozesse

| ID | Phase | Einstieg |
|---|---|---|
| P-Z0 | Stabilität Pages/News | `15` §9 |
| P-Z1 | Echte Karte | `15`,`16`,`17` Map Core |
| P-Z2 | Live-API | `15`,`11` |
| P-Z3 | Receiver | `17` Gateway |
| P-Z4 | Historie/Replay | `17` Flight Store |
| P-Z5 | Automation/KI | `17` AI Studio + Event |
| P-Z6 | Produkt/Monetarisierung | `15` Phase 6 |

## 11. Stop-Regeln (global)

1. Secret im Diff/Chat → stop + Security  
2. Unknown Publish → kein zweites Publish  
3. Safety Content → Human Review  
4. Migration ohne Backup-Nachweis → kein Prod  
5. Zielbild als Ist behaupten → korrigieren  
6. Fremde Worktree-Änderungen → nicht anfassen  

## 12. Schnellwahl nach Symptom

| Symptom | Starte Prozess |
|---|---|
| Button/UI kaputt | P-ENG-02 + P-FE-01 |
| API 500/Timeout | P-BE-01 + P-QA-01 |
| Karte falsch/stale | P-GIS-01 / P-AV-02 |
| Zweifel an Meldung | P-RES-01 + P-CNT-01 |
| Token/Auth Problem | P-SEC-01 (ohne Secret-Ausgabe) |
| Deploy bringt keine Daten | P-REL-03 |
| Doppelter IG-Post | P-IG-02 + P-SEC-01 |
| Agent blockiert | `02` S12 + `14` |

## 13. Qualitätsdefinition katalogweit

Prozess „wirksam“, wenn er: Owner, Eingabe, Ausgabe, Fehlerpfad, Nachweis und
Rollback benennt – und in einem Fachhandbuch detailliert ist.

## 14. Vollständige Ablaufketten (Copy-Paste für Agents)

### Feature End-to-End

```text
P-ENG-01 → (optional P-RES-01 || P-SEC-01) → Vertrag P-DAT-01
→ P-FE-01 und/oder P-BE-01 und/oder P-GIS-01
→ P-QA-01 → P-TEAM-01 Integration → optional P-REL-01
```

### Live-Karte Zielbild

```text
P-Z1 Map → P-MAP-01 Tiles → P-AV-01 Receiver → P-AV-02 Live Layer
→ P-GIS-01 Privacy/Liste → P-QA-01 Last/Offline → P-REL-01
```

### Content Tag

```text
P-RES-01 → P-CNT-01 → optional P-CNT-02 KI
→ Human Review → optional P-IG-01 → P-CNT-04 bei Korrektur
```

### Incident Secret

```text
P-SEC-02 → P-INC-01 contain → Rotation Betreiber
→ P-QA-01 Negativ → P-REL-02 falls nötig
```

## 15. Prozess-Ownership-Schnelltabelle

| Prozessfamilie | Default-Owner |
|---|---|
| ENG | Ali |
| QA | QA |
| RES | Research |
| SEC | Security |
| FE | Frontend |
| BE/DAT/API | Backend |
| AV/MAP/GIS | GIS |
| UX | UX |
| REL/INC Betrieb | DevOps + Ali |
| CNT | Research + Ali |
| Z-Phasen | Ali plant, Fach setzt um |

## Verwandte Dokumente

- `00-index.md` · `01-prozesshandbuch.md` · `05` · `06` · `14` · `18`
- Zielbild: `15` · `16` · `17`

## Dokumentpflege

Änderungen an Verhalten erfordern synchrone Doku-/Vertrags-Updates mit
Geltungsbereich, Annahmen, Testnachweis und Risiken.
