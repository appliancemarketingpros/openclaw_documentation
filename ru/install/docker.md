---
title: Docker
source_url: https://docs.openclaw.ai/ru/install/docker
scraped_at: 2026-06-29
---

InstallContainers

Docker **необязателен**. Используйте его только если вам нужен контейнеризированный Gateway или проверка Docker-сценария.

## Подходит ли мне Docker?

  * **Да** : вам нужна изолированная одноразовая среда Gateway или запуск OpenClaw на хосте без локальных установок.
  * **Нет** : вы запускаете OpenClaw на своей машине и хотите самый быстрый цикл разработки. Вместо этого используйте обычный процесс установки.
  * **Примечание о песочнице** : стандартный бэкенд песочницы использует Docker, когда песочница включена, но песочница по умолчанию отключена и **не** требует запуска всего Gateway в Docker. Также доступны бэкенды песочницы SSH и OpenShell. См. [Песочница](</ru/gateway/sandboxing>).


## Предварительные требования

  * Docker Desktop (или Docker Engine) + Docker Compose v2
  * Минимум 2 ГБ ОЗУ для сборки образа (`pnpm install` может быть завершен из-за нехватки памяти на хостах с 1 ГБ с кодом выхода 137)
  * Достаточно места на диске для образов и журналов
  * При запуске на VPS/публичном хосте изучите [Усиление безопасности для сетевой доступности](</ru/gateway/security>), особенно политику файрвола Docker `DOCKER-USER`.


## Контейнеризированный Gateway

* ### Соберите образ

Из корня репозитория запустите скрипт настройки:

bashCopy code
[code]
    ./scripts/docker/setup.sh
[/code]

Это локально собирает образ Gateway. Чтобы вместо этого использовать предварительно собранный образ:

bashCopy code
[code]
    export OPENCLAW_IMAGE="ghcr.io/openclaw/openclaw:latest"./scripts/docker/setup.sh
[/code]

Предварительно собранные образы сначала публикуются в [GitHub Container Registry](<https://github.com/openclaw/openclaw/pkgs/container/openclaw>). GHCR является основным реестром для автоматизации релизов, закрепленных развертываний и проверок происхождения. Тот же релизный процесс также публикует официальный зеркальный образ Docker Hub в `openclaw/openclaw` для хостов, предпочитающих Docker Hub:

bashCopy code
[code]
    export OPENCLAW_IMAGE="openclaw/openclaw:latest"./scripts/docker/setup.sh
[/code]

Используйте `ghcr.io/openclaw/openclaw` или `openclaw/openclaw`. Избегайте зеркал Docker Hub от сообщества, потому что OpenClaw не контролирует их сроки релизов, пересборки или политику хранения. Распространенные официальные теги: `main`, `latest`, `<version>` (например, `2026.2.26`) и бета-версии, такие как `2026.2.26-beta.1`. Бета-теги не перемещают `latest` или `main`.

* ### Повторный запуск без доступа к сети

На офлайн-хостах сначала перенесите и загрузите образ:

bashCopy code
[code]
    docker load -i openclaw-image.tarexport OPENCLAW_IMAGE="ghcr.io/openclaw/openclaw:latest"./scripts/docker/setup.sh --offline
[/code]

`--offline` проверяет, что `OPENCLAW_IMAGE` уже существует локально, отключает неявные загрузки и сборки Compose, затем выполняет обычный процесс настройки, включая синхронизацию `.env`, исправление разрешений, первичную настройку, синхронизацию конфигурации Gateway и запуск Compose.

Если задано `OPENCLAW_SANDBOX=1`, офлайн-настройка также проверяет настроенный стандартный образ песочницы и активные образы песочницы для каждого агента в демоне за `OPENCLAW_DOCKER_SOCKET`. Браузерные образы на базе Docker также должны содержать текущую метку контракта браузера OpenClaw. Если обязательный образ отсутствует или несовместим, настройка завершается без изменения конфигурации песочницы вместо сообщения об успехе с неработоспособной песочницей.

* ### Завершите первичную настройку

Скрипт настройки автоматически запускает первичную настройку. Он:

  * запросит API-ключи провайдера
  * сгенерирует токен Gateway и запишет его в `.env`
  * создаст каталог секретного ключа auth-profile
  * запустит Gateway через Docker Compose


Во время настройки первичная настройка перед запуском и записи конфигурации выполняются напрямую через `openclaw-gateway`. `openclaw-cli` предназначен для команд, которые вы запускаете после того, как контейнер Gateway уже существует.

* ### Откройте интерфейс управления

Откройте `http://127.0.0.1:18789/` в браузере и вставьте настроенный общий секрет в Settings. Скрипт настройки по умолчанию записывает токен в `.env`; если вы переключите конфигурацию контейнера на аутентификацию по паролю, используйте вместо него этот пароль.

Нужен URL еще раз?

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-open
[/code]

* ### Настройте каналы (необязательно)

Используйте контейнер CLI, чтобы добавить каналы сообщений:

bashCopy code
[code]
    # WhatsApp (QR)docker compose run --rm openclaw-cli channels login # Telegramdocker compose run --rm openclaw-cli channels add --channel telegram --token "<token>" # Discorddocker compose run --rm openclaw-cli channels add --channel discord --token "<token>"
[/code]

Документация: [WhatsApp](</ru/channels/whatsapp>), [Telegram](</ru/channels/telegram>), [Discord](</ru/channels/discord>)

### Ручной процесс

Если вы предпочитаете выполнять каждый шаг самостоятельно, а не использовать скрипт настройки:

bashCopy code
[code]
    docker build -t openclaw:local -f Dockerfile .docker compose run --rm --no-deps --entrypoint node openclaw-gateway \  dist/index.js onboard --mode local --no-install-daemondocker compose run --rm --no-deps --entrypoint node openclaw-gateway \  dist/index.js config set --batch-json '[{"path":"gateway.mode","value":"local"},{"path":"gateway.bind","value":"lan"},{"path":"gateway.controlUi.allowedOrigins","value":["http://localhost:18789","http://127.0.0.1:18789"]}]'docker compose up -d openclaw-gateway
[/code]

### Переменные окружения

Скрипт настройки принимает следующие необязательные переменные окружения:

Переменная | Назначение  
---|---  
`OPENCLAW_IMAGE` | Использовать удаленный образ вместо локальной сборки  
`OPENCLAW_IMAGE_APT_PACKAGES` | Установить дополнительные apt-пакеты во время сборки (через пробел)  
`OPENCLAW_IMAGE_PIP_PACKAGES` | Установить дополнительные пакеты Python во время сборки (через пробел)  
`OPENCLAW_EXTENSIONS` | Предварительно установить зависимости Plugin во время сборки (имена через пробел)  
`OPENCLAW_EXTRA_MOUNTS` | Дополнительные bind-mount с хоста (через запятую `source:target[:opts]`)  
`OPENCLAW_HOME_VOLUME` | Сохранять `/home/node` в именованном томе Docker  
`OPENCLAW_SANDBOX` | Включить начальную настройку песочницы (`1`, `true`, `yes`, `on`)  
`OPENCLAW_SKIP_ONBOARDING` | Пропустить интерактивный шаг первичной настройки (`1`, `true`, `yes`, `on`)  
`OPENCLAW_DOCKER_SOCKET` | Переопределить путь к сокету Docker  
`OPENCLAW_DISABLE_BONJOUR` | Отключить рекламу Bonjour/mDNS (по умолчанию `1` для Docker)  
`OPENCLAW_DISABLE_BUNDLED_SOURCE_OVERLAYS` | Отключить bind-mount-наложения исходного кода встроенных Plugin  
`OTEL_EXPORTER_OTLP_ENDPOINT` | Общая конечная точка коллектора OTLP/HTTP для экспорта OpenTelemetry  
`OTEL_EXPORTER_OTLP_*_ENDPOINT` | Конечные точки OTLP для отдельных сигналов: трасс, метрик или журналов  
`OTEL_EXPORTER_OTLP_PROTOCOL` | Переопределение протокола OTLP. Сегодня поддерживается только `http/protobuf`  
`OTEL_SERVICE_NAME` | Имя сервиса, используемое для ресурсов OpenTelemetry  
`OTEL_SEMCONV_STABILITY_OPT_IN` | Включить новейшие экспериментальные семантические атрибуты GenAI  
`OPENCLAW_OTEL_PRELOADED` | Не запускать второй SDK OpenTelemetry, если один уже предварительно загружен  
  
Официальный образ Docker не включает Homebrew. Во время первичной настройки OpenClaw скрывает установщики зависимостей Skills, доступные только через brew, когда он работает в Linux- контейнере без `brew`; эти зависимости должны быть предоставлены пользовательским образом или установлены вручную. Для зависимостей, доступных из пакетов Debian, используйте `OPENCLAW_IMAGE_APT_PACKAGES` во время сборки образа. Устаревшее имя `OPENCLAW_DOCKER_APT_PACKAGES` по-прежнему принимается. Для зависимостей Python используйте `OPENCLAW_IMAGE_PIP_PACKAGES`. Это выполняет `python3 -m pip install --break-system-packages` во время сборки образа, поэтому закрепляйте версии пакетов и используйте только доверенные индексы пакетов.

Сопровождающие могут тестировать исходный код встроенного Plugin с упакованным образом, смонтировав один каталог исходного кода Plugin поверх его упакованного пути исходного кода, например `OPENCLAW_EXTRA_MOUNTS=/path/to/fork/extensions/synology-chat:/app/extensions/synology-chat:ro`. Этот смонтированный каталог исходного кода переопределяет соответствующий скомпилированный бандл `/app/dist/extensions/synology-chat` для того же идентификатора Plugin.

### Наблюдаемость

Экспорт OpenTelemetry выполняется из контейнера Gateway наружу к вашему коллектору OTLP. Он не требует опубликованного порта Docker. Если вы собираете образ локально и хотите, чтобы встроенный экспортер OpenTelemetry был доступен внутри образа, добавьте его runtime-зависимости:

bashCopy code
[code]
    export OPENCLAW_EXTENSIONS="diagnostics-otel"export OTEL_EXPORTER_OTLP_ENDPOINT="http://otel-collector:4318"export OTEL_SERVICE_NAME="openclaw-gateway"./scripts/docker/setup.sh
[/code]

Установите официальный Plugin `@openclaw/diagnostics-otel` из ClawHub в упакованных установках Docker перед включением экспорта. Пользовательские образы, собранные из исходного кода, могут по-прежнему включать локальный исходный код Plugin с `OPENCLAW_EXTENSIONS=diagnostics-otel`. Чтобы включить экспорт, разрешите и включите Plugin `diagnostics-otel` в конфигурации, затем задайте `diagnostics.otel.enabled=true` или используйте пример конфигурации в [Экспорт OpenTelemetry ](</ru/gateway/opentelemetry>). Заголовки аутентификации коллектора настраиваются через `diagnostics.otel.headers`, а не через переменные окружения Docker.

Метрики Prometheus используют уже опубликованный порт Gateway. Установите `clawhub:@openclaw/diagnostics-prometheus`, включите Plugin `diagnostics-prometheus`, затем собирайте метрики:

textCopy code
[code]
    http://<gateway-host>:18789/api/diagnostics/prometheus
[/code]

Маршрут защищен аутентификацией Gateway. Не открывайте отдельный публичный порт `/metrics` или неаутентифицированный путь reverse-proxy. См. [Метрики Prometheus](</ru/gateway/prometheus>).

### Проверки работоспособности

Конечные точки проб контейнера (аутентификация не требуется):

bashCopy code
[code]
    curl -fsS http://127.0.0.1:18789/healthz   # livenesscurl -fsS http://127.0.0.1:18789/readyz     # readiness
[/code]

Образ Docker включает встроенный `HEALTHCHECK`, который опрашивает `/healthz`. Если проверки продолжают завершаться ошибкой, Docker помечает контейнер как `unhealthy`, и системы оркестрации могут перезапустить или заменить его.

Аутентифицированный глубокий снимок состояния:

bashCopy code
[code]
    docker compose exec openclaw-gateway node dist/index.js health --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

### LAN и loopback

`scripts/docker/setup.sh` по умолчанию задает `OPENCLAW_GATEWAY_BIND=lan`, чтобы доступ с хоста к `http://127.0.0.1:18789` работал через публикацию порта Docker.

  * `lan` (по умолчанию): браузер хоста и CLI хоста могут обращаться к опубликованному порту Gateway.
  * `loopback`: только процессы внутри сетевого пространства имен контейнера могут напрямую обращаться к Gateway.


### Локальные провайдеры хоста

Когда OpenClaw работает в Docker, `127.0.0.1` внутри контейнера — это сам контейнер, а не ваша хост-машина. Используйте `host.docker.internal` для AI-провайдеров, которые работают на хосте:

Провайдер | URL хоста по умолчанию | URL настройки Docker  
---|---|---  
LM Studio | `http://127.0.0.1:1234` | `http://host.docker.internal:1234`  
Ollama | `http://127.0.0.1:11434` | `http://host.docker.internal:11434`  
  
Встроенная настройка Docker использует эти URL хоста как значения по умолчанию для подключения LM Studio и Ollama при onboarding, а `docker-compose.yml` сопоставляет `host.docker.internal` с host gateway Docker для Linux Docker Engine. Docker Desktop уже предоставляет то же имя хоста в macOS и Windows.

Сервисы хоста также должны слушать на адресе, доступном из Docker:

bashCopy code
[code]
    lms server start --port 1234 --bind 0.0.0.0OLLAMA_HOST=0.0.0.0:11434 ollama serve
[/code]

Если вы используете собственный файл Compose или команду `docker run`, добавьте такое же сопоставление хоста самостоятельно, например `--add-host=host.docker.internal:host-gateway`.

### Бэкенд Claude CLI в Docker

Официальный Docker-образ OpenClaw не предустанавливает Claude Code. Установите и войдите в Claude Code внутри пользователя контейнера, который запускает OpenClaw, затем сохраните домашний каталог этого контейнера, чтобы обновления образа не стирали бинарный файл или состояние аутентификации Claude.

Для новых установок Docker включите постоянный том `/home/node` перед запуском настройки:

bashCopy code
[code]
    export OPENCLAW_IMAGE="ghcr.io/openclaw/openclaw:latest"export OPENCLAW_HOME_VOLUME="openclaw_home"./scripts/docker/setup.sh
[/code]

Для существующей установки Docker сначала остановите стек и повторно загрузите текущие значения Docker `.env` перед повторным запуском настройки. Скрипт настройки сам не читает `.env`; он перезаписывает `.env` из текущей оболочки и значений по умолчанию. Для сгенерированного `.env` выполните:

bashCopy code
[code]
    set -a. ./.envset +aexport OPENCLAW_HOME_VOLUME="${OPENCLAW_HOME_VOLUME:-openclaw_home}"./scripts/docker/setup.sh
[/code]

Если ваш `.env` содержит значения, которые ваша оболочка не может загрузить, сначала вручную повторно экспортируйте существующие значения, на которые вы полагаетесь, такие как `OPENCLAW_IMAGE`, порты, режим привязки, пользовательские пути, `OPENCLAW_EXTRA_MOUNTS`, песочница и настройки пропуска onboarding. Сгенерированный overlay монтирует домашний том как для `openclaw-gateway`, так и для `openclaw-cli`.

Запускайте оставшиеся команды со сгенерированным overlay Compose, чтобы оба сервиса монтировали сохраненный домашний каталог. Если ваша настройка также использует `docker-compose.override.yml`, включите его перед `docker-compose.extra.yml`.

Установите Claude Code в этот сохраненный домашний каталог:

bashCopy code
[code]
    docker compose -f docker-compose.yml -f docker-compose.extra.yml run --rm \  --entrypoint sh openclaw-cli -lc \  'curl -fsSL https://claude.ai/install.sh | bash'
[/code]

Нативный установщик записывает бинарный файл `claude` в `/home/node/.local/bin/claude`. Укажите OpenClaw использовать этот путь внутри контейнера:

bashCopy code
[code]
    docker compose -f docker-compose.yml -f docker-compose.extra.yml run --rm \  openclaw-cli config set \  agents.defaults.cliBackends.claude-cli.command \  /home/node/.local/bin/claude
[/code]

Войдите в систему и проверьте изнутри того же сохраненного домашнего каталога контейнера:

bashCopy code
[code]
    docker compose -f docker-compose.yml -f docker-compose.extra.yml run --rm \  --entrypoint /home/node/.local/bin/claude openclaw-cli auth logindocker compose -f docker-compose.yml -f docker-compose.extra.yml run --rm \  --entrypoint /home/node/.local/bin/claude openclaw-cli auth status --textdocker compose -f docker-compose.yml -f docker-compose.extra.yml run --rm \  openclaw-cli models auth login \  --provider anthropic --method cli --set-defaultdocker compose -f docker-compose.yml -f docker-compose.extra.yml run --rm \  openclaw-cli models list --provider anthropic
[/code]

После этого можно использовать встроенный бэкенд `claude-cli`:

bashCopy code
[code]
    docker compose -f docker-compose.yml -f docker-compose.extra.yml run --rm \  openclaw-cli agent \  --agent main \  --model claude-cli/claude-sonnet-4-6 \  --message "Say hello from Docker Claude CLI"
[/code]

`OPENCLAW_HOME_VOLUME` сохраняет нативную установку Claude Code в `/home/node/.local/bin` и `/home/node/.local/share/claude`, а также настройки и состояние аутентификации Claude Code в `/home/node/.claude` и `/home/node/.claude.json`. Сохранения только `/home/node/.openclaw` недостаточно для повторного использования Claude CLI. Если вы используете `OPENCLAW_EXTRA_MOUNTS` вместо домашнего тома, смонтируйте все эти пути Claude в оба сервиса Docker.

### Bonjour / mDNS

Сетевой мост Docker обычно ненадежно пересылает multicast Bonjour/mDNS (`224.0.0.251:5353`). Поэтому встроенная настройка Compose по умолчанию задает `OPENCLAW_DISABLE_BONJOUR=1`, чтобы Gateway не уходил в цикл сбоев и не перезапускал рекламу снова и снова, когда мост отбрасывает multicast-трафик.

Для Docker-хостов используйте опубликованный URL Gateway, Tailscale или wide-area DNS-SD. Задавайте `OPENCLAW_DISABLE_BONJOUR=0` только при запуске с host networking, macvlan или другой сетью, где multicast mDNS заведомо работает.

О подводных камнях и устранении неполадок см. [обнаружение Bonjour](</ru/gateway/bonjour>).

### Хранилище и сохранение данных

Docker Compose монтирует bind-mount `OPENCLAW_CONFIG_DIR` в `/home/node/.openclaw`, `OPENCLAW_WORKSPACE_DIR` в `/home/node/.openclaw/workspace` и `OPENCLAW_AUTH_PROFILE_SECRET_DIR` в `/home/node/.config/openclaw`, поэтому эти пути сохраняются при замене контейнера. Если какая-либо переменная не задана, встроенный `docker-compose.yml` использует запасной путь внутри `${HOME}` или `/tmp`, если сам `HOME` также отсутствует. Это не дает `docker compose up` вывести спецификацию тома с пустым источником в минимальных окружениях.

В этом смонтированном каталоге конфигурации OpenClaw хранит:

  * `openclaw.json` для конфигурации поведения
  * `agents/<agentId>/agent/auth-profiles.json` для сохраненной OAuth/API-key-аутентификации провайдера
  * `.env` для runtime-секретов из переменных окружения, таких как `OPENCLAW_GATEWAY_TOKEN`


Каталог секретного ключа auth-profile хранит локальный ключ шифрования, используемый для материала токенов профиля аутентификации на основе OAuth. Храните его вместе с состоянием вашего Docker-хоста, но отдельно от `OPENCLAW_CONFIG_DIR`.

Установленные загружаемые plugins хранят состояние своих пакетов в смонтированном домашнем каталоге OpenClaw, поэтому записи об установке plugin и корни пакетов сохраняются при замене контейнера. Запуск Gateway не создает деревья зависимостей bundled-plugin.

Полные сведения о сохранении данных в развертываниях VM см. в [Среда выполнения Docker VM — что и где сохраняется](</ru/install/docker-vm-runtime#what-persists-where>).

**Очаги роста диска:** следите за `media/`, JSONL-файлами сессий, общей базой данных состояния SQLite, корнями пакетов установленных plugin и ротационными файловыми логами в `/tmp/openclaw/`.

### Вспомогательные shell-скрипты (необязательно)

Для более удобного повседневного управления Docker установите `ClawDock`:

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

Если вы установили ClawDock из старого raw-пути `scripts/shell-helpers/clawdock-helpers.sh`, повторно выполните приведенную выше команду установки, чтобы ваш локальный файл помощника отслеживал новое расположение.

Затем используйте `clawdock-start`, `clawdock-stop`, `clawdock-dashboard` и т. д. Выполните `clawdock-help`, чтобы увидеть все команды. Полное руководство по помощнику см. в [ClawDock](</ru/install/clawdock>).

Включить песочницу агента для Docker gateway bashCopy code
[code]
    export OPENCLAW_SANDBOX=1./scripts/docker/setup.sh
[/code]

Пользовательский путь к сокету (например, rootless Docker):

bashCopy code
[code]
    export OPENCLAW_SANDBOX=1export OPENCLAW_DOCKER_SOCKET=/run/user/1000/docker.sock./scripts/docker/setup.sh
[/code]

Скрипт монтирует `docker.sock` только после успешного выполнения предварительных условий песочницы. Если настройку песочницы невозможно завершить, скрипт сбрасывает `agents.defaults.sandbox.mode` в `off`. Ходы Codex в code-mode по-прежнему ограничены Codex `workspace-write`, пока песочница OpenClaw активна; не монтируйте сокет Docker хоста в контейнеры песочницы агента.

Автоматизация / CI (неинтерактивный режим)

Отключите выделение Compose pseudo-TTY с помощью `-T`:

bashCopy code
[code]
    docker compose run -T --rm openclaw-cli gateway probedocker compose run -T --rm openclaw-cli devices list --json
[/code]

Примечание по безопасности общей сети

`openclaw-cli` использует `network_mode: "service:openclaw-gateway"`, чтобы команды CLI могли обращаться к gateway через `127.0.0.1`. Рассматривайте это как общую границу доверия. Конфигурация compose удаляет `NET_RAW`/`NET_ADMIN` и включает `no-new-privileges` как для `openclaw-gateway`, так и для `openclaw-cli`.

Сбои DNS Docker Desktop в openclaw-cli

В некоторых конфигурациях Docker Desktop DNS-запросы из sidecar-контейнера `openclaw-cli` с общей сетью завершаются ошибкой после удаления `NET_RAW`, что проявляется как `EAI_AGAIN` во время команд на основе npm, например `openclaw plugins install`. Оставляйте стандартный усиленный compose-файл для обычной работы gateway. Локальное переопределение ниже ослабляет профиль безопасности контейнера CLI, восстанавливая стандартные возможности Docker, поэтому используйте его только для одноразовой команды CLI, которой нужен доступ к реестру пакетов, а не как стандартный вызов Compose:

bashCopy code
[code]
    printf '%s\n' \  'services:' \  '  openclaw-cli:' \  '    cap_drop: !reset []' \  > docker-compose.cli-no-dropped-caps.local.yml docker compose -f docker-compose.yml -f docker-compose.cli-no-dropped-caps.local.yml run --rm openclaw-cli plugins install <package>
[/code]

Если вы уже создали долгоживущий контейнер `openclaw-cli`, пересоздайте его с тем же переопределением. `docker compose exec` и `docker exec` не могут изменить возможности Linux в уже созданном контейнере.

Разрешения и EACCES

Образ запускается от пользователя `node` (uid 1000). Если вы видите ошибки разрешений для `/home/node/.openclaw`, убедитесь, что ваши bind mount на хосте принадлежат uid 1000:

bashCopy code
[code]
    sudo chown -R 1000:1000 /path/to/openclaw-config /path/to/openclaw-workspace
[/code]

То же несоответствие может проявляться как предупреждение plugin, например `blocked plugin candidate: suspicious ownership (... uid=1000, expected uid=0 or root)` с последующим `plugin present but blocked`. Это означает, что uid процесса и владелец смонтированного каталога plugin не совпадают. Предпочтительно запускать контейнер от стандартного uid 1000 и исправить владельца bind mount. Выполняйте chown `/path/to/openclaw-config/npm` на `root:root` только если вы намеренно запускаете OpenClaw от root в долгосрочной перспективе.

Более быстрые пересборки

Упорядочьте Dockerfile так, чтобы слои зависимостей кэшировались. Это позволяет не запускать `pnpm install` повторно, пока lockfile не изменятся:

dockerfileCopy code
[code]
    FROM node:24-bookwormRUN curl -fsSL https://bun.sh/install | bashENV PATH="/root/.bun/bin:${PATH}"RUN corepack enableWORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scriptsRUN pnpm install --frozen-lockfileCOPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:buildENV NODE_ENV=productionCMD ["node","dist/index.js"]
[/code]

Параметры контейнера для опытных пользователей

Стандартный образ в первую очередь ориентирован на безопасность и запускается от непривилегированного пользователя `node`. Для более полнофункционального контейнера:

  1. **Сохраняйте`/home/node`**: `export OPENCLAW_HOME_VOLUME="openclaw_home"`
  2. **Встройте системные зависимости** : `export OPENCLAW_IMAGE_APT_PACKAGES="git curl jq"`
  3. **Встройте зависимости Python** : `export OPENCLAW_IMAGE_PIP_PACKAGES="requests==2.32.5 humanize==4.14.0"`
  4. **Встройте Playwright Chromium** : `export OPENCLAW_INSTALL_BROWSER=1`
  5. **Или установите браузеры Playwright в сохраняемый том** :bashCopy code
[code]docker compose run --rm openclaw-cli \  node /app/node_modules/playwright-core/cli.js install chromium
[/code]

  6. **Сохраняйте загрузки браузера** : используйте `OPENCLAW_HOME_VOLUME` или `OPENCLAW_EXTRA_MOUNTS`. OpenClaw автоматически обнаруживает управляемый Playwright Chromium из Docker-образа в Linux.

OpenAI Codex OAuth (безголовый Docker)

Если вы выберете OpenAI Codex OAuth в мастере, он откроет URL браузера. В Docker или безголовых окружениях скопируйте полный URL перенаправления, на который вы попали, и вставьте его обратно в мастер, чтобы завершить аутентификацию.

Метаданные базового образа

Основной Docker-образ среды выполнения использует `node:24-bookworm-slim` и включает `tini` как процесс инициализации точки входа (PID 1), чтобы процессы-зомби удалялись, а сигналы корректно обрабатывались в долгоживущих контейнерах. Он публикует аннотации базового OCI-образа, включая `org.opencontainers.image.base.name`, `org.opencontainers.image.source` и другие. Базовый digest Node обновляется через PR Dependabot для базового Docker-образа; релизные сборки не запускают слой обновления дистрибутива. См. [аннотации OCI-образов](<https://github.com/opencontainers/image-spec/blob/main/annotations.md>).

### Запуск на VPS?

См. [Hetzner (Docker VPS)](</ru/install/hetzner>) и [среду выполнения Docker VM](</ru/install/docker-vm-runtime>) для общих шагов развертывания VM, включая встраивание бинарных файлов, сохранение данных и обновления.

## Песочница агента

Когда `agents.defaults.sandbox` включен с бэкендом Docker, gateway запускает выполнение инструментов агента (shell, чтение/запись файлов и т. д.) внутри изолированных Docker-контейнеров, а сам gateway остается на хосте. Это дает жесткую границу вокруг недоверенных или многопользовательских сессий агентов без контейнеризации всего gateway.

Область песочницы может быть для каждого агента (по умолчанию), для каждой сессии или общей. Каждая область получает собственное рабочее пространство, смонтированное в `/workspace`. Также можно настроить политики разрешения/запрета инструментов, изоляцию сети, лимиты ресурсов и контейнеры браузера.

Полную конфигурацию, образы, заметки по безопасности и многоагентные профили см.:

  * [Песочница](</ru/gateway/sandboxing>) \-- полный справочник по песочнице
  * [OpenShell](</ru/gateway/openshell>) \-- интерактивный shell-доступ к контейнерам песочницы
  * [Многоагентная песочница и инструменты](</ru/tools/multi-agent-sandbox-tools>) \-- переопределения для каждого агента


### Быстрое включение

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main", // off | non-main | all        scope: "agent", // session | agent | shared      },    },  },}
[/code]

Соберите стандартный образ песочницы (из checkout исходников):

bashCopy code
[code]
    scripts/sandbox-setup.sh
[/code]

Для установок npm без checkout исходников см. [Песочница § Образы и настройка](</ru/gateway/sandboxing#images-and-setup>) для inline-команд `docker build`.

## Устранение неполадок

Образ отсутствует или контейнер песочницы не запускается

Соберите образ песочницы с помощью [`scripts/sandbox-setup.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/sandbox-setup.sh>) (checkout исходников) или inline-команды `docker build` из [Песочница § Образы и настройка](</ru/gateway/sandboxing#images-and-setup>) (установка npm), либо задайте `agents.defaults.sandbox.docker.image` для своего пользовательского образа. Контейнеры автоматически создаются для каждой сессии по требованию.

Ошибки разрешений в песочнице

Установите `docker.user` в UID:GID, соответствующий владельцу смонтированного рабочего пространства, или выполните chown для папки рабочего пространства.

Пользовательские инструменты не найдены в песочнице

OpenClaw запускает команды через `sh -lc` (login shell), который загружает `/etc/profile` и может сбросить PATH. Установите `docker.env.PATH`, чтобы добавить ваши пути пользовательских инструментов в начало, или добавьте скрипт в `/etc/profile.d/` в вашем Dockerfile.

OOM-killed во время сборки образа (exit 137)

VM требуется как минимум 2 ГБ RAM. Используйте более крупный класс машины и повторите попытку.

Требуется авторизация или сопряжение в Control UI

Получите свежую ссылку на dashboard и одобрите устройство браузера:

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-opendocker compose run --rm openclaw-cli devices listdocker compose run --rm openclaw-cli devices approve <requestId>
[/code]

Подробнее: [Dashboard](</ru/web/dashboard>), [Устройства](</ru/cli/devices>).

Цель Gateway показывает ws://172.x.x.x или ошибки сопряжения из Docker CLI

Сбросьте режим gateway и привязку:

bashCopy code
[code]
    docker compose run --rm openclaw-cli config set --batch-json '[{"path":"gateway.mode","value":"local"},{"path":"gateway.bind","value":"lan"}]'docker compose run --rm openclaw-cli devices list --url ws://127.0.0.1:18789
[/code]

## Связанные материалы

  * [Обзор установки](</ru/install>) — все способы установки
  * [Podman](</ru/install/podman>) — альтернатива Docker на базе Podman
  * [ClawDock](</ru/install/clawdock>) — настройка Docker Compose от сообщества
  * [Обновление](</ru/install/updating>) — поддержание OpenClaw в актуальном состоянии
  * [Конфигурация](</ru/gateway/configuration>) — конфигурация gateway после установки


Was this useful?YesNo

Open issue