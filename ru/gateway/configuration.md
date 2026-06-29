---
title: Конфигурация
source_url: https://docs.openclaw.ai/ru/gateway/configuration
scraped_at: 2026-06-29
---

Gateway & OpsGateway

OpenClaw читает необязательную конфигурацию **JSON5** из `~/.openclaw/openclaw.json`. Активный путь конфигурации должен быть обычным файлом. Макеты `openclaw.json` через symlink не поддерживаются для записей, которыми владеет OpenClaw; атомарная запись может заменить путь вместо сохранения symlink. Если вы храните конфигурацию вне каталога состояния по умолчанию, укажите `OPENCLAW_CONFIG_PATH` прямо на реальный файл.

Если файл отсутствует, OpenClaw использует безопасные значения по умолчанию. Частые причины добавить конфигурацию:

  * Подключить каналы и управлять тем, кто может писать боту
  * Задать модели, инструменты, sandboxing или автоматизацию (cron, хуки)
  * Настроить сессии, медиа, сеть или UI


См. [полный справочник](</ru/gateway/configuration-reference>) по всем доступным полям.

Агенты и автоматизация должны использовать `config.schema.lookup` для точной документации на уровне полей перед редактированием конфигурации. Используйте эту страницу для практических задач и [справочник по конфигурации](</ru/gateway/configuration-reference>) для более широкой карты полей и значений по умолчанию.

## Минимальная конфигурация

json5Copy code
[code]
    // ~/.openclaw/openclaw.json{  agents: { defaults: { workspace: "~/.openclaw/workspace" } },  channels: { whatsapp: { allowFrom: ["+15555550123"] } },}
[/code]

## Редактирование конфигурации

### Interactive wizard

bashCopy code
[code]
    openclaw onboard       # full onboarding flowopenclaw configure     # config wizard
[/code]

### CLI (one-liners)

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config set agents.defaults.heartbeat.every "2h"openclaw config unset plugins.entries.brave.config.webSearch.apiKey
[/code]

### Control UI

Откройте <http://127.0.0.1:18789> и используйте вкладку **Config**. Control UI строит форму из живой схемы конфигурации, включая документационные метаданные полей `title` / `description`, а также схемы plugin и каналов, когда они доступны, с редактором **Raw JSON** как резервным вариантом. Для интерфейсов с детализацией и других инструментов Gateway также предоставляет `config.schema.lookup`, чтобы получить один узел схемы, ограниченный путем, плюс краткие сведения о непосредственных дочерних элементах.

### Direct edit

Редактируйте `~/.openclaw/openclaw.json` напрямую. Gateway отслеживает файл и применяет изменения автоматически (см. горячая перезагрузка).

## Строгая валидация

`openclaw config schema` выводит каноническую JSON Schema, используемую Control UI и валидацией. `config.schema.lookup` получает один узел, ограниченный путем, плюс краткие сведения о дочерних элементах для инструментов с детализацией. Документационные метаданные полей `title`/`description` передаются через вложенные объекты, wildcard (`*`), элементы массива (`[]`) и ветви `anyOf`/ `oneOf`/`allOf`. Схемы runtime plugin и каналов объединяются, когда загружен реестр манифестов.

Когда валидация не проходит:

  * Gateway не загружается
  * Работают только диагностические команды (`openclaw doctor`, `openclaw logs`, `openclaw health`, `openclaw status`)
  * Запустите `openclaw doctor`, чтобы увидеть точные проблемы
  * Запустите `openclaw doctor --fix` (или `--yes`), чтобы применить исправления


Gateway хранит доверенную последнюю работоспособную копию после каждого успешного запуска, но запуск и горячая перезагрузка не восстанавливают ее автоматически. Если `openclaw.json` не проходит валидацию (включая локальную валидацию plugin), запуск Gateway завершается с ошибкой или перезагрузка пропускается, а текущий runtime сохраняет последнюю принятую конфигурацию. Запустите `openclaw doctor --fix` (или `--yes`), чтобы исправить конфигурацию с префиксами/перезаписанными данными или восстановить последнюю работоспособную копию. Повышение до последней работоспособной копии пропускается, когда кандидат содержит отредактированные placeholders секретов, такие как `***`.

## Распространенные задачи

Set up a channel (WhatsApp, Telegram, Discord, etc.)

У каждого канала есть собственный раздел конфигурации в `channels.<provider>`. См. отдельную страницу канала с шагами настройки:

  * [WhatsApp](</ru/channels/whatsapp>) \- `channels.whatsapp`
  * [Telegram](</ru/channels/telegram>) \- `channels.telegram`
  * [Discord](</ru/channels/discord>) \- `channels.discord`
  * [Feishu](</ru/channels/feishu>) \- `channels.feishu`
  * [Google Chat](</ru/channels/googlechat>) \- `channels.googlechat`
  * [Microsoft Teams](</ru/channels/msteams>) \- `channels.msteams`
  * [Slack](</ru/channels/slack>) \- `channels.slack`
  * [Signal](</ru/channels/signal>) \- `channels.signal`
  * [iMessage](</ru/channels/imessage>) \- `channels.imessage`
  * [Mattermost](</ru/channels/mattermost>) \- `channels.mattermost`


Все каналы используют один и тот же шаблон политики DM:

json5Copy code
[code]
    {  channels: {    telegram: {      enabled: true,      botToken: "123:abc",      dmPolicy: "pairing",   // pairing | allowlist | open | disabled      allowFrom: ["tg:123"], // only for allowlist/open    },  },}
[/code]

Choose and configure models

Задайте основную модель и необязательные резервные варианты:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "anthropic/claude-sonnet-4-6",        fallbacks: ["openai/gpt-5.4"],      },      models: {        "anthropic/claude-sonnet-4-6": { alias: "Sonnet" },        "openai/gpt-5.4": { alias: "GPT" },      },    },  },}
[/code]

  * `agents.defaults.models` определяет каталог моделей и действует как allowlist для `/model`; записи `provider/*` фильтруют `/model`, `/models` и средства выбора моделей до выбранных провайдеров, при этом по-прежнему используя динамическое обнаружение моделей.
  * Используйте `openclaw config set agents.defaults.models '<json>' --strict-json --merge`, чтобы добавить записи allowlist без удаления существующих моделей. Обычные замены, которые удалили бы записи, отклоняются, если не передать `--replace`.
  * Ссылки на модели используют формат `provider/model` (например, `anthropic/claude-opus-4-6`).
  * `agents.defaults.imageMaxDimensionPx` управляет уменьшением изображений стенограммы/инструментов (по умолчанию `1200`); более низкие значения обычно уменьшают использование vision-токенов в запусках с большим количеством скриншотов.
  * См. [CLI моделей](</ru/concepts/models>) для переключения моделей в чате и [аварийное переключение моделей](</ru/concepts/model-failover>) для ротации auth и поведения резервных вариантов.
  * Для пользовательских/самостоятельно размещенных провайдеров см. [пользовательские провайдеры](</ru/gateway/config-tools#custom-providers-and-base-urls>) в справочнике.

Control who can message the bot

Доступ к DM управляется отдельно для каждого канала через `dmPolicy`:

  * `"pairing"` (по умолчанию): неизвестные отправители получают одноразовый код сопряжения для подтверждения
  * `"allowlist"`: только отправители в `allowFrom` (или в хранилище разрешенных сопряженных отправителей)
  * `"open"`: разрешить все входящие DM (требует `allowFrom: ["*"]`)
  * `"disabled"`: игнорировать все DM


Для групп используйте `groupPolicy` \+ `groupAllowFrom` или allowlist, специфичные для канала.

См. [полный справочник](</ru/gateway/config-channels#dm-and-group-access>) для подробностей по каждому каналу.

Set up group chat mention gating

Для групповых сообщений по умолчанию **требуется упоминание**. Настройте шаблоны триггеров для каждого агента. Обычные ответы в группах/каналах публикуются автоматически; включите путь message-tool для общих комнат, где агент должен решать, когда говорить:

json5Copy code
[code]
    {  messages: {    visibleReplies: "automatic", // set "message_tool" to require message-tool sends everywhere    groupChat: {      visibleReplies: "message_tool", // opt-in; visible output requires message(action=send)      unmentionedInbound: "room_event", // unmentioned always-on group chatter is quiet context    },  },  agents: {    list: [      {        id: "main",        groupChat: {          mentionPatterns: ["@openclaw", "openclaw"],        },      },    ],  },  channels: {    whatsapp: {      groups: { "*": { requireMention: true } },    },  },}
[/code]

  * **Упоминания в метаданных** : нативные @-упоминания (WhatsApp tap-to-mention, Telegram @bot и т. д.)
  * **Текстовые шаблоны** : безопасные regex-шаблоны в `mentionPatterns`
  * **Видимые ответы** : `messages.visibleReplies` может требовать отправки через message-tool глобально; `messages.groupChat.visibleReplies` переопределяет это для групп/каналов.
  * См. [полный справочник](</ru/gateway/config-channels#group-chat-mention-gating>) по режимам видимых ответов, переопределениям для каналов и режиму чата с самим собой.

Restrict skills per agent

Используйте `agents.defaults.skills` как общий базовый набор, затем переопределяйте конкретных агентов через `agents.list[].skills`:

json5Copy code
[code]
    {  agents: {    defaults: {      skills: ["github", "weather"],    },    list: [      { id: "writer" }, // inherits github, weather      { id: "docs", skills: ["docs-search"] }, // replaces defaults      { id: "locked-down", skills: [] }, // no skills    ],  },}
[/code]

  * Опустите `agents.defaults.skills`, чтобы Skills по умолчанию были без ограничений.
  * Опустите `agents.list[].skills`, чтобы наследовать значения по умолчанию.
  * Задайте `agents.list[].skills: []`, чтобы Skills отсутствовали.
  * См. [Skills](</ru/tools/skills>), [конфигурация Skills](</ru/tools/skills-config>) и [справочник по конфигурации](</ru/gateway/config-agents#agents-defaults-skills>).

Tune gateway channel health monitoring

Управляйте тем, насколько агрессивно gateway перезапускает каналы, которые выглядят устаревшими:

json5Copy code
[code]
    {  gateway: {    channelHealthCheckMinutes: 5,    channelStaleEventThresholdMinutes: 30,    channelMaxRestartsPerHour: 10,  },  channels: {    telegram: {      healthMonitor: { enabled: false },      accounts: {        alerts: {          healthMonitor: { enabled: true },        },      },    },  },}
[/code]

  * Задайте `gateway.channelHealthCheckMinutes: 0`, чтобы глобально отключить перезапуски health monitor.
  * `channelStaleEventThresholdMinutes` должен быть больше интервала проверки или равен ему.
  * Используйте `channels.<provider>.healthMonitor.enabled` или `channels.<provider>.accounts.<id>.healthMonitor.enabled`, чтобы отключить автоматические перезапуски для одного канала или аккаунта, не отключая глобальный монитор.
  * См. [проверки работоспособности](</ru/gateway/health>) для операционной отладки и [полный справочник](</ru/gateway/configuration-reference#gateway>) по всем полям.

Tune gateway WebSocket handshake timeout

Дайте локальным клиентам больше времени на завершение pre-auth WebSocket handshake на загруженных или маломощных хостах:

json5Copy code
[code]
    {  gateway: {    handshakeTimeoutMs: 30000,  },}
[/code]

  * Значение по умолчанию — `15000` миллисекунд.
  * `OPENCLAW_HANDSHAKE_TIMEOUT_MS` по-прежнему имеет приоритет для разовых переопределений сервиса или оболочки.
  * Сначала предпочитайте исправлять задержки запуска/цикла событий; эта настройка предназначена для хостов, которые исправны, но медленны во время прогрева.

Configure sessions and resets

Сессии управляют непрерывностью и изоляцией разговоров:

json5Copy code
[code]
    {  session: {    dmScope: "per-channel-peer",  // recommended for multi-user    threadBindings: {      enabled: true,      idleHours: 24,      maxAgeHours: 0,    },    reset: {      mode: "daily",      atHour: 4,      idleMinutes: 120,    },  },}
[/code]

  * `dmScope`: `main` (общий) | `per-peer` | `per-channel-peer` | `per-account-channel-peer`
  * `threadBindings`: глобальные значения по умолчанию для маршрутизации сеансов, привязанных к тредам (Discord поддерживает `/focus`, `/unfocus`, `/agents`, `/session idle` и `/session max-age`).
  * См. [Управление сеансами](</ru/concepts/session>) о областях действия, связях идентичностей и политике отправки.
  * См. [полный справочник](</ru/gateway/config-agents#session>) по всем полям.

Включить песочницы

Запускайте сеансы агентов в изолированных средах песочницы:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main",  // off | non-main | all        scope: "agent",    // session | agent | shared      },    },  },}
[/code]

Сначала соберите образ: из checkout исходного кода выполните `scripts/sandbox-setup.sh`, а при установке из npm см. встроенную команду `docker build` в разделе [Песочницы § Образы и настройка](</ru/gateway/sandboxing#images-and-setup>).

См. [Песочницы](</ru/gateway/sandboxing>) для полного руководства и [полный справочник](</ru/gateway/config-agents#agentsdefaultssandbox>) по всем параметрам.

Включить push через ретранслятор для официальных сборок iOS

Push через ретранслятор для публичных сборок App Store/TestFlight использует размещенный ретранслятор OpenClaw: `https://ios-push-relay.openclaw.ai`.

Пользовательские развертывания ретранслятора требуют намеренно отдельного пути сборки/развертывания iOS, URL ретранслятора которого совпадает с URL ретранслятора Gateway. Если вы используете пользовательскую сборку с ретранслятором, задайте это в конфигурации Gateway:

json5Copy code
[code]
    {  gateway: {    push: {      apns: {        relay: {          baseUrl: "https://relay.example.com",          // Optional. Default: 10000          timeoutMs: 10000,        },      },    },  },}
[/code]

Эквивалент CLI:

bashCopy code
[code]
    openclaw config set gateway.push.apns.relay.baseUrl https://relay.example.com
[/code]

Что это делает:

  * Позволяет Gateway отправлять `push.test`, сигналы пробуждения и пробуждения для переподключения через внешний ретранслятор.
  * Использует разрешение на отправку в области регистрации, пересланное сопряженным приложением iOS. Gateway не нужен токен ретранслятора на уровне всего развертывания.
  * Привязывает каждую регистрацию через ретранслятор к идентичности Gateway, с которым было сопряжено приложение iOS, поэтому другой Gateway не сможет повторно использовать сохраненную регистрацию.
  * Оставляет локальные/ручные сборки iOS на прямом APNs. Отправки через ретранслятор применяются только к официальным распространяемым сборкам, зарегистрированным через ретранслятор.
  * Должно совпадать с базовым URL ретранслятора, встроенным в сборку iOS, чтобы трафик регистрации и отправки попадал в одно и то же развертывание ретранслятора.


Сквозной поток:

  1. Установите официальную/TestFlight-сборку iOS.
  2. Необязательно: настройте `gateway.push.apns.relay.baseUrl` на Gateway только при использовании намеренно отдельной пользовательской сборки с ретранслятором.
  3. Сопрягите приложение iOS с Gateway и дайте подключиться как сеансам узла, так и сеансам оператора.
  4. Приложение iOS получает идентичность Gateway, регистрируется в ретрансляторе с помощью App Attest и квитанции приложения, а затем публикует полезную нагрузку `push.apns.register` через ретранслятор в сопряженный Gateway.
  5. Gateway сохраняет дескриптор ретранслятора и разрешение на отправку, затем использует их для `push.test`, сигналов пробуждения и пробуждений для переподключения.


Операционные примечания:

  * Если вы переключаете приложение iOS на другой Gateway, переподключите приложение, чтобы оно могло опубликовать новую регистрацию ретранслятора, привязанную к этому Gateway.
  * Если вы выпускаете новую сборку iOS, указывающую на другое развертывание ретранслятора, приложение обновляет кешированную регистрацию ретранслятора вместо повторного использования старого источника ретранслятора.


Примечание о совместимости:

  * `OPENCLAW_APNS_RELAY_BASE_URL` и `OPENCLAW_APNS_RELAY_TIMEOUT_MS` по-прежнему работают как временные переопределения через переменные окружения.
  * Пользовательские URL ретранслятора Gateway должны совпадать с базовым URL ретранслятора, встроенным в сборку iOS. Публичный канал релиза App Store отклоняет пользовательские переопределения URL ретранслятора iOS.
  * `OPENCLAW_APNS_RELAY_ALLOW_HTTP=true` остается аварийным выходом для разработки только через local loopback; не сохраняйте HTTP URL ретранслятора в конфигурации.


См. [Приложение iOS](</ru/platforms/ios#relay-backed-push-for-official-builds>) для сквозного потока и [Поток аутентификации и доверия](</ru/platforms/ios#authentication-and-trust-flow>) для модели безопасности ретранслятора.

Настроить Heartbeat (периодические проверки) json5Copy code
[code]
    {  agents: {    defaults: {      heartbeat: {        every: "30m",        target: "last",      },    },  },}
[/code]

  * `every`: строка длительности (`30m`, `2h`). Задайте `0m`, чтобы отключить.
  * `target`: `last` | `none` | `<channel-id>` (например, `discord`, `matrix`, `telegram` или `whatsapp`)
  * `directPolicy`: `allow` (по умолчанию) или `block` для целей Heartbeat в стиле личных сообщений
  * См. [Heartbeat](</ru/gateway/heartbeat>) для полного руководства.

Настроить задания Cron json5Copy code
[code]
    {  cron: {    enabled: true,    maxConcurrentRuns: 8, // default; cron dispatch + isolated cron agent-turn execution    sessionRetention: "24h",    runLog: {      maxBytes: "2mb",      keepLines: 2000,    },  },}
[/code]

  * `sessionRetention`: удалять завершенные изолированные сеансы запусков из `sessions.json` (по умолчанию `24h`; задайте `false`, чтобы отключить).
  * `runLog`: удалять сохраненные строки истории запусков Cron для каждого задания. `maxBytes` остается допустимым для старых журналов запусков на основе файлов.
  * См. [Задания Cron](</ru/automation/cron-jobs>) для обзора функции и примеров CLI.

Настроить Webhook-и (хуки)

Включите HTTP-конечные точки Webhook на Gateway:

json5Copy code
[code]
    {  hooks: {    enabled: true,    token: "shared-secret",    path: "/hooks",    defaultSessionKey: "hook:ingress",    allowRequestSessionKey: false,    allowedSessionKeyPrefixes: ["hook:"],    mappings: [      {        match: { path: "gmail" },        action: "agent",        agentId: "main",        deliver: true,      },    ],  },}
[/code]

Примечание по безопасности:

  * Считайте все содержимое полезных нагрузок хуков/Webhook недоверенным вводом.
  * Используйте выделенный `hooks.token`; не используйте повторно активные секреты аутентификации Gateway (`gateway.auth.token` / `OPENCLAW_GATEWAY_TOKEN` или `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD`).
  * Аутентификация хуков выполняется только через заголовки (`Authorization: Bearer ...` или `x-openclaw-token`); токены в строке запроса отклоняются.
  * `hooks.path` не может быть `/`; держите вход Webhook на выделенном подпути, например `/hooks`.
  * Держите флаги обхода небезопасного содержимого отключенными (`hooks.gmail.allowUnsafeExternalContent`, `hooks.mappings[].allowUnsafeExternalContent`), кроме случаев строго ограниченной отладки.
  * Если вы включаете `hooks.allowRequestSessionKey`, также задайте `hooks.allowedSessionKeyPrefixes`, чтобы ограничить выбираемые вызывающей стороной ключи сеансов.
  * Для агентов, запускаемых хуками, предпочитайте сильные современные уровни моделей и строгую политику инструментов (например, только обмен сообщениями плюс песочница, где возможно).


См. [полный справочник](</ru/gateway/configuration-reference#hooks>) по всем параметрам сопоставления и интеграции Gmail.

Настроить маршрутизацию нескольких агентов

Запускайте несколько изолированных агентов с отдельными рабочими пространствами и сеансами:

json5Copy code
[code]
    {  agents: {    list: [      { id: "home", default: true, workspace: "~/.openclaw/workspace-home" },      { id: "work", workspace: "~/.openclaw/workspace-work" },    ],  },  bindings: [    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },  ],}
[/code]

См. [Мультиагентная работа](</ru/concepts/multi-agent>) и [полный справочник](</ru/gateway/config-agents#multi-agent-routing>) по правилам привязки и профилям доступа для отдельных агентов.

Разделить конфигурацию на несколько файлов ($include)

Используйте `$include`, чтобы организовывать большие конфигурации:

json5Copy code
[code]
    // ~/.openclaw/openclaw.json{  gateway: { port: 18789 },  agents: { $include: "./agents.json5" },  broadcast: {    $include: ["./clients/a.json5", "./clients/b.json5"],  },}
[/code]

  * **Один файл** : заменяет содержащий объект
  * **Массив файлов** : глубоко объединяется по порядку (последний имеет приоритет)
  * **Соседние ключи** : объединяются после включений (переопределяют включенные значения)
  * **Вложенные включения** : поддерживаются до 10 уровней глубины
  * **Относительные пути** : разрешаются относительно включающего файла
  * **Формат пути** : пути включения не должны содержать нулевых байтов и должны быть строго короче 4096 символов до и после разрешения
  * **Записи, принадлежащие OpenClaw** : когда запись изменяет только один раздел верхнего уровня, подкрепленный включением одного файла, например `plugins: { $include: "./plugins.json5" }`, OpenClaw обновляет этот включенный файл и оставляет `openclaw.json` нетронутым
  * **Неподдерживаемая сквозная запись** : корневые включения, массивы включений и включения с соседними переопределениями завершаются закрыто для записей, принадлежащих OpenClaw, вместо выравнивания конфигурации
  * **Ограничение** : пути `$include` должны разрешаться внутри каталога, содержащего `openclaw.json`. Чтобы совместно использовать дерево на разных машинах или для разных пользователей, задайте `OPENCLAW_INCLUDE_ROOTS` как список путей (`:` в POSIX, `;` в Windows) к дополнительным каталогам, на которые могут ссылаться включения. Символические ссылки разрешаются и проверяются повторно, поэтому путь, который лексически находится в каталоге конфигурации, но чей реальный целевой путь выходит за пределы всех разрешенных корней, все равно отклоняется.
  * **Обработка ошибок** : понятные ошибки для отсутствующих файлов, ошибок разбора, циклических включений, недопустимого формата пути и чрезмерной длины


## Горячая перезагрузка конфигурации

Gateway отслеживает `~/.openclaw/openclaw.json` и применяет изменения автоматически: ручной перезапуск для большинства настроек не требуется.

Прямые правки файла считаются недоверенными, пока не пройдут валидацию. Наблюдатель ждет, пока уляжется шум временной записи/переименования от редактора, читает итоговый файл и отклоняет недопустимые внешние правки без перезаписи `openclaw.json`. Записи конфигурации, принадлежащие OpenClaw, проходят через тот же шлюз схемы перед записью; разрушительные перезаписи, такие как удаление `gateway.mode` или уменьшение файла более чем наполовину, отклоняются и сохраняются как `.rejected.*` для проверки.

Если вы видите `config reload skipped (invalid config)` или запуск сообщает `Invalid config`, проверьте конфигурацию, выполните `openclaw config validate`, затем выполните `openclaw doctor --fix` для исправления. См. [Устранение неполадок Gateway](</ru/gateway/troubleshooting#gateway-rejected-invalid-config>) для контрольного списка.

### Режимы перезагрузки

Режим | Поведение  
---|---  
**`hybrid`** (по умолчанию) | Мгновенно горячо применяет безопасные изменения. Автоматически перезапускается для критических.  
**`hot`** | Горячо применяет только безопасные изменения. Записывает предупреждение, когда нужен перезапуск: вы выполняете его сами.  
**`restart`** | Перезапускает Gateway при любом изменении конфигурации, безопасном или нет.  
**`off`** | Отключает отслеживание файлов. Изменения вступают в силу при следующем ручном перезапуске.  
  
json5Copy code
[code]
    {  gateway: {    reload: { mode: "hybrid", debounceMs: 300 },  },}
[/code]

### Что применяется горячо, а что требует перезапуска

Большинство полей применяются горячо без простоя. В режиме `hybrid` изменения, требующие перезапуска, обрабатываются автоматически.

Категория | Поля | Требуется перезапуск?  
---|---|---  
Каналы | `channels.*`, `web` (WhatsApp) - все встроенные каналы и каналы Plugin | Нет  
Агент и модели | `agent`, `agents`, `models`, `routing` | Нет  
Автоматизация | `hooks`, `cron`, `agent.heartbeat` | Нет  
Сессии и сообщения | `session`, `messages` | Нет  
Инструменты и медиа | `tools`, `browser`, `skills`, `mcp`, `audio`, `talk` | Нет  
UI и прочее | `ui`, `logging`, `identity`, `bindings` | Нет  
Сервер Gateway | `gateway.*` (порт, привязка, аутентификация, tailscale, TLS, HTTP) | **Да**  
Инфраструктура | `discovery`, `plugins` | **Да**  
  
### Планирование перезагрузки

Когда вы редактируете исходный файл, на который ссылается `$include`, OpenClaw планирует перезагрузку по исходной авторской структуре, а не по развернутому представлению в памяти. Это сохраняет предсказуемость решений горячей перезагрузки (горячее применение или перезапуск), даже когда один раздел верхнего уровня находится в собственном включенном файле, например `plugins: { $include: "./plugins.json5" }`. Планирование перезагрузки завершается отказом, если исходная структура неоднозначна.

## Config RPC (программные обновления)

Для инструментов, которые записывают конфигурацию через API Gateway, предпочитайте такой поток:

  * `config.schema.lookup`, чтобы проверить одно поддерево (поверхностный узел схемы + сводки дочерних элементов)
  * `config.get`, чтобы получить текущий снимок плюс `hash`
  * `config.patch` для частичных обновлений (JSON merge patch: объекты сливаются, `null` удаляет, массивы заменяются при явном подтверждении через `replacePaths`, если записи будут удалены)
  * `config.apply` только когда вы намерены заменить всю конфигурацию
  * `update.run` для явного самообновления плюс перезапуска; включите `continuationMessage`, когда после перезапуска сессия должна выполнить один последующий ход
  * `update.status`, чтобы проверить последний sentinel перезапуска обновления и подтвердить запущенную версию после перезапуска


Агенты должны считать `config.schema.lookup` первой точкой обращения за точной документацией и ограничениями на уровне полей. Используйте [Справочник по конфигурации](</ru/gateway/configuration-reference>), когда им нужна более широкая карта конфигурации, значения по умолчанию или ссылки на специальные справочники подсистем.

Пример частичного patch:

bashCopy code
[code]
    openclaw gateway call config.get --params '{}'  # capture payload.hashopenclaw gateway call config.patch --params '{  "raw": "{ channels: { telegram: { groups: { \"*\": { requireMention: false } } } } }",  "baseHash": "<hash>"}'
[/code]

И `config.apply`, и `config.patch` принимают `raw`, `baseHash`, `sessionKey`, `note` и `restartDelayMs`. `baseHash` обязателен для обоих методов, когда конфигурация уже существует.

`config.patch` также принимает `replacePaths`, массив путей конфигурации, для которых замена массива является намеренной. Если patch заменит или удалит существующий массив с меньшим количеством записей, Gateway отклонит запись, если этот точный путь не указан в `replacePaths`; вложенные массивы в элементах массива используют `[]`, например `agents.list[].skills`. Это не дает усеченным снимкам `config.get` незаметно перезаписать массивы маршрутизации или списков разрешений. Используйте `config.apply`, когда вы намерены заменить всю конфигурацию.

## Переменные окружения

OpenClaw читает переменные окружения из родительского процесса, а также из:

  * `.env` из текущего рабочего каталога (если есть)
  * `~/.openclaw/.env` (глобальный fallback)


Ни один из файлов не переопределяет существующие переменные окружения. Вы также можете задавать inline-переменные окружения в конфигурации:

json5Copy code
[code]
    {  env: {    OPENROUTER_API_KEY: "sk-or-...",    vars: { GROQ_API_KEY: "gsk-..." },  },}
[/code]

Импорт окружения shell (необязательно)

Если включено и ожидаемые ключи не заданы, OpenClaw запускает ваш login shell и импортирует только отсутствующие ключи:

json5Copy code
[code]
    {env: {  shellEnv: { enabled: true, timeoutMs: 15000 },},}
[/code]

Эквивалент переменной окружения: `OPENCLAW_LOAD_SHELL_ENV=1`

Подстановка переменных окружения в значениях конфигурации

Ссылайтесь на переменные окружения в любом строковом значении конфигурации с помощью `${VAR_NAME}`:

json5Copy code
[code]
    {gateway: { auth: { token: "${OPENCLAW_GATEWAY_TOKEN}" } },models: { providers: { custom: { apiKey: "${CUSTOM_API_KEY}" } } },}
[/code]

Правила:

  * Сопоставляются только имена в верхнем регистре: `[A-Z_][A-Z0-9_]*`
  * Отсутствующие или пустые переменные вызывают ошибку во время загрузки
  * Экранируйте через `$${VAR}` для буквального вывода
  * Работает внутри файлов `$include`
  * Inline-подстановка: `"${BASE}/v1"` → `"https://api.example.com/v1"`

Ссылки на секреты (env, file, exec)

Для полей, поддерживающих объекты SecretRef, можно использовать:

json5Copy code
[code]
    {models: {  providers: {    openai: { apiKey: { source: "env", provider: "default", id: "OPENAI_API_KEY" } },  },},skills: {  entries: {    "image-lab": {      apiKey: {        source: "file",        provider: "filemain",        id: "/skills/entries/image-lab/apiKey",      },    },  },},channels: {  googlechat: {    serviceAccountRef: {      source: "exec",      provider: "vault",      id: "channels/googlechat/serviceAccount",    },  },},}
[/code]

Подробности SecretRef (включая `secrets.providers` для `env`/`file`/`exec`) находятся в [Управление секретами](</ru/gateway/secrets>). Поддерживаемые пути учетных данных перечислены в [Поверхность учетных данных SecretRef](</ru/reference/secretref-credential-surface>).

См. [Окружение](</ru/help/environment>) для полного порядка приоритета и источников.

## Полный справочник

Полный справочник по всем полям см. в **[Справочнике по конфигурации](</ru/gateway/configuration-reference>)**.

* * *

_Связанные материалы:[Примеры конфигурации](</ru/gateway/configuration-examples>) · [Справочник по конфигурации](</ru/gateway/configuration-reference>) · [Doctor](</ru/gateway/doctor>)_

## Связанные материалы

  * [Справочник по конфигурации](</ru/gateway/configuration-reference>)
  * [Примеры конфигурации](</ru/gateway/configuration-examples>)
  * [Runbook Gateway](</ru/gateway>)


Was this useful?YesNo

Open issue