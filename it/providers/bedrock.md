---
title: Amazon Bedrock
source_url: https://docs.openclaw.ai/it/providers/bedrock
scraped_at: 2026-05-25
---

OpenClaw può usare i modelli **Amazon Bedrock** tramite il provider di streaming **Bedrock Converse** di pi-ai. L'autenticazione Bedrock usa la **catena di credenziali predefinita dell'AWS SDK** , non una chiave API.

Proprietà | Valore  
---|---  
Provider | `amazon-bedrock`  
API | `bedrock-converse-stream`  
Autenticazione | credenziali AWS (variabili d'ambiente, configurazione condivisa o ruolo dell'istanza)  
Regione | `AWS_REGION` o `AWS_DEFAULT_REGION` (predefinito: `us-east-1`)  
  
## Per iniziare

Scegli il metodo di autenticazione preferito e segui i passaggi di configurazione.

### Access keys / env vars

**Ideale per:** macchine di sviluppo, CI o host in cui gestisci direttamente le credenziali AWS.

* ### Set AWS credentials on the gateway host

bashCopy code
[code]
    export AWS_ACCESS_KEY_ID="AKIA..."export AWS_SECRET_ACCESS_KEY="..."export AWS_REGION="us-east-1"# Optional:export AWS_SESSION_TOKEN="..."export AWS_PROFILE="your-profile"# Optional (Bedrock API key/bearer token):export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

* ### Add a Bedrock provider and model to your config

Non è richiesto alcun `apiKey`. Configura il provider con `auth: "aws-sdk"`:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock": {        baseUrl: "https://bedrock-runtime.us-east-1.amazonaws.com",        api: "bedrock-converse-stream",        auth: "aws-sdk",        models: [          {            id: "us.anthropic.claude-opus-4-6-v1:0",            name: "Claude Opus 4.6 (Bedrock)",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "amazon-bedrock/us.anthropic.claude-opus-4-6-v1:0" },    },  },}
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list
[/code]

### EC2 instance roles (IMDS)

**Ideale per:** istanze EC2 con un ruolo IAM associato, usando il servizio di metadati dell'istanza per l'autenticazione.

* ### Enable discovery explicitly

Quando usi IMDS, OpenClaw non può rilevare l'autenticazione AWS solo dai marker d'ambiente, quindi devi abilitarla esplicitamente:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1
[/code]

* ### Optionally add an env marker for auto mode

Se vuoi anche che il percorso di rilevamento automatico tramite marker d'ambiente funzioni (per esempio, per le superfici di `openclaw status`):

bashCopy code
[code]
    export AWS_PROFILE=defaultexport AWS_REGION=us-east-1
[/code]

**Non** hai bisogno di una chiave API falsa.

* ### Verify models are discovered

bashCopy code
[code]
    openclaw models list
[/code]

## Rilevamento automatico dei modelli

OpenClaw può rilevare automaticamente i modelli Bedrock che supportano lo **streaming** e l'**output di testo**. Il rilevamento usa `bedrock:ListFoundationModels` e `bedrock:ListInferenceProfiles`, e i risultati vengono memorizzati nella cache (predefinito: 1 ora).

Come viene abilitato il provider implicito:

  * Se `plugins.entries.amazon-bedrock.config.discovery.enabled` è `true`, OpenClaw proverà il rilevamento anche quando non è presente alcun marker d'ambiente AWS.
  * Se `plugins.entries.amazon-bedrock.config.discovery.enabled` non è impostato, OpenClaw aggiunge automaticamente il provider Bedrock implicito solo quando vede uno di questi marker di autenticazione AWS: `AWS_BEARER_TOKEN_BEDROCK`, `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, o `AWS_PROFILE`.
  * Il percorso effettivo di autenticazione del runtime Bedrock usa comunque la catena predefinita dell'AWS SDK, quindi configurazione condivisa, SSO e autenticazione con ruolo dell'istanza IMDS possono funzionare anche quando il rilevamento richiedeva `enabled: true` per l'abilitazione esplicita.


Discovery config options

Le opzioni di configurazione si trovano sotto `plugins.entries.amazon-bedrock.config.discovery`:

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          discovery: {            enabled: true,            region: "us-east-1",            providerFilter: ["anthropic", "amazon"],            refreshInterval: 3600,            defaultContextWindow: 32000,            defaultMaxTokens: 4096,          },        },      },    },  },}
[/code]

Opzione | Predefinito | Descrizione  
---|---|---  
`enabled` | auto | In modalità automatica, OpenClaw abilita il provider Bedrock implicito solo quando vede un marker d'ambiente AWS supportato. Imposta `true` per forzare il rilevamento.  
`region` | `AWS_REGION` / `AWS_DEFAULT_REGION` / `us-east-1` | Regione AWS usata per le chiamate API di rilevamento.  
`providerFilter` | (tutti) | Corrisponde ai nomi dei provider Bedrock (per esempio `anthropic`, `amazon`).  
`refreshInterval` | `3600` | Durata della cache in secondi. Imposta a `0` per disabilitare la cache.  
`defaultContextWindow` | `32000` | Finestra di contesto usata per i modelli rilevati (sovrascrivila se conosci i limiti del tuo modello).  
`defaultMaxTokens` | `4096` | Token massimi di output usati per i modelli rilevati (sovrascrivili se conosci i limiti del tuo modello).  
  
## Configurazione rapida (percorso AWS)

Questa procedura guidata crea un ruolo IAM, associa le autorizzazioni Bedrock, associa il profilo dell'istanza e abilita il rilevamento OpenClaw sull'host EC2.

bashCopy code
[code]
    # 1. Create IAM role and instance profileaws iam create-role --role-name EC2-Bedrock-Access \  --assume-role-policy-document '{    "Version": "2012-10-17",    "Statement": [{      "Effect": "Allow",      "Principal": {"Service": "ec2.amazonaws.com"},      "Action": "sts:AssumeRole"    }]  }' aws iam attach-role-policy --role-name EC2-Bedrock-Access \  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess aws iam create-instance-profile --instance-profile-name EC2-Bedrock-Accessaws iam add-role-to-instance-profile \  --instance-profile-name EC2-Bedrock-Access \  --role-name EC2-Bedrock-Access # 2. Attach to your EC2 instanceaws ec2 associate-iam-instance-profile \  --instance-id i-xxxxx \  --iam-instance-profile Name=EC2-Bedrock-Access # 3. On the EC2 instance, enable discovery explicitlyopenclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1 # 4. Optional: add an env marker if you want auto mode without explicit enableecho 'export AWS_PROFILE=default' >> ~/.bashrcecho 'export AWS_REGION=us-east-1' >> ~/.bashrcsource ~/.bashrc # 5. Verify models are discoveredopenclaw models list
[/code]

## Configurazione avanzata

Inference profiles

OpenClaw rileva i **profili di inferenza regionali e globali** insieme ai foundation model. Quando un profilo viene mappato a un foundation model noto, il profilo eredita le capacità di quel modello (finestra di contesto, token massimi, reasoning, visione) e viene inserita automaticamente la regione corretta della richiesta Bedrock. Questo significa che i profili Claude cross-region funzionano senza override manuali del provider.

Gli ID dei profili di inferenza hanno la forma `us.anthropic.claude-opus-4-6-v1:0` (regionali) o `anthropic.claude-opus-4-6-v1:0` (globali). Se il modello sottostante è già nei risultati del rilevamento, il profilo eredita il suo set completo di capacità; altrimenti vengono applicati valori predefiniti sicuri.

Non è necessaria alcuna configurazione aggiuntiva. Finché il rilevamento è abilitato e il principale IAM ha `bedrock:ListInferenceProfiles`, i profili appaiono insieme ai foundation model in `openclaw models list`.

Service tier

Alcuni modelli Bedrock supportano un parametro `service_tier` per ottimizzare costo o latenza. Sono disponibili i seguenti livelli:

Livello | Descrizione  
---|---  
`default` | Livello Bedrock standard  
`flex` | Elaborazione scontata per carichi di lavoro che possono tollerare una latenza più lunga  
`priority` | Elaborazione prioritaria per carichi di lavoro sensibili alla latenza  
`reserved` | Capacità riservata per carichi di lavoro stabili  
  
Imposta `serviceTier` (o `service_tier`) tramite `agents.defaults.params` per le richieste ai modelli Bedrock, oppure per singolo modello in `agents.defaults.models["<model-key>"].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      params: {        serviceTier: "flex", // applies to all models      },      models: {        "amazon-bedrock/mistral.mistral-large-3-675b-instruct": {          params: {            serviceTier: "priority", // per-model override          },        },      },    },  },}
[/code]

I valori validi sono `default`, `flex`, `priority` e `reserved`. Non tutti i modelli supportano tutti i livelli: se viene richiesto un livello non supportato, Bedrock restituirà un errore di validazione. Nota: il messaggio di errore è alquanto fuorviante; potrebbe dire "The provided model identifier is invalid" invece di indicare un livello di servizio non supportato. Se vedi questo errore, controlla se il modello supporta il livello richiesto.

Claude Opus 4.7 temperature

Bedrock rifiuta il parametro `temperature` per Claude Opus 4.7. OpenClaw omette automaticamente `temperature` per qualsiasi riferimento Bedrock a Opus 4.7, inclusi ID dei foundation model, profili di inferenza denominati, profili di inferenza applicativi il cui modello sottostante viene risolto in Opus 4.7 tramite `bedrock:GetInferenceProfile`, e varianti puntate `opus-4.7` con prefissi di regione opzionali (`us.`, `eu.`, `ap.`, `apac.`, `au.`, `jp.`, `global.`). Non è richiesta alcuna manopola di configurazione, e l'omissione si applica sia all'oggetto delle opzioni della richiesta sia al campo payload `inferenceConfig`.

Guardrail

Puoi applicare gli [Amazon Bedrock Guardrails](<https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>) a tutte le invocazioni dei modelli Bedrock aggiungendo un oggetto `guardrail` alla configurazione del plugin `amazon-bedrock`. I guardrail consentono di applicare il filtro dei contenuti, il rifiuto di argomenti, filtri di parole, filtri per informazioni sensibili e controlli di ancoraggio contestuale.

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          guardrail: {            guardrailIdentifier: "abc123", // guardrail ID or full ARN            guardrailVersion: "1", // version number or "DRAFT"            streamProcessingMode: "sync", // optional: "sync" or "async"            trace: "enabled", // optional: "enabled", "disabled", or "enabled_full"          },        },      },    },  },}
[/code]

Opzione | Obbligatorio | Descrizione  
---|---|---  
`guardrailIdentifier` | Sì | ID del guardrail (ad es. `abc123`) o ARN completo (ad es. `arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123`).  
`guardrailVersion` | Sì | Numero di versione pubblicata, oppure `"DRAFT"` per la bozza di lavoro.  
`streamProcessingMode` | No | `"sync"` o `"async"` per la valutazione del guardrail durante lo streaming. Se omesso, Bedrock usa il suo valore predefinito.  
`trace` | No | `"enabled"` o `"enabled_full"` per il debug; ometti o imposta `"disabled"` per la produzione.  
Embedding per la ricerca in memoria

Bedrock può anche fungere da provider di embedding per la [ricerca in memoria](</it/concepts/memory-search>). Questa opzione è configurata separatamente dal provider di inferenza: imposta `agents.defaults.memorySearch.provider` su `"bedrock"`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0", // default      },    },  },}
[/code]

Gli embedding di Bedrock usano la stessa catena di credenziali dell'AWS SDK usata per l'inferenza (ruoli di istanza, SSO, chiavi di accesso, configurazione condivisa e identità web). Non è necessaria alcuna chiave API. Quando `provider` è `"auto"`, Bedrock viene rilevato automaticamente se tale catena di credenziali viene risolta correttamente.

I modelli di embedding supportati includono Amazon Titan Embed (v1, v2), Amazon Nova Embed, Cohere Embed (v3, v4) e TwelveLabs Marengo. Consulta il [riferimento alla configurazione della memoria -- Bedrock](</it/reference/memory-config#bedrock-embedding-config>) per l'elenco completo dei modelli e le opzioni sulle dimensioni.

Note e avvertenze

  * Bedrock richiede **l'accesso ai modelli** abilitato nel tuo account/regione AWS.
  * Il rilevamento automatico richiede le autorizzazioni `bedrock:ListFoundationModels` e `bedrock:ListInferenceProfiles`.
  * Se ti affidi alla modalità automatica, imposta uno dei marker env di autenticazione AWS supportati sull'host del Gateway. Se preferisci l'autenticazione IMDS/configurazione condivisa senza marker env, imposta `plugins.entries.amazon-bedrock.config.discovery.enabled: true`.
  * OpenClaw espone l'origine delle credenziali in questo ordine: `AWS_BEARER_TOKEN_BEDROCK`, poi `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, poi `AWS_PROFILE`, quindi la catena AWS SDK predefinita.
  * Il supporto al ragionamento dipende dal modello; consulta la scheda del modello Bedrock per le capacità attuali.
  * Se preferisci un flusso con chiave gestita, puoi anche collocare un proxy compatibile con OpenAI davanti a Bedrock e configurarlo invece come provider OpenAI.


## Correlati

[**Selezione del modello** Scelta dei provider, dei riferimenti ai modelli e del comportamento di failover. ](</it/concepts/model-providers>) [**Ricerca in memoria** Configurazione degli embedding Bedrock per la ricerca in memoria. ](</it/concepts/memory-search>) [**Riferimento alla configurazione della memoria** Elenco completo dei modelli di embedding Bedrock e opzioni sulle dimensioni. ](</it/reference/memory-config#bedrock-embedding-config>) [**Risoluzione dei problemi** Risoluzione generale dei problemi e FAQ. ](</it/help/troubleshooting>)

Was this useful?YesNo