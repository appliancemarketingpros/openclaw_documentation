---
title: SenseAudio
source_url: https://docs.openclaw.ai/it/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio può trascrivere audio in ingresso e allegati di note vocali tramite la pipeline condivisa `tools.media.audio` di OpenClaw. OpenClaw invia audio multipart all'endpoint di trascrizione compatibile con OpenAI e inserisce il testo restituito come `{{Transcript}}` più un blocco `[Audio]`.

Proprietà | Valore  
---|---  
ID provider | `senseaudio`  
Plugin | integrato, `enabledByDefault: true`  
Contratto | `mediaUnderstandingProviders` (audio)  
Variabile env auth | `SENSEAUDIO_API_KEY`  
Modello predefinito | `senseaudio-asr-pro-1.5-260319`  
URL predefinito | `https://api.senseaudio.cn/v1`  
Sito web | [senseaudio.cn](<https://senseaudio.cn>)  
Documentazione | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## Per iniziare

* ### Imposta la tua chiave API

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### Abilita il provider audio

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### Invia una nota vocale

Invia un messaggio audio tramite qualsiasi canale connesso. OpenClaw carica l'audio su SenseAudio e usa la trascrizione nella pipeline di risposta.

## Opzioni

Opzione | Percorso | Descrizione  
---|---|---  
`model` | `tools.media.audio.models[].model` | ID modello ASR SenseAudio  
`language` | `tools.media.audio.models[].language` | Indicazione facoltativa della lingua  
`prompt` | `tools.media.audio.prompt` | Prompt di trascrizione facoltativo  
`baseUrl` | `tools.media.audio.baseUrl` or model | Sovrascrive la base compatibile con OpenAI  
`headers` | `tools.media.audio.request.headers` | Header di richiesta aggiuntivi  
  
## Correlati

  * [Comprensione dei media (audio)](</it/nodes/audio>)
  * [Provider di modelli](</it/concepts/model-providers>)


Was this useful?YesNo