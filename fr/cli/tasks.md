---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/fr/cli/tasks
scraped_at: 2026-05-25
---

Inspectez les tâches en arrière-plan durables et l’état de Task Flow. Sans sous-commande, `openclaw tasks` est équivalent à `openclaw tasks list`.

Consultez [Tâches en arrière-plan](</fr/automation/tasks>) pour le cycle de vie et le modèle de livraison.

## Utilisation

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Options Racine

  * `--json` : produit du JSON.
  * `--runtime <name>` : filtre par type : `subagent`, `acp`, `cron` ou `cli`.
  * `--status <name>` : filtre par état : `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled` ou `lost`.


## Sous-commandes

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

Liste les tâches en arrière-plan suivies, de la plus récente à la plus ancienne.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Affiche une tâche par ID de tâche, ID d’exécution ou clé de session.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Modifie la politique de notification pour une tâche en cours d’exécution.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Annule une tâche en arrière-plan en cours d’exécution.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Fait apparaître les enregistrements de tâches et de Task Flow obsolètes, perdus, dont la livraison a échoué ou autrement incohérents. Les tâches perdues conservées jusqu’à `cleanupAfter` sont des avertissements ; les tâches perdues expirées ou non horodatées sont des erreurs.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Prévisualise ou applique la réconciliation des tâches et de Task Flow, l’horodatage de nettoyage, l’élagage, ainsi que le nettoyage du registre de sessions d’exécution Cron obsolètes. Pour les tâches Cron, la réconciliation utilise les journaux d’exécution/l’état de tâche persistés avant de marquer une ancienne tâche active comme `lost`, afin que les exécutions Cron terminées ne deviennent pas de fausses erreurs d’audit simplement parce que l’état d’exécution en mémoire du Gateway a disparu. L’audit CLI hors ligne ne fait pas autorité pour l’ensemble des tâches Cron actives propre au processus du Gateway. Les tâches CLI avec un ID d’exécution/ID source sont marquées `lost` lorsque leur contexte d’exécution Gateway actif a disparu, même si une ancienne ligne de session enfant reste présente. Lorsqu’elle est appliquée, la maintenance élague également les lignes du registre de sessions `cron:<jobId>:run:<uuid>` datant de plus de 7 jours, tout en préservant les tâches Cron actuellement en cours d’exécution et en laissant les lignes de session non-Cron intactes.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Inspecte ou annule l’état durable de Task Flow dans le registre des tâches.

## Connexe

  * [Référence CLI](</fr/cli>)
  * [Tâches en arrière-plan](</fr/automation/tasks>)


Was this useful?YesNo