---
title: Autocomplétion
source_url: https://docs.openclaw.ai/fr/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

Générez des scripts d’autocomplétion shell et, en option, installez-les dans votre profil shell.

## Utilisation

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Options

  * `-s, --shell <shell>` : cible shell (`zsh`, `bash`, `powershell`, `fish` ; par défaut : `zsh`)
  * `-i, --install` : installe l’autocomplétion en ajoutant une ligne source à votre profil shell
  * `--write-state` : écrit le ou les scripts d’autocomplétion dans `$OPENCLAW_STATE_DIR/completions` sans les afficher sur stdout
  * `-y, --yes` : ignore les invites de confirmation d’installation


## Remarques

  * `--install` écrit un petit bloc « OpenClaw Completion » dans votre profil shell et le fait pointer vers le script mis en cache.
  * Sans `--install` ni `--write-state`, la commande affiche le script sur stdout.
  * La génération d’autocomplétion charge de manière anticipée les arborescences de commandes afin d’inclure les sous-commandes imbriquées.


## Liens associés

  * [Référence CLI](</fr/cli>)


Was this useful?YesNo