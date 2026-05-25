---
title: Qianfan
source_url: https://docs.openclaw.ai/pl/providers/qianfan
scraped_at: 2026-05-25
---

Qianfan to platforma MaaS firmy Baidu, zapewniająca **ujednolicone API** , które kieruje żądania do wielu modeli za jednym punktem końcowym i kluczem API. Jest zgodna z OpenAI, więc większość pakietów SDK OpenAI działa po zmianie bazowego URL-a.

Właściwość | Wartość  
---|---  
Dostawca | `qianfan`  
Uwierzytelnianie | `QIANFAN_API_KEY`  
API | zgodne z OpenAI  
Bazowy URL | `https://qianfan.baidubce.com/v2`  
  
## Pierwsze kroki

* ### Utwórz konto Baidu Cloud

Zarejestruj się lub zaloguj w [konsoli Qianfan](<https://console.bce.baidu.com/qianfan/ais/console/apiKey>) i upewnij się, że masz włączony dostęp do API Qianfan.

* ### Wygeneruj klucz API

Utwórz nową aplikację lub wybierz istniejącą, a następnie wygeneruj klucz API. Format klucza to `bce-v3/ALTAK-...`.

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice qianfan-api-key
[/code]

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider qianfan
[/code]

## Wbudowany katalog

Odwołanie do modelu | Wejście | Kontekst | Maks. wyjście | Rozumowanie | Uwagi  
---|---|---|---|---|---  
`qianfan/deepseek-v3.2` | tekst | 98,304 | 32,768 | Tak | Model domyślny  
`qianfan/ernie-5.0-thinking-preview` | tekst, obraz | 119,000 | 64,000 | Tak | Multimodalny  
  
## Przykład konfiguracji

json5Copy code
[code]
    {  env: { QIANFAN_API_KEY: "bce-v3/ALTAK-..." },  agents: {    defaults: {      model: { primary: "qianfan/deepseek-v3.2" },      models: {        "qianfan/deepseek-v3.2": { alias: "QIANFAN" },      },    },  },  models: {    providers: {      qianfan: {        baseUrl: "https://qianfan.baidubce.com/v2",        api: "openai-completions",        models: [          {            id: "deepseek-v3.2",            name: "DEEPSEEK V3.2",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 98304,            maxTokens: 32768,          },          {            id: "ernie-5.0-thinking-preview",            name: "ERNIE-5.0-Thinking-Preview",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 119000,            maxTokens: 64000,          },        ],      },    },  },}
[/code]

Transport i zgodność

Qianfan działa przez ścieżkę transportu zgodną z OpenAI, a nie przez natywne kształtowanie żądań OpenAI. Oznacza to, że standardowe funkcje pakietów SDK OpenAI działają, ale parametry specyficzne dla dostawcy mogą nie być przekazywane dalej.

Katalog i nadpisania

Wbudowany katalog obecnie obejmuje `deepseek-v3.2` i `ernie-5.0-thinking-preview`. Dodaj lub nadpisz `models.providers.qianfan` tylko wtedy, gdy potrzebujesz niestandardowego bazowego URL-a lub metadanych modelu.

Rozwiązywanie problemów

  * Upewnij się, że Twój klucz API zaczyna się od `bce-v3/ALTAK-` i ma włączony dostęp do API Qianfan w konsoli Baidu Cloud.
  * Jeśli modele nie są wyświetlane, potwierdź, że usługa Qianfan jest aktywowana na Twoim koncie.
  * Domyślny bazowy URL to `https://qianfan.baidubce.com/v2`. Zmień go tylko wtedy, gdy używasz niestandardowego punktu końcowego lub proxy.


## Powiązane

[**Wybór modelu** Wybieranie dostawców, odwołań do modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Dokumentacja konfiguracji** Pełna dokumentacja konfiguracji OpenClaw. ](</pl/gateway/configuration-reference>) [**Konfiguracja agenta** Konfigurowanie domyślnych ustawień agentów i przypisań modeli. ](</pl/concepts/agent>) [**Dokumentacja API Qianfan** Oficjalna dokumentacja API Qianfan. ](<https://cloud.baidu.com/doc/qianfan-api/s/3m7of64lb>)

Was this useful?YesNo