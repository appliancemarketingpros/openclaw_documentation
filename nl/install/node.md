---
title: Node.js
source_url: https://docs.openclaw.ai/nl/install/node
scraped_at: 2026-05-25
---

OpenClaw vereist **Node 22.16 of nieuwer**. **Node 24 is de standaard en aanbevolen runtime** voor installaties, CI en releaseworkflows. Node 22 blijft ondersteund via de actieve LTS-lijn. Het [installatiescript](</nl/install#alternative-install-methods>) detecteert en installeert Node automatisch - deze pagina is bedoeld voor wanneer je Node zelf wilt instellen en zeker wilt weten dat alles correct is gekoppeld (versies, PATH, globale installaties).

## Controleer je versie

bashCopy code
[code]
    node -v
[/code]

Als dit `v24.x.x` of hoger afdrukt, gebruik je de aanbevolen standaardversie. Als dit `v22.16.x` of hoger afdrukt, gebruik je het ondersteunde Node 22 LTS-pad, maar we raden nog steeds aan om naar Node 24 te upgraden wanneer dat uitkomt. Als Node niet is geïnstalleerd of de versie te oud is, kies dan hieronder een installatiemethode.

## Node installeren

### macOS

**Homebrew** (aanbevolen):

bashCopy code
[code]
    brew install node
[/code]

Of download het macOS-installatieprogramma van [nodejs.org](<https://nodejs.org/>).

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

Of gebruik een versiemanager (zie hieronder).

### Windows

**winget** (aanbevolen):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

Of download het Windows-installatieprogramma van [nodejs.org](<https://nodejs.org/>).

Using a version manager (nvm, fnm, mise, asdf)

Versiemanagers laten je eenvoudig wisselen tussen Node-versies. Populaire opties:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- snel, platformonafhankelijk
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- veelgebruikt op macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- polyglot (Node, Python, Ruby, enz.)


Voorbeeld met fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Problemen oplossen

### `openclaw: command not found`

Dit betekent bijna altijd dat de globale bin-map van npm niet op je PATH staat.

* ### Find your global npm prefix

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Check if it's on your PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

Zoek naar `<npm-prefix>/bin` (macOS/Linux) of `<npm-prefix>` (Windows) in de uitvoer.

* ### Add it to your shell startup file

### macOS / Linux

Voeg toe aan `~/.zshrc` of `~/.bashrc`:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Open daarna een nieuwe terminal (of voer `rehash` uit in zsh / `hash -r` in bash).

### Windows

Voeg de uitvoer van `npm prefix -g` toe aan je systeem-PATH via Instellingen → Systeem → Omgevingsvariabelen.

### Machtigingsfouten bij `npm install -g` (Linux)

Als je `EACCES`-fouten ziet, verplaats dan de globale prefix van npm naar een map waarin de gebruiker kan schrijven:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Voeg de regel `export PATH=...` toe aan je `~/.bashrc` of `~/.zshrc` om dit permanent te maken.

## Gerelateerd

  * [Installatie-overzicht](</nl/install>) \- alle installatiemethoden
  * [Bijwerken](</nl/install/updating>) \- OpenClaw up-to-date houden
  * [Aan de slag](</nl/start/getting-started>) \- eerste stappen na installatie


Was this useful?YesNo