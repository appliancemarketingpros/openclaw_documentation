---
title: Mistral
source_url: https://docs.openclaw.ai/pl/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw zawiera dołączony Plugin Mistral, który rejestruje cztery kontrakty: uzupełnianie czatu, rozumienie multimediów (transkrypcja wsadowa Voxtral), STT czasu rzeczywistego dla Voice Call (Voxtral Realtime) oraz embeddingi pamięci (`mistral-embed`).

Właściwość | Wartość  
---|---  
Identyfikator providera | `mistral`  
Plugin | dołączony, `enabledByDefault: true`  
Zmienna env uwierzytelniania | `MISTRAL_API_KEY`  
Flaga onboardingu | `--auth-choice mistral-api-key`  
Bezpośrednia flaga CLI | `--mistral-api-key <key>`  
API | zgodne z OpenAI (`openai-completions`)  
Bazowy URL | `https://api.mistral.ai/v1`  
Domyślny model | `mistral/mistral-large-latest`  
Model embeddingów | `mistral-embed`  
Wsadowy Voxtral | `voxtral-mini-latest` (transkrypcja audio)  
Voxtral realtime | `voxtral-mini-transcribe-realtime-2602`  
  
## Pierwsze kroki

* ### Uzyskaj klucz API

Utwórz klucz API w [Mistral Console](<https://console.mistral.ai/>).

* ### Uruchom onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

Albo przekaż klucz bezpośrednio:

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### Ustaw domyślny model

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### Sprawdź, czy model jest dostępny

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## Wbudowany katalog LLM

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) to bieżący, mieszany model Medium w dołączonym katalogu: 128B gęstych wag, wejście tekstowe i obrazowe, kontekst 256K, wywoływanie funkcji, dane wyjściowe strukturalne, programowanie oraz regulowane rozumowanie przez Chat Completions API. Użyj `mistral/mistral-medium-3-5`, gdy chcesz użyć nowszego zunifikowanego modelu agentowego/programistycznego Mistral zamiast domyślnego `mistral/mistral-large-latest`.

OpenClaw obecnie dostarcza ten dołączony katalog Mistral:

Ref modelu | Wejście | Kontekst | Maks. wyjście | Uwagi  
---|---|---|---|---  
`mistral/mistral-large-latest` | tekst, obraz | 262,144 | 16,384 | Domyślny model  
`mistral/mistral-medium-2508` | tekst, obraz | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | tekst, obraz | 262,144 | 8,192 | Mistral Medium 3.5; regulowane rozumowanie  
`mistral/mistral-small-latest` | tekst, obraz | 128,000 | 16,384 | Mistral Small 4; regulowane rozumowanie przez API `reasoning_effort`  
`mistral/pixtral-large-latest` | tekst, obraz | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | tekst | 256,000 | 4,096 | Programowanie  
`mistral/devstral-medium-latest` | tekst | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | tekst | 128,000 | 40,000 | Z włączonym rozumowaniem  
  
Po onboardingu wykonaj smoke test Medium 3.5 bez uruchamiania Gateway:

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

Aby przejrzeć wiersz dołączonego katalogu przed zmianą konfiguracji:

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## Transkrypcja audio (Voxtral)

Użyj Voxtral do wsadowej transkrypcji audio przez pipeline rozumienia multimediów.

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## Strumieniowe STT dla Voice Call

Dołączony Plugin `mistral` rejestruje Voxtral Realtime jako providera strumieniowego STT dla Voice Call.

Ustawienie | Ścieżka konfiguracji | Domyślnie  
---|---|---  
Klucz API | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | Używa awaryjnie `MISTRAL_API_KEY`  
Model | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
Kodowanie | `...mistral.encoding` | `pcm_mulaw`  
Częstotliwość próbkowania | `...mistral.sampleRate` | `8000`  
Docelowe opóźnienie | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## Konfiguracja zaawansowana

Regulowane rozumowanie

`mistral/mistral-small-latest` (Mistral Small 4) i `mistral/mistral-medium-3-5` obsługują [regulowane rozumowanie](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>) w Chat Completions API przez `reasoning_effort` (`none` minimalizuje dodatkowe myślenie w wyniku; `high` pokazuje pełne ślady myślenia przed końcową odpowiedzią). Mistral zaleca `reasoning_effort="high"` dla przypadków użycia agentowego i kodu w Medium 3.5.

OpenClaw mapuje poziom **thinking** sesji na API Mistral:

Poziom thinking OpenClaw | Mistral `reasoning_effort`  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Przykładowa konfiguracja zakresu modelu dla rozumowania Medium 3.5:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

Embeddingi pamięci

Mistral może obsługiwać embeddingi pamięci przez `/v1/embeddings` (domyślny model: `mistral-embed`).

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

Uwierzytelnianie i bazowy URL

  * Uwierzytelnianie Mistral używa `MISTRAL_API_KEY` (nagłówek Bearer).
  * Bazowy URL providera domyślnie to `https://api.mistral.ai/v1` i akceptuje standardowy, zgodny z OpenAI kształt żądania chat-completions.
  * Domyślny model onboardingu to `mistral/mistral-large-latest`.
  * Nadpisuj bazowy URL w `models.providers.mistral.baseUrl` tylko wtedy, gdy Mistral jawnie opublikuje regionalny endpoint, którego potrzebujesz.


## Powiązane

[**Wybór modelu** Wybieranie providerów, refów modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Rozumienie multimediów** Konfiguracja transkrypcji audio i wybór providera. ](</pl/nodes/media-understanding>)

Was this useful?YesNo