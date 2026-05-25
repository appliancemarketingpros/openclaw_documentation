---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/fr/cli/commitments
scraped_at: 2026-05-25
---

Répertoriez et gérez les engagements de suivi déduits.

Les engagements sont des mémoires de suivi optionnelles et de courte durée, créées à partir du contexte de conversation. Consultez [Engagements déduits](</fr/concepts/commitments>) pour le guide conceptuel.

Sans sous-commande, `openclaw commitments` répertorie les engagements en attente.

## Utilisation

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## Options

  * `--all` : afficher tous les statuts au lieu des seuls engagements en attente.
  * `--agent <id>` : filtrer sur un seul identifiant d’agent.
  * `--status <status>` : filtrer par statut. Valeurs : `pending`, `sent`, `dismissed`, `snoozed` ou `expired`.
  * `--json` : produire du JSON lisible par machine.


## Exemples

Répertorier les engagements en attente :

bashCopy code
[code]
    openclaw commitments
[/code]

Répertorier tous les engagements stockés :

bashCopy code
[code]
    openclaw commitments --all
[/code]

Filtrer sur un seul agent :

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

Trouver les engagements reportés :

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

Ignorer un ou plusieurs engagements :

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

Exporter au format JSON :

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## Sortie

La sortie texte inclut :

  * identifiant de l’engagement
  * statut
  * type
  * première échéance possible
  * portée
  * texte de relance suggéré


La sortie JSON inclut également le chemin du magasin d’engagements et les enregistrements stockés complets.

## Connexe

  * [Engagements déduits](</fr/concepts/commitments>)
  * [Vue d’ensemble de la mémoire](</fr/concepts/memory>)
  * [Heartbeat](</fr/gateway/heartbeat>)
  * [Tâches planifiées](</fr/automation/cron-jobs>)


Was this useful?YesNo