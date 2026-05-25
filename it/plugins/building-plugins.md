---
title: Creazione di Plugin
source_url: https://docs.openclaw.ai/it/plugins/building-plugins
scraped_at: 2026-05-25
---

I plugin estendono OpenClaw con nuove funzionalità: canali, provider di modelli, voce, trascrizione in tempo reale, voce in tempo reale, comprensione dei media, generazione di immagini, generazione video, recupero web, ricerca web, strumenti agent, o qualsiasi combinazione.

Non devi aggiungere il tuo plugin al repository OpenClaw. Pubblicalo su [ClawHub](</it/clawhub>) e gli utenti lo installano con `openclaw plugins install clawhub:<package-name>`. Le specifiche di pacchetto semplici continuano a installare da npm durante la transizione di lancio.

## Prerequisiti

  * Node >= 22 e un package manager (npm o pnpm)
  * Familiarità con TypeScript (ESM)
  * Per i plugin nel repository: repository clonato e `pnpm install` completato. Lo sviluppo di plugin da checkout sorgente è solo pnpm perché OpenClaw carica i plugin inclusi dai pacchetti workspace `extensions/*`.


## Che tipo di plugin?

[**Plugin canale** Connetti OpenClaw a una piattaforma di messaggistica (Discord, IRC, ecc.) ](</it/plugins/sdk-channel-plugins>) [**Plugin provider** Aggiungi un provider di modelli (LLM, proxy o endpoint personalizzato) ](</it/plugins/sdk-provider-plugins>) [**Plugin backend CLI** Mappa una CLI AI locale nel runner di fallback testuale di OpenClaw ](</it/plugins/cli-backend-plugins>) [**Plugin strumento / hook** Registra strumenti agent, hook di eventi o servizi - continua sotto ](</it/plugins/hooks>)

Per un plugin canale che non è garantito sia installato quando onboarding/configurazione vengono eseguiti, usa `createOptionalChannelSetupSurface(...)` da `openclaw/plugin-sdk/channel-setup`. Produce una coppia adattatore di configurazione + procedura guidata che segnala il requisito di installazione e fallisce in modo chiuso sulle scritture reali della configurazione finché il plugin non è installato.

## Avvio rapido: plugin strumento

Questa guida crea un plugin minimo che registra uno strumento agent. I plugin canale e provider hanno guide dedicate collegate sopra.

* ### Crea il pacchetto e il manifest

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {  "extensions": ["./index.ts"],  "compat": {    "pluginApi": ">=2026.3.24-beta.2",    "minGatewayVersion": "2026.3.24-beta.2"  },  "build": {    "openclawVersion": "2026.3.24-beta.2",    "pluginSdkVersion": "2026.3.24-beta.2"  }}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {  "tools": ["my_tool"]},"activation": {  "onStartup": true},"configSchema": {  "type": "object",  "additionalProperties": false}}
[/code]

Ogni plugin richiede un manifest, anche senza configurazione. Gli strumenti registrati a runtime devono essere elencati in `contracts.tools` così OpenClaw può scoprire il plugin proprietario senza caricare ogni runtime dei plugin. I plugin dovrebbero anche dichiarare `activation.onStartup` intenzionalmente. Questo esempio lo imposta a `true`. Vedi [Manifest](</it/plugins/manifest>) per lo schema completo. Gli snippet canonici per la pubblicazione su ClawHub si trovano in `docs/snippets/plugin-publish/`.

* ### Scrivi il punto di ingresso

typescriptCopy code
[code]
    // index.tsimport { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { Type } from "@sinclair/typebox"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Do a thing",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: `Got: ${params.input}` }] };      },    });  },});
[/code]

`definePluginEntry` è per plugin non-canale. Per i canali, usa `defineChannelPluginEntry` \- vedi [Plugin canale](</it/plugins/sdk-channel-plugins>). Per tutte le opzioni del punto di ingresso, vedi [Punti di ingresso](</it/plugins/sdk-entrypoints>).

* ### Testa e pubblica

**Plugin esterni:** valida e pubblica con ClawHub, poi installa:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginopenclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

Le specifiche di pacchetto semplici come `@myorg/openclaw-my-plugin` installano da npm durante la transizione di lancio. Usa `clawhub:` quando vuoi la risoluzione ClawHub.

**Plugin nel repository:** inseriscili sotto l'albero workspace dei plugin inclusi - scoperti automaticamente.

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-plugin/
[/code]

## Funzionalità dei plugin

Un singolo plugin può registrare qualsiasi numero di funzionalità tramite l'oggetto `api`:

Funzionalità | Metodo di registrazione | Guida dettagliata  
---|---|---  
Inferenza testuale (LLM) | `api.registerProvider(...)` | [Plugin provider](</it/plugins/sdk-provider-plugins>)  
Backend di inferenza CLI | `api.registerCliBackend(...)` | [Plugin backend CLI](</it/plugins/cli-backend-plugins>)  
Canale / messaggistica | `api.registerChannel(...)` | [Plugin canale](</it/plugins/sdk-channel-plugins>)  
Voce (TTS/STT) | `api.registerSpeechProvider(...)` | [Plugin provider](</it/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Trascrizione in tempo reale | `api.registerRealtimeTranscriptionProvider(...)` | [Plugin provider](</it/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Voce in tempo reale | `api.registerRealtimeVoiceProvider(...)` | [Plugin provider](</it/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Comprensione dei media | `api.registerMediaUnderstandingProvider(...)` | [Plugin provider](</it/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Generazione di immagini | `api.registerImageGenerationProvider(...)` | [Plugin provider](</it/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Generazione di musica | `api.registerMusicGenerationProvider(...)` | [Plugin provider](</it/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Generazione video | `api.registerVideoGenerationProvider(...)` | [Plugin provider](</it/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Recupero web | `api.registerWebFetchProvider(...)` | [Plugin provider](</it/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Ricerca web | `api.registerWebSearchProvider(...)` | [Plugin provider](</it/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Middleware risultati strumenti | `api.registerAgentToolResultMiddleware(...)` | [Panoramica SDK](</it/plugins/sdk-overview#registration-api>)  
Strumenti agent | `api.registerTool(...)` | Sotto  
Comandi personalizzati | `api.registerCommand(...)` | [Punti di ingresso](</it/plugins/sdk-entrypoints>)  
Hook dei plugin | `api.on(...)` | [Hook dei plugin](</it/plugins/hooks>)  
Hook di eventi interni | `api.registerHook(...)` | [Punti di ingresso](</it/plugins/sdk-entrypoints>)  
Route HTTP | `api.registerHttpRoute(...)` | [Interni](</it/plugins/architecture-internals#gateway-http-routes>)  
Sottocomandi CLI | `api.registerCli(...)` | [Punti di ingresso](</it/plugins/sdk-entrypoints>)  
  
Per l'API di registrazione completa, vedi [Panoramica SDK](</it/plugins/sdk-overview#registration-api>).

I plugin inclusi possono usare `api.registerAgentToolResultMiddleware(...)` quando hanno bisogno di riscrittura asincrona dei risultati degli strumenti prima che il modello veda l'output. Dichiara i runtime di destinazione in `contracts.agentToolResultMiddleware`, ad esempio `["pi", "codex"]`. Questo è un punto di integrazione attendibile per plugin inclusi; i plugin esterni dovrebbero preferire i normali hook dei plugin OpenClaw a meno che OpenClaw non aggiunga una policy di fiducia esplicita per questa funzionalità.

Se il tuo plugin registra metodi RPC Gateway personalizzati, mantienili su un prefisso specifico del plugin. I namespace amministrativi core (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) restano riservati e si risolvono sempre in `operator.admin`, anche se un plugin richiede un ambito più ristretto.

Semantiche di guardia degli hook da tenere a mente:

  * `before_tool_call`: `{ block: true }` è terminale e arresta gli handler con priorità inferiore.
  * `before_tool_call`: `{ block: false }` è trattato come nessuna decisione.
  * `before_tool_call`: `{ requireApproval: true }` mette in pausa l'esecuzione dell'agent e chiede l'approvazione all'utente tramite l'overlay di approvazione exec, i pulsanti Telegram, le interazioni Discord o il comando `/approve` su qualsiasi canale.
  * `before_install`: `{ block: true }` è terminale e arresta gli handler con priorità inferiore.
  * `before_install`: `{ block: false }` è trattato come nessuna decisione.
  * `message_sending`: `{ cancel: true }` è terminale e arresta gli handler con priorità inferiore.
  * `message_sending`: `{ cancel: false }` è trattato come nessuna decisione.
  * `message_received`: preferisci il campo tipizzato `threadId` quando ti serve l'instradamento di thread/argomenti in ingresso. Mantieni `metadata` per extra specifici del canale.
  * `message_sending`: preferisci i campi di instradamento tipizzati `replyToId` / `threadId` rispetto alle chiavi metadata specifiche del canale.


Il comando `/approve` gestisce sia le approvazioni exec sia quelle dei plugin con fallback limitato: quando un id di approvazione exec non viene trovato, OpenClaw riprova lo stesso id tramite le approvazioni dei plugin. L'inoltro delle approvazioni dei plugin può essere configurato indipendentemente tramite `approvals.plugin` nella configurazione.

Se il plumbing personalizzato delle approvazioni deve rilevare quello stesso caso di fallback limitato, preferisci `isApprovalNotFoundError` da `openclaw/plugin-sdk/error-runtime` invece di confrontare manualmente stringhe di scadenza delle approvazioni.

Vedi [Hook dei plugin](</it/plugins/hooks>) per esempi e il riferimento degli hook.

## Registrazione degli strumenti agent

Gli strumenti sono funzioni tipizzate che l'LLM può chiamare. Possono essere obbligatori (sempre disponibili) o opzionali (opt-in dell'utente):

typescriptCopy code
[code]
    register(api) {  // Required tool - always available  api.registerTool({    name: "my_tool",    description: "Do a thing",    parameters: Type.Object({ input: Type.String() }),    async execute(_id, params) {      return { content: [{ type: "text", text: params.input }] };    },  });   // Optional tool - user must add to allowlist  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

Le factory degli strumenti ricevono un oggetto di contesto fornito dal runtime. Usa `ctx.activeModel` quando uno strumento deve registrare, visualizzare o adattarsi al modello attivo per il turno corrente. L'oggetto può includere `provider`, `modelId` e `modelRef`. Trattalo come metadati runtime informativi, non come un confine di sicurezza rispetto all'operatore locale, al codice del plugin installato o a un runtime OpenClaw modificato. Per strumenti locali sensibili, mantieni un opt-in esplicito del plugin o dell'operatore e fallisci in modo chiuso quando i metadati del modello attivo sono assenti o non idonei.

Ogni strumento registrato con `api.registerTool(...)` deve anche essere dichiarato nel manifest del plugin:

jsonCopy code
[code]
    {  "contracts": {    "tools": ["my_tool", "workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

OpenClaw acquisisce e memorizza nella cache il descrittore validato dallo strumento registrato, quindi i plugin non duplicano `description` o i dati dello schema nel manifest. Il contratto del manifest dichiara solo proprietà e individuazione; l'esecuzione richiama comunque l'implementazione live dello strumento registrato. Imposta `toolMetadata.<tool>.optional: true` per gli strumenti registrati con `api.registerTool(..., { optional: true })` in modo che OpenClaw possa evitare di caricare quel runtime del plugin finché lo strumento non viene esplicitamente inserito nella allowlist.

Gli utenti abilitano gli strumenti opzionali nella configurazione:

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] },}
[/code]

  * I nomi degli strumenti non devono entrare in conflitto con gli strumenti core (i conflitti vengono ignorati)
  * Gli strumenti con oggetti di registrazione malformati, incluso `parameters` mancante, vengono ignorati e segnalati nella diagnostica del plugin invece di interrompere le esecuzioni degli agenti
  * Usa `optional: true` per strumenti con effetti collaterali o requisiti binari aggiuntivi
  * Gli utenti possono abilitare tutti gli strumenti di un plugin aggiungendo l'id del plugin a `tools.allow`


## Registrazione dei comandi CLI

I plugin possono aggiungere gruppi di comandi root `openclaw` con `api.registerCli`. Fornisci `descriptors` per ogni radice di comando di primo livello, così OpenClaw può mostrare e instradare il comando senza caricare avidamente ogni runtime di plugin.

typescriptCopy code
[code]
    register(api) {  api.registerCli(    ({ program }) => {      const demo = program        .command("demo-plugin")        .description("Run demo plugin commands");       demo        .command("ping")        .description("Check that the plugin CLI is executable")        .action(() => {          console.log("demo-plugin:pong");        });    },    {      descriptors: [        {          name: "demo-plugin",          description: "Run demo plugin commands",          hasSubcommands: true,        },      ],    },  );}
[/code]

Dopo l'installazione, verifica la registrazione del runtime ed esegui il comando:

bashCopy code
[code]
    openclaw plugins inspect demo-plugin --runtime --jsonopenclaw demo-plugin ping
[/code]

## Convenzioni di importazione

Importa sempre da percorsi mirati `openclaw/plugin-sdk/<subpath>`:

typescriptCopy code
[code]
      // Wrong: monolithic root (deprecated, will be removed) 
[/code]

Per il riferimento completo dei sottopercorsi, vedi [Panoramica dell'SDK](</it/plugins/sdk-overview>).

All'interno del tuo plugin, usa file barrel locali (`api.ts`, `runtime-api.ts`) per le importazioni interne - non importare mai il tuo plugin tramite il suo percorso SDK.

Per i plugin provider, mantieni gli helper specifici del provider in quei barrel alla root del pacchetto a meno che la separazione non sia davvero generica. Esempi bundled attuali:

  * Anthropic: wrapper di stream Claude e helper `service_tier` / beta
  * OpenAI: builder di provider, helper per modello predefinito, provider realtime
  * OpenRouter: builder di provider più helper di onboarding/configurazione


Se un helper è utile solo all'interno di un pacchetto provider bundled, mantienilo su quella separazione alla root del pacchetto invece di promuoverlo in `openclaw/plugin-sdk/*`.

Alcune separazioni helper generate `openclaw/plugin-sdk/<bundled-id>` esistono ancora per la manutenzione dei plugin bundled quando hanno utilizzi tracciati dai proprietari. Trattale come superfici riservate, non come modello predefinito per nuovi plugin di terze parti.

## Checklist pre-invio

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **package.json** contiene metadati `openclaw` corretti OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Il manifest **openclaw.plugin.json** è presente e valido OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Il punto di ingresso usa `defineChannelPluginEntry` o `definePluginEntry` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Tutte le importazioni usano percorsi mirati `plugin-sdk/<subpath>` OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo