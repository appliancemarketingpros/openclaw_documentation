---
title: Reimposta
source_url: https://docs.openclaw.ai/it/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

Reimposta configurazione/stato locali (mantiene installata la CLI).

Opzioni:

  * `--scope <scope>`: `config`, `config+creds+sessions` oppure `full`
  * `--yes`: salta le richieste di conferma
  * `--non-interactive`: disabilita i prompt; richiede `--scope` e `--yes`
  * `--dry-run`: stampa le azioni senza rimuovere i file


Esempi:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Note:

  * Esegui prima `openclaw backup create` se vuoi uno snapshot ripristinabile prima di rimuovere lo stato locale.
  * Se ometti `--scope`, `openclaw reset` usa un prompt interattivo per scegliere cosa rimuovere.
  * `--non-interactive` è valido solo quando sono impostati sia `--scope` sia `--yes`.


## Correlati

  * [Riferimento CLI](</it/cli>)


Was this useful?YesNo