---
title: Amazon Bedrock Mantle
source_url: https://docs.openclaw.ai/nl/providers/bedrock-mantle
scraped_at: 2026-05-25
---

OpenClaw bevat een gebundelde **Amazon Bedrock Mantle** -provider die verbinding maakt met het OpenAI-compatibele Mantle-eindpunt. Mantle host open-source- en externe modellen (GPT-OSS, Qwen, Kimi, GLM en vergelijkbare) via een standaard `/v1/chat/completions`-surface, ondersteund door Bedrock-infrastructuur.

Eigenschap | Waarde  
---|---  
Provider-ID | `amazon-bedrock-mantle`  
API | `openai-completions` (OpenAI-compatibel) of `anthropic-messages` (Anthropic Messages-route)  
Authenticatie | Expliciete `AWS_BEARER_TOKEN_BEDROCK` of bearer-token-generatie via IAM-credentialketen  
Standaardregio | `us-east-1` (overschrijven met `AWS_REGION` of `AWS_DEFAULT_REGION`)  
  
## Aan de slag

Kies je gewenste authenticatiemethode en volg de installatiestappen.

### Expliciet bearer-token

**Het meest geschikt voor:** omgevingen waarin je al een Mantle bearer-token hebt.

* ### Stel het bearer-token in op de Gateway-host

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

Stel eventueel een regio in (standaard `us-east-1`):

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### Controleer of modellen worden ontdekt

bashCopy code
[code]
    openclaw models list
[/code]

Ontdekte modellen verschijnen onder de provider `amazon-bedrock-mantle`. Er is geen aanvullende configuratie vereist, tenzij je standaardwaarden wilt overschrijven.

### IAM-credentials

**Het meest geschikt voor:** gebruik van AWS SDK-compatibele credentials (gedeelde configuratie, SSO, webidentiteit, instance- of taakrollen).

* ### Configureer AWS-credentials op de Gateway-host

Elke AWS SDK-compatibele authenticatiebron werkt:

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### Controleer of modellen worden ontdekt

bashCopy code
[code]
    openclaw models list
[/code]

OpenClaw genereert automatisch een Mantle bearer-token vanuit de credentialketen.

## Automatische modeldetectie

Wanneer `AWS_BEARER_TOKEN_BEDROCK` is ingesteld, gebruikt OpenClaw het direct. Anders probeert OpenClaw een Mantle bearer-token te genereren vanuit de standaard AWS-credentialketen. Daarna worden beschikbare Mantle-modellen ontdekt door het `/v1/models`-eindpunt van de regio op te vragen.

Gedrag | Detail  
---|---  
Detectiecache | Resultaten 1 uur gecachet  
IAM-tokenverversing | Elk uur  
  
Als je de Mantle-Plugin ingeschakeld wilt houden maar automatische detectie en IAM bearer-token-generatie wilt onderdrukken, schakel je de detectieschakelaar van de Plugin uit:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### Ondersteunde regio’s

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## Handmatige configuratie

Als je expliciete configuratie verkiest boven automatische detectie:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Geavanceerde configuratie

Ondersteuning voor reasoning

Ondersteuning voor reasoning wordt afgeleid uit model-ID’s die patronen bevatten zoals `thinking`, `reasoner` of `gpt-oss-120b`. OpenClaw stelt tijdens detectie automatisch `reasoning: true` in voor overeenkomende modellen.

Niet-beschikbaarheid van eindpunt

Als het Mantle-eindpunt niet beschikbaar is of geen modellen retourneert, wordt de provider stilzwijgend overgeslagen. OpenClaw geeft geen fout; andere geconfigureerde providers blijven normaal werken.

Claude Opus 4.7 via de Anthropic Messages-route

Mantle biedt ook een Anthropic Messages-route die Claude-modellen via hetzelfde met bearer-authenticatie beveiligde streamingpad doorgeeft. Claude Opus 4.7 (`amazon-bedrock-mantle/claude-opus-4.7`) kan via deze route worden aangeroepen met streaming die eigendom is van de provider, zodat AWS bearer-tokens niet worden behandeld als Anthropic API-sleutels.

Wanneer je een Anthropic Messages-model vastzet op de Mantle-provider, gebruikt OpenClaw voor dat model de `anthropic-messages`-API-surface in plaats van `openai-completions`. Authenticatie komt nog steeds van `AWS_BEARER_TOKEN_BEDROCK` (of het aangemaakte IAM bearer-token).

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Relatie tot de Amazon Bedrock-provider

Bedrock Mantle is een afzonderlijke provider naast de standaard [Amazon Bedrock](</nl/providers/bedrock>)-provider. Mantle gebruikt een OpenAI-compatibele `/v1`-surface, terwijl de standaard Bedrock-provider de native Bedrock-API gebruikt.

Beide providers delen dezelfde `AWS_BEARER_TOKEN_BEDROCK`-credential wanneer deze aanwezig is.

## Gerelateerd

[**Amazon Bedrock** Native Bedrock-provider voor Anthropic Claude, Titan en andere modellen. ](</nl/providers/bedrock>) [**Modelselectie** Providers, modelrefs en failover-gedrag kiezen. ](</nl/concepts/model-providers>) [**OAuth en authenticatie** Authenticatiedetails en regels voor hergebruik van credentials. ](</nl/gateway/authentication>) [**Probleemoplossing** Veelvoorkomende problemen en hoe je ze oplost. ](</nl/help/troubleshooting>)

Was this useful?YesNo