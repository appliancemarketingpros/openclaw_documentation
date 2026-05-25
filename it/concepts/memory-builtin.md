---
title: Motore di memoria integrato
source_url: https://docs.openclaw.ai/it/concepts/memory-builtin
scraped_at: 2026-05-25
---

Il motore integrato è il backend di memoria predefinito. Archivia il tuo indice di memoria in un database SQLite per agente e non richiede dipendenze aggiuntive per iniziare.

## Cosa offre

  * **Ricerca per parole chiave** tramite indicizzazione full-text FTS5 (punteggio BM25).
  * **Ricerca vettoriale** tramite embedding di qualsiasi provider supportato.
  * **Ricerca ibrida** che combina entrambe per ottenere i risultati migliori.
  * **Supporto CJK** tramite tokenizzazione a trigrammi per cinese, giapponese e coreano.
  * **Accelerazione sqlite-vec** per query vettoriali nel database (opzionale).


## Per iniziare

Se hai una chiave API per OpenAI, Gemini, Voyage, Mistral o DeepInfra, il motore integrato la rileva automaticamente e abilita la ricerca vettoriale. Non serve configurazione.

Per impostare esplicitamente un provider:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "openai",      },    },  },}
[/code]

Senza un provider di embedding, è disponibile solo la ricerca per parole chiave.

Per forzare il provider di embedding locale integrato, installa il pacchetto runtime opzionale `node-llama-cpp` accanto a OpenClaw, quindi punta `local.modelPath` a un file GGUF:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "local",        fallback: "none",        local: {          modelPath: "~/.node-llama-cpp/models/embeddinggemma-300m-qat-Q8_0.gguf",        },      },    },  },}
[/code]

## Provider di embedding supportati

Provider | ID | Rilevato automaticamente | Note  
---|---|---|---  
OpenAI | `openai` | Sì | Predefinito: `text-embedding-3-small`  
Gemini | `gemini` | Sì | Supporta multimodale (immagine + audio)  
Voyage | `voyage` | Sì |   
Mistral | `mistral` | Sì |   
DeepInfra | `deepinfra` | Sì | Predefinito: `BAAI/bge-m3`  
Ollama | `ollama` | No | Locale, da impostare esplicitamente  
Locale | `local` | Sì (per primo) | Runtime opzionale `node-llama-cpp`  
  
Il rilevamento automatico sceglie il primo provider la cui chiave API può essere risolta, nell'ordine mostrato. Imposta `memorySearch.provider` per sovrascrivere.

## Come funziona l'indicizzazione

OpenClaw indicizza `MEMORY.md` e `memory/*.md` in blocchi (~400 token con sovrapposizione di 80 token) e li archivia in un database SQLite per agente.

  * **Posizione dell'indice:** `~/.openclaw/memory/<agentId>.sqlite`
  * **Manutenzione dell'archiviazione:** i file sidecar WAL di SQLite sono limitati con checkpoint periodici e all'arresto.
  * **Monitoraggio dei file:** le modifiche ai file di memoria attivano una reindicizzazione con debounce (1,5 s).
  * **Reindicizzazione automatica:** quando cambiano il provider di embedding, il modello o la configurazione di suddivisione in blocchi, l'intero indice viene ricostruito automaticamente.
  * **Reindicizzazione su richiesta:** `openclaw memory index --force`


## Quando usarlo

Il motore integrato è la scelta giusta per la maggior parte degli utenti:

  * Funziona subito senza dipendenze aggiuntive.
  * Gestisce bene la ricerca per parole chiave e vettoriale.
  * Supporta tutti i provider di embedding.
  * La ricerca ibrida combina il meglio di entrambi gli approcci di recupero.


Valuta il passaggio a [QMD](</it/concepts/memory-qmd>) se hai bisogno di reranking, espansione delle query o vuoi indicizzare directory esterne al workspace.

Valuta [Honcho](</it/concepts/memory-honcho>) se vuoi memoria tra sessioni con modellazione automatica dell'utente.

## Risoluzione dei problemi

**Ricerca in memoria disabilitata?** Controlla `openclaw memory status`. Se non viene rilevato alcun provider, impostane uno esplicitamente o aggiungi una chiave API.

**Provider locale non rilevato?** Conferma che il percorso locale esista ed esegui:

bashCopy code
[code]
    openclaw memory status --deep --agent mainopenclaw memory index --force --agent main
[/code]

Sia i comandi CLI standalone sia il Gateway usano lo stesso id provider `local`. Se il provider è impostato su `auto`, gli embedding locali vengono considerati per primi solo quando `memorySearch.local.modelPath` punta a un file locale esistente.

**Risultati obsoleti?** Esegui `openclaw memory index --force` per ricostruire. Il watcher può non rilevare modifiche in rari casi limite.

**sqlite-vec non si carica?** OpenClaw ripiega automaticamente sulla similarità del coseno in-process. `openclaw memory status --deep` segnala l'archivio vettoriale locale separatamente dal provider di embedding, quindi `Vector store: unavailable` indica il caricamento di sqlite-vec mentre `Embeddings: unavailable` indica provider/autenticazione o prontezza del modello. Controlla i log per l'errore di caricamento specifico.

## Configurazione

Per la configurazione del provider di embedding, la regolazione della ricerca ibrida (pesi, MMR, decadimento temporale), l'indicizzazione batch, la memoria multimodale, sqlite-vec, percorsi aggiuntivi e tutti gli altri parametri di configurazione, consulta il [riferimento di configurazione della memoria](</it/reference/memory-config>).

## Correlati

  * [Panoramica della memoria](</it/concepts/memory>)
  * [Ricerca in memoria](</it/concepts/memory-search>)
  * [Active memory](</it/concepts/active-memory>)


Was this useful?YesNo