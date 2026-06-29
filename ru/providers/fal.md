---
title: Fal
source_url: https://docs.openclaw.ai/ru/providers/fal
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw поставляется со встроенным провайдером `fal` для размещенной генерации изображений, видео и музыки.

Свойство | Значение  
---|---  
Провайдер | `fal`  
Аутентификация | `FAL_KEY` (канонический; `FAL_API_KEY` также работает как fallback)  
API | эндпоинты моделей fal  
  
## Начало работы

* ### Задайте API-ключ

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Задайте модель изображений по умолчанию

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Генерация изображений

Встроенный провайдер генерации изображений `fal` по умолчанию использует `fal/fal-ai/flux/dev`.

Возможность | Значение  
---|---  
Макс. изображений | 4 на запрос; Krea 2: 1 на запрос  
Режим редактирования | Flux: 1 референсное изображение; GPT Image 2: 10; Nano Banana 2: 14  
Референсы стиля | Krea 2: до 10 референсов стиля через `image` / `images`  
Переопределения размера | Поддерживаются  
Соотношение сторон | Поддерживается для генерации, Krea 2 и редактирования GPT Image 2/Nano Banana 2  
Разрешение | Поддерживается  
Формат вывода | `png` или `jpeg`  
  
Модели Krea 2 используют нативную схему payload Krea в fal. OpenClaw отправляет `aspect_ratio`, `creativity` и `image_style_references` вместо универсального `image_size` / payload эндпоинта редактирования, используемого Flux. Рефы моделей:

  * `fal/krea/v2/medium/text-to-image`
  * `fal/krea/v2/large/text-to-image`


Используйте Medium для более быстрой выразительной иллюстрации, аниме, живописи и художественных стилей. Используйте Large для более медленных фотореалистичных результатов, сырой текстуры, зерна пленки и детализированного вида. Для Krea по умолчанию используется `fal.creativity: "medium"`; поддерживаемые значения: `raw`, `low`, `medium` и `high`.

Krea 2 предоставляет в схеме запросов fal соотношение сторон, а не `image_size`. Предпочитайте `aspectRatio`; OpenClaw сопоставляет `size` с ближайшим поддерживаемым соотношением сторон Krea и отклоняет `resolution` для Krea, а не отбрасывает его.

Используйте `outputFormat: "png"`, когда нужен PNG-вывод от моделей fal, которые предоставляют `output_format`. fal не объявляет в OpenClaw явного управления прозрачным фоном, поэтому `background: "transparent"` сообщается как проигнорированное переопределение для моделей fal. Эндпоинты Krea 2 не предоставляют поле запроса `output_format` через fal, поэтому OpenClaw отклоняет переопределения `outputFormat` для запросов Krea.

Чтобы использовать fal как провайдер изображений по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

Чтобы использовать Krea 2 Medium:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/krea/v2/medium/text-to-image",      },    },  },}
[/code]

## Генерация видео

Встроенный провайдер генерации видео `fal` по умолчанию использует `fal/fal-ai/minimax/video-01-live`.

Возможность | Значение  
---|---  
Режимы | Text-to-video, референс с одним изображением, Seedance reference-to-video  
Среда выполнения | Поток submit/status/result на базе очереди для долго выполняющихся заданий  
  
Доступные видеомодели

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Пример конфигурации Seedance 2.0 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Пример конфигурации Seedance 2.0 reference-to-video json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Reference-to-video принимает до 9 изображений, 3 видео и 3 аудиореференсов через общие параметры `video_generate` `images`, `videos` и `audioRefs`, но не более 12 референсных файлов всего.

Пример конфигурации HeyGen video-agent json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## Генерация музыки

Встроенный Plugin `fal` также регистрирует провайдер генерации музыки для общего инструмента `music_generate`.

Возможность | Значение  
---|---  
Модель по умолчанию | `fal/fal-ai/minimax-music/v2.6`  
Модели | `fal-ai/minimax-music/v2.6`, `fal-ai/ace-step/prompt-to-audio`, `fal-ai/stable-audio-25/text-to-audio`  
Среда выполнения | Синхронный запрос плюс загрузка сгенерированного аудио  
  
Используйте fal как провайдер музыки по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "fal/fal-ai/minimax-music/v2.6",      },    },  },}
[/code]

`fal-ai/minimax-music/v2.6` поддерживает явный текст песен и инструментальный режим. ACE-Step и Stable Audio — это эндпоинты prompt-to-audio; выбирайте их с переопределением `model`, когда нужны эти семейства моделей.

## Связанные материалы

[**Генерация изображений** Общие параметры инструмента изображений и выбор провайдера. ](</ru/tools/image-generation>) [**Генерация видео** Общие параметры инструмента видео и выбор провайдера. ](</ru/tools/video-generation>) [**Генерация музыки** Общие параметры инструмента музыки и выбор провайдера. ](</ru/tools/music-generation>) [**Справочник по конфигурации** Значения агента по умолчанию, включая выбор моделей изображений, видео и музыки. ](</ru/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue