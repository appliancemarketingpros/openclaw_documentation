---
title: Vydra
source_url: https://docs.openclaw.ai/ru/providers/vydra
scraped_at: 2026-06-29
---

ModelsProviders

Встроенный Plugin Vydra добавляет:

  * Генерацию изображений через `vydra/grok-imagine`
  * Генерацию видео через `vydra/veo3` и `vydra/kling`
  * Синтез речи через маршрут TTS Vydra на базе ElevenLabs


OpenClaw использует один и тот же `VYDRA_API_KEY` для всех трех возможностей.

Свойство | Значение  
---|---  
Идентификатор провайдера | `vydra`  
Plugin | встроенный, `enabledByDefault: true`  
Переменная окружения для аутентификации | `VYDRA_API_KEY`  
Флаг онбординга | `--auth-choice vydra-api-key`  
Прямой флаг CLI | `--vydra-api-key <key>`  
Контракты | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
Базовый URL | `https://www.vydra.ai/api/v1` (используйте хост `www`)  
  
## Настройка

* ### Run interactive onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

Или задайте переменную окружения напрямую:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Choose a default capability

Выберите одну или несколько возможностей ниже (изображение, видео или речь) и примените соответствующую конфигурацию.

## Возможности

Image generation

Модель изображений по умолчанию:

  * `vydra/grok-imagine`


Задайте ее как провайдера изображений по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

Текущая встроенная поддержка включает только преобразование текста в изображение. Размещенные маршруты редактирования Vydra ожидают удаленные URL изображений, а OpenClaw пока не добавляет во встроенный Plugin специальный мост загрузки для Vydra.

Video generation

Зарегистрированные модели видео:

  * `vydra/veo3` для преобразования текста в видео
  * `vydra/kling` для преобразования изображения в видео


Задайте Vydra как провайдера видео по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Примечания:

  * `vydra/veo3` встроена только для преобразования текста в видео.
  * `vydra/kling` сейчас требует ссылку на удаленный URL изображения. Загрузки локальных файлов отклоняются заранее.
  * Текущий HTTP-маршрут `kling` у Vydra ведет себя непоследовательно в том, требует ли он `image_url` или `video_url`; встроенный провайдер отображает один и тот же удаленный URL изображения в оба поля.
  * Встроенный Plugin остается консервативным и не передает недокументированные параметры стиля, такие как соотношение сторон, разрешение, водяной знак или сгенерированный звук.

Video live tests

Live-покрытие для конкретного провайдера:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

Встроенный live-файл Vydra теперь покрывает:

  * преобразование текста в видео `vydra/veo3`
  * преобразование изображения в видео `vydra/kling` с использованием удаленного URL изображения


При необходимости переопределите удаленную фикстуру изображения:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Speech synthesis

Задайте Vydra как провайдера речи:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          speakerVoiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Значения по умолчанию:

  * Модель: `elevenlabs/tts`
  * Идентификатор голоса: `21m00Tcm4TlvDq8ikWAM`


Встроенный Plugin сейчас предоставляет один проверенный голос по умолчанию и возвращает аудиофайлы MP3.

## Связанные материалы

[**Provider directory** Просмотрите всех доступных провайдеров. ](</ru/providers>) [**Image generation** Общие параметры инструмента изображений и выбор провайдера. ](</ru/tools/image-generation>) [**Video generation** Общие параметры инструмента видео и выбор провайдера. ](</ru/tools/video-generation>) [**Configuration reference** Значения по умолчанию для агентов и конфигурация моделей. ](</ru/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue