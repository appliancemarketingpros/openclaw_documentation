---
title: Правила отправки матрицы для тихих предварительных просмотров
source_url: https://docs.openclaw.ai/ru/channels/matrix-push-rules
scraped_at: 2026-06-29
---

ChannelsMainstream messaging

Когда `channels.matrix.streaming` имеет значение `"quiet"`, OpenClaw редактирует одно событие предпросмотра на месте и помечает финальную правку пользовательским флагом содержимого. Клиенты Matrix уведомляют о финальной правке только если push-правило конкретного пользователя совпадает с этим флагом. Эта страница предназначена для операторов, которые самостоятельно размещают Matrix и хотят установить это правило для каждой учетной записи получателя.

Если вам нужно только стандартное поведение уведомлений Matrix, используйте `streaming: "partial"` или оставьте потоковую передачу выключенной. См. [настройку канала Matrix](</ru/channels/matrix#streaming-previews>).

## Предварительные требования

  * пользователь-получатель = человек, который должен получить уведомление
  * пользователь-бот = учетная запись Matrix OpenClaw, которая отправляет ответ
  * используйте токен доступа пользователя-получателя для API-вызовов ниже
  * сопоставляйте `sender` в push-правиле с полным MXID пользователя-бота
  * у учетной записи получателя уже должны работать pushers — правила тихого предпросмотра работают только когда обычная доставка push-уведомлений Matrix исправна


## Шаги

* ### Configure quiet previews

json5Copy code
[code]
    {channels: {matrix: {  streaming: "quiet",},},}
[/code]

* ### Get the recipient's access token

По возможности повторно используйте токен существующего клиентского сеанса. Чтобы выпустить новый:

bashCopy code
[code]
    curl -sS -X POST \"https://matrix.example.org/_matrix/client/v3/login" \-H "Content-Type: application/json" \--data '{"type": "m.login.password","identifier": { "type": "m.id.user", "user": "@alice:example.org" },"password": "REDACTED"}'
[/code]

* ### Verify pushers exist

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushers"
[/code]

Если pushers не возвращаются, сначала исправьте обычную доставку push-уведомлений Matrix для этой учетной записи.

* ### Install the override push rule

OpenClaw помечает финальные текстовые правки предпросмотра с помощью `content["com.openclaw.finalized_preview"] = true`. Установите правило, которое совпадает с этим маркером и с MXID бота как отправителем:

bashCopy code
[code]
    curl -sS -X PUT \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname" \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \-H "Content-Type: application/json" \--data '{"conditions": [  { "kind": "event_match", "key": "type", "pattern": "m.room.message" },  {    "kind": "event_property_is",    "key": "content.m\\.relates_to.rel_type",    "value": "m.replace"  },  {    "kind": "event_property_is",    "key": "content.com\\.openclaw\\.finalized_preview",    "value": true  },  { "kind": "event_match", "key": "sender", "pattern": "@bot:example.org" }],"actions": [  "notify",  { "set_tweak": "sound", "value": "default" },  { "set_tweak": "highlight", "value": false }]}'
[/code]

Замените перед запуском:

  * `https://matrix.example.org`: базовый URL вашего homeserver
  * `$USER_ACCESS_TOKEN`: токен доступа пользователя-получателя
  * `openclaw-finalized-preview-botname`: ID правила, уникальный для каждого бота и получателя (шаблон: `openclaw-finalized-preview-<botname>`)
  * `@bot:example.org`: MXID вашего бота OpenClaw, а не получателя


* ### Verify

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname"
[/code]

Затем протестируйте потоковый ответ. В тихом режиме комната показывает тихий черновой предпросмотр и отправляет уведомление один раз, когда блок или ход завершается.

Чтобы позже удалить правило, выполните `DELETE` для того же URL правила с токеном получателя.

## Примечания для нескольких ботов

Push-правила индексируются по `ruleId`: повторный запуск `PUT` для того же ID обновляет одно правило. Если несколько ботов OpenClaw уведомляют одного и того же получателя, создайте по одному правилу для каждого бота с отдельным совпадением отправителя.

Новые пользовательские правила `override` вставляются перед стандартными правилами подавления, поэтому дополнительный параметр порядка не нужен. Правило влияет только на текстовые правки предпросмотра, которые можно финализировать на месте; резервные варианты для медиа и устаревших предпросмотров используют обычную доставку Matrix.

## Примечания homeserver

Synapse

Специальное изменение `homeserver.yaml` не требуется. Если обычные уведомления Matrix уже доходят до этого пользователя, основной шаг настройки — токен получателя и вызов `pushrules` выше.

Если Synapse работает за обратным прокси или workers, убедитесь, что `/_matrix/client/.../pushrules/` корректно достигает Synapse. Доставку push-уведомлений обрабатывает основной процесс или `synapse.app.pusher` / настроенные pusher workers — убедитесь, что они исправны.

Правило использует условие push-правила `event_property_is` (MSC3758, push rule v1.10), которое было добавлено в Synapse в 2023 году. Более старые выпуски Synapse принимают вызов `PUT pushrules/...`, но молча никогда не сопоставляют условие — обновите Synapse, если уведомление не приходит при финальной правке предпросмотра.

Tuwunel

Процесс такой же, как для Synapse; для маркера финального предпросмотра не нужна конфигурация, специфичная для Tuwunel.

Если уведомления исчезают, пока пользователь активен на другом устройстве, проверьте, включен ли `suppress_push_when_active`. Tuwunel добавил этот параметр в 1.4.2 (сентябрь 2025 года), и он может намеренно подавлять push-уведомления на другие устройства, пока одно устройство активно.

## Связанные материалы

  * [Настройка канала Matrix](</ru/channels/matrix>)
  * [Концепции потоковой передачи](</ru/concepts/streaming>)


Was this useful?YesNo

Open issue