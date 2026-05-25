---
title: Прапорці діагностики
source_url: https://docs.openclaw.ai/uk/diagnostics/flags
scraped_at: 2026-05-25
---

Прапорці діагностики дають змогу вмикати цільові журнали налагодження без увімкнення докладного журналювання всюди. Прапорці вмикаються явно й не мають ефекту, якщо підсистема їх не перевіряє.

## Як це працює

  * Прапорці — це рядки (без урахування регістру).
  * Ви можете ввімкнути прапорці в конфігурації або через перевизначення env.
  * Підтримуються шаблони: 
    * `telegram.*` відповідає `telegram.http`
    * `*` вмикає всі прапорці


## Увімкнення через конфігурацію

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

Кілька прапорців:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

Перезапустіть gateway після зміни прапорців.

## Перевизначення env (одноразове)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

Вимкнути всі прапорці:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## Артефакти часової шкали

Прапорець `timeline` записує структуровані події часу запуску й виконання для зовнішніх QA-стендів:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

Ви також можете ввімкнути його в конфігурації:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

Шлях до файлу часової шкали все одно береться з `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH`. Коли `timeline` увімкнено лише з конфігурації, найраніші проміжки завантаження конфігурації не виводяться, тому що OpenClaw ще не прочитав конфігурацію; наступні проміжки запуску використовують прапорець із конфігурації.

`OPENCLAW_DIAGNOSTICS=1`, `OPENCLAW_DIAGNOSTICS=all` і `OPENCLAW_DIAGNOSTICS=*` також вмикають часову шкалу, оскільки вони вмикають кожен прапорець діагностики. Використовуйте `timeline`, коли вам потрібен лише JSONL-артефакт часових вимірювань.

Записи часової шкали використовують оболонку `openclaw.diagnostics.v1`. Події можуть містити ідентифікатори процесів, назви фаз, назви проміжків, тривалості, ідентифікатори plugin, кількість залежностей, зразки затримки циклу подій, назви операцій провайдера, стан завершення дочірнього процесу, а також назви/повідомлення помилок запуску. Розглядайте файли часової шкали як локальні діагностичні артефакти; переглядайте їх перед поширенням за межами вашого комп’ютера.

## Куди потрапляють журнали

Прапорці виводять журнали у стандартний файл журналу діагностики. За замовчуванням:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

Якщо ви встановили `logging.file`, використовуйте цей шлях натомість. Журнали мають формат JSONL (один JSON-об’єкт на рядок). Редагування чутливих даних усе ще застосовується на основі `logging.redactSensitive`.

## Витягування журналів

Виберіть найновіший файл журналу:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

Фільтр для діагностики Telegram HTTP:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

Фільтр для діагностики Brave Search HTTP:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

Або переглядайте хвіст під час відтворення:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

Для віддалених gateway також можна використовувати `openclaw logs --follow` (див. [/cli/logs](</uk/cli/logs>)).

## Примітки

  * Якщо `logging.level` встановлено вище за `warn`, ці журнали можуть бути приглушені. Значення `info` за замовчуванням підходить.
  * `brave.http` журналює URL-адреси/параметри запиту Brave Search, статус/час відповіді та події влучання/промаху/запису кешу. Він не журналює API-ключі або тіла відповідей, але пошукові запити можуть бути чутливими.
  * Прапорці безпечно залишати ввімкненими; вони впливають лише на обсяг журналів для конкретної підсистеми.
  * Використовуйте [/logging](</uk/logging>), щоб змінити призначення журналів, рівні та редагування чутливих даних.


## Пов’язане

  * [Діагностика Gateway](</uk/gateway/diagnostics>)
  * [Усунення несправностей Gateway](</uk/gateway/troubleshooting>)


Was this useful?YesNo