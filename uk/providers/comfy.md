---
title: ComfyUI
source_url: https://docs.openclaw.ai/uk/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw постачається з вбудованим Plugin `comfy` для запусків ComfyUI на основі робочих процесів. Plugin повністю керується робочими процесами, тому OpenClaw не намагається зіставляти загальні `size`, `aspectRatio`, `resolution`, `durationSeconds` або елементи керування в стилі TTS з вашим графом.

Property | Detail  
---|---  
Provider | `comfy`  
Models | `comfy/workflow`  
Shared surfaces | `image_generate`, `video_generate`, `music_generate`  
Auth | Немає для локального ComfyUI; `COMFY_API_KEY` або `COMFY_CLOUD_API_KEY` для Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` та Comfy Cloud `/api/*`  
  
## Що підтримується

  * Генерація зображень із JSON робочого процесу
  * Редагування зображень з 1 завантаженим референсним зображенням
  * Генерація відео з JSON робочого процесу
  * Генерація відео з 1 завантаженим референсним зображенням
  * Генерація музики або аудіо через спільний інструмент `music_generate`
  * Завантаження результатів із налаштованого вузла або з усіх відповідних вузлів виводу


## Початок роботи

Оберіть між запуском ComfyUI на власному комп’ютері або використанням Comfy Cloud.

### Local

**Найкраще підходить для:** запуску власного екземпляра ComfyUI на вашому комп’ютері або в LAN.

* ### Запустіть ComfyUI локально

Переконайтеся, що ваш локальний екземпляр ComfyUI запущено (типово `http://127.0.0.1:8188`).

* ### Підготуйте JSON вашого робочого процесу

Експортуйте або створіть JSON-файл робочого процесу ComfyUI. Запишіть ідентифікатори вузлів для вузла введення prompt і вузла виводу, з якого OpenClaw має читати дані.

* ### Налаштуйте провайдер

Встановіть `mode: "local"` і вкажіть файл вашого робочого процесу. Ось мінімальний приклад для зображень:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Встановіть модель за замовчуванням

Вкажіть для OpenClaw модель `comfy/workflow` для налаштованої можливості:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Перевірте

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**Найкраще підходить для:** запуску робочих процесів у Comfy Cloud без керування локальними GPU-ресурсами.

* ### Отримайте API-ключ

Зареєструйтеся на [comfy.org](<https://comfy.org>) і згенеруйте API-ключ на інформаційній панелі свого облікового запису.

* ### Встановіть API-ключ

Надайте свій ключ одним із цих способів:

bashCopy code
[code]
    # Змінна середовища (рекомендовано)export COMFY_API_KEY="your-key" # Альтернативна змінна середовищаexport COMFY_CLOUD_API_KEY="your-key" # Або безпосередньо в конфігураціїopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Підготуйте JSON вашого робочого процесу

Експортуйте або створіть JSON-файл робочого процесу ComfyUI. Запишіть ідентифікатори вузлів для вузла введення prompt і вузла виводу.

* ### Налаштуйте провайдер

Встановіть `mode: "cloud"` і вкажіть файл вашого робочого процесу:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Встановіть модель за замовчуванням

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Перевірте

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Конфігурація

Comfy підтримує спільні налаштування з’єднання верхнього рівня, а також розділи робочих процесів для кожної можливості (`image`, `video`, `music`):

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Спільні ключі

Key | Type | Description  
---|---|---  
`mode` | `"local"` or `"cloud"` | Режим з’єднання.  
`baseUrl` | string | Типово `http://127.0.0.1:8188` для локального режиму або `https://cloud.comfy.org` для cloud.  
`apiKey` | string | Необов’язковий вбудований ключ, альтернатива змінним середовища `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | Дозволити приватний/LAN `baseUrl` у режимі cloud.  
  
### Ключі для кожної можливості

Ці ключі застосовуються всередині розділів `image`, `video` або `music`:

Key | Required | Default | Description  
---|---|---|---  
`workflow` or `workflowPath` | Yes | \-- | Шлях до JSON-файлу робочого процесу ComfyUI.  
`promptNodeId` | Yes | \-- | Ідентифікатор вузла, який отримує текстовий prompt.  
`promptInputName` | No | `"text"` | Назва входу на вузлі prompt.  
`outputNodeId` | No | \-- | Ідентифікатор вузла, з якого читати результат. Якщо не вказано, використовуються всі відповідні вузли виводу.  
`pollIntervalMs` | No | \-- | Інтервал опитування в мілісекундах для завершення завдання.  
`timeoutMs` | No | \-- | Тайм-аут у мілісекундах для запуску робочого процесу.  
  
Розділи `image` і `video` також підтримують:

Key | Required | Default | Description  
---|---|---|---  
`inputImageNodeId` | Yes (when passing a reference image) | \-- | Ідентифікатор вузла, який отримує завантажене референсне зображення.  
`inputImageInputName` | No | `"image"` | Назва входу на вузлі зображення.  
  
## Деталі робочого процесу

Image workflows

Встановіть типову модель зображень на `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Приклад редагування з референсним зображенням:**

Щоб увімкнути редагування зображень із завантаженим референсним зображенням, додайте `inputImageNodeId` до конфігурації `image`:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Video workflows

Встановіть типову модель відео на `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

Відеоробочі процеси Comfy підтримують text-to-video та image-to-video через налаштований граф.

Music workflows

Вбудований Plugin реєструє провайдер генерації музики для визначених робочим процесом аудіо- або музичних виходів, доступний через спільний інструмент `music_generate`:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Використовуйте розділ конфігурації `music`, щоб вказати JSON вашого аудіоробочого процесу та вузол виводу.

Backward compatibility

Наявна конфігурація зображень верхнього рівня (без вкладеного розділу `image`) усе ще працює:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw розглядає цю застарілу форму як конфігурацію робочого процесу для зображень. Вам не потрібно негайно виконувати міграцію, але для нових налаштувань рекомендовано вкладені розділи `image` / `video` / `music`.

Live tests

Для вбудованого Plugin доступне live-покриття за opt-in:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Live test пропускає окремі сценарії для зображень, відео або музики, якщо не налаштовано відповідний розділ робочого процесу Comfy.

## Пов’язане

[**Генерація зображень** Конфігурація та використання інструмента генерації зображень. ](</uk/tools/image-generation>) [**Генерація відео** Конфігурація та використання інструмента генерації відео. ](</uk/tools/video-generation>) [**Генерація музики** Налаштування інструмента генерації музики та аудіо. ](</uk/tools/music-generation>) [**Каталог провайдерів** Огляд усіх провайдерів і посилань на моделі. ](</uk/providers>) [**Довідник із конфігурації** Повний довідник із конфігурації, включно з типовими значеннями агентів. ](</uk/gateway/config-agents#agent-defaults>)

Was this useful?YesNo