---
title: ds4
source_url: https://docs.openclaw.ai/nl/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) serveert DeepSeek V4 Flash vanuit een lokale Metal-backend met een OpenAI-compatibele `/v1`-API. OpenClaw maakt verbinding met ds4 via de generieke `openai-completions`-providerfamilie.

ds4 is geen gebundelde OpenClaw-provider-Plugin. Configureer het onder `models.providers.ds4` en selecteer daarna `ds4/deepseek-v4-flash`.

  * Provider-id: `ds4`
  * Plugin: geen
  * API: OpenAI-compatibele Chat Completions (`openai-completions`)
  * Voorgestelde basis-URL: `http://127.0.0.1:18000/v1`
  * Model-id: `deepseek-v4-flash`
  * Toolaanroepen: ondersteund via OpenAI-stijl `tools` en `tool_calls`
  * Redeneren: DeepSeek-stijl `thinking` en `reasoning_effort`


## Vereisten

  * macOS met Metal-ondersteuning.
  * Een werkende ds4-checkout met `ds4-server` en het DeepSeek V4 Flash GGUF-bestand.
  * Genoeg geheugen voor de context die je kiest. Grotere `--ctx`-waarden wijzen meer KV-geheugen toe wanneer de server start.


## Snelstart

* ### Start ds4-server

Vervang `&lt;DS4_DIR&gt;` door het pad naar je ds4-checkout.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### Controleer het OpenAI-compatibele endpoint

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

Het antwoord moet `deepseek-v4-flash` bevatten.

* ### Voeg de OpenClaw-providerconfiguratie toe

Voeg de configuratie uit Volledige configuratie toe en voer daarna een eenmalige modelcontrole uit:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## Volledige configuratie

Gebruik deze configuratie wanneer ds4 al draait op `127.0.0.1:18000`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

Houd `contextWindow` afgestemd op de waarde van `ds4-server --ctx`. Houd `maxTokens` afgestemd op `--tokens`, tenzij je OpenClaw bewust minder uitvoer wilt laten aanvragen dan de serverstandaard.

## Opstarten op aanvraag

OpenClaw kan ds4 alleen starten wanneer een `ds4/...`-model is geselecteerd. Voeg `localService` toe aan dezelfde providervermelding:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` moet een absoluut pad naar een uitvoerbaar bestand zijn. Shell-lookup en `~`-uitbreiding worden niet gebruikt. Zie [Lokale modelservices](</nl/gateway/local-model-services>) voor elk `localService`-veld.

## Think Max

ds4 past Think Max alleen toe wanneer aan beide voorwaarden is voldaan:

  * `ds4-server` start met `--ctx 393216` of hoger.
  * De aanvraag gebruikt `reasoning_effort: "max"` of het equivalente ds4-effortveld.


Als je die grote context gebruikt, werk dan zowel de serverflags als de OpenClaw-modelmetadata bij:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## Testen

Begin met een directe HTTP-controle:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

Test daarna OpenClaw-modelroutering:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

Gebruik voor een volledige agent- en toolaanroep-smoketest een context van minstens 32768:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

Verwacht resultaat:

  * `executionTrace.winnerProvider` is `ds4`
  * `executionTrace.winnerModel` is `deepseek-v4-flash`
  * `toolSummary.calls` is minstens `1`
  * `finalAssistantVisibleText` begint met `tool-ok`


## Probleemoplossing

curl /v1/models kan geen verbinding maken

ds4 draait niet of is niet gebonden aan de host en poort in `baseUrl`. Start `ds4-server` en probeer het daarna opnieuw:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

De geconfigureerde `--ctx` is te klein voor de OpenClaw-beurt. Verhoog `ds4-server --ctx` en werk daarna `models.providers.ds4.models[].contextWindow` bij zodat deze overeenkomt. Volledige agentbeurten met tools hebben aanzienlijk meer context nodig dan een directe curl-aanvraag met één bericht.

Think Max wordt niet geactiveerd

ds4 gebruikt Think Max alleen wanneer `--ctx` minstens `393216` is en de aanvraag vraagt om `reasoning_effort: "max"`. Kleinere contexten vallen terug op hoog redeneren.

De eerste aanvraag is traag

ds4 heeft een koude Metal-residentie en een opwarmfase voor het model. Gebruik `localService.readyTimeoutMs: 300000` wanneer OpenClaw de server op aanvraag start.

## Gerelateerd

[**Lokale modelservices** Start lokale modelservers op aanvraag voordat modelaanvragen worden gedaan. ](</nl/gateway/local-model-services>) [**Lokale modellen** Kies en beheer lokale modelbackends. ](</nl/gateway/local-models>) [**Modelproviders** Configureer providerrefs, auth en failover. ](</nl/concepts/model-providers>) [**DeepSeek** Native DeepSeek-providergedrag en thinking-instellingen. ](</nl/providers/deepseek>)

Was this useful?YesNo

Open issue