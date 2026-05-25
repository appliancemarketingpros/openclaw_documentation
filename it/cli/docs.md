---
title: Documentazione
source_url: https://docs.openclaw.ai/it/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

Cerca l'indice della documentazione live di OpenClaw dal terminale. Il comando richiama l'endpoint pubblico di ricerca MCP della documentazione ospitata su Mintlify all'indirizzo `https://docs.openclaw.ai/mcp.SearchOpenClaw` e mostra i risultati nel terminale.

## Utilizzo

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

Argomenti:

Argomento | Descrizione  
---|---  
`[query...]` | Query di ricerca in formato libero. Le query con più parole vengono unite con spazi e inviate come una sola.  
  
## Esempi

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

Senza query, `openclaw docs` stampa l'URL del punto di ingresso della documentazione più un comando di ricerca di esempio, invece di eseguire una ricerca.

## Come funziona

`openclaw docs` invoca la CLI `mcporter` per chiamare lo strumento MCP di ricerca della documentazione, quindi analizza i blocchi `Title: / Link: / Content:` dall'output dello strumento in un elenco di risultati.

Per risolvere `mcporter`, OpenClaw controlla nell'ordine:

  1. `mcporter` su `PATH` (usato direttamente se presente).
  2. `pnpm dlx mcporter ...` se `pnpm` è installato.
  3. `npx -y mcporter ...` se `npx` è installato.


Se nessuno è disponibile, il comando fallisce con un suggerimento per installare `pnpm` (`npm install -g pnpm`).

La chiamata di ricerca usa un timeout fisso di 30 secondi. Gli estratti dei risultati vengono troncati a circa 220 caratteri per voce.

## Output

In un terminale avanzato (TTY), i risultati vengono mostrati come un'intestazione seguita da un elenco puntato. Ogni punto mostra il titolo della pagina, l'URL collegato della documentazione e un breve estratto nella riga successiva. I risultati vuoti stampano "Nessun risultato.".

Nell'output non avanzato (reindirizzato tramite pipe, `--no-color`, script), gli stessi dati vengono mostrati come Markdown:

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## Codici di uscita

Codice | Significato  
---|---  
`0` | Ricerca riuscita (incluse le risposte con zero risultati).  
`1` | La chiamata allo strumento MCP non è riuscita; stderr viene stampato inline.  
  
## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Documentazione live](<https://docs.openclaw.ai>)


Was this useful?YesNo