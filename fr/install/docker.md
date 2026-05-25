---
title: Docker
source_url: https://docs.openclaw.ai/fr/install/docker
scraped_at: 2026-05-25
---

Docker est **facultatif**. Utilisez-le uniquement si vous voulez un Gateway conteneurisé ou valider le flux Docker.

## Docker est-il adapté à mon cas ?

  * **Oui** : vous voulez un environnement Gateway isolé et jetable, ou exécuter OpenClaw sur un hôte sans installations locales.
  * **Non** : vous l’exécutez sur votre propre machine et voulez simplement la boucle de développement la plus rapide. Utilisez plutôt le flux d’installation normal.
  * **Remarque sur le sandboxing** : le backend de sandbox par défaut utilise Docker lorsque le sandboxing est activé, mais le sandboxing est désactivé par défaut et n’exige **pas** que l’ensemble du Gateway s’exécute dans Docker. Les backends de sandbox SSH et OpenShell sont également disponibles. Voir [Sandboxing](</fr/gateway/sandboxing>).


## Prérequis

  * Docker Desktop (ou Docker Engine) + Docker Compose v2
  * Au moins 2 Go de RAM pour la construction de l’image (`pnpm install` peut être arrêté pour cause d’OOM sur les hôtes de 1 Go avec le code de sortie 137)
  * Suffisamment d’espace disque pour les images et les journaux
  * En cas d’exécution sur un VPS/hôte public, consultez [Renforcement de la sécurité pour l’exposition réseau](</fr/gateway/security>), en particulier la politique de pare-feu Docker `DOCKER-USER`.


## Gateway conteneurisé

* ### Build the image

Depuis la racine du dépôt, exécutez le script de configuration :

bashCopy code
[code]
    ./scripts/docker/setup.sh
[/code]

Cela construit l’image Gateway localement. Pour utiliser plutôt une image préconstruite :

bashCopy code
[code]
    export OPENCLAW_IMAGE="ghcr.io/openclaw/openclaw:latest"./scripts/docker/setup.sh
[/code]

Les images préconstruites sont publiées dans le [GitHub Container Registry](<https://github.com/openclaw/openclaw/pkgs/container/openclaw>). Tags courants : `main`, `latest`, `<version>` (par exemple `2026.2.26`).

* ### Complete onboarding

Le script de configuration exécute automatiquement l’onboarding. Il va :

  * demander les clés d’API des fournisseurs
  * générer un jeton Gateway et l’écrire dans `.env`
  * créer le répertoire de clé secrète du profil d’authentification
  * démarrer le Gateway via Docker Compose


Pendant la configuration, l’onboarding avant démarrage et les écritures de configuration passent directement par `openclaw-gateway`. `openclaw-cli` sert aux commandes que vous exécutez après que le conteneur Gateway existe déjà.

* ### Open the Control UI

Ouvrez `http://127.0.0.1:18789/` dans votre navigateur et collez le secret partagé configuré dans Paramètres. Le script de configuration écrit un jeton dans `.env` par défaut ; si vous passez la configuration du conteneur à l’authentification par mot de passe, utilisez plutôt ce mot de passe.

Besoin de retrouver l’URL ?

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-open
[/code]

* ### Configure channels (optional)

Utilisez le conteneur CLI pour ajouter des canaux de messagerie :

bashCopy code
[code]
    # WhatsApp (QR)docker compose run --rm openclaw-cli channels login # Telegramdocker compose run --rm openclaw-cli channels add --channel telegram --token "<token>" # Discorddocker compose run --rm openclaw-cli channels add --channel discord --token "<token>"
[/code]

Docs : [WhatsApp](</fr/channels/whatsapp>), [Telegram](</fr/channels/telegram>), [Discord](</fr/channels/discord>)

### Flux manuel

Si vous préférez exécuter chaque étape vous-même au lieu d’utiliser le script de configuration :

bashCopy code
[code]
    docker build -t openclaw:local -f Dockerfile .docker compose run --rm --no-deps --entrypoint node openclaw-gateway \  dist/index.js onboard --mode local --no-install-daemondocker compose run --rm --no-deps --entrypoint node openclaw-gateway \  dist/index.js config set --batch-json '[{"path":"gateway.mode","value":"local"},{"path":"gateway.bind","value":"lan"},{"path":"gateway.controlUi.allowedOrigins","value":["http://localhost:18789","http://127.0.0.1:18789"]}]'docker compose up -d openclaw-gateway
[/code]

### Variables d’environnement

Le script de configuration accepte ces variables d’environnement facultatives :

Variable | Objectif  
---|---  
`OPENCLAW_IMAGE` | Utiliser une image distante au lieu de construire localement  
`OPENCLAW_DOCKER_APT_PACKAGES` | Installer des paquets apt supplémentaires pendant la construction (séparés par des espaces)  
`OPENCLAW_EXTENSIONS` | Inclure les assistants de Plugin groupés sélectionnés au moment de la construction  
`OPENCLAW_EXTRA_MOUNTS` | Montages bind hôte supplémentaires (`source:target[:opts]` séparés par des virgules)  
`OPENCLAW_HOME_VOLUME` | Persister `/home/node` dans un volume Docker nommé  
`OPENCLAW_SANDBOX` | Activer l’amorçage du sandbox (`1`, `true`, `yes`, `on`)  
`OPENCLAW_SKIP_ONBOARDING` | Ignorer l’étape d’onboarding interactive (`1`, `true`, `yes`, `on`)  
`OPENCLAW_DOCKER_SOCKET` | Remplacer le chemin du socket Docker  
`OPENCLAW_DISABLE_BONJOUR` | Désactiver l’annonce Bonjour/mDNS (par défaut `1` pour Docker)  
`OPENCLAW_DISABLE_BUNDLED_SOURCE_OVERLAYS` | Désactiver les superpositions bind-mount de source de Plugin groupé  
`OTEL_EXPORTER_OTLP_ENDPOINT` | Point de terminaison collecteur OTLP/HTTP partagé pour l’export OpenTelemetry  
`OTEL_EXPORTER_OTLP_*_ENDPOINT` | Points de terminaison OTLP propres au signal pour les traces, métriques ou journaux  
`OTEL_EXPORTER_OTLP_PROTOCOL` | Remplacement du protocole OTLP. Seul `http/protobuf` est pris en charge aujourd’hui  
`OTEL_SERVICE_NAME` | Nom du service utilisé pour les ressources OpenTelemetry  
`OTEL_SEMCONV_STABILITY_OPT_IN` | Activer les derniers attributs sémantiques GenAI expérimentaux  
`OPENCLAW_OTEL_PRELOADED` | Ignorer le démarrage d’un second SDK OpenTelemetry lorsqu’un est préchargé  
  
Les mainteneurs peuvent tester la source de Plugin groupé avec une image empaquetée en montant un répertoire source de Plugin par-dessus son chemin source empaqueté, par exemple `OPENCLAW_EXTRA_MOUNTS=/path/to/fork/extensions/synology-chat:/app/extensions/synology-chat:ro`. Ce répertoire source monté remplace le bundle compilé correspondant `/app/dist/extensions/synology-chat` pour le même identifiant de Plugin.

### Observabilité

L’export OpenTelemetry sort du conteneur Gateway vers votre collecteur OTLP. Il ne nécessite pas de port Docker publié. Si vous construisez l’image localement et voulez que l’exportateur OpenTelemetry groupé soit disponible dans l’image, incluez ses dépendances d’exécution :

bashCopy code
[code]
    export OPENCLAW_EXTENSIONS="diagnostics-otel"export OTEL_EXPORTER_OTLP_ENDPOINT="http://otel-collector:4318"export OTEL_SERVICE_NAME="openclaw-gateway"./scripts/docker/setup.sh
[/code]

Installez le Plugin officiel `@openclaw/diagnostics-otel` depuis ClawHub dans les installations Docker empaquetées avant d’activer l’export. Les images personnalisées construites depuis la source peuvent toujours inclure la source de Plugin locale avec `OPENCLAW_EXTENSIONS=diagnostics-otel`. Pour activer l’export, autorisez et activez le Plugin `diagnostics-otel` dans la configuration, puis définissez `diagnostics.otel.enabled=true` ou utilisez l’exemple de configuration dans [Export OpenTelemetry](</fr/gateway/opentelemetry>). Les en-têtes d’authentification du collecteur sont configurés via `diagnostics.otel.headers`, pas via les variables d’environnement Docker.

Les métriques Prometheus utilisent le port Gateway déjà publié. Installez `clawhub:@openclaw/diagnostics-prometheus`, activez le Plugin `diagnostics-prometheus`, puis collectez :

textCopy code
[code]
    http://<gateway-host>:18789/api/diagnostics/prometheus
[/code]

La route est protégée par l’authentification du Gateway. N’exposez pas de port `/metrics` public séparé ni de chemin de proxy inverse non authentifié. Voir [Métriques Prometheus](</fr/gateway/prometheus>).

### Vérifications de santé

Points de terminaison de sonde du conteneur (aucune authentification requise) :

bashCopy code
[code]
    curl -fsS http://127.0.0.1:18789/healthz   # livenesscurl -fsS http://127.0.0.1:18789/readyz     # readiness
[/code]

L’image Docker inclut un `HEALTHCHECK` intégré qui interroge `/healthz`. Si les vérifications continuent d’échouer, Docker marque le conteneur comme `unhealthy` et les systèmes d’orchestration peuvent le redémarrer ou le remplacer.

Instantané de santé approfondi authentifié :

bashCopy code
[code]
    docker compose exec openclaw-gateway node dist/index.js health --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

### LAN vs loopback

`scripts/docker/setup.sh` définit par défaut `OPENCLAW_GATEWAY_BIND=lan` afin que l’accès hôte à `http://127.0.0.1:18789` fonctionne avec la publication de port Docker.

  * `lan` (par défaut) : le navigateur hôte et la CLI hôte peuvent atteindre le port Gateway publié.
  * `loopback` : seuls les processus à l’intérieur de l’espace de noms réseau du conteneur peuvent atteindre directement le Gateway.


### Fournisseurs locaux de l’hôte

Quand OpenClaw s’exécute dans Docker, `127.0.0.1` à l’intérieur du conteneur est le conteneur lui-même, pas votre machine hôte. Utilisez `host.docker.internal` pour les fournisseurs d’IA qui s’exécutent sur l’hôte :

Fournisseur | URL hôte par défaut | URL de configuration Docker  
---|---|---  
LM Studio | `http://127.0.0.1:1234` | `http://host.docker.internal:1234`  
Ollama | `http://127.0.0.1:11434` | `http://host.docker.internal:11434`  
  
La configuration Docker groupée utilise ces URL hôte comme valeurs par défaut d’onboarding pour LM Studio et Ollama, et `docker-compose.yml` mappe `host.docker.internal` vers le Gateway hôte de Docker pour Docker Engine sous Linux. Docker Desktop fournit déjà le même nom d’hôte sous macOS et Windows.

Les services hôtes doivent aussi écouter sur une adresse joignable depuis Docker :

bashCopy code
[code]
    lms server start --port 1234 --bind 0.0.0.0OLLAMA_HOST=0.0.0.0:11434 ollama serve
[/code]

Si vous utilisez votre propre fichier Compose ou commande `docker run`, ajoutez vous-même le même mappage d’hôte, par exemple `--add-host=host.docker.internal:host-gateway`.

### Bonjour / mDNS

Le réseau bridge Docker ne transfère généralement pas le multicast Bonjour/mDNS (`224.0.0.251:5353`) de façon fiable. La configuration Compose groupée définit donc par défaut `OPENCLAW_DISABLE_BONJOUR=1` afin que le Gateway ne boucle pas en panne ou ne redémarre pas sans cesse l’annonce lorsque le bridge abandonne le trafic multicast.

Utilisez l’URL Gateway publiée, Tailscale ou DNS-SD à large portée pour les hôtes Docker. Définissez `OPENCLAW_DISABLE_BONJOUR=0` uniquement lors d’une exécution avec le réseau hôte, macvlan ou un autre réseau où le multicast mDNS est connu pour fonctionner.

Pour les pièges et le dépannage, voir [Découverte Bonjour](</fr/gateway/bonjour>).

### Stockage et persistance

Docker Compose monte en bind `OPENCLAW_CONFIG_DIR` vers `/home/node/.openclaw`, `OPENCLAW_WORKSPACE_DIR` vers `/home/node/.openclaw/workspace`, et `OPENCLAW_AUTH_PROFILE_SECRET_DIR` vers `/home/node/.config/openclaw`, afin que ces chemins survivent au remplacement du conteneur. Lorsqu’une variable n’est pas définie, le `docker-compose.yml` groupé se replie sous `${HOME}`, ou `/tmp` lorsque `HOME` lui-même est également absent. Cela évite que `docker compose up` émette une spécification de volume à source vide dans les environnements nus.

Ce répertoire de configuration monté est l’endroit où OpenClaw conserve :

  * `openclaw.json` pour la configuration du comportement
  * `agents/<agentId>/agent/auth-profiles.json` pour l’authentification OAuth/clé d’API fournisseur stockée
  * `.env` pour les secrets d’exécution fournis par l’environnement tels que `OPENCLAW_GATEWAY_TOKEN`


Le répertoire de clé secrète du profil d’authentification stocke la clé de chiffrement locale utilisée pour le matériel de jeton de profil d’authentification basé sur OAuth. Conservez-le avec l’état de votre hôte Docker, mais séparé de `OPENCLAW_CONFIG_DIR`.

Les plugins téléchargeables installés stockent leur état de package sous le répertoire personnel OpenClaw monté, ce qui permet aux enregistrements d'installation de plugins et aux racines de packages de survivre au remplacement du conteneur. Le démarrage du Gateway ne génère pas d'arborescences de dépendances pour les plugins groupés.

Pour tous les détails de persistance sur les déploiements de VM, consultez [Docker VM Runtime - Ce qui persiste et où](</fr/install/docker-vm-runtime#what-persists-where>).

**Points chauds de croissance du disque :** surveillez `media/`, les fichiers JSONL de session, `cron/runs/*.jsonl`, les racines de packages de plugins installés et les journaux de fichiers rotatifs sous `/tmp/openclaw/`.

### Assistants shell (facultatif)

Pour faciliter la gestion quotidienne de Docker, installez `ClawDock` :

bashCopy code
[code]
    mkdir -p ~/.clawdock && curl -sL https://raw.githubusercontent.com/openclaw/openclaw/main/scripts/clawdock/clawdock-helpers.sh -o ~/.clawdock/clawdock-helpers.shecho 'source ~/.clawdock/clawdock-helpers.sh' >> ~/.zshrc && source ~/.zshrc
[/code]

Si vous avez installé ClawDock depuis l'ancien chemin brut `scripts/shell-helpers/clawdock-helpers.sh`, relancez la commande d'installation ci-dessus afin que votre fichier d'assistance local suive le nouvel emplacement.

Utilisez ensuite `clawdock-start`, `clawdock-stop`, `clawdock-dashboard`, etc. Exécutez `clawdock-help` pour afficher toutes les commandes. Consultez [ClawDock](</fr/install/clawdock>) pour le guide complet de l'assistant.

Activer le bac à sable d'agent pour le Gateway Docker bashCopy code
[code]
    export OPENCLAW_SANDBOX=1./scripts/docker/setup.sh
[/code]

Chemin de socket personnalisé (par exemple Docker rootless) :

bashCopy code
[code]
    export OPENCLAW_SANDBOX=1export OPENCLAW_DOCKER_SOCKET=/run/user/1000/docker.sock./scripts/docker/setup.sh
[/code]

Le script monte `docker.sock` uniquement après validation des prérequis du bac à sable. Si la configuration du bac à sable ne peut pas se terminer, le script réinitialise `agents.defaults.sandbox.mode` à `off`. Les tours en mode code de Codex restent limités au `workspace-write` de Codex pendant que le bac à sable OpenClaw est actif ; ne montez pas le socket Docker de l'hôte dans les conteneurs de bac à sable des agents.

Automatisation / CI (non interactif)

Désactivez l'allocation pseudo-TTY de Compose avec `-T` :

bashCopy code
[code]
    docker compose run -T --rm openclaw-cli gateway probedocker compose run -T --rm openclaw-cli devices list --json
[/code]

Note de sécurité sur le réseau partagé

`openclaw-cli` utilise `network_mode: "service:openclaw-gateway"` afin que les commandes CLI puissent joindre le Gateway via `127.0.0.1`. Considérez cela comme une frontière de confiance partagée. La configuration Compose retire `NET_RAW`/`NET_ADMIN` et active `no-new-privileges` sur `openclaw-gateway` comme sur `openclaw-cli`.

Échecs DNS de Docker Desktop dans openclaw-cli

Certaines configurations Docker Desktop échouent à résoudre le DNS depuis le sidecar `openclaw-cli` en réseau partagé après la suppression de `NET_RAW`, ce qui apparaît sous forme de `EAI_AGAIN` pendant les commandes reposant sur npm, comme `openclaw plugins install`. Conservez le fichier Compose renforcé par défaut pour le fonctionnement normal du Gateway. La surcharge locale ci-dessous assouplit la posture de sécurité du conteneur CLI en restaurant les capacités par défaut de Docker ; utilisez-la donc uniquement pour la commande CLI ponctuelle qui a besoin d'accéder au registre de packages, et non comme invocation Compose par défaut :

bashCopy code
[code]
    printf '%s\n' \  'services:' \  '  openclaw-cli:' \  '    cap_drop: !reset []' \  > docker-compose.cli-no-dropped-caps.local.yml docker compose -f docker-compose.yml -f docker-compose.cli-no-dropped-caps.local.yml run --rm openclaw-cli plugins install <package>
[/code]

Si vous avez déjà créé un conteneur `openclaw-cli` à longue durée de vie, recréez-le avec la même surcharge. `docker compose exec` et `docker exec` ne peuvent pas modifier les capacités Linux d'un conteneur déjà créé.

Autorisations et EACCES

L'image s'exécute en tant que `node` (uid 1000). Si vous voyez des erreurs d'autorisation sur `/home/node/.openclaw`, assurez-vous que vos montages liés hôtes appartiennent à l'uid 1000 :

bashCopy code
[code]
    sudo chown -R 1000:1000 /path/to/openclaw-config /path/to/openclaw-workspace
[/code]

Le même décalage peut apparaître sous forme d'avertissement de plugin, par exemple `blocked plugin candidate: suspicious ownership (... uid=1000, expected uid=0 or root)` suivi de `plugin present but blocked`. Cela signifie que l'uid du processus et le propriétaire du répertoire de plugin monté ne correspondent pas. Préférez exécuter le conteneur avec l'uid par défaut 1000 et corriger la propriété du montage lié. N'appliquez un chown de `/path/to/openclaw-config/npm` à `root:root` que si vous exécutez volontairement OpenClaw en tant que root sur le long terme.

Reconstructions plus rapides

Organisez votre Dockerfile pour mettre en cache les couches de dépendances. Cela évite de relancer `pnpm install` sauf si les lockfiles changent :

dockerfileCopy code
[code]
    FROM node:24-bookwormRUN curl -fsSL https://bun.sh/install | bashENV PATH="/root/.bun/bin:${PATH}"RUN corepack enableWORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scriptsRUN pnpm install --frozen-lockfileCOPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:buildENV NODE_ENV=productionCMD ["node","dist/index.js"]
[/code]

Options de conteneur pour utilisateurs avancés

L'image par défaut privilégie la sécurité et s'exécute en tant que `node` non-root. Pour un conteneur plus complet :

  1. **Persister`/home/node`** : `export OPENCLAW_HOME_VOLUME="openclaw_home"`
  2. **Intégrer les dépendances système** : `export OPENCLAW_DOCKER_APT_PACKAGES="git curl jq"`
  3. **Intégrer Playwright Chromium** : `export OPENCLAW_INSTALL_BROWSER=1`
  4. **Ou installer les navigateurs Playwright dans un volume persistant** :bashCopy code
[code]docker compose run --rm openclaw-cli \  node /app/node_modules/playwright-core/cli.js install chromium
[/code]

  5. **Persister les téléchargements de navigateur** : utilisez `OPENCLAW_HOME_VOLUME` ou `OPENCLAW_EXTRA_MOUNTS`. OpenClaw détecte automatiquement le Chromium géré par Playwright de l'image Docker sous Linux.

OpenAI Codex OAuth (Docker sans interface graphique)

Si vous choisissez OpenAI Codex OAuth dans l'assistant, il ouvre une URL de navigateur. Dans Docker ou les configurations sans interface graphique, copiez l'URL de redirection complète sur laquelle vous arrivez et collez-la dans l'assistant pour terminer l'authentification.

Métadonnées de l'image de base

L'image principale du runtime Docker utilise `node:24-bookworm-slim` et inclut `tini` comme processus d'initialisation d'entrypoint (PID 1) afin de garantir que les processus zombies sont récupérés et que les signaux sont correctement gérés dans les conteneurs à longue durée de vie. Elle publie des annotations d'image de base OCI, notamment `org.opencontainers.image.base.name`, `org.opencontainers.image.source` et d'autres. Le digest de base Node est actualisé via les PR Dependabot d'image de base Docker ; les builds de version ne lancent pas de couche de mise à niveau de distribution. Consultez [Annotations d'image OCI](<https://github.com/opencontainers/image-spec/blob/main/annotations.md>).

### Exécution sur un VPS ?

Consultez [Hetzner (Docker VPS)](</fr/install/hetzner>) et [Docker VM Runtime](</fr/install/docker-vm-runtime>) pour les étapes partagées de déploiement sur VM, y compris l'intégration des binaires, la persistance et les mises à jour.

## Bac à sable d'agent

Lorsque `agents.defaults.sandbox` est activé avec le backend Docker, le Gateway exécute les outils d'agent (shell, lecture/écriture de fichiers, etc.) dans des conteneurs Docker isolés pendant que le Gateway lui-même reste sur l'hôte. Cela vous donne une séparation stricte autour des sessions d'agent non fiables ou multi-locataires sans conteneuriser tout le Gateway.

La portée du bac à sable peut être par agent (par défaut), par session ou partagée. Chaque portée dispose de son propre espace de travail monté sur `/workspace`. Vous pouvez aussi configurer des politiques d'autorisation/refus d'outils, l'isolation réseau, des limites de ressources et des conteneurs de navigateur.

Pour la configuration complète, les images, les notes de sécurité et les profils multi-agents, consultez :

  * [Sandboxing](</fr/gateway/sandboxing>) \-- référence complète du bac à sable
  * [OpenShell](</fr/gateway/openshell>) \-- accès shell interactif aux conteneurs de bac à sable
  * [Multi-Agent Sandbox and Tools](</fr/tools/multi-agent-sandbox-tools>) \-- remplacements par agent


### Activation rapide

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "non-main", // off | non-main | all        scope: "agent", // session | agent | shared      },    },  },}
[/code]

Construisez l'image de bac à sable par défaut (depuis un checkout source) :

bashCopy code
[code]
    scripts/sandbox-setup.sh
[/code]

Pour les installations npm sans checkout source, consultez [Sandboxing § Images and setup](</fr/gateway/sandboxing#images-and-setup>) pour les commandes `docker build` en ligne.

## Dépannage

Image manquante ou conteneur de bac à sable qui ne démarre pas

Construisez l'image de bac à sable avec [`scripts/sandbox-setup.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/sandbox-setup.sh>) (checkout source) ou la commande `docker build` en ligne depuis [Sandboxing § Images and setup](</fr/gateway/sandboxing#images-and-setup>) (installation npm), ou définissez `agents.defaults.sandbox.docker.image` sur votre image personnalisée. Les conteneurs sont créés automatiquement par session à la demande.

Erreurs d'autorisation dans le bac à sable

Définissez `docker.user` sur un UID:GID correspondant à la propriété de votre espace de travail monté, ou changez le propriétaire du dossier de l'espace de travail.

Outils personnalisés introuvables dans le bac à sable

OpenClaw exécute les commandes avec `sh -lc` (shell de connexion), qui source `/etc/profile` et peut réinitialiser PATH. Définissez `docker.env.PATH` pour préfixer vos chemins d'outils personnalisés, ou ajoutez un script sous `/etc/profile.d/` dans votre Dockerfile.

Processus tué par OOM pendant la construction de l'image (exit 137)

La VM a besoin d'au moins 2 Go de RAM. Utilisez une classe de machine plus grande et réessayez.

Non autorisé ou association requise dans l'interface de contrôle

Récupérez un nouveau lien de tableau de bord et approuvez l'appareil du navigateur :

bashCopy code
[code]
    docker compose run --rm openclaw-cli dashboard --no-opendocker compose run --rm openclaw-cli devices listdocker compose run --rm openclaw-cli devices approve <requestId>
[/code]

Plus de détails : [Dashboard](</fr/web/dashboard>), [Devices](</fr/cli/devices>).

La cible du Gateway affiche ws://172.x.x.x ou des erreurs d'association depuis la CLI Docker

Réinitialisez le mode et la liaison du Gateway :

bashCopy code
[code]
    docker compose run --rm openclaw-cli config set --batch-json '[{"path":"gateway.mode","value":"local"},{"path":"gateway.bind","value":"lan"}]'docker compose run --rm openclaw-cli devices list --url ws://127.0.0.1:18789
[/code]

## Associé

  * [Vue d'ensemble de l'installation](</fr/install>) — toutes les méthodes d'installation
  * [Podman](</fr/install/podman>) — alternative Podman à Docker
  * [ClawDock](</fr/install/clawdock>) — configuration communautaire Docker Compose
  * [Mise à jour](</fr/install/updating>) — maintenir OpenClaw à jour
  * [Configuration](</fr/gateway/configuration>) — configuration du Gateway après installation


Was this useful?YesNo