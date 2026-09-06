# AeroNewsFRA Instagram Connector

Lokale FastAPI-Anwendung für den offiziellen Instagram Login über die Meta Graph API. Die Anwendung verwendet keine Instagram-Passwörter und veröffentlicht nur nach manueller Bestätigung.

## Start unter Windows

```powershell
py -3 -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
python -m uvicorn app.main:app --reload --host 127.0.0.1 --port 8000
```

Danach `http://127.0.0.1:8000` öffnen. In `.env` müssen `META_APP_ID` und `META_APP_SECRET` eingetragen werden. Die Redirect-URI muss in der Meta-App exakt `http://127.0.0.1:8000/auth/callback` sein.

Ein Bild muss für die Meta API über eine öffentliche HTTPS-URL erreichbar sein. Eine lokale Datei-URL funktioniert nicht. Für lokale Tests kann später ein temporärer HTTPS-Tunnel verwendet werden.

## MCP

Der MCP-Prozess wird aus dem Projektordner mit `python mcp_server.py` gestartet. Die MCP-Laufzeit muss separat installiert werden, falls sie in der OpenCode-Umgebung noch fehlt. Die Werkzeuge speichern Entwürfe, lesen Status und verlangen für `publish_post` zwingend `confirmed=true`.

## Sicherheit

`.env`, Token-Datei, SQLite-Datenbank und Medien sind in `.gitignore` eingetragen. Niemals echte Zugangsdaten in Quellcode, Chat oder Dokumentation eintragen.

## Ist-Zustand und Betriebsvertrag

Der Connector ist lokal; die Unterlagen in `aeronewsfra2/` beschreiben ein
Zielbild und keine bereits implementierten Funktionen. Der Dienst bleibt an
`127.0.0.1` gebunden. Der sichere Ablauf lautet: Fakten/Quelle -> Validierung ->
Entwurf -> Vorschau -> explizite Bestätigung -> Publish -> Status erneut lesen.
Bei Timeout oder unbekanntem Meta-Status wird nicht erneut veröffentlicht.

Zu testen sind fehlende Konfiguration, ungültige Caption/Bild-URL, leere Daten,
doppelter Publish-Aufruf, 401/403/429/5xx, Timeout, Neustart und maskierte
Statusausgabe. Ein lokaler Start ist kein Nachweis für einen Meta-Integrationstest.
