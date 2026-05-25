---
title: OpenCode
source_url: https://docs.openclaw.ai/nl/providers/opencode
scraped_at: 2026-05-25
---

OpenCode biedt twee gehoste catalogi aan in OpenClaw:

Catalogus | Voorvoegsel | Runtimeprovider  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
Beide catalogi gebruiken dezelfde OpenCode API-sleutel. OpenClaw houdt de runtimeprovider-id's gescheiden zodat upstream-routering per model correct blijft, maar onboarding en documentatie behandelen ze als één OpenCode-configuratie.

## Aan de slag

### Zen-catalogus

**Het meest geschikt voor:** de gecureerde OpenCode multi-modelproxy (Claude, GPT, Gemini).

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

Of geef de sleutel direct door:

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### Een Zen-model als standaard instellen

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### Controleren of modellen beschikbaar zijn

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Go-catalogus

**Het meest geschikt voor:** de door OpenCode gehoste Kimi-, GLM- en MiniMax-reeks.

* ### Onboarding uitvoeren

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

Of geef de sleutel direct door:

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### Een Go-model als standaard instellen

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### Controleren of modellen beschikbaar zijn

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## Configuratievoorbeeld

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## Ingebouwde catalogi

### Zen

Eigenschap | Waarde  
---|---  
Runtimeprovider | `opencode`  
Voorbeeldmodellen | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

Eigenschap | Waarde  
---|---  
Runtimeprovider | `opencode-go`  
Voorbeeldmodellen | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## Geavanceerde configuratie

API-sleutelaliassen

`OPENCODE_ZEN_API_KEY` wordt ook ondersteund als alias voor `OPENCODE_API_KEY`.

Gedeelde inloggegevens

Als u tijdens de installatie één OpenCode-sleutel invoert, worden inloggegevens voor beide runtimeproviders opgeslagen. U hoeft niet voor elke catalogus afzonderlijk onboarding uit te voeren.

Facturering en dashboard

U meldt zich aan bij OpenCode, voegt factureringsgegevens toe en kopieert uw API-sleutel. Facturering en beschikbaarheid van catalogi worden beheerd vanuit het OpenCode-dashboard.

Gemini-replaygedrag

Door Gemini ondersteunde OpenCode-verwijzingen blijven op het proxy-Gemini-pad, dus OpenClaw houdt Gemini-sanitatie van gedachtehandtekeningen daar actief zonder native Gemini-replayvalidatie of bootstrap-herschrijvingen in te schakelen.

Niet-Gemini-replaygedrag

Niet-Gemini OpenCode-verwijzingen behouden het minimale OpenAI-compatibele replaybeleid.

## Gerelateerd

[**Modelselectie** Providers, modelverwijzingen en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Configuratiereferentie** Volledige configuratiereferentie voor agents, modellen en providers. ](</nl/gateway/configuration-reference>)

Was this useful?YesNo