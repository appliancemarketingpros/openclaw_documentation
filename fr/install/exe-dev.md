---
title: exe.dev
source_url: https://docs.openclaw.ai/fr/install/exe-dev
scraped_at: 2026-05-25
---

Objectif : OpenClaw Gateway exécuté sur une VM exe.dev, accessible depuis votre ordinateur portable via : `https://<vm-name>.exe.xyz`

Cette page suppose l’image **exeuntu** par défaut d’exe.dev. Si vous avez choisi une autre distribution, adaptez les paquets en conséquence.

## Parcours rapide pour débutants

  1. <https://exe.new/openclaw>
  2. Renseignez votre clé ou jeton d’authentification selon les besoins
  3. Cliquez sur « Agent » à côté de votre VM et attendez que Shelley termine le provisionnement
  4. Ouvrez `https://<vm-name>.exe.xyz/` et authentifiez-vous avec le secret partagé configuré (ce guide utilise l’authentification par jeton par défaut, mais l’authentification par mot de passe fonctionne aussi si vous modifiez `gateway.auth.mode`)
  5. Approuvez toute demande d’association d’appareil en attente avec `openclaw devices approve <requestId>`


## Ce dont vous avez besoin

  * Compte exe.dev
  * Accès `ssh exe.dev` aux machines virtuelles [exe.dev](<https://exe.dev>) (facultatif)


## Installation automatisée avec Shelley

Shelley, l’agent d’[exe.dev](<https://exe.dev>), peut installer OpenClaw instantanément avec notre invite. L’invite utilisée est la suivante :

CodeCopy code
[code]
    Set up OpenClaw (https://docs.openclaw.ai/install) on this VM. Use the non-interactive and accept-risk flags for openclaw onboarding. Add the supplied auth or token as needed. Configure nginx to forward from the default port 18789 to the root location on the default enabled site config, making sure to enable Websocket support. Pairing is done by "openclaw devices list" and "openclaw devices approve <request id>". Make sure the dashboard shows that OpenClaw's health is OK. exe.dev handles forwarding from port 8000 to port 80/443 and HTTPS for us, so the final "reachable" should be <vm-name>.exe.xyz, without port specification.
[/code]

## Installation manuelle

## 1) Créer la VM

Depuis votre appareil :

bashCopy code
[code]
    ssh exe.dev new
[/code]

Puis connectez-vous :

bashCopy code
[code]
    ssh <vm-name>.exe.xyz
[/code]

## 2) Installer les prérequis (sur la VM)

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl jq ca-certificates openssl
[/code]

## 3) Installer OpenClaw

Exécutez le script d’installation d’OpenClaw :

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

## 4) Configurer nginx pour proxifier OpenClaw vers le port 8000

Modifiez `/etc/nginx/sites-enabled/default` avec

CodeCopy code
[code]
    server {    listen 80 default_server;    listen [::]:80 default_server;    listen 8000;    listen [::]:8000;     server_name _;     location / {        proxy_pass http://127.0.0.1:18789;        proxy_http_version 1.1;         # WebSocket support        proxy_set_header Upgrade $http_upgrade;        proxy_set_header Connection "upgrade";         # Standard proxy headers        proxy_set_header Host $host;        proxy_set_header X-Real-IP $remote_addr;        proxy_set_header X-Forwarded-For $remote_addr;        proxy_set_header X-Forwarded-Proto $scheme;         # Timeout settings for long-lived connections        proxy_read_timeout 86400s;        proxy_send_timeout 86400s;    }}
[/code]

Remplacez les en-têtes de transfert au lieu de conserver les chaînes fournies par le client. OpenClaw ne fait confiance aux métadonnées d’IP transférées que depuis des proxys explicitement configurés, et les chaînes `X-Forwarded-For` de type ajout sont traitées comme un risque de renforcement.

## 5) Accéder à OpenClaw et accorder les privilèges

Accédez à `https://<vm-name>.exe.xyz/` (consultez la sortie de la Control UI lors de l’intégration). Si une authentification est demandée, collez le secret partagé configuré depuis la VM. Ce guide utilise l’authentification par jeton ; récupérez donc `gateway.auth.token` avec `openclaw config get gateway.auth.token` (ou générez-en un avec `openclaw doctor --generate-gateway-token`). Si vous avez basculé le gateway vers l’authentification par mot de passe, utilisez plutôt `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD`. Approuvez les appareils avec `openclaw devices list` et `openclaw devices approve <requestId>`. En cas de doute, utilisez Shelley depuis votre navigateur !

## Configuration des canaux distants

Pour les hôtes distants, préférez un seul appel `config patch` à de nombreux appels SSH à `config set`. Gardez les vrais jetons dans l’environnement de la VM ou `~/.openclaw/.env`, et ne placez que des SecretRefs dans `openclaw.json`.

Sur la VM, faites en sorte que l’environnement du service contienne les secrets dont il a besoin :

bashCopy code
[code]
    cat >> ~/.openclaw/.env <<'EOF'SLACK_BOT_TOKEN=xoxb-...SLACK_APP_TOKEN=xapp-...DISCORD_BOT_TOKEN=...OPENAI_API_KEY=sk-...EOF
[/code]

Depuis votre machine locale, créez un fichier de correctif et transmettez-le à la VM :

json5Copy code
[code]
    // openclaw.remote.patch.json5{  secrets: {    providers: {      default: { source: "env" },    },  },  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --dry-run' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw config patch --stdin' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw gateway restart && openclaw health'
[/code]

Utilisez `--replace-path` lorsqu’une liste d’autorisation imbriquée doit devenir exactement la valeur du correctif, par exemple lors du remplacement d’une liste d’autorisation de canal Discord :

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --replace-path "channels.discord.guilds[\"123\"].channels"' < ./discord.patch.json5
[/code]

## Accès distant

L’accès distant est géré par l’authentification d’[exe.dev](<https://exe.dev>). Par défaut, le trafic HTTP depuis le port 8000 est transféré vers `https://<vm-name>.exe.xyz` avec authentification par e-mail.

## Mise à jour

bashCopy code
[code]
    npm i -g openclaw@latestopenclaw doctoropenclaw gateway restartopenclaw health
[/code]

Guide : [Mise à jour](</fr/install/updating>)

## Connexe

  * [Gateway distant](</fr/gateway/remote>)
  * [Vue d’ensemble de l’installation](</fr/install>)


Was this useful?YesNo