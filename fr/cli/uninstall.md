---
title: Désinstaller
source_url: https://docs.openclaw.ai/fr/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

Désinstaller le service Gateway + les données locales (la CLI reste).

Options :

  * `--service` : supprimer le service Gateway
  * `--state` : supprimer l’état et la configuration
  * `--workspace` : supprimer les répertoires d’espace de travail
  * `--app` : supprimer l’app macOS
  * `--all` : supprimer le service, l’état, l’espace de travail et l’app
  * `--yes` : ignorer les invites de confirmation
  * `--non-interactive` : désactiver les invites ; nécessite `--yes`
  * `--dry-run` : afficher les actions sans supprimer de fichiers


Exemples :

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Remarques :

  * Exécutez d’abord `openclaw backup create` si vous souhaitez un instantané restaurable avant de supprimer l’état ou les espaces de travail.
  * `--all` est un raccourci pour supprimer ensemble le service, l’état, l’espace de travail et l’app.
  * `--non-interactive` nécessite `--yes`.


## Articles connexes

  * [Référence CLI](</fr/cli>)
  * [Désinstallation](</fr/install/uninstall>)


Was this useful?YesNo