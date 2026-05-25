---
title: Chutes
source_url: https://docs.openclaw.ai/it/providers/chutes
scraped_at: 2026-05-25
---

[Chutes](<https://chutes.ai>) espone cataloghi di modelli open-source tramite un'API compatibile con OpenAI. OpenClaw supporta sia OAuth via browser sia l'autenticazione diretta con chiave API per il provider `chutes` incluso.

Proprietà | Valore  
---|---  
Provider | `chutes`  
API | compatibile con OpenAI  
URL base | `https://llm.chutes.ai/v1`  
Auth | OAuth o chiave API (vedi sotto)  
  
## Per iniziare

### OAuth

* ### Run the OAuth onboarding flow

bashCopy code
[code]
    openclaw onboard --auth-choice chutes
[/code]

OpenClaw avvia il flusso nel browser localmente oppure mostra un flusso con URL + incolla del reindirizzamento sugli host remoti/headless. I token OAuth vengono aggiornati automaticamente tramite i profili di autenticazione di OpenClaw.

* ### Verify the default model

Dopo l'onboarding, il modello predefinito viene impostato su `chutes/zai-org/GLM-4.7-TEE` e il catalogo Chutes incluso viene registrato.

### API key

* ### Get an API key

Crea una chiave su [chutes.ai/settings/api-keys](<https://chutes.ai/settings/api-keys>).

* ### Run the API key onboarding flow

bashCopy code
[code]
    openclaw onboard --auth-choice chutes-api-key
[/code]

* ### Verify the default model

Dopo l'onboarding, il modello predefinito viene impostato su `chutes/zai-org/GLM-4.7-TEE` e il catalogo Chutes incluso viene registrato.

## Comportamento di rilevamento

Quando l'autenticazione Chutes è disponibile, OpenClaw interroga il catalogo Chutes con quelle credenziali e usa i modelli rilevati. Se il rilevamento non riesce, OpenClaw ripiega su un catalogo statico incluso, così onboarding e avvio continuano a funzionare.

## Alias predefiniti

OpenClaw registra tre alias pratici per il catalogo Chutes incluso:

Alias | Modello di destinazione  
---|---  
`chutes-fast` | `chutes/zai-org/GLM-4.7-FP8`  
`chutes-pro` | `chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes-vision` | `chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
  
## Catalogo iniziale integrato

Il catalogo di fallback incluso comprende i riferimenti Chutes correnti:

Riferimento modello  
---  
`chutes/zai-org/GLM-4.7-TEE`  
`chutes/zai-org/GLM-5-TEE`  
`chutes/deepseek-ai/DeepSeek-V3.2-TEE`  
`chutes/deepseek-ai/DeepSeek-R1-0528-TEE`  
`chutes/moonshotai/Kimi-K2.5-TEE`  
`chutes/chutesai/Mistral-Small-3.2-24B-Instruct-2506`  
`chutes/Qwen/Qwen3-Coder-Next-TEE`  
`chutes/openai/gpt-oss-120b-TEE`  
  
## Esempio di configurazione

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "chutes/zai-org/GLM-4.7-TEE" },      models: {        "chutes/zai-org/GLM-4.7-TEE": { alias: "Chutes GLM 4.7" },        "chutes/deepseek-ai/DeepSeek-V3.2-TEE": { alias: "Chutes DeepSeek V3.2" },      },    },  },}
[/code]

OAuth overrides

Puoi personalizzare il flusso OAuth con variabili d'ambiente facoltative:

Variabile | Scopo  
---|---  
`CHUTES_CLIENT_ID` | ID client OAuth personalizzato  
`CHUTES_CLIENT_SECRET` | Segreto client OAuth personalizzato  
`CHUTES_OAUTH_REDIRECT_URI` | URI di reindirizzamento personalizzato  
`CHUTES_OAUTH_SCOPES` | Scope OAuth personalizzati  
  
Consulta la [documentazione OAuth di Chutes](<https://chutes.ai/docs/sign-in-with-chutes/overview>) per i requisiti dell'app di reindirizzamento e assistenza.

Notes

  * Il rilevamento con chiave API e OAuth usa lo stesso ID provider `chutes`.
  * I modelli Chutes sono registrati come `chutes/<model-id>`.
  * Se il rilevamento fallisce all'avvio, il catalogo statico incluso viene usato automaticamente.


## Correlati

[**Model selection** Regole del provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Configuration reference** Schema di configurazione completo, incluse le impostazioni del provider. ](</it/gateway/configuration-reference>) [**Chutes** Dashboard Chutes e documentazione API. ](<https://chutes.ai>) [**Chutes API keys** Crea e gestisci le chiavi API Chutes. ](<https://chutes.ai/settings/api-keys>)

Was this useful?YesNo