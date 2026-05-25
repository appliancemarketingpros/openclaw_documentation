---
title: TUI
source_url: https://docs.openclaw.ai/it/cli/tui
scraped_at: 2026-05-25
---

# `openclaw tui`

Apri la UI da terminale connessa al Gateway oppure eseguila in modalità incorporata locale.

Correlati:

  * Guida TUI: [TUI](</it/web/tui>)


## Opzioni

Flag | Predefinito | Descrizione  
---|---|---  
`--local` | `false` | Esegui sul runtime dell'agente incorporato locale invece che su un Gateway.  
`--url <url>` | `gateway.remote.url` dalla configurazione | URL WebSocket del Gateway.  
`--token <token>` | (nessuno) | Token del Gateway se richiesto.  
`--password <pass>` | (nessuno) | Password del Gateway se richiesta.  
`--session <key>` | `main` (o `global` quando l'ambito è globale) | Chiave di sessione. Dentro un workspace agente seleziona automaticamente quell'agente, salvo prefisso.  
`--deliver` | `false` | Recapita le risposte dell'assistente tramite i canali configurati.  
`--thinking <level>` | (predefinito del modello) | Override del livello di ragionamento.  
`--message <text>` | (nessuno) | Invia un messaggio iniziale dopo la connessione.  
`--timeout-ms <ms>` | `agents.defaults.timeoutSeconds` | Timeout dell'agente. I valori non validi registrano un avviso e vengono ignorati.  
`--history-limit <n>` | `200` | Voci della cronologia da caricare all'attach.  
  
Alias: `openclaw chat` e `openclaw terminal` invocano lo stesso comando con `--local` implicito.

Note:

  * `chat` e `terminal` sono alias di `openclaw tui --local`.
  * `--local` non può essere combinato con `--url`, `--token` o `--password`.
  * `tui` risolve, quando possibile, le SecretRefs di autenticazione Gateway configurate per l'autenticazione tramite token/password (provider `env`/`file`/`exec`).
  * Quando avviata dall'interno di una directory workspace agente configurata, TUI seleziona automaticamente quell'agente come valore predefinito della chiave di sessione (salvo che `--session` sia esplicitamente `agent:<id>:...`).
  * La modalità locale usa direttamente il runtime dell'agente incorporato. La maggior parte degli strumenti locali funziona, ma le funzionalità solo Gateway non sono disponibili.
  * La modalità locale aggiunge `/auth [provider]` nella superficie dei comandi TUI.
  * I gate di approvazione dei Plugin si applicano comunque in modalità locale. Gli strumenti che richiedono approvazione chiedono una decisione nel terminale; nulla viene approvato automaticamente in silenzio solo perché il Gateway non è coinvolto.


## Esempi

bashCopy code
[code]
    openclaw chatopenclaw tui --localopenclaw tuiopenclaw tui --url ws://127.0.0.1:18789 --token <token>openclaw tui --session main --deliveropenclaw chat --message "Compare my config to the docs and tell me what to fix"# when run inside an agent workspace, infers that agent automaticallyopenclaw tui --session bugfix
[/code]

## Ciclo di riparazione della configurazione

Usa la modalità locale quando la configurazione corrente è già valida e vuoi che l'agente incorporato la ispezioni, la confronti con la documentazione e aiuti a ripararla dallo stesso terminale:

Se `openclaw config validate` sta già fallendo, usa prima `openclaw configure` o `openclaw doctor --fix`. `openclaw chat` non aggira la protezione contro la configurazione non valida.

bashCopy code
[code]
    openclaw chat
[/code]

Poi dentro la TUI:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

Applica correzioni mirate con `openclaw config set` o `openclaw configure`, quindi riesegui `openclaw config validate`. Vedi [TUI](</it/web/tui>) e [Configurazione](</it/cli/config>).

## Correlati

  * [Riferimento CLI](</it/cli>)
  * [TUI](</it/web/tui>)


Was this useful?YesNo