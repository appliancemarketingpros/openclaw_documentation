---
title: API entrante du canal
source_url: https://docs.openclaw.ai/fr/plugins/sdk-channel-inbound
scraped_at: 2026-06-29
---

ReferencePlugin maintainer reference

Les plugins de canal doivent modéliser les chemins de réception avec les noms inbound et message :

textCopy code
[code]
    platform event -> inbound facts/context -> agent reply -> message delivery
[/code]

Utilisez `openclaw/plugin-sdk/channel-inbound` pour la normalisation des événements entrants, le formatage, les racines et l’orchestration. Utilisez `openclaw/plugin-sdk/channel-outbound` pour l’envoi natif, les accusés de réception, la livraison durable et le comportement d’aperçu en direct.

## Helpers principaux

tsCopy code
[code]
       buildChannelInboundEventContext,  runChannelInboundEvent,  dispatchChannelInboundReply,} from "openclaw/plugin-sdk/channel-inbound";
[/code]

  * `buildChannelInboundEventContext(...)` : projette les faits de canal normalisés dans le contexte de prompt/session. Utilisez `channelContext` pour transmettre les métadonnées d’expéditeur/chat détenues par le canal au hook de plugin `ctx.channelContext` ; enrichissez `PluginHookChannelSenderContext` ou `PluginHookChannelChatContext` depuis ce sous-chemin pour les champs propres au canal.
  * `runChannelInboundEvent(...)` : exécute l’ingestion, la classification, la prévalidation, la résolution, l’enregistrement, la distribution et la finalisation pour un événement de plateforme entrant.
  * `dispatchChannelInboundReply(...)` : enregistre et distribue une réponse entrante déjà assemblée avec un adaptateur de livraison.


Le runtime de plugin injecté expose les mêmes helpers de haut niveau sous `runtime.channel.inbound.*` pour les canaux groupés/natifs qui reçoivent déjà l’objet runtime.

tsCopy code
[code]
    await runtime.channel.inbound.run({  channel: "demo",  accountId,  raw: platformEvent,  adapter: {    ingest: normalizePlatformEvent,    resolveTurn: resolveInboundReply,  },});
[/code]

Les répartiteurs de compatibilité doivent assembler les entrées de `dispatchChannelInboundReply(...)` et conserver la livraison de plateforme dans l’adaptateur de livraison. Les nouveaux chemins d’envoi doivent privilégier les adaptateurs de message et les helpers de message durable.

## Migration

Les anciens alias runtime `runtime.channel.turn.*` ont été supprimés. Utilisez :

  * `runtime.channel.inbound.run(...)` pour les événements entrants bruts.
  * `runtime.channel.inbound.dispatchReply(...)` pour les contextes de réponse assemblés.
  * `runtime.channel.inbound.buildContext(...)` pour les charges utiles de contexte entrant.
  * `runtime.channel.inbound.runPreparedReply(...)` uniquement pour les chemins de distribution préparés détenus par le canal qui assemblent déjà leur propre closure de distribution.


Le nouveau code de plugin ne doit pas introduire d’API de canal nommées `turn`. Conservez le vocabulaire de tour de modèle ou d’agent dans le code d’agent/fournisseur ; les plugins de canal utilisent les termes inbound, message, delivery et reply.

Was this useful?YesNo

Open issue