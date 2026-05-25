---
title: Fonctionnement interne de l’installateur
source_url: https://docs.openclaw.ai/fr/install/installer
scraped_at: 2026-05-25
---

OpenClaw fournit trois scripts d’installation, servis depuis `openclaw.ai`.

Script | Plateforme | Ce qu’il fait  
---|---|---  
`install.sh` | macOS / Linux / WSL | Installe Node si nécessaire, installe OpenClaw via npm (par défaut) ou git, et peut lancer l’onboarding.  
`install-cli.sh` | macOS / Linux / WSL | Installe Node + OpenClaw dans un préfixe local (`~/.openclaw`) avec npm ou les modes de checkout git. Aucun accès root requis.  
`install.ps1` | Windows (PowerShell) | Installe Node si nécessaire, installe OpenClaw via npm (par défaut) ou git, et peut lancer l’onboarding.  
  
## Commandes rapides

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

### Déroulement ([install.sh](<http://install.sh>))

* ### Detect OS

Prend en charge macOS et Linux (y compris WSL). Si macOS est détecté, installe Homebrew s’il est manquant.

* ### Ensure Node.js 24 by default

Vérifie la version de Node et installe Node 24 si nécessaire (Homebrew sur macOS, scripts de configuration NodeSource sur Linux apt/dnf/yum). OpenClaw prend toujours en charge Node 22 LTS, actuellement `22.16+`, pour la compatibilité.

* ### Ensure Git

Installe Git s’il est manquant.

* ### Install OpenClaw

  * Méthode `npm` (par défaut) : installation npm globale
  * Méthode `git` : clone/met à jour le dépôt, installe les dépendances avec pnpm, compile, puis installe le wrapper dans `~/.local/bin/openclaw`


* ### Post-install tasks

  * Actualise au mieux un service Gateway chargé (`openclaw gateway install --force`, puis redémarrage)
  * Exécute `openclaw doctor --non-interactive` lors des mises à niveau et des installations git (au mieux)
  * Tente l’onboarding lorsque c’est approprié (TTY disponible, onboarding non désactivé, et vérifications bootstrap/config réussies)
  * Définit par défaut `SHARP_IGNORE_GLOBAL_LIBVIPS=1`


### Détection d’un checkout source

S’il est exécuté dans un checkout OpenClaw (`package.json` \+ `pnpm-workspace.yaml`), le script propose :

  * utiliser le checkout (`git`), ou
  * utiliser l’installation globale (`npm`)


Si aucun TTY n’est disponible et qu’aucune méthode d’installation n’est définie, il utilise `npm` par défaut et affiche un avertissement.

Le script se termine avec le code `2` en cas de sélection de méthode invalide ou de valeurs `--install-method` invalides.

### Exemples ([install.sh](<http://install.sh>))

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

Flags reference Option | Description  
---|---  
`--install-method npm|git` | Choisir la méthode d’installation (par défaut : `npm`). Alias : `--method`  
`--npm` | Raccourci pour la méthode npm  
`--git` | Raccourci pour la méthode git. Alias : `--github`  
`--version <version|dist-tag|spec>` | Version npm, dist-tag ou spec de paquet (par défaut : `latest`)  
`--beta` | Utiliser le dist-tag bêta s’il est disponible, sinon revenir à `latest`  
`--git-dir <path>` | Répertoire de checkout (par défaut : `~/openclaw`). Alias : `--dir`  
`--no-git-update` | Ignorer `git pull` pour un checkout existant  
`--no-prompt` | Désactiver les invites  
`--no-onboard` | Ignorer l’onboarding  
`--onboard` | Activer l’onboarding  
`--dry-run` | Afficher les actions sans appliquer les changements  
`--verbose` | Activer la sortie de débogage (`set -x`, logs npm de niveau notice)  
`--help` | Afficher l’utilisation (`-h`)  
Environment variables reference Variable | Description  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Méthode d’installation  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | Version npm, dist-tag ou spec de paquet  
`OPENCLAW_BETA=0|1` | Utiliser la bêta si disponible  
`OPENCLAW_GIT_DIR=<path>` | Répertoire de checkout  
`OPENCLAW_GIT_UPDATE=0|1` | Activer/désactiver les mises à jour git  
`OPENCLAW_NO_PROMPT=1` | Désactiver les invites  
`OPENCLAW_NO_ONBOARD=1` | Ignorer l’onboarding  
`OPENCLAW_DRY_RUN=1` | Mode dry run  
`OPENCLAW_VERBOSE=1` | Mode débogage  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Niveau de log npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Contrôler le comportement sharp/libvips (par défaut : `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### Déroulement ([install-cli.sh](<http://install-cli.sh>))

* ### Install local Node runtime

Télécharge un tarball Node LTS pris en charge et épinglé (la version est intégrée dans le script et mise à jour indépendamment) vers `<prefix>/tools/node-v<version>` et vérifie le SHA-256.

* ### Ensure Git

Si Git est manquant, tente l’installation via apt/dnf/yum sur Linux ou Homebrew sur macOS.

* ### Install OpenClaw under prefix

  * Méthode `npm` (par défaut) : installe sous le préfixe avec npm, puis écrit le wrapper dans `<prefix>/bin/openclaw`
  * Méthode `git` : clone/met à jour un checkout (par défaut `~/openclaw`) et écrit tout de même le wrapper dans `<prefix>/bin/openclaw`


* ### Refresh loaded gateway service

Si un service Gateway est déjà chargé depuis ce même préfixe, le script exécute `openclaw gateway install --force`, puis `openclaw gateway restart`, et sonde au mieux l’état du Gateway.

### Exemples ([install-cli.sh](<http://install-cli.sh>))

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

Flags reference Option | Description  
---|---  
`--prefix <path>` | Préfixe d’installation (par défaut : `~/.openclaw`)  
`--install-method npm|git` | Choisir la méthode d’installation (par défaut : `npm`). Alias : `--method`  
`--npm` | Raccourci pour la méthode npm  
`--git`, `--github` | Raccourci pour la méthode git  
`--git-dir <path>` | Répertoire de checkout Git (par défaut : `~/openclaw`). Alias : `--dir`  
`--version <ver>` | Version ou dist-tag OpenClaw (par défaut : `latest`)  
`--node-version <ver>` | Version de Node (par défaut : `22.22.0`)  
`--json` | Émettre des événements NDJSON  
`--onboard` | Exécuter `openclaw onboard` après l’installation  
`--no-onboard` | Ignorer l’onboarding (par défaut)  
`--set-npm-prefix` | Sur Linux, forcer le préfixe npm à `~/.npm-global` si le préfixe actuel n’est pas accessible en écriture  
`--help` | Afficher l’utilisation (`-h`)  
Environment variables reference Variable | Description  
---|---  
`OPENCLAW_PREFIX=<path>` | Préfixe d’installation  
`OPENCLAW_INSTALL_METHOD=git|npm` | Méthode d’installation  
`OPENCLAW_VERSION=<ver>` | Version OpenClaw ou dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Version Node  
`OPENCLAW_GIT_DIR=<path>` | Répertoire de checkout Git pour les installations git  
`OPENCLAW_GIT_UPDATE=0|1` | Activer ou désactiver les mises à jour git pour les checkouts existants  
`OPENCLAW_NO_ONBOARD=1` | Ignorer l’onboarding  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Niveau de journalisation npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Contrôler le comportement de sharp/libvips (par défaut : `1`)  
  
* * *

## install.ps1

### Flux (install.ps1)

* ### Garantir l’environnement PowerShell + Windows

Nécessite PowerShell 5+.

* ### Garantir Node.js 24 par défaut

S’il est absent, tente l’installation via winget, puis Chocolatey, puis Scoop. Node 22 LTS, actuellement `22.16+`, reste pris en charge pour la compatibilité.

* ### Installer OpenClaw

  * Méthode `npm` (par défaut) : installation npm globale avec le `-Tag` sélectionné, lancée depuis un répertoire temporaire d’installation accessible en écriture afin que les shells ouverts dans des dossiers protégés comme `C:\` fonctionnent tout de même
  * Méthode `git` : clone/met à jour le dépôt, installe/compile avec pnpm, et installe le wrapper dans `%USERPROFILE%\.local\bin\openclaw.cmd`


* ### Tâches post-installation

  * Ajoute le répertoire bin nécessaire au PATH utilisateur lorsque c’est possible
  * Actualise au mieux un service Gateway chargé (`openclaw gateway install --force`, puis redémarrage)
  * Exécute `openclaw doctor --non-interactive` lors des mises à niveau et des installations git (au mieux)


* ### Gérer les échecs

`iwr ... | iex` et les installations par scriptblock signalent une erreur terminale sans fermer la session PowerShell actuelle. Les installations directes `powershell -File` / `pwsh -File` quittent toujours avec un code non nul pour l’automatisation.

### Exemples (install.ps1)

### Par défaut

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Installation Git

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### main GitHub via npm

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Répertoire git personnalisé

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Simulation

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Trace de débogage

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Référence des flags Flag | Description  
---|---  
`-InstallMethod npm|git` | Méthode d’installation (par défaut : `npm`)  
`-Tag <tag|version|spec>` | dist-tag npm, version ou spécification de package (par défaut : `latest`)  
`-GitDir <path>` | Répertoire de checkout (par défaut : `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Ignorer l’onboarding  
`-NoGitUpdate` | Ignorer `git pull`  
`-DryRun` | Afficher uniquement les actions  
Référence des variables d’environnement Variable | Description  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Méthode d’installation  
`OPENCLAW_GIT_DIR=<path>` | Répertoire de checkout  
`OPENCLAW_NO_ONBOARD=1` | Ignorer l’onboarding  
`OPENCLAW_GIT_UPDATE=0` | Désactiver git pull  
`OPENCLAW_DRY_RUN=1` | Mode simulation  
  
* * *

## CI et automatisation

Utilisez des flags/variables d’environnement non interactifs pour des exécutions prévisibles.

### install.sh (npm non interactif)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (git non interactif)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (ignorer l’onboarding)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Dépannage

Pourquoi Git est-il requis ?

Git est requis pour la méthode d’installation `git`. Pour les installations `npm`, Git est tout de même vérifié/installé afin d’éviter les échecs `spawn git ENOENT` lorsque des dépendances utilisent des URL git.

Pourquoi npm rencontre-t-il EACCES sous Linux ?

Certaines configurations Linux pointent le préfixe global npm vers des chemins appartenant à root. `install.sh` peut basculer le préfixe vers `~/.npm-global` et ajouter les exports PATH aux fichiers rc du shell (lorsque ces fichiers existent).

Problèmes sharp/libvips

Les scripts définissent par défaut `SHARP_IGNORE_GLOBAL_LIBVIPS=1` pour éviter que sharp soit compilé avec le libvips du système. Pour remplacer ce réglage :

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows : "npm error spawn git / ENOENT"

Installez Git for Windows, rouvrez PowerShell, puis relancez l’installateur.

Windows : "openclaw is not recognized"

Exécutez `npm config get prefix` et ajoutez ce répertoire à votre PATH utilisateur (aucun suffixe `\bin` n’est nécessaire sous Windows), puis rouvrez PowerShell.

Windows : comment obtenir une sortie détaillée de l’installateur

`install.ps1` n’expose actuellement pas de commutateur `-Verbose`. Utilisez le traçage PowerShell pour les diagnostics au niveau du script :

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

openclaw introuvable après l’installation

Il s’agit généralement d’un problème de PATH. Consultez le [dépannage Node.js](</fr/install/node#troubleshooting>).

## Connexe

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [Mise à jour](</fr/install/updating>)
  * [Désinstallation](</fr/install/uninstall>)


Was this useful?YesNo