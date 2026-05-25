---
title: Hetzner
source_url: https://docs.openclaw.ai/fr/install/hetzner
scraped_at: 2026-05-25
---

## Objectif

Exécuter un Gateway OpenClaw persistant sur un VPS Hetzner avec Docker, avec un état durable, des binaires intégrés à l’image et un comportement de redémarrage sûr.

Si vous voulez « OpenClaw 24/7 pour environ 5 $ », c’est la configuration fiable la plus simple. Les tarifs Hetzner changent ; choisissez le plus petit VPS Debian/Ubuntu et augmentez la capacité si vous rencontrez des erreurs de mémoire insuffisante.

Rappel du modèle de sécurité :

  * Les agents partagés à l’échelle de l’entreprise conviennent lorsque tout le monde se trouve dans la même frontière de confiance et que le runtime est réservé à un usage professionnel.
  * Maintenez une séparation stricte : VPS/runtime dédié + comptes dédiés ; aucun profil Apple/Google/navigateur/gestionnaire de mots de passe personnel sur cet hôte.
  * Si les utilisateurs sont adversaires les uns des autres, séparez-les par gateway/hôte/utilisateur d’OS.


Consultez [Sécurité](</fr/gateway/security>) et [Hébergement VPS](</fr/vps>).

## Que faisons-nous (en termes simples) ?

  * Louer un petit serveur Linux (VPS Hetzner)
  * Installer Docker (runtime d’application isolé)
  * Démarrer le Gateway OpenClaw dans Docker
  * Persister `~/.openclaw` \+ `~/.openclaw/workspace` sur l’hôte (survit aux redémarrages/reconstructions)
  * Accéder à l’interface utilisateur de contrôle depuis votre ordinateur portable via un tunnel SSH


Cet état monté `~/.openclaw` inclut `openclaw.json`, les fichiers par agent `agents/<agentId>/agent/auth-profiles.json`, et `.env`.

Le Gateway est accessible via :

  * Redirection de port SSH depuis votre ordinateur portable
  * Exposition directe du port si vous gérez vous-même le pare-feu et les jetons


Ce guide suppose l’utilisation d’Ubuntu ou Debian sur Hetzner.  
Si vous utilisez un autre VPS Linux, adaptez les paquets en conséquence. Pour le flux Docker générique, consultez [Docker](</fr/install/docker>).

* * *

## Parcours rapide (opérateurs expérimentés)

  1. Provisionner un VPS Hetzner
  2. Installer Docker
  3. Cloner le dépôt OpenClaw
  4. Créer des répertoires hôtes persistants
  5. Configurer `.env` et `docker-compose.yml`
  6. Intégrer les binaires requis dans l’image
  7. `docker compose up -d`
  8. Vérifier la persistance et l’accès au Gateway


* * *

## Ce dont vous avez besoin

  * VPS Hetzner avec accès root
  * Accès SSH depuis votre ordinateur portable
  * Aisance de base avec SSH + copier/coller
  * Environ 20 minutes
  * Docker et Docker Compose
  * Identifiants d’authentification du modèle
  * Identifiants fournisseur facultatifs 
    * QR WhatsApp
    * Jeton de bot Telegram
    * OAuth Gmail


* * *

* ### Provisionner le VPS

Créez un VPS Ubuntu ou Debian dans Hetzner.

Connectez-vous en tant que root :

bashCopy code
[code]
    ssh root@YOUR_VPS_IP
[/code]

Ce guide suppose que le VPS est stateful. Ne le traitez pas comme une infrastructure jetable.

* ### Installer Docker (sur le VPS)

bashCopy code
[code]
    apt-get updateapt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sh
[/code]

Vérifiez :

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### Cloner le dépôt OpenClaw

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

Ce guide suppose que vous allez construire une image personnalisée pour garantir la persistance des binaires.

* ### Créer des répertoires hôtes persistants

Les conteneurs Docker sont éphémères. Tout état durable doit vivre sur l’hôte.

bashCopy code
[code]
    mkdir -p /root/.openclaw/workspace # Set ownership to the container user (uid 1000):chown -R 1000:1000 /root/.openclaw
[/code]

* ### Configurer les variables d’environnement

Créez `.env` à la racine du dépôt.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/root/.openclawOPENCLAW_WORKSPACE_DIR=/root/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Définissez `OPENCLAW_GATEWAY_TOKEN` lorsque vous souhaitez gérer le jeton gateway stable via `.env` ; sinon, configurez `gateway.auth.token` avant de vous appuyer sur des clients entre les redémarrages. Si aucune des deux sources n’existe, OpenClaw utilise un jeton propre au runtime pour ce démarrage. Générez un mot de passe de trousseau et collez-le dans `GOG_KEYRING_PASSWORD` :

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**Ne commitez pas ce fichier.**

Ce fichier `.env` est destiné à l’environnement conteneur/runtime, par exemple `OPENCLAW_GATEWAY_TOKEN`. L’authentification OAuth/clé API fournisseur stockée vit dans le fichier monté `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`.

* ### Configuration Docker Compose

Créez ou mettez à jour `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VPS; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` sert uniquement à faciliter le bootstrap ; ce n’est pas un remplacement d’une configuration gateway appropriée. Définissez quand même l’authentification (`gateway.auth.token` ou mot de passe) et utilisez des paramètres de liaison sûrs pour votre déploiement.

* ### Étapes de runtime de VM Docker partagée

Utilisez le guide de runtime partagé pour le flux d’hôte Docker commun :

  * [Intégrer les binaires requis dans l’image](</fr/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Construire et lancer](</fr/install/docker-vm-runtime#build-and-launch>)
  * [Ce qui persiste et où](</fr/install/docker-vm-runtime#what-persists-where>)
  * [Mises à jour](</fr/install/docker-vm-runtime#updates>)


* ### Accès propre à Hetzner

Après les étapes de construction et de lancement partagées, terminez la configuration suivante pour ouvrir le tunnel :

**Prérequis :** Assurez-vous que la configuration sshd de votre VPS autorise la redirection TCP. Si vous avez renforcé votre configuration SSH, vérifiez `/etc/ssh/sshd_config` et définissez :

CodeCopy code
[code]
    AllowTcpForwarding local
[/code]

`local` autorise les redirections locales `ssh -L` depuis votre ordinateur portable tout en bloquant les redirections distantes depuis le serveur. Le définir sur `no` fera échouer le tunnel avec : `channel 3: open failed: administratively prohibited: open failed`

Après avoir confirmé que la redirection TCP est activée, redémarrez le service SSH (`systemctl restart ssh`) et lancez le tunnel depuis votre ordinateur portable :

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 root@YOUR_VPS_IP
[/code]

Ouvrez :

`http://127.0.0.1:18789/`

Collez le secret partagé configuré. Ce guide utilise le jeton gateway par défaut ; si vous êtes passé à l’authentification par mot de passe, utilisez plutôt ce mot de passe.

La carte de persistance partagée se trouve dans [Runtime de VM Docker](</fr/install/docker-vm-runtime#what-persists-where>).

## Infrastructure as Code (Terraform)

Pour les équipes qui préfèrent les flux de travail infrastructure-as-code, une configuration Terraform maintenue par la communauté fournit :

  * Configuration Terraform modulaire avec gestion de l’état distant
  * Provisionnement automatisé via cloud-init
  * Scripts de déploiement (bootstrap, deploy, sauvegarde/restauration)
  * Renforcement de la sécurité (pare-feu, UFW, accès SSH uniquement)
  * Configuration de tunnel SSH pour l’accès au gateway


**Dépôts :**

  * Infrastructure : [openclaw-terraform-hetzner](<https://github.com/andreesg/openclaw-terraform-hetzner>)
  * Configuration Docker : [openclaw-docker-config](<https://github.com/andreesg/openclaw-docker-config>)


Cette approche complète la configuration Docker ci-dessus avec des déploiements reproductibles, une infrastructure contrôlée par version et une reprise après sinistre automatisée.

## Étapes suivantes

  * Configurer les canaux de messagerie : [Canaux](</fr/channels>)
  * Configurer le Gateway : [Configuration du Gateway](</fr/gateway/configuration>)
  * Maintenir OpenClaw à jour : [Mise à jour](</fr/install/updating>)


## Connexe

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [Fly.io](</fr/install/fly>)
  * [Docker](</fr/install/docker>)
  * [Hébergement VPS](</fr/vps>)


Was this useful?YesNo