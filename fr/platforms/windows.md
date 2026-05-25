---
title: Windows
source_url: https://docs.openclaw.ai/fr/platforms/windows
scraped_at: 2026-05-25
---

OpenClaw prend en charge à la fois **Windows natif** et **WSL2**. WSL2 est le chemin le plus stable et recommandé pour l’expérience complète : la CLI, le Gateway et l’outillage s’exécutent dans Linux avec une compatibilité totale. Windows natif fonctionne pour l’utilisation de base de la CLI et du Gateway, avec certaines réserves indiquées ci-dessous.

Les applications compagnon Windows natives sont prévues.

## WSL2 (recommandé)

  * [Premiers pas](</fr/start/getting-started>) (à utiliser dans WSL)
  * [Installation et mises à jour](</fr/install/updating>)
  * Guide officiel de WSL2 (Microsoft) : <https://learn.microsoft.com/windows/wsl/install>


## État de Windows natif

Les flux CLI Windows natifs s’améliorent, mais WSL2 reste le chemin recommandé.

Ce qui fonctionne bien sur Windows natif aujourd’hui :

  * programme d’installation du site web via `install.ps1`
  * utilisation locale de la CLI, comme `openclaw --version`, `openclaw doctor` et `openclaw plugins list --json`
  * test de validation rapide de l’agent/fournisseur local intégré, comme :

powershellCopy code
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
[/code]

Réserves actuelles :

  * `openclaw onboard --non-interactive` attend toujours un Gateway local accessible, sauf si vous passez `--skip-health`
  * `openclaw onboard --non-interactive --install-daemon` et `openclaw gateway install` essaient d’abord les tâches planifiées Windows
  * si la création de tâche planifiée est refusée, OpenClaw se rabat sur un élément de connexion par utilisateur dans le dossier de démarrage et démarre immédiatement le Gateway
  * si `schtasks` lui-même se bloque ou cesse de répondre, OpenClaw abandonne désormais rapidement ce chemin et se rabat au lieu de rester suspendu indéfiniment
  * les tâches planifiées restent privilégiées lorsqu’elles sont disponibles, car elles fournissent un meilleur état de supervision


Si vous voulez uniquement la CLI native, sans installation du service Gateway, utilisez l’une de ces commandes :

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

Si vous voulez bien un démarrage géré sur Windows natif :

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

Si la création de tâche planifiée est bloquée, le mode de service de secours démarre tout de même automatiquement après la connexion via le dossier de démarrage de l’utilisateur actuel.

## Gateway

  * [Runbook Gateway](</fr/gateway>)
  * [Configuration](</fr/gateway/configuration>)


## Installation du service Gateway (CLI)

Dans WSL2 :

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Ou :

CodeCopy code
[code]
    openclaw gateway install
[/code]

Ou :

CodeCopy code
[code]
    openclaw configure
[/code]

Sélectionnez **Service Gateway** lorsque l’invite s’affiche.

Réparer/migrer :

CodeCopy code
[code]
    openclaw doctor
[/code]

## Démarrage automatique du Gateway avant la connexion Windows

Pour les configurations sans interface, assurez-vous que toute la chaîne de démarrage s’exécute même lorsque personne ne se connecte à Windows.

### 1) Maintenir les services utilisateur en cours d’exécution sans connexion

Dans WSL :

bashCopy code
[code]
    sudo loginctl enable-linger "$(whoami)"
[/code]

### 2) Installer le service utilisateur du Gateway OpenClaw

Dans WSL :

bashCopy code
[code]
    openclaw gateway install
[/code]

### 3) Démarrer WSL automatiquement au démarrage de Windows

Dans PowerShell en tant qu’administrateur :

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
[/code]

Remplacez `Ubuntu` par le nom de votre distribution obtenu avec :

powershellCopy code
[code]
    wsl --list --verbose
[/code]

### Vérifier la chaîne de démarrage

Après un redémarrage (avant la connexion Windows), vérifiez depuis WSL :

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## Avancé : exposer les services WSL sur le LAN (portproxy)

WSL possède son propre réseau virtuel. Si une autre machine doit atteindre un service s’exécutant **dans WSL** (SSH, un serveur TTS local ou le Gateway), vous devez transférer un port Windows vers l’IP WSL actuelle. L’IP WSL change après les redémarrages, vous devrez donc peut-être actualiser la règle de transfert.

Exemple (PowerShell **en tant qu’administrateur**) :

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort
[/code]

Autorisez le port dans le pare-feu Windows (une seule fois) :

powershellCopy code
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

Actualisez le portproxy après les redémarrages de WSL :

powershellCopy code
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Nullnetsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `  connectaddress=$WslIp connectport=$TargetPort | Out-Null
[/code]

Notes :

  * SSH depuis une autre machine cible l’**IP de l’hôte Windows** (exemple : `ssh user@windows-host -p 2222`).
  * Les nœuds distants doivent pointer vers une URL de Gateway **accessible** (pas `127.0.0.1`) ; utilisez `openclaw status --all` pour confirmer.
  * Utilisez `listenaddress=0.0.0.0` pour l’accès LAN ; `127.0.0.1` le garde uniquement local.
  * Si vous voulez que cela soit automatique, enregistrez une tâche planifiée pour exécuter l’étape d’actualisation à la connexion.


## Installation WSL2 étape par étape

### 1) Installer WSL2 + Ubuntu

Ouvrez PowerShell (administrateur) :

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

Redémarrez si Windows le demande.

### 2) Activer systemd (requis pour l’installation du Gateway)

Dans votre terminal WSL :

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

Puis depuis PowerShell :

powershellCopy code
[code]
    wsl --shutdown
[/code]

Rouvrez Ubuntu, puis vérifiez :

bashCopy code
[code]
    systemctl --user status
[/code]

### 3) Installer OpenClaw (dans WSL)

Pour une configuration initiale normale dans WSL, suivez le flux Linux Premiers pas :

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm installpnpm buildpnpm ui:buildpnpm openclaw onboard --install-daemon
[/code]

Si vous développez depuis les sources au lieu d’effectuer une configuration initiale, utilisez la boucle de développement source de [Configuration](</fr/start/setup>) :

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

Guide complet : [Premiers pas](</fr/start/getting-started>)

## Application compagnon Windows

Nous n’avons pas encore d’application compagnon Windows. Les contributions sont les bienvenues si vous voulez aider à la concrétiser.

## Connectivité Git et GitHub (contributeurs)

Certains réseaux bloquent ou limitent HTTPS vers GitHub. Si `git clone` échoue avec des délais d’attente ou des réinitialisations de connexion, essayez un autre réseau, un VPN ou un proxy HTTP/HTTPS fourni par votre organisation.

Si `gh auth login` échoue pendant le flux d’appareil du navigateur (par exemple avec un délai d’attente pour atteindre `github.com:443`), authentifiez-vous plutôt avec un jeton d’accès personnel :

  1. Créez un jeton avec au moins la portée `repo` (PAT classique) ou un accès finement granulaire équivalent.
  2. Dans PowerShell pour la session actuelle :

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

  3. Si `gh auth status` avertit que `read:org` est manquant, créez un jeton qui inclut cette portée et réaffectez la variable :

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token-with-repo-and-read:org>"gh auth status
[/code]

`gh auth refresh -s read:org` s’applique uniquement lorsque vous vous êtes authentifié via `gh auth login` et que vous avez des identifiants stockés à actualiser (pas lorsque vous utilisez `GH_TOKEN`).

Ne commettez jamais de jetons et ne les collez jamais dans des issues ou des pull requests.

## Connexe

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [Plateformes](</fr/platforms>)


Was this useful?YesNo