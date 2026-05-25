---
title: ClickClack
source_url: https://docs.openclaw.ai/fr/channels/clickclack
scraped_at: 2026-05-25
---

ClickClack connecte OpenClaw à un espace de travail ClickClack auto-hébergé au moyen de jetons de bot ClickClack de première classe.

Utilisez ceci lorsque vous voulez qu’un agent OpenClaw apparaisse comme un utilisateur bot ClickClack. ClickClack prend en charge des bots de service indépendants et des bots appartenant à un utilisateur ; les bots appartenant à un utilisateur conservent un `owner_user_id` et ne reçoivent que les portées de jeton que vous accordez.

## Configuration rapide

Créez un jeton de bot dans ClickClack :

bashCopy code
[code]
    clickclack admin bot create \  --workspace <workspace_id_or_slug> \  --name "OpenClaw" \  --handle openclaw \  --scopes bot:write \  --plain
[/code]

Pour un bot appartenant à un utilisateur, ajoutez `--owner <user_id>`.

Configurez OpenClaw :

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      token: { source: "env", provider: "default", id: "CLICKCLACK_BOT_TOKEN" },      workspace: "default",      defaultTo: "channel:general",      agentId: "clickclack-bot",      replyMode: "model",    },  },}
[/code]

Puis exécutez :

bashCopy code
[code]
    export CLICKCLACK_BOT_TOKEN="ccb_..."openclaw gateway
[/code]

## Plusieurs bots

Chaque compte ouvre sa propre connexion temps réel ClickClack et utilise son propre jeton de bot.

json5Copy code
[code]
    {  plugins: {    entries: {      clickclack: {        llm: {          allowAgentIdOverride: true,        },      },    },  },  channels: {    clickclack: {      enabled: true,      baseUrl: "https://app.clickclack.chat",      defaultAccount: "service",      accounts: {        service: {          token: { source: "env", provider: "default", id: "CLICKCLACK_SERVICE_BOT_TOKEN" },          workspace: "default",          defaultTo: "channel:general",          agentId: "service-bot",          replyMode: "model",        },        peter: {          token: { source: "env", provider: "default", id: "CLICKCLACK_PETER_BOT_TOKEN" },          workspace: "default",          defaultTo: "dm:usr_...",          agentId: "peter-bot",          replyMode: "model",        },      },    },  },}
[/code]

`replyMode: "model"` utilise directement `api.runtime.llm.complete` pour les réponses courtes du bot. Lorsqu’un compte définit `agentId`, OpenClaw exige le bit de confiance explicite `plugins.entries.clickclack.llm.allowAgentIdOverride` afin que le plugin puisse exécuter des complétions pour cet agent bot. Laissez-le désactivé si vous utilisez uniquement la route d’agent par défaut.

## Cibles

  * `channel:<name-or-id>` envoie vers un canal d’espace de travail. Les cibles sans préfixe utilisent `channel:` par défaut.
  * `dm:<user_id>` crée ou réutilise une conversation directe avec cet utilisateur.
  * `thread:<message_id>` répond dans un fil existant.


Exemples :

bashCopy code
[code]
    openclaw message send --channel clickclack --target channel:general --message "hello"openclaw message send --channel clickclack --target dm:usr_123 --message "hello"openclaw message send --channel clickclack --target thread:msg_123 --message "following up"
[/code]

## Autorisations

Les portées de jeton ClickClack sont appliquées par l’API ClickClack.

  * `bot:read` : lire les données d’espace de travail, de canal, de message, de fil, de DM, de temps réel et de profil.
  * `bot:write` : `bot:read` plus les messages de canal, les réponses de fil, les DM et les téléversements.
  * `bot:admin` : `bot:write` plus la création de canaux.


OpenClaw n’a besoin que de `bot:write` pour une conversation d’agent normale.

## Dépannage

  * `ClickClack is not configured` : définissez `channels.clickclack.token` ou `CLICKCLACK_BOT_TOKEN`.
  * `workspace not found` : définissez `workspace` sur l’identifiant ou le slug d’espace de travail renvoyé par ClickClack.
  * Aucune réponse entrante : confirmez que le jeton dispose d’un accès en lecture temps réel et que le bot ne répond pas à ses propres messages.
  * Les envois vers un canal échouent : vérifiez que le bot est membre de l’espace de travail et dispose de `bot:write`.


Was this useful?YesNo