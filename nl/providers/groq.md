---
title: Groq
source_url: https://docs.openclaw.ai/nl/providers/groq
scraped_at: 2026-05-25
---

[Groq](<https://groq.com>) biedt ultrasnelle inferentie op open-weight modellen (Llama, Gemma, Kimi, Qwen, GPT OSS en meer) met aangepaste LPU-hardware. OpenClaw bevat een gebundelde Groq-Plugin die zowel een OpenAI-compatibele chatprovider als een provider voor mediabegrip van audio registreert.

Eigenschap | Waarde  
---|---  
Provider-id | `groq`  
Plugin | gebundeld, `enabledByDefault: true`  
Auth-env-var | `GROQ_API_KEY`  
Onboarding-vlag | `--auth-choice groq-api-key`  
API | OpenAI-compatibel (`openai-completions`)  
Basis-URL | `https://api.groq.com/openai/v1`  
Audiotranscriptie | `whisper-large-v3-turbo` (standaard)  
Voorgestelde chatstandaard | `groq/llama-3.3-70b-versatile`  
  
## Aan de slag

* ### Een API-sleutel ophalen

Maak een API-sleutel aan op [console.groq.com/keys](<https://console.groq.com/keys>).

* ### De API-sleutel instellen

OnboardingCopy code
[code]
    openclaw onboard --auth-choice groq-api-key
[/code]

Alleen envCopy code
[code]
    export GROQ_API_KEY=gsk_...
[/code]

* ### Een standaardmodel instellen

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

* ### Controleren of de catalogus bereikbaar is

bashCopy code
[code]
    openclaw models list --provider groq
[/code]

### Voorbeeld van configuratiebestand

json5Copy code
[code]
    {  env: { GROQ_API_KEY: "gsk_..." },  agents: {    defaults: {      model: { primary: "groq/llama-3.3-70b-versatile" },    },  },}
[/code]

## Ingebouwde catalogus

OpenClaw wordt geleverd met een manifestondersteunde Groq-catalogus met zowel redenerende als niet-redenerende vermeldingen. Voer `openclaw models list --provider groq` uit om de gebundelde rijen voor je geïnstalleerde versie te bekijken, of raadpleeg [console.groq.com/docs/models](<https://console.groq.com/docs/models>) voor Groq's gezaghebbende lijst.

Modelreferentie | Naam | Redeneren | Invoer | Context  
---|---|---|---|---  
`groq/llama-3.3-70b-versatile` | Llama 3.3 70B Versatile | nee | tekst | 131,072  
`groq/llama-3.1-8b-instant` | Llama 3.1 8B Instant | nee | tekst | 131,072  
`groq/meta-llama/llama-4-maverick-17b-128e-instruct` | Llama 4 Maverick 17B | nee | tekst + afbeelding | 131,072  
`groq/meta-llama/llama-4-scout-17b-16e-instruct` | Llama 4 Scout 17B | nee | tekst + afbeelding | 131,072  
`groq/llama3-70b-8192` | Llama 3 70B | nee | tekst | 8,192  
`groq/llama3-8b-8192` | Llama 3 8B | nee | tekst | 8,192  
`groq/gemma2-9b-it` | Gemma 2 9B | nee | tekst | 8,192  
`groq/mistral-saba-24b` | Mistral Saba 24B | nee | tekst | 32,768  
`groq/moonshotai/kimi-k2-instruct` | Kimi K2 Instruct | nee | tekst | 131,072  
`groq/moonshotai/kimi-k2-instruct-0905` | Kimi K2 Instruct 0905 | nee | tekst | 262,144  
`groq/openai/gpt-oss-120b` | GPT OSS 120B | ja | tekst | 131,072  
`groq/openai/gpt-oss-20b` | GPT OSS 20B | ja | tekst | 131,072  
`groq/openai/gpt-oss-safeguard-20b` | Safety GPT OSS 20B | ja | tekst | 131,072  
`groq/qwen-qwq-32b` | Qwen QwQ 32B | ja | tekst | 131,072  
`groq/qwen/qwen3-32b` | Qwen3 32B | ja | tekst | 131,072  
`groq/deepseek-r1-distill-llama-70b` | DeepSeek R1 Distill Llama 70B | ja | tekst | 131,072  
`groq/groq/compound` | Compound | ja | tekst | 131,072  
`groq/groq/compound-mini` | Compound Mini | ja | tekst | 131,072  
  
## Redeneringsmodellen

OpenClaw koppelt zijn gedeelde `/think`-niveaus aan Groq's modelspecifieke `reasoning_effort`-waarden:

  * Voor `qwen/qwen3-32b` verzendt uitgeschakeld denken `none` en ingeschakeld denken `default`.
  * Voor Groq GPT OSS-redeneringsmodellen (`openai/gpt-oss-*`) verzendt OpenClaw `low`, `medium` of `high` op basis van het `/think`-niveau. Uitgeschakeld denken laat `reasoning_effort` weg, omdat die modellen geen uitgeschakelde waarde ondersteunen.
  * DeepSeek R1 Distill, Qwen QwQ en Compound gebruiken Groq's native redeneeroppervlak; `/think` regelt de zichtbaarheid, maar het model redeneert altijd.


Zie [Denkmodi](</nl/tools/thinking>) voor de gedeelde `/think`-niveaus en hoe OpenClaw deze per provider vertaalt.

## Audiotranscriptie

Groq's gebundelde Plugin registreert ook een **provider voor mediabegrip van audio** , zodat spraakberichten kunnen worden getranscribeerd via het gedeelde `tools.media.audio`-oppervlak.

Eigenschap | Waarde  
---|---  
Gedeeld configuratiepad | `tools.media.audio`  
Standaard basis-URL | `https://api.groq.com/openai/v1`  
Standaardmodel | `whisper-large-v3-turbo`  
Automatische prioriteit | 20  
API-eindpunt | OpenAI-compatibel `/audio/transcriptions`  
  
Om Groq de standaard audio-backend te maken:

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [{ provider: "groq" }],      },    },  },}
[/code]

Omgevingsbeschikbaarheid voor de daemon

Als de Gateway als beheerde service draait (launchd, systemd, Docker), moet `GROQ_API_KEY` zichtbaar zijn voor dat proces, niet alleen voor je interactieve shell.

Aangepaste Groq-model-id's

OpenClaw accepteert elke Groq-model-id tijdens runtime. Gebruik de exacte id die Groq toont en voeg er `groq/` als prefix aan toe. De gebundelde catalogus dekt de gangbare gevallen; niet-gecatalogiseerde id's vallen terug op de standaard OpenAI-compatibele template.

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "groq/<your-model-id>" },    },  },}
[/code]

## Gerelateerd

[**Modelproviders** Providers, modelreferenties en failovergedrag kiezen. ](</nl/concepts/model-providers>) [**Denkmodi** Niveaus voor redeneerinspanning en interactie met providerbeleid. ](</nl/tools/thinking>) [**Configuratiereferentie** Volledig configuratieschema inclusief provider- en audio-instellingen. ](</nl/gateway/configuration-reference>) [**Groq Console** Groq-dashboard, API-documentatie en prijzen. ](<https://console.groq.com>)

Was this useful?YesNo