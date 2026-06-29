---
title: NovitaAI
source_url: https://docs.openclaw.ai/uk/providers/novita
scraped_at: 2026-06-29
---

ModelsProviders

NovitaAI — це постачальник розміщеної AI-інфраструктури з OpenAI-сумісним API моделей. В OpenClaw це вбудований постачальник моделей, тому ідентифікатор постачальника — `novita`, облікові дані проходять через звичайний потік автентифікації моделей, а посилання на моделі мають вигляд `novita/deepseek/deepseek-v3-0324`.

Використовуйте Novita, коли потрібен розміщений доступ до open-weight і сторонніх маршрутів моделей без запуску власного сервера інференсу. Вбудований каталог зосереджений на чат-моделях, практичних для ходів агента, зокрема на маршрутах DeepSeek, Moonshot, MiniMax, GLM і Qwen, які надає Novita.

Цей постачальник використовує OpenAI-сумісну кінцеву точку Novita. OpenClaw обробляє реєстрацію постачальника, автентифікацію, псевдоніми, нормалізацію посилань на моделі та вибір базової URL-адреси; Novita контролює поточну доступність моделей, дозволи облікового запису, ціни та обмеження швидкості.

## Налаштування

Створіть API-ключ на [novita.ai/settings/key-management](<https://novita.ai/settings/key-management>), а потім виконайте:

bashCopy code
[code]
    openclaw onboard --auth-choice novita-api-key
[/code]

Або задайте:

bashCopy code
[code]
    export NOVITA_API_KEY="<your-novita-api-key>" # pragma: allowlist secret
[/code]

## Типові значення

  * Постачальник: `novita`
  * Псевдоніми: `novita-ai`, `novitaai`
  * Базова URL-адреса: `https://api.novita.ai/openai/v1`
  * Змінна середовища: `NOVITA_API_KEY`
  * Типова модель: `novita/deepseek/deepseek-v3-0324`


## Коли обирати Novita

  * Вам потрібен розміщений доступ до open-weight моделей через OpenAI-сумісний API.
  * Вам потрібні маршрути DeepSeek, Kimi, MiniMax, GLM або сімейства Qwen через один обліковий запис постачальника.
  * Вам потрібен ще один розміщений резервний шлях поруч з OpenRouter, GMI, DeepInfra або прямими API постачальників.
  * Ви віддаєте перевагу хостингу моделей на боці постачальника замість підтримки інфраструктури vLLM, SGLang, LM Studio або Ollama.


Оберіть прямого постачальника, коли потрібні нативні для постачальника параметри запитів або контракти підтримки. Оберіть локального постачальника, коли модель має працювати на вашому власному обладнанні або за межею вашої власної мережі.

## Моделі

Вбудований каталог попередньо додає поширені ідентифікатори маршрутів NovitaAI, зокрема:

  * `novita/moonshotai/kimi-k2.5`
  * `novita/minimax/minimax-m2.7`
  * `novita/zai-org/glm-5`
  * `novita/deepseek/deepseek-v3-0324`
  * `novita/deepseek/deepseek-r1-0528`
  * `novita/qwen/qwen3-235b-a22b-fp8`


Каталог є початковою точкою для вибору моделей OpenClaw. Ваш обліковий запис, регіон або поточний каталог Novita можуть додавати, видаляти або обмежувати маршрути. Перевірте постачальника з CLI, перш ніж задавати довготривале типове значення:

bashCopy code
[code]
    openclaw models list --provider novita
[/code]

## Усунення несправностей

  * `401` або `403`: перевірте ключ на сторінці керування ключами Novita та повторно запустіть `openclaw onboard --auth-choice novita-api-key`, якщо збережений профіль застарів.
  * Помилки невідомої моделі: використовуйте точний `novita/<route-id>`, повернений командою `openclaw models list --provider novita`.
  * Повільні або невдалі маршрути: спробуйте інший маршрут моделі Novita або задайте Novita як резервного постачальника для навантажень, які можуть витримувати специфічну для постачальника варіативність.


## Пов’язане

  * [Постачальники моделей](</uk/concepts/model-providers>)
  * [Усі постачальники](</uk/providers>)


Was this useful?YesNo

Open issue