---
title: OpenRouter
source_url: https://docs.openclaw.ai/ru/providers/openrouter
scraped_at: 2026-06-29
---

ModelsProviders

OpenRouter предоставляет **унифицированный API** , который маршрутизирует запросы ко множеству моделей за одним endpoint и ключом API. Он совместим с OpenAI, поэтому большинство SDK OpenAI работают после смены базового URL.

## Начало работы

### OAuth

* ### Запустите OAuth-онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice openrouter-oauth
[/code]

OpenClaw открывает браузерный поток входа OpenRouter, обменивает код PKCE на ключ API OpenRouter и сохраняет этот ключ в стандартном профиле аутентификации OpenRouter. На удаленных/безголовых хостах OpenClaw печатает URL входа и просит вставить URL перенаправления после входа.

* ### (Необязательно) Переключитесь на конкретную модель

Онбординг по умолчанию использует `openrouter/auto`. Позже выберите конкретную модель:

bashCopy code
[code]
    openclaw models set openrouter/<provider>/<model>
[/code]

### Ключ API

* ### Получите ключ API

Создайте ключ API на [openrouter.ai/keys](<https://openrouter.ai/keys>).

* ### Запустите онбординг с ключом API

bashCopy code
[code]
    openclaw onboard --auth-choice openrouter-api-key
[/code]

* ### (Необязательно) Переключитесь на конкретную модель

Онбординг по умолчанию использует `openrouter/auto`. Позже выберите конкретную модель:

bashCopy code
[code]
    openclaw models set openrouter/<provider>/<model>
[/code]

## Пример конфигурации

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      model: { primary: "openrouter/auto" },    },  },}
[/code]

## Идентификаторы моделей

Встроенные резервные примеры:

Идентификатор модели | Примечания  
---|---  
`openrouter/auto` | Автоматическая маршрутизация OpenRouter  
`openrouter/openrouter/fusion` | Маршрутизатор OpenRouter Fusion  
`openrouter/moonshotai/kimi-k2.6` | Kimi K2.6 через MoonshotAI  
`openrouter/moonshotai/kimi-k2.5` | Kimi K2.5 через MoonshotAI  
  
## Генерация изображений

OpenRouter также может обслуживать инструмент `image_generate`. Используйте модель изображений OpenRouter в `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",        timeoutMs: 180_000,      },    },  },}
[/code]

OpenClaw отправляет запросы изображений в API изображений chat completions OpenRouter с `modalities: ["image", "text"]`. Модели изображений Gemini получают поддерживаемые подсказки `aspectRatio` и `resolution` через `image_config` OpenRouter. Используйте `agents.defaults.imageGenerationModel.timeoutMs` для более медленных моделей изображений OpenRouter; параметр `timeoutMs` для отдельного вызова инструмента `image_generate` по-прежнему имеет приоритет.

## Генерация видео

OpenRouter также может обслуживать инструмент `video_generate` через свой асинхронный API `/videos`. Используйте видеомодель OpenRouter в `agents.defaults.videoGenerationModel`:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      videoGenerationModel: {        primary: "openrouter/google/veo-3.1-fast",      },    },  },}
[/code]

OpenClaw отправляет задания text-to-video и image-to-video в OpenRouter, опрашивает возвращенный `polling_url` и скачивает готовое видео из `unsigned_urls` OpenRouter или документированного endpoint содержимого задания. Эталонные изображения по умолчанию отправляются как изображения первого/последнего кадра; изображения с тегом `reference_image` отправляются как входные ссылки OpenRouter. Встроенное значение по умолчанию `google/veo-3.1-fast` объявляет текущие поддерживаемые длительности 4/6/8 секунд, разрешения `720P`/`1080P` и соотношения сторон `16:9`/`9:16`. Video-to-video не зарегистрирован для OpenRouter, потому что upstream API генерации видео сейчас принимает текст и ссылки на изображения.

## Генерация музыки

OpenRouter также может обслуживать инструмент `music_generate` через аудиовывод chat completions. Используйте аудиомодель OpenRouter в `agents.defaults.musicGenerationModel`:

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      musicGenerationModel: {        primary: "openrouter/google/lyria-3-pro-preview",        timeoutMs: 180_000,      },    },  },}
[/code]

Встроенный музыкальный провайдер OpenRouter по умолчанию использует `google/lyria-3-pro-preview` и также предоставляет `google/lyria-3-clip-preview`. OpenClaw отправляет `modalities: ["text", "audio"]`, включает потоковую передачу, собирает потоковые аудиофрагменты и сохраняет результат как сгенерированные медиа для доставки в канал. Эталонные изображения принимаются для моделей Lyria через общий параметр `music_generate image=...`.

## Text-to-speech

OpenRouter также можно использовать как TTS-провайдера через его совместимый с OpenAI endpoint `/audio/speech`.

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "openrouter",      providers: {        openrouter: {          model: "hexgrad/kokoro-82m",          speakerVoice: "af_alloy",          responseFormat: "mp3",        },      },    },  },}
[/code]

Если `messages.tts.providers.openrouter.apiKey` не указан, TTS повторно использует `models.providers.openrouter.apiKey`, затем `OPENROUTER_API_KEY`.

## Speech-to-text (входящее аудио)

OpenRouter может транскрибировать входящие голосовые/аудиовложения через общий путь `tools.media.audio`, используя свой STT endpoint (`/audio/transcriptions`). Это применяется к любому channel Plugin, который передает входящий голос/аудио в предварительную обработку понимания медиа.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "openrouter", model: "openai/whisper-large-v3-turbo" }],      },    },  },}
[/code]

OpenClaw отправляет STT-запросы OpenRouter как JSON с аудио base64 в `input_audio` (контракт STT OpenRouter), а не как multipart-загрузки форм OpenAI.

## Маршрутизатор Fusion

Используйте OpenRouter Fusion, когда хотите, чтобы один идентификатор модели OpenClaw запрашивал несколько моделей OpenRouter параллельно, OpenRouter оценивал их ответы и возвращал единый финальный ответ через обычный endpoint провайдера OpenRouter. Поскольку upstream slug модели — `openrouter/fusion`, идентификатор модели OpenClaw включает и префикс провайдера OpenClaw, и upstream namespace OpenRouter:

bashCopy code
[code]
    openclaw models set openrouter/openrouter/fusion
[/code]

Настройте панель и судью Fusion через `params.extraBody` модели. Эти поля передаются в тело запроса chat-completions OpenRouter. Fusion работает как с OAuth-онбордингом OpenRouter, так и с онбордингом по ключу API; если вы используете OAuth, опустите строку `env.OPENROUTER_API_KEY` из примера ниже.

json5Copy code
[code]
    {  env: { OPENROUTER_API_KEY: "sk-or-..." },  agents: {    defaults: {      model: { primary: "openrouter/openrouter/fusion" },      models: {        "openrouter/openrouter/fusion": {          params: {            extraBody: {              plugins: [                {                  id: "fusion",                  analysis_models: [                    "google/gemini-3.5-flash",                    "moonshotai/kimi-k2.6",                    "deepseek/deepseek-v4-pro",                  ],                  model: "google/gemini-3.5-flash",                },              ],            },          },        },      },    },  },}
[/code]

Список `analysis_models` — это параллельная панель, а `model` внутри конфигурации Plugin Fusion — модель-судья. Не задавайте верхнеуровневый `tool_choice` как `"required"` в обычных agent/chat-ходах OpenClaw, пытаясь принудительно включить Fusion; ходы OpenClaw могут включать определения инструментов OpenClaw, и верхнеуровневый обязательный выбор инструмента может потребовать один из этих инструментов вместо маршрутизатора Fusion. Когда эта конфигурация Plugin Fusion присутствует, OpenClaw также добавляет очищенную заметку в system prompt с настроенными моделями анализа и моделью-судьей, чтобы агент мог отвечать на вопросы о своей текущей панели Fusion. Другие поля `extraBody` не копируются в prompt.

Fusion намеренно медленнее. OpenRouter может отправить один и тот же prompt OpenClaw нескольким моделям анализа, а затем выполнить финальный шаг оценки/синтеза, поэтому задержка обычно выше, чем у прямого запроса к одной модели. Используйте Fusion для продуманных, высококачественных ответов или путей эскалации, а не как значение по умолчанию для чата, чувствительного к задержке. Для более быстрых ответов держите панель небольшой и выбирайте более быстрые модели анализа и судьи.

Проверьте настроенный идентификатор одноразовым локальным вызовом модели:

bashCopy code
[code]
    openclaw infer model run --local \  --model openrouter/openrouter/fusion \  --prompt "Reply with exactly: FUSION_OK" \  --json
[/code]

## Аутентификация и заголовки

OpenRouter под капотом использует Bearer-токен с вашим ключом API. OpenRouter OAuth — это поток входа PKCE, который выдает ключ API OpenRouter, поэтому OpenClaw сохраняет результат как тот же профиль аутентификации ключа API `openrouter:default`, который используется путем ручной настройки ключа API.

Для существующей установки войдите или замените сохраненный ключ OpenRouter без повторного полного онбординга:

bashCopy code
[code]
    openclaw models auth login --provider openrouter --method oauth
[/code]

Используйте `openclaw models auth login --provider openrouter --method api-key`, когда хотите вставить ключ, созданный вручную в OpenRouter.

В реальных запросах OpenRouter (`https://openrouter.ai/api/v1`) OpenClaw также добавляет документированные заголовки OpenRouter для атрибуции приложения:

Заголовок | Значение  
---|---  
`HTTP-Referer` | `https://openclaw.ai`  
`X-OpenRouter-Title` | `OpenClaw`  
`X-OpenRouter-Categories` | `cli-agent,cloud-agent,programming-app,creative-writing,writing-assistant,general-chat,personal-agent`  
  
## Расширенная конфигурация

Кэширование ответов

Кэширование ответов OpenRouter включается явно. Включите его для каждой модели OpenRouter с помощью параметров модели:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openrouter/auto": {          params: {            responseCache: true,            responseCacheTtlSeconds: 300,          },        },      },    },  },}
[/code]

OpenClaw отправляет `X-OpenRouter-Cache: true` и, если настроено, `X-OpenRouter-Cache-TTL`. `responseCacheClear: true` принудительно обновляет текущий запрос и сохраняет заменяющий ответ. Также принимаются snake_case-алиасы (`response_cache`, `response_cache_ttl_seconds` и `response_cache_clear`).

Это отдельно от кэширования prompt провайдера и от маркеров Anthropic `cache_control` OpenRouter. Оно применяется только на проверенных маршрутах `openrouter.ai`, а не на базовых URL пользовательских прокси.

Маркеры кэша Anthropic

На проверенных маршрутах OpenRouter идентификаторы моделей Anthropic сохраняют специфичные для OpenRouter маркеры Anthropic `cache_control`, которые OpenClaw использует для лучшего повторного использования prompt cache в блоках system/developer prompt.

Предзаполнение рассуждений Anthropic

На проверенных маршрутах OpenRouter ссылки на модели Anthropic с включенными рассуждениями удаляют завершающие ходы предзаполнения ассистента до того, как запрос дойдет до OpenRouter, что соответствует требованию Anthropic: диалоги с рассуждениями должны завершаться ходом пользователя.

Внедрение thinking / reasoning

На поддерживаемых маршрутах, отличных от `auto`, OpenClaw сопоставляет выбранный уровень thinking с полезными нагрузками рассуждений прокси OpenRouter. Неподдерживаемые подсказки моделей и `openrouter/auto` пропускают это внедрение рассуждений. Hunter Alpha также пропускает прокси-рассуждения для устаревших настроенных ссылок на модели, потому что OpenRouter мог возвращать текст финального ответа в полях рассуждений для этого выведенного из эксплуатации маршрута.

Повтор рассуждений DeepSeek V4

На проверенных маршрутах OpenRouter `openrouter/deepseek/deepseek-v4-flash` и `openrouter/deepseek/deepseek-v4-pro` заполняют отсутствующий `reasoning_content` в повторно воспроизводимых ходах ассистента, чтобы диалоги с thinking/инструментами сохраняли требуемую для DeepSeek V4 форму последующего ответа. OpenClaw отправляет поддерживаемые OpenRouter значения `reasoning_effort` для этих маршрутов; `xhigh` является самым высоким заявленным уровнем, а устаревшие переопределения `max` сопоставляются с `xhigh`.

Формирование запросов только для OpenAI

OpenRouter по-прежнему проходит через прокси-путь, совместимый с OpenAI, поэтому нативное формирование запросов только для OpenAI, такое как `serviceTier`, Responses `store`, полезные нагрузки совместимости рассуждений OpenAI и подсказки кэша промптов, не пересылается.

Маршруты на базе Gemini

Ссылки OpenRouter на базе Gemini остаются на прокси-Gemini пути: OpenClaw сохраняет там очистку сигнатур мыслей Gemini, но не включает нативную проверку воспроизведения Gemini или перезаписи начальной инициализации.

Метаданные маршрутизации провайдера

OpenRouter поддерживает объект запроса `provider` для маршрутизации базового провайдера. Настройте политику по умолчанию для всех запросов текстовых моделей OpenRouter с помощью `models.providers.openrouter.params.provider`:

json5Copy code
[code]
    {  models: {    providers: {      openrouter: {        params: {          provider: {            sort: "latency",            require_parameters: true,            data_collection: "deny",          },        },      },    },  },}
[/code]

OpenClaw пересылает этот объект в OpenRouter как полезную нагрузку `provider` запроса. Используйте документированные OpenRouter поля в snake_case, включая `sort`, `only`, `ignore`, `order`, `allow_fallbacks`, `require_parameters`, `data_collection`, `quantizations`, `max_price`, `preferred_max_latency`, `preferred_min_throughput`, `zdr` и `enforce_distillable_text`.

Параметры отдельных моделей по-прежнему переопределяют объект маршрутизации на уровне провайдера:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "openrouter/anthropic/claude-sonnet-4-6": {          params: {            provider: {              order: ["anthropic"],              allow_fallbacks: false,            },          },        },      },    },  },}
[/code]

Это применяется только к маршрутам chat-completions OpenRouter. Прямые маршруты Anthropic, Google, OpenAI или пользовательских провайдеров игнорируют параметры маршрутизации OpenRouter.

## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Справочник по конфигурации** Полный справочник по конфигурации для агентов, моделей и провайдеров. ](</ru/gateway/configuration-reference>)

Was this useful?YesNo

Open issue