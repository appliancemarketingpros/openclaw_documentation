---
title: Реакции
source_url: https://docs.openclaw.ai/ru/tools/reactions
scraped_at: 2026-06-29
---

CapabilitiesTools

Агент может добавлять и удалять реакции emoji на сообщениях с помощью инструмента `message` с действием `react`. Поведение реакций зависит от канала и транспорта.

## Как это работает

jsonCopy code
[code]
    {  "action": "react",  "messageId": "msg-123",  "emoji": "thumbsup"}
[/code]

  * `emoji` обязателен при добавлении реакции.
  * Задайте для `emoji` пустую строку (`""`), чтобы удалить реакцию(и) бота.
  * Задайте `remove: true`, чтобы удалить конкретный emoji (требуется непустой `emoji`).
  * В каналах, поддерживающих статусные реакции, `trackToolCalls: true` у реакции позволяет среде выполнения использовать это сообщение с реакцией для последующих реакций прогресса инструмента в рамках того же хода.


## Поведение каналов

Discord и Slack

  * Пустой `emoji` удаляет все реакции бота на сообщении.
  * `remove: true` удаляет только указанный emoji.

Google Chat

  * Пустой `emoji` удаляет реакции приложения на сообщении.
  * `remove: true` удаляет только указанный emoji.

Nextcloud Talk

  * Только добавление реакций: `emoji` обязателен и должен быть непустым.
  * Удаление реакций пока не поддерживается; вызовы с `remove: true` (или пустым `emoji`) отклоняются с понятной ошибкой, а не выполняются без видимого эффекта.
  * Требуется, чтобы бот Talk был зарегистрирован с функцией `reaction` (см. [документацию канала Nextcloud Talk](</ru/channels/nextcloud-talk>)).

Telegram

  * Пустой `emoji` удаляет реакции бота.
  * `remove: true` также удаляет реакции, но для проверки инструмента всё равно требуется непустой `emoji`.

WhatsApp

  * Пустой `emoji` удаляет реакцию бота.
  * `remove: true` внутренне сопоставляется с пустым emoji (при этом `emoji` всё равно требуется в вызове инструмента).
  * WhatsApp имеет один слот реакции бота на сообщение; обновления статусных реакций заменяют этот слот, а не накапливают несколько emoji.

Zalo Personal (zalouser)

  * Требуется непустое значение `emoji`.
  * `remove: true` удаляет именно эту реакцию emoji.

Feishu/Lark

  * Используйте инструмент `feishu_reaction` с действиями `add`, `remove` и `list`.
  * Для добавления/удаления требуется `emoji_type`; для удаления также требуется `reaction_id`.

Signal

  * Уведомления о входящих реакциях управляются параметром `channels.signal.reactionNotifications`: `"off"` отключает их, `"own"` (по умолчанию) отправляет события, когда пользователи реагируют на сообщения бота, а `"all"` отправляет события для всех реакций.

iMessage

  * Исходящие реакции — это tapback-реакции iMessage (`love`, `like`, `dislike`, `laugh`, `emphasize` и `question`).
  * Уведомления о входящих tapback-реакциях управляются параметром `channels.imessage.reactionNotifications`: `"off"` отключает их, `"own"` (по умолчанию) отправляет события, когда пользователи реагируют на сообщения, созданные ботом, а `"all"` отправляет события для всех tapback-реакций от авторизованных отправителей.


## Уровень реакций

Конфигурация `reactionLevel` для каждого канала управляет тем, насколько широко агент использует реакции. Значения обычно: `off`, `ack`, `minimal` или `extensive`.

  * [Telegram reactionLevel](</ru/channels/telegram#reaction-notifications>) — `channels.telegram.reactionLevel`
  * [WhatsApp reactionLevel](</ru/channels/whatsapp#reaction-level>) — `channels.whatsapp.reactionLevel`


Задайте `reactionLevel` для отдельных каналов, чтобы настроить, насколько активно агент реагирует на сообщения на каждой платформе.

## Связанные материалы

  * [Agent Send](</ru/tools/agent-send>) — инструмент `message`, который включает `react`
  * [Каналы](</ru/channels>) — конфигурация для отдельных каналов


Was this useful?YesNo

Open issue