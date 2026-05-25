---
title: Plugins bouwen
source_url: https://docs.openclaw.ai/nl/plugins/building-plugins
scraped_at: 2026-05-25
---

Plugins breiden OpenClaw uit met nieuwe mogelijkheden: kanalen, modelproviders, spraak, realtime transcriptie, realtime spraak, mediabegrip, beeldgeneratie, videogeneratie, web-fetch, webzoekopdrachten, agenttools of elke gewenste combinatie.

Je hoeft je plugin niet toe te voegen aan de OpenClaw-repository. Publiceer naar [ClawHub](</nl/clawhub>) en gebruikers installeren met `openclaw plugins install clawhub:<package-name>`. Pakketspecificaties zonder prefix installeren tijdens de overgang bij lancering nog steeds vanaf npm.

## Vereisten

  * Node >= 22 en een pakketbeheerder (npm of pnpm)
  * Bekendheid met TypeScript (ESM)
  * Voor plugins in de repo: repository gekloond en `pnpm install` uitgevoerd. Ontwikkeling met een source-checkout van plugins is alleen pnpm, omdat OpenClaw gebundelde plugins laadt vanuit de workspace-pakketten `extensions/*`.


## Welk soort plugin?

[**Kanaalplugin** Verbind OpenClaw met een berichtenplatform (Discord, IRC, enz.) ](</nl/plugins/sdk-channel-plugins>) [**Providerplugin** Voeg een modelprovider toe (LLM, proxy of aangepast endpoint) ](</nl/plugins/sdk-provider-plugins>) [**CLI-backendplugin** Koppel een lokale AI-CLI aan de tekstfallbackrunner van OpenClaw ](</nl/plugins/cli-backend-plugins>) [**Tool-/hookplugin** Registreer agenttools, eventhooks of services - ga hieronder verder ](</nl/plugins/hooks>)

Voor een kanaalplugin waarvan niet gegarandeerd is dat die is geïnstalleerd wanneer onboarding/setup wordt uitgevoerd, gebruik je `createOptionalChannelSetupSurface(...)` uit `openclaw/plugin-sdk/channel-setup`. Dit levert een setupadapter + wizard-paar op dat de installatievereiste communiceert en echt schrijven naar configuratie geblokkeerd laat totdat de plugin is geïnstalleerd.

## Snelstart: toolplugin

Deze walkthrough maakt een minimale plugin die een agenttool registreert. Kanaal- en providerplugins hebben eigen handleidingen die hierboven zijn gelinkt.

* ### Maak het pakket en het manifest

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {  "extensions": ["./index.ts"],  "compat": {    "pluginApi": ">=2026.3.24-beta.2",    "minGatewayVersion": "2026.3.24-beta.2"  },  "build": {    "openclawVersion": "2026.3.24-beta.2",    "pluginSdkVersion": "2026.3.24-beta.2"  }}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {  "tools": ["my_tool"]},"activation": {  "onStartup": true},"configSchema": {  "type": "object",  "additionalProperties": false}}
[/code]

Elke plugin heeft een manifest nodig, zelfs zonder configuratie. Runtime-geregistreerde tools moeten worden vermeld in `contracts.tools`, zodat OpenClaw de eigenaar-plugin kan vinden zonder elke pluginruntime te laden. Plugins moeten ook bewust `activation.onStartup` declareren. Dit voorbeeld zet dit op `true`. Zie [Manifest](</nl/plugins/manifest>) voor het volledige schema. De canonieke ClawHub- publicatiesnippets staan in `docs/snippets/plugin-publish/`.

* ### Schrijf het entrypoint

typescriptCopy code
[code]
    // index.tsimport { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { Type } from "@sinclair/typebox"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Do a thing",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: `Got: ${params.input}` }] };      },    });  },});
[/code]

`definePluginEntry` is voor niet-kanaalplugins. Gebruik voor kanalen `defineChannelPluginEntry` \- zie [Kanaalplugins](</nl/plugins/sdk-channel-plugins>). Zie [Entrypoints](</nl/plugins/sdk-entrypoints>) voor alle entrypointopties.

* ### Test en publiceer

**Externe plugins:** valideer en publiceer met ClawHub en installeer daarna:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginopenclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

Pakketspecificaties zonder prefix zoals `@myorg/openclaw-my-plugin` installeren tijdens de overgang bij lancering vanaf npm. Gebruik `clawhub:` wanneer je ClawHub-resolutie wilt.

**Plugins in de repo:** plaats ze onder de workspace-boom voor gebundelde plugins - automatisch gedetecteerd.

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-plugin/
[/code]

## Plugin-mogelijkheden

Een enkele plugin kan een willekeurig aantal mogelijkheden registreren via het `api`-object:

Mogelijkheid | Registratiemethode | Gedetailleerde handleiding  
---|---|---  
Tekstinferentie (LLM) | `api.registerProvider(...)` | [Providerplugins](</nl/plugins/sdk-provider-plugins>)  
CLI-inferentiebackend | `api.registerCliBackend(...)` | [CLI-backendplugins](</nl/plugins/cli-backend-plugins>)  
Kanaal / berichten | `api.registerChannel(...)` | [Kanaalplugins](</nl/plugins/sdk-channel-plugins>)  
Spraak (TTS/STT) | `api.registerSpeechProvider(...)` | [Providerplugins](</nl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Realtime transcriptie | `api.registerRealtimeTranscriptionProvider(...)` | [Providerplugins](</nl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Realtime spraak | `api.registerRealtimeVoiceProvider(...)` | [Providerplugins](</nl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Mediabegrip | `api.registerMediaUnderstandingProvider(...)` | [Providerplugins](</nl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Beeldgeneratie | `api.registerImageGenerationProvider(...)` | [Providerplugins](</nl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Muziekgeneratie | `api.registerMusicGenerationProvider(...)` | [Providerplugins](</nl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Videogeneratie | `api.registerVideoGenerationProvider(...)` | [Providerplugins](</nl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Web-fetch | `api.registerWebFetchProvider(...)` | [Providerplugins](</nl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Webzoekopdracht | `api.registerWebSearchProvider(...)` | [Providerplugins](</nl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Toolresultaatmiddleware | `api.registerAgentToolResultMiddleware(...)` | [SDK-overzicht](</nl/plugins/sdk-overview#registration-api>)  
Agenttools | `api.registerTool(...)` | Hieronder  
Aangepaste opdrachten | `api.registerCommand(...)` | [Entrypoints](</nl/plugins/sdk-entrypoints>)  
Pluginhooks | `api.on(...)` | [Pluginhooks](</nl/plugins/hooks>)  
Interne eventhooks | `api.registerHook(...)` | [Entrypoints](</nl/plugins/sdk-entrypoints>)  
HTTP-routes | `api.registerHttpRoute(...)` | [Internals](</nl/plugins/architecture-internals#gateway-http-routes>)  
CLI-subopdrachten | `api.registerCli(...)` | [Entrypoints](</nl/plugins/sdk-entrypoints>)  
  
Zie [SDK-overzicht](</nl/plugins/sdk-overview#registration-api>) voor de volledige registratie-API.

Gebundelde plugins kunnen `api.registerAgentToolResultMiddleware(...)` gebruiken wanneer ze asynchrone herschrijving van toolresultaten nodig hebben voordat het model de uitvoer ziet. Declareer de beoogde runtimes in `contracts.agentToolResultMiddleware`, bijvoorbeeld `["pi", "codex"]`. Dit is een vertrouwde seam voor gebundelde plugins; externe plugins kunnen beter reguliere OpenClaw-pluginhooks gebruiken, tenzij OpenClaw een expliciet vertrouwensbeleid voor deze mogelijkheid krijgt.

Als je plugin aangepaste Gateway-RPC-methoden registreert, houd ze dan op een pluginspecifieke prefix. Core-beheernamespaces (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) blijven gereserveerd en resolven altijd naar `operator.admin`, zelfs als een plugin om een nauwere scope vraagt.

Hook-guardsemantiek om rekening mee te houden:

  * `before_tool_call`: `{ block: true }` is terminaal en stopt handlers met lagere prioriteit.
  * `before_tool_call`: `{ block: false }` wordt behandeld als geen beslissing.
  * `before_tool_call`: `{ requireApproval: true }` pauzeert agentuitvoering en vraagt de gebruiker om goedkeuring via de exec-goedkeuringsoverlay, Telegram-knoppen, Discord-interacties of de opdracht `/approve` op elk kanaal.
  * `before_install`: `{ block: true }` is terminaal en stopt handlers met lagere prioriteit.
  * `before_install`: `{ block: false }` wordt behandeld als geen beslissing.
  * `message_sending`: `{ cancel: true }` is terminaal en stopt handlers met lagere prioriteit.
  * `message_sending`: `{ cancel: false }` wordt behandeld als geen beslissing.
  * `message_received`: geef de voorkeur aan het getypte veld `threadId` wanneer je inkomende thread-/topicrouting nodig hebt. Bewaar `metadata` voor kanaalspecifieke extra's.
  * `message_sending`: geef de voorkeur aan getypte routingvelden `replyToId` / `threadId` boven kanaalspecifieke metadatasleutels.


De opdracht `/approve` verwerkt zowel exec- als plugingoedkeuringen met begrensde fallback: wanneer een exec-goedkeurings-id niet wordt gevonden, probeert OpenClaw hetzelfde id opnieuw via plugingoedkeuringen. Doorsturen van plugingoedkeuringen kan onafhankelijk worden geconfigureerd via `approvals.plugin` in de configuratie.

Als aangepaste goedkeuringsplumbing diezelfde begrensde fallbackcase moet detecteren, gebruik dan bij voorkeur `isApprovalNotFoundError` uit `openclaw/plugin-sdk/error-runtime` in plaats van handmatig te matchen op strings voor verlopen goedkeuringen.

Zie [Pluginhooks](</nl/plugins/hooks>) voor voorbeelden en de hookreferentie.

## Agenttools registreren

Tools zijn getypte functies die de LLM kan aanroepen. Ze kunnen vereist zijn (altijd beschikbaar) of optioneel (opt-in door gebruiker):

typescriptCopy code
[code]
    register(api) {  // Required tool - always available  api.registerTool({    name: "my_tool",    description: "Do a thing",    parameters: Type.Object({ input: Type.String() }),    async execute(_id, params) {      return { content: [{ type: "text", text: params.input }] };    },  });   // Optional tool - user must add to allowlist  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

Tool-factories ontvangen een door de runtime geleverd contextobject. Gebruik `ctx.activeModel` wanneer een tool het actieve model voor de huidige beurt moet loggen, weergeven of zich eraan moet aanpassen. Het object kan `provider`, `modelId` en `modelRef` bevatten. Behandel het als informatieve runtimemetadata, niet als een beveiligingsgrens tegenover de lokale operator, geïnstalleerde plugincode of een aangepaste OpenClaw-runtime. Houd voor gevoelige lokale tools een expliciete opt-in van de Plugin of operator aan en faal gesloten wanneer de actieve-modelmetadata ontbreekt of ongeschikt is.

Elke tool die met `api.registerTool(...)` wordt geregistreerd, moet ook in het pluginmanifest worden gedeclareerd:

jsonCopy code
[code]
    {  "contracts": {    "tools": ["my_tool", "workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

OpenClaw legt de gevalideerde descriptor van de geregistreerde tool vast en cachet die, zodat plugins geen `description`\- of schemagegevens in het manifest dupliceren. Het manifestcontract declareert alleen eigenaarschap en ontdekking; uitvoering roept nog steeds de live geregistreerde toolimplementatie aan. Stel `toolMetadata.<tool>.optional: true` in voor tools die zijn geregistreerd met `api.registerTool(..., { optional: true })`, zodat OpenClaw kan voorkomen dat die pluginruntime wordt geladen totdat de tool expliciet op de toestaanlijst staat.

Gebruikers schakelen optionele tools in de configuratie in:

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] },}
[/code]

  * Toolnamen mogen niet botsen met kerntools (conflicten worden overgeslagen)
  * Tools met onjuist gevormde registratieobjecten, inclusief ontbrekende `parameters`, worden overgeslagen en in plugindiagnostiek gerapporteerd in plaats van agentruns te onderbreken
  * Gebruik `optional: true` voor tools met bijwerkingen of extra binaire vereisten
  * Gebruikers kunnen alle tools van een Plugin inschakelen door de plugin-id aan `tools.allow` toe te voegen


## CLI-opdrachten registreren

Plugins kunnen root-`openclaw`-opdrachtgroepen toevoegen met `api.registerCli`. Geef `descriptors` op voor elke opdrachtroot op topniveau, zodat OpenClaw de opdracht kan tonen en routeren zonder elke pluginruntime vooraf te laden.

typescriptCopy code
[code]
    register(api) {  api.registerCli(    ({ program }) => {      const demo = program        .command("demo-plugin")        .description("Run demo plugin commands");       demo        .command("ping")        .description("Check that the plugin CLI is executable")        .action(() => {          console.log("demo-plugin:pong");        });    },    {      descriptors: [        {          name: "demo-plugin",          description: "Run demo plugin commands",          hasSubcommands: true,        },      ],    },  );}
[/code]

Controleer na installatie de runtimeregistratie en voer de opdracht uit:

bashCopy code
[code]
    openclaw plugins inspect demo-plugin --runtime --jsonopenclaw demo-plugin ping
[/code]

## Importconventies

Importeer altijd uit gerichte `openclaw/plugin-sdk/<subpath>`-paden:

typescriptCopy code
[code]
      // Wrong: monolithic root (deprecated, will be removed) 
[/code]

Zie [SDK-overzicht](</nl/plugins/sdk-overview>) voor de volledige subpadreferentie.

Gebruik binnen je Plugin lokale barrelbestanden (`api.ts`, `runtime-api.ts`) voor interne imports - importeer je eigen Plugin nooit via het SDK-pad ervan.

Houd voor providerplugins provider-specifieke helpers in die package-root-barrels, tenzij de seam echt generiek is. Huidige gebundelde voorbeelden:

  * Anthropic: Claude-streamwrappers en `service_tier`-/betahelpers
  * OpenAI: providerbuilders, default-modelhelpers, realtimeproviders
  * OpenRouter: providerbuilder plus onboarding-/confighelpers


Als een helper alleen nuttig is binnen één gebundeld providerpakket, houd die dan op die package-root-seam in plaats van die naar `openclaw/plugin-sdk/*` te promoveren.

Sommige gegenereerde `openclaw/plugin-sdk/<bundled-id>`-helperseams bestaan nog voor onderhoud van gebundelde plugins wanneer ze gevolgd eigenaargebruik hebben. Behandel die als gereserveerde oppervlakken, niet als het standaardpatroon voor nieuwe plugins van derden.

## Checklist vóór indiening

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **package.json** heeft correcte `openclaw`-metadata OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **openclaw.plugin.json** -manifest is aanwezig en geldig OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Entry point gebruikt `defineChannelPluginEntry` of `definePluginEntry` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Alle imports gebruiken gerichte `plugin-sdk/<subpath>`-paden OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo