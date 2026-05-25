---
title: SenseAudio
source_url: https://docs.openclaw.ai/tr/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio, gelen ses ve sesli not eklerini OpenClaw'ın paylaşılan `tools.media.audio` işlem hattı üzerinden transkripsiyonlayabilir. OpenClaw, çok parçalı sesi OpenAI uyumlu transkripsiyon uç noktasına gönderir ve dönen metni `{{Transcript}}` olarak, ayrıca bir `[Audio]` bloğuyla enjekte eder.

Özellik | Değer  
---|---  
Sağlayıcı kimliği | `senseaudio`  
Plugin | birlikte gelir, `enabledByDefault: true`  
Sözleşme | `mediaUnderstandingProviders` (ses)  
Kimlik doğrulama ortam değişkeni | `SENSEAUDIO_API_KEY`  
Varsayılan model | `senseaudio-asr-pro-1.5-260319`  
Varsayılan URL | `https://api.senseaudio.cn/v1`  
Web sitesi | [senseaudio.cn](<https://senseaudio.cn>)  
Belgeler | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Başlarken

* ### Set your API key

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### Enable the audio provider

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### Send a voice note

Bağlı herhangi bir kanal üzerinden sesli mesaj gönderin. OpenClaw sesi SenseAudio'ya yükler ve yanıt işlem hattında transkripti kullanır.

## Seçenekler

Seçenek | Yol | Açıklama  
---|---|---  
`model` | `tools.media.audio.models[].model` | SenseAudio ASR model kimliği  
`language` | `tools.media.audio.models[].language` | İsteğe bağlı dil ipucu  
`prompt` | `tools.media.audio.prompt` | İsteğe bağlı transkripsiyon prompt'u  
`baseUrl` | `tools.media.audio.baseUrl` veya model | OpenAI uyumlu tabanı geçersiz kıl  
`headers` | `tools.media.audio.request.headers` | Ek istek üstbilgileri  
  
## İlgili

  * [Medya anlama (ses)](</tr/nodes/audio>)
  * [Model sağlayıcıları](</tr/concepts/model-providers>)


Was this useful?YesNo