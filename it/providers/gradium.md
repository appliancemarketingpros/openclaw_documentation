---
title: Gradium
source_url: https://docs.openclaw.ai/it/providers/gradium
scraped_at: 2026-05-25
---

[Gradium](<https://gradium.ai>) è un provider di sintesi vocale incluso in OpenClaw. Il plugin può generare normali risposte audio (WAV), output Opus compatibile con note vocali e audio u-law a 8 kHz per superfici di telefonia.

Proprietà | Valore  
---|---  
ID provider | `gradium`  
Autenticazione | `GRADIUM_API_KEY` o config `apiKey`  
URL di base | `https://api.gradium.ai` (default)  
Voce predefinita | `Emma` (`YTpq7expH9539ERJ`)  
  
## Configurazione

Crea una chiave API Gradium, quindi esponila a OpenClaw con una variabile d'ambiente o con la chiave di configurazione.

### Variabile d'ambiente

bashCopy code
[code]
    export GRADIUM_API_KEY="gsk_..."
[/code]

### Chiave di configurazione

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          apiKey: "${GRADIUM_API_KEY}",        },      },    },  },}
[/code]

Il plugin controlla prima l'`apiKey` risolta e, in alternativa, usa la variabile d'ambiente `GRADIUM_API_KEY`.

## Configurazione

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "gradium",      providers: {        gradium: {          voiceId: "YTpq7expH9539ERJ",          // apiKey: "${GRADIUM_API_KEY}",          // baseUrl: "https://api.gradium.ai",        },      },    },  },}
[/code]

Chiave | Tipo | Descrizione  
---|---|---  
`messages.tts.providers.gradium.apiKey` | string | Chiave API risolta. Supporta `${ENV}` e riferimenti a segreti.  
`messages.tts.providers.gradium.baseUrl` | string | Sovrascrive l'origine API. Le barre finali vengono rimosse. Il valore predefinito è `https://api.gradium.ai`.  
`messages.tts.providers.gradium.voiceId` | string | ID della voce predefinita usato quando non è presente alcuna sovrascrittura tramite direttiva.  
  
Il formato audio di output viene selezionato automaticamente dal runtime in base alla superficie di destinazione e non è configurabile da `openclaw.json`. Vedi Output sotto.

## Voci

Nome | ID voce  
---|---  
Emma | `YTpq7expH9539ERJ`  
Kent | `LFZvm12tW_z0xfGo`  
Tiffany | `Eu9iL_CYe8N-Gkx_`  
Christina | `2H4HY2CBNyJHBCrP`  
Sydney | `jtEKaLYNn6iif5PR`  
John | `KWJiFWu2O9nMPYcR`  
Arthur | `3jUdJyOi9pgbxBTK`  
  
Voce predefinita: Emma.

### Sovrascrittura della voce per messaggio

Quando la policy vocale attiva consente le sovrascritture della voce, puoi cambiare voce inline usando un token direttiva. Tutti questi vengono risolti nella stessa sovrascrittura di `voiceId`:

textCopy code
[code]
    /voice:LFZvm12tW_z0xfGo/voice_id:LFZvm12tW_z0xfGo/voiceid:LFZvm12tW_z0xfGo/gradium_voice:LFZvm12tW_z0xfGo/gradiumvoice:LFZvm12tW_z0xfGo
[/code]

Se la policy vocale disabilita le sovrascritture della voce, la direttiva viene consumata ma ignorata.

## Output

Il runtime sceglie il formato di output dalla superficie di destinazione. Oggi il provider non sintetizza altri formati.

Destinazione | Formato | Estensione file | Frequenza di campionamento | Flag compatibile con voce  
---|---|---|---|---  
Audio standard | `wav` | `.wav` | provider | no  
Nota vocale | `opus` | `.opus` | provider | sì  
Telefonia | `ulaw_8000` | n/d | 8 kHz | n/d  
  
## Ordine di selezione automatica

Tra i provider TTS configurati, l'ordine di selezione automatica di Gradium è `30`. Vedi [Sintesi vocale](</it/tools/tts>) per sapere come OpenClaw sceglie il provider attivo quando `messages.tts.provider` non è fissato.

## Correlati

  * [Sintesi vocale](</it/tools/tts>)
  * [Panoramica dei media](</it/tools/media-overview>)


Was this useful?YesNo