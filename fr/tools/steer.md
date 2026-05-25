---
title: Orienter
source_url: https://docs.openclaw.ai/fr/tools/steer
scraped_at: 2026-05-25
---

`/steer` envoie des consignes à une exécution déjà active. Il sert aux moments où il faut « ajuster cette exécution pendant qu’elle travaille encore », pas à démarrer un nouveau tour.

## Session actuelle

Utilisez `/steer` au niveau supérieur pour cibler l’exécution active de la session actuelle :

textCopy code
[code]
    /steer prefer the smaller patch and keep the tests focused/tell summarize before making the next tool call
[/code]

Comportement :

  * Cible uniquement l’exécution active de la session actuelle.
  * Fonctionne indépendamment du mode `/queue` de la session.
  * Ne démarre pas de nouvelle exécution lorsque la session est inactive.
  * Répond avec un avertissement lorsqu’il n’y a aucune exécution active à orienter.
  * Utilise le chemin d’orientation du runtime actif, afin que le modèle voie les consignes à la prochaine limite de runtime prise en charge.


## Orientation et file d’attente

`/queue steer` modifie le comportement des messages entrants normaux lorsqu’ils arrivent pendant qu’une exécution est active. `/steer <message>` est une commande explicite qui tente d’injecter le message de cette commande dans l’exécution active à la prochaine limite de runtime prise en charge, indépendamment du réglage `/queue` enregistré.

Utilisation :

  * `/steer <message>` lorsque vous voulez guider l’exécution active immédiatement.
  * `/queue steer` lorsque vous voulez que les futurs messages normaux orientent les exécutions actives par défaut.
  * `/queue collect` ou `/queue followup` lorsque les nouveaux messages doivent attendre un tour ultérieur au lieu d’orienter l’exécution active.


Pour les modes de file d’attente et le comportement de repli, consultez [File d’attente des commandes](</fr/concepts/queue>) et [File d’attente d’orientation](</fr/concepts/queue-steering>).

## Sous-agents

Utilisez `/subagents steer` lorsque la cible est une exécution enfant :

textCopy code
[code]
    /subagents steer 2 focus only on the API surface
[/code]

`/steer` au niveau supérieur ne sélectionne pas de sous-agent par id ou par index de liste. Il cible toujours l’exécution active de la session actuelle. Consultez [Sous-agents](</fr/tools/subagents>) pour les ids, libellés et commandes de contrôle des sous-agents.

## Sessions ACP

Utilisez `/acp steer` lorsque la cible est une session de harnais ACP :

textCopy code
[code]
    /acp steer --session agent:main:acp:codex tighten the repro
[/code]

Consultez [Agents ACP](</fr/tools/acp-agents>) pour la sélection des sessions ACP et le comportement du runtime.

## Associés

  * [Commandes slash](</fr/tools/slash-commands>)
  * [File d’attente des commandes](</fr/concepts/queue>)
  * [File d’attente d’orientation](</fr/concepts/queue-steering>)
  * [Sous-agents](</fr/tools/subagents>)


Was this useful?YesNo