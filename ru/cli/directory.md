---
title: Каталог
source_url: https://docs.openclaw.ai/ru/cli/directory
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw directory`

Поиск в каталогах для каналов, которые это поддерживают (контакты/собеседники, группы и «я»).

## Общие флаги

  * `--channel <name>`: идентификатор/псевдоним канала (обязательно, когда настроено несколько каналов; выбирается автоматически, когда настроен только один)
  * `--account <id>`: идентификатор учетной записи (по умолчанию: канал по умолчанию)
  * `--json`: вывести JSON


## Примечания

  * `directory` предназначен для поиска идентификаторов, которые можно вставлять в другие команды (особенно `openclaw message send --target ...`).
  * Для многих каналов результаты берутся из конфигурации (списки разрешений / настроенные группы), а не из живого каталога провайдера.
  * Установленные Plugin каналов все равно могут не поддерживать каталог; в этом случае команда сообщает о неподдерживаемой операции каталога вместо переустановки Plugin.
  * Вывод по умолчанию: `id` (а иногда `name`), разделенные табуляцией; используйте `--json` для скриптов.


## Использование результатов с `message send`

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## Форматы идентификаторов (по каналам)

  * WhatsApp: `+15551234567` (личное сообщение), `1234567890-1234567890@g.us` (группа), `120363123456789@newsletter` (исходящая цель канала/рассылки)
  * Telegram: `@username` или числовой идентификатор чата; группы используют числовые идентификаторы
  * Slack: `user:U…` и `channel:C…`
  * Discord: `user:<id>` и `channel:<id>`
  * Matrix (Plugin): `user:@user:server`, `room:!roomId:server` или `#alias:server`
  * Microsoft Teams (Plugin): `user:<id>` и `conversation:<id>`
  * Zalo (Plugin): идентификатор пользователя (Bot API)
  * Zalo Personal / `zalouser` (Plugin): идентификатор цепочки (личное сообщение/группа) из `zca` (`me`, `friend list`, `group list`)


## Собственный профиль («я»)

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## Собеседники (контакты/пользователи)

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## Группы

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## См. также

  * [Справочник CLI](</ru/cli>)


Was this useful?YesNo

Open issue