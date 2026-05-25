---
title: Skills
source_url: https://docs.openclaw.ai/fr/cli/skills
scraped_at: 2026-05-25
---

# `openclaw skills`

Inspecter les Skills locales et installer/mettre à jour des Skills depuis ClawHub.

Rubriques connexes :

  * Système Skills : [Skills](</fr/tools/skills>)
  * Configuration Skills : [Configuration Skills](</fr/tools/skills-config>)
  * Installations ClawHub : [ClawHub](</fr/clawhub/cli>)


## Commandes

bashCopy code
[code]
    openclaw skills search "calendar"openclaw skills search --limit 20 --jsonopenclaw skills install <slug>openclaw skills install <slug> --version <version>openclaw skills install <slug> --forceopenclaw skills install <slug> --agent <id>openclaw skills update <slug>openclaw skills update --allopenclaw skills update --all --agent <id>openclaw skills listopenclaw skills list --eligibleopenclaw skills list --jsonopenclaw skills list --verboseopenclaw skills list --agent <id>openclaw skills info <name>openclaw skills info <name> --jsonopenclaw skills info <name> --agent <id>openclaw skills checkopenclaw skills check --agent <id>openclaw skills check --json
[/code]

`search`/`install`/`update` utilisent directement ClawHub et installent dans le répertoire `skills/` de l’espace de travail actif. `list`/`info`/`check` inspectent toujours les Skills locales visibles par l’espace de travail et la configuration actuels. Les commandes adossées à l’espace de travail résolvent l’espace de travail cible à partir de `--agent <id>`, puis du répertoire de travail actuel lorsqu’il se trouve dans un espace de travail d’agent configuré, puis de l’agent par défaut.

Cette commande CLI `install` télécharge les dossiers de Skills depuis ClawHub. Les installations de dépendances de Skills adossées au Gateway, déclenchées depuis l’intégration ou les paramètres Skills, utilisent à la place le chemin de requête `skills.install` distinct.

Remarques :

  * `search [query...]` accepte une requête facultative ; omettez-la pour parcourir le flux de recherche ClawHub par défaut.
  * `search --limit <n>` limite le nombre de résultats renvoyés.
  * `install --force` écrase un dossier de Skill existant dans l’espace de travail pour le même slug.
  * `--agent <id>` cible un espace de travail d’agent configuré et remplace l’inférence à partir du répertoire de travail actuel.
  * `update --all` met uniquement à jour les installations ClawHub suivies dans l’espace de travail actif.
  * `check --agent <id>` vérifie l’espace de travail de l’agent sélectionné et indique quelles Skills prêtes sont réellement visibles dans le prompt ou la surface de commande de cet agent.
  * `list` est l’action par défaut lorsqu’aucune sous-commande n’est fournie.
  * `list`, `info` et `check` écrivent leur sortie rendue vers stdout. Avec `--json`, cela signifie que la charge utile lisible par machine reste sur stdout pour les pipes et les scripts.


## Connexe

  * [Référence CLI](</fr/cli>)
  * [Skills](</fr/tools/skills>)


Was this useful?YesNo