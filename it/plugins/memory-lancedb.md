---
title: Memoria LanceDB
source_url: https://docs.openclaw.ai/it/plugins/memory-lancedb
scraped_at: 2026-05-25
---

`memory-lancedb` è un Plugin di memoria incluso che archivia la memoria a lungo termine in LanceDB e usa embedding per il richiamo. Può richiamare automaticamente le memorie pertinenti prima del turno di un modello e acquisire fatti importanti dopo una risposta.

Usalo quando vuoi un database vettoriale locale per la memoria, hai bisogno di un endpoint di embedding compatibile con OpenAI, oppure vuoi mantenere un database di memoria al di fuori dell'archivio di memoria integrato predefinito.

## Avvio rapido

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "openai",            model: "text-embedding-3-small",          },          autoRecall: true,          autoCapture: false,        },      },    },  },}
[/code]

Riavvia il Gateway dopo aver modificato la configurazione del Plugin:

bashCopy code
[code]
    openclaw gateway restart
[/code]

Poi verifica che il Plugin sia caricato:

bashCopy code
[code]
    openclaw plugins list
[/code]

## Embedding supportati da provider

`memory-lancedb` può usare gli stessi adapter dei provider di embedding di memoria di `memory-core`. Imposta `embedding.provider` e ometti `embedding.apiKey` per usare il profilo di autenticazione configurato del provider, la variabile di ambiente o `models.providers.<provider>.apiKey`.

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "openai",            model: "text-embedding-3-small",          },          autoRecall: true,        },      },    },  },}
[/code]

Questo percorso funziona con i profili di autenticazione dei provider che espongono credenziali di embedding. Per esempio, GitHub Copilot può essere usato quando il profilo/piano Copilot supporta gli embedding:

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "github-copilot",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

OpenAI Codex / ChatGPT OAuth (`openai-codex`) non è una credenziale di embedding di OpenAI Platform. Per gli embedding OpenAI, usa un profilo di autenticazione con chiave API OpenAI, `OPENAI_API_KEY` o `models.providers.openai.apiKey`. Gli utenti solo OAuth possono usare un altro provider con supporto agli embedding, come GitHub Copilot o Ollama.

## Embedding Ollama

Per gli embedding Ollama, preferisci il provider di embedding Ollama incluso. Usa l'endpoint Ollama nativo `/api/embed` e segue le stesse regole di autenticazione/base URL del provider Ollama documentato in [Ollama](</it/providers/ollama>).

json5Copy code
[code]
    {  plugins: {    slots: {      memory: "memory-lancedb",    },    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            provider: "ollama",            baseUrl: "http://127.0.0.1:11434",            model: "mxbai-embed-large",            dimensions: 1024,          },          recallMaxChars: 400,          autoRecall: true,          autoCapture: false,        },      },    },  },}
[/code]

Imposta `dimensions` per i modelli di embedding non standard. OpenClaw conosce le dimensioni per `text-embedding-3-small` e `text-embedding-3-large`; i modelli personalizzati hanno bisogno del valore nella configurazione perché LanceDB possa creare la colonna vettoriale.

Per modelli di embedding locali piccoli, riduci `recallMaxChars` se vedi errori di lunghezza del contesto dal server locale.

## Provider compatibili con OpenAI

Alcuni provider di embedding compatibili con OpenAI rifiutano il parametro `encoding_format`, mentre altri lo ignorano e restituiscono sempre vettori `number[]`. `memory-lancedb` quindi omette `encoding_format` nelle richieste di embedding e accetta sia risposte con array di float sia risposte float32 codificate in base64.

Se hai un endpoint di embedding grezzo compatibile con OpenAI che non ha un adapter di provider incluso, ometti `embedding.provider` (o lascialo come `openai`) e imposta `embedding.apiKey` più `embedding.baseUrl`. Questo preserva il percorso client diretto compatibile con OpenAI.

Imposta `embedding.dimensions` per i provider le cui dimensioni del modello non sono integrate. Per esempio, ZhiPu `embedding-3` usa `2048` dimensioni:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          embedding: {            apiKey: "${ZHIPU_API_KEY}",            baseUrl: "https://open.bigmodel.cn/api/paas/v4",            model: "embedding-3",            dimensions: 2048,          },        },      },    },  },}
[/code]

## Limiti di richiamo e acquisizione

`memory-lancedb` ha due limiti di testo separati:

Impostazione | Predefinito | Intervallo | Si applica a  
---|---|---|---  
`recallMaxChars` | `1000` | 100-10000 | testo inviato all'API di embedding per il richiamo  
`captureMaxChars` | `500` | 100-10000 | lunghezza del messaggio dell'assistente idonea all'acquisizione  
  
`recallMaxChars` controlla il richiamo automatico, lo strumento `memory_recall`, il percorso di query `memory_forget` e `openclaw ltm search`. Il richiamo automatico preferisce il messaggio utente più recente del turno e ripiega sul prompt completo solo quando non è disponibile alcun messaggio utente. Questo mantiene i metadati del canale e i blocchi di prompt grandi fuori dalla richiesta di embedding.

`captureMaxChars` controlla se una risposta è abbastanza breve da essere considerata per l'acquisizione automatica. Non limita gli embedding delle query di richiamo.

## Comandi

Quando `memory-lancedb` è il Plugin di memoria attivo, registra lo spazio dei nomi CLI `ltm`:

bashCopy code
[code]
    openclaw ltm listopenclaw ltm search "project preferences"openclaw ltm stats
[/code]

Il Plugin estende anche `openclaw memory` con un sottocomando `query` non vettoriale che viene eseguito direttamente sulla tabella LanceDB:

bashCopy code
[code]
    openclaw memory query --cols id,text,createdAt --limit 20openclaw memory query --filter "category = 'preference'" --order-by createdAt:desc
[/code]

  * `--cols <columns>`: allowlist di colonne separate da virgole (valore predefinito: `id`, `text`, `importance`, `category`, `createdAt`).
  * `--filter <condition>`: clausola WHERE in stile SQL; limitata a 200 caratteri e ristretta ad alfanumerici, operatori di confronto, virgolette, parentesi e un piccolo insieme di punteggiatura sicura.
  * `--limit <n>`: intero positivo; valore predefinito `10`.
  * `--order-by <column>:<asc|desc>`: ordinamento in memoria applicato dopo il filtro; la colonna di ordinamento viene inclusa automaticamente nella proiezione.


Gli agenti ricevono anche strumenti di memoria LanceDB dal Plugin di memoria attivo:

  * `memory_recall` per il richiamo supportato da LanceDB
  * `memory_store` per salvare fatti importanti, preferenze, decisioni ed entità
  * `memory_forget` per rimuovere le memorie corrispondenti


## Archiviazione

Per impostazione predefinita, i dati LanceDB si trovano in `~/.openclaw/memory/lancedb`. Sovrascrivi il percorso con `dbPath`:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          dbPath: "~/.openclaw/memory/lancedb",          embedding: {            apiKey: "${OPENAI_API_KEY}",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

`storageOptions` accetta coppie chiave/valore stringa per i backend di archiviazione LanceDB e supporta l'espansione `${ENV_VAR}`:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        enabled: true,        config: {          dbPath: "s3://memory-bucket/openclaw",          storageOptions: {            access_key: "${AWS_ACCESS_KEY_ID}",            secret_key: "${AWS_SECRET_ACCESS_KEY}",            endpoint: "${AWS_ENDPOINT_URL}",          },          embedding: {            apiKey: "${OPENAI_API_KEY}",            model: "text-embedding-3-small",          },        },      },    },  },}
[/code]

## Dipendenze di runtime

`memory-lancedb` dipende dal pacchetto nativo `@lancedb/lancedb`. OpenClaw pacchettizzato tratta quel pacchetto come parte del pacchetto del Plugin. L'avvio del Gateway non ripara le dipendenze dei Plugin; se la dipendenza manca, reinstalla o aggiorna il pacchetto del Plugin e riavvia il Gateway.

Se un'installazione meno recente registra un errore di `dist/package.json` mancante o `@lancedb/lancedb` mancante durante il caricamento del Plugin, aggiorna OpenClaw e riavvia il Gateway.

Se il Plugin registra che LanceDB non è disponibile su `darwin-x64`, usa il backend di memoria predefinito su quella macchina, sposta il Gateway su una piattaforma supportata oppure disabilita `memory-lancedb`.

## Risoluzione dei problemi

### La lunghezza dell'input supera la lunghezza del contesto

Questo di solito significa che il modello di embedding ha rifiutato la query di richiamo:

textCopy code
[code]
    memory-lancedb: recall failed: Error: 400 the input length exceeds the context length
[/code]

Imposta un valore inferiore per `recallMaxChars`, poi riavvia il Gateway:

json5Copy code
[code]
    {  plugins: {    entries: {      "memory-lancedb": {        config: {          recallMaxChars: 400,        },      },    },  },}
[/code]

Per Ollama, verifica anche che il server di embedding sia raggiungibile dall'host del Gateway:

bashCopy code
[code]
    curl http://127.0.0.1:11434/v1/embeddings \  -H "Content-Type: application/json" \  -d '{"model":"mxbai-embed-large","input":"hello"}'
[/code]

### Modello di embedding non supportato

Senza `dimensions`, sono note solo le dimensioni di embedding OpenAI integrate. Per modelli di embedding locali o personalizzati, imposta `embedding.dimensions` sulla dimensione del vettore riportata da quel modello.

### Il Plugin si carica ma non compare alcuna memoria

Controlla che `plugins.slots.memory` punti a `memory-lancedb`, poi esegui:

bashCopy code
[code]
    openclaw ltm statsopenclaw ltm search "recent preference"
[/code]

Se `autoCapture` è disabilitato, il Plugin richiamerà le memorie esistenti ma non ne archivierà automaticamente di nuove. Usa lo strumento `memory_store` oppure abilita `autoCapture` se vuoi l'acquisizione automatica.

## Correlati

  * [Panoramica della memoria](</it/concepts/memory>)
  * [Active Memory](</it/concepts/active-memory>)
  * [Ricerca nella memoria](</it/concepts/memory-search>)
  * [Wiki della memoria](</it/plugins/memory-wiki>)
  * [Ollama](</it/providers/ollama>)


Was this useful?YesNo