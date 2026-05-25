---
title: Amazon Bedrock
source_url: https://docs.openclaw.ai/nl/providers/bedrock
scraped_at: 2026-05-25
---

OpenClaw kan **Amazon Bedrock** -modellen gebruiken via pi-ai's **Bedrock Converse** streamingprovider. Bedrock-authenticatie gebruikt de **AWS SDK default credential chain** , niet een API-sleutel.

Eigenschap | Waarde  
---|---  
Provider | `amazon-bedrock`  
API | `bedrock-converse-stream`  
Authenticatie | AWS-referenties (env-vars, gedeelde config, of instantierol)  
Regio | `AWS_REGION` of `AWS_DEFAULT_REGION` (standaard: `us-east-1`)  
  
## Aan de slag

Kies je gewenste authenticatiemethode en volg de installatiestappen.

### Toegangssleutels / env-vars

**Beste voor:** ontwikkelmachines, CI, of hosts waarop je AWS-referenties rechtstreeks beheert.

* ### Stel AWS-referenties in op de Gateway-host

bashCopy code
[code]
    export AWS_ACCESS_KEY_ID="AKIA..."export AWS_SECRET_ACCESS_KEY="..."export AWS_REGION="us-east-1"# Optional:export AWS_SESSION_TOKEN="..."export AWS_PROFILE="your-profile"# Optional (Bedrock API key/bearer token):export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

* ### Voeg een Bedrock-provider en model toe aan je config

Er is geen `apiKey` vereist. Configureer de provider met `auth: "aws-sdk"`:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock": {        baseUrl: "https://bedrock-runtime.us-east-1.amazonaws.com",        api: "bedrock-converse-stream",        auth: "aws-sdk",        models: [          {            id: "us.anthropic.claude-opus-4-6-v1:0",            name: "Claude Opus 4.6 (Bedrock)",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "amazon-bedrock/us.anthropic.claude-opus-4-6-v1:0" },    },  },}
[/code]

* ### Controleer of modellen beschikbaar zijn

bashCopy code
[code]
    openclaw models list
[/code]

### EC2-instantierollen (IMDS)

**Beste voor:** EC2-instanties waaraan een IAM-rol is gekoppeld, met de instance metadata service voor authenticatie.

* ### Schakel ontdekking expliciet in

Wanneer je IMDS gebruikt, kan OpenClaw AWS-authenticatie niet alleen op basis van env-markers detecteren, dus je moet expliciet kiezen:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1
[/code]

* ### Voeg optioneel een env-marker toe voor automatische modus

Als je ook wilt dat het pad voor automatische env-marker-detectie werkt (bijvoorbeeld voor `openclaw status`-oppervlakken):

bashCopy code
[code]
    export AWS_PROFILE=defaultexport AWS_REGION=us-east-1
[/code]

Je hebt **geen** nep-API-sleutel nodig.

* ### Controleer of modellen worden ontdekt

bashCopy code
[code]
    openclaw models list
[/code]

## Automatische modelontdekking

OpenClaw kan automatisch Bedrock-modellen ontdekken die **streaming** en **tekstuitvoer** ondersteunen. Ontdekking gebruikt `bedrock:ListFoundationModels` en `bedrock:ListInferenceProfiles`, en resultaten worden gecachet (standaard: 1 uur).

Zo wordt de impliciete provider ingeschakeld:

  * Als `plugins.entries.amazon-bedrock.config.discovery.enabled` `true` is, probeert OpenClaw discovery zelfs wanneer er geen AWS-env-marker aanwezig is.
  * Als `plugins.entries.amazon-bedrock.config.discovery.enabled` niet is ingesteld, voegt OpenClaw de impliciete Bedrock-provider alleen automatisch toe wanneer het een van deze AWS-auth-markers ziet: `AWS_BEARER_TOKEN_BEDROCK`, `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, of `AWS_PROFILE`.
  * Het daadwerkelijke auth-pad van de Bedrock-runtime gebruikt nog steeds de standaardketen van de AWS SDK, zodat gedeelde configuratie, SSO en IMDS-instance-role-auth kunnen werken, zelfs wanneer discovery `enabled: true` nodig had om in te schrijven.


Discovery-configuratieopties

Configuratieopties staan onder `plugins.entries.amazon-bedrock.config.discovery`:

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          discovery: {            enabled: true,            region: "us-east-1",            providerFilter: ["anthropic", "amazon"],            refreshInterval: 3600,            defaultContextWindow: 32000,            defaultMaxTokens: 4096,          },        },      },    },  },}
[/code]

Optie | Standaardwaarde | Beschrijving  
---|---|---  
`enabled` | auto | In automatische modus schakelt OpenClaw de impliciete Bedrock-provider alleen in wanneer het een ondersteunde AWS-env-marker ziet. Stel in op `true` om discovery af te dwingen.  
`region` | `AWS_REGION` / `AWS_DEFAULT_REGION` / `us-east-1` | AWS-regio die wordt gebruikt voor discovery-API-aanroepen.  
`providerFilter` | (alle) | Komt overeen met Bedrock-providernamen (bijvoorbeeld `anthropic`, `amazon`).  
`refreshInterval` | `3600` | Cacheduur in seconden. Stel in op `0` om caching uit te schakelen.  
`defaultContextWindow` | `32000` | Contextvenster dat wordt gebruikt voor gevonden modellen (overschrijf dit als je de limieten van je model kent).  
`defaultMaxTokens` | `4096` | Maximale outputtokens die worden gebruikt voor gevonden modellen (overschrijf dit als je de limieten van je model kent).  
  
## Snelle configuratie (AWS-pad)

Deze walkthrough maakt een IAM-rol aan, koppelt Bedrock-machtigingen, associeert het instance profile en schakelt OpenClaw-discovery in op de EC2-host.

bashCopy code
[code]
    # 1. Create IAM role and instance profileaws iam create-role --role-name EC2-Bedrock-Access \  --assume-role-policy-document '{    "Version": "2012-10-17",    "Statement": [{      "Effect": "Allow",      "Principal": {"Service": "ec2.amazonaws.com"},      "Action": "sts:AssumeRole"    }]  }' aws iam attach-role-policy --role-name EC2-Bedrock-Access \  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess aws iam create-instance-profile --instance-profile-name EC2-Bedrock-Accessaws iam add-role-to-instance-profile \  --instance-profile-name EC2-Bedrock-Access \  --role-name EC2-Bedrock-Access # 2. Attach to your EC2 instanceaws ec2 associate-iam-instance-profile \  --instance-id i-xxxxx \  --iam-instance-profile Name=EC2-Bedrock-Access # 3. On the EC2 instance, enable discovery explicitlyopenclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1 # 4. Optional: add an env marker if you want auto mode without explicit enableecho 'export AWS_PROFILE=default' >> ~/.bashrcecho 'export AWS_REGION=us-east-1' >> ~/.bashrcsource ~/.bashrc # 5. Verify models are discoveredopenclaw models list
[/code]

## Geavanceerde configuratie

Inference profiles

OpenClaw ontdekt **regionale en globale inference profiles** naast foundation models. Wanneer een profiel naar een bekend foundation model verwijst, erft het profiel de mogelijkheden van dat model (contextvenster, maximale tokens, reasoning, vision) en wordt de juiste Bedrock-aanvraagregio automatisch geïnjecteerd. Dit betekent dat Claude-profielen voor meerdere regio's werken zonder handmatige provider-overschrijvingen.

Inference profile-ID's zien eruit als `us.anthropic.claude-opus-4-6-v1:0` (regionaal) of `anthropic.claude-opus-4-6-v1:0` (globaal). Als het onderliggende model al in de discovery-resultaten staat, erft het profiel de volledige set mogelijkheden; anders worden veilige standaardwaarden toegepast.

Er is geen extra configuratie nodig. Zolang discovery is ingeschakeld en de IAM principal `bedrock:ListInferenceProfiles` heeft, verschijnen profielen naast foundation models in `openclaw models list`.

Serviceniveau

Sommige Bedrock-modellen ondersteunen een parameter `service_tier` om te optimaliseren voor kosten of latency. De volgende niveaus zijn beschikbaar:

Niveau | Beschrijving  
---|---  
`default` | Standaard Bedrock-niveau  
`flex` | Verwerking met korting voor workloads die langere latency kunnen verdragen  
`priority` | Geprioriteerde verwerking voor latencygevoelige workloads  
`reserved` | Gereserveerde capaciteit voor workloads met een stabiele belasting  
  
Stel `serviceTier` (of `service_tier`) in via `agents.defaults.params` voor Bedrock-modelaanvragen, of per model in `agents.defaults.models["<model-key>"].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      params: {        serviceTier: "flex", // applies to all models      },      models: {        "amazon-bedrock/mistral.mistral-large-3-675b-instruct": {          params: {            serviceTier: "priority", // per-model override          },        },      },    },  },}
[/code]

Geldige waarden zijn `default`, `flex`, `priority` en `reserved`. Niet alle modellen ondersteunen alle niveaus — als een niet-ondersteund niveau wordt aangevraagd, retourneert Bedrock een validatiefout. Let op: het foutbericht is enigszins misleidend; het kan "The provided model identifier is invalid" zeggen in plaats van een niet-ondersteund serviceniveau aan te geven. Als je deze fout ziet, controleer dan of het model het aangevraagde niveau ondersteunt.

Claude Opus 4.7-temperatuur

Bedrock wijst de parameter `temperature` af voor Claude Opus 4.7. OpenClaw laat `temperature` automatisch weg voor elke Opus 4.7-Bedrock-ref, inclusief foundation model-ID's, benoemde inference profiles, application inference profiles waarvan het onderliggende model via `bedrock:GetInferenceProfile` wordt opgelost naar Opus 4.7, en gestippelde `opus-4.7`-varianten met optionele regioprefixen (`us.`, `eu.`, `ap.`, `apac.`, `au.`, `jp.`, `global.`). Er is geen configuratieknop vereist, en de weglating geldt voor zowel het object met aanvraagopties als het payloadveld `inferenceConfig`.

Guardrails

Je kunt [Amazon Bedrock Guardrails](<https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>) toepassen op alle Bedrock-modelaanroepen door een `guardrail`-object toe te voegen aan de Plugin-configuratie van `amazon-bedrock`. Guardrails laten je inhoudsfiltering, onderwerpweigering, woordfilters, filters voor gevoelige informatie en controles op contextuele grounding afdwingen.

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          guardrail: {            guardrailIdentifier: "abc123", // guardrail ID or full ARN            guardrailVersion: "1", // version number or "DRAFT"            streamProcessingMode: "sync", // optional: "sync" or "async"            trace: "enabled", // optional: "enabled", "disabled", or "enabled_full"          },        },      },    },  },}
[/code]

Optie | Vereist | Beschrijving  
---|---|---  
`guardrailIdentifier` | Ja | Guardrail-ID (bijv. `abc123`) of volledige ARN (bijv. `arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123`).  
`guardrailVersion` | Ja | Gepubliceerd versienummer, of `"DRAFT"` voor het werkconcept.  
`streamProcessingMode` | Nee | `"sync"` of `"async"` voor guardrail-evaluatie tijdens streaming. Als dit wordt weggelaten, gebruikt Bedrock de standaardinstelling.  
`trace` | Nee | `"enabled"` of `"enabled_full"` voor foutopsporing; laat weg of stel in op `"disabled"` voor productie.  
Embeddings voor geheugenzoekopdrachten

Bedrock kan ook dienen als embeddingprovider voor [geheugenzoekopdrachten](</nl/concepts/memory-search>). Dit wordt afzonderlijk van de inferentieprovider geconfigureerd -- stel `agents.defaults.memorySearch.provider` in op `"bedrock"`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0", // default      },    },  },}
[/code]

Bedrock-embeddings gebruiken dezelfde AWS SDK-referentieketen als inferentie (instantie- rollen, SSO, toegangssleutels, gedeelde configuratie en webidentiteit). Er is geen API-sleutel nodig. Wanneer `provider` `"auto"` is, wordt Bedrock automatisch gedetecteerd als die referentieketen succesvol wordt opgelost.

Ondersteunde embeddingmodellen zijn onder meer Amazon Titan Embed (v1, v2), Amazon Nova Embed, Cohere Embed (v3, v4) en TwelveLabs Marengo. Zie [Referentie voor geheugenconfiguratie -- Bedrock](</nl/reference/memory-config#bedrock-embedding-config>) voor de volledige modellijst en dimensieopties.

Opmerkingen en kanttekeningen

  * Bedrock vereist dat **modeltoegang** is ingeschakeld in je AWS-account/regio.
  * Automatische ontdekking vereist de machtigingen `bedrock:ListFoundationModels` en `bedrock:ListInferenceProfiles`.
  * Als je op automatische modus vertrouwt, stel dan een van de ondersteunde AWS-auth-env-markeringen in op de Gateway-host. Als je IMDS/gedeelde-config-auth zonder env-markeringen verkiest, stel dan `plugins.entries.amazon-bedrock.config.discovery.enabled: true` in.
  * OpenClaw toont de referentiebron in deze volgorde: `AWS_BEARER_TOKEN_BEDROCK`, daarna `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, daarna `AWS_PROFILE`, daarna de standaard AWS SDK-keten.
  * Ondersteuning voor redeneren is afhankelijk van het model; controleer de Bedrock-modelkaart voor actuele mogelijkheden.
  * Als je een beheerde sleutelstroom verkiest, kun je ook een OpenAI-compatibele proxy voor Bedrock plaatsen en deze in plaats daarvan configureren als OpenAI-provider.


## Gerelateerd

[**Modelselectie** Providers, modelreferenties en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Geheugenzoekopdrachten** Bedrock-embeddings voor configuratie van geheugenzoekopdrachten. ](</nl/concepts/memory-search>) [**Referentie voor geheugenconfiguratie** Volledige lijst met Bedrock-embeddingmodellen en dimensieopties. ](</nl/reference/memory-config#bedrock-embedding-config>) [**Probleemoplossing** Algemene probleemoplossing en veelgestelde vragen. ](</nl/help/troubleshooting>)

Was this useful?YesNo