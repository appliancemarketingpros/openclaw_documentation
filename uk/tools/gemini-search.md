---
title: Пошук Gemini
source_url: https://docs.openclaw.ai/uk/tools/gemini-search
scraped_at: 2026-05-25
---

OpenClaw підтримує моделі Gemini з вбудованою [прив’язкою до Google Search](<https://ai.google.dev/gemini-api/docs/grounding>), яка повертає синтезовані ШІ відповіді на основі актуальних результатів Google Search із цитуваннями.

## Отримання API-ключа

* ### Створіть ключ

Перейдіть до [Google AI Studio](<https://aistudio.google.com/apikey>) і створіть API-ключ.

* ### Збережіть ключ

Задайте `GEMINI_API_KEY` у середовищі Gateway, повторно використайте `models.providers.google.apiKey` або налаштуйте окремий ключ для вебпошуку через:

bashCopy code
[code]
    openclaw configure --section web
[/code]

## Конфігурація

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // optional; falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash", // default          },        },      },    },  },  tools: {    web: {      search: {        provider: "gemini",      },    },  },}
[/code]

**Пріоритет облікових даних:** вебпошук Gemini спочатку використовує `plugins.entries.google.config.webSearch.apiKey`, потім `GEMINI_API_KEY`, а тоді `models.providers.google.apiKey`. Для базових URL окреме значення `plugins.entries.google.config.webSearch.baseUrl` має пріоритет перед `models.providers.google.baseUrl`.

Для встановлення Gateway розмістіть ключі середовища в `~/.openclaw/.env`.

## Як це працює

На відміну від традиційних пошукових провайдерів, які повертають список посилань і фрагментів, Gemini використовує прив’язку до Google Search, щоб створювати синтезовані ШІ відповіді з вбудованими цитуваннями. Результати містять і синтезовану відповідь, і вихідні URL.

  * URL цитувань із прив’язки Gemini автоматично перетворюються з URL перенаправлення Google на прямі URL.
  * Розв’язання перенаправлень використовує шлях захисту від SSRF (HEAD + перевірки перенаправлень + перевірка http/https), перш ніж повернути фінальний URL цитування.
  * Розв’язання перенаправлень використовує суворі стандартні налаштування SSRF, тому перенаправлення на приватні/внутрішні цілі блокуються.


## Підтримувані параметри

Пошук Gemini підтримує `query`, `freshness`, `date_after` і `date_before`.

`count` приймається для сумісності зі спільним `web_search`, але прив’язка Gemini усе одно повертає одну синтезовану відповідь із цитуваннями, а не список із N результатів.

`freshness` приймає `day`, `week`, `month`, `year` і спільні скорочення `pd`, `pw`, `pm` та `py`. OpenClaw перетворює ці значення або явний діапазон `date_after`/`date_before` на `timeRangeFilter` для прив’язки Gemini Google Search. `country`, `language` і `domain_filter` не підтримуються.

## Вибір моделі

Стандартна модель — `gemini-2.5-flash` (швидка та економічна). Будь-яку модель Gemini, що підтримує прив’язку, можна використовувати через `plugins.entries.google.config.webSearch.model`.

## Перевизначення базового URL

Задайте `plugins.entries.google.config.webSearch.baseUrl`, коли вебпошук Gemini має проходити через проксі оператора або користувацький Gemini-сумісний endpoint. Якщо це значення не задано, вебпошук Gemini повторно використовує `models.providers.google.baseUrl`. Звичайне значення `https://generativelanguage.googleapis.com` нормалізується до `https://generativelanguage.googleapis.com/v1beta`; користувацькі шляхи проксі зберігаються як надано після обрізання кінцевих скісних рисок.

## Пов’язане

  * [Огляд вебпошуку](</uk/tools/web>) \-- усі провайдери й автоматичне виявлення
  * [Brave Search](</uk/tools/brave-search>) \-- структуровані результати з фрагментами
  * [Perplexity Search](</uk/tools/perplexity-search>) \-- структуровані результати + витягування вмісту


Was this useful?YesNo