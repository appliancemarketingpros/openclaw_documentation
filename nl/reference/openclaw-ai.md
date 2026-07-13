---
title: @openclaw/ai-pakket
source_url: https://docs.openclaw.ai/nl/reference/openclaw-ai
scraped_at: 2026-07-13
---

ReferenceTechnical reference

`@openclaw/ai` is de publiceerbare bibliotheekvorm van OpenClaws modeluitvoeringslaag: providerneutrale contracten voor berichten, tools en streams, validatie, diagnostiek, gebeurtenisstreams, een geïsoleerd runtimeregister en lui geladen adapters voor de acht ingebouwde API-families (Anthropic Messages, OpenAI Completions, OpenAI Responses, Azure OpenAI Responses, ChatGPT/Codex Responses, Google Generative AI, Google Vertex, Mistral Conversations).

Het wordt bij elke release samen met het hoofdpakket `openclaw` gepubliceerd, vastgezet op dezelfde versie, met een eigen `npm-shrinkwrap.json`, zodat de transitieve afhankelijkheidsstructuur tijdens de installatie wordt vergrendeld. Bij installatie van `openclaw` wordt automatisch de overeenkomende versie van `@openclaw/ai` geïnstalleerd; bibliotheekgebruikers kunnen er rechtstreeks van afhankelijk zijn zonder enige OpenClaw-toepassingscode.

## Snel aan de slag

jsCopy code
[code]
      const runtime = createLlmRuntime();registerBuiltInApiProviders(runtime.registry); const stream = runtime.streamSimple(model, { messages }, { apiKey });for await (const event of stream) {  if (event.type === "text_delta") process.stdout.write(event.delta);}const result = await stream.result();
[/code]

Een uitvoerbare versie staat in de repository onder `examples/ai-chat`.

## Ontwerpcontract

  * **Standaard beperkt tot de instantie.** Bij het importeren van het pakket wordt niets globaal geregistreerd. `createApiRegistry()` / `createLlmRuntime()` retourneren geïsoleerde instanties; met `registerBuiltInApiProviders(registry)` worden de ingebouwde transporten expliciet ingeschakeld voor één register. SDK-modules van providers worden bij het eerste gebruik lui geladen.
  * **Hostbeleid wordt geïnjecteerd, niet meegeleverd.** Bewaking van `fetch`-aanvragen (bijvoorbeeld SSRF-beleid), het redigeren van geheimen in opnieuw afgespeelde tekst van toolresultaten, standaardinstellingen voor strikte OpenAI-tools en diagnostische logboekregistratie zijn `AiTransportHost`-poorten die met `configureAiTransportHost` worden geconfigureerd. De standaardinstellingen van de bibliotheek doen niets; OpenClaw installeert de werkelijke implementaties in zijn streamfacade.
  * **Eén identiteit voor gebeurtenisstreams.** `@openclaw/ai/event-stream` is de canonieke `EventStream`-constructor die wordt gedeeld door de OpenClaw-kern, agent-core en externe gebruikers.
  * **`internal/*`-subpaden zijn geen API.** Ze bestaan voor de OpenClaw-toepassing zelf en bieden geen semver-garantie.
  * Provider-id's, inloggegevens, modelcatalogi, nieuwe pogingen en failover blijven verantwoordelijkheden van de toepassing. OpenClaw bouwt deze rondom dit pakket op; een bibliotheekgebruiker levert rechtstreeks een `Model`-object en opties aan.


## Subpadexports

Subpad | Inhoud  
---|---  
`.` | Contracten, `createApiRegistry`, `createLlmRuntime`, `configureAiTransportHost`  
`./providers` | `registerBuiltInApiProviders`, `resetApiProviders`  
`./types` | Typen voor modellen, berichten, tools en streams  
`./validation` | Validatie van toolargumenten  
`./diagnostics` | Diagnostiekcontracten  
`./event-stream` | Gedeelde `EventStream`-implementatie  
`./internal/*` | Intern voor OpenClaw, geen semver-garantie  
  
Was this useful?YesNo

Open issue