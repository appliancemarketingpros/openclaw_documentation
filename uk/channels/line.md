---
title: РЯДОК
source_url: https://docs.openclaw.ai/uk/channels/line
scraped_at: 2026-05-25
---

LINE підключається до OpenClaw через LINE Messaging API. Plugin працює як отримувач Webhook на Gateway і використовує ваш channel access token + channel secret для автентифікації.

Статус: завантажуваний Plugin. Підтримуються особисті повідомлення, групові чати, медіа, локації, Flex messages, template messages і quick replies. Реакції та потоки не підтримуються.

## Установлення

Установіть LINE перед налаштуванням каналу:

bashCopy code
[code]
    openclaw plugins install @openclaw/line
[/code]

Локальна копія (під час запуску з git-репозиторію):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/line-plugin
[/code]

## Налаштування

  1. Створіть обліковий запис LINE Developers і відкрийте Console: <https://developers.line.biz/console/>
  2. Створіть (або виберіть) Provider і додайте канал **Messaging API**.
  3. Скопіюйте **Channel access token** і **Channel secret** з налаштувань каналу.
  4. Увімкніть **Use webhook** у налаштуваннях Messaging API.
  5. Установіть URL Webhook на endpoint вашого Gateway (потрібен HTTPS):

CodeCopy code
[code]
    https://gateway-host/line/webhook
[/code]

Gateway відповідає на перевірку Webhook від LINE (GET) і вхідні події (POST). Якщо вам потрібен власний шлях, установіть `channels.line.webhookPath` або `channels.line.accounts.<id>.webhookPath` і відповідно оновіть URL.

Примітка щодо безпеки:

  * Перевірка підпису LINE залежить від тіла (HMAC над сирим тілом), тому OpenClaw застосовує строгі ліміти тіла до автентифікації та тайм-аут перед перевіркою.
  * OpenClaw обробляє події Webhook з перевірених сирих байтів запиту. Значення `req.body`, перетворені проміжним ПЗ upstream, ігноруються для безпеки цілісності підпису.


## Конфігурація

Мінімальна конфігурація:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "pairing",    },  },}
[/code]

Публічна конфігурація DM:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "open",      allowFrom: ["*"],    },  },}
[/code]

Змінні середовища (лише стандартний обліковий запис):

  * `LINE_CHANNEL_ACCESS_TOKEN`
  * `LINE_CHANNEL_SECRET`


Файли токена/секрету:

json5Copy code
[code]
    {  channels: {    line: {      tokenFile: "/path/to/line-token.txt",      secretFile: "/path/to/line-secret.txt",    },  },}
[/code]

`tokenFile` і `secretFile` мають указувати на звичайні файли. Символічні посилання відхиляються.

Кілька облікових записів:

json5Copy code
[code]
    {  channels: {    line: {      accounts: {        marketing: {          channelAccessToken: "...",          channelSecret: "...",          webhookPath: "/line/marketing",        },      },    },  },}
[/code]

## Керування доступом

Для особистих повідомлень за замовчуванням використовується спарювання. Невідомі відправники отримують код спарювання, а їхні повідомлення ігноруються, доки їх не буде схвалено.

bashCopy code
[code]
    openclaw pairing list lineopenclaw pairing approve line &lt;CODE&gt;
[/code]

Списки дозволених і політики:

  * `channels.line.dmPolicy`: `pairing | allowlist | open | disabled`
  * `channels.line.allowFrom`: дозволені LINE user IDs для DM; `dmPolicy: "open"` потребує `["*"]`
  * `channels.line.groupPolicy`: `allowlist | open | disabled`
  * `channels.line.groupAllowFrom`: дозволені LINE user IDs для груп
  * Перевизначення для окремих груп: `channels.line.groups.<groupId>.allowFrom`
  * Статичні групи доступу відправників можна посилатися з `allowFrom`, `groupAllowFrom` і групового `allowFrom` за допомогою `accessGroup:<name>`.
  * Примітка щодо runtime: якщо `channels.line` повністю відсутній, runtime повертається до `groupPolicy="allowlist"` для перевірок груп (навіть якщо встановлено `channels.defaults.groupPolicy`).


LINE IDs чутливі до регістру. Дійсні IDs мають такий вигляд:

  * Користувач: `U` \+ 32 шістнадцяткові символи
  * Група: `C` \+ 32 шістнадцяткові символи
  * Кімната: `R` \+ 32 шістнадцяткові символи


## Поведінка повідомлень

  * Текст розбивається на частини по 5000 символів.
  * Форматування Markdown вилучається; блоки коду й таблиці за можливості перетворюються на Flex cards.
  * Потокові відповіді буферизуються; LINE отримує повні частини з анімацією завантаження, доки агент працює.
  * Завантаження медіа обмежені `channels.line.mediaMaxMb` (за замовчуванням 10).
  * Вхідні медіа зберігаються в `~/.openclaw/media/inbound/` перед передаванням агенту, відповідно до спільного сховища медіа, яке використовують інші вбудовані channel plugins.


## Дані каналу (насичені повідомлення)

Використовуйте `channelData.line`, щоб надсилати quick replies, локації, Flex cards або template messages.

json5Copy code
[code]
    {  text: "Here you go",  channelData: {    line: {      quickReplies: ["Status", "Help"],      location: {        title: "Office",        address: "123 Main St",        latitude: 35.681236,        longitude: 139.767125,      },      flexMessage: {        altText: "Status card",        contents: {          /* Flex payload */        },      },      templateMessage: {        type: "confirm",        text: "Proceed?",        confirmLabel: "Yes",        confirmData: "yes",        cancelLabel: "No",        cancelData: "no",      },    },  },}
[/code]

LINE Plugin також постачається з командою `/card` для шаблонів Flex message:

CodeCopy code
[code]
    /card info "Welcome" "Thanks for joining!"
[/code]

## Підтримка ACP

LINE підтримує прив’язки розмов ACP (Agent Communication Protocol):

  * `/acp spawn <agent> --bind here` прив’язує поточний чат LINE до сесії ACP без створення дочірнього потоку.
  * Налаштовані прив’язки ACP і активні сесії ACP, прив’язані до розмови, працюють у LINE так само, як в інших каналах розмов.


Докладніше див. [Агенти ACP](</uk/tools/acp-agents>).

## Вихідні медіа

LINE Plugin підтримує надсилання зображень, відео й аудіофайлів через інструмент повідомлень агента. Медіа надсилаються через специфічний для LINE шлях доставки з належною обробкою попереднього перегляду та відстеження:

  * **Зображення** : надсилаються як повідомлення із зображеннями LINE з автоматичною генерацією попереднього перегляду.
  * **Відео** : надсилаються з явною обробкою попереднього перегляду та content-type.
  * **Аудіо** : надсилаються як аудіоповідомлення LINE.


URL-адреси вихідних медіа мають бути публічними HTTPS URL. OpenClaw перевіряє цільове ім’я хоста перед передаванням URL до LINE і відхиляє цілі loopback, link-local і приватної мережі.

Загальні надсилання медіа повертаються до наявного маршруту лише для зображень, коли специфічний для LINE шлях недоступний.

## Усунення несправностей

  * **Помилка перевірки Webhook:** переконайтеся, що URL Webhook використовує HTTPS, а `channelSecret` відповідає консолі LINE.
  * **Немає вхідних подій:** підтвердьте, що шлях Webhook відповідає `channels.line.webhookPath` і що Gateway доступний з LINE.
  * **Помилки завантаження медіа:** збільште `channels.line.mediaMaxMb`, якщо медіа перевищує стандартний ліміт.


## Пов’язане

  * [Огляд каналів](</uk/channels>) — усі підтримувані канали
  * [Спарювання](</uk/channels/pairing>) — автентифікація DM і процес спарювання
  * [Групи](</uk/channels/groups>) — поведінка групового чату та обмеження згадками
  * [Маршрутизація каналів](</uk/channels/channel-routing>) — маршрутизація сесій для повідомлень
  * [Безпека](</uk/gateway/security>) — модель доступу та посилення захисту


Was this useful?YesNo