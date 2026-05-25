---
title: Migrare
source_url: https://docs.openclaw.ai/it/cli/migrate
scraped_at: 2026-05-25
---

# `openclaw migrate`

Importa lo stato da un altro sistema di agenti tramite un provider di migrazione gestito da un plugin. I provider inclusi coprono lo stato della CLI Codex, [Claude](</it/install/migrating-claude>) e [Hermes](</it/install/migrating-hermes>); i plugin di terze parti possono registrare provider aggiuntivi.

## Comandi

bashCopy code
[code]
    openclaw migrate listopenclaw migrate claude --dry-runopenclaw migrate codex --dry-runopenclaw migrate codex --skill gog-vault77-google-workspaceopenclaw migrate codex --plugin google-calendar --dry-runopenclaw migrate codex --plugin google-calendar --verify-plugin-apps --dry-runopenclaw migrate hermes --dry-runopenclaw migrate hermesopenclaw migrate apply codex --yes --skill gog-vault77-google-workspaceopenclaw migrate apply codex --yes --plugin google-calendaropenclaw migrate apply codex --yesopenclaw migrate apply claude --yesopenclaw migrate apply hermes --yesopenclaw migrate apply hermes --include-secrets --yesopenclaw onboard --flow importopenclaw onboard --import-from claude --import-source ~/.claudeopenclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ijxwcm92aWRlcg " type="string"> Nome di un provider di migrazione registrato, ad esempio `hermes`. Esegui `openclaw migrate list` per vedere i provider installati.

Crea il piano ed esce senza modificare lo stato.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tZnJvbSA8cGF0aA " type="string"> Sostituisce la directory dello stato sorgente. Hermes usa `~/.hermes` per impostazione predefinita.

Importa le credenziali supportate. Disattivato per impostazione predefinita.

Consente ad apply di sostituire le destinazioni esistenti quando il piano segnala conflitti.

Salta la richiesta di conferma. Obbligatorio in modalità non interattiva.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tcGx1Z2luIDxuYW1l " type="string"> Seleziona un elemento di installazione plugin Codex per nome plugin o ID elemento. Ripeti il flag per migrare più plugin Codex. Se omesso, le migrazioni Codex interattive mostrano un selettore nativo con caselle di spunta per i plugin Codex e le migrazioni non interattive mantengono tutti i plugin pianificati. Questo si applica solo ai plugin Codex `openai-curated` installati nella sorgente e rilevati dall'inventario dell'app-server Codex.

Solo Codex. Forza un nuovo attraversamento `app/list` dell'app-server Codex sorgente prima di pianificare l'attivazione nativa dei plugin. Disattivato per impostazione predefinita per mantenere rapida la pianificazione della migrazione.

Salta il backup prima dell'applicazione. Richiede `--force` quando esiste uno stato OpenClaw locale.

Obbligatorio insieme a `--no-backup` quando apply altrimenti rifiuterebbe di saltare il backup.

Stampa il piano o il risultato di apply come JSON. Con `--json` e senza `--yes`, apply stampa il piano e non modifica lo stato.

## Modello di sicurezza

`openclaw migrate` è basato prima sull'anteprima.

Anteprima prima dell'applicazione

Il provider restituisce un piano dettagliato prima che qualcosa cambi, inclusi conflitti, elementi saltati ed elementi sensibili. I piani JSON, l'output di apply e i report di migrazione oscurano le chiavi annidate che sembrano segreti, come chiavi API, token, header di autorizzazione, cookie e password.

`openclaw migrate apply <provider>` mostra l'anteprima del piano e chiede conferma prima di modificare lo stato, a meno che `--yes` sia impostato. In modalità non interattiva, apply richiede `--yes`.

Backup

Apply crea e verifica un backup OpenClaw prima di applicare la migrazione. Se non esiste ancora uno stato OpenClaw locale, il passaggio di backup viene saltato e la migrazione può continuare. Per saltare un backup quando lo stato esiste, passa sia `--no-backup` sia `--force`.

Conflitti

Apply rifiuta di continuare quando il piano ha conflitti. Esamina il piano, quindi riesegui con `--overwrite` se la sostituzione delle destinazioni esistenti è intenzionale. I provider possono comunque scrivere backup a livello di elemento per i file sovrascritti nella directory del report di migrazione.

Segreti

I segreti non vengono mai importati per impostazione predefinita. Usa `--include-secrets` per importare le credenziali supportate.

## Provider Claude

Il provider Claude incluso rileva lo stato di Claude Code in `~/.claude` per impostazione predefinita. Usa `--from <path>` per importare una home Claude Code specifica o una root di progetto.

### Cosa importa Claude

  * `CLAUDE.md` del progetto e `.claude/CLAUDE.md` nello spazio di lavoro dell'agente OpenClaw.
  * `~/.claude/CLAUDE.md` dell'utente aggiunto a `USER.md` dello spazio di lavoro.
  * Definizioni dei server MCP da `.mcp.json` del progetto, `~/.claude.json` di Claude Code e `claude_desktop_config.json` di Claude Desktop.
  * Directory delle skill Claude che includono `SKILL.md`.
  * File Markdown dei comandi Claude convertiti in skill OpenClaw solo con invocazione manuale.


### Stato archiviato e da revisione manuale

Hook Claude, autorizzazioni, valori predefiniti dell'ambiente, memoria locale, regole con ambito di percorso, subagenti, cache, piani e cronologia del progetto vengono conservati nel report di migrazione o segnalati come elementi da revisione manuale. OpenClaw non esegue hook, non copia allowlist ampie e non importa automaticamente lo stato delle credenziali OAuth/Desktop.

## Provider Codex

Il provider Codex incluso rileva lo stato della CLI Codex in `~/.codex` per impostazione predefinita, oppure in `CODEX_HOME` quando quella variabile d'ambiente è impostata. Usa `--from <path>` per inventariare una home Codex specifica.

Usa questo provider quando passi all'harness Codex di OpenClaw e vuoi promuovere deliberatamente asset personali utili della CLI Codex. Gli avvii locali dell'app-server Codex usano directory `CODEX_HOME` e `HOME` per agente, quindi non leggono lo stato personale della CLI Codex per impostazione predefinita.

Eseguire `openclaw migrate codex` in un terminale interattivo mostra l'anteprima del piano completo, quindi apre selettori con caselle di spunta prima della conferma finale di apply. Gli elementi di copia delle skill vengono richiesti per primi. Usa `Toggle all on` o `Toggle all off` per la selezione in blocco. Premi Spazio per attivare o disattivare le righe, oppure premi Invio per attivare la riga evidenziata e continuare. Le skill pianificate partono selezionate, le skill in conflitto partono deselezionate e `Skip for now` salta le copie delle skill per questa esecuzione continuando comunque alla selezione dei plugin. Quando i plugin Codex curati installati nella sorgente sono migrabili e `--plugin` non è stato fornito, la migrazione chiede quindi l'attivazione nativa dei plugin Codex per nome plugin. Gli elementi plugin partono selezionati a meno che la configurazione del plugin Codex OpenClaw di destinazione non abbia già quel plugin. I plugin di destinazione esistenti partono deselezionati e mostrano un suggerimento di conflitto come `conflict: plugin exists`; scegli `Toggle all off` per non migrare plugin Codex nativi in quella esecuzione, oppure `Skip for now` per fermarti prima dell'applicazione. Per esecuzioni scriptate o precise, passa `--skill <name>` una volta per skill, ad esempio:

bashCopy code
[code]
    openclaw migrate codex --dry-run --skill gog-vault77-google-workspaceopenclaw migrate apply codex --yes --skill gog-vault77-google-workspace
[/code]

Usa `--plugin <name>` per limitare in modo non interattivo la migrazione dei plugin Codex nativi a uno o più plugin curati installati nella sorgente:

bashCopy code
[code]
    openclaw migrate codex --dry-run --plugin google-calendaropenclaw migrate apply codex --yes --plugin google-calendar
[/code]

### Cosa importa Codex

  * Directory delle skill della CLI Codex sotto `$CODEX_HOME/skills`, esclusa la cache `.system` di Codex.
  * AgentSkills personali sotto `$HOME/.agents/skills`, copiati nello spazio di lavoro dell'agente OpenClaw corrente quando vuoi una proprietà per agente.
  * Plugin Codex `openai-curated` installati nella sorgente rilevati tramite `plugin/list` dell'app-server Codex. La pianificazione legge `plugin/read` per ogni plugin installato abilitato. I plugin supportati da app richiedono che la risposta dell'account dell'app-server Codex sorgente sia un account con abbonamento ChatGPT; le risposte account non ChatGPT o mancanti vengono saltate con `codex_subscription_required`. Per impostazione predefinita, la migrazione non chiama `app/list` sorgente, quindi i plugin supportati da app che superano il gate dell'account vengono pianificati senza verifica dell'accessibilità dell'app sorgente, e gli errori di trasporto della ricerca account vengono saltati con `codex_account_unavailable`. Passa `--verify-plugin-apps` quando vuoi che la migrazione forzi una nuova istantanea `app/list` sorgente e richieda che ogni app posseduta sia presente, abilitata e accessibile prima di pianificare l'attivazione nativa. In quella modalità, gli errori di trasporto della ricerca account passano alla verifica dell'inventario app sorgente. L'istantanea dell'inventario app sorgente viene mantenuta in memoria per il processo corrente; non viene scritta nell'output di migrazione o nella configurazione di destinazione. Plugin disabilitati, dettagli plugin non leggibili, account sorgente soggetti a gate di abbonamento e, quando la verifica è richiesta, app mancanti, app disabilitate, app inaccessibili o errori dell'inventario app sorgente diventano elementi manuali saltati con motivi tipizzati invece di voci della configurazione di destinazione. Apply chiama `plugin/install` dell'app-server per ogni plugin idoneo selezionato, anche se l'app-server di destinazione segnala già quel plugin come installato e abilitato. I plugin Codex migrati sono utilizzabili solo nelle sessioni che selezionano l'harness Codex nativo; non sono esposti a Pi, alle normali esecuzioni del provider OpenAI, ai binding di conversazione ACP o ad altri harness.


### Stato Codex da revisione manuale

`config.toml` di Codex, `hooks/hooks.json` nativo, marketplace non curati, bundle plugin memorizzati nella cache che non sono plugin curati installati nella sorgente e plugin installati nella sorgente che non superano il gate di abbonamento sorgente non vengono attivati automaticamente. Quando `--verify-plugin-apps` è impostato, vengono saltati anche i plugin che non superano il gate dell'inventario app sorgente. Vengono copiati o segnalati nel report di migrazione per revisione manuale.

Per i plugin curati installati nella sorgente migrati, apply scrive:

  * `plugins.entries.codex.enabled: true`
  * `plugins.entries.codex.config.codexPlugins.enabled: true`
  * `plugins.entries.codex.config.codexPlugins.allow_destructive_actions: true`
  * una voce plugin esplicita con `marketplaceName: "openai-curated"` e `pluginName` per ogni plugin selezionato


La migrazione non scrive mai `plugins["*"]` e non memorizza mai percorsi della cache marketplace locale. Gli errori di abbonamento lato sorgente vengono segnalati sugli elementi manuali con motivi tipizzati come `codex_subscription_required`, `codex_account_unavailable`, `plugin_disabled` o `plugin_read_unavailable`. Con `--verify-plugin-apps`, anche gli errori dell'inventario app sorgente possono apparire come `app_inaccessible`, `app_disabled`, `app_missing` o `app_inventory_unavailable`. I plugin saltati non vengono scritti nella configurazione di destinazione. Le installazioni lato destinazione che richiedono autenticazione vengono segnalate sull'elemento plugin interessato con `status: "skipped"`, `reason: "auth_required"` e identificatori app sanificati. Le loro voci di configurazione esplicite vengono scritte disabilitate finché non autorizzi di nuovo e le abiliti. Altri errori di installazione sono risultati `error` con ambito dell'elemento.

Se l'inventario plugin dell'app-server Codex non è disponibile durante la pianificazione, la migrazione ripiega su elementi di avviso dei bundle in cache invece di far fallire l'intera migrazione.

## Provider Hermes

Il provider Hermes incluso rileva lo stato in `~/.hermes` per impostazione predefinita. Usa `--from <path>` quando Hermes si trova altrove.

### Cosa importa Hermes

  * Configurazione del modello predefinita da `config.yaml`.
  * Provider di modelli configurati ed endpoint personalizzati compatibili con OpenAI da `providers` e `custom_providers`.
  * Definizioni del server MCP da `mcp_servers` o `mcp.servers`.
  * `SOUL.md` e `AGENTS.md` nello spazio di lavoro dell'agente OpenClaw.
  * `memories/MEMORY.md` e `memories/USER.md` aggiunti ai file di memoria dello spazio di lavoro.
  * Valori predefiniti della configurazione della memoria per la memoria su file di OpenClaw, più elementi di archivio o revisione manuale per provider di memoria esterni come Honcho.
  * Skills che includono un file `SKILL.md` in `skills/<name>/`.
  * Valori di configurazione per singola Skill da `skills.config`.
  * Chiavi API supportate da `.env`, solo con `--include-secrets`.


### Chiavi `.env` supportate

`OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`.

### Stato solo archivio

Lo stato di Hermes che OpenClaw non può interpretare in modo sicuro viene copiato nel report di migrazione per la revisione manuale, ma non viene caricato nella configurazione o nelle credenziali live di OpenClaw. Questo preserva lo stato opaco o non sicuro senza fingere che OpenClaw possa eseguirlo o considerarlo automaticamente attendibile:

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


### Dopo l'applicazione

bashCopy code
[code]
    openclaw doctor
[/code]

## Contratto del Plugin

Le origini di migrazione sono Plugin. Un Plugin dichiara i propri ID provider in `openclaw.plugin.json`:

jsonCopy code
[code]
    {  "contracts": {    "migrationProviders": ["hermes"]  }}
[/code]

A runtime il Plugin chiama `api.registerMigrationProvider(...)`. Il provider implementa `detect`, `plan` e `apply`. Il core gestisce l'orchestrazione della CLI, la policy di backup, i prompt, l'output JSON e la verifica preliminare dei conflitti. Il core passa il piano revisionato a `apply(ctx, plan)` e i provider possono ricostruire il piano solo quando quell'argomento è assente per compatibilità.

I Plugin provider possono usare `openclaw/plugin-sdk/migration` per la costruzione degli elementi e i conteggi di riepilogo, più `openclaw/plugin-sdk/migration-runtime` per copie di file consapevoli dei conflitti, copie di report solo archivio, wrapper di runtime della configurazione memorizzati nella cache e report di migrazione.

## Integrazione dell'onboarding

L'onboarding può offrire la migrazione quando un provider rileva un'origine nota. Sia `openclaw onboard --flow import` sia `openclaw setup --wizard --import-from hermes` usano lo stesso provider di migrazione del Plugin e mostrano comunque un'anteprima prima dell'applicazione.

## Correlati

  * [Migrazione da Hermes](</it/install/migrating-hermes>): guida passo passo rivolta agli utenti.
  * [Migrazione da Claude](</it/install/migrating-claude>): guida passo passo rivolta agli utenti.
  * [Migrazione](</it/install/migrating>): sposta OpenClaw su una nuova macchina.
  * [Doctor](</it/gateway/doctor>): controllo di integrità dopo l'applicazione di una migrazione.
  * [Plugin](</it/tools/plugin>): installazione e registrazione dei Plugin.


Was this useful?YesNo