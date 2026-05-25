---
title: Fly.io
source_url: https://docs.openclaw.ai/fr/install/fly
scraped_at: 2026-05-25
---

**Objectif :** Gateway OpenClaw exécuté sur une machine [Fly.io](<https://fly.io>) avec stockage persistant, HTTPS automatique et accès Discord/canal.

## Ce dont vous avez besoin

  * [CLI flyctl](<https://fly.io/docs/hands-on/install-flyctl/>) installée
  * Compte [Fly.io](<http://Fly.io>) (l’offre gratuite fonctionne)
  * Authentification de modèle : clé d’API pour le fournisseur de modèles choisi
  * Identifiants de canal : jeton de bot Discord, jeton Telegram, etc.


## Parcours rapide pour débuter

  1. Cloner le dépôt → personnaliser `fly.toml`
  2. Créer l’application + le volume → définir les secrets
  3. Déployer avec `fly deploy`
  4. Se connecter en SSH pour créer la configuration ou utiliser l’interface de contrôle


* ### Créer l’application Fly

bashCopy code
[code]
    # Clone the repogit clone https://github.com/openclaw/openclaw.gitcd openclaw # Create a new Fly app (pick your own name)fly apps create my-openclaw # Create a persistent volume (1GB is usually enough)fly volumes create openclaw_data --size 1 --region iad
[/code]

**Conseil :** Choisissez une région proche de vous. Options courantes : `lhr` (Londres), `iad` (Virginie), `sjc` (San Jose).

* ### Configurer fly.toml

Modifiez `fly.toml` pour qu’il corresponde au nom de votre application et à vos besoins.

**Note de sécurité :** La configuration par défaut expose une URL publique. Pour un déploiement renforcé sans IP publique, consultez Déploiement privé ou utilisez `deploy/fly.private.toml`.

tomlCopy code
[code]
    app = "my-openclaw"  # Your app nameprimary_region = "iad" [build]  dockerfile = "Dockerfile" [env]  NODE_ENV = "production"  OPENCLAW_PREFER_PNPM = "1"  OPENCLAW_STATE_DIR = "/data"  NODE_OPTIONS = "--max-old-space-size=1536" [processes]  app = "node dist/index.js gateway --allow-unconfigured --port 3000 --bind lan" [http_service]  internal_port = 3000  force_https = true  auto_stop_machines = false  auto_start_machines = true  min_machines_running = 1  processes = ["app"] [[vm]]  size = "shared-cpu-2x"  memory = "2048mb" [mounts]  source = "openclaw_data"  destination = "/data"
[/code]

L’image Docker OpenClaw utilise `tini` comme point d’entrée. Les commandes de processus Fly remplacent le `CMD` Docker sans remplacer l’`ENTRYPOINT`, donc le processus s’exécute toujours sous `tini`.

**Paramètres clés :**

Paramètre | Pourquoi  
---|---  
`--bind lan` | Lie à `0.0.0.0` afin que le proxy de Fly puisse atteindre le Gateway  
`--allow-unconfigured` | Démarre sans fichier de configuration (vous en créerez un ensuite)  
`internal_port = 3000` | Doit correspondre à `--port 3000` (ou `OPENCLAW_GATEWAY_PORT`) pour les contrôles de santé Fly  
`memory = "2048mb"` | 512 Mo est insuffisant ; 2 Go recommandés  
`OPENCLAW_STATE_DIR = "/data"` | Persiste l’état sur le volume  
* ### Définir les secrets

bashCopy code
[code]
    # Required: Gateway token (for non-loopback binding)fly secrets set OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 32) # Model provider API keysfly secrets set ANTHROPIC_API_KEY=sk-ant-... # Optional: Other providersfly secrets set OPENAI_API_KEY=sk-...fly secrets set GOOGLE_API_KEY=... # Channel tokensfly secrets set DISCORD_BOT_TOKEN=MTQ...
[/code]

**Notes :**

  * Les liaisons non loopback (`--bind lan`) nécessitent un chemin d’authentification Gateway valide. Cet exemple [Fly.io](<http://Fly.io>) utilise `OPENCLAW_GATEWAY_TOKEN`, mais `gateway.auth.password` ou un déploiement `trusted-proxy` non loopback correctement configuré satisfait également l’exigence.
  * Traitez ces jetons comme des mots de passe.
  * **Préférez les variables d’environnement au fichier de configuration** pour toutes les clés d’API et tous les jetons. Cela évite que les secrets se retrouvent dans `openclaw.json`, où ils pourraient être accidentellement exposés ou journalisés.


* ### Déployer

bashCopy code
[code]
    fly deploy
[/code]

Le premier déploiement construit l’image Docker (~2 à 3 minutes). Les déploiements suivants sont plus rapides.

Après le déploiement, vérifiez :

bashCopy code
[code]
    fly statusfly logs
[/code]

Vous devriez voir :

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:3000 (PID xxx)[discord] logged in to discord as xxx
[/code]

* ### Créer le fichier de configuration

Connectez-vous à la machine en SSH pour créer une configuration correcte :

bashCopy code
[code]
    fly ssh console
[/code]

Créez le répertoire et le fichier de configuration :

bashCopy code
[code]
    mkdir -p /datacat > /data/openclaw.json << 'EOF'{  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-opus-4-6",        "fallbacks": ["anthropic/claude-sonnet-4-6", "openai/gpt-5.4"]      },      "maxConcurrent": 4    },    "list": [      {        "id": "main",        "default": true      }    ]  },  "auth": {    "profiles": {      "anthropic:default": { "mode": "token", "provider": "anthropic" },      "openai:default": { "mode": "token", "provider": "openai" }    }  },  "bindings": [    {      "agentId": "main",      "match": { "channel": "discord" }    }  ],  "channels": {    "discord": {      "enabled": true,      "groupPolicy": "allowlist",      "guilds": {        "YOUR_GUILD_ID": {          "channels": { "general": { "allow": true } },          "requireMention": false        }      }    }  },  "gateway": {    "mode": "local",    "bind": "auto",    "controlUi": {      "allowedOrigins": [        "https://my-openclaw.fly.dev",        "http://localhost:3000",        "http://127.0.0.1:3000"      ]    }  },  "meta": {}}EOF
[/code]

**Note :** Avec `OPENCLAW_STATE_DIR=/data`, le chemin de configuration est `/data/openclaw.json`.

**Note :** Remplacez `https://my-openclaw.fly.dev` par l’origine réelle de votre application Fly. Le démarrage du Gateway initialise les origines locales de l’interface de contrôle à partir des valeurs d’exécution `--bind` et `--port`, afin que le premier démarrage puisse continuer avant que la configuration n’existe, mais l’accès via navigateur à travers Fly nécessite toujours que l’origine HTTPS exacte soit listée dans `gateway.controlUi.allowedOrigins`.

**Note :** Le jeton Discord peut provenir de l’une des deux sources suivantes :

  * Variable d’environnement : `DISCORD_BOT_TOKEN` (recommandé pour les secrets)
  * Fichier de configuration : `channels.discord.token`


Si vous utilisez la variable d’environnement, il n’est pas nécessaire d’ajouter le jeton à la configuration. Le Gateway lit automatiquement `DISCORD_BOT_TOKEN`.

Redémarrez pour appliquer :

bashCopy code
[code]
    exitfly machine restart <machine-id>
[/code]

* ### Accéder au Gateway

### Interface de contrôle

Ouvrez dans un navigateur :

bashCopy code
[code]
    fly open
[/code]

Ou visitez `https://my-openclaw.fly.dev/`

Authentifiez-vous avec le secret partagé configuré. Ce guide utilise le jeton Gateway de `OPENCLAW_GATEWAY_TOKEN` ; si vous êtes passé à l’authentification par mot de passe, utilisez plutôt ce mot de passe.

### Journaux

bashCopy code
[code]
    fly logs              # Live logsfly logs --no-tail    # Recent logs
[/code]

### Console SSH

bashCopy code
[code]
    fly ssh console
[/code]

## Dépannage

### « L’application n’écoute pas sur l’adresse attendue »

Le Gateway est lié à `127.0.0.1` au lieu de `0.0.0.0`.

**Correctif :** Ajoutez `--bind lan` à votre commande de processus dans `fly.toml`.

### Échec des contrôles de santé / connexion refusée

Fly ne peut pas atteindre le Gateway sur le port configuré.

**Correctif :** Assurez-vous que `internal_port` correspond au port du Gateway (définissez `--port 3000` ou `OPENCLAW_GATEWAY_PORT=3000`).

### Problèmes de mémoire / OOM

Le conteneur redémarre en boucle ou est tué. Signes : `SIGABRT`, `v8::internal::Runtime_AllocateInYoungGeneration` ou redémarrages silencieux.

**Correctif :** Augmentez la mémoire dans `fly.toml` :

tomlCopy code
[code]
    [[vm]]  memory = "2048mb"
[/code]

Ou mettez à jour une machine existante :

bashCopy code
[code]
    fly machine update <machine-id> --vm-memory 2048 -y
[/code]

**Note :** 512 Mo est insuffisant. 1 Go peut fonctionner, mais peut provoquer un OOM en charge ou avec une journalisation détaillée. **2 Go sont recommandés.**

### Problèmes de verrou du Gateway

Le Gateway refuse de démarrer avec des erreurs « déjà en cours d’exécution ».

Cela se produit lorsque le conteneur redémarre mais que le fichier de verrou PID persiste sur le volume.

**Correctif :** Supprimez le fichier de verrou :

bashCopy code
[code]
    fly ssh console --command "rm -f /data/gateway.*.lock"fly machine restart <machine-id>
[/code]

Le fichier de verrou se trouve à `/data/gateway.*.lock` (pas dans un sous-répertoire).

### La configuration n’est pas lue

`--allow-unconfigured` contourne seulement la garde de démarrage. Il ne crée ni ne répare `/data/openclaw.json`, assurez-vous donc que votre vraie configuration existe et inclut `gateway.mode="local"` lorsque vous voulez un démarrage normal du Gateway local.

Vérifiez que la configuration existe :

bashCopy code
[code]
    fly ssh console --command "cat /data/openclaw.json"
[/code]

### Écrire la configuration via SSH

La commande `fly ssh console -C` ne prend pas en charge la redirection shell. Pour écrire un fichier de configuration :

bashCopy code
[code]
    # Use echo + tee (pipe from local to remote)echo '{"your":"config"}' | fly ssh console -C "tee /data/openclaw.json" # Or use sftpfly sftp shell> put /local/path/config.json /data/openclaw.json
[/code]

**Note :** `fly sftp` peut échouer si le fichier existe déjà. Supprimez-le d’abord :

bashCopy code
[code]
    fly ssh console --command "rm /data/openclaw.json"
[/code]

### L’état ne persiste pas

Si vous perdez les profils d’authentification, l’état des canaux/fournisseurs ou les sessions après un redémarrage, le répertoire d’état écrit dans le système de fichiers du conteneur.

**Correctif :** Assurez-vous que `OPENCLAW_STATE_DIR=/data` est défini dans `fly.toml` et redéployez.

## Mises à jour

bashCopy code
[code]
    # Pull latest changesgit pull # Redeployfly deploy # Check healthfly statusfly logs
[/code]

### Mettre à jour la commande de la machine

Si vous devez changer la commande de démarrage sans redéploiement complet :

bashCopy code
[code]
    # Get machine IDfly machines list # Update commandfly machine update <machine-id> --command "node dist/index.js gateway --port 3000 --bind lan" -y # Or with memory increasefly machine update <machine-id> --vm-memory 2048 --command "node dist/index.js gateway --port 3000 --bind lan" -y
[/code]

**Note :** Après `fly deploy`, la commande de la machine peut revenir à celle définie dans `fly.toml`. Si vous avez effectué des changements manuels, réappliquez-les après le déploiement.

## Déploiement privé (renforcé)

Par défaut, Fly alloue des IP publiques, ce qui rend votre Gateway accessible à `https://your-app.fly.dev`. C’est pratique, mais cela signifie que votre déploiement est découvrable par les scanners Internet (Shodan, Censys, etc.).

Pour un déploiement renforcé avec **aucune exposition publique** , utilisez le modèle privé.

### Quand utiliser un déploiement privé

  * Vous effectuez uniquement des appels/messages **sortants** (aucun Webhook entrant)
  * Vous utilisez des tunnels **ngrok ou Tailscale** pour tous les rappels de Webhook
  * Vous accédez au Gateway via **SSH, proxy ou WireGuard** au lieu d’un navigateur
  * Vous voulez que le déploiement soit **caché des scanners Internet**


### Configuration

Utilisez `deploy/fly.private.toml` au lieu de la configuration standard :

bashCopy code
[code]
    # Deploy with private configfly deploy -c deploy/fly.private.toml
[/code]

Ou convertissez un déploiement existant :

bashCopy code
[code]
    # List current IPsfly ips list -a my-openclaw # Release public IPsfly ips release <public-ipv4> -a my-openclawfly ips release <public-ipv6> -a my-openclaw # Switch to private config so future deploys don't re-allocate public IPs# (remove [http_service] or deploy with the private template)fly deploy -c deploy/fly.private.toml # Allocate private-only IPv6fly ips allocate-v6 --private -a my-openclaw
[/code]

Après cela, `fly ips list` ne devrait afficher qu’une IP de type `private` :

CodeCopy code
[code]
    VERSION  IP                   TYPE             REGIONv6       fdaa:x:x:x:x::x      private          global
[/code]

### Accéder à un déploiement privé

Comme il n’y a pas d’URL publique, utilisez l’une de ces méthodes :

**Option 1 : Proxy local (le plus simple)**

bashCopy code
[code]
    # Forward local port 3000 to the appfly proxy 3000:3000 -a my-openclaw # Then open http://localhost:3000 in browser
[/code]

**Option 2 : VPN WireGuard**

bashCopy code
[code]
    # Create WireGuard config (one-time)fly wireguard create # Import to WireGuard client, then access via internal IPv6# Example: http://[fdaa:x:x:x:x::x]:3000
[/code]

**Option 3 : SSH uniquement**

bashCopy code
[code]
    fly ssh console -a my-openclaw
[/code]

### Webhooks avec un déploiement privé

Si vous avez besoin de callbacks Webhook (Twilio, Telnyx, etc.) sans exposition publique :

  1. **Tunnel ngrok** \- Exécutez ngrok dans le conteneur ou comme sidecar
  2. **Tailscale Funnel** \- Exposez des chemins spécifiques via Tailscale
  3. **Sortant uniquement** \- Certains fournisseurs (Twilio) fonctionnent correctement pour les appels sortants sans Webhook


Exemple de configuration d’appel vocal avec ngrok :

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio",          tunnel: { provider: "ngrok" },          webhookSecurity: {            allowedHosts: ["example.ngrok.app"],          },        },      },    },  },}
[/code]

Le tunnel ngrok s’exécute dans le conteneur et fournit une URL Webhook publique sans exposer l’application Fly elle-même. Définissez `webhookSecurity.allowedHosts` sur le nom d’hôte public du tunnel afin que les en-têtes d’hôte transférés soient acceptés.

### Avantages en matière de sécurité

Aspect | Public | Privé  
---|---|---  
Scanners Internet | Découvrable | Masqué  
Attaques directes | Possibles | Bloquées  
Accès à l’interface de contrôle | Navigateur | Proxy/VPN  
Livraison Webhook | Directe | Via tunnel  
  
## Notes

  * [Fly.io](<http://Fly.io>) utilise une **architecture x86** (pas ARM)
  * Le Dockerfile est compatible avec les deux architectures
  * Pour l’intégration WhatsApp/Telegram, utilisez `fly ssh console`
  * Les données persistantes se trouvent sur le volume à `/data`
  * Signal nécessite Java + signal-cli ; utilisez une image personnalisée et conservez au moins 2 Go de mémoire.


## Coût

Avec la configuration recommandée (`shared-cpu-2x`, 2 Go de RAM) :

  * ~10 à 15 $/mois selon l’utilisation
  * L’offre gratuite inclut une certaine allocation


Consultez la [tarification Fly.io](<https://fly.io/docs/about/pricing/>) pour plus de détails.

## Étapes suivantes

  * Configurer les canaux de messagerie : [Canaux](</fr/channels>)
  * Configurer le Gateway : [Configuration du Gateway](</fr/gateway/configuration>)
  * Maintenir OpenClaw à jour : [Mise à jour](</fr/install/updating>)


## Connexe

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [Hetzner](</fr/install/hetzner>)
  * [Docker](</fr/install/docker>)
  * [Hébergement VPS](</fr/vps>)


Was this useful?YesNo