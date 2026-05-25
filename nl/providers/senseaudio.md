---
title: SenseAudio
source_url: https://docs.openclaw.ai/nl/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio kan inkomende audio- en spraaknotitie-bijlagen transcriberen via OpenClaw's gedeelde `tools.media.audio`-pipeline. OpenClaw plaatst multipart-audio op het OpenAI-compatibele transcriptie-eindpunt en voegt de geretourneerde tekst in als `{{Transcript}}` plus een `[Audio]`-blok.

Eigenschap | Waarde  
---|---  
Provider-id | `senseaudio`  
Plugin | gebundeld, `enabledByDefault: true`  
Contract | `mediaUnderstandingProviders` (audio)  
Auth-env-var | `SENSEAUDIO_API_KEY`  
Standaardmodel | `senseaudio-asr-pro-1.5-260319`  
Standaard-URL | `https://api.senseaudio.cn/v1`  
Website | [senseaudio.cn](<https://senseaudio.cn>)  
Documentatie | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Aan de slag

* ### Stel je API-sleutel in

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### Schakel de audioprovider in

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### Verzend een spraaknotitie

Verzend een audiobericht via een verbonden kanaal. OpenClaw uploadt de audio naar SenseAudio en gebruikt het transcript in de antwoordpipeline.

## Opties

Optie | Pad | Beschrijving  
---|---|---  
`model` | `tools.media.audio.models[].model` | SenseAudio ASR-model-id  
`language` | `tools.media.audio.models[].language` | Optionele taalhint  
`prompt` | `tools.media.audio.prompt` | Optionele transcriptieprompt  
`baseUrl` | `tools.media.audio.baseUrl` of model | Overschrijf de OpenAI-compatibele basis  
`headers` | `tools.media.audio.request.headers` | Extra aanvraagheaders  
  
## Gerelateerd

  * [Mediabegrip (audio)](</nl/nodes/audio>)
  * [Modelproviders](</nl/concepts/model-providers>)


Was this useful?YesNo