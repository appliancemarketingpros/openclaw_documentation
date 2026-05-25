---
title: Slack
source_url: https://docs.openclaw.ai/uk/channels/slack
scraped_at: 2026-05-25
---

Готове до production-використання для DM і каналів через інтеграції застосунку Slack. Типовий режим — Socket Mode; також підтримуються URL-адреси HTTP-запитів.

[**Створення пари** DM у Slack типово використовують режим створення пари. ](</uk/channels/pairing>) [**Slash-команди** Нативна поведінка команд і каталог команд. ](</uk/tools/slash-commands>) [**Усунення несправностей каналів** Кросканальна діагностика та інструкції з відновлення. ](</uk/channels/troubleshooting>)

## Вибір Socket Mode або URL-адрес HTTP-запитів

Обидва транспорти готові до production-використання й мають паритет функцій для повідомлень, slash-команд, App Home та інтерактивності. Обирайте за формою розгортання, а не за функціями.

Аспект | Socket Mode (типово) | URL-адреси HTTP-запитів  
---|---|---  
Публічна URL-адреса Gateway | Не потрібна | Потрібна (DNS, TLS, reverse proxy або тунель)  
Вихідна мережа | Має бути доступний вихідний WSS до `wss-primary.slack.com` | Без вихідного WS; лише вхідний HTTPS  
Потрібні токени | Bot token (`xoxb-...`) + App-Level Token (`xapp-...`) з `connections:write` | Bot token (`xoxb-...`) + Signing Secret  
Ноутбук розробника / за firewall | Працює як є | Потрібен публічний тунель (ngrok, Cloudflare Tunnel, Tailscale Funnel) або staging Gateway  
Горизонтальне масштабування | Один сеанс Socket Mode на застосунок на хост; для кількох Gateway потрібні окремі застосунки Slack | Stateless POST-обробник; кілька реплік Gateway можуть спільно використовувати один застосунок за load balancer  
Кілька акаунтів на одному Gateway | Підтримується; кожен акаунт відкриває власний WS | Підтримується; кожному акаунту потрібен унікальний `webhookPath` (типово `/slack/events`), щоб реєстрації не конфліктували  
Транспорт slash-команд | Доставляється через WS-з’єднання; `slash_commands[].url` ігнорується | Slack надсилає POST на `slash_commands[].url`; поле потрібне для dispatch команди  
Підписування запитів | Не використовується (автентифікація — це App-Level Token) | Slack підписує кожен запит; OpenClaw перевіряє через `signingSecret`  
Відновлення після розриву з’єднання | Slack SDK автоматично перепідключається; застосовується налаштування pong-timeout транспорту gateway | Немає постійного з’єднання, яке може розірватися; повторні спроби виконуються для кожного запиту від Slack  
  
## Швидке налаштування

### Socket Mode (типово)

* ### Створіть новий застосунок Slack

Відкрийте [api.slack.com/apps](<https://api.slack.com/apps/new>) → **Create New App** → **From a manifest** → виберіть свій workspace → вставте один із наведених нижче маніфестів → **Next** → **Create**.

РекомендованоCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","emoji:read","files:read","files:write","groups:history","groups:read","im:history","im:read","im:write","mpim:history","mpim:read","mpim:write","pins:read","pins:write","reactions:read","reactions:write","usergroups:read","users:read"]}},"settings": {"socket_mode_enabled": true,"event_subscriptions": {"bot_events": ["app_home_opened","app_mention","channel_rename","member_joined_channel","member_left_channel","message.channels","message.groups","message.im","message.mpim","pin_added","pin_removed","reaction_added","reaction_removed"]}}}
[/code]

МінімальнийCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","groups:history","groups:read","im:history","im:read","im:write","users:read"]}},"settings": {"socket_mode_enabled": true,"event_subscriptions": {"bot_events": ["app_home_opened","app_mention","message.channels","message.groups","message.im"]}}}
[/code]

Після того як Slack створить застосунок:

  * **Basic Information → App-Level Tokens → Generate Token and Scopes** : додайте `connections:write`, збережіть, скопіюйте значення `xapp-...`.
  * **Install App → Install to Workspace** : скопіюйте `xoxb-...` Bot User OAuth Token.


* ### Налаштуйте OpenClaw

Рекомендоване налаштування SecretRef:

bashCopy code
[code]
    export SLACK_APP_TOKEN=xapp-...export SLACK_BOT_TOKEN=xoxb-...cat > slack.socket.patch.json5 <<'JSON5'{channels: {slack: {enabled: true,mode: "socket",appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },},},}JSON5openclaw config patch --file ./slack.socket.patch.json5 --dry-runopenclaw config patch --file ./slack.socket.patch.json5
[/code]

Резервний варіант через env (лише типовий акаунт):

bashCopy code
[code]
    SLACK_APP_TOKEN=xapp-...SLACK_BOT_TOKEN=xoxb-...
[/code]

* ### Запустіть gateway

bashCopy code
[code]
    openclaw gateway
[/code]

### URL-адреси HTTP-запитів

* ### Створіть новий застосунок Slack

Відкрийте [api.slack.com/apps](<https://api.slack.com/apps/new>) → **Create New App** → **From a manifest** → виберіть свій workspace → вставте один із наведених нижче маніфестів → замініть `https://gateway-host.example.com/slack/events` на публічну URL-адресу Gateway → **Next** → **Create**.

РекомендованоCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false,"url": "https://gateway-host.example.com/slack/events"}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","emoji:read","files:read","files:write","groups:history","groups:read","im:history","im:read","im:write","mpim:history","mpim:read","mpim:write","pins:read","pins:write","reactions:read","reactions:write","usergroups:read","users:read"]}},"settings": {"event_subscriptions": {"request_url": "https://gateway-host.example.com/slack/events","bot_events": ["app_home_opened","app_mention","channel_rename","member_joined_channel","member_left_channel","message.channels","message.groups","message.im","message.mpim","pin_added","pin_removed","reaction_added","reaction_removed"]},"interactivity": {"is_enabled": true,"request_url": "https://gateway-host.example.com/slack/events","message_menu_options_url": "https://gateway-host.example.com/slack/events"}}}
[/code]

MinimalCopy code
[code]
    {"display_information": {"name": "OpenClaw","description": "Slack connector for OpenClaw"},"features": {"bot_user": { "display_name": "OpenClaw", "always_online": true },"app_home": {"home_tab_enabled": true,"messages_tab_enabled": true,"messages_tab_read_only_enabled": false},"slash_commands": [{"command": "/openclaw","description": "Send a message to OpenClaw","should_escape": false,"url": "https://gateway-host.example.com/slack/events"}]},"oauth_config": {"scopes": {"bot": ["app_mentions:read","assistant:write","channels:history","channels:read","chat:write","commands","groups:history","groups:read","im:history","im:read","im:write","users:read"]}},"settings": {"event_subscriptions": {"request_url": "https://gateway-host.example.com/slack/events","bot_events": ["app_home_opened","app_mention","message.channels","message.groups","message.im"]},"interactivity": {"is_enabled": true,"request_url": "https://gateway-host.example.com/slack/events","message_menu_options_url": "https://gateway-host.example.com/slack/events"}}}
[/code]

Після створення застосунку в Slack:

  * **Basic Information → App Credentials** : скопіюйте **Signing Secret** для перевірки запитів.
  * **Install App → Install to Workspace** : скопіюйте `xoxb-...` Bot User OAuth Token.


* ### Налаштуйте OpenClaw

Рекомендоване налаштування SecretRef:

bashCopy code
[code]
    export SLACK_BOT_TOKEN=xoxb-...export SLACK_SIGNING_SECRET=...cat > slack.http.patch.json5 <<'JSON5'{channels: {slack: {enabled: true,mode: "http",botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },signingSecret: { source: "env", provider: "default", id: "SLACK_SIGNING_SECRET" },webhookPath: "/slack/events",},},}JSON5openclaw config patch --file ./slack.http.patch.json5 --dry-runopenclaw config patch --file ./slack.http.patch.json5
[/code]

* ### Запустіть Gateway

bashCopy code
[code]
    openclaw gateway
[/code]

## Налаштування транспорту Socket Mode

OpenClaw типово встановлює для клієнта Slack SDK тайм-аут pong у 15 секунд для Socket Mode. Перевизначайте налаштування транспорту лише тоді, коли потрібне налаштування під конкретний робочий простір або хост:

json5Copy code
[code]
    {  channels: {    slack: {      mode: "socket",      socketMode: {        clientPingTimeout: 20000,        serverPingTimeout: 30000,        pingPongLoggingEnabled: false,      },    },  },}
[/code]

Використовуйте це лише для робочих просторів Socket Mode, які журналюють тайм-аути Slack websocket pong/server-ping, або працюють на хостах із відомим блокуванням event loop. `clientPingTimeout` — це час очікування pong після того, як SDK надсилає клієнтський ping; `serverPingTimeout` — час очікування ping від сервера Slack. Повідомлення й події застосунку залишаються станом застосунку, а не сигналами життєздатності транспорту.

## Контрольний список маніфесту й областей доступу

Базовий маніфест застосунку Slack однаковий для Socket Mode і HTTP Request URLs. Відрізняється лише блок `settings` (і `url` slash-команди).

Базовий маніфест (типово Socket Mode):

jsonCopy code
[code]
    {  "display_information": {    "name": "OpenClaw",    "description": "Slack connector for OpenClaw"  },  "features": {    "bot_user": { "display_name": "OpenClaw", "always_online": true },    "app_home": {      "home_tab_enabled": true,      "messages_tab_enabled": true,      "messages_tab_read_only_enabled": false    },    "slash_commands": [      {        "command": "/openclaw",        "description": "Send a message to OpenClaw",        "should_escape": false      }    ]  },  "oauth_config": {    "scopes": {      "bot": [        "app_mentions:read",        "assistant:write",        "channels:history",        "channels:read",        "chat:write",        "commands",        "emoji:read",        "files:read",        "files:write",        "groups:history",        "groups:read",        "im:history",        "im:read",        "im:write",        "mpim:history",        "mpim:read",        "mpim:write",        "pins:read",        "pins:write",        "reactions:read",        "reactions:write",        "usergroups:read",        "users:read"      ]    }  },  "settings": {    "socket_mode_enabled": true,    "event_subscriptions": {      "bot_events": [        "app_home_opened",        "app_mention",        "channel_rename",        "member_joined_channel",        "member_left_channel",        "message.channels",        "message.groups",        "message.im",        "message.mpim",        "pin_added",        "pin_removed",        "reaction_added",        "reaction_removed"      ]    }  }}
[/code]

Для режиму **HTTP Request URLs** замініть `settings` на HTTP-варіант і додайте `url` до кожної slash-команди. Потрібен публічний URL:

jsonCopy code
[code]
    {  "features": {    "slash_commands": [      {        "command": "/openclaw",        "description": "Send a message to OpenClaw",        "should_escape": false,        "url": "https://gateway-host.example.com/slack/events"      }    ]  },  "settings": {    "event_subscriptions": {      "request_url": "https://gateway-host.example.com/slack/events",      "bot_events": [        "app_home_opened",        "app_mention",        "channel_rename",        "member_joined_channel",        "member_left_channel",        "message.channels",        "message.groups",        "message.im",        "message.mpim",        "pin_added",        "pin_removed",        "reaction_added",        "reaction_removed"      ]    },    "interactivity": {      "is_enabled": true,      "request_url": "https://gateway-host.example.com/slack/events",      "message_menu_options_url": "https://gateway-host.example.com/slack/events"    }  }}
[/code]

### Додаткові налаштування маніфесту

Відкрийте різні функції, що розширюють наведені вище типові значення.

Типовий маніфест вмикає вкладку Slack App Home **Home** і підписується на `app_home_opened`. Коли учасник робочого простору відкриває вкладку Home, OpenClaw публікує безпечний типовий Home view через `views.publish`; payload розмови або приватна конфігурація не включаються. Вкладка **Messages** залишається ввімкненою для Slack DM.

Необов’язкові нативні slash-команди

Можна використовувати кілька нативних slash-команд замість однієї налаштованої команди, з такими нюансами:

  * Використовуйте `/agentstatus` замість `/status`, оскільки команда `/status` зарезервована.
  * Одночасно можна зробити доступними не більше ніж 25 slash-команд.


Замініть наявний розділ `features.slash_commands` підмножиною [доступних команд](</uk/tools/slash-commands#command-list>):

### Socket Mode (типово)

jsonCopy code
[code]
    {"slash_commands": [{"command": "/new","description": "Start a new session","usage_hint": "[model]"},{"command": "/reset","description": "Reset the current session"},{"command": "/compact","description": "Compact the session context","usage_hint": "[instructions]"},{"command": "/stop","description": "Stop the current run"},{"command": "/session","description": "Manage thread-binding expiry","usage_hint": "idle <duration|off> or max-age <duration|off>"},{"command": "/think","description": "Set the thinking level","usage_hint": "<level>"},{"command": "/verbose","description": "Toggle verbose output","usage_hint": "on|off|full"},{"command": "/fast","description": "Show or set fast mode","usage_hint": "[status|on|off]"},{"command": "/reasoning","description": "Toggle reasoning visibility","usage_hint": "[on|off|stream]"},{"command": "/elevated","description": "Toggle elevated mode","usage_hint": "[on|off|ask|full]"},{"command": "/exec","description": "Show or set exec defaults","usage_hint": "host=<auto|sandbox|gateway|node> security=<deny|allowlist|full> ask=<off|on-miss|always> node=<id>"},{"command": "/model","description": "Show or set the model","usage_hint": "[name|#|status]"},{"command": "/models","description": "List providers/models","usage_hint": "[provider] [page] [limit=<n>|size=<n>|all]"},{"command": "/help","description": "Show the short help summary"},{"command": "/commands","description": "Show the generated command catalog"},{"command": "/tools","description": "Show what the current agent can use right now","usage_hint": "[compact|verbose]"},{"command": "/agentstatus","description": "Show runtime status, including provider usage/quota when available"},{"command": "/tasks","description": "List active/recent background tasks for the current session"},{"command": "/context","description": "Explain how context is assembled","usage_hint": "[list|detail|json]"},{"command": "/whoami","description": "Show your sender identity"},{"command": "/skill","description": "Run a skill by name","usage_hint": "<name> [input]"},{"command": "/btw","description": "Ask a side question without changing session context","usage_hint": "<question>"},{"command": "/side","description": "Ask a side question without changing session context","usage_hint": "<question>"},{"command": "/usage","description": "Control the usage footer or show cost summary","usage_hint": "off|tokens|full|cost"}]}
[/code]

### HTTP Request URLs

Використовуйте той самий список `slash_commands`, що й для Socket Mode вище, і додайте `"url": "https://gateway-host.example.com/slack/events"` до кожного запису. Приклад:

jsonCopy code
[code]
    {"slash_commands": [{"command": "/new","description": "Start a new session","usage_hint": "[model]","url": "https://gateway-host.example.com/slack/events"},{"command": "/help","description": "Show the short help summary","url": "https://gateway-host.example.com/slack/events"}]}
[/code]

Повторіть це значення `url` для кожної команди в списку.

Необов’язкові області авторства (операції запису)

Додайте область бота `chat:write.customize`, якщо хочете, щоб вихідні повідомлення використовували ідентичність активного агента (власне ім’я користувача та іконку) замість типової ідентичності застосунку Slack.

Якщо ви використовуєте іконку emoji, Slack очікує синтаксис `:emoji_name:`.

Необов’язкові області токена користувача (операції читання)

Якщо ви налаштовуєте `channels.slack.userToken`, типові області читання такі:

  * `channels:history`, `groups:history`, `im:history`, `mpim:history`
  * `channels:read`, `groups:read`, `im:read`, `mpim:read`
  * `users:read`
  * `reactions:read`
  * `pins:read`
  * `emoji:read`
  * `search:read` (якщо ви покладаєтеся на читання пошуку Slack)


## Модель токенів

  * `botToken` \+ `appToken` обов’язкові для Socket Mode.
  * HTTP-режим потребує `botToken` \+ `signingSecret`.
  * `botToken`, `appToken`, `signingSecret` і `userToken` приймають текстові рядки або об’єкти SecretRef.
  * Токени конфігурації перевизначають резервні значення env.
  * Резервні значення env `SLACK_BOT_TOKEN` / `SLACK_APP_TOKEN` застосовуються лише до типового облікового запису.
  * `userToken` (`xoxp-...`) налаштовується лише через конфігурацію (без резервного env) і типово має поведінку лише для читання (`userTokenReadOnly: true`).


Поведінка знімка стану:

  * Перевірка облікового запису Slack відстежує для кожних облікових даних поля `*Source` і `*Status` (`botToken`, `appToken`, `signingSecret`, `userToken`).
  * Стан може бути `available`, `configured_unavailable` або `missing`.
  * `configured_unavailable` означає, що обліковий запис налаштовано через SecretRef або інше неінлайнове джерело секретів, але поточна команда чи шлях виконання не змогли отримати фактичне значення.
  * У HTTP-режимі включено `signingSecretStatus`; у Socket Mode обов’язковою парою є `botTokenStatus` \+ `appTokenStatus`.


## Дії та шлюзи

Дії Slack керуються через `channels.slack.actions.*`.

Доступні групи дій у поточних інструментах Slack:

Група | Типово  
---|---  
messages | увімкнено  
reactions | увімкнено  
pins | увімкнено  
memberInfo | увімкнено  
emojiList | увімкнено  
  
Поточні дії повідомлень Slack включають `send`, `upload-file`, `download-file`, `read`, `edit`, `delete`, `pin`, `unpin`, `list-pins`, `member-info` і `emoji-list`. `download-file` приймає ID файлів Slack, показані у вхідних заповнювачах файлів, і повертає попередні перегляди зображень для зображень або локальні метадані файлів для інших типів файлів.

## Контроль доступу та маршрутизація

### Політика DM

`channels.slack.dmPolicy` керує доступом DM. `channels.slack.allowFrom` є канонічним списком дозволених DM.

  * `pairing` (типово)
  * `allowlist`
  * `open` (потребує, щоб `channels.slack.allowFrom` містив `"*"`)
  * `disabled`


Прапорці DM:

  * `dm.enabled` (типово true)
  * `channels.slack.allowFrom`
  * `dm.allowFrom` (застаріле)
  * `dm.groupEnabled` (групові DM типово false)
  * `dm.groupChannels` (необов’язковий список дозволених MPIM)


Пріоритет для кількох облікових записів:

  * `channels.slack.accounts.default.allowFrom` застосовується лише до облікового запису `default`.
  * Іменовані облікові записи успадковують `channels.slack.allowFrom`, коли їхній власний `allowFrom` не задано.
  * Іменовані облікові записи не успадковують `channels.slack.accounts.default.allowFrom`.


Застарілі `channels.slack.dm.policy` і `channels.slack.dm.allowFrom` все ще читаються для сумісності. `openclaw doctor --fix` переносить їх у `dmPolicy` і `allowFrom`, коли може зробити це без зміни доступу.

Сполучення в DM використовує `openclaw pairing approve slack <code>`.

### Політика каналів

`channels.slack.groupPolicy` керує обробкою каналів:

  * `open`
  * `allowlist`
  * `disabled`


Список дозволених каналів міститься в `channels.slack.channels` і **має використовувати стабільні ID каналів Slack** (наприклад, `C12345678`) як ключі конфігурації.

Примітка щодо виконання: якщо `channels.slack` повністю відсутній (налаштування лише через env), runtime повертається до `groupPolicy="allowlist"` і записує попередження в журнал (навіть якщо задано `channels.defaults.groupPolicy`).

Розпізнавання імені/ID:

  * записи списку дозволених каналів і записи списку дозволених DM розпізнаються під час запуску, коли доступ токена це дозволяє
  * нерозпізнані записи імен каналів зберігаються як налаштовані, але типово ігноруються для маршрутизації
  * вхідна авторизація та маршрутизація каналів типово спершу використовують ID; прямий збіг за іменем користувача/slug потребує `channels.slack.dangerouslyAllowNameMatching: true`


### Згадки та користувачі каналів

Повідомлення в каналах типово пропускаються через шлюз згадок.

Джерела згадок:

  * явна згадка застосунку (`<@botId>`)
  * згадка групи користувачів Slack (`<!subteam^S...>`), коли користувач-бот є учасником цієї групи користувачів; потребує `usergroups:read`
  * regex-шаблони згадок (`agents.list[].groupChat.mentionPatterns`, резервно `messages.groupChat.mentionPatterns`)
  * неявна поведінка відповіді в треді бота (вимкнено, коли `thread.requireExplicitMention` має значення `true`)


Поканальні засоби керування (`channels.slack.channels.<id>`; імена лише через розпізнавання під час запуску або `dangerouslyAllowNameMatching`):

  * `requireMention`
  * `users` (список дозволених)
  * `allowBots`
  * `skills`
  * `systemPrompt`
  * `tools`, `toolsBySender`
  * формат ключа `toolsBySender`: `channel:`, `id:`, `e164:`, `username:`, `name:` або wildcard `"*"` (застарілі ключі без префікса все ще зіставляються лише з `id:`)


`allowBots` є консервативним для каналів і приватних каналів: повідомлення кімнати, написані ботом, приймаються лише коли бота-відправника явно перелічено в списку дозволених `users` цієї кімнати або коли принаймні один явний ID власника Slack з `channels.slack.allowFrom` наразі є учасником кімнати. Wildcard і записи власників за відображуваними іменами не задовольняють наявність власника. Наявність власника використовує Slack `conversations.members`; переконайтеся, що застосунок має відповідну область читання для типу кімнати (`channels:read` для публічних каналів, `groups:read` для приватних каналів). Якщо пошук учасників не вдається, OpenClaw відкидає повідомлення кімнати, написане ботом.

## Треди, сесії та теги відповіді

  * DM маршрутизуються як `direct`; канали як `channel`; MPIM як `group`.
  * Прив’язки маршрутів Slack приймають сирі ID співрозмовників, а також форми цілей Slack, як-от `channel:C12345678`, `user:U12345678` і `<@U12345678>`.
  * З типовим `session.dmScope=main` DM Slack згортаються до основної сесії агента.
  * Сесії каналів: `agent:<agentId>:slack:channel:<channelId>`.
  * Відповіді в тредах можуть створювати суфікси сесій тредів (`:thread:<threadTs>`), коли це застосовно.
  * У каналах, де OpenClaw обробляє повідомлення верхнього рівня без вимоги явної згадки, не-`off` `replyToMode` маршрутизує кожен оброблений кореневий елемент у `agent:<agentId>:slack:channel:<channelId>:thread:<rootTs>`, щоб видимий тред Slack від першого ходу відповідав одній сесії OpenClaw.
  * Типове значення `channels.slack.thread.historyScope` — `thread`; типове значення `thread.inheritParent` — `false`.
  * `channels.slack.thread.initialHistoryLimit` керує тим, скільки наявних повідомлень треду завантажується, коли починається нова сесія треду (типово `20`; задайте `0`, щоб вимкнути).
  * `channels.slack.thread.requireExplicitMention` (типово `false`): коли `true`, пригнічує неявні згадки в треді, щоб бот відповідав лише на явні згадки `@bot` усередині тредів, навіть коли бот уже брав участь у треді. Без цього відповіді в треді, де брав участь бот, обходять шлюз `requireMention`.


Засоби керування відповідями в тредах:

  * `channels.slack.replyToMode`: `off|first|all|batched` (типово `off`)
  * `channels.slack.replyToModeByChatType`: для кожного `direct|group|channel`
  * застарілий резервний варіант для прямих чатів: `channels.slack.dm.replyToMode`


Підтримуються ручні теги відповіді:

  * `[[reply_to_current]]`
  * `[[reply_to:<id>]]`


Для явних відповідей у тредах Slack з інструмента `message` задайте `replyBroadcast: true` з `action: "send"` і `threadId` або `replyTo`, щоб попросити Slack також транслювати відповідь треду в батьківський канал. Це зіставляється з прапорцем `reply_broadcast` Slack `chat.postMessage` і підтримується лише для текстових або Block Kit надсилань, не для завантажень медіа.

Коли виклик інструмента `message` виконується всередині треду Slack і націлений на той самий канал, OpenClaw зазвичай успадковує поточний тред Slack відповідно до `replyToMode`. Задайте `topLevel: true` для `action: "send"` або `action: "upload-file"`, щоб натомість примусово створити нове повідомлення в батьківському каналі. `threadId: null` приймається як такий самий вихід на верхній рівень.

## Реакції підтвердження

`ackReaction` надсилає emoji підтвердження, поки OpenClaw обробляє вхідне повідомлення.

Порядок розв’язання:

  * `channels.slack.accounts.<accountId>.ackReaction`
  * `channels.slack.ackReaction`
  * `messages.ackReaction`
  * резервний emoji ідентичності агента (`agents.list[].identity.emoji`, інакше "👀")


Примітки:

  * Slack очікує shortcodes (наприклад, `"eyes"`).
  * Використовуйте `""`, щоб вимкнути реакцію для облікового запису Slack або глобально.


## Потокове передавання тексту

`channels.slack.streaming` керує поведінкою live preview:

  * `off`: вимкнути потокове передавання live preview.
  * `partial` (типово): замінювати текст попереднього перегляду найновішим частковим виводом.
  * `block`: додавати порційні оновлення попереднього перегляду.
  * `progress`: показувати текст стану перебігу під час генерації, потім надсилати фінальний текст.
  * `streaming.preview.toolProgress`: коли активний чернетковий попередній перегляд, спрямовувати оновлення інструментів/перебігу в те саме редаговане повідомлення попереднього перегляду (типово: `true`). Задайте `false`, щоб зберігати окремі повідомлення інструментів/перебігу.
  * `streaming.preview.commandText` / `streaming.progress.commandText`: задайте `status`, щоб зберігати компактні рядки перебігу інструментів, приховуючи сирий текст command/exec (типово: `raw`).


Приховати сирий текст command/exec, зберігаючи компактні рядки перебігу:

jsonCopy code
[code]
    {  "channels": {    "slack": {      "streaming": {        "mode": "progress",        "progress": {          "toolProgress": true,          "commandText": "status"        }      }    }  }}
[/code]

`channels.slack.streaming.nativeTransport` керує нативним потоковим передаванням тексту Slack, коли `channels.slack.streaming.mode` має значення `partial` (типово: `true`).

  * Ланцюжок відповіді має бути доступний, щоб з’являлися нативне потокове передавання тексту та статус ланцюжка помічника Slack. Вибір ланцюжка все одно відповідає `replyToMode`.
  * Корені каналів, групових чатів і DM верхнього рівня все ще можуть використовувати звичайний попередній перегляд чернетки, коли нативне потокове передавання недоступне або ланцюжка відповіді не існує.
  * DM Slack верхнього рівня за замовчуванням залишаються поза ланцюжками, тому вони не показують нативний потоковий перегляд/перегляд статусу у стилі ланцюжків Slack; натомість OpenClaw публікує та редагує попередній перегляд чернетки в DM.
  * Медіа та нетекстові корисні навантаження повертаються до звичайної доставки.
  * Фінальні медіа/помилки скасовують очікувані редагування попереднього перегляду; придатні фінальні текстові/блокові повідомлення скидаються лише тоді, коли можуть редагувати попередній перегляд на місці.
  * Якщо потокове передавання переривається посеред відповіді, OpenClaw повертається до звичайної доставки для решти корисних навантажень.


Використовуйте попередній перегляд чернетки замість нативного потокового передавання тексту Slack:

json5Copy code
[code]
    {  channels: {    slack: {      streaming: {        mode: "partial",        nativeTransport: false,      },    },  },}
[/code]

Застарілі ключі:

  * `channels.slack.streamMode` (`replace | status_final | append`) є застарілим runtime-псевдонімом для `channels.slack.streaming.mode`.
  * булевий `channels.slack.streaming` є застарілим runtime-псевдонімом для `channels.slack.streaming.mode` і `channels.slack.streaming.nativeTransport`.
  * застарілий `channels.slack.nativeStreaming` є runtime-псевдонімом для `channels.slack.streaming.nativeTransport`.
  * Запустіть `openclaw doctor --fix`, щоб переписати збережену конфігурацію потокового передавання Slack на канонічні ключі.


## Резервна реакція набору тексту

`typingReaction` додає тимчасову реакцію до вхідного повідомлення Slack, поки OpenClaw обробляє відповідь, а потім видаляє її після завершення запуску. Це найкорисніше поза відповідями у ланцюжках, які використовують стандартний індикатор статусу "is typing...".

Порядок визначення:

  * `channels.slack.accounts.<accountId>.typingReaction`
  * `channels.slack.typingReaction`


Примітки:

  * Slack очікує короткі коди (наприклад, `"hourglass_flowing_sand"`).
  * Реакція виконується за принципом best-effort, а очищення автоматично виконується після завершення відповіді або шляху помилки.


## Медіа, розбиття на частини та доставка

Inbound attachments

Файлові вкладення Slack завантажуються з приватних URL, розміщених у Slack (потік запитів з автентифікацією токеном), і записуються до сховища медіа, коли отримання успішне й обмеження розміру це дозволяють. Заповнювачі файлів містять Slack `fileId`, щоб агенти могли отримати оригінальний файл через `download-file`.

Завантаження використовують обмежені тайм-аути простою та загальні тайм-аути. Якщо отримання файлу Slack зависає або завершується помилкою, OpenClaw продовжує обробляти повідомлення та повертається до заповнювача файлу.

Runtime-обмеження розміру вхідних даних за замовчуванням становить `20MB`, якщо його не перевизначено через `channels.slack.mediaMaxMb`.

Outbound text and files

  * текстові частини використовують `channels.slack.textChunkLimit` (за замовчуванням 4000)
  * `channels.slack.chunkMode="newline"` вмикає розбиття з пріоритетом абзаців
  * надсилання файлів використовує API завантаження Slack і може включати відповіді у ланцюжках (`thread_ts`)
  * обмеження вихідних медіа відповідає `channels.slack.mediaMaxMb`, коли його налаштовано; інакше надсилання каналом використовує MIME-типові значення за замовчуванням із медіаконвеєра

Delivery targets

Бажані явні цілі:

  * `user:<id>` для DM
  * `channel:<id>` для каналів


DM Slack лише з текстом/блоками можуть публікуватися безпосередньо в ID користувачів; завантаження файлів і надсилання у ланцюжках спочатку відкривають DM через API розмов Slack, оскільки ці шляхи потребують конкретного ID розмови.

## Команди та поведінка слеш-команд

Слеш-команди відображаються в Slack або як одна налаштована команда, або як кілька нативних команд. Налаштуйте `channels.slack.slashCommand`, щоб змінити стандартні параметри команд:

  * `enabled: false`
  * `name: "openclaw"`
  * `sessionPrefix: "slack:slash"`
  * `ephemeral: true`

txtCopy code
[code]
    /openclaw /help
[/code]

Нативні команди потребують додаткових налаштувань маніфесту у вашому застосунку Slack і натомість вмикаються через `channels.slack.commands.native: true` або `commands.native: true` у глобальних конфігураціях.

  * Автоматичний режим нативних команд **вимкнено** для Slack, тому `commands.native: "auto"` не вмикає нативні команди Slack.

txtCopy code
[code]
    /help
[/code]

Нативні меню аргументів використовують адаптивну стратегію рендерингу, яка показує модальне вікно підтвердження перед надсиланням вибраного значення параметра:

  * до 5 параметрів: блоки кнопок
  * 6-100 параметрів: статичне меню вибору
  * понад 100 параметрів: зовнішній вибір з асинхронною фільтрацією параметрів, коли доступні обробники параметрів інтерактивності
  * перевищено обмеження Slack: закодовані значення параметрів повертаються до кнопок

txtCopy code
[code]
    /think
[/code]

Сеанси слеш-команд використовують ізольовані ключі на кшталт `agent:<agentId>:slack:slash:<userId>` і все одно спрямовують виконання команд до цільового сеансу розмови за допомогою `CommandTargetSessionKey`.

## Інтерактивні відповіді

Slack може відтворювати інтерактивні елементи керування відповідями, створені агентом, але ця функція за замовчуванням вимкнена.

Увімкніть її глобально:

json5Copy code
[code]
    {  channels: {    slack: {      capabilities: {        interactiveReplies: true,      },    },  },}
[/code]

Або увімкніть її лише для одного облікового запису Slack:

json5Copy code
[code]
    {  channels: {    slack: {      accounts: {        ops: {          capabilities: {            interactiveReplies: true,          },        },      },    },  },}
[/code]

Коли ввімкнено, агенти можуть видавати директиви відповідей лише для Slack:

  * `[[slack_buttons: Approve:approve, Reject:reject]]`
  * `[[slack_select: Choose a target | Canary:canary, Production:production]]`


Ці директиви компілюються у Slack Block Kit і маршрутизують кліки або вибори назад через наявний шлях подій взаємодії Slack.

Примітки:

  * Це UI, специфічний для Slack. Інші канали не перетворюють директиви Slack Block Kit на власні системи кнопок.
  * Значення інтерактивних зворотних викликів є непрозорими токенами, згенерованими OpenClaw, а не сирими значеннями, створеними агентом.
  * Якщо згенеровані інтерактивні блоки перевищили б ліміти Slack Block Kit, OpenClaw повертається до початкової текстової відповіді замість надсилання недійсного payload блоків.


## Підтвердження виконання у Slack

Slack може діяти як нативний клієнт підтверджень з інтерактивними кнопками та взаємодіями, замість повернення до Web UI або термінала.

  * Підтвердження виконання використовують `channels.slack.execApprovals.*` для нативної маршрутизації DM/каналу.
  * Підтвердження Plugin все ще можуть вирішуватися через ту саму нативну для Slack поверхню кнопок, коли запит уже потрапляє у Slack і тип ідентифікатора підтвердження є `plugin:`.
  * Авторизація затверджувачів усе ще застосовується: лише користувачі, визначені як затверджувачі, можуть схвалювати або відхиляти запити через Slack.


Це використовує ту саму спільну поверхню кнопок підтвердження, що й інші канали. Коли `interactivity` увімкнено в налаштуваннях вашого застосунку Slack, запити підтвердження відображаються як кнопки Block Kit безпосередньо в розмові. Коли ці кнопки присутні, вони є основним інтерфейсом підтвердження; OpenClaw має додавати ручну команду `/approve` лише тоді, коли результат інструмента вказує, що підтвердження в чаті недоступні або ручне підтвердження є єдиним шляхом.

Шлях конфігурації:

  * `channels.slack.execApprovals.enabled`
  * `channels.slack.execApprovals.approvers` (необов'язково; за можливості повертається до `commands.ownerAllowFrom`)
  * `channels.slack.execApprovals.target` (`dm` | `channel` | `both`, стандартно: `dm`)
  * `agentFilter`, `sessionFilter`


Slack автоматично вмикає нативні підтвердження виконання, коли `enabled` не задано або має значення `"auto"` і вдається визначити принаймні одного затверджувача. Задайте `enabled: false`, щоб явно вимкнути Slack як нативний клієнт підтверджень. Задайте `enabled: true`, щоб примусово ввімкнути нативні підтвердження, коли затверджувачів визначено.

Стандартна поведінка без явної конфігурації підтверджень виконання Slack:

json5Copy code
[code]
    {  commands: {    ownerAllowFrom: ["slack:U12345678"],  },}
[/code]

Явна нативна для Slack конфігурація потрібна лише тоді, коли потрібно перевизначити затверджувачів, додати фільтри або увімкнути доставку в початковий чат:

json5Copy code
[code]
    {  channels: {    slack: {      execApprovals: {        enabled: true,        approvers: ["U12345678"],        target: "both",      },    },  },}
[/code]

Спільне переспрямування `approvals.exec` є окремим. Використовуйте його лише тоді, коли запити підтвердження виконання також мають маршрутизуватися до інших чатів або явних позаканальних цілей. Спільне переспрямування `approvals.plugin` також є окремим; нативні кнопки Slack усе ще можуть вирішувати підтвердження Plugin, коли ці запити вже потрапляють у Slack.

Команда `/approve` у тому самому чаті також працює в каналах Slack і DM, які вже підтримують команди. Див. [Підтвердження виконання](</uk/tools/exec-approvals>) для повної моделі переспрямування підтверджень.

## Події та операційна поведінка

  * Редагування/видалення повідомлень перетворюються на системні події.
  * Трансляції гілок (відповіді в гілці "Також надіслати до каналу") обробляються як звичайні повідомлення користувача.
  * Події додавання/видалення реакцій перетворюються на системні події.
  * Події входу/виходу учасників, створення/перейменування каналів і додавання/видалення закріплень перетворюються на системні події.
  * `channel_id_changed` може мігрувати ключі конфігурації каналів, коли ввімкнено `configWrites`.
  * Метадані теми/призначення каналу вважаються недовіреним контекстом і можуть бути вставлені в контекст маршрутизації.
  * Ініціатор гілки та початкове заповнення контексту історії гілки фільтруються налаштованими списками дозволених відправників, коли це застосовно.
  * Дії блоків і модальні взаємодії видають структуровані системні події `Slack interaction: ...` з багатими полями payload: 
    * дії блоків: вибрані значення, мітки, значення селекторів і метадані `workflow_*`
    * події модальних `view_submission` і `view_closed` з маршрутизованими метаданими каналу та введенням форми


## Довідник конфігурації

Основний довідник: [Довідник конфігурації - Slack](</uk/gateway/config-channels#slack>).

Найважливіші поля Slack

  * режим/автентифікація: `mode`, `botToken`, `appToken`, `signingSecret`, `webhookPath`, `accounts.*`
  * доступ до DM: `dm.enabled`, `dmPolicy`, `allowFrom` (застаріле: `dm.policy`, `dm.allowFrom`), `dm.groupEnabled`, `dm.groupChannels`
  * перемикач сумісності: `dangerouslyAllowNameMatching` (аварійний; тримайте вимкненим, якщо не потрібно)
  * доступ до каналів: `groupPolicy`, `channels.*`, `channels.*.users`, `channels.*.requireMention`
  * гілки/історія: `replyToMode`, `replyToModeByChatType`, `thread.*`, `historyLimit`, `dmHistoryLimit`, `dms.*.historyLimit`
  * доставка: `textChunkLimit`, `chunkMode`, `mediaMaxMb`, `streaming`, `streaming.nativeTransport`, `streaming.preview.toolProgress`
  * розгортання прев'ю: `unfurlLinks`, `unfurlMedia` для керування прев'ю посилань/медіа `chat.postMessage`
  * операційні можливості/функції: `configWrites`, `commands.native`, `slashCommand.*`, `actions.*`, `userToken`, `userTokenReadOnly`


## Усунення несправностей

Немає відповідей у каналах

Перевірте по черзі:

  * `groupPolicy`
  * список дозволених каналів (`channels.slack.channels`) — **ключами мають бути ID каналів** (`C12345678`), а не назви (`#channel-name`). Ключі на основі назв непомітно не спрацьовують за `groupPolicy: "allowlist"`, бо маршрутизація каналів за замовчуванням спочатку використовує ID. Щоб знайти ID: клацніть канал у Slack правою кнопкою → **Копіювати посилання** — значення `C...` у кінці URL є ID каналу.
  * `requireMention`
  * список дозволених `users` для окремого каналу


Корисні команди:

bashCopy code
[code]
    openclaw channels status --probeopenclaw logs --followopenclaw doctor
[/code]

Повідомлення DM ігноруються

Перевірте:

  * `channels.slack.dm.enabled`
  * `channels.slack.dmPolicy` (або застаріле `channels.slack.dm.policy`)
  * підтвердження сполучення / записи списку дозволених
  * події DM Slack Assistant: докладні журнали зі згадкою `drop message_changed` зазвичай означають, що Slack надіслав відредаговану подію гілки Assistant без людського відправника, якого можна відновити з метаданих повідомлення

bashCopy code
[code]
    openclaw pairing list slack
[/code]

Socket Mode не підключається

Перевірте токени бота й застосунку та ввімкнення Socket Mode у налаштуваннях застосунку Slack.

Якщо `openclaw channels status --probe --json` показує `botTokenStatus` або `appTokenStatus: "configured_unavailable"`, обліковий запис Slack налаштовано, але поточне середовище виконання не змогло визначити значення, підкріплене SecretRef.

Режим HTTP не отримує події

Перевірте:

  * секрет підписування
  * шлях webhook
  * URL-адреси запитів Slack (події + інтерактивність + слеш-команди)
  * унікальний `webhookPath` для кожного облікового запису HTTP


Якщо `signingSecretStatus: "configured_unavailable"` з’являється у знімках облікового запису, обліковий запис HTTP налаштовано, але поточне середовище виконання не змогло розв’язати секрет підписування на основі SecretRef.

Нативні/слеш-команди не спрацьовують

Перевірте, що саме ви мали на увазі:

  * режим нативних команд (`channels.slack.commands.native: true`) із відповідними слеш-командами, зареєстрованими в Slack
  * або режим однієї слеш-команди (`channels.slack.slashCommand.enabled: true`)


Також перевірте `commands.useAccessGroups` і списки дозволених каналів/користувачів.

## Довідка щодо зору для вкладень

Slack може прикріплювати завантажені медіа до ходу агента, коли завантаження файлів Slack успішне та це дозволяють обмеження розміру. Файли зображень можна передавати через шлях розуміння медіа або безпосередньо до моделі відповіді з підтримкою зору; інші файли зберігаються як контекст файлів, доступних для завантаження, а не обробляються як вхідні зображення.

### Підтримувані типи медіа

Тип медіа | Джерело | Поточна поведінка | Примітки  
---|---|---|---  
Зображення JPEG / PNG / GIF / WebP | URL файлу Slack | Завантажуються та прикріплюються до ходу для обробки з підтримкою зору | Обмеження на файл: `channels.slack.mediaMaxMb` (типово 20 МБ)  
PDF-файли | URL файлу Slack | Завантажуються та надаються як файловий контекст для інструментів, як-от `download-file` або `pdf` | Вхідний Slack автоматично не перетворює PDF на вхідні дані для зору зображень  
Інші файли | URL файлу Slack | Завантажуються, коли це можливо, і надаються як файловий контекст | Бінарні файли не обробляються як вхідні зображення  
Відповіді в тредах | Файли початкового повідомлення треду | Файли кореневого повідомлення можуть бути додані як контекст, коли відповідь не має прямих медіа | Початкові повідомлення лише з файлами використовують заповнювач вкладення  
Повідомлення з кількома зображеннями | Кілька файлів Slack | Кожен файл оцінюється незалежно | Обробка Slack обмежена вісьмома файлами на повідомлення  
  
### Вхідний конвеєр

Коли надходить повідомлення Slack із файловими вкладеннями:

  1. OpenClaw завантажує файл із приватної URL-адреси Slack за допомогою токена бота (`xoxb-...`).
  2. У разі успіху файл записується до сховища медіа.
  3. Шляхи завантажених медіа та типи вмісту додаються до вхідного контексту.
  4. Шляхи моделей/інструментів із підтримкою зображень можуть використовувати вкладення зображень із цього контексту.
  5. Файли, що не є зображеннями, залишаються доступними як файлові метадані або медіапосилання для інструментів, які можуть їх обробляти.


### Успадкування вкладень кореневого повідомлення треду

Коли повідомлення надходить у тред (має батьківський `thread_ts`):

  * Якщо сама відповідь не має прямих медіа, а включене кореневе повідомлення має файли, Slack може додати кореневі файли як контекст початкового повідомлення треду.
  * Прямі вкладення відповіді мають пріоритет над вкладеннями кореневого повідомлення.
  * Кореневе повідомлення, яке має лише файли й не має тексту, представляється із заповнювачем вкладення, щоб резервний механізм усе одно міг включити його файли.


### Обробка кількох вкладень

Коли одне повідомлення Slack містить кілька файлових вкладень:

  * Кожне вкладення обробляється незалежно через медіаконвеєр.
  * Посилання на завантажені медіа агрегуються в контекст повідомлення.
  * Порядок обробки відповідає порядку файлів Slack у корисному навантаженні події.
  * Помилка завантаження одного вкладення не блокує інші.


### Обмеження розміру, завантаження та моделей

  * **Обмеження розміру** : типово 20 МБ на файл. Налаштовується через `channels.slack.mediaMaxMb`.
  * **Помилки завантаження** : файли, які Slack не може надати, протерміновані URL-адреси, недоступні файли, завеликі файли та HTML-відповіді автентифікації/входу Slack пропускаються, а не повідомляються як непідтримувані формати.
  * **Модель зору** : аналіз зображень використовує активну модель відповіді, коли вона підтримує зір, або модель зображень, налаштовану в `agents.defaults.imageModel`.


### Відомі обмеження

Сценарій | Поточна поведінка | Обхідний шлях  
---|---|---  
Протермінована URL-адреса файлу Slack | Файл пропускається; помилка не показується | Повторно завантажте файл у Slack  
Модель зору не налаштована | Вкладення зображень зберігаються як медіапосилання, але не аналізуються як зображення | Налаштуйте `agents.defaults.imageModel` або використайте модель відповіді з підтримкою зору  
Дуже великі зображення (> 20 МБ типово) | Пропускаються відповідно до обмеження розміру | Збільште `channels.slack.mediaMaxMb`, якщо Slack дозволяє  
Переслані/поширені вкладення | Текст і розміщені в Slack зображення/файлові медіа обробляються за найкращою спробою | Поділіться ними напряму в треді OpenClaw  
PDF-вкладення | Зберігаються як файловий/медіаконтекст, але автоматично не спрямовуються через зір зображень | Використайте `download-file` для файлових метаданих або інструмент `pdf` для аналізу PDF  
  
### Пов’язана документація

  * [Конвеєр розуміння медіа](</uk/nodes/media-understanding>)
  * [Інструмент PDF](</uk/tools/pdf>)
  * Епік: [#51349](<https://github.com/openclaw/openclaw/issues/51349>) — увімкнення зору для вкладень Slack
  * Регресійні тести: [#51353](<https://github.com/openclaw/openclaw/issues/51353>)
  * Жива перевірка: [#51354](<https://github.com/openclaw/openclaw/issues/51354>)


## Пов’язане

[**Спарювання** Спаруйте користувача Slack із gateway. ](</uk/channels/pairing>) [**Групи** Поведінка каналу та групових DM. ](</uk/channels/groups>) [**Маршрутизація каналів** Маршрутизуйте вхідні повідомлення до агентів. ](</uk/channels/channel-routing>) [**Безпека** Модель загроз і посилення захисту. ](</uk/gateway/security>) [**Конфігурація** Структура конфігурації та пріоритетність. ](</uk/gateway/configuration>) [**Слеш-команди** Каталог команд і поведінка. ](</uk/tools/slash-commands>)

Was this useful?YesNo