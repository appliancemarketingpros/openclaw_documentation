---
title: Configurazione del Gateway remoto
source_url: https://docs.openclaw.ai/it/gateway/remote-gateway-readme
scraped_at: 2026-05-25
---

> Questo contenuto è stato unito in [Accesso remoto](</it/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>). Consulta quella pagina per la guida attuale.

# Eseguire OpenClaw.app con un Gateway remoto

OpenClaw.app usa il tunneling SSH per connettersi a un gateway remoto. Questa guida mostra come configurarlo.

## Panoramica
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

## Configurazione rapida

### Passaggio 1: aggiungere la configurazione SSH

Modifica `~/.ssh/config` e aggiungi:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # e.g., 172.27.187.184    User &lt;REMOTE_USER&gt;            # e.g., jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

Sostituisci `&lt;REMOTE_IP&gt;` e `&lt;REMOTE_USER&gt;` con i tuoi valori.

### Passaggio 2: copiare la chiave SSH

Copia la tua chiave pubblica sulla macchina remota (inserisci la password una volta):

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### Passaggio 3: configurare l'autenticazione del Gateway remoto

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

Usa invece `gateway.remote.password` se il tuo Gateway remoto usa l'autenticazione con password. `OPENCLAW_GATEWAY_TOKEN` resta valido come override a livello di shell, ma la configurazione duratura del client remoto è `gateway.remote.token` / `gateway.remote.password`.

### Passaggio 4: avviare il tunnel SSH

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### Passaggio 5: riavviare OpenClaw.app

bashCopy code
[code]
    # Quit OpenClaw.app (⌘Q), then reopen:open /path/to/OpenClaw.app
[/code]

L'app ora si connetterà al Gateway remoto tramite il tunnel SSH.

* * *

## Avvio automatico del tunnel all'accesso

Per avviare automaticamente il tunnel SSH quando accedi, crea un Launch Agent.

### Creare il file PLIST

Salvalo come `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### Caricare il Launch Agent

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

Il tunnel ora:

  * Si avvierà automaticamente quando accedi
  * Si riavvierà in caso di arresto anomalo
  * Continuerà a essere eseguito in background


Nota legacy: rimuovi eventuali LaunchAgent `com.openclaw.ssh-tunnel` residui, se presenti.

* * *

## Risoluzione dei problemi

**Verificare se il tunnel è in esecuzione:**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**Riavviare il tunnel:**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**Arrestare il tunnel:**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## Come funziona

Componente | Cosa fa  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Inoltra la porta locale 18789 alla porta remota 18789  
`ssh -N` | SSH senza eseguire comandi remoti (solo inoltro di porte)  
`KeepAlive` | Riavvia automaticamente il tunnel in caso di arresto anomalo  
`RunAtLoad` | Avvia il tunnel quando l'agent viene caricato  
  
OpenClaw.app si connette a `ws://127.0.0.1:18789` sulla tua macchina client. Il tunnel SSH inoltra quella connessione alla porta 18789 sulla macchina remota in cui è in esecuzione il Gateway.

## Correlati

  * [Accesso remoto](</it/gateway/remote>)
  * [Tailscale](</it/gateway/tailscale>)


Was this useful?YesNo