---
title: Ollama Cloud
source_url: https://docs.openclaw.ai/uk/providers/ollama-cloud
scraped_at: 2026-06-29
---

ModelsProviders

Ollama Cloud — це розміщений API моделей від Ollama. Він дає OpenClaw змогу викликати моделі, розміщені в Ollama, напряму, без встановлення локального сервера Ollama або входу локального застосунку Ollama у хмарний режим. Використовуйте ідентифікатор постачальника `ollama-cloud` і посилання на моделі на кшталт `ollama-cloud/kimi-k2.6`.

Ця сторінка призначена для прямої маршрутизації лише через хмару. Постачальник використовує рідний стиль Ollama `/api/chat`, а не OpenAI-сумісний маршрут `/v1`. OpenClaw реєструє його як окремий ідентифікатор постачальника, щоб облікові дані лише для хмари, виявлення живого каталогу та вибір моделі не змішувалися з локальним хостом `ollama`.

Використовуйте цю сторінку, коли потрібна маршрутизація лише через хмару. Для локального Ollama, гібридної маршрутизації хмара-плюс-локально, embeddings і деталей власного хоста див. [Ollama](</uk/providers/ollama>).

## Налаштування

Створіть API-ключ Ollama Cloud на [ollama.com/settings/keys](<https://ollama.com/settings/keys>), а потім виконайте:

bashCopy code
[code]
    openclaw onboard --auth-choice ollama-cloud
[/code]

Або задайте:

bashCopy code
[code]
    export OLLAMA_API_KEY="<your-ollama-cloud-api-key>" # pragma: allowlist secret
[/code]

## Типові значення

  * Постачальник: `ollama-cloud`
  * Базова URL-адреса: `https://ollama.com`
  * Змінна середовища: `OLLAMA_API_KEY`
  * Стиль API: рідний Ollama `/api/chat`
  * Приклад моделі: `ollama-cloud/kimi-k2.6`


## Коли обирати Ollama Cloud

  * Вам потрібні розміщені моделі Ollama без локального запуску `ollama serve`.
  * Вам потрібна та сама рідна форма API чату Ollama, яку OpenClaw використовує для локального Ollama, але спрямована на `https://ollama.com`.
  * Вам потрібен простий хмарний шлях для моделей, які вже є в розміщеному каталозі Ollama.
  * Вам не потрібні локальні завантаження моделей, локальне керування GPU або інференс лише через LAN.


Натомість використовуйте [Ollama](</uk/providers/ollama>), коли потрібна маршрутизація лише локально або хмара-плюс-локально через хост Ollama з виконаним входом. Використовуйте OpenAI-сумісного постачальника, коли потрібна семантика `/v1/chat/completions` або специфічні для постачальника OpenAI-стильові можливості.

## Моделі

OpenClaw виявляє моделі Ollama Cloud із живого розміщеного каталогу. Поширені доступні розміщені ідентифікатори включають:

  * `ollama-cloud/gpt-oss:20b`
  * `ollama-cloud/kimi-k2.6`
  * `ollama-cloud/deepseek-v4-flash`
  * `ollama-cloud/minimax-m2.7`
  * `ollama-cloud/glm-5`


Використовуйте ідентифікатор моделі з вашого поточного розміщеного каталогу:

bashCopy code
[code]
    openclaw models list --provider ollama-cloudopenclaw models set ollama-cloud/kimi-k2.6
[/code]

Ідентифікатори моделей — це ідентифікатори хмарного каталогу, а не назви локального pull. Якщо назва моделі працює на локальному хості Ollama, але відсутня в розміщеному каталозі, натомість використовуйте постачальника `ollama` з цим локальним хостом.

## Живий тест

Для smoke-тестів Ollama Cloud з API-ключем спрямуйте живий тест Ollama на розміщену кінцеву точку та виберіть модель із вашого поточного каталогу:

bashCopy code
[code]
    export OLLAMA_API_KEY="<your-ollama-cloud-api-key>" # pragma: allowlist secret OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_OLLAMA=1 \OPENCLAW_LIVE_OLLAMA_BASE_URL=https://ollama.com \OPENCLAW_LIVE_OLLAMA_MODEL=kimi-k2.6 \OPENCLAW_LIVE_OLLAMA_WEB_SEARCH=1 \pnpm test:live -- extensions/ollama/ollama.live.test.ts
[/code]

Хмарний smoke-тест виконує текст, рідний stream і вебпошук. Він типово пропускає embeddings для `https://ollama.com`, тому що API-ключі Ollama Cloud можуть не авторизувати `/api/embed`.

## Усунення несправностей

  * Помилки `Set OLLAMA_API_KEY`: надайте справжній хмарний API-ключ. Локальний маркер `ollama-local` призначений лише для локальних або приватних хостів Ollama.
  * Помилки невідомої моделі: виконайте `openclaw models list --provider ollama-cloud` і точно скопіюйте ідентифікатор розміщеної моделі.
  * Проблеми з викликами інструментів або сирим JSON на власних хостах Ollama: перевірте, чи випадково не використовується OpenAI-сумісна URL-адреса `/v1`. Маршрути Ollama мають використовувати рідну базову URL-адресу без суфікса `/v1`.


## Пов’язане

  * [Ollama](</uk/providers/ollama>)
  * [Постачальники моделей](</uk/concepts/model-providers>)
  * [Усі постачальники](</uk/providers>)


Was this useful?YesNo

Open issue