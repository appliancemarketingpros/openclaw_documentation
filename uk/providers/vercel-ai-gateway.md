---
title: Gateway Vercel AI
source_url: https://docs.openclaw.ai/uk/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

[Vercel AI Gateway](<https://vercel.com/ai-gateway>) надає уніфікований API для доступу до сотень моделей через одну кінцеву точку.

Властивість | Значення  
---|---  
Провайдер | `vercel-ai-gateway`  
Автентифікація | `AI_GATEWAY_API_KEY`  
API | сумісний з Anthropic Messages  
Каталог моделей | автоматично виявляється через `/v1/models`  
  
## Початок роботи

* ### Установіть ключ API

Запустіть початкове налаштування й виберіть опцію автентифікації AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Установіть модель за замовчуванням

Додайте модель до конфігурації OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Неінтерактивний приклад

Для скриптів або налаштувань CI передайте всі значення в командному рядку:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Скорочення ID моделі

OpenClaw приймає скорочені посилання на моделі Vercel Claude і нормалізує їх під час виконання:

Скорочене введення | Нормалізоване посилання на модель  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Розширена конфігурація

Змінна середовища для процесів демона

Якщо OpenClaw Gateway працює як демон (launchd/systemd), переконайтеся, що `AI_GATEWAY_API_KEY` доступний цьому процесу.

Маршрутизація провайдера

Vercel AI Gateway спрямовує запити до вихідного провайдера на основі префікса посилання на модель. Наприклад, `vercel-ai-gateway/anthropic/claude-opus-4.6` спрямовується через Anthropic, тоді як `vercel-ai-gateway/openai/gpt-5.5` спрямовується через OpenAI, а `vercel-ai-gateway/moonshotai/kimi-k2.6` спрямовується через MoonshotAI. Ваш єдиний `AI_GATEWAY_API_KEY` обробляє автентифікацію для всіх вихідних провайдерів.

Рівні мислення

Параметри `/think` відповідають довіреним префіксам вихідних моделей, коли OpenClaw знає контракт вихідного провайдера. `vercel-ai-gateway/anthropic/...` використовує профіль мислення Claude, зокрема адаптивні значення за замовчуванням для моделей Claude 4.6. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5` і посилання в стилі Codex надають `/think xhigh` так само, як прямі провайдери OpenAI/OpenAI Codex. Інші просторово іменовані посилання зберігають звичайні рівні міркування, якщо їхні метадані каталогу не оголошують більше.

## Пов’язане

[**Вибір моделі** Вибір провайдерів, посилань на моделі та поведінки відмовостійкості. ](</uk/concepts/model-providers>) [**Усунення несправностей** Загальне усунення несправностей і поширені запитання. ](</uk/help/troubleshooting>)

Was this useful?YesNo