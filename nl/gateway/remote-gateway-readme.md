---
title: Externe Gateway instellen
source_url: https://docs.openclaw.ai/nl/gateway/remote-gateway-readme
scraped_at: 2026-05-25
---

> Deze inhoud is samengevoegd in [Externe toegang](</nl/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>). Zie die pagina voor de huidige handleiding.

# OpenClaw.app uitvoeren met een externe Gateway

OpenClaw.app gebruikt SSH-tunneling om verbinding te maken met een externe Gateway. Deze handleiding laat zien hoe je dit instelt.

## Overzicht
[code] 
    flowchart TB
        subgraph Client["Client Machine"]
            direction TB
            A["OpenClaw.app"]
            B["ws://127.0.0.1:18789\n(local port)"]
            T["SSH Tunnel"]
    
            A --> B
            B --> T
        end
        subgraph Remote["Remote Machine"]
            direction TB
            C["Gateway WebSocket"]
            D["ws://127.0.0.1:18789"]
    
            C --> D
        end
        T --> C
[/code]

## Snelle configuratie

### Stap 1: SSH-configuratie toevoegen

Bewerk `~/.ssh/config` en voeg toe:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # e.g., 172.27.187.184    User &lt;REMOTE_USER&gt;            # e.g., jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

Vervang `&lt;REMOTE_IP&gt;` en `&lt;REMOTE_USER&gt;` door je eigen waarden.

### Stap 2: SSH-sleutel kopiëren

Kopieer je openbare sleutel naar de externe machine (voer het wachtwoord één keer in):

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### Stap 3: Authenticatie voor externe Gateway configureren

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

Gebruik in plaats daarvan `gateway.remote.password` als je externe Gateway wachtwoordauthenticatie gebruikt. `OPENCLAW_GATEWAY_TOKEN` is nog steeds geldig als override op shellniveau, maar de duurzame configuratie voor externe clients is `gateway.remote.token` / `gateway.remote.password`.

### Stap 4: SSH-tunnel starten

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### Stap 5: OpenClaw.app opnieuw starten

bashCopy code
[code]
    # Quit OpenClaw.app (⌘Q), then reopen:open /path/to/OpenClaw.app
[/code]

De app maakt nu via de SSH-tunnel verbinding met de externe Gateway.

* * *

## Tunnel automatisch starten bij inloggen

Maak een Launch Agent aan om de SSH-tunnel automatisch te laten starten wanneer je inlogt.

### Het PLIST-bestand maken

Sla dit op als `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### De Launch Agent laden

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

De tunnel zal nu:

  * Automatisch starten wanneer je inlogt
  * Opnieuw starten als deze crasht
  * Op de achtergrond blijven draaien


Legacy-opmerking: verwijder eventuele overgebleven `com.openclaw.ssh-tunnel` LaunchAgent als die aanwezig is.

* * *

## Problemen oplossen

**Controleren of de tunnel draait:**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**De tunnel opnieuw starten:**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**De tunnel stoppen:**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## Hoe het werkt

Component | Wat het doet  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Stuurt lokale poort 18789 door naar externe poort 18789  
`ssh -N` | SSH zonder externe opdrachten uit te voeren (alleen poortdoorschakeling)  
`KeepAlive` | Start de tunnel automatisch opnieuw als deze crasht  
`RunAtLoad` | Start de tunnel wanneer de agent wordt geladen  
  
OpenClaw.app maakt verbinding met `ws://127.0.0.1:18789` op je clientmachine. De SSH-tunnel stuurt die verbinding door naar poort 18789 op de externe machine waarop de Gateway draait.

## Gerelateerd

  * [Externe toegang](</nl/gateway/remote>)
  * [Tailscale](</nl/gateway/tailscale>)


Was this useful?YesNo