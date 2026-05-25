---
title: Remote-Gateway einrichten
source_url: https://docs.openclaw.ai/de/gateway/remote-gateway-readme
scraped_at: 2026-05-25
---

> Dieser Inhalt wurde in [Remotezugriff](</de/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>) zusammengeführt. Die aktuelle Anleitung finden Sie auf dieser Seite.

# OpenClaw.app mit einem Remote-Gateway ausführen

OpenClaw.app verwendet SSH-Tunneling, um eine Verbindung zu einem Remote-Gateway herzustellen. Diese Anleitung zeigt Ihnen, wie Sie dies einrichten.

## Übersicht
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

## Schnelle Einrichtung

### Schritt 1: SSH-Konfiguration hinzufügen

Bearbeiten Sie `~/.ssh/config` und fügen Sie Folgendes hinzu:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # e.g., 172.27.187.184    User &lt;REMOTE_USER&gt;            # e.g., jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

Ersetzen Sie `&lt;REMOTE_IP&gt;` und `&lt;REMOTE_USER&gt;` durch Ihre Werte.

### Schritt 2: SSH-Schlüssel kopieren

Kopieren Sie Ihren öffentlichen Schlüssel auf den Remote-Rechner (Passwort einmal eingeben):

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### Schritt 3: Authentifizierung für den Remote-Gateway konfigurieren

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

Verwenden Sie stattdessen `gateway.remote.password`, wenn Ihr Remote-Gateway Passwortauthentifizierung nutzt. `OPENCLAW_GATEWAY_TOKEN` ist weiterhin als Override auf Shell-Ebene gültig, aber die dauerhafte Einrichtung für Remote-Clients ist `gateway.remote.token` / `gateway.remote.password`.

### Schritt 4: SSH-Tunnel starten

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### Schritt 5: OpenClaw.app neu starten

bashCopy code
[code]
    # Quit OpenClaw.app (⌘Q), then reopen:open /path/to/OpenClaw.app
[/code]

Die App verbindet sich nun über den SSH-Tunnel mit dem Remote-Gateway.

* * *

## Tunnel beim Anmelden automatisch starten

Damit der SSH-Tunnel automatisch startet, wenn Sie sich anmelden, erstellen Sie einen Launch Agent.

### PLIST-Datei erstellen

Speichern Sie dies als `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### Launch Agent laden

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

Der Tunnel wird nun:

  * Automatisch gestartet, wenn Sie sich anmelden
  * Neu gestartet, wenn er abstürzt
  * Im Hintergrund weiter ausgeführt


Hinweis zu älteren Versionen: Entfernen Sie alle verbliebenen `com.openclaw.ssh-tunnel`-LaunchAgents, falls vorhanden.

* * *

## Fehlerbehebung

**Prüfen, ob der Tunnel ausgeführt wird:**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**Tunnel neu starten:**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**Tunnel stoppen:**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## Funktionsweise

Komponente | Funktion  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Leitet den lokalen Port 18789 an den Remote-Port 18789 weiter  
`ssh -N` | SSH ohne Ausführen von Remote-Befehlen (nur Portweiterleitung)  
`KeepAlive` | Startet den Tunnel automatisch neu, wenn er abstürzt  
`RunAtLoad` | Startet den Tunnel, wenn der Agent geladen wird  
  
OpenClaw.app verbindet sich auf Ihrem Client-Rechner mit `ws://127.0.0.1:18789`. Der SSH-Tunnel leitet diese Verbindung an Port 18789 auf dem Remote-Rechner weiter, auf dem der Gateway ausgeführt wird.

## Verwandte Themen

  * [Remotezugriff](</de/gateway/remote>)
  * [Tailscale](</de/gateway/tailscale>)


Was this useful?YesNo