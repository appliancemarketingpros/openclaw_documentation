---
title: SMS
source_url: https://docs.openclaw.ai/uk/channels/sms
scraped_at: 2026-06-29
---

Get started

OpenClaw може отримувати й надсилати SMS через телефонний номер Twilio або Messaging Service. Gateway реєструє маршрут вхідного Webhook, за замовчуванням перевіряє підписи запитів Twilio та надсилає відповіді назад через Messages API Twilio.

[**Сполучення** Типова політика DM для SMS — сполучення. ](</uk/channels/pairing>) [**Безпека Gateway** Перегляньте доступність Webhook і засоби контролю доступу відправників. ](</uk/gateway/security>) [**Усунення несправностей каналу** Міжканальна діагностика та інструкції з виправлення. ](</uk/channels/troubleshooting>)

## Перед початком

Вам потрібно:

  * Офіційний Plugin SMS, установлений за допомогою `openclaw plugins install @openclaw/sms`.
  * Обліковий запис Twilio з телефонним номером, що підтримує SMS, або Twilio Messaging Service.
  * Twilio Account SID і Auth Token.
  * Публічна HTTPS-URL-адреса, яка веде до вашого OpenClaw Gateway.
  * Вибір політики відправників: `pairing` для приватного використання, `allowlist` для попередньо схвалених телефонних номерів або `open` лише для навмисно публічного доступу через SMS.


Використовуйте один номер Twilio і для SMS, і для голосових викликів, якщо номер підтримує обидві можливості. Налаштуйте SMS Webhook і голосовий Webhook окремо в Twilio; ця сторінка охоплює лише SMS Webhook.

## Швидке налаштування

* ### Установіть Plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/sms
[/code]

* ### Створіть або виберіть відправника Twilio

У Twilio відкрийте **Phone Numbers > Manage > Active numbers** і виберіть номер, що підтримує SMS. Збережіть:

  * Account SID, наприклад `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
  * Auth Token
  * Телефонний номер відправника, наприклад `+15551234567`


Якщо замість фіксованого номера відправника ви використовуєте Messaging Service, збережіть Messaging Service SID, наприклад `MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.

* ### Налаштуйте канал SMS

Збережіть це як `sms.patch.json5` і змініть заповнювачі:

json5Copy code
[code]
    {channels: {sms: {  enabled: true,  accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  authToken: "twilio-auth-token",  fromNumber: "+15551234567",  publicWebhookUrl: "https://gateway.example.com/webhooks/sms",  dmPolicy: "pairing",},},}
[/code]

Застосуйте його:

bashCopy code
[code]
    openclaw config patch --file ./sms.patch.json5 --dry-runopenclaw config patch --file ./sms.patch.json5
[/code]

* ### Спрямуйте Twilio на Webhook Gateway

У налаштуваннях телефонного номера Twilio відкрийте **Messaging** і встановіть **A message comes in** на:

textCopy code
[code]
    https://gateway.example.com/webhooks/sms
[/code]

Використовуйте HTTP `POST`. Типовий локальний шлях — `/webhooks/sms`; змініть `channels.sms.webhookPath`, якщо потрібен інший маршрут.

* ### Відкрийте точний шлях SMS Webhook

Ваша публічна URL-адреса має маршрутизувати шлях SMS до процесу Gateway. Якщо для локального тестування ви використовуєте Tailscale Funnel, явно відкрийте `/webhooks/sms`:

bashCopy code
[code]
    tailscale funnel --bg --set-path /webhooks/sms http://127.0.0.1:<gateway-port>/webhooks/smstailscale funnel status
[/code]

Голосові виклики й SMS використовують окремі шляхи Webhook. Якщо той самий номер Twilio обробляє обидва, збережіть обидва маршрути налаштованими в Twilio і у вашому тунелі.

* ### Запустіть Gateway і схваліть першого відправника

bashCopy code
[code]
    openclaw gateway
[/code]

Надішліть текстове повідомлення на номер Twilio. Перше повідомлення створює запит на сполучення. Схваліть його:

bashCopy code
[code]
    openclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;
[/code]

Коди сполучення спливають через 1 годину.

## Приклади конфігурації

### Файл конфігурації

Використовуйте налаштування через файл конфігурації, коли хочете, щоб визначення каналу передавалося разом із конфігурацією Gateway:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

### Змінні середовища

Використовуйте налаштування через env для розгортань з одним обліковим записом, де секрети надходять із середовища хоста:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"export TWILIO_AUTH_TOKEN="<twilio-auth-token>"export TWILIO_PHONE_NUMBER="+15551234567"export SMS_PUBLIC_WEBHOOK_URL="https://gateway.example.com/webhooks/sms"
[/code]

Потім увімкніть канал у конфігурації:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

`TWILIO_SMS_FROM` приймається як псевдонім для `TWILIO_PHONE_NUMBER`. Використовуйте `TWILIO_MESSAGING_SERVICE_SID` замість відправника за телефонним номером, коли Twilio має вибирати відправника з Messaging Service.

### Auth Token через SecretRef

`authToken` може бути SecretRef. Використовуйте це, коли Gateway має отримувати Twilio Auth Token із runtime секретів OpenClaw замість збереження конфігурації у відкритому тексті:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: { source: "env", provider: "default", id: "TWILIO_AUTH_TOKEN" },      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Зазначена змінна середовища або постачальник секретів має бути видимим для runtime Gateway. Перезапустіть керовані процеси Gateway після зміни змінних середовища хоста.

### Приватний номер лише зі списком дозволених

Використовуйте `allowlist`, коли лише відомі телефонні номери мають мати змогу спілкуватися з агентом:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "allowlist",      allowFrom: ["+15557654321"],    },  },}
[/code]

### Відправник Messaging Service

Використовуйте `messagingServiceSid` замість `fromNumber`, коли Twilio має вибирати відправника через Messaging Service:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      messagingServiceSid: "MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Якщо після розв’язання конфігурації та env присутні і `fromNumber`, і `messagingServiceSid`, використовується `fromNumber`.

### Типова ціль вихідних повідомлень

Установіть `defaultTo`, коли автоматизація або доставка, ініційована агентом, повинна мати типове місце призначення, якщо потік надсилання не вказує явну ціль:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      defaultTo: "+15557654321",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",    },  },}
[/code]

## Контроль доступу

`channels.sms.dmPolicy` керує прямим доступом через SMS:

  * `pairing` (типово)
  * `allowlist` (потребує щонайменше одного відправника в `allowFrom`)
  * `open` (потребує, щоб `allowFrom` містив `"*"`)
  * `disabled`


Записи `allowFrom` мають бути телефонними номерами E.164, як-от `+15551234567`. Префікси `sms:` приймаються та нормалізуються. Для приватного помічника віддавайте перевагу `dmPolicy: "allowlist"` з явними телефонними номерами.

## Надсилання SMS

Цілі вихідних SMS використовують службовий префікс `sms:` з вибраним каналом SMS:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15551234567 --message "hello"
[/code]

Коли вибір каналу неявний, `twilio-sms:+15551234567` вибирає цей канал, не перебираючи на себе наявний службовий префікс `sms:`, що належить каналу й використовується iMessage.

bashCopy code
[code]
    openclaw message send --target twilio-sms:+15551234567 --message "hello"
[/code]

CLI потребує явного `--target`. `defaultTo` призначений для автоматизації та шляхів доставки, ініційованих агентом, де ціль можна розв’язати з конфігурації каналу.

Відповіді агента з вхідних SMS-розмов автоматично повертаються відправнику через налаштованого відправника Twilio.

Вивід SMS — це звичайний текст. OpenClaw прибирає markdown, вирівнює fenced code blocks, зберігає читабельні посилання та розбиває довгі відповіді на частини перед надсиланням через Twilio.

## Перевірка налаштування

Після запуску Gateway:

  1. Переконайтеся, що журнал Gateway показує маршрут SMS Webhook.
  2. Запустіть перевірку з боку Twilio:

bashCopy code
[code]
    openclaw channels capabilities --channel smsopenclaw channels status --channel sms --probe --json
[/code]

  3. Надішліть SMS на номер Twilio зі свого телефона.
  4. Запустіть `openclaw pairing list sms`.
  5. Схваліть код сполучення за допомогою `openclaw pairing approve sms &lt;CODE&gt;`.
  6. Надішліть ще одне SMS і переконайтеся, що агент відповідає.


Для тестування лише вихідних повідомлень використовуйте:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15557654321 --message "OpenClaw SMS test"
[/code]

### Наскрізний тест з macOS iMessage/SMS

На Mac, який може надсилати операторські SMS через Messages, можна використовувати `imsg`, щоб керувати стороною відправника, не торкаючись телефона:

bashCopy code
[code]
    imsg send --to "+15551234567" --service sms --text "OpenClaw SMS E2E $(date -u +%Y%m%dT%H%M%SZ)" --jsonopenclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;imsg send --to "+15551234567" --service sms --text "reply exactly SMS pong" --json
[/code]

Перше повідомлення має створити запит на сполучення. Друге повідомлення має отримати відповідь агента через Twilio.

## Безпека Webhook

За замовчуванням OpenClaw перевіряє `X-Twilio-Signature` за допомогою `publicWebhookUrl` і `authToken`. Тримайте `publicWebhookUrl` побайтово узгодженою з URL-адресою, налаштованою в Twilio, включно зі схемою, хостом, шляхом і рядком запиту.

Лише для тестування локального тунелю можна встановити:

json5Copy code
[code]
    {  channels: {    sms: {      dangerouslyDisableSignatureValidation: true,    },  },}
[/code]

Не використовуйте вимкнену перевірку підпису на публічному Gateway.

## Конфігурація з кількома обліковими записами

Використовуйте `accounts`, коли працюєте з кількома номерами Twilio:

json5Copy code
[code]
    {  channels: {    sms: {      accounts: {        support: {          enabled: true,          accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",          authToken: "twilio-auth-token",          fromNumber: "+15551234567",          publicWebhookUrl: "https://gateway.example.com/webhooks/sms/support",          webhookPath: "/webhooks/sms/support",          dmPolicy: "allowlist",          allowFrom: ["+15557654321"],        },      },    },  },}
[/code]

Кожен обліковий запис має використовувати окремий `webhookPath`.

## Усунення несправностей

### Twilio повертає 403 або OpenClaw відхиляє Webhook

Перевірте, що `publicWebhookUrl` точно збігається з URL-адресою, налаштованою в Twilio, включно зі схемою, хостом, шляхом і рядком запиту. Twilio підписує рядок публічної URL-адреси, тому переписування проксі та альтернативні імена хостів можуть порушити перевірку підпису.

### Запит на сполучення не з’являється

Перевірте URL-адресу та метод Webhook **Messaging** для номера Twilio. Він має вказувати на URL-адресу SMS Webhook і використовувати `POST`. Також переконайтеся, що Gateway доступний із публічного інтернету або через ваш тунель.

Якщо журнал повідомлень Twilio показує помилку `11200`, Twilio прийняв вхідне SMS, але не зміг дістатися до вашого Webhook. Перевірте:

  * Twilio **Messaging > A message comes in** вказує на `publicWebhookUrl`.
  * Метод — `POST`.
  * Тунель або зворотний проксі відкриває точний `webhookPath`; для Tailscale Funnel запустіть `tailscale funnel status` і переконайтеся, що `/webhooks/sms` є у списку.
  * `publicWebhookUrl` використовує ту саму схему, хост, шлях і рядок запиту, які надсилає Twilio, щоб перевірка підпису могла відтворити підписану URL-адресу.


### Вихідні надсилання не вдаються

Переконайтеся, що `accountSid`, `authToken` і або `fromNumber`, або `messagingServiceSid` розв’язані. Якщо ви використовуєте пробний обліковий запис Twilio, можливо, номер призначення потрібно перевірити в Twilio, перш ніж вихідні SMS надсилатимуться.

### Повідомлення надходять, але агент не відповідає

Перевірте `dmPolicy` і `allowFrom`. За стандартної політики `pairing` відправника потрібно схвалити, перш ніж оброблятимуться звичайні ходи агента.

Was this useful?YesNo

Open issue