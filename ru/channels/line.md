---
title: LINE
source_url: https://docs.openclaw.ai/ru/channels/line
scraped_at: 2026-06-29
---

ChannelsRegional platforms

LINE подключается к OpenClaw через LINE Messaging API. Plugin работает как приемник webhook на gateway и использует ваш channel access token + channel secret для аутентификации.

Статус: загружаемый Plugin. Поддерживаются личные сообщения, групповые чаты, медиа, местоположения, Flex messages, template messages и быстрые ответы. Реакции и треды не поддерживаются.

## Установка

Установите LINE перед настройкой канала:

bashCopy code
[code]
    openclaw plugins install @openclaw/line
[/code]

Локальная рабочая копия (при запуске из git-репозитория):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/line-plugin
[/code]

## Настройка

  1. Создайте аккаунт LINE Developers и откройте Console: <https://developers.line.biz/console/>
  2. Создайте (или выберите) Provider и добавьте канал **Messaging API**.
  3. Скопируйте **Channel access token** и **Channel secret** из настроек канала.
  4. Включите **Use webhook** в настройках Messaging API.
  5. Задайте URL webhook для вашей конечной точки gateway (требуется HTTPS):

CodeCopy code
[code]
    https://gateway-host/line/webhook
[/code]

Gateway отвечает на проверку webhook от LINE (GET) и подтверждает подписанные входящие события (POST) сразу после проверки подписи и полезной нагрузки; обработка агентом продолжается асинхронно. Если нужен пользовательский путь, задайте `channels.line.webhookPath` или `channels.line.accounts.<id>.webhookPath` и соответственно обновите URL.

Примечание по безопасности:

  * Проверка подписи LINE зависит от тела запроса (HMAC по необработанному телу), поэтому OpenClaw применяет строгие ограничения размера тела и тайм-аут до аутентификации перед проверкой.
  * OpenClaw обрабатывает события webhook из проверенных необработанных байтов запроса. Значения `req.body`, преобразованные промежуточным ПО выше по цепочке, игнорируются для сохранения целостности подписи.


## Конфигурация

Минимальная конфигурация:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "pairing",    },  },}
[/code]

Конфигурация открытых личных сообщений:

json5Copy code
[code]
    {  channels: {    line: {      enabled: true,      channelAccessToken: "LINE_CHANNEL_ACCESS_TOKEN",      channelSecret: "LINE_CHANNEL_SECRET",      dmPolicy: "open",      allowFrom: ["*"],    },  },}
[/code]

Переменные окружения (только аккаунт по умолчанию):

  * `LINE_CHANNEL_ACCESS_TOKEN`
  * `LINE_CHANNEL_SECRET`


Файлы токена/секрета:

json5Copy code
[code]
    {  channels: {    line: {      tokenFile: "/path/to/line-token.txt",      secretFile: "/path/to/line-secret.txt",    },  },}
[/code]

`tokenFile` и `secretFile` должны указывать на обычные файлы. Символические ссылки отклоняются.

Несколько аккаунтов:

json5Copy code
[code]
    {  channels: {    line: {      accounts: {        marketing: {          channelAccessToken: "...",          channelSecret: "...",          webhookPath: "/line/marketing",        },      },    },  },}
[/code]

## Управление доступом

Личные сообщения по умолчанию требуют сопряжения. Неизвестные отправители получают код сопряжения, а их сообщения игнорируются до одобрения.

bashCopy code
[code]
    openclaw pairing list lineopenclaw pairing approve line &lt;CODE&gt;
[/code]

Списки разрешений и политики:

  * `channels.line.dmPolicy`: `pairing | allowlist | open | disabled`
  * `channels.line.allowFrom`: разрешенные ID пользователей LINE для личных сообщений; `dmPolicy: "open"` требует `["*"]`
  * `channels.line.groupPolicy`: `allowlist | open | disabled`
  * `channels.line.groupAllowFrom`: разрешенные ID пользователей LINE для групп
  * Переопределения для отдельных групп: `channels.line.groups.<groupId>.allowFrom`
  * Статические группы доступа отправителей можно ссылочно указывать из `allowFrom`, `groupAllowFrom` и группового `allowFrom` через `accessGroup:<name>`.
  * Примечание о runtime: если `channels.line` полностью отсутствует, runtime возвращается к `groupPolicy="allowlist"` для проверок групп (даже если задано `channels.defaults.groupPolicy`).


ID LINE чувствительны к регистру. Допустимые ID выглядят так:

  * Пользователь: `U` \+ 32 шестнадцатеричных символа
  * Группа: `C` \+ 32 шестнадцатеричных символа
  * Комната: `R` \+ 32 шестнадцатеричных символа


## Поведение сообщений

  * Текст разбивается на фрагменты по 5000 символов.
  * Форматирование Markdown удаляется; блоки кода и таблицы по возможности преобразуются в Flex cards.
  * Потоковые ответы буферизуются; LINE получает полные фрагменты с анимацией загрузки, пока агент работает.
  * Скачивание медиа ограничено `channels.line.mediaMaxMb` (по умолчанию 10).
  * Входящие медиа сохраняются в `~/.openclaw/media/inbound/` перед передачей агенту, что соответствует общему хранилищу медиа, используемому другими встроенными Plugin каналов.


## Данные канала (расширенные сообщения)

Используйте `channelData.line` для отправки быстрых ответов, местоположений, Flex cards или template messages.

json5Copy code
[code]
    {  text: "Here you go",  channelData: {    line: {      quickReplies: ["Status", "Help"],      location: {        title: "Office",        address: "123 Main St",        latitude: 35.681236,        longitude: 139.767125,      },      flexMessage: {        altText: "Status card",        contents: {          /* Flex payload */        },      },      templateMessage: {        type: "confirm",        text: "Proceed?",        confirmLabel: "Yes",        confirmData: "yes",        cancelLabel: "No",        cancelData: "no",      },    },  },}
[/code]

Plugin LINE также поставляется с командой `/card` для пресетов Flex messages:

CodeCopy code
[code]
    /card info "Welcome" "Thanks for joining!"
[/code]

## Поддержка ACP

LINE поддерживает привязки бесед ACP (Agent Communication Protocol):

  * `/acp spawn <agent> --bind here` привязывает текущий чат LINE к сессии ACP без создания дочернего треда.
  * Настроенные привязки ACP и активные сессии ACP, привязанные к беседе, работают в LINE так же, как и в других каналах бесед.


См. [агенты ACP](</ru/tools/acp-agents>) для подробностей.

## Исходящие медиа

Plugin LINE поддерживает отправку изображений, видео и аудиофайлов через инструмент сообщений агента. Медиа отправляется через специфичный для LINE путь доставки с соответствующей обработкой предпросмотра и отслеживания:

  * **Изображения** : отправляются как сообщения с изображениями LINE с автоматической генерацией предпросмотра.
  * **Видео** : отправляются с явной обработкой предпросмотра и типа содержимого.
  * **Аудио** : отправляется как аудиосообщения LINE.


URL исходящих медиа должны быть публичными HTTPS URL. OpenClaw проверяет целевое имя хоста перед передачей URL в LINE и отклоняет local loopback, link-local и цели в частных сетях.

Общие отправки медиа возвращаются к существующему маршруту только для изображений, когда специфичный для LINE путь недоступен.

## Устранение неполадок

  * **Проверка webhook не проходит:** убедитесь, что URL webhook использует HTTPS и `channelSecret` совпадает с LINE console.
  * **Нет входящих событий:** подтвердите, что путь webhook совпадает с `channels.line.webhookPath` и что gateway доступен из LINE.
  * **Ошибки скачивания медиа:** увеличьте `channels.line.mediaMaxMb`, если медиа превышает лимит по умолчанию.


## См. также

  * [Обзор каналов](</ru/channels>) — все поддерживаемые каналы
  * [Сопряжение](</ru/channels/pairing>) — аутентификация личных сообщений и поток сопряжения
  * [Группы](</ru/channels/groups>) — поведение групповых чатов и ограничение по упоминаниям
  * [Маршрутизация каналов](</ru/channels/channel-routing>) — маршрутизация сессий для сообщений
  * [Безопасность](</ru/gateway/security>) — модель доступа и усиление защиты


Was this useful?YesNo

Open issue