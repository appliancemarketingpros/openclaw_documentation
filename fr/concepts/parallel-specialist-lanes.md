---
title: Voies spécialisées parallèles
source_url: https://docs.openclaw.ai/fr/concepts/parallel-specialist-lanes
scraped_at: 2026-05-25
---

Les voies spécialisées parallèles permettent à un même Gateway d’acheminer différentes discussions ou différents salons vers différents agents, tout en gardant une expérience utilisateur rapide. L’astuce consiste à traiter le parallélisme comme un problème de conception lié à une ressource rare, et pas seulement comme « plus d’agents ».

## Principes fondamentaux

Une voie spécialisée n’améliore le débit que lorsqu’elle réduit la contention sur les véritables goulots d’étranglement :

  * **Verrous de session** : une seule exécution doit modifier une session donnée à la fois.
  * **Capacité globale du modèle** : toutes les exécutions de discussion visibles partagent toujours les limites du fournisseur.
  * **Capacité des outils** : le shell, le navigateur, le réseau et le travail sur le dépôt peuvent être plus lents que le tour de modèle lui-même.
  * **Budget de contexte** : les longs historiques rendent chaque tour futur plus lent et moins ciblé.
  * **Ambiguïté de responsabilité** : des agents en double qui font le même travail gaspillent de la capacité.


OpenClaw sérialise déjà les exécutions par session et plafonne le parallélisme global via la [file de commandes](</fr/concepts/queue>). Les voies spécialisées ajoutent une politique par-dessus : quel agent possède quel travail, ce qui reste dans la discussion, et ce qui devient un travail en arrière-plan.

## Déploiement recommandé

### Phase 1 : contrats de voie + travail lourd en arrière-plan

Donnez à chaque voie un contrat écrit dans son espace de travail et son prompt système :

  * **Objectif** : le travail dont cette voie est responsable.
  * **Non-objectifs** : le travail qu’elle doit déléguer au lieu de tenter.
  * **Budget de discussion** : les réponses rapides restent dans la discussion ; les longues tâches doivent accuser réception brièvement, puis s’exécuter dans un sous-agent ou une tâche en arrière-plan.
  * **Règle de transfert** : lorsqu’une autre voie possède le travail, dites où il doit aller et fournissez un résumé compact de transfert.
  * **Règle de risque des outils** : privilégiez la plus petite surface d’outil capable d’effectuer le travail.


C’est la phase la moins coûteuse et elle corrige la plupart des engorgements : une tâche de codage ne transforme plus la voie de recherche en mélasse, et chaque discussion garde son propre contexte propre.

### Phase 2 : contrôles de priorité et de concurrence

Réglez la file et la capacité du modèle autour de la valeur métier de chaque voie :

json5Copy code
[code]
    {  agents: {    defaults: {      maxConcurrent: 4,      subagents: { maxConcurrent: 8, delegationMode: "prefer" },    },  },  messages: {    queue: {      mode: "collect",      debounceMs: 1000,      cap: 20,      drop: "summarize",    },  },}
[/code]

Utilisez les discussions directes/personnelles et les agents d’opérations de production pour le travail hautement prioritaire. Laissez la recherche, la rédaction et le codage par lots passer aux tâches en arrière-plan lorsque le système est occupé.

### Phase 3 : coordinateur / contrôleur de trafic

Ajoutez un petit modèle de coordinateur une fois que plusieurs voies sont actives :

  * Suivre les tâches de voie actives et leurs responsables.
  * Détecter les demandes en double entre les groupes.
  * Acheminer les résumés de transfert entre les voies.
  * Remonter uniquement les blocages, les résultats terminés et les décisions que l’humain doit prendre.


Ne commencez pas ici. Un coordinateur sans contrats de voie ne fait que coordonner le chaos.

## Modèle minimal de contrat de voie

mdCopy code
[code]
    # Lane contract ## Owns - <job this lane is responsible for> ## Does not own - <work to hand off> ## Chat budget - Answer quick questions directly.- For multi-step, slow, or tool-heavy work: acknowledge briefly, spawn/background  the work, then return the result when complete. ## Handoff If another lane owns the request, reply with: - target lane- objective- relevant context- exact next action ## Tool posture Use the smallest tool surface that can complete the task. Avoid broad shell ornetwork work unless this lane explicitly owns it.
[/code]

## Connexe

  * [Routage multi-agent](</fr/concepts/multi-agent>)
  * [File de commandes](</fr/concepts/queue>)
  * [Sous-agents](</fr/tools/subagents>)


Was this useful?YesNo