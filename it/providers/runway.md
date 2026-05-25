---
title: Pista
source_url: https://docs.openclaw.ai/it/providers/runway
scraped_at: 2026-05-25
---

OpenClaw include un provider `runway` in bundle per la generazione video ospitata. Il Plugin è abilitato per impostazione predefinita e registra il provider `runway` rispetto al contratto `videoGenerationProviders`.

Proprietà | Valore  
---|---  
ID provider | `runway`  
Plugin | in bundle, `enabledByDefault: true`  
Variabili env di auth | `RUNWAYML_API_SECRET` (canonica) o `RUNWAY_API_KEY`  
Flag di onboarding | `--auth-choice runway-api-key`  
Flag CLI diretto | `--runway-api-key <key>`  
API | Generazione video basata su task di Runway (polling `GET /v1/tasks/{id}`)  
Modello predefinito | `runway/gen4.5`  
  
## Per iniziare

* ### Imposta la chiave API

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### Imposta Runway come provider video predefinito

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### Genera un video

Chiedi all'agente di generare un video. Runway verrà usato automaticamente.

## Modalità e modelli supportati

Il provider espone sette modelli Runway suddivisi in tre modalità. Lo stesso ID modello può servire più di una modalità (ad esempio `gen4.5` funziona sia per testo-a-video sia per immagine-a-video).

Modalità | Modelli | Input di riferimento  
---|---|---  
Testo-a-video | `gen4.5` (predefinito), `veo3.1`, `veo3.1_fast`, `veo3` | Nessuno  
Immagine-a-video | `gen4.5`, `gen4_turbo`, `gen3a_turbo`, `veo3.1`, `veo3.1_fast`, `veo3` | 1 immagine locale o remota  
Video-a-video | `gen4_aleph` | 1 video locale o remoto  
  
I riferimenti a immagini e video locali sono supportati tramite URI di dati.

Proporzioni | Valori consentiti  
---|---  
Testo-a-video | `16:9`, `9:16`  
Modifiche a immagini e video | `1:1`, `16:9`, `9:16`, `3:4`, `4:3`, `21:9`  
  
## Configurazione

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## Configurazione avanzata

Alias delle variabili d'ambiente

OpenClaw riconosce sia `RUNWAYML_API_SECRET` (canonica) sia `RUNWAY_API_KEY`. Entrambe le variabili autenticheranno il provider Runway.

Polling dei task

Runway usa un'API basata su task. Dopo l'invio di una richiesta di generazione, OpenClaw esegue il polling di `GET /v1/tasks/{id}` finché il video non è pronto. Non è necessaria alcuna configurazione aggiuntiva per il comportamento di polling.

## Correlati

[**Generazione video** Parametri dello strumento condivisi, selezione del provider e comportamento asincrono. ](</it/tools/video-generation>) [**Riferimento di configurazione** Impostazioni predefinite dell'agente, incluso il modello di generazione video. ](</it/gateway/config-agents#agent-defaults>)

Was this useful?YesNo