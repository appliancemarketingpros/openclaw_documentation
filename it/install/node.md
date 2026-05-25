---
title: Node.js
source_url: https://docs.openclaw.ai/it/install/node
scraped_at: 2026-05-25
---

OpenClaw richiede **Node 22.16 o versioni successive**. **Node 24 è il runtime predefinito e consigliato** per installazioni, CI e flussi di rilascio. Node 22 resta supportato tramite il ramo LTS attivo. Lo [script di installazione](</it/install#alternative-install-methods>) rileverà e installerà Node automaticamente: questa pagina serve quando vuoi configurare Node autonomamente e assicurarti che tutto sia collegato correttamente (versioni, PATH, installazioni globali).

## Controlla la tua versione

bashCopy code
[code]
    node -v
[/code]

Se stampa `v24.x.x` o superiore, stai usando l’impostazione predefinita consigliata. Se stampa `v22.16.x` o superiore, stai usando il percorso Node 22 LTS supportato, ma consigliamo comunque di passare a Node 24 quando ti è comodo. Se Node non è installato o la versione è troppo vecchia, scegli un metodo di installazione qui sotto.

## Installa Node

### macOS

**Homebrew** (consigliato):

bashCopy code
[code]
    brew install node
[/code]

Oppure scarica l’installer per macOS da [nodejs.org](<https://nodejs.org/>).

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

Oppure usa un gestore di versioni (vedi sotto).

### Windows

**winget** (consigliato):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

Oppure scarica l’installer per Windows da [nodejs.org](<https://nodejs.org/>).

Uso di un gestore di versioni (nvm, fnm, mise, asdf)

I gestori di versioni ti permettono di passare facilmente da una versione di Node all’altra. Opzioni popolari:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- veloce, multipiattaforma
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- ampiamente usato su macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- poliglotta (Node, Python, Ruby, ecc.)


Esempio con fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Risoluzione dei problemi

### `openclaw: command not found`

Questo significa quasi sempre che la directory bin globale di npm non è nel tuo PATH.

* ### Trova il prefisso globale di npm

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Controlla se è nel tuo PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

Cerca `<npm-prefix>/bin` (macOS/Linux) o `<npm-prefix>` (Windows) nell’output.

* ### Aggiungilo al file di avvio della shell

### macOS / Linux

Aggiungi a `~/.zshrc` o `~/.bashrc`:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Poi apri un nuovo terminale (oppure esegui `rehash` in zsh / `hash -r` in bash).

### Windows

Aggiungi l’output di `npm prefix -g` al PATH di sistema tramite Impostazioni → Sistema → Variabili d’ambiente.

### Errori di permesso su `npm install -g` (Linux)

Se vedi errori `EACCES`, cambia il prefisso globale di npm impostandolo su una directory scrivibile dall’utente:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Aggiungi la riga `export PATH=...` al tuo `~/.bashrc` o `~/.zshrc` per renderla permanente.

## Correlati

  * [Panoramica dell’installazione](</it/install>) \- tutti i metodi di installazione
  * [Aggiornamento](</it/install/updating>) \- mantenere OpenClaw aggiornato
  * [Primi passi](</it/start/getting-started>) \- primi passi dopo l’installazione


Was this useful?YesNo