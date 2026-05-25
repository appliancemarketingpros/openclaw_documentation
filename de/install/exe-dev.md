---
title: exe.dev
source_url: https://docs.openclaw.ai/de/install/exe-dev
scraped_at: 2026-05-25
---

Ziel: OpenClaw Gateway läuft auf einer exe.dev-VM und ist von Ihrem Laptop erreichbar über: `https://<vm-name>.exe.xyz`

Diese Seite setzt das standardmäßige **exeuntu** -Image von exe.dev voraus. Wenn Sie eine andere Distribution gewählt haben, ordnen Sie die Pakete entsprechend zu.

## Schneller Einstieg für Anfänger

  1. <https://exe.new/openclaw>
  2. Geben Sie Ihren Authentifizierungsschlüssel bzw. Ihr Token nach Bedarf ein
  3. Klicken Sie neben Ihrer VM auf „Agent“ und warten Sie, bis Shelley die Bereitstellung abgeschlossen hat
  4. Öffnen Sie `https://<vm-name>.exe.xyz/` und authentifizieren Sie sich mit dem konfigurierten gemeinsamen Secret. Diese Anleitung verwendet standardmäßig Token-Authentifizierung, aber Passwort-Authentifizierung funktioniert ebenfalls, wenn Sie `gateway.auth.mode` umstellen
  5. Genehmigen Sie ausstehende Anfragen zur Gerätekopplung mit `openclaw devices approve <requestId>`


## Was Sie benötigen

  * exe.dev-Konto
  * `ssh exe.dev`-Zugriff auf virtuelle Maschinen von [exe.dev](<https://exe.dev>) (optional)


## Automatisierte Installation mit Shelley

Shelley, der Agent von [exe.dev](<https://exe.dev>), kann OpenClaw mit unserem Prompt sofort installieren. Der verwendete Prompt lautet wie folgt:

CodeCopy code
[code]
    Set up OpenClaw (https://docs.openclaw.ai/install) on this VM. Use the non-interactive and accept-risk flags for openclaw onboarding. Add the supplied auth or token as needed. Configure nginx to forward from the default port 18789 to the root location on the default enabled site config, making sure to enable Websocket support. Pairing is done by "openclaw devices list" and "openclaw devices approve <request id>". Make sure the dashboard shows that OpenClaw's health is OK. exe.dev handles forwarding from port 8000 to port 80/443 and HTTPS for us, so the final "reachable" should be <vm-name>.exe.xyz, without port specification.
[/code]

## Manuelle Installation

## 1) VM erstellen

Von Ihrem Gerät aus:

bashCopy code
[code]
    ssh exe.dev new
[/code]

Dann verbinden:

bashCopy code
[code]
    ssh <vm-name>.exe.xyz
[/code]

## 2) Voraussetzungen installieren (auf der VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl jq ca-certificates openssl
[/code]

## 3) OpenClaw installieren

Führen Sie das OpenClaw-Installationsskript aus:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

## 4) nginx einrichten, um OpenClaw an Port 8000 weiterzuleiten

Bearbeiten Sie `/etc/nginx/sites-enabled/default` mit

CodeCopy code
[code]
    server {    listen 80 default_server;    listen [::]:80 default_server;    listen 8000;    listen [::]:8000;     server_name _;     location / {        proxy_pass http://127.0.0.1:18789;        proxy_http_version 1.1;         # WebSocket support        proxy_set_header Upgrade $http_upgrade;        proxy_set_header Connection "upgrade";         # Standard proxy headers        proxy_set_header Host $host;        proxy_set_header X-Real-IP $remote_addr;        proxy_set_header X-Forwarded-For $remote_addr;        proxy_set_header X-Forwarded-Proto $scheme;         # Timeout settings for long-lived connections        proxy_read_timeout 86400s;        proxy_send_timeout 86400s;    }}
[/code]

Überschreiben Sie Weiterleitungs-Header, statt vom Client bereitgestellte Ketten beizubehalten. OpenClaw vertraut weitergeleiteten IP-Metadaten nur von explizit konfigurierten Proxys, und `X-Forwarded-For`-Ketten im Append-Stil werden als Härtungsrisiko behandelt.

## 5) Auf OpenClaw zugreifen und Berechtigungen gewähren

Greifen Sie auf `https://<vm-name>.exe.xyz/` zu (siehe die Ausgabe der Control UI aus dem Onboarding). Wenn eine Authentifizierung angefordert wird, fügen Sie das konfigurierte gemeinsame Secret von der VM ein. Diese Anleitung verwendet Token-Authentifizierung; rufen Sie daher `gateway.auth.token` mit `openclaw config get gateway.auth.token` ab (oder erzeugen Sie eines mit `openclaw doctor --generate-gateway-token`). Wenn Sie den Gateway auf Passwort-Authentifizierung umgestellt haben, verwenden Sie stattdessen `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD`. Genehmigen Sie Geräte mit `openclaw devices list` und `openclaw devices approve <requestId>`. Verwenden Sie im Zweifel Shelley in Ihrem Browser!

## Remote-Channel-Einrichtung

Für Remote-Hosts sollten Sie einen einzelnen `config patch`-Aufruf vielen SSH-Aufrufen von `config set` vorziehen. Bewahren Sie echte Tokens in der VM-Umgebung oder in `~/.openclaw/.env` auf und legen Sie in `openclaw.json` nur SecretRefs ab.

Sorgen Sie auf der VM dafür, dass die Service-Umgebung die benötigten Secrets enthält:

bashCopy code
[code]
    cat >> ~/.openclaw/.env <<'EOF'SLACK_BOT_TOKEN=xoxb-...SLACK_APP_TOKEN=xapp-...DISCORD_BOT_TOKEN=...OPENAI_API_KEY=sk-...EOF
[/code]

Erstellen Sie auf Ihrem lokalen Rechner eine Patch-Datei und leiten Sie sie an die VM weiter:

json5Copy code
[code]
    // openclaw.remote.patch.json5{  secrets: {    providers: {      default: { source: "env" },    },  },  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --dry-run' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw config patch --stdin' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw gateway restart && openclaw health'
[/code]

Verwenden Sie `--replace-path`, wenn eine verschachtelte Allowlist exakt dem Patch-Wert entsprechen soll, zum Beispiel beim Ersetzen einer Discord-Channel-Allowlist:

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --replace-path "channels.discord.guilds[\"123\"].channels"' < ./discord.patch.json5
[/code]

## Remote-Zugriff

Der Remote-Zugriff wird durch die Authentifizierung von [exe.dev](<https://exe.dev>) verwaltet. Standardmäßig wird HTTP-Datenverkehr von Port 8000 mit E-Mail-Authentifizierung an `https://<vm-name>.exe.xyz` weitergeleitet.

## Aktualisieren

bashCopy code
[code]
    npm i -g openclaw@latestopenclaw doctoropenclaw gateway restartopenclaw health
[/code]

Anleitung: [Aktualisieren](</de/install/updating>)

## Verwandte Themen

  * [Remote-Gateway](</de/gateway/remote>)
  * [Installationsübersicht](</de/install>)


Was this useful?YesNo