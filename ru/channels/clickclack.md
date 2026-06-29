---
title: ClickClack
source_url: https://docs.openclaw.ai/ru/channels/clickclack
scraped_at: 2026-06-29
---

Get started

ClickClack подключает OpenClaw к самостоятельно размещенному рабочему пространству ClickClack через полноценные токены ботов ClickClack.

Используйте это, когда хотите, чтобы агент OpenClaw отображался как пользователь-бот ClickClack. ClickClack поддерживает независимых сервисных ботов и ботов, принадлежащих пользователям; боты, принадлежащие пользователям, сохраняют `owner_user_id` и получают только те области доступа токена, которые вы предоставите.

## Быстрая настройка

Создайте токен бота в ClickClack:

bashCopy code
[code]
    clickclack admin bot create \  --workspace <workspace_id_or_slug> \  --name "OpenClaw" \  --handle openclaw \  --scopes bot:write \  --plain
[/code]

Для бота, принадлежащего пользователю, добавьте `--owner <user_id>`.

Настройте OpenClaw:

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      token: { source: "env", provider: "default", id: "CLICKCLACK_BOT_TOKEN" },      workspace: "default",      defaultTo: "channel:general",      agentId: "clickclack-bot",      replyMode: "model",    },  },}
[/code]

Затем выполните:

bashCopy code
[code]
    export CLICKCLACK_BOT_TOKEN="ccb_..."openclaw gateway
[/code]

Если `plugins.allow` — непустой ограничительный список, явный выбор ClickClack при настройке канала или выполнение `openclaw plugins enable clickclack` добавляет `clickclack` в этот список. Установка при первичной настройке использует то же поведение явного выбора. Эти пути не переопределяют `plugins.deny` или глобальный параметр `plugins.enabled: false`. Прямое выполнение `openclaw plugins install @openclaw/clickclack` следует обычной политике установки Plugin и также записывает ClickClack в существующий список разрешенных.

## Несколько ботов

Каждая учетная запись открывает собственное realtime-подключение ClickClack и использует собственный токен бота.

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      defaultAccount: "service",      accounts: {        service: {          token: { source: "env", provider: "default", id: "CLICKCLACK_SERVICE_BOT_TOKEN" },          workspace: "default",          defaultTo: "channel:general",          agentId: "service-bot",          replyMode: "model",        },        peter: {          token: { source: "env", provider: "default", id: "CLICKCLACK_PETER_BOT_TOKEN" },          workspace: "default",          defaultTo: "dm:usr_...",          agentId: "peter-bot",          replyMode: "model",        },      },    },  },}
[/code]

`replyMode: "model"` использует `api.runtime.llm.complete` напрямую для коротких ответов бота. Когда учетная запись задает `agentId`, OpenClaw требует явный доверительный бит `plugins.entries.clickclack.llm.allowAgentIdOverride`, чтобы Plugin мог выполнять completions для этого агента-бота. Не включайте его, если используете только стандартный маршрут агента.

## Цели

  * `channel:<name-or-id>` отправляет сообщение в канал рабочего пространства. Цели без префикса по умолчанию используют `channel:`.
  * `dm:<user_id>` создает или повторно использует прямую беседу с этим пользователем.
  * `thread:<message_id>` отвечает в существующей ветке.


Примеры:

bashCopy code
[code]
    openclaw message send --channel clickclack --target channel:general --message "hello"openclaw message send --channel clickclack --target dm:usr_123 --message "hello"openclaw message send --channel clickclack --target thread:msg_123 --message "following up"
[/code]

## Разрешения

Области доступа токена ClickClack применяются API ClickClack.

  * `bot:read`: чтение данных рабочего пространства, каналов, сообщений, веток, личных сообщений, realtime и профиля.
  * `bot:write`: `bot:read` плюс сообщения в каналах, ответы в ветках, личные сообщения и загрузки.
  * `bot:admin`: `bot:write` плюс создание каналов.


OpenClaw нужен только `bot:write` для обычного чата агента.

## Устранение неполадок

  * `ClickClack is not configured`: задайте `channels.clickclack.token` или `CLICKCLACK_BOT_TOKEN`.
  * `workspace not found`: задайте для `workspace` идентификатор или slug рабочего пространства, возвращенный ClickClack.
  * Нет входящих ответов: подтвердите, что токен имеет доступ к чтению realtime и бот не отвечает на собственные сообщения.
  * Отправка в канал завершается ошибкой: убедитесь, что бот является участником рабочего пространства и имеет `bot:write`.


Was this useful?YesNo

Open issue