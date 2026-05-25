---
title: Виконання коду
source_url: https://docs.openclaw.ai/uk/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution` запускає ізольований віддалений аналіз Python в API Responses від xAI. Він реєструється вбудованим Plugin `xai` (за контрактом `tools`) і надсилає запити до того самого кінцевого пункту `https://api.x.ai/v1/responses`, який використовує `x_search`.

Властивість | Значення  
---|---  
Назва інструмента | `code_execution`  
Plugin постачальника | `xai` (вбудований, `enabledByDefault: true`)  
Автентифікація | профіль автентифікації xAI, `XAI_API_KEY` або `plugins.entries.xai.config.webSearch.apiKey`  
Модель за замовчуванням | `grok-4-1-fast`  
Тайм-аут за замовчуванням | 30 секунд  
`maxTurns` за замовчуванням | не задано (xAI застосовує власне внутрішнє обмеження)  
  
Це відрізняється від локального [`exec`](</uk/tools/exec>):

  * `exec` запускає команди оболонки на вашій машині або спареному вузлі.
  * `code_execution` запускає Python у віддаленій пісочниці xAI.


Використовуйте `code_execution` для:

  * Обчислень.
  * Табулювання.
  * Швидкої статистики.
  * Аналізу у стилі діаграм.
  * Аналізу даних, повернутих `x_search` або `web_search`.


**Не** використовуйте його, коли вам потрібні локальні файли, ваша оболонка, ваш репозиторій або спарені пристрої. Для цього використовуйте [`exec`](</uk/tools/exec>).

## Налаштування

* ### Надайте API-ключ xAI

Запустіть `openclaw onboard --auth-choice xai-api-key` для `code_execution` і `x_search`, або задайте `XAI_API_KEY` / налаштуйте ключ у Plugin xAI, якщо ви також хочете, щоб вебпошук Grok використовував ті самі облікові дані:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

Або через конфігурацію:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### Увімкніть і налаштуйте code_execution

Інструмент керується параметром `plugins.entries.xai.config.codeExecution.enabled`. За замовчуванням вимкнено.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // override the default xAI code-execution model            maxTurns: 2,            // optional cap on internal tool turns            timeoutSeconds: 30,     // request timeout (default: 30)          },        },      },    },  },}
[/code]

* ### Перезапустіть Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

`code_execution` з’явиться у списку інструментів агента, щойно Plugin xAI перереєструється з `enabled: true`.

## Як користуватися

Запитуйте природно й чітко вказуйте намір аналізу:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

Інструмент внутрішньо приймає один параметр `task`, тому агент має надіслати повний запит на аналіз і будь-які вбудовані дані в одному prompt.

## Помилки

Коли інструмент запускається без автентифікації, він повертає структуровану помилку `missing_xai_api_key`, яка вказує на профіль автентифікації, змінну середовища й параметри конфігурації. Помилка має формат JSON, а не викидається як виняток, тому агент може самостійно виправитися:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## Обмеження

  * Це віддалене виконання xAI, а не локальне виконання процесу.
  * Розглядайте результати як тимчасовий аналіз, а не як постійну сесію notebook.
  * Не припускайте доступу до локальних файлів або вашої робочої області.
  * Для свіжих даних X спочатку використовуйте [`x_search`](</uk/tools/web#x_search>), а потім передайте результат у `code_execution`.


## Пов’язане

[**Інструмент Exec** Локальне виконання команд оболонки на вашій машині або спареному вузлі. ](</uk/tools/exec>) [**Схвалення Exec** Політика дозволу/заборони для виконання команд оболонки. ](</uk/tools/exec-approvals>) [**Вебінструменти** `web_search`, `x_search` і `web_fetch`. ](</uk/tools/web>) [**Постачальник xAI** Моделі Grok, вебпошук/пошук X і конфігурація виконання коду. ](</uk/providers/xai>)

Was this useful?YesNo