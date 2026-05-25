---
title: DeepSeek
source_url: https://docs.openclaw.ai/nl/providers/deepseek
scraped_at: 2026-05-25
---

[DeepSeek](<https://www.deepseek.com>) biedt krachtige AI-modellen met een OpenAI-compatibele API.

Eigenschap | Waarde  
---|---  
Provider | `deepseek`  
Auth | `DEEPSEEK_API_KEY`  
API | OpenAI-compatibel  
Basis-URL | `https://api.deepseek.com`  
  
## Aan de slag

* ### Haal je API-sleutel op

Maak een API-sleutel aan op [platform.deepseek.com](<https://platform.deepseek.com/api_keys>).

* ### Voer onboarding uit

bashCopy code
[code]
    openclaw onboard --auth-choice deepseek-api-key
[/code]

Dit vraagt om je API-sleutel en stelt `deepseek/deepseek-v4-flash` in als standaardmodel.

* ### Controleer of modellen beschikbaar zijn

bashCopy code
[code]
    openclaw models list --provider deepseek
[/code]

Gebruik het volgende om de meegeleverde statische catalogus te inspecteren zonder een draaiende Gateway te vereisen:

bashCopy code
[code]
    openclaw models list --all --provider deepseek
[/code]

Niet-interactieve installatie

Geef voor gescripte of headless installaties alle flags direct mee:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice deepseek-api-key \  --deepseek-api-key "$DEEPSEEK_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Ingebouwde catalogus

Modelreferentie | Naam | Invoer | Context | Maximale uitvoer | Opmerkingen  
---|---|---|---|---|---  
`deepseek/deepseek-v4-flash` | DeepSeek V4 Flash | text | 1,000,000 | 384,000 | Standaardmodel; V4-oppervlak met thinking  
`deepseek/deepseek-v4-pro` | DeepSeek V4 Pro | text | 1,000,000 | 384,000 | V4-oppervlak met thinking  
`deepseek/deepseek-chat` | DeepSeek Chat | text | 131,072 | 8,192 | DeepSeek V3.2-oppervlak zonder thinking  
`deepseek/deepseek-reasoner` | DeepSeek Reasoner | text | 131,072 | 65,536 | V3.2-oppervlak met redeneren  
  
## Thinking en tools

DeepSeek V4-thinking-sessies hebben een strikter replay-contract dan de meeste OpenAI-compatibele providers: nadat een ronde met thinking ingeschakeld tools gebruikt, verwacht DeepSeek dat opnieuw afgespeelde assistentberichten uit die ronde `reasoning_content` bevatten bij vervolgverzoeken. OpenClaw handelt dit af binnen de DeepSeek-Plugin, zodat normaal toolgebruik over meerdere rondes werkt met `deepseek/deepseek-v4-flash` en `deepseek/deepseek-v4-pro`.

Als je een bestaande sessie overschakelt van een andere OpenAI-compatibele provider naar een DeepSeek V4-model, hebben oudere assistent-rondes met tool calls mogelijk geen native DeepSeek `reasoning_content`. OpenClaw vult dat ontbrekende veld in bij opnieuw afgespeelde assistentberichten voor DeepSeek V4-thinking-verzoeken, zodat de provider de geschiedenis kan accepteren zonder `/new` te vereisen.

Wanneer thinking is uitgeschakeld in OpenClaw (inclusief de UI-selectie **Geen**), stuurt OpenClaw DeepSeek `thinking: { type: "disabled" }` en verwijdert het opnieuw afgespeelde `reasoning_content` uit de uitgaande geschiedenis. Dit houdt sessies met uitgeschakelde thinking op het DeepSeek-pad zonder thinking.

Gebruik `deepseek/deepseek-v4-flash` voor het standaard snelle pad. Gebruik `deepseek/deepseek-v4-pro` wanneer je het sterkere V4-model wilt en hogere kosten of latentie kunt accepteren.

## Live testen

De directe live modelsuite bevat DeepSeek V4 in de moderne modelset. Voer alleen de directe modelcontroles voor DeepSeek V4 als volgt uit:

bashCopy code
[code]
    OPENCLAW_LIVE_PROVIDERS=deepseek \OPENCLAW_LIVE_MODELS="deepseek/deepseek-v4-flash,deepseek/deepseek-v4-pro" \pnpm test:live src/agents/models.profiles.live.test.ts
[/code]

Die live controle verifieert dat beide V4-modellen kunnen voltooien en dat thinking/tool- vervolgrondes de replay-payload behouden die DeepSeek vereist.

## Configuratievoorbeeld

json5Copy code
[code]
    {  env: { DEEPSEEK_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "deepseek/deepseek-v4-flash" },    },  },}
[/code]

## Gerelateerd

[**Modelselectie** Providers, modelreferenties en failover-gedrag kiezen. ](</nl/concepts/model-providers>) [**Configuratiereferentie** Volledige configuratiereferentie voor agents, modellen en providers. ](</nl/gateway/configuration-reference>)

Was this useful?YesNo