---
title: SMS
source_url: https://docs.openclaw.ai/ru/channels/sms
scraped_at: 2026-06-29
---

Get started

OpenClaw может получать и отправлять SMS через телефонный номер Twilio или Messaging Service. Gateway регистрирует маршрут входящего webhook, по умолчанию проверяет подписи запросов Twilio и отправляет ответы обратно через Messages API Twilio.

[**Сопряжение** Политика личных сообщений по умолчанию для SMS — сопряжение. ](</ru/channels/pairing>) [**Безопасность Gateway** Проверьте доступность webhook и средства контроля доступа отправителей. ](</ru/gateway/security>) [**Устранение неполадок каналов** Межканальная диагностика и сценарии восстановления. ](</ru/channels/troubleshooting>)

## Перед началом

Вам нужны:

  * Официальный SMS-Plugin, установленный с помощью `openclaw plugins install @openclaw/sms`.
  * Учетная запись Twilio с телефонным номером, поддерживающим SMS, или Twilio Messaging Service.
  * Twilio Account SID и Auth Token.
  * Публичный HTTPS-URL, который ведет к вашему OpenClaw Gateway.
  * Выбор политики отправителей: `pairing` для частного использования, `allowlist` для заранее одобренных телефонных номеров или `open` только для намеренно публичного SMS-доступа.


Используйте один номер Twilio и для SMS, и для Voice Call, если номер поддерживает обе возможности. Настройте SMS-webhook и Voice-webhook отдельно в Twilio; эта страница описывает только SMS-webhook.

## Быстрая настройка

* ### Установите Plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/sms
[/code]

* ### Создайте или выберите отправителя Twilio

В Twilio откройте **Phone Numbers > Manage > Active numbers** и выберите номер, поддерживающий SMS. Сохраните:

  * Account SID, например `ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`
  * Auth Token
  * Телефонный номер отправителя, например `+15551234567`


Если вместо фиксированного номера отправителя вы используете Messaging Service, сохраните SID Messaging Service, например `MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx`.

* ### Настройте SMS-канал

Сохраните это как `sms.patch.json5` и измените заполнители:

json5Copy code
[code]
    {channels: {sms: {  enabled: true,  accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",  authToken: "twilio-auth-token",  fromNumber: "+15551234567",  publicWebhookUrl: "https://gateway.example.com/webhooks/sms",  dmPolicy: "pairing",},},}
[/code]

Примените его:

bashCopy code
[code]
    openclaw config patch --file ./sms.patch.json5 --dry-runopenclaw config patch --file ./sms.patch.json5
[/code]

* ### Направьте Twilio на webhook Gateway

В настройках телефонного номера Twilio откройте **Messaging** и задайте для **A message comes in** :

textCopy code
[code]
    https://gateway.example.com/webhooks/sms
[/code]

Используйте HTTP `POST`. Локальный путь по умолчанию — `/webhooks/sms`; измените `channels.sms.webhookPath`, если вам нужен другой маршрут.

* ### Откройте точный путь SMS-webhook

Ваш публичный URL должен маршрутизировать SMS-путь к процессу Gateway. Если для локального тестирования вы используете Tailscale Funnel, явно откройте `/webhooks/sms`:

bashCopy code
[code]
    tailscale funnel --bg --set-path /webhooks/sms http://127.0.0.1:<gateway-port>/webhooks/smstailscale funnel status
[/code]

Voice Call и SMS используют отдельные пути webhook. Если один и тот же номер Twilio обрабатывает оба варианта, держите оба маршрута настроенными в Twilio и в вашем туннеле.

* ### Запустите Gateway и одобрите первого отправителя

bashCopy code
[code]
    openclaw gateway
[/code]

Отправьте текстовое сообщение на номер Twilio. Первое сообщение создает запрос на сопряжение. Одобрите его:

bashCopy code
[code]
    openclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;
[/code]

Коды сопряжения истекают через 1 час.

## Примеры конфигурации

### Файл конфигурации

Используйте настройку через файл конфигурации, когда нужно, чтобы определение канала передавалось вместе с конфигурацией Gateway:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

### Переменные окружения

Используйте настройку через переменные окружения для развертываний с одной учетной записью, где секреты поступают из окружения хоста:

bashCopy code
[code]
    export TWILIO_ACCOUNT_SID="ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"export TWILIO_AUTH_TOKEN="<twilio-auth-token>"export TWILIO_PHONE_NUMBER="+15551234567"export SMS_PUBLIC_WEBHOOK_URL="https://gateway.example.com/webhooks/sms"
[/code]

Затем включите канал в конфигурации:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      dmPolicy: "pairing",    },  },}
[/code]

`TWILIO_SMS_FROM` принимается как псевдоним для `TWILIO_PHONE_NUMBER`. Используйте `TWILIO_MESSAGING_SERVICE_SID` вместо отправителя с телефонным номером, когда Twilio должен выбирать отправителя из Messaging Service.

### Токен аутентификации SecretRef

`authToken` может быть SecretRef. Используйте это, когда Gateway должен получать Twilio Auth Token из среды выполнения секретов OpenClaw вместо хранения конфигурации открытым текстом:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: { source: "env", provider: "default", id: "TWILIO_AUTH_TOKEN" },      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Указанная переменная окружения или поставщик секретов должны быть видны среде выполнения Gateway. Перезапустите управляемые процессы Gateway после изменения переменных окружения хоста.

### Частный номер только с allowlist

Используйте `allowlist`, когда только известные телефонные номера должны иметь возможность общаться с агентом:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "allowlist",      allowFrom: ["+15557654321"],    },  },}
[/code]

### Отправитель Messaging Service

Используйте `messagingServiceSid` вместо `fromNumber`, когда Twilio должен выбирать отправителя через Messaging Service:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      messagingServiceSid: "MGxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",      dmPolicy: "pairing",    },  },}
[/code]

Если после разрешения конфигурации и переменных окружения присутствуют и `fromNumber`, и `messagingServiceSid`, используется `fromNumber`.

### Цель исходящих сообщений по умолчанию

Задайте `defaultTo`, когда автоматизация или доставка, инициированная агентом, должна иметь назначение по умолчанию, если поток отправки не указывает явную цель:

json5Copy code
[code]
    {  channels: {    sms: {      enabled: true,      accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",      authToken: "twilio-auth-token",      fromNumber: "+15551234567",      defaultTo: "+15557654321",      publicWebhookUrl: "https://gateway.example.com/webhooks/sms",    },  },}
[/code]

## Контроль доступа

`channels.sms.dmPolicy` управляет прямым SMS-доступом:

  * `pairing` (по умолчанию)
  * `allowlist` (требуется как минимум один отправитель в `allowFrom`)
  * `open` (требуется, чтобы `allowFrom` включал `"*"`)
  * `disabled`


Записи `allowFrom` должны быть телефонными номерами в формате E.164, например `+15551234567`. Префиксы `sms:` принимаются и нормализуются. Для частного ассистента предпочитайте `dmPolicy: "allowlist"` с явными телефонными номерами.

## Отправка SMS

Цели исходящих SMS используют служебный префикс `sms:` при выбранном SMS-канале:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15551234567 --message "hello"
[/code]

Когда выбор канала неявный, `twilio-sms:+15551234567` выбирает этот канал, не перехватывая существующий служебный префикс `sms:`, принадлежащий каналу и используемый iMessage.

bashCopy code
[code]
    openclaw message send --target twilio-sms:+15551234567 --message "hello"
[/code]

CLI требует явный `--target`. `defaultTo` предназначен для автоматизации и путей доставки, инициированных агентом, где цель может быть разрешена из конфигурации канала.

Ответы агента из входящих SMS-разговоров автоматически возвращаются отправителю через настроенного отправителя Twilio.

Вывод SMS — простой текст. OpenClaw удаляет markdown, выравнивает огражденные блоки кода, сохраняет читаемые ссылки и разбивает длинные ответы на части перед отправкой через Twilio.

## Проверка настройки

После запуска Gateway:

  1. Убедитесь, что журнал Gateway показывает маршрут SMS-webhook.
  2. Запустите проверку со стороны Twilio:

bashCopy code
[code]
    openclaw channels capabilities --channel smsopenclaw channels status --channel sms --probe --json
[/code]

  3. Отправьте SMS на номер Twilio со своего телефона.
  4. Выполните `openclaw pairing list sms`.
  5. Одобрите код сопряжения с помощью `openclaw pairing approve sms &lt;CODE&gt;`.
  6. Отправьте еще одно SMS и подтвердите, что агент отвечает.


Для тестирования только исходящей отправки используйте:

bashCopy code
[code]
    openclaw message send --channel sms --target sms:+15557654321 --message "OpenClaw SMS test"
[/code]

### Сквозной тест из macOS iMessage/SMS

На Mac, который может отправлять операторские SMS через Messages, можно использовать `imsg`, чтобы управлять стороной отправителя, не трогая телефон:

bashCopy code
[code]
    imsg send --to "+15551234567" --service sms --text "OpenClaw SMS E2E $(date -u +%Y%m%dT%H%M%SZ)" --jsonopenclaw pairing list smsopenclaw pairing approve sms &lt;CODE&gt;imsg send --to "+15551234567" --service sms --text "reply exactly SMS pong" --json
[/code]

Первое сообщение должно создать запрос на сопряжение. Второе сообщение должно получить ответ агента через Twilio.

## Безопасность webhook

По умолчанию OpenClaw проверяет `X-Twilio-Signature`, используя `publicWebhookUrl` и `authToken`. Держите `publicWebhookUrl` побайтно согласованным с URL, настроенным в Twilio, включая схему, хост, путь и строку запроса.

Только для тестирования локального туннеля можно задать:

json5Copy code
[code]
    {  channels: {    sms: {      dangerouslyDisableSignatureValidation: true,    },  },}
[/code]

Не используйте отключенную проверку подписи на публичном Gateway.

## Конфигурация нескольких учетных записей

Используйте `accounts`, когда вы обслуживаете более одного номера Twilio:

json5Copy code
[code]
    {  channels: {    sms: {      accounts: {        support: {          enabled: true,          accountSid: "ACxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx",          authToken: "twilio-auth-token",          fromNumber: "+15551234567",          publicWebhookUrl: "https://gateway.example.com/webhooks/sms/support",          webhookPath: "/webhooks/sms/support",          dmPolicy: "allowlist",          allowFrom: ["+15557654321"],        },      },    },  },}
[/code]

Каждая учетная запись должна использовать отдельный `webhookPath`.

## Устранение неполадок

### Twilio возвращает 403 или OpenClaw отклоняет webhook

Проверьте, что `publicWebhookUrl` точно совпадает с URL, настроенным в Twilio, включая схему, хост, путь и строку запроса. Twilio подписывает строку публичного URL, поэтому переписывание прокси и альтернативные имена хостов могут нарушить проверку подписи.

### Запрос на сопряжение не появляется

Проверьте URL и метод webhook в **Messaging** для номера Twilio. Он должен указывать на URL SMS-webhook и использовать `POST`. Также убедитесь, что Gateway доступен из публичного интернета или через ваш туннель.

Если журнал сообщений Twilio показывает ошибку `11200`, Twilio принял входящее SMS, но не смог достучаться до вашего webhook. Проверьте:

  * Twilio **Messaging > A message comes in** указывает на `publicWebhookUrl`.
  * Метод — `POST`.
  * Туннель или обратный прокси открывает точный `webhookPath`; для Tailscale Funnel выполните `tailscale funnel status` и убедитесь, что `/webhooks/sms` есть в списке.
  * `publicWebhookUrl` использует те же схему, хост, путь и строку запроса, которые отправляет Twilio, чтобы проверка подписи могла воспроизвести подписанный URL.


### Исходящие отправки не проходят

Убедитесь, что `accountSid`, `authToken` и либо `fromNumber`, либо `messagingServiceSid` разрешаются. Если вы используете пробную учетную запись Twilio, номер назначения может потребоваться подтвердить в Twilio перед отправкой исходящих SMS.

### Сообщения приходят, но агент не отвечает

Проверьте `dmPolicy` и `allowFrom`. При политике `pairing` по умолчанию отправитель должен быть одобрен, прежде чем будут обрабатываться обычные ходы агента.

Was this useful?YesNo

Open issue