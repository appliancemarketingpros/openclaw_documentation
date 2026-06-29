---
title: PixVerse
source_url: https://docs.openclaw.ai/it/providers/pixverse
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw fornisce `pixverse` come Plugin esterno ufficiale per la generazione video PixVerse ospitata. Il Plugin registra il provider `pixverse` rispetto al contratto `videoGenerationProviders`.

Proprietà | Valore  
---|---  
ID provider | `pixverse`  
Pacchetto Plugin | `@openclaw/pixverse-provider`  
Variabile env di auth | `PIXVERSE_API_KEY`  
Flag di onboarding | `--auth-choice pixverse-api-key`  
Flag CLI diretto | `--pixverse-api-key <key>`  
API | PixVerse Platform API v2 (invio `video_id` più polling del risultato)  
Modello predefinito | `pixverse/v6`  
Regione API predefinita | Internazionale  
  
## Per iniziare

* ### Installa il Plugin

bashCopy code
[code]
    openclaw plugins install clawhub:@openclaw/pixverse-provideropenclaw gateway restart
[/code]

* ### Imposta la chiave API

bashCopy code
[code]
    openclaw onboard --auth-choice pixverse-api-key
[/code]

La procedura guidata chiede se usare l'endpoint internazionale (`https://app-api.pixverse.ai/openapi/v2`) o l'endpoint CN (`https://app-api.pixverseai.cn/openapi/v2`) prima di scrivere `region` e `baseUrl` nella configurazione del provider.

* ### Imposta PixVerse come provider video predefinito

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "pixverse/v6"
[/code]

* ### Genera un video

Chiedi all'agente di generare un video. PixVerse verrà usato automaticamente.

## Modalità e modelli supportati

Il provider espone i modelli di generazione PixVerse tramite lo strumento video condiviso di OpenClaw.

Modalità | Modelli | Input di riferimento  
---|---|---  
Testo-video | `v6` (predefinito), `c1` | Nessuno  
Immagine-video | `v6` (predefinito), `c1` | 1 immagine locale o remota  
  
I riferimenti a immagini locali vengono caricati su PixVerse prima della richiesta immagine-video. Gli URL di immagini remote vengono passati all'endpoint di caricamento immagini di PixVerse come `image_url`.

Opzione | Valori supportati  
---|---  
Durata | 1-15 secondi  
Risoluzione | `360P`, `540P`, `720P`, `1080P`  
Proporzioni | `16:9`, `4:3`, `1:1`, `3:4`, `9:16`, `2:3`, `3:2`, `21:9` per testo-video  
Audio generato | `audio: true`  
  
## Opzioni del provider

Il provider video accetta queste chiavi opzionali specifiche del provider:

Opzione | Tipo | Effetto  
---|---|---  
`seed` | number | Seed deterministico quando supportato  
`negativePrompt` / `negative_prompt` | string | Prompt negativo  
`quality` | string | Qualità PixVerse come `720p`  
`motionMode` / `motion_mode` | string | Modalità movimento immagine-video  
`cameraMovement` / `camera_movement` | string | Preset di movimento camera PixVerse  
`templateId` / `template_id` | number | ID template PixVerse attivato  
  
## Configurazione

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "pixverse/v6",      },    },  },}
[/code]

## Configurazione avanzata

Regione API

OpenClaw usa per impostazione predefinita l'API PixVerse internazionale. Imposta `models.providers.pixverse.region` manualmente quando la tua chiave appartiene a una regione specifica della piattaforma PixVerse, oppure usa `openclaw onboard --auth-choice pixverse-api-key` per sceglierne una nella procedura guidata di configurazione:

Valore regione | URL base API PixVerse  
---|---  
`international` | `https://app-api.pixverse.ai/openapi/v2`  
`cn` | `https://app-api.pixverseai.cn/openapi/v2`  
  
json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        region: "cn", // "international" or "cn"        baseUrl: "https://app-api.pixverseai.cn/openapi/v2",        models: [],      },    },  },}
[/code]

URL base personalizzato

Imposta `models.providers.pixverse.baseUrl` solo quando instradi tramite un proxy compatibile attendibile. `baseUrl` ha precedenza su `region`.

json5Copy code
[code]
    {  models: {    providers: {      pixverse: {        baseUrl: "https://app-api.pixverse.ai/openapi/v2",      },    },  },}
[/code]

Polling delle attività

PixVerse restituisce un `video_id` dalla richiesta di generazione. OpenClaw esegue il polling di `/openapi/v2/video/result/{video_id}` finché l'attività riesce, fallisce o va in timeout.

## Correlati

[**Generazione video** Parametri dello strumento condiviso, selezione del provider e comportamento asincrono. ](</it/tools/video-generation>) [**Riferimento di configurazione** Impostazioni predefinite dell'agente, incluso il modello di generazione video. ](</it/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue