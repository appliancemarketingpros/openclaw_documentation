---
title: SenseAudio
source_url: https://docs.openclaw.ai/uk/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio може транскрибувати вхідні аудіо- та голосові вкладення через спільний конвеєр OpenClaw `tools.media.audio`. OpenClaw надсилає multipart-аудіо до OpenAI-сумісної кінцевої точки транскрипції та вставляє повернений текст як `{{Transcript}}` разом із блоком `[Audio]`.

Властивість | Значення  
---|---  
Ідентифікатор провайдера | `senseaudio`  
Plugin | вбудований, `enabledByDefault: true`  
Контракт | `mediaUnderstandingProviders` (аудіо)  
Змінна середовища автентифікації | `SENSEAUDIO_API_KEY`  
Модель за замовчуванням | `senseaudio-asr-pro-1.5-260319`  
URL за замовчуванням | `https://api.senseaudio.cn/v1`  
Вебсайт | [senseaudio.cn](<https://senseaudio.cn>)  
Документація | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Початок роботи

* ### Налаштуйте свій API-ключ

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### Увімкніть аудіопровайдера

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### Надішліть голосове повідомлення

Надішліть аудіоповідомлення через будь-який підключений канал. OpenClaw завантажує аудіо до SenseAudio і використовує транскрипт у конвеєрі відповіді.

## Параметри

Параметр | Шлях | Опис  
---|---|---  
`model` | `tools.media.audio.models[].model` | Ідентифікатор моделі ASR SenseAudio  
`language` | `tools.media.audio.models[].language` | Необов’язкова підказка мови  
`prompt` | `tools.media.audio.prompt` | Необов’язкова підказка транскрипції  
`baseUrl` | `tools.media.audio.baseUrl` або модель | Перевизначити OpenAI-сумісну базу  
`headers` | `tools.media.audio.request.headers` | Додаткові заголовки запиту  
  
## Пов’язане

  * [Розуміння медіа (аудіо)](</uk/nodes/audio>)
  * [Провайдери моделей](</uk/concepts/model-providers>)


Was this useful?YesNo