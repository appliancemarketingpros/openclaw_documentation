---
title: Fly.io
source_url: https://docs.openclaw.ai/nl/install/fly
scraped_at: 2026-05-25
---

**Doel:** OpenClaw Gateway draait op een [Fly.io](<https://fly.io>)-machine met persistente opslag, automatische HTTPS en Discord-/kanaaltoegang.

## Wat je nodig hebt

  * [flyctl CLI](<https://fly.io/docs/hands-on/install-flyctl/>) geïnstalleerd
  * Fly.io-account (gratis laag werkt)
  * Modelauthenticatie: API-sleutel voor je gekozen modelprovider
  * Kanaalreferenties: Discord-bottoken, Telegram-token, enz.


## Snelle route voor beginners

  1. Repo klonen → `fly.toml` aanpassen
  2. App + volume maken → secrets instellen
  3. Deployen met `fly deploy`
  4. Via SSH inloggen om configuratie te maken of de Control UI gebruiken


* ### Maak de Fly-app

bashCopy code
[code]
    # Clone the repogit clone https://github.com/openclaw/openclaw.gitcd openclaw # Create a new Fly app (pick your own name)fly apps create my-openclaw # Create a persistent volume (1GB is usually enough)fly volumes create openclaw_data --size 1 --region iad
[/code]

**Tip:** Kies een regio dicht bij jou. Veelgebruikte opties: `lhr` (Londen), `iad` (Virginia), `sjc` (San Jose).

* ### Configureer fly.toml

Bewerk `fly.toml` zodat deze overeenkomt met je appnaam en vereisten.

**Beveiligingsopmerking:** De standaardconfiguratie stelt een openbare URL beschikbaar. Zie Privé-deployment of gebruik `deploy/fly.private.toml` voor een geharde deployment zonder openbaar IP-adres.

tomlCopy code
[code]
    app = "my-openclaw"  # Your app nameprimary_region = "iad" [build]  dockerfile = "Dockerfile" [env]  NODE_ENV = "production"  OPENCLAW_PREFER_PNPM = "1"  OPENCLAW_STATE_DIR = "/data"  NODE_OPTIONS = "--max-old-space-size=1536" [processes]  app = "node dist/index.js gateway --allow-unconfigured --port 3000 --bind lan" [http_service]  internal_port = 3000  force_https = true  auto_stop_machines = false  auto_start_machines = true  min_machines_running = 1  processes = ["app"] [[vm]]  size = "shared-cpu-2x"  memory = "2048mb" [mounts]  source = "openclaw_data"  destination = "/data"
[/code]

De OpenClaw Docker-image gebruikt `tini` als entrypoint. Fly-procescommando's vervangen Docker `CMD` zonder `ENTRYPOINT` te vervangen, dus het proces draait nog steeds onder `tini`.

**Belangrijke instellingen:**

Instelling | Waarom  
---|---  
`--bind lan` | Bindt aan `0.0.0.0` zodat Fly's proxy de Gateway kan bereiken  
`--allow-unconfigured` | Start zonder configuratiebestand (dat maak je daarna)  
`internal_port = 3000` | Moet overeenkomen met `--port 3000` (of `OPENCLAW_GATEWAY_PORT`) voor Fly-healthchecks  
`memory = "2048mb"` | 512 MB is te weinig; 2 GB aanbevolen  
`OPENCLAW_STATE_DIR = "/data"` | Bewaart status persistent op het volume  
* ### Stel secrets in

bashCopy code
[code]
    # Required: Gateway token (for non-loopback binding)fly secrets set OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 32) # Model provider API keysfly secrets set ANTHROPIC_API_KEY=sk-ant-... # Optional: Other providersfly secrets set OPENAI_API_KEY=sk-...fly secrets set GOOGLE_API_KEY=... # Channel tokensfly secrets set DISCORD_BOT_TOKEN=MTQ...
[/code]

**Opmerkingen:**

  * Niet-loopback-binds (`--bind lan`) vereisen een geldig Gateway-authenticatiepad. Dit Fly.io-voorbeeld gebruikt `OPENCLAW_GATEWAY_TOKEN`, maar `gateway.auth.password` of een correct geconfigureerde niet-loopback-`trusted-proxy`-deployment voldoet ook aan de vereiste.
  * Behandel deze tokens als wachtwoorden.
  * **Geef de voorkeur aan omgevingsvariabelen boven een configuratiebestand** voor alle API-sleutels en tokens. Dit houdt secrets uit `openclaw.json`, waar ze per ongeluk kunnen worden blootgesteld of gelogd.


* ### Deploy

bashCopy code
[code]
    fly deploy
[/code]

De eerste deployment bouwt de Docker-image (~2-3 minuten). Volgende deployments zijn sneller.

Verifieer na deployment:

bashCopy code
[code]
    fly statusfly logs
[/code]

Je zou dit moeten zien:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:3000 (PID xxx)[discord] logged in to discord as xxx
[/code]

* ### Maak het configuratiebestand

Log via SSH in op de machine om een juiste configuratie te maken:

bashCopy code
[code]
    fly ssh console
[/code]

Maak de configuratiemap en het bestand:

bashCopy code
[code]
    mkdir -p /datacat > /data/openclaw.json << 'EOF'{  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-opus-4-6",        "fallbacks": ["anthropic/claude-sonnet-4-6", "openai/gpt-5.4"]      },      "maxConcurrent": 4    },    "list": [      {        "id": "main",        "default": true      }    ]  },  "auth": {    "profiles": {      "anthropic:default": { "mode": "token", "provider": "anthropic" },      "openai:default": { "mode": "token", "provider": "openai" }    }  },  "bindings": [    {      "agentId": "main",      "match": { "channel": "discord" }    }  ],  "channels": {    "discord": {      "enabled": true,      "groupPolicy": "allowlist",      "guilds": {        "YOUR_GUILD_ID": {          "channels": { "general": { "allow": true } },          "requireMention": false        }      }    }  },  "gateway": {    "mode": "local",    "bind": "auto",    "controlUi": {      "allowedOrigins": [        "https://my-openclaw.fly.dev",        "http://localhost:3000",        "http://127.0.0.1:3000"      ]    }  },  "meta": {}}EOF
[/code]

**Opmerking:** Met `OPENCLAW_STATE_DIR=/data` is het configuratiepad `/data/openclaw.json`.

**Opmerking:** Vervang `https://my-openclaw.fly.dev` door de echte origin van je Fly-app. Bij het starten seedt de Gateway lokale Control UI-origins op basis van de runtimewaarden `--bind` en `--port`, zodat de eerste start kan doorgaan voordat configuratie bestaat, maar browsertoegang via Fly vereist nog steeds dat de exacte HTTPS-origin in `gateway.controlUi.allowedOrigins` staat.

**Opmerking:** Het Discord-token kan uit een van beide bronnen komen:

  * Omgevingsvariabele: `DISCORD_BOT_TOKEN` (aanbevolen voor secrets)
  * Configuratiebestand: `channels.discord.token`


Als je de omgevingsvariabele gebruikt, hoef je geen token aan de configuratie toe te voegen. De Gateway leest `DISCORD_BOT_TOKEN` automatisch.

Herstart om toe te passen:

bashCopy code
[code]
    exitfly machine restart <machine-id>
[/code]

* ### Open de Gateway

### Control UI

Open in browser:

bashCopy code
[code]
    fly open
[/code]

Of ga naar `https://my-openclaw.fly.dev/`

Authenticeer met het geconfigureerde gedeelde geheim. Deze gids gebruikt het Gateway-token uit `OPENCLAW_GATEWAY_TOKEN`; als je bent overgestapt op wachtwoordauthenticatie, gebruik dan dat wachtwoord.

### Logs

bashCopy code
[code]
    fly logs              # Live logsfly logs --no-tail    # Recent logs
[/code]

### SSH-console

bashCopy code
[code]
    fly ssh console
[/code]

## Probleemoplossing

### "App is not listening on expected address"

De Gateway bindt aan `127.0.0.1` in plaats van aan `0.0.0.0`.

**Oplossing:** Voeg `--bind lan` toe aan je procescommando in `fly.toml`.

### Healthchecks mislukken / verbinding geweigerd

Fly kan de Gateway niet bereiken op de geconfigureerde poort.

**Oplossing:** Zorg dat `internal_port` overeenkomt met de Gateway-poort (stel `--port 3000` of `OPENCLAW_GATEWAY_PORT=3000` in).

### OOM / geheugenproblemen

Container blijft herstarten of wordt beëindigd. Signalen: `SIGABRT`, `v8::internal::Runtime_AllocateInYoungGeneration` of stille herstarts.

**Oplossing:** Verhoog het geheugen in `fly.toml`:

tomlCopy code
[code]
    [[vm]]  memory = "2048mb"
[/code]

Of werk een bestaande machine bij:

bashCopy code
[code]
    fly machine update <machine-id> --vm-memory 2048 -y
[/code]

**Opmerking:** 512 MB is te weinig. 1 GB kan werken, maar kan onder belasting of bij uitgebreide logging OOM veroorzaken. **2 GB wordt aanbevolen.**

### Problemen met Gateway-lock

Gateway weigert te starten met fouten over "already running".

Dit gebeurt wanneer de container herstart, maar het PID-lockbestand op het volume blijft bestaan.

**Oplossing:** Verwijder het lockbestand:

bashCopy code
[code]
    fly ssh console --command "rm -f /data/gateway.*.lock"fly machine restart <machine-id>
[/code]

Het lockbestand staat op `/data/gateway.*.lock` (niet in een submap).

### Configuratie wordt niet gelezen

`--allow-unconfigured` omzeilt alleen de opstartbeveiliging. Het maakt of repareert `/data/openclaw.json` niet, dus zorg dat je echte configuratie bestaat en `gateway.mode="local"` bevat wanneer je een normale lokale Gateway-start wilt.

Controleer of de configuratie bestaat:

bashCopy code
[code]
    fly ssh console --command "cat /data/openclaw.json"
[/code]

### Configuratie schrijven via SSH

Het commando `fly ssh console -C` ondersteunt geen shell-omleiding. Een configuratiebestand schrijven:

bashCopy code
[code]
    # Use echo + tee (pipe from local to remote)echo '{"your":"config"}' | fly ssh console -C "tee /data/openclaw.json" # Or use sftpfly sftp shell> put /local/path/config.json /data/openclaw.json
[/code]

**Opmerking:** `fly sftp` kan mislukken als het bestand al bestaat. Verwijder het eerst:

bashCopy code
[code]
    fly ssh console --command "rm /data/openclaw.json"
[/code]

### Status blijft niet behouden

Als je authenticatieprofielen, kanaal-/providerstatus of sessies kwijtraakt na een herstart, schrijft de statusmap naar het containerbestandssysteem.

**Oplossing:** Zorg dat `OPENCLAW_STATE_DIR=/data` is ingesteld in `fly.toml` en deploy opnieuw.

## Updates

bashCopy code
[code]
    # Pull latest changesgit pull # Redeployfly deploy # Check healthfly statusfly logs
[/code]

### Machinecommando bijwerken

Als je het opstartcommando moet wijzigen zonder volledige redeployment:

bashCopy code
[code]
    # Get machine IDfly machines list # Update commandfly machine update <machine-id> --command "node dist/index.js gateway --port 3000 --bind lan" -y # Or with memory increasefly machine update <machine-id> --vm-memory 2048 --command "node dist/index.js gateway --port 3000 --bind lan" -y
[/code]

**Opmerking:** Na `fly deploy` kan het machinecommando worden teruggezet naar wat in `fly.toml` staat. Als je handmatige wijzigingen hebt aangebracht, pas ze dan na deployment opnieuw toe.

## Privé-deployment (gehard)

Standaard wijst Fly openbare IP-adressen toe, waardoor je Gateway bereikbaar is op `https://your-app.fly.dev`. Dit is handig, maar betekent dat je deployment vindbaar is door internetscanners (Shodan, Censys, enz.).

Gebruik de privésilabloon voor een geharde deployment met **geen openbare blootstelling**.

### Wanneer je privé-deployment gebruikt

  * Je doet alleen **uitgaande** oproepen/berichten (geen inkomende webhooks)
  * Je gebruikt **ngrok- of Tailscale** -tunnels voor webhook-callbacks
  * Je benadert de Gateway via **SSH, proxy of WireGuard** in plaats van via de browser
  * Je wilt dat de deployment **verborgen blijft voor internetscanners**


### Installatie

Gebruik `deploy/fly.private.toml` in plaats van de standaardconfiguratie:

bashCopy code
[code]
    # Deploy with private configfly deploy -c deploy/fly.private.toml
[/code]

Of converteer een bestaande deployment:

bashCopy code
[code]
    # List current IPsfly ips list -a my-openclaw # Release public IPsfly ips release <public-ipv4> -a my-openclawfly ips release <public-ipv6> -a my-openclaw # Switch to private config so future deploys don't re-allocate public IPs# (remove [http_service] or deploy with the private template)fly deploy -c deploy/fly.private.toml # Allocate private-only IPv6fly ips allocate-v6 --private -a my-openclaw
[/code]

Daarna zou `fly ips list` alleen een IP van type `private` moeten tonen:

CodeCopy code
[code]
    VERSION  IP                   TYPE             REGIONv6       fdaa:x:x:x:x::x      private          global
[/code]

### Toegang tot een privé-deployment

Omdat er geen openbare URL is, gebruik je een van deze methoden:

**Optie 1: Lokale proxy (eenvoudigst)**

bashCopy code
[code]
    # Forward local port 3000 to the appfly proxy 3000:3000 -a my-openclaw # Then open http://localhost:3000 in browser
[/code]

**Optie 2: WireGuard-VPN**

bashCopy code
[code]
    # Create WireGuard config (one-time)fly wireguard create # Import to WireGuard client, then access via internal IPv6# Example: http://[fdaa:x:x:x:x::x]:3000
[/code]

**Optie 3: alleen SSH**

bashCopy code
[code]
    fly ssh console -a my-openclaw
[/code]

### Webhooks met privé-implementatie

Als je Webhook-callbacks nodig hebt (Twilio, Telnyx, enz.) zonder openbare blootstelling:

  1. **ngrok-tunnel** \- Voer ngrok uit in de container of als sidecar
  2. **Tailscale Funnel** \- Stel specifieke paden beschikbaar via Tailscale
  3. **Alleen outbound** \- Sommige providers (Twilio) werken prima voor outbound-oproepen zonder Webhooks


Voorbeeldconfiguratie voor spraakoproepen met ngrok:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio",          tunnel: { provider: "ngrok" },          webhookSecurity: {            allowedHosts: ["example.ngrok.app"],          },        },      },    },  },}
[/code]

De ngrok-tunnel draait in de container en biedt een openbare Webhook-URL zonder de Fly-app zelf bloot te stellen. Stel `webhookSecurity.allowedHosts` in op de openbare tunnelhostnaam zodat doorgestuurde hostheaders worden geaccepteerd.

### Beveiligingsvoordelen

Aspect | Openbaar | Privé  
---|---|---  
Internetscanners | Vindbaar | Verborgen  
Directe aanvallen | Mogelijk | Geblokkeerd  
Toegang tot beheer-UI | Browser | Proxy/VPN  
Webhook-bezorging | Direct | Via tunnel  
  
## Opmerkingen

  * [Fly.io](<http://Fly.io>) gebruikt **x86-architectuur** (niet ARM)
  * De Dockerfile is compatibel met beide architecturen
  * Gebruik `fly ssh console` voor onboarding van WhatsApp/Telegram
  * Persistente gegevens staan op het volume bij `/data`
  * Signal vereist Java + signal-cli; gebruik een aangepaste image en houd het geheugen op 2 GB+.


## Kosten

Met de aanbevolen configuratie (`shared-cpu-2x`, 2 GB RAM):

  * ~$10-15/maand, afhankelijk van gebruik
  * De gratis laag bevat enige ruimte


Zie [Fly.io-prijzen](<https://fly.io/docs/about/pricing/>) voor details.

## Volgende stappen

  * Stel berichtkanalen in: [Kanalen](</nl/channels>)
  * Configureer de Gateway: [Gateway-configuratie](</nl/gateway/configuration>)
  * Houd OpenClaw up-to-date: [Bijwerken](</nl/install/updating>)


## Gerelateerd

  * [Installatie-overzicht](</nl/install>)
  * [Hetzner](</nl/install/hetzner>)
  * [Docker](</nl/install/docker>)
  * [VPS-hosting](</nl/vps>)


Was this useful?YesNo