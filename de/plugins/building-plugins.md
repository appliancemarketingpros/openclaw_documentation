---
title: Plugins erstellen
source_url: https://docs.openclaw.ai/de/plugins/building-plugins
scraped_at: 2026-05-25
---

Plugins erweitern OpenClaw um neue Funktionen: Kanäle, Modell-Provider, Sprache, Echtzeit-Transkription, Echtzeit-Stimme, Medienverständnis, Bildgenerierung, Videogenerierung, Web-Abruf, Websuche, Agent-Tools oder beliebige Kombinationen davon.

Sie müssen Ihr Plugin nicht zum OpenClaw-Repository hinzufügen. Veröffentlichen Sie es auf [ClawHub](</de/clawhub>), und Benutzer installieren es mit `openclaw plugins install clawhub:<package-name>`. Reine Package-Spezifikationen installieren während der Launch-Umstellung weiterhin von npm.

## Voraussetzungen

  * Node >= 22 und ein Package-Manager (npm oder pnpm)
  * Vertrautheit mit TypeScript (ESM)
  * Für Plugins im Repository: Repository geklont und `pnpm install` ausgeführt. Die Plugin-Entwicklung aus einem Source-Checkout ist nur mit pnpm möglich, weil OpenClaw gebündelte Plugins aus den Workspace-Packages `extensions/*` lädt.


## Welche Art von Plugin?

[**Channel plugin** OpenClaw mit einer Messaging-Plattform verbinden (Discord, IRC usw.) ](</de/plugins/sdk-channel-plugins>) [**Provider plugin** Einen Modell-Provider hinzufügen (LLM, Proxy oder benutzerdefinierter Endpunkt) ](</de/plugins/sdk-provider-plugins>) [**CLI backend plugin** Eine lokale KI-CLI auf OpenClaws Text-Fallback-Runner abbilden ](</de/plugins/cli-backend-plugins>) [**Tool / hook plugin** Agent-Tools, Event-Hooks oder Dienste registrieren - fahren Sie unten fort ](</de/plugins/hooks>)

Für ein Kanal-Plugin, bei dem nicht garantiert ist, dass es installiert ist, wenn Onboarding/Setup ausgeführt wird, verwenden Sie `createOptionalChannelSetupSurface(...)` aus `openclaw/plugin-sdk/channel-setup`. Es erzeugt ein Setup-Adapter- und Wizard-Paar, das die Installationsanforderung kommuniziert und echte Konfigurationsschreibvorgänge geschlossen fehlschlagen lässt, bis das Plugin installiert ist.

## Schnellstart: Tool-Plugin

Diese Anleitung erstellt ein minimales Plugin, das ein Agent-Tool registriert. Für Kanal- und Provider-Plugins gibt es oben verlinkte eigene Anleitungen.

* ### Create the package and manifest

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {  "extensions": ["./index.ts"],  "compat": {    "pluginApi": ">=2026.3.24-beta.2",    "minGatewayVersion": "2026.3.24-beta.2"  },  "build": {    "openclawVersion": "2026.3.24-beta.2",    "pluginSdkVersion": "2026.3.24-beta.2"  }}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {  "tools": ["my_tool"]},"activation": {  "onStartup": true},"configSchema": {  "type": "object",  "additionalProperties": false}}
[/code]

Jedes Plugin benötigt ein Manifest, auch ohne Konfiguration. Zur Laufzeit registrierte Tools müssen in `contracts.tools` aufgeführt sein, damit OpenClaw das besitzende Plugin finden kann, ohne jede Plugin-Laufzeitumgebung zu laden. Plugins sollten außerdem `activation.onStartup` bewusst deklarieren. Dieses Beispiel setzt es auf `true`. Siehe [Manifest](</de/plugins/manifest>) für das vollständige Schema. Die kanonischen ClawHub- Veröffentlichungssnippets befinden sich in `docs/snippets/plugin-publish/`.

* ### Write the entry point

typescriptCopy code
[code]
    // index.tsimport { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { Type } from "@sinclair/typebox"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Do a thing",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: `Got: ${params.input}` }] };      },    });  },});
[/code]

`definePluginEntry` ist für Plugins, die keine Kanäle sind. Für Kanäle verwenden Sie `defineChannelPluginEntry` \- siehe [Kanal-Plugins](</de/plugins/sdk-channel-plugins>). Vollständige Entry-Point-Optionen finden Sie unter [Entry Points](</de/plugins/sdk-entrypoints>).

* ### Test and publish

**Externe Plugins:** Mit ClawHub validieren und veröffentlichen, dann installieren:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginopenclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

Reine Package-Spezifikationen wie `@myorg/openclaw-my-plugin` installieren während der Launch-Umstellung von npm. Verwenden Sie `clawhub:`, wenn Sie ClawHub-Auflösung wünschen.

**Plugins im Repository:** Unter dem gebündelten Plugin-Workspace-Baum ablegen - wird automatisch erkannt.

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-plugin/
[/code]

## Plugin-Funktionen

Ein einzelnes Plugin kann über das `api`-Objekt beliebig viele Funktionen registrieren:

Funktion | Registrierungsmethode | Detaillierte Anleitung  
---|---|---  
Text-Inferenz (LLM) | `api.registerProvider(...)` | [Provider-Plugins](</de/plugins/sdk-provider-plugins>)  
CLI-Inferenz-Backend | `api.registerCliBackend(...)` | [CLI-Backend-Plugins](</de/plugins/cli-backend-plugins>)  
Kanal / Messaging | `api.registerChannel(...)` | [Kanal-Plugins](</de/plugins/sdk-channel-plugins>)  
Sprache (TTS/STT) | `api.registerSpeechProvider(...)` | [Provider-Plugins](</de/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Echtzeit-Transkription | `api.registerRealtimeTranscriptionProvider(...)` | [Provider-Plugins](</de/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Echtzeit-Stimme | `api.registerRealtimeVoiceProvider(...)` | [Provider-Plugins](</de/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Medienverständnis | `api.registerMediaUnderstandingProvider(...)` | [Provider-Plugins](</de/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Bildgenerierung | `api.registerImageGenerationProvider(...)` | [Provider-Plugins](</de/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Musikgenerierung | `api.registerMusicGenerationProvider(...)` | [Provider-Plugins](</de/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Videogenerierung | `api.registerVideoGenerationProvider(...)` | [Provider-Plugins](</de/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Web-Abruf | `api.registerWebFetchProvider(...)` | [Provider-Plugins](</de/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Websuche | `api.registerWebSearchProvider(...)` | [Provider-Plugins](</de/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Tool-Ergebnis-Middleware | `api.registerAgentToolResultMiddleware(...)` | [SDK-Überblick](</de/plugins/sdk-overview#registration-api>)  
Agent-Tools | `api.registerTool(...)` | Unten  
Benutzerdefinierte Befehle | `api.registerCommand(...)` | [Entry Points](</de/plugins/sdk-entrypoints>)  
Plugin-Hooks | `api.on(...)` | [Plugin-Hooks](</de/plugins/hooks>)  
Interne Event-Hooks | `api.registerHook(...)` | [Entry Points](</de/plugins/sdk-entrypoints>)  
HTTP-Routen | `api.registerHttpRoute(...)` | [Interna](</de/plugins/architecture-internals#gateway-http-routes>)  
CLI-Unterbefehle | `api.registerCli(...)` | [Entry Points](</de/plugins/sdk-entrypoints>)  
  
Die vollständige Registrierungs-API finden Sie unter [SDK-Überblick](</de/plugins/sdk-overview#registration-api>).

Gebündelte Plugins können `api.registerAgentToolResultMiddleware(...)` verwenden, wenn sie asynchrones Umschreiben von Tool-Ergebnissen benötigen, bevor das Modell die Ausgabe sieht. Deklarieren Sie die Ziel-Laufzeiten in `contracts.agentToolResultMiddleware`, zum Beispiel `["pi", "codex"]`. Dies ist eine vertrauenswürdige Schnittstelle für gebündelte Plugins; externe Plugins sollten reguläre OpenClaw-Plugin-Hooks bevorzugen, solange OpenClaw keine explizite Vertrauensrichtlinie für diese Funktion erhält.

Wenn Ihr Plugin benutzerdefinierte Gateway-RPC-Methoden registriert, belassen Sie diese unter einem Plugin-spezifischen Präfix. Core-Admin-Namespaces (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) bleiben reserviert und werden immer zu `operator.admin` aufgelöst, selbst wenn ein Plugin einen engeren Scope anfordert.

Hook-Guard-Semantik, die Sie beachten sollten:

  * `before_tool_call`: `{ block: true }` ist terminal und stoppt Handler mit niedrigerer Priorität.
  * `before_tool_call`: `{ block: false }` wird als keine Entscheidung behandelt.
  * `before_tool_call`: `{ requireApproval: true }` pausiert die Agent-Ausführung und fordert den Benutzer über das Exec-Genehmigungs-Overlay, Telegram-Schaltflächen, Discord-Interaktionen oder den Befehl `/approve` auf einem beliebigen Kanal zur Genehmigung auf.
  * `before_install`: `{ block: true }` ist terminal und stoppt Handler mit niedrigerer Priorität.
  * `before_install`: `{ block: false }` wird als keine Entscheidung behandelt.
  * `message_sending`: `{ cancel: true }` ist terminal und stoppt Handler mit niedrigerer Priorität.
  * `message_sending`: `{ cancel: false }` wird als keine Entscheidung behandelt.
  * `message_received`: Bevorzugen Sie das typisierte Feld `threadId`, wenn Sie eingehendes Thread-/Topic-Routing benötigen. Behalten Sie `metadata` für kanalspezifische Extras bei.
  * `message_sending`: Bevorzugen Sie die typisierten Routing-Felder `replyToId` / `threadId` gegenüber kanalspezifischen Metadaten-Schlüsseln.


Der Befehl `/approve` behandelt sowohl Exec- als auch Plugin-Genehmigungen mit begrenztem Fallback: Wenn eine Exec-Genehmigungs-ID nicht gefunden wird, versucht OpenClaw dieselbe ID erneut über Plugin-Genehmigungen. Die Weiterleitung von Plugin-Genehmigungen kann unabhängig über `approvals.plugin` in der Konfiguration konfiguriert werden.

Wenn benutzerdefinierte Genehmigungslogik denselben begrenzten Fallback-Fall erkennen muss, bevorzugen Sie `isApprovalNotFoundError` aus `openclaw/plugin-sdk/error-runtime`, anstatt Genehmigungsablauf-Strings manuell abzugleichen.

Beispiele und die Hook-Referenz finden Sie unter [Plugin-Hooks](</de/plugins/hooks>).

## Agent-Tools registrieren

Tools sind typisierte Funktionen, die das LLM aufrufen kann. Sie können erforderlich (immer verfügbar) oder optional (Opt-in durch den Benutzer) sein:

typescriptCopy code
[code]
    register(api) {  // Required tool - always available  api.registerTool({    name: "my_tool",    description: "Do a thing",    parameters: Type.Object({ input: Type.String() }),    async execute(_id, params) {      return { content: [{ type: "text", text: params.input }] };    },  });   // Optional tool - user must add to allowlist  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

Tool-Factories erhalten ein vom Runtime bereitgestelltes Kontextobjekt. Verwenden Sie `ctx.activeModel`, wenn ein Tool das aktive Modell für den aktuellen Turn protokollieren, anzeigen oder sich daran anpassen muss. Das Objekt kann `provider`, `modelId` und `modelRef` enthalten. Behandeln Sie es als informative Runtime-Metadaten, nicht als Sicherheitsgrenze gegenüber dem lokalen Operator, installiertem Plugin-Code oder einer modifizierten OpenClaw-Runtime. Für sensible lokale Tools sollten Sie ein explizites Opt-in durch Plugin oder Operator beibehalten und geschlossen fehlschlagen, wenn die Metadaten des aktiven Modells fehlen oder ungeeignet sind.

Jedes mit `api.registerTool(...)` registrierte Tool muss auch im Plugin-Manifest deklariert werden:

jsonCopy code
[code]
    {  "contracts": {    "tools": ["my_tool", "workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

OpenClaw erfasst und cached den validierten Deskriptor aus dem registrierten Tool, sodass Plugins `description`\- oder Schemadaten im Manifest nicht duplizieren müssen. Der Manifest-Vertrag deklariert nur Ownership und Discovery; die Ausführung ruft weiterhin die live registrierte Tool-Implementierung auf. Setzen Sie `toolMetadata.<tool>.optional: true` für Tools, die mit `api.registerTool(..., { optional: true })` registriert wurden, damit OpenClaw das Laden dieser Plugin-Runtime vermeiden kann, bis das Tool ausdrücklich allowlisted wird.

Benutzer aktivieren optionale Tools in der Konfiguration:

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] },}
[/code]

  * Tool-Namen dürfen nicht mit Core-Tools kollidieren (Konflikte werden übersprungen)
  * Tools mit fehlerhaften Registrierungsobjekten, einschließlich fehlender `parameters`, werden übersprungen und in den Plugin-Diagnosen gemeldet, statt Agent-Läufe zu unterbrechen
  * Verwenden Sie `optional: true` für Tools mit Seiteneffekten oder zusätzlichen Binäranforderungen
  * Benutzer können alle Tools aus einem Plugin aktivieren, indem sie die Plugin-ID zu `tools.allow` hinzufügen


## CLI-Befehle registrieren

Plugins können Root-`openclaw`-Befehlsgruppen mit `api.registerCli` hinzufügen. Stellen Sie `descriptors` für jeden Top-Level-Befehlsroot bereit, damit OpenClaw den Befehl anzeigen und routen kann, ohne jede Plugin-Runtime vorab zu laden.

typescriptCopy code
[code]
    register(api) {  api.registerCli(    ({ program }) => {      const demo = program        .command("demo-plugin")        .description("Run demo plugin commands");       demo        .command("ping")        .description("Check that the plugin CLI is executable")        .action(() => {          console.log("demo-plugin:pong");        });    },    {      descriptors: [        {          name: "demo-plugin",          description: "Run demo plugin commands",          hasSubcommands: true,        },      ],    },  );}
[/code]

Prüfen Sie nach der Installation die Runtime-Registrierung und führen Sie den Befehl aus:

bashCopy code
[code]
    openclaw plugins inspect demo-plugin --runtime --jsonopenclaw demo-plugin ping
[/code]

## Import-Konventionen

Importieren Sie immer aus fokussierten `openclaw/plugin-sdk/<subpath>`-Pfaden:

typescriptCopy code
[code]
      // Wrong: monolithic root (deprecated, will be removed) 
[/code]

Die vollständige Subpath-Referenz finden Sie in der [SDK-Übersicht](</de/plugins/sdk-overview>).

Verwenden Sie innerhalb Ihres Plugins lokale Barrel-Dateien (`api.ts`, `runtime-api.ts`) für interne Importe - importieren Sie Ihr eigenes Plugin niemals über seinen SDK-Pfad.

Für Provider-Plugins sollten Provider-spezifische Helper in diesen Package-Root-Barrels bleiben, sofern die Schnittstelle nicht wirklich generisch ist. Aktuelle gebündelte Beispiele:

  * Anthropic: Claude-Stream-Wrapper und `service_tier`-/Beta-Helper
  * OpenAI: Provider-Builder, Default-Model-Helper, Realtime-Provider
  * OpenRouter: Provider-Builder plus Onboarding-/Konfigurations-Helper


Wenn ein Helper nur innerhalb eines gebündelten Provider-Pakets nützlich ist, belassen Sie ihn an dieser Package-Root-Schnittstelle, statt ihn nach `openclaw/plugin-sdk/*` zu befördern.

Einige generierte `openclaw/plugin-sdk/<bundled-id>`-Helper-Schnittstellen existieren weiterhin für die Wartung gebündelter Plugins, wenn sie nachverfolgte Owner-Nutzung haben. Behandeln Sie diese als reservierte Oberflächen, nicht als Standardmuster für neue Drittanbieter-Plugins.

## Checkliste vor der Einreichung

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **package.json** enthält korrekte `openclaw`-Metadaten OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **openclaw.plugin.json** -Manifest ist vorhanden und gültig OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Entry Point verwendet `defineChannelPluginEntry` oder `definePluginEntry` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Alle Importe verwenden fokussierte `plugin-sdk/<subpath>`-Pfade OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo