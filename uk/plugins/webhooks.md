---
title: Plugin Webhooks
source_url: https://docs.openclaw.ai/uk/plugins/webhooks
scraped_at: 2026-05-25
---

Plugin Webhooks додає автентифіковані HTTP-маршрути, які прив’язують зовнішню автоматизацію до OpenClaw TaskFlows.

Використовуйте його, коли потрібно, щоб довірена система, як-от Zapier, n8n, CI-завдання або внутрішній сервіс, створювала й керувала керованими TaskFlows без попереднього написання власного plugin.

## Де він виконується

Plugin Webhooks виконується всередині процесу Gateway.

Якщо ваш Gateway працює на іншому комп’ютері, встановіть і налаштуйте plugin на цьому хості Gateway, а потім перезапустіть Gateway.

## Налаштування маршрутів

Задайте конфігурацію в `plugins.entries.webhooks.config`:

json5Copy code
[code]
    {  plugins: {    entries: {      webhooks: {        enabled: true,        config: {          routes: {            zapier: {              path: "/plugins/webhooks/zapier",              sessionKey: "agent:main:main",              secret: {                source: "env",                provider: "default",                id: "OPENCLAW_WEBHOOK_SECRET",              },              controllerId: "webhooks/zapier",              description: "Zapier TaskFlow bridge",            },          },        },      },    },  },}
[/code]

Поля маршруту:

  * `enabled`: необов’язкове, стандартне значення — `true`
  * `path`: необов’язкове, стандартне значення — `/plugins/webhooks/<routeId>`
  * `sessionKey`: обов’язкова сесія, якій належать прив’язані TaskFlows
  * `secret`: обов’язковий спільний секрет або SecretRef
  * `controllerId`: необов’язковий ідентифікатор контролера для створених керованих потоків
  * `description`: необов’язкова примітка оператора


Підтримувані вхідні значення `secret`:

  * Звичайний рядок
  * SecretRef із `source: "env" | "file" | "exec"`


Якщо маршрут із секретом не може визначити свій секрет під час запуску, plugin пропускає цей маршрут і записує попередження в журнал, замість того щоб відкривати несправну кінцеву точку.

## Модель безпеки

Кожен маршрут є довіреним і діє з повноваженнями TaskFlow, визначеними його налаштованим `sessionKey`.

Це означає, що маршрут може переглядати й змінювати TaskFlows, які належать цій сесії, тому вам слід:

  * Використовувати надійний унікальний секрет для кожного маршруту
  * Надавати перевагу посиланням на секрети замість вбудованих відкритих секретів
  * Прив’язувати маршрути до найвужчої сесії, яка підходить для робочого процесу
  * Відкривати лише конкретний шлях Webhook, який вам потрібен


Plugin застосовує:

  * Автентифікацію за спільним секретом
  * Обмеження розміру тіла запиту й часу очікування
  * Обмеження частоти у фіксованому вікні
  * Обмеження паралельних запитів у виконанні
  * Доступ до TaskFlow, прив’язаний до власника, через `api.runtime.tasks.managedFlows.bindSession(...)`


## Формат запиту

Надсилайте запити `POST` із:

  * `Content-Type: application/json`
  * `Authorization: Bearer <secret>` або `x-openclaw-webhook-secret: <secret>`


Приклад:

bashCopy code
[code]
    curl -X POST https://gateway.example.com/plugins/webhooks/zapier \  -H 'Content-Type: application/json' \  -H 'Authorization: Bearer YOUR_SHARED_SECRET' \  -d '{"action":"create_flow","goal":"Review inbound queue"}'
[/code]

## Підтримувані дії

Plugin наразі приймає такі JSON-значення `action`:

  * `create_flow`
  * `get_flow`
  * `list_flows`
  * `find_latest_flow`
  * `resolve_flow`
  * `get_task_summary`
  * `set_waiting`
  * `resume_flow`
  * `finish_flow`
  * `fail_flow`
  * `request_cancel`
  * `cancel_flow`
  * `run_task`


### `create_flow`

Створює керований TaskFlow для прив’язаної до маршруту сесії.

Приклад:

jsonCopy code
[code]
    {  "action": "create_flow",  "goal": "Review inbound queue",  "status": "queued",  "notifyPolicy": "done_only"}
[/code]

### `run_task`

Створює кероване дочірнє завдання всередині наявного керованого TaskFlow.

Дозволені середовища виконання:

  * `subagent`
  * `acp`


Приклад:

jsonCopy code
[code]
    {  "action": "run_task",  "flowId": "flow_123",  "runtime": "acp",  "childSessionKey": "agent:main:acp:worker",  "task": "Inspect the next message batch"}
[/code]

## Форма відповіді

Успішні відповіді повертають:

jsonCopy code
[code]
    {  "ok": true,  "routeId": "zapier",  "result": {}}
[/code]

Відхилені запити повертають:

jsonCopy code
[code]
    {  "ok": false,  "routeId": "zapier",  "code": "not_found",  "error": "TaskFlow not found.",  "result": {}}
[/code]

Plugin навмисно вилучає метадані власника/сесії з відповідей Webhook.

## Пов’язані документи

  * [SDK середовища виконання Plugin](</uk/plugins/sdk-runtime>)
  * [Огляд hooks і webhooks](</uk/automation/hooks>)
  * [CLI webhooks](</uk/cli/webhooks>)


Was this useful?YesNo