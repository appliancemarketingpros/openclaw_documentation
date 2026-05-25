---
title: Arcee AI
source_url: https://docs.openclaw.ai/nl/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) biedt toegang tot de Trinity-familie van mixture-of-experts-modellen via een OpenAI-compatibele API. Alle Trinity-modellen hebben een Apache 2.0-licentie.

Arcee AI-modellen zijn rechtstreeks toegankelijk via het Arcee-platform of via [OpenRouter](</nl/providers/openrouter>).

Eigenschap | Waarde  
---|---  
Provider | `arcee`  
Auth | `ARCEEAI_API_KEY` (direct) or `OPENROUTER_API_KEY` (via OpenRouter)  
API | OpenAI-compatibel  
Base-URL | `https://api.arcee.ai/api/v1` (direct) or `https://openrouter.ai/api/v1` (OpenRouter)  
  
## Aan de slag

### Direct (Arcee platform)

* ### Get an API key

Maak een API-sleutel aan bij [Arcee AI](<https://chat.arcee.ai/>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### Via OpenRouter

* ### Get an API key

Maak een API-sleutel aan bij [OpenRouter](<https://openrouter.ai/keys>).

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

Dezelfde modelverwijzingen werken voor zowel directe configuraties als OpenRouter-configuraties (bijvoorbeeld `arcee/trinity-large-thinking`).

## Niet-interactieve configuratie

### Direct (Arcee platform)

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### Via OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## Ingebouwde catalogus

OpenClaw wordt momenteel geleverd met deze gebundelde Arcee-catalogus:

Modelverwijzing | Naam | Invoer | Context | Kosten (in/uit per 1M) | Opmerkingen  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | tekst | 256K | $0.25 / $0.90 | Standaardmodel; redeneren ingeschakeld  
`arcee/trinity-large-preview` | Trinity Large Preview | tekst | 128K | $0.25 / $1.00 | Algemeen gebruik; 400B params, 13B actief  
`arcee/trinity-mini` | Trinity Mini 26B | tekst | 128K | $0.045 / $0.15 | Snel en kostenefficient; function calling  
  
## Ondersteunde functies

Functie | Ondersteund  
---|---  
Streaming | Ja  
Toolgebruik / function calling | Ja (Trinity Mini, Trinity Large Preview)  
Gestructureerde uitvoer (JSON-modus en JSON-schema) | Ja  
Uitgebreid denken | Ja (Trinity Large Thinking; tools uitgeschakeld)  
  
Environment note

Als de Gateway als daemon draait (launchd/systemd), zorg er dan voor dat `ARCEEAI_API_KEY` (of `OPENROUTER_API_KEY`) beschikbaar is voor dat proces (bijvoorbeeld in `~/.openclaw/.env` of via `env.shellEnv`).

OpenRouter routing

Wanneer je Arcee-modellen via OpenRouter gebruikt, gelden dezelfde `arcee/*`-modelverwijzingen. OpenClaw handelt routering transparant af op basis van je auth-keuze. Zie de [OpenRouter-providerdocumentatie](</nl/providers/openrouter>) voor OpenRouter-specifieke configuratiedetails.

## Gerelateerd

[**OpenRouter** Krijg toegang tot Arcee-modellen en vele andere via een enkele API-sleutel. ](</nl/providers/openrouter>) [**Model selection** Providers, modelverwijzingen en failovergedrag kiezen. ](</nl/concepts/model-providers>)

Was this useful?YesNo