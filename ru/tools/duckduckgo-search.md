---
title: Поиск DuckDuckGo
source_url: https://docs.openclaw.ai/ru/tools/duckduckgo-search
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw поддерживает DuckDuckGo как провайдер `web_search` **без ключа**. API-ключ или учетная запись не требуются.

## Настройка

API-ключ не нужен - просто укажите DuckDuckGo как провайдера:

* ### Настройка

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## Конфигурация

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Необязательные настройки уровня Plugin для региона и SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## Параметры инструмента

Поисковый запрос.

Количество результатов для возврата (1-10).

Код региона DuckDuckGo (например, `us-en`, `uk-en`, `de-de`).

Уровень SafeSearch.

Регион и SafeSearch также можно задать в конфигурации Plugin (см. выше) - параметры инструмента переопределяют значения конфигурации для каждого запроса.

## Примечания

  * **Без API-ключа** \- работает после выбора DuckDuckGo в качестве провайдера `web_search`
  * **Экспериментально** \- собирает результаты с HTML-страниц поиска DuckDuckGo без JavaScript, а не из официального API или SDK
  * **Риск бот-проверок** \- DuckDuckGo может показывать CAPTCHA или блокировать запросы при интенсивном или автоматизированном использовании
  * **Разбор HTML** \- результаты зависят от структуры страницы, которая может измениться без уведомления
  * **Явный выбор** \- OpenClaw не выбирает DuckDuckGo автоматически, если не настроен провайдер на основе API
  * **SafeSearch по умолчанию имеет значение moderate** , если не настроен


## См. также

  * [Обзор Web Search](</ru/tools/web>) \-- все провайдеры и автообнаружение
  * [Brave Search](</ru/tools/brave-search>) \-- структурированные результаты с бесплатным тарифом
  * [Exa Search](</ru/tools/exa-search>) \-- нейронный поиск с извлечением содержимого


Was this useful?YesNo

Open issue