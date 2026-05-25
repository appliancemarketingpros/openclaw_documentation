---
title: Deepgram
source_url: https://docs.openclaw.ai/nl/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram is een speech-to-text-API. In OpenClaw wordt deze gebruikt voor inkomende audio-/spraaknotitie-transcriptie via `tools.media.audio` en voor streaming-STT voor Voice Call via `plugins.entries.voice-call.config.streaming`.

Voor batchtranscriptie uploadt OpenClaw het volledige audiobestand naar Deepgram en injecteert het transcript in de antwoordpipeline (`{{Transcript}}` \+ `[Audio]`-blok). Voor Voice Call-streaming stuurt OpenClaw live G.711 u-law-frames door via Deepgrams WebSocket-`listen`-endpoint en geeft gedeeltelijke of definitieve transcripties uit zodra Deepgram ze terugstuurt.

Detail | Waarde  
---|---  
Website | [deepgram.com](<https://deepgram.com>)  
Docs | [developers.deepgram.com](<https://developers.deepgram.com>)  
Auth | `DEEPGRAM_API_KEY`  
Standaardmodel | `nova-3`  
  
## Aan de slag

* ### Stel je API-sleutel in

Voeg je Deepgram-API-sleutel toe aan de omgeving:

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### Schakel de audioprovider in

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### Stuur een spraaknotitie

Stuur een audiobericht via een verbonden kanaal. OpenClaw transcribeert het via Deepgram en injecteert het transcript in de antwoordpipeline.

## Configuratieopties

Optie | Pad | Beschrijving  
---|---|---  
`model` | `tools.media.audio.models[].model` | Deepgram-model-id (standaard: `nova-3`)  
`language` | `tools.media.audio.models[].language` | Taalhint (optioneel)  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | Taaldetectie inschakelen (optioneel)  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | Interpunctie inschakelen (optioneel)  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | Slimme opmaak inschakelen (optioneel)  
  
### Met taalhint

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### Met Deepgram-opties

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Voice Call-streaming-STT

De gebundelde `deepgram`-plugin registreert ook een realtime transcriptieprovider voor de Voice Call-plugin.

Instelling | Configuratiepad | Standaard  
---|---|---  
API-sleutel | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | Valt terug op `DEEPGRAM_API_KEY`  
Model | `...deepgram.model` | `nova-3`  
Taal | `...deepgram.language` | (niet ingesteld)  
Codering | `...deepgram.encoding` | `mulaw`  
Samplefrequentie | `...deepgram.sampleRate` | `8000`  
Endpointing | `...deepgram.endpointingMs` | `800`  
Tussenresultaten | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## Opmerkingen

Authenticatie

Authenticatie volgt de standaardvolgorde voor provider-authenticatie. `DEEPGRAM_API_KEY` is de eenvoudigste route.

Proxy en aangepaste endpoints

Overschrijf endpoints of headers met `tools.media.audio.baseUrl` en `tools.media.audio.headers` wanneer je een proxy gebruikt.

Uitvoergedrag

Uitvoer volgt dezelfde audioregels als andere providers (groottelimieten, time-outs, transcriptinjectie).

## Gerelateerd

[**Mediatools** Overzicht van de verwerkingspipeline voor audio, afbeeldingen en video. ](</nl/tools/media-overview>) [**Configuratie** Volledige configuratiereferentie inclusief instellingen voor mediatools. ](</nl/gateway/configuration>) [**Probleemoplossing** Veelvoorkomende problemen en stappen voor foutopsporing. ](</nl/help/troubleshooting>) [**FAQ** Veelgestelde vragen over het instellen van OpenClaw. ](</nl/help/faq>)

Was this useful?YesNo