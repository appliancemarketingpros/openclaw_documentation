---
title: SenseAudio
source_url: https://docs.openclaw.ai/de/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio kann eingehende Audio- und Sprachnachrichten-Anhänge über OpenClaws gemeinsame `tools.media.audio`-Pipeline transkribieren. OpenClaw sendet Audiodaten als Multipart an den OpenAI-kompatiblen Transkriptions-Endpunkt und fügt den zurückgegebenen Text als `{{Transcript}}` plus einen `[Audio]`-Block ein.

Eigenschaft | Wert  
---|---  
Provider-ID | `senseaudio`  
Plugin | gebündelt, `enabledByDefault: true`  
Contract | `mediaUnderstandingProviders` (Audio)  
Auth-Umgebungsvariable | `SENSEAUDIO_API_KEY`  
Standardmodell | `senseaudio-asr-pro-1.5-260319`  
Standard-URL | `https://api.senseaudio.cn/v1`  
Website | [senseaudio.cn](<https://senseaudio.cn>)  
Dokumentation | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Erste Schritte

* ### Legen Sie Ihren API-Schlüssel fest

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### Aktivieren Sie den Audio-Provider

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### Senden Sie eine Sprachnachricht

Senden Sie eine Audionachricht über einen beliebigen verbundenen Kanal. OpenClaw lädt die Audiodaten zu SenseAudio hoch und verwendet das Transkript in der Antwort-Pipeline.

## Optionen

Option | Pfad | Beschreibung  
---|---|---  
`model` | `tools.media.audio.models[].model` | SenseAudio-ASR-Modell-ID  
`language` | `tools.media.audio.models[].language` | Optionaler Sprachhinweis  
`prompt` | `tools.media.audio.prompt` | Optionaler Transkriptions-Prompt  
`baseUrl` | `tools.media.audio.baseUrl` or model | OpenAI-kompatible Basis überschreiben  
`headers` | `tools.media.audio.request.headers` | Zusätzliche Request-Header  
  
## Verwandt

  * [Medienverständnis (Audio)](</de/nodes/audio>)
  * [Modell-Provider](</de/concepts/model-providers>)


Was this useful?YesNo