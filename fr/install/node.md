---
title: Node.js
source_url: https://docs.openclaw.ai/fr/install/node
scraped_at: 2026-05-25
---

OpenClaw nécessite **Node 22.16 ou version ultérieure**. **Node 24 est le runtime par défaut et recommandé** pour les installations, la CI et les workflows de publication. Node 22 reste pris en charge via la ligne LTS active. Le [script d’installation](</fr/install#alternative-install-methods>) détectera et installera Node automatiquement ; cette page s’adresse aux cas où vous voulez configurer Node vous-même et vous assurer que tout est correctement raccordé (versions, PATH, installations globales).

## Vérifier votre version

bashCopy code
[code]
    node -v
[/code]

Si cette commande affiche `v24.x.x` ou une version ultérieure, vous utilisez la valeur par défaut recommandée. Si elle affiche `v22.16.x` ou une version ultérieure, vous utilisez le chemin Node 22 LTS pris en charge, mais nous recommandons tout de même de passer à Node 24 lorsque cela vous convient. Si Node n’est pas installé ou si la version est trop ancienne, choisissez une méthode d’installation ci-dessous.

## Installer Node

### macOS

**Homebrew** (recommandé) :

bashCopy code
[code]
    brew install node
[/code]

Ou téléchargez l’installateur macOS depuis [nodejs.org](<https://nodejs.org/>).

### Linux

**Ubuntu / Debian :**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL :**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

Ou utilisez un gestionnaire de versions (voir ci-dessous).

### Windows

**winget** (recommandé) :

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey :**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

Ou téléchargez l’installateur Windows depuis [nodejs.org](<https://nodejs.org/>).

Utiliser un gestionnaire de versions (nvm, fnm, mise, asdf)

Les gestionnaires de versions vous permettent de passer facilement d’une version de Node à une autre. Options populaires :

  * [**fnm**](<https://github.com/Schniz/fnm>) \- rapide, multiplateforme
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- largement utilisé sur macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- polyglotte (Node, Python, Ruby, etc.)


Exemple avec fnm :

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Dépannage

### `openclaw: command not found`

Cela signifie presque toujours que le répertoire bin global de npm n’est pas dans votre PATH.

* ### Trouver votre préfixe npm global

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Vérifier s’il est dans votre PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

Recherchez `<npm-prefix>/bin` (macOS/Linux) ou `<npm-prefix>` (Windows) dans la sortie.

* ### L’ajouter au fichier de démarrage de votre shell

### macOS / Linux

Ajoutez ceci à `~/.zshrc` ou `~/.bashrc` :

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Ouvrez ensuite un nouveau terminal (ou exécutez `rehash` dans zsh / `hash -r` dans bash).

### Windows

Ajoutez la sortie de `npm prefix -g` à votre PATH système via Paramètres → Système → Variables d’environnement.

### Erreurs d’autorisation sur `npm install -g` (Linux)

Si vous voyez des erreurs `EACCES`, déplacez le préfixe global de npm vers un répertoire accessible en écriture par l’utilisateur :

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Ajoutez la ligne `export PATH=...` à votre `~/.bashrc` ou `~/.zshrc` pour rendre ce changement permanent.

## Articles connexes

  * [Vue d’ensemble de l’installation](</fr/install>) \- toutes les méthodes d’installation
  * [Mise à jour](</fr/install/updating>) \- garder OpenClaw à jour
  * [Premiers pas](</fr/start/getting-started>) \- premières étapes après l’installation


Was this useful?YesNo