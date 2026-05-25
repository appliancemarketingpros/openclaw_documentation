---
title: Tlon
source_url: https://docs.openclaw.ai/uk/channels/tlon
scraped_at: 2026-05-25
---

Tlon — це децентралізований месенджер, побудований на Urbit. OpenClaw підключається до вашого Urbit ship і може відповідати на DM та повідомлення групових чатів. Для групових відповідей за замовчуванням потрібна @-згадка, і їх можна додатково обмежити через allowlist.

Стан: вбудований plugin. Підтримуються DM, групові згадки, відповіді в гілках, форматування розширеного тексту та завантаження зображень. Реакції та опитування поки не підтримуються.

## Вбудований plugin

Tlon постачається як вбудований plugin у поточних випусках OpenClaw, тож звичайні пакетовані збірки не потребують окремого встановлення.

Якщо у вас старіша збірка або власне встановлення, яке не містить Tlon, встановіть поточний npm-пакет:

Встановлення через CLI (npm registry):

bashCopy code
[code]
    openclaw plugins install @openclaw/tlon
[/code]

Використовуйте пакет без версії, щоб стежити за поточним офіційним тегом випуску. Закріплюйте точну версію лише тоді, коли потрібне відтворюване встановлення.

Локальний checkout (під час запуску з git-репозиторію):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/tlon-plugin
[/code]

Докладніше: [Plugins](</uk/tools/plugin>)

## Налаштування

  1. Переконайтеся, що plugin Tlon доступний. 
     * Поточні пакетовані випуски OpenClaw уже містять його.
     * Старіші/власні встановлення можуть додати його вручну командами вище.
  2. Зберіть URL вашого ship і код входу.
  3. Налаштуйте `channels.tlon`.
  4. Перезапустіть gateway.
  5. Надішліть DM боту або згадайте його в груповому каналі.


Мінімальна конфігурація (один обліковий запис):

json5Copy code
[code]
    {  channels: {    tlon: {      enabled: true,      ship: "~sampel-palnet",      url: "https://your-ship-host",      code: "lidlut-tabwed-pillex-ridrup",      ownerShip: "~your-main-ship", // recommended: your ship, always allowed    },  },}
[/code]

## Приватні/LAN ship

За замовчуванням OpenClaw блокує приватні/внутрішні імена хостів та діапазони IP для захисту від SSRF. Якщо ваш ship працює в приватній мережі (localhost, LAN IP або внутрішнє ім'я хоста), потрібно явно ввімкнути це:

json5Copy code
[code]
    {  channels: {    tlon: {      url: "http://localhost:8080",      allowPrivateNetwork: true,    },  },}
[/code]

Це стосується URL на кшталт:

  * `http://localhost:8080`
  * `http://192.168.x.x:8080`
  * `http://my-ship.local:8080`


⚠️ Вмикайте це лише якщо довіряєте своїй локальній мережі. Це налаштування вимикає захист від SSRF для запитів до URL вашого ship.

## Групові канали

Автовиявлення ввімкнено за замовчуванням. Також можна закріпити канали вручну:

json5Copy code
[code]
    {  channels: {    tlon: {      groupChannels: ["chat/~host-ship/general", "chat/~host-ship/support"],    },  },}
[/code]

Вимкнення автовиявлення:

json5Copy code
[code]
    {  channels: {    tlon: {      autoDiscoverChannels: false,    },  },}
[/code]

## Контроль доступу

Allowlist для DM (порожній = DM не дозволені, використовуйте `ownerShip` для потоку схвалення):

json5Copy code
[code]
    {  channels: {    tlon: {      dmAllowlist: ["~zod", "~nec"],    },  },}
[/code]

Авторизація груп (обмежена за замовчуванням):

json5Copy code
[code]
    {  channels: {    tlon: {      defaultAuthorizedShips: ["~zod"],      authorization: {        channelRules: {          "chat/~host-ship/general": {            mode: "restricted",            allowedShips: ["~zod", "~nec"],          },          "chat/~host-ship/announcements": {            mode: "open",          },        },      },    },  },}
[/code]

## Власник і система схвалення

Задайте ship власника, щоб отримувати запити на схвалення, коли неавторизовані користувачі намагаються взаємодіяти:

json5Copy code
[code]
    {  channels: {    tlon: {      ownerShip: "~your-main-ship",    },  },}
[/code]

Ship власника **автоматично авторизований усюди** — запрошення в DM приймаються автоматично, а повідомлення в каналах завжди дозволені. Вам не потрібно додавати власника до `dmAllowlist` або `defaultAuthorizedShips`.

Якщо це налаштовано, власник отримує DM-сповіщення для:

  * Запитів DM від ship, яких немає в allowlist
  * Згадок у каналах без авторизації
  * Запитів на групові запрошення


## Налаштування автоматичного прийняття

Автоматично приймати запрошення в DM (для ship у dmAllowlist):

json5Copy code
[code]
    {  channels: {    tlon: {      autoAcceptDmInvites: true,    },  },}
[/code]

Автоматично приймати групові запрошення від довірених ship:

json5Copy code
[code]
    {  channels: {    tlon: {      autoAcceptGroupInvites: true,      groupInviteAllowlist: ["~zod"],    },  },}
[/code]

`autoAcceptGroupInvites` завершується закрито, коли `groupInviteAllowlist` порожній. Задайте allowlist для ship, чиї групові запрошення слід приймати автоматично.

## Цілі доставлення (CLI/cron)

Використовуйте їх із `openclaw message send` або доставленням через cron:

  * DM: `~sampel-palnet` або `dm/~sampel-palnet`
  * Група: `chat/~host-ship/channel` або `group:~host-ship/channel`


## Вбудований skill

Plugin Tlon містить вбудований skill ([`@tloncorp/tlon-skill`](<https://github.com/tloncorp/tlon-skill>)), який надає CLI-доступ до операцій Tlon:

  * **Контакти** : отримувати/оновлювати профілі, перелічувати контакти
  * **Канали** : перелічувати, створювати, публікувати повідомлення, отримувати історію
  * **Групи** : перелічувати, створювати, керувати учасниками
  * **DM** : надсилати повідомлення, реагувати на повідомлення
  * **Реакції** : додавати/видаляти emoji-реакції до дописів і DM
  * **Налаштування** : керувати дозволами plugin через slash-команди


Skill автоматично доступний після встановлення plugin.

## Можливості

Функція | Стан  
---|---  
Прямі повідомлення | ✅ Підтримується  
Групи/канали | ✅ Підтримується (за замовчуванням через згадку)  
Гілки | ✅ Підтримується (автовідповіді в гілці)  
Розширений текст | ✅ Markdown перетворюється у формат Tlon  
Зображення | ✅ Завантажуються до сховища Tlon  
Реакції | ✅ Через вбудований skill  
Опитування | ❌ Поки не підтримується  
Нативні команди | ✅ Підтримується (за замовчуванням лише власник)  
  
## Усунення несправностей

Спершу виконайте цю послідовність:

bashCopy code
[code]
    openclaw statusopenclaw gateway statusopenclaw logs --followopenclaw doctor
[/code]

Типові збої:

  * **DM ігноруються** : відправника немає в `dmAllowlist`, і `ownerShip` не налаштовано для потоку схвалення.
  * **Групові повідомлення ігноруються** : канал не виявлено або відправник не авторизований.
  * **Помилки підключення** : перевірте, що URL ship доступний; увімкніть `allowPrivateNetwork` для локальних ship.
  * **Помилки автентифікації** : переконайтеся, що код входу актуальний (коди змінюються).


## Довідник конфігурації

Повна конфігурація: [Конфігурація](</uk/gateway/configuration>)

Параметри провайдера:

  * `channels.tlon.enabled`: увімкнути/вимкнути запуск каналу.
  * `channels.tlon.ship`: ім'я Urbit ship бота (наприклад, `~sampel-palnet`).
  * `channels.tlon.url`: URL ship (наприклад, `https://sampel-palnet.tlon.network`).
  * `channels.tlon.code`: код входу ship.
  * `channels.tlon.allowPrivateNetwork`: дозволити localhost/LAN URL (обхід SSRF).
  * `channels.tlon.ownerShip`: ship власника для системи схвалення (завжди авторизований).
  * `channels.tlon.dmAllowlist`: ship, яким дозволено DM (порожній = жодного).
  * `channels.tlon.autoAcceptDmInvites`: автоматично приймати DM від ship з allowlist.
  * `channels.tlon.autoAcceptGroupInvites`: автоматично приймати групові запрошення від ship з allowlist.
  * `channels.tlon.groupInviteAllowlist`: ship, чиї групові запрошення можна автоматично приймати.
  * `channels.tlon.autoDiscoverChannels`: автоматично виявляти групові канали (за замовчуванням: true).
  * `channels.tlon.groupChannels`: вручну закріплені channel nests.
  * `channels.tlon.defaultAuthorizedShips`: ship, авторизовані для всіх каналів.
  * `channels.tlon.authorization.channelRules`: правила авторизації для кожного каналу.
  * `channels.tlon.showModelSignature`: додавати назву моделі до повідомлень.


## Примітки

  * Для групових відповідей потрібна згадка (наприклад, `~your-bot-ship`), щоб відповісти.
  * Відповіді в гілках: якщо вхідне повідомлення в гілці, OpenClaw відповідає в цій гілці.
  * Розширений текст: форматування Markdown (жирний, курсив, код, заголовки, списки) перетворюється в нативний формат Tlon.
  * Зображення: URL завантажуються до сховища Tlon і вбудовуються як блоки зображень.


## Пов'язане

  * [Огляд каналів](</uk/channels>) — усі підтримувані канали
  * [Pairing](</uk/channels/pairing>) — автентифікація DM і потік pairing
  * [Групи](</uk/channels/groups>) — поведінка групового чату та обмеження через згадки
  * [Маршрутизація каналів](</uk/channels/channel-routing>) — маршрутизація сесій для повідомлень
  * [Безпека](</uk/gateway/security>) — модель доступу та посилення захисту


Was this useful?YesNo