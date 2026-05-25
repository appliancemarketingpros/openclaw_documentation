---
title: Registrazione dei log del Gateway
source_url: https://docs.openclaw.ai/it/gateway/logging
scraped_at: 2026-05-25
---

# Registrazione dei log

Per una panoramica rivolta all’utente (CLI + Control UI + configurazione), vedi [/logging](</it/logging>).

OpenClaw ha due "superfici" di log:

  * **Output della console** (ciò che vedi nel terminale / Debug UI).
  * **Log su file** (righe JSON) scritti dal logger del Gateway.


All’avvio, il Gateway registra nei log il modello agente predefinito risolto insieme ai valori predefiniti della modalità che influiscono sulle nuove sessioni, per esempio:

textCopy code
[code]
    agent model: openai-codex/gpt-5.5 (thinking=medium, fast=on)
[/code]

`thinking` proviene dall’agente predefinito, dai parametri del modello o dal valore predefinito globale dell’agente; quando non è impostato, il riepilogo di avvio mostra `medium`. `fast` proviene dall’agente predefinito o dai parametri `fastMode` del modello.

## Logger basato su file

  * Il file di log rotativo predefinito si trova in `/tmp/openclaw/` (un file al giorno): `openclaw-YYYY-MM-DD.log`
    * La data usa il fuso orario locale dell’host del Gateway.
  * I file di log attivi ruotano a `logging.maxFileBytes` (predefinito: 100 MB), mantenendo fino a cinque archivi numerati e continuando a scrivere un nuovo file attivo.
  * Il percorso e il livello del file di log possono essere configurati tramite `~/.openclaw/openclaw.json`: 
    * `logging.file`
    * `logging.level`


Il formato del file è un oggetto JSON per riga.

I percorsi del codice per talk, voce in tempo reale e stanze gestite usano il logger di file condiviso per record del ciclo di vita delimitati. Questi record sono destinati al debug operativo e all’esportazione dei log OTLP; il testo della trascrizione, i payload audio, gli ID di turno, gli ID di chiamata e gli ID degli elementi del provider non vengono copiati nel record di log.

La scheda Logs della Control UI segue questo file tramite il Gateway (`logs.tail`). La CLI può fare lo stesso:

bashCopy code
[code]
    openclaw logs --follow
[/code]

**Verboso e livelli di log**

  * **Log su file** sono controllati esclusivamente da `logging.level`.
  * `--verbose` influisce solo sulla **verbosità della console** (e sullo stile dei log WS); **non** aumenta il livello dei log su file.
  * Per acquisire nei log su file dettagli visibili solo in modalità verbosa, imposta `logging.level` su `debug` o `trace`.
  * La registrazione a livello trace include anche riepiloghi diagnostici dei tempi per percorsi critici selezionati, come la preparazione della factory degli strumenti Plugin. Vedi [/tools/plugin#slow-plugin-tool-setup](</it/tools/plugin#slow-plugin-tool-setup>).


## Acquisizione della console

La CLI acquisisce `console.log/info/warn/error/debug/trace` e li scrive nei log su file, continuando comunque a stampare su stdout/stderr.

Puoi regolare la verbosità della console in modo indipendente tramite:

  * `logging.consoleLevel` (predefinito `info`)
  * `logging.consoleStyle` (`pretty` | `compact` | `json`)


## Redazione

OpenClaw può mascherare i token sensibili prima che l’output di log o trascrizione esca dal processo. Questa policy di redazione dei log viene applicata a console, log su file, record di log OTLP e sink di testo della trascrizione di sessione, quindi i valori segreti corrispondenti vengono mascherati prima che righe JSONL o messaggi vengano scritti su disco.

  * `logging.redactSensitive`: `off` | `tools` (predefinito: `tools`)
  * `logging.redactPatterns`: array di stringhe regex (sostituisce i valori predefiniti) 
    * Usa stringhe regex grezze (auto `gi`), oppure `/pattern/flags` se hai bisogno di flag personalizzati.
    * Le corrispondenze vengono mascherate mantenendo i primi 6 + gli ultimi 4 caratteri (lunghezza >= 18), altrimenti `***`.
    * I valori predefiniti coprono assegnazioni comuni di chiavi, flag CLI, campi JSON, header bearer, blocchi PEM, prefissi di token popolari e nomi di campi di credenziali di pagamento come numero di carta, CVC/CVV, token di pagamento condiviso e credenziale di pagamento.


Alcuni confini di sicurezza redigono sempre, indipendentemente da `logging.redactSensitive`. Ciò include gli eventi di chiamata degli strumenti della Control UI, l’output dello strumento `sessions_history`, le esportazioni di supporto diagnostico, le osservazioni degli errori dei provider, la visualizzazione dei comandi di approvazione exec e i log del protocollo WebSocket del Gateway. Queste superfici possono comunque usare `logging.redactPatterns` come pattern aggiuntivi, ma `redactSensitive: "off"` non fa sì che emettano segreti grezzi.

## Log WebSocket del Gateway

Il Gateway stampa i log del protocollo WebSocket in due modalità:

  * **Modalità normale (senza`--verbose`)**: vengono stampati solo i risultati RPC "interessanti": 
    * errori (`ok=false`)
    * chiamate lente (soglia predefinita: `>= 50ms`)
    * errori di parsing
  * **Modalità verbosa (`--verbose`)**: stampa tutto il traffico di richiesta/risposta WS.


### Stile dei log WS

`openclaw gateway` supporta un selettore di stile per singolo Gateway:

  * `--ws-log auto` (predefinito): la modalità normale è ottimizzata; la modalità verbosa usa output compatto
  * `--ws-log compact`: output compatto (richiesta/risposta abbinate) in modalità verbosa
  * `--ws-log full`: output completo per frame in modalità verbosa
  * `--compact`: alias per `--ws-log compact`


Esempi:

bashCopy code
[code]
    # optimized (only errors/slow)openclaw gateway # show all WS traffic (paired)openclaw gateway --verbose --ws-log compact # show all WS traffic (full meta)openclaw gateway --verbose --ws-log full
[/code]

## Formattazione della console (logging dei sottosistemi)

Il formatter della console è **consapevole del TTY** e stampa righe coerenti con prefisso. I logger dei sottosistemi mantengono l’output raggruppato e facilmente scansionabile.

Comportamento:

  * **Prefissi dei sottosistemi** su ogni riga (ad es. `[gateway]`, `[canvas]`, `[tailscale]`)
  * **Colori dei sottosistemi** (stabili per sottosistema) più colorazione del livello
  * **Colore quando l’output è un TTY o l’ambiente sembra un terminale ricco** (`TERM`/`COLORTERM`/`TERM_PROGRAM`), rispetta `NO_COLOR`
  * **Prefissi dei sottosistemi abbreviati** : rimuove `gateway/` \+ `channels/` iniziali, mantiene gli ultimi 2 segmenti (ad es. `whatsapp/outbound`)
  * **Sotto-logger per sottosistema** (prefisso automatico + campo strutturato `{ subsystem }`)
  * **`logRaw()`** per output QR/UX (nessun prefisso, nessuna formattazione)
  * **Stili della console** (ad es. `pretty | compact | json`)
  * **Livello di log della console** separato dal livello di log su file (il file mantiene tutti i dettagli quando `logging.level` è impostato su `debug`/`trace`)
  * **Corpi dei messaggi WhatsApp** vengono registrati a `debug` (usa `--verbose` per vederli)


Questo mantiene stabili i log su file esistenti rendendo al contempo l’output interattivo facilmente scansionabile.

## Correlati

  * [Registrazione dei log](</it/logging>)
  * [Esportazione OpenTelemetry](</it/gateway/opentelemetry>)
  * [Esportazione diagnostica](</it/gateway/diagnostics>)


Was this useful?YesNo