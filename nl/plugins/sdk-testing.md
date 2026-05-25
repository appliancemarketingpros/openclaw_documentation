---
title: Plugin testen
source_url: https://docs.openclaw.ai/nl/plugins/sdk-testing
scraped_at: 2026-05-25
---

Referentie voor testhulpprogramma's, patronen en lint-afdwinging voor OpenClaw-plugins.

## Testhulpprogramma's

Deze subpaden voor testhelpers zijn repo-lokale broninvoerpunten voor OpenClaw's eigen gebundelde plugintests. Het zijn geen package-exports voor plugins van derden.

**Mockimport voor Plugin-API:** `openclaw/plugin-sdk/plugin-test-api`

**Import voor agentruntimecontract:** `openclaw/plugin-sdk/agent-runtime-test-contracts`

**Import voor kanaalcontract:** `openclaw/plugin-sdk/channel-contract-testing`

**Import voor kanaaltesthelper:** `openclaw/plugin-sdk/channel-test-helpers`

**Import voor kanaaldoeltest:** `openclaw/plugin-sdk/channel-target-testing`

**Import voor Plugin-contract:** `openclaw/plugin-sdk/plugin-test-contracts`

**Import voor Plugin-runtimetest:** `openclaw/plugin-sdk/plugin-test-runtime`

**Import voor providercontract:** `openclaw/plugin-sdk/provider-test-contracts`

**Mockimport voor provider-HTTP:** `openclaw/plugin-sdk/provider-http-test-mocks`

**Import voor omgevings-/netwerktest:** `openclaw/plugin-sdk/test-env`

**Import voor generieke fixture:** `openclaw/plugin-sdk/test-fixtures`

**Mockimport voor ingebouwde Node-module:** `openclaw/plugin-sdk/test-node-mocks`

Geef voor nieuwe plugintests de voorkeur aan de gerichte subpaden hieronder. Het brede barrelbestand `openclaw/plugin-sdk/testing` is alleen bedoeld voor verouderde compatibiliteit. Repo-guardrails weigeren nieuwe echte imports uit `plugin-sdk/testing` en `plugin-sdk/test-utils`; die namen blijven alleen bestaan als verouderde compatibiliteitsoppervlakken voor compatibiliteitsrecordtests.

typescriptCopy code
[code]
       shouldAckReaction,  removeAckReactionAfterReply,} from "openclaw/plugin-sdk/channel-feedback";             bundledPluginRoot,  createCliRuntimeCapture,  typedCases,} from "openclaw/plugin-sdk/test-fixtures"; 
[/code]

### Beschikbare exports

Export | Doel  
---|---  
`createTestPluginApi` | Bouw een minimale Plugin-API-nabootsing voor directe eenheidstests voor registratie. Importeer uit `plugin-sdk/plugin-test-api`  
`AUTH_PROFILE_RUNTIME_CONTRACT` | Gedeelde contractfixture voor auth-profielen voor native agent-runtimeadapters. Importeer uit `plugin-sdk/agent-runtime-test-contracts`  
`DELIVERY_NO_REPLY_RUNTIME_CONTRACT` | Gedeelde contractfixture voor leveringsonderdrukking voor native agent-runtimeadapters. Importeer uit `plugin-sdk/agent-runtime-test-contracts`  
`OUTCOME_FALLBACK_RUNTIME_CONTRACT` | Gedeelde contractfixture voor fallback-classificatie voor native agent-runtimeadapters. Importeer uit `plugin-sdk/agent-runtime-test-contracts`  
`createParameterFreeTool` | Bouw schemafixtures voor dynamische tools voor native runtimecontracttests. Importeer uit `plugin-sdk/agent-runtime-test-contracts`  
`expectChannelInboundContextContract` | Controleer de vorm van de inkomende kanaalcontext. Importeer uit `plugin-sdk/channel-contract-testing`  
`installChannelOutboundPayloadContractSuite` | Installeer contractgevallen voor uitgaande kanaalpayloads. Importeer uit `plugin-sdk/channel-contract-testing`  
`createStartAccountContext` | Bouw kanaalaccountcontexten voor de levenscyclus. Importeer uit `plugin-sdk/channel-test-helpers`  
`installChannelActionsContractSuite` | Installeer algemene contractgevallen voor kanaalberichtacties. Importeer uit `plugin-sdk/channel-test-helpers`  
`installChannelSetupContractSuite` | Installeer algemene contractgevallen voor kanaalconfiguratie. Importeer uit `plugin-sdk/channel-test-helpers`  
`installChannelStatusContractSuite` | Installeer algemene contractgevallen voor kanaalstatus. Importeer uit `plugin-sdk/channel-test-helpers`  
`expectDirectoryIds` | Controleer kanaaldirectory-id's vanuit een directorylijstfunctie. Importeer uit `plugin-sdk/channel-test-helpers`  
`assertBundledChannelEntries` | Controleer dat gebundelde kanaalentrypoints het verwachte openbare contract blootstellen. Importeer uit `plugin-sdk/channel-test-helpers`  
`formatEnvelopeTimestamp` | Formatteer deterministische enveloptijdstempels. Importeer uit `plugin-sdk/channel-test-helpers`  
`expectPairingReplyText` | Controleer de kanaalkoppelingsantwoordtekst en extraheer de code ervan. Importeer uit `plugin-sdk/channel-test-helpers`  
`describePluginRegistrationContract` | Installeer contractcontroles voor Plugin-registratie. Importeer uit `plugin-sdk/plugin-test-contracts`  
`registerSingleProviderPlugin` | Registreer één provider-Plugin in loader-rooktests. Importeer uit `plugin-sdk/plugin-test-runtime`  
`registerProviderPlugin` | Leg alle providersoorten uit één Plugin vast. Importeer uit `plugin-sdk/plugin-test-runtime`  
`registerProviderPlugins` | Leg providerregistraties over meerdere Plugins vast. Importeer uit `plugin-sdk/plugin-test-runtime`  
`requireRegisteredProvider` | Controleer dat een providercollectie een id bevat. Importeer uit `plugin-sdk/plugin-test-runtime`  
`createRuntimeEnv` | Bouw een nagebootste CLI-/Plugin-runtimeomgeving. Importeer uit `plugin-sdk/plugin-test-runtime`  
`createPluginSetupWizardStatus` | Bouw configuratiestatushelpers voor kanaal-Plugins. Importeer uit `plugin-sdk/plugin-test-runtime`  
`describeOpenAIProviderRuntimeContract` | Installeer runtimecontractcontroles voor providerfamilies. Importeer uit `plugin-sdk/provider-test-contracts`  
`expectPassthroughReplayPolicy` | Controleer dat provider-replaybeleid provider-eigen tools en metadata doorgeeft. Importeer uit `plugin-sdk/provider-test-contracts`  
`runRealtimeSttLiveTest` | Voer een live realtime-STT-providertest uit met gedeelde audiofixtures. Importeer uit `plugin-sdk/provider-test-contracts`  
`normalizeTranscriptForMatch` | Normaliseer live transcriptuitvoer vóór fuzzy-controles. Importeer uit `plugin-sdk/provider-test-contracts`  
`expectExplicitVideoGenerationCapabilities` | Controleer dat videoproviders expliciete mogelijkheden voor generatiemodi declareren. Importeer uit `plugin-sdk/provider-test-contracts`  
`expectExplicitMusicGenerationCapabilities` | Controleer dat muziekproviders expliciete mogelijkheden voor genereren/bewerken declareren. Importeer uit `plugin-sdk/provider-test-contracts`  
`mockSuccessfulDashscopeVideoTask` | Installeer een geslaagde DashScope-compatibele videotaakrespons. Importeer uit `plugin-sdk/provider-test-contracts`  
`getProviderHttpMocks` | Gebruik opt-in Vitest-nabootsingen voor provider-HTTP/auth. Importeer uit `plugin-sdk/provider-http-test-mocks`  
`installProviderHttpMockCleanup` | Reset provider-HTTP/auth-nabootsingen na elke test. Importeer uit `plugin-sdk/provider-http-test-mocks`  
`installCommonResolveTargetErrorCases` | Gedeelde testgevallen voor foutafhandeling bij doelresolutie. Importeer uit `plugin-sdk/channel-target-testing`  
`shouldAckReaction` | Controleer of een kanaal een bevestigingsreactie moet toevoegen. Importeer uit `plugin-sdk/channel-feedback`  
`removeAckReactionAfterReply` | Verwijder de bevestigingsreactie na levering van het antwoord. Importeer uit `plugin-sdk/channel-feedback`  
`createTestRegistry` | Bouw een registryfixture voor kanaal-Plugins. Importeer uit `plugin-sdk/plugin-test-runtime` of `plugin-sdk/channel-test-helpers`  
`createEmptyPluginRegistry` | Bouw een lege Plugin-registryfixture. Importeer uit `plugin-sdk/plugin-test-runtime` of `plugin-sdk/channel-test-helpers`  
`setActivePluginRegistry` | Installeer een registryfixture voor Plugin-runtimetests. Importeer uit `plugin-sdk/plugin-test-runtime` of `plugin-sdk/channel-test-helpers`  
`createRequestCaptureJsonFetch` | Leg JSON-fetchverzoeken vast in mediahelpertests. Importeer uit `plugin-sdk/test-env`  
`withServer` | Voer tests uit tegen een wegwerpbare lokale HTTP-server. Importeer uit `plugin-sdk/test-env`  
`createMockIncomingRequest` | Bouw een minimaal inkomend HTTP-verzoekobject. Importeer uit `plugin-sdk/test-env`  
`withFetchPreconnect` | Voer fetch-tests uit met geïnstalleerde preconnect-hooks. Importeer uit `plugin-sdk/test-env`  
`withEnv` / `withEnvAsync` | Patch tijdelijk omgevingsvariabelen. Importeer uit `plugin-sdk/test-env`  
`createTempHomeEnv` / `withTempHome` / `withTempDir` | Maak geïsoleerde testfixtures voor het bestandssysteem. Importeer uit `plugin-sdk/test-env`  
`createMockServerResponse` | Maak een minimale nabootsing van een HTTP-serverrespons. Importeer uit `plugin-sdk/test-env`  
`createCliRuntimeCapture` | Leg CLI-runtimeuitvoer vast in tests. Importeer uit `plugin-sdk/test-fixtures`  
`importFreshModule` | Importeer een ESM-module met een verse querytoken om de modulecache te omzeilen. Importeer uit `plugin-sdk/test-fixtures`  
`bundledPluginRoot` / `bundledPluginFile` | Los fixturepaden voor gebundelde Plugin-broncode of dist op. Importeer uit `plugin-sdk/test-fixtures`  
`mockNodeBuiltinModule` | Installeer smalle Vitest-nabootsingen voor ingebouwde Node-modules. Importeer uit `plugin-sdk/test-node-mocks`  
`createSandboxTestContext` | Bouw sandboxtestcontexten. Importeer uit `plugin-sdk/test-fixtures`  
`writeSkill` | Schrijf skillfixtures. Importeer uit `plugin-sdk/test-fixtures`  
`makeAgentAssistantMessage` | Bouw berichtfixtures voor agenttranscripten. Importeer uit `plugin-sdk/test-fixtures`  
`peekSystemEvents` / `resetSystemEventsForTest` | Inspecteer en reset systeemeventfixtures. Importeer uit `plugin-sdk/test-fixtures`  
`sanitizeTerminalText` | Ontsmet terminaluitvoer voor controles. Importeer uit `plugin-sdk/test-fixtures`  
`countLines` / `hasBalancedFences` | Controleer de vorm van chunking-uitvoer. Importeer uit `plugin-sdk/test-fixtures`  
`runProviderCatalog` | Voer een provider-cataloghook uit met testafhankelijkheden  
`resolveProviderWizardOptions` | Los keuzes van de providerconfiguratiewizard op in contracttests  
`resolveProviderModelPickerEntries` | Los provider-modelkiezeritems op in contracttests  
`buildProviderPluginMethodChoice` | Bouw keuze-id's voor de providerwizard voor controles  
`setProviderWizardProvidersResolverForTest` | Injecteer providerwizardproviders voor geïsoleerde tests  
`createProviderUsageFetch` | Bouw testgegevens voor het ophalen van providergebruik  
`useFrozenTime` / `useRealTime` | Bevries en herstel timers voor tijdgevoelige tests. Importeer uit `plugin-sdk/test-env`  
`createTestWizardPrompter` | Bouw een gemockte prompter voor de installatiewizard  
`createRuntimeTaskFlow` | Maak geïsoleerde runtime-status voor TaskFlow  
`typedCases` | Behoud letterlijke typen voor tabelgestuurde tests. Importeer uit `plugin-sdk/test-fixtures`  
  
Gebundelde Plugin-contractsuites gebruiken ook SDK-testsubpaden voor helpers voor register-, manifest-, openbaar-artifact- en runtime-fixtures die alleen voor tests zijn. Suites die alleen voor core zijn en afhankelijk zijn van de gebundelde OpenClaw-inventaris blijven onder `src/plugins/contracts`. Houd nieuwe extensietests op een gedocumenteerd, gericht SDK-subpad zoals `plugin-sdk/plugin-test-api`, `plugin-sdk/channel-contract-testing`, `plugin-sdk/agent-runtime-test-contracts`, `plugin-sdk/channel-test-helpers`, `plugin-sdk/plugin-test-contracts`, `plugin-sdk/plugin-test-runtime`, `plugin-sdk/provider-test-contracts`, `plugin-sdk/provider-http-test-mocks`, `plugin-sdk/test-env`, of `plugin-sdk/test-fixtures` in plaats van rechtstreeks de brede compatibiliteitsbarrel `plugin-sdk/testing`, repo-`src/**`-bestanden, of repo-`test/helpers/*`-bridges te importeren.

### Typen

Gerichte testsubpaden exporteren ook typen opnieuw die nuttig zijn in testbestanden:

typescriptCopy code
[code]
       ChannelAccountSnapshot,  ChannelGatewayContext,} from "openclaw/plugin-sdk/channel-contract";  
[/code]

## Resolutie van testdoelen

Gebruik `installCommonResolveTargetErrorCases` om standaard foutgevallen toe te voegen voor resolutie van kanaaldoelen:

typescriptCopy code
[code]
      describe("my-channel target resolution", () => {  installCommonResolveTargetErrorCases({    resolveTarget: ({ to, mode, allowFrom }) => {      // Your channel's target resolution logic      return myChannelResolveTarget({ to, mode, allowFrom });    },    implicitAllowFrom: ["user1", "user2"],  });   // Add channel-specific test cases  it("should resolve @username targets", () => {    // ...  });});
[/code]

## Testpatronen

### Registratiecontracten testen

Unit-tests die een handgeschreven `api`-mock doorgeven aan `register(api)` oefenen de acceptatiepoorten van de OpenClaw-loader niet uit. Voeg ten minste één door de loader ondersteunde rooktest toe voor elk registratieoppervlak waarvan je Plugin afhankelijk is, vooral hooks en exclusieve mogelijkheden zoals memory.

De echte loader laat Plugin-registratie mislukken wanneer vereiste metadata ontbreken of een Plugin een capability-API aanroept waarvan het geen eigenaar is. Bijvoorbeeld: `api.registerHook(...)` vereist een hooknaam, en `api.registerMemoryCapability(...)` vereist dat het Plugin-manifest of de geëxporteerde entry `kind: "memory"` declareert.

### Runtime-configuratietoegang testen

Geef de voorkeur aan de gedeelde Plugin-runtime-mock uit `openclaw/plugin-sdk/channel-test-helpers` bij het testen van gebundelde kanaal-Plugins. De verouderde mocks `runtime.config.loadConfig()` en `runtime.config.writeConfigFile(...)` geven standaard een fout, zodat tests nieuw gebruik van compatibiliteits-API's onderscheppen. Overschrijf die mocks alleen wanneer de test expliciet legacy-compatibiliteitsgedrag behandelt.

### Een kanaal-Plugin unit-testen

typescriptCopy code
[code]
     describe("my-channel plugin", () => {  it("should resolve account from config", () => {    const cfg = {      channels: {        "my-channel": {          token: "test-token",          allowFrom: ["user1"],        },      },    };     const account = myPlugin.setup.resolveAccount(cfg, undefined);    expect(account.token).toBe("test-token");  });   it("should inspect account without materializing secrets", () => {    const cfg = {      channels: {        "my-channel": { token: "test-token" },      },    };     const inspection = myPlugin.setup.inspectAccount(cfg, undefined);    expect(inspection.configured).toBe(true);    expect(inspection.tokenStatus).toBe("available");    // No token value exposed    expect(inspection).not.toHaveProperty("token");  });});
[/code]

### Een provider-Plugin unit-testen

typescriptCopy code
[code]
     describe("my-provider plugin", () => {  it("should resolve dynamic models", () => {    const model = myProvider.resolveDynamicModel({      modelId: "custom-model-v2",      // ... context    });     expect(model.id).toBe("custom-model-v2");    expect(model.provider).toBe("my-provider");    expect(model.api).toBe("openai-completions");  });   it("should return catalog when API key is available", async () => {    const result = await myProvider.catalog.run({      resolveProviderApiKey: () => ({ apiKey: "test-key" }),      // ... context    });     expect(result?.provider?.models).toHaveLength(2);  });});
[/code]

### De Plugin-runtime mocken

Voor code die `createPluginRuntimeStore` gebruikt, mock je de runtime in tests:

typescriptCopy code
[code]
      const store = createPluginRuntimeStore&lt;PluginRuntime&gt;({  pluginId: "test-plugin",  errorMessage: "test runtime not set",}); // In test setupconst mockRuntime = {  agent: {    resolveAgentDir: vi.fn().mockReturnValue("/tmp/agent"),    // ... other mocks  },  config: {    current: vi.fn(() => ({}) as const),    mutateConfigFile: vi.fn(),    replaceConfigFile: vi.fn(),  },  // ... other namespaces} as unknown as PluginRuntime; store.setRuntime(mockRuntime); // After testsstore.clearRuntime();
[/code]

### Testen met stubs per instantie

Geef de voorkeur aan stubs per instantie boven prototype-mutatie:

typescriptCopy code
[code]
    // Preferred: per-instance stubconst client = new MyChannelClient();client.sendMessage = vi.fn().mockResolvedValue({ id: "msg-1" }); // Avoid: prototype mutation// MyChannelClient.prototype.sendMessage = vi.fn();
[/code]

## Contracttests (in-repo Plugins)

Gebundelde Plugins hebben contracttests die registratie-eigenaarschap verifiëren:

bashCopy code
[code]
    pnpm test -- src/plugins/contracts/
[/code]

Deze tests controleren:

  * Welke Plugins welke providers registreren
  * Welke Plugins welke speech-providers registreren
  * Correctheid van de registratievorm
  * Naleving van het runtime-contract


### Scoped tests uitvoeren

Voor een specifieke Plugin:

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-channel/
[/code]

Alleen voor contracttests:

bashCopy code
[code]
    pnpm test -- src/plugins/contracts/shape.contract.test.tspnpm test -- src/plugins/contracts/auth-choice.contract.test.tspnpm test -- src/plugins/contracts/runtime-seams.contract.test.ts
[/code]

## Lint-afdwinging (in-repo Plugins)

Drie regels worden afgedwongen door `pnpm check` voor in-repo Plugins:

  1. **Geen monolithische root-imports** \-- de root-barrel `openclaw/plugin-sdk` wordt geweigerd
  2. **Geen directe`src/`-imports** \-- Plugins kunnen `../../src/` niet rechtstreeks importeren
  3. **Geen zelfimports** \-- Plugins kunnen hun eigen subpad `plugin-sdk/<name>` niet importeren


Externe Plugins vallen niet onder deze lintregels, maar het volgen van dezelfde patronen wordt aanbevolen.

## Testconfiguratie

OpenClaw gebruikt Vitest met V8-dekkingsdrempels. Voor Plugin-tests:

bashCopy code
[code]
    # Run all testspnpm test # Run specific plugin testspnpm test -- <bundled-plugin-root>/my-channel/src/channel.test.ts # Run with a specific test name filterpnpm test -- <bundled-plugin-root>/my-channel/ -t "resolves account" # Run with coveragepnpm test:coverage
[/code]

Als lokale runs geheugendruk veroorzaken:

bashCopy code
[code]
    OPENCLAW_VITEST_MAX_WORKERS=1 pnpm test
[/code]

## Gerelateerd

  * [SDK-overzicht](</nl/plugins/sdk-overview>) \-- importconventies
  * [SDK-kanaal-Plugins](</nl/plugins/sdk-channel-plugins>) \-- interface voor kanaal-Plugins
  * [SDK-provider-Plugins](</nl/plugins/sdk-provider-plugins>) \-- hooks voor provider-Plugins
  * [Plugins bouwen](</nl/plugins/building-plugins>) \-- gids om aan de slag te gaan


Was this useful?YesNo