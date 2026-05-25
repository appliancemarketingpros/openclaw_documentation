---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/uk/providers/google
scraped_at: 2026-05-25
---

Plugin Google надає доступ до моделей Gemini через Google AI Studio, а також генерацію зображень, розуміння медіа (зображення/аудіо/відео), перетворення тексту на мовлення та вебпошук через Gemini Grounding.

  * Провайдер: `google`
  * Автентифікація: `GEMINI_API_KEY` або `GOOGLE_API_KEY`
  * API: Google Gemini API
  * Параметр середовища виконання: provider/model `agentRuntime.id: "google-gemini-cli"` повторно використовує OAuth Gemini CLI, зберігаючи посилання на моделі канонічними як `google/*`.


## Початок роботи

Виберіть бажаний метод автентифікації та виконайте кроки налаштування.

### Ключ API

**Найкраще для:** стандартного доступу до Gemini API через Google AI Studio.

* ### Запустіть онбординг

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

Або передайте ключ напряму:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### Установіть модель за замовчуванням

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**Найкраще для:** повторного використання наявного входу Gemini CLI через PKCE OAuth замість окремого ключа API.

* ### Установіть Gemini CLI

Локальна команда `gemini` має бути доступна в `PATH`.

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw підтримує як встановлення через Homebrew, так і глобальні встановлення npm, зокрема поширені макети Windows/npm.

* ### Увійдіть через OAuth

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * Модель за замовчуванням: `google/gemini-3.1-pro-preview`
  * Середовище виконання: `google-gemini-cli`
  * Псевдонім: `gemini-cli`


Ідентифікатор моделі Gemini API для Gemini 3.1 Pro — `gemini-3.1-pro-preview`. OpenClaw приймає коротший `google/gemini-3.1-pro` як зручний псевдонім і нормалізує його перед викликами провайдера.

**Змінні середовища:**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


(Або варіанти `GEMINI_CLI_*`.)

Посилання на моделі `google-gemini-cli/*` є застарілими псевдонімами сумісності. Нові конфігурації мають використовувати посилання на моделі `google/*` разом із середовищем виконання `google-gemini-cli`, коли потрібне локальне виконання Gemini CLI.

## Можливості

Можливість | Підтримується  
---|---  
Завершення чату | Так  
Генерація зображень | Так  
Генерація музики | Так  
Перетворення тексту на мовлення | Так  
Голос у реальному часі | Так (Google Live API)  
Розуміння зображень | Так  
Транскрибування аудіо | Так  
Розуміння відео | Так  
Вебпошук (Grounding) | Так  
Мислення/міркування | Так (Gemini 2.5+ / Gemini 3+)  
Моделі Gemma 4 | Так  
  
## Вебпошук

Вбудований провайдер вебпошуку `gemini` використовує grounding Google Search у Gemini. Налаштуйте окремий ключ пошуку в `plugins.entries.google.config.webSearch`, або дозвольте повторно використати `models.providers.google.apiKey` після `GEMINI_API_KEY`:

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

Пріоритет облікових даних: окремий `webSearch.apiKey`, потім `GEMINI_API_KEY`, потім `models.providers.google.apiKey`. `webSearch.baseUrl` є необов’язковим і існує для операторських проксі або сумісних кінцевих точок Gemini API; якщо його опущено, вебпошук Gemini повторно використовує `models.providers.google.baseUrl`. Див. [Пошук Gemini](</uk/tools/gemini-search>) щодо поведінки інструмента, специфічної для провайдера.

## Генерація зображень

Вбудований провайдер генерації зображень `google` за замовчуванням використовує `google/gemini-3.1-flash-image-preview`.

  * Також підтримує `google/gemini-3-pro-image-preview`
  * Генерація: до 4 зображень на запит
  * Режим редагування: увімкнено, до 5 вхідних зображень
  * Елементи керування геометрією: `size`, `aspectRatio` і `resolution`


Щоб використовувати Google як провайдера зображень за замовчуванням:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## Генерація відео

Вбудований Plugin `google` також реєструє генерацію відео через спільний інструмент `video_generate`.

  * Модель відео за замовчуванням: `google/veo-3.1-fast-generate-preview`
  * Режими: текст-у-відео, зображення-у-відео та потоки з посиланням на одне відео
  * Підтримує `aspectRatio` (`16:9`, `9:16`) і `resolution` (`720P`, `1080P`); виведення аудіо наразі не підтримується Veo
  * Підтримувані тривалості: **4, 6 або 8 секунд** (інші значення округлюються до найближчого дозволеного значення)


Щоб використовувати Google як провайдера відео за замовчуванням:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## Генерація музики

Вбудований Plugin `google` також реєструє генерацію музики через спільний інструмент `music_generate`.

  * Модель музики за замовчуванням: `google/lyria-3-clip-preview`
  * Також підтримує `google/lyria-3-pro-preview`
  * Елементи керування промптом: `lyrics` і `instrumental`
  * Формат виводу: `mp3` за замовчуванням, плюс `wav` у `google/lyria-3-pro-preview`
  * Вхідні посилання: до 10 зображень
  * Запуски на основі сесії від’єднуються через спільний потік завдань/статусу, зокрема `action: "status"`


Щоб використовувати Google як провайдера музики за замовчуванням:

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## Перетворення тексту на мовлення

Вбудований мовленнєвий провайдер `google` використовує шлях TTS Gemini API з `gemini-3.1-flash-tts-preview`.

  * Голос за замовчуванням: `Kore`
  * Автентифікація: `messages.tts.providers.google.apiKey`, `models.providers.google.apiKey`, `GEMINI_API_KEY` або `GOOGLE_API_KEY`
  * Вивід: WAV для звичайних вкладень TTS, Opus для цілей голосових нотаток, PCM для Talk/телефонії
  * Вивід голосових нотаток: Google PCM обгортається як WAV і транскодується у 48 кГц Opus за допомогою `ffmpeg`


Пакетний шлях Gemini TTS від Google повертає згенероване аудіо в завершеній відповіді `generateContent`. Для розмов із мовленням із найнижчою затримкою використовуйте провайдера голосу Google у реальному часі на основі Gemini Live API замість пакетного TTS.

Щоб використовувати Google як провайдера TTS за замовчуванням:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS використовує промпти природною мовою для керування стилем. Установіть `audioProfile`, щоб додавати багаторазовий промпт стилю перед озвучуваним текстом. Установіть `speakerName`, коли текст промпта посилається на названого мовця.

Gemini API TTS також приймає виразні аудіотеги у квадратних дужках у тексті, як-от `[whispers]` або `[laughs]`. Щоб теги не потрапляли до видимої відповіді чату, але надсилалися до TTS, помістіть їх у блок `[[tts:text]]...[[/tts:text]]`:

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## Голос у реальному часі

Вбудований Plugin `google` реєструє провайдера голосу в реальному часі на основі Gemini Live API для бекенд-мостів аудіо, таких як Voice Call і Google Meet.

Налаштування | Шлях конфігурації | Типове значення  
---|---|---  
Модель | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
Голос | `...google.voice` | `Kore`  
Температура | `...google.temperature` | (не задано)  
Чутливість початку VAD | `...google.startSensitivity` | (не задано)  
Чутливість завершення VAD | `...google.endSensitivity` | (не задано)  
Тривалість тиші | `...google.silenceDurationMs` | (не задано)  
Обробка активності | `...google.activityHandling` | типове значення Google, `start-of-activity-interrupts`  
Покриття репліки | `...google.turnCoverage` | типове значення Google, `only-activity`  
Вимкнути автоматичний VAD | `...google.automaticActivityDetectionDisabled` | `false`  
Відновлення сеансу | `...google.sessionResumption` | `true`  
Стиснення контексту | `...google.contextWindowCompression` | `true`  
API-ключ | `...google.apiKey` | Повертається до `models.providers.google.apiKey`, `GEMINI_API_KEY` або `GOOGLE_API_KEY`  
  
Приклад realtime-конфігурації Voice Call:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

Для live-перевірки мейнтейнером запустіть `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`. Smoke також покриває шляхи бекенду OpenAI/WebRTC; гілка Google створює ту саму форму обмеженого токена Live API, яку використовує Control UI Talk, відкриває браузерну кінцеву точку WebSocket, надсилає початкове setup-навантаження та очікує на `setupComplete`.

## Розширена конфігурація

Direct Gemini cache reuse

Для прямих запусків Gemini API (`api: "google-generative-ai"`) OpenClaw передає налаштований дескриптор `cachedContent` до запитів Gemini.

  * Налаштуйте параметри для окремої моделі або глобальні параметри за допомогою `cachedContent` чи застарілого `cached_content`
  * Якщо присутні обидва, перевагу має `cachedContent`
  * Приклад значення: `cachedContents/prebuilt-context`
  * Використання cache-hit Gemini нормалізується в OpenClaw `cacheRead` з upstream `cachedContentTokenCount`

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Gemini CLI JSON usage notes

Під час використання OAuth-провайдера `google-gemini-cli` OpenClaw нормалізує JSON-вивід CLI так:

  * Текст відповіді береться з поля CLI JSON `response`.
  * Використання повертається до `stats`, коли CLI залишає `usage` порожнім.
  * `stats.cached` нормалізується в OpenClaw `cacheRead`.
  * Якщо `stats.input` відсутній, OpenClaw виводить вхідні токени з `stats.input_tokens - stats.cached`.

Environment and daemon setup

Якщо Gateway працює як демон (launchd/systemd), переконайтеся, що `GEMINI_API_KEY` доступний цьому процесу (наприклад, у `~/.openclaw/.env` або через `env.shellEnv`).

## Пов’язане

[**Model selection** Вибір провайдерів, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Image generation** Спільні параметри інструмента зображень і вибір провайдера. ](</uk/tools/image-generation>) [**Video generation** Спільні параметри інструмента відео та вибір провайдера. ](</uk/tools/video-generation>) [**Music generation** Спільні параметри інструмента музики та вибір провайдера. ](</uk/tools/music-generation>)

Was this useful?YesNo