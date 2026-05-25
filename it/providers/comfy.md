---
title: ComfyUI
source_url: https://docs.openclaw.ai/it/providers/comfy
scraped_at: 2026-05-25
---

OpenClaw include un Plugin `comfy` che fornisce esecuzioni ComfyUI guidate da workflow. Il Plugin è interamente guidato dal workflow, quindi OpenClaw non prova a mappare controlli generici come `size`, `aspectRatio`, `resolution`, `durationSeconds` o controlli in stile TTS sul tuo grafo.

Proprietà | Dettaglio  
---|---  
Provider | `comfy`  
Modelli | `comfy/workflow`  
Superfici condivise | `image_generate`, `video_generate`, `music_generate`  
Autenticazione | Nessuna per ComfyUI locale; `COMFY_API_KEY` o `COMFY_CLOUD_API_KEY` per Comfy Cloud  
API | ComfyUI `/prompt` / `/history` / `/view` e Comfy Cloud `/api/*`  
  
## Cosa supporta

  * Generazione di immagini da un workflow JSON
  * Modifica di immagini con 1 immagine di riferimento caricata
  * Generazione video da un workflow JSON
  * Generazione video con 1 immagine di riferimento caricata
  * Generazione di musica o audio tramite lo strumento condiviso `music_generate`
  * Download dell'output da un nodo configurato o da tutti i nodi di output corrispondenti


## Per iniziare

Scegli tra eseguire ComfyUI sulla tua macchina oppure usare Comfy Cloud.

### Locale

**Ideale per:** eseguire la tua istanza ComfyUI sulla tua macchina o LAN.

* ### Avvia ComfyUI in locale

Assicurati che la tua istanza ComfyUI locale sia in esecuzione (predefinito `http://127.0.0.1:8188`).

* ### Prepara il tuo workflow JSON

Esporta o crea un file JSON di workflow ComfyUI. Annota gli ID dei nodi per il nodo di input del prompt e per il nodo di output da cui vuoi che OpenClaw legga.

* ### Configura il provider

Imposta `mode: "local"` e punta al file del workflow. Ecco un esempio minimo per immagini:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Imposta il modello predefinito

Punta OpenClaw al modello `comfy/workflow` per la capability che hai configurato:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verifica

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

### Comfy Cloud

**Ideale per:** eseguire workflow su Comfy Cloud senza gestire risorse GPU locali.

* ### Ottieni una chiave API

Registrati su [comfy.org](<https://comfy.org>) e genera una chiave API dalla dashboard del tuo account.

* ### Imposta la chiave API

Fornisci la tua chiave tramite uno di questi metodi:

bashCopy code
[code]
    # Variabile d'ambiente (consigliata)export COMFY_API_KEY="your-key" # Variabile d'ambiente alternativaexport COMFY_CLOUD_API_KEY="your-key" # Oppure inline nella configurazioneopenclaw config set plugins.entries.comfy.config.apiKey "your-key"
[/code]

* ### Prepara il tuo workflow JSON

Esporta o crea un file JSON di workflow ComfyUI. Annota gli ID dei nodi per il nodo di input del prompt e il nodo di output.

* ### Configura il provider

Imposta `mode: "cloud"` e punta al file del workflow:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "cloud",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },        },      },    },  },}
[/code]

* ### Imposta il modello predefinito

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

* ### Verifica

bashCopy code
[code]
    openclaw models list --provider comfy
[/code]

## Configurazione

Comfy supporta impostazioni di connessione condivise di primo livello più sezioni di workflow per capability (`image`, `video`, `music`):

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          mode: "local",          baseUrl: "http://127.0.0.1:8188",          image: {            workflowPath: "./workflows/flux-api.json",            promptNodeId: "6",            outputNodeId: "9",          },          video: {            workflowPath: "./workflows/video-api.json",            promptNodeId: "12",            outputNodeId: "21",          },          music: {            workflowPath: "./workflows/music-api.json",            promptNodeId: "3",            outputNodeId: "18",          },        },      },    },  },}
[/code]

### Chiavi condivise

Chiave | Tipo | Descrizione  
---|---|---  
`mode` | `"local"` o `"cloud"` | Modalità di connessione.  
`baseUrl` | string | Predefinito `http://127.0.0.1:8188` per locale o `https://cloud.comfy.org` per cloud.  
`apiKey` | string | Chiave inline facoltativa, alternativa alle variabili env `COMFY_API_KEY` / `COMFY_CLOUD_API_KEY`.  
`allowPrivateNetwork` | boolean | Consente un `baseUrl` privato/LAN in modalità cloud.  
  
### Chiavi per capability

Queste chiavi si applicano dentro le sezioni `image`, `video` o `music`:

Chiave | Obbligatoria | Predefinito | Descrizione  
---|---|---|---  
`workflow` o `workflowPath` | Sì | \-- | Percorso al file JSON del workflow ComfyUI.  
`promptNodeId` | Sì | \-- | ID del nodo che riceve il prompt testuale.  
`promptInputName` | No | `"text"` | Nome dell'input sul nodo del prompt.  
`outputNodeId` | No | \-- | ID del nodo da cui leggere l'output. Se omesso, vengono usati tutti i nodi di output corrispondenti.  
`pollIntervalMs` | No | \-- | Intervallo di polling in millisecondi per il completamento del job.  
`timeoutMs` | No | \-- | Timeout in millisecondi per l'esecuzione del workflow.  
  
Le sezioni `image` e `video` supportano anche:

Chiave | Obbligatoria | Predefinito | Descrizione  
---|---|---|---  
`inputImageNodeId` | Sì (quando si passa un'immagine di riferimento) | \-- | ID del nodo che riceve l'immagine di riferimento caricata.  
`inputImageInputName` | No | `"image"` | Nome dell'input sul nodo immagine.  
  
## Dettagli del workflow

Workflow immagine

Imposta il modello immagine predefinito su `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

**Esempio di modifica con immagine di riferimento:**

Per abilitare la modifica immagini con un'immagine di riferimento caricata, aggiungi `inputImageNodeId` alla tua configurazione immagine:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          image: {            workflowPath: "./workflows/edit-api.json",            promptNodeId: "6",            inputImageNodeId: "7",            inputImageInputName: "image",            outputNodeId: "9",          },        },      },    },  },}
[/code]

Workflow video

Imposta il modello video predefinito su `comfy/workflow`:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "comfy/workflow",      },    },  },}
[/code]

I workflow video Comfy supportano text-to-video e image-to-video tramite il grafo configurato.

Workflow musicali

Il Plugin incluso registra un provider di generazione musicale per output audio o musicali definiti dal workflow, esposti tramite lo strumento condiviso `music_generate`:

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Usa la sezione di configurazione `music` per puntare al tuo workflow JSON audio e al nodo di output.

Retrocompatibilità

La configurazione immagine esistente di primo livello (senza la sezione annidata `image`) continua a funzionare:

json5Copy code
[code]
    {  plugins: {    entries: {      comfy: {        config: {          workflowPath: "./workflows/flux-api.json",          promptNodeId: "6",          outputNodeId: "9",        },      },    },  },}
[/code]

OpenClaw tratta questa forma legacy come configurazione del workflow immagine. Non devi migrare subito, ma le sezioni annidate `image` / `video` / `music` sono consigliate per le nuove configurazioni.

Test live

Esiste copertura live opt-in per il Plugin incluso:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Il test live salta i singoli casi immagine, video o musica a meno che la sezione di workflow Comfy corrispondente non sia configurata.

## Correlati

[**Generazione di immagini** Configurazione e utilizzo dello strumento di generazione di immagini. ](</it/tools/image-generation>) [**Generazione video** Configurazione e utilizzo dello strumento di generazione video. ](</it/tools/video-generation>) [**Generazione musicale** Configurazione dello strumento per la generazione di musica e audio. ](</it/tools/music-generation>) [**Directory dei provider** Panoramica di tutti i provider e riferimenti ai modelli. ](</it/providers>) [**Riferimento della configurazione** Riferimento completo della configurazione, inclusi i valori predefiniti degli agenti. ](</it/gateway/config-agents#agent-defaults>)

Was this useful?YesNo