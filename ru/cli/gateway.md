---
title: Gateway
source_url: https://docs.openclaw.ai/ru/cli/gateway
scraped_at: 2026-06-29
---

ReferenceCLI commands

Gateway — это WebSocket-сервер OpenClaw (каналы, узлы, сессии, хуки). Подкоманды на этой странице находятся в `openclaw gateway …`.

[**Обнаружение Bonjour** Настройка локального mDNS + глобального DNS-SD. ](</ru/gateway/bonjour>) [**Обзор обнаружения** Как OpenClaw объявляет и находит шлюзы. ](</ru/gateway/discovery>) [**Конфигурация** Ключи конфигурации Gateway верхнего уровня. ](</ru/gateway/configuration>)

## Запуск Gateway

Запустите локальный процесс Gateway:

bashCopy code
[code]
    openclaw gateway
[/code]

Алиас для запуска на переднем плане:

bashCopy code
[code]
    openclaw gateway run
[/code]

Поведение при запуске

  * По умолчанию Gateway отказывается запускаться, если в `~/.openclaw/openclaw.json` не задано `gateway.mode=local`. Используйте `--allow-unconfigured` для разовых запусков или запусков в разработке.
  * Ожидается, что `openclaw onboard --mode local` и `openclaw setup` запишут `gateway.mode=local`. Если файл существует, но `gateway.mode` отсутствует, считайте это поврежденной или перезаписанной конфигурацией и исправьте ее, вместо того чтобы неявно предполагать локальный режим.
  * Если файл существует, а `gateway.mode` отсутствует, Gateway считает это подозрительным повреждением конфигурации и отказывается «угадывать local» за вас.
  * Привязка за пределами loopback без аутентификации блокируется (защитное ограничение).
  * `lan`, `tailnet` и `custom` сейчас разрешаются через BYOH-пути только IPv4.
  * BYOH только с IPv6 сейчас нативно не поддерживается на этом пути. Используйте IPv4-sidecar или прокси, если сам хост работает только с IPv6.
  * `SIGUSR1` запускает внутрипроцессный перезапуск, когда это разрешено (`commands.restart` включен по умолчанию; задайте `commands.restart: false`, чтобы заблокировать ручной перезапуск, при этом применение/обновление через инструмент или конфигурацию gateway остается разрешенным).
  * Обработчики `SIGINT`/`SIGTERM` останавливают процесс Gateway, но не восстанавливают какое-либо пользовательское состояние терминала. Если вы оборачиваете CLI с помощью TUI или ввода в raw-режиме, восстановите терминал перед выходом.


### Параметры

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> WebSocket-порт (значение по умолчанию берется из конфигурации/env; обычно `18789`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tYmluZCA8bG9vcGJhY2t8bGFufHRhaWxuZXR8YXV0b3xjdXN0b20 " type="string"> Режим привязки слушателя. `lan`, `tailnet` и `custom` сейчас разрешаются через пути только IPv4.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdG9rZW4gPHRva2Vu " type="string"> Переопределение токена (также задает `OPENCLAW_GATEWAY_TOKEN` для процесса).

Сбрасывать конфигурацию Tailscale serve/funnel при завершении работы.

На сегодня ожидается IPv4-адрес. Для BYOH только с IPv6 разместите IPv4-sidecar или прокси перед Gateway и укажите OpenClaw этот IPv4 endpoint.

Разрешить запуск gateway без `gateway.mode=local` в конфигурации. Обходит защиту запуска только для разовой/dev-начальной настройки; не записывает и не исправляет файл конфигурации.

Создать dev-конфигурацию + workspace, если они отсутствуют (пропускает BOOTSTRAP.md).

Сбросить dev-конфигурацию + учетные данные + сессии + workspace (требует `--dev`).

Завершить любой существующий слушатель на выбранном порту перед запуском.

Подробные логи.

Показывать в консоли только логи backend CLI (и включить stdout/stderr).

Алиас для `--ws-log compact`.

Логировать сырые события потока модели в jsonl.

## Перезапуск Gateway

bashCopy code
[code]
    openclaw gateway restartopenclaw gateway restart --safeopenclaw gateway restart --safe --skip-deferralopenclaw gateway restart --force
[/code]

`openclaw gateway restart --safe` просит работающий Gateway выполнить предварительную проверку активной работы OpenClaw перед перезапуском. Если активны операции в очереди, доставка ответов, встроенные запуски или запуски задач, Gateway сообщает о блокерах, объединяет повторяющиеся запросы безопасного перезапуска и перезапускается после завершения активной работы. Обычный `restart` сохраняет существующее поведение менеджера служб для совместимости. Используйте `--force` только тогда, когда вам явно нужен путь немедленного принудительного переопределения.

`openclaw gateway restart --safe --skip-deferral` выполняет тот же скоординированный перезапуск с учетом OpenClaw, что и `--safe`, но обходит gate отсрочки активной работы, поэтому Gateway немедленно выдает перезапуск даже при сообщенных блокерах. Используйте это как аварийный выход оператора, когда отсрочка закреплена зависшим запуском задачи и один только `--safe` ждал бы бесконечно. `--skip-deferral` требует `--safe`.

### Профилирование Gateway

  * Задайте `OPENCLAW_GATEWAY_STARTUP_TRACE=1`, чтобы логировать тайминги фаз при запуске Gateway, включая задержку `eventLoopMax` по фазам и тайминги таблиц поиска плагинов для installed-index, registry манифестов, планирования запуска и работы owner-map.
  * Задайте `OPENCLAW_GATEWAY_RESTART_TRACE=1`, чтобы логировать строки `restart trace:` в рамках перезапуска для обработки сигнала перезапуска, ожидания завершения активной работы, фаз завершения, следующего запуска, тайминга готовности и метрик памяти.
  * Задайте `OPENCLAW_DIAGNOSTICS=timeline` с `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=<path>`, чтобы записывать best-effort JSONL-таймлайн диагностики запуска для внешних QA harnesses. Также можно включить флаг через `diagnostics.flags: ["timeline"]` в конфигурации; путь по-прежнему предоставляется через env. Добавьте `OPENCLAW_DIAGNOSTICS_EVENT_LOOP=1`, чтобы включить выборки event-loop.
  * Сначала выполните `pnpm build`, затем `pnpm test:startup:gateway -- --runs 5 --warmup 1`, чтобы измерить запуск Gateway относительно собранной точки входа CLI. Бенчмарк записывает первый вывод процесса, `/healthz`, `/readyz`, тайминги startup trace, задержку event-loop и подробности таймингов таблиц поиска плагинов.
  * Сначала выполните `pnpm build`, затем `pnpm test:restart:gateway -- --case skipChannels --runs 1 --restarts 5`, чтобы измерить внутрипроцессный перезапуск Gateway относительно собранной точки входа CLI на macOS или Linux. Бенчмарк перезапуска использует SIGUSR1, включает в дочернем процессе и startup, и restart traces, а также записывает следующие `/healthz`, `/readyz`, downtime, тайминг готовности, CPU, RSS и метрики restart trace.
  * Считайте `/healthz` проверкой живости, а `/readyz` — пригодной готовностью. Строки трассировки и вывод бенчмарка предназначены для атрибуции владельцу; не считайте один интервал трассировки или одну выборку полноценным выводом о производительности.


## Запрос к работающему Gateway

Все команды запросов используют WebSocket RPC.

### Режимы вывода

  * По умолчанию: человекочитаемый (цветной в TTY).
  * `--json`: машиночитаемый JSON (без стилизации/спиннера).
  * `--no-color` (или `NO_COLOR=1`): отключить ANSI, сохранив человекочитаемую компоновку.


### Общие параметры

  * `--url <url>`: WebSocket URL Gateway.
  * `--token <token>`: токен Gateway.
  * `--password <password>`: пароль Gateway.
  * `--timeout <ms>`: timeout/бюджет (зависит от команды).
  * `--expect-final`: ждать «final» response (вызовы агента).


### `gateway health`

bashCopy code
[code]
    openclaw gateway health --url ws://127.0.0.1:18789openclaw gateway health --port 18789
[/code]

HTTP endpoint `/healthz` — это liveness probe: он возвращает ответ, когда сервер может отвечать по HTTP. HTTP endpoint `/readyz` строже и остается красным, пока startup sidecars плагинов, каналы или настроенные хуки еще стабилизируются. Локальные или аутентифицированные подробные ответы готовности включают диагностический блок `eventLoop` с задержкой event-loop, утилизацией event-loop, соотношением ядер CPU и флагом `degraded`.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> Нацелиться на локальный local loopback Gateway на этом порту. Это переопределяет `OPENCLAW_GATEWAY_URL` и `OPENCLAW_GATEWAY_PORT` для вызова health.

### `gateway usage-cost`

Получить сводки usage-cost из логов сессий.

bashCopy code
[code]
    openclaw gateway usage-costopenclaw gateway usage-cost --days 7openclaw gateway usage-cost --agent work --jsonopenclaw gateway usage-cost --all-agentsopenclaw gateway usage-cost --json
[/code]

Агрегировать сводку расходов по всем настроенным агентам. Нельзя сочетать с `--agent`.

### `gateway stability`

Получить недавние данные регистратора диагностической стабильности из работающего Gateway.

bashCopy code
[code]
    openclaw gateway stabilityopenclaw gateway stability --type payload.largeopenclaw gateway stability --bundle latestopenclaw gateway stability --bundle latest --exportopenclaw gateway stability --json
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tbGltaXQgPGxpbWl0 " type="number" default="25"> Максимальное количество недавних событий для включения (максимум `1000`).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tdHlwZSA8dHlwZQ " type="string"> Фильтровать по типу диагностического события, например `payload.large` или `diagnostic.memory.pressure`.

Читать сохраненный bundle стабильности вместо вызова работающего Gateway. Используйте `--bundle latest` (или просто `--bundle`) для новейшего bundle в каталоге состояния либо передайте путь к bundle JSON напрямую.

Записать общий zip-файл диагностики поддержки вместо вывода сведений о стабильности.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tb3V0cHV0IDxwYXRo " type="string"> Путь вывода для `--export`.

Конфиденциальность и поведение bundle

  * Записи хранят операционные метаданные: имена событий, счетчики, размеры в байтах, показания памяти, состояние очередей/сессий, имена каналов/плагинов и отредактированные сводки сессий. Они не хранят текст чата, тела webhook, выводы инструментов, сырые тела запросов или ответов, токены, cookies, секретные значения, имена хостов или сырые id сессий. Задайте `diagnostics.enabled: false`, чтобы полностью отключить регистратор.
  * При фатальных завершениях Gateway, таймаутах завершения и сбоях запуска после перезапуска OpenClaw записывает тот же диагностический snapshot в `~/.openclaw/logs/stability/openclaw-stability-*.json`, когда у регистратора есть события. Изучите новейший bundle с помощью `openclaw gateway stability --bundle latest`; `--limit`, `--type` и `--since-seq` также применяются к выводу bundle.


### `gateway diagnostics export`

Записать локальный zip диагностики, предназначенный для прикрепления к отчетам об ошибках. О модели конфиденциальности и содержимом bundle см. [Экспорт диагностики](</ru/gateway/diagnostics>).

bashCopy code
[code]
    openclaw gateway diagnostics exportopenclaw gateway diagnostics export --output openclaw-diagnostics.zipopenclaw gateway diagnostics export --json
[/code]

Пропустить поиск сохраненного пакета стабильности.

Вывести записанный путь, размер и манифест в формате JSON.

Экспорт содержит манифест, сводку Markdown, форму конфигурации, очищенные сведения о конфигурации, очищенные сводки журналов, очищенные снимки состояния/работоспособности Gateway и самый новый пакет стабильности, если он существует.

Он предназначен для передачи другим. Он сохраняет операционные сведения, которые помогают при отладке, такие как безопасные поля журналов OpenClaw, имена подсистем, коды состояния, длительности, настроенные режимы, порты, идентификаторы plugin, идентификаторы провайдеров, несекретные настройки функций и отредактированные операционные сообщения журналов. Он пропускает или редактирует текст чатов, тела webhook, вывод инструментов, учетные данные, cookie, идентификаторы учетных записей/сообщений, текст промптов/инструкций, имена хостов и секретные значения. Когда сообщение в стиле LogTape похоже на текст пользовательской/чатовой/инструментальной полезной нагрузки, экспорт сохраняет только факт, что сообщение было пропущено, и количество его байтов.

### `gateway status`

`gateway status` показывает службу Gateway (launchd/systemd/schtasks) и необязательную проверку возможности подключения/аутентификации.

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --jsonopenclaw gateway status --require-rpc
[/code]

Пропустить проверку подключения (представление только службы).

Также сканировать службы системного уровня.

Повысить проверку подключения по умолчанию до проверки чтения и завершить работу с ненулевым кодом, если эта проверка чтения не пройдет. Нельзя сочетать с `--no-probe`.

Status semantics

  * `gateway status` остается доступной для диагностики, даже если локальная конфигурация CLI отсутствует или недействительна.
  * `gateway status` по умолчанию подтверждает состояние службы, подключение WebSocket и возможность аутентификации, видимую во время рукопожатия. Она не подтверждает операции чтения/записи/администрирования.
  * Диагностические проверки не изменяют состояние при первичной аутентификации устройства: они повторно используют существующий кэшированный токен устройства, если он есть, но не создают новую идентичность устройства CLI или запись связывания устройства только для чтения только для проверки состояния.
  * `gateway status` по возможности разрешает настроенные SecretRefs аутентификации для аутентификации проверки.
  * Если требуемый SecretRef аутентификации не разрешен в этом пути команды, `gateway status --json` сообщает `rpc.authWarning`, когда проверка подключения/аутентификации не проходит; передайте `--token`/`--password` явно или сначала разрешите источник секрета.
  * Если проверка проходит успешно, предупреждения о неразрешенных ссылках аутентификации подавляются, чтобы избежать ложных срабатываний.
  * Когда проверка включена, вывод JSON включает `gateway.version`, если запущенный Gateway сообщает ее; `--require-rpc` может откатиться к полезной нагрузке RPC `status.runtimeVersion`, если последующая проверка рукопожатия не может предоставить метаданные версии.
  * Используйте `--require-rpc` в скриптах и автоматизации, когда прослушивающей службы недостаточно и требуется, чтобы RPC-вызовы с областью чтения тоже были работоспособны.
  * `--deep` добавляет best-effort-сканирование дополнительных установок launchd/systemd/schtasks. Когда обнаружено несколько служб, похожих на gateway, человекочитаемый вывод печатает подсказки по очистке и предупреждает, что в большинстве установок должен выполняться один gateway на машину.
  * `--deep` также сообщает о недавней передаче перезапуска супервизора Gateway, когда процесс службы завершился корректно для внешнего перезапуска супервизором.
  * `--deep` запускает проверку конфигурации в режиме с учетом plugin (`pluginValidation: "full"`) и показывает предупреждения настроенного манифеста plugin (например, отсутствующие метаданные конфигурации канала), чтобы smoke-проверки установки и обновления их ловили. `gateway status` по умолчанию сохраняет быстрый путь только для чтения, который пропускает проверку plugin.
  * Человекочитаемый вывод включает разрешенный путь к файловому журналу, а также снимок путей/действительности конфигурации CLI и службы, чтобы помочь диагностировать расхождение профиля или каталога состояния.

Linux systemd auth-drift checks

  * В установках Linux systemd проверки расхождения аутентификации службы читают значения `Environment=` и `EnvironmentFile=` из unit (включая `%h`, пути в кавычках, несколько файлов и необязательные файлы `-`).
  * Проверки расхождения разрешают SecretRefs `gateway.auth.token` с использованием объединенного runtime-окружения (сначала окружение команды службы, затем резервно окружение процесса).
  * Если аутентификация токеном фактически не активна (явный `gateway.auth.mode` со значением `password`/`none`/`trusted-proxy` или режим не задан, когда пароль может иметь приоритет и ни один кандидат токена не может иметь приоритет), проверки расхождения токена пропускают разрешение токена конфигурации.


### `gateway probe`

`gateway probe` — это команда «отладить все». Она всегда проверяет:

  * ваш настроенный удаленный gateway (если задан), и
  * localhost (loopback) **даже если удаленная цель настроена**.


Если передать `--url`, эта явная цель добавляется перед ними. Человекочитаемый вывод помечает цели так:

  * `URL (explicit)`
  * `Remote (configured)` или `Remote (configured, inactive)`
  * `Local loopback`

bashCopy code
[code]
    openclaw gateway probeopenclaw gateway probe --jsonopenclaw gateway probe --port 18789
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcG9ydCA8cG9ydA " type="number"> Использовать этот порт для цели проверки local loopback и удаленного порта SSH-туннеля. Без `--url` это выбирает цель local loopback вместо настроенного URL окружения gateway, порта окружения или удаленных целей.

Interpretation

  * `Reachable: yes` означает, что как минимум одна цель приняла подключение WebSocket.
  * `Capability: read-only|write-capable|admin-capable|pairing-pending|connect-only` сообщает, что проверка смогла подтвердить об аутентификации. Это отдельно от достижимости.
  * `Read probe: ok` означает, что подробные RPC-вызовы с областью чтения (`health`/`status`/`system-presence`/`config.get`) также прошли успешно.
  * `Read probe: limited - missing scope: operator.read` означает, что подключение прошло успешно, но RPC с областью чтения ограничен. Это сообщается как **деградировавшая** достижимость, а не полный сбой.
  * `Read probe: failed` после `Connect: ok` означает, что Gateway принял подключение WebSocket, но последующая диагностика чтения истекла по тайм-ауту или завершилась ошибкой. Это также **деградировавшая** достижимость, а не недостижимый Gateway.
  * Как и `gateway status`, проверка повторно использует существующую кэшированную аутентификацию устройства, но не создает первичную идентичность устройства или состояние связывания.
  * Код выхода ненулевой только когда ни одна проверенная цель недостижима.

JSON output

Верхний уровень:

  * `ok`: как минимум одна цель достижима.
  * `degraded`: как минимум одна цель приняла подключение, но не завершила полную подробную RPC-диагностику.
  * `capability`: лучшая возможность, увиденная среди достижимых целей (`read_only`, `write_capable`, `admin_capable`, `pairing_pending`, `connected_no_operator_scope` или `unknown`).
  * `primaryTargetId`: лучшая цель, которую следует считать активным победителем, в таком порядке: явный URL, SSH-туннель, настроенная удаленная цель, затем local loopback.
  * `warnings[]`: best-effort-записи предупреждений с `code`, `message` и необязательными `targetIds`.
  * `network`: подсказки URL local loopback/tailnet, выведенные из текущей конфигурации и сетевых настроек хоста.
  * `discovery.timeoutMs` и `discovery.count`: фактический бюджет обнаружения/количество результатов, использованные для этого прохода проверки.


Для каждой цели (`targets[].connect`):

  * `ok`: достижимость после подключения + классификация деградации.
  * `rpcOk`: полный успех подробного RPC.
  * `scopeLimited`: подробный RPC завершился неудачно из-за отсутствующей области оператора.


Для каждой цели (`targets[].auth`):

  * `role`: роль аутентификации, сообщенная в `hello-ok`, когда доступна.
  * `scopes`: предоставленные области, сообщенные в `hello-ok`, когда доступны.
  * `capability`: показанная классификация возможности аутентификации для этой цели.

Common warning codes

  * `ssh_tunnel_failed`: настройка SSH-туннеля завершилась неудачно; команда вернулась к прямым проверкам.
  * `multiple_gateways`: были достижимы отдельные идентичности gateway, или OpenClaw не смог подтвердить, что достижимые цели являются одним и тем же gateway. SSH-туннель, URL proxy или настроенный удаленный URL к тому же gateway не вызывает это предупреждение.
  * `auth_secretref_unresolved`: настроенный SecretRef аутентификации не удалось разрешить для неудачной цели.
  * `probe_scope_limited`: подключение WebSocket прошло успешно, но проверка чтения была ограничена отсутствующей `operator.read`.


#### Удаленный доступ через SSH (паритет с приложением Mac)

Режим приложения macOS «Remote over SSH» использует локальную переадресацию порта, чтобы удаленный gateway (который может быть привязан только к loopback) стал доступен по `ws://127.0.0.1:<port>`.

Эквивалент CLI:

bashCopy code
[code]
    openclaw gateway probe --ssh user@gateway-host
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc3NoIDx0YXJnZXQ " type="string"> `user@host` или `user@host:port` (порт по умолчанию `22`).

Выбрать первый обнаруженный хост gateway в качестве цели SSH из разрешенной конечной точки обнаружения (`local.` плюс настроенный глобальный домен, если есть). Подсказки только TXT игнорируются.

Конфигурация (необязательно, используется как значения по умолчанию):

  * `gateway.remote.sshTarget`
  * `gateway.remote.sshIdentity`


### `gateway call <method>`

Низкоуровневый помощник RPC.

bashCopy code
[code]
    openclaw gateway call statusopenclaw gateway call logs.tail --params '{"sinceMs": 60000}'
[/code]

В основном для RPC в стиле агентов, которые перед финальной полезной нагрузкой транслируют промежуточные события.

Машиночитаемый вывод JSON.

## Управление службой Gateway

bashCopy code
[code]
    openclaw gateway installopenclaw gateway startopenclaw gateway stopopenclaw gateway restartopenclaw gateway uninstall
[/code]

### Установка с оберткой

Используйте `--wrapper`, когда управляемый сервис должен запускаться через другой исполняемый файл, например через прослойку менеджера секретов или помощник запуска от другого пользователя. Обертка получает обычные аргументы Gateway и отвечает за то, чтобы в итоге выполнить `openclaw` или Node с этими аргументами.

bashCopy code
[code]
    cat > ~/.local/bin/openclaw-doppler <<'EOF'#!/usr/bin/env bashset -euo pipefailexec doppler run --project my-project --config production -- openclaw "$@"EOFchmod +x ~/.local/bin/openclaw-doppler openclaw gateway install --wrapper ~/.local/bin/openclaw-doppler --forceopenclaw gateway restart
[/code]

Также можно задать обертку через окружение. `gateway install` проверяет, что путь указывает на исполняемый файл, записывает обертку в `ProgramArguments` сервиса и сохраняет `OPENCLAW_WRAPPER` в окружении сервиса для последующих принудительных переустановок, обновлений и исправлений через doctor.

bashCopy code
[code]
    OPENCLAW_WRAPPER="$HOME/.local/bin/openclaw-doppler" openclaw gateway install --forceopenclaw doctor
[/code]

Чтобы удалить сохраненную обертку, очистите `OPENCLAW_WRAPPER` при переустановке:

bashCopy code
[code]
    OPENCLAW_WRAPPER= openclaw gateway install --forceopenclaw gateway restart
[/code]

Параметры команды

  * `gateway status`: `--url`, `--token`, `--password`, `--timeout`, `--no-probe`, `--require-rpc`, `--deep`, `--json`
  * `gateway install`: `--port`, `--runtime <node|bun>`, `--token`, `--wrapper <path>`, `--force`, `--json`
  * `gateway restart`: `--safe`, `--skip-deferral`, `--force`, `--wait <duration>`, `--json`
  * `gateway uninstall|start`: `--json`
  * `gateway stop`: `--disable`, `--json`

Поведение жизненного цикла

  * Используйте `gateway restart`, чтобы перезапустить управляемый сервис. Не объединяйте `gateway stop` и `gateway start` как замену перезапуску.
  * В macOS `gateway stop` по умолчанию использует `launchctl bootout`, что удаляет LaunchAgent из текущего загрузочного сеанса без сохранения отключения — автоматическое восстановление KeepAlive остается активным для будущих сбоев, а `gateway start` снова чисто включает сервис без ручного `launchctl enable`. Передайте `--disable`, чтобы постоянно подавить KeepAlive и RunAtLoad, чтобы Gateway не запускался повторно до следующего явного `gateway start`; используйте это, когда ручная остановка должна сохраняться после перезагрузок или рестартов системы.
  * `gateway restart --safe` просит работающий Gateway предварительно проверить активную работу OpenClaw и отложить перезапуск, пока не завершатся доставка ответов, встроенные запуски и запуски задач. `--safe` нельзя сочетать с `--force` или `--wait`.
  * `gateway restart --wait 30s` переопределяет настроенный бюджет ожидания завершения перед перезапуском для этого перезапуска. Числа без единиц измеряются в миллисекундах; принимаются единицы вроде `s`, `m` и `h`. `--wait 0` ожидает неограниченно.
  * `gateway restart --safe --skip-deferral` выполняет безопасный перезапуск с учетом OpenClaw, но обходит шлюз откладывания, поэтому Gateway немедленно отправляет событие перезапуска, даже если сообщены блокирующие факторы. Аварийный выход для оператора при зависших отложениях запусков задач; требует `--safe`.
  * `gateway restart --force` пропускает ожидание завершения активной работы и немедленно перезапускает сервис. Используйте это, когда оператор уже проверил перечисленные блокировщики задач и хочет вернуть Gateway в работу сейчас.
  * Команды жизненного цикла принимают `--json` для скриптов.

Аутентификация и SecretRef во время установки

  * Когда аутентификация по токену требует токен и `gateway.auth.token` управляется через SecretRef, `gateway install` проверяет, что SecretRef разрешается, но не сохраняет разрешенный токен в метаданные окружения сервиса.
  * Если аутентификация по токену требует токен, а настроенный токен SecretRef не разрешается, установка завершается закрытым отказом вместо сохранения резервного открытого текста.
  * Для аутентификации по паролю в `gateway run` предпочитайте `OPENCLAW_GATEWAY_PASSWORD`, `--password-file` или `gateway.auth.password` на базе SecretRef вместо встроенного `--password`.
  * В режиме выводимой аутентификации только shell-переменная `OPENCLAW_GATEWAY_PASSWORD` не ослабляет требования к токену при установке; используйте долговечную конфигурацию (`gateway.auth.password` или config `env`) при установке управляемого сервиса.
  * Если настроены и `gateway.auth.token`, и `gateway.auth.password`, а `gateway.auth.mode` не задан, установка блокируется, пока режим не будет задан явно.


## Обнаружение Gateway (Bonjour)

`gateway discover` сканирует маяки Gateway (`_openclaw-gw._tcp`).

  * Multicast DNS-SD: `local.`
  * Unicast DNS-SD (Wide-Area Bonjour): выберите домен (пример: `openclaw.internal.`) и настройте split DNS + DNS-сервер; см. [Bonjour](</ru/gateway/bonjour>).


Только Gateway с включенным обнаружением Bonjour (по умолчанию) публикуют маяк.

Записи широкозонного обнаружения могут включать эти TXT-подсказки:

  * `role` (подсказка роли Gateway)
  * `transport` (подсказка транспорта, например `gateway`)
  * `gatewayPort` (порт WebSocket, обычно `18789`)
  * `sshPort` (только режим полного обнаружения; клиенты по умолчанию используют SSH-цели `22`, когда он отсутствует)
  * `tailnetDns` (имя хоста MagicDNS, когда доступно)
  * `gatewayTls` / `gatewayTlsSha256` (TLS включен + отпечаток сертификата)
  * `cliPath` (только режим полного обнаружения)


### `gateway discover`

bashCopy code
[code]
    openclaw gateway discover
[/code]

Машиночитаемый вывод (также отключает стилизацию/индикатор).

Примеры:

bashCopy code
[code]
    openclaw gateway discover --timeout 4000openclaw gateway discover --json | jq '.beacons[].wsUrl'
[/code]

## Связанные материалы

  * [Справочник CLI](</ru/cli>)
  * [Регламент Gateway](</ru/gateway>)


Was this useful?YesNo

Open issue