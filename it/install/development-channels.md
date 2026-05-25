---
title: Canali di rilascio
source_url: https://docs.openclaw.ai/it/install/development-channels
scraped_at: 2026-05-25
---

OpenClaw offre tre canali di aggiornamento:

  * **stable** : dist-tag npm `latest`. Consigliato per la maggior parte degli utenti.
  * **beta** : dist-tag npm `beta` quando è corrente; se beta manca o è più vecchio dell'ultima release stabile, il flusso di aggiornamento ripiega su `latest`.
  * **dev** : head mobile di `main` (git). dist-tag npm: `dev` (quando pubblicato). Il branch `main` è destinato alla sperimentazione e allo sviluppo attivo. Può contenere funzionalità incomplete o modifiche incompatibili. Non usarlo per Gateway di produzione.


Di solito pubblichiamo le build stabili prima su **beta** , le testiamo lì, poi eseguiamo un passaggio esplicito di promozione che sposta la build verificata su `latest` senza modificare il numero di versione. I maintainer possono anche pubblicare una release stabile direttamente su `latest` quando necessario. I dist-tag sono la fonte di verità per le installazioni npm.

## Cambio di canale

bashCopy code
[code]
    openclaw update --channel stableopenclaw update --channel betaopenclaw update --channel dev
[/code]

`--channel` conserva la scelta nella configurazione (`update.channel`) e allinea il metodo di installazione:

  * **`stable`** (installazioni da pacchetto): aggiorna tramite il dist-tag npm `latest`.
  * **`beta`** (installazioni da pacchetto): preferisce il dist-tag npm `beta`, ma ripiega su `latest` quando `beta` manca o è più vecchio del tag stabile corrente.
  * **`stable`** (installazioni git): passa all'ultimo tag git stabile.
  * **`beta`** (installazioni git): preferisce l'ultimo tag git beta, ma ripiega sull'ultimo tag git stabile quando beta manca o è più vecchio.
  * **`dev`** : assicura un checkout git (predefinito `~/openclaw`, sovrascrivibile con `OPENCLAW_GIT_DIR`), passa a `main`, esegue il rebase su upstream, compila e installa la CLI globale da quel checkout.


## Destinazione di una versione o di un tag una tantum

Usa `--tag` per puntare a un dist-tag, una versione o una spec di pacchetto specifici per un singolo aggiornamento **senza** modificare il canale salvato:

bashCopy code
[code]
    # Install a specific versionopenclaw update --tag 2026.4.1-beta.1 # Install from the beta dist-tag (one-off, does not persist)openclaw update --tag beta # Install from GitHub main branch (npm tarball)openclaw update --tag main # Install a specific npm package specopenclaw update --tag openclaw@2026.4.1-beta.1
[/code]

Note:

  * `--tag` si applica **solo alle installazioni da pacchetto (npm)**. Le installazioni git lo ignorano.
  * Il tag non viene salvato. Il prossimo `openclaw update` userà come di consueto il canale configurato.
  * Protezione dal downgrade: se la versione di destinazione è più vecchia della tua versione corrente, OpenClaw chiede conferma (salta con `--yes`).
  * `--channel beta` è diverso da `--tag beta`: il flusso del canale può ripiegare su stable/latest quando beta manca o è più vecchio, mentre `--tag beta` punta al dist-tag `beta` grezzo per quella singola esecuzione.


## Prova a secco

Visualizza in anteprima cosa farebbe `openclaw update` senza apportare modifiche:

bashCopy code
[code]
    openclaw update --dry-runopenclaw update --channel beta --dry-runopenclaw update --tag 2026.4.1-beta.1 --dry-runopenclaw update --dry-run --json
[/code]

La prova a secco mostra il canale effettivo, la versione di destinazione, le azioni pianificate e se sarebbe richiesta una conferma di downgrade.

## Plugin e canali

Quando cambi canale con `openclaw update`, OpenClaw sincronizza anche le sorgenti dei Plugin:

  * `dev` preferisce i Plugin inclusi dal checkout git.
  * `stable` e `beta` ripristinano i pacchetti Plugin installati da npm.
  * I Plugin installati da npm vengono aggiornati dopo il completamento dell'aggiornamento del core.


## Verifica dello stato corrente

bashCopy code
[code]
    openclaw update status
[/code]

Mostra il canale attivo, il tipo di installazione (git o pacchetto), la versione corrente e l'origine (configurazione, tag git, branch git o predefinita).

## Migliori pratiche per i tag

  * Tagga le release su cui vuoi che arrivino i checkout git (`vYYYY.M.D` per stable, `vYYYY.M.D-beta.N` per beta).
  * Anche `vYYYY.M.D.beta.N` è riconosciuto per compatibilità, ma preferisci `-beta.N`.
  * I tag legacy `vYYYY.M.D-<patch>` sono ancora riconosciuti come stabili (non beta).
  * Mantieni i tag immutabili: non spostare né riutilizzare mai un tag.
  * I dist-tag npm restano la fonte di verità per le installazioni npm: 
    * `latest` -> stable
    * `beta` -> build candidata o build stabile prima in beta
    * `dev` -> snapshot di main (facoltativo)


## Disponibilità dell'app macOS

Le build beta e dev potrebbero **non** includere una release dell'app macOS. Va bene così:

  * Il tag git e il dist-tag npm possono comunque essere pubblicati.
  * Indica "nessuna build macOS per questa beta" nelle note di release o nel changelog.


## Correlati

  * [Aggiornamento](</it/install/updating>)
  * [Interni dell'installer](</it/install/installer>)


Was this useful?YesNo