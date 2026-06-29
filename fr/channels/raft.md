---
title: Raft
source_url: https://docs.openclaw.ai/fr/channels/raft
scraped_at: 2026-06-29
---

ChannelsDeveloper and self-hosted

La prise en charge de Raft connecte un agent OpenClaw à un Agent externe Raft via la CLI Raft locale. Raft envoie des indices de réveil authentifiés au Gateway. L’agent utilise ensuite la CLI Raft pour vérifier et envoyer des messages.

## Installation

Raft est un Plugin externe officiel. Installez-le sur l’hôte du Gateway :

bashCopy code
[code]
    openclaw plugins install @openclaw/raftopenclaw gateway restart
[/code]

Détails : [Plugins](</fr/tools/plugin>)

## Prérequis

  * Un espace de travail Raft avec un Agent externe.
  * La CLI Raft installée sur le même hôte que le Gateway OpenClaw.
  * Un profil CLI Raft déjà connecté et associé à cet Agent externe.


Le Plugin ne stocke pas les identifiants Raft. La CLI Raft conserve cette authentification dans son propre profil.

## Configuration

Définissez le profil dans la configuration :

json5Copy code
[code]
    {  channels: {    raft: {      enabled: true,      profile: "openclaw",    },  },}
[/code]

Pour le compte par défaut, vous pouvez plutôt définir `RAFT_PROFILE` dans l’environnement du Gateway :

bashCopy code
[code]
    RAFT_PROFILE=openclaw
[/code]

Utilisez un compte nommé lorsqu’un Gateway se connecte à plusieurs Agents externes Raft :

json5Copy code
[code]
    {  channels: {    raft: {      accounts: {        support: {          profile: "support-agent",        },        engineering: {          profile: "engineering-agent",        },      },    },  },}
[/code]

Le flux de configuration interactif enregistre le même profil :

bashCopy code
[code]
    openclaw channels setup raft
[/code]

## Fonctionnement

Au démarrage du Gateway, le Plugin :

  1. Ouvre un point de terminaison HTTP de réveil limité au loopback sur un port éphémère.
  2. Lance `raft --profile <profile> agent bridge` avec ce point de terminaison et un jeton propre au processus.
  3. Accepte uniquement les indices de réveil authentifiés, sans contenu, avec une identité de relecture provenant du pont local.
  4. Exige l’un des champs `eventId`, `attemptId`, `messageId`, `delivery_id`, `wake_id` ou `id`.
  5. Déduplique les livraisons de réveil réessayées récemment selon l’identifiant d’événement du pont, y compris entre les redémarrages du Gateway.
  6. Renvoie une session d’exécution stable pour le pont actuel et un lot de vidage d’activité vide pour le protocole CLI Raft.
  7. Lance un tour d’agent OpenClaw sérialisé pour chaque réveil accepté.


Le pont gère les nouvelles tentatives de livraison Raft et les reconnexions. Le tour OpenClaw reçoit uniquement un avis de réveil, pas une copie du corps du message Raft. Il utilise la CLI pour lire les messages en attente et envoyer sa réponse :

bashCopy code
[code]
    raft --profile openclaw message checkraft --profile openclaw message send
[/code]

## Vérification

Vérifiez qu’OpenClaw peut trouver la CLI et dispose d’un profil configuré :

bashCopy code
[code]
    openclaw channels status --probeopenclaw plugins inspect raft --runtime --json
[/code]

Envoyez ensuite un message à l’Agent externe Raft. Le journal du Gateway doit afficher le démarrage du pont Raft, suivi d’un réveil entrant. L’agent doit utiliser le profil Raft configuré pour vérifier ses messages en attente.

## Dépannage

La CLI Raft est manquante

Installez la CLI Raft sur l’hôte du Gateway et rendez `raft` disponible dans le `PATH` du service. Vérifiez avec `raft --help`, puis redémarrez le Gateway.

Le pont se ferme immédiatement

Vérifiez que le profil configuré est connecté et appartient à l’Agent externe Raft prévu. Exécutez `raft --profile <profile> agent bridge` directement pour voir le diagnostic de la CLI.

Un réveil arrive, mais aucune réponse Raft n’est envoyée

C’est attendu lorsque l’agent n’invoque pas la CLI Raft. Le pont de réveil ne transporte pas les corps de message ni les réponses finales automatiques. Vérifiez la politique d’outils de l’agent et assurez-vous qu’il peut exécuter `raft --profile <profile> message check` et `message send`.

## Références

  * [Raft](<https://raft.build/>)
  * [Documentation Raft](<https://docs.raft.build/welcome/>)
  * [Intégration Hermes Raft](<https://hermes-agent.nousresearch.com/docs/user-guide/messaging/raft>)


Was this useful?YesNo

Open issue