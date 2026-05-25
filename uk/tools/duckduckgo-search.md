---
title: Пошук DuckDuckGo
source_url: https://docs.openclaw.ai/uk/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw підтримує DuckDuckGo як провайдера `web_search` **без ключа**. API ключ або обліковий запис не потрібні.

## Налаштування

API ключ не потрібен — просто встановіть DuckDuckGo як свого провайдера:

* ### Configure

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## Конфігурація

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

Додаткові налаштування рівня Plugin для регіону та SafeSearch:

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## Параметри інструмента

Пошуковий запит.

Кількість результатів для повернення (1-10).

Код регіону DuckDuckGo (наприклад, `us-en`, `uk-en`, `de-de`).

Рівень SafeSearch.

Регіон і SafeSearch також можна встановити в конфігурації Plugin (див. вище) — параметри інструмента перевизначають значення конфігурації для кожного запиту.

## Примітки

  * **Без API ключа** — працює одразу, без конфігурації
  * **Експериментально** — збирає результати з HTML-сторінок пошуку DuckDuckGo без JavaScript, а не з офіційного API чи SDK
  * **Ризик перевірки ботів** — DuckDuckGo може показувати CAPTCHA або блокувати запити за інтенсивного чи автоматизованого використання
  * **HTML-парсинг** — результати залежать від структури сторінки, яка може змінитися без попередження
  * **Порядок автовиявлення** — DuckDuckGo є першим резервним варіантом без ключа (порядок 100) в автовиявленні. Провайдери на основі API з налаштованими ключами запускаються першими, потім Ollama Web Search (порядок 110), потім SearXNG (порядок 200)
  * **SafeSearch за замовчуванням має рівень moderate** , якщо його не налаштовано


## Пов’язане

  * [Огляд Web Search](</uk/tools/web>) \-- усі провайдери та автовиявлення
  * [Brave Search](</uk/tools/brave-search>) \-- структуровані результати з безкоштовним рівнем
  * [Exa Search](</uk/tools/exa-search>) \-- нейронний пошук із витягуванням вмісту


Was this useful?YesNo