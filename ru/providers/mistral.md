---
title: Mistral
source_url: https://docs.openclaw.ai/ru/providers/mistral
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw включает встроенный Plugin Mistral, который регистрирует четыре контракта: чат-завершения, понимание медиа (пакетная транскрипция Voxtral), realtime STT для Voice Call (Voxtral Realtime) и эмбеддинги памяти (`mistral-embed`).

Свойство | Значение  
---|---  
ID провайдера | `mistral`  
Plugin | встроенный, `enabledByDefault: true`  
Env var авторизации | `MISTRAL_API_KEY`  
Флаг онбординга | `--auth-choice mistral-api-key`  
Прямой флаг CLI | `--mistral-api-key <key>`  
API | совместимый с OpenAI (`openai-completions`)  
Базовый URL | `https://api.mistral.ai/v1`  
Модель по умолчанию | `mistral/mistral-large-latest`  
Модель эмбеддингов | `mistral-embed`  
Пакетный Voxtral | `voxtral-mini-latest` (транскрипция аудио)  
Realtime Voxtral | `voxtral-mini-transcribe-realtime-2602`  
  
## Начало работы

* ### Получите ключ API

Создайте ключ API в [Mistral Console](<https://console.mistral.ai/>).

* ### Запустите онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

Или передайте ключ напрямую:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### Задайте модель по умолчанию

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### Проверьте, что модель доступна

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## Встроенный каталог LLM

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) — текущая смешанная модель Medium во встроенном каталоге: 128B плотных весов, ввод текста и изображений, контекст 256K, вызов функций, структурированный вывод, программирование и настраиваемое рассуждение через API Chat Completions. Используйте `mistral/mistral-medium-3-5`, когда вам нужна более новая унифицированная агентная/кодинговая модель Mistral вместо модели по умолчанию `mistral/mistral-large-latest`.

Сейчас OpenClaw поставляет такой встроенный каталог Mistral:

Ссылка на модель | Ввод | Контекст | Макс. вывод | Примечания  
---|---|---|---|---  
`mistral/mistral-large-latest` | текст, изображение | 262,144 | 16,384 | Модель по умолчанию  
`mistral/mistral-medium-2508` | текст, изображение | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | текст, изображение | 262,144 | 8,192 | Mistral Medium 3.5; настраиваемое рассуждение  
`mistral/mistral-small-latest` | текст, изображение | 128,000 | 16,384 | Mistral Small 4; настраиваемое рассуждение через API `reasoning_effort`  
`mistral/pixtral-large-latest` | текст, изображение | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | текст | 256,000 | 4,096 | Программирование  
`mistral/devstral-medium-latest` | текст | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | текст | 128,000 | 40,000 | С поддержкой рассуждения  
  
После онбординга выполните smoke-тест Medium 3.5 без запуска Gateway:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

Чтобы просмотреть строку встроенного каталога перед изменением конфигурации:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## Транскрипция аудио (Voxtral)

Используйте Voxtral для пакетной транскрипции аудио через конвейер понимания медиа.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## Потоковый STT для Voice Call

Встроенный Plugin `mistral` регистрирует Voxtral Realtime как провайдера потокового STT для Voice Call.

Настройка | Путь конфигурации | По умолчанию  
---|---|---  
Ключ API | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | Откатывается к `MISTRAL_API_KEY`  
Модель | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
Кодирование | `...mistral.encoding` | `pcm_mulaw`  
Частота дискретизации | `...mistral.sampleRate` | `8000`  
Целевая задержка | `...mistral.targetStreamingDelayMs` | `800`  
  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## Расширенная конфигурация

Настраиваемое рассуждение

`mistral/mistral-small-latest` (Mistral Small 4) и `mistral/mistral-medium-3-5` поддерживают [настраиваемое рассуждение](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) в API Chat Completions через `reasoning_effort` (`none` минимизирует дополнительные размышления в выводе; `high` показывает полные трассы рассуждения перед финальным ответом). Mistral рекомендует `reasoning_effort="high"` для агентных и кодовых сценариев Medium 3.5.

OpenClaw сопоставляет уровень **thinking** сеанса с API Mistral:

Уровень thinking в OpenClaw | Mistral `reasoning_effort`  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Пример конфигурации для Medium 3.5 reasoning на уровне модели:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Эмбеддинги памяти

Mistral может обслуживать эмбеддинги памяти через `/v1/embeddings` (модель по умолчанию: `mistral-embed`).

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Авторизация и базовый URL

  * Авторизация Mistral использует `MISTRAL_API_KEY` (заголовок Bearer).
  * Базовый URL провайдера по умолчанию — `https://api.mistral.ai/v1`; он принимает стандартную форму запроса chat-completions, совместимую с OpenAI.
  * Модель онбординга по умолчанию — `mistral/mistral-large-latest`.
  * Переопределяйте базовый URL в `models.providers.mistral.baseUrl` только когда Mistral явно публикует нужный вам региональный endpoint.


## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок на модели и поведения failover. ](</ru/concepts/model-providers>) [**Понимание медиа** Настройка транскрипции аудио и выбор провайдера. ](</ru/nodes/media-understanding>)

Was this useful?YesNo

Open issue