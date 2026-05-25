---
title: Memoria
source_url: https://docs.openclaw.ai/it/cli/memory
scraped_at: 2026-05-25
---

# `openclaw memory`

Gestisci l'indicizzazione e la ricerca della memoria semantica. Fornito dal Plugin Active Memory attivo (predefinito: `memory-core`; imposta `plugins.slots.memory = "none"` per disabilitarlo).

Correlati:

  * Concetto di memoria: [Memoria](</it/concepts/memory>)
  * Wiki della memoria: [Wiki della memoria](</it/plugins/memory-wiki>)
  * CLI wiki: [wiki](</it/cli/wiki>)
  * Plugin: [Plugin](</it/tools/plugin>)


## Esempi

bashCopy code
[code]
    openclaw memory statusopenclaw memory status --deepopenclaw memory status --fixopenclaw memory index --forceopenclaw memory search "meeting notes"openclaw memory search --query "deployment" --max-results 20openclaw memory promote --limit 10 --min-score 0.75openclaw memory promote --applyopenclaw memory promote --json --min-recall-count 0 --min-unique-queries 0openclaw memory promote-explain "router vlan"openclaw memory promote-explain "router vlan" --jsonopenclaw memory rem-harnessopenclaw memory rem-harness --jsonopenclaw memory status --jsonopenclaw memory status --deep --indexopenclaw memory status --deep --index --verboseopenclaw memory status --agent mainopenclaw memory index --agent main --verbose
[/code]

## Opzioni

`memory status` e `memory index`:

  * `--agent <id>`: limita l'ambito a un singolo agente. Senza questa opzione, questi comandi vengono eseguiti per ogni agente configurato; se non è configurato alcun elenco di agenti, ricadono sull'agente predefinito.
  * `--verbose`: emette log dettagliati durante i controlli e l'indicizzazione.


`memory status`:

  * `--deep`: verifica la prontezza del vector-store locale, del provider di embedding e della ricerca vettoriale semantica. Il semplice `memory status` resta rapido e non esegue embedding live né lavoro di rilevamento dei provider; uno stato sconosciuto del vector-store o del vettore semantico significa che non è stato verificato in quel comando. QMD lessicale `searchMode: "search"` salta i controlli vettoriali semantici e la manutenzione degli embedding anche con `--deep`.
  * `--index`: esegue una reindicizzazione se lo store è sporco (implica `--deep`).
  * `--fix`: ripara lock di richiamo obsoleti e normalizza i metadati di promozione.
  * `--json`: stampa output JSON.


Se `memory status` mostra `Dreaming status: blocked`, il Cron di dreaming gestito è abilitato ma l'Heartbeat che lo guida non sta scattando per l'agente predefinito. Consulta [Dreaming non viene mai eseguito](</it/concepts/dreaming#dreaming-never-runs-status-shows-blocked>) per le due cause comuni.

`memory index`:

  * `--force`: forza una reindicizzazione completa.


`memory search`:

  * Input della query: passa `[query]` posizionale oppure `--query <text>`.
  * Se vengono forniti entrambi, `--query` ha la precedenza.
  * Se non viene fornito nessuno dei due, il comando termina con un errore.
  * `--agent <id>`: limita l'ambito a un singolo agente (predefinito: l'agente predefinito).
  * `--max-results <n>`: limita il numero di risultati restituiti.
  * `--min-score <n>`: filtra le corrispondenze con punteggio basso.
  * `--json`: stampa risultati JSON.


`memory promote`:

Visualizza in anteprima e applica promozioni della memoria a breve termine.

bashCopy code
[code]
    openclaw memory promote [--apply] [--limit <n>] [--include-promoted]
[/code]

  * `--apply` \-- scrive le promozioni in `MEMORY.md` (predefinito: solo anteprima).
  * `--limit <n>` \-- limita il numero di candidati mostrati.
  * `--include-promoted` \-- include le voci già promosse nei cicli precedenti.


Opzioni complete:

  * Classifica i candidati a breve termine da `memory/YYYY-MM-DD.md` usando segnali di promozione ponderati (`frequency`, `relevance`, `query diversity`, `recency`, `consolidation`, `conceptual richness`).
  * Usa segnali a breve termine sia dai richiami di memoria sia dai passaggi di ingestione giornaliera, più segnali di rinforzo delle fasi light/REM.
  * Quando Dreaming è abilitato, `memory-core` gestisce automaticamente un job Cron che esegue una scansione completa (`light -> REM -> deep`) in background (non è richiesto alcun `openclaw cron add` manuale).
  * `--agent <id>`: limita l'ambito a un singolo agente (predefinito: l'agente predefinito).
  * `--limit <n>`: numero massimo di candidati da restituire/applicare.
  * `--min-score <n>`: punteggio minimo ponderato di promozione.
  * `--min-recall-count <n>`: numero minimo di richiami richiesto per un candidato.
  * `--min-unique-queries <n>`: numero minimo di query distinte richiesto per un candidato.
  * `--apply`: aggiunge i candidati selezionati a `MEMORY.md` e li marca come promossi.
  * `--include-promoted`: include nell'output i candidati già promossi.
  * `--json`: stampa output JSON.


`memory promote-explain`:

Spiega uno specifico candidato alla promozione e la scomposizione del suo punteggio.

bashCopy code
[code]
    openclaw memory promote-explain <selector> [--agent <id>] [--include-promoted] [--json]
[/code]

  * `<selector>`: chiave del candidato, frammento di percorso o frammento di snippet da cercare.
  * `--agent <id>`: limita l'ambito a un singolo agente (predefinito: l'agente predefinito).
  * `--include-promoted`: include i candidati già promossi.
  * `--json`: stampa output JSON.


`memory rem-harness`:

Visualizza in anteprima riflessioni REM, verità candidate e output di promozione deep senza scrivere nulla.

bashCopy code
[code]
    openclaw memory rem-harness [--agent <id>] [--include-promoted] [--json]
[/code]

  * `--agent <id>`: limita l'ambito a un singolo agente (predefinito: l'agente predefinito).
  * `--include-promoted`: include i candidati deep già promossi.
  * `--json`: stampa output JSON.


## Dreaming

Dreaming è il sistema di consolidamento della memoria in background con tre fasi cooperative: **light** (ordina/prepara il materiale a breve termine), **deep** (promuove fatti durevoli in `MEMORY.md`) e **REM** (riflette e fa emergere temi).

  * Abilitalo con `plugins.entries.memory-core.config.dreaming.enabled: true`.
  * Attivalo o disattivalo dalla chat con `/dreaming on|off` (oppure ispezionalo con `/dreaming status`).
  * Dreaming viene eseguito su una pianificazione di sweep gestita (`dreaming.frequency`) ed esegue le fasi in ordine: light, REM, deep.
  * Solo la fase deep scrive memoria durevole in `MEMORY.md`.
  * L'output delle fasi leggibile da persone e le voci di diario vengono scritti in `DREAMS.md` (o in `dreams.md` esistente), con report opzionali per fase in `memory/dreaming/<phase>/YYYY-MM-DD.md`.
  * Il ranking usa segnali ponderati: frequenza di richiamo, rilevanza del recupero, diversità delle query, recenza temporale, consolidamento tra giorni e ricchezza concettuale derivata.
  * La promozione rilegge la nota giornaliera live prima di scrivere in `MEMORY.md`, quindi snippet a breve termine modificati o eliminati non vengono promossi da snapshot obsoleti dello store di richiamo.
  * Le esecuzioni pianificate e manuali di `memory promote` condividono gli stessi valori predefiniti della fase deep, a meno che tu non passi override delle soglie tramite CLI.
  * Le esecuzioni automatiche vengono distribuite su tutti gli spazi di lavoro di memoria configurati.


Pianificazione predefinita:

  * **Cadenza dello sweep** : `dreaming.frequency = 0 3 * * *`
  * **Soglie deep** : `minScore=0.8`, `minRecallCount=3`, `minUniqueQueries=3`, `recencyHalfLifeDays=14`, `maxAgeDays=30`


Esempio:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true          }        }      }    }  }}
[/code]

Note:

  * `memory index --verbose` stampa dettagli per fase (provider, modello, fonti, attività batch).
  * `memory status` include eventuali percorsi aggiuntivi configurati tramite `memorySearch.extraPaths`.
  * Se i campi chiave API remoti della memoria attiva effettiva sono configurati come SecretRefs, il comando risolve quei valori dallo snapshot del Gateway attivo. Se il Gateway non è disponibile, il comando fallisce rapidamente.
  * Nota sul disallineamento di versione del Gateway: questo percorso di comando richiede un Gateway che supporti `secrets.resolve`; i Gateway più vecchi restituiscono un errore di metodo sconosciuto.
  * Regola la cadenza dello sweep pianificato con `dreaming.frequency`. La policy di promozione deep è altrimenti interna; usa i flag CLI su `memory promote` quando ti servono override manuali una tantum.
  * `memory rem-harness --path <file-or-dir> --grounded` visualizza in anteprima `What Happened`, `Reflections` e `Possible Lasting Updates` fondati da note giornaliere storiche senza scrivere nulla.
  * `memory rem-backfill --path <file-or-dir>` scrive voci di diario fondate e reversibili in `DREAMS.md` per la revisione nell'interfaccia utente.
  * `memory rem-backfill --path <file-or-dir> --stage-short-term` semina anche candidati durevoli fondati nello store di promozione a breve termine live, così la normale fase deep può classificarli.
  * `memory rem-backfill --rollback` rimuove le voci di diario fondate scritte in precedenza e `memory rem-backfill --rollback-short-term` rimuove i candidati a breve termine fondati precedentemente preparati.
  * Consulta [Dreaming](</it/concepts/dreaming>) per le descrizioni complete delle fasi e il riferimento di configurazione.


## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Panoramica della memoria](</it/concepts/memory>)


Was this useful?YesNo