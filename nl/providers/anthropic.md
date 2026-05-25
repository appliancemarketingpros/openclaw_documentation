---
title: Anthropic
source_url: https://docs.openclaw.ai/nl/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic bouwt de **Claude** -modelfamilie. OpenClaw ondersteunt twee authenticatieroutes:

  * **API-sleutel** — directe toegang tot de Anthropic API met gebruiksgebaseerde facturering (`anthropic/*`-modellen)
  * **Claude CLI** — hergebruik een bestaande Claude CLI-login op dezelfde host


## Aan de slag

### API key

**Beste voor:** standaard API-toegang en gebruiksgebaseerde facturering.

* ### Get your API key

Maak een API-sleutel in de [Anthropic Console](<https://console.anthropic.com/>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

Of geef de sleutel rechtstreeks door:

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Configuratievoorbeeld

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**Beste voor:** een bestaande Claude CLI-login hergebruiken zonder aparte API-sleutel.

* ### Ensure Claude CLI is installed and logged in

Controleer met:

bashCopy code
[code]
    claude --version
[/code]

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw detecteert en hergebruikt de bestaande Claude CLI-inloggegevens.

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### Configuratievoorbeeld

Geef de voorkeur aan de canonieke Anthropic-modelreferentie plus een CLI-runtime-override:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

Verouderde `claude-cli/claude-opus-4-7`-modelreferenties werken nog steeds voor compatibiliteit, maar nieuwe configuratie moet provider-/modelselectie als `anthropic/*` houden en de uitvoeringsbackend in het runtimebeleid voor provider/model zetten.

## Denkstandaarden (Claude 4.6)

Claude 4.6-modellen gebruiken standaard `adaptive`-denken in OpenClaw wanneer er geen expliciet denkniveau is ingesteld.

Overschrijf per bericht met `/think:<level>` of in modelparameters:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## Promptcaching

OpenClaw ondersteunt de promptcachingfunctie van Anthropic voor API-sleutel-authenticatie.

Waarde | Cacheduur | Beschrijving  
---|---|---  
`"short"` (standaard) | 5 minuten | Automatisch toegepast voor API-sleutel-authenticatie  
`"long"` | 1 uur | Uitgebreide cache  
`"none"` | Geen caching | Promptcaching uitschakelen  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

Per-agent cache overrides

Gebruik parameters op modelniveau als je basislijn en overschrijf daarna specifieke agents via `agents.list[].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

Volgorde voor samenvoegen van configuratie:

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params` (overeenkomende `id`, overschrijft per sleutel)


Hierdoor kan één agent een langlevende cache behouden, terwijl een andere agent op hetzelfde model caching uitschakelt voor piekerig verkeer met weinig hergebruik.

Bedrock Claude notes

  * Anthropic Claude-modellen op Bedrock (`amazon-bedrock/*anthropic.claude*`) accepteren `cacheRetention`-doorgifte wanneer geconfigureerd.
  * Niet-Anthropic Bedrock-modellen worden tijdens runtime geforceerd naar `cacheRetention: "none"`.
  * Slimme standaarden voor API-sleutels vullen ook `cacheRetention: "short"` in voor Claude-op-Bedrock-referenties wanneer er geen expliciete waarde is ingesteld.


## Geavanceerde configuratie

Fast mode

De gedeelde `/fast`-schakelaar van OpenClaw ondersteunt direct Anthropic-verkeer (API-sleutel en OAuth naar `api.anthropic.com`).

Opdracht | Wordt toegewezen aan  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

Media understanding (image and PDF)

De meegeleverde Anthropic Plugin registreert begrip van afbeeldingen en PDF's. OpenClaw lost mediacapabilities automatisch op vanuit de geconfigureerde Anthropic-authenticatie; er is geen aanvullende configuratie nodig.

Eigenschap | Waarde  
---|---  
Standaardmodel | `claude-opus-4-7`  
Ondersteunde invoer | Afbeeldingen, PDF-documenten  
  
Wanneer een afbeelding of PDF aan een gesprek wordt gekoppeld, routeert OpenClaw deze automatisch via de Anthropic-provider voor mediabegrip.

1M context window (beta)

Het 1M-contextvenster van Anthropic is beta-gated. Schakel het per model in:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw wijst dit op requests toe aan `anthropic-beta: context-1m-2025-08-07`.

`params.context1m: true` geldt ook voor de Claude CLI-backend (`claude-cli/*`) voor daarvoor geschikte Opus- en Sonnet-modellen, waardoor het runtime- contextvenster voor die CLI-sessies wordt uitgebreid zodat het overeenkomt met het gedrag van de directe API.

Claude Opus 4.7 1M context

`anthropic/claude-opus-4.7` en de bijbehorende `claude-cli`-variant hebben standaard een 1M-context- venster; geen `params.context1m: true` nodig.

## Probleemoplossing

401 errors / token suddenly invalid

Anthropic-tokenauthenticatie verloopt en kan worden ingetrokken. Gebruik voor nieuwe installaties in plaats daarvan een Anthropic API-sleutel.

No API key found for provider "anthropic"

Anthropic-authenticatie is **per agent** — nieuwe agents erven de sleutels van de hoofdagent niet. Voer onboarding opnieuw uit voor die agent (of configureer een API-sleutel op de gatewayhost) en controleer daarna met `openclaw models status`.

No credentials found for profile "anthropic:default"

Voer `openclaw models status` uit om te zien welk auth-profiel actief is. Voer onboarding opnieuw uit of configureer een API-sleutel voor dat profielpad.

No available auth profile (all in cooldown)

Controleer `openclaw models status --json` op `auth.unusableProfiles`. Anthropic-rate-limit-cooldowns kunnen modelspecifiek zijn, dus een verwant Anthropic-model kan nog steeds bruikbaar zijn. Voeg een ander Anthropic-profiel toe of wacht tot de cooldown voorbij is.

## Gerelateerd

[**Model selection** Providers, modelreferenties en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**CLI backends** Installatie- en runtimedetails van de Claude CLI-backend. ](</nl/gateway/cli-backends>) [**Prompt caching** Hoe promptcaching werkt bij providers. ](</nl/reference/prompt-caching>) [**OAuth and auth** Auth-details en regels voor hergebruik van inloggegevens. ](</nl/gateway/authentication>)

Was this useful?YesNo