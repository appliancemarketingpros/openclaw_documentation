---
title: LiteLLM
source_url: https://docs.openclaw.ai/nl/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) is een open-source LLM-Gateway die een uniforme API biedt voor meer dan 100 modelproviders. Routeer OpenClaw via LiteLLM voor gecentraliseerde kostenregistratie, logging en de flexibiliteit om backends te wisselen zonder je OpenClaw-configuratie te wijzigen.

## Snelstart

### Onboarding (recommended)

**Beste voor:** de snelste route naar een werkende LiteLLM-installatie.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

Geef voor een niet-interactieve installatie met een externe proxy expliciet de proxy-URL door:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Manual setup

**Beste voor:** volledige controle over installatie en configuratie.

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

Dat is alles. OpenClaw routeert nu via LiteLLM.

## Configuratie

### Omgevingsvariabelen

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### Configuratiebestand

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## Geavanceerde configuratie

### Afbeeldingen genereren

LiteLLM kan ook de `image_generate`-tool ondersteunen via OpenAI-compatibele `/images/generations`\- en `/images/edits`-routes. Configureer een LiteLLM-afbeeldingsmodel onder `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Loopback-LiteLLM-URL's zoals `http://localhost:4000` werken zonder globale override voor privénetwerken. Stel voor een proxy die op een LAN wordt gehost `models.providers.litellm.request.allowPrivateNetwork: true` in, omdat de API-sleutel naar de geconfigureerde proxyhost wordt verzonden.

Virtual keys

Maak een speciale sleutel voor OpenClaw met bestedingslimieten:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

Gebruik de gegenereerde sleutel als `LITELLM_API_KEY`.

Model routing

LiteLLM kan modelaanvragen naar verschillende backends routeren. Configureer dit in je LiteLLM `config.yaml`:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw blijft `claude-opus-4-6` aanvragen — LiteLLM handelt de routering af.

Viewing usage

Controleer het dashboard of de API van LiteLLM:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Proxy behavior notes

  * LiteLLM draait standaard op `http://localhost:4000`
  * OpenClaw maakt verbinding via het proxy-achtige OpenAI-compatibele `/v1`-endpoint van LiteLLM
  * Aanvraagvorming die alleen voor native OpenAI geldt, is niet van toepassing via LiteLLM: geen `service_tier`, geen Responses `store`, geen prompt-cache-hints en geen OpenAI-reasoning-compat payload-vorming
  * Verborgen OpenClaw-attributieheaders (`originator`, `version`, `User-Agent`) worden niet geïnjecteerd op aangepaste LiteLLM-basis-URL's


## Gerelateerd

[**LiteLLM Docs** Officiële LiteLLM-documentatie en API-referentie. ](<https://docs.litellm.ai>) [**Model selection** Overzicht van alle providers, modelverwijzingen en failovergedrag. ](</nl/concepts/model-providers>) [**Configuration** Volledige configuratiereferentie. ](</nl/gateway/configuration>) [**Model selection** Hoe je modellen kiest en configureert. ](</nl/concepts/models>)

Was this useful?YesNo