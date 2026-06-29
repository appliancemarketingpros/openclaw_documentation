---
title: SGLang
source_url: https://docs.openclaw.ai/ru/providers/sglang
scraped_at: 2026-06-29
---

ModelsProviders

SGLang обслуживает модели с открытыми весами через OpenAI-совместимый HTTP API. OpenClaw подключается к SGLang с помощью семейства провайдеров `openai-completions` с автообнаружением доступных моделей.

Свойство | Значение  
---|---  
ID провайдера | `sglang`  
Plugin | встроенный, `enabledByDefault: true`  
Переменная окружения auth | `SGLANG_API_KEY` (любое непустое значение, если на сервере нет auth)  
Флаг онбординга | `--auth-choice sglang`  
API | OpenAI-совместимый (`openai-completions`)  
Базовый URL по умолчанию | `http://127.0.0.1:30000/v1`  
Заполнитель модели по умолчанию | `sglang/Qwen/Qwen3-8B`  
Использование streaming | Да (`supportsStreamingUsage: true`)  
Цены | Помечено как внешне-бесплатное (`modelPricing.external: false`)  
  
OpenClaw также **автоматически обнаруживает** доступные модели из SGLang, когда вы включаете это через `SGLANG_API_KEY`. Используйте `sglang/*` в `agents.defaults.models`, чтобы discovery оставалось динамическим, когда вы также настраиваете пользовательский базовый URL SGLang. См. Обнаружение моделей (неявный провайдер) ниже.

## Начало работы

* ### Запустите SGLang

Запустите SGLang с OpenAI-совместимым сервером. Ваш базовый URL должен предоставлять endpoints `/v1` (например, `/v1/models`, `/v1/chat/completions`). SGLang обычно работает на:

  * `http://127.0.0.1:30000/v1`


* ### Задайте ключ API

Подойдет любое значение, если на вашем сервере не настроен auth:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Запустите онбординг или задайте модель напрямую

bashCopy code
[code]
    openclaw onboard
[/code]

Или настройте модель вручную:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## Обнаружение моделей (неявный провайдер)

Когда задан `SGLANG_API_KEY` (или существует профиль auth) и вы **не** определяете `models.providers.sglang`, OpenClaw выполнит запрос:

  * `GET http://127.0.0.1:30000/v1/models`


и преобразует возвращенные ID в записи моделей.

## Явная конфигурация (модели вручную)

Используйте явную конфигурацию, когда:

  * SGLang работает на другом хосте/порту.
  * Вы хотите закрепить значения `contextWindow`/`maxTokens`.
  * Ваш сервер требует настоящий ключ API (или вы хотите управлять заголовками).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Расширенная конфигурация

Поведение в стиле прокси

SGLang рассматривается как proxy-style OpenAI-совместимый backend `/v1`, а не как нативный endpoint OpenAI.

Поведение | SGLang  
---|---  
Формирование запросов только для OpenAI | Не применяется  
`service_tier`, Responses `store`, подсказки prompt-cache | Не отправляются  
Формирование payload для reasoning-compat | Не применяется  
Скрытые заголовки атрибуции (`originator`, `version`, `User-Agent`) | Не внедряются для пользовательских базовых URL SGLang  
  
Устранение неполадок

**Сервер недоступен**

Проверьте, что сервер запущен и отвечает:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**Ошибки auth**

Если запросы завершаются ошибками auth, задайте настоящий `SGLANG_API_KEY`, который соответствует конфигурации вашего сервера, или явно настройте провайдера в `models.providers.sglang`.

## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок на модели и поведения failover. ](</ru/concepts/model-providers>) [**Справочник по конфигурации** Полная схема конфигурации, включая записи провайдеров. ](</ru/gateway/configuration-reference>)

Was this useful?YesNo

Open issue