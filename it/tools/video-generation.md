---
title: Generazione di video
source_url: https://docs.openclaw.ai/it/tools/video-generation
scraped_at: 2026-05-25
---

Gli agenti OpenClaw possono generare video da prompt di testo, immagini di riferimento o video esistenti. Sono supportati sedici backend di fornitori, ciascuno con opzioni di modello, modalità di input e set di funzionalità diversi. L'agente sceglie automaticamente il fornitore corretto in base alla tua configurazione e alle chiavi API disponibili.

OpenClaw tratta la generazione video come tre modalità di runtime:

  * `generate` \- richieste da testo a video senza media di riferimento.
  * `imageToVideo` \- la richiesta include una o più immagini di riferimento.
  * `videoToVideo` \- la richiesta include uno o più video di riferimento.


I fornitori possono supportare qualsiasi sottoinsieme di queste modalità. Lo strumento convalida la modalità attiva prima dell'invio e segnala le modalità supportate in `action=list`.

## Avvio rapido

* ### Configura l'autenticazione

Imposta una chiave API per qualsiasi fornitore supportato:

bashCopy code
[code]
    export GEMINI_API_KEY="your-key"
[/code]

* ### Scegli un modello predefinito (opzionale)

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "google/veo-3.1-fast-generate-preview"
[/code]

* ### Chiedi all'agente

> Genera un video cinematografico di 5 secondi di un'aragosta amichevole che fa surf al tramonto.

L'agente chiama automaticamente `video_generate`. Non è necessario consentire esplicitamente lo strumento.

## Come funziona la generazione asincrona

La generazione video è asincrona. Quando l'agente chiama `video_generate` in una sessione:

  1. OpenClaw invia la richiesta al fornitore e restituisce immediatamente un ID attività.
  2. Il fornitore elabora il job in background (in genere da 30 secondi a diversi minuti a seconda del fornitore e della risoluzione; i fornitori lenti basati su coda possono arrivare fino al timeout configurato).
  3. Quando il video è pronto, OpenClaw riattiva la stessa sessione con un evento interno di completamento.
  4. L'agente informa l'utente e allega il video completato. Nelle chat di gruppo/canale che usano la consegna visibile solo tramite strumento di messaggistica, l'agente inoltra il risultato tramite lo strumento di messaggistica invece che pubblicarlo direttamente con OpenClaw.


Mentre un job è in corso, le chiamate `video_generate` duplicate nella stessa sessione restituiscono lo stato dell'attività corrente invece di avviare un'altra generazione. Usa `openclaw tasks list` o `openclaw tasks show <taskId>` per controllare l'avanzamento dalla CLI.

Al di fuori delle esecuzioni dell'agente supportate da sessione (ad esempio, invocazioni dirette dello strumento), lo strumento ricade sulla generazione inline e restituisce il percorso del media finale nello stesso turno.

I file video generati vengono salvati nell'archiviazione media gestita da OpenClaw quando il fornitore restituisce byte. Il limite predefinito di salvataggio dei video generati segue il limite dei media video e `agents.defaults.mediaMaxMb` lo aumenta per render più grandi. Quando un fornitore restituisce anche un URL di output ospitato, OpenClaw può consegnare quell'URL invece di far fallire l'attività se la persistenza locale rifiuta un file troppo grande.

### Ciclo di vita dell'attività

Stato | Significato  
---|---  
`queued` | Attività creata, in attesa che il fornitore la accetti.  
`running` | Il fornitore sta elaborando (in genere da 30 secondi a diversi minuti a seconda del fornitore e della risoluzione).  
`succeeded` | Video pronto; l'agente si riattiva e lo pubblica nella conversazione.  
`failed` | Errore del fornitore o timeout; l'agente si riattiva con i dettagli dell'errore.  
  
Controlla lo stato dalla CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

Se un'attività video è già `queued` o `running` per la sessione corrente, `video_generate` restituisce lo stato dell'attività esistente invece di avviarne una nuova. Usa `action: "status"` per controllare esplicitamente senza attivare una nuova generazione.

## Fornitori supportati

Fornitore | Modello predefinito | Testo | Rif. immagine | Rif. video | Autenticazione  
---|---|---|---|---|---  
Alibaba | `wan2.6-t2v` | ✓ | Sì (URL remoto) | Sì (URL remoto) | `MODELSTUDIO_API_KEY`  
BytePlus (1.0) | `seedance-1-0-pro-250528` | ✓ | Fino a 2 immagini (solo modelli I2V; primo + ultimo fotogramma) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 1.5 | `seedance-1-5-pro-251215` | ✓ | Fino a 2 immagini (primo + ultimo fotogramma tramite ruolo) | - | `BYTEPLUS_API_KEY`  
BytePlus Seedance 2.0 | `dreamina-seedance-2-0-260128` | ✓ | Fino a 9 immagini di riferimento | Fino a 3 video | `BYTEPLUS_API_KEY`  
ComfyUI | `workflow` | ✓ | 1 immagine | - | `COMFY_API_KEY` o `COMFY_CLOUD_API_KEY`  
DeepInfra | `Pixverse/Pixverse-T2V` | ✓ | - | - | `DEEPINFRA_API_KEY`  
fal | `fal-ai/minimax/video-01-live` | ✓ | 1 immagine; fino a 9 con Seedance da riferimento a video | Fino a 3 video con Seedance da riferimento a video | `FAL_KEY`  
Google | `veo-3.1-fast-generate-preview` | ✓ | 1 immagine | 1 video | `GEMINI_API_KEY`  
MiniMax | `MiniMax-Hailuo-2.3` | ✓ | 1 immagine | - | `MINIMAX_API_KEY` o MiniMax OAuth  
OpenAI | `sora-2` | ✓ | 1 immagine | 1 video | `OPENAI_API_KEY`  
OpenRouter | `google/veo-3.1-fast` | ✓ | Fino a 4 immagini (primo/ultimo fotogramma o riferimenti) | - | `OPENROUTER_API_KEY`  
Qwen | `wan2.6-t2v` | ✓ | Sì (URL remoto) | Sì (URL remoto) | `QWEN_API_KEY`  
Runway | `gen4.5` | ✓ | 1 immagine | 1 video | `RUNWAYML_API_SECRET`  
Together | `Wan-AI/Wan2.2-T2V-A14B` | ✓ | 1 immagine | - | `TOGETHER_API_KEY`  
Vydra | `veo3` | ✓ | 1 immagine (`kling`) | - | `VYDRA_API_KEY`  
xAI | `grok-imagine-video` | ✓ | 1 immagine del primo fotogramma o fino a 7 `reference_image` | 1 video | `XAI_API_KEY`  
  
Alcuni fornitori accettano variabili di ambiente aggiuntive o alternative per le chiavi API. Consulta le singole pagine dei fornitori per i dettagli.

Esegui `video_generate action=list` per ispezionare fornitori, modelli e modalità di runtime disponibili in fase di esecuzione.

### Matrice delle capacità

Il contratto di modalità esplicito usato da `video_generate`, dai test di contratto e dallo sweep live condiviso:

Fornitore | `generate` | `imageToVideo` | `videoToVideo` | Lane live condivise oggi  
---|---|---|---|---  
Alibaba | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` saltato perché questo fornitore richiede URL video remoti `http(s)`  
BytePlus | ✓ | ✓ | - | `generate`, `imageToVideo`  
ComfyUI | ✓ | ✓ | - | Non incluso nello sweep condiviso; la copertura specifica del workflow vive con i test Comfy  
DeepInfra | ✓ | - | - | `generate`; gli schemi video nativi di DeepInfra sono da testo a video nel contratto incluso  
fal | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` solo quando si usa Seedance da riferimento a video  
Google | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` condiviso saltato perché lo sweep Gemini/Veo corrente basato su buffer non accetta quell'input  
MiniMax | ✓ | ✓ | - | `generate`, `imageToVideo`  
OpenAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` condiviso saltato perché questo percorso org/input richiede attualmente accesso inpaint/remix lato fornitore  
OpenRouter | ✓ | ✓ | - | `generate`, `imageToVideo`  
Qwen | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` saltato perché questo fornitore richiede URL video remoti `http(s)`  
Runway | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` viene eseguito solo quando il modello selezionato è `runway/gen4_aleph`  
Together | ✓ | ✓ | - | `generate`, `imageToVideo`  
Vydra | ✓ | ✓ | - | `generate`; `imageToVideo` condiviso saltato perché `veo3` incluso è solo testo e `kling` incluso richiede un URL immagine remoto  
xAI | ✓ | ✓ | ✓ | `generate`, `imageToVideo`; `videoToVideo` saltato perché questo fornitore attualmente richiede un URL MP4 remoto  
  
## Parametri dello strumento

### Obbligatori

Descrizione testuale del video da generare. Obbligatoria per `action: "generate"`.

### Input di contenuto

Suggerimenti di ruolo opzionali per posizione, paralleli all'elenco combinato delle immagini. Valori canonici: `first_frame`, `last_frame`, `reference_image`.

Suggerimenti di ruolo opzionali per posizione, paralleli all'elenco combinato dei video. Valore canonico: `reference_video`.

Singolo audio di riferimento (percorso o URL). Usato per musica di sottofondo o come riferimento vocale quando il provider supporta input audio.

Suggerimenti di ruolo opzionali per posizione, paralleli all'elenco combinato degli audio. Valore canonico: `reference_audio`.

### Controlli dello stile

Suggerimento per le proporzioni, come `1:1`, `16:9`, `9:16`, `adaptive` o un valore specifico del provider. OpenClaw normalizza o ignora i valori non supportati in base al provider.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc29sdXRpb24iIHR5cGU9InN0cmluZyI Suggerimento per la risoluzione, come `480P`, `720P`, `768P`, `1080P`, `4K` o un valore specifico del provider. OpenClaw normalizza o ignora i valori non supportati in base al provider. OPENCLAW_DOCS_MARKER:paramClose:

Durata di destinazione in secondi (arrotondata al valore supportato dal provider più vicino).

Abilita l'audio generato nell'output quando supportato. Distinto da `audioRef*` (input).

`adaptive` è un sentinel specifico del provider: viene inoltrato così com'è ai provider che dichiarano `adaptive` nelle proprie capacità (ad esempio BytePlus Seedance lo usa per rilevare automaticamente le proporzioni dalle dimensioni dell'immagine di input). I provider che non lo dichiarano espongono il valore tramite `details.ignoredOverrides` nel risultato dello strumento, così lo scarto è visibile.

### Avanzate

`"status"` restituisce il task della sessione corrente; `"list"` ispeziona i provider.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Override di provider/modello (ad esempio `runway/gen4.5`). OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Timeout opzionale dell'operazione del provider in millisecondi. Se omesso, OpenClaw usa `agents.defaults.videoGenerationModel.timeoutMs` se configurato. OPENCLAW_DOCS_MARKER:paramClose:

Opzioni specifiche del provider come oggetto JSON (ad esempio `{"seed": 42, "draft": true}`). I provider che dichiarano uno schema tipizzato convalidano chiavi e tipi; chiavi sconosciute o mismatch escludono il candidato durante il fallback. I provider senza uno schema dichiarato ricevono le opzioni così come sono. Esegui `video_generate action=list` per vedere cosa accetta ciascun provider.

Gli input di riferimento selezionano la modalità runtime:

  * Nessun media di riferimento → `generate`
  * Qualsiasi riferimento immagine → `imageToVideo`
  * Qualsiasi riferimento video → `videoToVideo`
  * Gli input audio di riferimento **non** cambiano la modalità risolta; si applicano sopra qualsiasi modalità selezionata dai riferimenti immagine/video e funzionano solo con provider che dichiarano `maxInputAudios`.


Riferimenti misti di immagini e video non sono una superficie di capacità condivisa stabile. Preferisci un solo tipo di riferimento per richiesta.

#### Fallback e opzioni tipizzate

Alcuni controlli di capacità vengono applicati a livello di fallback invece che al confine dello strumento, quindi una richiesta che supera i limiti del provider primario può comunque essere eseguita su un fallback capace:

  * Il candidato attivo che non dichiara `maxInputAudios` (o dichiara `0`) viene saltato quando la richiesta contiene riferimenti audio; viene provato il candidato successivo.
  * Il `maxDurationSeconds` del candidato attivo è inferiore al `durationSeconds` richiesto senza un elenco `supportedDurationSeconds` dichiarato → saltato.
  * La richiesta contiene `providerOptions` e il candidato attivo dichiara esplicitamente uno schema `providerOptions` tipizzato → saltato se le chiavi fornite non sono nello schema o i tipi dei valori non corrispondono. I provider senza uno schema dichiarato ricevono le opzioni così come sono (pass-through retrocompatibile). Un provider può disattivare tutte le opzioni del provider dichiarando uno schema vuoto (`capabilities.providerOptions: {}`), il che causa lo stesso salto di un mismatch di tipo.


Il primo motivo di salto in una richiesta viene registrato a livello `warn`, così gli operatori vedono quando il loro provider primario è stato ignorato; i salti successivi vengono registrati a livello `debug` per mantenere silenziose le catene di fallback lunghe. Se ogni candidato viene saltato, l'errore aggregato include il motivo di salto per ciascuno.

## Azioni

Azione | Cosa fa  
---|---  
`generate` | Predefinita. Crea un video dal prompt fornito e dagli input di riferimento opzionali.  
`status` | Controlla lo stato del task video in corso per la sessione corrente senza avviare un'altra generazione.  
`list` | Mostra i provider, i modelli e le loro capacità disponibili.  
  
## Selezione del modello

OpenClaw risolve il modello in questo ordine:

  1. **Parametro strumento`model`** \- se l'agente ne specifica uno nella chiamata.
  2. **`videoGenerationModel.primary`** dalla configurazione.
  3. **`videoGenerationModel.fallbacks`** in ordine.
  4. **Rilevamento automatico** \- provider con autenticazione valida, a partire dal provider predefinito corrente, poi i provider rimanenti in ordine alfabetico.


Se un provider fallisce, il candidato successivo viene provato automaticamente. Se tutti i candidati falliscono, l'errore include i dettagli di ogni tentativo.

Imposta `agents.defaults.mediaGenerationAutoProviderFallback: false` per usare solo le voci esplicite `model`, `primary` e `fallbacks`.

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",        fallbacks: ["runway/gen4.5", "qwen/wan2.6-t2v"],      },    },  },}
[/code]

## Note sui provider

Alibaba

Usa l'endpoint asincrono DashScope / Model Studio. Le immagini e i video di riferimento devono essere URL remoti `http(s)`.

BytePlus (1.0)

ID provider: `byteplus`.

Modelli: `seedance-1-0-pro-250528` (predefinito), `seedance-1-0-pro-t2v-250528`, `seedance-1-0-pro-fast-251015`, `seedance-1-0-lite-t2v-250428`, `seedance-1-0-lite-i2v-250428`.

I modelli T2V (`*-t2v-*`) non accettano input immagine; i modelli I2V e i modelli generali `*-pro-*` supportano una singola immagine di riferimento (primo frame). Passa l'immagine posizionalmente o imposta `role: "first_frame"`. Gli ID dei modelli T2V vengono automaticamente cambiati nella variante I2V corrispondente quando viene fornita un'immagine.

Chiavi `providerOptions` supportate: `seed` (numero), `draft` (booleano - forza 480p), `camera_fixed` (booleano).

BytePlus Seedance 1.5

Richiede il Plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). ID provider: `byteplus-seedance15`. Modello: `seedance-1-5-pro-251215`.

Usa l'API unificata `content[]`. Supporta al massimo 2 immagini di input (`first_frame` \+ `last_frame`). Tutti gli input devono essere URL remoti `https://`. Imposta `role: "first_frame"` / `"last_frame"` su ogni immagine oppure passa le immagini posizionalmente.

`aspectRatio: "adaptive"` rileva automaticamente le proporzioni dall'immagine di input. `audio: true` viene mappato a `generate_audio`. `providerOptions.seed` (numero) viene inoltrato.

BytePlus Seedance 2.0

Richiede il Plugin [`@openclaw/byteplus-modelark`](<https://www.npmjs.com/package/@openclaw/byteplus-modelark>). ID provider: `byteplus-seedance2`. Modelli: `dreamina-seedance-2-0-260128`, `dreamina-seedance-2-0-fast-260128`.

Usa l'API unificata `content[]`. Supporta fino a 9 immagini di riferimento, 3 video di riferimento e 3 audio di riferimento. Tutti gli input devono essere URL remoti `https://`. Imposta `role` su ogni asset - valori supportati: `"first_frame"`, `"last_frame"`, `"reference_image"`, `"reference_video"`, `"reference_audio"`.

`aspectRatio: "adaptive"` rileva automaticamente le proporzioni dall'immagine di input. `audio: true` viene mappato a `generate_audio`. `providerOptions.seed` (numero) viene inoltrato.

ComfyUI

Esecuzione locale o cloud basata su workflow. Supporta text-to-video e image-to-video tramite il grafo configurato.

fal

Usa un flusso basato su coda per i job di lunga durata. OpenClaw attende fino a 20 minuti per impostazione predefinita prima di considerare scaduto un job della coda fal ancora in corso. La maggior parte dei modelli video fal accetta un singolo riferimento immagine. I modelli Seedance 2.0 reference-to-video accettano fino a 9 immagini, 3 video e 3 riferimenti audio, con al massimo 12 file di riferimento totali.

Google (Gemini / Veo)

Supporta un riferimento immagine o un riferimento video. Le richieste con audio generato vengono ignorate con un avviso nel percorso API Gemini perché quell'API rifiuta il parametro `generateAudio` per l'attuale generazione video Veo.

MiniMax

Solo un singolo riferimento immagine. MiniMax accetta risoluzioni `768P` e `1080P`; richieste come `720P` vengono normalizzate al valore supportato più vicino prima dell'invio.

OpenAI

Viene inoltrato solo l'override `size`. Gli altri override di stile (`aspectRatio`, `resolution`, `audio`, `watermark`) vengono ignorati con un avviso.

OpenRouter

Usa l'API asincrona `/videos` di OpenRouter. OpenClaw invia il job, interroga `polling_url` e scarica `unsigned_urls` oppure l'endpoint documentato del contenuto del job. Il valore predefinito incluso `google/veo-3.1-fast` dichiara durate di 4/6/8 secondi, risoluzioni `720P`/`1080P` e proporzioni `16:9`/`9:16`.

Qwen

Stesso backend DashScope di Alibaba. Gli input di riferimento devono essere URL remoti `http(s)`; i file locali vengono rifiutati in anticipo.

Runway

Supporta file locali tramite data URI. Video-to-video richiede `runway/gen4_aleph`. Le esecuzioni solo testo espongono proporzioni `16:9` e `9:16`.

Together

Solo un singolo riferimento immagine.

Vydra

Usa direttamente `https://www.vydra.ai/api/v1` per evitare redirect che eliminano l'autenticazione. `veo3` è incluso solo come text-to-video; `kling` richiede un URL immagine remoto.

xAI

Supporta text-to-video, image-to-video con una singola immagine del primo frame, fino a 7 input `reference_image` tramite `reference_images` di xAI e flussi remoti di modifica/estensione video.

## Modalità delle capacità dei provider

Il contratto condiviso di generazione video supporta capacità specifiche per modalità anziché solo limiti aggregati piatti. Le nuove implementazioni dei provider dovrebbero preferire blocchi di modalità espliciti:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxVideos: 1,    maxDurationSeconds: 10,    supportsResolution: true,  },  imageToVideo: {    enabled: true,    maxVideos: 1,    maxInputImages: 1,    maxInputImagesByModel: { "provider/reference-to-video": 9 },    maxDurationSeconds: 5,  },  videoToVideo: {    enabled: true,    maxVideos: 1,    maxInputVideos: 1,    maxDurationSeconds: 5,  },}
[/code]

Campi aggregati piatti come `maxInputImages` e `maxInputVideos` **non** sono sufficienti per dichiarare il supporto della modalità di trasformazione. I provider dovrebbero dichiarare esplicitamente `generate`, `imageToVideo` e `videoToVideo` affinché i test live, i test di contratto e lo strumento condiviso `video_generate` possano convalidare il supporto delle modalità in modo deterministico.

Quando un modello in un provider ha un supporto per input di riferimento più ampio rispetto agli altri, usa `maxInputImagesByModel`, `maxInputVideosByModel` o `maxInputAudiosByModel` invece di aumentare il limite dell'intera modalità.

## Test live

Copertura live opzionale per i provider inclusi condivisi:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/video-generation-providers.live.test.ts
[/code]

Wrapper del repo:

bashCopy code
[code]
    pnpm test:live:media video
[/code]

Questo file live carica le variabili d'ambiente mancanti dei provider da `~/.profile`, preferisce per impostazione predefinita le chiavi API live/da ambiente rispetto ai profili di autenticazione salvati ed esegue uno smoke test sicuro per la release per impostazione predefinita:

  * `generate` per ogni provider non FAL nello sweep.
  * Prompt di un'aragosta della durata di un secondo.
  * Limite di operazioni per provider da `OPENCLAW_LIVE_VIDEO_GENERATION_TIMEOUT_MS` (`180000` per impostazione predefinita).


FAL è opzionale perché la latenza della coda lato provider può dominare il tempo di release:

bashCopy code
[code]
    pnpm test:live:media video --video-providers fal
[/code]

Imposta `OPENCLAW_LIVE_VIDEO_GENERATION_FULL_MODES=1` per eseguire anche le modalità di trasformazione dichiarate che lo sweep condiviso può esercitare in sicurezza con media locali:

  * `imageToVideo` quando `capabilities.imageToVideo.enabled`.
  * `videoToVideo` quando `capabilities.videoToVideo.enabled` e il provider/modello accetta input video locali basati su buffer nello sweep condiviso.


Oggi la lane live condivisa `videoToVideo` copre `runway` solo quando selezioni `runway/gen4_aleph`.

## Configurazione

Imposta il modello predefinito di generazione video nella tua configurazione OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "qwen/wan2.6-t2v",        fallbacks: ["qwen/wan2.6-r2v-flash"],      },    },  },}
[/code]

Oppure tramite la CLI:

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "qwen/wan2.6-t2v"
[/code]

## Correlati

  * [Alibaba Model Studio](</it/providers/alibaba>)
  * [Attività in background](</it/automation/tasks>) \- tracciamento delle attività per la generazione video asincrona
  * [BytePlus](</it/concepts/model-providers#byteplus-international>)
  * [ComfyUI](</it/providers/comfy>)
  * [Riferimento di configurazione](</it/gateway/config-agents#agent-defaults>)
  * [fal](</it/providers/fal>)
  * [Google (Gemini)](</it/providers/google>)
  * [MiniMax](</it/providers/minimax>)
  * [Modelli](</it/concepts/models>)
  * [OpenAI](</it/providers/openai>)
  * [Qwen](</it/providers/qwen>)
  * [Runway](</it/providers/runway>)
  * [Together AI](</it/providers/together>)
  * [Panoramica degli strumenti](</it/tools>)
  * [Vydra](</it/providers/vydra>)
  * [xAI](</it/providers/xai>)


Was this useful?YesNo