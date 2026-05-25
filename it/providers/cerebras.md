---
title: Cerebras
source_url: https://docs.openclaw.ai/it/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) offre inferenza ad alta velocità compatibile con OpenAI su hardware di inferenza personalizzato. OpenClaw include un Plugin provider Cerebras integrato con un catalogo statico di quattro modelli.

Proprietà | Valore  
---|---  
ID provider | `cerebras`  
Plugin | integrato, `enabledByDefault: true`  
Variabile env auth | `CEREBRAS_API_KEY`  
Flag di onboarding | `--auth-choice cerebras-api-key`  
Flag CLI diretto | `--cerebras-api-key <key>`  
API | compatibile con OpenAI (`openai-completions`)  
URL di base | `https://api.cerebras.ai/v1`  
Modello predefinito | `cerebras/zai-glm-4.7`  
  
## Per iniziare

* ### Ottieni una chiave API

Crea una chiave API nella [Cerebras Cloud Console](<https://cloud.cerebras.ai>).

* ### Esegui l’onboarding

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Flag direttoCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Solo envCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### Verifica che i modelli siano disponibili

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

L’elenco dovrebbe includere tutti e quattro i modelli integrati. Se `CEREBRAS_API_KEY` non viene risolto, `openclaw models status --json` segnala la credenziale mancante in `auth.unusableProfiles`.

## Configurazione non interattiva

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## Catalogo integrato

OpenClaw include un catalogo Cerebras statico che rispecchia l’endpoint pubblico compatibile con OpenAI. Tutti e quattro i modelli condividono un contesto da 128k e 8.192 token di output massimo.

Rif. modello | Nome | Ragionamento | Note  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | sì | Modello predefinito; modello di ragionamento in anteprima  
`cerebras/gpt-oss-120b` | GPT OSS 120B | sì | Modello di ragionamento di produzione  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | no | Modello in anteprima senza ragionamento  
`cerebras/llama3.1-8b` | Llama 3.1 8B | no | Modello di produzione ottimizzato per la velocità  
  
## Configurazione manuale

Il Plugin integrato di solito significa che ti serve solo la chiave API. Usa la configurazione esplicita `models.providers.cerebras` quando vuoi sovrascrivere i metadati dei modelli o eseguire in `mode: "merge"` rispetto al catalogo statico:

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## Correlati

[**Provider di modelli** Scelta dei provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Modalità di pensiero** Livelli di impegno di ragionamento per i due modelli Cerebras con capacità di ragionamento. ](</it/tools/thinking>) [**Riferimento di configurazione** Valori predefiniti degli agenti e configurazione dei modelli. ](</it/gateway/config-agents#agent-defaults>) [**FAQ sui modelli** Profili auth, cambio dei modelli e risoluzione degli errori "no profile". ](</it/help/faq-models>)

Was this useful?YesNo