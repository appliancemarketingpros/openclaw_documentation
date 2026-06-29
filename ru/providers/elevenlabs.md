---
title: ElevenLabs
source_url: https://docs.openclaw.ai/ru/providers/elevenlabs
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw использует ElevenLabs для синтеза речи, пакетного распознавания речи с Scribe v2 и потокового распознавания речи с Scribe v2 Realtime.

Возможность | Интерфейс OpenClaw | По умолчанию  
---|---|---  
Синтез речи | `messages.tts` / `talk` | `eleven_multilingual_v2`  
Пакетное распознавание речи | `tools.media.audio` | `scribe_v2`  
Потоковое распознавание речи | Потоковая передача Voice Call или Google Meet `realtime.transcriptionProvider` | `scribe_v2_realtime`  
  
## Аутентификация

Задайте `ELEVENLABS_API_KEY` в окружении. `XI_API_KEY` также принимается для совместимости с существующими инструментами ElevenLabs.

bashCopy code
[code]
    export ELEVENLABS_API_KEY="..."
[/code]

## Синтез речи

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        elevenlabs: {          apiKey: "${ELEVENLABS_API_KEY}",          speakerVoiceId: "pMsXgVXv3BLzUgSXRplE",          modelId: "eleven_multilingual_v2",        },      },    },  },}
[/code]

Задайте для `modelId` значение `eleven_v3`, чтобы использовать ElevenLabs v3 TTS. OpenClaw сохраняет `eleven_multilingual_v2` вариантом по умолчанию для существующих установок.

Голосовые каналы Discord используют потоковую конечную точку TTS ElevenLabs, когда ElevenLabs выбран как провайдер `voice.tts`/`messages.tts`. Воспроизведение начинается из возвращенного аудиопотока, а не после того, как OpenClaw сначала загрузит и запишет весь аудиофайл. `latencyTier` сопоставляется с параметром запроса ElevenLabs `optimize_streaming_latency` для моделей, которые его принимают; OpenClaw пропускает этот параметр для `eleven_v3`, которая его отклоняет.

## Распознавание речи

Используйте Scribe v2 для входящих аудиовложений и коротких записанных голосовых фрагментов:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "elevenlabs", model: "scribe_v2" }],      },    },  },}
[/code]

OpenClaw отправляет multipart-аудио в ElevenLabs `/v1/speech-to-text` с `model_id: "scribe_v2"`. Подсказки языка сопоставляются с `language_code`, если присутствуют.

## Потоковое распознавание речи

Встроенный `elevenlabs` Plugin регистрирует Scribe v2 Realtime для потоковой транскрипции Voice Call и Google Meet в режиме агента.

Настройка | Путь конфигурации | По умолчанию  
---|---|---  
Ключ API | `plugins.entries.voice-call.config.streaming.providers.elevenlabs.apiKey` | Использует резервно `ELEVENLABS_API_KEY` / `XI_API_KEY`  
Модель | `...elevenlabs.modelId` | `scribe_v2_realtime`  
Формат аудио | `...elevenlabs.audioFormat` | `ulaw_8000`  
Частота дискретизации | `...elevenlabs.sampleRate` | `8000`  
Стратегия коммита | `...elevenlabs.commitStrategy` | `vad`  
Язык | `...elevenlabs.languageCode` | (не задано)  
  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "elevenlabs",            providers: {              elevenlabs: {                apiKey: "${ELEVENLABS_API_KEY}",                audioFormat: "ulaw_8000",                commitStrategy: "vad",                languageCode: "en",              },            },          },        },      },    },  },}
[/code]

Для режима агента Google Meet задайте `plugins.entries.google-meet.config.realtime.transcriptionProvider` значение `"elevenlabs"` и настройте тот же блок провайдера в `plugins.entries.google-meet.config.realtime.providers.elevenlabs`.

## Связанные материалы

  * [Синтез речи](</ru/tools/tts>)
  * [Google Meet](</ru/plugins/google-meet>)
  * [Выбор модели](</ru/concepts/model-providers>)


Was this useful?YesNo

Open issue