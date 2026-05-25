---
title: Cloudflare AI gateway
source_url: https://docs.openclaw.ai/uk/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway розташовується перед API постачальників і дає змогу додавати аналітику, кешування та елементи керування. Для Anthropic OpenClaw використовує Anthropic Messages API через вашу кінцеву точку Gateway.

Властивість | Значення  
---|---  
Постачальник | `cloudflare-ai-gateway`  
Базова URL | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Модель за замовчуванням | `cloudflare-ai-gateway/claude-sonnet-4-6`  
Ключ API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (ваш ключ API постачальника для запитів через Gateway)  
  
Коли для моделей Anthropic Messages увімкнено thinking, OpenClaw видаляє кінцеві попередньо заповнені ходи assistant перед надсиланням корисного навантаження через Cloudflare AI Gateway. Anthropic відхиляє попереднє заповнення відповіді з extended thinking, тоді як звичайне попереднє заповнення без thinking залишається доступним.

## Початок роботи

* ### Задайте ключ API постачальника та дані Gateway

Запустіть онбординг і виберіть варіант автентифікації Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Буде запропоновано ввести ID вашого облікового запису, ID Gateway і ключ API.

* ### Задайте модель за замовчуванням

Додайте модель до конфігурації OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Неінтерактивний приклад

Для сценаріїв або налаштувань CI передайте всі значення в командному рядку:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Розширена конфігурація

Автентифіковані gateway

Якщо ви ввімкнули автентифікацію Gateway у Cloudflare, додайте заголовок `cf-aig-authorization`. Це **додатково до** вашого ключа API постачальника.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Примітка щодо середовища

Якщо Gateway працює як демон (launchd/systemd), переконайтеся, що `CLOUDFLARE_AI_GATEWAY_API_KEY` доступний для цього процесу.

## Пов’язане

[**Вибір моделі** Вибір постачальників, посилань на моделі та поведінки перемикання при збої. ](</uk/concepts/model-providers>) [**Усунення несправностей** Загальне усунення несправностей і поширені запитання. ](</uk/help/troubleshooting>)

Was this useful?YesNo