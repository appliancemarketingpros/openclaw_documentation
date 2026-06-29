---
title: Twitch
source_url: https://docs.openclaw.ai/ru/channels/twitch
scraped_at: 2026-06-29
---

ChannelsDeveloper and self-hosted

Поддержка чата Twitch через IRC-соединение. OpenClaw подключается как пользователь Twitch (аккаунт бота), чтобы получать и отправлять сообщения в каналах.

## Встроенный Plugin

Если вы используете более старую сборку или пользовательскую установку, которая исключает Twitch, установите npm-пакет напрямую:

### npm registry

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### Local checkout

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

Используйте пакет без версии, чтобы следовать текущему официальному тегу релиза. Закрепляйте точную версию только тогда, когда вам нужна воспроизводимая установка.

Подробности: [Plugins](</ru/tools/plugin>)

## Быстрая настройка (для начинающих)

* ### Ensure plugin is available

Текущие пакетные релизы OpenClaw уже включают его. Более старые или пользовательские установки могут добавить его вручную командами выше.

* ### Create a Twitch bot account

Создайте отдельный аккаунт Twitch для бота (или используйте существующий аккаунт).

* ### Generate credentials

Используйте [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Выберите **Bot Token**
  * Убедитесь, что выбраны области доступа `chat:read` и `chat:write`
  * Скопируйте **Client ID** и **Access Token**


* ### Find your Twitch user ID

Используйте <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/>, чтобы преобразовать имя пользователя в ID пользователя Twitch.

* ### Configure the token

  * Env: `OPENCLAW_TWITCH_ACCESS_TOKEN=...` (только аккаунт по умолчанию)
  * Или конфиг: `channels.twitch.accessToken`


Если заданы оба варианта, конфиг имеет приоритет (резервный env-вариант работает только для аккаунта по умолчанию).

* ### Start the gateway

Запустите Gateway с настроенным каналом.

Минимальный конфиг:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## Что это такое

  * Канал Twitch, принадлежащий Gateway.
  * Детерминированная маршрутизация: ответы всегда возвращаются в Twitch.
  * Каждый аккаунт сопоставляется с изолированным ключом сессии `agent:<agentId>:twitch:<accountName>`.
  * `username` — это аккаунт бота (который проходит аутентификацию), `channel` — чат, к которому нужно присоединиться.


## Настройка (подробно)

### Создание учетных данных

Используйте [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Выберите **Bot Token**
  * Убедитесь, что выбраны области доступа `chat:read` и `chat:write`
  * Скопируйте **Client ID** и **Access Token**


### Настройка бота

### Env var (default account only)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### Config

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

Если заданы и env, и конфиг, конфиг имеет приоритет.

### Контроль доступа (рекомендуется)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

Предпочитайте `allowFrom` для жесткого списка разрешенных пользователей. Используйте `allowedRoles`, если нужен доступ на основе ролей.

**Доступные роли:** `"moderator"`, `"owner"`, `"vip"`, `"subscriber"`, `"all"`.

## Обновление токена (необязательно)

Токены из [Twitch Token Generator](<https://twitchtokengenerator.com/>) нельзя обновлять автоматически — создавайте их заново после истечения срока действия.

Для автоматического обновления токена создайте собственное приложение Twitch в [Twitch Developer Console](<https://dev.twitch.tv/console>) и добавьте в конфиг:

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

Бот автоматически обновляет токены до истечения срока действия и записывает события обновления в журнал.

## Поддержка нескольких аккаунтов

Используйте `channels.twitch.accounts` с токенами для каждого аккаунта. Общий шаблон см. в разделе [Конфигурация](</ru/gateway/configuration>).

Пример (один аккаунт бота в двух каналах):

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## Контроль доступа

### User ID allowlist (most secure)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### Role-based

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` — это жесткий список разрешенных пользователей. Если он задан, разрешены только эти ID пользователей. Если вам нужен доступ на основе ролей, не задавайте `allowFrom` и вместо этого настройте `allowedRoles`.

### Disable @mention requirement

По умолчанию `requireMention` равно `true`. Чтобы отключить это требование и отвечать на все сообщения:

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## Устранение неполадок

Сначала выполните диагностические команды:

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

Bot does not respond to messages

  * **Проверьте контроль доступа:** Убедитесь, что ваш ID пользователя указан в `allowFrom`, или временно удалите `allowFrom` и задайте `allowedRoles: ["all"]` для проверки.
  * **Проверьте, что бот находится в канале:** Бот должен присоединиться к каналу, указанному в `channel`.

Token issues

"Failed to connect" или ошибки аутентификации:

  * Убедитесь, что `accessToken` — это значение токена доступа OAuth (обычно начинается с префикса `oauth:`)
  * Проверьте, что у токена есть области доступа `chat:read` и `chat:write`
  * Если используется обновление токена, убедитесь, что заданы `clientSecret` и `refreshToken`

Token refresh not working

Проверьте журналы на наличие событий обновления:

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

Если вы видите "token refresh disabled (no refresh token)":

  * Убедитесь, что указан `clientSecret`
  * Убедитесь, что указан `refreshToken`


## Конфиг

### Конфиг аккаунта

Имя пользователя бота.

Токен доступа OAuth с `chat:read` и `chat:write`.

Client ID Twitch (из Token Generator или вашего приложения).

Канал, к которому нужно присоединиться.

Включить этот аккаунт.

Необязательно: для автоматического обновления токена.

Необязательно: для автоматического обновления токена.

Срок действия токена в секундах.

Метка времени получения токена.

Список разрешенных ID пользователей.

Требовать @mention.

### Параметры провайдера

  * `channels.twitch.enabled` \- Включить/отключить запуск канала
  * `channels.twitch.username` \- Имя пользователя бота (упрощенный конфиг для одного аккаунта)
  * `channels.twitch.accessToken` \- Токен доступа OAuth (упрощенный конфиг для одного аккаунта)
  * `channels.twitch.clientId` \- Client ID Twitch (упрощенный конфиг для одного аккаунта)
  * `channels.twitch.channel` \- Канал, к которому нужно присоединиться (упрощенный конфиг для одного аккаунта)
  * `channels.twitch.accounts.<accountName>` \- Конфиг для нескольких аккаунтов (все поля аккаунта выше)


Полный пример:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## Действия инструментов

Агент может вызвать `twitch` с действием:

  * `send` \- Отправить сообщение в канал


Пример:

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## Безопасность и эксплуатация

  * **Обращайтесь с токенами как с паролями** — Никогда не коммитьте токены в git.
  * **Используйте автоматическое обновление токенов** для долгоживущих ботов.
  * **Используйте списки разрешенных ID пользователей** вместо имен пользователей для контроля доступа.
  * **Отслеживайте журналы** на предмет событий обновления токенов и состояния подключения.
  * **Минимизируйте области доступа токенов** — Запрашивайте только `chat:read` и `chat:write`.
  * **Если вы застряли** : перезапустите Gateway после подтверждения, что никакой другой процесс не владеет сессией.


## Ограничения

  * **500 символов** на сообщение (автоматически разбивается по границам слов).
  * Markdown удаляется перед разбиением.
  * Нет ограничения частоты отправки (используются встроенные ограничения частоты Twitch).


## Связанные разделы

  * [Маршрутизация каналов](</ru/channels/channel-routing>) — маршрутизация сессий для сообщений
  * [Обзор каналов](</ru/channels>) — все поддерживаемые каналы
  * [Группы](</ru/channels/groups>) — поведение групповых чатов и ограничение по упоминанию
  * [Pairing](</ru/channels/pairing>) — аутентификация в DM и процесс Pairing
  * [Безопасность](</ru/gateway/security>) — модель доступа и усиление защиты


Was this useful?YesNo

Open issue