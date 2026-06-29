---
title: Chutes
source_url: https://docs.openclaw.ai/ru/providers/chutes
scraped_at: 2026-06-29
---

ModelsProviders

[Chutes](<https://chutes.ai>) предоставляет каталоги open-source моделей через API, совместимый с OpenAI. OpenClaw поддерживает как браузерный OAuth, так и аутентификацию напрямую по API-ключу для провайдера `chutes`.

Свойство | Значение  
---|---  
Провайдер | `chutes`  
API | совместимый с OpenAI  
Базовый URL | `https://llm.chutes.ai/v1`  
Аутентификация | OAuth или API-ключ (см. ниже)  
  
## Установка Plugin

Установите официальный Plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/chutes-provideropenclaw gateway restart
[/code]

## Начало работы

### OAuth

* ### Run the OAuth onboarding flow

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw запускает браузерный поток локально или показывает поток с URL + вставкой redirect на удаленных/headless хостах. OAuth-токены автоматически обновляются через профили аутентификации OpenClaw.

* ### Verify the default model

После онбординга модель по умолчанию задается как `chutes/zai-org/GLM-4.7-TEE`, а статический каталог Chutes регистрируется.

### API key

* ### Get an API key

Создайте ключ на [chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>).

* ### Run the API key onboarding flow

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Verify the default model

После онбординга модель по умолчанию задается как `chutes/zai-org/GLM-4.7-TEE`, а статический каталог Chutes регистрируется.

## Поведение обнаружения

Когда аутентификация Chutes доступна, OpenClaw запрашивает каталог Chutes с этими учетными данными и использует обнаруженные модели. Если обнаружение завершается сбоем, OpenClaw возвращается к статическому каталогу, чтобы онбординг и запуск по-прежнему работали.

## Псевдонимы по умолчанию

OpenClaw регистрирует три удобных псевдонима для статического каталога Chutes:

Псевдоним | Целевая модель  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## Встроенный стартовый каталог

Статический резервный каталог включает текущие ссылки Chutes:

Ссылка модели  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## Пример конфигурации

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

OAuth overrides

Вы можете настроить поток OAuth с помощью необязательных переменных окружения:

Переменная | Назначение  
---|---  
`CHUTES_CLIENT_ID` | Пользовательский ID OAuth-клиента  
`CHUTES_CLIENT_SECRET` | Пользовательский секрет OAuth-клиента  
`CHUTES_OAUTH_REDIRECT_URI` | Пользовательский URI перенаправления  
`CHUTES_OAUTH_SCOPES` | Пользовательские области OAuth  
  
См. [документацию Chutes OAuth](<https://chutes.ai/docs/sign-in-with-chutes/overview>) для требований к приложению перенаправления и справки.

Notes

  * Обнаружение по API-ключу и OAuth использует один и тот же id провайдера `chutes`.
  * Модели Chutes регистрируются как `chutes/<model-id>`.
  * Если обнаружение при запуске завершается сбоем, статический каталог используется автоматически.


## Связанные материалы

[**Model selection** Правила провайдеров, ссылки моделей и поведение failover. ](</ru/concepts/model-providers>) [**Configuration reference** Полная схема конфигурации, включая настройки провайдера. ](</ru/gateway/configuration-reference>) [**Chutes** Панель управления Chutes и документация API. ](<https://chutes.ai>) [**Chutes API keys** Создавайте API-ключи Chutes и управляйте ими. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo

Open issue