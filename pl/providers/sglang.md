---
title: SGLang
source_url: https://docs.openclaw.ai/pl/providers/sglang
scraped_at: 2026-05-25
---

SGLang udostępnia modele o otwartych wagach przez zgodne z OpenAI API HTTP. OpenClaw łączy się z SGLang przy użyciu rodziny dostawców `openai-completions` z automatycznym wykrywaniem dostępnych modeli.

Właściwość | Wartość  
---|---  
Identyfikator dostawcy | `sglang`  
Plugin | wbudowany, `enabledByDefault: true`  
Zmienna środowiskowa uwierzytelniania | `SGLANG_API_KEY` (dowolna niepusta wartość, jeśli serwer nie ma uwierzytelniania)  
Flaga konfiguracji początkowej | `--auth-choice sglang`  
API | zgodne z OpenAI (`openai-completions`)  
Domyślny bazowy URL | `http://127.0.0.1:30000/v1`  
Domyślny symbol zastępczy modelu | `sglang/Qwen/Qwen3-8B`  
Użycie strumieniowania | Tak (`supportsStreamingUsage: true`)  
Cennik | Oznaczone jako zewnętrznie bezpłatne (`modelPricing.external: false`)  
  
OpenClaw także **automatycznie wykrywa** dostępne modele z SGLang, gdy włączysz tę opcję za pomocą `SGLANG_API_KEY`. Użyj `sglang/*` w `agents.defaults.models`, aby zachować dynamiczne wykrywanie, gdy konfigurujesz także niestandardowy bazowy URL SGLang. Zobacz Wykrywanie modeli (niejawny dostawca) poniżej.

## Pierwsze kroki

* ### Uruchom SGLang

Uruchom SGLang z serwerem zgodnym z OpenAI. Twój bazowy URL powinien udostępniać punkty końcowe `/v1` (na przykład `/v1/models`, `/v1/chat/completions`). SGLang zwykle działa pod adresem:

  * `http://127.0.0.1:30000/v1`


* ### Ustaw klucz API

Dowolna wartość działa, jeśli na serwerze nie skonfigurowano uwierzytelniania:

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### Uruchom konfigurację początkową lub ustaw model bezpośrednio

bashCopy code
[code]
    openclaw onboard
[/code]

Albo skonfiguruj model ręcznie:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## Wykrywanie modeli (niejawny dostawca)

Gdy `SGLANG_API_KEY` jest ustawione (albo istnieje profil uwierzytelniania), a Ty **nie** definiujesz `models.providers.sglang`, OpenClaw wyśle zapytanie do:

  * `GET http://127.0.0.1:30000/v1/models`


i przekształci zwrócone identyfikatory w wpisy modeli.

## Jawna konfiguracja (modele ręczne)

Użyj jawnej konfiguracji, gdy:

  * SGLang działa na innym hoście/porcie.
  * Chcesz przypiąć wartości `contextWindow`/`maxTokens`.
  * Twój serwer wymaga prawdziwego klucza API (albo chcesz kontrolować nagłówki).

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## Konfiguracja zaawansowana

Zachowanie w stylu proxy

SGLang jest traktowany jako backend `/v1` w stylu proxy zgodny z OpenAI, a nie natywny punkt końcowy OpenAI.

Zachowanie | SGLang  
---|---  
Kształtowanie żądań tylko dla OpenAI | Nie jest stosowane  
`service_tier`, Responses `store`, wskazówki pamięci podręcznej promptów | Nie są wysyłane  
Kształtowanie ładunku zgodności rozumowania | Nie jest stosowane  
Ukryte nagłówki atrybucji (`originator`, `version`, `User-Agent`) | Nie są wstrzykiwane dla niestandardowych bazowych URL-i SGLang  
Rozwiązywanie problemów

**Serwer nieosiągalny**

Sprawdź, czy serwer działa i odpowiada:

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**Błędy uwierzytelniania**

Jeśli żądania kończą się błędami uwierzytelniania, ustaw prawdziwy `SGLANG_API_KEY`, który pasuje do konfiguracji serwera, albo skonfiguruj dostawcę jawnie w `models.providers.sglang`.

## Powiązane

[**Wybór modelu** Wybieranie dostawców, referencji modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Dokumentacja konfiguracji** Pełny schemat konfiguracji, w tym wpisy dostawców. ](</pl/gateway/configuration-reference>)

Was this useful?YesNo