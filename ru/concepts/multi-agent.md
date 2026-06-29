---
title: Маршрутизация нескольких агентов
source_url: https://docs.openclaw.ai/ru/concepts/multi-agent
scraped_at: 2026-06-29
---

AgentsMulti-agent

Запускайте несколько _изолированных_ агентов — каждый со своим рабочим пространством, каталогом состояния (`agentDir`) и историей сеансов — а также несколько учетных записей каналов (например, два WhatsApp) в одном работающем Gateway. Входящие сообщения маршрутизируются к нужному агенту через привязки.

Здесь **агент** — это полный контекст отдельной персоны: файлы рабочего пространства, профили аутентификации, реестр моделей и хранилище сеансов. `agentDir` — это каталог состояния на диске, в котором хранится эта конфигурация отдельного агента по пути `~/.openclaw/agents/<agentId>/`. **Привязка** сопоставляет учетную запись канала (например, рабочее пространство Slack или номер WhatsApp) с одним из этих агентов.

## Что такое «один агент»?

**Агент** — это полностью ограниченный по области «мозг» со своими:

  * **Рабочим пространством** (файлы, AGENTS.md/SOUL.md/USER.md, локальные заметки, правила персоны).
  * **Каталогом состояния** (`agentDir`) для профилей аутентификации, реестра моделей и конфигурации отдельного агента.
  * **Хранилищем сеансов** (история чата + состояние маршрутизации) в `~/.openclaw/agents/<agentId>/sessions`.


Профили аутентификации являются **отдельными для каждого агента**. Каждый агент читает их из своего файла:

textCopy code
[code]
    ~/.openclaw/agents/<agentId>/agent/auth-profiles.json
[/code]

Skills загружаются из рабочего пространства каждого агента плюс из общих корней, таких как `~/.openclaw/skills`, затем фильтруются по эффективному списку разрешенных Skills агента, если он настроен. Используйте `agents.defaults.skills` для общей базы и `agents.list[].skills` для замены на уровне агента. См. [Skills: для отдельного агента и общие](</ru/tools/skills#per-agent-vs-shared-skills>) и [Skills: списки разрешенных Skills агента](</ru/tools/skills#agent-allowlists>).

Gateway может размещать **одного агента** (по умолчанию) или **много агентов** рядом друг с другом.

## Пути (краткая карта)

  * Конфигурация: `~/.openclaw/openclaw.json` (или `OPENCLAW_CONFIG_PATH`)
  * Каталог состояния: `~/.openclaw` (или `OPENCLAW_STATE_DIR`)
  * Рабочее пространство: `~/.openclaw/workspace` (или `~/.openclaw/workspace-<agentId>`)
  * Каталог агента: `~/.openclaw/agents/<agentId>/agent` (или `agents.list[].agentDir`)
  * Сеансы: `~/.openclaw/agents/<agentId>/sessions`


### Режим одного агента (по умолчанию)

Если вы ничего не настраиваете, OpenClaw запускает одного агента:

  * `agentId` по умолчанию равен **`main`**.
  * Сеансы получают ключи вида `agent:main:<mainKey>`.
  * Рабочее пространство по умолчанию — `~/.openclaw/workspace` (или `~/.openclaw/workspace-<profile>`, когда задан `OPENCLAW_PROFILE`).
  * Состояние по умолчанию — `~/.openclaw/agents/main/agent`.


## Помощник агентов

Используйте мастер агентов, чтобы добавить нового изолированного агента:

bashCopy code
[code]
    openclaw agents add work
[/code]

Затем добавьте `bindings` (или позвольте мастеру сделать это), чтобы маршрутизировать входящие сообщения.

Проверьте с помощью:

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

## Быстрый старт

* ### Создайте рабочее пространство каждого агента

Используйте мастер или создайте рабочие пространства вручную:

bashCopy code
[code]
    openclaw agents add codingopenclaw agents add social
[/code]

Каждый агент получает собственное рабочее пространство с `SOUL.md`, `AGENTS.md` и необязательным `USER.md`, а также выделенный `agentDir` и хранилище сеансов в `~/.openclaw/agents/<agentId>`.

* ### Создайте учетные записи каналов

Создайте по одной учетной записи на агента в предпочитаемых каналах:

  * Discord: один бот на агента, включите Message Content Intent, скопируйте каждый токен.
  * Telegram: один бот на агента через BotFather, скопируйте каждый токен.
  * WhatsApp: привяжите каждый номер телефона к отдельной учетной записи.

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account work
[/code]

См. руководства по каналам: [Discord](</ru/channels/discord>), [Telegram](</ru/channels/telegram>), [WhatsApp](</ru/channels/whatsapp>).

* ### Добавьте агентов, учетные записи и привязки

Добавьте агентов в `agents.list`, учетные записи каналов в `channels.<channel>.accounts` и соедините их с помощью `bindings` (примеры ниже).

* ### Перезапустите и проверьте

bashCopy code
[code]
    openclaw gateway restartopenclaw agents list --bindingsopenclaw channels status --probe
[/code]

## Несколько агентов = несколько людей, несколько личностей

С **несколькими агентами** каждый `agentId` становится **полностью изолированной персоной** :

  * **Разные номера телефонов/учетные записи** (по `accountId` канала).
  * **Разные личности** (файлы рабочего пространства отдельного агента, например `AGENTS.md` и `SOUL.md`).
  * **Отдельные аутентификация + сеансы** (без перекрестного общения, если оно явно не включено).


Это позволяет **нескольким людям** совместно использовать один сервер Gateway, сохраняя изоляцию их AI-«мозгов» и данных.

## Поиск памяти QMD между агентами

Если один агент должен искать в стенограммах сеансов QMD другого агента, добавьте дополнительные коллекции в `agents.list[].memorySearch.qmd.extraCollections`. Используйте `agents.defaults.memorySearch.qmd.extraCollections` только когда каждый агент должен наследовать одинаковые общие коллекции стенограмм.

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/workspaces/main",      memorySearch: {        qmd: {          extraCollections: [{ path: "~/agents/family/sessions", name: "family-sessions" }],        },      },    },    list: [      {        id: "main",        workspace: "~/workspaces/main",        memorySearch: {          qmd: {            extraCollections: [{ path: "notes" }], // resolves inside workspace -> collection named "notes-main"          },        },      },      { id: "family", workspace: "~/workspaces/family" },    ],  },  memory: {    backend: "qmd",    qmd: { includeDefaultMemory: false },  },}
[/code]

Путь дополнительной коллекции может быть общим для нескольких агентов, но имя коллекции остается явным, когда путь находится вне рабочего пространства агента. Пути внутри рабочего пространства остаются ограниченными агентом, чтобы каждый агент сохранял собственный набор поиска по стенограммам.

## Один номер WhatsApp, несколько людей (разделение DM)

Вы можете маршрутизировать **разные DM WhatsApp** разным агентам, оставаясь в **одной учетной записи WhatsApp**. Сопоставляйте по отправителю E.164 (например, `+15551234567`) с `peer.kind: "direct"`. Ответы все равно приходят с того же номера WhatsApp (без отдельной идентичности отправителя на агента).

Пример:

json5Copy code
[code]
    {  agents: {    list: [      { id: "alex", workspace: "~/.openclaw/workspace-alex" },      { id: "mia", workspace: "~/.openclaw/workspace-mia" },    ],  },  bindings: [    {      agentId: "alex",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230001" } },    },    {      agentId: "mia",      match: { channel: "whatsapp", peer: { kind: "direct", id: "+15551230002" } },    },  ],  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551230001", "+15551230002"],    },  },}
[/code]

Примечания:

  * Контроль доступа к DM является **глобальным для учетной записи WhatsApp** (сопряжение/allowlist), а не отдельным для агента.
  * Для общих групп привяжите группу к одному агенту или используйте [Группы рассылки](</ru/channels/broadcast-groups>).


## Правила маршрутизации (как сообщения выбирают агента)

Привязки являются **детерминированными** , и **побеждает самая специфичная** :

* ### совпадение peer

Точный ID DM/группы/канала.

* ### совпадение parentPeer

Наследование треда.

* ### guildId + роли

Маршрутизация по ролям Discord.

* ### guildId

Discord.

* ### teamId

Slack.

* ### совпадение accountId для канала

Резервный вариант на уровне учетной записи.

* ### Совпадение на уровне канала

`accountId: "*"`.

* ### Агент по умолчанию

Резервный переход к `agents.list[].default`, иначе первая запись списка, по умолчанию: `main`.

Разрешение ничьих и семантика AND

  * Если несколько привязок совпадают на одном уровне, побеждает первая в порядке конфигурации.
  * Если привязка задает несколько полей совпадения (например, `peer` \+ `guildId`), требуются все указанные поля (семантика `AND`).

Детали области учетной записи

  * Привязка, в которой опущен `accountId`, соответствует только учетной записи по умолчанию. Она не соответствует всем учетным записям.
  * Используйте `accountId: "*"` для резервного варианта на весь канал по всем учетным записям.
  * Используйте `accountId: "<name>"`, чтобы сопоставить одну учетную запись.
  * Если позже вы добавите такую же привязку для того же агента с явным ID учетной записи, OpenClaw обновит существующую привязку только к каналу до области учетной записи вместо ее дублирования.


## Несколько учетных записей / номеров телефонов

Каналы, поддерживающие **несколько учетных записей** (например, WhatsApp), используют `accountId` для идентификации каждого входа. Каждый `accountId` можно маршрутизировать к другому агенту, поэтому один сервер может размещать несколько номеров телефонов без смешивания сеансов.

Если вам нужна учетная запись по умолчанию на уровне канала, когда `accountId` опущен, задайте `channels.<channel>.defaultAccount` (необязательно). Если значение не задано, OpenClaw использует `default`, если он присутствует, иначе первый настроенный ID учетной записи (после сортировки).

Распространенные каналы, поддерживающие этот шаблон, включают:

  * `whatsapp`, `telegram`, `discord`, `slack`, `signal`, `imessage`
  * `irc`, `line`, `googlechat`, `mattermost`, `matrix`, `nextcloud-talk`
  * `zalo`, `zalouser`, `nostr`, `feishu`


## Основные понятия

  * `agentId`: один «мозг» (рабочее пространство, аутентификация отдельного агента, хранилище сеансов отдельного агента).
  * `accountId`: один экземпляр учетной записи канала (например, учетная запись WhatsApp `"personal"` и `"biz"`).
  * `binding`: маршрутизирует входящие сообщения к `agentId` по `(channel, accountId, peer)` и необязательно по ID guild/team.
  * Прямые чаты сворачиваются в `agent:<agentId>:<mainKey>` («основной» для отдельного агента; `session.mainKey`).


## Примеры платформ

Боты Discord на каждого агента

Каждая учетная запись бота Discord сопоставляется с уникальным `accountId`. Привяжите каждую учетную запись к агенту и держите allowlist отдельно для каждого бота.

json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "coding", workspace: "~/.openclaw/workspace-coding" },    ],  },  bindings: [    { agentId: "main", match: { channel: "discord", accountId: "default" } },    { agentId: "coding", match: { channel: "discord", accountId: "coding" } },  ],  channels: {    discord: {      groupPolicy: "allowlist",      accounts: {        default: {          token: "DISCORD_BOT_TOKEN_MAIN",          guilds: {            "123456789012345678": {              channels: {                "222222222222222222": { allow: true, requireMention: false },              },            },          },        },        coding: {          token: "DISCORD_BOT_TOKEN_CODING",          guilds: {            "123456789012345678": {              channels: {                "333333333333333333": { allow: true, requireMention: false },              },            },          },        },      },    },  },}
[/code]

  * Пригласите каждого бота на сервер и включите Message Content Intent.
  * Токены находятся в `channels.discord.accounts.<id>.token` (учетная запись по умолчанию может использовать `DISCORD_BOT_TOKEN`).

Telegram bots per agent json5Copy code
[code]
    {  agents: {    list: [      { id: "main", workspace: "~/.openclaw/workspace-main" },      { id: "alerts", workspace: "~/.openclaw/workspace-alerts" },    ],  },  bindings: [    { agentId: "main", match: { channel: "telegram", accountId: "default" } },    { agentId: "alerts", match: { channel: "telegram", accountId: "alerts" } },  ],  channels: {    telegram: {      accounts: {        default: {          botToken: "123456:ABC...",          dmPolicy: "pairing",        },        alerts: {          botToken: "987654:XYZ...",          dmPolicy: "allowlist",          allowFrom: ["tg:123456789"],        },      },    },  },}
[/code]

  * Создайте по одному боту на агента через BotFather и скопируйте каждый токен.
  * Токены находятся в `channels.telegram.accounts.<id>.botToken` (учетная запись по умолчанию может использовать `TELEGRAM_BOT_TOKEN`).
  * Для нескольких ботов в одной группе Telegram пригласите каждого бота и упомяните бота, который должен отвечать.
  * Отключите BotFather Privacy Mode для каждого группового бота, затем добавьте бота повторно, чтобы Telegram применил настройку.
  * Разрешите группы через `channels.telegram.groups` или используйте `groupPolicy: "open"` только для доверенных групповых развертываний.
  * Поместите пользовательские ID отправителей в `groupAllowFrom`. ID групп и супергрупп должны быть в `channels.telegram.groups`, а не в `groupAllowFrom`.
  * Выполните привязку по `accountId`, чтобы каждый бот маршрутизировался к своему агенту.

WhatsApp numbers per agent

Свяжите каждую учетную запись перед запуском gateway:

bashCopy code
[code]
    openclaw channels login --channel whatsapp --account personalopenclaw channels login --channel whatsapp --account biz
[/code]

`~/.openclaw/openclaw.json` (JSON5):

jsCopy code
[code]
    {  agents: {    list: [      {        id: "home",        default: true,        name: "Home",        workspace: "~/.openclaw/workspace-home",        agentDir: "~/.openclaw/agents/home/agent",      },      {        id: "work",        name: "Work",        workspace: "~/.openclaw/workspace-work",        agentDir: "~/.openclaw/agents/work/agent",      },    ],  },   // Deterministic routing: first match wins (most-specific first).  bindings: [    { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },    { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },     // Optional per-peer override (example: send a specific group to work agent).    {      agentId: "work",      match: {        channel: "whatsapp",        accountId: "personal",        peer: { kind: "group", id: "1203630...@g.us" },      },    },  ],   // Off by default: agent-to-agent messaging must be explicitly enabled + allowlisted.  tools: {    agentToAgent: {      enabled: false,      allow: ["home", "work"],    },  },   channels: {    whatsapp: {      accounts: {        personal: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/personal          // authDir: "~/.openclaw/credentials/whatsapp/personal",        },        biz: {          // Optional override. Default: ~/.openclaw/credentials/whatsapp/biz          // authDir: "~/.openclaw/credentials/whatsapp/biz",        },      },    },  },}
[/code]

## Распространенные шаблоны

### WhatsApp daily + Telegram deep work

Разделение по каналам: маршрутизируйте WhatsApp к быстрому повседневному агенту, а Telegram — к агенту Opus.

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    { agentId: "chat", match: { channel: "whatsapp", accountId: "*" } },    { agentId: "opus", match: { channel: "telegram", accountId: "*" } },  ],}
[/code]

Примечания:

  * В этих примерах используется `accountId: "*"`, поэтому привязки продолжат работать, если вы добавите учетные записи позже.
  * Чтобы маршрутизировать один DM/группу к Opus, оставив остальные чаты на агенте chat, добавьте привязку `match.peer` для этого собеседника; совпадения по собеседнику всегда имеют приоритет над правилами для всего канала.


### Same channel, one peer to Opus

Оставьте WhatsApp на быстром агенте, но маршрутизируйте один DM к Opus:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "chat",        name: "Everyday",        workspace: "~/.openclaw/workspace-chat",        model: "anthropic/claude-sonnet-4-6",      },      {        id: "opus",        name: "Deep Work",        workspace: "~/.openclaw/workspace-opus",        model: "anthropic/claude-opus-4-6",      },    ],  },  bindings: [    {      agentId: "opus",      match: { channel: "whatsapp", accountId: "*", peer: { kind: "direct", id: "+15551234567" } },    },    { agentId: "chat", match: { channel: "whatsapp", accountId: "*" } },  ],}
[/code]

Привязки собеседников всегда имеют приоритет, поэтому держите их выше правила для всего канала.

### Family agent bound to a WhatsApp group

Привяжите выделенного семейного агента к одной группе WhatsApp, с ограничением по упоминаниям и более строгой политикой инструментов:

json5Copy code
[code]
    {  agents: {    list: [      {        id: "family",        name: "Family",        workspace: "~/.openclaw/workspace-family",        identity: { name: "Family Bot" },        groupChat: {          mentionPatterns: ["@family", "@familybot", "@Family Bot"],        },        sandbox: {          mode: "all",          scope: "agent",        },        tools: {          allow: [            "exec",            "read",            "sessions_list",            "sessions_history",            "sessions_send",            "sessions_spawn",            "session_status",          ],          deny: ["write", "edit", "apply_patch", "browser", "canvas", "nodes", "cron"],        },      },    ],  },  bindings: [    {      agentId: "family",      match: {        channel: "whatsapp",        peer: { kind: "group", id: "120363999999999999@g.us" },      },    },  ],}
[/code]

Примечания:

  * Списки разрешения/запрета инструментов относятся к **инструментам** , а не к Skills. Если Skills нужно запустить бинарный файл, убедитесь, что `exec` разрешен и бинарный файл существует в песочнице.
  * Для более строгого ограничения задайте `agents.list[].groupChat.mentionPatterns` и оставьте списки разрешенных групп включенными для канала.


## Песочница и конфигурация инструментов для каждого агента

У каждого агента могут быть собственная песочница и ограничения инструментов:

jsCopy code
[code]
    {  agents: {    list: [      {        id: "personal",        workspace: "~/.openclaw/workspace-personal",        sandbox: {          mode: "off",  // No sandbox for personal agent        },        // No tool restrictions - all tools available      },      {        id: "family",        workspace: "~/.openclaw/workspace-family",        sandbox: {          mode: "all",     // Always sandboxed          scope: "agent",  // One container per agent          docker: {            // Optional one-time setup after container creation            setupCommand: "apt-get update && apt-get install -y git curl",          },        },        tools: {          allow: ["read"],                    // Only read tool          deny: ["exec", "write", "edit", "apply_patch"],    // Deny others        },      },    ],  },}
[/code]

**Преимущества:**

  * **Изоляция безопасности** : ограничивайте инструменты для недоверенных агентов.
  * **Контроль ресурсов** : помещайте отдельных агентов в песочницу, оставляя других на хосте.
  * **Гибкие политики** : разные разрешения для каждого агента.


Подробные примеры см. в разделе [Песочница и инструменты для нескольких агентов](</ru/tools/multi-agent-sandbox-tools>).

## Связанные разделы

  * [Агенты ACP](</ru/tools/acp-agents>) — запуск внешних сред кодирования
  * [Маршрутизация каналов](</ru/channels/channel-routing>) — как сообщения маршрутизируются к агентам
  * [Присутствие](</ru/concepts/presence>) — присутствие и доступность агента
  * [Сессия](</ru/concepts/session>) — изоляция и маршрутизация сессий
  * [Субагенты](</ru/tools/subagents>) — запуск фоновых выполнений агентов


Was this useful?YesNo

Open issue