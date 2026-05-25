---
title: Anthropic
source_url: https://docs.openclaw.ai/it/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic sviluppa la famiglia di modelli **Claude**. OpenClaw supporta due percorsi di autenticazione:

  * **Chiave API** — accesso diretto all'API Anthropic con fatturazione basata sull'utilizzo (modelli `anthropic/*`)
  * **Claude CLI** — riusa un login Claude CLI esistente sullo stesso host


## Per iniziare

### Chiave API

**Ideale per:** accesso API standard e fatturazione basata sull'utilizzo.

* ### Ottieni la tua chiave API

Crea una chiave API nella [Console Anthropic](<https://console.anthropic.com/>).

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

Oppure passa direttamente la chiave:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### Verifica che il modello sia disponibile

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Esempio di configurazione

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**Ideale per:** riusare un login Claude CLI esistente senza una chiave API separata.

* ### Assicurati che Claude CLI sia installata e abbia effettuato l'accesso

Verifica con:

bashCopy code
[code]
    claude --version
[/code]

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw rileva e riusa le credenziali Claude CLI esistenti.

* ### Verifica che il modello sia disponibile

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Esempio di configurazione

Preferisci il riferimento canonico al modello Anthropic più un override del runtime CLI:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

I riferimenti modello legacy `claude-cli/claude-opus-4-7` continuano a funzionare per compatibilità, ma la nuova configurazione dovrebbe mantenere la selezione provider/modello come `anthropic/*` e inserire il backend di esecuzione nella policy di runtime provider/modello.

## Impostazioni predefinite del ragionamento (Claude 4.6)

I modelli Claude 4.6 usano per impostazione predefinita il ragionamento `adaptive` in OpenClaw quando non è impostato un livello di ragionamento esplicito.

Esegui l'override per messaggio con `/think:<level>` o nei parametri del modello:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## Memorizzazione nella cache dei prompt

OpenClaw supporta la funzionalità di memorizzazione nella cache dei prompt di Anthropic per l'autenticazione con chiave API.

Valore | Durata cache | Descrizione  
---|---|---  
`"short"` (predefinito) | 5 minuti | Applicata automaticamente per l'autenticazione con chiave API  
`"long"` | 1 ora | Cache estesa  
`"none"` | Nessuna cache | Disattiva la memorizzazione nella cache dei prompt  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Override della cache per agente

Usa i parametri a livello di modello come baseline, quindi esegui l'override di agenti specifici tramite `agents.list[].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Ordine di unione della configurazione:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (`id` corrispondente, override per chiave)


Questo consente a un agente di mantenere una cache a lunga durata mentre un altro agente sullo stesso modello disattiva la cache per traffico a raffiche o con basso riuso.

Note su Bedrock Claude

  * I modelli Anthropic Claude su Bedrock (`amazon-bedrock/*anthropic.claude*`) accettano il pass-through di `cacheRetention` quando configurato.
  * I modelli Bedrock non Anthropic sono forzati a `cacheRetention: "none"` a runtime.
  * Le impostazioni predefinite intelligenti per chiave API inizializzano anche `cacheRetention: "short"` per i riferimenti Claude-on-Bedrock quando non è impostato alcun valore esplicito.


## Configurazione avanzata

Modalità veloce

Il toggle condiviso `/fast` di OpenClaw supporta il traffico Anthropic diretto (chiave API e OAuth verso `api.anthropic.com`).

Comando | Mappa a  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Comprensione dei media (immagini e PDF)

Il Plugin Anthropic incluso registra la comprensione di immagini e PDF. OpenClaw risolve automaticamente le capacità multimediali dall'autenticazione Anthropic configurata: non è necessaria alcuna configurazione aggiuntiva.

Proprietà | Valore  
---|---  
Modello predefinito | `claude-opus-4-7`  
Input supportato | Immagini, documenti PDF  
  
Quando un'immagine o un PDF è allegato a una conversazione, OpenClaw lo instrada automaticamente tramite il provider di comprensione multimediale Anthropic.

Finestra di contesto 1M (beta)

La finestra di contesto 1M di Anthropic è vincolata alla beta. Abilitala per modello:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw la mappa a `anthropic-beta: context-1m-2025-08-07` nelle richieste.

`params.context1m: true` si applica anche al backend Claude CLI (`claude-cli/*`) per i modelli Opus e Sonnet idonei, espandendo la finestra di contesto runtime per quelle sessioni CLI in modo che corrisponda al comportamento API diretto.

Contesto 1M di Claude Opus 4.7

`anthropic/claude-opus-4.7` e la sua variante `claude-cli` hanno una finestra di contesto 1M per impostazione predefinita: non serve `params.context1m: true`.

## Risoluzione dei problemi

Errori 401 / token improvvisamente non valido

L'autenticazione token Anthropic scade e può essere revocata. Per nuove configurazioni, usa invece una chiave API Anthropic.

Nessuna chiave API trovata per il provider "anthropic"

L'autenticazione Anthropic è **per agente** : i nuovi agenti non ereditano le chiavi dell'agente principale. Riesegui l'onboarding per quell'agente (o configura una chiave API sull'host Gateway), quindi verifica con `openclaw models status`.

Nessuna credenziale trovata per il profilo "anthropic:default"

Esegui `openclaw models status` per vedere quale profilo di autenticazione è attivo. Riesegui l'onboarding oppure configura una chiave API per quel percorso di profilo.

Nessun profilo di autenticazione disponibile (tutti in cooldown)

Controlla `openclaw models status --json` per `auth.unusableProfiles`. I cooldown dei limiti di frequenza Anthropic possono essere specifici del modello, quindi un modello Anthropic affine potrebbe essere ancora utilizzabile. Aggiungi un altro profilo Anthropic o attendi il cooldown.

## Correlati

[**Selezione del modello** Scelta di provider, riferimenti modello e comportamento di failover. ](</it/concepts/model-providers>) [**Backend CLI** Configurazione del backend Claude CLI e dettagli runtime. ](</it/gateway/cli-backends>) [**Memorizzazione nella cache dei prompt** Come funziona la memorizzazione nella cache dei prompt tra provider. ](</it/reference/prompt-caching>) [**OAuth e autenticazione** Dettagli di autenticazione e regole di riuso delle credenziali. ](</it/gateway/authentication>)

Was this useful?YesNo