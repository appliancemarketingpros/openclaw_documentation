---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/ru/providers/google
scraped_at: 2026-06-29
---

ModelsProviders

Plugin Google предоставляет доступ к моделям Gemini через Google AI Studio, а также генерацию изображений, понимание медиа (изображения/аудио/видео), преобразование текста в речь и веб-поиск через Gemini Grounding.

  * Поставщик: `google`
  * Аутентификация: `GEMINI_API_KEY` или `GOOGLE_API_KEY`
  * API: Google Gemini API
  * Параметр среды выполнения: provider/model `agentRuntime.id: "google-gemini-cli"` повторно использует OAuth Gemini CLI, сохраняя ссылки на модели каноническими как `google/*`.


## Начало работы

Выберите предпочитаемый способ аутентификации и выполните шаги настройки.

### API key

**Лучше всего для:** стандартного доступа к Gemini API через Google AI Studio.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

Или передайте ключ напрямую:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**Лучше всего для:** повторного использования существующего входа Gemini CLI через PKCE OAuth вместо отдельного API-ключа.

* ### Install the Gemini CLI

Локальная команда `gemini` должна быть доступна в `PATH`.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw поддерживает установки через Homebrew и глобальные установки npm, включая распространенные схемы Windows/npm.

* ### Log in via OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * Модель по умолчанию: `google/gemini-3.1-pro-preview`
  * Среда выполнения: `google-gemini-cli`
  * Псевдоним: `gemini-cli`


Идентификатор модели Gemini 3.1 Pro в Gemini API — `gemini-3.1-pro-preview`. Для удобства OpenClaw принимает более короткий псевдоним `google/gemini-3.1-pro` и нормализует его перед вызовами поставщика.

**Переменные окружения:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(Или варианты `GEMINI_CLI_*`.)

Ссылки на модели `google-gemini-cli/*` являются устаревшими псевдонимами для совместимости. Новые конфигурации должны использовать ссылки на модели `google/*` вместе со средой выполнения `google-gemini-cli`, когда требуется локальное выполнение Gemini CLI.

## Возможности

Возможность | Поддерживается  
---|---  
Чат-завершения | Да  
Генерация изображений | Да  
Генерация музыки | Да  
Преобразование текста в речь | Да  
Голос в реальном времени | Да (Google Live API)  
Понимание изображений | Да  
Транскрипция аудио | Да  
Понимание видео | Да  
Веб-поиск (Grounding) | Да  
Мышление/рассуждение | Да (Gemini 2.5+ / Gemini 3+)  
Модели Gemma 4 | Да  
  
## Веб-поиск

Встроенный поставщик веб-поиска `gemini` использует Grounding Gemini Google Search. Настройте отдельный ключ поиска в `plugins.entries.google.config.webSearch`, или разрешите повторно использовать `models.providers.google.apiKey` после `GEMINI_API_KEY`:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

Приоритет учетных данных: сначала отдельный `webSearch.apiKey`, затем `GEMINI_API_KEY`, затем `models.providers.google.apiKey`. `webSearch.baseUrl` необязателен и предназначен для операторских прокси или совместимых конечных точек Gemini API; если он не указан, веб-поиск Gemini повторно использует `models.providers.google.baseUrl`. См. [поиск Gemini](</ru/tools/gemini-search>) для поведения инструмента, специфичного для поставщика.

## Генерация изображений

Встроенный поставщик генерации изображений `google` по умолчанию использует `google/gemini-3.1-flash-image-preview`.

  * Также поддерживает `google/gemini-3-pro-image-preview`
  * Генерация: до 4 изображений за запрос
  * Режим редактирования: включен, до 5 входных изображений
  * Элементы управления геометрией: `size`, `aspectRatio` и `resolution`


Чтобы использовать Google как поставщика изображений по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## Генерация видео

Встроенный Plugin `google` также регистрирует генерацию видео через общий инструмент `video_generate`.

  * Модель видео по умолчанию: `google/veo-3.1-fast-generate-preview`
  * Режимы: текст-в-видео, изображение-в-видео и потоки с одним видео-референсом
  * Поддерживает `aspectRatio` (`16:9`, `9:16`) и `resolution` (`720P`, `1080P`); аудиовывод сегодня не поддерживается Veo
  * Поддерживаемые длительности: **4, 6 или 8 секунд** (другие значения округляются до ближайшего разрешенного значения)


Чтобы использовать Google как поставщика видео по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## Генерация музыки

Встроенный Plugin `google` также регистрирует генерацию музыки через общий инструмент `music_generate`.

  * Модель музыки по умолчанию: `google/lyria-3-clip-preview`
  * Также поддерживает `google/lyria-3-pro-preview`
  * Элементы управления промптом: `lyrics` и `instrumental`
  * Формат вывода: `mp3` по умолчанию, а также `wav` в `google/lyria-3-pro-preview`
  * Референсные входные данные: до 10 изображений
  * Запуски, поддерживаемые сессиями, отделяются через общий поток задач/статусов, включая `action: "status"`


Чтобы использовать Google как поставщика музыки по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## Преобразование текста в речь

Встроенный поставщик речи `google` использует путь TTS Gemini API с `gemini-3.1-flash-tts-preview`.

  * Голос по умолчанию: `Kore`
  * Аутентификация: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` или `GOOGLE_API_KEY`
  * Вывод: WAV для обычных вложений TTS, Opus для целей голосовых заметок, PCM для Talk/телефонии
  * Вывод голосовых заметок: Google PCM упаковывается как WAV и транскодируется в Opus 48 кГц с помощью `ffmpeg`


Путь пакетного Gemini TTS от Google возвращает сгенерированное аудио в завершенном ответе `generateContent`. Для разговоров с минимальной задержкой используйте поставщика голоса Google в реальном времени на базе Gemini Live API вместо пакетного TTS.

Чтобы использовать Google как поставщика TTS по умолчанию:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          speakerVoice: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS использует промпты на естественном языке для управления стилем. Задайте `audioProfile`, чтобы добавлять повторно используемый стилевой промпт перед произносимым текстом. Задайте `speakerName`, когда текст промпта ссылается на именованного говорящего.

Gemini API TTS также принимает выразительные аудиотеги в квадратных скобках в тексте, например `[whispers]` или `[laughs]`. Чтобы теги не попадали в видимый ответ чата, но отправлялись в TTS, поместите их в блок `[[tts:text]]...[[/tts:text]]`:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## Голос в реальном времени

Встроенный Plugin `google` регистрирует поставщика голоса в реальном времени на базе Gemini Live API для серверных аудиомостов, таких как Voice Call и Google Meet.

Настройка | Путь конфигурации | По умолчанию  
---|---|---  
Модель | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
Голос | `...google.voice` | `Kore`  
Температура | `...google.temperature` | (не задано)  
Чувствительность начала VAD | `...google.startSensitivity` | (не задано)  
Чувствительность завершения VAD | `...google.endSensitivity` | (не задано)  
Длительность тишины | `...google.silenceDurationMs` | (не задано)  
Обработка активности | `...google.activityHandling` | значение Google по умолчанию, `start-of-activity-interrupts`  
Покрытие хода | `...google.turnCoverage` | значение Google по умолчанию, `only-activity`  
Отключить авто-VAD | `...google.automaticActivityDetectionDisabled` | `false`  
Возобновление сессии | `...google.sessionResumption` | `true`  
Сжатие контекста | `...google.contextWindowCompression` | `true`  
API-ключ | `...google.apiKey` | Использует запасной вариант `models.providers.google.apiKey`, `GEMINI_API_KEY` или `GOOGLE_API_KEY`  
  
Пример конфигурации голосовых вызовов в реальном времени:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                speakerVoice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

Для live-проверки сопровождающим запустите `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`. Этот smoke-тест также покрывает серверные/WebRTC-пути OpenAI; ветка Google выпускает тот же ограниченный токен Live API, который используется Control UI Talk, открывает браузерную конечную точку WebSocket, отправляет начальную полезную нагрузку настройки и ожидает `setupComplete`.

## Расширенная конфигурация

Прямое повторное использование кэша Gemini

Для прямых запусков Gemini API (`api: "google-generative-ai"`) OpenClaw передает настроенный дескриптор `cachedContent` в запросы Gemini.

  * Настраивайте параметры для отдельной модели или глобально с помощью `cachedContent` либо устаревшего `cached_content`
  * Если присутствуют оба, приоритет имеет `cachedContent`
  * Пример значения: `cachedContents/prebuilt-context`
  * Использование попаданий в кэш Gemini нормализуется в OpenClaw `cacheRead` из upstream `cachedContentTokenCount`

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Примечания по использованию Gemini CLI

При использовании OAuth-провайдера `google-gemini-cli` OpenClaw по умолчанию использует вывод Gemini CLI `stream-json` и нормализует использование из финальной полезной нагрузки `stats`. Устаревшие переопределения `--output-format json` по-прежнему используют JSON-парсер.

  * Текст потокового ответа берется из событий assistant `message`.
  * Для устаревшего JSON-вывода текст ответа берется из поля CLI JSON `response`.
  * Использование использует запасной вариант `stats`, когда CLI оставляет `usage` пустым.
  * `stats.cached` нормализуется в OpenClaw `cacheRead`.
  * Если `stats.input` отсутствует, OpenClaw выводит входные токены из `stats.input_tokens - stats.cached`.

Настройка окружения и демона

Если Gateway работает как демон (launchd/systemd), убедитесь, что `GEMINI_API_KEY` доступен этому процессу (например, в `~/.openclaw/.env` или через `env.shellEnv`).

## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок на модели и поведения отработки отказа. ](</ru/concepts/model-providers>) [**Генерация изображений** Общие параметры инструмента изображений и выбор провайдера. ](</ru/tools/image-generation>) [**Генерация видео** Общие параметры инструмента видео и выбор провайдера. ](</ru/tools/video-generation>) [**Генерация музыки** Общие параметры инструмента музыки и выбор провайдера. ](</ru/tools/music-generation>)

Was this useful?YesNo

Open issue