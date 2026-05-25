---
title: Twitch
source_url: https://docs.openclaw.ai/uk/channels/twitch
scraped_at: 2026-05-25
---

Підтримка чату Twitch через IRC-з’єднання. OpenClaw підключається як користувач Twitch (обліковий запис бота), щоб отримувати й надсилати повідомлення в каналах.

## Вбудований Plugin

Якщо ви використовуєте старішу збірку або кастомне встановлення, яке не включає Twitch, встановіть npm-пакет напряму:

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

Використовуйте пакет без версії, щоб стежити за поточним офіційним тегом випуску. Закріплюйте точну версію лише тоді, коли вам потрібне відтворюване встановлення.

Докладніше: [Plugins](</uk/tools/plugin>)

## Швидке налаштування (для початківців)

* ### Переконайтеся, що Plugin доступний

Поточні пакетовані випуски OpenClaw вже включають його. У старіших або кастомних встановленнях його можна додати вручну командами вище.

* ### Створіть обліковий запис бота Twitch

Створіть окремий обліковий запис Twitch для бота (або використайте наявний обліковий запис).

* ### Згенеруйте облікові дані

Використайте [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Виберіть **Bot Token**
  * Перевірте, що вибрано області доступу `chat:read` і `chat:write`
  * Скопіюйте **Client ID** і **Access Token**


* ### Знайдіть свій ідентифікатор користувача Twitch

Використайте <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/>, щоб перетворити ім’я користувача на ідентифікатор користувача Twitch.

* ### Налаштуйте токен

  * Змінна середовища: `OPENCLAW_TWITCH_ACCESS_TOKEN=...` (лише обліковий запис за замовчуванням)
  * Або конфігурація: `channels.twitch.accessToken`


Якщо задано обидва варіанти, конфігурація має пріоритет (резервна змінна середовища діє лише для облікового запису за замовчуванням).

* ### Запустіть Gateway

Запустіть Gateway із налаштованим каналом.

Мінімальна конфігурація:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## Що це таке

  * Канал Twitch, яким володіє Gateway.
  * Детермінована маршрутизація: відповіді завжди повертаються до Twitch.
  * Кожен обліковий запис відповідає ізольованому ключу сеансу `agent:<agentId>:twitch:<accountName>`.
  * `username` — це обліковий запис бота (який проходить автентифікацію), `channel` — це чат-кімната, до якої потрібно приєднатися.


## Налаштування (докладно)

### Згенеруйте облікові дані

Використайте [Twitch Token Generator](<https://twitchtokengenerator.com/>):

  * Виберіть **Bot Token**
  * Перевірте, що вибрано області доступу `chat:read` і `chat:write`
  * Скопіюйте **Client ID** і **Access Token**


### Налаштуйте бота

### Змінна середовища (лише обліковий запис за замовчуванням)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### Конфігурація

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

Якщо задано і змінну середовища, і конфігурацію, конфігурація має пріоритет.

### Контроль доступу (рекомендовано)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

Надавайте перевагу `allowFrom` для жорсткого списку дозволених. Використовуйте `allowedRoles` натомість, якщо вам потрібен доступ на основі ролей.

**Доступні ролі:** `"moderator"`, `"owner"`, `"vip"`, `"subscriber"`, `"all"`.

## Оновлення токена (необов’язково)

Токени з [Twitch Token Generator](<https://twitchtokengenerator.com/>) не можна автоматично оновлювати — згенеруйте новий після завершення строку дії.

Для автоматичного оновлення токена створіть власний застосунок Twitch у [Twitch Developer Console](<https://dev.twitch.tv/console>) і додайте до конфігурації:

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

Бот автоматично оновлює токени до завершення строку дії та записує події оновлення в журнали.

## Підтримка кількох облікових записів

Використовуйте `channels.twitch.accounts` із токенами для кожного облікового запису. Спільний шаблон див. у [Конфігурації](</uk/gateway/configuration>).

Приклад (один обліковий запис бота у двох каналах):

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## Контроль доступу

### Список дозволених ID користувачів (найбезпечніше)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### На основі ролей

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` — це жорсткий список дозволених. Якщо його задано, дозволені лише ці ідентифікатори користувачів. Якщо вам потрібен доступ на основі ролей, не задавайте `allowFrom` і налаштуйте натомість `allowedRoles`.

### Вимкнути вимогу @mention

За замовчуванням `requireMention` має значення `true`. Щоб вимкнути це й відповідати на всі повідомлення:

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## Усунення несправностей

Спочатку запустіть діагностичні команди:

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

Бот не відповідає на повідомлення

  * **Перевірте контроль доступу:** Переконайтеся, що ваш ID користувача є в `allowFrom`, або тимчасово видаліть `allowFrom` і задайте `allowedRoles: ["all"]` для тестування.
  * **Перевірте, що бот у каналі:** Бот має приєднатися до каналу, указаного в `channel`.

Проблеми з токеном

"Failed to connect" або помилки автентифікації:

  * Перевірте, що `accessToken` — це значення токена доступу OAuth (зазвичай починається з префікса `oauth:`)
  * Перевірте, що токен має області доступу `chat:read` і `chat:write`
  * Якщо використовується оновлення токена, перевірте, що `clientSecret` і `refreshToken` задані

Оновлення токена не працює

Перевірте журнали на наявність подій оновлення:

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

Якщо ви бачите "token refresh disabled (no refresh token)":

  * Переконайтеся, що `clientSecret` надано
  * Переконайтеся, що `refreshToken` надано


## Конфігурація

### Конфігурація облікового запису

Ім’я користувача бота.

Токен доступу OAuth із `chat:read` і `chat:write`.

Twitch Client ID (з Token Generator або вашого застосунку).

Канал, до якого потрібно приєднатися.

Увімкнути цей обліковий запис.

Необов’язково: для автоматичного оновлення токена.

Необов’язково: для автоматичного оновлення токена.

Строк дії токена в секундах.

Час отримання токена.

Список дозволених ID користувачів.

Вимагати @mention.

### Параметри провайдера

  * `channels.twitch.enabled` \- Увімкнути/вимкнути запуск каналу
  * `channels.twitch.username` \- Ім’я користувача бота (спрощена конфігурація одного облікового запису)
  * `channels.twitch.accessToken` \- Токен доступу OAuth (спрощена конфігурація одного облікового запису)
  * `channels.twitch.clientId` \- Twitch Client ID (спрощена конфігурація одного облікового запису)
  * `channels.twitch.channel` \- Канал, до якого потрібно приєднатися (спрощена конфігурація одного облікового запису)
  * `channels.twitch.accounts.<accountName>` \- Конфігурація кількох облікових записів (усі поля облікового запису вище)


Повний приклад:

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## Дії інструментів

Агент може викликати `twitch` з дією:

  * `send` \- Надіслати повідомлення в канал


Приклад:

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## Безпека та експлуатація

  * **Ставтеся до токенів як до паролів** — ніколи не комітьте токени в git.
  * **Використовуйте автоматичне оновлення токенів** для довготривалих ботів.
  * **Використовуйте списки дозволених ID користувачів** замість імен користувачів для контролю доступу.
  * **Стежте за журналами** для подій оновлення токенів і стану з’єднання.
  * **Мінімізуйте області доступу токенів** — запитуйте лише `chat:read` і `chat:write`.
  * **Якщо застрягли** : перезапустіть Gateway після підтвердження, що жоден інший процес не володіє сеансом.


## Обмеження

  * **500 символів** на повідомлення (автоматично розбивається на частини на межах слів).
  * Markdown видаляється перед розбиттям на частини.
  * Без обмеження частоти (використовуються вбудовані обмеження частоти Twitch).


## Пов’язане

  * [Маршрутизація каналів](</uk/channels/channel-routing>) — маршрутизація сеансів для повідомлень
  * [Огляд каналів](</uk/channels>) — усі підтримувані канали
  * [Групи](</uk/channels/groups>) — поведінка групового чату та обмеження за згадкою
  * [Сполучення](</uk/channels/pairing>) — автентифікація DM і потік сполучення
  * [Безпека](</uk/gateway/security>) — модель доступу та посилення захисту


Was this useful?YesNo