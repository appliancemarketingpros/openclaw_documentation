---
title: NVIDIA
source_url: https://docs.openclaw.ai/ru/providers/nvidia
scraped_at: 2026-06-29
---

ModelsProviders

NVIDIA предоставляет OpenAI-совместимый API по адресу `https://integrate.api.nvidia.com/v1` для открытых моделей бесплатно. Выполните аутентификацию с помощью API-ключа с [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>). OpenClaw по умолчанию использует для провайдера NVIDIA Nemotron 3 Ultra, модель NVIDIA для рассуждений с 550B параметрами всего / 55B активными параметрами для агентной работы с длинным контекстом.

## Начало работы

* ### Получите API-ключ

Создайте API-ключ на [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>).

* ### Экспортируйте ключ и запустите онбординг

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### Задайте модель NVIDIA

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-ultra-550b-a55b
[/code]

Для неинтерактивной настройки ключ также можно передать напрямую:

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## Пример конфигурации

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-ultra-550b-a55b" },    },  },}
[/code]

## Избранный каталог

Когда API-ключ NVIDIA настроен, пути настройки OpenClaw и выбора моделей пытаются использовать публичный каталог избранных моделей NVIDIA с `https://assets.ngc.nvidia.com/products/api-catalog/featured-models.json` и кэшируют ранжированный результат на 24 часа. Поэтому новые избранные модели с build.nvidia.com появляются в интерфейсах настройки и выбора моделей без ожидания релиза OpenClaw. Когда живой фид доступен, первая возвращенная модель становится вариантом по умолчанию, показанным во время настройки NVIDIA.

Получение данных использует фиксированную политику HTTPS-хоста для `assets.ngc.nvidia.com`. Если API-ключ NVIDIA не настроен или если этот публичный каталог недоступен либо имеет некорректный формат, OpenClaw возвращается к встроенному каталогу и встроенному значению по умолчанию ниже.

## Nemotron 3 Ultra

Nemotron 3 Ultra — модель NVIDIA по умолчанию в OpenClaw. Страница сборки NVIDIA для [`nvidia/nemotron-3-ultra-550b-a55b`](<https://build.nvidia.com/nvidia/nemotron-3-ultra-550b-a55b>) указывает ее как доступную бесплатную конечную точку со спецификацией контекста в 1M токенов. Во встроенном каталоге указан максимальный вывод в 16 384 токена, чтобы соответствовать текущему OpenAI-совместимому примеру запроса NVIDIA для размещенной конечной точки.

Используйте Ultra как вариант NVIDIA по умолчанию с максимальными возможностями. Оставьте Super выбранной, когда нужен меньший вариант Nemotron 3, или выберите одну из сторонних моделей, размещенных в каталоге NVIDIA, если их контекст, задержка или поведение подходят лучше. Встроенная строка Ultra по умолчанию отправляет `chat_template_kwargs.enable_thinking: false` и `force_nonempty_content: true`, чтобы обычный вывод чата оставался в видимом ответе вместо раскрытия текста рассуждений.

## Встроенный резервный каталог

Ссылка на модель | Название | Контекст | Макс. вывод | Примечания  
---|---|---|---|---  
`nvidia/nvidia/nemotron-3-ultra-550b-a55b` | NVIDIA Nemotron 3 Ultra 550B | 1,000,000 | 16,384 | По умолчанию  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192 | Резервный вариант из избранного каталога  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192 | Резервный вариант из избранного каталога  
`nvidia/minimaxai/minimax-m2.7` | Minimax M2.7 | 196,608 | 8,192 | Резервный вариант из избранного каталога  
`nvidia/z-ai/glm-5.1` | GLM 5.1 | 202,752 | 8,192 | Резервный вариант из избранного каталога  
`nvidia/minimaxai/minimax-m2.5` | MiniMax M2.5 | 196,608 | 8,192 | Устарело, совместимость обновления  
`nvidia/z-ai/glm5` | GLM-5 | 202,752 | 8,192 | Устарело, совместимость обновления  
  
## Расширенная конфигурация

Поведение автоматического включения

Провайдер автоматически включается, когда установлена переменная окружения `NVIDIA_API_KEY`. Явная конфигурация провайдера помимо ключа не требуется.

Каталог и цены

OpenClaw предпочитает публичный каталог избранных моделей NVIDIA, когда аутентификация NVIDIA настроена, и кэширует его на 24 часа. Встроенный резервный каталог статичен и сохраняет устаревшие поставлявшиеся ссылки для совместимости обновления. Стоимость по умолчанию равна `0` в исходном коде, поскольку NVIDIA сейчас предлагает бесплатный API-доступ для перечисленных моделей.

OpenAI-совместимая конечная точка

NVIDIA использует стандартную конечную точку завершений `/v1`. Любой OpenAI-совместимый инструментарий должен работать сразу с базовым URL NVIDIA.

Параметры рассуждений Nemotron 3 Ultra

Пример запроса NVIDIA для Ultra использует `chat_template_kwargs.enable_thinking` и `reasoning_budget` для вывода рассуждений. Встроенная строка Ultra в OpenClaw по умолчанию отключает шаблонное мышление для обычного использования чата. Если нужно включить вывод рассуждений NVIDIA или принудительно задать другие специфичные для NVIDIA поля запроса, задайте параметры для модели и ограничьте специфичные для провайдера переопределения моделью NVIDIA:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "nvidia/nvidia/nemotron-3-ultra-550b-a55b": {          params: {            chat_template_kwargs: { enable_thinking: true },            extra_body: { reasoning_budget: 16384 },          },        },      },    },  },}
[/code]

`params.extra_body` — итоговое переопределение тела OpenAI-совместимого запроса, поэтому используйте его только для полей, которые NVIDIA документирует для выбранной конечной точки.

Медленные ответы пользовательского провайдера

Некоторым пользовательским моделям, размещенным NVIDIA, может требоваться больше времени, чем допускает стандартный сторожевой таймер простоя модели, прежде чем они выдадут первый фрагмент ответа. Для пользовательских записей провайдера NVIDIA увеличьте тайм-аут провайдера вместо увеличения тайм-аута всей среды выполнения агента:

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Справочник конфигурации** Полный справочник конфигурации для агентов, моделей и провайдеров. ](</ru/gateway/configuration-reference>)

Was this useful?YesNo

Open issue