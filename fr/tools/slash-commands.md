---
title: Commandes slash
source_url: https://docs.openclaw.ai/fr/tools/slash-commands
scraped_at: 2026-05-25
---

Les commandes sont gérées par le Gateway. La plupart des commandes doivent être envoyées comme message **autonome** commençant par `/`. La commande de chat bash réservée à l’hôte utilise `! <cmd>` (avec `/bash <cmd>` comme alias).

Lorsqu’une conversation ou un fil est lié à une session ACP, le texte de suivi normal est routé vers ce harnais ACP. Les commandes de gestion du Gateway restent locales : `/acp ...` atteint toujours le gestionnaire de commandes ACP d’OpenClaw, et `/status` ainsi que `/unfocus` restent locales chaque fois que la gestion des commandes est activée pour la surface.

Il existe deux systèmes liés :

Commands

Messages `/...` autonomes.

Directives

`/think`, `/fast`, `/verbose`, `/trace`, `/reasoning`, `/elevated`, `/exec`, `/model`, `/queue`.

  * Les directives sont retirées du message avant que le modèle ne le voie.
  * Dans les messages de chat normaux (non composés uniquement de directives), elles sont traitées comme des « indications en ligne » et ne conservent **pas** les paramètres de session.
  * Dans les messages composés uniquement de directives (le message ne contient que des directives), elles persistent dans la session et répondent par un accusé de réception.
  * Les directives ne sont appliquées qu’aux **expéditeurs autorisés**. Si `commands.allowFrom` est défini, c’est la seule liste d’autorisation utilisée ; sinon l’autorisation provient des listes d’autorisation/appariement du canal plus `commands.useAccessGroups`. Les expéditeurs non autorisés voient les directives traitées comme du texte brut.

Inline shortcuts

Expéditeurs sur liste d’autorisation/autorisés uniquement : `/help`, `/commands`, `/status`, `/whoami` (`/id`).

Elles s’exécutent immédiatement, sont retirées avant que le modèle ne voie le message, et le texte restant continue dans le flux normal.

## Configuration

json5Copy code
[code]
    {  commands: {    native: "auto",    nativeSkills: "auto",    text: true,    bash: false,    bashForegroundMs: 2000,    config: false,    mcp: false,    plugins: false,    debug: false,    restart: true,    ownerAllowFrom: ["discord:123456789012345678"],    ownerDisplay: "raw",    ownerDisplaySecret: "${OWNER_ID_HASH_SECRET}",    allowFrom: {      "*": ["user1"],      discord: ["user:123"],    },    useAccessGroups: true,  },}
[/code]

Active l’analyse de `/...` dans les messages de chat. Sur les surfaces sans commandes natives (WhatsApp/WebChat/Signal/iMessage/Google Chat/Microsoft Teams), les commandes textuelles fonctionnent encore même si vous définissez cette option sur `false`.

Enregistre les commandes natives. Auto : activé pour Discord/Telegram ; désactivé pour Slack (jusqu’à ce que vous ajoutiez des commandes slash) ; ignoré pour les fournisseurs sans prise en charge native. Définissez `channels.discord.commands.native`, `channels.telegram.commands.native` ou `channels.slack.commands.native` pour remplacer par fournisseur (booléen ou `"auto"`). Sur Discord, `false` ignore l’enregistrement des commandes slash et le nettoyage au démarrage ; les commandes précédemment enregistrées peuvent rester visibles jusqu’à ce que vous les supprimiez de l’application Discord. Les commandes Slack sont gérées dans l’application Slack et ne sont pas supprimées automatiquement.

Sur Discord, les spécifications de commandes natives peuvent inclure `descriptionLocalizations`, qu’OpenClaw publie comme `description_localizations` Discord et inclut dans les comparaisons de réconciliation.

Enregistre les commandes de **Skills** nativement lorsque c’est pris en charge. Auto : activé pour Discord/Telegram ; désactivé pour Slack (Slack exige de créer une commande slash par Skills). Définissez `channels.discord.commands.nativeSkills`, `channels.telegram.commands.nativeSkills` ou `channels.slack.commands.nativeSkills` pour remplacer par fournisseur (booléen ou `"auto"`).

Active `! <cmd>` pour exécuter des commandes shell sur l’hôte (`/bash <cmd>` est un alias ; nécessite des listes d’autorisation `tools.elevated`).

Contrôle la durée d’attente de bash avant de passer en mode arrière-plan (`0` met immédiatement en arrière-plan).

Active `/config` (lit/écrit `openclaw.json`).

Active `/mcp` (lit/écrit la configuration MCP gérée par OpenClaw sous `mcp.servers`).

Active `/plugins` (découverte/état des plugins plus contrôles d’installation et d’activation/désactivation).

Active `/debug` (remplacements uniquement au moment de l’exécution).

Active `/restart` ainsi que les actions d’outil de redémarrage du Gateway.

Définit la liste d’autorisation explicite du propriétaire pour les surfaces de commandes/outils réservées au propriétaire. Il s’agit du compte opérateur humain qui peut approuver les actions dangereuses et exécuter des commandes telles que `/diagnostics`, `/export-trajectory` et `/config`. Elle est distincte de `commands.allowFrom` et de l’accès par appariement en message direct.

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImNoYW5uZWxzLjxjaGFubmVs .commands.enforceOwnerForCommands" type="boolean" default="false"> Par canal : exige une **identité propriétaire** pour exécuter les commandes réservées au propriétaire sur cette surface. Lorsque `true`, l’expéditeur doit soit correspondre à un candidat propriétaire résolu (par exemple une entrée dans `commands.ownerAllowFrom` ou des métadonnées de propriétaire natives du fournisseur), soit détenir la portée interne `operator.admin` sur un canal de message interne. Une entrée générique dans `allowFrom` du canal, ou une liste de candidats propriétaires vide/non résolue, n’est **pas** suffisante : les commandes réservées au propriétaire échouent en mode fermé sur ce canal. Laissez cette option désactivée si vous voulez que les commandes réservées au propriétaire soient limitées uniquement par `ownerAllowFrom` et les listes d’autorisation de commandes standard.

Contrôle la façon dont les identifiants de propriétaire apparaissent dans l’invite système.

Définit facultativement le secret HMAC utilisé lorsque `commands.ownerDisplay="hash"`.

Liste d’autorisation par fournisseur pour l’autorisation des commandes. Lorsqu’elle est configurée, c’est la seule source d’autorisation pour les commandes et directives (les listes d’autorisation/appariement des canaux et `commands.useAccessGroups` sont ignorés). Utilisez `"*"` comme valeur par défaut globale ; les clés propres au fournisseur la remplacent.

Applique les listes d’autorisation/politiques pour les commandes lorsque `commands.allowFrom` n’est pas défini.

## Liste des commandes

Source de vérité actuelle :

  * les commandes intégrées du cœur proviennent de `src/auto-reply/commands-registry.shared.ts`
  * les commandes du dock générées proviennent de `src/auto-reply/commands-registry.data.ts`
  * les commandes de plugins proviennent des appels `registerCommand()` des plugins
  * la disponibilité réelle sur votre Gateway dépend toujours des indicateurs de configuration, de la surface du canal et des plugins installés/activés


### Commandes intégrées du cœur

Sessions and runs

  * `/new [model]` démarre une nouvelle session ; `/reset` est l’alias de réinitialisation.
  * L’interface de contrôle intercepte `/new` saisi pour créer et basculer vers une nouvelle session de tableau de bord, sauf lorsque `session.dmScope: "main"` est configuré et que le parent actuel est la session principale de l’agent ; dans ce cas, `/new` réinitialise la session principale sur place. `/reset` saisi exécute toujours la réinitialisation sur place du Gateway.
  * `/reset soft [message]` conserve la transcription actuelle, abandonne les identifiants de session du backend CLI réutilisés et relance le chargement de démarrage/de l’invite système sur place.
  * `/compact [instructions]` compacte le contexte de session. Voir [Compaction](</fr/concepts/compaction>).
  * `/stop` interrompt l’exécution actuelle.
  * `/session idle <duration|off>` et `/session max-age <duration|off>` gèrent l’expiration de liaison au fil.
  * `/export-session [path]` exporte la session actuelle en HTML. Alias : `/export`.
  * `/export-trajectory [path]` demande l’approbation d’exécution, puis exporte un [lot de trajectoire](</fr/tools/trajectory>) JSONL pour la session actuelle. Utilisez-le lorsque vous avez besoin de la chronologie de l’invite, des outils et de la transcription pour une session OpenClaw. Dans les discussions de groupe, l’invite d’approbation et le résultat d’exportation sont envoyés au propriétaire en privé. Alias : `/trajectory`.

Model and run controls

  * `/think <level|default>` définit le niveau de réflexion ou efface le remplacement de session. Les options proviennent du profil fournisseur du modèle actif ; les niveaux courants sont `off`, `minimal`, `low`, `medium` et `high`, avec des niveaux personnalisés comme `xhigh`, `adaptive`, `max`, ou le binaire `on` uniquement lorsque c’est pris en charge. Alias : `/thinking`, `/t`.
  * `/verbose on|off|full` active/désactive la sortie détaillée. Alias : `/v`.
  * `/trace on|off` active/désactive la sortie de trace des plugins pour la session actuelle.
  * `/fast [status|on|off|default]` affiche, définit ou efface le mode rapide.
  * `/reasoning [on|off|stream]` active/désactive la visibilité du raisonnement. Alias : `/reason`.
  * `/elevated [on|off|ask|full]` active/désactive le mode élevé. Alias : `/elev`.
  * `/exec host=<auto|sandbox|gateway|node> security=<deny|allowlist|full> ask=<off|on-miss|always> node=<id>` affiche ou définit les valeurs par défaut d’exécution.
  * `/model [name|#|status]` affiche ou définit le modèle.
  * `/models [provider] [page] [limit=<n>|size=<n>|all]` liste les fournisseurs configurés/disponibles par authentification ou les modèles pour un fournisseur ; ajoutez `all` pour parcourir le catalogue complet de ce fournisseur. Les entrées `provider/*` dans `agents.defaults.models` font que `/model` et `/models` affichent les modèles découverts uniquement pour ces fournisseurs.
  * `/queue <mode>` gère le comportement de file d’attente (`steer`, `queue` hérité, `followup`, `collect`, `steer-backlog`, `interrupt`) plus des options comme `debounce:0.5s cap:25 drop:summarize` ; `/queue default` ou `/queue reset` efface le remplacement de session. Voir [File d’attente de commandes](</fr/concepts/queue>) et [File d’attente de guidage](</fr/concepts/queue-steering>).
  * `/steer <message>` injecte des consignes dans l’exécution active pour la session actuelle, indépendamment du mode `/queue`. Cela ne démarre pas une nouvelle exécution lorsque la session est inactive. Alias : `/tell`. Voir [Steer](</fr/tools/steer>).

Discovery and status

  * `/help` affiche le court résumé d’aide.
  * `/commands` affiche le catalogue de commandes généré.
  * `/tools [compact|verbose]` affiche ce que l’agent actuel peut utiliser maintenant.
  * `/status` affiche l’état d’exécution/du runtime, la disponibilité du Gateway et du système, ainsi que l’utilisation/le quota du fournisseur lorsque disponible.
  * `/diagnostics [note]` est le flux de rapport d’assistance réservé au propriétaire pour les bogues du Gateway et les exécutions du harnais Codex. Il demande une approbation d’exécution explicite à chaque fois avant d’exécuter `openclaw gateway diagnostics export --json` ; n’approuvez pas les diagnostics avec une règle tout autoriser. Après approbation, il envoie un rapport prêt à coller avec le chemin du lot local, le résumé du manifeste, les notes de confidentialité et les identifiants de session pertinents. Dans les discussions de groupe, l’invite d’approbation et le rapport sont envoyés au propriétaire en privé. Lorsque la session active utilise le harnais OpenAI Codex, la même approbation envoie également les retours Codex pertinents aux serveurs OpenAI, et la réponse terminée liste les identifiants de session OpenClaw, les identifiants de fil Codex et les commandes `codex resume <thread-id>`. Voir [Exportation de diagnostics](</fr/gateway/diagnostics>).
  * `/crestodian <request>` exécute l’assistant de configuration et de réparation Crestodian depuis un message direct du propriétaire.
  * `/tasks` liste les tâches d’arrière-plan actives/récentes pour la session actuelle.
  * `/context [list|detail|map|json]` explique comment le contexte est assemblé. `map` envoie une image en carte proportionnelle du contexte de la session actuelle.
  * `/whoami` affiche votre identifiant d’expéditeur. Alias : `/id`.
  * `/usage off|tokens|full|cost` contrôle le pied de page d’utilisation par réponse ou imprime un résumé local des coûts.

Skills, listes d’autorisation, approbations

  * `/skill <name> [input]` exécute une skill par nom.
  * `/allowlist [list|add|remove] ...` gère les entrées de liste d’autorisation. Texte uniquement.
  * `/approve <id> <decision>` résout les invites d’approbation d’exécution.
  * `/btw <question>` pose une question annexe sans modifier le contexte des futures sessions. Alias : `/side`. Voir [BTW](</fr/tools/btw>).

Sous-agents et ACP

  * `/subagents list|kill|log|info|send|steer|spawn` gère les exécutions de sous-agents pour la session actuelle.
  * `/acp spawn|cancel|steer|close|sessions|status|set-mode|set|cwd|permissions|timeout|model|reset-options|doctor|install|help` gère les sessions ACP et les options d’exécution.
  * `/focus <target>` lie le fil Discord actuel ou le sujet/la conversation Telegram à une cible de session.
  * `/unfocus` supprime le lien actuel.
  * `/agents` liste les agents liés au fil pour la session actuelle.
  * `/kill <id|#|all>` interrompt un ou tous les sous-agents en cours d’exécution.
  * `/subagents steer <id|#> <message>` envoie un guidage à un sous-agent en cours d’exécution. Voir [Steer](</fr/tools/steer>).

Écritures réservées au propriétaire et administration

  * `/config show|get|set|unset` lit ou écrit `openclaw.json`. Réservé au propriétaire. Nécessite `commands.config: true`.
  * `/mcp show|get|set|unset` lit ou écrit la configuration de serveur MCP gérée par OpenClaw sous `mcp.servers`. Réservé au propriétaire. Nécessite `commands.mcp: true`.
  * `/plugins list|inspect|show|get|install|enable|disable` inspecte ou modifie l’état des plugins. `/plugin` est un alias. Écritures réservées au propriétaire. Nécessite `commands.plugins: true`.
  * `/debug show|set|unset|reset` gère les remplacements de configuration propres à l’exécution. Réservé au propriétaire. Nécessite `commands.debug: true`.
  * `/restart` redémarre OpenClaw lorsque cette option est activée. Par défaut : activé ; définissez `commands.restart: false` pour la désactiver.
  * `/send on|off|inherit` définit la politique d’envoi. Réservé au propriétaire.

Voix, TTS, contrôle des canaux

  * `/tts on|off|status|chat|latest|provider|limit|summary|audio|help` contrôle TTS. Voir [TTS](</fr/tools/tts>).
  * `/activation mention|always` définit le mode d’activation de groupe.
  * `/bash <command>` exécute une commande shell hôte. Texte uniquement. Alias : `! <command>`. Nécessite `commands.bash: true` ainsi que les listes d’autorisation `tools.elevated`.
  * `!poll [sessionId]` vérifie une tâche bash en arrière-plan.
  * `!stop [sessionId]` arrête une tâche bash en arrière-plan.


### Commandes de dock générées

Les commandes de dock basculent la route de réponse de la session actuelle vers un autre canal lié. Voir [Channel docking](</fr/concepts/channel-docking>) pour la configuration, les exemples et le dépannage.

Les commandes de dock sont générées à partir de plugins de canaux prenant en charge les commandes natives. Ensemble intégré actuel :

  * `/dock-discord` (alias : `/dock_discord`)
  * `/dock-mattermost` (alias : `/dock_mattermost`)
  * `/dock-slack` (alias : `/dock_slack`)
  * `/dock-telegram` (alias : `/dock_telegram`)


Utilisez les commandes de dock depuis une conversation directe pour basculer la route de réponse de la session actuelle vers un autre canal lié. L’agent conserve le même contexte de session, mais les futures réponses de cette session sont livrées au pair de canal sélectionné.

Les commandes de dock nécessitent `session.identityLinks`. L’expéditeur source et le pair cible doivent appartenir au même groupe d’identité, par exemple `["telegram:123", "discord:456"]`. Si un utilisateur Telegram avec l’identifiant `123` envoie `/dock_discord`, OpenClaw stocke `lastChannel: "discord"` et `lastTo: "456"` sur la session active. Si l’expéditeur n’est pas lié à un pair Discord, la commande répond avec une indication de configuration au lieu de passer à la conversation normale.

Le docking modifie uniquement la route de session active. Il ne crée pas de comptes de canal, n’accorde pas d’accès, ne contourne pas les listes d’autorisation de canal et ne déplace pas l’historique de transcription vers une autre session. Utilisez `/dock-telegram`, `/dock-slack`, `/dock-mattermost` ou une autre commande de dock générée pour changer de nouveau la route.

### Commandes des plugins intégrés

Les plugins intégrés peuvent ajouter davantage de commandes slash. Commandes intégrées actuelles dans ce dépôt :

  * `/dreaming [on|off|status|help]` active ou désactive Dreaming pour la mémoire. Voir [Dreaming](</fr/concepts/dreaming>).
  * `/pair [qr|status|pending|approve|cleanup|notify]` gère le flux d’appairage/configuration d’appareil. Voir [Pairing](</fr/channels/pairing>).
  * `/phone status|arm <camera|screen|writes|all> [duration]|disarm` arme temporairement les commandes de nœud téléphonique à haut risque.
  * `/voice status|list [limit]|set <voiceId|name>` gère la configuration de voix Talk. Sur Discord, le nom de commande natif est `/talkvoice`.
  * `/card ...` envoie des préréglages de carte riche LINE. Voir [LINE](</fr/channels/line>).
  * `/codex status|models|threads|resume|compact|review|diagnostics|account|mcp|skills` inspecte et contrôle le harnais de serveur d’application Codex intégré. Voir [Codex harness](</fr/plugins/codex-harness>).
  * Commandes réservées à QQBot : 
    * `/bot-ping`
    * `/bot-version`
    * `/bot-help`
    * `/bot-upgrade`
    * `/bot-logs`


### Commandes de skill dynamiques

Les skills invocables par l’utilisateur sont également exposées comme commandes slash :

  * `/skill <name> [input]` fonctionne toujours comme point d’entrée générique.
  * les skills peuvent aussi apparaître comme commandes directes, par exemple `/prose`, lorsque la skill/le plugin les enregistre.
  * l’enregistrement natif des commandes de skill est contrôlé par `commands.nativeSkills` et `channels.<provider>.commands.nativeSkills`.
  * les spécifications de commande peuvent fournir `descriptionLocalizations` pour les surfaces natives qui prennent en charge les descriptions localisées, notamment Discord.


Notes sur les arguments et l’analyseur

  * Les commandes acceptent un `:` facultatif entre la commande et les arguments (par ex. `/think: high`, `/send: on`, `/help:`).
  * `/new <model>` accepte un alias de modèle, `provider/model` ou un nom de fournisseur (correspondance approximative) ; s’il n’y a aucune correspondance, le texte est traité comme le corps du message.
  * Pour une ventilation complète de l’utilisation des fournisseurs, utilisez `openclaw status --usage`.
  * `/allowlist add|remove` nécessite `commands.config=true` et respecte `configWrites` du canal.
  * Dans les canaux à plusieurs comptes, `/allowlist --account <id>` ciblé sur la configuration et `/config set channels.<provider>.accounts.<id>...` respectent également `configWrites` du compte cible.
  * `/usage` contrôle le pied de page d’utilisation par réponse ; `/usage cost` imprime un résumé local des coûts à partir des journaux de session OpenClaw.
  * `/restart` est activé par défaut ; définissez `commands.restart: false` pour le désactiver.
  * `/plugins install <spec>` accepte les mêmes spécifications de plugin que `openclaw plugins install` : chemin/archive local, paquet npm, `git:<repo>` ou `clawhub:<pkg>`, puis demande un redémarrage du Gateway parce que les modules sources du plugin ont changé.
  * `/plugins enable|disable` met à jour la configuration du plugin et déclenche le rechargement des plugins du Gateway pour les nouveaux tours d’agent.

Comportement propre aux canaux

  * Commande native réservée à Discord : `/vc join|leave|status` contrôle les canaux vocaux (non disponible en texte). `join` nécessite une guilde et un canal vocal/de scène sélectionné. Nécessite `channels.discord.voice` et les commandes natives.
  * Les commandes Discord de liaison de fil (`/focus`, `/unfocus`, `/agents`, `/session idle`, `/session max-age`) nécessitent l’activation effective des liaisons de fil (`session.threadBindings.enabled` et/ou `channels.discord.threadBindings.enabled`).
  * Référence des commandes ACP et comportement d’exécution : [ACP agents](</fr/tools/acp-agents>).

Sécurité de verbose / trace / fast / reasoning

  * `/verbose` est destiné au débogage et à une visibilité supplémentaire ; gardez-le **désactivé** en utilisation normale.
  * `/trace` est plus restreint que `/verbose` : il révèle uniquement les lignes de trace/débogage appartenant aux plugins et garde désactivé le bavardage verbose normal des outils.
  * `/fast on|off` conserve un remplacement de session. Utilisez l’option `inherit` de l’interface Sessions pour l’effacer et revenir aux valeurs par défaut de configuration.
  * `/fast` dépend du fournisseur : OpenAI/OpenAI Codex le mappe vers `service_tier=priority` sur les points de terminaison Responses natifs, tandis que les requêtes Anthropic publiques directes, y compris le trafic authentifié par OAuth envoyé à `api.anthropic.com`, le mappent vers `service_tier=auto` ou `standard_only`. Voir [OpenAI](</fr/providers/openai>) et [Anthropic](</fr/providers/anthropic>).
  * Les résumés d’échec d’outil restent affichés lorsqu’ils sont pertinents, mais le texte détaillé de l’échec n’est inclus que lorsque `/verbose` vaut `on` ou `full`.
  * `/reasoning`, `/verbose` et `/trace` sont risqués dans les contextes de groupe : ils peuvent révéler du raisonnement interne, la sortie d’outils ou des diagnostics de plugins que vous n’aviez pas l’intention d’exposer. Préférez les laisser désactivés, en particulier dans les discussions de groupe.

Changement de modèle

  * `/model` conserve immédiatement le nouveau modèle de session.
  * Si l’agent est inactif, la prochaine exécution l’utilise immédiatement.
  * Si une exécution est déjà active, OpenClaw marque un changement en direct comme en attente et ne redémarre sur le nouveau modèle qu’à un point de nouvelle tentative propre.
  * Si l’activité d’outil ou la sortie de réponse a déjà commencé, le changement en attente peut rester en file d’attente jusqu’à une occasion de nouvelle tentative ultérieure ou jusqu’au prochain tour utilisateur.
  * Dans la TUI locale, `/crestodian [request]` revient de la TUI d’agent normale à Crestodian. Cela est distinct du mode de secours des canaux de messages et n’accorde pas d’autorité de configuration distante.

Chemin rapide et raccourcis en ligne

  * **Chemin rapide :** les messages composés uniquement d’une commande provenant d’expéditeurs autorisés sont traités immédiatement (contournement de la file d’attente + du modèle).
  * **Filtrage par mention de groupe :** les messages composés uniquement d’une commande provenant d’expéditeurs autorisés contournent les exigences de mention.
  * **Raccourcis en ligne (expéditeurs autorisés uniquement) :** certaines commandes fonctionnent aussi lorsqu’elles sont intégrées dans un message normal et sont retirées avant que le modèle voie le texte restant. 
    * Exemple : `hey /status` déclenche une réponse de statut, et le texte restant continue dans le flux normal.
  * Actuellement : `/help`, `/commands`, `/status`, `/whoami` (`/id`).
  * Les messages non autorisés composés uniquement d’une commande sont ignorés silencieusement, et les jetons `/...` en ligne sont traités comme du texte brut.

Commandes de skill et arguments natifs

  * **Commandes de skill :** les skills `user-invocable` sont exposées comme commandes slash. Les noms sont normalisés en `a-z0-9_` (32 caractères max) ; les collisions reçoivent des suffixes numériques (par ex. `_2`). 
    * `/skill <name> [input]` exécute une skill par nom (utile lorsque les limites des commandes natives empêchent les commandes par skill).
    * Par défaut, les commandes de skill sont transmises au modèle comme une requête normale.
    * Les Skills peuvent éventuellement déclarer `command-dispatch: tool` pour acheminer la commande directement vers un outil (déterministe, sans modèle).
    * Exemple : `/prose` (plugin OpenProse) — voir [OpenProse](</fr/prose>).
  * **Arguments de commande natifs :** Discord utilise l’autocomplétion pour les options dynamiques (et des menus de boutons lorsque vous omettez des arguments obligatoires). Telegram et Slack affichent un menu de boutons lorsqu’une commande prend en charge des choix et que vous omettez l’argument. Les choix dynamiques sont résolus par rapport au modèle de session cible, de sorte que les options propres au modèle, comme les niveaux `/think`, suivent le remplacement `/model` de cette session.


## `/tools`

`/tools` répond à une question d’exécution, pas à une question de configuration : **ce que cet agent peut utiliser maintenant dans cette conversation**.

  * Le `/tools` par défaut est compact et optimisé pour une lecture rapide.
  * `/tools verbose` ajoute de courtes descriptions.
  * Les surfaces de commandes natives qui prennent en charge les arguments exposent le même changement de mode que `compact|verbose`.
  * Les résultats sont propres à la session ; changer d’agent, de canal, de fil, d’autorisation d’expéditeur ou de modèle peut donc modifier la sortie.
  * `/tools` inclut les outils réellement accessibles à l’exécution, y compris les outils cœur, les outils de plugins connectés et les outils appartenant aux canaux.


Pour modifier les profils et les remplacements, utilisez le panneau Tools de l’interface Control ou les surfaces de configuration/catalogue au lieu de traiter `/tools` comme un catalogue statique.

## Surfaces d’utilisation (ce qui apparaît où)

  * **Utilisation/quota du fournisseur** (exemple : "Claude 80% left") apparaît dans `/status` pour le fournisseur de modèle actuel lorsque le suivi de l’utilisation est activé. OpenClaw normalise les fenêtres des fournisseurs en `% left` ; pour MiniMax, les champs de pourcentage indiquant uniquement le restant sont inversés avant l’affichage, et les réponses `model_remains` privilégient l’entrée du modèle de discussion plus une étiquette de plan balisée par modèle.
  * **Lignes de tokens/cache** dans `/status` peuvent se replier sur la dernière entrée d’utilisation de la transcription lorsque l’instantané de session en direct est incomplet. Les valeurs en direct non nulles existantes restent prioritaires, et le repli sur la transcription peut aussi récupérer l’étiquette du modèle d’exécution actif ainsi qu’un total plus élevé orienté invite lorsque les totaux stockés sont absents ou plus petits.
  * **Exécution vs runtime :** `/status` indique `Execution` pour le chemin de sandbox effectif et `Runtime` pour ce qui exécute réellement la session : `OpenClaw Pi Default`, `OpenAI Codex`, un backend CLI ou un backend ACP.
  * **Tokens/coût par réponse** est contrôlé par `/usage off|tokens|full` (ajouté aux réponses normales).
  * `/model status` concerne les **modèles/authentification/points de terminaison** , pas l’utilisation.


## Sélection du modèle (`/model`)

`/model` est implémenté comme une directive.

Exemples :

CodeCopy code
[code]
    /model/model list/model 3/model openai/gpt-5.4/model opus@anthropic:default/model status
[/code]

Notes :

  * `/model` et `/model list` affichent un sélecteur compact et numéroté (famille de modèles + fournisseurs disponibles).
  * Sur Discord, `/model` et `/models` ouvrent un sélecteur interactif avec des listes déroulantes de fournisseur et de modèle, plus une étape Envoyer. Le sélecteur respecte `agents.defaults.models`, y compris les entrées `provider/*`, afin que la découverte limitée au fournisseur puisse maintenir le sélecteur sous la limite de 25 options de composant de Discord.
  * `/model <#>` sélectionne dans ce sélecteur (et privilégie le fournisseur actuel lorsque c’est possible).
  * `/model status` affiche la vue détaillée, y compris le point de terminaison du fournisseur configuré (`baseUrl`) et le mode API (`api`) lorsqu’ils sont disponibles.


## Remplacements de débogage

`/debug` vous permet de définir des remplacements de configuration **uniquement runtime** (mémoire, pas disque). Réservé au propriétaire. Désactivé par défaut ; activez avec `commands.debug: true`.

Exemples :

CodeCopy code
[code]
    /debug show/debug set messages.responsePrefix="[openclaw]"/debug set channels.whatsapp.allowFrom=["+1555","+4477"]/debug unset messages.responsePrefix/debug reset
[/code]

## Sortie de trace de Plugin

`/trace` vous permet d’activer ou désactiver les **lignes de trace/débogage de Plugin limitées à la session** sans activer le mode verbeux complet.

Exemples :

textCopy code
[code]
    /trace/trace on/trace off
[/code]

Notes :

  * `/trace` sans argument affiche l’état actuel de trace de la session.
  * `/trace on` active les lignes de trace de Plugin pour la session actuelle.
  * `/trace off` les désactive à nouveau.
  * Les lignes de trace de Plugin peuvent apparaître dans `/status` et sous forme de message de diagnostic de suivi après la réponse normale de l’assistant.
  * `/trace` ne remplace pas `/debug` ; `/debug` gère toujours les remplacements de configuration uniquement runtime.
  * `/trace` ne remplace pas `/verbose` ; la sortie verbeuse normale des outils/états relève toujours de `/verbose`.


## Mises à jour de configuration

`/config` écrit dans votre configuration sur disque (`openclaw.json`). Réservé au propriétaire. Désactivé par défaut ; activez avec `commands.config: true`.

Exemples :

CodeCopy code
[code]
    /config show/config show messages.responsePrefix/config get messages.responsePrefix/config set messages.responsePrefix="[openclaw]"/config unset messages.responsePrefix
[/code]

## Mises à jour MCP

`/mcp` écrit les définitions de serveurs MCP gérées par OpenClaw sous `mcp.servers`. Réservé au propriétaire. Désactivé par défaut ; activez avec `commands.mcp: true`.

Exemples :

textCopy code
[code]
    /mcp show/mcp show context7/mcp set context7={"command":"uvx","args":["context7-mcp"]}/mcp unset context7
[/code]

## Mises à jour de Plugin

`/plugins` permet aux opérateurs d’inspecter les plugins découverts et d’activer ou désactiver leur activation dans la configuration. Les flux en lecture seule peuvent utiliser `/plugin` comme alias. Désactivé par défaut ; activez avec `commands.plugins: true`.

Exemples :

textCopy code
[code]
    /plugins/plugins list/plugin show context7/plugins enable context7/plugins disable context7
[/code]

## Notes de surface

Sessions par surface

  * **Les commandes texte** s’exécutent dans la session de discussion normale (les messages privés partagent `main`, les groupes ont leur propre session).
  * **Les commandes natives** utilisent des sessions isolées : 
    * Discord : `agent:<agentId>:discord:slash:<userId>`
    * Slack : `agent:<agentId>:slack:slash:<userId>` (préfixe configurable via `channels.slack.slashCommand.sessionPrefix`)
    * Telegram : `telegram:slash:<userId>` (cible la session de discussion via `CommandTargetSessionKey`)
  * **`/stop`** cible la session de discussion active afin de pouvoir interrompre l’exécution en cours.

Spécificités de Slack

`channels.slack.slashCommand` reste pris en charge pour une commande unique de style `/openclaw`. Si vous activez `commands.native`, vous devez créer une commande slash Slack par commande intégrée (mêmes noms que `/help`). Les menus d’arguments de commande pour Slack sont fournis sous forme de boutons Block Kit éphémères.

Exception native Slack : enregistrez `/agentstatus` (et non `/status`) parce que Slack réserve `/status`. Le texte `/status` fonctionne toujours dans les messages Slack.

## Questions annexes BTW

`/btw` est une **question annexe** rapide sur la session actuelle. `/side` est un alias.

Contrairement à la discussion normale :

  * elle utilise la session actuelle comme contexte d’arrière-plan,
  * dans les sessions du harnais Codex, elle s’exécute comme un fil annexe Codex éphémère avec les autorisations Codex actuelles et la surface d’outils native,
  * dans les sessions non-Codex, elle conserve l’ancien comportement d’appel annexe direct en une seule fois,
  * elle ne modifie pas le contexte futur de la session,
  * elle n’est pas écrite dans l’historique de transcription,
  * elle est livrée comme résultat annexe en direct plutôt que comme message d’assistant normal.


Cela rend `/btw` utile lorsque vous voulez une clarification temporaire pendant que la tâche principale continue.

Exemple :

textCopy code
[code]
    /btw what are we doing right now?/side what changed while the main run continued?
[/code]

Consultez [Questions annexes BTW](</fr/tools/btw>) pour le comportement complet et les détails de l’UX client.

## Connexe

  * [Créer des Skills](</fr/tools/creating-skills>)
  * [Skills](</fr/tools/skills>)
  * [Configuration des Skills](</fr/tools/skills-config>)


Was this useful?YesNo