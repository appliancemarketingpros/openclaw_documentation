---
title: GMI Cloud
source_url: https://docs.openclaw.ai/it/providers/gmi
scraped_at: 2026-06-29
---

ModelsProviders

GMI Cloud è una piattaforma di inferenza ospitata per modelli frontier e a pesi aperti dietro un'API compatibile con OpenAI. In OpenClaw è un Plugin provider esterno ufficiale, il che significa che lo installi una volta, lo selezioni con l'id provider `gmi`, archivi le credenziali tramite la normale autenticazione dei modelli e usi riferimenti ai modelli come `gmi/google/gemini-3.1-flash-lite`.

Usa GMI quando vuoi una sola chiave API per diverse famiglie di modelli ospitati, incluse le route Google, Anthropic, OpenAI, DeepSeek, Moonshot e Z.AI esposte dal catalogo di GMI. È utile come provider secondario per il fallback dei modelli, per confrontare route ospitate tra fornitori, o quando GMI rende disponibile un modello prima del tuo provider principale.

Questo provider usa semantiche di chat compatibili con OpenAI. OpenClaw possiede l'id provider, il profilo di autenticazione, gli alias, il seed del catalogo modelli e l'URL di base; GMI possiede la disponibilità live dei modelli, la fatturazione, i limiti di frequenza e qualsiasi criterio di instradamento lato provider.

## Configurazione

Installa il Plugin, riavvia il Gateway, poi crea una chiave API in GMI Cloud:

bashCopy code
[code]
    openclaw plugins install @openclaw/gmi-provideropenclaw gateway restart
[/code]

Poi esegui:

bashCopy code
[code]
    openclaw onboard --auth-choice gmi-api-key
[/code]

Oppure imposta:

bashCopy code
[code]
    export GMI_API_KEY="<your-gmi-api-key>" # pragma: allowlist secret
[/code]

## Valori predefiniti

  * Provider: `gmi`
  * Alias: `gmi-cloud`, `gmicloud`
  * URL di base: `https://api.gmi-serving.com/v1`
  * Variabile d'ambiente: `GMI_API_KEY`
  * Modello predefinito: `gmi/google/gemini-3.1-flash-lite`


## Quando scegliere GMI

  * Vuoi un endpoint ospitato compatibile con OpenAI invece di un server di modelli locale.
  * Vuoi provare diverse famiglie di modelli commerciali e a pesi aperti tramite un solo account provider.
  * Vuoi un provider di fallback con instradamento upstream diverso da OpenRouter, DeepInfra, Together o dalle API dirette dei fornitori.
  * Ti servono id modello, prezzi o controlli account specifici di GMI.


Scegli invece il provider diretto del fornitore quando ti servono funzionalità native del fornitore che GMI non espone tramite la sua route compatibile con OpenAI. Scegli un provider locale come Ollama, LM Studio, vLLM o SGLang quando la località dei dati o il controllo della GPU locale conta più della comodità dell'hosting.

## Modelli

Il catalogo del Plugin inizializza id route di GMI Cloud comunemente disponibili, tra cui:

  * `gmi/zai-org/GLM-5.1-FP8`
  * `gmi/deepseek-ai/DeepSeek-V3.2`
  * `gmi/moonshotai/Kimi-K2.5`
  * `gmi/google/gemini-3.1-flash-lite`
  * `gmi/anthropic/claude-sonnet-4.6`
  * `gmi/openai/gpt-5.4`


Il catalogo è un seed, non una promessa che ogni account possa chiamare ogni modello in qualsiasi momento. Usa il comando di elenco dei modelli di OpenClaw per vedere cosa segnala il provider configurato nel tuo ambiente:

bashCopy code
[code]
    openclaw models list --provider gmi
[/code]

## Risoluzione dei problemi

  * `401` o `403`: controlla che `GMI_API_KEY` sia impostata per il processo che esegue OpenClaw, oppure riesegui l'onboarding per archiviare la chiave nel profilo di autenticazione del provider.
  * Errori di modello sconosciuto: conferma che il modello esista nel tuo account GMI e usa il riferimento completo `gmi/<route-id>` mostrato da `openclaw models list --provider gmi`.
  * Errori intermittenti del provider: prova una route GMI diversa oppure configura GMI come fallback invece che come unico provider di modelli principale.


## Correlati

  * [Provider di modelli](</it/concepts/model-providers>)
  * [Tutti i provider](</it/providers>)


Was this useful?YesNo

Open issue