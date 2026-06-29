---
title: Руководство по эксплуатации Gateway
source_url: https://docs.openclaw.ai/ru/gateway
scraped_at: 2026-06-29
---

Gateway & OpsGateway

Используйте эту страницу для запуска сервиса Gateway в первый день и эксплуатации во второй день.

[**Deep troubleshooting** Диагностика от симптомов с точными цепочками команд и сигнатурами логов. ](</ru/gateway/troubleshooting>) [**Configuration** Руководство по настройке, ориентированное на задачи, и полный справочник конфигурации. ](</ru/gateway/configuration>) [**Secrets management** Контракт SecretRef, поведение снимка во время выполнения и операции миграции/перезагрузки. ](</ru/gateway/secrets>) [**Secrets plan contract** Точные правила цели/пути `secrets apply` и поведение профиля аутентификации только по ссылкам. ](</ru/gateway/secrets-plan-contract>)

## Локальный запуск за 5 минут

* ### Start the Gateway

bashCopy code
[code]
    openclaw gateway --port 18789# debug/trace mirrored to stdioopenclaw gateway --port 18789 --verbose# force-kill listener on selected port, then startopenclaw gateway --force
[/code]

* ### Verify service health

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --follow
[/code]

Базовое исправное состояние: `Runtime: running`, `Connectivity probe: ok` и `Capability: ...`, соответствующий ожидаемому. Используйте `openclaw gateway status --require-rpc`, когда нужно подтверждение RPC с областью чтения, а не только доступность.

* ### Validate channel readiness

bashCopy code
[code]
    openclaw channels status --probe
[/code]

При доступном gateway это запускает живые проверки каналов для каждой учетной записи и дополнительные аудиты. Если gateway недоступен, CLI вместо вывода живой проверки возвращается к сводкам каналов только из конфигурации.

## Модель времени выполнения

  * Один постоянно работающий процесс для маршрутизации, плоскости управления и подключений каналов.
  * Один мультиплексированный порт для: 
    * Управления/RPC по WebSocket
    * HTTP API (`/v1/models`, `/v1/embeddings`, `/v1/chat/completions`, `/v1/responses`, `/tools/invoke`)
    * HTTP-маршрутов Plugin, например необязательного `/api/v1/admin/rpc`
    * Control UI и хуков
  * Режим привязки по умолчанию: `loopback`.
  * По умолчанию требуется аутентификация. Настройки с общим секретом используют `gateway.auth.token` / `gateway.auth.password` (или `OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD`), а настройки reverse proxy не для loopback могут использовать `gateway.auth.mode: "trusted-proxy"`.


## OpenAI-совместимые конечные точки

Самая важная поверхность совместимости OpenClaw теперь:

  * `GET /v1/models`
  * `GET /v1/models/{id}`
  * `POST /v1/embeddings`
  * `POST /v1/chat/completions`
  * `POST /v1/responses`


Почему этот набор важен:

  * Большинство интеграций Open WebUI, LobeChat и LibreChat сначала проверяют `/v1/models`.
  * Многие конвейеры RAG и памяти ожидают `/v1/embeddings`.
  * Клиенты, ориентированные на агентов, все чаще предпочитают `/v1/responses`.


Примечание по планированию:

  * `/v1/models` ориентирован на агентов: он возвращает `openclaw`, `openclaw/default` и `openclaw/<agentId>`.
  * `openclaw/default` — стабильный псевдоним, который всегда сопоставляется с настроенным агентом по умолчанию.
  * Используйте `x-openclaw-model`, когда нужно переопределить backend-провайдера/модель; иначе обычная модель и настройка embeddings выбранного агента остаются управляющими.


Все эти конечные точки работают на основном порту Gateway и используют ту же доверенную границу аутентификации оператора, что и остальная HTTP API Gateway.

Административный HTTP RPC (`POST /api/v1/admin/rpc`) — это отдельный, по умолчанию отключенный маршрут Plugin для инструментов хоста, которые не могут использовать WebSocket RPC. См. [Административный HTTP RPC](</ru/plugins/admin-http-rpc>).

### Приоритет порта и привязки

Параметр | Порядок разрешения  
---|---  
Порт Gateway | `--port` → `OPENCLAW_GATEWAY_PORT` → `gateway.port` → `18789`  
Режим привязки | CLI/переопределение → `gateway.bind` → `loopback`  
  
Установленные сервисы gateway записывают разрешенный `--port` в метаданные supervisor. После изменения `gateway.port` запустите `openclaw doctor --fix` или `openclaw gateway install --force`, чтобы launchd/systemd/schtasks запускали процесс на новом порту.

Запуск Gateway использует тот же эффективный порт и привязку, когда подготавливает локальные источники Control UI для привязок не к loopback. Например, `--bind lan --port 3000` подготавливает `http://localhost:3000` и `http://127.0.0.1:3000` перед выполнением runtime-проверки. Явно добавьте любые удаленные источники браузера, например HTTPS proxy URL, в `gateway.controlUi.allowedOrigins`.

### Режимы горячей перезагрузки

`gateway.reload.mode` | Поведение  
---|---  
`off` | Без перезагрузки конфигурации  
`hot` | Применять только изменения, безопасные для hot-режима  
`restart` | Перезапускать при изменениях, требующих перезапуска  
`hybrid` (по умолчанию) | Применять hot-режим, когда безопасно, перезапускать, когда требуется  
  
## Набор команд оператора

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --deep   # adds a system-level service scanopenclaw gateway status --jsonopenclaw gateway installopenclaw gateway restartopenclaw gateway stopopenclaw secrets reloadopenclaw logs --followopenclaw doctor
[/code]

`gateway status --deep` предназначен для дополнительного обнаружения сервисов (LaunchDaemons/systemd system units/schtasks), а не для более глубокой проверки здоровья RPC.

## Несколько gateway на одном хосте

В большинстве установок следует запускать один gateway на машину. Один gateway может размещать несколько агентов и каналов.

Несколько gateway нужны только тогда, когда вы намеренно хотите изоляцию или rescue bot.

Полезные проверки:

bashCopy code
[code]
    openclaw gateway status --deepopenclaw gateway probe
[/code]

Чего ожидать:

  * `gateway status --deep` может сообщить `Other gateway-like services detected (best effort)` и вывести подсказки по очистке, когда устаревшие установки launchd/systemd/schtasks все еще присутствуют.
  * `gateway probe` может предупредить о `multiple reachable gateway identities`, когда отвечают разные gateway или когда OpenClaw не может доказать, что достижимые цели являются одним и тем же gateway. SSH-туннель, proxy URL или настроенный удаленный URL к тому же gateway — это один gateway с несколькими транспортами, даже если порты транспортов различаются.
  * Если это намеренно, изолируйте порты, конфигурацию/состояние и корни рабочих областей для каждого gateway.


Чеклист для каждого экземпляра:

  * Уникальный `gateway.port`
  * Уникальный `OPENCLAW_CONFIG_PATH`
  * Уникальный `OPENCLAW_STATE_DIR`
  * Уникальный `agents.defaults.workspace`


Пример:

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/a.json OPENCLAW_STATE_DIR=~/.openclaw-a openclaw gateway --port 19001OPENCLAW_CONFIG_PATH=~/.openclaw/b.json OPENCLAW_STATE_DIR=~/.openclaw-b openclaw gateway --port 19002
[/code]

Подробная настройка: [/gateway/multiple-gateways](</ru/gateway/multiple-gateways>).

## Удаленный доступ

Предпочтительно: Tailscale/VPN. Резервный вариант: SSH-туннель.

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@host
[/code]

Затем подключайте клиентов локально к `ws://127.0.0.1:18789`.

См.: [Удаленный Gateway](</ru/gateway/remote>), [Аутентификация](</ru/gateway/authentication>), [Tailscale](</ru/gateway/tailscale>).

## Надзор и жизненный цикл сервиса

Используйте запуск под надзором для надежности, похожей на production.

### macOS (launchd)

bashCopy code
[code]
    openclaw gateway installopenclaw gateway statusopenclaw gateway restartopenclaw gateway stop
[/code]

Используйте `openclaw gateway restart` для перезапусков. Не объединяйте `openclaw gateway stop` и `openclaw gateway start` как замену перезапуску.

В macOS `gateway stop` по умолчанию использует `launchctl bootout` — это удаляет LaunchAgent из текущей загрузочной сессии без постоянного отключения, поэтому автоматическое восстановление KeepAlive все еще работает после неожиданных сбоев, а `gateway start` повторно включает его чисто. Чтобы постоянно подавить автоматический повторный запуск между перезагрузками, передайте `--disable`: `openclaw gateway stop --disable`.

Метки LaunchAgent: `ai.openclaw.gateway` (по умолчанию) или `ai.openclaw.<profile>` (именованный профиль). `openclaw doctor` проверяет и исправляет дрейф конфигурации сервиса.

### Linux (systemd user)

bashCopy code
[code]
    openclaw gateway installsystemctl --user enable --now openclaw-gateway[-<profile>].serviceopenclaw gateway status
[/code]

Для сохранения работы после выхода из системы включите lingering:

bashCopy code
[code]
    sudo loginctl enable-linger <user>
[/code]

Пример пользовательского unit вручную, когда нужен пользовательский путь установки:

iniCopy code
[code]
    [Unit]Description=OpenClaw GatewayAfter=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143OOMPolicy=continueKillMode=control-group [Install]WantedBy=default.target
[/code]

### Windows (native)

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --jsonopenclaw gateway restartopenclaw gateway stop
[/code]

Управляемый нативный запуск Windows использует Scheduled Task с именем `OpenClaw Gateway` (или `OpenClaw Gateway (<profile>)` для именованных профилей). Если создание Scheduled Task запрещено, OpenClaw возвращается к launcher в папке автозагрузки текущего пользователя, который указывает на `gateway.cmd` внутри каталога состояния.

### Linux (system service)

Используйте системный unit для много пользовательских/постоянно включенных хостов.

bashCopy code
[code]
    sudo systemctl daemon-reloadsudo systemctl enable --now openclaw-gateway[-<profile>].service
[/code]

Используйте то же тело сервиса, что и для пользовательского unit, но установите его в `/etc/systemd/system/openclaw-gateway[-<profile>].service` и настройте `ExecStart=`, если ваш бинарный файл `openclaw` находится в другом месте.

Не позволяйте также `openclaw doctor --fix` устанавливать gateway-сервис уровня пользователя для того же профиля/порта. Doctor отказывается от такой автоматической установки, когда находит системный сервис OpenClaw gateway; используйте `OPENCLAW_SERVICE_REPAIR_POLICY=external`, когда системный unit владеет жизненным циклом.

## Быстрый путь dev-профиля

bashCopy code
[code]
    openclaw --dev setupopenclaw --dev gateway --allow-unconfiguredopenclaw --dev status
[/code]

Значения по умолчанию включают изолированные состояние/конфигурацию и базовый порт gateway `19001`.

## Краткий справочник протокола (вид оператора)

  * Первый кадр клиента должен быть `connect`.
  * Gateway возвращает снимок `hello-ok` (`presence`, `health`, `stateVersion`, `uptimeMs`, limits/policy).
  * `hello-ok.features.methods` / `events` — это консервативный список обнаружения, а не сгенерированный дамп каждого вызываемого вспомогательного маршрута.
  * Запросы: `req(method, params)` → `res(ok/payload|error)`.
  * Частые события включают `connect.challenge`, `agent`, `chat`, `session.message`, `session.operation`, `session.tool`, `sessions.changed`, `presence`, `tick`, `health`, `heartbeat`, события жизненного цикла сопряжения/одобрения и `shutdown`.


Запуски агента двухэтапные:

  1. Немедленное подтверждение принятия (`status:"accepted"`)
  2. Итоговый ответ завершения (`status:"ok"|"error"`) с потоковыми событиями `agent` между ними.


См. полную документацию протокола: [Протокол Gateway](</ru/gateway/protocol>).

## Операционные проверки

### Работоспособность

  * Откройте WS и отправьте `connect`.
  * Ожидайте ответ `hello-ok` со снимком.


### Готовность

bashCopy code
[code]
    openclaw gateway statusopenclaw channels status --probeopenclaw health
[/code]

### Восстановление после пропусков

События не воспроизводятся повторно. При пропусках последовательности обновите состояние (`health`, `system-presence`) перед продолжением.

## Частые сигнатуры отказов

Сигнатура | Вероятная проблема  
---|---  
`refusing to bind gateway ... without auth` | Привязка не к интерфейсу обратной петли без действительного пути аутентификации Gateway  
`another gateway instance is already listening` / `EADDRINUSE` | Конфликт порта  
`Gateway start blocked: set gateway.mode=local` | В конфигурации задан удаленный режим, или в поврежденной конфигурации отсутствует метка локального режима  
`unauthorized` during connect | Несоответствие аутентификации между клиентом и Gateway  
  
Для полных цепочек диагностики используйте [Устранение неполадок Gateway](</ru/gateway/troubleshooting>).

## Гарантии безопасности

  * Клиенты протокола Gateway быстро завершаются с ошибкой, когда Gateway недоступен (без неявного отката к прямому каналу).
  * Недопустимые или не являющиеся подключением первые кадры отклоняются и закрываются.
  * Корректное завершение работы отправляет событие `shutdown` перед закрытием сокета.


* * *

Связанные разделы:

  * [Устранение неполадок](</ru/gateway/troubleshooting>)
  * [Фоновый процесс](</ru/gateway/background-process>)
  * [Конфигурация](</ru/gateway/configuration>)
  * [Состояние](</ru/gateway/health>)
  * [Doctor](</ru/gateway/doctor>)
  * [Аутентификация](</ru/gateway/authentication>)


## Связанные разделы

  * [Конфигурация](</ru/gateway/configuration>)
  * [Устранение неполадок Gateway](</ru/gateway/troubleshooting>)
  * [Удаленный доступ](</ru/gateway/remote>)
  * [Управление секретами](</ru/gateway/secrets>)


Was this useful?YesNo

Open issue