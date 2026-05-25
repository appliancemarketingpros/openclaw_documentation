---
title: Mantello di Amazon Bedrock
source_url: https://docs.openclaw.ai/it/providers/bedrock-mantle
scraped_at: 2026-05-25
---

OpenClaw include un provider **Amazon Bedrock Mantle** integrato che si connette all'endpoint compatibile con OpenAI di Mantle. Mantle ospita modelli open-source e di terze parti (GPT-OSS, Qwen, Kimi, GLM e simili) tramite una superficie `/v1/chat/completions` standard supportata dall'infrastruttura Bedrock.

Proprietà | Valore  
---|---  
ID provider | `amazon-bedrock-mantle`  
API | `openai-completions` (compatibile con OpenAI) o `anthropic-messages` (route Anthropic Messages)  
Auth | `AWS_BEARER_TOKEN_BEDROCK` esplicito o generazione del bearer token tramite catena di credenziali IAM  
Regione predefinita | `us-east-1` (sovrascrivi con `AWS_REGION` o `AWS_DEFAULT_REGION`)  
  
## Per iniziare

Scegli il metodo di autenticazione preferito e segui i passaggi di configurazione.

### Bearer token esplicito

**Ideale per:** ambienti in cui hai già un bearer token Mantle.

* ### Imposta il bearer token sull'host del Gateway

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

Facoltativamente, imposta una regione (il valore predefinito è `us-east-1`):

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### Verifica che i modelli vengano rilevati

bashCopy code
[code]
    openclaw models list
[/code]

I modelli rilevati compaiono sotto il provider `amazon-bedrock-mantle`. Non è richiesta alcuna configurazione aggiuntiva, a meno che tu non voglia sovrascrivere i valori predefiniti.

### Credenziali IAM

**Ideale per:** usare credenziali compatibili con AWS SDK (configurazione condivisa, SSO, identità web, ruoli di istanza o task).

* ### Configura le credenziali AWS sull'host del Gateway

Qualsiasi origine di autenticazione compatibile con AWS SDK funziona:

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### Verifica che i modelli vengano rilevati

bashCopy code
[code]
    openclaw models list
[/code]

OpenClaw genera automaticamente un bearer token Mantle dalla catena di credenziali.

## Rilevamento automatico dei modelli

Quando `AWS_BEARER_TOKEN_BEDROCK` è impostato, OpenClaw lo usa direttamente. In caso contrario, OpenClaw prova a generare un bearer token Mantle dalla catena di credenziali predefinita di AWS. Poi rileva i modelli Mantle disponibili interrogando l'endpoint `/v1/models` della regione.

Comportamento | Dettaglio  
---|---  
Cache di rilevamento | Risultati memorizzati per 1 ora  
Aggiornamento token IAM | Ogni ora  
  
Per mantenere abilitato il Plugin Mantle ma sopprimere il rilevamento automatico e la generazione del bearer token IAM, disabilita l'interruttore di rilevamento di proprietà del Plugin:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### Regioni supportate

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## Configurazione manuale

Se preferisci una configurazione esplicita invece del rilevamento automatico:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Configurazione avanzata

Supporto al reasoning

Il supporto al reasoning viene inferito dagli ID dei modelli che contengono pattern come `thinking`, `reasoner` o `gpt-oss-120b`. OpenClaw imposta `reasoning: true` automaticamente per i modelli corrispondenti durante il rilevamento.

Indisponibilità dell'endpoint

Se l'endpoint Mantle non è disponibile o non restituisce modelli, il provider viene ignorato silenziosamente. OpenClaw non genera errori; gli altri provider configurati continuano a funzionare normalmente.

Claude Opus 4.7 tramite la route Anthropic Messages

Mantle espone anche una route Anthropic Messages che trasporta i modelli Claude attraverso lo stesso percorso di streaming autenticato con bearer token. Claude Opus 4.7 (`amazon-bedrock-mantle/claude-opus-4.7`) è chiamabile tramite questa route con streaming di proprietà del provider, quindi i bearer token AWS non vengono trattati come chiavi API Anthropic.

Quando fissi un modello Anthropic Messages sul provider Mantle, OpenClaw usa la superficie API `anthropic-messages` invece di `openai-completions` per quel modello. L'autenticazione proviene comunque da `AWS_BEARER_TOKEN_BEDROCK` (o dal bearer token IAM coniato).

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Relazione con il provider Amazon Bedrock

Bedrock Mantle è un provider separato dal provider standard [Amazon Bedrock](</it/providers/bedrock>). Mantle usa una superficie `/v1` compatibile con OpenAI, mentre il provider Bedrock standard usa l'API Bedrock nativa.

Entrambi i provider condividono la stessa credenziale `AWS_BEARER_TOKEN_BEDROCK` quando presente.

## Correlati

[**Amazon Bedrock** Provider Bedrock nativo per Anthropic Claude, Titan e altri modelli. ](</it/providers/bedrock>) [**Selezione del modello** Scelta di provider, riferimenti ai modelli e comportamento di failover. ](</it/concepts/model-providers>) [**OAuth e autenticazione** Dettagli di autenticazione e regole di riuso delle credenziali. ](</it/gateway/authentication>) [**Risoluzione dei problemi** Problemi comuni e come risolverli. ](</it/help/troubleshooting>)

Was this useful?YesNo