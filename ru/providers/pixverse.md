---
title: PixVerse
source_url: https://docs.openclaw.ai/ru/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw предоставляет `pixverse` как официальный внешний Plugin для размещенной генерации видео PixVerse. Plugin регистрирует провайдера `pixverse` в контракте `videoGenerationProviders`.

Свойство | Значение  
---|---  
Идентификатор провайдера | `pixverse`  
Пакет Plugin | `@openclaw/pixverse-provider`  
Env-переменная авторизации | `PIXVERSE_API_KEY`  
Флаг онбординга | `--auth-choice pixverse-api-key`  
Прямой флаг CLI | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2 (отправка `video_id` и опрос результата)  
Модель по умолчанию | `pixverse/v6`  
Регион API по умолчанию | Международный  
  
## Начало работы

* ### Install the plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

Мастер спрашивает, использовать ли международную конечную точку (`https://app-api.pixverse.ai/openapi/v2`) или конечную точку CN (`https://app-api.pixverseai.cn/openapi/v2`), прежде чем записать `region` и `baseUrl` в конфигурацию провайдера.

* ### Set PixVerse as the default video provider

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Generate a video

Попросите агента сгенерировать видео. PixVerse будет использоваться автоматически.

## Поддерживаемые режимы и модели

Провайдер предоставляет модели генерации PixVerse через общий видеоинструмент OpenClaw.

Режим | Модели | Входные ссылочные данные  
---|---|---  
Текст в видео | `v6` (по умолчанию), `c1` | Нет  
Изображение в видео | `v6` (по умолчанию), `c1` | 1 локальное или удаленное изображение  
  
Локальные ссылки на изображения загружаются в PixVerse перед запросом преобразования изображения в видео. URL удаленных изображений передаются через конечную точку загрузки изображений PixVerse как `image_url`.

Параметр | Поддерживаемые значения  
---|---  
Длительность | 1-15 секунд  
Разрешение | `360P`, `540P`, `720P`, `1080P`  
Соотношение сторон | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` для текста в видео  
Сгенерированное аудио | `audio: true`  
  
## Параметры провайдера

Видеопровайдер принимает следующие необязательные ключи, специфичные для провайдера:

Параметр | Тип | Эффект  
---|---|---  
`seed` | number | Детерминированное зерно, если поддерживается  
`negativePrompt` / `negative_prompt` | string | Негативный промпт  
`quality` | string | Качество PixVerse, например `720p`  
`motionMode` / `motion_mode` | string | Режим движения для изображения в видео  
`cameraMovement` / `camera_movement` | string | Пресет движения камеры PixVerse  
`templateId` / `template_id` | number | Активированный идентификатор шаблона PixVerse  
  
## Конфигурация

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## Расширенная конфигурация

API region

OpenClaw по умолчанию использует международный API PixVerse. Задайте `models.providers.pixverse.region` вручную, если ваш ключ относится к определенному региону платформы PixVerse, или используйте `openclaw onboard --auth-choice pixverse-api-key`, чтобы выбрать регион в мастере настройки:

Значение региона | Базовый URL API PixVerse  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

Custom base URL

Задавайте `models.providers.pixverse.baseUrl` только при маршрутизации через доверенный совместимый прокси. `baseUrl` имеет приоритет над `region`.

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Task polling

PixVerse возвращает `video_id` из запроса генерации. OpenClaw опрашивает `/openapi/v2/video/result/{video_id}`, пока задача не завершится успешно, не завершится ошибкой или не истечет время ожидания.

## Связанные материалы

[**Video generation** Общие параметры инструмента, выбор провайдера и асинхронное поведение. ](</ru/tools/video-generation>) [**Configuration reference** Настройки агента по умолчанию, включая модель генерации видео. ](</ru/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue