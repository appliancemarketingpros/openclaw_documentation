---
title: Fal
source_url: https://docs.openclaw.ai/it/providers/fal
scraped_at: 2026-05-25
---

OpenClaw include un provider `fal` in bundle per la generazione ospitata di immagini e video.

Proprietà | Valore  
---|---  
Provider | `fal`  
Autenticazione | `FAL_KEY` (canonico; `FAL_API_KEY` funziona anche come fallback)  
API | endpoint dei modelli fal  
  
## Per iniziare

* ### Set the API key

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### Set a default image model

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Generazione di immagini

Il provider di generazione di immagini `fal` in bundle usa come impostazione predefinita `fal/fal-ai/flux/dev`.

Funzionalità | Valore  
---|---  
Immagini massime | 4 per richiesta  
Modalità di modifica | Flux: 1 immagine di riferimento; GPT Image 2: 10; Nano Banana 2: 14  
Override delle dimensioni | Supportati  
Proporzioni | Supportate per generate e per la modifica con GPT Image 2/Nano Banana 2  
Risoluzione | Supportata  
Formato di output | `png` o `jpeg`  
  
Usa `outputFormat: "png"` quando vuoi output PNG. fal non dichiara un controllo esplicito dello sfondo trasparente in OpenClaw, quindi `background: "transparent"` viene segnalato come override ignorato per i modelli fal.

Per usare fal come provider di immagini predefinito:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## Generazione di video

Il provider di generazione di video `fal` in bundle usa come impostazione predefinita `fal/fal-ai/minimax/video-01-live`.

Funzionalità | Valore  
---|---  
Modalità | Da testo a video, riferimento a immagine singola, da riferimento Seedance a video  
Runtime | Flusso submit/status/result basato su coda per processi di lunga durata  
  
Available video models

**video-agent HeyGen:**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0:**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Seedance 2.0 config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Seedance 2.0 reference-to-video config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

Reference-to-video accetta fino a 9 immagini, 3 video e 3 riferimenti audio tramite i parametri condivisi `video_generate` `images`, `videos` e `audioRefs`, con un massimo di 12 file di riferimento totali.

HeyGen video-agent config example json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## Correlati

[**Image generation** Parametri condivisi dello strumento immagine e selezione del provider. ](</it/tools/image-generation>) [**Video generation** Parametri condivisi dello strumento video e selezione del provider. ](</it/tools/video-generation>) [**Configuration reference** Impostazioni predefinite degli agenti, inclusa la selezione dei modelli di immagine e video. ](</it/gateway/config-agents#agent-defaults>)

Was this useful?YesNo