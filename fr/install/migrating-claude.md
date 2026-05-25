---
title: Migration depuis Claude
source_url: https://docs.openclaw.ai/fr/install/migrating-claude
scraped_at: 2026-05-25
---

OpenClaw importe l’état local de Claude via le fournisseur de migration Claude intégré. Le fournisseur affiche un aperçu de chaque élément avant de modifier l’état, masque les secrets dans les plans et les rapports, et crée une sauvegarde vérifiée avant l’application.

## Deux façons d’importer

### Assistant d’intégration

L’assistant propose Claude lorsqu’il détecte un état Claude local.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Ou pointez vers une source précise :

bashCopy code
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
[/code]

### CLI

Utilisez `openclaw migrate` pour les exécutions scriptées ou reproductibles. Consultez [`openclaw migrate`](</fr/cli/migrate>) pour la référence complète.

bashCopy code
[code]
    openclaw migrate claude --dry-runopenclaw migrate apply claude --yes
[/code]

Ajoutez `--from <path>` pour importer un répertoire personnel Claude Code ou une racine de projet spécifique.

## Ce qui est importé

Instructions et mémoire

  * Le contenu du projet `CLAUDE.md` et de `.claude/CLAUDE.md` est copié ou ajouté à l’`AGENTS.md` de l’espace de travail de l’agent OpenClaw.
  * Le contenu utilisateur de `~/.claude/CLAUDE.md` est ajouté au `USER.md` de l’espace de travail.

Serveurs MCP

Les définitions de serveurs MCP sont importées depuis le projet `.mcp.json`, Claude Code `~/.claude.json` et Claude Desktop `claude_desktop_config.json` lorsqu’elles sont présentes.

Skills et commandes

  * Les Skills Claude avec un fichier `SKILL.md` sont copiées dans le répertoire des Skills de l’espace de travail OpenClaw.
  * Les fichiers Markdown de commandes Claude sous `.claude/commands/` ou `~/.claude/commands/` sont convertis en Skills OpenClaw avec `disable-model-invocation: true`.


## Ce qui reste uniquement archivé

Le fournisseur copie ces éléments dans le rapport de migration pour examen manuel, mais ne les charge **pas** dans la configuration OpenClaw active :

  * Hooks Claude
  * Autorisations Claude et listes d’autorisation larges pour les outils
  * Valeurs par défaut de l’environnement Claude
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * Sous-agents Claude sous `.claude/agents/` ou `~/.claude/agents/`
  * Répertoires de caches, plans et historiques de projet de Claude Code
  * Extensions Claude Desktop et identifiants stockés par le système d’exploitation


OpenClaw refuse d’exécuter automatiquement des hooks, de faire confiance aux listes d’autorisation, ou de décoder l’état opaque des identifiants OAuth et Desktop. Déplacez manuellement ce dont vous avez besoin après avoir examiné l’archive.

## Sélection de la source

Sans `--from`, OpenClaw inspecte le répertoire personnel Claude Code par défaut dans `~/.claude`, le fichier d’état Claude Code échantillonné `~/.claude.json` et la configuration MCP de Claude Desktop sur macOS.

Lorsque `--from` pointe vers une racine de projet, OpenClaw importe uniquement les fichiers Claude de ce projet, comme `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/` et `.mcp.json`. Il ne lit pas votre répertoire personnel Claude global pendant un import depuis une racine de projet.

## Flux recommandé

* ### Prévisualiser le plan

bashCopy code
[code]
    openclaw migrate claude --dry-run
[/code]

Le plan liste tout ce qui changera, y compris les conflits, les éléments ignorés et les valeurs sensibles masquées depuis les champs MCP imbriqués `env` ou `headers`.

* ### Appliquer avec sauvegarde

bashCopy code
[code]
    openclaw migrate apply claude --yes
[/code]

OpenClaw crée et vérifie une sauvegarde avant l’application.

* ### Exécuter doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</fr/gateway/doctor>) vérifie les problèmes de configuration ou d’état après l’import.

* ### Redémarrer et vérifier

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Confirmez que le Gateway est sain et que vos instructions, serveurs MCP et Skills importés sont chargés.

## Gestion des conflits

L’application refuse de continuer lorsque le plan signale des conflits (un fichier ou une valeur de configuration existe déjà à la cible).

Pour une installation OpenClaw neuve, les conflits sont inhabituels. Ils apparaissent généralement lorsque vous relancez l’import sur une configuration qui comporte déjà des modifications utilisateur.

## Sortie JSON pour l’automatisation

bashCopy code
[code]
    openclaw migrate claude --dry-run --jsonopenclaw migrate apply claude --json --yes
[/code]

Avec `--json` et sans `--yes`, l’application affiche le plan et ne modifie pas l’état. C’est le mode le plus sûr pour la CI et les scripts partagés.

## Dépannage

L’état Claude se trouve hors de ~/.claude

Passez `--from /actual/path` (CLI) ou `--import-source /actual/path` (intégration).

L’intégration refuse d’importer sur une configuration existante

Les imports lors de l’intégration nécessitent une configuration neuve. Réinitialisez l’état et recommencez l’intégration, ou utilisez directement `openclaw migrate apply claude`, qui prend en charge `--overwrite` et le contrôle explicite des sauvegardes.

Les serveurs MCP de Claude Desktop n’ont pas été importés

Claude Desktop lit `claude_desktop_config.json` depuis un chemin propre à la plateforme. Pointez `--from` vers le répertoire de ce fichier si OpenClaw ne l’a pas détecté automatiquement.

Les commandes Claude sont devenues des Skills avec l’invocation de modèle désactivée

C’est intentionnel. Les commandes Claude sont déclenchées par l’utilisateur, donc OpenClaw les importe comme Skills avec `disable-model-invocation: true`. Modifiez le frontmatter de chaque Skill si vous voulez que l’agent les invoque automatiquement.

## Connexe

  * [`openclaw migrate`](</fr/cli/migrate>) : référence CLI complète, contrat de Plugin et formes JSON.
  * [Guide de migration](</fr/install/migrating>) : tous les chemins de migration.
  * [Migration depuis Hermes](</fr/install/migrating-hermes>) : l’autre chemin d’import inter-systèmes.
  * [Intégration](</fr/cli/onboard>) : flux de l’assistant et indicateurs non interactifs.
  * [Doctor](</fr/gateway/doctor>) : contrôle de santé après migration.
  * [Espace de travail de l’agent](</fr/concepts/agent-workspace>) : où résident `AGENTS.md`, `USER.md` et les Skills.


Was this useful?YesNo