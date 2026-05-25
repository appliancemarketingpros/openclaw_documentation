---
title: Installer
source_url: https://docs.openclaw.ai/fr/install
scraped_at: 2026-05-25
---

## Prérequis système

  * **Node 24** (recommandé) ou Node 22.16+ - le script d’installation s’en charge automatiquement
  * **macOS, Linux ou Windows** \- Windows natif et WSL2 sont tous deux pris en charge ; WSL2 est plus stable. Consultez [Windows](</fr/platforms/windows>).
  * `pnpm` est nécessaire uniquement si vous compilez depuis les sources


## Recommandé : script d’installation

La façon la plus rapide d’installer. Il détecte votre OS, installe Node si nécessaire, installe OpenClaw et lance l’onboarding.

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

Pour installer sans exécuter l’onboarding :

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

Pour tous les flags et les options CI/automatisation, consultez [Fonctionnement interne de l’installateur](</fr/install/installer>).

## Méthodes d’installation alternatives

### Installateur à préfixe local (`install-cli.sh`)

Utilisez ceci lorsque vous souhaitez conserver OpenClaw et Node sous un préfixe local tel que `~/.openclaw`, sans dépendre d’une installation système de Node :

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

Il prend en charge les installations npm par défaut, ainsi que les installations depuis un checkout git dans le même flux de préfixe. Référence complète : [Fonctionnement interne de l’installateur](</fr/install/installer#install-clish>).

Déjà installé ? Basculez entre les installations par package et par git avec `openclaw update --channel dev` et `openclaw update --channel stable`. Consultez [Mise à jour](</fr/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm ou bun

Si vous gérez déjà Node vous-même :

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Dépannage : erreurs de build sharp (npm)

Si `sharp` échoue à cause d’un libvips installé globalement :

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### Depuis les sources

Pour les contributeurs ou toute personne souhaitant exécuter depuis un checkout local :

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Ou ignorez le lien et utilisez `pnpm openclaw ...` depuis l’intérieur du dépôt. Consultez [Configuration](</fr/start/setup>) pour les flux de développement complets.

### Installer depuis GitHub main

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Conteneurs et gestionnaires de packages

[**Docker** Déploiements conteneurisés ou headless. ](</fr/install/docker>) [**Podman** Alternative à Docker avec conteneurs rootless. ](</fr/install/podman>) [**Nix** Installation déclarative via une flake Nix. ](</fr/install/nix>) [**Ansible** Provisionnement automatisé de parc. ](</fr/install/ansible>) [**Bun** Utilisation CLI uniquement via l’environnement d’exécution Bun. ](</fr/install/bun>)

## Vérifier l’installation

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

Si vous souhaitez un démarrage géré après l’installation :

  * macOS : LaunchAgent via `openclaw onboard --install-daemon` ou `openclaw gateway install`
  * Linux/WSL2 : service utilisateur systemd via les mêmes commandes
  * Windows natif : tâche planifiée en premier, avec un élément de connexion par utilisateur dans le dossier de démarrage comme solution de secours si la création de la tâche est refusée


## Hébergement et déploiement

Déployez OpenClaw sur un serveur cloud ou un VPS :

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9mci9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** Mettre à jour, migrer ou désinstaller [**Updating** Gardez OpenClaw à jour. ](</fr/install/updating>) [**Migrating** Passer à une nouvelle machine. ](</fr/install/migrating>) [**Uninstall** Supprimer complètement OpenClaw. ](</fr/install/uninstall>) Dépannage : `openclaw` introuvable Si l’installation a réussi mais que `openclaw` est introuvable dans votre terminal : bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

Si `$(npm prefix -g)/bin` n’est pas dans votre `$PATH`, ajoutez-le à votre fichier de démarrage du shell (`~/.zshrc` ou `~/.bashrc`) : bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Ouvrez ensuite un nouveau terminal. Consultez [Configuration de Node](</fr/install/node>) pour plus de détails. ](</fr/install/northflank>) Was this useful?YesNo ](</fr/install/render>)](</fr/install/railway>)](</fr/install/azure>)](</fr/install/gcp>)](</fr/install/hetzner>)](</fr/install/kubernetes>)](</fr/install/docker-vm-runtime>)](</fr/vps>)