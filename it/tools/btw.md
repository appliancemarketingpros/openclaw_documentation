---
title: A proposito, domande secondarie
source_url: https://docs.openclaw.ai/it/tools/btw
scraped_at: 2026-05-25
---

`/btw` ti consente di porre una rapida domanda laterale sulla **sessione corrente** senza trasformare quella domanda nella normale cronologia della conversazione. `/side` è un alias.

È modellato sul comportamento di `/btw` di Claude Code, ma adattato al Gateway di OpenClaw e all'architettura multicanale.

## Cosa fa

Quando invii:

textCopy code
[code]
    /btw what changed?
[/code]

OpenClaw:

  1. acquisisce uno snapshot del contesto della sessione corrente,
  2. esegue una query laterale effimera separata,
  3. risponde solo alla domanda laterale,
  4. lascia invariata l'esecuzione principale,
  5. **non** scrive la domanda o la risposta BTW nella cronologia della sessione,
  6. emette la risposta come **risultato laterale live** invece che come normale messaggio dell'assistente.


Il modello mentale importante è:

  * stesso contesto di sessione
  * query laterale separata e monouso
  * stesso trasporto harness nativo quando la sessione usa un harness nativo
  * nessun inquinamento del contesto futuro
  * nessuna persistenza della trascrizione


Per le sessioni con harness Codex, BTW rimane dentro Codex creando una fork del thread app-server attivo come thread laterale effimero. Questo mantiene intatti OAuth di Codex e il comportamento nativo dei thread, isolando comunque la risposta laterale dalla trascrizione padre. Come `/side` di Codex, il thread laterale mantiene le autorizzazioni Codex correnti e la superficie degli strumenti nativa, con guardrail che indicano al modello di non trattare il lavoro ereditato dal thread padre come istruzioni attive. I runtime non Codex mantengono il percorso diretto monouso precedente.

## Cosa non fa

`/btw` **non** :

  * crea una nuova sessione durevole,
  * continua l'attività principale incompiuta,
  * scrive i dati della domanda/risposta BTW nella cronologia della trascrizione,
  * appare in `chat.history`,
  * sopravvive a un ricaricamento.


È intenzionalmente **effimero**.

## Come funziona il contesto

BTW usa la sessione corrente solo come **contesto di sfondo**.

Se l'esecuzione principale è attualmente attiva, OpenClaw acquisisce uno snapshot dello stato corrente dei messaggi e include il prompt principale in corso come contesto di sfondo, indicando esplicitamente al modello di:

  * rispondere solo alla domanda laterale,
  * non riprendere o completare l'attività principale incompiuta,
  * non orientare la conversazione padre.


Questo mantiene BTW isolato dall'esecuzione principale, pur rendendolo consapevole di ciò di cui tratta la sessione.

## Modello di consegna

BTW **non** viene consegnato come normale messaggio di trascrizione dell'assistente.

A livello di protocollo Gateway:

  * la normale chat dell'assistente usa l'evento `chat`
  * BTW usa l'evento `chat.side_result`


Questa separazione è intenzionale. Se BTW riutilizzasse il normale percorso dell'evento `chat`, i client lo tratterebbero come cronologia di conversazione ordinaria.

Poiché BTW usa un evento live separato e non viene riprodotto da `chat.history`, scompare dopo il ricaricamento.

## Comportamento della superficie

### TUI

Nella TUI, BTW viene renderizzato in linea nella vista della sessione corrente, ma rimane effimero:

  * visibilmente distinto da una normale risposta dell'assistente
  * eliminabile con `Enter` o `Esc`
  * non riprodotto al ricaricamento


### Canali esterni

Su canali come Telegram, WhatsApp e Discord, BTW viene consegnato come risposta monouso chiaramente etichettata, perché queste superfici non hanno un concetto locale di overlay effimero.

La risposta viene comunque trattata come risultato laterale, non come normale cronologia della sessione.

### UI di controllo / web

Il Gateway emette correttamente BTW come `chat.side_result`, e BTW non è incluso in `chat.history`, quindi il contratto di persistenza è già corretto per il web.

L'attuale UI di controllo necessita ancora di un consumer `chat.side_result` dedicato per renderizzare BTW live nel browser. Finché quel supporto lato client non arriva, BTW è una funzionalità a livello Gateway con comportamento completo nella TUI e nei canali esterni, ma non ancora una UX browser completa.

## Quando usare BTW

Usa `/btw` quando vuoi:

  * un rapido chiarimento sul lavoro corrente,
  * una risposta fattuale laterale mentre un'esecuzione lunga è ancora in corso,
  * una risposta temporanea che non dovrebbe diventare parte del contesto futuro della sessione.


Esempi:

textCopy code
[code]
    /btw what file are we editing?/side what changed while the main run continued?/btw what does this error mean?/btw summarize the current task in one sentence/btw what is 17 * 19?
[/code]

## Quando non usare BTW

Non usare `/btw` quando vuoi che la risposta diventi parte del futuro contesto di lavoro della sessione.

In quel caso, chiedi normalmente nella sessione principale invece di usare BTW.

## Correlati

[**Comandi slash** Catalogo dei comandi nativi e direttive di chat. ](</it/tools/slash-commands>) [**Livelli di ragionamento** Livelli di impegno di ragionamento per la chiamata al modello della domanda laterale. ](</it/tools/thinking>) [**Sessione** Chiavi di sessione, cronologia e semantica di persistenza. ](</it/concepts/session>) [**Comando steer** Inietta un messaggio di orientamento nell'esecuzione attiva senza terminarla. ](</it/tools/steer>)

Was this useful?YesNo