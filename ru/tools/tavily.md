---
title: Tavily
source_url: https://docs.openclaw.ai/ru/tools/tavily
scraped_at: 2026-06-29
---

CapabilitiesTools

[Tavily](<https://tavily.com>) — это поисковый API, созданный для AI-приложений. OpenClaw предоставляет его двумя способами:

  * как provider `web_search` для общего инструмента поиска
  * как явные инструменты Plugin: `tavily_search` и `tavily_extract`


Tavily возвращает структурированные результаты, оптимизированные для потребления LLM, с настраиваемой глубиной поиска, фильтрацией по темам, фильтрами доменов, AI-сгенерированными сводками ответов и извлечением контента из URL-адресов (включая страницы, отрисованные JavaScript).

Свойство | Значение  
---|---  
ID Plugin | `tavily`  
Пакет | `@openclaw/tavily-plugin`  
Auth | `TAVILY_API_KEY` или config `apiKey`  
Базовый URL | `https://api.tavily.com` (по умолчанию)  
Инструменты | `tavily_search`, `tavily_extract`  
  
## Начало работы

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/tavily-plugin
[/code]

* ### Get an API key

Создайте учетную запись Tavily на [tavily.com](<https://tavily.com>), затем сгенерируйте API-ключ на панели управления.

* ### Configure the plugin and provider

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### Verify search runs

Запустите `web_search` из любого агента или вызовите `tavily_search` напрямую.

## Справочник инструментов

### `tavily_search`

Используйте это, когда нужны специфичные для Tavily элементы управления поиском вместо общего `web_search`.

Параметр | Тип | Ограничения / значение по умолчанию | Описание  
---|---|---|---  
`query` | string | обязательно | Строка поискового запроса. Не более 400 символов.  
`search_depth` | enum | `basic` (по умолчанию), `advanced` | `advanced` медленнее, но дает более высокую релевантность.  
`topic` | enum | `general` (по умолчанию), `news`, `finance` | Фильтрация по семейству тем.  
`max_results` | integer | 1-20 | Количество результатов.  
`include_answer` | boolean | по умолчанию `false` | Включить AI-сгенерированную сводку ответа Tavily.  
`time_range` | enum | `day`, `week`, `month`, `year` | Фильтровать результаты по давности.  
`include_domains` | string array | (нет) | Включать результаты только с этих доменов.  
`exclude_domains` | string array | (нет) | Исключать результаты с этих доменов.  
  
Компромисс глубины поиска:

Глубина | Скорость | Релевантность | Лучше всего для  
---|---|---|---  
`basic` | Быстрее | Высокая | Запросы общего назначения (по умолчанию).  
`advanced` | Медленнее | Самая высокая | Точные исследования и поиск фактов.  
  
### `tavily_extract`

Используйте это для извлечения чистого контента из одного или нескольких URL-адресов. Обрабатывает страницы, отрисованные JavaScript, и поддерживает разбиение на фрагменты с учетом запроса для целевого извлечения.

Параметр | Тип | Ограничения / значение по умолчанию | Описание  
---|---|---|---  
`urls` | string array | обязательно, 1-20 | URL-адреса, из которых нужно извлечь контент.  
`query` | string | (необязательно) | Повторно ранжировать извлеченные фрагменты по релевантности этому запросу.  
`extract_depth` | enum | `basic` (по умолчанию), `advanced` | Используйте `advanced` для страниц с большим объемом JS, SPA или динамических таблиц.  
`chunks_per_source` | integer | 1-5; **требует`query`** | Фрагменты, возвращаемые для каждого URL. Выдает ошибку, если задано без `query`.  
`include_images` | boolean | по умолчанию `false` | Включить URL-адреса изображений в результаты.  
  
Компромисс глубины извлечения:

Глубина | Когда использовать  
---|---  
`basic` | Простые страницы. Попробуйте сначала это.  
`advanced` | SPA, отрисованные JS, динамический контент, таблицы.  
  
## Выбор подходящего инструмента

Потребность | Инструмент  
---|---  
Быстрый веб-поиск без специальных параметров | `web_search`  
Поиск с глубиной, темой и AI-ответами | `tavily_search`  
Извлечение контента из конкретных URL | `tavily_extract`  
  
## Расширенная конфигурация

API key resolution order

Клиент Tavily ищет свой API-ключ в таком порядке:

  1. `plugins.entries.tavily.config.webSearch.apiKey` (разрешается через SecretRefs).
  2. `TAVILY_API_KEY` из окружения Gateway.


`tavily_extract` выдает ошибку настройки, если отсутствуют оба значения.

Custom base URL

Переопределите `plugins.entries.tavily.config.webSearch.baseUrl`, если вы проксируете Tavily. Значение по умолчанию — `https://api.tavily.com`.

`chunks_per_source` requires `query`

`tavily_extract` отклоняет вызовы, которые передают `chunks_per_source` без `query`. Tavily ранжирует фрагменты по релевантности запросу, поэтому без него параметр не имеет смысла.

## Связанные материалы

[**Web Search overview** Все providers и правила автообнаружения. ](</ru/tools/web>) [**Firecrawl** Поиск плюс scraping с извлечением контента. ](</ru/tools/firecrawl>) [**Exa Search** Нейронный поиск с извлечением контента. ](</ru/tools/exa-search>) [**Configuration** Полная схема config для записей Plugin и маршрутизации инструментов. ](</ru/gateway/configuration>)

Was this useful?YesNo

Open issue