---
title: Deepgram
source_url: https://docs.openclaw.ai/it/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram è un'API di speech-to-text. In OpenClaw viene usata per la trascrizione in ingresso di audio/note vocali tramite `tools.media.audio` e per la STT in streaming di Voice Call tramite `plugins.entries.voice-call.config.streaming`.

Per la trascrizione batch, OpenClaw carica il file audio completo su Deepgram e inietta la trascrizione nella pipeline di risposta (`{{Transcript}}` \+ blocco `[Audio]`). Per la trascrizione in streaming di Voice Call, OpenClaw inoltra frame live G.711 u-law tramite l'endpoint WebSocket `listen` di Deepgram ed emette trascrizioni parziali o finali man mano che Deepgram le restituisce.

Dettaglio | Valore  
---|---  
Sito web | [deepgram.com](<https://deepgram.com>)  
Documentazione | [developers.deepgram.com](<https://developers.deepgram.com>)  
Autenticazione | `DEEPGRAM_API_KEY`  
Modello predefinito | `nova-3`  
  
## Per iniziare

* ### Imposta la tua chiave API

Aggiungi la tua chiave API Deepgram all'ambiente:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Abilita il provider audio

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Invia una nota vocale

Invia un messaggio audio tramite qualsiasi canale collegato. OpenClaw lo trascrive tramite Deepgram e inietta la trascrizione nella pipeline di risposta.

## Opzioni di configurazione

Opzione | Percorso | Descrizione  
---|---|---  
`model` | `tools.media.audio.models[].model` | Id modello Deepgram (predefinito: `nova-3`)  
`language` | `tools.media.audio.models[].language` | Suggerimento lingua (facoltativo)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Abilita il rilevamento della lingua (facoltativo)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Abilita la punteggiatura (facoltativo)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Abilita la formattazione intelligente (facoltativo)  
  
### Con suggerimento lingua

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### Con opzioni Deepgram

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## STT in streaming di Voice Call

Il Plugin incluso `deepgram` registra anche un provider di trascrizione realtime per il Plugin Voice Call.

Impostazione | Percorso di configurazione | Predefinito  
---|---|---  
Chiave API | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | Usa `DEEPGRAM_API_KEY` come fallback  
Modello | `...deepgram.model` | `nova-3`  
Lingua | `...deepgram.language` | (non impostata)  
Encoding | `...deepgram.encoding` | `mulaw`  
Frequenza di campionamento | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Risultati intermedi | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Note

Autenticazione

L'autenticazione segue l'ordine standard di autenticazione del provider. `DEEPGRAM_API_KEY` è il percorso più semplice.

Proxy ed endpoint personalizzati

Sovrascrivi endpoint o header con `tools.media.audio.baseUrl` e `tools.media.audio.headers` quando usi un proxy.

Comportamento dell'output

L'output segue le stesse regole audio degli altri provider (limiti di dimensione, timeout, iniezione della trascrizione).

## Correlati

[**Strumenti media** Panoramica della pipeline di elaborazione audio, immagini e video. ](</it/tools/media-overview>) [**Configurazione** Riferimento completo della configurazione, incluse le impostazioni degli strumenti media. ](</it/gateway/configuration>) [**Risoluzione dei problemi** Problemi comuni e passaggi di debug. ](</it/help/troubleshooting>) [**FAQ** Domande frequenti sulla configurazione di OpenClaw. ](</it/help/faq>)

Was this useful?YesNo