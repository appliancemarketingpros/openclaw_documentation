---
title: Konfiguracja zdalnego Gateway
source_url: https://docs.openclaw.ai/pl/gateway/remote-gateway-readme
scraped_at: 2026-05-25
---

> Ta treść została przeniesiona do [Zdalny dostęp](</pl/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>). Aktualny przewodnik znajdziesz na tej stronie.

# Uruchamianie OpenClaw.app ze zdalnym Gateway

OpenClaw.app używa tunelowania SSH do łączenia się ze zdalnym Gateway. Ten przewodnik pokazuje, jak to skonfigurować.

## Omówienie
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

## Szybka konfiguracja

### Krok 1: Dodaj konfigurację SSH

Edytuj `~/.ssh/config` i dodaj:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # e.g., 172.27.187.184    User &lt;REMOTE_USER&gt;            # e.g., jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

Zastąp `&lt;REMOTE_IP&gt;` i `&lt;REMOTE_USER&gt;` swoimi wartościami.

### Krok 2: Skopiuj klucz SSH

Skopiuj swój klucz publiczny na zdalną maszynę (wpisz hasło jeden raz):

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### Krok 3: Skonfiguruj uwierzytelnianie zdalnego Gateway

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

Zamiast tego użyj `gateway.remote.password`, jeśli zdalny Gateway używa uwierzytelniania hasłem. `OPENCLAW_GATEWAY_TOKEN` nadal jest prawidłowe jako nadpisanie na poziomie powłoki, ale trwała konfiguracja zdalnego klienta to `gateway.remote.token` / `gateway.remote.password`.

### Krok 4: Uruchom tunel SSH

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### Krok 5: Uruchom ponownie OpenClaw.app

bashCopy code
[code]
    # Quit OpenClaw.app (⌘Q), then reopen:open /path/to/OpenClaw.app
[/code]

Aplikacja połączy się teraz ze zdalnym Gateway przez tunel SSH.

* * *

## Automatyczne uruchamianie tunelu przy logowaniu

Aby tunel SSH uruchamiał się automatycznie po zalogowaniu, utwórz agenta uruchamiania.

### Utwórz plik PLIST

Zapisz to jako `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### Załaduj agenta uruchamiania

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

Tunel będzie teraz:

  * Uruchamiać się automatycznie po zalogowaniu
  * Uruchamiać się ponownie po awarii
  * Działać w tle


Uwaga dotycząca starszej konfiguracji: usuń wszelki pozostały LaunchAgent `com.openclaw.ssh-tunnel`, jeśli istnieje.

* * *

## Rozwiązywanie problemów

**Sprawdź, czy tunel działa:**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**Uruchom tunel ponownie:**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**Zatrzymaj tunel:**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## Jak to działa

Komponent | Co robi  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Przekierowuje lokalny port 18789 na zdalny port 18789  
`ssh -N` | SSH bez wykonywania zdalnych poleceń (tylko przekierowanie portów)  
`KeepAlive` | Automatycznie uruchamia tunel ponownie, jeśli ulegnie awarii  
`RunAtLoad` | Uruchamia tunel po załadowaniu agenta  
  
OpenClaw.app łączy się z `ws://127.0.0.1:18789` na maszynie klienta. Tunel SSH przekierowuje to połączenie do portu 18789 na zdalnej maszynie, na której działa Gateway.

## Powiązane

  * [Zdalny dostęp](</pl/gateway/remote>)
  * [Tailscale](</pl/gateway/tailscale>)


Was this useful?YesNo