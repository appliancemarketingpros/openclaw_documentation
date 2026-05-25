---
title: Багатоагентна маршрутизація
source_url: https://docs.openclaw.ai/uk/concepts/multi-agent
scraped_at: 2026-05-25
---

Запускайте кілька _ізольованих_ агентів — кожен із власним робочим простором, каталогом стану (`agentDir`) та історією сесій — а також кілька облікових записів каналів (наприклад, два WhatsApp) в одному запущеному Gateway. Вхідні повідомлення маршрутизуються до потрібного агента через прив’язки.

**Агент** тут — це повна область окремої персони: файли робочого простору, профілі автентифікації, реєстр моделей і сховище сесій. `agentDir` — це каталог стану на диску, який містить цю конфігурацію для кожного агента за шляхом `~/.openclaw/agents/<agentId>/`. **Прив’язка** зіставляє обліковий запис каналу (наприклад, робочий простір Slack або номер WhatsApp) з одним із цих агентів.

## Що таке «один агент»?

**Агент** — це повністю ізольований «мозок» із власними:

  * **Робочим простором** (файли, [AGENTS.md/SOUL.md/USER.md](<http://AGENTS.md/SOUL.md/USER.md>), локальні нотатки, правила персони).
  * **Каталогом стану** (`agentDir`) для профілів автентифікації, реєстру моделей і конфігурації для кожного агента.
  * **Сховищем сесій** (історія чатів + стан маршрутизації) у `~/.openclaw/agents/<agentId>/sessions`.


Профілі автентифікації є **окремими для кожного агента**. Кожен агент читає зі свого власного:

textCopy code
[code]
    ~/.openclaw/agents/<agentId>/agent/auth-profiles.json
[/code]

Skills завантажуються з робочого простору кожного агента, а також зі спільних коренів, таких як `~/.openclaw/skills`, а потім фільтруються за ефективним allowlist Skills агента, якщо його налаштовано. Використовуйте `agents.defaults.skills` для спільної бази та `agents.list[].skills` для заміни на рівні агента. Див. [Skills: на рівні агента чи спільні](</uk/tools/skills#per-agent-vs-shared-skills>) і [Skills: allowlist Skills агента](</uk/tools/skills#agent-skill-allowlists>).

Gateway може розміщувати **одного агента** (стандартно) або **багатьох агентів** поруч.

## Шляхи (швидка мапа)

  * Конфігурація: `~/.openclaw/openclaw.json` (або `OPENCLAW_CONFIG_PATH`)
  * Каталог стану: `~/.openclaw` (або `OPENCLAW_STATE_DIR`)
  * Робочий простір: `~/.openclaw/workspace` (або `~/.openclaw/workspace-<agentId>`)
  * Каталог агента: `~/.openclaw/agents/<agentId>/agent` (або `agents.list[].agentDir`)
  * Сесії: `~/.openclaw/agents/<agentId>/sessions`


### Режим одного агента (стандартно)

Якщо ви нічого не змінюєте, OpenClaw запускає одного агента:

  * `agentId` стандартно має значення **`main`**.
  * Сесії ключуються як `agent:main:<mainKey>`.
  * Робочий простір стандартно має шлях `~/.openclaw/workspace` (або `~/.openclaw/workspace-<profile>`, коли встановлено `OPENCLAW_PROFILE`).
  * Стан стандартно має шлях `~/.openclaw/agents/main/agent`.


## Помічник агента

Використайте майстер агентів, щоб додати нового ізольованого агента:

bashCopy code
[code]
    openclaw agents add work
[/code]

Потім додайте `bindings` (або дозвольте майстру зробити це), щоб маршрутизувати вхідні повідомлення.

Перевірте за допомогою:

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

## Швидкий старт

* ### Create each agent workspace

Використайте майстер або створіть робочі простори вручну:

bashCopy code
[code]
    openclaw agents add codingopenclaw agents add social
[/code]

Кожен агент отримує власний робочий простір із `SOUL.md`, `AGENTS.md` і необов’язковим `USER.md`, а також окремий `agentDir` і сховище сесій у `~/.openclaw/agents/<agentId>`.

* ### Create channel accounts

Створіть один обліковий запис на агента у вибраних каналах:

  * Discord: один бот на агента, увімкніть Message Content Intent, скопіюйте кожен токен.
  * Telegram: один бот на агента через BotFather, скопіюйте кожен токен.
  * WhatsApp: прив’яжіть кожен номер телефону для кожного облікового запису.

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account work
[/code]

Див. посібники каналів: [Discord](</uk/channels/discord>), [Telegram](</uk/channels/telegram>), [WhatsApp](</uk/channels/whatsapp>).

* ### Add agents, accounts, and bindings

Додайте агентів у `agents.list`, облікові записи каналів у `channels.<channel>.accounts` і з’єднайте їх за допомогою `bindings` (приклади нижче).

* ### Restart and verify

bashCopy code
[code]
    openclaw gateway restartopenclaw agents list --bindingsopenclaw channels status --probe
[/code]

## Кілька агентів = кілька людей, кілька особистостей

З **кількома агентами** кожен `agentId` стає **повністю ізольованою персоною** :

  * **Різні номери телефонів/облікові записи** (для кожного каналу `accountId`).
  * **Різні особистості** (файли робочого простору для кожного агента, як-от `AGENTS.md` і `SOUL.md`).
  * **Окрема автентифікація + сесії** (без перетину, якщо його явно не ввімкнено).


Це дає змогу **кільком людям** спільно використовувати один сервер Gateway, зберігаючи їхні AI-«мозки» та дані ізольованими.

## Пошук QMD-пам’яті між агентами

Якщо один агент має шукати в стенограмах QMD-сесій іншого агента, додайте додаткові колекції в `agents.list[].memorySearch.qmd.extraCollections`. Використовуйте `agents.defaults.memorySearch.qmd.extraCollections` лише тоді, коли кожен агент має успадковувати ті самі спільні колекції стенограм.

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/workspaces/main",      memorySearch: {        qmd: {          extraCollections: [{ path: "~/agents/family/sessions", name: "family-sessions" }],        },      },    },    list: [      {        id: "main",        workspace: "~/workspaces/main",        memorySearch: {          qmd: {            extraCollections: [{ path: "notes" }], // resolves inside workspace -> collection named "notes-main"          },        },      },      { id: "family", workspace: "~/workspaces/family" },    ],  },  memory: {    backend: "qmd",    qmd: { includeDefaultMemory: false },  },}
[/code]

Шлях додаткової колекції може бути спільним для агентів, але назва колекції залишається явною, коли шлях розташований поза робочим простором агента. Шляхи всередині робочого простору залишаються обмеженими агентом, тож кожен агент зберігає власний набір пошуку стенограм.

## Один номер WhatsApp, кілька людей (розділення DM)

Ви можете маршрутизувати **різні DM WhatsApp** до різних агентів, залишаючись на **одному обліковому записі WhatsApp**. Зіставляйте за відправником E.164 (наприклад, `+15551234567`) з `peer.kind: "direct"`. Відповіді все одно надходять із того самого номера WhatsApp (без окремої ідентичності відправника для кожного агента).

Приклад:

json5Copy code
[code]
    {  agents: {    list: [      { id: "alex", workspace: "~/.openclaw/workspace-alex" },      { id: "mia", workspace: "~/.openclaw/workspace-mia" },    ],  },  bindings: [    {      agentId: "alex",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230001" } },    },    {      agentId: "mia",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230002" } },    },  ],  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551230001", "+15551230002"],    },  },}
[/code]

Нотатки:

  * Контроль доступу DM є **глобальним для облікового запису WhatsApp** (сполучення/allowlist), а не для кожного агента.
  * Для спільних груп прив’яжіть групу до одного агента або використовуйте [групи розсилання](</uk/channels/broadcast-groups>).


## Правила маршрутизації (як повідомлення вибирають агента)

Прив’язки є **детермінованими** , і **найспецифічніша перемагає** :

* ### peer match

Точний ідентифікатор DM/групи/каналу.

* ### parentPeer match

Успадкування треду.

* ### guildId + roles

Маршрутизація ролей Discord.

* ### guildId

Discord.

* ### teamId

Slack.

* ### accountId match for a channel

Резервний варіант для облікового запису.

* ### Channel-level match

`accountId: "*"`.

* ### Default agent

Резервний перехід до `agents.list[].default`, інакше перший запис списку, стандартно: `main`.

Tie-breaking and AND semantics

  * Якщо кілька прив’язок збігаються на тому самому рівні, перемагає перша в порядку конфігурації.
  * Якщо прив’язка задає кілька полів збігу (наприклад, `peer` \+ `guildId`), потрібні всі указані поля (семантика `AND`).

Account-scope detail

  * Прив’язка, яка пропускає `accountId`, збігається лише зі стандартним обліковим записом.
  * Використовуйте `accountId: "*"` для резервного варіанта на весь канал для всіх облікових записів.
  * Якщо пізніше ви додасте ту саму прив’язку для того самого агента з явним ідентифікатором облікового запису, OpenClaw оновить наявну прив’язку лише на рівні каналу до обмеженої обліковим записом, а не дублюватиме її.


## Кілька облікових записів / номерів телефонів

Канали, що підтримують **кілька облікових записів** (наприклад, WhatsApp), використовують `accountId` для ідентифікації кожного входу. Кожен `accountId` можна маршрутизувати до іншого агента, тож один сервер може розміщувати кілька номерів телефонів без змішування сесій.

Якщо вам потрібен стандартний обліковий запис на рівні каналу, коли `accountId` пропущено, задайте `channels.<channel>.defaultAccount` (необов’язково). Якщо його не задано, OpenClaw повертається до `default`, якщо він є, інакше до першого налаштованого ідентифікатора облікового запису (відсортовано).

Поширені канали, що підтримують цей шаблон, включають:

  * `whatsapp`, `telegram`, `discord`, `slack`, `signal`, `imessage`
  * `irc`, `line`, `googlechat`, `mattermost`, `matrix`, `nextcloud-talk`
  * `zalo`, `zalouser`, `nostr`, `feishu`


## Поняття

  * `agentId`: один «мозок» (робочий простір, автентифікація для кожного агента, сховище сесій для кожного агента).
  * `accountId`: один екземпляр облікового запису каналу (наприклад, обліковий запис WhatsApp `"personal"` проти `"biz"`).
  * `binding`: маршрутизує вхідні повідомлення до `agentId` за `(channel, accountId, peer)` і необов’язково ідентифікаторами гільдії/команди.
  * Прямі чати згортаються до `agent:<agentId>:<mainKey>` («main» для кожного агента; `session.mainKey`).


## Приклади платформ

Discord bots per agent

Кожен обліковий запис бота Discord зіставляється з унікальним `accountId`. Прив’яжіть кожен обліковий запис до агента й зберігайте allowlist окремо для кожного бота.

json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "coding", workspace: "~/.openclaw/workspace-coding" },    ],  },  bindings: [    { agentId: "main", match: { channel: "discord", accountId: "default" } },    { agentId: "coding", match: { channel: "discord", accountId: "coding" } },  ],  channels: {    discord: {      groupPolicy: "allowlist",      accounts: {        default: {          token: "DISCORD_BOT_TOKEN_MAIN",          guilds: {            "123456789012345678": {              channels: {                "222222222222222222": { allow: true, requireMention: false },              },            },          },        },        coding: {          token: "DISCORD_BOT_TOKEN_CODING",          guilds: {            "123456789012345678": {              channels: {                "333333333333333333": { allow: true, requireMention: false },              },            },          },        },      },    },  },}
[/code]

  * Запросіть кожного бота до гільдії та ввімкніть Message Content Intent.
  * Токени зберігаються в `channels.discord.accounts.<id>.token` (обліковий запис за замовчуванням може використовувати `DISCORD_BOT_TOKEN`).

Боти Telegram для кожного агента json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "alerts", workspace: "~/.openclaw/workspace-alerts" },    ],  },  bindings: [    { agentId: "main", match: { channel: "telegram", accountId: "default" } },    { agentId: "alerts", match: { channel: "telegram", accountId: "alerts" } },  ],  channels: {    telegram: {      accounts: {        default: {          botToken: "123456:ABC...",          dmPolicy: "pairing",        },        alerts: {          botToken: "987654:XYZ...",          dmPolicy: "allowlist",          allowFrom: ["tg:123456789"],        },      },    },  },}
[/code]

  * Створіть по одному боту для кожного агента через BotFather і скопіюйте кожен токен.
  * Токени зберігаються в `channels.telegram.accounts.<id>.botToken` (обліковий запис за замовчуванням може використовувати `TELEGRAM_BOT_TOKEN`).

Номери WhatsApp для кожного агента

Прив’яжіть кожен обліковий запис перед запуском gateway:

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account personalopenclaw channels login --channel whatsapp --account biz
[/code]

`~/.openclaw/openclaw.json` (JSON5):

jsCopy code
[code]
    {  agents: {    list: [      {        id: "home",        default: true,        name: "Home",        workspace: "~/.openclaw/workspace-home",        agentDir: "~/.openclaw/agents/home/agent",      },      {        id: "work",        name: "Work",        workspace: "~/.openclaw/workspace-work",        agentDir: "~/.openclaw/agents/work/agent",      },    ],  },   // Deterministic routing: first match wins (most-specific first).  bindings: [    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },     // Optional per-peer override (example: send a specific group to work agent).    {      agentId: "work",      match: {        channel: "whatsapp",        accountId: "personal",        peer: { kind: "group", id: "1203630...@g.us" },      },    },  ],   // Off by default: agent-to-agent messaging must be explicitly enabled + allowlisted.  tools: {    agentToAgent: {      enabled: false,      allow: ["home", "work"],    },  },   channels: {    whatsapp: {      accounts: {        personal: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/personal          // authDir: "~/.openclaw/credentials/whatsapp/personal",        },        biz: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/biz          // authDir: "~/.openclaw/credentials/whatsapp/biz",        },      },    },  },}
[/code]

## Поширені шаблони

### Щоденна робота у WhatsApp + глибока робота в Telegram

Розділіть за каналом: спрямовуйте WhatsApp до швидкого повсякденного агента, а Telegram — до агента Opus.

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    { agentId: "chat", match: { channel: "whatsapp" } },    { agentId: "opus", match: { channel: "telegram" } },  ],}
[/code]

Примітки:

  * Якщо у вас кілька облікових записів для каналу, додайте `accountId` до прив’язки (наприклад, `{ channel: "whatsapp", accountId: "personal" }`).
  * Щоб спрямувати один DM/групу до Opus, залишивши решту в chat, додайте прив’язку `match.peer` для цього співрозмовника; збіги за співрозмовником завжди мають перевагу над правилами для всього каналу.


### Той самий канал, один співрозмовник до Opus

Залиште WhatsApp на швидкому агенті, але спрямовуйте один DM до Opus:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    {      agentId: "opus",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551234567" } },    },    { agentId: "chat", match: { channel: "whatsapp" } },  ],}
[/code]

Прив’язки peer завжди мають пріоритет, тому тримайте їх вище за правило для всього каналу.

### Family agent bound to a WhatsApp group

Прив’яжіть спеціального сімейного агента до однієї групи WhatsApp з обмеженням за згадками та суворішою політикою інструментів:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "family",        name: "Family",        workspace: "~/.openclaw/workspace-family",        identity: { name: "Family Bot" },        groupChat: {          mentionPatterns: ["@family", "@familybot", "@Family Bot"],        },        sandbox: {          mode: "all",          scope: "agent",        },        tools: {          allow: [            "exec",            "read",            "sessions_list",            "sessions_history",            "sessions_send",            "sessions_spawn",            "session_status",          ],          deny: ["write", "edit", "apply_patch", "browser", "canvas", "nodes", "cron"],        },      },    ],  },  bindings: [    {      agentId: "family",      match: {        channel: "whatsapp",        peer: { kind: "group", id: "120363999999999999@g.us" },      },    },  ],}
[/code]

Примітки:

  * Списки дозволу/заборони інструментів — це **інструменти** , а не skills. Якщо skill потрібно запускати двійковий файл, переконайтеся, що `exec` дозволено, а двійковий файл існує в пісочниці.
  * Для суворішого обмеження задайте `agents.list[].groupChat.mentionPatterns` і залиште списки дозволених груп увімкненими для каналу.


## Конфігурація пісочниці та інструментів для кожного агента

Кожен агент може мати власні обмеження пісочниці та інструментів:

jsCopy code
[code]
    {  agents: {    list: [      {        id: "personal",        workspace: "~/.openclaw/workspace-personal",        sandbox: {          mode: "off",  // No sandbox for personal agent        },        // No tool restrictions - all tools available      },      {        id: "family",        workspace: "~/.openclaw/workspace-family",        sandbox: {          mode: "all",     // Always sandboxed          scope: "agent",  // One container per agent          docker: {            // Optional one-time setup after container creation            setupCommand: "apt-get update && apt-get install -y git curl",          },        },        tools: {          allow: ["read"],                    // Only read tool          deny: ["exec", "write", "edit", "apply_patch"],    // Deny others        },      },    ],  },}
[/code]

**Переваги:**

  * **Ізоляція безпеки** : обмежуйте інструменти для ненадійних агентів.
  * **Контроль ресурсів** : запускайте певних агентів у пісочниці, залишаючи інших на хості.
  * **Гнучкі політики** : різні дозволи для кожного агента.


Див. [пісочниця та інструменти для кількох агентів](</uk/tools/multi-agent-sandbox-tools>) для докладних прикладів.

## Пов’язане

  * [Агенти ACP](</uk/tools/acp-agents>) — запуск зовнішніх середовищ кодування
  * [Маршрутизація каналів](</uk/channels/channel-routing>) — як повідомлення маршрутизуються до агентів
  * [Присутність](</uk/concepts/presence>) — присутність і доступність агента
  * [Сесія](</uk/concepts/session>) — ізоляція та маршрутизація сесій
  * [Підагенті](</uk/tools/subagents>) — запуск фонових виконань агентів


Was this useful?YesNo