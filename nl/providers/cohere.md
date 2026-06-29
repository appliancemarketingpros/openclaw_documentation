---
title: Cohere
source_url: https://docs.openclaw.ai/nl/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) biedt OpenAI-compatibele inferentie via de compatibiliteits-API. OpenClaw levert de Cohere-provider tijdens de overgang naar externalisatie en publiceert deze ook als officiële externe plugin met de modelcatalogus van Command A.

Eigenschap | Waarde  
---|---  
Provider-id | `cohere`  
Plugin | gebundeld tijdens overgang; officieel extern pakket  
Auth-env-var | `COHERE_API_KEY`  
Onboarding-vlag | `--auth-choice cohere-api-key`  
Directe CLI-vlag | `--cohere-api-key <key>`  
API | OpenAI-compatibel (`openai-completions`)  
Basis-URL | `https://api.cohere.ai/compatibility/v1`  
Standaardmodel | `cohere/command-a-03-2025`  
  
## Aan de slag

  1. Cohere is opgenomen in huidige OpenClaw-pakketten. Als het niet beschikbaar is, installeer dan het externe pakket en herstart de Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Maak een Cohere-API-sleutel.
  3. Voer onboarding uit:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Controleer of de catalogus beschikbaar is:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

Het standaardmodel wordt alleen ingesteld wanneer er nog geen primair model is geconfigureerd.

## Setup alleen via omgeving

Maak `COHERE_API_KEY` beschikbaar voor het Gateway-proces en selecteer daarna het Cohere-model:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## Gerelateerd

  * [Modelproviders](</nl/concepts/model-providers>)
  * [Modellen-CLI](</nl/cli/models>)
  * [Providerdirectory](</nl/providers>)


Was this useful?YesNo

Open issue