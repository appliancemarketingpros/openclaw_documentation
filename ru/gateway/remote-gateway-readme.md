---
title: Настройка удаленного Gateway
source_url: https://docs.openclaw.ai/ru/gateway/remote-gateway-readme
scraped_at: 2026-06-29
---

Gateway & OpsRemote access

> Этот контент был объединен с разделом [Удаленный доступ](</ru/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>). Актуальное руководство см. на этой странице.

# Запуск OpenClaw.app с удаленным Gateway

OpenClaw.app использует SSH-туннелирование для подключения к удаленному gateway. В этом руководстве показано, как его настроить.

## Обзор
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

## Быстрая настройка

### Шаг 1: Добавьте конфигурацию SSH

Отредактируйте `~/.ssh/config` и добавьте:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # e.g., 172.27.187.184    User &lt;REMOTE_USER&gt;            # e.g., jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

Замените `&lt;REMOTE_IP&gt;` и `&lt;REMOTE_USER&gt;` своими значениями.

### Шаг 2: Скопируйте SSH-ключ

Скопируйте свой открытый ключ на удаленную машину (введите пароль один раз):

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### Шаг 3: Настройте аутентификацию удаленного Gateway

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

Вместо этого используйте `gateway.remote.password`, если ваш удаленный gateway использует аутентификацию по паролю. `OPENCLAW_GATEWAY_TOKEN` по-прежнему действителен как переопределение на уровне оболочки, но постоянная настройка удаленного клиента — это `gateway.remote.token` / `gateway.remote.password`.

### Шаг 4: Запустите SSH-туннель

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### Шаг 5: Перезапустите OpenClaw.app

bashCopy code
[code]
    # Quit OpenClaw.app (⌘Q), then reopen:open /path/to/OpenClaw.app
[/code]

Теперь приложение будет подключаться к удаленному gateway через SSH-туннель.

* * *

## Автозапуск туннеля при входе в систему

Чтобы SSH-туннель запускался автоматически при входе в систему, создайте Launch Agent.

### Создайте файл PLIST

Сохраните это как `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### Загрузите Launch Agent

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

Теперь туннель будет:

  * запускаться автоматически при входе в систему
  * перезапускаться при сбое
  * продолжать работать в фоновом режиме


Устаревшее примечание: удалите оставшийся LaunchAgent `com.openclaw.ssh-tunnel`, если он есть.

* * *

## Устранение неполадок

**Проверьте, запущен ли туннель:**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**Перезапустите туннель:**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**Остановите туннель:**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## Как это работает

Компонент | Что он делает  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Перенаправляет локальный порт 18789 на удаленный порт 18789  
`ssh -N` | SSH без выполнения удаленных команд (только проброс портов)  
`KeepAlive` | Автоматически перезапускает туннель при сбое  
`RunAtLoad` | Запускает туннель при загрузке агента  
  
OpenClaw.app подключается к `ws://127.0.0.1:18789` на вашей клиентской машине. SSH-туннель перенаправляет это подключение на порт 18789 на удаленной машине, где работает Gateway.

## Связанные разделы

  * [Удаленный доступ](</ru/gateway/remote>)
  * [Tailscale](</ru/gateway/tailscale>)


Was this useful?YesNo

Open issue