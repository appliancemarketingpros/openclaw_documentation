---
title: Approbations d’exécution
source_url: https://docs.openclaw.ai/fr/tools/exec-approvals
scraped_at: 2026-05-25
---

Les approbations d’exécution sont la **barrière de sécurité de l’app compagnon / de l’hôte Node** qui permet à un agent en bac à sable d’exécuter des commandes sur un hôte réel (`gateway` ou `node`). Un verrou de sécurité : les commandes ne sont autorisées que lorsque la stratégie + la liste d’autorisation + l’approbation utilisateur (facultative) concordent toutes. Les approbations d’exécution s’empilent **au-dessus de** la stratégie d’outils et du verrouillage d’élévation (sauf si l’élévation est définie sur `full`, ce qui ignore les approbations).

## Inspection de la stratégie effective

Commande | Ce qu’elle affiche  
---|---  
`openclaw approvals get` / `--gateway` / `--node <id|name|ip>` | Stratégie demandée, sources de stratégie de l’hôte, et résultat effectif.  
`openclaw exec-policy show` | Vue fusionnée de la machine locale.  
`openclaw exec-policy set` / `preset` | Synchronise la stratégie demandée locale avec le fichier local d’approbations de l’hôte en une étape.  
  
Lorsqu’un périmètre local demande `host=node`, `exec-policy show` signale ce périmètre comme géré par Node à l’exécution au lieu de prétendre que le fichier local d’approbations est la source de vérité.

Si l’interface de l’app compagnon n’est **pas disponible** , toute demande qui déclencherait normalement une invite est résolue par le **repli ask** (par défaut : `deny`).

## Où cela s’applique

Les approbations d’exécution sont appliquées localement sur l’hôte d’exécution :

  * **Hôte Gateway** → processus `openclaw` sur la machine Gateway.
  * **Hôte Node** → exécuteur Node (app compagnon macOS ou hôte Node sans interface).


### Modèle de confiance

  * Les appelants authentifiés auprès du Gateway sont des opérateurs de confiance pour ce Gateway.
  * Les Nodes appairés étendent cette capacité d’opérateur de confiance à l’hôte Node.
  * Les approbations d’exécution réduisent le risque d’exécution accidentelle, mais ne constituent **pas** une frontière d’authentification par utilisateur ni une stratégie de système de fichiers en lecture seule.
  * Une fois approuvée, une commande peut modifier des fichiers selon les permissions de l’hôte ou du système de fichiers du bac à sable sélectionné.
  * Les exécutions approuvées sur hôte Node lient le contexte d’exécution canonique : cwd canonique, argv exact, liaison d’environnement lorsqu’elle est présente, et chemin d’exécutable épinglé le cas échéant.
  * Pour les scripts shell et les invocations directes de fichiers d’interpréteur/runtime, OpenClaw tente aussi de lier un opérande de fichier local concret. Si ce fichier lié change après approbation mais avant exécution, l’exécution est refusée au lieu d’exécuter un contenu modifié.
  * La liaison de fichiers est volontairement au mieux, **pas** un modèle sémantique complet de chaque chemin de chargeur d’interpréteur/runtime. Si le mode d’approbation ne peut pas identifier exactement un fichier local concret à lier, il refuse de créer une exécution adossée à une approbation au lieu de prétendre couvrir tous les cas.


### Séparation macOS

  * Le **service hôte Node** transmet `system.run` à l’**app macOS** via l’IPC local.
  * L’**app macOS** applique les approbations et exécute la commande dans le contexte de l’interface utilisateur.


## Paramètres et stockage

Les approbations résident dans un fichier JSON local sur l’hôte d’exécution :

textCopy code
[code]
    ~/.openclaw/exec-approvals.json
[/code]

Exemple de schéma :

jsonCopy code
[code]
    {  "version": 1,  "socket": {    "path": "~/.openclaw/exec-approvals.sock",    "token": "base64url-token"  },  "defaults": {    "security": "deny",    "ask": "on-miss",    "askFallback": "deny",    "autoAllowSkills": false  },  "agents": {    "main": {      "security": "allowlist",      "ask": "on-miss",      "askFallback": "deny",      "autoAllowSkills": true,      "allowlist": [        {          "id": "B0C8C0B3-2C2D-4F8A-9A3C-5A4B3C2D1E0F",          "pattern": "~/Projects/**/bin/rg",          "source": "allow-always",          "commandText": "rg -n TODO",          "lastUsedAt": 1737150000000,          "lastUsedCommand": "rg -n TODO",          "lastResolvedPath": "/Users/user/Projects/.../bin/rg"        }      ]    }  }}
[/code]

## Boutons de stratégie

### `exec.security`

  * `deny` \- bloque toutes les demandes d’exécution sur l’hôte.
  * `allowlist` \- autorise uniquement les commandes de la liste d’autorisation.
  * `full` \- autorise tout (équivalent à l’élévation).


### `exec.ask`

  * `off` \- ne demande jamais.
  * `on-miss` \- demande uniquement lorsque la liste d’autorisation ne correspond pas.
  * `always` \- demande pour chaque commande. La confiance durable `allow-always` ne supprime **pas** les invites lorsque le mode ask effectif est `always`.


### `askFallback`

Résolution lorsqu’une invite est requise mais qu’aucune interface utilisateur n’est joignable.

  * `deny` \- bloque.
  * `allowlist` \- autorise uniquement si la liste d’autorisation correspond.
  * `full` \- autorise.


### `tools.exec.strictInlineEval`

Lorsque `true`, OpenClaw traite les formes d’évaluation de code en ligne comme nécessitant uniquement une approbation, même si le binaire de l’interpréteur lui-même figure dans la liste d’autorisation. Défense en profondeur pour les chargeurs d’interpréteur qui ne se mappent pas proprement à un opérande de fichier stable unique.

Exemples interceptés par le mode strict :

  * `python -c`
  * `node -e`, `node --eval`, `node -p`
  * `ruby -e`
  * `perl -e`, `perl -E`
  * `php -r`
  * `lua -e`
  * `osascript -e`


En mode strict, ces commandes nécessitent toujours une approbation explicite, et `allow-always` ne persiste pas automatiquement de nouvelles entrées de liste d’autorisation pour elles.

### `tools.exec.commandHighlighting`

Contrôle uniquement la présentation dans les invites d’approbation d’exécution. Lorsqu’il est activé, OpenClaw peut joindre des plages de commande dérivées du parseur afin que les invites d’approbation Web puissent mettre en évidence les jetons de commande. Définissez-le sur `true` pour activer la mise en évidence du texte des commandes.

Ce paramètre ne change **pas** `security`, `ask`, la correspondance de liste d’autorisation, le comportement strict d’évaluation en ligne, le transfert d’approbation ni l’exécution des commandes. Il peut être défini globalement sous `tools.exec.commandHighlighting` ou par agent sous `agents.list[].tools.exec.commandHighlighting`.

## Mode YOLO (sans approbation)

Si vous voulez que l’exécution sur l’hôte fonctionne sans invites d’approbation, vous devez ouvrir **les deux** couches de stratégie : la stratégie d’exécution demandée dans la configuration OpenClaw (`tools.exec.*`) **et** la stratégie d’approbations locale à l’hôte dans `~/.openclaw/exec-approvals.json`.

YOLO est le comportement d’hôte par défaut, sauf si vous le resserrez explicitement :

Couche | Paramètre YOLO  
---|---  
`tools.exec.security` | `full` sur `gateway`/`node`  
`tools.exec.ask` | `off`  
`askFallback` de l’hôte | `full`  
  
Les fournisseurs adossés à une CLI qui exposent leur propre mode d’autorisation non interactif peuvent suivre cette stratégie. Claude CLI ajoute `--permission-mode bypassPermissions` lorsque la stratégie d’exécution demandée par OpenClaw est YOLO. Remplacez ce comportement backend avec des arguments Claude explicites sous `agents.defaults.cliBackends.claude-cli.args` / `resumeArgs` \- par exemple `--permission-mode default`, `acceptEdits`, ou `bypassPermissions`.

Si vous voulez une configuration plus conservatrice, resserrez l’une ou l’autre couche à `allowlist` / `on-miss` ou `deny`.

### Configuration persistante « ne jamais demander » sur l’hôte Gateway

* ### Définir la stratégie de configuration demandée

bashCopy code
[code]
    openclaw config set tools.exec.host gatewayopenclaw config set tools.exec.security fullopenclaw config set tools.exec.ask offopenclaw gateway restart
[/code]

* ### Faire correspondre le fichier d’approbations de l’hôte

bashCopy code
[code]
    openclaw approvals set --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

### Raccourci local

bashCopy code
[code]
    openclaw exec-policy preset yolo
[/code]

Ce raccourci local met à jour les deux éléments :

  * `tools.exec.host/security/ask` local.
  * Les valeurs par défaut locales de `~/.openclaw/exec-approvals.json`.


Il est volontairement limité au local. Pour modifier à distance les approbations de l’hôte Gateway ou de l’hôte Node, utilisez `openclaw approvals set --gateway` ou `openclaw approvals set --node <id|name|ip>`.

### Hôte Node

Pour un hôte Node, appliquez plutôt le même fichier d’approbations sur ce Node :

bashCopy code
[code]
    openclaw approvals set --node <id|name|ip> --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

### Raccourci limité à la session

  * `/exec security=full ask=off` modifie uniquement la session actuelle.
  * `/elevated full` est un raccourci de dernier recours qui ignore aussi les approbations d’exécution pour cette session.


Si le fichier d’approbations de l’hôte reste plus strict que la configuration, la stratégie d’hôte plus stricte gagne tout de même.

## Liste d’autorisation (par agent)

Les listes d’autorisation sont **propres à chaque agent**. Si plusieurs agents existent, changez l’agent que vous modifiez dans l’app macOS. Les motifs sont des correspondances glob.

Les motifs peuvent être des globs de chemin binaire résolu ou des globs de nom de commande nu. Les noms nus ne correspondent qu’aux commandes invoquées via `PATH`, donc `rg` peut correspondre à `/opt/homebrew/bin/rg` lorsque la commande est `rg`, mais **pas** à `./rg` ni à `/tmp/rg`. Utilisez un glob de chemin lorsque vous voulez faire confiance à un emplacement binaire spécifique.

Les entrées héritées `agents.default` sont migrées vers `agents.main` au chargement. Les chaînes shell comme `echo ok && pwd` doivent toujours avoir chaque segment de premier niveau conforme aux règles de la liste d’autorisation.

Exemples :

  * `rg`
  * `~/Projects/**/bin/peekaboo`
  * `~/.local/bin/*`
  * `/opt/homebrew/bin/rg`


### Restriction des arguments avec argPattern

Ajoutez `argPattern` lorsqu’une entrée de liste d’autorisation doit correspondre à un binaire et à une forme d’arguments spécifique. OpenClaw évalue l’expression régulière sur les arguments de commande analysés, en excluant le jeton exécutable (`argv[0]`). Pour les entrées écrites à la main, les arguments sont joints avec un seul espace ; ancrez donc le motif lorsque vous avez besoin d’une correspondance exacte.

jsonCopy code
[code]
    {  "version": 1,  "agents": {    "main": {      "allowlist": [        {          "pattern": "python3",          "argPattern": "^safe\\.py$"        }      ]    }  }}
[/code]

Cette entrée autorise `python3 safe.py` ; `python3 other.py` est une absence de correspondance avec la liste d’autorisation. Si une entrée portant uniquement sur le chemin pour le même binaire est aussi présente, les arguments non correspondants peuvent toujours se rabattre sur cette entrée limitée au chemin. Omettez l’entrée limitée au chemin lorsque l’objectif est de restreindre le binaire aux arguments déclarés.

Les entrées enregistrées par les flux d’approbation peuvent utiliser un format de séparateur interne pour une correspondance exacte avec argv. Préférez l’interface utilisateur ou le flux d’approbation pour régénérer ces entrées plutôt que de modifier manuellement la valeur encodée. Si OpenClaw ne peut pas analyser argv pour un segment de commande, les entrées avec `argPattern` ne correspondent pas.

Chaque entrée de liste d’autorisation prend en charge :

Champ | Signification  
---|---  
`pattern` | Glob du chemin binaire résolu ou glob du nom de commande brut  
`argPattern` | Regex argv facultative ; les entrées omises ne portent que sur le chemin  
`id` | UUID stable utilisé pour l’identité dans l’interface utilisateur  
`source` | Source de l’entrée, comme `allow-always`  
`commandText` | Texte de commande capturé lorsqu’un flux d’approbation a créé l’entrée  
`lastUsedAt` | Horodatage de dernière utilisation  
`lastUsedCommand` | Dernière commande ayant correspondu  
`lastResolvedPath` | Dernier chemin binaire résolu  
  
## CLI de Skills autorisés automatiquement

Lorsque **CLI de Skills autorisés automatiquement** est activé, les exécutables référencés par les Skills connus sont traités comme autorisés sur les nœuds (nœud macOS ou hôte de nœud sans interface graphique). Cela utilise `skills.bins` via le RPC du Gateway pour récupérer la liste des binaires de Skills. Désactivez cette option si vous voulez des listes d’autorisation manuelles strictes.

## Binaires sûrs et transfert des approbations

Pour les binaires sûrs (le chemin rapide uniquement stdin), les détails de liaison des interpréteurs et la façon de transférer les invites d’approbation vers Slack/Discord/Telegram (ou de les exécuter comme clients d’approbation natifs), consultez [Approbations exec - avancé](</fr/tools/exec-approvals-advanced>).

## Modification dans l’interface de contrôle

Utilisez la carte **Interface de contrôle → Nœuds → Approbations exec** pour modifier les valeurs par défaut, les remplacements par agent et les listes d’autorisation. Choisissez une portée (Valeurs par défaut ou un agent), ajustez la stratégie, ajoutez/supprimez des motifs de liste d’autorisation, puis cliquez sur **Enregistrer**. L’interface utilisateur affiche les métadonnées de dernière utilisation par motif afin que vous puissiez garder la liste propre.

Le sélecteur de cible choisit **Gateway** (approbations locales) ou un **Nœud**. Les nœuds doivent annoncer `system.execApprovals.get/set` (application macOS ou hôte de nœud sans interface graphique). Si un nœud n’annonce pas encore les approbations exec, modifiez directement son fichier local `~/.openclaw/exec-approvals.json`.

CLI : `openclaw approvals` prend en charge la modification du gateway ou d’un nœud - voir [CLI des approbations](</fr/cli/approvals>).

## Flux d’approbation

Lorsqu’une invite est requise, le gateway diffuse `exec.approval.requested` aux clients opérateurs. L’interface de contrôle et l’application macOS la résolvent via `exec.approval.resolve`, puis le gateway transfère la requête approuvée à l’hôte du nœud.

Pour `host=node`, les requêtes d’approbation incluent une charge utile `systemRunPlan` canonique. Le gateway utilise ce plan comme contexte de commande/cwd/session faisant autorité lors du transfert des requêtes `system.run` approuvées.

C’est important pour la latence des approbations asynchrones :

  * Le chemin exec du nœud prépare un plan canonique dès le départ.
  * L’enregistrement d’approbation stocke ce plan et ses métadonnées de liaison.
  * Une fois approuvé, l’appel final transféré à `system.run` réutilise le plan stocké au lieu de faire confiance à des modifications ultérieures de l’appelant.
  * Si l’appelant modifie `command`, `rawCommand`, `cwd`, `agentId` ou `sessionKey` après la création de la requête d’approbation, le gateway rejette l’exécution transférée comme non-concordance d’approbation.


## Événements système

Le cycle de vie exec est exposé sous forme de messages système :

  * `Exec running` (uniquement si la commande dépasse le seuil de notification d’exécution).
  * `Exec finished`.
  * `Exec denied`.


Ils sont publiés dans la session de l’agent après que le nœud a signalé l’événement. Les approbations exec hébergées par le Gateway émettent les mêmes événements de cycle de vie lorsque la commande se termine (et, facultativement, lorsqu’elle s’exécute plus longtemps que le seuil). Les execs soumises à approbation réutilisent l’identifiant d’approbation comme `runId` dans ces messages pour faciliter la corrélation.

## Comportement en cas d’approbation refusée

Lorsqu’une approbation exec asynchrone est refusée, OpenClaw empêche l’agent de réutiliser la sortie d’une exécution antérieure de la même commande dans la session. Le motif du refus est transmis avec des consignes explicites indiquant qu’aucune sortie de commande n’est disponible, ce qui empêche l’agent d’affirmer qu’il existe une nouvelle sortie ou de répéter la commande refusée avec des résultats obsolètes provenant d’une exécution réussie précédente.

## Implications

  * **`full`** est puissant ; préférez les listes d’autorisation lorsque c’est possible.
  * **`ask`** vous garde dans la boucle tout en permettant des approbations rapides.
  * Les listes d’autorisation par agent empêchent les approbations d’un agent de se propager aux autres.
  * Les approbations ne s’appliquent qu’aux requêtes exec d’hôte provenant d’**expéditeurs autorisés**. Les expéditeurs non autorisés ne peuvent pas émettre `/exec`.
  * `/exec security=full` est une commodité au niveau de la session pour les opérateurs autorisés et ignore les approbations par conception. Pour bloquer strictement l’exec d’hôte, définissez la sécurité des approbations sur `deny` ou refusez l’outil `exec` via la stratégie d’outils.


## Connexe

[**Approbations exec - avancé** Binaires sûrs, liaison d’interpréteur et transfert des approbations vers le chat. ](</fr/tools/exec-approvals-advanced>) [**Outil exec** Outil d’exécution de commandes shell. ](</fr/tools/exec>) [**Mode élevé** Chemin d’urgence qui ignore aussi les approbations. ](</fr/tools/elevated>) [**Sandboxing** Modes de sandbox et accès à l’espace de travail. ](</fr/gateway/sandboxing>) [**Sécurité** Modèle de sécurité et durcissement. ](</fr/gateway/security>) [**Sandbox vs stratégie d’outils vs mode élevé** Quand utiliser chaque contrôle. ](</fr/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Skills** Comportement d’autorisation automatique fondé sur les Skills. ](</fr/tools/skills>)

Was this useful?YesNo