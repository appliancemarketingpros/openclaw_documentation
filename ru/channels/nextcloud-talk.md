---
title: Nextcloud Talk
source_url: https://docs.openclaw.ai/ru/channels/nextcloud-talk
scraped_at: 2026-06-29
---

ChannelsDeveloper and self-hosted

Статус: встроенный Plugin (бот Webhook). Поддерживаются личные сообщения, комнаты, реакции и сообщения Markdown.

## Встроенный Plugin

Nextcloud Talk поставляется как встроенный Plugin в текущих релизах OpenClaw, поэтому обычным пакетным сборкам не нужна отдельная установка.

Если вы используете более старую сборку или пользовательскую установку, из которой исключен Nextcloud Talk, установите npm-пакет напрямую:

Установка через CLI (реестр npm):

bashCopy code
[code]
    openclaw plugins install @openclaw/nextcloud-talk
[/code]

Используйте пакет без версии, чтобы следовать текущему официальному тегу релиза. Закрепляйте точную версию только когда нужна воспроизводимая установка.

Локальная рабочая копия (при запуске из git-репозитория):

bashCopy code
[code]
    openclaw plugins install ./path/to/local/nextcloud-talk-plugin
[/code]

Подробнее: [Plugins](</ru/tools/plugin>)

## Быстрая настройка (для начинающих)

  1. Убедитесь, что Plugin Nextcloud Talk доступен.

     * Текущие пакетные релизы OpenClaw уже включают его.
     * В более старые/пользовательские установки его можно добавить вручную командами выше.
  2. На вашем сервере Nextcloud создайте бота:

bashCopy code
[code]./occ talk:bot:install "OpenClaw" "<shared-secret>" "<webhook-url>" --feature webhook --feature response --feature reaction
[/code]

  3. Включите бота в настройках целевой комнаты.

  4. Настройте OpenClaw:

     * Конфигурация: `channels.nextcloud-talk.baseUrl` \+ `channels.nextcloud-talk.botSecret`
     * Или переменная окружения: `NEXTCLOUD_TALK_BOT_SECRET` (только учетная запись по умолчанию)

Настройка через CLI:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --url https://cloud.example.com \  --token "<shared-secret>"
[/code]

Эквивалентные явные поля:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret "<shared-secret>"
[/code]

Секрет из файла:

bashCopy code
[code]openclaw channels add --channel nextcloud-talk \  --base-url https://cloud.example.com \  --secret-file /path/to/nextcloud-talk-secret
[/code]

  5. Перезапустите gateway (или завершите настройку).


Минимальная конфигурация:

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      enabled: true,      baseUrl: "https://cloud.example.com",      botSecret: "shared-secret",      dmPolicy: "pairing",    },  },}
[/code]

## Примечания

  * Боты не могут инициировать личные сообщения. Пользователь должен сначала написать боту.
  * URL Webhook должен быть доступен для Gateway; если используется прокси, задайте `webhookPublicUrl`.
  * Загрузка медиа не поддерживается API бота; медиа отправляются как URL.
  * Полезная нагрузка Webhook не различает личные сообщения и комнаты; задайте `apiUser` \+ `apiPassword`, чтобы включить определение типа комнаты (иначе личные сообщения обрабатываются как комнаты).


## Управление доступом (личные сообщения)

  * По умолчанию: `channels.nextcloud-talk.dmPolicy = "pairing"`. Неизвестные отправители получают код сопряжения.
  * Подтверждение: 
    * `openclaw pairing list nextcloud-talk`
    * `openclaw pairing approve nextcloud-talk &lt;CODE&gt;`
  * Публичные личные сообщения: `channels.nextcloud-talk.dmPolicy="open"` плюс `channels.nextcloud-talk.allowFrom=["*"]`.
  * `allowFrom` сопоставляет только идентификаторы пользователей Nextcloud; отображаемые имена игнорируются.


## Комнаты (группы)

  * По умолчанию: `channels.nextcloud-talk.groupPolicy = "allowlist"` (доступ по упоминанию).
  * Добавьте комнаты в список разрешенных через `channels.nextcloud-talk.rooms`:

json5Copy code
[code]
    {  channels: {    "nextcloud-talk": {      rooms: {        "room-token": { requireMention: true },      },    },  },}
[/code]

  * Чтобы не разрешать ни одну комнату, оставьте список разрешенных пустым или задайте `channels.nextcloud-talk.groupPolicy="disabled"`.


## Возможности

Возможность | Статус  
---|---  
Личные сообщения | Поддерживаются  
Комнаты | Поддерживаются  
Ветки | Не поддерживаются  
Медиа | Только URL  
Реакции | Поддерживаются  
Встроенные команды | Не поддерживаются  
  
## Справочник конфигурации (Nextcloud Talk)

Полная конфигурация: [Configuration](</ru/gateway/configuration>)

Параметры провайдера:

  * `channels.nextcloud-talk.enabled`: включить/отключить запуск канала.
  * `channels.nextcloud-talk.baseUrl`: URL экземпляра Nextcloud.
  * `channels.nextcloud-talk.botSecret`: общий секрет бота.
  * `channels.nextcloud-talk.botSecretFile`: путь к обычному файлу с секретом. Символические ссылки отклоняются.
  * `channels.nextcloud-talk.apiUser`: пользователь API для поиска комнат (определение личных сообщений).
  * `channels.nextcloud-talk.apiPassword`: пароль API/приложения для поиска комнат.
  * `channels.nextcloud-talk.apiPasswordFile`: путь к файлу пароля API.
  * `channels.nextcloud-talk.webhookPort`: порт слушателя Webhook (по умолчанию: 8788).
  * `channels.nextcloud-talk.webhookHost`: хост Webhook (по умолчанию: 0.0.0.0).
  * `channels.nextcloud-talk.webhookPath`: путь Webhook (по умолчанию: /nextcloud-talk-webhook).
  * `channels.nextcloud-talk.webhookPublicUrl`: внешне доступный URL Webhook.
  * `channels.nextcloud-talk.dmPolicy`: `pairing | allowlist | open | disabled`.
  * `channels.nextcloud-talk.allowFrom`: список разрешенных для личных сообщений (идентификаторы пользователей). `open` требует `"*"`.
  * `channels.nextcloud-talk.groupPolicy`: `allowlist | open | disabled`.
  * `channels.nextcloud-talk.groupAllowFrom`: список разрешенных для групп (идентификаторы пользователей).
  * `channels.nextcloud-talk.rooms`: настройки и список разрешенных для отдельных комнат.
  * Статические группы доступа отправителей можно указывать в `allowFrom` и `groupAllowFrom` через `accessGroup:<name>`.
  * `channels.nextcloud-talk.historyLimit`: лимит истории группы (0 отключает).
  * `channels.nextcloud-talk.dmHistoryLimit`: лимит истории личных сообщений (0 отключает).
  * `channels.nextcloud-talk.dms`: переопределения для отдельных личных сообщений (historyLimit).
  * `channels.nextcloud-talk.textChunkLimit`: размер исходящего фрагмента текста (символы).
  * `channels.nextcloud-talk.chunkMode`: `length` (по умолчанию) или `newline` для разделения по пустым строкам (границам абзацев) перед разбиением по длине.
  * `channels.nextcloud-talk.blockStreaming`: отключить потоковую передачу блоков для этого канала.
  * `channels.nextcloud-talk.blockStreamingCoalesce`: настройка объединения потоковой передачи блоков.
  * `channels.nextcloud-talk.mediaMaxMb`: лимит входящих медиа (МБ).


## См. также

  * [Обзор каналов](</ru/channels>) — все поддерживаемые каналы
  * [Сопряжение](</ru/channels/pairing>) — аутентификация личных сообщений и поток сопряжения
  * [Группы](</ru/channels/groups>) — поведение групповых чатов и доступ по упоминанию
  * [Маршрутизация каналов](</ru/channels/channel-routing>) — маршрутизация сессий для сообщений
  * [Безопасность](</ru/gateway/security>) — модель доступа и усиление защиты


Was this useful?YesNo

Open issue