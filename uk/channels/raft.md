---
title: Raft
source_url: https://docs.openclaw.ai/uk/channels/raft
scraped_at: 2026-06-29
---

ChannelsDeveloper and self-hosted

Підтримка Raft підключає агента OpenClaw до зовнішнього агента Raft через локальний Raft CLI. Raft надсилає автентифіковані підказки пробудження до Gateway. Потім агент використовує Raft CLI, щоб перевіряти й надсилати повідомлення.

## Установлення

Raft є офіційним зовнішнім Plugin. Установіть його на хості Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/raftopenclaw gateway restart
[/code]

Докладніше: [Plugins](</uk/tools/plugin>)

## Передумови

  * Робочий простір Raft із зовнішнім агентом.
  * Raft CLI, установлений на тому самому хості, що й OpenClaw Gateway.
  * Профіль Raft CLI, у який уже виконано вхід і який пов’язаний із цим зовнішнім агентом.


Plugin не зберігає облікові дані Raft. Raft CLI зберігає цю автентифікацію у власному профілі.

## Налаштування

Задайте профіль у конфігурації:

json5Copy code
[code]
    {  channels: {    raft: {      enabled: true,      profile: "openclaw",    },  },}
[/code]

Для стандартного облікового запису натомість можна задати `RAFT_PROFILE` у середовищі Gateway:

bashCopy code
[code]
    RAFT_PROFILE=openclaw
[/code]

Використовуйте іменований обліковий запис, коли один Gateway підключається до більш ніж одного зовнішнього агента Raft:

json5Copy code
[code]
    {  channels: {    raft: {      accounts: {        support: {          profile: "support-agent",        },        engineering: {          profile: "engineering-agent",        },      },    },  },}
[/code]

Інтерактивний процес налаштування записує той самий профіль:

bashCopy code
[code]
    openclaw channels setup raft
[/code]

## Як це працює

Коли Gateway запускається, Plugin:

  1. Відкриває HTTP-кінцеву точку пробудження лише для loopback на ефемерному порту.
  2. Запускає `raft --profile <profile> agent bridge` із цією кінцевою точкою та токеном для кожного процесу.
  3. Приймає лише автентифіковані підказки пробудження без вмісту з ідентифікатором повторного відтворення від локального bridge.
  4. Вимагає один із `eventId`, `attemptId`, `messageId`, `delivery_id`, `wake_id` або `id`.
  5. Дедуплікує нещодавні повторні доставки пробудження за ідентифікатором події bridge, зокрема після перезапусків Gateway.
  6. Повертає стабільну runtime-сесію для поточного bridge і порожній пакет спорожнення активності для протоколу Raft CLI.
  7. Запускає один серіалізований хід агента OpenClaw для кожного прийнятого пробудження.


Bridge відповідає за повторні спроби доставлення Raft і повторні підключення. Хід OpenClaw отримує лише сповіщення про пробудження, а не скопійований вміст повідомлення Raft. Він використовує CLI, щоб читати очікувані повідомлення й надсилати свою відповідь:

bashCopy code
[code]
    raft --profile openclaw message checkraft --profile openclaw message send
[/code]

## Перевірка

Перевірте, що OpenClaw може знайти CLI і має налаштований профіль:

bashCopy code
[code]
    openclaw channels status --probeopenclaw plugins inspect raft --runtime --json
[/code]

Потім надішліть повідомлення зовнішньому агенту Raft. У журналі Gateway має бути видно запуск Raft bridge, а потім вхідне пробудження. Агент має використати налаштований профіль Raft, щоб перевірити свої очікувані повідомлення.

## Усунення несправностей

Raft CLI відсутній

Установіть Raft CLI на хості Gateway і зробіть `raft` доступним у `PATH` служби. Перевірте це за допомогою `raft --help`, а потім перезапустіть Gateway.

Bridge завершується негайно

Перевірте, що в налаштований профіль виконано вхід і що він належить потрібному зовнішньому агенту Raft. Запустіть `raft --profile <profile> agent bridge` напряму, щоб побачити діагностику CLI.

Пробудження надходить, але відповідь Raft не надсилається

Це очікувано, якщо агент не викликає Raft CLI. Bridge пробудження не передає тіла повідомлень або автоматичні фінальні відповіді. Перевірте політику інструментів агента й переконайтеся, що він може виконувати `raft --profile <profile> message check` і `message send`.

## Посилання

  * [Raft](<https://raft.build/>)
  * [Документація Raft](<https://docs.raft.build/welcome/>)
  * [Інтеграція Hermes Raft](<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/raft>)


Was this useful?YesNo

Open issue