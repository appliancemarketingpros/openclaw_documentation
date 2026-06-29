---
title: Поиск Perplexity
source_url: https://docs.openclaw.ai/ru/tools/perplexity-search
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw поддерживает Perplexity Search API как провайдера `web_search`. Он возвращает структурированные результаты с полями `title`, `url` и `snippet`.

Для совместимости OpenClaw также поддерживает устаревшие настройки Perplexity Sonar/OpenRouter. Если вы используете `OPENROUTER_API_KEY`, ключ `sk-or-...` в `plugins.entries.perplexity.config.webSearch.apiKey` или задаете `plugins.entries.perplexity.config.webSearch.baseUrl` / `model`, провайдер переключается на путь chat-completions и возвращает сгенерированные ИИ ответы с цитированием вместо структурированных результатов Search API.

## Установите Plugin

Установите официальный Plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/perplexity-pluginopenclaw gateway restart
[/code]

## Получение API-ключа Perplexity

  1. Создайте учетную запись Perplexity на [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>)
  2. Создайте API-ключ в панели управления
  3. Сохраните ключ в конфигурации или задайте `PERPLEXITY_API_KEY` в окружении Gateway.


## Совместимость с OpenRouter

Если вы уже использовали OpenRouter для Perplexity Sonar, оставьте `provider: "perplexity"` и задайте `OPENROUTER_API_KEY` в окружении Gateway либо сохраните ключ `sk-or-...` в `plugins.entries.perplexity.config.webSearch.apiKey`.

Необязательные параметры совместимости:

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## Примеры конфигурации

### Нативный Perplexity Search API

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### Совместимость с OpenRouter / Sonar

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## Где задать ключ

**Через конфигурацию:** выполните `openclaw configure --section web`. Команда сохраняет ключ в `~/.openclaw/openclaw.json` в поле `plugins.entries.perplexity.config.webSearch.apiKey`. Это поле также принимает объекты SecretRef.

**Через окружение:** задайте `PERPLEXITY_API_KEY` или `OPENROUTER_API_KEY` в окружении процесса Gateway. Для установки Gateway поместите его в `~/.openclaw/.env` (или в окружение вашего сервиса). См. [Переменные окружения](</ru/help/faq#env-vars-and-env-loading>).

Если настроен `provider: "perplexity"` и SecretRef ключа Perplexity не разрешается без резервного значения из окружения, запуск или перезагрузка быстро завершается ошибкой.

## Параметры инструмента

Эти параметры применяются к нативному пути Perplexity Search API.

Поисковый запрос.

Количество возвращаемых результатов (1-10).

Двухбуквенный код страны ISO (например, `US`, `DE`).

Код языка ISO 639-1 (например, `en`, `de`, `fr`).

Фильтр по времени: `day` означает 24 часа.

Только результаты, опубликованные после этой даты (`YYYY-MM-DD`).

Только результаты, опубликованные до этой даты (`YYYY-MM-DD`).

Массив списка разрешенных или запрещенных доменов (максимум 20).

Общий бюджет содержимого (максимум 1000000).

Лимит токенов на страницу.

Для устаревшего пути совместимости Sonar/OpenRouter:

  * принимаются `query`, `count` и `freshness`
  * `count` там предназначен только для совместимости; ответ все равно представляет собой один синтезированный ответ с цитированием, а не список из N результатов
  * фильтры только для Search API, такие как `country`, `language`, `date_after`, `date_before`, `domain_filter`, `max_tokens` и `max_tokens_per_page`, возвращают явные ошибки


**Примеры:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### Правила фильтра доменов

  * Максимум 20 доменов на фильтр
  * Нельзя смешивать список разрешенных и список запрещенных доменов в одном запросе
  * Используйте префикс `-` для записей списка запрещенных доменов (например, `["-reddit.com"]`)


## Примечания

  * Perplexity Search API возвращает структурированные результаты веб-поиска (`title`, `url`, `snippet`)
  * OpenRouter или явные `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` переключают Perplexity обратно на chat completions Sonar для совместимости
  * Совместимость Sonar/OpenRouter возвращает один синтезированный ответ с цитированием, а не строки структурированных результатов
  * Результаты по умолчанию кэшируются на 15 минут (настраивается через `cacheTtlMinutes`)


## См. также

[**Web search overview** Все провайдеры и правила автоопределения. ](</ru/tools/web>) [**Brave search** Структурированные результаты с фильтрами по стране и языку. ](</ru/tools/brave-search>) [**Exa search** Нейронный поиск с извлечением содержимого. ](</ru/tools/exa-search>) [**Perplexity Search API docs** Официальное краткое руководство и справочник Perplexity Search API. ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo

Open issue