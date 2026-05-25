---
title: Indirizza
source_url: https://docs.openclaw.ai/it/tools/steer
scraped_at: 2026-05-25
---

`/steer` invia indicazioni a un'esecuzione già attiva. Serve per i momenti in cui si vuole "adattare questa esecuzione mentre sta ancora lavorando", non per avviare un nuovo turno.

## Sessione corrente

Usa `/steer` di primo livello per indirizzare l'esecuzione attiva della sessione corrente:

textCopy code
[code]
    /steer prefer the smaller patch and keep the tests focused/tell summarize before making the next tool call
[/code]

Comportamento:

  * Indirizza solo l'esecuzione attiva della sessione corrente.
  * Funziona indipendentemente dalla modalità `/queue` della sessione.
  * Non avvia una nuova esecuzione quando la sessione è inattiva.
  * Risponde con un avviso quando non c'è alcuna esecuzione attiva da indirizzare.
  * Usa il percorso di indirizzamento del runtime attivo, quindi il modello vede le indicazioni al successivo confine del runtime supportato.


## Steer e coda

`/queue steer` cambia il comportamento dei normali messaggi in ingresso quando arrivano mentre un'esecuzione è attiva. `/steer <message>` è un comando esplicito che prova a iniettare il messaggio di quel comando nell'esecuzione attiva al successivo confine del runtime supportato, indipendentemente dall'impostazione `/queue` salvata.

Usa:

  * `/steer <message>` quando vuoi guidare subito l'esecuzione attiva.
  * `/queue steer` quando vuoi che i futuri messaggi normali guidino le esecuzioni attive per impostazione predefinita.
  * `/queue collect` o `/queue followup` quando i nuovi messaggi devono attendere un turno successivo invece di guidare l'esecuzione attiva.


Per le modalità di coda e il comportamento di fallback, consulta [Coda dei comandi](</it/concepts/queue>) e [Coda di indirizzamento](</it/concepts/queue-steering>).

## Sotto-agenti

Usa `/subagents steer` quando la destinazione è un'esecuzione figlia:

textCopy code
[code]
    /subagents steer 2 focus only on the API surface
[/code]

`/steer` di primo livello non seleziona un sotto-agente per id o indice di elenco. Indirizza sempre l'esecuzione attiva della sessione corrente. Consulta [Sotto-agenti](</it/tools/subagents>) per id, etichette e comandi di controllo dei sotto-agenti.

## Sessioni ACP

Usa `/acp steer` quando la destinazione è una sessione harness ACP:

textCopy code
[code]
    /acp steer --session agent:main:acp:codex tighten the repro
[/code]

Consulta [Agenti ACP](</it/tools/acp-agents>) per la selezione delle sessioni ACP e il comportamento del runtime.

## Correlati

  * [Comandi slash](</it/tools/slash-commands>)
  * [Coda dei comandi](</it/concepts/queue>)
  * [Coda di indirizzamento](</it/concepts/queue-steering>)
  * [Sotto-agenti](</it/tools/subagents>)


Was this useful?YesNo