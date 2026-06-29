---
title: Поиск в интернете
source_url: https://docs.openclaw.ai/ru/tools/web
scraped_at: 2026-06-29
---

CapabilitiesTools

Инструмент `web_search` выполняет поиск в интернете через настроенного поставщика и возвращает результаты. Результаты кэшируются по запросу на 15 минут (настраивается).

OpenClaw также включает `x_search` для публикаций X (ранее Twitter) и `web_fetch` для легкого получения URL. На этом этапе `web_fetch` остается локальным, а `web_search` и `x_search` могут использовать xAI Responses под капотом.

## Быстрый старт

* ### Choose a provider

Выберите поставщика и выполните необходимую настройку. Некоторые поставщики не требуют ключей, а другие используют API-ключи. Подробности см. на страницах поставщиков ниже.

* ### Configure

bashCopy code
[code]
    openclaw configure --section web
[/code]

Это сохраняет поставщика и все необходимые учетные данные. Также можно задать переменную окружения (например, `BRAVE_API_KEY`) и пропустить этот шаг для поставщиков с API.

* ### Use it

Агент теперь может вызывать `web_search`:

javascriptCopy code
[code]
    await web_search({ query: "OpenClaw plugin SDK" });
[/code]

Для публикаций X используйте:

javascriptCopy code
[code]
    await x_search({ query: "dinner recipes" });
[/code]

## Выбор поставщика

[**Brave Search** Структурированные результаты со сниппетами. Поддерживает режим `llm-context`, фильтры по стране и языку. Доступен бесплатный уровень. ](</ru/tools/brave-search>) [**Codex Hosted Search** Синтезированные ИИ ответы с привязкой к источникам через вашу учетную запись app-server Codex. ](</ru/plugins/codex-harness>) [**DuckDuckGo** Поставщик без ключа. API-ключ не нужен. Неофициальная интеграция на основе HTML. ](</ru/tools/duckduckgo-search>) [**Exa** Нейронный и ключевой поиск с извлечением содержимого (выделения, текст, сводки). ](</ru/tools/exa-search>) [**Firecrawl** Структурированные результаты. Лучше всего использовать вместе с `firecrawl_search` и `firecrawl_scrape` для глубокого извлечения. ](</ru/tools/firecrawl>) [**Gemini** Синтезированные ИИ ответы с цитированием через привязку к Google Search. ](</ru/tools/gemini-search>) [**Grok** Синтезированные ИИ ответы с цитированием через веб-привязку xAI. ](</ru/tools/grok-search>) [**Kimi** Синтезированные ИИ ответы с цитированием через веб-поиск Moonshot; резервные варианты чата без привязки явно завершаются ошибкой. ](</ru/tools/kimi-search>) [**MiniMax Search** Структурированные результаты через API поиска MiniMax Token Plan. ](</ru/tools/minimax-search>) [**Ollama Web Search** Поиск через локальный хост Ollama с выполненным входом или размещенный API Ollama. ](</ru/tools/ollama-search>) [**Parallel** Платный Parallel Search API (`PARALLEL_API_KEY`); более высокие лимиты частоты и настройка объективности. ](</ru/tools/parallel-search>) [**Parallel Search (Free)** Подключаемый вариант без ключа. Бесплатный Search MCP от Parallel, с плотными отрывками, оптимизированными для LLM, и без API-ключа. ](</ru/tools/parallel-search>) [**Perplexity** Структурированные результаты с настройками извлечения содержимого и фильтрацией по доменам. ](</ru/tools/perplexity-search>) [**SearXNG** Самостоятельно размещаемый метапоиск. API-ключ не нужен. Агрегирует Google, Bing, DuckDuckGo и другие. ](</ru/tools/searxng-search>) [**Tavily** Структурированные результаты с глубиной поиска, фильтрацией по темам и `tavily_extract` для извлечения URL. ](</ru/tools/tavily>)

### Сравнение поставщиков

Поставщик | Стиль результатов | Фильтры | API-ключ  
---|---|---|---  
[Brave](</ru/tools/brave-search>) | Структурированные сниппеты | Страна, язык, время, режим `llm-context` | `BRAVE_API_KEY`  
[Codex Hosted Search](</ru/plugins/codex-harness>) | Синтезированные ИИ ответы + URL источников | Домены, размер контекста, местоположение пользователя | Нет; используется вход Codex/OpenAI  
[DuckDuckGo](</ru/tools/duckduckgo-search>) | Структурированные сниппеты | \-- | Нет (без ключа)  
[Exa](</ru/tools/exa-search>) | Структурированные + извлеченные | Нейронный/ключевой режим, дата, извлечение содержимого | `EXA_API_KEY`  
[Firecrawl](</ru/tools/firecrawl>) | Структурированные сниппеты | Через инструмент `firecrawl_search` | `FIRECRAWL_API_KEY`  
[Gemini](</ru/tools/gemini-search>) | Синтезированные ИИ ответы + цитирование | \-- | `GEMINI_API_KEY`  
[Grok](</ru/tools/grok-search>) | Синтезированные ИИ ответы + цитирование | \-- | OAuth xAI, `XAI_API_KEY` или `plugins.entries.xai.config.webSearch.apiKey`  
[Kimi](</ru/tools/kimi-search>) | Синтезированные ИИ ответы + цитирование; завершается ошибкой при резервных вариантах чата без привязки | \-- | `KIMI_API_KEY` / `MOONSHOT_API_KEY`  
[MiniMax Search](</ru/tools/minimax-search>) | Структурированные сниппеты | Регион (`global` / `cn`) | `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN`  
[Ollama Web Search](</ru/tools/ollama-search>) | Структурированные сниппеты | \-- | Нет для локальных хостов с выполненным входом; `OLLAMA_API_KEY` для прямого поиска `https://ollama.com`  
[Parallel](</ru/tools/parallel-search>) | Плотные отрывки, ранжированные для контекста LLM | \-- | `PARALLEL_API_KEY` (платный)  
[Parallel Search (Free)](</ru/tools/parallel-search>) | Плотные отрывки, ранжированные для контекста LLM | \-- | Нет (бесплатный Search MCP)  
[Perplexity](</ru/tools/perplexity-search>) | Структурированные сниппеты | Страна, язык, время, домены, лимиты содержимого | `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY`  
[SearXNG](</ru/tools/searxng-search>) | Структурированные сниппеты | Категории, язык | Нет (самостоятельное размещение)  
[Tavily](</ru/tools/tavily>) | Структурированные сниппеты | Через инструмент `tavily_search` | `TAVILY_API_KEY`  
  
## Автообнаружение

## Нативный веб-поиск OpenAI

Прямые модели OpenAI Responses автоматически используют размещенный инструмент OpenAI `web_search`, когда веб-поиск OpenClaw включен и управляемый поставщик не закреплен. Это поведение принадлежит поставщику в составе встроенного OpenAI Plugin и применяется только к нативному трафику OpenAI API, а не к OpenAI-совместимым базовым URL прокси или маршрутам Azure. Задайте `tools.web.search.provider` на другого поставщика, например `brave`, чтобы сохранить управляемый инструмент `web_search` для моделей OpenAI, или задайте `tools.web.search.enabled: false`, чтобы отключить и управляемый поиск, и нативный поиск OpenAI.

## Нативный веб-поиск Codex

Среда выполнения app-server Codex автоматически использует размещенный инструмент Codex `web_search`, когда веб-поиск включен и управляемый поставщик не выбран. Нативный размещенный поиск и управляемый динамический инструмент OpenClaw `web_search` являются взаимоисключающими, поэтому управляемый поиск не может обходить нативные ограничения доменов. OpenClaw использует управляемый инструмент, когда размещенный поиск недоступен, явно отключен или заменен выбранным управляемым поставщиком. OpenClaw держит автономное расширение Codex `web.run` отключенным, потому что производственный трафик app-server отклоняет его пользовательское пространство имен `web`.

  * Настраивайте нативный поиск в `tools.web.search.openaiCodex`
  * Задайте `tools.web.search.provider: "codex"`, чтобы подготовить Codex Hosted Search как управляемого поставщика `web_search` для любой родительской модели. Каждый вызов выполняет ограниченный эфемерный ход app-server Codex и завершается ошибкой, если Codex не выдает размещенный элемент `webSearch`.
  * `mode: "cached"` — предпочтение по умолчанию, но Codex разрешает его в живой внешний доступ для неограниченных ходов app-server; задайте `"live"`, чтобы явно запросить живой доступ
  * Задайте `tools.web.search.provider` на управляемого поставщика, например `brave`, чтобы использовать управляемый `web_search` OpenClaw вместо него
  * Задайте `tools.web.search.openaiCodex.enabled: false`, чтобы отказаться от размещенного в Codex поиска; другие управляемые поставщики остаются доступны
  * Ограничение нативной поверхности инструментов Codex также оставляет управляемый `web_search` доступным
  * Когда задан `allowedDomains`, автоматический управляемый резервный вариант завершается закрыто, если размещенный поиск недоступен, чтобы нативный список разрешенных доменов нельзя было обойти
  * Запуски LLM-only с отключенными инструментами отключают и нативный, и управляемый поиск
  * `tools.web.search.enabled: false` отключает и управляемый, и нативный поиск


Постоянные эффективные изменения политики поиска Codex запускают свежую привязанную ветку, чтобы уже загруженная ветка app-server не могла сохранить устаревший доступ к размещенному поиску. Временные ограничения на один ход используют временную ограниченную ветку и сохраняют существующую привязку для последующего возобновления.

Прямой трафик OpenAI ChatGPT Responses также может использовать размещенный OpenAI инструмент `web_search`. Этот отдельный путь остается подключаемым через `tools.web.search.openaiCodex.enabled: true` и применяется только к подходящим моделям `openai/*`, использующим `api: "openai-chatgpt-responses"`.

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true,        // Optional: use Codex Hosted Search from non-Codex parent models too.        provider: "codex",        openaiCodex: {          enabled: true,          mode: "cached",          allowedDomains: ["example.com"],          contextSize: "high",          userLocation: {            country: "US",            city: "New York",            timezone: "America/New_York",          },        },      },    },  },}
[/code]

Для сред выполнения и поставщиков, которые не поддерживают нативный поиск Codex, Codex может использовать управляемый резервный `web_search` через динамическое пространство имен инструментов OpenClaw. Используйте явного управляемого поставщика, когда вам нужны сетевые настройки OpenClaw, специфичные для поставщика, вместо размещенного в Codex поиска.

Выбор `provider: "codex"` включает встроенный plugin `codex` и использует те же ограничения `tools.web.search.openaiCodex`, которые показаны выше. Сначала аутентифицируйте app-server Codex с помощью `openclaw models auth login --provider openai`. Родительский агент может использовать любую модель или runtime; только ограниченный поиск-worker выполняется через Codex.

## Сетевая безопасность

Вызовы управляемого HTTP-поставщика `web_search` используют защищенный путь fetch OpenClaw. Для доверенных API-хостов поставщиков OpenClaw разрешает DNS-ответы fake-IP от Surge, Clash и sing-box в `198.18.0.0/15` и `fc00::/7` только для этого имени хоста поставщика. Другие частные, loopback, link-local и metadata назначения остаются заблокированными. Codex Hosted Search является исключением: его ограниченный worker делегирует сетевой доступ размещенному инструменту `web_search` app-server Codex.

Это автоматическое разрешение не применяется к произвольным URL `web_fetch`. Для `web_fetch` явно включайте `tools.web.fetch.ssrfPolicy.allowRfc2544BenchmarkRange` и `tools.web.fetch.ssrfPolicy.allowIpv6UniqueLocalRange` только если ваш доверенный proxy владеет этими синтетическими диапазонами.

## Настройка веб-поиска

Списки поставщиков в документации и потоках настройки упорядочены по алфавиту. Автообнаружение сохраняет отдельный порядок приоритета.

Если `provider` не задан, OpenClaw проверяет поставщиков в этом порядке и использует первого готового:

Сначала поставщики с поддержкой API:

  1. **Brave** \-- `BRAVE_API_KEY` или `plugins.entries.brave.config.webSearch.apiKey` (порядок 10)
  2. **MiniMax Search** \-- `MINIMAX_CODE_PLAN_KEY` / `MINIMAX_CODING_API_KEY` / `MINIMAX_OAUTH_TOKEN` / `MINIMAX_API_KEY` или `plugins.entries.minimax.config.webSearch.apiKey` (порядок 15)
  3. **Gemini** \-- `plugins.entries.google.config.webSearch.apiKey`, `GEMINI_API_KEY` или `models.providers.google.apiKey` (порядок 20)
  4. **Grok** \-- xAI OAuth, `XAI_API_KEY` или `plugins.entries.xai.config.webSearch.apiKey` (порядок 30)
  5. **Kimi** \-- `KIMI_API_KEY` / `MOONSHOT_API_KEY` или `plugins.entries.moonshot.config.webSearch.apiKey` (порядок 40)
  6. **Perplexity** \-- `PERPLEXITY_API_KEY` / `OPENROUTER_API_KEY` или `plugins.entries.perplexity.config.webSearch.apiKey` (порядок 50)
  7. **Firecrawl** \-- `FIRECRAWL_API_KEY` или `plugins.entries.firecrawl.config.webSearch.apiKey` (порядок 60)
  8. **Exa** \-- `EXA_API_KEY` или `plugins.entries.exa.config.webSearch.apiKey`; необязательный `plugins.entries.exa.config.webSearch.baseUrl` переопределяет endpoint Exa (порядок 65)
  9. **Tavily** \-- `TAVILY_API_KEY` или `plugins.entries.tavily.config.webSearch.apiKey` (порядок 70)
  10. **Parallel** \-- платный Parallel Search API через `PARALLEL_API_KEY` или `plugins.entries.parallel.config.webSearch.apiKey`; необязательный `plugins.entries.parallel.config.webSearch.baseUrl` переопределяет endpoint (порядок 75)


После этого идут поставщики с настроенным endpoint:

  11. **SearXNG** \-- `SEARXNG_BASE_URL` или `plugins.entries.searxng.config.webSearch.baseUrl` (порядок 200)


Поставщики без ключа, такие как **Parallel Search (Free)** , **DuckDuckGo** , **Ollama Web Search** и **Codex Hosted Search** , доступны только когда вы явно выбираете их через `tools.web.search.provider` или через `openclaw configure --section web`. OpenClaw не отправляет управляемые запросы `web_search` поставщику без ключа только потому, что не настроен поставщик с поддержкой API.

Модели OpenAI Responses являются исключением: пока `tools.web.search.provider` не задан, они используют нативный веб-поиск OpenAI вместо управляемых поставщиков выше. Установите `tools.web.search.provider` в `parallel-free` (или другого поставщика), чтобы направить их через управляемый путь.

## Конфигурация

json5Copy code
[code]
    {  tools: {    web: {      search: {        enabled: true, // default: true        provider: "brave", // or omit for auto-detection        maxResults: 5,        timeoutSeconds: 30,        cacheTtlMinutes: 15,      },    },  },}
[/code]

Конфигурация, специфичная для поставщика (ключи API, базовые URL, режимы), находится в `plugins.entries.<plugin>.config.webSearch.*`. Gemini также может повторно использовать `models.providers.google.apiKey` и `models.providers.google.baseUrl` как fallback с более низким приоритетом после своей выделенной конфигурации веб-поиска и `GEMINI_API_KEY`. См. примеры на страницах поставщиков. Grok также может повторно использовать auth profile xAI OAuth из `openclaw models auth login --provider xai --method oauth`; конфигурация API-ключа остается fallback.

`tools.web.search.provider` проверяется по id поставщиков веб-поиска, объявленным в манифестах встроенных и установленных plugin. Опечатка вроде `"brvae"` приводит к ошибке валидации конфигурации вместо тихого fallback к автообнаружению. Если у настроенного поставщика есть только устаревшее свидетельство plugin, например оставшийся блок `plugins.entries.<plugin>` после удаления стороннего plugin, OpenClaw сохраняет устойчивость запуска и сообщает предупреждение, чтобы вы могли переустановить plugin или выполнить `openclaw doctor --fix` для очистки устаревшей конфигурации.

Выбор fallback-поставщика `web_fetch` выполняется отдельно:

  * выберите его с помощью `tools.web.fetch.provider`
  * или опустите это поле и позвольте OpenClaw автообнаружить первого готового поставщика web-fetch по настроенным учетным данным
  * несандбоксированный `web_fetch` может использовать установленные поставщики plugin, которые объявляют `contracts.webFetchProviders`; сандбоксированные fetch разрешают встроенных поставщиков и проверенные установки официальных plugin, но исключают сторонние внешние plugin
  * официальный plugin Firecrawl предоставляет fallback web-fetch, настроенный в `plugins.entries.firecrawl.config.webFetch.*`


Когда вы выбираете **Kimi** во время `openclaw onboard` или `openclaw configure --section web`, OpenClaw также может запросить:

  * регион Moonshot API (`https://api.moonshot.ai/v1` или `https://api.moonshot.cn/v1`)
  * модель веб-поиска Kimi по умолчанию (по умолчанию `kimi-k2.6`)


Для `x_search` настройте `plugins.entries.xai.config.xSearch.*`. Он использует тот же auth profile xAI, что и chat, или учетные данные `XAI_API_KEY` / plugin web-search, используемые веб-поиском Grok. Устаревшая конфигурация `tools.web.x_search.*` автоматически мигрируется командой `openclaw doctor --fix`. Когда вы выбираете Grok во время `openclaw onboard` или `openclaw configure --section web`, OpenClaw также может предложить необязательную настройку `x_search` с теми же учетными данными. Это отдельный последующий шаг внутри пути Grok, а не отдельный вариант поставщика веб-поиска верхнего уровня. Если вы выберете другого поставщика, OpenClaw не покажет prompt `x_search`.

### Хранение API-ключей

### Config file

Выполните `openclaw configure --section web` или задайте ключ напрямую:

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "YOUR_KEY", // pragma: allowlist secret          },        },      },    },  },}
[/code]

### Environment variable

Задайте env var поставщика в окружении процесса Gateway:

bashCopy code
[code]
    export BRAVE_API_KEY="YOUR_KEY"
[/code]

Для установки gateway поместите ее в `~/.openclaw/.env`. См. [Env vars](</ru/help/faq#env-vars-and-env-loading>).

## Параметры инструмента

Параметр | Описание  
---|---  
`query` | Поисковый запрос (обязательно)  
`count` | Возвращаемые результаты (1-10, по умолчанию: 5)  
`country` | 2-буквенный код страны ISO (например, "US", "DE")  
`language` | Код языка ISO 639-1 (например, "en", "de")  
`search_lang` | Код языка поиска (только Brave)  
`freshness` | Фильтр времени: `day`, `week`, `month` или `year`  
`date_after` | Результаты после этой даты (YYYY-MM-DD)  
`date_before` | Результаты до этой даты (YYYY-MM-DD)  
`ui_lang` | Код языка UI (только Brave)  
`domain_filter` | Массив allowlist/denylist доменов (только Perplexity)  
`max_tokens` | Общий бюджет содержимого, по умолчанию 25000 (только Perplexity)  
`max_tokens_per_page` | Лимит токенов на страницу, по умолчанию 2048 (только Perplexity)  
  
## x_search

`x_search` запрашивает посты X (ранее Twitter) с помощью xAI и возвращает AI-синтезированные ответы с citations. Он принимает запросы на естественном языке и необязательные структурированные фильтры. OpenClaw включает встроенный инструмент xAI `x_search` только для запроса, который обслуживает этот вызов инструмента.

### Конфигурация x_search

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast-non-reasoning",            baseUrl: "https://api.x.ai/v1", // optional, overrides webSearch.baseUrl            inlineCitations: false,            maxTurns: 2,            timeoutSeconds: 30,            cacheTtlMinutes: 15,          },          webSearch: {            apiKey: "xai-...", // optional if an xAI auth profile or XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional shared xAI Responses base URL          },        },      },    },  },}
[/code]

`x_search` отправляет POST в `<baseUrl>/responses`, когда задан `plugins.entries.xai.config.xSearch.baseUrl`. Если это поле опущено, он переходит к `plugins.entries.xai.config.webSearch.baseUrl`, затем к устаревшему `tools.web.search.grok.baseUrl` и, наконец, к публичному endpoint xAI.

### Параметры x_search

Параметр | Описание  
---|---  
`query` | Поисковый запрос (обязательно)  
`allowed_x_handles` | Ограничить результаты указанными именами пользователей X  
`excluded_x_handles` | Исключить указанные имена пользователей X  
`from_date` | Включать только публикации за эту дату или позже (YYYY-MM-DD)  
`to_date` | Включать только публикации за эту дату или раньше (YYYY-MM-DD)  
`enable_image_understanding` | Разрешить xAI анализировать изображения, прикрепленные к найденным публикациям  
`enable_video_understanding` | Разрешить xAI анализировать видео, прикрепленные к найденным публикациям  
  
### Пример x_search

javascriptCopy code
[code]
    await x_search({  query: "dinner recipes",  allowed_x_handles: ["nytfood"],  from_date: "2026-03-01",});
[/code]

javascriptCopy code
[code]
    // Per-post stats: use the exact status URL or status ID when possibleawait x_search({  query: "https://x.com/huntharo/status/1905678901234567890",});
[/code]

## Примеры

javascriptCopy code
[code]
    // Basic searchawait web_search({ query: "OpenClaw plugin SDK" }); // German-specific searchawait web_search({ query: "TV online schauen", country: "DE", language: "de" }); // Recent results (past week)await web_search({ query: "AI developments", freshness: "week" }); // Date rangeawait web_search({  query: "climate research",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (Perplexity only)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],});
[/code]

## Профили инструментов

Если вы используете профили инструментов или списки разрешений, добавьте `web_search`, `x_search` или `group:web`:

json5Copy code
[code]
    {  tools: {    allow: ["web_search", "x_search"],    // or: allow: ["group:web"]  (includes web_search, x_search, and web_fetch)  },}
[/code]

## Связанные материалы

  * [Получение веб-страниц](</ru/tools/web-fetch>) \-- получить URL и извлечь читаемое содержимое
  * [Веб-браузер](</ru/tools/browser>) \-- полноценная автоматизация браузера для сайтов с активным использованием JS
  * [Поиск Grok](</ru/tools/grok-search>) \-- Grok как поставщик `web_search`
  * [Веб-поиск Ollama](</ru/tools/ollama-search>) \-- веб-поиск без ключей через ваш хост Ollama


Was this useful?YesNo

Open issue