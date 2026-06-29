---
title: Поиск Kimi
source_url: https://docs.openclaw.ai/ru/tools/kimi-search
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw поддерживает Kimi как провайдера `web_search`, используя веб-поиск Moonshot для создания AI-синтезированных ответов с цитированием.

## Получение API-ключа

* ### Создайте ключ

Получите API-ключ в [Moonshot AI](<https://platform.moonshot.cn/>).

* ### Сохраните ключ

Задайте `KIMI_API_KEY` или `MOONSHOT_API_KEY` в окружении Gateway либо настройте через:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Когда вы выбираете **Kimi** во время `openclaw onboard` или `openclaw configure --section web`, OpenClaw также может запросить:

  * регион Moonshot API: 
    * `https://api.moonshot.ai/v1`
    * `https://api.moonshot.cn/v1`
  * модель веб-поиска Kimi по умолчанию (по умолчанию `kimi-k2.6`)


## Конфигурация

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // optional if KIMI_API_KEY or MOONSHOT_API_KEY is set            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

Если вы используете китайский хост API для чата (`models.providers.moonshot.baseUrl`: `https://api.moonshot.cn/v1`), OpenClaw повторно использует тот же хост для Kimi `web_search`, когда `tools.web.search.kimi.baseUrl` не указан, поэтому ключи с [platform.moonshot.cn](<https://platform.moonshot.cn/>) по ошибке не отправляются на международный endpoint (который часто возвращает HTTP 401). Переопределите через `tools.web.search.kimi.baseUrl`, если вам нужен другой базовый URL поиска.

**Альтернатива через окружение:** задайте `KIMI_API_KEY` или `MOONSHOT_API_KEY` в окружении Gateway. Для установки gateway поместите его в `~/.openclaw/.env`.

Если `baseUrl` не указан, OpenClaw по умолчанию использует `https://api.moonshot.ai/v1`. Если `model` не указан, OpenClaw по умолчанию использует `kimi-k2.6`.

## Как это работает

Kimi использует веб-поиск Moonshot для синтеза ответов со встроенными цитатами, похожий на подход Gemini и Grok к ответам, основанным на подтверждающих источниках.

OpenClaw считает Kimi `web_search` успешным только после того, как Moonshot вернет нативные подтверждающие данные веб-поиска, например воспроизводимую полезную нагрузку инструмента `$web_search`, `search_results` или URL цитирования. Если Kimi сразу останавливается с обычным ответом чата вроде «Я не могу просматривать интернет» и без подтверждающих данных, OpenClaw возвращает структурированную ошибку `kimi_web_search_ungrounded` вместо упаковки этого текста как результата поиска. Повторите запрос, переключитесь на структурированного провайдера, например Brave, или используйте `web_fetch` / инструмент браузера, если у вас уже есть целевой URL.

## Поддерживаемые параметры

Поиск Kimi поддерживает `query`.

`count` принимается для совместимости с общим `web_search`, но Kimi все равно возвращает один синтезированный ответ с цитатами, а не список из N результатов.

Фильтры, специфичные для провайдера, сейчас не поддерживаются.

## См. также

  * [Обзор веб-поиска](</ru/tools/web>) \-- все провайдеры и автообнаружение
  * [Moonshot AI](</ru/providers/moonshot>) \-- документация по модели Moonshot и провайдеру Kimi Coding
  * [Поиск Gemini](</ru/tools/gemini-search>) \-- AI-синтезированные ответы через подтверждение Google
  * [Поиск Grok](</ru/tools/grok-search>) \-- AI-синтезированные ответы через подтверждение xAI


Was this useful?YesNo

Open issue