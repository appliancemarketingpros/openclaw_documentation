---
title: Impegni dedotti
source_url: https://docs.openclaw.ai/it/concepts/commitments
scraped_at: 2026-05-25
---

Gli impegni sono memorie di ricontatto a breve durata. Quando sono abilitati, OpenClaw può notare che una conversazione ha creato un'opportunità di verifica futura e ricordarsi di riprenderla più avanti.

Esempi:

  * Menzioni un colloquio domani. OpenClaw potrebbe controllare in seguito.
  * Dici di essere esausto. OpenClaw potrebbe chiederti più avanti se hai dormito.
  * L'agente dice che farà un ricontatto dopo che qualcosa cambia. OpenClaw potrebbe tracciare quel ciclo aperto.


Gli impegni non sono fatti durevoli come `MEMORY.md` e non sono promemoria esatti. Si collocano tra memoria e automazione: OpenClaw ricorda un obbligo legato alla conversazione, poi Heartbeat lo consegna quando è il momento.

## Abilitare gli impegni

Gli impegni sono disattivati per impostazione predefinita. Abilitali nella configurazione:

bashCopy code
[code]
    openclaw config set commitments.enabled trueopenclaw config set commitments.maxPerDay 3
[/code]

`openclaw.json` equivalente:

jsonCopy code
[code]
    {  "commitments": {    "enabled": true,    "maxPerDay": 3  }}
[/code]

`commitments.maxPerDay` limita quanti ricontatti dedotti possono essere consegnati per sessione agente in un giorno mobile. Il valore predefinito è `3`.

## Come funziona

Dopo una risposta dell'agente, OpenClaw può eseguire un passaggio nascosto di estrazione in background in un contesto separato. Quel passaggio cerca solo impegni di ricontatto dedotti. Non scrive nella conversazione visibile e non chiede all'agente principale di ragionare sull'estrazione.

Quando trova un candidato ad alta confidenza, OpenClaw memorizza un impegno con:

  * l'id dell'agente
  * la chiave di sessione
  * il canale originale e la destinazione di consegna
  * una finestra di scadenza
  * una breve verifica suggerita
  * metadati non istruttivi per consentire a Heartbeat di decidere se inviarlo


La consegna avviene tramite Heartbeat. Quando un impegno arriva a scadenza, Heartbeat aggiunge l'impegno al turno Heartbeat per lo stesso agente e ambito di canale. Il modello può inviare una verifica naturale oppure rispondere `HEARTBEAT_OK` per ignorarlo. Se Heartbeat è configurato con `target: "none"`, gli impegni in scadenza rimangono interni e non inviano verifiche esterne. I prompt di consegna degli impegni non riproducono il testo della conversazione originale, e i turni Heartbeat degli impegni in scadenza vengono eseguiti senza strumenti OpenClaw.

OpenClaw non consegna mai un impegno dedotto subito dopo averlo scritto. Il momento di scadenza viene vincolato ad almeno un intervallo Heartbeat dopo la creazione dell'impegno, quindi il ricontatto non può risuonare nello stesso momento in cui è stato dedotto.

## Ambito

Gli impegni sono limitati all'esatto contesto di agente e canale in cui sono stati creati. Un ricontatto dedotto mentre parli con un agente in Discord non viene consegnato da un altro agente, da un altro canale o da una sessione non correlata.

Questo ambito fa parte della funzionalità. Le verifiche naturali dovrebbero sembrare la continuazione della stessa conversazione, non un sistema globale di promemoria.

## Impegni e promemoria

Esigenza | Usa  
---|---  
"Ricordamelo alle 15:00" | [Attività pianificate](</it/automation/cron-jobs>)  
"Avvisami tra 20 minuti" | [Attività pianificate](</it/automation/cron-jobs>)  
"Esegui questo report ogni giorno feriale" | [Attività pianificate](</it/automation/cron-jobs>)  
"Ho un colloquio domani" | Impegni  
"Sono rimasto sveglio tutta la notte" | Impegni  
"Ricontattami se non rispondo a questa conversazione aperta" | Impegni  
  
Le richieste esatte dell'utente appartengono già al percorso dello scheduler. Gli impegni servono solo per ricontatti dedotti: i momenti in cui l'utente non ha chiesto un promemoria, ma la conversazione ha chiaramente creato una verifica futura utile.

## Gestire gli impegni

Usa la CLI per ispezionare e cancellare gli impegni memorizzati:

bashCopy code
[code]
    openclaw commitmentsopenclaw commitments --allopenclaw commitments --agent mainopenclaw commitments --status snoozedopenclaw commitments dismiss cm_abc123
[/code]

Consulta [`openclaw commitments`](</it/cli/commitments>) per il riferimento del comando.

## Privacy e costi

L'estrazione degli impegni usa un passaggio LLM, quindi abilitarla aggiunge uso del modello in background dopo i turni idonei. Il passaggio è nascosto dalla conversazione visibile all'utente, ma può leggere lo scambio recente necessario per decidere se esiste un ricontatto.

Gli impegni memorizzati sono stato locale di OpenClaw. Sono memoria operativa, non memoria a lungo termine. Disabilita la funzionalità con:

bashCopy code
[code]
    openclaw config set commitments.enabled false
[/code]

## Risoluzione dei problemi

Se i ricontatti attesi non compaiono:

  * Conferma che `commitments.enabled` sia `true`.
  * Controlla `openclaw commitments --all` per record in attesa, ignorati, posticipati o scaduti.
  * Assicurati che Heartbeat sia in esecuzione per l'agente.
  * Controlla se `commitments.maxPerDay` è già stato raggiunto per quella sessione agente.
  * Ricorda che i promemoria esatti vengono saltati dall'estrazione degli impegni e dovrebbero comparire invece sotto [attività pianificate](</it/automation/cron-jobs>).


## Correlati

  * [Panoramica della memoria](</it/concepts/memory>)
  * [Active memory](</it/concepts/active-memory>)
  * [Heartbeat](</it/gateway/heartbeat>)
  * [Attività pianificate](</it/automation/cron-jobs>)
  * [`openclaw commitments`](</it/cli/commitments>)
  * [Riferimento di configurazione](</it/gateway/configuration-reference#commitments>)


Was this useful?YesNo