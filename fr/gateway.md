---
title: Guide d’exploitation du Gateway
source_url: https://docs.openclaw.ai/fr/gateway
scraped_at: 2026-05-25
---

Utilisez cette page pour le démarrage du jour 1 et les opérations du jour 2 du service Gateway.

[**Dépannage approfondi** Diagnostics orientés symptômes avec des séquences de commandes exactes et des signatures de journaux. ](</fr/gateway/troubleshooting>) [**Configuration** Guide de configuration orienté tâches + référence de configuration complète. ](</fr/gateway/configuration>) [**Gestion des secrets** Contrat SecretRef, comportement des instantanés d’exécution et opérations de migration/rechargement. ](</fr/gateway/secrets>) [**Contrat de plan des secrets** Règles exactes cible/chemin de `secrets apply` et comportement des profils d’authentification par référence uniquement. ](</fr/gateway/secrets-plan-contract>)

## Démarrage local en 5 minutes

* ### Démarrer le Gateway

bashCopy code
[code]
    openclaw gateway --port 18789# debug/trace mirrored to stdioopenclaw gateway --port 18789 --verbose# force-kill listener on selected port, then startopenclaw gateway --force
[/code]

* ### Vérifier l’état du service

bashCopy code
[code]
    openclaw gateway statusopenclaw statusopenclaw logs --follow
[/code]

Base saine : `Runtime: running`, `Connectivity probe: ok` et `Capability: ...` correspondant à ce que vous attendez. Utilisez `openclaw gateway status --require-rpc` lorsque vous avez besoin d’une preuve RPC avec périmètre de lecture, et pas seulement d’une joignabilité.

* ### Valider la disponibilité des canaux

bashCopy code
[code]
    openclaw channels status --probe
[/code]

Avec un Gateway joignable, cela exécute des sondes de canaux en direct par compte et des audits facultatifs. Si le Gateway est injoignable, la CLI se replie sur des résumés de canaux fondés uniquement sur la configuration au lieu de la sortie de sonde en direct.

## Modèle d’exécution

  * Un processus toujours actif pour le routage, le plan de contrôle et les connexions de canaux.
  * Port multiplexé unique pour : 
    * Contrôle/RPC WebSocket
    * API HTTP, compatibles OpenAI (`/v1/models`, `/v1/embeddings`, `/v1/chat/completions`, `/v1/responses`, `/tools/invoke`)
    * Interface de contrôle et hooks
  * Mode de liaison par défaut : `loopback`.
  * L’authentification est requise par défaut. Les configurations à secret partagé utilisent `gateway.auth.token` / `gateway.auth.password` (ou `OPENCLAW_GATEWAY_TOKEN` / `OPENCLAW_GATEWAY_PASSWORD`), et les configurations de proxy inverse non-loopback peuvent utiliser `gateway.auth.mode: "trusted-proxy"`.


## Points de terminaison compatibles OpenAI

La surface de compatibilité la plus utile d’OpenClaw est désormais :

  * `GET /v1/models`
  * `GET /v1/models/{id}`
  * `POST /v1/embeddings`
  * `POST /v1/chat/completions`
  * `POST /v1/responses`


Pourquoi cet ensemble est important :

  * La plupart des intégrations Open WebUI, LobeChat et LibreChat sondent d’abord `/v1/models`.
  * De nombreux pipelines RAG et de mémoire attendent `/v1/embeddings`.
  * Les clients natifs pour agents préfèrent de plus en plus `/v1/responses`.


Note de planification :

  * `/v1/models` est pensé d’abord pour les agents : il renvoie `openclaw`, `openclaw/default` et `openclaw/<agentId>`.
  * `openclaw/default` est l’alias stable qui correspond toujours à l’agent par défaut configuré.
  * Utilisez `x-openclaw-model` lorsque vous voulez une substitution du fournisseur/modèle backend ; sinon, la configuration normale du modèle et des embeddings de l’agent sélectionné reste aux commandes.


Tout cela s’exécute sur le port principal du Gateway et utilise la même frontière d’authentification opérateur de confiance que le reste de l’API HTTP du Gateway.

### Précédence du port et de la liaison

Paramètre | Ordre de résolution  
---|---  
Port Gateway | `--port` → `OPENCLAW_GATEWAY_PORT` → `gateway.port` → `18789`  
Mode de liaison | CLI/override → `gateway.bind` → `loopback`  
  
Les services Gateway installés enregistrent le `--port` résolu dans les métadonnées du superviseur. Après avoir modifié `gateway.port`, exécutez `openclaw doctor --fix` ou `openclaw gateway install --force` afin que launchd/systemd/schtasks démarre le processus sur le nouveau port.

Au démarrage, le Gateway utilise le même port effectif et la même liaison lorsqu’il initialise les origines locales de l’interface de contrôle pour les liaisons non-loopback. Par exemple, `--bind lan --port 3000` initialise `http://localhost:3000` et `http://127.0.0.1:3000` avant l’exécution de la validation d’exécution. Ajoutez explicitement toutes les origines de navigateurs distants, comme les URL de proxy HTTPS, à `gateway.controlUi.allowedOrigins`.

### Modes de rechargement à chaud

`gateway.reload.mode` | Comportement  
---|---  
`off` | Aucun rechargement de configuration  
`hot` | Applique uniquement les changements sûrs à chaud  
`restart` | Redémarre pour les changements nécessitant un rechargement  
`hybrid` (par défaut) | Applique à chaud si sûr, redémarre si nécessaire  
  
## Jeu de commandes opérateur

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway status --deep   # adds a system-level service scanopenclaw gateway status --jsonopenclaw gateway installopenclaw gateway restartopenclaw gateway stopopenclaw secrets reloadopenclaw logs --followopenclaw doctor
[/code]

`gateway status --deep` sert à la découverte supplémentaire des services (LaunchDaemons/unités système systemd/schtasks), pas à une sonde de santé RPC plus approfondie.

## Gateways multiples (même hôte)

La plupart des installations devraient exécuter un Gateway par machine. Un seul Gateway peut héberger plusieurs agents et canaux.

Vous n’avez besoin de plusieurs Gateways que si vous voulez intentionnellement de l’isolation ou un bot de secours.

Vérifications utiles :

bashCopy code
[code]
    openclaw gateway status --deepopenclaw gateway probe
[/code]

À quoi s’attendre :

  * `gateway status --deep` peut signaler `Other gateway-like services detected (best effort)` et afficher des conseils de nettoyage lorsque d’anciennes installations launchd/systemd/schtasks sont encore présentes.
  * `gateway probe` peut avertir à propos de `multiple reachable gateways` lorsque plusieurs cibles répondent.
  * Si c’est intentionnel, isolez les ports, la configuration/l’état et les racines d’espaces de travail par Gateway.


Liste de contrôle par instance :

  * `gateway.port` unique
  * `OPENCLAW_CONFIG_PATH` unique
  * `OPENCLAW_STATE_DIR` unique
  * `agents.defaults.workspace` unique


Exemple :

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/a.json OPENCLAW_STATE_DIR=~/.openclaw-a openclaw gateway --port 19001OPENCLAW_CONFIG_PATH=~/.openclaw/b.json OPENCLAW_STATE_DIR=~/.openclaw-b openclaw gateway --port 19002
[/code]

Configuration détaillée : [/gateway/multiple-gateways](</fr/gateway/multiple-gateways>).

## Accès distant

Préféré : Tailscale/VPN. Solution de repli : tunnel SSH.

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@host
[/code]

Connectez ensuite les clients localement à `ws://127.0.0.1:18789`.

Voir : [Gateway distant](</fr/gateway/remote>), [Authentification](</fr/gateway/authentication>), [Tailscale](</fr/gateway/tailscale>).

## Supervision et cycle de vie du service

Utilisez des exécutions supervisées pour une fiabilité proche de la production.

### macOS (launchd)

bashCopy code
[code]
    openclaw gateway installopenclaw gateway statusopenclaw gateway restartopenclaw gateway stop
[/code]

Utilisez `openclaw gateway restart` pour les redémarrages. N’enchaînez pas `openclaw gateway stop` et `openclaw gateway start` comme substitut de redémarrage.

Sur macOS, `gateway stop` utilise `launchctl bootout` par défaut — cela retire le LaunchAgent de la session de démarrage actuelle sans persister de désactivation, de sorte que la récupération automatique KeepAlive fonctionne toujours après des plantages inattendus et que `gateway start` le réactive proprement. Pour supprimer durablement la relance automatique entre les redémarrages, passez `--disable` : `openclaw gateway stop --disable`.

Les libellés LaunchAgent sont `ai.openclaw.gateway` (par défaut) ou `ai.openclaw.<profile>` (profil nommé). `openclaw doctor` audite et répare la dérive de configuration du service.

### Linux (systemd utilisateur)

bashCopy code
[code]
    openclaw gateway installsystemctl --user enable --now openclaw-gateway[-<profile>].serviceopenclaw gateway status
[/code]

Pour la persistance après déconnexion, activez le lingering :

bashCopy code
[code]
    sudo loginctl enable-linger <user>
[/code]

Exemple manuel d’unité utilisateur lorsque vous avez besoin d’un chemin d’installation personnalisé :

iniCopy code
[code]
    [Unit]Description=OpenClaw GatewayAfter=network-online.targetWants=network-online.target [Service]ExecStart=/usr/local/bin/openclaw gateway --port 18789Restart=alwaysRestartSec=5TimeoutStopSec=30TimeoutStartSec=30SuccessExitStatus=0 143KillMode=control-group [Install]WantedBy=default.target
[/code]

### Windows (natif)

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --jsonopenclaw gateway restartopenclaw gateway stop
[/code]

Le démarrage géré Windows natif utilise une tâche planifiée nommée `OpenClaw Gateway` (ou `OpenClaw Gateway (<profile>)` pour les profils nommés). Si la création de la tâche planifiée est refusée, OpenClaw se replie sur un lanceur par utilisateur dans le dossier de démarrage qui pointe vers `gateway.cmd` dans le répertoire d’état.

### Linux (service système)

Utilisez une unité système pour les hôtes multi-utilisateurs/toujours actifs.

bashCopy code
[code]
    sudo systemctl daemon-reloadsudo systemctl enable --now openclaw-gateway[-<profile>].service
[/code]

Utilisez le même corps de service que l’unité utilisateur, mais installez-le sous `/etc/systemd/system/openclaw-gateway[-<profile>].service` et ajustez `ExecStart=` si votre binaire `openclaw` se trouve ailleurs.

Ne laissez pas aussi `openclaw doctor --fix` installer un service Gateway au niveau utilisateur pour le même profil/port. Doctor refuse cette installation automatique lorsqu’il trouve un service Gateway OpenClaw au niveau système ; utilisez `OPENCLAW_SERVICE_REPAIR_POLICY=external` lorsque l’unité système possède le cycle de vie.

## Chemin rapide du profil dev

bashCopy code
[code]
    openclaw --dev setupopenclaw --dev gateway --allow-unconfiguredopenclaw --dev status
[/code]

Les valeurs par défaut incluent une configuration/un état isolés et le port Gateway de base `19001`.

## Référence rapide du protocole (vue opérateur)

  * La première trame client doit être `connect`.
  * Le Gateway renvoie l’instantané `hello-ok` (`presence`, `health`, `stateVersion`, `uptimeMs`, limites/politique).
  * `hello-ok.features.methods` / `events` sont une liste de découverte prudente, pas un dump généré de toutes les routes d’aide appelables.
  * Requêtes : `req(method, params)` → `res(ok/payload|error)`.
  * Les événements courants incluent `connect.challenge`, `agent`, `chat`, `session.message`, `session.tool`, `sessions.changed`, `presence`, `tick`, `health`, `heartbeat`, les événements de cycle de vie d’appairage/approbation et `shutdown`.


Les exécutions d’agents se font en deux étapes :

  1. Accusé d’acceptation immédiat (`status:"accepted"`)
  2. Réponse finale de complétion (`status:"ok"|"error"`), avec des événements `agent` diffusés entre les deux.


Voir la documentation complète du protocole : [Protocole Gateway](</fr/gateway/protocol>).

## Contrôles opérationnels

### Vivacité

  * Ouvrir WS et envoyer `connect`.
  * Attendre une réponse `hello-ok` avec instantané.


### Disponibilité

bashCopy code
[code]
    openclaw gateway statusopenclaw channels status --probeopenclaw health
[/code]

### Récupération des lacunes

Les événements ne sont pas rejoués. En cas de lacunes de séquence, actualisez l’état (`health`, `system-presence`) avant de continuer.

## Signatures de défaillance courantes

Signature | Problème probable  
---|---  
`refusing to bind gateway ... without auth` | Liaison non-loopback sans chemin d’authentification de gateway valide  
`another gateway instance is already listening` / `EADDRINUSE` | Conflit de port  
`Gateway start blocked: set gateway.mode=local` | Configuration définie en mode distant, ou horodatage du mode local absent d’une configuration endommagée  
`unauthorized` pendant la connexion | Incompatibilité d’authentification entre le client et le gateway  
  
Pour des procédures de diagnostic complètes, utilisez [Dépannage du Gateway](</fr/gateway/troubleshooting>).

## Garanties de sécurité

  * Les clients du protocole Gateway échouent rapidement lorsque le Gateway est indisponible (pas de repli implicite vers un canal direct).
  * Les premières trames invalides ou non connectées sont rejetées et fermées.
  * L’arrêt gracieux émet l’événement `shutdown` avant la fermeture du socket.


* * *

Associé :

  * [Dépannage](</fr/gateway/troubleshooting>)
  * [Processus en arrière-plan](</fr/gateway/background-process>)
  * [Configuration](</fr/gateway/configuration>)
  * [Santé](</fr/gateway/health>)
  * [Doctor](</fr/gateway/doctor>)
  * [Authentification](</fr/gateway/authentication>)


## Associé

  * [Configuration](</fr/gateway/configuration>)
  * [Dépannage du Gateway](</fr/gateway/troubleshooting>)
  * [Accès distant](</fr/gateway/remote>)
  * [Gestion des secrets](</fr/gateway/secrets>)


Was this useful?YesNo