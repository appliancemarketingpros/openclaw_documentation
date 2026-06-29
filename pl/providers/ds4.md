---
title: ds4
source_url: https://docs.openclaw.ai/pl/providers/ds4
scraped_at: 2026-06-29
---

ModelsProviders

[ds4](<https://github.com/antirez/ds4>) udostępnia DeepSeek V4 Flash z lokalnego backendu Metal przez zgodne z OpenAI API `/v1`. OpenClaw łączy się z ds4 przez ogólną rodzinę dostawców `openai-completions`.

ds4 nie jest dołączonym pluginem dostawcy OpenClaw. Skonfiguruj go pod `models.providers.ds4`, a następnie wybierz `ds4/deepseek-v4-flash`.

  * Identyfikator dostawcy: `ds4`
  * Plugin: brak
  * API: zgodne z OpenAI Chat Completions (`openai-completions`)
  * Sugerowany bazowy adres URL: `http://127.0.0.1:18000/v1`
  * Identyfikator modelu: `deepseek-v4-flash`
  * Wywołania narzędzi: obsługiwane przez `tools` i `tool_calls` w stylu OpenAI
  * Rozumowanie: `thinking` i `reasoning_effort` w stylu DeepSeek


## Wymagania

  * macOS z obsługą Metal.
  * Działający checkout ds4 z `ds4-server` i plikiem GGUF DeepSeek V4 Flash.
  * Wystarczająca ilość pamięci dla wybranego kontekstu. Większe wartości `--ctx` alokują więcej pamięci KV podczas uruchamiania serwera.


## Szybki start

* ### Start ds4-server

Zastąp `&lt;DS4_DIR&gt;` ścieżką do swojego checkoutu ds4.

bashCopy code
[code]
    &lt;DS4_DIR&gt;/ds4-server \  --model &lt;DS4_DIR&gt;/ds4flash.gguf \  --host 127.0.0.1 \  --port 18000 \  --ctx 32768 \  --tokens 128
[/code]

* ### Verify the OpenAI-compatible endpoint

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

Odpowiedź powinna zawierać `deepseek-v4-flash`.

* ### Add the OpenClaw provider config

Dodaj konfigurację z sekcji Pełna konfiguracja, a następnie uruchom jednorazowe sprawdzenie modelu:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

## Pełna konfiguracja

Użyj tej konfiguracji, gdy ds4 działa już na `127.0.0.1:18000`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "ds4/deepseek-v4-flash" },      models: {        "ds4/deepseek-v4-flash": {          alias: "DS4 local",        },      },    },  },  models: {    mode: "merge",    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

Utrzymuj `contextWindow` zgodne z wartością `ds4-server --ctx`. Utrzymuj `maxTokens` zgodne z `--tokens`, chyba że celowo chcesz, aby OpenClaw żądał mniej danych wyjściowych niż domyślne ustawienie serwera.

## Uruchamianie na żądanie

OpenClaw może uruchamiać ds4 tylko wtedy, gdy wybrany jest model `ds4/...`. Dodaj `localService` do tego samego wpisu dostawcy:

json5Copy code
[code]
    {  models: {    providers: {      ds4: {        baseUrl: "http://127.0.0.1:18000/v1",        apiKey: "ds4-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "&lt;DS4_DIR&gt;/ds4-server",          args: [            "--model",            "&lt;DS4_DIR&gt;/ds4flash.gguf",            "--host",            "127.0.0.1",            "--port",            "18000",            "--ctx",            "32768",            "--tokens",            "128",          ],          cwd: "&lt;DS4_DIR&gt;",          healthUrl: "http://127.0.0.1:18000/v1/models",          readyTimeoutMs: 300000,          idleStopMs: 0,        },        models: [          {            id: "deepseek-v4-flash",            name: "DeepSeek V4 Flash (ds4)",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32768,            maxTokens: 128,            compat: {              supportsUsageInStreaming: true,              supportsReasoningEffort: true,              maxTokensField: "max_tokens",              supportsStrictMode: false,              thinkingFormat: "deepseek",              supportedReasoningEfforts: ["low", "medium", "high", "xhigh"],            },          },        ],      },    },  },}
[/code]

`command` musi być bezwzględną ścieżką do pliku wykonywalnego. Wyszukiwanie w powłoce i rozwijanie `~` nie są używane. Zobacz [Lokalne usługi modeli](</pl/gateway/local-model-services>), aby poznać każde pole `localService`.

## Think Max

ds4 stosuje Think Max tylko wtedy, gdy oba warunki są spełnione:

  * `ds4-server` uruchamia się z `--ctx 393216` lub wyższym.
  * Żądanie używa `reasoning_effort: "max"` albo równoważnego pola effort ds4.


Jeśli uruchamiasz tak duży kontekst, zaktualizuj zarówno flagi serwera, jak i metadane modelu OpenClaw:

json5Copy code
[code]
    {  contextWindow: 393216,  maxTokens: 384000,  compat: {    supportsUsageInStreaming: true,    supportsReasoningEffort: true,    maxTokensField: "max_tokens",    supportsStrictMode: false,    thinkingFormat: "deepseek",    supportedReasoningEfforts: ["low", "medium", "high", "xhigh", "max"],  },}
[/code]

## Test

Zacznij od bezpośredniego sprawdzenia HTTP:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"deepseek-v4-flash","messages":[{"role":"user","content":"Reply with exactly: ds4-ok"}],"max_tokens":16,"stream":false,"thinking":{"type":"disabled"}}'
[/code]

Następnie przetestuj routing modelu OpenClaw:

bashCopy code
[code]
    openclaw infer model run \  --local \  --model ds4/deepseek-v4-flash \  --thinking off \  --prompt "Reply with exactly: openclaw-ds4-ok" \  --json
[/code]

Dla pełnego smoke testu agenta i wywołania narzędzia użyj kontekstu co najmniej 32768:

bashCopy code
[code]
    openclaw agent \  --local \  --session-id ds4-tool-smoke \  --model ds4/deepseek-v4-flash \  --thinking off \  --message "Use the shell command pwd once, then reply exactly: tool-ok <output>" \  --json \  --timeout 240
[/code]

Oczekiwany wynik:

  * `executionTrace.winnerProvider` to `ds4`
  * `executionTrace.winnerModel` to `deepseek-v4-flash`
  * `toolSummary.calls` wynosi co najmniej `1`
  * `finalAssistantVisibleText` zaczyna się od `tool-ok`


## Rozwiązywanie problemów

curl /v1/models cannot connect

ds4 nie działa albo nie jest przypisany do hosta i portu w `baseUrl`. Uruchom `ds4-server`, a następnie spróbuj ponownie:

bashCopy code
[code]
    curl http://127.0.0.1:18000/v1/models
[/code]

500 prompt exceeds context

Skonfigurowane `--ctx` jest zbyt małe dla tury OpenClaw. Zwiększ `ds4-server --ctx`, a następnie zaktualizuj `models.providers.ds4.models[].contextWindow`, aby pasowało. Pełne tury agenta z narzędziami potrzebują znacznie więcej kontekstu niż bezpośrednie jednowiadomościowe żądanie curl.

Think Max does not activate

ds4 używa Think Max tylko wtedy, gdy `--ctx` wynosi co najmniej `393216`, a żądanie prosi o `reasoning_effort: "max"`. Mniejsze konteksty wracają do wysokiego poziomu rozumowania.

The first request is slow

ds4 ma zimną fazę rezydencji Metal i rozgrzewania modelu. Użyj `localService.readyTimeoutMs: 300000`, gdy OpenClaw uruchamia serwer na żądanie.

## Powiązane

[**Local model services** Uruchamiaj lokalne serwery modeli na żądanie przed żądaniami modeli. ](</pl/gateway/local-model-services>) [**Local models** Wybieraj i obsługuj lokalne backendy modeli. ](</pl/gateway/local-models>) [**Model providers** Skonfiguruj referencje dostawców, uwierzytelnianie i przełączanie awaryjne. ](</pl/concepts/model-providers>) [**DeepSeek** Natywne zachowanie dostawcy DeepSeek i kontrolki myślenia. ](</pl/providers/deepseek>)

Was this useful?YesNo

Open issue