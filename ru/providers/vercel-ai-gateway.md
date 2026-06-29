---
title: Vercel AI Gateway
source_url: https://docs.openclaw.ai/ru/providers/vercel-ai-gateway
scraped_at: 2026-06-29
---

ModelsProviders

[Vercel AI Gateway](<https://vercel.com/ai-gateway>) предоставляет единый API для доступа к сотням моделей через одну конечную точку.

Свойство | Значение  
---|---  
Поставщик | `vercel-ai-gateway`  
Пакет | `@openclaw/vercel-ai-gateway-provider`  
Аутентификация | `AI_GATEWAY_API_KEY`  
API | Совместим с Anthropic Messages  
Каталог моделей | Автоматически обнаруживается через `/v1/models`  
  
## Начало работы

* ### Установите Plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/vercel-ai-gateway-provider
[/code]

* ### Задайте ключ API

Запустите первичную настройку и выберите вариант аутентификации AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Задайте модель по умолчанию

Добавьте модель в конфигурацию OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Проверьте, что модель доступна

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Неинтерактивный пример

Для сценариев или настроек CI передайте все значения в командной строке:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Сокращенная запись ID модели

OpenClaw принимает сокращенные ссылки на модели Vercel Claude и нормализует их во время выполнения:

Сокращенный ввод | Нормализованная ссылка на модель  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Расширенная конфигурация

Переменная окружения для фоновых процессов

Если OpenClaw Gateway работает как фоновый процесс (launchd/systemd), убедитесь, что `AI_GATEWAY_API_KEY` доступен этому процессу.

Маршрутизация поставщика

Vercel AI Gateway направляет запросы вышестоящему поставщику на основе префикса ссылки на модель. Например, `vercel-ai-gateway/anthropic/claude-opus-4.6` направляется через Anthropic, а `vercel-ai-gateway/openai/gpt-5.5` направляется через OpenAI и `vercel-ai-gateway/moonshotai/kimi-k2.6` направляется через MoonshotAI. Единый `AI_GATEWAY_API_KEY` обрабатывает аутентификацию для всех вышестоящих поставщиков.

Уровни Thinking

Параметры `/think` следуют доверенным префиксам вышестоящих моделей, когда OpenClaw знает контракт вышестоящего поставщика. `vercel-ai-gateway/anthropic/...` использует профиль thinking Claude, включая адаптивные значения по умолчанию для моделей Claude 4.6. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5` и ссылки в стиле Codex предоставляют `/think xhigh` так же, как прямые поставщики OpenAI/OpenAI Codex. Другие ссылки с пространствами имен сохраняют обычные уровни рассуждения, если их метаданные каталога не объявляют больше.

## См. также

[**Выбор модели** Выбор поставщиков, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Устранение неполадок** Общее устранение неполадок и часто задаваемые вопросы. ](</ru/help/troubleshooting>)

Was this useful?YesNo

Open issue