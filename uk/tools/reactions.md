---
title: Реакції
source_url: https://docs.openclaw.ai/uk/tools/reactions
scraped_at: 2026-05-25
---

Агент може додавати й видаляти реакції емодзі на повідомленнях за допомогою інструмента `message` з дією `react`. Поведінка реакцій залежить від каналу й транспорту.

## Як це працює

jsonCopy code
[code]
    {  "action": "react",  "messageId": "msg-123",  "emoji": "thumbsup"}
[/code]

  * `emoji` обов’язковий під час додавання реакції.
  * Установіть `emoji` як порожній рядок (`""`), щоб видалити реакцію(ї) бота.
  * Установіть `remove: true`, щоб видалити певний емодзі (потрібен непорожній `emoji`).
  * У каналах, які підтримують статусні реакції, `trackToolCalls: true` на реакції дає середовищу виконання змогу використовувати це повідомлення з реакцією для подальших реакцій прогресу інструментів протягом того самого ходу.


## Поведінка каналів

Discord and Slack

  * Порожній `emoji` видаляє всі реакції бота на повідомленні.
  * `remove: true` видаляє лише вказаний емодзі.

Google Chat

  * Порожній `emoji` видаляє реакції застосунку на повідомленні.
  * `remove: true` видаляє лише вказаний емодзі.

Telegram

  * Порожній `emoji` видаляє реакції бота.
  * `remove: true` також видаляє реакції, але все одно потребує непорожнього `emoji` для перевірки інструмента.

WhatsApp

  * Порожній `emoji` видаляє реакцію бота.
  * `remove: true` внутрішньо зіставляється з порожнім емодзі (але все одно потребує `emoji` у виклику інструмента).

Zalo Personal (zalouser)

  * Потребує непорожнього `emoji`.
  * `remove: true` видаляє реакцію з цим конкретним емодзі.

Feishu/Lark

  * Використовуйте інструмент `feishu_reaction` з діями `add`, `remove` і `list`.
  * Для додавання/видалення потрібен `emoji_type`; для видалення також потрібен `reaction_id`.

Signal

  * Сповіщення про вхідні реакції контролюються параметром `channels.signal.reactionNotifications`: `"off"` вимикає їх, `"own"` (за замовчуванням) генерує події, коли користувачі реагують на повідомлення бота, а `"all"` генерує події для всіх реакцій.

iMessage

  * Вихідні реакції є tapback-реакціями iMessage (`love`, `like`, `dislike`, `laugh`, `emphasize` і `question`).
  * Сповіщення про вхідні tapback-реакції контролюються параметром `channels.imessage.reactionNotifications`: `"off"` вимикає їх, `"own"` (за замовчуванням) генерує події, коли користувачі реагують на повідомлення, створені ботом, а `"all"` генерує події для всіх tapback-реакцій від авторизованих відправників.


## Рівень реакцій

Конфігурація `reactionLevel` для кожного каналу контролює, наскільки широко агент використовує реакції. Значення зазвичай такі: `off`, `ack`, `minimal` або `extensive`.

  * [Telegram reactionLevel](</uk/channels/telegram#reaction-notifications>) — `channels.telegram.reactionLevel`
  * [WhatsApp reactionLevel](</uk/channels/whatsapp#reaction-level>) — `channels.whatsapp.reactionLevel`


Установіть `reactionLevel` для окремих каналів, щоб налаштувати, наскільки активно агент реагує на повідомлення на кожній платформі.

## Пов’язане

  * [Agent Send](</uk/tools/agent-send>) — інструмент `message`, який містить `react`
  * [Канали](</uk/channels>) — конфігурація для окремих каналів


Was this useful?YesNo