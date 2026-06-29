---
title: Fly.io
source_url: https://docs.openclaw.ai/ru/install/fly
scraped_at: 2026-06-29
---

InstallHosting

**Цель:** OpenClaw Gateway работает на машине [Fly.io](<https://fly.io>) с постоянным хранилищем, автоматическим HTTPS и доступом к Discord/каналам.

## Что потребуется

  * Установленный [flyctl CLI](<https://fly.io/docs/hands-on/install-flyctl/>)
  * Учетная запись Fly.io (подойдет бесплатный тариф)
  * Аутентификация модели: API-ключ выбранного поставщика моделей
  * Учетные данные канала: токен бота Discord, токен Telegram и т. д.


## Быстрый путь для начинающих

  1. Клонируйте репозиторий → настройте `fly.toml`
  2. Создайте приложение и том → задайте секреты
  3. Разверните с помощью `fly deploy`
  4. Подключитесь по SSH, чтобы создать конфигурацию, или используйте интерфейс управления


* ### Создайте приложение Fly

bashCopy code
[code]
    # Clone the repogit clone https://github.com/openclaw/openclaw.gitcd openclaw # Create a new Fly app (pick your own name)fly apps create my-openclaw # Create a persistent volume (1GB is usually enough)fly volumes create openclaw_data --size 1 --region iad
[/code]

**Совет:** Выберите регион рядом с вами. Частые варианты: `lhr` (Лондон), `iad` (Вирджиния), `sjc` (Сан-Хосе).

* ### Настройте fly.toml

Отредактируйте `fly.toml` под имя вашего приложения и требования.

**Примечание по безопасности:** Конфигурация по умолчанию открывает публичный URL. Для усиленного развертывания без публичного IP см. Приватное развертывание или используйте `deploy/fly.private.toml`.

tomlCopy code
[code]
    app = "my-openclaw"  # Your app nameprimary_region = "iad" [build]  dockerfile = "Dockerfile" [env]  NODE_ENV = "production"  OPENCLAW_PREFER_PNPM = "1"  OPENCLAW_STATE_DIR = "/data"  NODE_OPTIONS = "--max-old-space-size=1536" [processes]  app = "node dist/index.js gateway --allow-unconfigured --port 3000 --bind lan" [http_service]  internal_port = 3000  force_https = true  auto_stop_machines = false  auto_start_machines = true  min_machines_running = 1  processes = ["app"] [[vm]]  size = "shared-cpu-2x"  memory = "2048mb" [mounts]  source = "openclaw_data"  destination = "/data"
[/code]

Docker-образ OpenClaw использует `tini` как точку входа. Команды процессов Fly заменяют Docker `CMD`, не заменяя `ENTRYPOINT`, поэтому процесс по-прежнему запускается под `tini`.

**Ключевые настройки:**

Настройка | Зачем  
---|---  
`--bind lan` | Привязывает к `0.0.0.0`, чтобы прокси Fly мог достучаться до Gateway  
`--allow-unconfigured` | Запускает без файла конфигурации (вы создадите его позже)  
`internal_port = 3000` | Должен совпадать с `--port 3000` (или `OPENCLAW_GATEWAY_PORT`) для проверок работоспособности Fly  
`memory = "2048mb"` | 512 МБ слишком мало; рекомендуется 2 ГБ  
`OPENCLAW_STATE_DIR = "/data"` | Сохраняет состояние на томе  
  
* ### Задайте секреты

bashCopy code
[code]
    # Required: Gateway token (for non-loopback binding)fly secrets set OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 32) # Model provider API keysfly secrets set ANTHROPIC_API_KEY=example-anthropic-key-not-real # Optional: Other providersfly secrets set OPENAI_API_KEY=example-openai-key-not-realfly secrets set GOOGLE_API_KEY=... # Channel tokensfly secrets set DISCORD_BOT_TOKEN=example-discord-bot-token
[/code]

**Примечания:**

  * Привязки не к loopback (`--bind lan`) требуют корректного пути аутентификации Gateway. В этом примере Fly.io используется `OPENCLAW_GATEWAY_TOKEN`, но `gateway.auth.password` или правильно настроенное развертывание `trusted-proxy` не к loopback также удовлетворяют этому требованию.
  * Обращайтесь с этими токенами как с паролями.
  * **Предпочитайте переменные окружения файлу конфигурации** для всех API-ключей и токенов. Так секреты не попадут в `openclaw.json`, где их можно случайно раскрыть или записать в логи.


* ### Разверните

bashCopy code
[code]
    fly deploy
[/code]

Первое развертывание собирает Docker-образ (~2-3 минуты). Последующие развертывания выполняются быстрее.

После развертывания проверьте:

bashCopy code
[code]
    fly statusfly logs
[/code]

Вы должны увидеть:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:3000 (PID xxx)[discord] logged in to discord as xxx
[/code]

* ### Создайте файл конфигурации

Подключитесь к машине по SSH, чтобы создать корректную конфигурацию:

bashCopy code
[code]
    fly ssh console
[/code]

Создайте каталог и файл конфигурации:

bashCopy code
[code]
    mkdir -p /datacat > /data/openclaw.json << 'EOF'{  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-opus-4-6",        "fallbacks": ["anthropic/claude-sonnet-4-6", "openai/gpt-5.4"]      },      "maxConcurrent": 4    },    "list": [      {        "id": "main",        "default": true      }    ]  },  "auth": {    "profiles": {      "anthropic:default": { "mode": "token", "provider": "anthropic" },      "openai:default": { "mode": "token", "provider": "openai" }    }  },  "bindings": [    {      "agentId": "main",      "match": { "channel": "discord" }    }  ],  "channels": {    "discord": {      "enabled": true,      "groupPolicy": "allowlist",      "guilds": {        "YOUR_GUILD_ID": {          "channels": { "general": { "allow": true } },          "requireMention": false        }      }    }  },  "gateway": {    "mode": "local",    "bind": "auto",    "controlUi": {      "allowedOrigins": [        "https://my-openclaw.fly.dev",        "http://localhost:3000",        "http://127.0.0.1:3000"      ]    }  },  "meta": {}}EOF
[/code]

**Примечание:** При `OPENCLAW_STATE_DIR=/data` путь к конфигурации — `/data/openclaw.json`.

**Примечание:** Замените `https://my-openclaw.fly.dev` на настоящий origin вашего приложения Fly. При запуске Gateway начальные локальные origin интерфейса управления берутся из значений времени выполнения `--bind` и `--port`, чтобы первая загрузка могла пройти до появления конфигурации, но для доступа через браузер через Fly все равно нужен точный HTTPS-origin, указанный в `gateway.controlUi.allowedOrigins`.

**Примечание:** Токен Discord может поступать из любого из этих источников:

  * Переменная окружения: `DISCORD_BOT_TOKEN` (рекомендуется для секретов)
  * Файл конфигурации: `channels.discord.token`


Если используется переменная окружения, добавлять токен в конфигурацию не нужно. Gateway автоматически читает `DISCORD_BOT_TOKEN`.

Перезапустите, чтобы применить:

bashCopy code
[code]
    exitfly machine restart <machine-id>
[/code]

* ### Получите доступ к Gateway

### Интерфейс управления

Откройте в браузере:

bashCopy code
[code]
    fly open
[/code]

Или перейдите на `https://my-openclaw.fly.dev/`

Аутентифицируйтесь с настроенным общим секретом. В этом руководстве используется токен Gateway из `OPENCLAW_GATEWAY_TOKEN`; если вы переключились на аутентификацию по паролю, используйте этот пароль.

### Логи

bashCopy code
[code]
    fly logs              # Live logsfly logs --no-tail    # Recent logs
[/code]

### Консоль SSH

bashCopy code
[code]
    fly ssh console
[/code]

## Устранение неполадок

### "App is not listening on expected address"

Gateway привязан к `127.0.0.1` вместо `0.0.0.0`.

**Исправление:** Добавьте `--bind lan` в команду процесса в `fly.toml`.

### Проверки работоспособности не проходят / в соединении отказано

Fly не может достучаться до Gateway на настроенном порту.

**Исправление:** Убедитесь, что `internal_port` совпадает с портом Gateway (задайте `--port 3000` или `OPENCLAW_GATEWAY_PORT=3000`).

### OOM / проблемы с памятью

Контейнер постоянно перезапускается или завершается принудительно. Признаки: `SIGABRT`, `v8::internal::Runtime_AllocateInYoungGeneration` или тихие перезапуски.

**Исправление:** Увеличьте память в `fly.toml`:

tomlCopy code
[code]
    [[vm]]  memory = "2048mb"
[/code]

Или обновите существующую машину:

bashCopy code
[code]
    fly machine update <machine-id> --vm-memory 2048 -y
[/code]

**Примечание:** 512 МБ слишком мало. 1 ГБ может работать, но возможен OOM под нагрузкой или при подробном логировании. **Рекомендуется 2 ГБ.**

### Проблемы с блокировкой Gateway

Gateway отказывается запускаться с ошибками "already running".

Это происходит, когда контейнер перезапускается, но файл блокировки PID сохраняется на томе.

**Исправление:** Удалите файл блокировки:

bashCopy code
[code]
    fly ssh console --command "rm -f /data/gateway.*.lock"fly machine restart <machine-id>
[/code]

Файл блокировки находится в `/data/gateway.*.lock` (не в подкаталоге).

### Конфигурация не читается

`--allow-unconfigured` только обходит стартовую защиту. Он не создает и не исправляет `/data/openclaw.json`, поэтому убедитесь, что настоящая конфигурация существует и включает `gateway.mode="local"`, если нужен обычный локальный запуск Gateway.

Проверьте, что конфигурация существует:

bashCopy code
[code]
    fly ssh console --command "cat /data/openclaw.json"
[/code]

### Запись конфигурации через SSH

Команда `fly ssh console -C` не поддерживает shell-перенаправление. Чтобы записать файл конфигурации:

bashCopy code
[code]
    # Use echo + tee (pipe from local to remote)echo '{"your":"config"}' | fly ssh console -C "tee /data/openclaw.json" # Or use sftpfly sftp shell> put /local/path/config.json /data/openclaw.json
[/code]

**Примечание:** `fly sftp` может завершиться ошибкой, если файл уже существует. Сначала удалите его:

bashCopy code
[code]
    fly ssh console --command "rm /data/openclaw.json"
[/code]

### Состояние не сохраняется

Если после перезапуска пропадают профили аутентификации, состояние канала/поставщика или сессии, каталог состояния записывается в файловую систему контейнера.

**Исправление:** Убедитесь, что `OPENCLAW_STATE_DIR=/data` задан в `fly.toml`, и выполните повторное развертывание.

## Обновления

bashCopy code
[code]
    # Pull latest changesgit pull # Redeployfly deploy # Check healthfly statusfly logs
[/code]

### Обновление команды машины

Если нужно изменить команду запуска без полного повторного развертывания:

bashCopy code
[code]
    # Get machine IDfly machines list # Update commandfly machine update <machine-id> --command "node dist/index.js gateway --port 3000 --bind lan" -y # Or with memory increasefly machine update <machine-id> --vm-memory 2048 --command "node dist/index.js gateway --port 3000 --bind lan" -y
[/code]

**Примечание:** После `fly deploy` команда машины может сброситься к значению из `fly.toml`. Если вы вносили ручные изменения, примените их повторно после развертывания.

## Приватное развертывание (усиленное)

По умолчанию Fly выделяет публичные IP, делая ваш Gateway доступным по адресу `https://your-app.fly.dev`. Это удобно, но означает, что ваше развертывание обнаруживается интернет-сканерами (Shodan, Censys и т. д.).

Для усиленного развертывания **без публичной доступности** используйте приватный шаблон.

### Когда использовать приватное развертывание

  * Вы выполняете только **исходящие** вызовы/сообщения (без входящих Webhook)
  * Вы используете туннели **ngrok или Tailscale** для любых обратных вызовов Webhook
  * Вы получаете доступ к Gateway через **SSH, прокси или WireGuard** , а не через браузер
  * Вы хотите, чтобы развертывание было **скрыто от интернет-сканеров**


### Настройка

Используйте `deploy/fly.private.toml` вместо стандартной конфигурации:

bashCopy code
[code]
    # Deploy with private configfly deploy -c deploy/fly.private.toml
[/code]

Или преобразуйте существующее развертывание:

bashCopy code
[code]
    # List current IPsfly ips list -a my-openclaw # Release public IPsfly ips release <public-ipv4> -a my-openclawfly ips release <public-ipv6> -a my-openclaw # Switch to private config so future deploys don't re-allocate public IPs# (remove [http_service] or deploy with the private template)fly deploy -c deploy/fly.private.toml # Allocate private-only IPv6fly ips allocate-v6 --private -a my-openclaw
[/code]

После этого `fly ips list` должен показывать только IP типа `private`:

CodeCopy code
[code]
    VERSION  IP                   TYPE             REGIONv6       fdaa:x:x:x:x::x      private          global
[/code]

### Доступ к приватному развертыванию

Так как публичного URL нет, используйте один из этих способов:

**Вариант 1: Локальный прокси (самый простой)**

bashCopy code
[code]
    # Forward local port 3000 to the appfly proxy 3000:3000 -a my-openclaw # Then open http://localhost:3000 in browser
[/code]

**Вариант 2: WireGuard VPN**

bashCopy code
[code]
    # Create WireGuard config (one-time)fly wireguard create # Import to WireGuard client, then access via internal IPv6# Example: http://[fdaa:x:x:x:x::x]:3000
[/code]

**Вариант 3: только SSH**

bashCopy code
[code]
    fly ssh console -a my-openclaw
[/code]

### Webhook-и с приватным развертыванием

Если вам нужны обратные вызовы Webhook (Twilio, Telnyx и т. д.) без публичного доступа:

  1. **Туннель ngrok** \- Запустите ngrok внутри контейнера или как sidecar
  2. **Tailscale Funnel** \- Откройте доступ к определенным путям через Tailscale
  3. **Только исходящие** \- Некоторые провайдеры (Twilio) нормально работают для исходящих вызовов без Webhook-ов


Пример конфигурации голосовых вызовов с ngrok:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio",          tunnel: { provider: "ngrok" },          webhookSecurity: {            allowedHosts: ["example.ngrok.app"],          },        },      },    },  },}
[/code]

Туннель ngrok запускается внутри контейнера и предоставляет публичный URL Webhook без раскрытия самого приложения Fly. Задайте `webhookSecurity.allowedHosts` как публичное имя хоста туннеля, чтобы перенаправленные заголовки host принимались.

### Преимущества безопасности

Аспект | Публично | Приватно  
---|---|---  
Интернет-сканеры | Обнаруживается | Скрыто  
Прямые атаки | Возможны | Заблокированы  
Доступ к Control UI | Браузер | Прокси/VPN  
Доставка Webhook | Напрямую | Через туннель  
  
## Примечания

  * Fly.io использует **архитектуру x86** (не ARM)
  * Dockerfile совместим с обеими архитектурами
  * Для первоначальной настройки WhatsApp/Telegram используйте `fly ssh console`
  * Постоянные данные находятся на томе в `/data`
  * Signal требует Java + signal-cli; используйте пользовательский образ и оставьте память на уровне 2 ГБ+.


## Стоимость

С рекомендуемой конфигурацией (`shared-cpu-2x`, 2 ГБ RAM):

  * ~$10-15/месяц в зависимости от использования
  * Бесплатный тариф включает некоторую квоту


Подробности см. в [тарифах Fly.io](<https://fly.io/docs/about/pricing/>).

## Следующие шаги

  * Настройте каналы обмена сообщениями: [Каналы](</ru/channels>)
  * Настройте Gateway: [Конфигурация Gateway](</ru/gateway/configuration>)
  * Поддерживайте OpenClaw в актуальном состоянии: [Обновление](</ru/install/updating>)


## Связанные материалы

  * [Обзор установки](</ru/install>)
  * [Hetzner](</ru/install/hetzner>)
  * [Docker](</ru/install/docker>)
  * [VPS-хостинг](</ru/vps>)


Was this useful?YesNo

Open issue