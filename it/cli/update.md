---
title: Aggiorna
source_url: https://docs.openclaw.ai/it/cli/update
scraped_at: 2026-05-25
---

# `openclaw update`

Aggiorna OpenClaw in sicurezza e passa tra i canali stable/beta/dev.

Se hai installato tramite **npm/pnpm/bun** (installazione globale, senza metadati git), gli aggiornamenti avvengono tramite il flusso del gestore di pacchetti in [Aggiornamento](</it/install/updating>).

## Utilizzo

bashCopy code
[code]
    openclaw updateopenclaw update statusopenclaw update wizardopenclaw update --channel betaopenclaw update --channel devopenclaw update --tag betaopenclaw update --tag mainopenclaw update --dry-runopenclaw update --no-restartopenclaw update --yesopenclaw update --jsonopenclaw --update
[/code]

## Opzioni

  * `--no-restart`: salta il riavvio del servizio Gateway dopo un aggiornamento riuscito. Gli aggiornamenti tramite gestore di pacchetti che riavviano il Gateway verificano che il servizio riavviato riporti la versione aggiornata prevista prima che il comando venga completato con successo.
  * `--channel <stable|beta|dev>`: imposta il canale di aggiornamento (git + npm; persistito nella configurazione).
  * `--tag <dist-tag|version|spec>`: sovrascrive la destinazione del pacchetto solo per questo aggiornamento. Per le installazioni da pacchetto, `main` corrisponde a `github:openclaw/openclaw#main`.
  * `--dry-run`: mostra in anteprima le azioni di aggiornamento pianificate (flusso canale/tag/destinazione/riavvio) senza scrivere la configurazione, installare, sincronizzare plugin o riavviare.
  * `--json`: stampa JSON `UpdateRunResult` leggibile da macchina, inclusi `postUpdate.plugins.warnings` quando plugin gestiti corrotti o non caricabili richiedono una riparazione dopo il completamento dell’aggiornamento del core, i dettagli del fallback dei plugin del canale beta quando un plugin non ha una release beta, e `postUpdate.plugins.integrityDrifts` quando viene rilevata una deriva degli artefatti dei plugin npm durante la sincronizzazione dei plugin post-aggiornamento.
  * `--timeout <seconds>`: timeout per passaggio (il valore predefinito è 1800s).
  * `--yes`: salta le richieste di conferma (per esempio la conferma di downgrade).


`openclaw update` non ha un flag `--verbose`. Usa `--dry-run` per visualizzare in anteprima le azioni pianificate di canale/tag/installazione/riavvio, `--json` per risultati leggibili da macchina e `openclaw update status --json` quando ti servono solo i dettagli su canale e disponibilità. Se stai eseguendo il debug dei log del Gateway durante un aggiornamento, la verbosità della console e il livello dei log su file sono separati: `--verbose` del Gateway influisce sull’output del terminale/WebSocket, mentre i log su file richiedono `logging.level: "debug"` o `"trace"` nella configurazione. Vedi [Logging del Gateway](</it/gateway/logging>).

## `update status`

Mostra il canale di aggiornamento attivo + tag/branch/SHA git (per checkout sorgente), oltre alla disponibilità di aggiornamenti.

bashCopy code
[code]
    openclaw update statusopenclaw update status --jsonopenclaw update status --timeout 10
[/code]

Opzioni:

  * `--json`: stampa JSON di stato leggibile da macchina.
  * `--timeout <seconds>`: timeout per i controlli (il valore predefinito è 3s).


## `update wizard`

Flusso interattivo per scegliere un canale di aggiornamento e confermare se riavviare il Gateway dopo l’aggiornamento (il valore predefinito è riavviare). Se selezioni `dev` senza un checkout git, offre di crearne uno.

Opzioni:

  * `--timeout <seconds>`: timeout per ogni passaggio di aggiornamento (valore predefinito `1800`)


## Cosa fa

Quando cambi canale esplicitamente (`--channel ...`), OpenClaw mantiene allineato anche il metodo di installazione:

  * `dev` → assicura un checkout git (valore predefinito: `~/openclaw`, sovrascrivibile con `OPENCLAW_GIT_DIR`), lo aggiorna e installa la CLI globale da quel checkout.
  * `stable` → installa da npm usando `latest`.
  * `beta` → preferisce il dist-tag npm `beta`, ma ripiega su `latest` quando beta è mancante o precedente alla release stabile corrente.


L’auto-updater del core del Gateway (quando abilitato tramite configurazione) avvia il percorso di aggiornamento della CLI fuori dall’handler di richiesta Gateway attivo. Gli aggiornamenti tramite gestore di pacchetti del control-plane `update.run` forzano un riavvio di aggiornamento non differito e senza cooldown dopo la sostituzione del pacchetto, perché il vecchio processo Gateway potrebbe avere ancora in memoria chunk che puntano a file rimossi dal nuovo pacchetto.

Per le installazioni tramite gestore di pacchetti, `openclaw update` risolve la versione del pacchetto di destinazione prima di invocare il gestore di pacchetti. Le installazioni globali npm usano un’installazione a staging: OpenClaw installa il nuovo pacchetto in un prefisso npm temporaneo, verifica l’inventario `dist` pacchettizzato lì, poi scambia quell’albero di pacchetti pulito nel prefisso globale reale. Se la verifica fallisce, doctor post-aggiornamento, sincronizzazione dei plugin e riavvio non vengono eseguiti dall’albero sospetto. Anche quando la versione installata corrisponde già alla destinazione, il comando aggiorna l’installazione globale del pacchetto, poi esegue la sincronizzazione dei plugin, un aggiornamento del completamento dei comandi core e il riavvio. Questo mantiene sidecar pacchettizzati e record di plugin posseduti dal canale allineati con la build OpenClaw installata, lasciando le ricostruzioni complete del completamento dei comandi dei plugin alle esecuzioni esplicite di `openclaw completion --write-state`.

Quando è installato un servizio Gateway gestito locale e il riavvio è abilitato, gli aggiornamenti tramite gestore di pacchetti arrestano il servizio in esecuzione prima di sostituire l’albero del pacchetto, poi aggiornano i metadati del servizio dall’installazione aggiornata, riavviano il servizio e verificano che il Gateway riavviato riporti la versione prevista prima di segnalare il successo. Su macOS, il controllo post-aggiornamento verifica anche che il LaunchAgent sia caricato/in esecuzione per il profilo attivo e che la porta local loopback configurata sia integra. Se il plist è installato ma launchd non lo sta supervisionando, OpenClaw riesegue automaticamente il bootstrap del LaunchAgent, poi riesegue i controlli di prontezza di salute/versione/canale. Un bootstrap pulito carica direttamente il job RunAtLoad, quindi il recupero dell’aggiornamento non esegue immediatamente `kickstart -k` sul Gateway appena avviato. Se il Gateway continua a non diventare integro, il comando termina con codice diverso da zero e stampa il percorso del log di riavvio più istruzioni esplicite per riavvio, reinstallazione e rollback del pacchetto. Con `--no-restart`, la sostituzione del pacchetto viene comunque eseguita ma il servizio gestito non viene arrestato o riavviato, quindi il Gateway in esecuzione può mantenere il vecchio codice finché non lo riavvii manualmente.

## Flusso di checkout git

### Selezione del canale

  * `stable`: esegue il checkout del tag non beta più recente, poi build e doctor.
  * `beta`: preferisce il tag `-beta` più recente, ma ripiega sul tag stabile più recente quando beta è mancante o precedente.
  * `dev`: esegue il checkout di `main`, poi fetch e rebase.


### Passaggi di aggiornamento

* ### Verifica worktree pulito

Richiede che non ci siano modifiche non committate.

* ### Cambia canale

Passa al canale selezionato (tag o branch).

* ### Fetch upstream

Solo dev.

* ### Build preflight (solo dev)

Esegue la build TypeScript in un worktree temporaneo. Se la punta fallisce, risale fino a 10 commit per trovare il commit più recente che può essere compilato. Imposta `OPENCLAW_UPDATE_PREFLIGHT_LINT=1` per eseguire anche il lint durante questo preflight; il lint viene eseguito in modalità seriale vincolata perché gli host di aggiornamento degli utenti sono spesso più piccoli dei runner CI.

* ### Rebase

Esegue il rebase sul commit selezionato (solo dev).

* ### Installa dipendenze

Usa il gestore di pacchetti del repo. Per checkout pnpm, l’updater esegue il bootstrap di `pnpm` su richiesta (prima tramite `corepack`, poi con fallback temporaneo `npm install pnpm@11`) invece di eseguire `npm run build` dentro un workspace pnpm.

* ### Build Control UI

Compila il gateway e la Control UI.

* ### Esegui doctor

`openclaw doctor` viene eseguito come controllo finale di aggiornamento sicuro.

* ### Sincronizza plugin

Sincronizza i plugin con il canale attivo. Dev usa plugin inclusi; stable e beta usano npm. Aggiorna le installazioni di plugin tracciate.

Sul canale di aggiornamento beta, le installazioni di plugin npm e ClawHub tracciate che seguono la linea predefinita/latest provano prima una release plugin `@beta`. Se il plugin non ha una release beta, OpenClaw ripiega sulla spec predefinita/latest registrata e lo segnala come avviso. Per i plugin npm, OpenClaw ripiega anche quando il pacchetto beta esiste ma non supera la validazione dell’installazione. Questi avvisi di fallback dei plugin non fanno fallire l’aggiornamento del core. Versioni esatte e tag espliciti non vengono riscritti.

## Scorciatoia `--update`

`openclaw --update` viene riscritto in `openclaw update` (utile per shell e script di avvio).

## Correlati

  * `openclaw doctor` (offre di eseguire prima update sui checkout git)
  * [Canali di sviluppo](</it/install/development-channels>)
  * [Aggiornamento](</it/install/updating>)
  * [Riferimento CLI](</it/cli>)


Was this useful?YesNo