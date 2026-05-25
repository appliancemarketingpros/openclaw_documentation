---
title: Esecuzione di codice
source_url: https://docs.openclaw.ai/it/tools/code-execution
scraped_at: 2026-05-25
---

`code_execution` esegue analisi Python remote in sandbox sull'API Responses di xAI. È registrato dal plugin `xai` in bundle (sotto il contratto `tools`) e inoltra le richieste allo stesso endpoint `https://api.x.ai/v1/responses` usato da `x_search`.

Proprietà | Valore  
---|---  
Nome dello strumento | `code_execution`  
Plugin del provider | `xai` (in bundle, `enabledByDefault: true`)  
Autenticazione | profilo di autenticazione xAI, `XAI_API_KEY`, o `plugins.entries.xai.config.webSearch.apiKey`  
Modello predefinito | `grok-4-1-fast`  
Timeout predefinito | 30 secondi  
`maxTurns` predefinito | non impostato (xAI applica il proprio limite interno)  
  
È diverso da [`exec`](</it/tools/exec>) locale:

  * `exec` esegue comandi shell sulla tua macchina o sul node associato.
  * `code_execution` esegue Python nel sandbox remoto di xAI.


Usa `code_execution` per:

  * Calcoli.
  * Tabulazione.
  * Statistiche rapide.
  * Analisi in stile grafico.
  * Analizzare dati restituiti da `x_search` o `web_search`.


**Non** usarlo quando hai bisogno di file locali, della tua shell, del tuo repo o di dispositivi associati. Usa [`exec`](</it/tools/exec>) per quello.

## Configurazione

* ### Fornisci una chiave API xAI

Esegui `openclaw onboard --auth-choice xai-api-key` per `code_execution` e `x_search`, oppure imposta `XAI_API_KEY` / configura la chiave sotto il plugin xAI quando vuoi anche che la ricerca web Grok usi la stessa credenziale:

bashCopy code
[code]
    export XAI_API_KEY=xai-...
[/code]

Oppure tramite configurazione:

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...",          },        },      },    },  },}
[/code]

* ### Abilita e configura code_execution

Lo strumento è controllato da `plugins.entries.xai.config.codeExecution.enabled`. Il valore predefinito è disattivato.

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast", // sovrascrive il modello di esecuzione codice xAI predefinito            maxTurns: 2,            // limite opzionale sui turni interni dello strumento            timeoutSeconds: 30,     // timeout della richiesta (predefinito: 30)          },        },      },    },  },}
[/code]

* ### Riavvia il Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

`code_execution` compare nell'elenco degli strumenti dell'agente dopo che il plugin xAI si registra di nuovo con `enabled: true`.

## Come usarlo

Chiedi in modo naturale e rendi esplicito l'obiettivo dell'analisi:

textCopy code
[code]
    Use code_execution to calculate the 7-day moving average for these numbers: ...
[/code]

textCopy code
[code]
    Use x_search to find posts mentioning OpenClaw this week, then use code_execution to count them by day.
[/code]

textCopy code
[code]
    Use web_search to gather the latest AI benchmark numbers, then use code_execution to compare percent changes.
[/code]

Lo strumento accetta internamente un singolo parametro `task`, quindi l'agente deve inviare la richiesta di analisi completa e tutti i dati inline in un unico prompt.

## Errori

Quando lo strumento viene eseguito senza autenticazione, restituisce un errore strutturato `missing_xai_api_key` che punta al profilo di autenticazione, alla variabile di ambiente e alle opzioni di configurazione. L'errore è JSON, non un'eccezione generata, quindi l'agente può correggersi autonomamente:

jsonCopy code
[code]
    {  "error": "missing_xai_api_key",  "message": "code_execution needs an xAI API key. Run openclaw onboard --auth-choice xai-api-key, set XAI_API_KEY in the Gateway environment, or configure plugins.entries.xai.config.webSearch.apiKey.",  "docs": "https://docs.openclaw.ai/tools/code-execution"}
[/code]

## Limiti

  * Questa è esecuzione remota xAI, non esecuzione di processi locali.
  * Considera i risultati come analisi effimera, non come una sessione notebook persistente.
  * Non presumere l'accesso a file locali o al tuo workspace.
  * Per dati X aggiornati, usa prima [`x_search`](</it/tools/web#x_search>) e passa il risultato a `code_execution`.


## Correlati

[**Strumento exec** Esecuzione shell locale sulla tua macchina o sul node associato. ](</it/tools/exec>) [**Approvazioni exec** Criterio di autorizzazione/rifiuto per l'esecuzione shell. ](</it/tools/exec-approvals>) [**Strumenti web** `web_search`, `x_search` e `web_fetch`. ](</it/tools/web>) [**Provider xAI** Modelli Grok, ricerca web/X e configurazione di esecuzione codice. ](</it/providers/xai>)

Was this useful?YesNo