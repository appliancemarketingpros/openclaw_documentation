---
title: SenseAudio
source_url: https://docs.openclaw.ai/ru/providers/senseaudio
scraped_at: 2026-06-29
---

ModelsProviders

SenseAudio может расшифровывать входящие аудио и вложения с голосовыми заметками через общий конвейер OpenClaw `tools.media.audio`. OpenClaw отправляет multipart-аудио в OpenAI-совместимый endpoint транскрибации и добавляет возвращенный текст как `{{Transcript}}` плюс блок `[Audio]`.

Свойство | Значение  
---|---  
ID провайдера | `senseaudio`  
Plugin | встроенный, `enabledByDefault: true`  
Контракт | `mediaUnderstandingProviders` (audio)  
Переменная env для auth | `SENSEAUDIO_API_KEY`  
Модель по умолчанию | `senseaudio-asr-pro-1.5-260319`  
URL по умолчанию | `https://api.senseaudio.cn/v1`  
Сайт | [senseaudio.cn](<https://senseaudio.cn>)  
Документация | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Начало работы

* ### Задайте API-ключ

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### Включите аудиопровайдера

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### Отправьте голосовую заметку

Отправьте аудиосообщение через любой подключенный канал. OpenClaw загружает аудио в SenseAudio и использует транскрипт в конвейере ответа.

## Параметры

Параметр | Путь | Описание  
---|---|---  
`model` | `tools.media.audio.models[].model` | ID модели SenseAudio ASR  
`language` | `tools.media.audio.models[].language` | Необязательная подсказка языка  
`prompt` | `tools.media.audio.prompt` | Необязательный prompt транскрибации  
`baseUrl` | `tools.media.audio.baseUrl` or model | Переопределяет OpenAI-совместимую базу  
`headers` | `tools.media.audio.request.headers` | Дополнительные заголовки запроса  
  
## Связанные материалы

  * [Понимание медиа (аудио)](</ru/nodes/audio>)
  * [Провайдеры моделей](</ru/concepts/model-providers>)


Was this useful?YesNo

Open issue