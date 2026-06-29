---
title: Паралельний пошук
source_url: https://docs.openclaw.ai/uk/tools/parallel-search
scraped_at: 2026-06-29
---

CapabilitiesTools

Plugin Parallel надає два провайдери `web_search` для [Parallel](<https://parallel.ai/>):

  * **Parallel Search (Free)** (`parallel-free`) -- безкоштовний [Search MCP](<https://docs.parallel.ai/integrations/mcp/search-mcp>) від Parallel. Не потребує облікового запису або API-ключа. Вибирайте його явно, коли потрібен розміщений у Parallel шлях пошуку без ключа.
  * **Parallel Search** (`parallel`) -- платний Search API від Parallel. Потребує `PARALLEL_API_KEY` і пропонує вищі ліміти частоти та налаштування цілі.


Обидва повертають ранжовані, оптимізовані для LLM уривки з вебіндексу, створеного для AI-агентів. Установіть `tools.web.search.provider` на `parallel-free` або `parallel`, щоб явно вибрати один із них.

## Встановлення Plugin

Встановіть офіційний Plugin, потім перезапустіть Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/parallel-pluginopenclaw gateway restart
[/code]

## API-ключ (платний провайдер)

`parallel-free` не потребує API-ключа, але його все одно потрібно вибрати як керований провайдер. Платному провайдеру `parallel` потрібен API-ключ:

* ### Create an account

Зареєструйтеся на [platform.parallel.ai](<https://platform.parallel.ai>) і згенеруйте API-ключ у своїй панелі керування.

* ### Store the key

Установіть `PARALLEL_API_KEY` у середовищі Gateway або налаштуйте через:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Конфігурація

json5Copy code
[code]
    {  plugins: {    entries: {      parallel: {        config: {          webSearch: {            apiKey: "par-...", // optional if PARALLEL_API_KEY is set            baseUrl: "https://api.parallel.ai", // optional; OpenClaw appends /v1/search          },        },      },    },  },  tools: {    web: {      search: {        // Use "parallel-free" for the free Search MCP, or "parallel" for        // the paid API-backed provider shown here.        provider: "parallel",      },    },  },}
[/code]

**Альтернатива через середовище:** установіть `PARALLEL_API_KEY` у середовищі Gateway. Для встановлення gateway розмістіть його в `~/.openclaw/.env`.

## Перевизначення базової URL-адреси

Перевизначення базової URL-адреси застосовується лише до платного провайдера `parallel`. Безкоштовний провайдер `parallel-free` завжди використовує `https://search.parallel.ai/mcp`.

Установіть `plugins.entries.parallel.config.webSearch.baseUrl`, коли запити Parallel мають проходити через сумісний проксі або альтернативну кінцеву точку Parallel (наприклад, Cloudflare AI Gateway). OpenClaw нормалізує голі хости, додаючи `https://` на початок, і додає `/v1/search`, якщо шлях ще не закінчується так. Розв’язана кінцева точка включається до ключа кешу пошуку, тому результати з різних кінцевих точок Parallel не спільно використовуються.

## Параметри інструмента

OpenClaw надає нативну форму пошуку Parallel, щоб модель могла заповнити і ціль природною мовою, і кілька коротких ключових запитів — поєднання, яке Parallel [рекомендує](<https://docs.parallel.ai/search/best-practices>) для найкращих результатів.

Опис базового запитання або цілі природною мовою (максимум 5000 символів). Має бути самодостатнім.

Стислі ключові пошукові запити, по 3-6 слів кожен (1-5 записів, максимум 200 символів кожен). Надайте 2-3 різноманітні запити для найкращих результатів.

Кількість результатів для повернення (1-40).

Необов’язковий ідентифікатор сесії Parallel (максимум 1000 символів для `parallel`; безкоштовний Search MCP `parallel-free` обмежує його до 100). Передавайте `sessionId` із попереднього результату Parallel у подальших пошуках, що є частиною того самого завдання, щоб Parallel міг групувати пов’язані виклики та покращувати наступні результати. Ідентифікатор, що перевищує ліміт, відкидається, і генерується новий.

Необов’язковий ідентифікатор моделі, яка виконує виклик (наприклад, `claude-opus-4-7`, `gpt-5.5`). Дає Parallel змогу адаптувати стандартні налаштування до можливостей вашої моделі. Передавайте точний slug активної моделі; не скорочуйте його до псевдоніма сімейства.

## Примітки

  * Parallel ранжує та стискає результати на основі корисності для міркування LLM, а не людських переходів за кліками; очікуйте щільних уривків у кожному результаті замість вмісту повної сторінки
  * Уривки результатів повертаються як масив `excerpts` і також об’єднуються в поле `description` для сумісності із загальним контрактом `web_search`
  * Parallel повертає `session_id` у кожній відповіді; OpenClaw надає його як `sessionId` у payload інструмента, щоб викликачі могли групувати подальші пошуки
  * `searchId`, `warnings` і `usage` від Parallel передаються далі, коли вони присутні
  * OpenClaw завжди передає розв’язану кількість результатів до Parallel як `advanced_settings.max_results`. Аргумент `count` викликача має пріоритет, потім налаштування верхнього рівня `tools.web.search.maxResults`, інакше використовується стандартне значення OpenClaw для загального `web_search` (5). Це підтримує узгоджений обсяг результатів під час перемикання між провайдерами; сам Parallel за замовчуванням використовує 10
  * Результати кешуються за замовчуванням на 15 хвилин (налаштовується через `cacheTtlMinutes`)
  * Безкоштовний провайдер `parallel-free` приймає ті самі параметри. Він застосовує `count` на стороні клієнта та генерує `session_id` для кожного виклику, якщо його не надано.


## Пов’язане

  * [Огляд Web Search](</uk/tools/web>) \-- усі провайдери й автоматичне виявлення
  * [Пошук Exa](</uk/tools/exa-search>) \-- нейронний пошук із витягненням вмісту
  * [Пошук Perplexity](</uk/tools/perplexity-search>) \-- структуровані результати з фільтрацією доменів


Was this useful?YesNo

Open issue