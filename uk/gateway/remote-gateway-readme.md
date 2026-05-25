---
title: Налаштування віддаленого Gateway
source_url: https://docs.openclaw.ai/uk/gateway/remote-gateway-readme
scraped_at: 2026-05-25
---

> Цей вміст було об’єднано в [Віддалений доступ](</uk/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>). Актуальні інструкції дивіться на цій сторінці.

# Запуск OpenClaw.app із віддаленим Gateway

OpenClaw.app використовує SSH-тунелювання для підключення до віддаленого Gateway. У цьому посібнику показано, як це налаштувати.

## Огляд
[code] 
    flowchart TB
        subgraph Client["Клієнтська машина"]
            direction TB
            A["OpenClaw.app"]
            B["ws://127.0.0.1:18789\n(локальний порт)"]
            T["SSH-тунель"]
    
            A --> B
            B --> T
        end
        subgraph Remote["Віддалена машина"]
            direction TB
            C["WebSocket Gateway"]
            D["ws://127.0.0.1:18789"]
    
            C --> D
        end
        T --> C
[/code]

## Швидке налаштування

### Крок 1: Додайте конфігурацію SSH

Відредагуйте `~/.ssh/config` і додайте:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # наприклад, 172.27.187.184    User &lt;REMOTE_USER&gt;            # наприклад, jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

Замініть `&lt;REMOTE_IP&gt;` і `&lt;REMOTE_USER&gt;` на ваші значення.

### Крок 2: Скопіюйте SSH-ключ

Скопіюйте ваш відкритий ключ на віддалену машину (введіть пароль один раз):

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### Крок 3: Налаштуйте автентифікацію віддаленого Gateway

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

Використовуйте `gateway.remote.password` замість цього, якщо ваш віддалений Gateway використовує автентифікацію за паролем. `OPENCLAW_GATEWAY_TOKEN` усе ще дійсний як перевизначення на рівні оболонки, але стале налаштування віддаленого клієнта — це `gateway.remote.token` / `gateway.remote.password`.

### Крок 4: Запустіть SSH-тунель

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### Крок 5: Перезапустіть OpenClaw.app

bashCopy code
[code]
    # Закрийте OpenClaw.app (⌘Q), потім відкрийте знову:open /path/to/OpenClaw.app
[/code]

Тепер застосунок підключатиметься до віддаленого Gateway через SSH-тунель.

* * *

## Автозапуск тунелю під час входу в систему

Щоб SSH-тунель запускався автоматично, коли ви входите в систему, створіть агент Launch Agent.

### Створіть файл PLIST

Збережіть це як `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### Завантажте агент Launch Agent

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

Тепер тунель буде:

  * Запускатися автоматично, коли ви входите в систему
  * Перезапускатися, якщо аварійно завершиться
  * Працювати у фоновому режимі


Примітка щодо застарілих налаштувань: видаліть будь-який залишковий LaunchAgent `com.openclaw.ssh-tunnel`, якщо він є.

* * *

## Усунення несправностей

**Перевірте, чи працює тунель:**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**Перезапустіть тунель:**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**Зупиніть тунель:**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## Як це працює

Компонент | Що він робить  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Перенаправляє локальний порт 18789 на віддалений порт 18789  
`ssh -N` | SSH без виконання віддалених команд (лише перенаправлення портів)  
`KeepAlive` | Автоматично перезапускає тунель, якщо він аварійно завершується  
`RunAtLoad` | Запускає тунель, коли агент завантажується  
  
OpenClaw.app підключається до `ws://127.0.0.1:18789` на вашій клієнтській машині. SSH-тунель перенаправляє це з’єднання на порт 18789 віддаленої машини, де запущено Gateway.

## Пов’язане

  * [Віддалений доступ](</uk/gateway/remote>)
  * [Tailscale](</uk/gateway/tailscale>)


Was this useful?YesNo