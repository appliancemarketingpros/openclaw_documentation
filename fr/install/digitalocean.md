---
title: DigitalOcean
source_url: https://docs.openclaw.ai/fr/install/digitalocean
scraped_at: 2026-05-25
---

Exécutez un OpenClaw Gateway persistant sur un Droplet DigitalOcean (~6 $/mois pour l’offre Basic 1 Go).

DigitalOcean est l’option VPS payante la plus simple. Si vous préférez des options moins chères ou gratuites :

  * [Hetzner](</fr/install/hetzner>) — 3,79 €/mois, plus de cœurs/RAM par dollar.
  * [Oracle Cloud](</fr/install/oracle>) — ARM Always Free (jusqu’à 4 OCPU, 24 Go de RAM), mais l’inscription peut être capricieuse et l’offre est uniquement ARM.


## Prérequis

  * Compte DigitalOcean ([inscription](<https://cloud.digitalocean.com/registrations/new>))
  * Paire de clés SSH (ou volonté d’utiliser l’authentification par mot de passe)
  * Environ 20 minutes


## Configuration

* ### Créer un Droplet

  1. Connectez-vous à [DigitalOcean](<https://cloud.digitalocean.com/>).
  2. Cliquez sur **Create > Droplets**.
  3. Choisissez : 
     * **Région :** la plus proche de vous
     * **Image :** Ubuntu 24.04 LTS
     * **Taille :** Basic, Regular, 1 vCPU / 1 Go de RAM / 25 Go SSD
     * **Authentification :** clé SSH (recommandé) ou mot de passe
  4. Cliquez sur **Create Droplet** et notez l’adresse IP.


* ### Se connecter et installer

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

Utilisez le shell root uniquement pour l’amorçage du système. Exécutez les commandes OpenClaw avec l’utilisateur non-root `openclaw` afin que l’état réside sous `/home/openclaw/.openclaw/` et que le Gateway s’installe comme service systemd de cet utilisateur.

* ### Lancer l’onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

L’assistant vous guide dans l’authentification du modèle, la configuration du canal, la génération du jeton du Gateway et l’installation du démon (systemd).

* ### Ajouter du swap (recommandé pour les Droplets de 1 Go)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### Vérifier le Gateway

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Accéder à l’interface utilisateur de contrôle

Le Gateway se lie au loopback par défaut. Choisissez l’une de ces options.

**Option A : tunnel SSH (le plus simple)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

Ouvrez ensuite `http://localhost:18789`.

**Option B : Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

Ouvrez ensuite `https://<magicdns>/` depuis n’importe quel appareil de votre tailnet.

Tailscale Serve authentifie le trafic de l’interface utilisateur de contrôle et WebSocket via les en-têtes d’identité du tailnet, ce qui suppose que l’hôte du Gateway lui-même est fiable. Les points de terminaison de l’API HTTP suivent le mode d’authentification normal du Gateway (jeton/mot de passe) dans tous les cas. Pour exiger des identifiants à secret partagé explicites via Serve, définissez `gateway.auth.allowTailscale: false` et utilisez `gateway.auth.mode: "token"` ou `"password"`.

**Option C : liaison au tailnet (sans Serve)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

Ouvrez ensuite `http://<tailscale-ip>:18789` (jeton requis).

## Persistance et sauvegardes

L’état d’OpenClaw réside sous :

  * `~/.openclaw/` — `openclaw.json`, les fichiers `auth-profiles.json` par agent, l’état des canaux/fournisseurs et les données de session.
  * `~/.openclaw/workspace/` — l’espace de travail de l’agent ([SOUL.md](<http://SOUL.md>), mémoire, artefacts).


Ces données survivent aux redémarrages du Droplet. Pour créer un instantané portable :

bashCopy code
[code]
    openclaw backup create
[/code]

Les instantanés DigitalOcean sauvegardent l’intégralité du Droplet ; `openclaw backup create` est portable entre hôtes.

## Conseils pour 1 Go de RAM

Le Droplet à 6 $ ne dispose que de 1 Go de RAM. Pour garder un fonctionnement fluide :

  * Assurez-vous que l’étape de swap ci-dessus est présente dans `/etc/fstab` afin qu’elle survive aux redémarrages.
  * Préférez les modèles basés sur API (Claude, GPT) aux modèles locaux — l’inférence LLM locale ne tient pas dans 1 Go.
  * Définissez `agents.defaults.model.primary` sur un modèle plus petit si vous rencontrez des OOM sur de grandes invites.
  * Surveillez avec `free -h` et `htop`.


## Dépannage

**Le Gateway ne démarre pas** \-- Exécutez `openclaw doctor --non-interactive` et consultez les journaux avec `journalctl --user -u openclaw-gateway.service -n 50`.

**Port déjà utilisé** \-- Exécutez `lsof -i :18789` pour trouver le processus, puis arrêtez-le.

**Mémoire insuffisante** \-- Vérifiez que le swap est actif avec `free -h`. Si vous rencontrez encore des OOM, utilisez des modèles basés sur API (Claude, GPT) plutôt que des modèles locaux, ou passez à un Droplet de 2 Go.

## Étapes suivantes

  * [Canaux](</fr/channels>) \-- connectez Telegram, WhatsApp, Discord et plus encore
  * [Configuration du Gateway](</fr/gateway/configuration>) \-- toutes les options de configuration
  * [Mise à jour](</fr/install/updating>) \-- maintenez OpenClaw à jour


## Connexe

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [Fly.io](</fr/install/fly>)
  * [Hetzner](</fr/install/hetzner>)
  * [Hébergement VPS](</fr/vps>)


Was this useful?YesNo