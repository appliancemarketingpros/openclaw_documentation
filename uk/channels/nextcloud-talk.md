---
title: Nextcloud Talk
source_url: https://docs.openclaw.ai/uk/channels/nextcloud-talk
scraped_at: 2026-05-25
---

Стан: bundled plugin (webhook бот). Direct messages, кімнати, реакції та повідомлення markdown підтримуються.

## Bundled plugin

Nextcloud Talk постачається як bundled plugin у поточних випусках OpenClaw, тому звичайні пакетовані збірки не потребують окремого встановлення.

Якщо ви використовуєте старішу збірку або власне встановлення, що виключає Nextcloud Talk, встановіть npm-пакет напряму:

Встановлення через CLI (npm registry):

bashCopy code
[code]
    openclaw plugins install @openclaw/nextcloud-talk
[/code]

Використовуйте bare package, щоб стежити за поточним офіційним release tag. Закріплюйте точну версію лише тоді, коли вам потрібне відтворюване встановлення.

Локальний checkout (під час запуску з git repo):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/nextcloud-talk-plugin
[/code]

Докладніше: [Plugins](</uk/tools/plugin>)

## Швидке налаштування (для початківців)

  1. Переконайтеся, що Plugin Nextcloud Talk доступний.

     * Поточні пакетовані випуски OpenClaw вже містять його.
     * Старіші/власні встановлення можуть додати його вручну за допомогою команд вище.
  2. На вашому сервері Nextcloud створіть бота:

bashCopy code
[code]./occ talk:bot:install "OpenClaw" "<shared-secret>" "<webhook-url>" --feature webhook --feature response --feature reaction
[/code]

  3. Увімкніть бота в налаштуваннях цільової кімнати.

  4. Налаштуйте OpenClaw:

     * Конфігурація: `channels.nextcloud-talk.baseUrl` \+ `channels.nextcloud-talk.botSecret`
     * Або env: `NEXTCLOUD_TALK_BOT_SECRET` (лише обліковий запис за замовчуванням)

Налаштування CLI:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --url https://cloud.example.com \  --token "<shared-secret>"
[/code]

Еквівалентні явні поля:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret "<shared-secret>"
[/code]

Секрет із файлу:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret-file /path/to/nextcloud-talk-secret
[/code]

  5. Перезапустіть Gateway (або завершіть налаштування).


Мінімальна конфігурація:

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      enabled: true,      baseUrl: "https://cloud.example.com",      botSecret: "shared-secret",      dmPolicy: "pairing",    },  },}
[/code]

## Примітки

  * Боти не можуть ініціювати DMs. Користувач має спочатку надіслати повідомлення боту.
  * URL Webhook має бути доступним для Gateway; установіть `webhookPublicUrl`, якщо він за проксі.
  * Завантаження медіа не підтримуються bot API; медіа надсилаються як URLs.
  * Корисне навантаження webhook не розрізняє DMs і кімнати; установіть `apiUser` \+ `apiPassword`, щоб увімкнути визначення типу кімнати (інакше DMs обробляються як кімнати).


## Контроль доступу (DMs)

  * За замовчуванням: `channels.nextcloud-talk.dmPolicy = "pairing"`. Невідомі відправники отримують код сполучення.
  * Схваліть через: 
    * `openclaw pairing list nextcloud-talk`
    * `openclaw pairing approve nextcloud-talk &lt;CODE&gt;`
  * Публічні DMs: `channels.nextcloud-talk.dmPolicy="open"` плюс `channels.nextcloud-talk.allowFrom=["*"]`.
  * `allowFrom` зіставляє лише IDs користувачів Nextcloud; відображувані імена ігноруються.


## Кімнати (групи)

  * За замовчуванням: `channels.nextcloud-talk.groupPolicy = "allowlist"` (керовано згадками).
  * Додавайте кімнати до allowlist за допомогою `channels.nextcloud-talk.rooms`:

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      rooms: {        "room-token": { requireMention: true },      },    },  },}
[/code]

  * Щоб не дозволяти жодних кімнат, залиште allowlist порожнім або встановіть `channels.nextcloud-talk.groupPolicy="disabled"`.


## Можливості

Функція | Стан  
---|---  
Direct messages | Підтримується  
Кімнати | Підтримується  
Ланцюжки | Не підтримується  
Медіа | Лише URL  
Реакції | Підтримується  
Нативні команди | Не підтримується  
  
## Довідник конфігурації (Nextcloud Talk)

Повна конфігурація: [Конфігурація](</uk/gateway/configuration>)

Параметри провайдера:

  * `channels.nextcloud-talk.enabled`: увімкнути/вимкнути запуск каналу.
  * `channels.nextcloud-talk.baseUrl`: URL інстансу Nextcloud.
  * `channels.nextcloud-talk.botSecret`: спільний секрет бота.
  * `channels.nextcloud-talk.botSecretFile`: шлях до секрету у звичайному файлі. Symlinks відхиляються.
  * `channels.nextcloud-talk.apiUser`: користувач API для пошуку кімнат (визначення DM).
  * `channels.nextcloud-talk.apiPassword`: пароль API/app для пошуку кімнат.
  * `channels.nextcloud-talk.apiPasswordFile`: шлях до файлу пароля API.
  * `channels.nextcloud-talk.webhookPort`: порт слухача webhook (за замовчуванням: 8788).
  * `channels.nextcloud-talk.webhookHost`: хост webhook (за замовчуванням: 0.0.0.0).
  * `channels.nextcloud-talk.webhookPath`: шлях webhook (за замовчуванням: /nextcloud-talk-webhook).
  * `channels.nextcloud-talk.webhookPublicUrl`: зовнішньо доступний URL webhook.
  * `channels.nextcloud-talk.dmPolicy`: `pairing | allowlist | open | disabled`.
  * `channels.nextcloud-talk.allowFrom`: allowlist для DM (IDs користувачів). `open` потребує `"*"`.
  * `channels.nextcloud-talk.groupPolicy`: `allowlist | open | disabled`.
  * `channels.nextcloud-talk.groupAllowFrom`: allowlist для груп (IDs користувачів).
  * `channels.nextcloud-talk.rooms`: налаштування й allowlist для окремих кімнат.
  * Статичні групи доступу відправників можна посилати з `allowFrom` і `groupAllowFrom` через `accessGroup:<name>`.
  * `channels.nextcloud-talk.historyLimit`: ліміт історії групи (0 вимикає).
  * `channels.nextcloud-talk.dmHistoryLimit`: ліміт історії DM (0 вимикає).
  * `channels.nextcloud-talk.dms`: перевизначення для окремих DM (historyLimit).
  * `channels.nextcloud-talk.textChunkLimit`: розмір вихідного текстового фрагмента (символи).
  * `channels.nextcloud-talk.chunkMode`: `length` (за замовчуванням) або `newline` для поділу за порожніми рядками (межами абзаців) перед поділом за довжиною.
  * `channels.nextcloud-talk.blockStreaming`: вимкнути block streaming для цього каналу.
  * `channels.nextcloud-talk.blockStreamingCoalesce`: налаштування об’єднання block streaming.
  * `channels.nextcloud-talk.mediaMaxMb`: ліміт вхідних медіа (MB).


## Пов’язане

  * [Огляд каналів](</uk/channels>) — усі підтримувані канали
  * [Сполучення](</uk/channels/pairing>) — автентифікація DM і потік сполучення
  * [Групи](</uk/channels/groups>) — поведінка групового чату та керування згадками
  * [Маршрутизація каналів](</uk/channels/channel-routing>) — маршрутизація сесій для повідомлень
  * [Безпека](</uk/gateway/security>) — модель доступу та зміцнення захисту


Was this useful?YesNo