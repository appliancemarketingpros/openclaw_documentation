---
title: Vercel AI Gateway
source_url: https://docs.openclaw.ai/nl/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

De [Vercel AI Gateway](<https://vercel.com/ai-gateway>) biedt een uniforme API om toegang te krijgen tot honderden modellen via één enkel eindpunt.

Eigenschap | Waarde  
---|---  
Provider | `vercel-ai-gateway`  
Auth | `AI_GATEWAY_API_KEY`  
API | compatibel met Anthropic Messages  
Modelcatalogus | automatisch ontdekt via `/v1/models`  
  
## Aan de slag

* ### De API-sleutel instellen

Voer onboarding uit en kies de AI Gateway-authoptie:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Een standaardmodel instellen

Voeg het model toe aan je OpenClaw-configuratie:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Controleren of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Niet-interactief voorbeeld

Voor gescripte of CI-installaties geef je alle waarden door op de opdrachtregel:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Verkorte model-ID

OpenClaw accepteert verkorte Vercel Claude-modelverwijzingen en normaliseert ze tijdens runtime:

Verkorte invoer | Genormaliseerde modelverwijzing  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Geavanceerde configuratie

Omgevingsvariabele voor daemonprocessen

Als de OpenClaw Gateway als daemon draait (launchd/systemd), zorg er dan voor dat `AI_GATEWAY_API_KEY` beschikbaar is voor dat proces.

Providerroutering

Vercel AI Gateway routeert aanvragen naar de upstream provider op basis van het prefix van de modelverwijzing. Bijvoorbeeld: `vercel-ai-gateway/anthropic/claude-opus-4.6` routeert via Anthropic, terwijl `vercel-ai-gateway/openai/gpt-5.5` via OpenAI routeert en `vercel-ai-gateway/moonshotai/kimi-k2.6` via MoonshotAI. Je enkele `AI_GATEWAY_API_KEY` verzorgt authenticatie voor alle upstream providers.

Denk­niveaus

`/think`-opties volgen vertrouwde upstream modelprefixen wanneer OpenClaw het contract van de upstream provider kent. `vercel-ai-gateway/anthropic/...` gebruikt het Claude-denkprofiel, inclusief adaptieve standaardwaarden voor Claude 4.6-modellen. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5` en Codex-achtige verwijzingen bieden `/think xhigh`, net als de directe OpenAI/OpenAI Codex-providers. Andere namespaced verwijzingen behouden de normale redeneerniveaus, tenzij hun catalogusmetadata meer declareert.

## Gerelateerd

[**Modelselectie** Providers, modelverwijzingen en failover-gedrag kiezen. ](</nl/concepts/model-providers>) [**Probleemoplossing** Algemene probleemoplossing en veelgestelde vragen. ](</nl/help/troubleshooting>)

Was this useful?YesNo