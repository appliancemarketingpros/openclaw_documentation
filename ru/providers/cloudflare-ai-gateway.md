---
title: Gateway ИИ Cloudflare
source_url: https://docs.openclaw.ai/ru/providers/cloudflare-ai-gateway
scraped_at: 2026-06-29
---

ModelsProviders

Cloudflare AI Gateway находится перед API провайдеров и позволяет добавлять аналитику, кеширование и средства управления. Для Anthropic OpenClaw использует Anthropic Messages API через вашу конечную точку Gateway.

Свойство | Значение  
---|---  
Провайдер | `cloudflare-ai-gateway`  
Базовый URL | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Модель по умолчанию | `cloudflare-ai-gateway/claude-sonnet-4-6`  
Ключ API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (ваш ключ API провайдера для запросов через Gateway)  
  
Когда для моделей Anthropic Messages включен режим мышления, OpenClaw удаляет завершающие предзаполненные ходы ассистента перед отправкой полезной нагрузки через Cloudflare AI Gateway. Anthropic отклоняет предзаполнение ответов при расширенном мышлении, тогда как обычное предзаполнение без мышления остается доступным.

## Установка Plugin

Установите официальный Plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cloudflare-ai-gateway-provideropenclaw gateway restart
[/code]

## Начало работы

* ### Задайте ключ API провайдера и сведения Gateway

Запустите онбординг и выберите вариант аутентификации Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Будет запрошен ваш идентификатор учетной записи, идентификатор gateway и ключ API.

* ### Задайте модель по умолчанию

Добавьте модель в конфигурацию OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Проверьте, что модель доступна

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Неинтерактивный пример

Для скриптовых или CI-настроек передайте все значения в командной строке:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Расширенная конфигурация

Аутентифицированные gateway

Если вы включили аутентификацию Gateway в Cloudflare, добавьте заголовок `cf-aig-authorization`. Это **дополнение к** вашему ключу API провайдера.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Примечание об окружении

Если Gateway работает как демон (launchd/systemd), убедитесь, что `CLOUDFLARE_AI_GATEWAY_API_KEY` доступен этому процессу.

## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Устранение неполадок** Общие сведения об устранении неполадок и часто задаваемые вопросы. ](</ru/help/troubleshooting>)

Was this useful?YesNo

Open issue