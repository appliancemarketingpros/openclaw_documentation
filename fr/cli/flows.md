---
title: Flux (redirection)
source_url: https://docs.openclaw.ai/fr/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

Il n’existe pas de commande `openclaw flows` de premier niveau. L’inspection persistante de TaskFlow se trouve sous `openclaw tasks flow`.

## Sous-commandes

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Sous-commande | Description | Arguments / options  
---|---|---  
`list` | Répertorier les TaskFlows suivis. | Sortie lisible par machine `--json` ; filtre `--status <name>` (voir les valeurs d’état ci-dessous).  
`show` | Afficher un TaskFlow. | ID de flux ou clé de propriétaire `<lookup>` ; sortie lisible par machine `--json`.  
`cancel` | Annuler un TaskFlow en cours d’exécution. | ID de flux ou clé de propriétaire `<lookup>`.  
  
`<lookup>` accepte soit un ID de flux (renvoyé par `list` / `show`), soit la clé de propriétaire du flux (l’identifiant stable que le sous-système propriétaire utilise pour suivre le flux).

### Valeurs du filtre d’état

`--status` sur `list` accepte l’une des valeurs suivantes :

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## Exemples

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

Pour les concepts complets de TaskFlow et sa création, consultez [TaskFlow](</fr/automation/taskflow>). Pour la commande parente `tasks`, consultez la [référence CLI de tasks](</fr/cli/tasks>).

## Associés

  * [Référence CLI](</fr/cli>)
  * [Automatisation](</fr/automation>)
  * [TaskFlow](</fr/automation/taskflow>)


Was this useful?YesNo