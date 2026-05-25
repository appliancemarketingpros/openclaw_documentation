---
title: Пошук Brave
source_url: https://docs.openclaw.ai/uk/tools/brave-search
scraped_at: 2026-05-25
---

OpenClaw підтримує Brave Search API як провайдера `web_search`.

## Отримання API-ключа

  1. Створіть обліковий запис Brave Search API на <https://brave.com/search/api/>
  2. На панелі керування виберіть план **Search** і згенеруйте API-ключ.
  3. Збережіть ключ у конфігурації або задайте `BRAVE_API_KEY` у середовищі Gateway.


## Приклад конфігурації

json5Copy code
[code]
    {  plugins: {    entries: {      brave: {        config: {          webSearch: {            apiKey: "BRAVE_API_KEY_HERE",            mode: "web", // or "llm-context"            baseUrl: "https://api.search.brave.com", // optional proxy/base URL override          },        },      },    },  },  tools: {    web: {      search: {        provider: "brave",        maxResults: 5,        timeoutSeconds: 30,      },    },  },}
[/code]

Налаштування пошуку Brave, специфічні для провайдера, тепер розміщуються в `plugins.entries.brave.config.webSearch.*`. Застарілий `tools.web.search.apiKey` досі завантажується через shim сумісності, але це більше не канонічний шлях конфігурації.

`webSearch.mode` керує транспортом Brave:

  * `web` (за замовчуванням): звичайний вебпошук Brave із заголовками, URL-адресами та фрагментами
  * `llm-context`: Brave LLM Context API із попередньо витягнутими текстовими фрагментами та джерелами для обґрунтування


`webSearch.baseUrl` може спрямовувати запити Brave до довіреного Brave-сумісного проксі або gateway. OpenClaw додає `/res/v1/web/search` або `/res/v1/llm/context` до налаштованої базової URL-адреси та зберігає базову URL-адресу в ключі кешу. Публічні кінцеві точки мають використовувати `https://`; `http://` приймається лише для довірених loopback або проксі-хостів приватної мережі.

## Параметри інструмента

Пошуковий запит.

Кількість результатів для повернення (1–10).

2-літерний код країни ISO (наприклад, `US`, `DE`).

Код мови ISO 639-1 для результатів пошуку (наприклад, `en`, `de`, `fr`).

Код мови пошуку Brave (наприклад, `en`, `en-gb`, `zh-hans`).

Код мови ISO для елементів інтерфейсу.

Фільтр часу — `day` означає 24 години.

Лише результати, опубліковані після цієї дати (`YYYY-MM-DD`).

Лише результати, опубліковані до цієї дати (`YYYY-MM-DD`).

**Приклади:**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",});
[/code]

## Примітки

  * OpenClaw використовує план Brave **Search**. Якщо у вас є застаріла підписка (наприклад, початковий безплатний план із 2 000 запитів на місяць), вона залишається чинною, але не включає новіші функції, як-от LLM Context або вищі ліміти частоти запитів.
  * Кожен план Brave включає **$5/місяць безплатного кредиту** (з поновленням). План Search коштує $5 за 1 000 запитів, тож кредит покриває 1 000 запитів на місяць. Установіть ліміт використання на панелі керування Brave, щоб уникнути неочікуваних витрат. Поточні плани дивіться на [порталі Brave API](<https://brave.com/search/api/>).
  * План Search включає кінцеву точку LLM Context і права на AI-виведення. Зберігання результатів для навчання або налаштування моделей потребує плану з явними правами на зберігання. Дивіться [Умови надання послуг](<https://api-dashboard.search.brave.com/terms-of-service>) Brave.
  * Режим `llm-context` повертає обґрунтовані записи джерел замість звичайної форми фрагментів вебпошуку.
  * Режим `llm-context` підтримує `freshness` і обмежені діапазони `date_after` \+ `date_before`. Він не підтримує `ui_lang`; `date_before` без `date_after` відхиляється, оскільки Brave вимагає, щоб користувацькі діапазони свіжості містили і початкову, і кінцеву дати.
  * `ui_lang` має містити підтег регіону, як-от `en-US`.
  * Результати кешуються за замовчуванням на 15 хвилин (налаштовується через `cacheTtlMinutes`).
  * Користувацькі значення `webSearch.baseUrl` включаються в ідентичність кешу Brave, тому відповіді, специфічні для проксі, не конфліктують.
  * Увімкніть діагностичний прапорець `brave.http`, щоб під час усунення несправностей журналювати URL-адреси/параметри запитів Brave, стан/час відповіді та події влучання/промаху/запису пошукового кешу. Прапорець ніколи не журналює API-ключ або тіла відповідей, але пошукові запити можуть бути конфіденційними.


## Пов’язане

  * [Огляд вебпошуку](</uk/tools/web>) \-- усі провайдери та автовиявлення
  * [Пошук Perplexity](</uk/tools/perplexity-search>) \-- структуровані результати з фільтрацією за доменами
  * [Пошук Exa](</uk/tools/exa-search>) \-- нейронний пошук із витягуванням вмісту


Was this useful?YesNo