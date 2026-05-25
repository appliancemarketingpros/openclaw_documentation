---
title: Twitch
source_url: https://docs.openclaw.ai/fr/channels/twitch
scraped_at: 2026-05-25
---

Prise en charge du chat Twitch via une connexion IRC. OpenClaw se connecte en tant qu’utilisateur Twitch (compte de bot) pour recevoir et envoyer des messages dans les chaînes.

## Plugin intégré

Si vous utilisez un build plus ancien ou une installation personnalisée qui exclut Twitch, installez directement le paquet npm :

### npm registry

bashCopy code
[code]
    openclaw plugins install @openclaw/twitch
[/code]

### Local checkout

bashCopy code
[code]
    openclaw plugins install ./path/to/local/twitch-plugin
[/code]

Utilisez le paquet nu pour suivre l’étiquette de version officielle actuelle. N’épinglez une version exacte que lorsque vous avez besoin d’une installation reproductible.

Détails : [Plugins](</fr/tools/plugin>)

## Configuration rapide (débutant)

* ### Ensure plugin is available

Les versions empaquetées actuelles d’OpenClaw l’intègrent déjà. Les installations plus anciennes/personnalisées peuvent l’ajouter manuellement avec les commandes ci-dessus.

* ### Create a Twitch bot account

Créez un compte Twitch dédié pour le bot (ou utilisez un compte existant).

* ### Generate credentials

Utilisez [Twitch Token Generator](<https://twitchtokengenerator.com/>) :

  * Sélectionnez **Bot Token**
  * Vérifiez que les portées `chat:read` et `chat:write` sont sélectionnées
  * Copiez le **Client ID** et l’**Access Token**


* ### Find your Twitch user ID

Utilisez <https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/> pour convertir un nom d’utilisateur en ID utilisateur Twitch.

* ### Configure the token

  * Env : `OPENCLAW_TWITCH_ACCESS_TOKEN=...` (compte par défaut uniquement)
  * Ou config : `channels.twitch.accessToken`


Si les deux sont définis, la configuration est prioritaire (le repli sur l’env concerne uniquement le compte par défaut).

* ### Start the gateway

Démarrez le Gateway avec la chaîne configurée.

Configuration minimale :

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw", // Bot's Twitch account      accessToken: "oauth:abc123...", // OAuth Access Token (or use OPENCLAW_TWITCH_ACCESS_TOKEN env var)      clientId: "xyz789...", // Client ID from Token Generator      channel: "vevisk", // Which Twitch channel's chat to join (required)      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only - get it from https://www.streamweasels.com/tools/convert-twitch-username-to-user-id/    },  },}
[/code]

## Ce que c’est

  * Une chaîne Twitch détenue par le Gateway.
  * Routage déterministe : les réponses retournent toujours vers Twitch.
  * Chaque compte correspond à une clé de session isolée `agent:<agentId>:twitch:<accountName>`.
  * `username` est le compte du bot (celui qui s’authentifie), `channel` est le salon de chat à rejoindre.


## Configuration (détaillée)

### Générer les identifiants

Utilisez [Twitch Token Generator](<https://twitchtokengenerator.com/>) :

  * Sélectionnez **Bot Token**
  * Vérifiez que les portées `chat:read` et `chat:write` sont sélectionnées
  * Copiez le **Client ID** et l’**Access Token**


### Configurer le bot

### Env var (default account only)

bashCopy code
[code]
    OPENCLAW_TWITCH_ACCESS_TOKEN=oauth:abc123...
[/code]

### Config

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",    },  },}
[/code]

Si l’env et la configuration sont tous deux définis, la configuration est prioritaire.

### Contrôle d’accès (recommandé)

json5Copy code
[code]
    {  channels: {    twitch: {      allowFrom: ["123456789"], // (recommended) Your Twitch user ID only    },  },}
[/code]

Préférez `allowFrom` pour une liste d’autorisation stricte. Utilisez plutôt `allowedRoles` si vous souhaitez un accès basé sur les rôles.

**Rôles disponibles :** `"moderator"`, `"owner"`, `"vip"`, `"subscriber"`, `"all"`.

## Actualisation du jeton (facultatif)

Les jetons de [Twitch Token Generator](<https://twitchtokengenerator.com/>) ne peuvent pas être actualisés automatiquement ; régénérez-les lorsqu’ils expirent.

Pour l’actualisation automatique du jeton, créez votre propre application Twitch dans la [Twitch Developer Console](<https://dev.twitch.tv/console>) et ajoutez ceci à la configuration :

json5Copy code
[code]
    {  channels: {    twitch: {      clientSecret: "your_client_secret",      refreshToken: "your_refresh_token",    },  },}
[/code]

Le bot actualise automatiquement les jetons avant expiration et journalise les événements d’actualisation.

## Prise en charge multi-comptes

Utilisez `channels.twitch.accounts` avec des jetons propres à chaque compte. Consultez [Configuration](</fr/gateway/configuration>) pour le modèle partagé.

Exemple (un compte de bot dans deux chaînes) :

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        channel1: {          username: "openclaw",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "vevisk",        },        channel2: {          username: "openclaw",          accessToken: "oauth:def456...",          clientId: "uvw012...",          channel: "secondchannel",        },      },    },  },}
[/code]

## Contrôle d’accès

### User ID allowlist (most secure)

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowFrom: ["123456789", "987654321"],        },      },    },  },}
[/code]

### Role-based

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          allowedRoles: ["moderator", "vip"],        },      },    },  },}
[/code]

`allowFrom` est une liste d’autorisation stricte. Lorsqu’elle est définie, seuls ces ID utilisateur sont autorisés. Si vous souhaitez un accès basé sur les rôles, laissez `allowFrom` non défini et configurez plutôt `allowedRoles`.

### Disable @mention requirement

Par défaut, `requireMention` vaut `true`. Pour le désactiver et répondre à tous les messages :

json5Copy code
[code]
    {  channels: {    twitch: {      accounts: {        default: {          requireMention: false,        },      },    },  },}
[/code]

## Dépannage

Commencez par exécuter les commandes de diagnostic :

bashCopy code
[code]
    openclaw doctoropenclaw channels status --probe
[/code]

Bot does not respond to messages

  * **Vérifiez le contrôle d’accès :** Assurez-vous que votre ID utilisateur figure dans `allowFrom`, ou supprimez temporairement `allowFrom` et définissez `allowedRoles: ["all"]` pour tester.
  * **Vérifiez que le bot est dans la chaîne :** Le bot doit rejoindre la chaîne spécifiée dans `channel`.

Token issues

« Échec de la connexion » ou erreurs d’authentification :

  * Vérifiez que `accessToken` est la valeur du jeton d’accès OAuth (elle commence généralement par le préfixe `oauth:`)
  * Vérifiez que le jeton possède les portées `chat:read` et `chat:write`
  * Si vous utilisez l’actualisation du jeton, vérifiez que `clientSecret` et `refreshToken` sont définis

Token refresh not working

Consultez les journaux pour les événements d’actualisation :

CodeCopy code
[code]
    Using env token source for mybotAccess token refreshed for user 123456 (expires in 14400s)
[/code]

Si vous voyez « token refresh disabled (no refresh token) » :

  * Assurez-vous que `clientSecret` est fourni
  * Assurez-vous que `refreshToken` est fourni


## Configuration

### Configuration du compte

Nom d’utilisateur du bot.

Jeton d’accès OAuth avec `chat:read` et `chat:write`.

Twitch Client ID (depuis Token Generator ou votre application).

Chaîne à rejoindre.

Activer ce compte.

Facultatif : pour l’actualisation automatique du jeton.

Facultatif : pour l’actualisation automatique du jeton.

Expiration du jeton en secondes.

Horodatage d’obtention du jeton.

Liste d’autorisation des ID utilisateur.

Exiger une @mention.

### Options du fournisseur

  * `channels.twitch.enabled` \- Activer/désactiver le démarrage de la chaîne
  * `channels.twitch.username` \- Nom d’utilisateur du bot (configuration simplifiée à compte unique)
  * `channels.twitch.accessToken` \- Jeton d’accès OAuth (configuration simplifiée à compte unique)
  * `channels.twitch.clientId` \- Twitch Client ID (configuration simplifiée à compte unique)
  * `channels.twitch.channel` \- Chaîne à rejoindre (configuration simplifiée à compte unique)
  * `channels.twitch.accounts.<accountName>` \- Configuration multi-comptes (tous les champs de compte ci-dessus)


Exemple complet :

json5Copy code
[code]
    {  channels: {    twitch: {      enabled: true,      username: "openclaw",      accessToken: "oauth:abc123...",      clientId: "xyz789...",      channel: "vevisk",      clientSecret: "secret123...",      refreshToken: "refresh456...",      allowFrom: ["123456789"],      allowedRoles: ["moderator", "vip"],      accounts: {        default: {          username: "mybot",          accessToken: "oauth:abc123...",          clientId: "xyz789...",          channel: "your_channel",          enabled: true,          clientSecret: "secret123...",          refreshToken: "refresh456...",          expiresIn: 14400,          obtainmentTimestamp: 1706092800000,          allowFrom: ["123456789", "987654321"],          allowedRoles: ["moderator"],        },      },    },  },}
[/code]

## Actions d’outil

L’agent peut appeler `twitch` avec l’action :

  * `send` \- Envoyer un message à une chaîne


Exemple :

json5Copy code
[code]
    {  action: "twitch",  params: {    message: "Hello Twitch!",    to: "#mychannel",  },}
[/code]

## Sécurité et opérations

  * **Traitez les jetons comme des mots de passe** — Ne validez jamais de jetons dans git.
  * **Utilisez l’actualisation automatique des jetons** pour les bots de longue durée.
  * **Utilisez des listes d’autorisation d’ID utilisateur** plutôt que des noms d’utilisateur pour le contrôle d’accès.
  * **Surveillez les journaux** pour les événements d’actualisation des jetons et l’état de connexion.
  * **Limitez les portées des jetons au minimum** — Ne demandez que `chat:read` et `chat:write`.
  * **Si vous êtes bloqué** : Redémarrez le Gateway après avoir confirmé qu’aucun autre processus ne possède la session.


## Limites

  * **500 caractères** par message (découpage automatique aux limites de mots).
  * Le Markdown est supprimé avant le découpage.
  * Aucune limitation de débit (utilise les limites de débit intégrées de Twitch).


## Connexe

  * [Routage des chaînes](</fr/channels/channel-routing>) — routage de session pour les messages
  * [Vue d’ensemble des chaînes](</fr/channels>) — toutes les chaînes prises en charge
  * [Groupes](</fr/channels/groups>) — comportement des chats de groupe et filtrage par mention
  * [Appairage](</fr/channels/pairing>) — authentification en DM et flux d’appairage
  * [Sécurité](</fr/gateway/security>) — modèle d’accès et durcissement


Was this useful?YesNo