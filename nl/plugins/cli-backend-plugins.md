---
title: CLI-backend-Plugins bouwen
source_url: https://docs.openclaw.ai/nl/plugins/cli-backend-plugins
scraped_at: 2026-05-25
---

CLI-backendplugins laten OpenClaw een lokale AI-CLI aanroepen als tekstinferentiebackend. De backend verschijnt als een providerprefix in modelverwijzingen:

textCopy code
[code]
    acme-cli/acme-large
[/code]

Gebruik een CLI-backend wanneer de upstreamintegratie al als lokale opdracht beschikbaar is, wanneer de CLI lokale aanmeldstatus beheert, of wanneer de CLI een nuttige fallback is als API-providers niet beschikbaar zijn.

## Wat de plugin beheert

Een CLI-backendplugin heeft drie contracten:

Contract | Bestand | Doel  
---|---|---  
Pakketinvoer | `package.json` | Wijst OpenClaw naar de runtime-module van de plugin  
Manifesteigenaarschap | `openclaw.plugin.json` | Declareert de backend-id voordat de runtime wordt geladen  
Runtimeregistratie | `index.ts` | Roept `api.registerCliBackend(...)` aan met opdrachtstandaarden  
  
Het manifest is discoverymetadata. Het voert de CLI niet uit en registreert geen runtimegedrag. Runtimegedrag start wanneer de plugininvoer `api.registerCliBackend(...)` aanroept.

## Minimale backendplugin

* ### Create package metadata

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-acme-cli",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  },  "dependencies": {    "openclaw": "^2026.3.24"  },  "devDependencies": {    "typescript": "^5.9.0"  }}
[/code]

Gepubliceerde pakketten moeten gebouwde JavaScript-runtimebestanden meeleveren. Als je broninvoer `./src/index.ts` is, voeg dan `openclaw.runtimeExtensions` toe die naar de gebouwde JavaScript-tegenhanger wijst. Zie [Invoerpunten](</nl/plugins/sdk-entrypoints>).

* ### Declare backend ownership

openclaw.plugin.jsonCopy code
[code]
    {  "id": "acme-cli",  "name": "Acme CLI",  "description": "Run Acme's local AI CLI through OpenClaw",  "cliBackends": ["acme-cli"],  "setup": {    "cliBackends": ["acme-cli"],    "requiresRuntime": false  },  "activation": {    "onStartup": false  },  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

`cliBackends` is de runtime-eigenaarschapslijst. Hiermee kan OpenClaw de plugin automatisch laden wanneer configuratie of modelselectie `acme-cli/...` vermeldt.

`setup.cliBackends` is het descriptor-first setup-oppervlak. Voeg het toe wanneer modeldiscovery, onboarding of status de backend moet herkennen zonder pluginruntime te laden. Gebruik `requiresRuntime: false` alleen wanneer die statische descriptors voldoende zijn voor setup.

* ### Register the backend

index.tsCopy code
[code]
    import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import {  CLI_FRESH_WATCHDOG_DEFAULTS,  CLI_RESUME_WATCHDOG_DEFAULTS,  type CliBackendPlugin,} from "openclaw/plugin-sdk/cli-backend"; function buildAcmeCliBackend(): CliBackendPlugin {  return {    id: "acme-cli",    liveTest: {      defaultModelRef: "acme-cli/acme-large",      defaultImageProbe: false,      defaultMcpProbe: false,      docker: {        npmPackage: "@acme/acme-cli",        binaryName: "acme",      },    },    config: {      command: "acme",      args: ["chat", "--json"],      output: "json",      input: "stdin",      modelArg: "--model",      sessionArg: "--session",      sessionMode: "existing",      sessionIdFields: ["session_id", "conversation_id"],      systemPromptFileArg: "--system-file",      systemPromptWhen: "first",      imageArg: "--image",      imageMode: "repeat",      reliability: {        watchdog: {          fresh: { ...CLI_FRESH_WATCHDOG_DEFAULTS },          resume: { ...CLI_RESUME_WATCHDOG_DEFAULTS },        },      },      serialize: true,    },  };} export default definePluginEntry({  id: "acme-cli",  name: "Acme CLI",  description: "Run Acme's local AI CLI through OpenClaw",  register(api) {    api.registerCliBackend(buildAcmeCliBackend());  },});
[/code]

De backend-id moet overeenkomen met de `cliBackends`-invoer in het manifest. De geregistreerde `config` is alleen de standaard; gebruikersconfiguratie onder `agents.defaults.cliBackends.acme-cli` wordt er tijdens runtime overheen samengevoegd.

## Configuratievorm

`CliBackendConfig` beschrijft hoe OpenClaw de CLI moet starten en parsen:

Veld | Gebruik  
---|---  
`command` | Binaire naam of absoluut opdrachtpad  
`args` | Basis-argv voor nieuwe runs  
`resumeArgs` | Alternatieve argv voor hervatte sessies; ondersteunt `{sessionId}`  
`output` / `resumeOutput` | Parser: `json`, `jsonl` of `text`  
`input` | Prompttransport: `arg` of `stdin`  
`modelArg` | Vlag die voor de model-id wordt gebruikt  
`modelAliases` | Koppelt OpenClaw-model-id's aan CLI-native id's  
`sessionArg` / `sessionArgs` | Hoe een sessie-id wordt doorgegeven  
`sessionMode` | `always`, `existing` of `none`  
`sessionIdFields` | JSON-velden die OpenClaw uit CLI-uitvoer leest  
`systemPromptArg` / `systemPromptFileArg` | Systeemprompttransport  
`systemPromptWhen` | `first`, `always` of `never`  
`imageArg` / `imageMode` | Ondersteuning voor afbeeldingspaden  
`serialize` | Houd runs op dezelfde backend geordend  
`reliability.watchdog` | Afstelling van time-out zonder uitvoer  
  
Geef de voorkeur aan de kleinste statische configuratie die bij de CLI past. Voeg plugincallbacks alleen toe voor gedrag dat echt bij de backend hoort.

## Geavanceerde backendhooks

`CliBackendPlugin` kan ook definiëren:

Hook | Gebruik  
---|---  
`normalizeConfig(config, context)` | Herschrijf verouderde gebruikersconfiguratie na samenvoegen  
`resolveExecutionArgs(ctx)` | Voeg aanvraaggebonden vlaggen toe, zoals denkintensiteit  
`prepareExecution(ctx)` | Maak tijdelijke auth- of configuratiebruggen vóór het starten  
`transformSystemPrompt(ctx)` | Pas een laatste CLI-specifieke systeemprompttransformatie toe  
`textTransforms` | Bidirectionele prompt-/uitvoervervangingen  
`defaultAuthProfileId` | Geef voorkeur aan een specifiek OpenClaw-auth-profiel  
`authEpochMode` | Bepaal hoe authwijzigingen opgeslagen CLI-sessies ongeldig maken  
`nativeToolMode` | Declareer of de CLI altijd ingeschakelde native tools heeft  
`bundleMcp` / `bundleMcpMode` | Kies voor OpenClaw's loopback-MCP-toolbrug  
  
Houd deze hooks provider-eigendom. Voeg geen CLI-specifieke vertakkingen toe aan core wanneer een backendhook het gedrag kan uitdrukken.

## MCP-toolbrug

CLI-backends ontvangen standaard geen OpenClaw-tools. Als de CLI een MCP-configuratie kan gebruiken, kies daar dan expliciet voor:

typescriptCopy code
[code]
    return {  id: "acme-cli",  bundleMcp: true,  bundleMcpMode: "codex-config-overrides",  config: {    command: "acme",    args: ["chat", "--json"],    output: "json",  },};
[/code]

Ondersteunde brugmodi zijn:

Modus | Gebruik  
---|---  
`claude-config-file` | CLI's die een MCP-configuratiebestand accepteren  
`codex-config-overrides` | CLI's die configuratie-overschrijvingen op argv accepteren  
`gemini-system-settings` | CLI's die MCP-instellingen lezen uit hun systeeminstellingenmap  
  
Schakel de brug alleen in wanneer de CLI die daadwerkelijk kan gebruiken. Als de CLI een eigen ingebouwde toollaag heeft die niet kan worden uitgeschakeld, stel dan `nativeToolMode: "always-on"` in zodat OpenClaw gesloten kan falen wanneer een aanroeper geen native tools vereist.

## Gebruikersconfiguratie

Gebruikers kunnen elke backendstandaard overschrijven:

json5Copy code
[code]
    {  agents: {    defaults: {      cliBackends: {        "acme-cli": {          command: "/opt/acme/bin/acme",          args: ["chat", "--json", "--profile", "work"],          modelAliases: {            large: "acme-large-2026",          },        },      },      model: {        primary: "openai/gpt-5.5",        fallbacks: ["acme-cli/large"],      },    },  },}
[/code]

Documenteer de minimale overschrijving die gebruikers waarschijnlijk nodig hebben. Meestal is dat alleen `command` wanneer de binary buiten `PATH` staat.

## Verificatie

Voor gebundelde plugins voeg je een gerichte test toe rond de builder en setupregistratie, en voer je daarna de gerichte testlane van de plugin uit:

bashCopy code
[code]
    pnpm test extensions/acme-cli
[/code]

Voor lokale of geïnstalleerde plugins verifieer je discovery en één echte modelrun:

bashCopy code
[code]
    openclaw plugins inspect acme-cli --runtime --jsonopenclaw agent --message "reply exactly: backend ok" --model acme-cli/acme-large
[/code]

Als de backend afbeeldingen of MCP ondersteunt, voeg dan een live smoke toe die die paden met de echte CLI bewijst. Vertrouw niet op statische inspectie voor prompt-, afbeeldings-, MCP- of sessiehervattingsgedrag.

## Checklist

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `package.json` heeft `openclaw.extensions` en gebouwde runtime-invoerpunten voor gepubliceerde pakketten OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `openclaw.plugin.json` declareert `cliBackends` en intentionele `activation.onStartup` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `setup.cliBackends` is aanwezig wanneer setup/modeldiscovery de backend koud moet zien OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `api.registerCliBackend(...)` gebruikt dezelfde backend-id als het manifest OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Gebruikersoverschrijvingen onder `agents.defaults.cliBackends.<id>` winnen nog steeds OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo