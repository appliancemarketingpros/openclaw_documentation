---
title: Points d’accroche
source_url: https://docs.openclaw.ai/fr/cli/hooks
scraped_at: 2026-05-25
---

# `openclaw hooks`

Gérer les hooks d’agent (automatisations événementielles pour des commandes comme `/new`, `/reset` et le démarrage du Gateway).

Exécuter `openclaw hooks` sans sous-commande équivaut à `openclaw hooks list`.

Associé :

  * Hooks : [Hooks](</fr/automation/hooks>)
  * Hooks de Plugin : [Hooks de Plugin](</fr/plugins/hooks>)


## Lister tous les hooks

bashCopy code
[code]
    openclaw hooks list
[/code]

Liste tous les hooks découverts dans les répertoires de l’espace de travail, gérés, supplémentaires et intégrés. Le démarrage du Gateway ne charge pas les gestionnaires de hooks internes tant qu’au moins un hook interne n’est pas configuré.

**Options :**

  * `--eligible` : Afficher uniquement les hooks admissibles (exigences satisfaites)
  * `--json` : Sortie au format JSON
  * `-v, --verbose` : Afficher des informations détaillées, y compris les exigences manquantes


**Exemple de sortie :**

CodeCopy code
[code]
    Hooks (4/4 ready) Ready:  🚀 boot-md ✓ - Run BOOT.md on gateway startup  📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap  📝 command-logger ✓ - Log all command events to a centralized audit file  💾 session-memory ✓ - Save session context to memory when /new or /reset command is issued
[/code]

**Exemple (détaillé) :**

bashCopy code
[code]
    openclaw hooks list --verbose
[/code]

Affiche les exigences manquantes pour les hooks non admissibles.

**Exemple (JSON) :**

bashCopy code
[code]
    openclaw hooks list --json
[/code]

Renvoie du JSON structuré pour une utilisation programmatique.

## Obtenir les informations d’un hook

bashCopy code
[code]
    openclaw hooks info <name>
[/code]

Afficher des informations détaillées sur un hook spécifique.

**Arguments :**

  * `<name>` : Nom du hook ou clé du hook (par exemple, `session-memory`)


**Options :**

  * `--json` : Sortie au format JSON


**Exemple :**

bashCopy code
[code]
    openclaw hooks info session-memory
[/code]

**Sortie :**

CodeCopy code
[code]
    💾 session-memory ✓ Ready Save session context to memory when /new or /reset command is issued Details:  Source: openclaw-bundled  Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md  Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts  Homepage: https://docs.openclaw.ai/automation/hooks#session-memory  Events: command:new, command:reset Requirements:  Config: ✓ workspace.dir
[/code]

## Vérifier l’admissibilité des hooks

bashCopy code
[code]
    openclaw hooks check
[/code]

Afficher un résumé de l’état d’admissibilité des hooks (combien sont prêts ou non).

**Options :**

  * `--json` : Sortie au format JSON


**Exemple de sortie :**

CodeCopy code
[code]
    Hooks Status Total hooks: 4Ready: 4Not ready: 0
[/code]

## Activer un hook

bashCopy code
[code]
    openclaw hooks enable <name>
[/code]

Activer un hook spécifique en l’ajoutant à votre configuration (`~/.openclaw/openclaw.json` par défaut).

**Remarque :** Les hooks de l’espace de travail sont désactivés par défaut jusqu’à leur activation ici ou dans la configuration. Les hooks gérés par des plugins affichent `plugin:<id>` dans `openclaw hooks list` et ne peuvent pas être activés/désactivés ici. Activez/désactivez plutôt le plugin.

**Arguments :**

  * `<name>` : Nom du hook (par exemple, `session-memory`)


**Exemple :**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Sortie :**

CodeCopy code
[code]
    ✓ Enabled hook: 💾 session-memory
[/code]

**Ce que cela fait :**

  * Vérifie si le hook existe et est admissible
  * Met à jour `hooks.internal.entries.<name>.enabled = true` dans votre configuration
  * Enregistre la configuration sur le disque


Si le hook provient de `<workspace>/hooks/`, cette étape d’adhésion explicite est requise avant que le Gateway ne le charge.

**Après l’activation :**

  * Redémarrez le Gateway afin que les hooks soient rechargés (redémarrage de l’application de la barre de menus sur macOS, ou redémarrage de votre processus Gateway en développement).


## Désactiver un hook

bashCopy code
[code]
    openclaw hooks disable <name>
[/code]

Désactiver un hook spécifique en mettant à jour votre configuration.

**Arguments :**

  * `<name>` : Nom du hook (par exemple, `command-logger`)


**Exemple :**

bashCopy code
[code]
    openclaw hooks disable command-logger
[/code]

**Sortie :**

CodeCopy code
[code]
    ⏸ Disabled hook: 📝 command-logger
[/code]

**Après la désactivation :**

  * Redémarrez le Gateway afin que les hooks soient rechargés


## Notes

  * `openclaw hooks list --json`, `info --json` et `check --json` écrivent du JSON structuré directement sur stdout.
  * Les hooks gérés par des plugins ne peuvent pas être activés ni désactivés ici ; activez ou désactivez plutôt le plugin propriétaire.


## Installer des packs de hooks

bashCopy code
[code]
    openclaw plugins install <package>        # npm by defaultopenclaw plugins install npm:<package>    # npm onlyopenclaw plugins install <package> --pin  # pin versionopenclaw plugins install <path>           # local path
[/code]

Installer des packs de hooks via l’installateur de plugins unifié.

`openclaw hooks install` fonctionne toujours comme alias de compatibilité, mais il affiche un avertissement d’obsolescence et transfère vers `openclaw plugins install`.

Les spécifications npm sont **uniquement issues du registre** (nom du paquet + **version exacte** facultative ou **dist-tag**). Les spécifications Git/URL/fichier et les plages semver sont rejetées. Les installations de dépendances s’exécutent localement au projet avec `--ignore-scripts` par sécurité, même lorsque votre shell a des paramètres globaux d’installation npm.

Les spécifications nues et `@latest` restent sur le canal stable. Si npm résout l’une ou l’autre vers une préversion, OpenClaw s’arrête et vous demande d’accepter explicitement avec une balise de préversion comme `@beta`/`@rc` ou une version de préversion exacte.

**Ce que cela fait :**

  * Copie le pack de hooks dans `~/.openclaw/hooks/<id>`
  * Active les hooks installés dans `hooks.internal.entries.*`
  * Enregistre l’installation sous `hooks.internal.installs`


**Options :**

  * `-l, --link` : Lier un répertoire local au lieu de le copier (l’ajoute à `hooks.internal.load.extraDirs`)
  * `--pin` : Enregistrer les installations npm comme `name@version` résolus exacts dans `hooks.internal.installs`


**Archives prises en charge :** `.zip`, `.tgz`, `.tar.gz`, `.tar`

**Exemples :**

bashCopy code
[code]
    # Local directoryopenclaw plugins install ./my-hook-pack # Local archiveopenclaw plugins install ./my-hook-pack.zip # NPM packageopenclaw plugins install @openclaw/my-hook-pack # Link a local directory without copyingopenclaw plugins install -l ./my-hook-pack
[/code]

Les packs de hooks liés sont traités comme des hooks gérés depuis un répertoire configuré par l’opérateur, et non comme des hooks de l’espace de travail.

## Mettre à jour des packs de hooks

bashCopy code
[code]
    openclaw plugins update <id>openclaw plugins update --all
[/code]

Mettre à jour les packs de hooks basés sur npm suivis via le programme de mise à jour de plugins unifié.

`openclaw hooks update` fonctionne toujours comme alias de compatibilité, mais il affiche un avertissement d’obsolescence et transfère vers `openclaw plugins update`.

**Options :**

  * `--all` : Mettre à jour tous les packs de hooks suivis
  * `--dry-run` : Afficher ce qui changerait sans écrire


Lorsqu’un hachage d’intégrité enregistré existe et que le hachage de l’artefact récupéré change, OpenClaw affiche un avertissement et demande confirmation avant de continuer. Utilisez l’option globale `--yes` pour contourner les invites dans les exécutions CI/non interactives.

## Hooks intégrés

### session-memory

Enregistre le contexte de session en mémoire lorsque vous exécutez `/new` ou `/reset`.

**Activer :**

bashCopy code
[code]
    openclaw hooks enable session-memory
[/code]

**Sortie :** `~/.openclaw/workspace/memory/YYYY-MM-DD-HHMM.md` par défaut. Définissez `hooks.internal.entries.session-memory.llmSlug: true` pour des slugs de noms de fichiers générés par le modèle.

**Voir :** [documentation de session-memory](</fr/automation/hooks#session-memory>)

### bootstrap-extra-files

Injecte des fichiers d’amorçage supplémentaires (par exemple `AGENTS.md` / `TOOLS.md` locaux au monorepo) pendant `agent:bootstrap`.

**Activer :**

bashCopy code
[code]
    openclaw hooks enable bootstrap-extra-files
[/code]

**Voir :** [documentation de bootstrap-extra-files](</fr/automation/hooks#bootstrap-extra-files>)

### command-logger

Journalise tous les événements de commande dans un fichier d’audit centralisé.

**Activer :**

bashCopy code
[code]
    openclaw hooks enable command-logger
[/code]

**Sortie :** `~/.openclaw/logs/commands.log`

**Voir les journaux :**

bashCopy code
[code]
    # Recent commandstail -n 20 ~/.openclaw/logs/commands.log # Pretty-printcat ~/.openclaw/logs/commands.log | jq . # Filter by actiongrep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
[/code]

**Voir :** [documentation de command-logger](</fr/automation/hooks#command-logger>)

### boot-md

Exécute `BOOT.md` au démarrage du Gateway (après le démarrage des canaux).

**Événements** : `gateway:startup`

**Activer** :

bashCopy code
[code]
    openclaw hooks enable boot-md
[/code]

**Voir :** [documentation de boot-md](</fr/automation/hooks#boot-md>)

## Associé

  * [Référence CLI](</fr/cli>)
  * [Hooks d’automatisation](</fr/automation/hooks>)


Was this useful?YesNo