---
title: Réinitialiser
source_url: https://docs.openclaw.ai/fr/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

Réinitialiser la configuration/l’état local (conserve la CLI installée).

Options :

  * `--scope <scope>` : `config`, `config+creds+sessions` ou `full`
  * `--yes` : ignorer les invites de confirmation
  * `--non-interactive` : désactiver les invites ; nécessite `--scope` et `--yes`
  * `--dry-run` : afficher les actions sans supprimer de fichiers


Exemples :

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Remarques :

  * Exécutez d’abord `openclaw backup create` si vous souhaitez un snapshot restaurable avant de supprimer l’état local.
  * Si vous omettez `--scope`, `openclaw reset` utilise une invite interactive pour choisir ce qu’il faut supprimer.
  * `--non-interactive` n’est valide que lorsque `--scope` et `--yes` sont tous deux définis.


## Associé

  * [Référence CLI](</fr/cli>)


Was this useful?YesNo