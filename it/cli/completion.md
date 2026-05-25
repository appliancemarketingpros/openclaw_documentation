---
title: Completamento
source_url: https://docs.openclaw.ai/it/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

Genera script di completamento della shell e facoltativamente li installa nel profilo della shell.

## Utilizzo

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Opzioni

  * `-s, --shell <shell>`: target shell (`zsh`, `bash`, `powershell`, `fish`; predefinito: `zsh`)
  * `-i, --install`: installa il completamento aggiungendo una riga source al profilo della shell
  * `--write-state`: scrive gli script di completamento in `$OPENCLAW_STATE_DIR/completions` senza stamparli su stdout
  * `-y, --yes`: salta le richieste di conferma per l'installazione


## Note

  * `--install` scrive un piccolo blocco "OpenClaw Completion" nel profilo della shell e lo punta allo script memorizzato nella cache.
  * Senza `--install` o `--write-state`, il comando stampa lo script su stdout.
  * La generazione del completamento carica in modo eager gli alberi dei comandi così che siano inclusi i sottocomandi annidati.


## Correlati

  * [Riferimento CLI](</it/cli>)


Was this useful?YesNo