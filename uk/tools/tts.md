---
title: Перетворення тексту на мовлення
source_url: https://docs.openclaw.ai/uk/tools/tts
scraped_at: 2026-05-25
---

OpenClaw може перетворювати вихідні відповіді на аудіо через **14 постачальників мовлення** і надсилати нативні голосові повідомлення у Feishu, Matrix, Telegram і WhatsApp, аудіовкладення всюди деінде, а також потоки PCM/Ulaw для телефонії та Talk.

TTS — це половина виведення мовлення в режимі `stt-tts` Talk. Нативні для постачальника `realtime` сеанси Talk синтезують мовлення всередині постачальника realtime замість виклику цього шляху TTS, тоді як сеанси `transcription` не синтезують голосову відповідь асистента.

## Швидкий старт

* ### Pick a provider

OpenAI та ElevenLabs — найнадійніші розміщені варіанти. Microsoft і локальний CLI працюють без ключа API. Повний список дивіться у матриці постачальників.

* ### Set the API key

Експортуйте змінну середовища для вашого постачальника (наприклад `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`). Microsoft і локальний CLI не потребують ключа.

* ### Enable in config

Задайте `messages.tts.auto: "always"` і `messages.tts.provider`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### Try it in chat

`/tts status` показує поточний стан. `/tts audio Hello from OpenClaw` надсилає одноразову аудіовідповідь.

## Підтримувані постачальники

Постачальник | Автентифікація | Примітки  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (також `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | Нативний вихід голосових нотаток Ogg/Opus і телефонія.  
**DeepInfra** | `DEEPINFRA_API_KEY` | TTS, сумісний з OpenAI. За замовчуванням `hexgrad/Kokoro-82M`.  
**ElevenLabs** | `ELEVENLABS_API_KEY` або `XI_API_KEY` | Клонування голосу, багатомовність, детермінованість через `seed`; потокове відтворення голосу Discord.  
**Google Gemini** | `GEMINI_API_KEY` або `GOOGLE_API_KEY` | Пакетний TTS API Gemini; враховує персону через `promptTemplate: "audio-profile-v1"`.  
**Gradium** | `GRADIUM_API_KEY` | Вихід голосових нотаток і телефонії.  
**Inworld** | `INWORLD_API_KEY` | Потоковий TTS API. Нативні голосові нотатки Opus і телефонія PCM.  
**Локальний CLI** | немає | Запускає налаштовану локальну команду TTS.  
**Microsoft** | немає | Публічний нейронний TTS Edge через `node-edge-tts`. Найкраще зусилля, без SLA.  
**MiniMax** | `MINIMAX_API_KEY` (або Token Plan: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | T2A v2 API. За замовчуванням `speech-2.8-hd`.  
**OpenAI** | `OPENAI_API_KEY` | Також використовується для автоматичного підсумку; підтримує персону `instructions`.  
**OpenRouter** | `OPENROUTER_API_KEY` (може повторно використовувати `models.providers.openrouter.apiKey`) | Модель за замовчуванням `hexgrad/kokoro-82m`.  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` або `BYTEPLUS_SEED_SPEECH_API_KEY` (застарілі AppID/токен: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | HTTP API BytePlus Seed Speech.  
**Vydra** | `VYDRA_API_KEY` | Спільний постачальник зображень, відео та мовлення.  
**xAI** | `XAI_API_KEY` | Пакетний TTS xAI. Нативна голосова нотатка Opus **не** підтримується.  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | MiMo TTS через завершення чату Xiaomi.  
  
Якщо налаштовано кілька постачальників, вибраний використовується першим, а інші є резервними варіантами. Автоматичний підсумок використовує `summaryModel` (або `agents.defaults.model.primary`), тому цей постачальник також має бути автентифікований, якщо ви залишаєте підсумки ввімкненими.

## Конфігурація

Конфігурація TTS міститься в `messages.tts` у `~/.openclaw/openclaw.json`. Виберіть preset і адаптуйте блок постачальника:

### Azure Speech

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "azure-speech",  providers: {    "azure-speech": {      apiKey: "${AZURE_SPEECH_KEY}",      region: "eastus",      voice: "en-US-JennyNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      voiceNoteOutputFormat: "ogg-24khz-16bit-mono-opus",    },  },},},}
[/code]

### ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "elevenlabs",  providers: {    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",    },  },},},}
[/code]

### Google Gemini

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "google",  providers: {    google: {      apiKey: "${GEMINI_API_KEY}",      model: "gemini-3.1-flash-tts-preview",      voiceName: "Kore",      // Optional natural-language style prompts:      // audioProfile: "Speak in a calm, podcast-host tone.",      // speakerName: "Alex",    },  },},},}
[/code]

### Gradium

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "gradium",  providers: {    gradium: {      apiKey: "${GRADIUM_API_KEY}",      voiceId: "YTpq7expH9539ERJ",    },  },},},}
[/code]

### Inworld

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "inworld",  providers: {    inworld: {      apiKey: "${INWORLD_API_KEY}",      modelId: "inworld-tts-1.5-max",      voiceId: "Sarah",      temperature: 0.7,    },  },},},}
[/code]

### Local CLI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "tts-local-cli",  providers: {    "tts-local-cli": {      command: "say",      args: ["-o", "{{OutputPath}}", "{{Text}}"],      outputFormat: "wav",      timeoutMs: 120000,    },  },},},}
[/code]

### Microsoft (no key)

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "microsoft",  providers: {    microsoft: {      enabled: true,      voice: "en-US-MichelleNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      rate: "+0%",      pitch: "+0%",    },  },},},}
[/code]

### MiniMax

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "minimax",  providers: {    minimax: {      apiKey: "${MINIMAX_API_KEY}",      model: "speech-2.8-hd",      voiceId: "English_expressive_narrator",      speed: 1.0,      vol: 1.0,      pitch: 0,    },  },},},}
[/code]

### OpenAI + ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openai",  summaryModel: "openai/gpt-4.1-mini",  modelOverrides: { enabled: true },  providers: {    openai: {      apiKey: "${OPENAI_API_KEY}",      model: "gpt-4o-mini-tts",      voice: "alloy",    },    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",      voiceSettings: { stability: 0.5, similarityBoost: 0.75, style: 0.0, useSpeakerBoost: true, speed: 1.0 },      applyTextNormalization: "auto",      languageCode: "en",    },  },},},}
[/code]

### OpenRouter

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openrouter",  providers: {    openrouter: {      apiKey: "${OPENROUTER_API_KEY}",      model: "hexgrad/kokoro-82m",      voice: "af_alloy",      responseFormat: "mp3",    },  },},},}
[/code]

### Volcengine

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "volcengine",  providers: {    volcengine: {      apiKey: "${VOLCENGINE_TTS_API_KEY}",      resourceId: "seed-tts-1.0",      voice: "en_female_anna_mars_bigtts",    },  },},},}
[/code]

### xAI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xai",  providers: {    xai: {      apiKey: "${XAI_API_KEY}",      voiceId: "eve",      language: "en",      responseFormat: "mp3",    },  },},},}
[/code]

### Xiaomi MiMo

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xiaomi",  providers: {    xiaomi: {      apiKey: "${XIAOMI_API_KEY}",      model: "mimo-v2.5-tts",      voice: "mimo_default",      format: "mp3",    },  },},},}
[/code]

### Перевизначення голосу для окремого агента

Використовуйте `agents.list[].tts`, коли один агент має говорити з іншим постачальником, голосом, моделлю, персоною або режимом Auto-TTS. Блок агента глибоко зливається з `messages.tts`, тому облікові дані постачальника можуть залишатися в глобальній конфігурації постачальника:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

Щоб закріпити персону для окремого агента, задайте `agents.list[].tts.persona` поруч із конфігурацією провайдера — це перевизначає глобальне `messages.tts.persona` лише для цього агента.

Порядок пріоритету для автоматичних відповідей, `/tts audio`, `/tts status` та агентського інструмента `tts`:

  1. `messages.tts`
  2. активне `agents.list[].tts`
  3. перевизначення каналу, коли канал підтримує `channels.<channel>.tts`
  4. перевизначення облікового запису, коли канал передає `channels.<channel>.accounts.<id>.tts`
  5. локальні налаштування `/tts` для цього хоста
  6. вбудовані директиви `[[tts:...]]`, коли ввімкнено перевизначення моделі


Перевизначення каналу й облікового запису використовують ту саму форму, що й `messages.tts`, і глибоко зливаються з попередніми шарами, тож спільні облікові дані провайдера можуть залишатися в `messages.tts`, а канал або обліковий запис бота змінює лише голос, модель, персону або автоматичний режим:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

## Персони

**Персона** — це стабільна мовлена ідентичність, яку можна детерміновано застосовувати між провайдерами. Вона може надавати перевагу одному провайдеру, визначати провайдерно-нейтральний намір промпта та містити прив’язки для конкретних провайдерів: голоси, моделі, шаблони промптів, зерна та налаштування голосу.

### Мінімальна персона

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL", modelId: "eleven_multilingual_v2" },          },        },      },    },  },}
[/code]

### Повна персона (провайдерно-нейтральний промпт)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              voiceName: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", voice: "cedar" },            elevenlabs: {              voiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### Розв’язання персони

Активна персона вибирається детерміновано:

  1. локальне налаштування `/tts persona <id>`, якщо задано.
  2. `messages.tts.persona`, якщо задано.
  3. Без персони.


Вибір провайдера виконується за принципом «явні налаштування першими»:

  1. Прямі перевизначення (CLI, Gateway, Talk, дозволені TTS-директиви).
  2. локальне налаштування `/tts provider <id>`.
  3. `provider` активної персони.
  4. `messages.tts.provider`.
  5. Автовибір із реєстру.


Для кожної спроби провайдера OpenClaw зливає конфігурації в такому порядку:

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. Довірені перевизначення запиту
  4. Дозволені перевизначення TTS-директив, згенерованих моделлю


### Як провайдери використовують промпти персони

Поля промпта персони (`profile`, `scene`, `sampleContext`, `style`, `accent`, `pacing`, `constraints`) є **провайдерно-нейтральними**. Кожен провайдер вирішує, як їх використовувати:

Google Gemini

Обгортає поля промпта персони у структуру промпта Gemini TTS **лише тоді** , коли ефективна конфігурація провайдера Google задає `promptTemplate: "audio-profile-v1"` або `personaPrompt`. Старіші поля `audioProfile` і `speakerName` усе ще додаються на початок як специфічний для Google текст промпта. Вбудовані аудіотеги, як-от `[whispers]` або `[laughs]`, усередині блока `[[tts:text]]` зберігаються в транскрипті Gemini; OpenClaw не генерує ці теги.

OpenAI

Зіставляє поля промпта персони з полем запиту `instructions` **лише тоді** , коли явні OpenAI `instructions` не налаштовано. Явні `instructions` завжди мають пріоритет.

Інші провайдери

Використовують лише специфічні для провайдера прив’язки персони в `personas.<id>.providers.<provider>`. Поля промпта персони ігноруються, якщо провайдер не реалізує власне зіставлення промпта персони.

### Політика резервного переходу

`fallbackPolicy` керує поведінкою, коли персона **не має прив’язки** для провайдера, що пробується:

Політика | Поведінка  
---|---  
`preserve-persona` | **Типово.** Провайдерно-нейтральні поля промпта залишаються доступними; провайдер може використати їх або проігнорувати.  
`provider-defaults` | Персону опущено з підготовки промпта для цієї спроби; провайдер використовує свої нейтральні типові значення, а резервний перехід до інших провайдерів продовжується.  
`fail` | Пропускає цю спробу провайдера з `reasonCode: "not_configured"` і `personaBinding: "missing"`. Резервні провайдери все ще пробуються.  
  
Увесь TTS-запит завершується помилкою лише тоді, коли **кожного** спробуваного провайдера пропущено або він завершується помилкою.

Вибір провайдера сесії Talk обмежений сесією. Клієнт Talk має вибирати ідентифікатори провайдерів, моделей, голосів і локалі з `talk.catalog` та передавати їх через сесію Talk або запит handoff. Відкриття голосової сесії не повинно змінювати `messages.tts` або глобальні стандартні налаштування провайдера Talk.

## Директиви, керовані моделлю

За замовчуванням асистент **може** надсилати директиви `[[tts:...]]`, щоб перевизначити голос, модель або швидкість для однієї відповіді, а також необов’язковий блок `[[tts:text]]...[[/tts:text]]` для виразних підказок, які мають з’являтися лише в аудіо:

textCopy code
[code]
    Here you go. [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

Коли `messages.tts.auto` має значення `"tagged"`, **директиви обов’язкові** , щоб запустити аудіо. Потокове доставлення блоків вилучає директиви з видимого тексту до того, як канал їх побачить, навіть якщо вони розділені між сусідніми блоками.

`provider=...` ігнорується, якщо не задано `modelOverrides.allowProvider: true`. Коли відповідь оголошує `provider=...`, інші ключі в цій директиві обробляються лише цим провайдером; непідтримувані ключі вилучаються і повідомляються як попередження директив TTS.

**Доступні ключі директив:**

  * `provider` (ідентифікатор зареєстрованого провайдера; потребує `allowProvider: true`)
  * `voice` / `voiceName` / `voice_name` / `google_voice` / `voiceId`
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (гучність MiniMax, 0–10)
  * `pitch` (цілочисельна висота тону MiniMax, від −12 до 12; дробові значення обрізаються)
  * `emotion` (тег емоції Volcengine)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**Повністю вимкнути перевизначення моделлю:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**Дозволити перемикання провайдера, залишивши інші параметри налаштовуваними:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## Slash-команди

Одна команда `/tts`. У Discord OpenClaw також реєструє `/voice`, оскільки `/tts` є вбудованою командою Discord — текстова `/tts ...` усе ще працює.

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

Примітки щодо поведінки:

  * `/tts on` записує локальне налаштування TTS як `always`; `/tts off` записує його як `off`.
  * `/tts chat on|off|default` записує перевизначення auto-TTS, обмежене сесією, для поточного чату.
  * `/tts persona <id>` записує локальне налаштування персони; `/tts persona off` очищує його.
  * `/tts latest` читає останню відповідь асистента з поточного транскрипта сесії та один раз надсилає її як аудіо. Він зберігає лише хеш цієї відповіді в записі сесії, щоб пригнічувати дублікати голосових надсилань.
  * `/tts audio` генерує одноразову аудіовідповідь (це **не** вмикає TTS).
  * `limit` і `summary` зберігаються в **локальних налаштуваннях** , а не в основній конфігурації.
  * `/tts status` містить діагностику fallback для останньої спроби — `Fallback: <primary> -> <used>`, `Attempts: ...` і деталі для кожної спроби (`provider:outcome(reasonCode) latency`).
  * `/status` показує активний режим TTS, а також налаштовані провайдер, модель, голос і очищені метадані користувацького endpoint, коли TTS увімкнено.


## Налаштування для кожного користувача

Slash-команди записують локальні перевизначення в `prefsPath`. Типове значення — `~/.openclaw/settings/tts.json`; перевизначте його за допомогою змінної середовища `OPENCLAW_TTS_PREFS` або `messages.tts.prefsPath`.

Збережене поле | Ефект  
---|---  
`auto` | Локальне перевизначення auto-TTS (`always`, `off`, …)  
`provider` | Локальне перевизначення основного провайдера  
`persona` | Локальне перевизначення персони  
`maxLength` | Поріг підсумку (типово `1500` символів)  
`summarize` | Перемикач підсумку (типово `true`)  
  
Вони перевизначають ефективну конфігурацію з `messages.tts` плюс активний блок `agents.list[].tts` для цього хоста.

## Формати виведення (фіксовані)

Доставлення голосу TTS керується можливостями каналу. Plugins каналів оголошують, чи має voice-style TTS запитувати в провайдерів нативну ціль `voice-note`, чи зберігати звичайний синтез `audio-file` і лише позначати сумісний вивід для голосового доставлення.

  * **Канали з підтримкою голосових нотаток** : відповіді голосовими нотатками надають перевагу Opus (`opus_48000_64` від ElevenLabs, `opus` від OpenAI). 
    * 48 кГц / 64 кбіт/с — вдалий компроміс для голосових повідомлень.
  * **Feishu / WhatsApp** : коли відповідь голосовою нотаткою створено як MP3/WebM/WAV/M4A або інший імовірний аудіофайл, Plugin каналу перекодовує її у 48 кГц Ogg/Opus за допомогою `ffmpeg` перед надсиланням нативного голосового повідомлення. WhatsApp надсилає результат через payload `audio` Baileys з `ptt: true` і `audio/ogg; codecs=opus`. Якщо конвертація не вдається, Feishu отримує оригінальний файл як вкладення; надсилання WhatsApp завершується помилкою замість публікації несумісного payload PTT.
  * **Інші канали** : MP3 (`mp3_44100_128` від ElevenLabs, `mp3` від OpenAI). 
    * 44,1 кГц / 128 кбіт/с — стандартний баланс для чіткості мовлення.
  * **MiniMax** : MP3 (модель `speech-2.8-hd`, частота дискретизації 32 кГц) для звичайних аудіовкладень. Для оголошених каналом цілей голосових нотаток OpenClaw перекодовує MiniMax MP3 у 48 кГц Opus за допомогою `ffmpeg` перед доставленням, коли канал оголошує перекодування.
  * **Xiaomi MiMo** : MP3 за замовчуванням або WAV, якщо налаштовано. Для оголошених каналом цілей голосових нотаток OpenClaw перекодовує вивід Xiaomi у 48 кГц Opus за допомогою `ffmpeg` перед доставленням, коли канал оголошує перекодування.
  * **Локальний CLI** : використовує налаштований `outputFormat`. Цілі голосових нотаток конвертуються в Ogg/Opus, а телефонний вивід конвертується в сирий 16 кГц mono PCM за допомогою `ffmpeg`.
  * **Google Gemini** : Gemini API TTS повертає сирий 24 кГц PCM. OpenClaw обгортає його як WAV для аудіовкладень, перекодовує його у 48 кГц Opus для цілей голосових нотаток і повертає PCM напряму для Talk/телефонії.
  * **Gradium** : WAV для аудіовкладень, Opus для цілей голосових нотаток і `ulaw_8000` на 8 кГц для телефонії.
  * **Inworld** : MP3 для звичайних аудіовкладень, нативний `OGG_OPUS` для цілей голосових нотаток і сирий `PCM` на 22050 Гц для Talk/телефонії.
  * **xAI** : MP3 за замовчуванням; `responseFormat` може бути `mp3`, `wav`, `pcm`, `mulaw` або `alaw`. OpenClaw використовує batch REST TTS endpoint xAI і повертає повне аудіовкладення; streaming TTS WebSocket xAI не використовується цим шляхом провайдера. Нативний формат голосових нотаток Opus не підтримується цим шляхом.
  * **Microsoft** : використовує `microsoft.outputFormat` (за замовчуванням `audio-24khz-48kbitrate-mono-mp3`). 
    * Вбудований транспорт приймає `outputFormat`, але не всі формати доступні в сервісі.
    * Значення формату виводу відповідають форматам виводу Microsoft Speech (зокрема Ogg/WebM Opus).
    * Telegram `sendVoice` приймає OGG/MP3/M4A; використовуйте OpenAI/ElevenLabs, якщо вам потрібні гарантовані голосові повідомлення Opus.
    * Якщо налаштований формат виводу Microsoft не спрацьовує, OpenClaw повторює спробу з MP3.


Формати виводу OpenAI/ElevenLabs фіксовані для кожного каналу (див. вище).

## Поведінка Auto-TTS

Коли ввімкнено `messages.tts.auto`, OpenClaw:

  * Пропускає TTS, якщо відповідь уже містить медіа або директиву `MEDIA:`.
  * Пропускає дуже короткі відповіді (менше 10 символів).
  * Підсумовує довгі відповіді, коли підсумки ввімкнені, використовуючи `summaryModel` (або `agents.defaults.model.primary`).
  * Додає згенероване аудіо до відповіді.
  * У `mode: "final"` все одно надсилає audio-only TTS для потокових фінальних відповідей після завершення текстового потоку; згенероване медіа проходить ту саму нормалізацію медіа каналу, що й звичайні вкладення відповіді.


Якщо відповідь перевищує `maxLength` і підсумок вимкнено (або немає API key для моделі підсумку), аудіо пропускається, а надсилається звичайна текстова відповідь.

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / MEDIA: / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## Формати виводу за каналом

Ціль | Формат  
---|---  
Feishu / Matrix / Telegram / WhatsApp | Відповіді голосовими нотатками надають перевагу **Opus** (`opus_48000_64` від ElevenLabs, `opus` від OpenAI). 48 кГц / 64 кбіт/с балансують чіткість і розмір.  
Інші канали | **MP3** (`mp3_44100_128` від ElevenLabs, `mp3` від OpenAI). 44,1 кГц / 128 кбіт/с — стандарт для мовлення.  
Talk / телефонія | Нативний для провайдера **PCM** (Inworld 22050 Гц, Google 24 кГц) або `ulaw_8000` від Gradium для телефонії.  
  
Примітки за провайдерами:

  * **Перекодування Feishu / WhatsApp:** Коли відповідь голосовою нотаткою надходить як MP3/WebM/WAV/M4A, Plugin каналу перекодовує її у 48 кГц Ogg/Opus за допомогою `ffmpeg`. WhatsApp надсилає через Baileys з `ptt: true` і `audio/ogg; codecs=opus`. Якщо конвертація не вдається: Feishu повертається до прикріплення оригінального файлу; надсилання WhatsApp завершується помилкою замість публікації несумісного payload PTT.
  * **MiniMax / Xiaomi MiMo:** MP3 за замовчуванням (32 кГц для MiniMax `speech-2.8-hd`); перекодовується у 48 кГц Opus для цілей голосових нотаток через `ffmpeg`.
  * **Локальний CLI:** Використовує налаштований `outputFormat`. Цілі голосових нотаток конвертуються в Ogg/Opus, а телефонний вивід — у сирий 16 кГц mono PCM.
  * **Google Gemini:** Повертає сирий 24 кГц PCM. OpenClaw обгортає як WAV для вкладень, перекодовує у 48 кГц Opus для цілей голосових нотаток, повертає PCM напряму для Talk/телефонії.
  * **Inworld:** MP3-вкладення, нативна голосова нотатка `OGG_OPUS`, сирий `PCM` 22050 Гц для Talk/телефонії.
  * **xAI:** MP3 за замовчуванням; `responseFormat` може бути `mp3|wav|pcm|mulaw|alaw`. Використовує batch REST endpoint xAI — streaming WebSocket TTS **не** використовується. Нативний формат голосових нотаток Opus **не** підтримується.
  * **Microsoft:** Використовує `microsoft.outputFormat` (за замовчуванням `audio-24khz-48kbitrate-mono-mp3`). Telegram `sendVoice` приймає OGG/MP3/M4A; використовуйте OpenAI/ElevenLabs, якщо вам потрібні гарантовані голосові повідомлення Opus. Якщо налаштований формат Microsoft не спрацьовує, OpenClaw повторює спробу з MP3.


Формати виводу OpenAI та ElevenLabs фіксовані для кожного каналу, як зазначено вище.

## Довідник полів

Top-level messages.tts.*

Режим Auto-TTS. `inbound` надсилає аудіо лише після вхідного голосового повідомлення; `tagged` надсилає аудіо лише тоді, коли відповідь містить директиви `[[tts:...]]` або блок `[[tts:text]]`.

Застарілий перемикач. `openclaw doctor --fix` переносить це в `auto`.

`"all"` включає відповіді tool/block на додачу до фінальних відповідей.

Ідентифікатор мовленнєвого провайдера. Якщо не задано, OpenClaw використовує першого налаштованого провайдера в порядку автоматичного вибору registry. Застаріле `provider: "edge"` переписується на `"microsoft"` командою `openclaw doctor --fix`.

Ідентифікатор активної персони з `personas`. Нормалізується до нижнього регістру.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> Стабільна мовленнєва ідентичність. Поля: `label`, `description`, `provider`, `fallbackPolicy`, `prompt`, `providers.<provider>`. Див. Персони.

Дешева модель для автоматичного підсумку; за замовчуванням `agents.defaults.model.primary`. Приймає `provider/model` або налаштований псевдонім моделі.

Дозволити моделі випускати директиви TTS. `enabled` за замовчуванням має значення `true`; `allowProvider` за замовчуванням має значення `false`.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> Налаштування, що належать провайдеру, індексовані ідентифікатором мовленнєвого провайдера. Застарілі прямі блоки (`messages.tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) переписуються командою `openclaw doctor --fix`; комітьте лише `messages.tts.providers.<id>`.

Жорстке обмеження для символів вхідного тексту TTS. `/tts audio` завершується помилкою, якщо його перевищено.

Тайм-аут запиту в мілісекундах.

Перевизначає локальний шлях JSON prefs (провайдер/ліміт/підсумок). За замовчуванням `~/.openclaw/settings/tts.json`.

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` або `SPEECH_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg Регіон Azure Speech (наприклад, `eastus`). Env: `AZURE_SPEECH_REGION` або `SPEECH_REGION`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci Необов'язкове перевизначення endpoint Azure Speech (псевдонім `baseUrl`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci ShortName голосу Azure. За замовчуванням `en-US-JennyNeural`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Код мови SSML. За замовчуванням `en-US`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` для стандартного аудіо. За замовчуванням `audio-24khz-48kbitrate-mono-mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` для виводу голосових нотаток. За замовчуванням `ogg-24khz-16bit-mono-opus`. OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Повертається до `ELEVENLABS_API_KEY` або `XI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Ідентифікатор моделі (наприклад, `eleven_multilingual_v2`, `eleven_v3`). OPENCLAW_DOCS_MARKER:paramClose:

`stability`, `similarityBoost`, `style` (кожне `0..1`), `useSpeakerBoost` (`true|false`), `speed` (`0.5..2.0`, `1.0` = нормально).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg 2-літерний ISO 639-1 (наприклад, `en`, `de`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI Ціле число `0..4294967295` для детермінізму best-effort. OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Повертається до `GEMINI_API_KEY` / `GOOGLE_API_KEY`. Якщо пропущено, TTS може повторно використати `models.providers.google.apiKey` перед fallback до env. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Модель Gemini TTS. За замовчуванням `gemini-3.1-flash-tts-preview`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTmFtZSIgdHlwZT0ic3RyaW5nIg Назва готового голосу Gemini. За замовчуванням `Kore`. Псевдонім: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn Установіть `audio-profile-v1`, щоб обгорнути активні поля підказки персони в детерміновану структуру підказки Gemini TTS. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Приймається лише `https://generativelanguage.googleapis.com`. OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Типове значення `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Типове значення Emma (`YTpq7expH9539ERJ`). OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Основний Inworld

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Типове значення `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI Типове значення `inworld-tts-1.5-max`. Також: `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Типове значення `Sarah`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi Температура семплювання `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

Local CLI (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg Аргументи команди. Підтримує заповнювачі `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic Очікуваний формат виводу CLI. Типове значення `mp3` для аудіовкладень. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Час очікування команди в мілісекундах. Типове значення `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (no API key)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Назва нейронного голосу Microsoft (наприклад, `en-US-MichelleNeural`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Код мови (наприклад, `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Формат виводу Microsoft. Типове значення `audio-24khz-48kbitrate-mono-mp3`. Не всі формати підтримуються вбудованим транспортом на основі Edge. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg Відсоткові рядки (наприклад, `+10%`, `-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk Застарілий псевдонім. Запустіть `openclaw doctor --fix`, щоб переписати збережену конфігурацію на `providers.microsoft`. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Повертається до `MINIMAX_API_KEY`. Автентифікація Token Plan через `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY` або `MINIMAX_CODING_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Типове значення `https://api.minimax.io`. Env: `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Типове значення `speech-2.8-hd`. Env: `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Типове значення `English_expressive_narrator`. Env: `MINIMAX_TTS_VOICE_ID`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`. Типове значення `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`. Типове значення `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi Ціле число `-12..12`. Типове значення `0`. Дробові значення обрізаються перед запитом. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Повертається до `OPENAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Ідентифікатор моделі OpenAI TTS (наприклад, `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Назва голосу (наприклад, `alloy`, `cedar`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg Явне поле OpenAI `instructions`. Якщо його задано, поля промпту персони **не** зіставляються автоматично. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">Додаткові JSON-поля, які об’єднуються в тіла запитів `/audio/speech` після згенерованих полів OpenAI TTS. Використовуйте це для сумісних з OpenAI кінцевих точок, як-от Kokoro, що потребують специфічних для провайдера ключів на кшталт `lang`; небезпечні ключі прототипу ігноруються. OPENCLAW_DOCS_MARKER:paramClose:

Перевизначає кінцеву точку OpenAI TTS. Порядок визначення: конфігурація → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. Нетипові значення розглядаються як сумісні з OpenAI кінцеві точки TTS, тому власні назви моделей і голосів приймаються.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `OPENROUTER_API_KEY`. Може повторно використовувати `models.providers.openrouter.apiKey`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Типове значення `https://openrouter.ai/api/v1`. Застаріле `https://openrouter.ai/v1` нормалізується. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Типове значення `hexgrad/kokoro-82m`. Псевдонім: `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Типове значення `af_alloy`. Псевдонім: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw Типове значення `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `VOLCENGINE_TTS_API_KEY` або `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI Типове значення `seed-tts-1.0`. Env: `VOLCENGINE_TTS_RESOURCE_ID`. Використовуйте `seed-tts-2.0`, якщо ваш проєкт має право на TTS 2.0. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg Заголовок ключа застосунку. Типове значення `aGjiRDfUWi`. Env: `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Перевизначає HTTP-кінцеву точку Seed Speech TTS. Env: `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Тип голосу. Типове значення `en_female_anna_mars_bigtts`. Env: `VOLCENGINE_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ Застарілі поля Volcengine Speech Console. Env: `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (типове значення `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Типове значення `https://api.x.ai/v1`. Env: `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI Типове значення `eve`. Живі голоси: `ara`, `eve`, `leo`, `rex`, `sal`, `una`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci Код мови BCP-47 або `auto`. Типове значення `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw Типове значення `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env: `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Типове значення `https://api.xiaomimimo.com/v1`. Env: `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Типове значення `mimo-v2.5-tts`. Env: `XIAOMI_TTS_MODEL`. Також підтримує `mimo-v2-tts`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Типове значення `mimo_default`. Env: `XIAOMI_TTS_VOICE`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic Типове значення `mp3`. Env: `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

## Інструмент агента

Інструмент `tts` перетворює текст на мовлення та повертає аудіовкладення для доставки відповіді. У Feishu, Matrix, Telegram і WhatsApp аудіо доставляється як голосове повідомлення, а не як файлове вкладення. Feishu і WhatsApp можуть перекодувати вивід TTS не у форматі Opus на цьому шляху, коли `ffmpeg` доступний.

WhatsApp надсилає аудіо через Baileys як голосову нотатку PTT (`audio` з `ptt: true`) і надсилає видимий текст **окремо** від PTT-аудіо, оскільки клієнти не завжди стабільно відображають підписи до голосових нотаток.

Інструмент приймає необов’язкові поля `channel` і `timeoutMs`; `timeoutMs` — це час очікування запиту до провайдера для кожного виклику в мілісекундах.

## Gateway RPC

Метод | Призначення  
---|---  
`tts.status` | Прочитати поточний стан TTS і останню спробу.  
`tts.enable` | Установити локальну автоматичну перевагу на `always`.  
`tts.disable` | Установити локальну автоматичну перевагу на `off`.  
`tts.convert` | Одноразове перетворення текст → аудіо.  
`tts.setProvider` | Установити локальну перевагу провайдера.  
`tts.setPersona` | Установити локальну перевагу персони.  
`tts.providers` | Перелічити налаштованих провайдерів і стан.  
  
## Посилання на сервіси

  * [Посібник OpenAI з перетворення тексту на мовлення](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [Довідник OpenAI Audio API](<https://platform.openai.com/docs/api-reference/audio>)
  * [Перетворення тексту на мовлення Azure Speech REST](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [Провайдер Azure Speech](</uk/providers/azure-speech>)
  * [Перетворення тексту на мовлення ElevenLabs](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [Автентифікація ElevenLabs](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</uk/providers/gradium>)
  * [Inworld TTS API](<https://docs.inworld.ai/tts/tts>)
  * [MiniMax T2A v2 API](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [Volcengine TTS HTTP API](</uk/providers/volcengine#text-to-speech>)
  * [Синтез мовлення Xiaomi MiMo](</uk/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Формати виводу Microsoft Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [Перетворення тексту на мовлення xAI](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## Пов’язане

  * [Огляд медіа](</uk/tools/media-overview>)
  * [Генерація музики](</uk/tools/music-generation>)
  * [Генерація відео](</uk/tools/video-generation>)
  * [Команди зі скісною рискою](</uk/tools/slash-commands>)
  * [Plugin голосових викликів](</uk/plugins/voice-call>)


Was this useful?YesNo