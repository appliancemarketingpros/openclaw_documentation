---
title: GCP
source_url: https://docs.openclaw.ai/fr/install/gcp
scraped_at: 2026-05-25
---

Exécutez un OpenClaw Gateway persistant sur une VM GCP Compute Engine avec Docker, avec un état durable, des binaires intégrés et un comportement de redémarrage sûr.

Si vous voulez « OpenClaw 24/7 pour environ 5 à 12 $/mois », c’est une configuration fiable sur Google Cloud. Les prix varient selon le type de machine et la région ; choisissez la plus petite VM adaptée à votre charge de travail et augmentez la capacité si vous rencontrez des erreurs OOM.

## Que faisons-nous (en termes simples) ?

  * Créer un projet GCP et activer la facturation
  * Créer une VM Compute Engine
  * Installer Docker (runtime d’application isolé)
  * Démarrer l’OpenClaw Gateway dans Docker
  * Conserver `~/.openclaw` \+ `~/.openclaw/workspace` sur l’hôte (survit aux redémarrages/reconstructions)
  * Accéder à l’UI de contrôle depuis votre ordinateur portable via un tunnel SSH


Cet état `~/.openclaw` monté inclut `openclaw.json`, les fichiers par agent `agents/<agentId>/agent/auth-profiles.json`, et `.env`.

Le Gateway est accessible via :

  * redirection de port SSH depuis votre ordinateur portable
  * exposition directe du port si vous gérez vous-même le pare-feu et les jetons


Ce guide utilise Debian sur GCP Compute Engine. Ubuntu fonctionne aussi ; adaptez les paquets en conséquence. Pour le flux Docker générique, consultez [Docker](</fr/install/docker>).

* * *

## Parcours rapide (opérateurs expérimentés)

  1. Créer un projet GCP + activer l’API Compute Engine
  2. Créer une VM Compute Engine (e2-small, Debian 12, 20 Go)
  3. Se connecter à la VM en SSH
  4. Installer Docker
  5. Cloner le dépôt OpenClaw
  6. Créer des répertoires hôtes persistants
  7. Configurer `.env` et `docker-compose.yml`
  8. Intégrer les binaires requis, construire et lancer


* * *

## Ce dont vous avez besoin

  * Compte GCP (éligible au niveau gratuit pour e2-micro)
  * gcloud CLI installé (ou utiliser Cloud Console)
  * Accès SSH depuis votre ordinateur portable
  * Aisance de base avec SSH + copier/coller
  * Environ 20 à 30 minutes
  * Docker et Docker Compose
  * Identifiants d’authentification du modèle
  * Identifiants de fournisseur facultatifs 
    * QR WhatsApp
    * Jeton de bot Telegram
    * OAuth Gmail


* * *

* ### Installer gcloud CLI (ou utiliser Console)

**Option A : gcloud CLI** (recommandé pour l’automatisation)

Installez depuis <https://cloud.google.com/sdk/docs/install>

Initialisez et authentifiez-vous :

bashCopy code
[code]
    gcloud initgcloud auth login
[/code]

**Option B : Cloud Console**

Toutes les étapes peuvent être effectuées via l’UI web à l’adresse <https://console.cloud.google.com>

* ### Créer un projet GCP

**CLI :**

bashCopy code
[code]
    gcloud projects create my-openclaw-project --name="OpenClaw Gateway"gcloud config set project my-openclaw-project
[/code]

Activez la facturation sur <https://console.cloud.google.com/billing> (requise pour Compute Engine).

Activez l’API Compute Engine :

bashCopy code
[code]
    gcloud services enable compute.googleapis.com
[/code]

**Console :**

  1. Accédez à IAM & Admin > Create Project
  2. Nommez-le et créez-le
  3. Activez la facturation pour le projet
  4. Accédez à APIs & Services > Enable APIs > recherchez « Compute Engine API » > Enable


* ### Créer la VM

**Types de machines :**

Type | Spécifications | Coût | Notes  
---|---|---|---  
e2-medium | 2 vCPU, 4 Go de RAM | environ 25 $/mois | Le plus fiable pour les builds Docker locaux  
e2-small | 2 vCPU, 2 Go de RAM | environ 12 $/mois | Minimum recommandé pour un build Docker  
e2-micro | 2 vCPU (partagés), 1 Go de RAM | Éligible au niveau gratuit | Échoue souvent avec un OOM de build Docker (exit 137)  
  
**CLI :**

bashCopy code
[code]
    gcloud compute instances create openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small \  --boot-disk-size=20GB \  --image-family=debian-12 \  --image-project=debian-cloud
[/code]

**Console :**

  1. Accédez à Compute Engine > VM instances > Create instance
  2. Nom : `openclaw-gateway`
  3. Région : `us-central1`, Zone : `us-central1-a`
  4. Type de machine : `e2-small`
  5. Disque de démarrage : Debian 12, 20 Go
  6. Créez


* ### Se connecter à la VM en SSH

**CLI :**

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
[/code]

**Console :**

Cliquez sur le bouton « SSH » à côté de votre VM dans le tableau de bord Compute Engine.

Remarque : la propagation des clés SSH peut prendre 1 à 2 minutes après la création de la VM. Si la connexion est refusée, attendez puis réessayez.

* ### Installer Docker (sur la VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sudo shsudo usermod -aG docker $USER
[/code]

Déconnectez-vous puis reconnectez-vous pour que le changement de groupe prenne effet :

bashCopy code
[code]
    exit
[/code]

Ensuite, reconnectez-vous en SSH :

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
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

Ce guide suppose que vous construirez une image personnalisée pour garantir la persistance des binaires.

* ### Créer des répertoires hôtes persistants

Les conteneurs Docker sont éphémères. Tout état durable doit vivre sur l’hôte.

bashCopy code
[code]
    mkdir -p ~/.openclawmkdir -p ~/.openclaw/workspace
[/code]

* ### Configurer les variables d’environnement

Créez `.env` à la racine du dépôt.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/home/$USER/.openclawOPENCLAW_WORKSPACE_DIR=/home/$USER/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Définissez `OPENCLAW_GATEWAY_TOKEN` lorsque vous voulez gérer le jeton stable du gateway via `.env` ; sinon, configurez `gateway.auth.token` avant de vous appuyer sur les clients entre les redémarrages. Si aucune source n’existe, OpenClaw utilise un jeton valable uniquement pour le runtime lors de ce démarrage. Générez un mot de passe de trousseau et collez-le dans `GOG_KEYRING_PASSWORD` :

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**Ne committez pas ce fichier.**

Ce fichier `.env` sert aux variables d’environnement du conteneur/runtime comme `OPENCLAW_GATEWAY_TOKEN`. L’authentification OAuth/clé API des fournisseurs stockée réside dans le fichier monté `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`.

* ### Configuration Docker Compose

Créez ou mettez à jour `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VM; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` sert uniquement à faciliter l’amorçage ; ce n’est pas un remplacement d’une configuration de gateway appropriée. Définissez tout de même l’authentification (`gateway.auth.token` ou mot de passe) et utilisez des paramètres de liaison sûrs pour votre déploiement.

* ### Étapes partagées du runtime de VM Docker

Utilisez le guide de runtime partagé pour le flux hôte Docker commun :

  * [Intégrer les binaires requis dans l’image](</fr/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Construire et lancer](</fr/install/docker-vm-runtime#build-and-launch>)
  * [Ce qui persiste et où](</fr/install/docker-vm-runtime#what-persists-where>)
  * [Mises à jour](</fr/install/docker-vm-runtime#updates>)


* ### Notes de lancement spécifiques à GCP

Sur GCP, si le build échoue avec `Killed` ou `exit code 137` pendant `pnpm install --frozen-lockfile`, la VM manque de mémoire. Utilisez au minimum `e2-small`, ou `e2-medium` pour des premiers builds plus fiables.

Lors de la liaison au LAN (`OPENCLAW_GATEWAY_BIND=lan`), configurez une origine de navigateur approuvée avant de continuer :

bashCopy code
[code]
    docker compose run --rm openclaw-cli config set gateway.controlUi.allowedOrigins '["http://127.0.0.1:18789"]' --strict-json
[/code]

Si vous avez changé le port du gateway, remplacez `18789` par votre port configuré.

* ### Accéder depuis votre ordinateur portable

Créez un tunnel SSH pour transférer le port du Gateway :

bashCopy code
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a -- -L 18789:127.0.0.1:18789
[/code]

Ouvrez dans votre navigateur :

`http://127.0.0.1:18789/`

Réaffichez un lien de tableau de bord propre :

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-open
[/code]

Si l’UI demande une authentification par secret partagé, collez le jeton configuré ou le mot de passe dans les paramètres de l’UI de contrôle. Ce flux Docker écrit un jeton par défaut ; si vous basculez la configuration du conteneur vers l’authentification par mot de passe, utilisez plutôt ce mot de passe.

Si l’UI de contrôle affiche `unauthorized` ou `disconnected (1008): pairing required`, approuvez l’appareil du navigateur :

bashCopy code
[code]
    docker compose run --rm openclaw-cli devices listdocker compose run --rm openclaw-cli devices approve <requestId>
[/code]

Besoin à nouveau de la référence sur la persistance partagée et les mises à jour ? Consultez [Runtime de VM Docker](</fr/install/docker-vm-runtime#what-persists-where>) et [mises à jour du runtime de VM Docker](</fr/install/docker-vm-runtime#updates>).

* * *

## Dépannage

**Connexion SSH refusée**

La propagation des clés SSH peut prendre 1 à 2 minutes après la création de la VM. Attendez puis réessayez.

**Problèmes OS Login**

Vérifiez votre profil OS Login :

bashCopy code
[code]
    gcloud compute os-login describe-profile
[/code]

Assurez-vous que votre compte dispose des autorisations IAM requises (Compute OS Login ou Compute OS Admin Login).

**Mémoire insuffisante (OOM)**

Si le build Docker échoue avec `Killed` et `exit code 137`, la VM a été tuée par OOM. Passez à e2-small (minimum) ou e2-medium (recommandé pour des builds locaux fiables) :

bashCopy code
[code]
    # Stop the VM firstgcloud compute instances stop openclaw-gateway --zone=us-central1-a # Change machine typegcloud compute instances set-machine-type openclaw-gateway \  --zone=us-central1-a \  --machine-type=e2-small # Start the VMgcloud compute instances start openclaw-gateway --zone=us-central1-a
[/code]

* * *

## Comptes de service (meilleure pratique de sécurité)

Pour un usage personnel, votre compte utilisateur par défaut convient très bien.

Pour l’automatisation ou les pipelines CI/CD, créez un compte de service dédié avec des autorisations minimales :

  1. Créez un compte de service :

bashCopy code
[code]gcloud iam service-accounts create openclaw-deploy \  --display-name="OpenClaw Deployment"
[/code]

  2. Accordez le rôle Compute Instance Admin (ou un rôle personnalisé plus restreint) :

bashCopy code
[code]gcloud projects add-iam-policy-binding my-openclaw-project \  --member="serviceAccount:openclaw-deploy@my-openclaw-project.iam.gserviceaccount.com" \  --role="roles/compute.instanceAdmin.v1"
[/code]


Évitez d’utiliser le rôle Owner pour l’automatisation. Appliquez le principe du moindre privilège.

Consultez <https://cloud.google.com/iam/docs/understanding-roles> pour les détails des rôles IAM.

* * *

## Étapes suivantes

  * Configurer les canaux de messagerie : [Canaux](</fr/channels>)
  * Appairer les appareils locaux en tant que nœuds : [Nœuds](</fr/nodes>)
  * Configurer le Gateway : [Configuration du Gateway](</fr/gateway/configuration>)


## Associé

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [Azure](</fr/install/azure>)
  * [Hébergement VPS](</fr/vps>)


Was this useful?YesNo