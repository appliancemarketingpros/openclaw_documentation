---
title: Gateway AI di Vercel
source_url: https://docs.openclaw.ai/it/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

[Vercel AI Gateway](<https://vercel.com/ai-gateway>) fornisce un'API unificata per accedere a centinaia di modelli tramite un unico endpoint.

Proprietà | Valore  
---|---  
Provider | `vercel-ai-gateway`  
Autenticazione | `AI_GATEWAY_API_KEY`  
API | compatibile con Anthropic Messages  
Catalogo dei modelli | Rilevato automaticamente tramite `/v1/models`  
  
## Per iniziare

* ### Imposta la chiave API

Esegui l'onboarding e scegli l'opzione di autenticazione AI Gateway:

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### Imposta un modello predefinito

Aggiungi il modello alla tua configurazione OpenClaw:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### Verifica che il modello sia disponibile

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## Esempio non interattivo

Per configurazioni con script o CI, passa tutti i valori dalla riga di comando:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## Abbreviazione dell'ID del modello

OpenClaw accetta riferimenti di modello abbreviati per Vercel Claude e li normalizza in fase di esecuzione:

Input abbreviato | Riferimento di modello normalizzato  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## Configurazione avanzata

Variabile d'ambiente per processi daemon

Se OpenClaw Gateway viene eseguito come daemon (launchd/systemd), assicurati che `AI_GATEWAY_API_KEY` sia disponibile per quel processo.

Instradamento del provider

Vercel AI Gateway instrada le richieste al provider upstream in base al prefisso del riferimento di modello. Ad esempio, `vercel-ai-gateway/anthropic/claude-opus-4.6` viene instradato tramite Anthropic, mentre `vercel-ai-gateway/openai/gpt-5.5` viene instradato tramite OpenAI e `vercel-ai-gateway/moonshotai/kimi-k2.6` viene instradato tramite MoonshotAI. La tua singola chiave `AI_GATEWAY_API_KEY` gestisce l'autenticazione per tutti i provider upstream.

Livelli di pensiero

Le opzioni `/think` seguono i prefissi dei modelli upstream attendibili quando OpenClaw conosce il contratto del provider upstream. `vercel-ai-gateway/anthropic/...` usa il profilo di pensiero Claude, inclusi i valori predefiniti adattivi per i modelli Claude 4.6. `vercel-ai-gateway/openai/gpt-5.4`, `gpt-5.5` e i riferimenti in stile Codex espongono `/think xhigh` proprio come i provider diretti OpenAI/OpenAI Codex. Gli altri riferimenti con namespace mantengono i normali livelli di ragionamento, a meno che i metadati del loro catalogo non ne dichiarino altri.

## Correlati

[**Selezione del modello** Scelta dei provider, dei riferimenti di modello e del comportamento di failover. ](</it/concepts/model-providers>) [**Risoluzione dei problemi** Risoluzione generale dei problemi e domande frequenti. ](</it/help/troubleshooting>)

Was this useful?YesNo