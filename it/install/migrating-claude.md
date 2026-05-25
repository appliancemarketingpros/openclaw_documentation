---
title: Migrazione da Claude
source_url: https://docs.openclaw.ai/it/install/migrating-claude
scraped_at: 2026-05-25
---

OpenClaw importa lo stato locale di Claude tramite il provider di migrazione Claude incluso. Il provider mostra un'anteprima di ogni elemento prima di modificare lo stato, oscura i segreti nei piani e nei report e crea un backup verificato prima dell'applicazione.

## Due modi per importare

### Procedura guidata di onboarding

La procedura guidata propone Claude quando rileva uno stato Claude locale.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Oppure punta a una sorgente specifica:

bashCopy code
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
[/code]

### CLI

Usa `openclaw migrate` per esecuzioni tramite script o ripetibili. Vedi [`openclaw migrate`](</it/cli/migrate>) per il riferimento completo.

bashCopy code
[code]
    openclaw migrate claude --dry-runopenclaw migrate apply claude --yes
[/code]

Aggiungi `--from <path>` per importare una home Claude Code o una radice di progetto specifica.

## Cosa viene importato

Istruzioni e memoria

  * Il contenuto di progetto `CLAUDE.md` e `.claude/CLAUDE.md` viene copiato o aggiunto al file `AGENTS.md` del workspace dell'agente OpenClaw.
  * Il contenuto utente `~/.claude/CLAUDE.md` viene aggiunto a `USER.md` del workspace.

Server MCP

Le definizioni dei server MCP vengono importate da `.mcp.json` del progetto, da Claude Code `~/.claude.json` e da Claude Desktop `claude_desktop_config.json` quando presenti.

Skills e comandi

  * Le Skills di Claude con un file `SKILL.md` vengono copiate nella directory Skills del workspace OpenClaw.
  * I file Markdown dei comandi Claude in `.claude/commands/` o `~/.claude/commands/` vengono convertiti in Skills OpenClaw con `disable-model-invocation: true`.


## Cosa resta solo in archivio

Il provider copia questi elementi nel report di migrazione per la revisione manuale, ma **non** li carica nella configurazione OpenClaw attiva:

  * Hook Claude
  * Autorizzazioni Claude e allowlist ampie degli strumenti
  * Valori predefiniti dell'ambiente Claude
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * Subagenti Claude in `.claude/agents/` o `~/.claude/agents/`
  * Cache, piani e directory della cronologia dei progetti di Claude Code
  * Estensioni Claude Desktop e credenziali archiviate dal sistema operativo


OpenClaw rifiuta di eseguire hook, considerare attendibili le allowlist delle autorizzazioni o decodificare automaticamente lo stato opaco delle credenziali OAuth e Desktop. Sposta manualmente ciò che ti serve dopo aver esaminato l'archivio.

## Selezione della sorgente

Senza `--from`, OpenClaw ispeziona la home predefinita di Claude Code in `~/.claude`, il file di stato campionato di Claude Code `~/.claude.json` e la configurazione MCP di Claude Desktop su macOS.

Quando `--from` punta alla radice di un progetto, OpenClaw importa solo i file Claude di quel progetto, come `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/` e `.mcp.json`. Non legge la tua home Claude globale durante un'importazione dalla radice del progetto.

## Flusso consigliato

* ### Visualizza l'anteprima del piano

bashCopy code
[code]
    openclaw migrate claude --dry-run
[/code]

Il piano elenca tutto ciò che cambierà, inclusi conflitti, elementi saltati e valori sensibili oscurati dai campi MCP annidati `env` o `headers`.

* ### Applica con backup

bashCopy code
[code]
    openclaw migrate apply claude --yes
[/code]

OpenClaw crea e verifica un backup prima di applicare le modifiche.

* ### Esegui doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</it/gateway/doctor>) verifica eventuali problemi di configurazione o stato dopo l'importazione.

* ### Riavvia e verifica

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Conferma che il Gateway sia integro e che le istruzioni, i server MCP e le Skills importati siano caricati.

## Gestione dei conflitti

L'applicazione rifiuta di continuare quando il piano segnala conflitti (un file o valore di configurazione esiste già nella destinazione).

Per una nuova installazione OpenClaw, i conflitti sono insoliti. In genere compaiono quando riesegui l'importazione su una configurazione che contiene già modifiche utente.

## Output JSON per automazione

bashCopy code
[code]
    openclaw migrate claude --dry-run --jsonopenclaw migrate apply claude --json --yes
[/code]

Con `--json` e senza `--yes`, apply stampa il piano e non modifica lo stato. Questa è la modalità più sicura per CI e script condivisi.

## Risoluzione dei problemi

Lo stato Claude si trova fuori da ~/.claude

Passa `--from /actual/path` (CLI) o `--import-source /actual/path` (onboarding).

L'onboarding rifiuta l'importazione su una configurazione esistente

Le importazioni durante l'onboarding richiedono una configurazione nuova. Reimposta lo stato e ripeti l'onboarding, oppure usa direttamente `openclaw migrate apply claude`, che supporta `--overwrite` e il controllo esplicito dei backup.

I server MCP da Claude Desktop non sono stati importati

Claude Desktop legge `claude_desktop_config.json` da un percorso specifico della piattaforma. Punta `--from` alla directory di quel file se OpenClaw non lo ha rilevato automaticamente.

I comandi Claude sono diventati Skills con invocazione del modello disabilitata

È intenzionale. I comandi Claude vengono attivati dall'utente, quindi OpenClaw li importa come Skills con `disable-model-invocation: true`. Modifica il frontmatter di ogni skill se vuoi che l'agente le invochi automaticamente.

## Correlati

  * [`openclaw migrate`](</it/cli/migrate>): riferimento CLI completo, contratto del Plugin e forme JSON.
  * [Guida alla migrazione](</it/install/migrating>): tutti i percorsi di migrazione.
  * [Migrazione da Hermes](</it/install/migrating-hermes>): l'altro percorso di importazione tra sistemi.
  * [Onboarding](</it/cli/onboard>): flusso della procedura guidata e flag non interattivi.
  * [Doctor](</it/gateway/doctor>): controllo di integrità post-migrazione.
  * [Workspace dell'agente](</it/concepts/agent-workspace>): dove si trovano `AGENTS.md`, `USER.md` e le Skills.


Was this useful?YesNo