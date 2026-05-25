---
title: Пошук у Perplexity
source_url: https://docs.openclaw.ai/uk/tools/perplexity-search
scraped_at: 2026-05-25
---

OpenClaw підтримує Perplexity Search API як провайдера `web_search`. Він повертає структуровані результати з полями `title`, `url` і `snippet`.

Для сумісності OpenClaw також підтримує застарілі налаштування Perplexity Sonar/OpenRouter. Якщо ви використовуєте `OPENROUTER_API_KEY`, ключ `sk-or-...` у `plugins.entries.perplexity.config.webSearch.apiKey` або задаєте `plugins.entries.perplexity.config.webSearch.baseUrl` / `model`, провайдер перемикається на шлях chat-completions і повертає AI-синтезовані відповіді з цитуваннями замість структурованих результатів Search API.

## Отримання API-ключа Perplexity

  1. Створіть обліковий запис Perplexity на [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>)
  2. Згенеруйте API-ключ у панелі керування
  3. Збережіть ключ у конфігурації або задайте `PERPLEXITY_API_KEY` у середовищі Gateway.


## Сумісність з OpenRouter

Якщо ви вже використовували OpenRouter для Perplexity Sonar, залиште `provider: "perplexity"` і задайте `OPENROUTER_API_KEY` у середовищі Gateway або збережіть ключ `sk-or-...` у `plugins.entries.perplexity.config.webSearch.apiKey`.

Необов’язкові параметри сумісності:

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## Приклади конфігурації

### Нативний Perplexity Search API

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### Сумісність OpenRouter / Sonar

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## Де задавати ключ

**Через конфігурацію:** виконайте `openclaw configure --section web`. Це зберігає ключ у `~/.openclaw/openclaw.json` у `plugins.entries.perplexity.config.webSearch.apiKey`. Це поле також приймає об’єкти SecretRef.

**Через середовище:** задайте `PERPLEXITY_API_KEY` або `OPENROUTER_API_KEY` у середовищі процесу Gateway. Для встановленого gateway помістіть його в `~/.openclaw/.env` (або у середовище вашої служби). Див. [змінні середовища](</uk/help/faq#env-vars-and-env-loading>).

Якщо налаштовано `provider: "perplexity"` і SecretRef ключа Perplexity не розв’язується без резервного варіанта в середовищі, запуск/перезавантаження швидко завершується помилкою.

## Параметри інструмента

Ці параметри застосовуються до нативного шляху Perplexity Search API.

Пошуковий запит.

Кількість результатів для повернення (1-10).

2-літерний код країни ISO (наприклад, `US`, `DE`).

Код мови ISO 639-1 (наприклад, `en`, `de`, `fr`).

Фільтр часу - `day` означає 24 години.

Лише результати, опубліковані після цієї дати (`YYYY-MM-DD`).

Лише результати, опубліковані до цієї дати (`YYYY-MM-DD`).

Масив дозволених/заборонених доменів (макс. 20).

Загальний бюджет вмісту (макс. 1000000).

Ліміт токенів на сторінку.

Для застарілого шляху сумісності Sonar/OpenRouter:

  * приймаються `query`, `count` і `freshness`
  * `count` там призначений лише для сумісності; відповідь усе одно є однією синтезованою відповіддю з цитуваннями, а не списком із N результатів
  * фільтри лише для Search API, такі як `country`, `language`, `date_after`, `date_before`, `domain_filter`, `max_tokens` і `max_tokens_per_page`, повертають явні помилки


**Приклади:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### Правила фільтра доменів

  * Максимум 20 доменів на фільтр
  * Не можна змішувати список дозволених і список заборонених в одному запиті
  * Використовуйте префікс `-` для записів списку заборонених (наприклад, `["-reddit.com"]`)


## Примітки

  * Perplexity Search API повертає структуровані результати вебпошуку (`title`, `url`, `snippet`)
  * OpenRouter або явні `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` перемикають Perplexity назад на chat completions Sonar для сумісності
  * Сумісність Sonar/OpenRouter повертає одну синтезовану відповідь із цитуваннями, а не структуровані рядки результатів
  * Результати кешуються на 15 хвилин за замовчуванням (налаштовується через `cacheTtlMinutes`)


## Пов’язане

[**Огляд вебпошуку** Усі провайдери та правила автовизначення. ](</uk/tools/web>) [**Пошук Brave** Структуровані результати з фільтрами країни та мови. ](</uk/tools/brave-search>) [**Пошук Exa** Нейронний пошук із витягуванням вмісту. ](</uk/tools/exa-search>) [**Документація Perplexity Search API** Офіційний quickstart і довідник Perplexity Search API. ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo