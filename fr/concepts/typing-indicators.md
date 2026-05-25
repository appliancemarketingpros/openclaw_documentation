---
title: Indicateurs de saisie
source_url: https://docs.openclaw.ai/fr/concepts/typing-indicators
scraped_at: 2026-05-25
---

Les indicateurs de saisie sont envoyés au canal de discussion pendant qu’une exécution est active. Utilisez `agents.defaults.typingMode` pour contrôler **quand** la saisie commence et `typingIntervalSeconds` pour contrôler **à quelle fréquence** elle est actualisée.

## Valeurs par défaut

Quand `agents.defaults.typingMode` est **non défini** , OpenClaw conserve le comportement hérité :

  * **Discussions directes** : la saisie commence immédiatement une fois que la boucle du modèle démarre.
  * **Discussions de groupe avec une mention** : la saisie commence immédiatement.
  * **Discussions de groupe sans mention** : la saisie ne commence que lorsque le texte du message commence à être diffusé en streaming.
  * **Exécutions Heartbeat** : la saisie commence lorsque l’exécution Heartbeat démarre si la cible Heartbeat résolue est une discussion compatible avec la saisie et que la saisie n’est pas désactivée.


## Modes

Définissez `agents.defaults.typingMode` sur l’une des valeurs suivantes :

  * `never` \- aucun indicateur de saisie, jamais.
  * `instant` \- commence à saisir **dès que la boucle du modèle démarre** , même si l’exécution renvoie ensuite uniquement le jeton de réponse silencieuse.
  * `thinking` \- commence à saisir au **premier delta de raisonnement** (nécessite `reasoningLevel: "stream"` pour l’exécution).
  * `message` \- commence à saisir au **premier delta de texte non silencieux** (ignore le jeton silencieux `NO_REPLY`).


Ordre de « précocité de déclenchement » : `never` → `message` → `thinking` → `instant`

## Configuration

Définissez la valeur par défaut au niveau de l’agent :

json5Copy code
[code]
    {  agents: {    defaults: {      typingMode: "thinking",      typingIntervalSeconds: 6,    },  },}
[/code]

Remplacez le mode ou la cadence par session :

json5Copy code
[code]
    {  session: {    typingMode: "message",    typingIntervalSeconds: 4,  },}
[/code]

## Remarques

  * Le mode `message` n’affichera pas la saisie pour les réponses uniquement silencieuses lorsque toute la charge utile est le jeton silencieux exact (par exemple `NO_REPLY` / `no_reply`, correspondant sans tenir compte de la casse).
  * `thinking` ne se déclenche que si l’exécution diffuse le raisonnement en streaming (`reasoningLevel: "stream"`). Si le modèle n’émet pas de deltas de raisonnement, la saisie ne commencera pas.
  * La saisie Heartbeat est un signal de vivacité pour la cible de livraison résolue. Elle commence au démarrage de l’exécution Heartbeat au lieu de suivre le calendrier du flux `message` ou `thinking`. Définissez `typingMode: "never"` pour la désactiver.
  * Les Heartbeats n’affichent pas la saisie lorsque `target: "none"`, lorsque la cible ne peut pas être résolue, lorsque la livraison de discussion est désactivée pour le Heartbeat, ou lorsque le canal ne prend pas en charge la saisie.
  * `typingIntervalSeconds` contrôle la **cadence d’actualisation** , pas l’heure de début. La valeur par défaut est de 6 secondes.


## Liens associés

[**Presence** Comment le Gateway suit les clients connectés et les expose dans l’onglet Instances de macOS. ](</fr/concepts/presence>) [**Streaming and chunking** Comportement du streaming sortant, limites des fragments et livraison propre à chaque canal. ](</fr/concepts/streaming>)

Was this useful?YesNo