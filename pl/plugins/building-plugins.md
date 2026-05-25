---
title: Tworzenie Pluginów
source_url: https://docs.openclaw.ai/pl/plugins/building-plugins
scraped_at: 2026-05-25
---

Pluginy rozszerzają OpenClaw o nowe możliwości: kanały, dostawców modeli, mowę, transkrypcję w czasie rzeczywistym, głos w czasie rzeczywistym, rozumienie mediów, generowanie obrazów, generowanie wideo, pobieranie z sieci, wyszukiwanie w sieci, narzędzia agenta lub dowolne połączenie tych funkcji.

Nie musisz dodawać swojego pluginu do repozytorium OpenClaw. Opublikuj go w [ClawHub](</pl/clawhub>), a użytkownicy zainstalują go poleceniem `openclaw plugins install clawhub:<package-name>`. Podczas przejścia uruchomieniowego gołe specyfikacje pakietów nadal instalują się z npm.

## Wymagania wstępne

  * Node >= 22 i menedżer pakietów (npm lub pnpm)
  * Znajomość TypeScript (ESM)
  * W przypadku pluginów w repozytorium: sklonowane repozytorium i wykonane `pnpm install`. Rozwój pluginów z checkoutu źródeł obsługuje wyłącznie pnpm, ponieważ OpenClaw ładuje dołączone pluginy z pakietów workspace `extensions/*`.


## Jaki rodzaj pluginu?

[**Plugin kanału** Połącz OpenClaw z platformą komunikacyjną (Discord, IRC itd.) ](</pl/plugins/sdk-channel-plugins>) [**Plugin dostawcy** Dodaj dostawcę modelu (LLM, proxy lub niestandardowy punkt końcowy) ](</pl/plugins/sdk-provider-plugins>) [**Plugin backendu CLI** Zamapuj lokalne AI CLI do tekstowego runnera awaryjnego OpenClaw ](</pl/plugins/cli-backend-plugins>) [**Plugin narzędzi / hooków** Zarejestruj narzędzia agenta, hooki zdarzeń lub usługi - kontynuuj poniżej ](</pl/plugins/hooks>)

W przypadku pluginu kanału, który nie musi być zainstalowany, gdy uruchamia się onboarding/konfiguracja, użyj `createOptionalChannelSetupSurface(...)` z `openclaw/plugin-sdk/channel-setup`. Tworzy parę adaptera konfiguracji i kreatora, która informuje o wymaganiu instalacji i bezpiecznie odmawia rzeczywistych zapisów konfiguracji, dopóki plugin nie zostanie zainstalowany.

## Szybki start: plugin narzędziowy

Ten przewodnik tworzy minimalny plugin, który rejestruje narzędzie agenta. Pluginy kanałów i dostawców mają osobne przewodniki podlinkowane powyżej.

* ### Utwórz pakiet i manifest

package.jsonCopy code
[code]
    {"name": "@myorg/openclaw-my-plugin","version": "1.0.0","type": "module","openclaw": {  "extensions": ["./index.ts"],  "compat": {    "pluginApi": ">=2026.3.24-beta.2",    "minGatewayVersion": "2026.3.24-beta.2"  },  "build": {    "openclawVersion": "2026.3.24-beta.2",    "pluginSdkVersion": "2026.3.24-beta.2"  }}}
[/code]

openclaw.plugin.jsonCopy code
[code]
    {"id": "my-plugin","name": "My Plugin","description": "Adds a custom tool to OpenClaw","contracts": {  "tools": ["my_tool"]},"activation": {  "onStartup": true},"configSchema": {  "type": "object",  "additionalProperties": false}}
[/code]

Każdy plugin potrzebuje manifestu, nawet bez konfiguracji. Narzędzia rejestrowane w runtime muszą być wymienione w `contracts.tools`, aby OpenClaw mógł wykryć plugin właścicielski bez ładowania runtime każdego pluginu. Pluginy powinny też świadomie deklarować `activation.onStartup`. Ten przykład ustawia ją na `true`. Pełny schemat znajdziesz w [Manifest](</pl/plugins/manifest>). Kanoniczne fragmenty publikowania w ClawHub znajdują się w `docs/snippets/plugin-publish/`.

* ### Napisz punkt wejścia

typescriptCopy code
[code]
    // index.tsimport { definePluginEntry } from "openclaw/plugin-sdk/plugin-entry";import { Type } from "@sinclair/typebox"; export default definePluginEntry({  id: "my-plugin",  name: "My Plugin",  description: "Adds a custom tool to OpenClaw",  register(api) {    api.registerTool({      name: "my_tool",      description: "Do a thing",      parameters: Type.Object({ input: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: `Got: ${params.input}` }] };      },    });  },});
[/code]

`definePluginEntry` służy do pluginów innych niż kanały. W przypadku kanałów użyj `defineChannelPluginEntry` \- zobacz [Pluginy kanałów](</pl/plugins/sdk-channel-plugins>). Pełne opcje punktu wejścia znajdziesz w [Punkty wejścia](</pl/plugins/sdk-entrypoints>).

* ### Przetestuj i opublikuj

**Pluginy zewnętrzne:** zweryfikuj i opublikuj z ClawHub, a następnie zainstaluj:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-pluginopenclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

Gołe specyfikacje pakietów, takie jak `@myorg/openclaw-my-plugin`, instalują się z npm podczas przejścia uruchomieniowego. Użyj `clawhub:`, gdy chcesz rozwiązywania przez ClawHub.

**Pluginy w repozytorium:** umieść pod drzewem workspace dołączonych pluginów - zostaną wykryte automatycznie.

bashCopy code
[code]
    pnpm test -- <bundled-plugin-root>/my-plugin/
[/code]

## Możliwości pluginów

Pojedynczy plugin może zarejestrować dowolną liczbę możliwości przez obiekt `api`:

Możliwość | Metoda rejestracji | Szczegółowy przewodnik  
---|---|---  
Wnioskowanie tekstowe (LLM) | `api.registerProvider(...)` | [Pluginy dostawców](</pl/plugins/sdk-provider-plugins>)  
Backend wnioskowania CLI | `api.registerCliBackend(...)` | [Pluginy backendu CLI](</pl/plugins/cli-backend-plugins>)  
Kanał / komunikacja | `api.registerChannel(...)` | [Pluginy kanałów](</pl/plugins/sdk-channel-plugins>)  
Mowa (TTS/STT) | `api.registerSpeechProvider(...)` | [Pluginy dostawców](</pl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Transkrypcja w czasie rzeczywistym | `api.registerRealtimeTranscriptionProvider(...)` | [Pluginy dostawców](</pl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Głos w czasie rzeczywistym | `api.registerRealtimeVoiceProvider(...)` | [Pluginy dostawców](</pl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Rozumienie mediów | `api.registerMediaUnderstandingProvider(...)` | [Pluginy dostawców](</pl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Generowanie obrazów | `api.registerImageGenerationProvider(...)` | [Pluginy dostawców](</pl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Generowanie muzyki | `api.registerMusicGenerationProvider(...)` | [Pluginy dostawców](</pl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Generowanie wideo | `api.registerVideoGenerationProvider(...)` | [Pluginy dostawców](</pl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Pobieranie z sieci | `api.registerWebFetchProvider(...)` | [Pluginy dostawców](</pl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Wyszukiwanie w sieci | `api.registerWebSearchProvider(...)` | [Pluginy dostawców](</pl/plugins/sdk-provider-plugins#step-5-add-extra-capabilities>)  
Middleware wyników narzędzi | `api.registerAgentToolResultMiddleware(...)` | [Omówienie SDK](</pl/plugins/sdk-overview#registration-api>)  
Narzędzia agenta | `api.registerTool(...)` | Poniżej  
Niestandardowe polecenia | `api.registerCommand(...)` | [Punkty wejścia](</pl/plugins/sdk-entrypoints>)  
Hooki pluginów | `api.on(...)` | [Hooki pluginów](</pl/plugins/hooks>)  
Wewnętrzne hooki zdarzeń | `api.registerHook(...)` | [Punkty wejścia](</pl/plugins/sdk-entrypoints>)  
Trasy HTTP | `api.registerHttpRoute(...)` | [Internals](</pl/plugins/architecture-internals#gateway-http-routes>)  
Podpolecenia CLI | `api.registerCli(...)` | [Punkty wejścia](</pl/plugins/sdk-entrypoints>)  
  
Pełne API rejestracji znajdziesz w [Omówienie SDK](</pl/plugins/sdk-overview#registration-api>).

Dołączone pluginy mogą używać `api.registerAgentToolResultMiddleware(...)`, gdy potrzebują asynchronicznego przepisywania wyniku narzędzia, zanim model zobaczy dane wyjściowe. Zadeklaruj docelowe runtime w `contracts.agentToolResultMiddleware`, na przykład `["pi", "codex"]`. To zaufany interfejs dla dołączonych pluginów; zewnętrzne pluginy powinny preferować zwykłe hooki pluginów OpenClaw, chyba że OpenClaw wprowadzi jawną politykę zaufania dla tej możliwości.

Jeśli Twój plugin rejestruje niestandardowe metody RPC Gateway, trzymaj je pod prefiksem specyficznym dla pluginu. Przestrzenie nazw administracyjnych core (`config.*`, `exec.approvals.*`, `wizard.*`, `update.*`) pozostają zarezerwowane i zawsze rozwiązują się do `operator.admin`, nawet jeśli plugin zażąda węższego zakresu.

Semantyka guardów hooków, o której warto pamiętać:

  * `before_tool_call`: `{ block: true }` jest końcowe i zatrzymuje handlery o niższym priorytecie.
  * `before_tool_call`: `{ block: false }` jest traktowane jako brak decyzji.
  * `before_tool_call`: `{ requireApproval: true }` wstrzymuje wykonanie agenta i prosi użytkownika o zatwierdzenie przez nakładkę zatwierdzania exec, przyciski Telegram, interakcje Discord lub polecenie `/approve` w dowolnym kanale.
  * `before_install`: `{ block: true }` jest końcowe i zatrzymuje handlery o niższym priorytecie.
  * `before_install`: `{ block: false }` jest traktowane jako brak decyzji.
  * `message_sending`: `{ cancel: true }` jest końcowe i zatrzymuje handlery o niższym priorytecie.
  * `message_sending`: `{ cancel: false }` jest traktowane jako brak decyzji.
  * `message_received`: preferuj typowane pole `threadId`, gdy potrzebujesz routingu wątków/tematów przychodzących. Zachowaj `metadata` dla dodatków specyficznych dla kanału.
  * `message_sending`: preferuj typowane pola routingu `replyToId` / `threadId` zamiast kluczy metadanych specyficznych dla kanału.


Polecenie `/approve` obsługuje zarówno zatwierdzenia exec, jak i pluginów z ograniczonym fallbackiem: gdy identyfikator zatwierdzenia exec nie zostanie znaleziony, OpenClaw ponawia próbę użycia tego samego identyfikatora przez zatwierdzenia pluginów. Przekazywanie zatwierdzeń pluginów można skonfigurować niezależnie przez `approvals.plugin` w konfiguracji.

Jeśli niestandardowe mechanizmy zatwierdzania muszą wykryć ten sam przypadek ograniczonego fallbacku, preferuj `isApprovalNotFoundError` z `openclaw/plugin-sdk/error-runtime` zamiast ręcznego dopasowywania ciągów wygaśnięcia zatwierdzenia.

Przykłady i referencję hooków znajdziesz w [Hooki pluginów](</pl/plugins/hooks>).

## Rejestrowanie narzędzi agenta

Narzędzia to typowane funkcje, które LLM może wywoływać. Mogą być wymagane (zawsze dostępne) lub opcjonalne (włączane przez użytkownika):

typescriptCopy code
[code]
    register(api) {  // Required tool - always available  api.registerTool({    name: "my_tool",    description: "Do a thing",    parameters: Type.Object({ input: Type.String() }),    async execute(_id, params) {      return { content: [{ type: "text", text: params.input }] };    },  });   // Optional tool - user must add to allowlist  api.registerTool(    {      name: "workflow_tool",      description: "Run a workflow",      parameters: Type.Object({ pipeline: Type.String() }),      async execute(_id, params) {        return { content: [{ type: "text", text: params.pipeline }] };      },    },    { optional: true },  );}
[/code]

Fabryki narzędzi otrzymują obiekt kontekstu dostarczany przez runtime. Używaj `ctx.activeModel`, gdy narzędzie musi rejestrować, wyświetlać lub dostosowywać się do aktywnego modelu dla bieżącej tury. Obiekt może zawierać `provider`, `modelId` i `modelRef`. Traktuj go jako informacyjne metadane runtime, a nie jako granicę bezpieczeństwa wobec lokalnego operatora, zainstalowanego kodu Pluginu lub zmodyfikowanego runtime OpenClaw. W przypadku wrażliwych narzędzi lokalnych zachowaj jawne wymaganie zgody Pluginu lub operatora i odmawiaj działania, gdy metadane aktywnego modelu są brakujące albo nieodpowiednie.

Każde narzędzie zarejestrowane przez `api.registerTool(...)` musi być także zadeklarowane w manifeście Pluginu:

jsonCopy code
[code]
    {  "contracts": {    "tools": ["my_tool", "workflow_tool"]  },  "toolMetadata": {    "workflow_tool": {      "optional": true    }  }}
[/code]

OpenClaw przechwytuje i buforuje zweryfikowany deskryptor z zarejestrowanego narzędzia, więc Pluginy nie duplikują `description` ani danych schematu w manifeście. Kontrakt manifestu deklaruje tylko własność i wykrywanie; wykonanie nadal wywołuje aktywną implementację zarejestrowanego narzędzia. Ustaw `toolMetadata.<tool>.optional: true` dla narzędzi zarejestrowanych za pomocą `api.registerTool(..., { optional: true })`, aby OpenClaw mógł uniknąć ładowania tego runtime Pluginu, dopóki narzędzie nie zostanie jawnie dodane do listy dozwolonych.

Użytkownicy włączają opcjonalne narzędzia w konfiguracji:

json5Copy code
[code]
    {  tools: { allow: ["workflow_tool"] },}
[/code]

  * Nazwy narzędzi nie mogą kolidować z narzędziami rdzenia (konflikty są pomijane)
  * Narzędzia z nieprawidłowymi obiektami rejestracji, w tym bez `parameters`, są pomijane i zgłaszane w diagnostyce Pluginu zamiast przerywać uruchomienia agenta
  * Używaj `optional: true` dla narzędzi z efektami ubocznymi lub dodatkowymi wymaganiami binarnymi
  * Użytkownicy mogą włączyć wszystkie narzędzia z Pluginu, dodając identyfikator Pluginu do `tools.allow`


## Rejestrowanie poleceń CLI

Pluginy mogą dodawać główne grupy poleceń `openclaw` za pomocą `api.registerCli`. Podaj `descriptors` dla każdego najwyższego poziomu korzenia polecenia, aby OpenClaw mógł wyświetlić i przekierować polecenie bez zachłannego ładowania każdego runtime Pluginu.

typescriptCopy code
[code]
    register(api) {  api.registerCli(    ({ program }) => {      const demo = program        .command("demo-plugin")        .description("Run demo plugin commands");       demo        .command("ping")        .description("Check that the plugin CLI is executable")        .action(() => {          console.log("demo-plugin:pong");        });    },    {      descriptors: [        {          name: "demo-plugin",          description: "Run demo plugin commands",          hasSubcommands: true,        },      ],    },  );}
[/code]

Po instalacji zweryfikuj rejestrację runtime i wykonaj polecenie:

bashCopy code
[code]
    openclaw plugins inspect demo-plugin --runtime --jsonopenclaw demo-plugin ping
[/code]

## Konwencje importu

Zawsze importuj ze skoncentrowanych ścieżek `openclaw/plugin-sdk/<subpath>`:

typescriptCopy code
[code]
      // Wrong: monolithic root (deprecated, will be removed) 
[/code]

Pełną referencję podścieżek znajdziesz w [Przeglądzie SDK](</pl/plugins/sdk-overview>).

W obrębie swojego Pluginu używaj lokalnych plików baryłkowych (`api.ts`, `runtime-api.ts`) do importów wewnętrznych - nigdy nie importuj własnego Pluginu przez jego ścieżkę SDK.

W przypadku Pluginów dostawców trzymaj helpery specyficzne dla dostawcy w tych baryłkach katalogu głównego pakietu, chyba że granica jest naprawdę generyczna. Obecne dołączone przykłady:

  * Anthropic: wrappery strumienia Claude oraz helpery `service_tier` / beta
  * OpenAI: konstruktory dostawcy, helpery modeli domyślnych, dostawcy realtime
  * OpenRouter: konstruktor dostawcy oraz helpery onboardingu/konfiguracji


Jeśli helper jest użyteczny tylko wewnątrz jednego dołączonego pakietu dostawcy, zostaw go na tej granicy katalogu głównego pakietu zamiast promować go do `openclaw/plugin-sdk/*`.

Niektóre wygenerowane granice helperów `openclaw/plugin-sdk/<bundled-id>` nadal istnieją na potrzeby utrzymania dołączonych Pluginów, gdy mają śledzone użycie właściciela. Traktuj je jako powierzchnie zarezerwowane, a nie jako domyślny wzorzec dla nowych Pluginów firm trzecich.

## Lista kontrolna przed zgłoszeniem

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s **package.json** ma poprawne metadane `openclaw` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Manifest **openclaw.plugin.json** jest obecny i prawidłowy OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Punkt wejścia używa `defineChannelPluginEntry` lub `definePluginEntry` OPENCLAW_DOCS_MARKER:calloutClose:

OPENCLAW_DOCS_MARKER:calloutOpen:Q2hlY2s Wszystkie importy używają skoncentrowanych ścieżek `plugin-sdk/<subpath>` OPENCLAW_DOCS_MARKER:calloutClose:

Was this useful?YesNo