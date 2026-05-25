---
title: Railway
source_url: https://docs.openclaw.ai/de/install/railway
scraped_at: 2026-05-25
---

# Railway

Stellen Sie OpenClaw mit einer One-Click-Vorlage auf Railway bereit und greifen Sie über die webbasierte Control UI darauf zu. Dies ist der einfachste Weg „ohne Terminal auf dem Server“: Railway führt das Gateway für Sie aus.

## Schnelle Checkliste (neue Benutzer)

  1. Klicken Sie auf **Deploy on Railway** (unten).
  2. Fügen Sie ein **Volume** hinzu, das unter `/data` gemountet ist.
  3. Setzen Sie die erforderlichen **Variables** (mindestens `OPENCLAW_GATEWAY_PORT` und `OPENCLAW_GATEWAY_TOKEN`).
  4. Aktivieren Sie **HTTP Proxy** auf Port `8080`.
  5. Öffnen Sie `https://<your-railway-domain>/openclaw` und verbinden Sie sich mit dem konfigurierten Shared Secret. Diese Vorlage verwendet standardmäßig `OPENCLAW_GATEWAY_TOKEN`; wenn Sie es durch Passwortauthentifizierung ersetzen, verwenden Sie stattdessen dieses Passwort.


## One-Click-Deployment

[ Deploy on Railway ](<https://railway.com/deploy/clawdbot-railway-template>)

Nach der Bereitstellung finden Sie Ihre öffentliche URL unter **Railway → Ihr Dienst → Settings → Domains**.

Railway wird entweder:

  * Ihnen eine generierte Domain geben (oft `https://<something>.up.railway.app`), oder
  * Ihre benutzerdefinierte Domain verwenden, wenn Sie eine hinzugefügt haben.


Öffnen Sie dann:

  * `https://<your-railway-domain>/openclaw` — Control UI


## Was Sie erhalten

  * Gehostetes OpenClaw Gateway + Control UI
  * Persistenter Speicher über Railway Volume (`/data`), damit `openclaw.json`, `auth-profiles.json` pro Agent, Kanal-/Provider-Status, Sitzungen und Workspace erneute Bereitstellungen überdauern


## Erforderliche Railway-Einstellungen

### Public Networking

Aktivieren Sie **HTTP Proxy** für den Dienst.

  * Port: `8080`


### Volume (erforderlich)

Hängen Sie ein Volume an, das unter folgendem Pfad gemountet ist:

  * `/data`


### Variables

Setzen Sie diese Variablen für den Dienst:

  * `OPENCLAW_GATEWAY_PORT=8080` (erforderlich — muss mit dem Port in Public Networking übereinstimmen)
  * `OPENCLAW_GATEWAY_TOKEN` (erforderlich; als Admin-Geheimnis behandeln)
  * `OPENCLAW_STATE_DIR=/data/.openclaw` (empfohlen)
  * `OPENCLAW_WORKSPACE_DIR=/data/workspace` (empfohlen)


## Einen Kanal verbinden

Verwenden Sie die Control UI unter `/openclaw` oder führen Sie `openclaw onboard` über die Railway-Shell aus, um Anweisungen zur Kanaleinrichtung zu erhalten:

  * [Telegram](</de/channels/telegram>) (am schnellsten — nur ein Bot-Token)
  * [Discord](</de/channels/discord>)
  * [Alle Kanäle](</de/channels>)


## Backups und Migration

Exportieren Sie Ihren Status, Ihre Konfiguration, Auth-Profile und Ihren Workspace:

bashCopy code
[code]
    openclaw backup create
[/code]

Dadurch wird ein portables Backup-Archiv mit dem OpenClaw-Status sowie jedem konfigurierten Workspace erstellt. Siehe [Backup](</de/cli/backup>) für Details.

## Nächste Schritte

  * Messaging-Kanäle einrichten: [Channels](</de/channels>)
  * Das Gateway konfigurieren: [Gateway configuration](</de/gateway/configuration>)
  * OpenClaw aktuell halten: [Updating](</de/install/updating>)


Was this useful?YesNo