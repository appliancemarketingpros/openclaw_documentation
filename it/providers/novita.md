---
title: NovitaAI
source_url: https://docs.openclaw.ai/it/providers/novita
scraped_at: 2026-06-29
---

ModelsProviders

NovitaAI è un provider di infrastruttura AI ospitata con un'API per modelli compatibile con OpenAI. In OpenClaw è un provider di modelli in bundle, quindi l'id del provider è `novita`, le credenziali passano attraverso il normale flusso di autenticazione dei modelli e i riferimenti ai modelli hanno un aspetto simile a `novita/deepseek/deepseek-v3-0324`.

Usa Novita quando vuoi accesso ospitato a route di modelli open-weight e di terze parti senza eseguire un tuo server di inferenza. Il catalogo in bundle si concentra su modelli di chat pratici per i turni degli agenti, incluse le route DeepSeek, Moonshot, MiniMax, GLM e Qwen esposte da Novita.

Questo provider usa l'endpoint compatibile con OpenAI di Novita. OpenClaw gestisce registrazione del provider, autenticazione, alias, normalizzazione dei riferimenti ai modelli e selezione dell'URL di base; Novita controlla disponibilità live dei modelli, permessi dell'account, prezzi e limiti di frequenza.

## Configurazione

Crea una chiave API su [novita.ai/settings/key-management](<https://novita.ai/settings/key-management>), quindi esegui:

bashCopy code
[code]
    openclaw onboard --auth-choice novita-api-key
[/code]

Oppure imposta:

bashCopy code
[code]
    export NOVITA_API_KEY="<your-novita-api-key>" # pragma: allowlist secret
[/code]

## Predefiniti

  * Provider: `novita`
  * Alias: `novita-ai`, `novitaai`
  * URL di base: `https://api.novita.ai/openai/v1`
  * Variabile di ambiente: `NOVITA_API_KEY`
  * Modello predefinito: `novita/deepseek/deepseek-v3-0324`


## Quando scegliere Novita

  * Vuoi accesso ospitato a modelli open-weight con un'API compatibile con OpenAI.
  * Vuoi route DeepSeek, Kimi, MiniMax, GLM o della famiglia Qwen tramite un unico account provider.
  * Vuoi un altro percorso di fallback ospitato accanto a OpenRouter, GMI, DeepInfra o API dirette dei vendor.
  * Preferisci l'hosting dei modelli lato provider rispetto alla manutenzione di infrastruttura vLLM, SGLang, LM Studio o Ollama.


Scegli un provider diretto del vendor quando hai bisogno di parametri di richiesta nativi del vendor o di contratti di supporto. Scegli un provider locale quando il modello deve essere eseguito sul tuo hardware o dietro il perimetro della tua rete.

## Modelli

Il catalogo in bundle inizializza id di route NovitaAI comunemente disponibili, tra cui:

  * `novita/moonshotai/kimi-k2.5`
  * `novita/minimax/minimax-m2.7`
  * `novita/zai-org/glm-5`
  * `novita/deepseek/deepseek-v3-0324`
  * `novita/deepseek/deepseek-r1-0528`
  * `novita/qwen/qwen3-235b-a22b-fp8`


Il catalogo è un punto di partenza per la selezione dei modelli OpenClaw. Il tuo account, la tua regione o il catalogo attuale di Novita possono aggiungere, rimuovere o limitare route. Controlla il provider dalla CLI prima di impostare un valore predefinito di lunga durata:

bashCopy code
[code]
    openclaw models list --provider novita
[/code]

## Risoluzione dei problemi

  * `401` o `403`: verifica la chiave nella pagina di gestione chiavi di Novita e riesegui `openclaw onboard --auth-choice novita-api-key` se il profilo salvato è obsoleto.
  * Errori di modello sconosciuto: usa l'esatto `novita/<route-id>` restituito da `openclaw models list --provider novita`.
  * Route lente o non riuscite: prova un'altra route di modello Novita oppure imposta Novita come provider di fallback per carichi di lavoro che possono tollerare variabilità specifica del provider.


## Correlati

  * [Provider di modelli](</it/concepts/model-providers>)
  * [Tutti i provider](</it/providers>)


Was this useful?YesNo

Open issue