---
title: Generazione di immagini
source_url: https://docs.openclaw.ai/it/tools/image-generation
scraped_at: 2026-05-25
---

Lo strumento `image_generate` consente all'agente di creare e modificare immagini usando i provider configurati. Le immagini generate vengono recapitate automaticamente come allegati multimediali nella risposta dell'agente.

## Avvio rapido

* ### Configura l'autenticazione

Imposta una chiave API per almeno un provider (per esempio `OPENAI_API_KEY`, `GEMINI_API_KEY`, `OPENROUTER_API_KEY`) oppure accedi con OpenAI Codex OAuth.

* ### Scegli un modello predefinito (opzionale)

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Codex OAuth usa lo stesso riferimento modello `openai/gpt-image-2`. Quando è configurato un profilo OAuth `openai-codex`, OpenClaw instrada le richieste di immagini tramite quel profilo OAuth invece di provare prima `OPENAI_API_KEY`. La configurazione esplicita `models.providers.openai` (chiave API, URL di base personalizzato/Azure) riattiva il percorso diretto dell'API OpenAI Images.

* ### Chiedi all'agente

_"Genera un'immagine di una mascotte robot amichevole."_

L'agente chiama automaticamente `image_generate`. Non è necessario inserirlo in una lista di strumenti consentiti: è abilitato per impostazione predefinita quando è disponibile un provider.

## Percorsi comuni

Obiettivo | Rif. modello | Autenticazione  
---|---|---  
Generazione immagini OpenAI con fatturazione API | `openai/gpt-image-2` | `OPENAI_API_KEY`  
Generazione immagini OpenAI con autenticazione tramite abbonamento Codex | `openai/gpt-image-2` | OpenAI Codex OAuth  
PNG/WebP OpenAI con sfondo trasparente | `openai/gpt-image-1.5` | `OPENAI_API_KEY` o OpenAI Codex OAuth  
Generazione immagini DeepInfra | `deepinfra/black-forest-labs/FLUX-1-schnell` | `DEEPINFRA_API_KEY`  
Generazione immagini OpenRouter | `openrouter/google/gemini-3.1-flash-image-preview` | `OPENROUTER_API_KEY`  
Generazione immagini LiteLLM | `litellm/gpt-image-2` | `LITELLM_API_KEY`  
Generazione immagini Google Gemini | `google/gemini-3.1-flash-image-preview` | `GEMINI_API_KEY` o `GOOGLE_API_KEY`  
  
Lo stesso strumento `image_generate` gestisce testo-in-immagine e la modifica con immagini di riferimento. Usa `image` per un riferimento o `images` per più riferimenti. I suggerimenti di output supportati dal provider, come `quality`, `outputFormat` e `background`, vengono inoltrati quando disponibili e segnalati come ignorati quando un provider non li supporta. Il supporto incluso per sfondi trasparenti è specifico di OpenAI; altri provider possono comunque preservare il canale alfa PNG se il loro backend lo emette.

## Provider supportati

Provider | Modello predefinito | Supporto modifica | Autenticazione  
---|---|---|---  
ComfyUI | `workflow` | Sì (1 immagine, configurata dal workflow) | `COMFY_API_KEY` o `COMFY_CLOUD_API_KEY` per il cloud  
DeepInfra | `black-forest-labs/FLUX-1-schnell` | Sì (1 immagine) | `DEEPINFRA_API_KEY`  
fal | `fal-ai/flux/dev` | Sì (limiti specifici del modello) | `FAL_KEY`  
Google | `gemini-3.1-flash-image-preview` | Sì | `GEMINI_API_KEY` o `GOOGLE_API_KEY`  
LiteLLM | `gpt-image-2` | Sì (fino a 5 immagini di input) | `LITELLM_API_KEY`  
MiniMax | `image-01` | Sì (riferimento soggetto) | `MINIMAX_API_KEY` o MiniMax OAuth (`minimax-portal`)  
OpenAI | `gpt-image-2` | Sì (fino a 4 immagini) | `OPENAI_API_KEY` o OpenAI Codex OAuth  
OpenRouter | `google/gemini-3.1-flash-image-preview` | Sì (fino a 5 immagini di input) | `OPENROUTER_API_KEY`  
Vydra | `grok-imagine` | No | `VYDRA_API_KEY`  
xAI | `grok-imagine-image` | Sì (fino a 5 immagini) | `XAI_API_KEY`  
  
Usa `action: "list"` per ispezionare provider e modelli disponibili a runtime:

textCopy code
[code]
    /tool image_generate action=list
[/code]

## Capacità dei provider

Capacità | ComfyUI | DeepInfra | fal | Google | MiniMax | OpenAI | Vydra | xAI  
---|---|---|---|---|---|---|---|---  
Generazione (conteggio massimo) | Definito dal workflow | 4 | 4 | 4 | 9 | 4 | 1 | 4  
Modifica / riferimento | 1 immagine (workflow) | 1 immagine | Flux: 1; GPT: 10; NB2: 14 | Fino a 5 immagini | 1 immagine (rif. soggetto) | Fino a 5 immagini | - | Fino a 5 immagini  
Controllo dimensioni | - | ✓ | ✓ | ✓ | - | Fino a 4K | - | -  
Proporzioni | - | - | ✓ | ✓ | ✓ | - | - | ✓  
Risoluzione (1K/2K/4K) | - | - | ✓ | ✓ | - | - | - | 1K, 2K  
  
## Parametri dello strumento

Prompt di generazione immagini. Obbligatorio per `action: "generate"`.

Usa `"list"` per ispezionare provider e modelli disponibili a runtime.

Override provider/modello (ad es. `openai/gpt-image-2`). Usa `openai/gpt-image-1.5` per sfondi OpenAI trasparenti.

Percorso o URL di una singola immagine di riferimento per la modalità di modifica.

Più immagini di riferimento per la modalità di modifica (fino a 5 sui provider supportati).

Suggerimento dimensione: `1024x1024`, `1536x1024`, `1024x1536`, `2048x2048`, `3840x2160`.

Proporzioni: `1:1`, `2:3`, `3:2`, `3:4`, `4:3`, `4:5`, `5:4`, `9:16`, `16:9`, `21:9`.

Suggerimento qualità quando il provider lo supporta.

Suggerimento formato di output quando il provider lo supporta.

Suggerimento sfondo quando il provider lo supporta. Usa `transparent` con `outputFormat: "png"` o `"webp"` per provider capaci di trasparenza.

Timeout opzionale della richiesta al provider in millisecondi. Quando Codex chiama `image_generate` tramite strumenti dinamici, questo valore per chiamata sovrascrive comunque il valore predefinito configurato ed è limitato a 600000 ms.

Suggerimenti solo OpenAI: `background`, `moderation`, `outputCompression` e `user`.

## Configurazione

### Selezione del modello

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openai/gpt-image-2",        timeoutMs: 180_000,        fallbacks: [          "openrouter/google/gemini-3.1-flash-image-preview",          "google/gemini-3.1-flash-image-preview",          "fal/fal-ai/flux/dev",        ],      },    },  },}
[/code]

### Ordine di selezione dei provider

OpenClaw prova i provider in questo ordine:

  1. Parametro **`model`** dalla chiamata allo strumento (se l'agente ne specifica uno).
  2. **`imageGenerationModel.primary`** dalla configurazione.
  3. **`imageGenerationModel.fallbacks`** in ordine.
  4. **Rilevamento automatico** : solo valori predefiniti dei provider con autenticazione: 
     * prima il provider predefinito corrente;
     * poi i restanti provider registrati per generazione immagini in ordine di ID provider.


Se un provider fallisce (errore di autenticazione, limite di frequenza, ecc.), il candidato configurato successivo viene provato automaticamente. Se tutti falliscono, l'errore include i dettagli di ogni tentativo.

Gli override del modello per chiamata sono esatti

Un override `model` per chiamata prova solo quel provider/modello e non continua con primary/fallback configurati o provider rilevati automaticamente.

Il rilevamento automatico è consapevole dell'autenticazione

Il valore predefinito di un provider entra nell'elenco dei candidati solo quando OpenClaw può effettivamente autenticare quel provider. Imposta `agents.defaults.mediaGenerationAutoProviderFallback: false` per usare solo voci esplicite `model`, `primary` e `fallbacks`.

Timeout

Imposta `agents.defaults.imageGenerationModel.timeoutMs` per backend di immagini lenti. Un parametro dello strumento `timeoutMs` per chiamata sovrascrive il valore predefinito configurato. Le chiamate agli strumenti dinamici di Codex rispettano lo stesso budget di timeout, limitato dal massimo di 600000 ms del bridge per strumenti dinamici di OpenClaw.

Ispeziona a runtime

Usa `action: "list"` per ispezionare i provider attualmente registrati, i loro modelli predefiniti e i suggerimenti per le variabili d'ambiente di autenticazione.

### Modifica delle immagini

OpenAI, OpenRouter, Google, DeepInfra, fal, MiniMax, ComfyUI e xAI supportano la modifica delle immagini di riferimento. Passa un percorso o URL di un'immagine di riferimento:

textCopy code
[code]
    "Generate a watercolor version of this photo" + image: "/path/to/photo.jpg"
[/code]

OpenAI, OpenRouter, Google e xAI supportano fino a 5 immagini di riferimento tramite il parametro `images`. fal supporta 1 immagine di riferimento per Flux image-to-image, fino a 10 per le modifiche GPT Image 2 e fino a 14 per le modifiche Nano Banana 2. MiniMax e ComfyUI ne supportano 1.

## Approfondimenti sui provider

OpenAI gpt-image-2 (and gpt-image-1.5)

La generazione di immagini OpenAI usa per impostazione predefinita `openai/gpt-image-2`. Se è configurato un profilo OAuth `openai-codex`, OpenClaw riutilizza lo stesso profilo OAuth usato dai modelli chat in abbonamento Codex e invia la richiesta immagine tramite il backend Codex Responses. Gli URL di base Codex legacy come `https://chatgpt.com/backend-api` vengono canonicalizzati in `https://chatgpt.com/backend-api/codex` per le richieste immagine. OpenClaw **non** ripiega silenziosamente su `OPENAI_API_KEY` per quella richiesta - per forzare l'instradamento diretto tramite OpenAI Images API, configura esplicitamente `models.providers.openai` con una chiave API, un URL di base personalizzato o un endpoint Azure.

I modelli `openai/gpt-image-1.5`, `openai/gpt-image-1` e `openai/gpt-image-1-mini` possono ancora essere selezionati esplicitamente. Usa `gpt-image-1.5` per output PNG/WebP con sfondo trasparente; l'API attuale `gpt-image-2` rifiuta `background: "transparent"`.

`gpt-image-2` supporta sia la generazione text-to-image sia la modifica con immagini di riferimento tramite lo stesso strumento `image_generate`. OpenClaw inoltra `prompt`, `count`, `size`, `quality`, `outputFormat` e le immagini di riferimento a OpenAI. OpenAI **non** riceve direttamente `aspectRatio` o `resolution`; quando possibile OpenClaw mappa questi valori in una `size` supportata, altrimenti lo strumento li segnala come override ignorati.

Le opzioni specifiche di OpenAI si trovano nell'oggetto `openai`:

jsonCopy code
[code]
    {  "quality": "low",  "outputFormat": "jpeg",  "openai": {    "background": "opaque",    "moderation": "low",    "outputCompression": 60,    "user": "end-user-42"  }}
[/code]

`openai.background` accetta `transparent`, `opaque` o `auto`; gli output trasparenti richiedono `outputFormat` `png` o `webp` e un modello immagine OpenAI compatibile con la trasparenza. OpenClaw instrada le richieste predefinite `gpt-image-2` con sfondo trasparente verso `gpt-image-1.5`. `openai.outputCompression` si applica agli output JPEG/WebP.

Il suggerimento di primo livello `background` è neutrale rispetto al provider e attualmente viene mappato allo stesso campo di richiesta OpenAI `background` quando è selezionato il provider OpenAI. I provider che non dichiarano il supporto per lo sfondo lo restituiscono in `ignoredOverrides` invece di ricevere il parametro non supportato.

Per instradare la generazione di immagini OpenAI tramite una distribuzione Azure OpenAI invece di `api.openai.com`, consulta [endpoint Azure OpenAI](</it/providers/openai#azure-openai-endpoints>).

OpenRouter image models

La generazione di immagini OpenRouter usa la stessa `OPENROUTER_API_KEY` e passa attraverso l'API immagini per chat completions di OpenRouter. Seleziona i modelli immagine OpenRouter con il prefisso `openrouter/`:

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "openrouter/google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

OpenClaw inoltra `prompt`, `count`, le immagini di riferimento e i suggerimenti `aspectRatio` / `resolution` compatibili con Gemini a OpenRouter. Le scorciatoie integrate attuali per i modelli immagine OpenRouter includono `google/gemini-3.1-flash-image-preview`, `google/gemini-3-pro-image-preview` e `openai/gpt-5.4-image-2`. Usa `action: "list"` per vedere cosa espone il Plugin configurato.

MiniMax dual-auth

La generazione di immagini MiniMax è disponibile tramite entrambi i percorsi di autenticazione MiniMax inclusi:

  * `minimax/image-01` per configurazioni con chiave API
  * `minimax-portal/image-01` per configurazioni OAuth

xAI grok-imagine-image

Il provider xAI incluso usa `/v1/images/generations` per le richieste con solo prompt e `/v1/images/edits` quando è presente `image` o `images`.

  * Modelli: `xai/grok-imagine-image`, `xai/grok-imagine-image-pro`
  * Conteggio: fino a 4
  * Riferimenti: una `image` o fino a cinque `images`
  * Rapporti d'aspetto: `1:1`, `16:9`, `9:16`, `4:3`, `3:4`, `2:3`, `3:2`
  * Risoluzioni: `1K`, `2K`
  * Output: restituiti come allegati immagine gestiti da OpenClaw


OpenClaw intenzionalmente non espone `quality`, `mask`, `user` specifici di xAI, né rapporti d'aspetto aggiuntivi solo nativi, finché tali controlli non esistono nel contratto condiviso cross-provider `image_generate`.

## Esempi

### Generate (4K landscape)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="A clean editorial poster for OpenClaw image generation" size=3840x2160 count=1
[/code]

### Generate (transparent PNG)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-1.5 prompt="A simple red circle sticker on a transparent background" outputFormat=png background=transparent
[/code]

CLI equivalente:

bashCopy code
[code]
    openclaw infer image generate \--model openai/gpt-image-1.5 \--output-format png \--background transparent \--prompt "A simple red circle sticker on a transparent background" \--json
[/code]

### Generate (two square)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Two visual directions for a calm productivity app icon" size=1024x1024 count=2
[/code]

### Edit (one reference)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Keep the subject, replace the background with a bright studio setup" image=/path/to/reference.png size=1024x1536
[/code]

### Edit (multiple references)

textCopy code
[code]
    /tool image_generate action=generate model=openai/gpt-image-2 prompt="Combine the character identity from the first image with the color palette from the second" images='["/path/to/character.png","/path/to/palette.jpg"]' size=1536x1024
[/code]

Gli stessi flag `--output-format` e `--background` sono disponibili su `openclaw infer image edit`; `--openai-background` resta un alias specifico di OpenAI. I provider inclusi diversi da OpenAI oggi non dichiarano un controllo esplicito dello sfondo, quindi `background: "transparent"` viene segnalato come ignorato per loro.

## Correlati

  * [Panoramica degli strumenti](</it/tools>) \- tutti gli strumenti agent disponibili
  * [ComfyUI](</it/providers/comfy>) \- configurazione del workflow ComfyUI locale e Comfy Cloud
  * [fal](</it/providers/fal>) \- configurazione del provider immagini e video fal
  * [Google (Gemini)](</it/providers/google>) \- configurazione del provider immagini Gemini
  * [MiniMax](</it/providers/minimax>) \- configurazione del provider immagini MiniMax
  * [OpenAI](</it/providers/openai>) \- configurazione del provider OpenAI Images
  * [Vydra](</it/providers/vydra>) \- configurazione di immagini, video e voce Vydra
  * [xAI](</it/providers/xai>) \- configurazione di immagini Grok, video, ricerca, esecuzione di codice e TTS
  * [Riferimento di configurazione](</it/gateway/config-agents#agent-defaults>) \- configurazione `imageGenerationModel`
  * [Modelli](</it/concepts/models>) \- configurazione dei modelli e failover


Was this useful?YesNo