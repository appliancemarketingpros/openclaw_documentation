---
title: Inworld
source_url: https://docs.openclaw.ai/it/providers/inworld
scraped_at: 2026-05-25
---

Inworld è un provider di sintesi vocale (TTS) in streaming. In OpenClaw sintetizza l'audio delle risposte in uscita (MP3 per impostazione predefinita, OGG_OPUS per le note vocali) e audio PCM per canali di telefonia come Voice Call.

OpenClaw invia richieste all'endpoint TTS in streaming di Inworld, concatena i chunk audio base64 restituiti in un unico buffer e passa il risultato alla pipeline standard dell'audio di risposta.

Proprietà | Valore  
---|---  
ID provider | `inworld`  
Plugin | in bundle, `enabledByDefault: true`  
Contratto | `speechProviders` (solo TTS)  
Var env auth | `INWORLD_API_KEY` (HTTP Basic, credenziale dashboard Base64)  
URL base | `https://api.inworld.ai`  
Voce predefinita | `Sarah`  
Modello predefinito | `inworld-tts-1.5-max`  
Uscita | MP3 (predefinita), OGG_OPUS (note vocali), PCM 22050 Hz (telefonia)  
Sito web | [inworld.ai](<https://inworld.ai>)  
Documentazione | [docs.inworld.ai/tts/tts](<https://docs.inworld.ai/tts/tts>)  
  
## Per iniziare

* ### Imposta la tua chiave API

Copia la credenziale dalla dashboard Inworld (Workspace > API Keys) e impostala come variabile env. Il valore viene inviato letteralmente come credenziale HTTP Basic, quindi non codificarlo di nuovo in Base64 né convertirlo in un token bearer.

CodeCopy code
[code]
    INWORLD_API_KEY=<base64-credential-from-dashboard>
[/code]

* ### Seleziona Inworld in messages.tts

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "inworld",      providers: {        inworld: {          voiceId: "Sarah",          modelId: "inworld-tts-1.5-max",        },      },    },  },}
[/code]

* ### Invia un messaggio

Invia una risposta tramite qualsiasi canale connesso. OpenClaw sintetizza l'audio con Inworld e lo consegna come MP3 (o OGG_OPUS quando il canale richiede una nota vocale).

## Opzioni di configurazione

Opzione | Percorso | Descrizione  
---|---|---  
`apiKey` | `messages.tts.providers.inworld.apiKey` | Credenziale dashboard Base64. Ripiega su `INWORLD_API_KEY`.  
`baseUrl` | `messages.tts.providers.inworld.baseUrl` | Sovrascrive l'URL base dell'API Inworld (predefinito `https://api.inworld.ai`).  
`voiceId` | `messages.tts.providers.inworld.voiceId` | Identificatore della voce (predefinito `Sarah`).  
`modelId` | `messages.tts.providers.inworld.modelId` | ID modello TTS (predefinito `inworld-tts-1.5-max`).  
`temperature` | `messages.tts.providers.inworld.temperature` | Temperatura di campionamento `0..2` (opzionale).  
  
## Note

Autenticazione

Inworld usa l'autenticazione HTTP Basic con una singola stringa di credenziale codificata in Base64. Copiala letteralmente dalla dashboard Inworld. Il provider la invia come `Authorization: Basic <apiKey>` senza alcuna ulteriore codifica, quindi non codificarla tu stesso in Base64 e non passare un token in stile bearer. Vedi le [note sull'autenticazione TTS](</it/tools/tts#inworld-primary>) per lo stesso richiamo.

Modelli

ID modello supportati: `inworld-tts-1.5-max` (predefinito), `inworld-tts-1.5-mini`, `inworld-tts-1-max`, `inworld-tts-1`.

Output audio

Le risposte usano MP3 per impostazione predefinita. Quando il target del canale è `voice-note`, OpenClaw chiede a Inworld `OGG_OPUS` affinché l'audio venga riprodotto come una bolla vocale nativa. La sintesi per telefonia usa `PCM` grezzo a 22050 Hz per alimentare il bridge di telefonia.

Endpoint personalizzati

Sovrascrivi l'host API con `messages.tts.providers.inworld.baseUrl`. Le barre finali vengono rimosse prima dell'invio delle richieste.

## Correlati

[**Sintesi vocale** Panoramica TTS, provider e configurazione `messages.tts`. ](</it/tools/tts>) [**Configurazione** Riferimento completo alla configurazione, incluse le impostazioni `messages.tts`. ](</it/gateway/configuration>) [**Provider** Tutti i provider OpenClaw in bundle. ](</it/providers>) [**Risoluzione dei problemi** Problemi comuni e passaggi di debug. ](</it/help/troubleshooting>)

Was this useful?YesNo