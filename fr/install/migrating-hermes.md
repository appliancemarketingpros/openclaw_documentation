---
title: Migrer depuis Hermes
source_url: https://docs.openclaw.ai/fr/install/migrating-hermes
scraped_at: 2026-05-25
---

OpenClaw importe l’état Hermes via un fournisseur de migration intégré. Le fournisseur prévisualise tout avant de modifier l’état, masque les secrets dans les plans et les rapports, et crée une sauvegarde vérifiée avant l’application.

## Deux façons d’importer

### Assistant d’intégration

Le chemin le plus rapide. L’assistant détecte Hermes dans `~/.hermes` et affiche une prévisualisation avant l’application.

bashCopy code
[code]
    openclaw onboard --flow import
[/code]

Ou indiquez une source spécifique :

bashCopy code
[code]
    openclaw onboard --import-from hermes --import-source ~/.hermes
[/code]

### CLI

Utilisez `openclaw migrate` pour les exécutions scriptées ou reproductibles. Consultez [`openclaw migrate`](</fr/cli/migrate>) pour la référence complète.

bashCopy code
[code]
    openclaw migrate hermes --dry-run    # preview onlyopenclaw migrate apply hermes --yes  # apply with confirmation skipped
[/code]

Ajoutez `--from <path>` lorsque Hermes se trouve hors de `~/.hermes`.

## Ce qui est importé

Configuration du modèle

  * Sélection du modèle par défaut depuis le `config.yaml` de Hermes.
  * Fournisseurs de modèles configurés et points de terminaison personnalisés compatibles OpenAI depuis `providers` et `custom_providers`.

Serveurs MCP

Définitions de serveurs MCP depuis `mcp_servers` ou `mcp.servers`.

Fichiers de l’espace de travail

  * `SOUL.md` et `AGENTS.md` sont copiés dans l’espace de travail de l’agent OpenClaw.
  * `memories/MEMORY.md` et `memories/USER.md` sont **ajoutés** aux fichiers de mémoire OpenClaw correspondants au lieu de les remplacer.

Configuration de la mémoire

Valeurs par défaut de configuration de la mémoire pour la mémoire de fichiers OpenClaw. Les fournisseurs de mémoire externes comme Honcho sont enregistrés comme éléments d’archive ou de révision manuelle afin que vous puissiez les déplacer délibérément.

Skills

Les Skills comportant un fichier `SKILL.md` sous `skills/<name>/` sont copiées, avec les valeurs de configuration propres à chaque Skill depuis `skills.config`.

Clés d’API (optionnel)

Définissez `--include-secrets` pour importer les clés `.env` prises en charge : `OPENAI_API_KEY`, `ANTHROPIC_API_KEY`, `OPENROUTER_API_KEY`, `GOOGLE_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`, `XAI_API_KEY`, `MISTRAL_API_KEY`, `DEEPSEEK_API_KEY`. Sans cet indicateur, les secrets ne sont jamais copiés.

## Ce qui reste uniquement archivé

Le fournisseur copie ces éléments dans le répertoire de rapport de migration pour révision manuelle, mais ne les charge **pas** dans la configuration ou les identifiants OpenClaw actifs :

  * `plugins/`
  * `sessions/`
  * `logs/`
  * `cron/`
  * `mcp-tokens/`
  * `auth.json`
  * `state.db`


OpenClaw refuse d’exécuter cet état ou de lui faire automatiquement confiance, car les formats et les hypothèses de confiance peuvent diverger entre les systèmes. Déplacez manuellement ce dont vous avez besoin après avoir examiné l’archive.

## Flux recommandé

* ### Prévisualiser le plan

bashCopy code
[code]
    openclaw migrate hermes --dry-run
[/code]

Le plan répertorie tout ce qui changera, y compris les conflits, les éléments ignorés et tout élément sensible. La sortie du plan masque les clés imbriquées qui ressemblent à des secrets.

* ### Appliquer avec sauvegarde

bashCopy code
[code]
    openclaw migrate apply hermes --yes
[/code]

OpenClaw crée et vérifie une sauvegarde avant d’appliquer. Si vous devez importer des clés d’API, ajoutez `--include-secrets`.

* ### Exécuter doctor

bashCopy code
[code]
    openclaw doctor
[/code]

[Doctor](</fr/gateway/doctor>) réapplique toute migration de configuration en attente et recherche les problèmes introduits pendant l’import.

* ### Redémarrer et vérifier

bashCopy code
[code]
    openclaw gateway restartopenclaw status
[/code]

Confirmez que le Gateway est sain et que votre modèle, votre mémoire et vos Skills importés sont chargés.

## Gestion des conflits

L’application refuse de continuer lorsque le plan signale des conflits (un fichier ou une valeur de configuration existe déjà à la cible).

Pour une installation OpenClaw propre, les conflits sont inhabituels. Ils apparaissent généralement lorsque vous relancez l’import sur une configuration qui comporte déjà des modifications utilisateur.

Si un conflit survient en cours d’application (par exemple, une course inattendue sur un fichier de configuration), Hermes marque les éléments de configuration dépendants restants comme `skipped` avec la raison `blocked by earlier apply conflict` au lieu de les écrire partiellement. Le rapport de migration enregistre chaque élément bloqué afin que vous puissiez résoudre le conflit d’origine et relancer l’import.

## Secrets

Les secrets ne sont jamais importés par défaut.

  * Exécutez d’abord `openclaw migrate apply hermes --yes` pour importer l’état non secret.
  * Si vous souhaitez aussi copier les clés `.env` prises en charge, relancez avec `--include-secrets`.
  * Pour les identifiants gérés par SecretRef, configurez la source SecretRef une fois l’import terminé.


## Sortie JSON pour l’automatisation

bashCopy code
[code]
    openclaw migrate hermes --dry-run --jsonopenclaw migrate apply hermes --json --yes
[/code]

Avec `--json` et sans `--yes`, l’application affiche le plan et ne modifie pas l’état. C’est le mode le plus sûr pour la CI et les scripts partagés.

## Dépannage

L’application refuse avec des conflits

Inspectez la sortie du plan. Chaque conflit identifie le chemin source et la cible existante. Décidez pour chaque élément s’il faut l’ignorer, modifier la cible ou relancer avec `--overwrite`.

Hermes se trouve hors de ~/.hermes

Passez `--from /actual/path` (CLI) ou `--import-source /actual/path` (intégration).

L’intégration refuse d’importer sur une configuration existante

Les imports d’intégration nécessitent une configuration propre. Réinitialisez l’état et relancez l’intégration, ou utilisez directement `openclaw migrate apply hermes`, qui prend en charge `--overwrite` et le contrôle explicite de la sauvegarde.

Les clés d’API n’ont pas été importées

`--include-secrets` est requis, et seules les clés listées ci-dessus sont reconnues. Les autres variables dans `.env` sont ignorées.

## Associés

  * [`openclaw migrate`](</fr/cli/migrate>) : référence CLI complète, contrat de plugin et formes JSON.
  * [Intégration](</fr/cli/onboard>) : flux de l’assistant et indicateurs non interactifs.
  * [Migration](</fr/install/migrating>) : déplacer une installation OpenClaw entre machines.
  * [Doctor](</fr/gateway/doctor>) : contrôle de santé post-migration.
  * [Espace de travail de l’agent](</fr/concepts/agent-workspace>) : emplacement de `SOUL.md`, `AGENTS.md` et des fichiers de mémoire.


Was this useful?YesNo