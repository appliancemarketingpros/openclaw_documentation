---
title: Правила надсилання Matrix для тихих попередніх переглядів
source_url: https://docs.openclaw.ai/uk/channels/matrix-push-rules
scraped_at: 2026-05-25
---

Коли `channels.matrix.streaming` має значення `"quiet"`, OpenClaw редагує одну подію попереднього перегляду на місці та позначає завершене редагування спеціальним прапорцем у вмісті. Клієнти Matrix надсилають сповіщення про фінальне редагування, лише якщо правило надсилання для конкретного користувача відповідає цьому прапорцю. Ця сторінка призначена для операторів, які самостійно розміщують Matrix і хочуть встановити це правило для кожного облікового запису одержувача.

Якщо вам потрібна лише стандартна поведінка сповіщень Matrix, використовуйте `streaming: "partial"` або залиште потокову передачу вимкненою. Див. [Налаштування каналу Matrix](</uk/channels/matrix#streaming-previews>).

## Передумови

  * користувач-одержувач = людина, яка має отримувати сповіщення
  * користувач бота = обліковий запис Matrix OpenClaw, який надсилає відповідь
  * для наведених нижче викликів API використовуйте токен доступу користувача-одержувача
  * зіставляйте `sender` у правилі надсилання з повним MXID користувача бота
  * обліковий запис одержувача вже повинен мати налаштовані й працездатні pushers — правила тихого попереднього перегляду працюють лише тоді, коли звичайна доставка push-сповіщень Matrix справна


## Кроки

* ### Налаштуйте тихі попередні перегляди

json5Copy code
[code]
    {channels: {matrix: {  streaming: "quiet",},},}
[/code]

* ### Отримайте токен доступу одержувача

За можливості повторно використайте токен наявної сесії клієнта. Щоб створити новий:

bashCopy code
[code]
    curl -sS -X POST \"https://matrix.example.org/_matrix/client/v3/login" \-H "Content-Type: application/json" \--data '{"type": "m.login.password","identifier": { "type": "m.id.user", "user": "@alice:example.org" },"password": "REDACTED"}'
[/code]

* ### Переконайтеся, що pushers існують

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushers"
[/code]

Якщо pushers не повертаються, спочатку виправте звичайну доставку push-сповіщень Matrix для цього облікового запису, а вже потім продовжуйте.

* ### Встановіть override-правило надсилання

OpenClaw позначає завершені редагування текстових попередніх переглядів за допомогою `content["com.openclaw.finalized_preview"] = true`. Встановіть правило, яке зіставляє цей маркер і MXID бота як відправника:

bashCopy code
[code]
    curl -sS -X PUT \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname" \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \-H "Content-Type: application/json" \--data '{"conditions": [  { "kind": "event_match", "key": "type", "pattern": "m.room.message" },  {    "kind": "event_property_is",    "key": "content.m\\.relates_to.rel_type",    "value": "m.replace"  },  {    "kind": "event_property_is",    "key": "content.com\\.openclaw\\.finalized_preview",    "value": true  },  { "kind": "event_match", "key": "sender", "pattern": "@bot:example.org" }],"actions": [  "notify",  { "set_tweak": "sound", "value": "default" },  { "set_tweak": "highlight", "value": false }]}'
[/code]

Замініть перед виконанням:

  * `https://matrix.example.org`: базовий URL вашого homeserver
  * `$USER_ACCESS_TOKEN`: токен доступу користувача-одержувача
  * `openclaw-finalized-preview-botname`: ідентифікатор правила, унікальний для кожного бота й одержувача (шаблон: `openclaw-finalized-preview-<botname>`)
  * `@bot:example.org`: MXID вашого бота OpenClaw, а не одержувача


* ### Перевірте

bashCopy code
[code]
    curl -sS \-H "Authorization: Bearer $USER_ACCESS_TOKEN" \"https://matrix.example.org/_matrix/client/v3/pushrules/global/override/openclaw-finalized-preview-botname"
[/code]

Потім протестуйте потокову відповідь. У тихому режимі кімната показує тихий чернетковий попередній перегляд і надсилає одне сповіщення, коли блок або хід завершується.

Щоб пізніше видалити правило, виконайте `DELETE` для того самого URL правила з токеном одержувача.

## Примітки щодо кількох ботів

Правила надсилання визначаються ключем `ruleId`: повторний запуск `PUT` для того самого ідентифікатора оновлює одне правило. Якщо того самого одержувача сповіщають кілька ботів OpenClaw, створіть окреме правило для кожного бота з окремою умовою відповідності відправника.

Нові визначені користувачем `override`-правила вставляються перед стандартними правилами придушення, тому додатковий параметр порядку не потрібен. Правило впливає лише на текстові редагування попереднього перегляду, які можна завершити на місці; резервні варіанти для медіа та застарілих попередніх переглядів використовують звичайну доставку Matrix.

## Примітки щодо homeserver

Synapse

Спеціальні зміни в `homeserver.yaml` не потрібні. Якщо звичайні сповіщення Matrix вже доходять до цього користувача, основним кроком налаштування є токен одержувача та виклик `pushrules`, наведений вище.

Якщо ви запускаєте Synapse за зворотним проксі або через workers, переконайтеся, що `/_matrix/client/.../pushrules/` коректно спрямовується до Synapse. Доставка push-сповіщень обробляється основним процесом або `synapse.app.pusher` / налаштованими pusher workers — переконайтеся, що вони працюють справно.

Правило використовує умову правила надсилання `event_property_is` (MSC3758, push rule v1.10), яку було додано до Synapse у 2023 році. Старіші випуски Synapse приймають виклик `PUT pushrules/...`, але мовчки ніколи не зіставляють цю умову — оновіть Synapse, якщо сповіщення не надходить після завершеного редагування попереднього перегляду.

Tuwunel

Той самий процес, що й для Synapse; спеціальна конфігурація Tuwunel для маркера завершеного попереднього перегляду не потрібна.

Якщо сповіщення зникають, поки користувач активний на іншому пристрої, перевірте, чи ввімкнено `suppress_push_when_active`. Tuwunel додав цю опцію у версії 1.4.2 (вересень 2025 року), і вона може навмисно приглушувати push-сповіщення на інших пристроях, поки один пристрій активний.

## Пов’язане

  * [Налаштування каналу Matrix](</uk/channels/matrix>)
  * [Концепції потокової передачі](</uk/concepts/streaming>)


Was this useful?YesNo