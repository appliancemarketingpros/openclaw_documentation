---
title: ACP
source_url: https://docs.openclaw.ai/fr/cli/acp
scraped_at: 2026-05-25
---

Exécute le pont [Agent Client Protocol (ACP)](<https://agentclientprotocol.com/>) qui communique avec un Gateway OpenClaw.

Cette commande parle ACP sur stdio pour les IDE et transmet les invites au Gateway via WebSocket. Elle conserve les sessions ACP associées aux clés de session du Gateway.

`openclaw acp` est un pont ACP adossé au Gateway, et non un runtime d’éditeur entièrement natif ACP. Il se concentre sur le routage des sessions, la livraison des invites et les mises à jour de streaming de base.

Si vous voulez qu’un client MCP externe communique directement avec les conversations de canal OpenClaw au lieu d’héberger une session de harnais ACP, utilisez plutôt [`openclaw mcp serve`](</fr/cli/mcp>).

## Ce que ce n’est pas

Cette page est souvent confondue avec les sessions de harnais ACP.

`openclaw acp` signifie :

  * OpenClaw agit comme serveur ACP
  * un IDE ou client ACP se connecte à OpenClaw
  * OpenClaw transmet ce travail à une session Gateway


C’est différent des [agents ACP](</fr/tools/acp-agents>), où OpenClaw exécute un harnais externe comme Codex ou Claude Code via `acpx`.

Règle rapide :

  * l’éditeur/client veut parler ACP à OpenClaw : utilisez `openclaw acp`
  * OpenClaw doit lancer Codex/Claude/Gemini comme harnais ACP : utilisez `/acp spawn` et [agents ACP](</fr/tools/acp-agents>)


## Matrice de compatibilité

Zone ACP | État | Notes  
---|---|---  
`initialize`, `newSession`, `prompt`, `cancel` | Implémenté | Flux de pont principal sur stdio vers chat/send + abandon du Gateway.  
`listSessions`, commandes slash | Implémenté | La liste des sessions fonctionne avec l’état de session du Gateway, une pagination bornée par curseur et un filtrage `cwd` lorsque les lignes de session du Gateway portent des métadonnées d’espace de travail ; les commandes sont annoncées via `available_commands_update`.  
Métadonnées de lignée de session | Implémenté | Les listes de sessions et instantanés d’informations de session incluent la lignée parent et enfant OpenClaw dans `_meta` afin que les clients ACP puissent afficher des graphes de sous-agents sans canaux latéraux privés du Gateway.  
`resumeSession`, `closeSession` | Implémenté | La reprise rattache une session ACP à une session Gateway existante sans rejouer l’historique. La fermeture annule le travail actif du pont, résout les invites en attente comme annulées et libère l’état de session du pont.  
`loadSession` | Partiel | Rattache la session ACP à une clé de session Gateway et rejoue l’historique du registre d’événements ACP pour les sessions créées par le pont. Les sessions plus anciennes/sans registre se replient sur le texte utilisateur/assistant stocké.  
Contenu d’invite (`text`, `resource` intégré, images) | Partiel | Le texte et les ressources sont aplatis dans l’entrée de chat ; les images deviennent des pièces jointes Gateway.  
Modes de session | Partiel | `session/set_mode` est pris en charge et le pont expose des contrôles de session initiaux adossés au Gateway pour le niveau de pensée, la verbosité des outils, le raisonnement, le détail d’utilisation et les actions élevées. Les surfaces de mode/configuration natives ACP plus larges restent hors périmètre.  
Informations de session et mises à jour d’utilisation | Partiel | Le pont émet des notifications `session_info_update` et `usage_update` au mieux à partir d’instantanés de session Gateway mis en cache. L’utilisation est approximative et envoyée uniquement lorsque les totaux de jetons Gateway sont marqués comme frais.  
Streaming d’outils | Partiel | Les événements `tool_call` / `tool_call_update` incluent les E/S brutes, le contenu textuel et, au mieux, les emplacements de fichiers lorsque les arguments/résultats d’outils Gateway les exposent. Les terminaux intégrés et les sorties plus riches natives de diff ne sont pas encore exposés.  
Approbations d’exécution | Partiel | Les demandes d’approbation d’exécution du Gateway pendant les tours d’invite ACP actifs sont relayées au client ACP avec `session/request_permission`.  
Serveurs MCP par session (`mcpServers`) | Non pris en charge | Le mode pont rejette les demandes de serveur MCP par session. Configurez plutôt MCP sur le gateway ou l’agent OpenClaw.  
Méthodes de système de fichiers client (`fs/read_text_file`, `fs/write_text_file`) | Non pris en charge | Le pont n’appelle pas les méthodes de système de fichiers du client ACP.  
Méthodes de terminal client (`terminal/*`) | Non pris en charge | Le pont ne crée pas de terminaux client ACP et ne diffuse pas d’identifiants de terminal via les appels d’outils.  
Plans de session / streaming de pensée | Non pris en charge | Le pont émet actuellement du texte de sortie et l’état des outils, pas de mises à jour de plan ou de pensée ACP.  
  
## Limitations connues

  * `loadSession` ne peut rejouer l’historique complet du registre d’événements ACP que pour les sessions créées par le pont. Les sessions plus anciennes/sans registre utilisent toujours le repli sur la transcription et ne reconstruisent pas les appels d’outils historiques ni les avis système.
  * Si plusieurs clients ACP partagent la même clé de session Gateway, le routage des événements et des annulations est au mieux approximatif plutôt que strictement isolé par client. Préférez les sessions isolées par défaut `acp:<uuid>` lorsque vous avez besoin de tours propres locaux à l’éditeur.
  * Les états d’arrêt du Gateway sont traduits en raisons d’arrêt ACP, mais ce mappage est moins expressif qu’un runtime entièrement natif ACP.
  * Les contrôles de session initiaux exposent actuellement un sous-ensemble ciblé de réglages Gateway : niveau de pensée, verbosité des outils, raisonnement, détail d’utilisation et actions élevées. La sélection de modèle et les contrôles d’hôte d’exécution ne sont pas encore exposés comme options de configuration ACP.
  * `session_info_update` et `usage_update` sont dérivés d’instantanés de session Gateway, et non d’une comptabilité de runtime native ACP en direct. L’utilisation est approximative, ne contient aucune donnée de coût et n’est émise que lorsque le Gateway marque les données de total de jetons comme fraîches.
  * Les données de suivi d’outils sont au mieux approximatives. Le pont peut exposer les chemins de fichiers qui apparaissent dans des arguments/résultats d’outils connus, mais il n’émet pas encore de terminaux ACP ni de diffs de fichiers structurés.
  * Le relais d’approbation d’exécution est limité au tour d’invite ACP actif ; les approbations provenant d’autres sessions Gateway sont ignorées.


## Utilisation

bashCopy code
[code]
    openclaw acp # Remote Gatewayopenclaw acp --url wss://gateway-host:18789 --token <token> # Remote Gateway (token from file)openclaw acp --url wss://gateway-host:18789 --token-file ~/.openclaw/gateway.token # Attach to an existing session keyopenclaw acp --session agent:main:main # Attach by label (must already exist)openclaw acp --session-label "support inbox" # Reset the session key before the first promptopenclaw acp --session agent:main:main --reset-session
[/code]

## Client ACP (débogage)

Utilisez le client ACP intégré pour vérifier rapidement le pont sans IDE. Il lance le pont ACP et vous permet de saisir des invites de façon interactive.

bashCopy code
[code]
    openclaw acp client # Point the spawned bridge at a remote Gatewayopenclaw acp client --server-args --url wss://gateway-host:18789 --token-file ~/.openclaw/gateway.token # Override the server command (default: openclaw)openclaw acp client --server "node" --server-args openclaw.mjs acp --url ws://127.0.0.1:19001
[/code]

Modèle d’autorisation (mode de débogage client) :

  * L’approbation automatique repose sur une liste d’autorisation et s’applique uniquement aux identifiants d’outils principaux approuvés.
  * L’approbation automatique de `read` est limitée au répertoire de travail actuel (`--cwd` lorsqu’il est défini).
  * ACP n’approuve automatiquement que des classes étroites en lecture seule : les appels `read` limités sous le cwd actif ainsi que les outils de recherche en lecture seule (`search`, `web_search`, `memory_search`). Les outils inconnus/non principaux, les lectures hors périmètre, les outils capables d’exécution, les outils de plan de contrôle, les outils modificateurs et les flux interactifs nécessitent toujours une approbation explicite de l’invite.
  * `toolCall.kind` fourni par le serveur est traité comme une métadonnée non fiable (pas comme une source d’autorisation).
  * Cette politique de pont ACP est distincte des permissions de harnais ACPX. Si vous exécutez OpenClaw via le backend `acpx`, `plugins.entries.acpx.config.permissionMode=approve-all` est le commutateur d’urgence « yolo » pour cette session de harnais.


## Test rapide du protocole

Pour le débogage au niveau protocole, démarrez un Gateway avec un état isolé et pilotez `openclaw acp` sur stdio avec un client JSON-RPC ACP. Couvrez `initialize`, `session/new`, `session/list` avec un `cwd` absolu, `session/resume`, `session/close`, une fermeture en double et une reprise manquante.

La preuve doit inclure les capacités de cycle de vie annoncées, une ligne de session adossée au Gateway, les notifications de mise à jour et le journal `sessions.list` du Gateway :

jsonCopy code
[code]
    {  "initialize": {    "protocolVersion": 1,    "agentCapabilities": {      "sessionCapabilities": {        "list": {},        "resume": {},        "close": {}      }    }  },  "listSessions": {    "sessions": [      {        "sessionId": "agent:main:acp-smoke",        "cwd": "/path/to/workspace",        "_meta": {          "sessionKey": "agent:main:acp-smoke",          "kind": "direct"        }      }    ],    "nextCursor": null  },  "notifications": ["session_info_update", "available_commands_update", "usage_update"],  "gatewayLogTail": ["[gateway] ready", "[ws] ⇄ res ✓ sessions.list 305ms"]}
[/code]

Évitez d’utiliser `openclaw gateway call sessions.list` comme seule preuve ACP. Ce chemin CLI peut demander une montée de périmètre opérateur avec jeton frais ; la correction du pont ACP se prouve par les trames stdio ACP ainsi que par le journal `sessions.list` du Gateway.

## Comment l’utiliser

Utilisez ACP lorsqu’un IDE (ou un autre client) parle Agent Client Protocol et que vous voulez qu’il pilote une session Gateway OpenClaw.

  1. Assurez-vous que le Gateway est en cours d’exécution (local ou distant).
  2. Configurez la cible Gateway (configuration ou indicateurs).
  3. Pointez votre IDE pour exécuter `openclaw acp` sur stdio.


Exemple de configuration (persistée) :

bashCopy code
[code]
    openclaw config set gateway.remote.url wss://gateway-host:18789openclaw config set gateway.remote.token <token>
[/code]

Exemple d’exécution directe (sans écriture de configuration) :

bashCopy code
[code]
    openclaw acp --url wss://gateway-host:18789 --token <token># preferred for local process safetyopenclaw acp --url wss://gateway-host:18789 --token-file ~/.openclaw/gateway.token
[/code]

## Sélection des agents

ACP ne choisit pas les agents directement. Il route selon la clé de session Gateway.

Utilisez des clés de session limitées à un agent pour cibler un agent spécifique :

bashCopy code
[code]
    openclaw acp --session agent:main:mainopenclaw acp --session agent:design:mainopenclaw acp --session agent:qa:bug-123
[/code]

Chaque session ACP correspond à une seule clé de session Gateway. Un agent peut avoir plusieurs sessions ; ACP utilise par défaut une session isolée `acp:<uuid>`, sauf si vous remplacez la clé ou le libellé.

Les `mcpServers` par session ne sont pas pris en charge en mode pont. Si un client ACP les envoie pendant `newSession` ou `loadSession`, le pont renvoie une erreur claire au lieu de les ignorer silencieusement.

Si vous voulez que les sessions adossées à ACPX voient les outils de Plugin OpenClaw ou certains outils intégrés comme `cron`, activez plutôt les ponts ACPX MCP côté Gateway au lieu d'essayer de transmettre des `mcpServers` par session. Consultez [Agents ACP](</fr/tools/acp-agents-setup#plugin-tools-mcp-bridge>) et [Pont MCP des outils OpenClaw](</fr/tools/acp-agents-setup#openclaw-tools-mcp-bridge>).

## Utilisation depuis `acpx` (Codex, Claude, autres clients ACP)

Si vous voulez qu'un agent de codage comme Codex ou Claude Code communique avec votre bot OpenClaw via ACP, utilisez `acpx` avec sa cible intégrée `openclaw`.

Flux typique :

  1. Exécutez le Gateway et assurez-vous que le pont ACP peut l'atteindre.
  2. Pointez `acpx openclaw` vers `openclaw acp`.
  3. Ciblez la clé de session OpenClaw que vous voulez que l'agent de codage utilise.


Exemples :

bashCopy code
[code]
    # One-shot request into your default OpenClaw ACP sessionacpx openclaw exec "Summarize the active OpenClaw session state." # Persistent named session for follow-up turnsacpx openclaw sessions ensure --name codex-bridgeacpx openclaw -s codex-bridge --cwd /path/to/repo \  "Ask my OpenClaw work agent for recent context relevant to this repo."
[/code]

Si vous voulez que `acpx openclaw` cible un Gateway et une clé de session spécifiques à chaque fois, remplacez la commande de l'agent `openclaw` dans `~/.acpx/config.json` :

jsonCopy code
[code]
    {  "agents": {    "openclaw": {      "command": "env OPENCLAW_HIDE_BANNER=1 OPENCLAW_SUPPRESS_NOTES=1 openclaw acp --url ws://127.0.0.1:18789 --token-file ~/.openclaw/gateway.token --session agent:main:main"    }  }}
[/code]

Pour un checkout OpenClaw local au dépôt, utilisez le point d'entrée CLI direct au lieu du lanceur de développement afin que le flux ACP reste propre. Par exemple :

bashCopy code
[code]
    env OPENCLAW_HIDE_BANNER=1 OPENCLAW_SUPPRESS_NOTES=1 node openclaw.mjs acp ...
[/code]

C'est la façon la plus simple de permettre à Codex, Claude Code ou à un autre client compatible ACP d'extraire des informations contextuelles d'un agent OpenClaw sans analyser un terminal.

## Configuration de l'éditeur Zed

Ajoutez un agent ACP personnalisé dans `~/.config/zed/settings.json` (ou utilisez l'interface Settings de Zed) :

jsonCopy code
[code]
    {  "agent_servers": {    "OpenClaw ACP": {      "type": "custom",      "command": "openclaw",      "args": ["acp"],      "env": {}    }  }}
[/code]

Pour cibler un Gateway ou un agent spécifique :

jsonCopy code
[code]
    {  "agent_servers": {    "OpenClaw ACP": {      "type": "custom",      "command": "openclaw",      "args": [        "acp",        "--url",        "wss://gateway-host:18789",        "--token",        "<token>",        "--session",        "agent:design:main"      ],      "env": {}    }  }}
[/code]

Dans Zed, ouvrez le panneau Agent et sélectionnez "OpenClaw ACP" pour démarrer un fil.

## Correspondance des sessions

Par défaut, les sessions ACP obtiennent une clé de session Gateway isolée avec un préfixe `acp:`. Pour réutiliser une session connue, transmettez une clé ou un libellé de session :

  * `--session <key>` : utiliser une clé de session Gateway spécifique.
  * `--session-label <label>` : résoudre une session existante par libellé.
  * `--reset-session` : émettre un nouvel identifiant de session pour cette clé (même clé, nouveau transcript).


Si votre client ACP prend en charge les métadonnées, vous pouvez les remplacer par session :

jsonCopy code
[code]
    {  "_meta": {    "sessionKey": "agent:main:main",    "sessionLabel": "support inbox",    "resetSession": true  }}
[/code]

Apprenez-en plus sur les clés de session à l'adresse [/concepts/session](</fr/concepts/session>).

## Options

  * `--url <url>` : URL WebSocket du Gateway (par défaut, gateway.remote.url lorsqu'elle est configurée).
  * `--token <token>` : jeton d'authentification du Gateway.
  * `--token-file <path>` : lire le jeton d'authentification du Gateway depuis un fichier.
  * `--password <password>` : mot de passe d'authentification du Gateway.
  * `--password-file <path>` : lire le mot de passe d'authentification du Gateway depuis un fichier.
  * `--session <key>` : clé de session par défaut.
  * `--session-label <label>` : libellé de session par défaut à résoudre.
  * `--require-existing` : échouer si la clé ou le libellé de session n'existe pas.
  * `--reset-session` : réinitialiser la clé de session avant la première utilisation.
  * `--no-prefix-cwd` : ne pas préfixer les prompts avec le répertoire de travail.
  * `--provenance <off|meta|meta+receipt>` : inclure les métadonnées ou reçus de provenance ACP.
  * `--verbose, -v` : journalisation détaillée vers stderr.


Note de sécurité :

  * `--token` et `--password` peuvent être visibles dans les listes de processus locales sur certains systèmes.
  * Préférez `--token-file`/`--password-file` ou les variables d'environnement (`OPENCLAW_GATEWAY_TOKEN`, `OPENCLAW_GATEWAY_PASSWORD`).
  * La résolution d'authentification Gateway suit le contrat partagé utilisé par les autres clients Gateway : 
    * mode local : env (`OPENCLAW_GATEWAY_*`) -> `gateway.auth.*` -> solution de repli `gateway.remote.*` uniquement lorsque `gateway.auth.*` n'est pas défini (les SecretRefs locaux configurés mais non résolus échouent en mode fermé)
    * mode distant : `gateway.remote.*` avec repli env/config selon les règles de précédence distantes
    * `--url` est sûr comme remplacement et ne réutilise pas les identifiants implicites config/env ; transmettez explicitement `--token`/`--password` (ou les variantes par fichier)
  * Les processus enfants du backend d'exécution ACP reçoivent `OPENCLAW_SHELL=acp`, qui peut être utilisé pour des règles de shell/profil propres au contexte.
  * `openclaw acp client` définit `OPENCLAW_SHELL=acp-client` sur le processus de pont lancé.


### Options de `acp client`

  * `--cwd <dir>` : répertoire de travail pour la session ACP.
  * `--server <command>` : commande du serveur ACP (par défaut : `openclaw`).
  * `--server-args <args...>` : arguments supplémentaires transmis au serveur ACP.
  * `--server-verbose` : activer la journalisation détaillée sur le serveur ACP.
  * `--verbose, -v` : journalisation détaillée du client.


## Connexe

  * [Référence CLI](</fr/cli>)
  * [Agents ACP](</fr/tools/acp-agents>)


Was this useful?YesNo