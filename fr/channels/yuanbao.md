---
title: Yuanbao
source_url: https://docs.openclaw.ai/fr/channels/yuanbao
scraped_at: 2026-05-25
---

Tencent Yuanbao est la plateforme d’assistant IA de Tencent. Le Plugin de canal OpenClaw connecte les bots Yuanbao à OpenClaw via WebSocket afin qu’ils puissent interagir avec les utilisateurs dans des messages directs et des discussions de groupe.

**État :** prêt pour la production pour les DM de bot et les discussions de groupe. WebSocket est le seul mode de connexion pris en charge.

* * *

## Démarrage rapide

> **Nécessite OpenClaw 2026.4.10 ou version ultérieure.** Exécutez `openclaw --version` pour vérifier. Mettez à niveau avec `openclaw update`.

* ### Ajoutez le canal Yuanbao avec vos identifiants

bashCopy code
[code]
    openclaw channels add --channel yuanbao --token "appKey:appSecret"
[/code]

La valeur `--token` utilise le format `appKey:appSecret` séparé par deux-points. Vous pouvez les obtenir depuis l’app Yuanbao en créant un robot dans les paramètres de votre application.

* ### Une fois la configuration terminée, redémarrez le Gateway pour appliquer les changements

bashCopy code
[code]
    openclaw gateway restart
[/code]

### Configuration interactive (alternative)

Vous pouvez aussi utiliser l’assistant interactif :

bashCopy code
[code]
    openclaw channels login --channel yuanbao
[/code]

Suivez les invites pour saisir votre ID d’app et votre secret d’app.

* * *

## Contrôle d’accès

### Messages directs

Configurez `dmPolicy` pour contrôler qui peut envoyer un DM au bot :

  * `"pairing"` \- les utilisateurs inconnus reçoivent un code d’appairage ; approuvez via la CLI
  * `"allowlist"` \- seuls les utilisateurs listés dans `allowFrom` peuvent discuter
  * `"open"` \- autorise tous les utilisateurs (par défaut)
  * `"disabled"` \- désactive tous les DM


**Approuver une demande d’appairage :**

bashCopy code
[code]
    openclaw pairing list yuanbaoopenclaw pairing approve yuanbao &lt;CODE&gt;
[/code]

### Discussions de groupe

**Exigence de mention** (`channels.yuanbao.requireMention`) :

  * `true` \- exige une @mention (par défaut)
  * `false` \- répond sans @mention


Répondre au message du bot dans une discussion de groupe est traité comme une mention implicite.

* * *

## Exemples de configuration

### Configuration de base avec une politique de DM ouverte

json5Copy code
[code]
    {  channels: {    yuanbao: {      appKey: "your_app_key",      appSecret: "your_app_secret",      dm: {        policy: "open",      },    },  },}
[/code]

### Restreindre les DM à des utilisateurs spécifiques

json5Copy code
[code]
    {  channels: {    yuanbao: {      appKey: "your_app_key",      appSecret: "your_app_secret",      dm: {        policy: "allowlist",        allowFrom: ["user_id_1", "user_id_2"],      },    },  },}
[/code]

### Désactiver l’exigence de @mention dans les groupes

json5Copy code
[code]
    {  channels: {    yuanbao: {      requireMention: false,    },  },}
[/code]

### Optimiser la livraison des messages sortants

json5Copy code
[code]
    {  channels: {    yuanbao: {      // Send each chunk immediately without buffering      outboundQueueStrategy: "immediate",    },  },}
[/code]

### Ajuster la stratégie merge-text

json5Copy code
[code]
    {  channels: {    yuanbao: {      outboundQueueStrategy: "merge-text",      minChars: 2800, // buffer until this many chars      maxChars: 3000, // force split above this limit      idleMs: 5000, // auto-flush after idle timeout (ms)    },  },}
[/code]

* * *

## Commandes courantes

Commande | Description  
---|---  
`/help` | Afficher les commandes disponibles  
`/status` | Afficher l’état du bot  
`/new` | Démarrer une nouvelle session  
`/stop` | Arrêter l’exécution en cours  
`/restart` | Redémarrer OpenClaw  
`/compact` | Compacter le contexte de la session  
  
> Yuanbao prend en charge les menus natifs de commandes slash. Les commandes sont synchronisées automatiquement avec la plateforme au démarrage du Gateway.

* * *

## Dépannage

### Le bot ne répond pas dans les discussions de groupe

  1. Vérifiez que le bot est ajouté au groupe
  2. Vérifiez que vous @mentionnez le bot (requis par défaut)
  3. Consultez les journaux : `openclaw logs --follow`


### Le bot ne reçoit pas les messages

  1. Vérifiez que le bot est créé et approuvé dans l’app Yuanbao
  2. Vérifiez que `appKey` et `appSecret` sont correctement configurés
  3. Vérifiez que le Gateway est en cours d’exécution : `openclaw gateway status`
  4. Consultez les journaux : `openclaw logs --follow`


### Le bot envoie des réponses vides ou de secours

  1. Vérifiez si le modèle d’IA renvoie du contenu valide
  2. La réponse de secours par défaut est : "暂时无法解答，你可以换个问题问问我哦"
  3. Personnalisez-la via `channels.yuanbao.fallbackReply`


### Secret d’app divulgué

  1. Réinitialisez le secret d’app dans YuanBao APP
  2. Mettez à jour la valeur dans votre configuration
  3. Redémarrez le Gateway : `openclaw gateway restart`


* * *

## Configuration avancée

### Comptes multiples

json5Copy code
[code]
    {  channels: {    yuanbao: {      defaultAccount: "main",      accounts: {        main: {          appKey: "key_xxx",          appSecret: "secret_xxx",          name: "Primary bot",        },        backup: {          appKey: "key_yyy",          appSecret: "secret_yyy",          name: "Backup bot",          enabled: false,        },      },    },  },}
[/code]

`defaultAccount` contrôle le compte utilisé lorsque les API sortantes ne spécifient pas d’`accountId`.

### Limites de messages

  * `maxChars` \- nombre maximal de caractères pour un seul message (par défaut : `3000` caractères)
  * `mediaMaxMb` \- limite d’envoi/téléchargement de médias (par défaut : `20` Mo)
  * `overflowPolicy` \- comportement lorsque le message dépasse la limite : `"split"` (par défaut) ou `"stop"`


### Streaming

Yuanbao prend en charge la sortie en Streaming au niveau des blocs. Lorsqu’elle est activée, le bot envoie le texte par segments au fur et à mesure de sa génération.

json5Copy code
[code]
    {  channels: {    yuanbao: {      disableBlockStreaming: false, // block streaming enabled (default)    },  },}
[/code]

Définissez `disableBlockStreaming: true` pour envoyer la réponse complète dans un seul message.

### Contexte d’historique des discussions de groupe

Contrôlez le nombre de messages historiques inclus dans le contexte IA pour les discussions de groupe :

json5Copy code
[code]
    {  channels: {    yuanbao: {      historyLimit: 100, // default: 100, set 0 to disable    },  },}
[/code]

### Mode de réponse à

Contrôlez la façon dont le bot cite les messages lorsqu’il répond dans les discussions de groupe :

json5Copy code
[code]
    {  channels: {    yuanbao: {      replyToMode: "first", // "off" | "first" | "all" (default: "first")    },  },}
[/code]

Valeur | Comportement  
---|---  
`"off"` | Aucune réponse citée  
`"first"` | Citer uniquement la première réponse par message entrant (par défaut)  
`"all"` | Citer chaque réponse  
  
### Injection d’indice Markdown

Par défaut, le bot injecte des instructions dans l’invite système pour empêcher le modèle d’IA d’envelopper toute la réponse dans des blocs de code markdown.

json5Copy code
[code]
    {  channels: {    yuanbao: {      markdownHintEnabled: true, // default: true    },  },}
[/code]

### Mode de débogage

Activez la sortie de journal non assainie pour des ID de bots spécifiques :

json5Copy code
[code]
    {  channels: {    yuanbao: {      debugBotIds: ["bot_user_id_1", "bot_user_id_2"],    },  },}
[/code]

### Routage multi-agent

Utilisez `bindings` pour router les DM ou groupes Yuanbao vers différents agents.

json5Copy code
[code]
    {  agents: {    list: [      { id: "main" },      { id: "agent-a", workspace: "/home/user/agent-a" },      { id: "agent-b", workspace: "/home/user/agent-b" },    ],  },  bindings: [    {      agentId: "agent-a",      match: {        channel: "yuanbao",        peer: { kind: "direct", id: "user_xxx" },      },    },    {      agentId: "agent-b",      match: {        channel: "yuanbao",        peer: { kind: "group", id: "group_zzz" },      },    },  ],}
[/code]

Champs de routage :

  * `match.channel` : `"yuanbao"`
  * `match.peer.kind` : `"direct"` (DM) ou `"group"` (discussion de groupe)
  * `match.peer.id` : ID utilisateur ou code de groupe


* * *

## Référence de configuration

Configuration complète : [Configuration du Gateway](</fr/gateway/configuration>)

Paramètre | Description | Valeur par défaut  
---|---|---  
`channels.yuanbao.enabled` | Activer/désactiver le canal | `true`  
`channels.yuanbao.defaultAccount` | Compte par défaut pour le routage sortant | `default`  
`channels.yuanbao.accounts.<id>.appKey` | Clé d’app (utilisée pour la signature et la génération de ticket) | -  
`channels.yuanbao.accounts.<id>.appSecret` | Secret d’app (utilisé pour la signature) | -  
`channels.yuanbao.accounts.<id>.token` | Jeton pré-signé (ignore la signature automatique de ticket) | -  
`channels.yuanbao.accounts.<id>.name` | Nom d’affichage du compte | -  
`channels.yuanbao.accounts.<id>.enabled` | Activer/désactiver un compte spécifique | `true`  
`channels.yuanbao.dm.policy` | Politique de DM | `open`  
`channels.yuanbao.dm.allowFrom` | Liste d’autorisation DM (liste d’ID utilisateur) | -  
`channels.yuanbao.requireMention` | Exiger une @mention dans les groupes | `true`  
`channels.yuanbao.overflowPolicy` | Gestion des messages longs (`split` ou `stop`) | `split`  
`channels.yuanbao.replyToMode` | Stratégie de réponse à en groupe (`off`, `first`, `all`) | `first`  
`channels.yuanbao.outboundQueueStrategy` | Stratégie sortante (`merge-text` ou `immediate`) | `merge-text`  
`channels.yuanbao.minChars` | Merge-text : caractères min. pour déclencher l’envoi | `2800`  
`channels.yuanbao.maxChars` | Merge-text : caractères max. par message | `3000`  
`channels.yuanbao.idleMs` | Merge-text : délai d’inactivité avant vidage automatique (ms) | `5000`  
`channels.yuanbao.mediaMaxMb` | Limite de taille des médias (Mo) | `20`  
`channels.yuanbao.historyLimit` | Entrées de contexte d’historique de discussion de groupe | `100`  
`channels.yuanbao.disableBlockStreaming` | Désactiver la sortie en Streaming au niveau des blocs | `false`  
`channels.yuanbao.fallbackReply` | Réponse de secours lorsque l’IA ne renvoie aucun contenu | `暂时无法解答，你可以换个问题问问我哦`  
`channels.yuanbao.markdownHintEnabled` | Injecter des instructions anti-enveloppement markdown | `true`  
`channels.yuanbao.debugBotIds` | ID de bots de liste blanche de débogage (journaux non assainis) | `[]`  
  
* * *

## Types de messages pris en charge

### Réception

  * ✅ Texte
  * ✅ Images
  * ✅ Fichiers
  * ✅ Audio / Voix
  * ✅ Vidéo
  * ✅ Stickers / Émojis personnalisés
  * ✅ Éléments personnalisés (cartes de liens, etc.)


### Envoi

  * ✅ Texte (avec prise en charge markdown)
  * ✅ Images
  * ✅ Fichiers
  * ✅ Audio
  * ✅ Vidéo
  * ✅ Stickers


### Fils et réponses

  * ✅ Réponses citées (configurables via `replyToMode`)
  * ❌ Réponses de fil (non prises en charge par la plateforme)


* * *

## Liens connexes

  * [Vue d’ensemble des canaux](</fr/channels>) \- tous les canaux pris en charge
  * [Appairage](</fr/channels/pairing>) \- authentification DM et flux d’appairage
  * [Groupes](</fr/channels/groups>) \- comportement des discussions de groupe et contrôle par mention
  * [Routage des canaux](</fr/channels/channel-routing>) \- routage de session pour les messages
  * [Sécurité](</fr/gateway/security>) \- modèle d’accès et renforcement


Was this useful?YesNo