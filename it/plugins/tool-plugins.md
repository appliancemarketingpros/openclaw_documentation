---
title: Plugin di strumenti
source_url: https://docs.openclaw.ai/it/plugins/tool-plugins
scraped_at: 2026-06-29
---

CapabilitiesBuilding plugins

I Plugin di strumenti aggiungono a OpenClaw strumenti richiamabili dagli agenti senza aggiungere un canale, provider di modelli, hook, servizio o backend di configurazione. Usa `defineToolPlugin` quando il Plugin possiede un elenco fisso di strumenti e vuoi che OpenClaw generi i metadati del manifesto che mantengono quegli strumenti rilevabili senza caricare codice di runtime.

Il flusso consigliato è:

  1. Genera lo scaffold di un pacchetto con `openclaw plugins init`.
  2. Scrivi gli strumenti con `defineToolPlugin`.
  3. Compila JavaScript.
  4. Genera i metadati di `openclaw.plugin.json` e `package.json` con `openclaw plugins build`.
  5. Valida i metadati generati prima di pubblicare o installare.


Per Plugin provider, di canale, hook, servizio o con funzionalità miste, inizia invece da [Creare Plugin](</it/plugins/building-plugins>), [Plugin di canale](</it/plugins/sdk-channel-plugins>) o [Plugin provider](</it/plugins/sdk-provider-plugins>).

## Requisiti

  * Node >= 22.
  * Output del pacchetto TypeScript ESM.
  * `typebox` per schemi di configurazione e dei parametri degli strumenti.
  * `openclaw >=2026.5.17`, la prima versione di OpenClaw che esporta `openclaw/plugin-sdk/tool-plugin`.
  * Una radice del pacchetto che possa distribuire `dist/`, `openclaw.plugin.json` e `package.json`.


Il Plugin generato importa `typebox` a runtime, quindi mantieni `typebox` in `dependencies`, non solo in `devDependencies`.

## Avvio rapido

Crea un nuovo pacchetto Plugin:

bashCopy code
[code]
    openclaw plugins init stock-quotes --name "Stock Quotes"cd stock-quotesnpm installnpm run plugin:buildnpm run plugin:validatenpm test
[/code]

Lo scaffold crea:

  * `src/index.ts`: una voce `defineToolPlugin` con uno strumento `echo`.
  * `src/index.test.ts`: un piccolo test dei metadati.
  * `tsconfig.json`: output TypeScript NodeNext in `dist/`.
  * `package.json`: script, dipendenze di runtime e `openclaw.extensions: ["./dist/index.js"]`.
  * `openclaw.plugin.json`: metadati del manifesto generati per lo strumento iniziale.


Output di validazione previsto:

textCopy code
[code]
    Plugin stock-quotes is valid.
[/code]

## Scrivere uno strumento

`defineToolPlugin` accetta l'identità del Plugin, uno schema di configurazione opzionale e un elenco statico di strumenti. I tipi dei parametri e della configurazione vengono dedotti dagli schemi TypeBox.

typescriptCopy code
[code]
      export default defineToolPlugin({  id: "stock-quotes",  name: "Stock Quotes",  description: "Fetch stock quote snapshots.",  configSchema: Type.Object({    apiKey: Type.Optional(Type.String({ description: "Quote API key." })),    baseUrl: Type.Optional(Type.String({ description: "Quote API base URL." })),  }),  tools: (tool) => [    tool({      name: "stock_quote",      label: "Stock Quote",      description: "Fetch a stock quote snapshot.",      parameters: Type.Object({        symbol: Type.String({ description: "Ticker symbol, for example OPEN." }),      }),      async execute({ symbol }, config, context) {        context.signal?.throwIfAborted();        return {          symbol: symbol.toUpperCase(),          configured: Boolean(config.apiKey),          baseUrl: config.baseUrl ?? "https://api.example.com",        };      },    }),  ],});
[/code]

I nomi degli strumenti sono l'API stabile. Scegli nomi univoci, in minuscolo e abbastanza specifici da evitare collisioni con gli strumenti core o altri Plugin.

## Strumenti opzionali e factory

Imposta `optional: true` quando gli utenti devono inserire esplicitamente lo strumento in allowlist prima che venga inviato a un modello:

typescriptCopy code
[code]
    tool({  name: "workflow_run",  description: "Run an external workflow.",  parameters: Type.Object({ goal: Type.String() }),  optional: true,  execute: ({ goal }) => ({ queued: true, goal }),});
[/code]

`openclaw plugins build` scrive la voce di manifesto `toolMetadata.<tool>.optional` corrispondente, così OpenClaw può rilevare lo strumento senza caricare il codice di runtime del Plugin.

Usa `factory` quando uno strumento ha bisogno del contesto degli strumenti di runtime prima di poter essere creato. La factory mantiene statici i metadati consentendo allo strumento di escludersi da una run specifica, ispezionare lo stato della sandbox o collegare helper di runtime.

typescriptCopy code
[code]
    tool({  name: "local_workflow",  description: "Run a local workflow outside sandboxed sessions.",  parameters: Type.Object({ goal: Type.String() }),  optional: true,  factory({ api, toolContext }) {    if (toolContext.sandboxed) {      return null;    }    return createLocalWorkflowTool(api);  },});
[/code]

Le factory servono comunque per nomi di strumenti fissi. Usa direttamente `definePluginEntry` quando il Plugin calcola dinamicamente i nomi degli strumenti o combina strumenti con hook, servizi, provider, comandi o altre superfici di runtime.

## Valori restituiti

`defineToolPlugin` incapsula i valori restituiti semplici nel formato di risultato degli strumenti di OpenClaw:

  * Restituisci una stringa quando il modello deve vedere esattamente quel testo.
  * Restituisci un valore compatibile con JSON quando vuoi che il modello veda JSON formattato e che OpenClaw mantenga il valore originale in `details`.

typescriptCopy code
[code]
    tool({  name: "echo_text",  description: "Echo input text.",  parameters: Type.Object({    input: Type.String(),  }),  execute: ({ input }) => input,});
[/code]

typescriptCopy code
[code]
    tool({  name: "echo_json",  description: "Echo input as structured JSON.",  parameters: Type.Object({    input: Type.String(),  }),  execute: ({ input }) => ({ input, length: input.length }),});
[/code]

Usa uno strumento factory quando devi restituire un `AgentToolResult` personalizzato o riutilizzare un'implementazione `api.registerTool` esistente. Usa `definePluginEntry` invece di `defineToolPlugin` quando ti servono strumenti completamente dinamici o funzionalità di Plugin miste.

## Configurazione

`configSchema` è opzionale. Se lo ometti, OpenClaw usa uno schema a oggetto vuoto rigido e il manifesto generato include comunque `configSchema`.

typescriptCopy code
[code]
    export default defineToolPlugin({  id: "no-config-tools",  name: "No Config Tools",  description: "Adds tools that do not need configuration.",  tools: () => [],});
[/code]

Quando includi `configSchema`, il secondo argomento di `execute` è tipizzato dallo schema:

typescriptCopy code
[code]
    const configSchema = Type.Object({  apiKey: Type.String(),}); export default defineToolPlugin({  id: "configured-tools",  name: "Configured Tools",  description: "Adds configured tools.",  configSchema,  tools: (tool) => [    tool({      name: "configured_ping",      description: "Check whether configuration is available.",      parameters: Type.Object({}),      execute: (_params, config) => ({ hasKey: config.apiKey.length > 0 }),    }),  ],});
[/code]

OpenClaw legge la configurazione del Plugin dalla voce del Plugin nella configurazione del Gateway. Non inserire segreti hardcoded nel sorgente o negli esempi della documentazione. Usa la configurazione, le variabili di ambiente o SecretRefs in base al modello di sicurezza del Plugin.

## Metadati generati

OpenClaw rileva i Plugin installati dai metadati a freddo. Deve poter leggere il manifesto del Plugin prima di importare il codice di runtime del Plugin. `defineToolPlugin` espone quindi metadati statici e `openclaw plugins build` scrive quei metadati nel pacchetto.

Esegui il generatore dopo aver modificato ID, nome, descrizione, schema di configurazione, attivazione o nomi degli strumenti del Plugin:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js
[/code]

Per un Plugin con un solo strumento, il manifesto generato appare così:

jsonCopy code
[code]
    {  "id": "stock-quotes",  "name": "Stock Quotes",  "description": "Fetch stock quote snapshots.",  "version": "0.1.0",  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {}  },  "activation": {    "onStartup": true  },  "contracts": {    "tools": ["stock_quote"]  }}
[/code]

`contracts.tools` è il contratto di rilevamento importante. Indica a OpenClaw quale Plugin possiede ogni strumento senza caricare il runtime di ogni Plugin installato. Se il manifesto non è aggiornato, lo strumento potrebbe mancare dal rilevamento o il Plugin sbagliato potrebbe essere indicato come responsabile di un errore di registrazione.

## Metadati del pacchetto

Per il flusso semplice dei Plugin di strumenti, `openclaw plugins build` allinea `package.json` alla singola voce di runtime selezionata:

jsonCopy code
[code]
    {  "type": "module",  "files": ["dist", "openclaw.plugin.json", "README.md"],  "dependencies": {    "typebox": "^1.1.38"  },  "peerDependencies": {    "openclaw": ">=2026.5.17"  },  "openclaw": {    "extensions": ["./dist/index.js"]  }}
[/code]

Usa JavaScript compilato come `./dist/index.js` per i pacchetti installati. Le voci sorgente sono utili nello sviluppo in workspace, ma i pacchetti pubblicati non dovrebbero dipendere dal caricamento runtime di TypeScript.

## Validare in CI

Usa `plugins build --check` per far fallire la CI quando i metadati generati non sono aggiornati senza riscrivere file:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js --checkopenclaw plugins validate --entry ./dist/index.jsnpm test
[/code]

`plugins validate` controlla che:

  * `openclaw.plugin.json` esista e superi il normale loader del manifesto.
  * La voce corrente esporti metadati `defineToolPlugin`.
  * I campi del manifesto generato corrispondano ai metadati della voce.
  * `contracts.tools` corrisponda ai nomi degli strumenti dichiarati.
  * `package.json` punti `openclaw.extensions` alla voce di runtime selezionata.


## Installare e ispezionare localmente

Da un checkout OpenClaw separato o da una CLI installata, installa il percorso del pacchetto:

bashCopy code
[code]
    openclaw plugins install ./stock-quotesopenclaw plugins inspect stock-quotes --runtime
[/code]

Per uno smoke del pacchetto, crea prima il pacchetto e installa il tarball:

bashCopy code
[code]
    npm packopenclaw plugins install npm-pack:./openclaw-plugin-stock-quotes-0.1.0.tgzopenclaw plugins inspect stock-quotes --runtime --json
[/code]

Dopo l'installazione, avvia o riavvia il Gateway e chiedi all'agente di usare lo strumento. Se stai eseguendo il debug della visibilità degli strumenti, ispeziona il runtime del Plugin e il catalogo degli strumenti effettivo prima di modificare il codice.

## Pubblicare

Pubblica tramite ClawHub quando il pacchetto è pronto:

bashCopy code
[code]
    clawhub package publish your-org/stock-quotes --dry-runclawhub package publish your-org/stock-quotes
[/code]

Installa con un locator ClawHub esplicito:

bashCopy code
[code]
    openclaw plugins install clawhub:your-org/stock-quotes
[/code]

Le specifiche nude dei pacchetti npm rimangono supportate durante il passaggio di lancio, ma ClawHub è la superficie preferita di rilevamento e distribuzione per i Plugin OpenClaw.

## Risoluzione dei problemi

### `plugin entry not found: ./dist/index.js`

Il file della voce selezionata non esiste. Esegui `npm run build`, quindi riesegui `openclaw plugins build --entry ./dist/index.js` o `openclaw plugins validate --entry ./dist/index.js`.

### `plugin entry does not expose defineToolPlugin metadata`

La voce non ha esportato un valore creato da `defineToolPlugin`. Controlla che l'export predefinito del modulo sia il risultato di `defineToolPlugin(...)`, oppure passa la voce corretta con `--entry`.

### `openclaw.plugin.json generated metadata is stale`

Il manifesto non corrisponde più ai metadati della voce. Esegui:

bashCopy code
[code]
    npm run buildopenclaw plugins build --entry ./dist/index.js
[/code]

Committa sia le modifiche a `openclaw.plugin.json` sia quelle a `package.json`.

### `package.json openclaw.extensions must include ./dist/index.js`

I metadati del pacchetto puntano a una voce di runtime diversa. Esegui `openclaw plugins build --entry ./dist/index.js` così il generatore allinea i metadati del pacchetto con la voce che intendi distribuire.

### `Cannot find package 'typebox'`

Il Plugin compilato importa `typebox` a runtime. Mantieni `typebox` in `dependencies`, reinstalla le dipendenze del pacchetto, ricompila e riesegui la validazione.

### Lo strumento non appare dopo l'installazione

Controlla questi elementi in ordine:

  1. `openclaw plugins inspect <plugin-id> --runtime`
  2. `openclaw plugins validate --root <plugin-root> --entry ./dist/index.js`
  3. `openclaw.plugin.json` contiene `contracts.tools` con i nomi degli strumenti previsti.
  4. `package.json` contiene `openclaw.extensions: ["./dist/index.js"]`.
  5. Il Gateway è stato riavviato o ricaricato dopo l'installazione del Plugin.


## Vedi anche

  * [Creare Plugin](</it/plugins/building-plugins>)
  * [Punti di ingresso dei Plugin](</it/plugins/sdk-entrypoints>)
  * [Sottopercorsi dell'SDK dei Plugin](</it/plugins/sdk-subpaths>)
  * [Manifesto dei Plugin](</it/plugins/manifest>)
  * [CLI dei Plugin](</it/cli/plugins>)
  * [Pubblicazione su ClawHub](</it/clawhub/publishing>)


Was this useful?YesNo

Open issue