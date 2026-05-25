---
title: Nœuds
source_url: https://docs.openclaw.ai/fr/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

Gérez les nœuds appairés (appareils) et invoquez les capacités des nœuds.

Liens connexes :

  * Vue d’ensemble des nœuds : [Nœuds](</fr/nodes>)
  * Caméra : [Nœuds caméra](</fr/nodes/camera>)
  * Images : [Nœuds d’image](</fr/nodes/images>)


Options courantes :

  * `--url`, `--token`, `--timeout`, `--json`


## Commandes courantes

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

`nodes list` affiche les tableaux des demandes en attente et des appairages. Les lignes appairées incluent l’âge de connexion le plus récent (Dernière connexion). Utilisez `--connected` pour afficher uniquement les nœuds actuellement connectés. Utilisez `--last-connected <duration>` pour filtrer les nœuds qui se sont connectés dans une durée donnée (par exemple `24h`, `7d`). Utilisez `nodes remove --node <id|name|ip>` pour supprimer un enregistrement obsolète d’appairage de nœud détenu par le Gateway.

Note d’approbation :

  * `openclaw nodes pending` ne nécessite que le périmètre d’appairage.
  * `gateway.nodes.pairing.autoApproveCidrs` peut ignorer l’étape d’attente uniquement pour l’appairage d’un appareil `role: node` explicitement approuvé et effectué pour la première fois. Il est désactivé par défaut et n’approuve pas les mises à niveau.
  * `openclaw nodes approve <requestId>` hérite des exigences de périmètre supplémentaires de la demande en attente : 
    * demande sans commande : appairage uniquement
    * commandes de nœud non-exec : appairage + écriture
    * `system.run` / `system.run.prepare` / `system.which` : appairage + admin


## Invoquer

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

Indicateurs d’invocation :

  * `--params <json>` : chaîne d’objet JSON (par défaut `{}`).
  * `--invoke-timeout <ms>` : délai d’expiration d’invocation du nœud (par défaut `15000`).
  * `--idempotency-key <key>` : clé d’idempotence facultative.
  * `system.run` et `system.run.prepare` sont bloqués ici ; utilisez l’outil `exec` avec `host=node` pour l’exécution shell.


Pour l’exécution shell sur un nœud, utilisez l’outil `exec` avec `host=node` au lieu de `openclaw nodes run`. La CLI `nodes` est désormais axée sur les capacités : RPC direct via `nodes invoke`, ainsi que l’appairage, la caméra, l’écran, la localisation, Canvas et les notifications. Les commandes Canvas sont implémentées par le Plugin Canvas expérimental intégré ; le noyau conserve un point d’extension de compatibilité afin qu’elles restent disponibles sous `openclaw nodes canvas`.

## Liens connexes

  * [Référence CLI](</fr/cli>)
  * [Nœuds](</fr/nodes>)


Was this useful?YesNo