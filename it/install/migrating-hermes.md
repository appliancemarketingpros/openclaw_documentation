---
title: Migrazione da Hermes
source_url: https://docs.openclaw.ai/it/install/migrating-hermes
scraped_at: 2026-05-25
---

OpenClaw importa lo stato di Hermes tramite un provider di migrazione incluso. Il provider mostra un'anteprima di tutto prima di modificare lo stato, redige i segreti nei piani e nei report e crea un backup verificato prima dell'applicazione.

## Due modi per importare

### Procedura guidata di onboarding

Il percorso più rapido. La procedura guidata rileva Hermes in `~/.hermes` e mostra un'anteprima prima dell'applicazione.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Oppure indica una sorgente specifica:

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

Usa `openclaw migrate` per esecuzioni con script o ripetibili. Consulta [`openclaw migrate`](</it/cli/migrate>) per il riferimento completo.

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # solo anteprimaopenclaw migrate apply hermes --yes  # applica saltando la conferma
[/code]

Aggiungi `--from <path>` quando Hermes si trova fuori da `~/.hermes`.

## Cosa viene importato

Configurazione del modello

  * Selezione del modello predefinito da `config.yaml` di Hermes.
  * Provider di modelli configurati ed endpoint personalizzati compatibili con OpenAI da `providers` e `custom_providers`.

Server MCP

Definizioni dei server MCP da `mcp_servers` o `mcp.servers`.

File del workspace

  * `SOUL.md` e `AGENTS.md` vengono copiati nel workspace dell'agente OpenClaw.
  * `memories/MEMORY.md` e `memories/USER.md` vengono **aggiunti** ai file di memoria OpenClaw corrispondenti invece di sovrascriverli.

Configurazione della memoria

Valori predefiniti della configurazione della memoria per la memoria su file di OpenClaw. I provider di memoria esterni, come Honcho, vengono registrati come elementi di archivio o di revisione manuale, così puoi spostarli deliberatamente.

Skills

Le Skills con un file `SKILL.md` sotto `skills/<name>/` vengono copiate, insieme ai valori di configurazione per singola Skill da `skills.config`.

Chiavi API (opzionale)

Imposta `--include-secrets` per importare le chiavi `.env` supportate: `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`. Senza il flag, i segreti non vengono mai copiati.

## Cosa resta solo in archivio

Il provider copia questi elementi nella directory del report di migrazione per la revisione manuale, ma **non** li carica nella configurazione o nelle credenziali OpenClaw attive:

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


OpenClaw rifiuta di eseguire o considerare attendibile automaticamente questo stato perché i formati e le assunzioni di fiducia possono divergere tra sistemi. Sposta manualmente ciò che ti serve dopo aver esaminato l'archivio.

## Flusso consigliato

* ### Visualizza l'anteprima del piano

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

Il piano elenca tutto ciò che cambierà, inclusi conflitti, elementi saltati ed eventuali elementi sensibili. L'output del piano redige le chiavi annidate che sembrano segreti.

* ### Applica con backup

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

OpenClaw crea e verifica un backup prima dell'applicazione. Se devi importare chiavi API, aggiungi `--include-secrets`.

* ### Esegui doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</it/gateway/doctor>) riapplica eventuali migrazioni di configurazione in sospeso e controlla i problemi introdotti durante l'importazione.

* ### Riavvia e verifica

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Conferma che il Gateway sia integro e che il modello, la memoria e le Skills importati siano caricati.

## Gestione dei conflitti

L'applicazione rifiuta di continuare quando il piano segnala conflitti (un file o un valore di configurazione esiste già nella destinazione).

Per un'installazione OpenClaw nuova, i conflitti sono insoliti. In genere compaiono quando riesegui l'importazione su una configurazione che contiene già modifiche dell'utente.

Se emerge un conflitto durante l'applicazione (ad esempio una race imprevista su un file di configurazione), Hermes contrassegna gli elementi di configurazione dipendenti rimanenti come `skipped` con motivo `blocked by earlier apply conflict` invece di scriverli parzialmente. Il report di migrazione registra ogni elemento bloccato, così puoi risolvere il conflitto originale e rieseguire l'importazione.

## Segreti

I segreti non vengono mai importati per impostazione predefinita.

  * Esegui prima `openclaw migrate apply hermes --yes` per importare lo stato non segreto.
  * Se vuoi anche copiare le chiavi `.env` supportate, riesegui con `--include-secrets`.
  * Per le credenziali gestite da SecretRef, configura la sorgente SecretRef dopo il completamento dell'importazione.


## Output JSON per l'automazione

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

Con `--json` e senza `--yes`, apply stampa il piano e non modifica lo stato. Questa è la modalità più sicura per CI e script condivisi.

## Risoluzione dei problemi

L'applicazione rifiuta con conflitti

Ispeziona l'output del piano. Ogni conflitto identifica il percorso sorgente e la destinazione esistente. Decidi per ogni elemento se saltarlo, modificare la destinazione o rieseguire con `--overwrite`.

Hermes si trova fuori da ~/.hermes

Passa `--from /actual/path` (CLI) o `--import-source /actual/path` (onboarding).

L'onboarding rifiuta di importare su una configurazione esistente

Le importazioni tramite onboarding richiedono una configurazione nuova. Reimposta lo stato e ripeti l'onboarding, oppure usa direttamente `openclaw migrate apply hermes`, che supporta `--overwrite` e il controllo esplicito del backup.

Le chiavi API non sono state importate

`--include-secrets` è obbligatorio e vengono riconosciute solo le chiavi elencate sopra. Le altre variabili in `.env` vengono ignorate.

## Correlati

  * [`openclaw migrate`](</it/cli/migrate>): riferimento CLI completo, contratto del plugin e forme JSON.
  * [Onboarding](</it/cli/onboard>): flusso della procedura guidata e flag non interattivi.
  * [Migrazione](</it/install/migrating>): spostare un'installazione OpenClaw tra macchine.
  * [Doctor](</it/gateway/doctor>): controllo dello stato dopo la migrazione.
  * [Workspace dell'agente](</it/concepts/agent-workspace>): dove si trovano `SOUL.md`, `AGENTS.md` e i file di memoria.


Was this useful?YesNo