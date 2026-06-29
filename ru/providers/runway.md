---
title: Запас времени
source_url: https://docs.openclaw.ai/ru/providers/runway
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw поставляется со встроенным провайдером `runway` для размещенной генерации видео. Plugin включен по умолчанию и регистрирует провайдер `runway` для контракта `videoGenerationProviders`.

Свойство | Значение  
---|---  
Идентификатор провайдера | `runway`  
Plugin | встроенный, `enabledByDefault: true`  
Переменные среды для auth | `RUNWAYML_API_SECRET` (каноническая) или `RUNWAY_API_KEY`  
Флаг онбординга | `--auth-choice runway-api-key`  
Прямой флаг CLI | `--runway-api-key <key>`  
API | Генерация видео Runway на основе задач (опрос `GET /v1/tasks/{id}`)  
Модель по умолчанию | `runway/gen4.5`  
  
## Начало работы

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Set Runway as the default video provider

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Generate a video

Попросите агента сгенерировать видео. Runway будет использован автоматически.

## Поддерживаемые режимы и модели

Провайдер предоставляет семь моделей Runway, разделенных на три режима. Один и тот же идентификатор модели может обслуживать более одного режима (например, `gen4.5` работает как для преобразования текста в видео, так и для преобразования изображения в видео).

Режим | Модели | Входная ссылка  
---|---|---  
Текст в видео | `gen4.5` (по умолчанию), `veo3.1`, `veo3.1_fast`, `veo3` | Нет  
Изображение в видео | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 локальное или удаленное изображение  
Видео в видео | `gen4_aleph` | 1 локальное или удаленное видео  
  
Локальные ссылки на изображения и видео поддерживаются через data URI.

Соотношения сторон | Допустимые значения  
---|---  
Текст в видео | `16:9`, `9:16`  
Редактирование изображений и видео | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Конфигурация

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Расширенная конфигурация

Environment variable aliases

OpenClaw распознает как `RUNWAYML_API_SECRET` (каноническую), так и `RUNWAY_API_KEY`. Любая из этих переменных аутентифицирует провайдер Runway.

Task polling

Runway использует API на основе задач. После отправки запроса на генерацию OpenClaw опрашивает `GET /v1/tasks/{id}`, пока видео не будет готово. Для поведения опроса дополнительная конфигурация не требуется.

## Связанные материалы

[**Video generation** Общие параметры инструмента, выбор провайдера и асинхронное поведение. ](</ru/tools/video-generation>) [**Configuration reference** Настройки агента по умолчанию, включая модель генерации видео. ](</ru/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue