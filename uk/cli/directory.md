---
title: Каталог
source_url: https://docs.openclaw.ai/uk/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

Пошук у каталозі для каналів, які його підтримують (контакти/пири, групи та "me").

## Спільні прапорці

  * `--channel <name>`: id/псевдонім каналу (обов’язково, коли налаштовано кілька каналів; автоматично, коли налаштовано лише один)
  * `--account <id>`: id облікового запису (типово: типовий для каналу)
  * `--json`: вивести JSON


## Примітки

  * `directory` призначено, щоб допомогти вам знайти ID, які можна вставити в інші команди (особливо `openclaw message send --target ...`).
  * Для багатьох каналів результати спираються на конфігурацію (списки дозволених / налаштовані групи), а не на живий каталог провайдера.
  * Установлені Plugin каналів усе ще можуть не підтримувати каталог; у такому разі команда повідомляє про непідтримувану операцію каталогу замість перевстановлення Plugin.
  * Типовий вивід — це `id` (і іноді `name`), розділені табуляцією; використовуйте `--json` для сценаріїв.


## Використання результатів із `message send`

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## Формати ID (за каналом)

  * WhatsApp: `+15551234567` (DM), `1234567890-1234567890@g.us` (група), `120363123456789@newsletter` (вихідна ціль каналу/розсилки)
  * Telegram: `@username` або числовий id чату; групи мають числові id
  * Slack: `user:U…` і `channel:C…`
  * Discord: `user:<id>` і `channel:<id>`
  * Matrix (Plugin): `user:@user:server`, `room:!roomId:server` або `#alias:server`
  * Microsoft Teams (Plugin): `user:<id>` і `conversation:<id>`
  * Zalo (Plugin): id користувача (Bot API)
  * Zalo Personal / `zalouser` (Plugin): id гілки (DM/група) з `zca` (`me`, `friend list`, `group list`)


## Себе ("me")

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## Пири (контакти/користувачі)

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## Групи

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## Пов’язане

  * [Довідник CLI](</uk/cli>)


Was this useful?YesNo