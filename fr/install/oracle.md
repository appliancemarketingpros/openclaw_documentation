---
title: Oracle Cloud
source_url: https://docs.openclaw.ai/fr/install/oracle
scraped_at: 2026-05-25
---

Exécutez un OpenClaw Gateway persistant sur le niveau ARM **Always Free** d’Oracle Cloud (jusqu’à 4 OCPU, 24 Go de RAM, 200 Go de stockage) sans frais.

## Prérequis

  * Compte Oracle Cloud ([inscription](<https://www.oracle.com/cloud/free/>)) -- consultez le [guide d’inscription communautaire](<https://gist.github.com/rssnyder/51e3cfedd730e7dd5f4a816143b25dbd>) si vous rencontrez des problèmes
  * Compte Tailscale (gratuit sur [tailscale.com](<https://tailscale.com>))
  * Une paire de clés SSH
  * Environ 30 minutes


## Configuration

* ### Créer une instance OCI

  1. Connectez-vous à l’[Oracle Cloud Console](<https://cloud.oracle.com/>).
  2. Accédez à **Compute > Instances > Create Instance**.
  3. Configurez : 
     * **Nom :** `openclaw`
     * **Image :** Ubuntu 24.04 (aarch64)
     * **Forme :** `VM.Standard.A1.Flex` (Ampere ARM)
     * **OCPU :** 2 (ou jusqu’à 4)
     * **Mémoire :** 12 Go (ou jusqu’à 24 Go)
     * **Volume de démarrage :** 50 Go (jusqu’à 200 Go gratuits)
     * **Clé SSH :** ajoutez votre clé publique
  4. Cliquez sur **Create** et notez l’adresse IP publique.


* ### Se connecter et mettre à jour le système

bashCopy code
[code]
    ssh ubuntu@YOUR_PUBLIC_IP sudo apt update && sudo apt upgrade -ysudo apt install -y build-essential
[/code]

`build-essential` est requis pour la compilation ARM de certaines dépendances.

* ### Configurer l’utilisateur et le nom d’hôte

bashCopy code
[code]
    sudo hostnamectl set-hostname openclawsudo passwd ubuntusudo loginctl enable-linger ubuntu
[/code]

L’activation de linger maintient les services utilisateur en cours d’exécution après la déconnexion.

* ### Installer Tailscale

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | shsudo tailscale up --ssh --hostname=openclaw
[/code]

À partir de maintenant, connectez-vous via Tailscale : `ssh ubuntu@openclaw`.

* ### Installer OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bashsource ~/.bashrc
[/code]

Lorsque l’invite « How do you want to hatch your bot? » s’affiche, sélectionnez **Faire cela plus tard**.

* ### Configurer le Gateway

Utilisez l’authentification par jeton avec Tailscale Serve pour un accès distant sécurisé.

bashCopy code
[code]
    openclaw config set gateway.bind loopbackopenclaw config set gateway.auth.mode tokenopenclaw doctor --generate-gateway-tokenopenclaw config set gateway.tailscale.mode serveopenclaw config set gateway.trustedProxies '["127.0.0.1"]' systemctl --user restart openclaw-gateway.service
[/code]

`gateway.trustedProxies=["127.0.0.1"]` ici sert uniquement à la gestion des IP transférées/clients locaux par le proxy local Tailscale Serve. Ce n’est **pas** `gateway.auth.mode: "trusted-proxy"`. Les routes de visualisation des diffs conservent un comportement de fermeture en cas d’échec dans cette configuration : les requêtes brutes du visualiseur vers `127.0.0.1` sans en-têtes de proxy transférés peuvent renvoyer `Diff not found`. Utilisez `mode=file` / `mode=both` pour les pièces jointes, ou activez intentionnellement les visualiseurs distants et définissez `plugins.entries.diffs.config.viewerBaseUrl` (ou transmettez un `baseUrl` de proxy) si vous avez besoin de liens de visualiseur partageables.

* ### Verrouiller la sécurité du VCN

Bloquez tout le trafic sauf Tailscale à la périphérie du réseau :

  1. Accédez à **Networking > Virtual Cloud Networks** dans la console OCI.
  2. Cliquez sur votre VCN, puis sur **Security Lists > Default Security List**.
  3. **Supprimez** toutes les règles d’entrée sauf `0.0.0.0/0 UDP 41641` (Tailscale).
  4. Conservez les règles de sortie par défaut (autoriser tout le trafic sortant).


Cela bloque SSH sur le port 22, HTTP, HTTPS et tout le reste à la périphérie du réseau. À partir de ce point, vous ne pouvez vous connecter que via Tailscale.

* ### Vérifier

bashCopy code
[code]
    openclaw --versionsystemctl --user status openclaw-gateway.servicetailscale serve statuscurl http://localhost:18789
[/code]

Accédez à l’interface de contrôle depuis n’importe quel appareil sur votre tailnet :

CodeCopy code
[code]
    https://openclaw.<tailnet-name>.ts.net/
[/code]

Remplacez `<tailnet-name>` par le nom de votre tailnet (visible dans `tailscale status`).

## Vérifier la posture de sécurité

Avec le VCN verrouillé (seul UDP 41641 ouvert) et le Gateway lié au local loopback, le trafic public est bloqué à la périphérie du réseau et l’accès administrateur est réservé au tailnet. Cela supprime la nécessité de plusieurs étapes traditionnelles de durcissement d’un VPS :

Étape traditionnelle | Nécessaire ? | Pourquoi  
---|---|---  
Pare-feu UFW | Non | Le VCN bloque le trafic avant qu’il n’atteigne l’instance.  
fail2ban | Non | Le port 22 est bloqué au niveau du VCN ; aucune surface de force brute.  
Durcissement de sshd | Non | Tailscale SSH n’utilise pas sshd.  
Désactiver la connexion root | Non | Tailscale authentifie par identité de tailnet, pas par utilisateurs système.  
Authentification SSH par clé seule | Non | Même raison — l’identité de tailnet remplace les clés SSH système.  
Durcissement IPv6 | Généralement non | Dépend des paramètres VCN/sous-réseau ; vérifiez ce qui est réellement attribué/exposé.  
  
Toujours recommandé :

  * `chmod 700 ~/.openclaw` pour restreindre les autorisations des fichiers d’identifiants.
  * `openclaw security audit` pour une vérification de posture propre à OpenClaw.
  * `sudo apt update && sudo apt upgrade` régulièrement pour les correctifs du système d’exploitation.
  * Examinez périodiquement les appareils dans la [console d’administration Tailscale](<https://login.tailscale.com/admin>).


Commandes de vérification rapides :

bashCopy code
[code]
    # Confirm no public ports are listeningsudo ss -tlnp | grep -v '127.0.0.1\|::1' # Verify Tailscale SSH is activetailscale status | grep -q 'offers: ssh' && echo "Tailscale SSH active" # Optional: disable sshd entirely once Tailscale SSH is confirmed workingsudo systemctl disable --now ssh
[/code]

## Notes ARM

Le niveau Always Free est ARM (`aarch64`). La plupart des fonctionnalités d’OpenClaw fonctionnent correctement ; un petit nombre de binaires natifs nécessitent des builds ARM :

  * Node.js, Telegram, WhatsApp (Baileys) : JavaScript pur, aucun problème.
  * La plupart des paquets npm avec du code natif : artefacts `linux-arm64` précompilés disponibles.
  * Assistants CLI facultatifs (par exemple les binaires Go/Rust fournis par des skills) : vérifiez qu’une version `aarch64` / `linux-arm64` existe avant l’installation.


Vérifiez l’architecture avec `uname -m` (doit afficher `aarch64`). Pour les binaires sans build ARM, installez depuis les sources ou ignorez-les.

## Persistance et sauvegardes

L’état d’OpenClaw se trouve sous :

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` par agent, état des canaux/fournisseurs et données de session.
  * `~/.openclaw/workspace/` — l’espace de travail de l’agent ([SOUL.md](<http://SOUL.md>), mémoire, artefacts).


Ces données survivent aux redémarrages. Pour créer un instantané portable :

bashCopy code
[code]
    openclaw backup create
[/code]

## Solution de repli : tunnel SSH

Si Tailscale Serve ne fonctionne pas, utilisez un tunnel SSH depuis votre machine locale :

bashCopy code
[code]
    ssh -L 18789:127.0.0.1:18789 ubuntu@openclaw
[/code]

Ouvrez ensuite `http://localhost:18789`.

## Dépannage

**La création de l’instance échoue (« Out of capacity »)** \-- Les instances ARM du niveau gratuit sont populaires. Essayez un autre domaine de disponibilité ou réessayez pendant les heures creuses.

**Tailscale ne se connecte pas** \-- Exécutez `sudo tailscale up --ssh --hostname=openclaw --reset` pour vous réauthentifier.

**Le Gateway ne démarre pas** \-- Exécutez `openclaw doctor --non-interactive` et consultez les journaux avec `journalctl --user -u openclaw-gateway.service -n 50`.

**Problèmes de binaires ARM** \-- La plupart des paquets npm fonctionnent sur ARM64. Pour les binaires natifs, recherchez des versions `linux-arm64` ou `aarch64`. Vérifiez l’architecture avec `uname -m`.

## Étapes suivantes

  * [Canaux](</fr/channels>) \-- connectez Telegram, WhatsApp, Discord et plus encore
  * [Configuration du Gateway](</fr/gateway/configuration>) \-- toutes les options de configuration
  * [Mise à jour](</fr/install/updating>) \-- maintenez OpenClaw à jour


## Connexe

  * [Vue d’ensemble de l’installation](</fr/install>)
  * [GCP](</fr/install/gcp>)
  * [Hébergement VPS](</fr/vps>)


Was this useful?YesNo