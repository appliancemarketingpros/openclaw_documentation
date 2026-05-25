---
title: Disinstalla
source_url: https://docs.openclaw.ai/it/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

Disinstalla il servizio Gateway + i dati locali (la CLI resta).

Opzioni:

  * `--service`: rimuove il servizio Gateway
  * `--state`: rimuove stato e configurazione
  * `--workspace`: rimuove le directory dello spazio di lavoro
  * `--app`: rimuove l'app macOS
  * `--all`: rimuove servizio, stato, spazio di lavoro e app
  * `--yes`: salta i prompt di conferma
  * `--non-interactive`: disattiva i prompt; richiede `--yes`
  * `--dry-run`: stampa le azioni senza rimuovere i file


Esempi:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Note:

  * Esegui prima `openclaw backup create` se vuoi un'istantanea ripristinabile prima di rimuovere stato o spazi di lavoro.
  * `--all` è l'abbreviazione per rimuovere insieme servizio, stato, spazio di lavoro e app.
  * `--non-interactive` richiede `--yes`.


## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Disinstallazione](</it/install/uninstall>)


Was this useful?YesNo