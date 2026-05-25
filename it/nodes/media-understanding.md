---
title: Comprensione dei contenuti multimediali
source_url: https://docs.openclaw.ai/it/nodes/media-understanding
scraped_at: 2026-05-25
---

OpenClaw può **riassumere i contenuti multimediali in ingresso** (immagini/audio/video) prima dell'esecuzione della pipeline di risposta. Rileva automaticamente quando sono disponibili strumenti locali o chiavi dei provider e può essere disabilitato o personalizzato. Se la comprensione è disattivata, i modelli ricevono comunque i file/URL originali come di consueto.

Il comportamento multimediale specifico del fornitore viene registrato dai plugin del fornitore, mentre il core di OpenClaw gestisce la configurazione condivisa `tools.media`, l'ordine di fallback e l'integrazione della pipeline di risposta.

## Obiettivi

  * Facoltativo: pre-elaborare i contenuti multimediali in ingresso in testo breve per un instradamento più rapido e un parsing dei comandi migliore.
  * Conservare la consegna dei contenuti multimediali originali al modello (sempre).
  * Supportare **API dei provider** e **fallback CLI**.
  * Consentire più modelli con fallback ordinato (errore/dimensione/timeout).


## Comportamento ad alto livello

* ### Raccogli allegati

Raccogli gli allegati in ingresso (`MediaPaths`, `MediaUrls`, `MediaTypes`).

* ### Seleziona per capacità

Per ogni capacità abilitata (immagine/audio/video), seleziona gli allegati in base alla policy (predefinito: **primo**).

* ### Scegli modello

Scegli la prima voce modello idonea (dimensione + capacità + autenticazione).

* ### Fallback in caso di errore

Se un modello non riesce o il contenuto multimediale è troppo grande, **passa alla voce successiva**.

* ### Applica blocco di successo

In caso di successo:

  * `Body` diventa un blocco `[Image]`, `[Audio]` o `[Video]`.
  * L'audio imposta `{{Transcript}}`; il parsing dei comandi usa il testo della didascalia quando presente, altrimenti la trascrizione.
  * Le didascalie vengono conservate come `User text:` all'interno del blocco.


Se la comprensione non riesce o è disabilitata, **il flusso di risposta continua** con il corpo originale + allegati.

## Panoramica della configurazione

`tools.media` supporta **modelli condivisi** più override per capacità:

Chiavi di primo livello

  * `tools.media.models`: elenco di modelli condivisi (usa `capabilities` per limitare).
  * `tools.media.image` / `tools.media.audio` / `tools.media.video`: 
    * valori predefiniti (`prompt`, `maxChars`, `maxBytes`, `timeoutSeconds`, `language`)
    * override dei provider (`baseUrl`, `headers`, `providerOptions`)
    * opzioni audio Deepgram tramite `tools.media.audio.providerOptions.deepgram`
    * controlli di eco della trascrizione audio (`echoTranscript`, predefinito `false`; `echoFormat`)
    * **elenco`models` per capacità** facoltativo (preferito prima dei modelli condivisi)
    * policy `attachments` (`mode`, `maxAttachments`, `prefer`)
    * `scope` (gating facoltativo per canale/chatType/chiave sessione)
  * `tools.media.concurrency`: esecuzioni concorrenti massime per capacità (predefinito **2**).


json5Copy code
[code]
    {  tools: {    media: {      models: [        /* shared list */      ],      image: {        /* optional overrides */      },      audio: {        /* optional overrides */        echoTranscript: true,        echoFormat: '📝 "{transcript}"',      },      video: {        /* optional overrides */      },    },  },}
[/code]

### Voci modello

Ogni voce `models[]` può essere **provider** o **CLI** :

### Voce provider

json5Copy code
[code]
    {  type: "provider", // default if omitted  provider: "openai",  model: "gpt-5.5",  prompt: "Describe the image in <= 500 chars.",  maxChars: 500,  maxBytes: 10485760,  timeoutSeconds: 60,  capabilities: ["image"], // optional, used for multi-modal entries  profile: "vision-profile",  preferredProfile: "vision-fallback",}
[/code]

### Voce CLI

json5Copy code
[code]
    {  type: "cli",  command: "gemini",  args: [    "-m",    "gemini-3-flash",    "--allowed-tools",    "read_file",    "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",  ],  maxChars: 500,  maxBytes: 52428800,  timeoutSeconds: 120,  capabilities: ["video", "image"],}
[/code]

I template CLI possono usare anche:

  * `{{MediaDir}}` (directory contenente il file multimediale)
  * `{{OutputDir}}` (directory temporanea creata per questa esecuzione)
  * `{{OutputBase}}` (percorso base del file temporaneo, senza estensione)


## Valori predefiniti e limiti

Valori predefiniti consigliati:

  * `maxChars`: **500** per immagine/video (breve, adatto ai comandi)
  * `maxChars`: **non impostato** per audio (trascrizione completa a meno che tu non imposti un limite)
  * `maxBytes`: 
    * immagine: **10MB**
    * audio: **20MB**
    * video: **50MB**


Regole

  * Se il contenuto multimediale supera `maxBytes`, quel modello viene saltato e viene provato il **modello successivo**.
  * I file audio più piccoli di **1024 byte** vengono trattati come vuoti/corrotti e saltati prima della trascrizione provider/CLI; il contesto di risposta in ingresso riceve una trascrizione segnaposto deterministica in modo che l'agente sappia che la nota era troppo piccola.
  * Se il modello restituisce più di `maxChars`, l'output viene troncato.
  * `prompt` usa come valore predefinito un semplice "Describe the {media}." più le indicazioni di `maxChars` (solo immagine/video).
  * Se il modello immagine primario attivo supporta già nativamente la visione, OpenClaw salta il blocco di riepilogo `[Image]` e passa invece l'immagine originale al modello.
  * Se un modello primario Gateway/WebChat è solo testo, gli allegati immagine vengono conservati come riferimenti `media://inbound/*` esternalizzati, così gli strumenti immagine/PDF o il modello immagine configurato possono ancora ispezionarli invece di perdere l'allegato.
  * Le richieste esplicite `openclaw infer image describe --model <provider/model>` sono diverse: eseguono direttamente quel provider/modello con capacità immagine, inclusi riferimenti Ollama come `ollama/qwen2.5vl:7b`.
  * Se `<capability>.enabled: true` ma non sono configurati modelli, OpenClaw prova il **modello di risposta attivo** quando il suo provider supporta la capacità.


### Rilevamento automatico della comprensione multimediale (predefinito)

Se `tools.media.<capability>.enabled` **non** è impostato su `false` e non hai configurato modelli, OpenClaw rileva automaticamente in questo ordine e **si ferma alla prima opzione funzionante** :

* ### Modello di risposta attivo

Modello di risposta attivo quando il suo provider supporta la capacità.

* ### agents.defaults.imageModel

Riferimenti primario/fallback di `agents.defaults.imageModel` (solo immagine). Preferisci riferimenti `provider/model`. I riferimenti semplici vengono qualificati dalle voci dei modelli provider configurati con capacità immagine solo quando la corrispondenza è univoca.

* ### CLI locali (solo audio)

CLI locali (se installate):

  * `sherpa-onnx-offline` (richiede `SHERPA_ONNX_MODEL_DIR` con encoder/decoder/joiner/tokens)
  * `whisper-cli` (`whisper-cpp`; usa `WHISPER_CPP_MODEL` o il modello tiny incluso)
  * `whisper` (CLI Python; scarica automaticamente i modelli)


* ### CLI Gemini

`gemini` che usa `read_many_files`.

* ### Autenticazione provider

  * Le voci `models.providers.*` configurate che supportano la capacità vengono provate prima dell'ordine di fallback incluso.
  * I provider di configurazione solo immagine con un modello con capacità immagine si registrano automaticamente per la comprensione multimediale anche quando non sono un plugin fornitore incluso.
  * La comprensione immagini Ollama è disponibile quando selezionata esplicitamente, ad esempio tramite `agents.defaults.imageModel` o `openclaw infer image describe --model ollama/<vision-model>`.


Ordine di fallback incluso:

  * Audio: OpenAI → Groq → xAI → Deepgram → OpenRouter → Google → SenseAudio → ElevenLabs → Mistral
  * Immagine: OpenAI → Anthropic → Google → MiniMax → MiniMax Portal → [Z.AI](<http://Z.AI>)
  * Video: Google → Qwen → Moonshot


Per disabilitare il rilevamento automatico, imposta:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: false,      },    },  },}
[/code]

### Supporto dell'ambiente proxy (modelli provider)

Quando la comprensione multimediale **audio** e **video** basata su provider è abilitata, OpenClaw rispetta le variabili d'ambiente proxy in uscita standard per le chiamate HTTP ai provider:

  * `HTTPS_PROXY`
  * `HTTP_PROXY`
  * `ALL_PROXY`
  * `https_proxy`
  * `http_proxy`
  * `all_proxy`


Se non sono impostate variabili d'ambiente proxy, la comprensione multimediale usa l'uscita diretta. Se il valore del proxy è malformato, OpenClaw registra un avviso e torna al recupero diretto.

## Capacità (facoltativo)

Se imposti `capabilities`, la voce viene eseguita solo per quei tipi di contenuto multimediale. Per gli elenchi condivisi, OpenClaw può inferire i valori predefiniti:

  * `openai`, `anthropic`, `minimax`: **immagine**
  * `minimax-portal`: **immagine**
  * `moonshot`: **immagine + video**
  * `openrouter`: **immagine + audio**
  * `google` (API Gemini): **immagine + audio + video**
  * `qwen`: **immagine + video**
  * `mistral`: **audio**
  * `zai`: **immagine**
  * `groq`: **audio**
  * `xai`: **audio**
  * `deepgram`: **audio**
  * Qualsiasi catalogo `models.providers.<id>.models[]` con un modello con capacità immagine: **immagine**


Per le voci CLI, **imposta`capabilities` esplicitamente** per evitare corrispondenze inattese. Se ometti `capabilities`, la voce è idonea per l'elenco in cui compare.

## Matrice di supporto dei provider (integrazioni OpenClaw)

Capacità | Integrazione provider | Note  
---|---|---  
Immagine | OpenAI, OpenAI Codex OAuth, Codex app-server, OpenRouter, Anthropic, Google, MiniMax, Moonshot, Qwen, [Z.AI](<http://Z.AI>), provider config | I plugin del fornitore registrano il supporto immagini; `openai-codex/*` usa l'impianto del provider OAuth; `codex/*` usa un turno limitato del Codex app-server; MiniMax e MiniMax OAuth usano entrambi `MiniMax-VL-01`; i provider di configurazione con capacità immagine si registrano automaticamente.  
Audio | OpenAI, Groq, xAI, Deepgram, OpenRouter, Google, SenseAudio, ElevenLabs, Mistral | Trascrizione provider (Whisper/Groq/xAI/Deepgram/OpenRouter STT/Gemini/SenseAudio/Scribe/Voxtral).  
Video | Google, Qwen, Moonshot | Comprensione video provider tramite plugin del fornitore; la comprensione video Qwen usa gli endpoint Standard DashScope.  
  
## Guida alla selezione dei modelli

  * Preferisci il modello più potente di ultima generazione disponibile per ogni capacità multimediale quando qualità e sicurezza sono importanti.
  * Per agenti con strumenti abilitati che gestiscono input non attendibili, evita modelli multimediali più vecchi/deboli.
  * Mantieni almeno un fallback per capacità per garantire disponibilità (modello di qualità + modello più rapido/economico).
  * I fallback CLI (`whisper-cli`, `whisper`, `gemini`) sono utili quando le API dei provider non sono disponibili.
  * Nota `parakeet-mlx`: con `--output-dir`, OpenClaw legge `<output-dir>/<media-basename>.txt` quando il formato di output è `txt` (o non specificato); i formati non `txt` ripiegano su stdout.


## Policy degli allegati

`attachments` per capacità controlla quali allegati vengono elaborati:

Se elaborare il primo allegato selezionato o tutti.

Limita il numero elaborato.

Preferenza di selezione tra gli allegati candidati.

Quando `mode: "all"`, gli output sono etichettati `[Image 1/2]`, `[Audio 2/2]` e così via.

Comportamento di estrazione degli allegati file

  * Il testo estratto dai file viene racchiuso come **contenuto esterno non attendibile** prima di essere aggiunto al prompt multimediale.
  * Il blocco inserito usa marcatori di confine espliciti come `<<&lt;EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` / `<<&lt;END_EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` e include una riga di metadati `Source: External`.
  * Questo percorso di estrazione degli allegati omette intenzionalmente il lungo banner `SECURITY NOTICE:` per evitare di appesantire il prompt multimediale; i marcatori di confine e i metadati rimangono comunque.
  * Se un file non contiene testo estraibile, OpenClaw inserisce `[No extractable text]`.
  * Se un PDF ricorre alle immagini di pagina renderizzate in questo percorso, il prompt multimediale mantiene il segnaposto `[PDF content rendered to images; images not forwarded to model]` perché questo passaggio di estrazione degli allegati inoltra blocchi di testo, non le immagini PDF renderizzate.


## Esempi di configurazione

### Modelli condivisi + override

json5Copy code
[code]
    {  tools: {    media: {      models: [        { provider: "openai", model: "gpt-5.5", capabilities: ["image"] },        {          provider: "google",          model: "gemini-3-flash-preview",          capabilities: ["image", "audio", "video"],        },        {          type: "cli",          command: "gemini",          args: [            "-m",            "gemini-3-flash",            "--allowed-tools",            "read_file",            "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",          ],          capabilities: ["image", "video"],        },      ],      audio: {        attachments: { mode: "all", maxAttachments: 2 },      },      video: {        maxChars: 500,      },    },  },}
[/code]

### Solo audio + video

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [          { provider: "openai", model: "gpt-4o-mini-transcribe" },          {            type: "cli",            command: "whisper",            args: ["--model", "base", "{{MediaPath}}"],          },        ],      },      video: {        enabled: true,        maxChars: 500,        models: [          { provider: "google", model: "gemini-3-flash-preview" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Solo immagini

json5Copy code
[code]
    {  tools: {    media: {      image: {        enabled: true,        maxBytes: 10485760,        maxChars: 500,        models: [          { provider: "openai", model: "gpt-5.5" },          { provider: "anthropic", model: "claude-opus-4-6" },          {            type: "cli",            command: "gemini",            args: [              "-m",              "gemini-3-flash",              "--allowed-tools",              "read_file",              "Read the media at {{MediaPath}} and describe it in <= {{MaxChars}} characters.",            ],          },        ],      },    },  },}
[/code]

### Singola voce multimodale

json5Copy code
[code]
    {  tools: {    media: {      image: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      audio: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },      video: {        models: [          {            provider: "google",            model: "gemini-3.1-pro-preview",            capabilities: ["image", "video", "audio"],          },        ],      },    },  },}
[/code]

## Output di stato

Quando viene eseguita la comprensione dei media, `/status` include una breve riga di riepilogo:

CodeCopy code
[code]
    📎 Media: image ok (openai/gpt-5.4) · audio skipped (maxBytes)
[/code]

Mostra gli esiti per capacità e il provider/modello scelto, quando applicabile.

## Note

  * La comprensione è **best-effort**. Gli errori non bloccano le risposte.
  * Gli allegati vengono comunque passati ai modelli anche quando la comprensione è disabilitata.
  * Usa `scope` per limitare dove viene eseguita la comprensione (ad esempio solo nei DM).


## Correlati

  * [Configurazione](</it/gateway/configuration>)
  * [Supporto per immagini e media](</it/nodes/images>)


Was this useful?YesNo