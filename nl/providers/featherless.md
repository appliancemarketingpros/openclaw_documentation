---
title: Featherless AI
source_url: https://docs.openclaw.ai/nl/providers/featherless
scraped_at: 2026-07-13
---

ModelsProviders

[Featherless AI](<https://featherless.ai>) biedt open modellen aan via een OpenAI-compatibele API. OpenClaw installeert Featherless als een officiële externe providerplugin en houdt de ingebouwde catalogus klein, terwijl tijdens runtime exacte model-id's van Featherless worden geaccepteerd.

Eigenschap | Waarde  
---|---  
Provider-id | `featherless`  
Pakket | `@openclaw/featherless-provider`  
Omgevingsvariabele voor authenticatie | `FEATHERLESS_API_KEY`  
Onboardingvlag | `--auth-choice featherless-api-key`  
Directe CLI-vlag | `--featherless-api-key <key>`  
API | OpenAI-compatibel (`openai-completions`)  
Basis-URL | `https://api.featherless.ai/v1`  
Standaardmodel | `featherless/Qwen/Qwen3-32B`  
  
## Configuratie

Installeer de plugin en start de Gateway opnieuw:

bashCopy code
[code]
    openclaw plugins install @openclaw/featherless-provideropenclaw gateway restart
[/code]

Voer de onboarding uit:

bashCopy code
[code]
    openclaw onboard --auth-choice featherless-api-key
[/code]

Voor niet-interactieve configuratie:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice featherless-api-key \  --featherless-api-key "$FEATHERLESS_API_KEY"
[/code]

Of stel de sleutel beschikbaar aan het Gateway-proces:

bashCopy code
[code]
    export FEATHERLESS_API_KEY="<your-featherless-api-key>" # pragma: allowlist secret
[/code]

Controleer de provider:

bashCopy code
[code]
    openclaw models list --provider featherless
[/code]

## Standaardmodel

De plugin gebruikt `Qwen/Qwen3-32B` als standaardmodel voor de configuratie, omdat Featherless native toolaanroepen voor de Qwen 3-familie documenteert. OpenClaw configureert het contextvenster van 32.768 tokens, een conservatieve uitvoerlimiet van 4.096 tokens en de denkbesturing van de Qwen-chatsjabloon.

De kostenvelden in de catalogus zijn nul, omdat Featherless meerdere factureringsmodi ondersteunt en OpenClaw geen accountspecifieke abonnements- of tariefgegevens per aanvraag insluit.

## Andere Featherless-modellen

Gebruik de exacte model-id van Featherless na het providerprefix `featherless/`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "featherless/moonshotai/Kimi-K2-Instruct",      },    },  },}
[/code]

OpenClaw kopieert bewust niet de volledige openbare modelindex van Featherless naar de keuzelijst. De index is groot en bevat onvoldoende gestructureerde metadata over mogelijkheden om elk tekst-, visie-, embedding- en redeneermodel veilig te classificeren. Onbekende id's worden daarom verwerkt met conservatieve standaardinstellingen voor alleen tekst, zonder redeneren: een contextvenster van 4.096 tokens en een uitvoerlimiet van 1.024 tokens.

Voeg een expliciete modelvermelding voor de provider toe wanneer een model andere metadata nodig heeft:

json5Copy code
[code]
    {  models: {    mode: "merge",    providers: {      featherless: {        baseUrl: "https://api.featherless.ai/v1",        apiKey: "${FEATHERLESS_API_KEY}",        api: "openai-completions",        models: [          {            id: "google/gemma-3-27b-it",            name: "Gemma 3 27B",            input: ["text", "image"],            reasoning: false,            contextWindow: 32768,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

Controleer de modelcatalogus van Featherless op de actuele beschikbaarheid van modellen en mogelijkheidslabels voordat u aangepaste metadata toevoegt.

## Probleemoplossing

  * `401` of `403`: controleer of `FEATHERLESS_API_KEY` zichtbaar is voor het Gateway-proces of voer de onboarding opnieuw uit.
  * Onbekend model: gebruik na het prefix `featherless/` de exacte hoofdlettergevoelige id van Featherless.
  * Toolaanroepen worden als tekst geretourneerd: kies een modelfamilie waarvoor Featherless native functieaanroepen documenteert, zoals Qwen 3.
  * Beheerde Gateway kan de sleutel niet zien: plaats deze in `~/.openclaw/.env` of een andere omgevingsbron die door de service wordt geladen en start vervolgens de Gateway opnieuw.


## Gerelateerd

  * [Modelproviders](</nl/concepts/model-providers>)
  * [Alle providers](</nl/providers>)
  * [Denkmodi](</nl/tools/thinking>)


Was this useful?YesNo

Open issue