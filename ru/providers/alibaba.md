---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/ru/providers/alibaba
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw поставляется со встроенным plugin `alibaba`, который регистрирует провайдера генерации видео для моделей Wan в Alibaba Model Studio (международное название DashScope). Plugin включен по умолчанию; вам нужно только задать API-ключ.

Свойство | Значение  
---|---  
Идентификатор провайдера | `alibaba`  
Plugin | встроенный, `enabledByDefault: true`  
Env vars для авторизации | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY` (используется первое совпадение)  
Флаг онбординга | `--auth-choice alibaba-model-studio-api-key`  
Прямой флаг CLI | `--alibaba-model-studio-api-key <key>`  
Модель по умолчанию | `alibaba/wan2.6-t2v`  
Базовый URL по умолчанию | `https://dashscope-intl.aliyuncs.com`  
  
## Начало работы

* ### Set an API key

Используйте онбординг, чтобы сохранить ключ для провайдера `alibaba`:

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

Или передайте ключ напрямую во время установки/онбординга:

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

Или экспортируйте любую из поддерживаемых env vars перед запуском Gateway:

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### Set a default video model

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### Verify the provider is configured

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

Список должен включать все пять встроенных моделей Wan. Если `MODELSTUDIO_API_KEY` не разрешается, `openclaw models status --json` сообщает об отсутствующих учетных данных в `auth.unusableProfiles`.

## Встроенные модели Wan

Ссылка на модель | Режим  
---|---  
`alibaba/wan2.6-t2v` | Текст-в-видео (по умолчанию)  
`alibaba/wan2.6-i2v` | Изображение-в-видео  
`alibaba/wan2.6-r2v` | Референс-в-видео  
`alibaba/wan2.6-r2v-flash` | Референс-в-видео (быстро)  
`alibaba/wan2.7-r2v` | Референс-в-видео  
  
## Возможности и ограничения

Встроенный провайдер отражает ограничения видео API Wan в DashScope. У всех трех режимов одинаковые лимиты количества видео и длительности на запрос; отличается только форма входных данных.

Режим | Макс. выходных видео | Макс. входных изображений | Макс. входных видео | Макс. длительность | Поддерживаемые элементы управления  
---|---|---|---|---|---  
Текст-в-видео | 1 | n/a | n/a | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Изображение-в-видео | 1 | 1 | n/a | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
Референс-в-видео | 1 | n/a | 4 | 10 s | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
Когда в запросе не указано `durationSeconds`, провайдер отправляет принятое в DashScope значение по умолчанию — **5 секунд**. Задайте `durationSeconds` явно в [инструменте генерации видео](</ru/tools/video-generation>), чтобы увеличить длительность до 10 s.

## Расширенная конфигурация

Override the DashScope base URL

По умолчанию провайдер использует международный endpoint DashScope. Чтобы выбрать endpoint региона China, задайте:

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

Провайдер удаляет завершающие косые черты перед построением URL задач AIGC.

Auth env priority

OpenClaw разрешает API-ключ Alibaba из переменных окружения в таком порядке, выбирая первое непустое значение:

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


Настроенные записи `auth.profiles` (заданные через `openclaw models auth login`) переопределяют разрешение env-var. См. [профили авторизации в FAQ по моделям](</ru/help/faq-models#what-is-an-auth-profile>) для механики ротации профилей, cooldown и переопределения.

Relationship to the Qwen plugin

Оба встроенных plugin взаимодействуют с DashScope и принимают пересекающиеся API-ключи. Используйте:

  * идентификаторы `alibaba/wan*.*` для выделенного провайдера видео Wan, описанного на этой странице.
  * идентификаторы `qwen/*` для чата, эмбеддингов и понимания медиа Qwen (см. [Qwen](</ru/providers/qwen>)).


Однократная настройка `MODELSTUDIO_API_KEY` авторизует оба plugin, потому что список auth env var намеренно пересекается; вам не нужно выполнять онбординг каждого plugin отдельно.

## Связанные материалы

[**Video generation** Общие параметры инструмента видео и выбор провайдера. ](</ru/tools/video-generation>) [**Qwen** Настройка чата, эмбеддингов и понимания медиа Qwen с той же авторизацией DashScope. ](</ru/providers/qwen>) [**Configuration reference** Значения агентов по умолчанию и конфигурация моделей. ](</ru/gateway/config-agents#agent-defaults>) [**Models FAQ** Профили авторизации, переключение моделей и устранение ошибок "no profile". ](</ru/help/faq-models>)

Was this useful?YesNo

Open issue