---
title: Integrità
source_url: https://docs.openclaw.ai/it/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

Recupera lo stato di salute dal Gateway in esecuzione.

## Opzioni

Opzione | Predefinito | Descrizione  
---|---|---  
`--json` | `false` | Stampa JSON leggibile da macchina invece di testo.  
`--timeout <ms>` | `10000` | Timeout di connessione in millisecondi.  
`--verbose` | `false` | Logging dettagliato. Forza una verifica live ed espande l'output per agent.  
`--debug` | `false` | Alias di `--verbose`.  
  
Esempi:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Note:

  * `openclaw health` predefinito richiede al Gateway in esecuzione la sua istantanea dello stato di salute. Quando il Gateway ha già un'istantanea memorizzata nella cache e recente, può restituire quel payload in cache e aggiornarsi in background.
  * `--verbose` forza una verifica live, stampa i dettagli di connessione del Gateway ed espande l' output leggibile dall'uomo su tutti gli account e gli agent configurati.
  * L'output include gli archivi di sessione per agent quando sono configurati più agent.


## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Stato di salute del Gateway](</it/gateway/health>)


Was this useful?YesNo