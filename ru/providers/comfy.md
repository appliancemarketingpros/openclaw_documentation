---
title: ComfyUI
source_url: https://docs.openclaw.ai/ru/providers/comfy
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw поставляется со встроенным Plugin `comfy` для запусков ComfyUI на основе рабочих процессов. Plugin полностью управляется рабочими процессами, поэтому OpenClaw не пытается сопоставлять универсальные элементы управления `size`, `aspectRatio`, `resolution`, `durationSeconds` или элементы управления в стиле TTS с вашим графом.

Свойство | Детали  
---|---  
Провайдер | `comfy`  
Модели | `comfy/workflow`  
Общие поверхности | `image_generate`, `video_generate`, `music_generate`  
Авторизация | Не требуется для локального ComfyUI; `COMFY_API_KEY` или `COMFY_CLOUD_API_KEY` для Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` и Comfy Cloud `/api/*`  
  
## Что поддерживается

  * Генерация изображений из workflow JSON
  * Редактирование изображений с 1 загруженным референсным изображением
  * Генерация видео из workflow JSON
  * Генерация видео с 1 загруженным референсным изображением
  * Генерация музыки или аудио через общий инструмент `music_generate`
  * Загрузка выходных данных из настроенного узла или всех подходящих выходных узлов


## Начало работы

Выберите между запуском ComfyUI на собственной машине и использованием Comfy Cloud.

### Local

**Лучше всего подходит для:** запуска собственного экземпляра ComfyUI на вашей машине или в LAN.

* ### Start ComfyUI locally

Убедитесь, что ваш локальный экземпляр ComfyUI запущен (по умолчанию `http://127.0.0.1:8188`).

* ### Prepare your workflow JSON

Экспортируйте или создайте JSON-файл рабочего процесса ComfyUI. Запомните идентификаторы узлов для узла ввода промпта и выходного узла, из которого OpenClaw должен читать данные.

* ### Configure the provider

Установите `mode: "local"` и укажите файл рабочего процесса. Минимальный пример для изображения:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Set the default model

Направьте OpenClaw на модель `comfy/workflow` для настроенной возможности:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verify

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**Лучше всего подходит для:** запуска рабочих процессов в Comfy Cloud без управления локальными ресурсами GPU.

* ### Get an API key

Зарегистрируйтесь на [comfy.org](<https://comfy.org>) и сгенерируйте API-ключ в панели управления своей учетной записи.

* ### Set the API key

Передайте ключ одним из этих способов:

bashCopy code
[code]
    # Environment variable (preferred)export COMFY_API_KEY="your-key" # Alternative environment variableexport COMFY_CLOUD_API_KEY="your-key" # Or inline in configopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Prepare your workflow JSON

Экспортируйте или создайте JSON-файл рабочего процесса ComfyUI. Запомните идентификаторы узлов для узла ввода промпта и выходного узла.

* ### Configure the provider

Установите `mode: "cloud"` и укажите файл рабочего процесса:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Set the default model

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verify

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Конфигурация

Comfy поддерживает общие настройки подключения верхнего уровня, а также разделы рабочих процессов для каждой возможности (`image`, `video`, `music`):

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Общие ключи

Ключ | Тип | Описание  
---|---|---  
`mode` | `"local"` или `"cloud"` | Режим подключения.  
`baseUrl` | строка | По умолчанию `http://127.0.0.1:8188` для локального режима или `https://cloud.comfy.org` для облачного.  
`apiKey` | строка | Необязательный встроенный ключ, альтернатива переменным окружения `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | Разрешить частный/LAN `baseUrl` в облачном режиме.  
  
### Ключи для каждой возможности

Эти ключи применяются внутри разделов `image`, `video` или `music`:

Ключ | Обязателен | По умолчанию | Описание  
---|---|---|---  
`workflow` или `workflowPath` | Да | \-- | Путь к JSON-файлу рабочего процесса ComfyUI.  
`promptNodeId` | Да | \-- | Идентификатор узла, который получает текстовый промпт.  
`promptInputName` | Нет | `"text"` | Имя входа на узле промпта.  
`outputNodeId` | Нет | \-- | Идентификатор узла, из которого читаются выходные данные. Если опущен, используются все подходящие выходные узлы.  
`pollIntervalMs` | Нет | \-- | Интервал опроса в миллисекундах для завершения задания.  
`timeoutMs` | Нет | \-- | Тайм-аут в миллисекундах для запуска рабочего процесса.  
  
Разделы `image` и `video` также поддерживают:

Ключ | Обязателен | По умолчанию | Описание  
---|---|---|---  
`inputImageNodeId` | Да (при передаче референсного изображения) | \-- | Идентификатор узла, который получает загруженное референсное изображение.  
`inputImageInputName` | Нет | `"image"` | Имя входа на узле изображения.  
  
## Детали рабочих процессов

Image workflows

Установите модель изображения по умолчанию на `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Пример редактирования с референсным изображением:**

Чтобы включить редактирование изображения с загруженным референсным изображением, добавьте `inputImageNodeId` в конфигурацию изображения:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Video workflows

Установите модель видео по умолчанию на `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Видеорабочие процессы Comfy поддерживают text-to-video и image-to-video через настроенный граф.

Music workflows

Встроенный Plugin регистрирует провайдера генерации музыки для аудио- или музыкальных выходных данных, определенных рабочим процессом, доступных через общий инструмент `music_generate`:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Используйте раздел конфигурации `music`, чтобы указать JSON-файл аудиорабочего процесса и выходной узел.

Backward compatibility

Существующая конфигурация изображения верхнего уровня (без вложенного раздела `image`) по-прежнему работает:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw рассматривает эту устаревшую форму как конфигурацию рабочего процесса изображения. Немедленно мигрировать не нужно, но вложенные разделы `image` / `video` / `music` рекомендуются для новых настроек.

Live tests

Для встроенного Plugin доступно подключаемое live-покрытие:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Live-тест пропускает отдельные случаи для изображений, видео или музыки, если соответствующий раздел рабочего процесса Comfy не настроен.

## Связанные материалы

[**Генерация изображений** Настройка и использование инструмента генерации изображений. ](</ru/tools/image-generation>) [**Генерация видео** Настройка и использование инструмента генерации видео. ](</ru/tools/video-generation>) [**Генерация музыки** Настройка инструмента генерации музыки и аудио. ](</ru/tools/music-generation>) [**Каталог провайдеров** Обзор всех провайдеров и ссылок на модели. ](</ru/providers>) [**Справочник по конфигурации** Полный справочник по конфигурации, включая настройки агентов по умолчанию. ](</ru/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue