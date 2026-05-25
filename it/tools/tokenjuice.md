---
title: Tokenjuice
source_url: https://docs.openclaw.ai/it/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice` è un Plugin incluso facoltativo che compatta i risultati rumorosi degli strumenti `exec` e `bash` dopo che il comando è già stato eseguito.

Modifica il `tool_result` restituito, non il comando stesso. Tokenjuice non riscrive l'input della shell, non riesegue i comandi e non cambia gli exit code.

Oggi questo si applica alle esecuzioni PI integrate e agli strumenti dinamici OpenClaw nell'harness app-server Codex. Tokenjuice si aggancia al middleware dei risultati degli strumenti di OpenClaw e riduce l'output prima che ritorni nella sessione harness attiva.

## Abilita il Plugin

Percorso rapido:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

Equivalente:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw distribuisce già il Plugin. Non esiste un passaggio separato `plugins install` o `tokenjuice install openclaw`.

Se preferisci modificare direttamente la configurazione:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## Cosa cambia tokenjuice

  * Compatta i risultati rumorosi di `exec` e `bash` prima che vengano reinseriti nella sessione.
  * Mantiene invariata l'esecuzione del comando originale.
  * Preserva le letture esatte del contenuto dei file e gli altri comandi che tokenjuice deve lasciare grezzi.
  * Resta opzionale: disabilita il Plugin se vuoi output verbatim ovunque.


## Verifica che funzioni

  1. Abilita il Plugin.
  2. Avvia una sessione che possa chiamare `exec`.
  3. Esegui un comando rumoroso come `git status`.
  4. Controlla che il risultato dello strumento restituito sia più breve e più strutturato dell'output grezzo della shell.


## Disabilita il Plugin

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

Oppure:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## Correlati

  * [Strumento Exec](</it/tools/exec>)
  * [Livelli di thinking](</it/tools/thinking>)
  * [Motore di contesto](</it/concepts/context-engine>)


Was this useful?YesNo