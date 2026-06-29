---
title: Volcengine (Doubao)
source_url: https://docs.openclaw.ai/ru/providers/volcengine
scraped_at: 2026-06-29
---

ModelsProviders

Провайдер Volcengine предоставляет доступ к моделям Doubao и сторонним моделям, размещенным на Volcano Engine, с отдельными конечными точками для общих и кодовых рабочих нагрузок. Тот же встроенный Plugin также может зарегистрировать Volcengine Speech как провайдера TTS.

Сведения | Значение  
---|---  
Провайдеры | `volcengine` (общие + TTS) + `volcengine-plan` (кодовые)  
Аутентификация моделей | `VOLCANO_ENGINE_API_KEY`  
Аутентификация TTS | `VOLCENGINE_TTS_API_KEY` или `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | OpenAI-совместимые модели, BytePlus Seed Speech TTS  
  
## Начало работы

* ### Set the API key

Запустите интерактивную настройку:

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

Это регистрирует и общего (`volcengine`), и кодового (`volcengine-plan`) провайдеров с помощью одного API-ключа.

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## Провайдеры и конечные точки

Провайдер | Конечная точка | Сценарий использования  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | Общие модели  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | Кодовые модели  
  
## Встроенный каталог

### General (volcengine)

Ссылка на модель | Название | Ввод | Контекст  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | текст, изображение | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | текст, изображение | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | текст, изображение | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | текст, изображение | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | текст, изображение | 128,000  
  
### Coding (volcengine-plan)

Ссылка на модель | Название | Ввод | Контекст  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | текст | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | текст | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | текст | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | текст | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | текст | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | текст | 256,000  
  
## Преобразование текста в речь

Volcengine TTS использует HTTP API BytePlus Seed Speech и настраивается отдельно от API-ключа OpenAI-совместимых моделей Doubao. В консоли BytePlus откройте Seed Speech > Settings > API Keys и скопируйте API-ключ, затем задайте:

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

Затем включите его в `openclaw.json`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

Для целей с голосовыми заметками OpenClaw запрашивает у Volcengine нативный для провайдера `ogg_opus`. Для обычных аудиовложений он запрашивает `mp3`. Псевдонимы провайдера `bytedance` и `doubao` также указывают на того же провайдера речи.

Идентификатор ресурса по умолчанию — `seed-tts-1.0`, потому что именно его BytePlus выдает новым API-ключам Seed Speech в проекте по умолчанию. Если у вашего проекта есть право на TTS 2.0, задайте `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`.

Устаревшая аутентификация AppID/токен остается поддерживаемой для старых приложений Speech Console:

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## Расширенная конфигурация

Default model after onboarding

`openclaw onboard --auth-choice volcengine-api-key` сейчас задает `volcengine-plan/ark-code-latest` как модель по умолчанию, одновременно регистрируя общий каталог `volcengine`.

Model picker fallback behavior

Во время выбора модели при onboarding/configure вариант аутентификации Volcengine предпочитает строки `volcengine/*` и `volcengine-plan/*`. Если эти модели еще не загружены, OpenClaw откатывается к нефильтрованному каталогу вместо показа пустого средства выбора, ограниченного провайдером.

Environment variables for daemon processes

Если Gateway работает как daemon (launchd/systemd), убедитесь, что переменные окружения для моделей и TTS, такие как `VOLCANO_ENGINE_API_KEY`, `VOLCENGINE_TTS_API_KEY`, `BYTEPLUS_SEED_SPEECH_API_KEY`, `VOLCENGINE_TTS_APPID` и `VOLCENGINE_TTS_TOKEN`, доступны этому процессу (например, в `~/.openclaw/.env` или через `env.shellEnv`).

## Связанные материалы

[**Model selection** Выбор провайдеров, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Configuration** Полный справочник конфигурации для агентов, моделей и провайдеров. ](</ru/gateway/configuration>) [**Troubleshooting** Распространенные проблемы и шаги отладки. ](</ru/help/troubleshooting>) [**FAQ** Часто задаваемые вопросы о настройке OpenClaw. ](</ru/help/faq>)

Was this useful?YesNo

Open issue