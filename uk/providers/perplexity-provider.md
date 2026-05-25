---
title: Perplexity
source_url: https://docs.openclaw.ai/uk/providers/perplexity-provider
scraped_at: 2026-05-25
---

Plugin Perplexity надає можливості вебпошуку через Perplexity Search API або Perplexity Sonar через OpenRouter.

Властивість | Значення  
---|---  
Тип | Провайдер вебпошуку (не провайдер моделей)  
Автентифікація | `PERPLEXITY_API_KEY` (напряму) або `OPENROUTER_API_KEY` (через OpenRouter)  
Шлях конфігурації | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Початок роботи

* ### Установіть API-ключ

Запустіть інтерактивний процес налаштування вебпошуку:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Або задайте ключ напряму:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Почніть пошук

Агент автоматично використовуватиме Perplexity для вебпошуку, щойно ключ буде налаштовано. Жодних додаткових кроків не потрібно.

## Режими пошуку

Plugin автоматично вибирає транспорт на основі префікса API-ключа:

### Нативний Perplexity API (pplx-)

Коли ваш ключ починається з `pplx-`, OpenClaw використовує нативний Perplexity Search API. Цей транспорт повертає структуровані результати й підтримує фільтри за доменом, мовою та датою (див. параметри фільтрації нижче).

### OpenRouter / Sonar (sk-or-)

Коли ваш ключ починається з `sk-or-`, OpenClaw маршрутизує запити через OpenRouter з використанням моделі Perplexity Sonar. Цей транспорт повертає відповіді, синтезовані ШІ, з цитуваннями.

Префікс ключа | Транспорт | Можливості  
---|---|---  
`pplx-` | Нативний Perplexity Search API | Структуровані результати, фільтри домену/мови/дати  
`sk-or-` | OpenRouter (Sonar) | Відповіді, синтезовані ШІ, з цитуваннями  
  
## Фільтрація нативного API

При використанні нативного Perplexity API пошук підтримує такі фільтри:

Фільтр | Опис | Приклад  
---|---|---  
Країна | 2-літерний код країни | `us`, `de`, `jp`  
Мова | Код мови ISO 639-1 | `en`, `fr`, `zh`  
Діапазон дат | Вікно давності | `day`, `week`, `month`, `year`  
Фільтри доменів | Allowlist або denylist (макс. 20 доменів) | `example.com`  
Бюджет вмісту | Ліміти токенів на відповідь / на сторінку | `max_tokens`, `max_tokens_per_page`  
  
## Розширене налаштування

Змінна середовища для процесів демона

Якщо Gateway OpenClaw працює як демон (launchd/systemd), переконайтеся, що `PERPLEXITY_API_KEY` доступний цьому процесу.

Налаштування проксі OpenRouter

Якщо ви хочете маршрутизувати пошуки Perplexity через OpenRouter, задайте `OPENROUTER_API_KEY` (префікс `sk-or-`) замість нативного ключа Perplexity. OpenClaw виявить префікс і автоматично переключиться на транспорт Sonar.

## Пов’язане

[**Інструмент пошуку Perplexity** Як агент викликає пошук Perplexity та інтерпретує результати. ](</uk/tools/perplexity-search>) [**Довідка з конфігурації** Повна довідка з конфігурації, включно із записами plugin. ](</uk/gateway/configuration-reference>)

Was this useful?YesNo