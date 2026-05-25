---
title: Vydra
source_url: https://docs.openclaw.ai/it/providers/vydra
scraped_at: 2026-05-25
---

Il Plugin Vydra in bundle aggiunge:

  * Generazione di immagini tramite `vydra/grok-imagine`
  * Generazione di video tramite `vydra/veo3` e `vydra/kling`
  * Sintesi vocale tramite la route TTS di Vydra basata su ElevenLabs


OpenClaw usa la stessa `VYDRA_API_KEY` per tutte e tre le capacità.

Proprietà | Valore  
---|---  
ID provider | `vydra`  
Plugin | in bundle, `enabledByDefault: true`  
Variabile env auth | `VYDRA_API_KEY`  
Flag di onboarding | `--auth-choice vydra-api-key`  
Flag CLI diretto | `--vydra-api-key <key>`  
Contratti | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
URL base | `https://www.vydra.ai/api/v1` (usa l'host `www`)  
  
## Configurazione

* ### Esegui l'onboarding interattivo

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

Oppure imposta direttamente la variabile env:

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### Scegli una capacità predefinita

Scegli una o più delle capacità sotto (immagine, video o voce) e applica la configurazione corrispondente.

## Capacità

Generazione di immagini

Modello di immagini predefinito:

  * `vydra/grok-imagine`


Impostalo come provider di immagini predefinito:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

Il supporto in bundle attuale è solo da testo a immagine. Le route di modifica ospitate da Vydra si aspettano URL di immagini remote, e OpenClaw non aggiunge ancora un bridge di upload specifico per Vydra nel Plugin in bundle.

Generazione di video

Modelli video registrati:

  * `vydra/veo3` per testo-a-video
  * `vydra/kling` per immagine-a-video


Imposta Vydra come provider video predefinito:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

Note:

  * `vydra/veo3` è incluso in bundle solo come testo-a-video.
  * `vydra/kling` attualmente richiede un riferimento a un URL di immagine remota. I caricamenti di file locali vengono rifiutati in anticipo.
  * L'attuale route HTTP `kling` di Vydra è stata incoerente sul fatto che richieda `image_url` o `video_url`; il provider in bundle mappa lo stesso URL di immagine remota in entrambi i campi.
  * Il Plugin in bundle resta conservativo e non inoltra controlli di stile non documentati come proporzioni, risoluzione, watermark o audio generato.

Test live video

Copertura live specifica del provider:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

Il file live Vydra in bundle ora copre:

  * `vydra/veo3` testo-a-video
  * `vydra/kling` immagine-a-video usando un URL di immagine remota


Sovrascrivi la fixture dell'immagine remota quando necessario:

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

Sintesi vocale

Imposta Vydra come provider vocale:

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

Valori predefiniti:

  * Modello: `elevenlabs/tts`
  * ID voce: `21m00Tcm4TlvDq8ikWAM`


Il Plugin in bundle attualmente espone una voce predefinita nota e affidabile e restituisce file audio MP3.

## Correlati

[**Directory provider** Sfoglia tutti i provider disponibili. ](</it/providers>) [**Generazione di immagini** Parametri condivisi dello strumento per immagini e selezione del provider. ](</it/tools/image-generation>) [**Generazione di video** Parametri condivisi dello strumento per video e selezione del provider. ](</it/tools/video-generation>) [**Riferimento di configurazione** Valori predefiniti degli agenti e configurazione dei modelli. ](</it/gateway/config-agents#agent-defaults>)

Was this useful?YesNo