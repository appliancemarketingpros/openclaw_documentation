---
title: SenseAudio
source_url: https://docs.openclaw.ai/pl/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio może transkrybować przychodzące załączniki audio i notatki głosowe przez współdzielony potok `tools.media.audio` OpenClaw. OpenClaw wysyła wieloczęściowe audio do zgodnego z OpenAI punktu końcowego transkrypcji i wstrzykuje zwrócony tekst jako `{{Transcript}}` oraz blok `[Audio]`.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `senseaudio`  
Plugin | wbudowany, `enabledByDefault: true`  
Kontrakt | `mediaUnderstandingProviders` (audio)  
Zmienna środowiskowa uwierzytelniania | `SENSEAUDIO_API_KEY`  
Domyślny model | `senseaudio-asr-pro-1.5-260319`  
Domyślny URL | `https://api.senseaudio.cn/v1`  
Witryna | [senseaudio.cn](<https://senseaudio.cn>)  
Dokumentacja | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Pierwsze kroki

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

Wyślij wiadomość audio przez dowolny połączony kanał. OpenClaw przesyła audio do SenseAudio i używa transkrypcji w potoku odpowiedzi.

## Opcje

Opcja | Ścieżka | Opis  
---|---|---  
`model` | `tools.media.audio.models[].model` | Identyfikator modelu ASR SenseAudio  
`language` | `tools.media.audio.models[].language` | Opcjonalna podpowiedź językowa  
`prompt` | `tools.media.audio.prompt` | Opcjonalny prompt transkrypcji  
`baseUrl` | `tools.media.audio.baseUrl` lub model | Zastąp zgodną z OpenAI bazę  
`headers` | `tools.media.audio.request.headers` | Dodatkowe nagłówki żądania  
  
## Powiązane

  * [Rozumienie mediów (audio)](</pl/nodes/audio>)
  * [Dostawcy modeli](</pl/concepts/model-providers>)


Was this useful?YesNo