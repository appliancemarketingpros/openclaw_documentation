---
title: Mattermost
source_url: https://docs.openclaw.ai/uk/channels/mattermost
scraped_at: 2026-05-25
---

Статус: завантажуваний plugin (токен бота + події WebSocket). Підтримуються канали, групи та особисті повідомлення. Mattermost — це платформа командного обміну повідомленнями, яку можна розгорнути самостійно; докладні відомості про продукт і завантаження див. на офіційному сайті [mattermost.com](<https://mattermost.com>).

## Встановлення

Встановіть Mattermost перед налаштуванням каналу:

### реєстр npm

bashCopy code
[code]
    openclaw plugins install @openclaw/mattermost
[/code]

### локальна робоча копія

bashCopy code
[code]
    openclaw plugins install ./path/to/local/mattermost-plugin
[/code]

Докладніше: [Plugins](</uk/tools/plugin>)

## Швидке налаштування

* ### Переконайтеся, що plugin доступний

Поточні пакетовані випуски OpenClaw уже містять його. Старіші або користувацькі встановлення можуть додати його вручну за допомогою команд вище.

* ### Створіть бота Mattermost

Створіть обліковий запис бота Mattermost і скопіюйте **токен бота**.

* ### Скопіюйте базову URL-адресу

Скопіюйте **базову URL-адресу** Mattermost (наприклад, `https://chat.example.com`).

* ### Налаштуйте OpenClaw і запустіть gateway

Мінімальна конфігурація:

json5Copy code
[code]
    {  channels: {    mattermost: {      enabled: true,      botToken: "mm-token",      baseUrl: "https://chat.example.com",      dmPolicy: "pairing",    },  },}
[/code]

## Вбудовані slash-команди

Вбудовані slash-команди вмикаються явно. Коли їх увімкнено, OpenClaw реєструє slash-команди `oc_*` через API Mattermost і отримує callback POST-запити на HTTP-сервері gateway.

json5Copy code
[code]
    {  channels: {    mattermost: {      commands: {        native: true,        nativeSkills: true,        callbackPath: "/api/channels/mattermost/command",        // Use when Mattermost cannot reach the gateway directly (reverse proxy/public URL).        callbackUrl: "https://gateway.example.com/api/channels/mattermost/command",      },    },  },}
[/code]

Примітки щодо поведінки

  * `native: "auto"` для Mattermost за замовчуванням вимкнено. Задайте `native: true`, щоб увімкнути.
  * Якщо `callbackUrl` пропущено, OpenClaw виводить його з хоста/порту gateway + `callbackPath`.
  * Для налаштувань із кількома обліковими записами `commands` можна задати на верхньому рівні або в `channels.mattermost.accounts.<id>.commands` (значення облікового запису перевизначають поля верхнього рівня).
  * Callback-запити команд перевіряються за токенами для кожної команди, які Mattermost повертає, коли OpenClaw реєструє команди `oc_*`.
  * OpenClaw оновлює поточну реєстрацію команд Mattermost перед прийняттям кожного callback-запиту, тож застарілі токени з видалених або повторно згенерованих slash-команд припиняють прийматися без перезапуску gateway.
  * Перевірка callback-запиту завершується закрито, якщо API Mattermost не може підтвердити, що команда досі актуальна; невдалі перевірки коротко кешуються, одночасні пошуки об’єднуються, а запуск нових пошуків обмежується за частотою для кожної команди, щоб стримувати тиск повторного відтворення.
  * Slash-callback-запити завершуються закрито, коли реєстрація не вдалася, запуск був частковим або токен callback-запиту не збігається із зареєстрованим токеном розв’язаної команди (токен, чинний для однієї команди, не може дійти до upstream-перевірки для іншої команди).

Вимога доступності

Кінцева точка callback має бути доступною із сервера Mattermost.

  * Не задавайте `callbackUrl` як `localhost`, якщо Mattermost не працює на тому самому хості або в тому самому мережевому просторі імен, що й OpenClaw.
  * Не задавайте `callbackUrl` як базову URL-адресу Mattermost, якщо ця URL-адреса не reverse-proxy-ть `/api/channels/mattermost/command` до OpenClaw.
  * Швидка перевірка: `curl https://<gateway-host>/api/channels/mattermost/command`; GET має повернути `405 Method Not Allowed` від OpenClaw, а не `404`.

Allowlist вихідних з’єднань Mattermost

Якщо ваш callback спрямовано на приватні/tailnet/внутрішні адреси, задайте Mattermost `ServiceSettings.AllowedUntrustedInternalConnections`, щоб включити хост/домен callback.

Використовуйте записи хоста/домену, а не повні URL-адреси.

  * Добре: `gateway.tailnet-name.ts.net`
  * Погано: `https://gateway.tailnet-name.ts.net`


## Змінні середовища (обліковий запис за замовчуванням)

Задайте їх на хості gateway, якщо віддаєте перевагу змінним середовища:

  * `MATTERMOST_BOT_TOKEN=...`
  * `MATTERMOST_URL=https://chat.example.com`


## Режими чату

Mattermost автоматично відповідає на особисті повідомлення. Поведінка в каналі контролюється параметром `chatmode`:

### oncall (за замовчуванням)

Відповідати в каналах лише при @згадуванні.

### onmessage

Відповідати на кожне повідомлення каналу.

### onchar

Відповідати, коли повідомлення починається з префікса-тригера.

Приклад конфігурації:

json5Copy code
[code]
    {  channels: {    mattermost: {      chatmode: "onchar",      oncharPrefixes: [">", "!"],    },  },}
[/code]

Примітки:

  * `onchar` усе одно відповідає на явні @згадування.
  * `channels.mattermost.requireMention` підтримується для застарілих конфігурацій, але бажано використовувати `chatmode`.


## Потоки та сеанси

Використовуйте `channels.mattermost.replyToMode`, щоб керувати тим, чи відповіді в каналах і групах залишаються в основному каналі, чи запускають потік під дописом-тригером.

  * `off` (за замовчуванням): відповідати в потоці лише тоді, коли вхідний допис уже в потоці.
  * `first`: для дописів верхнього рівня в каналі/групі запустити потік під цим дописом і маршрутизувати розмову до сеансу з областю видимості потоку.
  * `all`: така сама поведінка, як `first`, для Mattermost на сьогодні.
  * Особисті повідомлення ігнорують це налаштування та залишаються без потоків.


Приклад конфігурації:

json5Copy code
[code]
    {  channels: {    mattermost: {      replyToMode: "all",    },  },}
[/code]

Примітки:

  * Сеанси з областю видимості потоку використовують id допису-тригера як корінь потоку.
  * `first` і `all` наразі еквівалентні, бо щойно Mattermost має корінь потоку, наступні фрагменти й медіа продовжуються в тому самому потоці.


## Контроль доступу (особисті повідомлення)

  * За замовчуванням: `channels.mattermost.dmPolicy = "pairing"` (невідомі відправники отримують код сполучення).
  * Підтвердьте через: 
    * `openclaw pairing list mattermost`
    * `openclaw pairing approve mattermost &lt;CODE&gt;`
  * Публічні особисті повідомлення: `channels.mattermost.dmPolicy="open"` плюс `channels.mattermost.allowFrom=["*"]`.
  * `channels.mattermost.allowFrom` приймає записи `accessGroup:<name>`. Див. [групи доступу](</uk/channels/access-groups>).


## Канали (групи)

  * За замовчуванням: `channels.mattermost.groupPolicy = "allowlist"` (з доступом через згадування).
  * Додайте відправників до allowlist за допомогою `channels.mattermost.groupAllowFrom` (рекомендовано ID користувачів).
  * `channels.mattermost.groupAllowFrom` приймає записи `accessGroup:<name>`. Див. [групи доступу](</uk/channels/access-groups>).
  * Перевизначення згадувань для окремих каналів містяться в `channels.mattermost.groups.<channelId>.requireMention` або `channels.mattermost.groups["*"].requireMention` для значення за замовчуванням.
  * Зіставлення `@username` є змінним і вмикається лише коли `channels.mattermost.dangerouslyAllowNameMatching: true`.
  * Відкриті канали: `channels.mattermost.groupPolicy="open"` (з доступом через згадування).
  * Примітка щодо runtime: якщо `channels.mattermost` повністю відсутній, runtime повертається до `groupPolicy="allowlist"` для перевірок груп (навіть якщо задано `channels.defaults.groupPolicy`).


Приклад:

json5Copy code
[code]
    {  channels: {    mattermost: {      groupPolicy: "open",      groups: {        "*": { requireMention: true },        "team-channel-id": { requireMention: false },      },    },  },}
[/code]

## Цілі для вихідної доставки

Використовуйте ці формати цілей з `openclaw message send` або cron/webhooks:

  * `channel:<id>` для каналу
  * `user:<id>` для особистого повідомлення
  * `@username` для особистого повідомлення (розв’язується через API Mattermost)


## Повторні спроби для каналу особистих повідомлень

Коли OpenClaw надсилає до цілі особистого повідомлення Mattermost і спершу має розв’язати прямий канал, він за замовчуванням повторює спроби після тимчасових помилок створення прямого каналу.

Використовуйте `channels.mattermost.dmChannelRetry`, щоб налаштувати цю поведінку глобально для plugin Mattermost, або `channels.mattermost.accounts.<id>.dmChannelRetry` для одного облікового запису.

json5Copy code
[code]
    {  channels: {    mattermost: {      dmChannelRetry: {        maxRetries: 3,        initialDelayMs: 1000,        maxDelayMs: 10000,        timeoutMs: 30000,      },    },  },}
[/code]

Примітки:

  * Це застосовується лише до створення каналу особистих повідомлень (`/api/v4/channels/direct`), а не до кожного виклику API Mattermost.
  * Повторні спроби застосовуються до тимчасових збоїв, як-от обмеження частоти, відповіді 5xx і помилки мережі або тайм-ауту.
  * Клієнтські помилки 4xx, крім `429`, вважаються постійними й не повторюються.


## Streaming попереднього перегляду

Mattermost транслює міркування, активність інструментів і частковий текст відповіді в один **чернетковий допис попереднього перегляду** , який фіналізується на місці, коли остаточну відповідь безпечно надсилати. Попередній перегляд оновлюється в тому самому id допису замість засмічення каналу повідомленнями для кожного фрагмента. Остаточні медіа/помилки скасовують очікувані редагування попереднього перегляду й використовують звичайну доставку замість скидання одноразового допису попереднього перегляду.

Увімкніть через `channels.mattermost.streaming`:

json5Copy code
[code]
    {  channels: {    mattermost: {      streaming: "partial", // off | partial | block | progress    },  },}
[/code]

Режими streaming

  * `partial` — звичайний вибір: один допис попереднього перегляду, який редагується в міру зростання відповіді, а потім фіналізується з повною відповіддю.
  * `block` використовує чернеткові фрагменти в стилі додавання всередині допису попереднього перегляду.
  * `progress` показує статусний попередній перегляд під час генерації та публікує остаточну відповідь лише після завершення.
  * `off` вимикає streaming попереднього перегляду.

Примітки щодо поведінки streaming

  * Якщо stream не можна фіналізувати на місці (наприклад, допис було видалено посеред stream), OpenClaw повертається до надсилання нового остаточного допису, щоб відповідь ніколи не загубилася.
  * Payload-и лише з міркуваннями пригнічуються в дописах каналу, включно з текстом, що надходить як blockquote `> Reasoning:`. Задайте `/reasoning on`, щоб бачити міркування в інших поверхнях; остаточний допис Mattermost зберігає лише відповідь.
  * Див. [Streaming](</uk/concepts/streaming#preview-streaming-modes>) для матриці зіставлення каналів.


## Реакції (інструмент повідомлень)

  * Використовуйте `message action=react` з `channel=mattermost`.
  * `messageId` — це id допису Mattermost.
  * `emoji` приймає назви на кшталт `thumbsup` або `:+1:` (двокрапки необов’язкові).
  * Задайте `remove=true` (boolean), щоб видалити реакцію.
  * Події додавання/видалення реакцій пересилаються як системні події до маршрутизованого сеансу агента.


Приклади:

CodeCopy code
[code]
    message action=react channel=mattermost target=channel:<channelId> messageId=<postId> emoji=thumbsupmessage action=react channel=mattermost target=channel:<channelId> messageId=<postId> emoji=thumbsup remove=true
[/code]

Конфігурація:

  * `channels.mattermost.actions.reactions`: увімкнути/вимкнути дії реакцій (за замовчуванням true).
  * Перевизначення для облікового запису: `channels.mattermost.accounts.<id>.actions.reactions`.


## Інтерактивні кнопки (інструмент повідомлень)

Надсилайте повідомлення з клікабельними кнопками. Коли користувач натискає кнопку, агент отримує вибір і може відповісти.

Увімкніть кнопки, додавши `inlineButtons` до можливостей каналу:

json5Copy code
[code]
    {  channels: {    mattermost: {      capabilities: ["inlineButtons"],    },  },}
[/code]

Використовуйте `message action=send` з параметром `buttons`. Кнопки — це 2D-масив (рядки кнопок):

CodeCopy code
[code]
    message action=send channel=mattermost target=channel:<channelId> buttons=[[{"text":"Yes","callback_data":"yes"},{"text":"No","callback_data":"no"}]]
[/code]

Поля кнопки:

Відображувана мітка.

Значення, яке надсилається назад під час натискання (використовується як ID дії).

Стиль кнопки.

Коли користувач натискає кнопку:

* ### Кнопки замінено підтвердженням

Усі кнопки замінюються рядком підтвердження (наприклад, "✓ **Yes** selected by @user").

* ### Агент отримує вибір

Агент отримує вибір як вхідне повідомлення й відповідає.

Нотатки щодо реалізації

  * Зворотні виклики кнопок використовують перевірку HMAC-SHA256 (автоматично, конфігурація не потрібна).
  * Mattermost вилучає дані зворотного виклику зі своїх відповідей API (функція безпеки), тому всі кнопки видаляються під час натискання - часткове видалення неможливе.
  * ID дій, що містять дефіси або підкреслення, автоматично очищуються (обмеження маршрутизації Mattermost).

Конфігурація та доступність

  * `channels.mattermost.capabilities`: масив рядків можливостей. Додайте `"inlineButtons"`, щоб увімкнути опис інструмента кнопок у системній підказці агента.
  * `channels.mattermost.interactions.callbackBaseUrl`: необов'язкова зовнішня базова URL-адреса для зворотних викликів кнопок (наприклад, `https://gateway.example.com`). Використовуйте це, коли Mattermost не може напряму досягти gateway за його прив'язаним хостом.
  * У налаштуваннях із кількома обліковими записами можна також встановити те саме поле в `channels.mattermost.accounts.<id>.interactions.callbackBaseUrl`.
  * Якщо `interactions.callbackBaseUrl` опущено, OpenClaw виводить URL-адресу зворотного виклику з `gateway.customBindHost` \+ `gateway.port`, а потім повертається до `http://localhost:<port>`.
  * Правило доступності: URL-адреса зворотного виклику кнопки має бути доступною із сервера Mattermost. `localhost` працює лише тоді, коли Mattermost і OpenClaw працюють на тому самому хості/у тому самому мережевому просторі імен.
  * Якщо ваша ціль зворотного виклику приватна/tailnet/внутрішня, додайте її хост/домен до Mattermost `ServiceSettings.AllowedUntrustedInternalConnections`.


### Пряма інтеграція API (зовнішні скрипти)

Зовнішні скрипти й webhooks можуть публікувати кнопки напряму через Mattermost REST API замість проходження через інструмент `message` агента. За можливості використовуйте `buildButtonAttachments()` із plugin; якщо публікуєте сирий JSON, дотримуйтеся цих правил:

**Структура навантаження:**

json5Copy code
[code]
    {  channel_id: "<channelId>",  message: "Choose an option:",  props: {    attachments: [      {        actions: [          {            id: "mybutton01", // alphanumeric only - see below            type: "button", // required, or clicks are silently ignored            name: "Approve", // display label            style: "primary", // optional: "default", "primary", "danger"            integration: {              url: "https://gateway.example.com/mattermost/interactions/default",              context: {                action_id: "mybutton01", // must match button id (for name lookup)                action: "approve",                // ... any custom fields ...                _token: "<hmac>", // see HMAC section below              },            },          },        ],      },    ],  },}
[/code]

**Генерація токена HMAC**

Gateway перевіряє натискання кнопок за допомогою HMAC-SHA256. Зовнішні скрипти мають генерувати токени, які відповідають логіці перевірки gateway:

* ### Виведіть секрет із токена бота

`HMAC-SHA256(key="openclaw-mattermost-interactions", data=botToken)`

* ### Створіть об'єкт контексту

Створіть об'єкт контексту з усіма полями **крім** `_token`.

* ### Серіалізуйте з відсортованими ключами

Серіалізуйте з **відсортованими ключами** та **без пробілів** (gateway використовує `JSON.stringify` з відсортованими ключами, що створює компактний вивід).

* ### Підпишіть навантаження

`HMAC-SHA256(key=secret, data=serializedContext)`

* ### Додайте токен

Додайте отриманий шістнадцятковий дайджест як `_token` у контексті.

Приклад Python:

pythonCopy code
[code]
     secret = hmac.new(    b"openclaw-mattermost-interactions",    bot_token.encode(), hashlib.sha256).hexdigest() ctx = {"action_id": "mybutton01", "action": "approve"}payload = json.dumps(ctx, sort_keys=True, separators=(",", ":"))token = hmac.new(secret.encode(), payload.encode(), hashlib.sha256).hexdigest() context = {**ctx, "_token": token}
[/code]

Поширені помилки HMAC

  * `json.dumps` у Python типово додає пробіли (`{"key": "val"}`). Використовуйте `separators=(",", ":")`, щоб відповідати компактному виводу JavaScript (`{"key":"val"}`).
  * Завжди підписуйте **всі** поля контексту (без `_token`). Gateway вилучає `_token`, а потім підписує все, що залишилося. Підписування підмножини спричиняє мовчазну помилку перевірки.
  * Використовуйте `sort_keys=True` \- gateway сортує ключі перед підписуванням, а Mattermost може перевпорядковувати поля контексту під час збереження навантаження.
  * Виводьте секрет із токена бота (детерміновано), а не з випадкових байтів. Секрет має бути однаковим у процесі, який створює кнопки, і в gateway, який перевіряє.


## Адаптер каталогу

Plugin Mattermost містить адаптер каталогу, який розв'язує назви каналів і користувачів через Mattermost API. Це вмикає цілі `#channel-name` і `@username` в `openclaw message send` та доставках cron/webhook.

Конфігурація не потрібна - адаптер використовує токен бота з конфігурації облікового запису.

## Кілька облікових записів

Mattermost підтримує кілька облікових записів у `channels.mattermost.accounts`:

json5Copy code
[code]
    {  channels: {    mattermost: {      accounts: {        default: { name: "Primary", botToken: "mm-token", baseUrl: "https://chat.example.com" },        alerts: { name: "Alerts", botToken: "mm-token-2", baseUrl: "https://alerts.example.com" },      },    },  },}
[/code]

## Усунення несправностей

Немає відповідей у каналах

Переконайтеся, що бот перебуває в каналі, і згадайте його (oncall), використовуйте префікс тригера (onchar) або встановіть `chatmode: "onmessage"`.

Помилки автентифікації або кількох облікових записів

  * Перевірте токен бота, базову URL-адресу та чи ввімкнено обліковий запис.
  * Проблеми з кількома обліковими записами: змінні середовища застосовуються лише до облікового запису `default`.

Власні команди зі скісною рискою не працюють

  * `Unauthorized: invalid command token.`: OpenClaw не прийняв токен зворотного виклику. Типові причини: 
    * реєстрація команди зі скісною рискою не вдалася або лише частково завершилася під час запуску
    * зворотний виклик потрапляє не в той gateway/обліковий запис
    * Mattermost усе ще має старі команди, що вказують на попередню ціль зворотного виклику
    * gateway перезапустився без повторної активації команд зі скісною рискою
  * Якщо власні команди зі скісною рискою перестали працювати, перевірте журнали на `mattermost: failed to register slash commands` або `mattermost: native slash commands enabled but no commands could be registered`.
  * Якщо `callbackUrl` опущено, а журнали попереджають, що зворотний виклик розв'язано до `http://127.0.0.1:18789/...`, ця URL-адреса, ймовірно, доступна лише тоді, коли Mattermost працює на тому самому хості/у тому самому мережевому просторі імен, що й OpenClaw. Натомість задайте явний зовнішньо доступний `commands.callbackUrl`.

Проблеми з кнопками

  * Кнопки відображаються як білі прямокутники: агент може надсилати неправильно сформовані дані кнопок. Перевірте, що кожна кнопка має поля `text` і `callback_data`.
  * Кнопки відображаються, але натискання нічого не роблять: перевірте, що `AllowedUntrustedInternalConnections` у конфігурації сервера Mattermost містить `127.0.0.1 localhost`, а `EnablePostActionIntegration` має значення `true` у ServiceSettings.
  * Кнопки повертають 404 під час натискання: `id` кнопки, ймовірно, містить дефіси або підкреслення. Маршрутизатор дій Mattermost ламається на небуквено-цифрових ID. Використовуйте лише `[a-zA-Z0-9]`.
  * Журнали Gateway показують `invalid _token`: невідповідність HMAC. Перевірте, що ви підписуєте всі поля контексту (не підмножину), використовуєте відсортовані ключі та компактний JSON (без пробілів). Дивіться розділ HMAC вище.
  * Журнали Gateway показують `missing _token in context`: поле `_token` відсутнє в контексті кнопки. Переконайтеся, що воно включене під час створення навантаження інтеграції.
  * Підтвердження показує сирий ID замість назви кнопки: `context.action_id` не відповідає `id` кнопки. Встановіть обидва в однакове очищене значення.
  * Агент не знає про кнопки: додайте `capabilities: ["inlineButtons"]` до конфігурації каналу Mattermost.


## Пов'язане

  * [Маршрутизація каналів](</uk/channels/channel-routing>) \- маршрутизація сеансів для повідомлень
  * [Огляд каналів](</uk/channels>) \- усі підтримувані канали
  * [Групи](</uk/channels/groups>) \- поведінка групових чатів і контроль згадок
  * [Спарювання](</uk/channels/pairing>) \- автентифікація DM і потік спарювання
  * [Безпека](</uk/gateway/security>) \- модель доступу та посилення безпеки


Was this useful?YesNo