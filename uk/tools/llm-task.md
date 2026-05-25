---
title: Завдання LLM
source_url: https://docs.openclaw.ai/uk/tools/llm-task
scraped_at: 2026-05-25
---

`llm-task` — це **необов’язковий інструмент Plugin** , який запускає LLM-завдання лише з JSON і повертає структурований вивід (за потреби перевірений за JSON Schema).

Це ідеально підходить для рушіїв робочих процесів на кшталт Lobster: ви можете додати один крок LLM без написання власного коду OpenClaw для кожного робочого процесу.

## Увімкнення Plugin

  1. Увімкніть Plugin:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  }}
[/code]

  2. Дозвольте необов’язковий інструмент:

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["llm-task"]  }}
[/code]

Використовуйте `tools.allow` лише тоді, коли потрібен режим обмежувального списку дозволів.

## Конфігурація (необов’язково)

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": {        "enabled": true,        "config": {          "defaultProvider": "openai-codex",          "defaultModel": "gpt-5.5",          "defaultAuthProfileId": "main",          "allowedModels": ["openai/gpt-5.4"],          "maxTokens": 800,          "timeoutMs": 30000        }      }    }  }}
[/code]

`allowedModels` — це список дозволів із рядків `provider/model`. Якщо його задано, будь-який запит поза списком буде відхилено.

## Параметри інструмента

  * `prompt` (рядок, обов’язково)
  * `input` (будь-який, необов’язково)
  * `schema` (об’єкт, необов’язкова JSON Schema)
  * `provider` (рядок, необов’язково)
  * `model` (рядок, необов’язково)
  * `thinking` (рядок, необов’язково)
  * `authProfileId` (рядок, необов’язково)
  * `temperature` (число, необов’язково)
  * `maxTokens` (число, необов’язково)
  * `timeoutMs` (число, необов’язково)


`thinking` приймає стандартні пресети міркування OpenClaw, як-от `low` або `medium`.

## Вивід

Повертає `details.json`, що містить розібраний JSON (і перевіряє його за `schema`, якщо її надано).

## Приклад: крок робочого процесу Lobster

### Важливе обмеження

Наведений нижче приклад припускає, що **автономний Lobster CLI** працює в середовищі, де `openclaw.invoke` вже має правильний URL Gateway і контекст автентифікації.

Для вбудованого **embedded** запускника Lobster всередині OpenClaw цей вкладений шаблон CLI **наразі ненадійний** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

Доки embedded Lobster не матиме підтримуваного мосту для цього потоку, надавайте перевагу одному з варіантів:

  * прямим викликам інструмента `llm-task` поза Lobster, або
  * крокам Lobster, які не залежать від вкладених викликів `openclaw.invoke`.


Приклад автономного Lobster CLI:

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": {    "subject": "Hello",    "body": "Can you help?"  },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

## Нотатки щодо безпеки

  * Інструмент працює **лише з JSON** і вказує моделі виводити тільки JSON (без блоків коду й без коментарів).
  * Для цього запуску моделі не надаються жодні інструменти.
  * Вважайте вивід ненадійним, якщо не перевіряєте його за допомогою `schema`.
  * Розміщуйте схвалення перед будь-яким кроком із побічними ефектами (надсилання, публікація, виконання).


## Пов’язане

  * [Рівні міркування](</uk/tools/thinking>)
  * [Підагенті](</uk/tools/subagents>)
  * [Slash-команди](</uk/tools/slash-commands>)


Was this useful?YesNo