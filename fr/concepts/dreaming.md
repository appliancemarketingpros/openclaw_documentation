---
title: Dreaming
source_url: https://docs.openclaw.ai/fr/concepts/dreaming
scraped_at: 2026-05-25
---

Dreaming est le système de consolidation de mémoire en arrière-plan dans `memory-core`. Il aide OpenClaw à déplacer les signaux forts à court terme vers une mémoire durable tout en gardant le processus explicable et révisable.

## Ce que Dreaming écrit

Dreaming conserve deux types de sortie :

  * **État machine** dans `memory/.dreams/` (magasin de rappel, signaux de phase, points de reprise d’ingestion, verrous).
  * **Sortie lisible par l’humain** dans `DREAMS.md` (ou le fichier `dreams.md` existant) et les fichiers optionnels de rapport de phase sous `memory/dreaming/<phase>/YYYY-MM-DD.md`.


La promotion à long terme écrit toujours uniquement dans `MEMORY.md`.

## Modèle de phases

Dreaming utilise trois phases coopératives :

Phase | Objectif | Écriture durable  
---|---|---  
Légère | Trier et préparer le contenu récent à court terme | Non  
Profonde | Noter et promouvoir les candidats durables | Oui (`MEMORY.md`)  
REM | Réfléchir aux thèmes et aux idées récurrentes | Non  
  
Ces phases sont des détails d’implémentation internes, pas des « modes » séparés configurés par l’utilisateur.

Phase légère

La phase légère ingère les signaux récents de mémoire quotidienne et les traces de rappel, les déduplique et prépare les lignes candidates.

  * Lit l’état de rappel à court terme, les fichiers récents de mémoire quotidienne et les transcriptions de session expurgées lorsqu’elles sont disponibles.
  * Écrit un bloc `## Light Sleep` géré lorsque le stockage inclut une sortie en ligne.
  * Enregistre les signaux de renforcement pour le classement profond ultérieur.
  * N’écrit jamais dans `MEMORY.md`.

Phase profonde

La phase profonde décide de ce qui devient de la mémoire à long terme.

  * Classe les candidats à l’aide d’un score pondéré et de seuils de validation.
  * Exige que `minScore`, `minRecallCount` et `minUniqueQueries` soient satisfaits.
  * Réhydrate les extraits depuis les fichiers quotidiens actifs avant l’écriture, afin que les extraits obsolètes ou supprimés soient ignorés.
  * Ajoute les entrées promues à `MEMORY.md`.
  * Écrit un résumé `## Deep Sleep` dans `DREAMS.md` et écrit éventuellement `memory/dreaming/deep/YYYY-MM-DD.md`.

Phase REM

La phase REM extrait les motifs et les signaux réflexifs.

  * Construit des résumés de thèmes et de réflexions à partir des traces récentes à court terme.
  * Écrit un bloc `## REM Sleep` géré lorsque le stockage inclut une sortie en ligne.
  * Enregistre les signaux de renforcement REM utilisés par le classement profond.
  * N’écrit jamais dans `MEMORY.md`.


## Ingestion des transcriptions de session

Dreaming peut ingérer des transcriptions de session expurgées dans le corpus de Dreaming. Lorsque des transcriptions sont disponibles, elles sont fournies à la phase légère avec les signaux de mémoire quotidienne et les traces de rappel. Le contenu personnel et sensible est expurgé avant l’ingestion.

## Journal des rêves

Dreaming conserve aussi un **Journal des rêves** narratif dans `DREAMS.md`. Une fois que chaque phase dispose d’assez de contenu, `memory-core` exécute un tour de sous-agent en arrière-plan au mieux et ajoute une courte entrée de journal. Il utilise le modèle d’exécution par défaut sauf si `dreaming.model` est configuré. Si le modèle configuré est indisponible, le Journal des rêves réessaie une fois avec le modèle par défaut de la session.

Il existe aussi une voie de remplissage historique fondée pour les travaux de révision et de récupération :

Commandes de remplissage

  * `memory rem-harness --path ... --grounded` prévisualise la sortie de journal fondée à partir des notes historiques `YYYY-MM-DD.md`.
  * `memory rem-backfill --path ...` écrit des entrées de journal fondées et réversibles dans `DREAMS.md`.
  * `memory rem-backfill --path ... --stage-short-term` prépare les candidats durables fondés dans le même magasin de preuves à court terme que la phase profonde normale utilise déjà.
  * `memory rem-backfill --rollback` et `--rollback-short-term` suppriment ces artefacts de remplissage préparés sans toucher aux entrées de journal ordinaires ni au rappel à court terme actif.


L’interface de contrôle expose le même flux de remplissage/réinitialisation du journal afin que vous puissiez inspecter les résultats dans la scène Dreams avant de décider si les candidats fondés méritent une promotion. La scène affiche aussi une voie fondée distincte afin que vous puissiez voir quelles entrées à court terme préparées proviennent d’une relecture historique, quels éléments promus ont été pilotés par du contenu fondé, et effacer uniquement les entrées préparées exclusivement fondées sans toucher à l’état ordinaire actif à court terme.

## Signaux de classement profond

Le classement profond utilise six signaux de base pondérés plus le renforcement de phase :

Signal | Poids | Description  
---|---|---  
Fréquence | 0.24 | Nombre de signaux à court terme accumulés par l’entrée  
Pertinence | 0.30 | Qualité moyenne de récupération pour l’entrée  
Diversité des requêtes | 0.15 | Contextes distincts de requête/jour qui l’ont fait ressortir  
Récence | 0.15 | Score de fraîcheur avec décroissance temporelle  
Consolidation | 0.10 | Force de récurrence sur plusieurs jours  
Richesse conceptuelle | 0.06 | Densité des balises de concept issues de l’extrait/du chemin  
  
Les occurrences des phases légère et REM ajoutent un léger bonus avec décroissance de récence depuis `memory/.dreams/phase-signals.json`.

## Planification

Lorsqu’il est activé, `memory-core` gère automatiquement une tâche cron pour un balayage complet de Dreaming. Chaque balayage exécute les phases dans l’ordre : légère → REM → profonde.

Le balayage inclut l’espace de travail d’exécution principal et tous les espaces de travail d’agent configurés, dédupliqués par chemin, afin que la dispersion des espaces de travail de sous-agents n’exclue pas le `DREAMS.md` et l’état mémoire de l’agent principal.

Comportement de cadence par défaut :

Paramètre | Par défaut  
---|---  
`dreaming.frequency` | `0 3 * * *`  
`dreaming.model` | modèle par défaut  
  
## Démarrage rapide

### Activer Dreaming

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true          }        }      }    }  }}
[/code]

### Cadence de balayage personnalisée

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true,            "timezone": "America/Los_Angeles",            "frequency": "0 */6 * * *"          }        }      }    }  }}
[/code]

## Commande slash

CodeCopy code
[code]
    /dreaming status/dreaming on/dreaming off/dreaming help
[/code]

## Flux de travail CLI

### Prévisualiser / appliquer une promotion

bashCopy code
[code]
    openclaw memory promoteopenclaw memory promote --applyopenclaw memory promote --limit 5openclaw memory status --deep
[/code]

La commande manuelle `memory promote` utilise par défaut les seuils de la phase profonde, sauf remplacement par des indicateurs CLI.

### Expliquer la promotion

Explique pourquoi un candidat précis serait ou ne serait pas promu :

bashCopy code
[code]
    openclaw memory promote-explain "router vlan"openclaw memory promote-explain "router vlan" --json
[/code]

### Prévisualisation du harnais REM

Prévisualisez les réflexions REM, les vérités candidates et la sortie de promotion profonde sans rien écrire :

bashCopy code
[code]
    openclaw memory rem-harnessopenclaw memory rem-harness --json
[/code]

## Valeurs par défaut clés

Tous les paramètres se trouvent sous `plugins.entries.memory-core.config.dreaming`.

Active ou désactive le balayage Dreaming.

Cadence Cron du balayage Dreaming complet.

Remplacement optionnel du modèle du sous-agent Journal des rêves. Utilisez une valeur canonique `provider/model` lorsque vous définissez aussi une liste d’autorisation `allowedModels` de sous-agent.

## Interface Dreams

Lorsqu’il est activé, l’onglet **Dreams** du Gateway affiche :

  * l’état actuel d’activation de Dreaming
  * le statut par phase et la présence d’un balayage géré
  * les décomptes à court terme, fondés, de signaux et promus aujourd’hui
  * le moment de la prochaine exécution planifiée
  * une voie de scène fondée distincte pour les entrées de relecture historique préparées
  * un lecteur extensible de Journal des rêves alimenté par `doctor.memory.dreamDiary`


## Dreaming ne s’exécute jamais : le statut indique un blocage

Si `openclaw memory status` signale `Dreaming status: blocked`, le cron géré existe mais le Heartbeat de l’agent par défaut ne se déclenche pas. Vérifiez que le Heartbeat est activé pour l’agent par défaut et que sa cible n’est pas `none`, puis exécutez de nouveau `openclaw memory status --deep` après le prochain intervalle de Heartbeat.

## Connexe

  * [Mémoire](</fr/concepts/memory>)
  * [CLI de mémoire](</fr/cli/memory>)
  * [Référence de configuration de la mémoire](</fr/reference/memory-config>)
  * [Recherche de mémoire](</fr/concepts/memory-search>)


Was this useful?YesNo