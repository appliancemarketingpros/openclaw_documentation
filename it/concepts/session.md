---
title: Gestione delle sessioni
source_url: https://docs.openclaw.ai/it/concepts/session
scraped_at: 2026-05-25
---

OpenClaw organizza le conversazioni in **sessioni**. Ogni messaggio viene instradato a una sessione in base alla sua provenienza -- DM, chat di gruppo, processi cron, ecc.

## Come vengono instradati i messaggi

Origine | Comportamento  
---|---  
Messaggi diretti | Sessione condivisa per impostazione predefinita  
Chat di gruppo | Isolata per gruppo  
Stanze/canali | Isolata per stanza  
Processi Cron | Sessione nuova a ogni esecuzione  
Webhook | Isolata per hook  
  
## Isolamento dei DM

Per impostazione predefinita, tutti i DM condividono una sessione per garantire continuità. Questo va bene per configurazioni con un solo utente.

**La correzione:**

json5Copy code
[code]
    {  session: {    dmScope: "per-channel-peer", // isolate by channel + sender  },}
[/code]

Altre opzioni:

  * `main` (predefinita) -- tutti i DM condividono una sessione.
  * `per-peer` \-- isola per mittente (tra canali).
  * `per-channel-peer` \-- isola per canale + mittente (consigliata).
  * `per-account-channel-peer` \-- isola per account + canale + mittente.


### Collega canali agganciati

I comandi di aggancio consentono a un utente di spostare il percorso di risposta della sessione di chat diretta corrente a un altro canale collegato senza avviare una nuova sessione. Consulta [Aggancio dei canali](</it/concepts/channel-docking>) per esempi, configurazione e risoluzione dei problemi.

Verifica la tua configurazione con `openclaw security audit`.

## Ciclo di vita della sessione

Le sessioni vengono riutilizzate fino alla scadenza:

  * **Reset giornaliero** (predefinito) -- nuova sessione alle 4:00 ora locale sull'host del Gateway. La freschezza giornaliera si basa su quando è iniziato il `sessionId` corrente, non su successive scritture dei metadati.
  * **Reset per inattività** (opzionale) -- nuova sessione dopo un periodo di inattività. Imposta `session.reset.idleMinutes`. La freschezza per inattività si basa sull'ultima interazione reale utente/canale, quindi heartbeat, cron ed eventi di sistema exec non mantengono viva la sessione.
  * **Reset manuale** \-- digita `/new` o `/reset` in chat. `/new <model>` cambia anche il modello.


Quando sono configurati sia il reset giornaliero sia quello per inattività, prevale quello che scade per primo. Heartbeat, cron, exec e altri turni di eventi di sistema possono scrivere metadati della sessione, ma queste scritture non estendono la freschezza del reset giornaliero o per inattività. Quando un reset fa avanzare la sessione, gli avvisi di eventi di sistema in coda per la vecchia sessione vengono scartati, così gli aggiornamenti in background obsoleti non vengono anteposti al primo prompt nella nuova sessione.

Le sessioni con una sessione CLI attiva di proprietà del provider non vengono interrotte dall'impostazione predefinita giornaliera implicita. Usa `/reset` o configura esplicitamente `session.reset` quando queste sessioni devono scadere con un timer.

## Dove risiede lo stato

Tutto lo stato della sessione è di proprietà del **Gateway**. I client UI interrogano il Gateway per i dati della sessione.

  * **Archivio:** `~/.openclaw/agents/<agentId>/sessions/sessions.json`
  * **Trascrizioni:** `~/.openclaw/agents/<agentId>/sessions/<sessionId>.jsonl`


`sessions.json` mantiene timestamp separati per il ciclo di vita:

  * `sessionStartedAt`: quando è iniziato il `sessionId` corrente; il reset giornaliero usa questo valore.
  * `lastInteractionAt`: ultima interazione utente/canale che estende la durata per inattività.
  * `updatedAt`: ultima mutazione della riga dell'archivio; utile per elenchi e potatura, ma non autorevole per la freschezza del reset giornaliero/per inattività.


Le righe più vecchie senza `sessionStartedAt` vengono risolte dall'intestazione della sessione JSONL della trascrizione quando disponibile. Se una riga più vecchia manca anche di `lastInteractionAt`, la freschezza per inattività ricade sull'ora di inizio di quella sessione, non su successive scritture di manutenzione.

## Manutenzione delle sessioni

OpenClaw limita automaticamente nel tempo l'archiviazione delle sessioni. Per impostazione predefinita, viene eseguito in modalità `warn` (segnala cosa verrebbe ripulito). Imposta `session.maintenance.mode` su `"enforce"` per la pulizia automatica:

json5Copy code
[code]
    {  session: {    maintenance: {      mode: "enforce",      pruneAfter: "30d",      maxEntries: 500,    },  },}
[/code]

Per limiti `maxEntries` dimensionati per la produzione, le scritture del runtime Gateway usano un piccolo buffer high-water e ripuliscono a lotti fino al limite configurato. Le letture dell'archivio sessioni non potano né limitano le voci durante l'avvio del Gateway. Questo evita di eseguire la pulizia completa dell'archivio a ogni avvio o sessione cron isolata. `openclaw sessions cleanup --enforce` applica subito il limite.

La manutenzione preserva i puntatori durevoli alle conversazioni esterne, incluse le sessioni di gruppo e le sessioni di chat con ambito thread, pur consentendo alle voci sintetiche di cron, hook, heartbeat, ACP e sub-agenti di invecchiare ed essere rimosse.

Se in precedenza hai usato l'isolamento dei messaggi diretti e poi hai riportato `session.dmScope` a `main`, visualizza in anteprima le righe DM obsolete con chiave peer usando `openclaw sessions cleanup --dry-run --fix-dm-scope`. L'applicazione dello stesso flag ritira quelle vecchie righe DM dirette e mantiene le relative trascrizioni come archivi eliminati.

Visualizza l'anteprima con `openclaw sessions cleanup --dry-run`.

## Ispezione delle sessioni

  * `openclaw status` \-- percorso dell'archivio sessioni e attività recente.
  * `openclaw sessions --json` \-- tutte le sessioni (filtra con `--active <minutes>`).
  * `/status` in chat -- uso del contesto, modello e toggle.
  * `/context list` \-- cosa contiene il prompt di sistema.


## Ulteriori letture

  * [Potatura delle sessioni](</it/concepts/session-pruning>) \-- riduzione dei risultati degli strumenti
  * [Compaction](</it/concepts/compaction>) \-- riepilogo delle conversazioni lunghe
  * [Strumenti di sessione](</it/concepts/session-tool>) \-- strumenti dell'agente per il lavoro tra sessioni
  * [Approfondimento sulla gestione delle sessioni](</it/reference/session-management-compaction>) \-- schema dell'archivio, trascrizioni, policy di invio, metadati di origine e configurazione avanzata
  * [Multi-agente](</it/concepts/multi-agent>) — instradamento e isolamento delle sessioni tra agenti
  * [Attività in background](</it/automation/tasks>) — come il lavoro scollegato crea record di attività con riferimenti alla sessione
  * [Instradamento dei canali](</it/channels/channel-routing>) — come i messaggi in ingresso vengono instradati alle sessioni


## Correlati

  * [Potatura delle sessioni](</it/concepts/session-pruning>)
  * [Strumenti di sessione](</it/concepts/session-tool>)
  * [Coda dei comandi](</it/concepts/queue>)


Was this useful?YesNo