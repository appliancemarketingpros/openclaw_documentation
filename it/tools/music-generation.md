---
title: Generazione musicale
source_url: https://docs.openclaw.ai/it/tools/music-generation
scraped_at: 2026-05-25
---

Lo strumento `music_generate` consente all'agente di creare musica o audio tramite la capacità condivisa di generazione musicale con provider configurati: Google, MiniMax e, al momento, ComfyUI configurato tramite workflow.

Per le esecuzioni dell'agente basate su sessione, OpenClaw avvia la generazione musicale come attività in background, la traccia nel registro delle attività, quindi risveglia nuovamente l'agente quando la traccia è pronta, così l'agente può informare l'utente e allegare l'audio finito. Nelle chat di gruppo/canale che usano la consegna visibile solo tramite strumento di messaggistica, l'agente inoltra il risultato tramite lo strumento di messaggistica. Se l'agente di completamento scrive solo una risposta finale privata, OpenClaw ripiega su un invio diretto al canale con i media generati. Il risveglio di completamento avvisa esplicitamente l'agente che le normali risposte finali sono private in quelle route.

## Avvio rapido

### Basato su provider condiviso

* ### Configura l'autenticazione

Imposta una chiave API per almeno un provider, ad esempio `GEMINI_API_KEY` o `MINIMAX_API_KEY`.

* ### Scegli un modello predefinito (facoltativo)

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

* ### Chiedi all'agente

_"Genera una traccia synthpop energica su un viaggio notturno in auto attraverso una città al neon."_

L'agente chiama `music_generate` automaticamente. Non è necessario inserire lo strumento in una lista di consentiti.

Per i contesti sincroni diretti senza un'esecuzione dell'agente basata su sessione, lo strumento integrato ripiega comunque sulla generazione inline e restituisce il percorso finale dei media nel risultato dello strumento.

### Workflow ComfyUI

* ### Configura il workflow

Configura `plugins.entries.comfy.config.music` con un workflow JSON e nodi di prompt/output.

* ### Autenticazione cloud (facoltativa)

Per Comfy Cloud, imposta `COMFY_API_KEY` o `COMFY_CLOUD_API_KEY`.

* ### Chiama lo strumento

textCopy code
[code]
    /tool music_generate prompt="Warm ambient synth loop with soft tape texture"
[/code]

Prompt di esempio:

textCopy code
[code]
    Generate a cinematic piano track with soft strings and no vocals.
[/code]

textCopy code
[code]
    Generate an energetic chiptune loop about launching a rocket at sunrise.
[/code]

## Provider supportati

Provider | Modello predefinito | Input di riferimento | Controlli supportati | Autenticazione  
---|---|---|---|---  
ComfyUI | `workflow` | Fino a 1 immagine | Musica o audio definiti dal workflow | `COMFY_API_KEY`, `COMFY_CLOUD_API_KEY`  
Google | `lyria-3-clip-preview` | Fino a 10 immagini | `lyrics`, `instrumental`, `format` | `GEMINI_API_KEY`, `GOOGLE_API_KEY`  
MiniMax | `music-2.6` | Nessuno | `lyrics`, `instrumental`, `durationSeconds`, `format=mp3` | `MINIMAX_API_KEY` o OAuth MiniMax  
  
### Matrice delle capacità

Il contratto di modalità esplicito usato da `music_generate`, dai test del contratto e dallo sweep live condiviso:

Provider | `generate` | `edit` | Limite di modifica | Lane live condivise  
---|---|---|---|---  
ComfyUI | ✓ | ✓ | 1 immagine | Non nello sweep condiviso; coperto da `extensions/comfy/comfy.live.test.ts`  
Google | ✓ | ✓ | 10 immagini | `generate`, `edit`  
MiniMax | ✓ | — | Nessuno | `generate`  
  
Usa `action: "list"` per ispezionare i provider e i modelli condivisi disponibili a runtime:

textCopy code
[code]
    /tool music_generate action=list
[/code]

Usa `action: "status"` per ispezionare l'attività musicale attiva basata su sessione:

textCopy code
[code]
    /tool music_generate action=status
[/code]

Esempio di generazione diretta:

textCopy code
[code]
    /tool music_generate prompt="Dreamy lo-fi hip hop with vinyl texture and gentle rain" instrumental=true
[/code]

## Parametri dello strumento

Prompt di generazione musicale. Obbligatorio per `action: "generate"`.

`"status"` restituisce l'attività di sessione corrente; `"list"` ispeziona i provider.

Override provider/modello (ad esempio `google/lyria-3-pro-preview`, `comfy/workflow`).

Testo facoltativo quando il provider supporta l'input esplicito dei testi.

Richiede output solo strumentale quando il provider lo supporta.

Percorso o URL di una singola immagine di riferimento.

Più immagini di riferimento (fino a 10 sui provider che le supportano).

Durata target in secondi quando il provider supporta i suggerimenti di durata.

Suggerimento del formato di output quando il provider lo supporta.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg Timeout facoltativo della richiesta al provider in millisecondi. Quando omesso, OpenClaw usa `agents.defaults.musicGenerationModel.timeoutMs` se configurato. I valori inferiori a 10000ms vengono aumentati a 10000ms e segnalati nel risultato dello strumento. OPENCLAW_DOCS_MARKER:paramClose:

## Comportamento asincrono

La generazione musicale basata su sessione viene eseguita come attività in background:

  * **Attività in background:** `music_generate` crea un'attività in background, restituisce subito una risposta di avvio/attività e pubblica la traccia finita più tardi in un messaggio di follow-up dell'agente.
  * **Prevenzione dei duplicati:** mentre un'attività è `queued` o `running`, le chiamate successive a `music_generate` nella stessa sessione restituiscono lo stato dell'attività invece di avviare un'altra generazione. Usa `action: "status"` per controllare esplicitamente.
  * **Ricerca dello stato:** `openclaw tasks list` o `openclaw tasks show <taskId>` ispeziona gli stati in coda, in esecuzione e terminali.
  * **Risveglio di completamento:** OpenClaw inietta un evento interno di completamento nella stessa sessione, così il modello può scrivere autonomamente il follow-up visibile all'utente.
  * **Suggerimento nel prompt:** i turni successivi dell'utente/manuali nella stessa sessione ricevono un piccolo suggerimento di runtime quando un'attività musicale è già in corso, così il modello non richiama alla cieca `music_generate`.
  * **Fallback senza sessione:** i contesti diretti/locali senza una reale sessione dell'agente vengono eseguiti inline e restituiscono il risultato audio finale nello stesso turno.


### Ciclo di vita dell'attività

Stato | Significato  
---|---  
`queued` | Attività creata, in attesa che il provider la accetti.  
`running` | Il provider sta elaborando (in genere da 30 secondi a 3 minuti a seconda di provider e durata).  
`succeeded` | Traccia pronta; l'agente si risveglia e la pubblica nella conversazione.  
`failed` | Errore del provider o timeout; l'agente si risveglia con i dettagli dell'errore.  
  
Controlla lo stato dalla CLI:

bashCopy code
[code]
    openclaw tasks listopenclaw tasks show <taskId>openclaw tasks cancel <taskId>
[/code]

## Configurazione

### Selezione del modello

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",        fallbacks: ["minimax/music-2.6"],      },    },  },}
[/code]

### Ordine di selezione dei provider

OpenClaw prova i provider in questo ordine:

  1. Parametro `model` della chiamata allo strumento (se l'agente ne specifica uno).
  2. `musicGenerationModel.primary` dalla configurazione.
  3. `musicGenerationModel.fallbacks` in ordine.
  4. Rilevamento automatico usando solo valori predefiniti dei provider basati su autenticazione: 
     * prima il provider predefinito corrente;
     * poi i restanti provider di generazione musicale registrati in ordine di id provider.


Se un provider fallisce, il candidato successivo viene provato automaticamente. Se tutti falliscono, l'errore include i dettagli di ogni tentativo.

Imposta `agents.defaults.mediaGenerationAutoProviderFallback: false` per usare solo voci esplicite `model`, `primary` e `fallbacks`.

## Note sui provider

ComfyUI

Basato su workflow e dipende dal grafo configurato più la mappatura dei nodi per i campi prompt/output. Il plugin `comfy` incluso si collega allo strumento condiviso `music_generate` tramite il registro dei provider di generazione musicale.

Google (Lyria 3)

Usa la generazione batch Lyria 3. Il flusso incluso corrente supporta prompt, testo facoltativo dei brani e immagini di riferimento facoltative.

MiniMax

Usa l'endpoint batch `music_generation`. Supporta prompt, testi facoltativi, modalità strumentale, controllo della durata e output mp3 tramite autenticazione con chiave API `minimax` oppure OAuth `minimax-portal`.

## Scegliere il percorso giusto

  * **Basato su provider condiviso** quando vuoi selezione del modello, failover dei provider e il flusso integrato asincrono di attività/stato.
  * **Percorso Plugin (ComfyUI)** quando ti serve un grafo di workflow personalizzato o un provider che non fa parte della capacità musicale condivisa inclusa.


Se stai eseguendo il debug di un comportamento specifico di ComfyUI, consulta [ComfyUI](</it/providers/comfy>). Se stai eseguendo il debug di un comportamento del provider condiviso, inizia con [Google (Gemini)](</it/providers/google>) o [MiniMax](</it/providers/minimax>).

## Modalità delle capacità del provider

Il contratto condiviso di generazione musicale supporta dichiarazioni di modalità esplicite:

  * `generate` per la generazione solo da prompt.
  * `edit` quando la richiesta include una o più immagini di riferimento.


Le nuove implementazioni dei provider dovrebbero preferire blocchi di modalità espliciti:

typescriptCopy code
[code]
    capabilities: {  generate: {    maxTracks: 1,    supportsLyrics: true,    supportsFormat: true,  },  edit: {    enabled: true,    maxTracks: 1,    maxInputImages: 1,    supportsFormat: true,  },}
[/code]

I campi flat legacy come `maxInputImages`, `supportsLyrics` e `supportsFormat` **non** sono sufficienti per dichiarare il supporto di modifica. I provider dovrebbero dichiarare `generate` e `edit` esplicitamente, così i test live, i test del contratto e lo strumento condiviso `music_generate` possono convalidare il supporto delle modalità in modo deterministico.

## Test live

Copertura live opt-in per i provider condivisi inclusi:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test:live -- extensions/music-generation-providers.live.test.ts
[/code]

Wrapper del repository:

bashCopy code
[code]
    pnpm test:live:media music
[/code]

Questo file live carica le variabili env del provider mancanti da `~/.profile`, preferisce per impostazione predefinita le chiavi API live/env ai profili di autenticazione archiviati e viene eseguito sia per la copertura `generate` sia per la copertura `edit` dichiarata quando il provider abilita la modalità di modifica. Copertura attuale:

  * `google`: `generate` più `edit`
  * `minimax`: solo `generate`
  * `comfy`: copertura live Comfy separata, non lo sweep condiviso dei provider


Copertura live opt-in per il percorso musicale ComfyUI incluso:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 COMFY_LIVE_TEST=1 pnpm test:live -- extensions/comfy/comfy.live.test.ts
[/code]

Il file live Comfy copre anche i workflow di immagini e video comfy quando quelle sezioni sono configurate.

## Correlati

  * [Attività in background](</it/automation/tasks>) — monitoraggio delle attività per esecuzioni `music_generate` scollegate
  * [ComfyUI](</it/providers/comfy>)
  * [Riferimento di configurazione](</it/gateway/config-agents#agent-defaults>) — configurazione `musicGenerationModel`
  * [Google (Gemini)](</it/providers/google>)
  * [MiniMax](</it/providers/minimax>)
  * [Modelli](</it/concepts/models>) — configurazione del modello e failover
  * [Panoramica degli strumenti](</it/tools>)


Was this useful?YesNo