---
title: Chiamata vocale
source_url: https://docs.openclaw.ai/it/cli/voicecall
scraped_at: 2026-05-25
---

# `openclaw voicecall`

`voicecall` è un comando fornito da un Plugin. Compare solo quando il Plugin per le chiamate vocali è installato e abilitato.

Quando il Gateway è in esecuzione, i comandi operativi (`call`, `start`, `continue`, `speak`, `dtmf`, `end`, `status`) vengono instradati al runtime delle chiamate vocali di quel Gateway. Se nessun Gateway è raggiungibile, ricadono su un runtime CLI autonomo.

## Sottocomandi

bashCopy code
[code]
    openclaw voicecall setup    [--json]openclaw voicecall smoke    [-t <phone>] [--message <text>] [--mode <m>] [--yes] [--json]openclaw voicecall call     -m <text> [-t <phone>] [--mode <m>]openclaw voicecall start    --to <phone> [--message <text>] [--mode <m>]openclaw voicecall continue --call-id <id> --message <text>openclaw voicecall speak    --call-id <id> --message <text>openclaw voicecall dtmf     --call-id <id> --digits <digits>openclaw voicecall end      --call-id <id>openclaw voicecall status   [--call-id <id>] [--json]openclaw voicecall tail     [--file <path>] [--since <n>] [--poll <ms>]openclaw voicecall latency  [--file <path>] [--last <n>]openclaw voicecall expose   [--mode <m>] [--path <p>] [--port <port>] [--serve-path <p>]
[/code]

Sottocomando | Descrizione  
---|---  
`setup` | Mostra i controlli di prontezza del provider e del Webhook.  
`smoke` | Esegue i controlli di prontezza; effettua una chiamata di test live solo con `--yes`.  
`call` | Avvia una chiamata vocale in uscita.  
`start` | Alias di `call` con `--to` obbligatorio e `--message` opzionale.  
`continue` | Pronuncia un messaggio e attende la risposta successiva.  
`speak` | Pronuncia un messaggio senza attendere una risposta.  
`dtmf` | Invia cifre DTMF a una chiamata attiva.  
`end` | Termina una chiamata attiva.  
`status` | Ispeziona le chiamate attive (o una tramite `--call-id`).  
`tail` | Segue `calls.jsonl` (utile durante i test del provider).  
`latency` | Riassume le metriche di latenza dei turni da `calls.jsonl`.  
`expose` | Attiva/disattiva Tailscale serve/funnel per l'endpoint Webhook.  
  
## Configurazione e smoke

### `setup`

Per impostazione predefinita stampa controlli di prontezza leggibili. Passa `--json` per gli script.

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall setup --json
[/code]

### `smoke`

Esegue gli stessi controlli di prontezza. Non effettuerà una vera telefonata a meno che siano presenti sia `--to` sia `--yes`.

Flag | Predefinito | Descrizione  
---|---|---  
`-t, --to <phone>` | (nessuno) | Numero di telefono da chiamare per uno smoke live.  
`--message <text>` | `OpenClaw voice call smoke test.` | Messaggio da pronunciare durante la chiamata smoke.  
`--mode <mode>` | `notify` | Modalità chiamata: `notify` o `conversation`.  
`--yes` | `false` | Effettua davvero la chiamata live in uscita.  
`--json` | `false` | Stampa JSON leggibile dalla macchina.  
bashCopy code
[code]
    openclaw voicecall smokeopenclaw voicecall smoke --to "+15555550123"        # dry runopenclaw voicecall smoke --to "+15555550123" --yes  # live notify call
[/code]

## Ciclo di vita della chiamata

### `call`

Avvia una chiamata vocale in uscita.

Flag | Obbligatorio | Predefinito | Descrizione  
---|---|---|---  
`-m, --message <text>` | sì | (nessuno) | Messaggio da pronunciare quando la chiamata si connette.  
`-t, --to <phone>` | no | config `toNumber` | Numero di telefono E.164 da chiamare.  
`--mode <mode>` | no | `conversation` | Modalità chiamata: `notify` (riaggancia dopo il messaggio) o `conversation` (resta aperta).  
bashCopy code
[code]
    openclaw voicecall call --to "+15555550123" --message "Hello"openclaw voicecall call -m "Heads up" --mode notify
[/code]

### `start`

Alias di `call` con una diversa forma predefinita dei flag.

Flag | Obbligatorio | Predefinito | Descrizione  
---|---|---|---  
`--to <phone>` | sì | (nessuno) | Numero di telefono da chiamare.  
`--message <text>` | no | (nessuno) | Messaggio da pronunciare quando la chiamata si connette.  
`--mode <mode>` | no | `conversation` | Modalità chiamata: `notify` o `conversation`.  
  
### `continue`

Pronuncia un messaggio e attende una risposta.

Flag | Obbligatorio | Descrizione  
---|---|---  
`--call-id <id>` | sì | ID chiamata.  
`--message <text>` | sì | Messaggio da pronunciare.  
  
### `speak`

Pronuncia un messaggio senza attendere una risposta.

Flag | Obbligatorio | Descrizione  
---|---|---  
`--call-id <id>` | sì | ID chiamata.  
`--message <text>` | sì | Messaggio da pronunciare.  
  
### `dtmf`

Invia cifre DTMF a una chiamata attiva.

Flag | Obbligatorio | Descrizione  
---|---|---  
`--call-id <id>` | sì | ID chiamata.  
`--digits <digits>` | sì | Cifre DTMF (ad es. `ww123456#` per le attese).  
  
### `end`

Termina una chiamata attiva.

Flag | Obbligatorio | Descrizione  
---|---|---  
`--call-id <id>` | sì | ID chiamata.  
  
### `status`

Ispeziona le chiamate attive.

Flag | Predefinito | Descrizione  
---|---|---  
`--call-id <id>` | (nessuno) | Limita l'output a una sola chiamata.  
`--json` | `false` | Stampa JSON leggibile dalla macchina.  
bashCopy code
[code]
    openclaw voicecall statusopenclaw voicecall status --jsonopenclaw voicecall status --call-id <id>
[/code]

## Log e metriche

### `tail`

Segue il log JSONL delle chiamate vocali. Stampa le ultime righe indicate da `--since` all'avvio, poi trasmette le nuove righe man mano che vengono scritte.

Flag | Predefinito | Descrizione  
---|---|---  
`--file <path>` | risolto dallo store del Plugin | Percorso di `calls.jsonl`.  
`--since <n>` | `25` | Righe da stampare prima del tailing.  
`--poll <ms>` | `250` (minimo 50) | Intervallo di polling in millisecondi.  
  
### `latency`

Riassume le metriche di latenza dei turni e di attesa dell'ascolto da `calls.jsonl`. L'output è JSON con riepiloghi `recordsScanned`, `turnLatency` e `listenWait`.

Flag | Predefinito | Descrizione  
---|---|---  
`--file <path>` | risolto dallo store del Plugin | Percorso di `calls.jsonl`.  
`--last <n>` | `200` (minimo 1) | Numero di record recenti da analizzare.  
  
## Esporre i Webhook

### `expose`

Abilita, disabilita o modifica la configurazione Tailscale serve/funnel per il Webhook vocale.

Flag | Predefinito | Descrizione  
---|---|---  
`--mode <mode>` | `funnel` | `off`, `serve` (tailnet) o `funnel` (pubblico).  
`--path <path>` | config `tailscale.path` o `--serve-path` | Percorso Tailscale da esporre.  
`--port <port>` | config `serve.port` o `3334` | Porta Webhook locale.  
`--serve-path <path>` | config `serve.path` o `/voice/webhook` | Percorso Webhook locale.  
bashCopy code
[code]
    openclaw voicecall expose --mode serveopenclaw voicecall expose --mode funnelopenclaw voicecall expose --mode off
[/code]

## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Plugin per chiamate vocali](</it/plugins/voice-call>)


Was this useful?YesNo