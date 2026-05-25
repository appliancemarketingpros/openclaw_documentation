---
title: Configurazione
source_url: https://docs.openclaw.ai/it/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

Inizializza la configurazione di base e il workspace dell'agente. Con qualsiasi opzione di configurazione iniziale presente, esegue anche la procedura guidata.

## Opzioni

Opzione | Descrizione  
---|---  
`--workspace <dir>` | Directory del workspace dell'agente (predefinita `~/.openclaw/workspace`; salvata come `agents.defaults.workspace`).  
`--wizard` | Esegue la configurazione iniziale interattiva.  
`--non-interactive` | Esegue la configurazione iniziale senza prompt.  
`--mode <mode>` | Modalità di configurazione iniziale: `local` o `remote`.  
`--import-from <provider>` | Provider di migrazione da eseguire durante la configurazione iniziale.  
`--import-source <path>` | Home dell'agente sorgente per `--import-from`.  
`--import-secrets` | Importa i segreti supportati durante la migrazione della configurazione iniziale.  
`--remote-url <url>` | URL WebSocket del Gateway remoto.  
`--remote-token <token>` | Token del Gateway remoto (facoltativo).  
  
### Avvio automatico della procedura guidata

`openclaw setup` esegue la procedura guidata quando una di queste opzioni è esplicitamente presente, anche senza `--wizard`:

`--wizard`, `--non-interactive`, `--mode`, `--import-from`, `--import-source`, `--import-secrets`, `--remote-url`, `--remote-token`.

## Esempi

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## Note

  * Il semplice `openclaw setup` inizializza configurazione e workspace senza eseguire il flusso completo di configurazione iniziale.
  * Dopo il setup semplice, esegui `openclaw onboard` per il percorso guidato completo, `openclaw configure` per modifiche mirate oppure `openclaw channels add` per aggiungere account di canale.
  * Se viene rilevato lo stato di Hermes, la configurazione iniziale interattiva può proporre automaticamente la migrazione. La configurazione iniziale con importazione richiede un setup nuovo; usa [Migra](</it/cli/migrate>) per piani di simulazione, backup e modalità di sovrascrittura al di fuori della configurazione iniziale.


## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Configurazione iniziale (CLI)](</it/start/wizard>)
  * [Primi passi](</it/start/getting-started>)
  * [Panoramica dell'installazione](</it/install>)


Was this useful?YesNo