---
title: Dettagli interni del programma di installazione
source_url: https://docs.openclaw.ai/it/install/installer
scraped_at: 2026-05-25
---

OpenClaw distribuisce tre script di installazione, serviti da `openclaw.ai`.

Script | Piattaforma | Cosa fa  
---|---|---  
`install.sh` | macOS / Linux / WSL | Installa Node se necessario, installa OpenClaw tramite npm (predefinito) o git, e può eseguire l’onboarding.  
`install-cli.sh` | macOS / Linux / WSL | Installa Node + OpenClaw in un prefisso locale (`~/.openclaw`) con modalità npm o checkout git. Root non richiesto.  
`install.ps1` | Windows (PowerShell) | Installa Node se necessario, installa OpenClaw tramite npm (predefinito) o git, e può eseguire l’onboarding.  
  
## Comandi rapidi

### install.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --help
[/code]

### install-cli.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --help
[/code]

### install.ps1

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag beta -NoOnboard -DryRun
[/code]

* * *

## [install.sh](<http://install.sh>)

### Flusso ([install.sh](<http://install.sh>))

* ### Detect OS

Supporta macOS e Linux (incluso WSL). Se viene rilevato macOS, installa Homebrew se manca.

* ### Ensure Node.js 24 by default

Controlla la versione di Node e installa Node 24 se necessario (Homebrew su macOS, script di configurazione NodeSource su Linux apt/dnf/yum). OpenClaw supporta ancora Node 22 LTS, attualmente `22.16+`, per compatibilità.

* ### Ensure Git

Installa Git se manca.

* ### Install OpenClaw

  * metodo `npm` (predefinito): installazione npm globale
  * metodo `git`: clona/aggiorna il repo, installa le dipendenze con pnpm, compila, quindi installa il wrapper in `~/.local/bin/openclaw`


* ### Post-install tasks

  * Aggiorna al meglio un servizio Gateway caricato (`openclaw gateway install --force`, quindi riavvio)
  * Esegue `openclaw doctor --non-interactive` sugli aggiornamenti e sulle installazioni git (al meglio)
  * Tenta l’onboarding quando appropriato (TTY disponibile, onboarding non disabilitato e controlli bootstrap/config superati)
  * Imposta per impostazione predefinita `SHARP_IGNORE_GLOBAL_LIBVIPS=1`


### Rilevamento del checkout sorgente

Se eseguito dentro un checkout di OpenClaw (`package.json` \+ `pnpm-workspace.yaml`), lo script offre:

  * usa il checkout (`git`), oppure
  * usa l’installazione globale (`npm`)


Se non è disponibile alcun TTY e non è impostato alcun metodo di installazione, usa `npm` come predefinito e mostra un avviso.

Lo script termina con codice `2` per selezione del metodo non valida o valori `--install-method` non validi.

### Esempi ([install.sh](<http://install.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Skip onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### GitHub main via npm

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### Dry run

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Flags reference Flag | Descrizione  
---|---  
`--install-method npm|git` | Sceglie il metodo di installazione (predefinito: `npm`). Alias: `--method`  
`--npm` | Scorciatoia per il metodo npm  
`--git` | Scorciatoia per il metodo git. Alias: `--github`  
`--version <version|dist-tag|spec>` | Versione npm, dist-tag o specifica pacchetto (predefinito: `latest`)  
`--beta` | Usa il dist-tag beta se disponibile, altrimenti ripiega su `latest`  
`--git-dir <path>` | Directory di checkout (predefinita: `~/openclaw`). Alias: `--dir`  
`--no-git-update` | Salta `git pull` per un checkout esistente  
`--no-prompt` | Disabilita i prompt  
`--no-onboard` | Salta l’onboarding  
`--onboard` | Abilita l’onboarding  
`--dry-run` | Stampa le azioni senza applicare modifiche  
`--verbose` | Abilita l’output di debug (`set -x`, log npm a livello notice)  
`--help` | Mostra l’utilizzo (`-h`)  
Environment variables reference Variabile | Descrizione  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Metodo di installazione  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | Versione npm, dist-tag o specifica pacchetto  
`OPENCLAW_BETA=0|1` | Usa beta se disponibile  
`OPENCLAW_GIT_DIR=<path>` | Directory di checkout  
`OPENCLAW_GIT_UPDATE=0|1` | Attiva/disattiva gli aggiornamenti git  
`OPENCLAW_NO_PROMPT=1` | Disabilita i prompt  
`OPENCLAW_NO_ONBOARD=1` | Salta l’onboarding  
`OPENCLAW_DRY_RUN=1` | Modalità dry run  
`OPENCLAW_VERBOSE=1` | Modalità debug  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Livello di log npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Controlla il comportamento sharp/libvips (predefinito: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### Flusso ([install-cli.sh](<http://install-cli.sh>))

* ### Install local Node runtime

Scarica un tarball Node LTS supportato e fissato (la versione è incorporata nello script e aggiornata indipendentemente) in `<prefix>/tools/node-v<version>` e verifica SHA-256.

* ### Ensure Git

Se Git manca, tenta l’installazione tramite apt/dnf/yum su Linux o Homebrew su macOS.

* ### Install OpenClaw under prefix

  * metodo `npm` (predefinito): installa sotto il prefisso con npm, quindi scrive il wrapper in `<prefix>/bin/openclaw`
  * metodo `git`: clona/aggiorna un checkout (predefinito `~/openclaw`) e scrive comunque il wrapper in `<prefix>/bin/openclaw`


* ### Refresh loaded gateway service

Se un servizio Gateway è già caricato da quello stesso prefisso, lo script esegue `openclaw gateway install --force`, quindi `openclaw gateway restart`, e verifica al meglio lo stato di salute del Gateway.

### Esempi ([install-cli.sh](<http://install-cli.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Custom prefix + version

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### Automation JSON output

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Run onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Flags reference Flag | Descrizione  
---|---  
`--prefix <path>` | Prefisso di installazione (predefinito: `~/.openclaw`)  
`--install-method npm|git` | Sceglie il metodo di installazione (predefinito: `npm`). Alias: `--method`  
`--npm` | Scorciatoia per il metodo npm  
`--git`, `--github` | Scorciatoia per il metodo git  
`--git-dir <path>` | Directory di checkout Git (predefinita: `~/openclaw`). Alias: `--dir`  
`--version <ver>` | Versione OpenClaw o dist-tag (predefinito: `latest`)  
`--node-version <ver>` | Versione Node (predefinita: `22.22.0`)  
`--json` | Emette eventi NDJSON  
`--onboard` | Esegue `openclaw onboard` dopo l’installazione  
`--no-onboard` | Salta l’onboarding (predefinito)  
`--set-npm-prefix` | Su Linux, forza il prefisso npm a `~/.npm-global` se il prefisso corrente non è scrivibile  
`--help` | Mostra l’utilizzo (`-h`)  
Environment variables reference Variabile | Descrizione  
---|---  
`OPENCLAW_PREFIX=<path>` | Prefisso di installazione  
`OPENCLAW_INSTALL_METHOD=git|npm` | Metodo di installazione  
`OPENCLAW_VERSION=<ver>` | Versione di OpenClaw o dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Versione di Node  
`OPENCLAW_GIT_DIR=<path>` | Directory di checkout Git per installazioni git  
`OPENCLAW_GIT_UPDATE=0|1` | Attiva/disattiva gli aggiornamenti git per checkout esistenti  
`OPENCLAW_NO_ONBOARD=1` | Salta l'onboarding  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Livello di log npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Controlla il comportamento di sharp/libvips (predefinito: `1`)  
  
* * *

## install.ps1

### Flusso (install.ps1)

* ### Verifica l'ambiente PowerShell + Windows

Richiede PowerShell 5+.

* ### Assicura Node.js 24 per impostazione predefinita

Se manca, tenta l'installazione tramite winget, poi Chocolatey, poi Scoop. Node 22 LTS, attualmente `22.16+`, resta supportato per compatibilità.

* ### Installa OpenClaw

  * Metodo `npm` (predefinito): installazione npm globale usando il `-Tag` selezionato, avviata da una directory temporanea dell'installer scrivibile, così le shell aperte in cartelle protette come `C:\` funzionano comunque
  * Metodo `git`: clona/aggiorna il repo, installa/compila con pnpm e installa il wrapper in `%USERPROFILE%\.local\bin\openclaw.cmd`


* ### Attività post-installazione

  * Aggiunge la directory bin necessaria al PATH utente quando possibile
  * Aggiorna al meglio un servizio Gateway caricato (`openclaw gateway install --force`, poi riavvio)
  * Esegue `openclaw doctor --non-interactive` sugli aggiornamenti e sulle installazioni git (al meglio)


* ### Gestisce gli errori

Le installazioni con `iwr ... | iex` e scriptblock segnalano un errore terminante senza chiudere la sessione PowerShell corrente. Le installazioni dirette con `powershell -File` / `pwsh -File` continuano a terminare con codice diverso da zero per l'automazione.

### Esempi (install.ps1)

### Predefinito

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Installazione git

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### Main di GitHub tramite npm

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Directory git personalizzata

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Esecuzione di prova

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Traccia di debug

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Riferimento dei flag Flag | Descrizione  
---|---  
`-InstallMethod npm|git` | Metodo di installazione (predefinito: `npm`)  
`-Tag <tag|version|spec>` | dist-tag npm, versione o specifica del pacchetto (predefinito: `latest`)  
`-GitDir <path>` | Directory di checkout (predefinita: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Salta l'onboarding  
`-NoGitUpdate` | Salta `git pull`  
`-DryRun` | Stampa solo le azioni  
Riferimento delle variabili d'ambiente Variabile | Descrizione  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Metodo di installazione  
`OPENCLAW_GIT_DIR=<path>` | Directory di checkout  
`OPENCLAW_NO_ONBOARD=1` | Salta l'onboarding  
`OPENCLAW_GIT_UPDATE=0` | Disabilita git pull  
`OPENCLAW_DRY_RUN=1` | Modalità di prova  
  
* * *

## CI e automazione

Usa flag/variabili d'ambiente non interattivi per esecuzioni prevedibili.

### install.sh (npm non interattivo)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (git non interattivo)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (salta l'onboarding)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Risoluzione dei problemi

Perché è richiesto Git?

Git è richiesto per il metodo di installazione `git`. Per le installazioni `npm`, Git viene comunque controllato/installato per evitare errori `spawn git ENOENT` quando le dipendenze usano URL git.

Perché npm incontra EACCES su Linux?

Alcune configurazioni Linux puntano il prefisso globale di npm a percorsi di proprietà di root. `install.sh` può spostare il prefisso su `~/.npm-global` e aggiungere esportazioni PATH ai file rc della shell (quando tali file esistono).

Problemi con sharp/libvips

Gli script impostano per impostazione predefinita `SHARP_IGNORE_GLOBAL_LIBVIPS=1` per evitare che sharp venga compilato contro libvips di sistema. Per sovrascrivere:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Installa Git for Windows, riapri PowerShell, riesegui l'installer.

Windows: "openclaw is not recognized"

Esegui `npm config get prefix` e aggiungi quella directory al PATH utente (su Windows non è necessario il suffisso `\bin`), poi riapri PowerShell.

Windows: come ottenere output dettagliato dell'installer

`install.ps1` attualmente non espone un'opzione `-Verbose`. Usa il tracing di PowerShell per la diagnostica a livello di script:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

openclaw non trovato dopo l'installazione

Di solito è un problema di PATH. Vedi [risoluzione dei problemi di Node.js](</it/install/node#troubleshooting>).

## Correlati

  * [Panoramica dell'installazione](</it/install>)
  * [Aggiornamento](</it/install/updating>)
  * [Disinstallazione](</it/install/uninstall>)


Was this useful?YesNo