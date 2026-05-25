---
title: Tworzenie pluginów backendu CLI
source_url: https://docs.openclaw.ai/pl/plugins/cli-backend-plugins
scraped_at: 2026-05-25
---

CLI backend plugins pozwalają OpenClaw wywoływać lokalne AI CLI jako backend wnioskowania tekstowego. Backend pojawia się jako prefiks dostawcy w referencjach modeli:

textCopy code
[code]
    acme-cli/acme-large
[/code]

Użyj backendu CLI, gdy integracja upstream jest już udostępniona jako lokalne polecenie, gdy CLI zarządza lokalnym stanem logowania albo gdy CLI jest użytecznym rozwiązaniem awaryjnym, jeśli dostawcy API są niedostępni.

## Za co odpowiada plugin

Plugin backendu CLI ma trzy kontrakty:

Kontrakt | Plik | Cel  
---|---|---  
Wejście pakietu | `package.json` | Wskazuje OpenClaw moduł runtime pluginu  
Własność manifestu | `openclaw.plugin.json` | Deklaruje identyfikator backendu przed załadowaniem runtime  
Rejestracja runtime | `index.ts` | Wywołuje `api.registerCliBackend(...)` z domyślnymi poleceniami  
  
Manifest to metadane wykrywania. Nie wykonuje CLI ani nie rejestruje zachowania runtime. Zachowanie runtime zaczyna się, gdy punkt wejścia pluginu wywoła `api.registerCliBackend(...)`.

## Minimalny plugin backendu

* ### Utwórz metadane pakietu

package.jsonCopy code
[code]
    {  "name": "@acme/openclaw-acme-cli",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  },  "dependencies": {    "openclaw": "^2026.3.24"  },  "devDependencies": {    "typescript": "^5.9.0"  }}
[/code]

Opublikowane pakiety muszą zawierać zbudowane pliki runtime JavaScript. Jeśli wpis źródłowy to `./src/index.ts`, dodaj `openclaw.runtimeExtensions`, które wskazuje zbudowany odpowiednik JavaScript. Zobacz [Punkty wejścia](</pl/plugins/sdk-entrypoints>).

* ### Zadeklaruj własność backendu

openclaw.plugin.jsonCopy code
[code]
    {  "id": "acme-cli",  "name": "Acme CLI",  "description": "Run Acme's local AI CLI through OpenClaw",  "cliBackends": ["acme-cli"],  "setup": {    "cliBackends": ["acme-cli"],    "requiresRuntime": false  },  "activation": {    "onStartup": false  },  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

`cliBackends` to lista własności runtime. Pozwala OpenClaw automatycznie ładować plugin, gdy konfiguracja lub wybór modelu wspomina `acme-cli/...`.

`setup.cliBackends` to powierzchnia konfiguracji oparta najpierw na deskryptorze. Dodaj ją, gdy wykrywanie modeli, onboarding lub status powinny rozpoznawać backend bez ładowania runtime pluginu. Używaj `requiresRuntime: false` tylko wtedy, gdy te statyczne deskryptory wystarczają do konfiguracji.

* ### Zarejestruj backend

index.tsCopy code
[code]
    import { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import {  CLI_FRESH_WATCHDOG_DEFAULTS,  CLI_RESUME_WATCHDOG_DEFAULTS,  type CliBackendPlugin,} from "openclaw/plugin-sdk/cli-backend"; function buildAcmeCliBackend(): CliBackendPlugin {  return {    id: "acme-cli",    liveTest: {      defaultModelRef: "acme-cli/acme-large",      defaultImageProbe: false,      defaultMcpProbe: false,      docker: {        npmPackage: "@acme/acme-cli",        binaryName: "acme",      },    },    config: {      command: "acme",      args: ["chat", "--json"],      output: "json",      input: "stdin",      modelArg: "--model",      sessionArg: "--session",      sessionMode: "existing",      sessionIdFields: ["session_id", "conversation_id"],      systemPromptFileArg: "--system-file",      systemPromptWhen: "first",      imageArg: "--image",      imageMode: "repeat",      reliability: {        watchdog: {          fresh: { ...CLI_FRESH_WATCHDOG_DEFAULTS },          resume: { ...CLI_RESUME_WATCHDOG_DEFAULTS },        },      },      serialize: true,    },  };} export default definePluginEntry({  id: "acme-cli",  name: "Acme CLI",  description: "Run Acme's local AI CLI through OpenClaw",  register(api) {    api.registerCliBackend(buildAcmeCliBackend());  },});
[/code]

Identyfikator backendu musi pasować do wpisu `cliBackends` w manifeście. Zarejestrowana `config` jest tylko wartością domyślną; konfiguracja użytkownika pod `agents.defaults.cliBackends.acme-cli` jest nakładana na nią w runtime.

## Kształt konfiguracji

`CliBackendConfig` opisuje, jak OpenClaw ma uruchamiać i analizować CLI:

Pole | Zastosowanie  
---|---  
`command` | Nazwa binarna lub bezwzględna ścieżka polecenia  
`args` | Bazowe argv dla nowych uruchomień  
`resumeArgs` | Alternatywne argv dla wznawianych sesji; obsługuje `{sessionId}`  
`output` / `resumeOutput` | Parser: `json`, `jsonl` lub `text`  
`input` | Transport promptu: `arg` lub `stdin`  
`modelArg` | Flaga używana przed identyfikatorem modelu  
`modelAliases` | Mapuje identyfikatory modeli OpenClaw na natywne identyfikatory CLI  
`sessionArg` / `sessionArgs` | Jak przekazać identyfikator sesji  
`sessionMode` | `always`, `existing` lub `none`  
`sessionIdFields` | Pola JSON, które OpenClaw odczytuje z wyjścia CLI  
`systemPromptArg` / `systemPromptFileArg` | Transport promptu systemowego  
`systemPromptWhen` | `first`, `always` lub `never`  
`imageArg` / `imageMode` | Obsługa ścieżek obrazów  
`serialize` | Utrzymuje uporządkowanie uruchomień tego samego backendu  
`reliability.watchdog` | Dostrajanie limitu czasu bez wyjścia  
  
Preferuj najmniejszą statyczną konfigurację, która pasuje do CLI. Dodawaj callbacki pluginu tylko dla zachowania, które rzeczywiście należy do backendu.

## Zaawansowane hooki backendu

`CliBackendPlugin` może również definiować:

Hook | Zastosowanie  
---|---  
`normalizeConfig(config, context)` | Przepisuje starszą konfigurację użytkownika po scaleniu  
`resolveExecutionArgs(ctx)` | Dodaje flagi zakresu żądania, takie jak wysiłek myślenia  
`prepareExecution(ctx)` | Tworzy tymczasowe mosty uwierzytelniania lub konfiguracji przed uruchomieniem  
`transformSystemPrompt(ctx)` | Stosuje końcową transformację promptu systemowego specyficzną dla CLI  
`textTransforms` | Dwukierunkowe zamiany promptu/wyjścia  
`defaultAuthProfileId` | Preferuje określony profil uwierzytelniania OpenClaw  
`authEpochMode` | Decyduje, jak zmiany uwierzytelniania unieważniają zapisane sesje CLI  
`nativeToolMode` | Deklaruje, czy CLI ma zawsze włączone narzędzia natywne  
`bundleMcp` / `bundleMcpMode` | Włącza most narzędzi MCP loopback OpenClaw  
  
Te hooki powinny pozostawać własnością dostawcy. Nie dodawaj gałęzi specyficznych dla CLI do rdzenia, gdy hook backendu może wyrazić dane zachowanie.

## Most narzędzi MCP

Backendy CLI domyślnie nie otrzymują narzędzi OpenClaw. Jeśli CLI potrafi użyć konfiguracji MCP, włącz to jawnie:

typescriptCopy code
[code]
    return {  id: "acme-cli",  bundleMcp: true,  bundleMcpMode: "codex-config-overrides",  config: {    command: "acme",    args: ["chat", "--json"],    output: "json",  },};
[/code]

Obsługiwane tryby mostu to:

Tryb | Zastosowanie  
---|---  
`claude-config-file` | CLI, które akceptują plik konfiguracji MCP  
`codex-config-overrides` | CLI, które akceptują nadpisania konfiguracji w argv  
`gemini-system-settings` | CLI, które odczytują ustawienia MCP z katalogu ustawień systemowych  
  
Włączaj most tylko wtedy, gdy CLI rzeczywiście potrafi go użyć. Jeśli CLI ma własną wbudowaną warstwę narzędzi, której nie można wyłączyć, ustaw `nativeToolMode: "always-on"`, aby OpenClaw mógł bezpiecznie odmówić, gdy wywołujący wymaga braku narzędzi natywnych.

## Konfiguracja użytkownika

Użytkownicy mogą nadpisać dowolną wartość domyślną backendu:

json5Copy code
[code]
    {  agents: {    defaults: {      cliBackends: {        "acme-cli": {          command: "/opt/acme/bin/acme",          args: ["chat", "--json", "--profile", "work"],          modelAliases: {            large: "acme-large-2026",          },        },      },      model: {        primary: "openai/gpt-5.5",        fallbacks: ["acme-cli/large"],      },    },  },}
[/code]

Udokumentuj minimalne nadpisanie, którego użytkownicy prawdopodobnie będą potrzebować. Zwykle jest to tylko `command`, gdy plik binarny znajduje się poza `PATH`.

## Weryfikacja

Dla dołączonych pluginów dodaj ukierunkowany test wokół buildera i rejestracji konfiguracji, a następnie uruchom ukierunkowaną ścieżkę testową pluginu:

bashCopy code
[code]
    pnpm test extensions/acme-cli
[/code]

Dla lokalnych lub zainstalowanych pluginów zweryfikuj wykrywanie i jedno rzeczywiste uruchomienie modelu:

bashCopy code
[code]
    openclaw plugins inspect acme-cli --runtime --jsonopenclaw agent --message "reply exactly: backend ok" --model acme-cli/acme-large
[/code]

Jeśli backend obsługuje obrazy lub MCP, dodaj live smoke potwierdzający te ścieżki z rzeczywistym CLI. Nie polegaj na statycznej inspekcji dla zachowania promptu, obrazu, MCP ani wznawiania sesji.

## Lista kontrolna

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `package.json` ma `openclaw.extensions` i zbudowane wpisy runtime dla opublikowanych pakietów OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `openclaw.plugin.json` deklaruje `cliBackends` i zamierzone `activation.onStartup` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `setup.cliBackends` jest obecne, gdy konfiguracja/wykrywanie modeli powinny widzieć backend na zimno OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s `api.registerCliBackend(...)` używa tego samego identyfikatora backendu co manifest OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Nadpisania użytkownika pod `agents.defaults.cliBackends.<id>` nadal mają pierwszeństwo OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo