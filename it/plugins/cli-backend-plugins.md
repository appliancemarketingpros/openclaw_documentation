---
title: Creazione di Plugin backend per CLI
source_url: https://docs.openclaw.ai/it/plugins/cli-backend-plugins
scraped_at: 2026-05-25
---

I plugin backend CLI consentono a OpenClaw di chiamare una CLI AI locale come backend di inferenza testuale. Il backend appare come prefisso provider nei riferimenti modello:

textCopy code
[code]
    acme-cli/acme-large
[/code]

Usa un backend CLI quando l'integrazione upstream è già esposta come comando locale, quando la CLI gestisce lo stato di login locale, oppure quando la CLI è un fallback utile se i provider API non sono disponibili.

## Cosa gestisce il plugin

Un plugin backend CLI ha tre contratti:

Contratto | File | Scopo  
---|---|---  
Entry del package | `package.json` | Punta OpenClaw al modulo runtime del plugin  
Proprietà manifest | `openclaw.plugin.json` | Dichiara l'id backend prima del caricamento del runtime  
Registrazione runtime | `index.ts` | Chiama `api.registerCliBackend(...)` con i default comando  
  
Il manifest è metadato di discovery. Non esegue la CLI e non registra comportamenti runtime. Il comportamento runtime inizia quando l'entry del plugin chiama `api.registerCliBackend(...)`.

## Plugin backend minimale

* ### Crea i metadati del package

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-acme-cli",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  },  "dependencies": {    "openclaw": "^2026.3.24"  },  "devDependencies": {    "typescript": "^5.9.0"  }}
[/code]

I package pubblicati devono includere file runtime JavaScript compilati. Se la tua entry sorgente è `./src/index.ts`, aggiungi `openclaw.runtimeExtensions` che punta al peer JavaScript compilato. Vedi [Entry point](</it/plugins/sdk-entrypoints>).

* ### Dichiara la proprietà del backend

openclaw.plugin.jsonCopy code
[code]
    {  "id": "acme-cli",  "name": "Acme CLI",  "description": "Run Acme's local AI CLI through OpenClaw",  "cliBackends": ["acme-cli"],  "setup": {    "cliBackends": ["acme-cli"],    "requiresRuntime": false  },  "activation": {    "onStartup": false  },  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

`cliBackends` è l'elenco di proprietà runtime. Consente a OpenClaw di caricare automaticamente il plugin quando la configurazione o la selezione del modello menziona `acme-cli/...`.

`setup.cliBackends` è la superficie di setup descriptor-first. Aggiungila quando discovery dei modelli, onboarding o stato devono riconoscere il backend senza caricare il runtime del plugin. Usa `requiresRuntime: false` solo quando quei descrittori statici sono sufficienti per il setup.

* ### Registra il backend

index.tsCopy code
[code]
    import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import {  CLI_FRESH_WATCHDOG_DEFAULTS,  CLI_RESUME_WATCHDOG_DEFAULTS,  type CliBackendPlugin,} from "openclaw/plugin-sdk/cli-backend"; function buildAcmeCliBackend(): CliBackendPlugin {  return {    id: "acme-cli",    liveTest: {      defaultModelRef: "acme-cli/acme-large",      defaultImageProbe: false,      defaultMcpProbe: false,      docker: {        npmPackage: "@acme/acme-cli",        binaryName: "acme",      },    },    config: {      command: "acme",      args: ["chat", "--json"],      output: "json",      input: "stdin",      modelArg: "--model",      sessionArg: "--session",      sessionMode: "existing",      sessionIdFields: ["session_id", "conversation_id"],      systemPromptFileArg: "--system-file",      systemPromptWhen: "first",      imageArg: "--image",      imageMode: "repeat",      reliability: {        watchdog: {          fresh: { ...CLI_FRESH_WATCHDOG_DEFAULTS },          resume: { ...CLI_RESUME_WATCHDOG_DEFAULTS },        },      },      serialize: true,    },  };} export default definePluginEntry({  id: "acme-cli",  name: "Acme CLI",  description: "Run Acme's local AI CLI through OpenClaw",  register(api) {    api.registerCliBackend(buildAcmeCliBackend());  },});
[/code]

L'id backend deve corrispondere alla voce `cliBackends` del manifest. La `config` registrata è solo il default; la configurazione utente sotto `agents.defaults.cliBackends.acme-cli` viene unita sopra di essa a runtime.

## Forma della configurazione

`CliBackendConfig` descrive come OpenClaw deve avviare e analizzare la CLI:

Campo | Uso  
---|---  
`command` | Nome binario o percorso comando assoluto  
`args` | Argv base per esecuzioni nuove  
`resumeArgs` | Argv alternativo per sessioni riprese; supporta `{sessionId}`  
`output` / `resumeOutput` | Parser: `json`, `jsonl` o `text`  
`input` | Trasporto prompt: `arg` o `stdin`  
`modelArg` | Flag usato prima dell'id modello  
`modelAliases` | Mappa gli id modello OpenClaw agli id nativi della CLI  
`sessionArg` / `sessionArgs` | Come passare un id sessione  
`sessionMode` | `always`, `existing` o `none`  
`sessionIdFields` | Campi JSON che OpenClaw legge dall'output della CLI  
`systemPromptArg` / `systemPromptFileArg` | Trasporto del prompt di sistema  
`systemPromptWhen` | `first`, `always` o `never`  
`imageArg` / `imageMode` | Supporto percorso immagine  
`serialize` | Mantiene ordinate le esecuzioni dello stesso backend  
`reliability.watchdog` | Regolazione timeout senza output  
  
Preferisci la configurazione statica più piccola che corrisponde alla CLI. Aggiungi callback del plugin solo per comportamenti che appartengono davvero al backend.

## Hook backend avanzati

`CliBackendPlugin` può anche definire:

Hook | Uso  
---|---  
`normalizeConfig(config, context)` | Riscrive la configurazione utente legacy dopo il merge  
`resolveExecutionArgs(ctx)` | Aggiunge flag con ambito richiesta come il thinking effort  
`prepareExecution(ctx)` | Crea bridge temporanei di auth o configurazione prima dell'avvio  
`transformSystemPrompt(ctx)` | Applica una trasformazione finale del prompt di sistema specifica della CLI  
`textTransforms` | Sostituzioni bidirezionali prompt/output  
`defaultAuthProfileId` | Preferisce un profilo auth OpenClaw specifico  
`authEpochMode` | Decide come le modifiche auth invalidano le sessioni CLI archiviate  
`nativeToolMode` | Dichiara se la CLI ha strumenti nativi sempre attivi  
`bundleMcp` / `bundleMcpMode` | Abilita il bridge tool MCP loopback di OpenClaw  
  
Mantieni questi hook di proprietà del provider. Non aggiungere branch specifici della CLI al core quando un hook backend può esprimere il comportamento.

## Bridge tool MCP

I backend CLI non ricevono i tool OpenClaw per impostazione predefinita. Se la CLI può consumare una configurazione MCP, abilitala esplicitamente:

typescriptCopy code
[code]
    return {  id: "acme-cli",  bundleMcp: true,  bundleMcpMode: "codex-config-overrides",  config: {    command: "acme",    args: ["chat", "--json"],    output: "json",  },};
[/code]

Le modalità bridge supportate sono:

Modalità | Uso  
---|---  
`claude-config-file` | CLI che accettano un file di configurazione MCP  
`codex-config-overrides` | CLI che accettano override di configurazione su argv  
`gemini-system-settings` | CLI che leggono impostazioni MCP dalla propria directory impostazioni di sistema  
  
Abilita il bridge solo quando la CLI può effettivamente consumarlo. Se la CLI ha un proprio layer tool integrato che non può essere disabilitato, imposta `nativeToolMode: "always-on"` così OpenClaw può fallire chiuso quando un chiamante richiede nessun tool nativo.

## Configurazione utente

Gli utenti possono sovrascrivere qualsiasi default del backend:

json5Copy code
[code]
    {  agents: {    defaults: {      cliBackends: {        "acme-cli": {          command: "/opt/acme/bin/acme",          args: ["chat", "--json", "--profile", "work"],          modelAliases: {            large: "acme-large-2026",          },        },      },      model: {        primary: "openai/gpt-5.5",        fallbacks: ["acme-cli/large"],      },    },  },}
[/code]

Documenta l'override minimo di cui gli utenti avranno probabilmente bisogno. Di solito è solo `command` quando il binario è fuori da `PATH`.

## Verifica

Per i plugin bundled, aggiungi un test mirato intorno al builder e alla registrazione setup, quindi esegui la lane di test mirata del plugin:

bashCopy code
[code]
    pnpm test extensions/acme-cli
[/code]

Per plugin locali o installati, verifica discovery e un'esecuzione reale del modello:

bashCopy code
[code]
    openclaw plugins inspect acme-cli --runtime --jsonopenclaw agent --message "reply exactly: backend ok" --model acme-cli/acme-large
[/code]

Se il backend supporta immagini o MCP, aggiungi uno smoke live che provi quei percorsi con la CLI reale. Non affidarti all'ispezione statica per prompt, immagine, MCP o comportamento di ripresa sessione.

## Checklist

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `package.json` ha `openclaw.extensions` e entry runtime compilate per i package pubblicati OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `openclaw.plugin.json` dichiara `cliBackends` e `activation.onStartup` intenzionale OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `setup.cliBackends` è presente quando setup/discovery dei modelli deve vedere il backend a freddo OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `api.registerCliBackend(...)` usa lo stesso id backend del manifest OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Gli override utente sotto `agents.defaults.cliBackends.<id>` continuano a prevalere OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo