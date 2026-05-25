---
title: Ganci
source_url: https://docs.openclaw.ai/it/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

Gestisci gli hook degli agenti (automazioni guidate da eventi per comandi come `/new`, `/reset` e l'avvio del gateway).

Eseguire `openclaw hooks` senza sottocomando equivale a `openclaw hooks list`.

Correlati:

  * Hook: [Hook](</it/automation/hooks>)
  * Hook dei Plugin: [Hook dei Plugin](</it/plugins/hooks>)


## Elencare tutti gli hook

bashCopy code
[code]
    openclaw hooks list
[/code]

Elenca tutti gli hook rilevati dalle directory del workspace, gestite, extra e in bundle. L'avvio del Gateway non carica i gestori di hook interni finché non viene configurato almeno un hook interno.

**Opzioni:**

  * `--eligible`: Mostra solo gli hook idonei (requisiti soddisfatti)
  * `--json`: Output in JSON
  * `-v, --verbose`: Mostra informazioni dettagliate, inclusi i requisiti mancanti


**Output di esempio:**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**Esempio (dettagliato):**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

Mostra i requisiti mancanti per gli hook non idonei.

**Esempio (JSON):**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

Restituisce JSON strutturato per l'uso programmatico.

## Ottenere informazioni su un hook

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

Mostra informazioni dettagliate su uno specifico hook.

**Argomenti:**

  * `<name>`: Nome dell'hook o chiave dell'hook (ad esempio, `session-memory`)


**Opzioni:**

  * `--json`: Output in JSON


**Esempio:**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Output:**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Verificare l'idoneità degli hook

bashCopy code
[code]
    openclaw hooks check
[/code]

Mostra il riepilogo dello stato di idoneità degli hook (quanti sono pronti rispetto a quanti non lo sono).

**Opzioni:**

  * `--json`: Output in JSON


**Output di esempio:**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Abilitare un hook

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

Abilita uno specifico hook aggiungendolo alla tua configurazione (`~/.openclaw/openclaw.json` per impostazione predefinita).

**Nota:** Gli hook del workspace sono disabilitati per impostazione predefinita finché non vengono abilitati qui o nella configurazione. Gli hook gestiti dai Plugin mostrano `plugin:<id>` in `openclaw hooks list` e non possono essere abilitati/disabilitati qui. Abilita/disabilita invece il Plugin.

**Argomenti:**

  * `<name>`: Nome dell'hook (ad esempio, `session-memory`)


**Esempio:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Output:**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**Cosa fa:**

  * Verifica se l'hook esiste ed è idoneo
  * Aggiorna `hooks.internal.entries.<name>.enabled = true` nella tua configurazione
  * Salva la configurazione su disco


Se l'hook proviene da `<workspace>/hooks/`, questo passaggio di opt-in è richiesto prima che il Gateway lo carichi.

**Dopo l'abilitazione:**

  * Riavvia il gateway in modo che gli hook vengano ricaricati (riavvio dell'app nella barra dei menu su macOS, oppure riavvio del processo gateway in sviluppo).


## Disabilitare un hook

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

Disabilita uno specifico hook aggiornando la tua configurazione.

**Argomenti:**

  * `<name>`: Nome dell'hook (ad esempio, `command-logger`)


**Esempio:**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Output:**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**Dopo la disabilitazione:**

  * Riavvia il gateway in modo che gli hook vengano ricaricati


## Note

  * `openclaw hooks list --json`, `info --json` e `check --json` scrivono JSON strutturato direttamente su stdout.
  * Gli hook gestiti dai Plugin non possono essere abilitati o disabilitati qui; abilita o disabilita invece il Plugin proprietario.


## Installare pacchetti di hook

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

Installa pacchetti di hook tramite il programma di installazione unificato dei plugins.

`openclaw hooks install` funziona ancora come alias di compatibilità, ma stampa un avviso di deprecazione e inoltra a `openclaw plugins install`.

Le specifiche npm sono **solo registry** (nome del pacchetto + **versione esatta** opzionale o **dist-tag**). Le specifiche Git/URL/file e gli intervalli semver vengono rifiutati. Le installazioni delle dipendenze vengono eseguite localmente al progetto con `--ignore-scripts` per sicurezza, anche quando la shell ha impostazioni globali di installazione npm.

Le specifiche bare e `@latest` restano sul canale stabile. Se npm risolve una di queste in una prerelease, OpenClaw si arresta e ti chiede di aderire esplicitamente con un tag prerelease come `@beta`/`@rc` o una versione prerelease esatta.

**Cosa fa:**

  * Copia il pacchetto di hook in `~/.openclaw/hooks/<id>`
  * Abilita gli hook installati in `hooks.internal.entries.*`
  * Registra l'installazione in `hooks.internal.installs`


**Opzioni:**

  * `-l, --link`: Collega una directory locale invece di copiarla (la aggiunge a `hooks.internal.load.extraDirs`)
  * `--pin`: Registra le installazioni npm come `name@version` risolto esatto in `hooks.internal.installs`


**Archivi supportati:** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Esempi:**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

I pacchetti di hook collegati sono trattati come hook gestiti da una directory configurata dall'operatore, non come hook del workspace.

## Aggiornare pacchetti di hook

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

Aggiorna i pacchetti di hook basati su npm tracciati tramite l'aggiornatore unificato dei plugins.

`openclaw hooks update` funziona ancora come alias di compatibilità, ma stampa un avviso di deprecazione e inoltra a `openclaw plugins update`.

**Opzioni:**

  * `--all`: Aggiorna tutti i pacchetti di hook tracciati
  * `--dry-run`: Mostra cosa cambierebbe senza scrivere


Quando esiste un hash di integrità memorizzato e l'hash dell'artefatto recuperato cambia, OpenClaw stampa un avviso e chiede conferma prima di procedere. Usa l'opzione globale `--yes` per bypassare i prompt in CI/esecuzioni non interattive.

## Hook in bundle

### session-memory

Salva il contesto della sessione in memoria quando usi `/new` o `/reset`.

**Abilita:**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Output:** `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md` per impostazione predefinita. Imposta `hooks.internal.entries.session-memory.llmSlug: true` per slug dei nomi file generati dal modello.

**Vedi:** [documentazione di session-memory](</it/automation/hooks#session-memory>)

### bootstrap-extra-files

Inietta file bootstrap aggiuntivi (ad esempio `AGENTS.md` / `TOOLS.md` locali al monorepo) durante `agent:bootstrap`.

**Abilita:**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**Vedi:** [documentazione di bootstrap-extra-files](</it/automation/hooks#bootstrap-extra-files>)

### command-logger

Registra tutti gli eventi di comando in un file di audit centralizzato.

**Abilita:**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Output:** `~/.openclaw/logs/commands.log`

**Visualizza log:**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**Vedi:** [documentazione di command-logger](</it/automation/hooks#command-logger>)

### boot-md

Esegue `BOOT.md` quando il gateway si avvia (dopo l'avvio dei canali).

**Eventi** : `gateway:startup`

**Abilita** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**Vedi:** [documentazione di boot-md](</it/automation/hooks#boot-md>)

## Correlati

  * [Riferimento CLI](</it/cli>)
  * [Hook di automazione](</it/automation/hooks>)


Was this useful?YesNo