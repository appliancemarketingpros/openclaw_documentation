---
title: Installazione e configurazione del Plugin
source_url: https://docs.openclaw.ai/it/plugins/sdk-setup
scraped_at: 2026-05-25
---

Riferimento per il packaging dei Plugin (metadati di `package.json`), manifest (`openclaw.plugin.json`), voci di configurazione e schemi di configurazione.

## Metadati del pacchetto

Il tuo `package.json` richiede un campo `openclaw` che indichi al sistema di Plugin cosa fornisce il tuo Plugin:

### Channel plugin

jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-channel",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "channel": {      "id": "my-channel",      "label": "My Channel",      "blurb": "Short description of the channel."    }  }}
[/code]

### Provider plugin / ClawHub baseline

openclaw-clawhub-package.jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  }}
[/code]

### Campi `openclaw`

File dei punti di ingresso (relativi alla radice del pacchetto).

Punto di ingresso leggero solo per la configurazione (facoltativo).

Metadati del catalogo canali per configurazione, selettore, avvio rapido e superfici di stato.

ID provider registrati da questo Plugin.

Suggerimenti di installazione: `npmSpec`, `localPath`, `defaultChoice`, `minHostVersion`, `expectedIntegrity`, `allowInvalidConfigRecovery`.

Flag del comportamento di avvio.

### `openclaw.channel`

`openclaw.channel` è costituito da metadati di pacchetto leggeri per la scoperta dei canali e le superfici di configurazione prima del caricamento del runtime.

Campo | Tipo | Significato  
---|---|---  
`id` | `string` | ID canale canonico.  
`label` | `string` | Etichetta principale del canale.  
`selectionLabel` | `string` | Etichetta del selettore/configurazione quando deve differire da `label`.  
`detailLabel` | `string` | Etichetta di dettaglio secondaria per cataloghi canali e superfici di stato più ricchi.  
`docsPath` | `string` | Percorso della documentazione per i link di configurazione e selezione.  
`docsLabel` | `string` | Etichetta alternativa usata per i link alla documentazione quando deve differire dall'ID canale.  
`blurb` | `string` | Breve descrizione per onboarding/catalogo.  
`order` | `number` | Ordine di ordinamento nei cataloghi canali.  
`aliases` | `string[]` | Alias di ricerca aggiuntivi per la selezione del canale.  
`preferOver` | `string[]` | ID di Plugin/canale a priorità inferiore che questo canale deve superare.  
`systemImage` | `string` | Nome facoltativo dell'icona/immagine di sistema per i cataloghi dell'interfaccia canali.  
`selectionDocsPrefix` | `string` | Testo di prefisso prima dei link alla documentazione nelle superfici di selezione.  
`selectionDocsOmitLabel` | `boolean` | Mostra direttamente il percorso della documentazione invece di un link etichettato nella copia di selezione.  
`selectionExtras` | `string[]` | Brevi stringhe aggiuntive accodate nella copia di selezione.  
`markdownCapable` | `boolean` | Contrassegna il canale come compatibile con Markdown per le decisioni di formattazione in uscita.  
`exposure` | `object` | Controlli di visibilità del canale per configurazione, elenchi configurati e superfici della documentazione.  
`quickstartAllowFrom` | `boolean` | Abilita questo canale al flusso di configurazione standard di avvio rapido `allowFrom`.  
`forceAccountBinding` | `boolean` | Richiede l'associazione esplicita dell'account anche quando esiste un solo account.  
`preferSessionLookupForAnnounceTarget` | `boolean` | Preferisce la ricerca della sessione quando risolve i target di annuncio per questo canale.  
  
Esempio:

jsonCopy code
[code]
    {  "openclaw": {    "channel": {      "id": "my-channel",      "label": "My Channel",      "selectionLabel": "My Channel (self-hosted)",      "detailLabel": "My Channel Bot",      "docsPath": "/channels/my-channel",      "docsLabel": "my-channel",      "blurb": "Webhook-based self-hosted chat integration.",      "order": 80,      "aliases": ["mc"],      "preferOver": ["my-channel-legacy"],      "selectionDocsPrefix": "Guide:",      "selectionExtras": ["Markdown"],      "markdownCapable": true,      "exposure": {        "configured": true,        "setup": true,        "docs": true      },      "quickstartAllowFrom": true    }  }}
[/code]

`exposure` supporta:

  * `configured`: include il canale nelle superfici di elenco in stile configurazione/stato
  * `setup`: include il canale nei selettori interattivi di configurazione
  * `docs`: contrassegna il canale come rivolto al pubblico nelle superfici di documentazione/navigazione


### `openclaw.install`

`openclaw.install` contiene metadati del pacchetto, non metadati del manifest.

Campo | Tipo | Significato  
---|---|---  
`clawhubSpec` | `string` | Specifica ClawHub canonica per installazione/aggiornamento e flussi di onboarding con installazione su richiesta.  
`npmSpec` | `string` | Specifica npm canonica per i flussi di fallback di installazione/aggiornamento.  
`localPath` | `string` | Percorso di sviluppo locale o installazione in bundle.  
`defaultChoice` | `"clawhub"` | `"npm"` | `"local"` | Origine di installazione preferita quando sono disponibili più origini.  
`minHostVersion` | `string` | Versione minima supportata di OpenClaw nel formato `>=x.y.z` o `>=x.y.z-prerelease`.  
`expectedIntegrity` | `string` | Stringa di integrità npm dist prevista, di solito `sha512-...`, per installazioni fissate.  
`allowInvalidConfigRecovery` | `boolean` | Consente ai flussi di reinstallazione dei Plugin in bundle di recuperare da specifici errori di configurazione obsoleti.  
  
Onboarding behavior

L'onboarding interattivo usa anche `openclaw.install` per le superfici di installazione su richiesta. Se il tuo Plugin espone scelte di autenticazione provider o metadati di configurazione/catalogo canali prima del caricamento del runtime, l'onboarding può mostrare tale scelta, richiedere l'installazione da ClawHub, npm o locale, installare o abilitare il Plugin e poi continuare il flusso selezionato. Le scelte di onboarding ClawHub usano `clawhubSpec` e sono preferite quando presenti; le scelte npm richiedono metadati di catalogo attendibili con un `npmSpec` di registro; le versioni esatte e `expectedIntegrity` sono pin npm facoltativi. Se `expectedIntegrity` è presente, i flussi di installazione/aggiornamento lo applicano per npm. Mantieni i metadati su "cosa mostrare" in `openclaw.plugin.json` e i metadati su "come installarlo" in `package.json`.

minHostVersion enforcement

Se `minHostVersion` è impostato, sia l'installazione sia il caricamento del registro dei manifest non in bundle lo applicano. Gli host più vecchi saltano i Plugin esterni; le stringhe di versione non valide vengono rifiutate. Si presume che i Plugin sorgente in bundle abbiano la stessa versione del checkout host.

Pinned npm installs

Per installazioni npm fissate, mantieni la versione esatta in `npmSpec` e aggiungi l'integrità prevista dell'artefatto:

jsonCopy code
[code]
    {  "openclaw": {    "install": {      "npmSpec": "@wecom/wecom-openclaw-plugin@1.2.3",      "expectedIntegrity": "sha512-REPLACE_WITH_NPM_DIST_INTEGRITY",      "defaultChoice": "npm"    }  }}
[/code]

allowInvalidConfigRecovery scope

`allowInvalidConfigRecovery` non è un bypass generale per configurazioni non valide. È solo per il recupero ristretto dei Plugin in bundle, così reinstallazione/configurazione possono correggere residui di aggiornamenti noti, come un percorso mancante di un Plugin in bundle o una voce `channels.<id>` obsoleta per quello stesso Plugin. Se la configurazione è non valida per motivi non correlati, l'installazione continua a fallire in modo chiuso e indica all'operatore di eseguire `openclaw doctor --fix`.

### Caricamento completo differito

I Plugin di canale possono abilitare il caricamento differito con:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "startup": {      "deferConfiguredChannelFullLoadUntilAfterListen": true    }  }}
[/code]

Quando abilitato, OpenClaw carica solo `setupEntry` durante la fase di avvio prima dell'ascolto, anche per i canali già configurati. La voce completa viene caricata dopo che il Gateway inizia ad ascoltare.

Se la tua voce di configurazione/completa registra metodi RPC del Gateway, mantienili su un prefisso specifico del Plugin. Gli spazi dei nomi di amministrazione core riservati (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) restano di proprietà del core e si risolvono sempre in `operator.admin`.

## Manifest del Plugin

Ogni Plugin nativo deve includere un `openclaw.plugin.json` nella radice del pacchetto. OpenClaw lo usa per validare la configurazione senza eseguire codice del Plugin.

jsonCopy code
[code]
    {  "id": "my-plugin",  "name": "My Plugin",  "description": "Adds My Plugin capabilities to OpenClaw",  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {      "webhookSecret": {        "type": "string",        "description": "Webhook verification secret"      }    }  }}
[/code]

Per i Plugin di canale, aggiungi `kind` e `channels`:

jsonCopy code
[code]
    {  "id": "my-channel",  "kind": "channel",  "channels": ["my-channel"],  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {}  }}
[/code]

Anche i Plugin senza configurazione devono includere uno schema. Uno schema vuoto è valido:

jsonCopy code
[code]
    {  "id": "my-plugin",  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

Consulta [Manifest del Plugin](</it/plugins/manifest>) per il riferimento completo dello schema.

## Pubblicazione su ClawHub

Per i pacchetti Plugin, usa il comando ClawHub specifico del pacchetto:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-plugin
[/code]

## Voce di setup

Il file `setup-entry.ts` è un'alternativa leggera a `index.ts` che OpenClaw carica quando ha bisogno solo delle superfici di setup (onboarding, riparazione della config, ispezione dei canali disabilitati).

typescriptCopy code
[code]
    // setup-entry.ts  export default defineSetupPluginEntry(myChannelPlugin);
[/code]

Questo evita di caricare codice runtime pesante (librerie crittografiche, registrazioni CLI, servizi in background) durante i flussi di setup.

I canali dell'area di lavoro inclusi nel bundle che mantengono esportazioni sicure per il setup in moduli sidecar possono usare `defineBundledChannelSetupEntry(...)` da `openclaw/plugin-sdk/channel-entry-contract` invece di `defineSetupPluginEntry(...)`. Quel contratto incluso nel bundle supporta anche un'esportazione opzionale `runtime`, così il cablaggio runtime in fase di setup può restare leggero ed esplicito.

Quando OpenClaw usa setupEntry invece della voce completa

  * Il canale è disabilitato ma richiede superfici di setup/onboarding.
  * Il canale è abilitato ma non configurato.
  * Il caricamento differito è abilitato (`deferConfiguredChannelFullLoadUntilAfterListen`).

Cosa deve registrare setupEntry

  * L'oggetto Plugin del canale (tramite `defineSetupPluginEntry`).
  * Qualsiasi route HTTP richiesta prima dell'ascolto del Gateway.
  * Qualsiasi metodo del Gateway necessario durante l'avvio.


Quei metodi del Gateway all'avvio devono comunque evitare namespace di amministrazione core riservati come `config.*` o `update.*`.

Cosa setupEntry NON deve includere

  * Registrazioni CLI.
  * Servizi in background.
  * Import runtime pesanti (crittografia, SDK).
  * Metodi del Gateway necessari solo dopo l'avvio.


### Import mirati degli helper di setup

Per percorsi critici solo di setup, preferisci le interfacce ristrette degli helper di setup rispetto al più ampio ombrello `plugin-sdk/setup` quando ti serve solo una parte della superficie di setup:

Percorso di import | Usalo per | Esportazioni chiave  
---|---|---  
`plugin-sdk/setup-runtime` | helper runtime in fase di setup che restano disponibili in `setupEntry` / avvio differito del canale | `createPatchedAccountSetupAdapter`, `createEnvPatchedAccountSetupAdapter`, `createSetupInputPresenceValidator`, `noteChannelLookupFailure`, `noteChannelLookupSummary`, `promptResolvedAllowFrom`, `splitSetupEntries`, `createAllowlistSetupWizardProxy`, `createDelegatedSetupWizardProxy`  
`plugin-sdk/setup-adapter-runtime` | alias di compatibilità deprecato; usa `plugin-sdk/setup-runtime` | `createEnvPatchedAccountSetupAdapter`  
`plugin-sdk/setup-tools` | helper CLI/archivio/docs per setup/installazione | `formatCliCommand`, `detectBinary`, `extractArchive`, `resolveBrewExecutable`, `formatDocsLink`, `CONFIG_DIR`  
  
Usa l'interfaccia più ampia `plugin-sdk/setup` quando vuoi l'intero set di strumenti di setup condiviso, inclusi helper per patch di config come `moveSingleAccountChannelSectionToDefaultAccount(...)`.

Gli adapter di patch del setup restano sicuri da importare nei percorsi critici. La loro ricerca della superficie del contratto di promozione per account singolo inclusa nel bundle è lazy, quindi importare `plugin-sdk/setup-runtime` non carica anticipatamente la discovery della superficie del contratto inclusa nel bundle prima che l'adapter venga effettivamente usato.

### Promozione single-account di proprietà del canale

Quando un canale passa da una config top-level per account singolo a `channels.<id>.accounts.*`, il comportamento condiviso predefinito è spostare i valori promossi con ambito account in `accounts.default`.

I canali inclusi nel bundle possono restringere o sovrascrivere quella promozione tramite la loro superficie di contratto di setup:

  * `singleAccountKeysToMove`: chiavi top-level aggiuntive che devono essere spostate nell'account promosso
  * `namedAccountPromotionKeys`: quando esistono già account con nome, solo queste chiavi vengono spostate nell'account promosso; le chiavi condivise di policy/delivery restano alla radice del canale
  * `resolveSingleAccountPromotionTarget(...)`: sceglie quale account esistente riceve i valori promossi


## Schema di config

La config del Plugin viene convalidata rispetto al JSON Schema nel tuo manifest. Gli utenti configurano i Plugin tramite:

json5Copy code
[code]
    {  plugins: {    entries: {      "my-plugin": {        config: {          webhookSecret: "abc123",        },      },    },  },}
[/code]

Il tuo Plugin riceve questa config come `api.pluginConfig` durante la registrazione.

Per la config specifica del canale, usa invece la sezione di config del canale:

json5Copy code
[code]
    {  channels: {    "my-channel": {      token: "bot-token",      allowFrom: ["user1", "user2"],    },  },}
[/code]

### Costruire schemi di config dei canali

Usa `buildChannelConfigSchema` per convertire uno schema Zod nel wrapper `ChannelConfigSchema` usato dagli artefatti di config di proprietà del Plugin:

typescriptCopy code
[code]
      const accountSchema = z.object({  token: z.string().optional(),  allowFrom: z.array(z.string()).optional(),  accounts: z.object({}).catchall(z.any()).optional(),  defaultAccount: z.string().optional(),}); const configSchema = buildChannelConfigSchema(accountSchema);
[/code]

Se hai già scritto il contratto come JSON Schema o TypeBox, usa l'helper diretto così OpenClaw può saltare la conversione da Zod a JSON Schema nei percorsi di metadati:

typescriptCopy code
[code]
      const configSchema = buildJsonChannelConfigSchema(  Type.Object({    token: Type.Optional(Type.String()),    allowFrom: Type.Optional(Type.Array(Type.String())),  }),);
[/code]

Per Plugin di terze parti, il contratto del percorso a freddo resta il manifest del Plugin: replica il JSON Schema generato in `openclaw.plugin.json#channelConfigs` così le superfici di schema di config, setup e UI possono ispezionare `channels.<id>` senza caricare codice runtime.

## Wizard di setup

I Plugin di canale possono fornire wizard di setup interattivi per `openclaw onboard`. Il wizard è un oggetto `ChannelSetupWizard` sul `ChannelPlugin`:

typescriptCopy code
[code]
     const setupWizard: ChannelSetupWizard = {  channel: "my-channel",  status: {    configuredLabel: "Connected",    unconfiguredLabel: "Not configured",    resolveConfigured: ({ cfg }) => Boolean((cfg.channels as any)?.["my-channel"]?.token),  },  credentials: [    {      inputKey: "token",      providerHint: "my-channel",      credentialLabel: "Bot token",      preferredEnvVar: "MY_CHANNEL_BOT_TOKEN",      envPrompt: "Use MY_CHANNEL_BOT_TOKEN from environment?",      keepPrompt: "Keep current token?",      inputPrompt: "Enter your bot token:",      inspect: ({ cfg, accountId }) => {        const token = (cfg.channels as any)?.["my-channel"]?.token;        return {          accountConfigured: Boolean(token),          hasConfiguredValue: Boolean(token),        };      },    },  ],};
[/code]

Il tipo `ChannelSetupWizard` supporta `credentials`, `textInputs`, `dmPolicy`, `allowFrom`, `groupAccess`, `prepare`, `finalize` e altro. Vedi i pacchetti Plugin inclusi nel bundle (per esempio il Plugin Discord `src/channel.setup.ts`) per esempi completi.

Prompt allowFrom condivisi

Per prompt di allowlist DM che richiedono solo il flusso standard `note -> prompt -> parse -> merge -> patch`, preferisci gli helper di setup condivisi da `openclaw/plugin-sdk/setup`: `createPromptParsedAllowFromForAccount(...)`, `createTopLevelChannelParsedAllowFromPrompt(...)` e `createNestedChannelParsedAllowFromPrompt(...)`.

Stato standard del setup del canale

Per blocchi di stato del setup del canale che variano solo per etichette, punteggi e righe extra opzionali, preferisci `createStandardChannelSetupStatus(...)` da `openclaw/plugin-sdk/setup` invece di ricreare manualmente lo stesso oggetto `status` in ogni Plugin.

Superficie opzionale di setup del canale

Per superfici opzionali di setup che devono apparire solo in determinati contesti, usa `createOptionalChannelSetupSurface` da `openclaw/plugin-sdk/channel-setup`:

typescriptCopy code
[code]
    import { createOptionalChannelSetupSurface } from "openclaw/plugin-sdk/channel-setup"; const setupSurface = createOptionalChannelSetupSurface({  channel: "my-channel",  label: "My Channel",  npmSpec: "@myorg/openclaw-my-channel",  docsPath: "/channels/my-channel",});// Returns { setupAdapter, setupWizard }
[/code]

`plugin-sdk/channel-setup` espone anche i builder di livello inferiore `createOptionalChannelSetupAdapter(...)` e `createOptionalChannelSetupWizard(...)` quando ti serve solo una metà di quella superficie di installazione opzionale.

L'adapter/wizard opzionale generato fallisce chiuso sulle scritture di config reali. Riusa un unico messaggio di installazione richiesta in `validateInput`, `applyAccountConfig` e `finalize`, e aggiunge un link alla documentazione quando `docsPath` è impostato.

Helper di setup basati su binari

Per UI di setup basate su binari, preferisci gli helper delegati condivisi invece di copiare lo stesso collante binario/stato in ogni canale:

  * `createDetectedBinaryStatus(...)` per blocchi di stato che variano solo per etichette, suggerimenti, punteggi e rilevamento del binario
  * `createCliPathTextInput(...)` per input di testo basati su percorso
  * `createDelegatedSetupWizardStatusResolvers(...)`, `createDelegatedPrepare(...)`, `createDelegatedFinalize(...)` e `createDelegatedResolveConfigured(...)` quando `setupEntry` deve inoltrare lazy a un wizard completo più pesante
  * `createDelegatedTextInputShouldPrompt(...)` quando `setupEntry` deve solo delegare una decisione `textInputs[*].shouldPrompt`


## Pubblicazione e installazione

**Plugin esterni:** pubblica su [ClawHub](</it/clawhub>), poi installa:

### npm

bashCopy code
[code]
    openclaw plugins install @myorg/openclaw-my-plugin
[/code]

Le specifiche di pacchetto semplici installano da npm durante il passaggio di lancio.

### Solo ClawHub

bashCopy code
[code]
    openclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

### Specifica di pacchetto npm

Usa npm quando un pacchetto non è ancora stato spostato su ClawHub, o quando ti serve un percorso diretto di installazione npm durante la migrazione:

bashCopy code
[code]
    openclaw plugins install npm:@myorg/openclaw-my-plugin
[/code]

**Plugin nel repository:** posizionali sotto l'albero dell'area di lavoro dei Plugin inclusi e vengono rilevati automaticamente durante la build.

**Gli utenti possono installare:**

bashCopy code
[code]
    openclaw plugins install <package-name>
[/code]

I metadati dei pacchetti inclusi sono espliciti, non dedotti dal JavaScript compilato all'avvio del Gateway. Le dipendenze runtime appartengono al pacchetto Plugin che le possiede; l'avvio di OpenClaw pacchettizzato non ripara ne' replica mai le dipendenze dei Plugin.

## Correlati

  * [Creazione di Plugin](</it/plugins/building-plugins>) — guida introduttiva passo passo
  * [Manifest del Plugin](</it/plugins/manifest>) — riferimento completo allo schema del manifest
  * [Punti di ingresso SDK](</it/plugins/sdk-entrypoints>) — `definePluginEntry` e `defineChannelPluginEntry`


Was this useful?YesNo