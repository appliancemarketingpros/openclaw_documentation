---
title: MiniMax
source_url: https://docs.openclaw.ai/ru/providers/minimax
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw по умолчанию использует **MiniMax M3** для провайдера MiniMax.

MiniMax также предоставляет:

  * Встроенный синтез речи через T2A v2
  * Встроенное понимание изображений через `MiniMax-VL-01`
  * Встроенную генерацию музыки через `music-2.6`
  * Встроенный `web_search` через поисковый API MiniMax Token Plan


Разделение провайдеров:

ID провайдера | Аутентификация | Возможности  
---|---|---  
`minimax` | API-ключ | Текст, генерация изображений, генерация музыки, генерация видео, понимание изображений, речь, веб-поиск  
`minimax-portal` | OAuth | Текст, генерация изображений, генерация музыки, генерация видео, понимание изображений, речь  
  
## Встроенный каталог

Модель | Тип | Описание  
---|---|---  
`MiniMax-M3` | Чат (reasoning) | Стандартная размещенная модель reasoning  
`MiniMax-M2.7` | Чат (reasoning) | Предыдущая размещенная модель reasoning  
`MiniMax-M2.7-highspeed` | Чат (reasoning) | Более быстрый уровень reasoning M2.7  
`MiniMax-VL-01` | Vision | Модель понимания изображений  
`image-01` | Генерация изображений | Редактирование text-to-image и image-to-image  
`music-2.6` | Генерация музыки | Стандартная модель для музыки  
`music-2.5` | Генерация музыки | Предыдущий уровень генерации музыки  
`music-2.0` | Генерация музыки | Устаревший уровень генерации музыки  
`MiniMax-Hailuo-2.3` | Генерация видео | Потоки text-to-video и ссылок на изображения  
  
## Начало работы

Выберите предпочитаемый способ аутентификации и выполните шаги настройки.

### OAuth (Coding Plan)

**Лучше всего подходит для:** быстрой настройки MiniMax Coding Plan через OAuth; API-ключ не требуется.

### International

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-global-oauth
[/code]

Это выполняет аутентификацию через `api.minimax.io`.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax-portal
[/code]

### China

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-cn-oauth
[/code]

Это выполняет аутентификацию через `api.minimaxi.com`.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax-portal
[/code]

### API key

**Лучше всего подходит для:** размещенного MiniMax с API, совместимым с Anthropic.

### International

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-global-api
[/code]

Это настраивает `api.minimax.io` как базовый URL.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax
[/code]

### China

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice minimax-cn-api
[/code]

Это настраивает `api.minimaxi.com` как базовый URL.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider minimax
[/code]

### Пример конфигурации

json5Copy code
[code]
    {  env: { MINIMAX_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "minimax/MiniMax-M3" } } },  models: {    mode: "merge",    providers: {      minimax: {        baseUrl: "https://api.minimax.io/anthropic",        apiKey: "${MINIMAX_API_KEY}",        api: "anthropic-messages",        models: [          {            id: "MiniMax-M3",            name: "MiniMax M3",            reasoning: true,            input: ["text", "image"],            cost: { input: 0.6, output: 2.4, cacheRead: 0.12, cacheWrite: 0 },            contextWindow: 1000000,            maxTokens: 131072,          },          {            id: "MiniMax-M2.7",            name: "MiniMax M2.7",            reasoning: true,            input: ["text"],            cost: { input: 0.3, output: 1.2, cacheRead: 0.06, cacheWrite: 0.375 },            contextWindow: 204800,            maxTokens: 131072,          },          {            id: "MiniMax-M2.7-highspeed",            name: "MiniMax M2.7 Highspeed",            reasoning: true,            input: ["text"],            cost: { input: 0.6, output: 2.4, cacheRead: 0.06, cacheWrite: 0.375 },            contextWindow: 204800,            maxTokens: 131072,          },        ],      },    },  },}
[/code]

## Настройка через `openclaw configure`

Используйте интерактивный мастер конфигурации, чтобы настроить MiniMax без редактирования JSON:

* ### Launch the wizard

bashCopy code
[code]
    openclaw configure
[/code]

* ### Select Model/auth

Выберите **Model/auth** в меню.

* ### Choose a MiniMax auth option

Выберите один из доступных вариантов MiniMax:

Вариант аутентификации | Описание  
---|---  
`minimax-global-oauth` | Международный OAuth (Coding Plan)  
`minimax-cn-oauth` | Китайский OAuth (Coding Plan)  
`minimax-global-api` | Международный API-ключ  
`minimax-cn-api` | Китайский API-ключ  
  
* ### Pick your default model

Выберите модель по умолчанию при появлении запроса.

## Возможности

### Генерация изображений

Plugin MiniMax регистрирует модель `image-01` для инструмента `image_generate`. Она поддерживает:

  * **Генерацию text-to-image** с управлением соотношением сторон
  * **Редактирование image-to-image** (ссылка на объект) с управлением соотношением сторон
  * До **9 выходных изображений** на запрос
  * До **1 референсного изображения** на запрос редактирования
  * Поддерживаемые соотношения сторон: `1:1`, `16:9`, `4:3`, `3:2`, `2:3`, `3:4`, `9:16`, `21:9`


Чтобы использовать MiniMax для генерации изображений, задайте его как провайдера генерации изображений:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: { primary: "minimax/image-01" },    },  },}
[/code]

Plugin использует тот же `MINIMAX_API_KEY` или OAuth-аутентификацию, что и текстовые модели. Если MiniMax уже настроен, дополнительная конфигурация не нужна.

И `minimax`, и `minimax-portal` регистрируют `image_generate` с одной и той же моделью `image-01`. Настройки с API-ключом используют `MINIMAX_API_KEY`; настройки OAuth могут вместо этого использовать встроенный путь аутентификации `minimax-portal`.

Генерация изображений всегда использует выделенную конечную точку MiniMax для изображений (`/v1/image_generation`) и игнорирует `models.providers.minimax.baseUrl`, поскольку это поле настраивает базовый URL для чата/совместимости с Anthropic. Задайте `MINIMAX_API_HOST=https://api.minimaxi.com`, чтобы направлять генерацию изображений через конечную точку CN; глобальная конечная точка по умолчанию: `https://api.minimax.io`.

Когда onboarding или настройка API-ключа записывает явные записи `models.providers.minimax`, OpenClaw материализует `MiniMax-M3`, `MiniMax-M2.7` и `MiniMax-M2.7-highspeed` как чат-модели. M3 объявляет поддержку текстового и графического ввода; понимание изображений остается отдельно доступным через принадлежащего Plugin медиапровайдера `MiniMax-VL-01`.

### Text-to-speech

Встроенный Plugin `minimax` регистрирует MiniMax T2A v2 как провайдера речи для `messages.tts`.

  * Модель TTS по умолчанию: `speech-2.8-hd`
  * Голос по умолчанию: `English_expressive_narrator`
  * Поддерживаемые встроенные id моделей включают `speech-2.8-hd`, `speech-2.8-turbo`, `speech-2.6-hd`, `speech-2.6-turbo`, `speech-02-hd`, `speech-02-turbo`, `speech-01-hd` и `speech-01-turbo`.
  * Разрешение аутентификации: сначала `messages.tts.providers.minimax.apiKey`, затем профили OAuth/токен-аутентификации `minimax-portal`, затем ключи среды Token Plan (`MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`), затем `MINIMAX_API_KEY`.
  * Если хост TTS не настроен, OpenClaw повторно использует настроенный OAuth-хост `minimax-portal` и удаляет суффиксы пути, совместимые с Anthropic, такие как `/anthropic`.
  * Обычные аудиовложения остаются в MP3.
  * Целевые voice-note, такие как Feishu и Telegram, транскодируются из MP3 MiniMax в Opus 48 кГц с помощью `ffmpeg`, потому что файловый API Feishu/Lark принимает только `file_type: "opus"` для нативных аудиосообщений.
  * MiniMax T2A принимает дробные `speed` и `vol`, но `pitch` отправляется как целое число; OpenClaw отбрасывает дробную часть значений `pitch` перед API-запросом.


Настройка | Переменная среды | По умолчанию | Описание  
---|---|---|---  
`messages.tts.providers.minimax.baseUrl` | `MINIMAX_API_HOST` | `https://api.minimax.io` | Хост API MiniMax T2A.  
`messages.tts.providers.minimax.model` | `MINIMAX_TTS_MODEL` | `speech-2.8-hd` | id модели TTS.  
`messages.tts.providers.minimax.speakerVoiceId` | `MINIMAX_TTS_VOICE_ID` | `English_expressive_narrator` | id голоса, используемый для речевого вывода.  
`messages.tts.providers.minimax.speed` |  | `1.0` | Скорость воспроизведения, `0.5..2.0`.  
`messages.tts.providers.minimax.vol` |  | `1.0` | Громкость, `(0, 10]`.  
`messages.tts.providers.minimax.pitch` |  | `0` | Целочисленный сдвиг высоты тона, `-12..12`.  
  
### Генерация музыки

Встроенный Plugin MiniMax регистрирует генерацию музыки через общий инструмент `music_generate` как для `minimax`, так и для `minimax-portal`.

  * Модель музыки по умолчанию: `minimax/music-2.6`
  * Музыкальная модель OAuth: `minimax-portal/music-2.6`
  * Также поддерживает `minimax/music-2.5` и `minimax/music-2.0`
  * Параметры prompt: `lyrics`, `instrumental`
  * Формат вывода: `mp3`
  * Запуски с поддержкой сессий отсоединяются через общий поток задач/статусов, включая `action: "status"`


Чтобы использовать MiniMax как поставщика музыки по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "minimax/music-2.6",      },    },  },}
[/code]

### Генерация видео

Встроенный Plugin MiniMax регистрирует генерацию видео через общий инструмент `video_generate` как для `minimax`, так и для `minimax-portal`.

  * Модель видео по умолчанию: `minimax/MiniMax-Hailuo-2.3`
  * Видеомодель OAuth: `minimax-portal/MiniMax-Hailuo-2.3`
  * Режимы: преобразование текста в видео и потоки с одной эталонной картинкой
  * Поддерживает `aspectRatio` и `resolution`


Чтобы использовать MiniMax как поставщика видео по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "minimax/MiniMax-Hailuo-2.3",      },    },  },}
[/code]

### Понимание изображений

Plugin MiniMax регистрирует понимание изображений отдельно от текстового каталога:

ID поставщика | Модель изображений по умолчанию  
---|---  
`minimax` | `MiniMax-VL-01`  
`minimax-portal` | `MiniMax-VL-01`  
  
Поэтому автоматическая маршрутизация медиа может использовать понимание изображений MiniMax, даже когда встроенный каталог текстовых поставщиков также включает chat refs M3 с поддержкой изображений.

### Веб-поиск

Plugin MiniMax также регистрирует `web_search` через поисковый API MiniMax Token Plan.

  * ID поставщика: `minimax`
  * Структурированные результаты: заголовки, URL, фрагменты, связанные запросы
  * Предпочтительная переменная окружения: `MINIMAX_CODE_PLAN_KEY`
  * Допустимые псевдонимы переменных окружения: `MINIMAX_CODING_API_KEY`, `MINIMAX_OAUTH_TOKEN`
  * Резервная совместимость: `MINIMAX_API_KEY`, когда она уже указывает на учетные данные token-plan
  * Повторное использование региона: `plugins.entries.minimax.config.webSearch.region`, затем `MINIMAX_API_HOST`, затем базовые URL поставщика MiniMax
  * Поиск остается на ID поставщика `minimax`; настройка OAuth для CN/global может косвенно направлять регион через `models.providers.minimax-portal.baseUrl` и предоставлять bearer-аутентификацию через `MINIMAX_OAUTH_TOKEN`


Конфигурация находится в `plugins.entries.minimax.config.webSearch.*`.

## Расширенная конфигурация

Параметры конфигурации

Параметр | Описание  
---|---  
`models.providers.minimax.baseUrl` | Предпочитайте `https://api.minimax.io/anthropic` (совместимо с Anthropic); `https://api.minimax.io/v1` необязательно для payload, совместимых с OpenAI  
`models.providers.minimax.api` | Предпочитайте `anthropic-messages`; `openai-completions` необязательно для payload, совместимых с OpenAI  
`models.providers.minimax.apiKey` | API-ключ MiniMax (`MINIMAX_API_KEY`)  
`models.providers.minimax.models` | Определяет `id`, `name`, `reasoning`, `contextWindow`, `maxTokens`, `cost`  
`agents.defaults.models` | Назначает псевдонимы моделям, которые вы хотите включить в allowlist  
`models.mode` | Оставьте `merge`, если хотите добавить MiniMax вместе со встроенными моделями  
  
Значения thinking по умолчанию

При `api: "anthropic-messages"` OpenClaw добавляет `thinking: { type: "disabled" }` для моделей MiniMax M2.x, если thinking уже не задан явно в params/config.

Это предотвращает выдачу `reasoning_content` потоковой конечной точкой M2.x в delta-чанках в стиле OpenAI, что привело бы к утечке внутреннего reasoning в видимый вывод.

MiniMax-M3 (и M3.x) исключен: M3 выводит корректные блоки thinking Anthropic и возвращает пустой массив `content` с `stop_reason: "end_turn"`, когда thinking отключен, поэтому wrapper оставляет M3 на пропущенном/адаптивном пути thinking поставщика.

Быстрый режим

`/fast on` или `params.fastMode: true` переписывает `MiniMax-M2.7` в `MiniMax-M2.7-highspeed` на потоковом пути, совместимом с Anthropic.

Пример fallback

**Лучше всего для:** держать самую сильную модель последнего поколения основной, с переключением на MiniMax M2.7 при сбое. Пример ниже использует Opus как конкретную основную модель; замените ее на предпочитаемую основную модель последнего поколения.

json5Copy code
[code]
    {  env: { MINIMAX_API_KEY: "sk-..." },  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": { alias: "primary" },        "minimax/MiniMax-M2.7": { alias: "minimax" },      },      model: {        primary: "anthropic/claude-opus-4-6",        fallbacks: ["minimax/MiniMax-M2.7"],      },    },  },}
[/code]

Сведения об использовании Coding Plan

  * API использования Coding Plan: `https://api.minimaxi.com/v1/token_plan/remains` или `https://api.minimax.io/v1/token_plan/remains` (требуется ключ coding plan).
  * Опрос использования выводит host из `models.providers.minimax-portal.baseUrl` или `models.providers.minimax.baseUrl`, если они настроены, поэтому глобальные настройки с `https://api.minimax.io/anthropic` опрашивают `api.minimax.io`. Отсутствующие или некорректные базовые URL сохраняют fallback CN для совместимости.
  * OpenClaw нормализует использование MiniMax coding-plan к тому же отображению `% left`, которое используется другими поставщиками. Сырые поля MiniMax `usage_percent` / `usagePercent` означают оставшуюся квоту, а не израсходованную, поэтому OpenClaw инвертирует их. Поля на основе счетчиков имеют приоритет, когда присутствуют.
  * Когда API возвращает `model_remains`, OpenClaw предпочитает запись chat-модели, при необходимости выводит метку окна из `start_time` / `end_time` и включает имя выбранной модели в метку плана, чтобы окна coding-plan было проще различать.
  * Снимки использования рассматривают `minimax`, `minimax-cn` и `minimax-portal` как одну и ту же квотную поверхность MiniMax и предпочитают сохраненный OAuth MiniMax перед fallback к переменным окружения ключа Coding Plan.


## Примечания

  * Model refs следуют пути аутентификации: 
    * Настройка API-ключа: `minimax/<model>`
    * Настройка OAuth: `minimax-portal/<model>`
  * Chat-модель по умолчанию: `MiniMax-M3`
  * Альтернативные chat-модели: `MiniMax-M2.7`, `MiniMax-M2.7-highspeed`
  * Онбординг и прямая настройка API-ключа записывают определения моделей для M3 и обоих вариантов M2.7
  * Понимание изображений использует принадлежащий Plugin медиапоставщик `MiniMax-VL-01`
  * Обновите значения цен в `models.json`, если вам нужен точный учет стоимости
  * Используйте `openclaw models list`, чтобы подтвердить текущий ID поставщика, затем переключитесь с помощью `openclaw models set minimax/MiniMax-M3` или `openclaw models set minimax-portal/MiniMax-M3`


## Устранение неполадок

"Unknown model: minimax/MiniMax-M3"

Обычно это означает, что **поставщик MiniMax не настроен** (нет подходящей записи поставщика и не найден профиль аутентификации MiniMax/ключ окружения). Исправление этого обнаружения есть в **2026.1.12**. Исправьте так:

  * Обновитесь до **2026.1.12** (или запустите из исходного кода `main`), затем перезапустите gateway.
  * Запустите `openclaw configure` и выберите вариант аутентификации **MiniMax** , или
  * Добавьте соответствующий блок `models.providers.minimax` или `models.providers.minimax-portal` вручную, или
  * Задайте `MINIMAX_API_KEY`, `MINIMAX_OAUTH_TOKEN` или профиль аутентификации MiniMax, чтобы можно было внедрить соответствующего поставщика.


Убедитесь, что ID модели **чувствителен к регистру** :

  * Путь API-ключа: `minimax/MiniMax-M3`, `minimax/MiniMax-M2.7` или `minimax/MiniMax-M2.7-highspeed`
  * Путь OAuth: `minimax-portal/MiniMax-M3`, `minimax-portal/MiniMax-M2.7` или `minimax-portal/MiniMax-M2.7-highspeed`


Затем повторно проверьте с помощью:

bashCopy code
[code]
    openclaw models list
[/code]

## Связанные разделы

[**Выбор модели** Выбор поставщиков, model refs и поведения при failover. ](</ru/concepts/model-providers>) [**Генерация изображений** Общие параметры инструмента изображений и выбор поставщика. ](</ru/tools/image-generation>) [**Генерация музыки** Общие параметры музыкального инструмента и выбор поставщика. ](</ru/tools/music-generation>) [**Генерация видео** Общие параметры видеоинструмента и выбор поставщика. ](</ru/tools/video-generation>) [**Поиск MiniMax** Конфигурация веб-поиска через MiniMax Token Plan. ](</ru/tools/minimax-search>) [**Устранение неполадок** Общее устранение неполадок и FAQ. ](</ru/help/troubleshooting>)

Was this useful?YesNo

Open issue