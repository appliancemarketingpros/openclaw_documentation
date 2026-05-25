---
title: Fal
source_url: https://docs.openclaw.ai/uk/providers/fal
scraped_at: 2026-05-25
---

OpenClaw постачається з вбудованим провайдером `fal` для хостингової генерації зображень і відео.

Властивість | Значення  
---|---  
Провайдер | `fal`  
Автентифікація | `FAL_KEY` (канонічний; `FAL_API_KEY` також працює як резервний варіант)  
API | кінцеві точки моделей fal  
  
## Початок роботи

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Set a default image model

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Генерація зображень

Вбудований провайдер генерації зображень `fal` за замовчуванням використовує `fal/fal-ai/flux/dev`.

Можливість | Значення  
---|---  
Максимум зображень | 4 на запит  
Режим редагування | Flux: 1 еталонне зображення; GPT Image 2: 10; Nano Banana 2: 14  
Перевизначення розміру | Підтримується  
Співвідношення сторін | Підтримується для генерації та редагування GPT Image 2/Nano Banana 2  
Роздільна здатність | Підтримується  
Формат виводу | `png` або `jpeg`  
  
Використовуйте `outputFormat: "png"`, коли потрібен вивід у PNG. fal не оголошує явного керування прозорим тлом в OpenClaw, тому `background: "transparent"` повідомляється як проігнороване перевизначення для моделей fal.

Щоб використовувати fal як провайдера зображень за замовчуванням:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Генерація відео

Вбудований провайдер генерації відео `fal` за замовчуванням використовує `fal/fal-ai/minimax/video-01-live`.

Можливість | Значення  
---|---  
Режими | Текст-у-відео, еталон за одним зображенням, Seedance еталон-у-відео  
Середовище виконання | Потік submit/status/result на основі черги для довготривалих завдань  
  
Available video models

**HeyGen video-agent:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Seedance 2.0 config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Seedance 2.0 reference-to-video config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Reference-to-video приймає до 9 зображень, 3 відео та 3 аудіоеталонів через спільні параметри `video_generate` `images`, `videos` і `audioRefs`, із максимум 12 еталонними файлами загалом.

HeyGen video-agent config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## Пов’язане

[**Image generation** Спільні параметри інструмента зображень і вибір провайдера. ](</uk/tools/image-generation>) [**Video generation** Спільні параметри інструмента відео та вибір провайдера. ](</uk/tools/video-generation>) [**Configuration reference** Значення агентів за замовчуванням, включно з вибором моделі зображень і відео. ](</uk/gateway/config-agents#agent-defaults>)

Was this useful?YesNo