---
title: Wnioskuje
source_url: https://docs.openclaw.ai/pl/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) może udostępniać modele lokalne za API `/v1` zgodnym z OpenAI. OpenClaw współpracuje z `inferrs` przez ogólną ścieżkę `openai-completions`.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `inferrs` (niestandardowy; skonfiguruj w `models.providers.inferrs`)  
Plugin | brak — `inferrs` nie jest dołączonym pluginem dostawcy OpenClaw  
Zmienna środowiskowa uwierzytelniania | Opcjonalna. Dowolna wartość działa, jeśli Twój serwer inferrs nie ma uwierzytelniania  
API | Zgodne z OpenAI (`openai-completions`)  
Sugerowany bazowy URL | `http://127.0.0.1:8080/v1` (lub tam, gdzie działa Twój serwer inferrs)  
  
## Pierwsze kroki

* ### Uruchom inferrs z modelem

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### Sprawdź, czy serwer jest osiągalny

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### Dodaj wpis dostawcy OpenClaw

Dodaj jawny wpis dostawcy i skieruj na niego domyślny model. Zobacz pełny przykład konfiguracji poniżej.

## Pełny przykład konfiguracji

Ten przykład używa Gemma 4 na lokalnym serwerze `inferrs`.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## Uruchamianie na żądanie

Inferrs może być też uruchamiany przez OpenClaw tylko wtedy, gdy zostanie wybrany model `inferrs/...`. Dodaj `localService` do tego samego wpisu dostawcy:

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` musi być ścieżką bezwzględną. Użyj `which inferrs` na hoście Gateway i umieść tę ścieżkę w konfiguracji. Pełny opis pól znajdziesz w [Usługach modeli lokalnych](</pl/gateway/local-model-services>).

## Zaawansowana konfiguracja

Dlaczego requiresStringContent ma znaczenie

Niektóre trasy Chat Completions w `inferrs` akceptują tylko ciąg znaków `messages[].content`, a nie strukturalne tablice części treści.

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw spłaszczy części treści zawierające czysty tekst do zwykłych ciągów znaków przed wysłaniem żądania.

Gemma i zastrzeżenie dotyczące schematu narzędzi

Niektóre obecne kombinacje `inferrs` \+ Gemma akceptują małe bezpośrednie żądania `/v1/chat/completions`, ale nadal zawodzą przy pełnych turach środowiska wykonawczego agenta OpenClaw.

Jeśli tak się stanie, najpierw spróbuj tego:

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

To wyłącza powierzchnię schematu narzędzi OpenClaw dla modelu i może zmniejszyć presję promptu na bardziej rygorystyczne lokalne backendy.

Jeśli bardzo małe bezpośrednie żądania nadal działają, ale zwykłe tury agenta OpenClaw nadal kończą się awarią wewnątrz `inferrs`, pozostały problem zwykle dotyczy zachowania modelu lub serwera upstream, a nie warstwy transportowej OpenClaw.

Ręczny test smoke

Po skonfigurowaniu przetestuj obie warstwy:

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

Jeśli pierwsze polecenie działa, a drugie kończy się niepowodzeniem, sprawdź poniższą sekcję rozwiązywania problemów.

Zachowanie w stylu proxy

`inferrs` jest traktowany jako backend `/v1` zgodny z OpenAI w stylu proxy, a nie jako natywny punkt końcowy OpenAI.

  * Natywne kształtowanie żądań tylko dla OpenAI nie ma tutaj zastosowania
  * Brak `service_tier`, brak Responses `store`, brak podpowiedzi prompt-cache i brak kształtowania payloadu zgodnego z rozumowaniem OpenAI
  * Ukryte nagłówki atrybucji OpenClaw (`originator`, `version`, `User-Agent`) nie są wstrzykiwane dla niestandardowych bazowych URL `inferrs`


## Rozwiązywanie problemów

curl /v1/models kończy się niepowodzeniem

`inferrs` nie działa, jest nieosiągalny albo nie jest powiązany z oczekiwanym hostem/portem. Upewnij się, że serwer jest uruchomiony i nasłuchuje pod adresem, który skonfigurowano.

messages[].content oczekiwano ciągu znaków

Ustaw `compat.requiresStringContent: true` we wpisie modelu. Szczegóły znajdziesz w sekcji `requiresStringContent` powyżej.

Bezpośrednie wywołania /v1/chat/completions przechodzą, ale openclaw infer model run kończy się niepowodzeniem

Spróbuj ustawić `compat.supportsTools: false`, aby wyłączyć powierzchnię schematu narzędzi. Zobacz zastrzeżenie dotyczące schematu narzędzi Gemma powyżej.

inferrs nadal ulega awarii przy większych turach agenta

Jeśli OpenClaw nie otrzymuje już błędów schematu, ale `inferrs` nadal ulega awarii przy większych turach agenta, potraktuj to jako ograniczenie upstream `inferrs` lub modelu. Zmniejsz presję promptu albo przełącz się na inny lokalny backend lub model.

## Powiązane

[**Modele lokalne** Uruchamianie OpenClaw z lokalnymi serwerami modeli. ](</pl/gateway/local-models>) [**Usługi modeli lokalnych** Uruchamianie lokalnych serwerów modeli na żądanie dla skonfigurowanych dostawców. ](</pl/gateway/local-model-services>) [**Rozwiązywanie problemów z Gateway** Debugowanie lokalnych backendów zgodnych z OpenAI, które przechodzą próby, ale zawodzą przy uruchomieniach agenta. ](</pl/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**Wybór modelu** Omówienie wszystkich dostawców, referencji modeli i zachowania failover. ](</pl/concepts/model-providers>)

Was this useful?YesNo