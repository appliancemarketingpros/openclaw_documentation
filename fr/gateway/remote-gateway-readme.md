---
title: Configuration du Gateway distant
source_url: https://docs.openclaw.ai/fr/gateway/remote-gateway-readme
scraped_at: 2026-05-25
---

> Ce contenu a été fusionné dans [Accès à distance](</fr/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>). Consultez cette page pour le guide actuel.

# Exécuter OpenClaw.app avec un Gateway distant

OpenClaw.app utilise un tunnel SSH pour se connecter à un Gateway distant. Ce guide vous montre comment le configurer.

## Vue d’ensemble
[code] 
    flowchart TB
        subgraph Client["Client Machine"]
            direction TB
            A["OpenClaw.app"]
            B["ws://127.0.0.1:18789\n(local port)"]
            T["SSH Tunnel"]
    
            A --> B
            B --> T
        end
        subgraph Remote["Remote Machine"]
            direction TB
            C["Gateway WebSocket"]
            D["ws://127.0.0.1:18789"]
    
            C --> D
        end
        T --> C
[/code]

## Configuration rapide

### Étape 1 : ajouter la configuration SSH

Modifiez `~/.ssh/config` et ajoutez :

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # e.g., 172.27.187.184    User &lt;REMOTE_USER&gt;            # e.g., jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

Remplacez `&lt;REMOTE_IP&gt;` et `&lt;REMOTE_USER&gt;` par vos valeurs.

### Étape 2 : copier la clé SSH

Copiez votre clé publique sur la machine distante (saisissez le mot de passe une fois) :

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### Étape 3 : configurer l’authentification du Gateway distant

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

Utilisez plutôt `gateway.remote.password` si votre Gateway distant utilise une authentification par mot de passe. `OPENCLAW_GATEWAY_TOKEN` reste valide comme remplacement au niveau du shell, mais la configuration durable du client distant est `gateway.remote.token` / `gateway.remote.password`.

### Étape 4 : démarrer le tunnel SSH

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### Étape 5 : redémarrer OpenClaw.app

bashCopy code
[code]
    # Quit OpenClaw.app (⌘Q), then reopen:open /path/to/OpenClaw.app
[/code]

L’application se connectera maintenant au Gateway distant via le tunnel SSH.

* * *

## Démarrage automatique du tunnel à la connexion

Pour que le tunnel SSH démarre automatiquement lorsque vous vous connectez, créez un Launch Agent.

### Créer le fichier PLIST

Enregistrez ceci sous `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist` :

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### Charger le Launch Agent

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

Le tunnel va maintenant :

  * Démarrer automatiquement lorsque vous vous connectez
  * Redémarrer s’il plante
  * Continuer à s’exécuter en arrière-plan


Note héritée : supprimez tout LaunchAgent `com.openclaw.ssh-tunnel` restant, s’il est présent.

* * *

## Dépannage

**Vérifier si le tunnel est en cours d’exécution :**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**Redémarrer le tunnel :**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**Arrêter le tunnel :**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## Fonctionnement

Composant | Rôle  
---|---  
`LocalForward 18789 127.0.0.1:18789` | Transfère le port local 18789 vers le port distant 18789  
`ssh -N` | SSH sans exécuter de commandes distantes (transfert de port uniquement)  
`KeepAlive` | Redémarre automatiquement le tunnel s’il plante  
`RunAtLoad` | Démarre le tunnel lorsque l’agent se charge  
  
OpenClaw.app se connecte à `ws://127.0.0.1:18789` sur votre machine cliente. Le tunnel SSH transfère cette connexion vers le port 18789 sur la machine distante où le Gateway est en cours d’exécution.

## Connexe

  * [Accès à distance](</fr/gateway/remote>)
  * [Tailscale](</fr/gateway/tailscale>)


Was this useful?YesNo