---
title: Flag di diagnostica
source_url: https://docs.openclaw.ai/it/diagnostics/flags
scraped_at: 2026-05-25
---

I flag di diagnostica consentono di abilitare log di debug mirati senza attivare la registrazione dettagliata ovunque. I flag sono opt-in e non hanno effetto a meno che un sottosistema non li controlli.

## Come funziona

  * I flag sono stringhe (senza distinzione tra maiuscole e minuscole).
  * Puoi abilitare i flag nella configurazione o tramite un override env.
  * I caratteri jolly sono supportati: 
    * `telegram.*` corrisponde a `telegram.http`
    * `*` abilita tutti i flag


## Abilitare tramite configurazione

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

Più flag:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

Riavvia il gateway dopo aver modificato i flag.

## Override env (una tantum)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

Disabilitare tutti i flag:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## Artefatti della timeline

Il flag `timeline` scrive eventi strutturati di avvio e temporizzazione runtime per harness QA esterni:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

Puoi abilitarlo anche nella configurazione:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

Il percorso del file della timeline proviene comunque da `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH`. Quando `timeline` è abilitato solo dalla configurazione, i primi intervalli di caricamento della configurazione non vengono emessi perché OpenClaw non ha ancora letto la configurazione; gli intervalli di avvio successivi usano il flag di configurazione.

Anche `OPENCLAW_DIAGNOSTICS=1`, `OPENCLAW_DIAGNOSTICS=all` e `OPENCLAW_DIAGNOSTICS=*` abilitano la timeline perché abilitano ogni flag di diagnostica. Preferisci `timeline` quando vuoi solo l'artefatto di temporizzazione JSONL.

I record della timeline usano l'involucro `openclaw.diagnostics.v1`. Gli eventi possono includere ID di processo, nomi di fase, nomi di intervallo, durate, ID di plugin, conteggi delle dipendenze, campioni di ritardo dell'event loop, nomi di operazioni provider, stato di uscita dei processi figlio e nomi/messaggi degli errori di avvio. Tratta i file della timeline come artefatti di diagnostica locali; esaminali prima di condividerli fuori dalla tua macchina.

## Dove vanno i log

I flag emettono log nel file di log di diagnostica standard. Per impostazione predefinita:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

Se imposti `logging.file`, usa invece quel percorso. I log sono JSONL (un oggetto JSON per riga). La redazione si applica comunque in base a `logging.redactSensitive`.

## Estrarre i log

Scegli il file di log più recente:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

Filtra per la diagnostica HTTP di Telegram:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

Filtra per la diagnostica HTTP di Brave Search:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

Oppure segui il log mentre riproduci il problema:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

Per i gateway remoti, puoi anche usare `openclaw logs --follow` (vedi [/cli/logs](</it/cli/logs>)).

## Note

  * Se `logging.level` è impostato su un valore superiore a `warn`, questi log potrebbero essere soppressi. Il valore predefinito `info` va bene.
  * `brave.http` registra URL/parametri di query delle richieste Brave Search, stato/tempi delle risposte ed eventi di hit/miss/scrittura della cache. Non registra chiavi API o corpi delle risposte, ma le query di ricerca possono essere sensibili.
  * I flag possono essere lasciati abilitati in sicurezza; influiscono solo sul volume dei log per il sottosistema specifico.
  * Usa [/logging](</it/logging>) per modificare destinazioni, livelli e redazione dei log.


## Correlati

  * [Diagnostica del gateway](</it/gateway/diagnostics>)
  * [Risoluzione dei problemi del gateway](</it/gateway/troubleshooting>)


Was this useful?YesNo