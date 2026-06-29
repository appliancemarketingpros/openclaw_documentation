---
title: Выполнение кода
source_url: https://docs.openclaw.ai/ru/tools/code-execution
scraped_at: 2026-06-29
---

CapabilitiesTools

`code_execution` запускает изолированный удаленный анализ на Python через Responses API xAI. Он регистрируется встроенным plugin `xai` (по контракту `tools`) и отправляет запросы на тот же endpoint `https://api.x.ai/v1/responses`, который используется `x_search`.

Свойство | Значение  
---|---  
Имя инструмента | `code_execution`  
Plugin провайдера | `xai` (встроенный, `enabledByDefault: true`)  
Аутентификация | профиль аутентификации xAI, `XAI_API_KEY` или `plugins.entries.xai.config.webSearch.apiKey`  
Модель по умолчанию | `grok-4-1-fast`  
Тайм-аут по умолчанию | 30 секунд  
`maxTurns` по умолчанию | не задано (xAI применяет собственный внутренний лимит)  
  
Это отличается от локального [`exec`](</ru/tools/exec>):

  * `exec` запускает команды оболочки на вашем компьютере или сопряженном узле.
  * `code_execution` запускает Python в удаленной песочнице xAI.


Используйте `code_execution` для:

  * Расчетов.
  * Табулирования.
  * Быстрой статистики.
  * Анализа в стиле диаграмм.
  * Анализа данных, возвращенных `x_search` или `web_search`.


**Не** используйте его, когда нужны локальные файлы, ваша оболочка, ваш репозиторий или сопряженные устройства. Для этого используйте [`exec`](</ru/tools/exec>).

## Настройка

* ### Provide xAI credentials

Войдите через Grok OAuth с подходящей подпиской SuperGrok или X Premium либо сохраните API-ключ. xAI OAuth использует проверку с кодом устройства, поэтому работает с удаленных хостов без callback на localhost. OAuth работает для `code_execution` и `x_search`; `XAI_API_KEY` или web-search config plugin также могут обеспечивать работу Grok `web_search`.

bashCopy code
[code]
    openclaw models auth login --provider xai --method oauth
[/code]

При новой установке те же варианты аутентификации доступны во время onboarding:

bashCopy code
[code]
    openclaw onboard --install-daemonopenclaw onboard --install-daemon --auth-choice xai-oauth
[/code]

Или используйте API-ключ:

bashCopy code
[code]
    openclaw models auth login --provider xai --method api-keyexport XAI_API_KEY=xai-...
[/code]

Или через config:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### Enable and tune code_execution

`code_execution` доступен, когда доступны учетные данные xAI. Установите `plugins.entries.xai.config.codeExecution.enabled` в `false`, чтобы отключить его, или используйте тот же блок для настройки модели и тайм-аута.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // override the default xAI code-execution model            maxTurns: 2,            // optional cap on internal tool turns            timeoutSeconds: 30,     // request timeout (default: 30)          },        },      },    },  },}
[/code]

* ### Restart the Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

`code_execution` появляется в списке инструментов агента после повторной регистрации plugin xAI с `enabled: true`.

## Как использовать

Задавайте запрос естественно и явно указывайте цель анализа:

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

Внутренне инструмент принимает один параметр `task`, поэтому агент должен отправлять полный запрос на анализ и любые встроенные данные в одном prompt.

## Ошибки

Когда инструмент запускается без аутентификации, он возвращает структурированную ошибку `missing_xai_api_key`, указывающую на профиль аутентификации, переменную окружения и параметры config. Ошибка представлена в JSON и не выбрасывается как исключение, поэтому агент может исправиться самостоятельно:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs xAI credentials. Run `openclaw onboard --auth-choice xai-oauth` to sign in with Grok, run `openclaw onboard --auth-choice xai-api-key`, set `XAI_API_KEY` in the Gateway environment, or configure `plugins.entries.xai.config.webSearch.apiKey`.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## Ограничения

  * Это удаленное выполнение xAI, а не выполнение локального процесса.
  * Рассматривайте результаты как временный анализ, а не как постоянную сессию notebook.
  * Не предполагается доступ к локальным файлам или вашему рабочему пространству.
  * Для свежих данных X сначала используйте [`x_search`](</ru/tools/web#x_search>), а затем передайте результат в `code_execution`.


## Связанное

[**Exec tool** Локальное выполнение команд оболочки на вашем компьютере или сопряженном узле. ](</ru/tools/exec>) [**Exec approvals** Политика разрешения и запрета для выполнения команд оболочки. ](</ru/tools/exec-approvals>) [**Web tools** `web_search`, `x_search` и `web_fetch`. ](</ru/tools/web>) [**xAI provider** Модели Grok, веб-поиск/поиск в X и config выполнения кода. ](</ru/providers/xai>)

Was this useful?YesNo

Open issue