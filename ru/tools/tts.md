---
title: Преобразование текста в речь
source_url: https://docs.openclaw.ai/ru/tools/tts
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw может преобразовывать исходящие ответы в аудио через **14 речевых провайдеров** и доставлять нативные голосовые сообщения в Feishu, Matrix, Telegram и WhatsApp, аудиовложения во всех остальных каналах, а также потоки PCM/Ulaw для телефонии и Talk.

TTS — это половина речевого вывода в режиме Talk `stt-tts`. Провайдер-нативные `realtime`-сеансы Talk синтезируют речь внутри realtime-провайдера вместо вызова этого пути TTS, а `transcription`-сеансы не синтезируют голосовой ответ ассистента.

## Быстрый старт

* ### Pick a provider

OpenAI и ElevenLabs — самые надежные размещенные варианты. Microsoft и локальный CLI работают без API-ключа. Полный список см. в матрице провайдеров.

* ### Set the API key

Экспортируйте переменную окружения для своего провайдера (например, `OPENAI_API_KEY`, `ELEVENLABS_API_KEY`). Microsoft и локальному CLI ключ не нужен.

* ### Enable in config

Задайте `messages.tts.auto: "always"` и `messages.tts.provider`:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### Try it in chat

`/tts status` показывает текущее состояние. `/tts audio Hello from OpenClaw` отправляет разовый аудиоответ.

## Поддерживаемые провайдеры

Провайдер | Аутентификация | Примечания  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION` (также `AZURE_SPEECH_API_KEY`, `SPEECH_KEY`, `SPEECH_REGION`) | Нативный вывод голосовых заметок Ogg/Opus и телефония.  
**DeepInfra** | `DEEPINFRA_API_KEY` | TTS, совместимый с OpenAI. По умолчанию `hexgrad/Kokoro-82M`.  
**ElevenLabs** | `ELEVENLABS_API_KEY` или `XI_API_KEY` | Клонирование голоса, многоязычность, детерминированность через `seed`; потоковая передача для голосового воспроизведения в Discord.  
**Google Gemini** | `GEMINI_API_KEY` или `GOOGLE_API_KEY` | Пакетный TTS через Gemini API; учитывает персону через `promptTemplate: "audio-profile-v1"`.  
**Gradium** | `GRADIUM_API_KEY` | Вывод голосовых заметок и телефонии.  
**Inworld** | `INWORLD_API_KEY` | Потоковый TTS API. Нативные голосовые заметки Opus и телефония PCM.  
**Local CLI** | нет | Запускает настроенную локальную команду TTS.  
**Microsoft** | нет | Публичный нейронный TTS Edge через `node-edge-tts`. Best-effort, без SLA.  
**MiniMax** | `MINIMAX_API_KEY` (или Token Plan: `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY`, `MINIMAX_CODING_API_KEY`) | API T2A v2. По умолчанию `speech-2.8-hd`.  
**OpenAI** | `OPENAI_API_KEY` | Также используется для автосводки; поддерживает `instructions` для персоны.  
**OpenRouter** | `OPENROUTER_API_KEY` (можно повторно использовать `models.providers.openrouter.apiKey`) | Модель по умолчанию `hexgrad/kokoro-82m`.  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` или `BYTEPLUS_SEED_SPEECH_API_KEY` (устаревшие AppID/токен: `VOLCENGINE_TTS_APPID`/`_TOKEN`) | HTTP API BytePlus Seed Speech.  
**Vydra** | `VYDRA_API_KEY` | Общий провайдер изображений, видео и речи.  
**xAI** | `XAI_API_KEY` | Пакетный TTS xAI. Нативные голосовые заметки Opus **не** поддерживаются.  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | MiMo TTS через chat completions Xiaomi.  
  
Если настроено несколько провайдеров, выбранный используется первым, а остальные служат резервными вариантами. Автосводка использует `summaryModel` (или `agents.defaults.model.primary`), поэтому этот провайдер также должен быть аутентифицирован, если вы оставляете сводки включенными.

## Конфигурация

Конфигурация TTS находится в `messages.tts` в `~/.openclaw/openclaw.json`. Выберите пресет и адаптируйте блок провайдера:

### Azure Speech

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "azure-speech",  providers: {    "azure-speech": {      apiKey: "${AZURE_SPEECH_KEY}",      region: "eastus",      speakerVoice: "en-US-JennyNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      voiceNoteOutputFormat: "ogg-24khz-16bit-mono-opus",    },  },},},}
[/code]

### ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "elevenlabs",  providers: {    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      speakerVoiceId: "EXAVITQu4vr4xnSDxMaL",    },  },},},}
[/code]

### Google Gemini

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "google",  providers: {    google: {      apiKey: "${GEMINI_API_KEY}",      model: "gemini-3.1-flash-tts-preview",      speakerVoice: "Kore",      // Optional natural-language style prompts:      // audioProfile: "Speak in a calm, podcast-host tone.",      // speakerName: "Alex",    },  },},},}
[/code]

### Gradium

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "gradium",  providers: {    gradium: {      apiKey: "${GRADIUM_API_KEY}",      speakerVoiceId: "YTpq7expH9539ERJ",    },  },},},}
[/code]

### Inworld

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "inworld",  providers: {    inworld: {      apiKey: "${INWORLD_API_KEY}",      modelId: "inworld-tts-1.5-max",      speakerVoiceId: "Sarah",      temperature: 0.7,    },  },},},}
[/code]

### Local CLI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "tts-local-cli",  providers: {    "tts-local-cli": {      command: "say",      args: ["-o", "{{OutputPath}}", "{{Text}}"],      outputFormat: "wav",      timeoutMs: 120000,    },  },},},}
[/code]

### Microsoft (no key)

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "microsoft",  providers: {    microsoft: {      enabled: true,      speakerVoice: "en-US-MichelleNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      rate: "+0%",      pitch: "+0%",    },  },},},}
[/code]

### MiniMax

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "minimax",  providers: {    minimax: {      apiKey: "${MINIMAX_API_KEY}",      model: "speech-2.8-hd",      speakerVoiceId: "English_expressive_narrator",      speed: 1.0,      vol: 1.0,      pitch: 0,    },  },},},}
[/code]

### OpenAI + ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openai",  summaryModel: "openai/gpt-4.1-mini",  modelOverrides: { enabled: true },  providers: {    openai: {      apiKey: "${OPENAI_API_KEY}",      model: "gpt-4o-mini-tts",      speakerVoice: "alloy",    },    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      speakerVoiceId: "EXAVITQu4vr4xnSDxMaL",      voiceSettings: { stability: 0.5, similarityBoost: 0.75, style: 0.0, useSpeakerBoost: true, speed: 1.0 },      applyTextNormalization: "auto",      languageCode: "en",    },  },},},}
[/code]

### OpenRouter

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openrouter",  providers: {    openrouter: {      apiKey: "${OPENROUTER_API_KEY}",      model: "hexgrad/kokoro-82m",      speakerVoice: "af_alloy",      responseFormat: "mp3",    },  },},},}
[/code]

### Volcengine

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "volcengine",  providers: {    volcengine: {      apiKey: "${VOLCENGINE_TTS_API_KEY}",      resourceId: "seed-tts-1.0",      speakerVoice: "en_female_anna_mars_bigtts",    },  },},},}
[/code]

### xAI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xai",  providers: {    xai: {      apiKey: "${XAI_API_KEY}",      speakerVoiceId: "eve",      language: "en",      responseFormat: "mp3",    },  },},},}
[/code]

### Xiaomi MiMo

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xiaomi",  providers: {    xiaomi: {      apiKey: "${XIAOMI_API_KEY}",      model: "mimo-v2.5-tts",      speakerVoice: "mimo_default",      format: "mp3",    },  },},},}
[/code]

Для Xiaomi `mimo-v2.5-tts-voicedesign` опустите `speakerVoice` и задайте `style` как подсказку для дизайна голоса. OpenClaw отправляет эту подсказку как TTS-сообщение `user` и не отправляет `audio.voice` для модели voicedesign.

### Переопределения голоса для отдельных агентов

Используйте `agents.list[].tts`, когда один агент должен говорить с другим провайдером, голосом, моделью, персоной или режимом автоматического TTS. Блок агента глубоко объединяется поверх `messages.tts`, поэтому учетные данные провайдера могут оставаться в глобальной конфигурации провайдера:

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { speakerVoiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

Чтобы закрепить персону для отдельного агента, задайте `agents.list[].tts.persona` вместе с конфигурацией провайдера — она переопределяет глобальную `messages.tts.persona` только для этого агента.

Порядок приоритета для автоматических ответов, `/tts audio`, `/tts status` и инструмента агента `tts`:

  1. `messages.tts`
  2. активная `agents.list[].tts`
  3. переопределение канала, когда канал поддерживает `channels.<channel>.tts`
  4. переопределение учетной записи, когда канал передает `channels.<channel>.accounts.<id>.tts`
  5. локальные настройки `/tts` для этого хоста
  6. встроенные директивы `[[tts:...]]`, когда включены переопределения модели


Переопределения канала и учетной записи используют ту же форму, что и `messages.tts`, и глубоко объединяются поверх предыдущих слоев, поэтому общие учетные данные провайдера могут оставаться в `messages.tts`, а канал или учетная запись бота меняет только голос диктора, модель, персону или автоматический режим:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { speakerVoice: "shimmer" },            },          },        },      },    },  },}
[/code]

## Персоны

**Персона** — это стабильная речевая идентичность, которую можно детерминированно применять у разных провайдеров. Она может предпочитать одного провайдера, определять независимое от провайдера намерение промпта и хранить привязки для конкретных провайдеров: голоса, модели, шаблоны промптов, seed-значения и настройки голоса.

### Минимальная персона

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: {              speakerVoiceId: "EXAVITQu4vr4xnSDxMaL",              modelId: "eleven_multilingual_v2",            },          },        },      },    },  },}
[/code]

### Полная персона (независимый от провайдера промпт)

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              speakerVoice: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", speakerVoice: "cedar" },            elevenlabs: {              speakerVoiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### Разрешение персоны

Активная персона выбирается детерминированно:

  1. локальная настройка `/tts persona <id>`, если задана.
  2. `messages.tts.persona`, если задана.
  3. Без персоны.


Выбор провайдера выполняется по принципу «сначала явные настройки»:

  1. Прямые переопределения (CLI, Gateway, Talk, разрешенные директивы TTS).
  2. локальная настройка `/tts provider <id>`.
  3. `provider` активной персоны.
  4. `messages.tts.provider`.
  5. Автовыбор из реестра.


Для каждой попытки провайдера OpenClaw объединяет конфигурации в таком порядке:

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. доверенные переопределения запроса
  4. разрешенные переопределения директив TTS, сгенерированных моделью


### Как провайдеры используют промпты персон

Поля промпта персоны (`profile`, `scene`, `sampleContext`, `style`, `accent`, `pacing`, `constraints`) **независимы от провайдера**. Каждый провайдер сам решает, как их использовать:

Google Gemini

Оборачивает поля промпта персоны в структуру промпта Gemini TTS **только когда** эффективная конфигурация провайдера Google задает `promptTemplate: "audio-profile-v1"` или `personaPrompt`. Более старые поля `audioProfile` и `speakerName` по-прежнему добавляются в начало как текст промпта, специфичный для Google. Встроенные аудиотеги, такие как `[whispers]` или `[laughs]` внутри блока `[[tts:text]]`, сохраняются внутри транскрипта Gemini; OpenClaw не генерирует эти теги.

OpenAI

Сопоставляет поля промпта персоны с полем запроса `instructions` **только когда** явные OpenAI `instructions` не настроены. Явные `instructions` всегда имеют приоритет.

Другие провайдеры

Используют только привязки персоны для конкретного провайдера в `personas.<id>.providers.<provider>`. Поля промпта персоны игнорируются, если провайдер не реализует собственное сопоставление промпта персоны.

### Политика fallback

`fallbackPolicy` управляет поведением, когда у персоны **нет привязки** для проверяемого провайдера:

Политика | Поведение  
---|---  
`preserve-persona` | **По умолчанию.** Нейтральные к провайдеру поля промпта остаются доступными; провайдер может использовать или игнорировать их.  
`provider-defaults` | Персона исключается из подготовки промпта для этой попытки; провайдер использует свои нейтральные значения по умолчанию, при этом fallback к другим провайдерам продолжается.  
`fail` | Пропустить эту попытку провайдера с `reasonCode: "not_configured"` и `personaBinding: "missing"`. Fallback-провайдеры всё равно пробуются.  
  
Весь TTS-запрос завершается неудачей только тогда, когда **каждый** испробованный провайдер пропущен или завершается ошибкой.

Выбор провайдера сеанса Talk ограничен областью сеанса. Клиент Talk должен выбирать идентификаторы провайдеров, моделей, голосов и локали из `talk.catalog` и передавать их через сеанс Talk или запрос передачи. Открытие голосового сеанса не должно изменять `messages.tts` или глобальные значения провайдера Talk по умолчанию.

## Директивы, управляемые моделью

По умолчанию ассистент **может** выдавать директивы `[[tts:...]]`, чтобы переопределить голос, модель или скорость для одного ответа, а также необязательный блок `[[tts:text]]...[[/tts:text]]` для выразительных подсказок, которые должны появляться только в аудио:

textCopy code
[code]
    Here you go. [[tts:speakerVoiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

Когда `messages.tts.auto` равно `"tagged"`, **директивы обязательны** , чтобы запустить аудио. Потоковая доставка блоков удаляет директивы из видимого текста до того, как канал их увидит, даже если они разделены между соседними блоками.

`provider=...` игнорируется, если не задано `modelOverrides.allowProvider: true`. Когда ответ объявляет `provider=...`, остальные ключи в этой директиве разбираются только этим провайдером; неподдерживаемые ключи удаляются и сообщаются как предупреждения директив TTS.

**Доступные ключи директив:**

  * `provider` (идентификатор зарегистрированного провайдера; требует `allowProvider: true`)
  * `speakerVoice` / `speakerVoiceId` (устаревшие псевдонимы: `voice`, `voiceName`, `voice_name`, `google_voice`, `voiceId`)
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume` (громкость MiniMax, 0–10)
  * `pitch` (целочисленная высота тона MiniMax, −12 до 12; дробные значения отбрасываются)
  * `emotion` (тег эмоции Volcengine)
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**Полностью отключить переопределения модели:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**Разрешить переключение провайдера, сохранив настройку других параметров:**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## Слэш-команды

Одна команда `/tts`. В Discord OpenClaw также регистрирует `/voice`, потому что `/tts` является встроенной командой Discord — текстовая `/tts ...` всё равно работает.

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

Примечания по поведению:

  * `/tts on` записывает локальную настройку TTS в `always`; `/tts off` записывает её в `off`.
  * `/tts chat on|off|default` записывает ограниченное сеансом переопределение авто-TTS для текущего чата.
  * `/tts persona <id>` записывает локальную настройку персоны; `/tts persona off` очищает её.
  * `/tts latest` считывает последний ответ ассистента из транскрипта текущего сеанса и один раз отправляет его как аудио. Он сохраняет только хеш этого ответа в записи сеанса, чтобы подавлять дублирующие голосовые отправки.
  * `/tts audio` создаёт одноразовый аудиоответ (**не** включает TTS).
  * `limit` и `summary` хранятся в **локальных настройках** , а не в основной конфигурации.
  * `/tts status` включает диагностику fallback для последней попытки — `Fallback: <primary> -> <used>`, `Attempts: ...` и подробности по каждой попытке (`provider:outcome(reasonCode) latency`).
  * `/status` показывает активный режим TTS, а также настроенного провайдера, модель, голос и очищенные метаданные пользовательского endpoint, когда TTS включён.


## Пользовательские настройки

Слэш-команды записывают локальные переопределения в `prefsPath`. Значение по умолчанию: `~/.openclaw/settings/tts.json`; переопределите его с помощью env var `OPENCLAW_TTS_PREFS` или `messages.tts.prefsPath`.

Сохранённое поле | Эффект  
---|---  
`auto` | Локальное переопределение авто-TTS (`always`, `off`, …)  
`provider` | Локальное переопределение основного провайдера  
`persona` | Локальное переопределение персоны  
`maxLength` | Порог сводки (по умолчанию `1500` символов)  
`summarize` | Переключатель сводки (по умолчанию `true`)  
  
Они переопределяют эффективную конфигурацию из `messages.tts` плюс активный блок `agents.list[].tts` для этого хоста.

## Форматы вывода (фиксированные)

Доставка голоса TTS определяется возможностями канала. Plugins каналов объявляют, должен ли TTS в стиле голоса запрашивать у провайдеров нативную цель `voice-note` или сохранять обычный синтез `audio-file` и только помечать совместимый вывод для голосовой доставки.

  * **Каналы с поддержкой голосовых заметок** : для ответов голосовыми заметками предпочтителен Opus (`opus_48000_64` от ElevenLabs, `opus` от OpenAI). 
    * 48 кГц / 64 кбит/с — хороший компромисс для голосовых сообщений.
  * **Feishu / WhatsApp** : когда ответ голосовой заметкой создается как MP3/WebM/WAV/M4A или другой вероятный аудиофайл, Plugin канала перекодирует его в 48 кГц Ogg/Opus с помощью `ffmpeg` перед отправкой нативного голосового сообщения. WhatsApp отправляет результат через полезную нагрузку Baileys `audio` с `ptt: true` и `audio/ogg; codecs=opus`. Если преобразование завершается ошибкой, Feishu получает исходный файл как вложение; отправка WhatsApp завершается ошибкой вместо публикации несовместимой полезной нагрузки PTT.
  * **Другие каналы** : MP3 (`mp3_44100_128` от ElevenLabs, `mp3` от OpenAI). 
    * 44,1 кГц / 128 кбит/с — баланс по умолчанию для четкости речи.
  * **MiniMax** : MP3 (модель `speech-2.8-hd`, частота дискретизации 32 кГц) для обычных аудиовложений. Для целей голосовых заметок, объявленных каналом, OpenClaw перекодирует MiniMax MP3 в Opus 48 кГц с помощью `ffmpeg` перед доставкой, когда канал объявляет перекодирование.
  * **Xiaomi MiMo** : по умолчанию MP3 или WAV при соответствующей настройке. Для целей голосовых заметок, объявленных каналом, OpenClaw перекодирует вывод Xiaomi в Opus 48 кГц с помощью `ffmpeg` перед доставкой, когда канал объявляет перекодирование.
  * **Локальный CLI** : использует настроенный `outputFormat`. Цели голосовых заметок преобразуются в Ogg/Opus, а телефонный вывод преобразуется в необработанный моно PCM 16 кГц с помощью `ffmpeg`.
  * **Google Gemini** : Gemini API TTS возвращает необработанный PCM 24 кГц. OpenClaw упаковывает его как WAV для аудиовложений, перекодирует в Opus 48 кГц для целей голосовых заметок и возвращает PCM напрямую для Talk/телефонии.
  * **Gradium** : WAV для аудиовложений, Opus для целей голосовых заметок и `ulaw_8000` при 8 кГц для телефонии.
  * **Inworld** : MP3 для обычных аудиовложений, нативный `OGG_OPUS` для целей голосовых заметок и необработанный `PCM` при 22050 Гц для Talk/телефонии.
  * **xAI** : по умолчанию MP3; `responseFormat` может быть `mp3`, `wav`, `pcm`, `mulaw` или `alaw`. OpenClaw использует пакетную конечную точку REST TTS xAI и возвращает полное аудиовложение; потоковый WebSocket TTS xAI не используется в этом пути провайдера. Нативный формат Opus для голосовых заметок в этом пути не поддерживается.
  * **Microsoft** : использует `microsoft.outputFormat` (по умолчанию `audio-24khz-48kbitrate-mono-mp3`). 
    * Встроенный транспорт принимает `outputFormat`, но не все форматы доступны в сервисе.
    * Значения формата вывода соответствуют форматам вывода Microsoft Speech (включая Ogg/WebM Opus).
    * Telegram `sendVoice` принимает OGG/MP3/M4A; используйте OpenAI/ElevenLabs, если вам нужны гарантированные голосовые сообщения Opus.
    * Если настроенный формат вывода Microsoft завершается ошибкой, OpenClaw повторяет попытку с MP3.


Форматы вывода OpenAI/ElevenLabs фиксированы для каждого канала (см. выше).

## Поведение Auto-TTS

Когда включен `messages.tts.auto`, OpenClaw:

  * Пропускает TTS, если ответ уже содержит структурированные медиа.
  * Пропускает очень короткие ответы (меньше 10 символов).
  * Резюмирует длинные ответы, когда резюме включены, используя `summaryModel` (или `agents.defaults.model.primary`).
  * Прикрепляет созданное аудио к ответу.
  * В `mode: "final"` все равно отправляет TTS только с аудио для потоковых финальных ответов после завершения текстового потока; созданные медиа проходят ту же нормализацию медиа канала, что и обычные вложения ответа.


Если ответ превышает `maxLength`, а резюме выключено (или нет API-ключа для модели резюме), аудио пропускается и отправляется обычный текстовый ответ.

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## Форматы вывода по каналам

Цель | Формат  
---|---  
Feishu / Matrix / Telegram / WhatsApp | Ответы голосовыми заметками предпочитают **Opus** (`opus_48000_64` от ElevenLabs, `opus` от OpenAI). 48 кГц / 64 кбит/с балансирует четкость и размер.  
Другие каналы | **MP3** (`mp3_44100_128` от ElevenLabs, `mp3` от OpenAI). 44,1 кГц / 128 кбит/с по умолчанию для речи.  
Talk / телефония | Нативный для провайдера **PCM** (Inworld 22050 Гц, Google 24 кГц) или `ulaw_8000` от Gradium для телефонии.  
  
Примечания по провайдерам:

  * **Транскодирование Feishu / WhatsApp:** Когда ответ голосовой заметкой приходит как MP3/WebM/WAV/M4A, Plugin канала транскодирует его в 48 кГц Ogg/Opus с помощью `ffmpeg`. WhatsApp отправляет через Baileys с `ptt: true` и `audio/ogg; codecs=opus`. Если преобразование не удается: Feishu откатывается к прикреплению исходного файла; отправка WhatsApp завершается ошибкой вместо публикации несовместимой полезной нагрузки PTT.
  * **MiniMax / Xiaomi MiMo:** MP3 по умолчанию (32 кГц для MiniMax `speech-2.8-hd`); транскодируется в 48 кГц Opus для целей голосовых заметок через `ffmpeg`.
  * **Локальный CLI:** Использует настроенный `outputFormat`. Цели голосовых заметок преобразуются в Ogg/Opus, а телефонный вывод — в необработанный моно PCM 16 кГц.
  * **Google Gemini:** Возвращает необработанный PCM 24 кГц. OpenClaw оборачивает его как WAV для вложений, транскодирует в 48 кГц Opus для целей голосовых заметок, возвращает PCM напрямую для Talk/телефонии.
  * **Inworld:** MP3-вложения, нативный `OGG_OPUS` для голосовых заметок, необработанный `PCM` 22050 Гц для Talk/телефонии.
  * **xAI:** MP3 по умолчанию; `responseFormat` может быть `mp3|wav|pcm|mulaw|alaw`. Использует пакетную REST-конечную точку xAI — потоковый WebSocket TTS **не** используется. Нативный формат Opus для голосовых заметок **не** поддерживается.
  * **Microsoft:** Использует `microsoft.outputFormat` (по умолчанию `audio-24khz-48kbitrate-mono-mp3`). Telegram `sendVoice` принимает OGG/MP3/M4A; используйте OpenAI/ElevenLabs, если вам нужны гарантированные голосовые сообщения Opus. Если настроенный формат Microsoft завершается ошибкой, OpenClaw повторяет попытку с MP3.


Форматы вывода OpenAI и ElevenLabs фиксированы для каждого канала, как указано выше.

## Справочник полей

Top-level messages.tts.*

Режим Auto-TTS. `inbound` отправляет аудио только после входящего голосового сообщения; `tagged` отправляет аудио только когда ответ включает директивы `[[tts:...]]` или блок `[[tts:text]]`.

Устаревший переключатель. `openclaw doctor --fix` переносит его в `auto`.

`"all"` включает ответы инструментов/блоков в дополнение к финальным ответам.

Идентификатор речевого провайдера. Если не задан, OpenClaw использует первый настроенный провайдер в порядке авто-выбора реестра. Устаревшее `provider: "edge"` переписывается в `"microsoft"` командой `openclaw doctor --fix`.

Идентификатор активной персоны из `personas`. Нормализуется к нижнему регистру.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> Стабильная речевая идентичность. Поля: `label`, `description`, `provider`, `fallbackPolicy`, `prompt`, `providers.<provider>`. См. Персоны.

Недорогая модель для автосводки; по умолчанию `agents.defaults.model.primary`. Принимает `provider/model` или настроенный псевдоним модели.

Разрешить модели выдавать директивы TTS. `enabled` по умолчанию равно `true`; `allowProvider` по умолчанию равно `false`.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> Настройки, принадлежащие провайдеру, с ключами по идентификатору речевого провайдера. Устаревшие прямые блоки (`messages.tts.openai`, `.elevenlabs`, `.microsoft`, `.edge`) переписываются командой `openclaw doctor --fix`; коммитьте только `messages.tts.providers.<id>`.

Жесткий лимит символов входного текста TTS. `/tts audio` завершается ошибкой при превышении.

Тайм-аут запроса в миллисекундах.

Переопределить локальный путь JSON настроек (провайдер/лимит/сводка). По умолчанию `~/.openclaw/settings/tts.json`.

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Переменная окружения: `AZURE_SPEECH_KEY`, `AZURE_SPEECH_API_KEY` или `SPEECH_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg Регион Azure Speech (например, `eastus`). Переменная окружения: `AZURE_SPEECH_REGION` или `SPEECH_REGION`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci Необязательное переопределение конечной точки Azure Speech (псевдоним `baseUrl`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg ShortName голоса Azure. По умолчанию `en-US-JennyNeural`. Устаревший псевдоним: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Код языка SSML. По умолчанию `en-US`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` для стандартного аудио. По умолчанию `audio-24khz-48kbitrate-mono-mp3`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Azure `X-Microsoft-OutputFormat` для вывода голосовых заметок. По умолчанию `ogg-24khz-16bit-mono-opus`. OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Откатывается к `ELEVENLABS_API_KEY` или `XI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Идентификатор модели (например, `eleven_multilingual_v2`, `eleven_v3`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZUlkIiB0eXBlPSJzdHJpbmci Идентификатор голоса ElevenLabs. Устаревший псевдоним: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

`stability`, `similarityBoost`, `style` (каждый `0..1`), `useSpeakerBoost` (`true|false`), `speed` (`0.5..2.0`, `1.0` = нормальная).

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg 2-буквенный ISO 639-1 (например, `en`, `de`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI Целое число `0..4294967295` для детерминизма по мере возможности. OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Откатывается к `GEMINI_API_KEY` / `GOOGLE_API_KEY`. Если опущено, TTS может повторно использовать `models.providers.google.apiKey` до отката к переменным окружения. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Модель Gemini TTS. По умолчанию `gemini-3.1-flash-tts-preview`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg Имя готового голоса Gemini. По умолчанию `Kore`. Устаревшие псевдонимы: `voiceName`, `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn Установите `audio-profile-v1`, чтобы обернуть поля запроса активной персоны в детерминированную структуру запроса Gemini TTS. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Принимается только `https://generativelanguage.googleapis.com`. OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Переменная окружения: `GRADIUM_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI По умолчанию `https://api.gradium.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZUlkIiB0eXBlPSJzdHJpbmci По умолчанию Emma (`YTpq7expH9539ERJ`). Устаревший псевдоним: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Основной Inworld

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Переменная окружения: `INWORLD_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI По умолчанию `https://api.inworld.ai`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI По умолчанию `inworld-tts-1.5-max`. Также: `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZUlkIiB0eXBlPSJzdHJpbmci По умолчанию `Sarah`. Устаревший псевдоним: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi Температура сэмплирования `0..2`. OPENCLAW_DOCS_MARKER:paramClose:

Локальный CLI (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg Аргументы команды. Поддерживает плейсхолдеры `{{Text}}`, `{{OutputPath}}`, `{{OutputDir}}`, `{{OutputBase}}`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic Ожидаемый формат вывода CLI. По умолчанию `mp3` для аудиовложений. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Тайм-аут команды в миллисекундах. По умолчанию `120000`. OPENCLAW_DOCS_MARKER:paramClose:

Microsoft (без ключа API)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg Имя нейронного голоса Microsoft (например, `en-US-MichelleNeural`). Устаревший псевдоним: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI Код языка (например, `en-US`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Формат вывода Microsoft. По умолчанию `audio-24khz-48kbitrate-mono-mp3`. Не все форматы поддерживаются встроенным транспортом на базе Edge. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg Процентные строки (например, `+10%`, `-5%`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk Устаревший псевдоним. Запустите `openclaw doctor --fix`, чтобы переписать сохраненную конфигурацию в `providers.microsoft`. OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Использует `MINIMAX_API_KEY` как запасной вариант. Аутентификация Token Plan через `MINIMAX_OAUTH_TOKEN`, `MINIMAX_CODE_PLAN_KEY` или `MINIMAX_CODING_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI По умолчанию `https://api.minimax.io`. Переменная окружения: `MINIMAX_API_HOST`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci По умолчанию `speech-2.8-hd`. Переменная окружения: `MINIMAX_TTS_MODEL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZUlkIiB0eXBlPSJzdHJpbmci По умолчанию `English_expressive_narrator`. Переменная окружения: `MINIMAX_TTS_VOICE_ID`. Устаревший псевдоним: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`. По умолчанию `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`. По умолчанию `1.0`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi Целое число `-12..12`. По умолчанию `0`. Дробные значения усекаются перед запросом. OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Использует `OPENAI_API_KEY` как запасной вариант. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Идентификатор модели OpenAI TTS (например, `gpt-4o-mini-tts`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg Имя голоса (например, `alloy`, `cedar`). Устаревший псевдоним: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg Явное поле OpenAI `instructions`. Если оно задано, поля промпта персоны **не** сопоставляются автоматически. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">Дополнительные поля JSON, объединяемые с телами запросов `/audio/speech` после сгенерированных полей OpenAI TTS. Используйте это для OpenAI-совместимых конечных точек, таких как Kokoro, которым требуются ключи, специфичные для провайдера, например `lang`; небезопасные ключи прототипов игнорируются. OPENCLAW_DOCS_MARKER:paramClose:

Переопределяет конечную точку OpenAI TTS. Порядок разрешения: конфигурация → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`. Значения, отличные от стандартного, считаются OpenAI-совместимыми конечными точками TTS, поэтому пользовательские имена моделей и голосов принимаются.

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Переменная окружения: `OPENROUTER_API_KEY`. Может повторно использовать `models.providers.openrouter.apiKey`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI По умолчанию `https://openrouter.ai/api/v1`. Устаревший `https://openrouter.ai/v1` нормализуется. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci По умолчанию `hexgrad/kokoro-82m`. Псевдоним: `modelId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg По умолчанию `af_alloy`. Устаревшие псевдонимы: `voice`, `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw По умолчанию `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Volcengine (BytePlus Seed Speech)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Переменная окружения: `VOLCENGINE_TTS_API_KEY` или `BYTEPLUS_SEED_SPEECH_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI По умолчанию `seed-tts-1.0`. Переменная окружения: `VOLCENGINE_TTS_RESOURCE_ID`. Используйте `seed-tts-2.0`, если у вашего проекта есть право на TTS 2.0. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg Заголовок ключа приложения. По умолчанию `aGjiRDfUWi`. Переменная окружения: `VOLCENGINE_TTS_APP_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI Переопределяет HTTP-конечную точку Seed Speech TTS. Переменная окружения: `VOLCENGINE_TTS_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg Тип голоса. По умолчанию `en_female_anna_mars_bigtts`. Переменная окружения: `VOLCENGINE_TTS_VOICE`. Устаревший псевдоним: `voice`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ Устаревшие поля Volcengine Speech Console. Переменные окружения: `VOLCENGINE_TTS_APPID`, `VOLCENGINE_TTS_TOKEN`, `VOLCENGINE_TTS_CLUSTER` (по умолчанию `volcano_tts`). OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Переменная окружения: `XAI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI По умолчанию `https://api.x.ai/v1`. Переменная окружения: `XAI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZUlkIiB0eXBlPSJzdHJpbmci По умолчанию `eve`. Доступные рабочие голоса: `ara`, `eve`, `leo`, `rex`, `sal`, `una`. Устаревший псевдоним: `voiceId`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci Код языка BCP-47 или `auto`. По умолчанию `en`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw По умолчанию `mp3`. OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Переменная окружения: `XIAOMI_API_KEY`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI По умолчанию `https://api.xiaomimimo.com/v1`. Переменная окружения: `XIAOMI_BASE_URL`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci По умолчанию `mimo-v2.5-tts`. Переменная окружения: `XIAOMI_TTS_MODEL`. Также поддерживает `mimo-v2-tts` и `mimo-v2.5-tts-voicedesign`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWFrZXJWb2ljZSIgdHlwZT0ic3RyaW5nIg По умолчанию `mimo_default` для моделей с предустановленными голосами. Переменная окружения: `XIAOMI_TTS_VOICE`. Устаревший псевдоним: `voice`. Не отправляется для `mimo-v2.5-tts-voicedesign`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic По умолчанию `mp3`. Переменная окружения: `XIAOMI_TTS_FORMAT`. OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InN0eWxlIiB0eXBlPSJzdHJpbmci Необязательная инструкция стиля на естественном языке, отправляемая как сообщение пользователя; не озвучивается. Для `mimo-v2.5-tts-voicedesign` это промпт проектирования голоса; OpenClaw предоставляет значение по умолчанию, если оно опущено. OPENCLAW_DOCS_MARKER:paramClose:

## Инструмент агента

Инструмент `tts` преобразует текст в речь и возвращает аудиовложение для доставки ответа. В Feishu, Matrix, Telegram и WhatsApp аудио доставляется как голосовое сообщение, а не как вложенный файл. Feishu и WhatsApp могут транскодировать вывод TTS не в формате Opus на этом пути, когда доступен `ffmpeg`.

WhatsApp отправляет аудио через Baileys как голосовую заметку PTT (`audio` с `ptt: true`) и отправляет видимый текст **отдельно** от PTT-аудио, потому что клиенты не всегда корректно отображают подписи к голосовым заметкам.

Инструмент принимает необязательные поля `channel` и `timeoutMs`; `timeoutMs` — это тайм-аут запроса к провайдеру для отдельного вызова в миллисекундах. Значения для отдельного вызова переопределяют `messages.tts.timeoutMs`; настроенные тайм-ауты TTS переопределяют любое значение по умолчанию провайдера, заданное Plugin.

## Gateway RPC

Метод | Назначение  
---|---  
`tts.status` | Читать текущее состояние TTS и последнюю попытку.  
`tts.enable` | Установить локальную автоматическую настройку в `always`.  
`tts.disable` | Установить локальную автоматическую настройку в `off`.  
`tts.convert` | Разовое преобразование текста → аудио.  
`tts.setProvider` | Установить локальную настройку провайдера.  
`tts.setPersona` | Установить локальную настройку персоны.  
`tts.providers` | Список настроенных провайдеров и их статус.  
  
## Ссылки на сервисы

  * [Руководство OpenAI по преобразованию текста в речь](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [Справочник OpenAI Audio API](<https://platform.openai.com/docs/api-reference/audio>)
  * [Azure Speech REST для преобразования текста в речь](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [Провайдер Azure Speech](</ru/providers/azure-speech>)
  * [ElevenLabs Text to Speech](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [Аутентификация ElevenLabs](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</ru/providers/gradium>)
  * [Inworld TTS API](<https://docs.inworld.ai/tts/tts>)
  * [MiniMax T2A v2 API](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [Volcengine TTS HTTP API](</ru/providers/volcengine#text-to-speech>)
  * [Синтез речи Xiaomi MiMo](</ru/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Форматы вывода Microsoft Speech](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [xAI text to speech](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## См. также

  * [Обзор медиа](</ru/tools/media-overview>)
  * [Генерация музыки](</ru/tools/music-generation>)
  * [Генерация видео](</ru/tools/video-generation>)
  * [Слэш-команды](</ru/tools/slash-commands>)
  * [Plugin голосовых вызовов](</ru/plugins/voice-call>)


Was this useful?YesNo

Open issue