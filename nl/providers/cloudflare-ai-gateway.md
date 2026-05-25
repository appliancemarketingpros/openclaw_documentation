---
title: Cloudflare AI Gateway
source_url: https://docs.openclaw.ai/nl/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway staat voor provider-API's en laat je analytics, caching en besturingselementen toevoegen. Voor Anthropic gebruikt OpenClaw de Anthropic Messages API via je Gateway-eindpunt.

Eigenschap | Waarde  
---|---  
Provider | `cloudflare-ai-gateway`  
Basis-URL | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Standaardmodel | `cloudflare-ai-gateway/claude-sonnet-4-6`  
API-sleutel | `CLOUDFLARE_AI_GATEWAY_API_KEY` (je provider-API-sleutel voor aanvragen via de Gateway)  
  
Wanneer denken is ingeschakeld voor Anthropic Messages-modellen, verwijdert OpenClaw afsluitende assistant-prefill-beurten voordat de payload via Cloudflare AI Gateway wordt verzonden. Anthropic weigert antwoord-prefilling met uitgebreid denken, terwijl gewone prefill zonder denken beschikbaar blijft.

## Aan de slag

* ### Stel de provider-API-sleutel en Gateway-gegevens in

Voer onboarding uit en kies de authenticatieoptie voor Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Dit vraagt om je account-ID, gateway-ID en API-sleutel.

* ### Stel een standaardmodel in

Voeg het model toe aan je OpenClaw-configuratie:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Controleer of het model beschikbaar is

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Niet-interactief voorbeeld

Geef voor gescripte of CI-configuraties alle waarden door via de opdrachtregel:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Geavanceerde configuratie

Geauthenticeerde gateways

Als je Gateway-authenticatie in Cloudflare hebt ingeschakeld, voeg dan de header `cf-aig-authorization` toe. Dit komt **naast** je provider-API-sleutel.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Omgevingsnotitie

Als de Gateway als daemon draait (launchd/systemd), zorg er dan voor dat `CLOUDFLARE_AI_GATEWAY_API_KEY` beschikbaar is voor dat proces.

## Gerelateerd

[**Modelselectie** Providers, modelreferenties en failover-gedrag kiezen. ](</nl/concepts/model-providers>) [**Probleemoplossing** Algemene probleemoplossing en veelgestelde vragen. ](</nl/help/troubleshooting>)

Was this useful?YesNo