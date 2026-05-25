---
title: Environnement d’exécution de VM Docker
source_url: https://docs.openclaw.ai/fr/install/docker-vm-runtime
scraped_at: 2026-05-25
---

Étapes d’exécution partagées pour les installations Docker basées sur des VM, comme GCP, Hetzner et les fournisseurs de VPS similaires.

## Intégrer les binaires requis dans l’image

Installer des binaires dans un conteneur en cours d’exécution est un piège. Tout ce qui est installé à l’exécution sera perdu au redémarrage.

Tous les binaires externes requis par les Skills doivent être installés au moment de la construction de l’image.

Les exemples ci-dessous ne montrent que trois binaires courants :

  * `gog` (depuis `gogcli`) pour l’accès à Gmail
  * `goplaces` pour Google Places
  * `wacli` pour WhatsApp


Ce sont des exemples, pas une liste complète. Vous pouvez installer autant de binaires que nécessaire en utilisant le même modèle.

Si vous ajoutez plus tard de nouvelles Skills qui dépendent de binaires supplémentaires, vous devez :

  1. Mettre à jour le Dockerfile
  2. Reconstruire l’image
  3. Redémarrer les conteneurs


**Exemple de Dockerfile**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## Construire et lancer

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

Si la construction échoue avec `Killed` ou `exit code 137` pendant `pnpm install --frozen-lockfile`, la VM manque de mémoire. Utilisez une classe de machine plus grande avant de réessayer.

Vérifier les binaires :

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

Sortie attendue :

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

Vérifier le Gateway :

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

Sortie attendue :

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## Ce qui persiste, et où

OpenClaw s’exécute dans Docker, mais Docker n’est pas la source de vérité. Tout état durable doit survivre aux redémarrages, reconstructions et redémarrages système.

Composant | Emplacement | Mécanisme de persistance | Notes  
---|---|---|---  
Configuration du Gateway | `/home/node/.openclaw/` | Montage de volume hôte | Inclut `openclaw.json`, `.env`  
Profils d’authentification des modèles | `/home/node/.openclaw/agents/` | Montage de volume hôte | `agents/<agentId>/agent/auth-profiles.json` (OAuth, clés API)  
Clé de profil d’authentification | `/home/node/.config/openclaw/` | Montage de volume hôte | Clé de chiffrement locale pour le matériel de jeton du profil d’authentification OAuth  
Configurations des Skills | `/home/node/.openclaw/skills/` | Montage de volume hôte | État au niveau des Skills  
Espace de travail de l’agent | `/home/node/.openclaw/workspace/` | Montage de volume hôte | Code et artefacts d’agent  
Session WhatsApp | `/home/node/.openclaw/` | Montage de volume hôte | Préserve la connexion par QR code  
Trousseau Gmail | `/home/node/.openclaw/` | Volume hôte + mot de passe | Nécessite `GOG_KEYRING_PASSWORD`  
Paquets de Plugin | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | Montage de volume hôte | Racines des paquets de Plugin téléchargeables  
Binaires externes | `/usr/local/bin/` | Image Docker | Doivent être intégrés au moment de la construction  
Runtime Node | Système de fichiers du conteneur | Image Docker | Reconstruit à chaque construction d’image  
Paquets du système d’exploitation | Système de fichiers du conteneur | Image Docker | Ne pas installer à l’exécution  
Conteneur Docker | Éphémère | Redémarrable | Peut être détruit sans risque  
  
## Mises à jour

Pour mettre à jour OpenClaw sur la VM :

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## Connexe

  * [Docker](</fr/install/docker>)
  * [Podman](</fr/install/podman>)
  * [ClawDock](</fr/install/clawdock>)


Was this useful?YesNo