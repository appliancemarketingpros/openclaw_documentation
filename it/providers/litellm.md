---
title: LiteLLM
source_url: https://docs.openclaw.ai/it/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) è un gateway LLM open-source che fornisce un'API unificata per oltre 100 provider di modelli. Instrada OpenClaw tramite LiteLLM per ottenere monitoraggio centralizzato dei costi, registrazione e la flessibilità di cambiare backend senza modificare la configurazione di OpenClaw.

## Avvio rapido

### Onboarding (consigliato)

**Ideale per:** il percorso più rapido verso una configurazione LiteLLM funzionante.

* ### Esegui l'onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

Per una configurazione non interattiva verso un proxy remoto, passa esplicitamente l'URL del proxy:

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Configurazione manuale

**Ideale per:** controllo completo su installazione e configurazione.

* ### Avvia LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Punta OpenClaw a LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

Tutto qui. OpenClaw ora instrada tramite LiteLLM.

## Configurazione

### Variabili d'ambiente

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### File di configurazione

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## Configurazione avanzata

### Generazione di immagini

LiteLLM può anche supportare lo strumento `image_generate` tramite rotte compatibili con OpenAI `/images/generations` e `/images/edits`. Configura un modello di immagini LiteLLM in `agents.defaults.imageGenerationModel`:

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

Gli URL LiteLLM di loopback come `http://localhost:4000` funzionano senza una sostituzione globale per reti private. Per un proxy ospitato sulla LAN, imposta `models.providers.litellm.request.allowPrivateNetwork: true` perché la chiave API verrà inviata all'host proxy configurato.

Chiavi virtuali

Crea una chiave dedicata per OpenClaw con limiti di spesa:

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

Usa la chiave generata come `LITELLM_API_KEY`.

Instradamento dei modelli

LiteLLM può instradare le richieste dei modelli verso backend diversi. Configura nel tuo `config.yaml` di LiteLLM:

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw continua a richiedere `claude-opus-4-6` — LiteLLM gestisce l'instradamento.

Visualizzazione dell'utilizzo

Controlla la dashboard o l'API di LiteLLM:

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Note sul comportamento del proxy

  * LiteLLM viene eseguito su `http://localhost:4000` per impostazione predefinita
  * OpenClaw si connette tramite l'endpoint proxy-style compatibile con OpenAI `/v1` di LiteLLM
  * La formattazione delle richieste nativa solo OpenAI non si applica tramite LiteLLM: niente `service_tier`, niente `store` di Responses, niente suggerimenti di prompt-cache e niente formattazione dei payload di compatibilità reasoning di OpenAI
  * Gli header di attribuzione nascosti di OpenClaw (`originator`, `version`, `User-Agent`) non vengono inseriti negli URL base LiteLLM personalizzati


## Correlati

[**Documentazione LiteLLM** Documentazione ufficiale di LiteLLM e riferimento API. ](<https://docs.litellm.ai>) [**Selezione del modello** Panoramica di tutti i provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Configurazione** Riferimento completo della configurazione. ](</it/gateway/configuration>) [**Selezione del modello** Come scegliere e configurare i modelli. ](</it/concepts/models>)

Was this useful?YesNo