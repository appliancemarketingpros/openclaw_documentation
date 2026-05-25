---
title: Fly.io
source_url: https://docs.openclaw.ai/de/install/fly
scraped_at: 2026-05-25
---

**Ziel:** OpenClaw Gateway auf einer [Fly.io](<https://fly.io>)-Maschine mit persistentem Speicher, automatischem HTTPS und Discord-/Channel-Zugriff betreiben.

## Was Sie benötigen

  * Installierte [flyctl CLI](<https://fly.io/docs/hands-on/install-flyctl/>)
  * Fly.io-Konto (kostenlose Stufe funktioniert)
  * Modellauthentifizierung: API-Schlüssel für Ihren gewählten Modell-Provider
  * Channel-Zugangsdaten: Discord-Bot-Token, Telegram-Token usw.


## Schneller Einstieg für Anfänger

  1. Repository klonen → `fly.toml` anpassen
  2. App + Volume erstellen → Secrets setzen
  3. Mit `fly deploy` bereitstellen
  4. Per SSH verbinden, um die Konfiguration zu erstellen, oder die Steuerungs-UI verwenden


* ### Fly-App erstellen

bashCopy code
[code]
    # Clone the repogit clone https://github.com/openclaw/openclaw.gitcd openclaw # Create a new Fly app (pick your own name)fly apps create my-openclaw # Create a persistent volume (1GB is usually enough)fly volumes create openclaw_data --size 1 --region iad
[/code]

**Tipp:** Wählen Sie eine Region in Ihrer Nähe. Häufige Optionen: `lhr` (London), `iad` (Virginia), `sjc` (San Jose).

* ### fly.toml konfigurieren

Bearbeiten Sie `fly.toml`, damit sie zu Ihrem App-Namen und Ihren Anforderungen passt.

**Sicherheitshinweis:** Die Standardkonfiguration stellt eine öffentliche URL bereit. Für eine gehärtete Bereitstellung ohne öffentliche IP siehe Private Bereitstellung oder verwenden Sie `deploy/fly.private.toml`.

tomlCopy code
[code]
    app = "my-openclaw"  # Your app nameprimary_region = "iad" [build]  dockerfile = "Dockerfile" [env]  NODE_ENV = "production"  OPENCLAW_PREFER_PNPM = "1"  OPENCLAW_STATE_DIR = "/data"  NODE_OPTIONS = "--max-old-space-size=1536" [processes]  app = "node dist/index.js gateway --allow-unconfigured --port 3000 --bind lan" [http_service]  internal_port = 3000  force_https = true  auto_stop_machines = false  auto_start_machines = true  min_machines_running = 1  processes = ["app"] [[vm]]  size = "shared-cpu-2x"  memory = "2048mb" [mounts]  source = "openclaw_data"  destination = "/data"
[/code]

Das OpenClaw-Docker-Image verwendet `tini` als Einstiegspunkt. Fly-Prozessbefehle ersetzen Docker `CMD`, ohne `ENTRYPOINT` zu ersetzen; der Prozess läuft daher weiterhin unter `tini`.

**Wichtige Einstellungen:**

Einstellung | Warum  
---|---  
`--bind lan` | Bindet an `0.0.0.0`, damit der Proxy von Fly das Gateway erreichen kann  
`--allow-unconfigured` | Startet ohne Konfigurationsdatei (Sie erstellen sie anschließend)  
`internal_port = 3000` | Muss für Fly-Health-Checks zu `--port 3000` (oder `OPENCLAW_GATEWAY_PORT`) passen  
`memory = "2048mb"` | 512 MB sind zu wenig; 2 GB empfohlen  
`OPENCLAW_STATE_DIR = "/data"` | Persistiert den Zustand auf dem Volume  
* ### Secrets setzen

bashCopy code
[code]
    # Required: Gateway token (for non-loopback binding)fly secrets set OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 32) # Model provider API keysfly secrets set ANTHROPIC_API_KEY=sk-ant-... # Optional: Other providersfly secrets set OPENAI_API_KEY=sk-...fly secrets set GOOGLE_API_KEY=... # Channel tokensfly secrets set DISCORD_BOT_TOKEN=MTQ...
[/code]

**Hinweise:**

  * Nicht-loopback-Bindings (`--bind lan`) erfordern einen gültigen Gateway-Authentifizierungspfad. Dieses Fly.io-Beispiel verwendet `OPENCLAW_GATEWAY_TOKEN`, aber `gateway.auth.password` oder eine korrekt konfigurierte nicht-loopback-`trusted-proxy`-Bereitstellung erfüllen die Anforderung ebenfalls.
  * Behandeln Sie diese Tokens wie Passwörter.
  * **Verwenden Sie für alle API-Schlüssel und Tokens bevorzugt Umgebungsvariablen statt einer Konfigurationsdatei.** So bleiben Secrets aus `openclaw.json` heraus, wo sie versehentlich offengelegt oder protokolliert werden könnten.


* ### Bereitstellen

bashCopy code
[code]
    fly deploy
[/code]

Die erste Bereitstellung baut das Docker-Image (~2-3 Minuten). Nachfolgende Bereitstellungen sind schneller.

Nach der Bereitstellung prüfen Sie:

bashCopy code
[code]
    fly statusfly logs
[/code]

Sie sollten Folgendes sehen:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:3000 (PID xxx)[discord] logged in to discord as xxx
[/code]

* ### Konfigurationsdatei erstellen

Verbinden Sie sich per SSH mit der Maschine, um eine passende Konfiguration zu erstellen:

bashCopy code
[code]
    fly ssh console
[/code]

Erstellen Sie das Konfigurationsverzeichnis und die Datei:

bashCopy code
[code]
    mkdir -p /datacat > /data/openclaw.json << 'EOF'{  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-opus-4-6",        "fallbacks": ["anthropic/claude-sonnet-4-6", "openai/gpt-5.4"]      },      "maxConcurrent": 4    },    "list": [      {        "id": "main",        "default": true      }    ]  },  "auth": {    "profiles": {      "anthropic:default": { "mode": "token", "provider": "anthropic" },      "openai:default": { "mode": "token", "provider": "openai" }    }  },  "bindings": [    {      "agentId": "main",      "match": { "channel": "discord" }    }  ],  "channels": {    "discord": {      "enabled": true,      "groupPolicy": "allowlist",      "guilds": {        "YOUR_GUILD_ID": {          "channels": { "general": { "allow": true } },          "requireMention": false        }      }    }  },  "gateway": {    "mode": "local",    "bind": "auto",    "controlUi": {      "allowedOrigins": [        "https://my-openclaw.fly.dev",        "http://localhost:3000",        "http://127.0.0.1:3000"      ]    }  },  "meta": {}}EOF
[/code]

**Hinweis:** Mit `OPENCLAW_STATE_DIR=/data` ist der Konfigurationspfad `/data/openclaw.json`.

**Hinweis:** Ersetzen Sie `https://my-openclaw.fly.dev` durch den tatsächlichen Origin Ihrer Fly-App. Der Gateway-Start initialisiert lokale Origins für die Steuerungs-UI aus den Laufzeitwerten `--bind` und `--port`, damit der erste Start erfolgen kann, bevor eine Konfiguration existiert. Für den Browserzugriff über Fly muss der genaue HTTPS-Origin jedoch weiterhin in `gateway.controlUi.allowedOrigins` aufgeführt sein.

**Hinweis:** Das Discord-Token kann aus einer der folgenden Quellen stammen:

  * Umgebungsvariable: `DISCORD_BOT_TOKEN` (für Secrets empfohlen)
  * Konfigurationsdatei: `channels.discord.token`


Wenn Sie die Umgebungsvariable verwenden, müssen Sie das Token nicht zur Konfiguration hinzufügen. Das Gateway liest `DISCORD_BOT_TOKEN` automatisch.

Zum Anwenden neu starten:

bashCopy code
[code]
    exitfly machine restart <machine-id>
[/code]

* ### Auf das Gateway zugreifen

### Steuerungs-UI

Im Browser öffnen:

bashCopy code
[code]
    fly open
[/code]

Oder besuchen Sie `https://my-openclaw.fly.dev/`

Authentifizieren Sie sich mit dem konfigurierten gemeinsamen Secret. Diese Anleitung verwendet das Gateway-Token aus `OPENCLAW_GATEWAY_TOKEN`; wenn Sie auf Passwortauthentifizierung umgestellt haben, verwenden Sie stattdessen dieses Passwort.

### Logs

bashCopy code
[code]
    fly logs              # Live logsfly logs --no-tail    # Recent logs
[/code]

### SSH-Konsole

bashCopy code
[code]
    fly ssh console
[/code]

## Fehlerbehebung

### „App is not listening on expected address“

Das Gateway bindet an `127.0.0.1` statt an `0.0.0.0`.

**Behebung:** Fügen Sie Ihrem Prozessbefehl in `fly.toml` `--bind lan` hinzu.

### Health-Checks schlagen fehl / Verbindung abgelehnt

Fly kann das Gateway auf dem konfigurierten Port nicht erreichen.

**Behebung:** Stellen Sie sicher, dass `internal_port` zum Gateway-Port passt (setzen Sie `--port 3000` oder `OPENCLAW_GATEWAY_PORT=3000`).

### OOM / Speicherprobleme

Der Container startet immer wieder neu oder wird beendet. Anzeichen: `SIGABRT`, `v8::internal::Runtime_AllocateInYoungGeneration` oder stille Neustarts.

**Behebung:** Erhöhen Sie den Speicher in `fly.toml`:

tomlCopy code
[code]
    [[vm]]  memory = "2048mb"
[/code]

Oder aktualisieren Sie eine bestehende Maschine:

bashCopy code
[code]
    fly machine update <machine-id> --vm-memory 2048 -y
[/code]

**Hinweis:** 512 MB sind zu wenig. 1 GB kann funktionieren, kann aber unter Last oder bei ausführlicher Protokollierung zu OOM führen. **2 GB werden empfohlen.**

### Gateway-Lock-Probleme

Das Gateway verweigert den Start mit „already running“-Fehlern.

Das passiert, wenn der Container neu startet, die PID-Lock-Datei aber auf dem Volume bestehen bleibt.

**Behebung:** Löschen Sie die Lock-Datei:

bashCopy code
[code]
    fly ssh console --command "rm -f /data/gateway.*.lock"fly machine restart <machine-id>
[/code]

Die Lock-Datei befindet sich unter `/data/gateway.*.lock` (nicht in einem Unterverzeichnis).

### Konfiguration wird nicht gelesen

`--allow-unconfigured` umgeht nur die Startprüfung. Es erstellt oder repariert `/data/openclaw.json` nicht. Stellen Sie daher sicher, dass Ihre echte Konfiguration existiert und `gateway.mode="local"` enthält, wenn Sie einen normalen lokalen Gateway-Start wünschen.

Prüfen Sie, ob die Konfiguration existiert:

bashCopy code
[code]
    fly ssh console --command "cat /data/openclaw.json"
[/code]

### Konfiguration über SSH schreiben

Der Befehl `fly ssh console -C` unterstützt keine Shell-Umleitung. Um eine Konfigurationsdatei zu schreiben:

bashCopy code
[code]
    # Use echo + tee (pipe from local to remote)echo '{"your":"config"}' | fly ssh console -C "tee /data/openclaw.json" # Or use sftpfly sftp shell> put /local/path/config.json /data/openclaw.json
[/code]

**Hinweis:** `fly sftp` kann fehlschlagen, wenn die Datei bereits existiert. Löschen Sie sie zuerst:

bashCopy code
[code]
    fly ssh console --command "rm /data/openclaw.json"
[/code]

### Zustand wird nicht persistiert

Wenn Sie nach einem Neustart Authentifizierungsprofile, Channel-/Provider-Zustand oder Sitzungen verlieren, schreibt das Zustandsverzeichnis in das Container-Dateisystem.

**Behebung:** Stellen Sie sicher, dass `OPENCLAW_STATE_DIR=/data` in `fly.toml` gesetzt ist, und stellen Sie erneut bereit.

## Aktualisierungen

bashCopy code
[code]
    # Pull latest changesgit pull # Redeployfly deploy # Check healthfly statusfly logs
[/code]

### Maschinenbefehl aktualisieren

Wenn Sie den Startbefehl ohne vollständige erneute Bereitstellung ändern müssen:

bashCopy code
[code]
    # Get machine IDfly machines list # Update commandfly machine update <machine-id> --command "node dist/index.js gateway --port 3000 --bind lan" -y # Or with memory increasefly machine update <machine-id> --vm-memory 2048 --command "node dist/index.js gateway --port 3000 --bind lan" -y
[/code]

**Hinweis:** Nach `fly deploy` kann der Maschinenbefehl auf den Inhalt von `fly.toml` zurückgesetzt werden. Wenn Sie manuelle Änderungen vorgenommen haben, wenden Sie sie nach der Bereitstellung erneut an.

## Private Bereitstellung (gehärtet)

Standardmäßig weist Fly öffentliche IPs zu, wodurch Ihr Gateway unter `https://your-app.fly.dev` erreichbar ist. Das ist praktisch, bedeutet aber, dass Ihre Bereitstellung von Internet-Scannern (Shodan, Censys usw.) gefunden werden kann.

Für eine gehärtete Bereitstellung mit **keiner öffentlichen Exposition** verwenden Sie die private Vorlage.

### Wann Sie eine private Bereitstellung verwenden sollten

  * Sie führen nur **ausgehende** Aufrufe/Nachrichten aus (keine eingehenden Webhooks)
  * Sie verwenden **ngrok- oder Tailscale** -Tunnel für Webhook-Callbacks
  * Sie greifen statt über den Browser per **SSH, Proxy oder WireGuard** auf das Gateway zu
  * Sie möchten, dass die Bereitstellung **vor Internet-Scannern verborgen** ist


### Einrichtung

Verwenden Sie `deploy/fly.private.toml` statt der Standardkonfiguration:

bashCopy code
[code]
    # Deploy with private configfly deploy -c deploy/fly.private.toml
[/code]

Oder konvertieren Sie eine bestehende Bereitstellung:

bashCopy code
[code]
    # List current IPsfly ips list -a my-openclaw # Release public IPsfly ips release <public-ipv4> -a my-openclawfly ips release <public-ipv6> -a my-openclaw # Switch to private config so future deploys don't re-allocate public IPs# (remove [http_service] or deploy with the private template)fly deploy -c deploy/fly.private.toml # Allocate private-only IPv6fly ips allocate-v6 --private -a my-openclaw
[/code]

Danach sollte `fly ips list` nur noch eine IP vom Typ `private` anzeigen:

CodeCopy code
[code]
    VERSION  IP                   TYPE             REGIONv6       fdaa:x:x:x:x::x      private          global
[/code]

### Zugriff auf eine private Bereitstellung

Da es keine öffentliche URL gibt, verwenden Sie eine dieser Methoden:

**Option 1: Lokaler Proxy (am einfachsten)**

bashCopy code
[code]
    # Forward local port 3000 to the appfly proxy 3000:3000 -a my-openclaw # Then open http://localhost:3000 in browser
[/code]

**Option 2: WireGuard-VPN**

bashCopy code
[code]
    # Create WireGuard config (one-time)fly wireguard create # Import to WireGuard client, then access via internal IPv6# Example: http://[fdaa:x:x:x:x::x]:3000
[/code]

**Option 3: Nur SSH**

bashCopy code
[code]
    fly ssh console -a my-openclaw
[/code]

### Webhooks bei privatem Deployment

Wenn Sie Webhook-Callbacks (Twilio, Telnyx usw.) ohne öffentliche Exponierung benötigen:

  1. **ngrok-Tunnel** \- Führen Sie ngrok im Container oder als Sidecar aus
  2. **Tailscale Funnel** \- Machen Sie bestimmte Pfade über Tailscale zugänglich
  3. **Nur ausgehend** \- Einige Provider (Twilio) funktionieren für ausgehende Anrufe auch ohne Webhooks problemlos


Beispielkonfiguration für Sprachanrufe mit ngrok:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio",          tunnel: { provider: "ngrok" },          webhookSecurity: {            allowedHosts: ["example.ngrok.app"],          },        },      },    },  },}
[/code]

Der ngrok-Tunnel läuft im Container und stellt eine öffentliche Webhook-URL bereit, ohne die Fly-App selbst offenzulegen. Setzen Sie `webhookSecurity.allowedHosts` auf den öffentlichen Tunnel-Hostnamen, damit weitergeleitete Host-Header akzeptiert werden.

### Sicherheitsvorteile

Aspekt | Öffentlich | Privat  
---|---|---  
Internet-Scanner | Auffindbar | Versteckt  
Direkte Angriffe | Möglich | Blockiert  
Zugriff auf Steuerungs-UI | Browser | Proxy/VPN  
Webhook-Zustellung | Direkt | Über Tunnel  
  
## Hinweise

  * [Fly.io](<http://Fly.io>) verwendet **x86-Architektur** (nicht ARM)
  * Das Dockerfile ist mit beiden Architekturen kompatibel
  * Verwenden Sie für das WhatsApp/Telegram-Onboarding `fly ssh console`
  * Persistente Daten liegen auf dem Volume unter `/data`
  * Signal erfordert Java + signal-cli; verwenden Sie ein eigenes Image und halten Sie den Arbeitsspeicher bei 2 GB+.


## Kosten

Mit der empfohlenen Konfiguration (`shared-cpu-2x`, 2 GB RAM):

  * ca. 10-15 USD/Monat, abhängig von der Nutzung
  * Der kostenlose Tarif enthält ein gewisses Kontingent


Weitere Informationen finden Sie unter [Fly.io-Preise](<https://fly.io/docs/about/pricing/>).

## Nächste Schritte

  * Richten Sie Messaging-Kanäle ein: [Kanäle](</de/channels>)
  * Konfigurieren Sie den Gateway: [Gateway-Konfiguration](</de/gateway/configuration>)
  * Halten Sie OpenClaw aktuell: [Aktualisierung](</de/install/updating>)


## Verwandt

  * [Installationsübersicht](</de/install>)
  * [Hetzner](</de/install/hetzner>)
  * [Docker](</de/install/docker>)
  * [VPS-Hosting](</de/vps>)


Was this useful?YesNo