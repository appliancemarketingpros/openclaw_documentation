---
title: LiteLLM
source_url: https://docs.openclaw.ai/pl/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) to otwartoźródłowy LLM gateway, który zapewnia ujednolicone API do ponad 100 dostawców modeli. Kieruj OpenClaw przez LiteLLM, aby uzyskać scentralizowane śledzenie kosztów, logowanie oraz elastyczność przełączania backendów bez zmiany konfiguracji OpenClaw.

## Szybki start

### Onboarding (recommended)

**Najlepsze dla:** najszybszej ścieżki do działającej konfiguracji LiteLLM.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

W przypadku nieinteraktywnej konfiguracji zdalnego proxy przekaż jawnie URL proxy:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Manual setup

**Najlepsze dla:** pełnej kontroli nad instalacją i konfiguracją.

* ### Start LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Point OpenClaw to LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

To wszystko. OpenClaw kieruje teraz ruch przez LiteLLM.

## Konfiguracja

### Zmienne środowiskowe

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### Plik konfiguracyjny

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## Konfiguracja zaawansowana

### Generowanie obrazów

LiteLLM może też obsługiwać narzędzie `image_generate` za pośrednictwem zgodnych z OpenAI tras `/images/generations` i `/images/edits`. Skonfiguruj model obrazów LiteLLM w `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Adresy URL LiteLLM dla local loopback, takie jak `http://localhost:4000`, działają bez globalnego nadpisania sieci prywatnej. W przypadku proxy hostowanego w sieci LAN ustaw `models.providers.litellm.request.allowPrivateNetwork: true`, ponieważ klucz API zostanie wysłany do skonfigurowanego hosta proxy.

Virtual keys

Utwórz dedykowany klucz dla OpenClaw z limitami wydatków:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

Użyj wygenerowanego klucza jako `LITELLM_API_KEY`.

Model routing

LiteLLM może kierować żądania modeli do różnych backendów. Skonfiguruj to w pliku LiteLLM `config.yaml`:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw nadal żąda `claude-opus-4-6` — LiteLLM obsługuje routing.

Viewing usage

Sprawdź pulpit LiteLLM lub API:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Proxy behavior notes

  * LiteLLM domyślnie działa pod adresem `http://localhost:4000`
  * OpenClaw łączy się przez zgodny z OpenAI endpoint `/v1` LiteLLM w stylu proxy
  * Natywne kształtowanie żądań tylko dla OpenAI nie ma zastosowania przez LiteLLM: brak `service_tier`, brak Responses `store`, brak wskazówek pamięci podręcznej promptów i brak kształtowania payloadu zgodnego z rozumowaniem OpenAI
  * Ukryte nagłówki atrybucji OpenClaw (`originator`, `version`, `User-Agent`) nie są wstrzykiwane dla niestandardowych bazowych adresów URL LiteLLM


## Powiązane

[**LiteLLM Docs** Oficjalna dokumentacja LiteLLM i referencja API. ](<https://docs.litellm.ai>) [**Model selection** Przegląd wszystkich dostawców, referencji modeli i zachowania przełączania awaryjnego. ](</pl/concepts/model-providers>) [**Configuration** Pełna referencja konfiguracji. ](</pl/gateway/configuration>) [**Model selection** Jak wybierać i konfigurować modele. ](</pl/concepts/models>)

Was this useful?YesNo