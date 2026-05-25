---
title: Gateway IA di Cloudflare
source_url: https://docs.openclaw.ai/it/providers/cloudflare-ai-gateway
scraped_at: 2026-05-25
---

Cloudflare AI Gateway si pone davanti alle API dei provider e consente di aggiungere analytics, caching e controlli. Per Anthropic, OpenClaw usa l'API Anthropic Messages tramite il tuo endpoint Gateway.

Proprietà | Valore  
---|---  
Fornitore | `cloudflare-ai-gateway`  
URL di base | `https://gateway.ai.cloudflare.com/v1/<account_id>/<gateway_id>/anthropic`  
Modello predefinito | `cloudflare-ai-gateway/claude-sonnet-4-6`  
Chiave API | `CLOUDFLARE_AI_GATEWAY_API_KEY` (la chiave API del tuo provider per le richieste tramite il Gateway)  
  
Quando il thinking è abilitato per i modelli Anthropic Messages, OpenClaw rimuove i turni finali di prefill dell'assistente prima di inviare il payload tramite Cloudflare AI Gateway. Anthropic rifiuta il prefill delle risposte con extended thinking, mentre il normale prefill senza thinking rimane disponibile.

## Introduzione

* ### Imposta la chiave API del provider e i dettagli del Gateway

Esegui l'onboarding e scegli l'opzione di autenticazione Cloudflare AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice cloudflare-ai-gateway-api-key
[/code]

Questo richiede il tuo ID account, ID gateway e chiave API.

* ### Imposta un modello predefinito

Aggiungi il modello alla tua configurazione OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cloudflare-ai-gateway/claude-sonnet-4-6" },    },  },}
[/code]

* ### Verifica che il modello sia disponibile

bashCopy code
[code]
    openclaw models list --provider cloudflare-ai-gateway
[/code]

## Esempio non interattivo

Per configurazioni scriptate o CI, passa tutti i valori dalla riga di comando:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cloudflare-ai-gateway-api-key \  --cloudflare-ai-gateway-account-id "your-account-id" \  --cloudflare-ai-gateway-gateway-id "your-gateway-id" \  --cloudflare-ai-gateway-api-key "$CLOUDFLARE_AI_GATEWAY_API_KEY"
[/code]

## Configurazione avanzata

Gateway autenticati

Se hai abilitato l'autenticazione del Gateway in Cloudflare, aggiungi l'header `cf-aig-authorization`. Questo è **in aggiunta a** la chiave API del tuo provider.

json5Copy code
[code]
    {  models: {    providers: {      "cloudflare-ai-gateway": {        headers: {          "cf-aig-authorization": "Bearer <cloudflare-ai-gateway-token>",        },      },    },  },}
[/code]

Nota sull'ambiente

Se il Gateway viene eseguito come daemon (launchd/systemd), assicurati che `CLOUDFLARE_AI_GATEWAY_API_KEY` sia disponibile per quel processo.

## Correlati

[**Selezione del modello** Scelta dei provider, riferimenti dei modelli e comportamento di failover. ](</it/concepts/model-providers>) [**Risoluzione dei problemi** Risoluzione generale dei problemi e FAQ. ](</it/help/troubleshooting>)

Was this useful?YesNo