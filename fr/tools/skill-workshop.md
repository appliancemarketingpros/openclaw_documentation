---
title: Atelier Skills
source_url: https://docs.openclaw.ai/fr/tools/skill-workshop
scraped_at: 2026-06-29
---

CapabilitiesSkills

Skill Workshop est le parcours gouverné d’OpenClaw pour créer et mettre à jour les skills d’espace de travail.

Les agents et les opérateurs n’écrivent pas directement les fichiers `SKILL.md` actifs par ce parcours. Ils créent d’abord une **proposition**. Une proposition est un brouillon en attente contenant le contenu de skill proposé, la liaison de cible, l’état du scanner, les hachages, les métadonnées des fichiers de support et les métadonnées de rollback. Elle devient un skill actif uniquement une fois appliquée.

Skill Workshop écrit uniquement les skills d’espace de travail. Il ne modifie pas les skills groupés, de Plugin, ClawHub, de racine supplémentaire, administrés, d’agent personnel ou système.

## Fonctionnement

  * **Proposition d’abord :** le contenu de skill généré est stocké sous `PROPOSAL.md`, pas sous `SKILL.md`.
  * **Appliquer est la seule écriture active :** créer, mettre à jour et réviser ne modifient pas les skills actifs.
  * **Portée limitée à l’espace de travail :** les créations ciblent la racine `skills/` de l’espace de travail. Les mises à jour sont autorisées uniquement pour les skills d’espace de travail inscriptibles.
  * **Aucun écrasement :** la création échoue si le skill cible existe déjà.
  * **Lié au hachage :** les propositions de mise à jour se lient au hachage actuel de la cible et deviennent obsolètes si le skill actif change avant l’application.
  * **Contrôlé par scanner :** l’application relance le scan avant l’écriture.
  * **Récupérable :** l’application écrit les métadonnées de rollback avant de modifier les fichiers actifs.
  * **Surfaces cohérentes :** le chat, la CLI et le Gateway appellent tous le même service Skill Workshop.


## Cycle de vie

textCopy code
[code]
    create/update -> pendingrevise        -> pendingapply         -> appliedreject        -> rejectedquarantine    -> quarantinedtarget change -> stale
[/code]

Seules les propositions `pending` peuvent être révisées, appliquées, rejetées ou mises en quarantaine.

## Chat

Demandez à l’agent le skill souhaité. L’agent appelle `skill_workshop` et renvoie un identifiant de proposition.

Créer :

textCopy code
[code]
    Make a skill called morning-catchup that runs my Monday inbox routine.
[/code]

Mettre à jour un skill d’espace de travail existant :

textCopy code
[code]
    Update trip-planning to also check seat maps before booking.
[/code]

Itérer sur une proposition en attente :

textCopy code
[code]
    Show me the morning-catchup proposal.Revise it to also flag anything marked urgent.Apply the morning-catchup proposal.
[/code]

Par défaut, les actions `apply`, `reject` et `quarantine` initiées par l’agent affichent une invite d’approbation avant leur exécution. Définissez `skills.workshop.approvalPolicy` sur `"auto"` pour ignorer l’invite dans les environnements de confiance.

## CLI

Créer une nouvelle proposition de skill :

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name morning-catchup \  --description "Daily inbox catch-up: triage, archive, surface, draft, plan" \  --proposal ./PROPOSAL.md
[/code]

Créer une proposition de mise à jour pour un skill d’espace de travail existant :

bashCopy code
[code]
    openclaw skills workshop propose-update trip-planning --proposal ./PROPOSAL.md
[/code]

Lister et inspecter :

bashCopy code
[code]
    openclaw skills workshop listopenclaw skills workshop inspect <proposal-id>
[/code]

Réviser avant approbation :

bashCopy code
[code]
    openclaw skills workshop revise <proposal-id> --proposal ./PROPOSAL.md
[/code]

Clore la proposition :

bashCopy code
[code]
    openclaw skills workshop apply <proposal-id>openclaw skills workshop reject <proposal-id> --reason "Duplicate"openclaw skills workshop quarantine <proposal-id> --reason "Needs security review"
[/code]

## Contenu de la proposition

Tant qu’elle est en attente, la proposition est stockée sous `PROPOSAL.md` avec un frontmatter propre aux propositions :

markdownCopy code
[code]
    ---name: "morning-catchup"description: "Daily inbox catch-up: triage, archive, surface, draft, plan"status: proposalversion: "v1"date: "2026-05-30T00:00:00.000Z"---
[/code]

Lors de l’application, Skill Workshop écrit le `SKILL.md` actif et supprime les champs propres à la proposition : `status`, la `version` de proposition et la `date` de proposition.

## Fichiers de support

Utilisez `--proposal-dir` lorsque le skill proposé a besoin de fichiers à côté de `PROPOSAL.md` :

bashCopy code
[code]
    openclaw skills workshop propose-create \  --name weekly-update \  --description "Friday wrap-up: stats, highlights, next week's top three" \  --proposal-dir ./weekly-update-proposal
[/code]

Le répertoire doit contenir `PROPOSAL.md`. Les fichiers de support doivent se trouver sous :

  * `assets/`
  * `examples/`
  * `references/`
  * `scripts/`
  * `templates/`


Skill Workshop scanne, hache et stocke les fichiers de support avec la proposition. Ils sont écrits à côté du `SKILL.md` actif uniquement lors de l’application.

Les chemins de fichiers de support rejetés incluent les chemins absolus, les segments de chemin masqués, la traversée de chemins, les chemins qui se chevauchent, les fichiers exécutables issus de répertoires de proposition, le texte non UTF-8, les octets nuls et les fichiers hors des dossiers de support standard.

## Outil d’agent

Le modèle utilise `skill_workshop` :

textCopy code
[code]
    action: create | update | revise | list | inspect | apply | reject | quarantine
[/code]

Les agents doivent utiliser `skill_workshop` pour le travail de skill généré. Ils ne doivent pas créer ni modifier les fichiers de proposition au moyen de `write`, `edit`, `exec`, de commandes shell ou d’opérations directes sur le système de fichiers.

## Approbation et autonomie

json5Copy code
[code]
    {  skills: {    workshop: {      autonomous: {        enabled: false,      },      allowSymlinkTargetWrites: false,      approvalPolicy: "pending",      maxPending: 50,      maxSkillBytes: 40000,    },  },}
[/code]

  * `autonomous.enabled` : autorise OpenClaw à créer des propositions en attente à partir de signaux de conversation durables après des tours réussis. Par défaut : `false`.
  * `allowSymlinkTargetWrites` : autorise l’application à écrire à travers les liens symboliques de skills d’espace de travail dont la cible réelle est listée dans `skills.load.allowSymlinkTargets`. Par défaut : `false`.
  * `approvalPolicy: "pending"` : exige une invite d’approbation avant une action `apply`, `reject` ou `quarantine` initiée par l’agent.
  * `approvalPolicy: "auto"` : ignore cette invite d’approbation. L’agent doit tout de même appeler l’action.
  * `maxPending` : limite les propositions en attente et mises en quarantaine par espace de travail.
  * `maxSkillBytes` : limite la taille du corps de la proposition. Par défaut : `40000`.


Les descriptions de proposition sont toujours limitées à 160 octets.

## Méthodes Gateway

textCopy code
[code]
    skills.proposals.listskills.proposals.inspectskills.proposals.createskills.proposals.updateskills.proposals.reviseskills.proposals.applyskills.proposals.rejectskills.proposals.quarantine
[/code]

Les méthodes en lecture seule nécessitent `operator.read`. Les méthodes mutantes nécessitent `operator.admin`.

## Stockage

textCopy code
[code]
    &lt;OPENCLAW_STATE_DIR&gt;/skill-workshop/  proposals.json  proposals/<proposal-id>/    proposal.json    PROPOSAL.md    rollback.json    assets/    examples/    references/    scripts/    templates/
[/code]

Répertoire d’état par défaut : `~/.openclaw`.

  * `proposal.json` : enregistrement canonique de la proposition.
  * `proposals.json` : index de listage rapide, reconstructible à partir des dossiers de proposition.
  * `PROPOSAL.md` : proposition de skill en attente.
  * `rollback.json` : métadonnées de récupération écrites avant que l’application ne modifie les fichiers actifs.


## Limites

  * Description : 160 octets.
  * Corps de proposition : `skills.workshop.maxSkillBytes` (40 000 par défaut).
  * Fichiers de support : 64 par proposition.
  * Taille des fichiers de support : 256 Ko chacun, 2 Mo au total.
  * Propositions en attente et mises en quarantaine : `skills.workshop.maxPending` par espace de travail (50 par défaut).


## Dépannage

Problème | Résolution  
---|---  
`Skill proposal description is too large` | Raccourcissez `description` à 160 octets ou moins.  
`Skill proposal content is too large` | Raccourcissez le corps de la proposition ou augmentez `skills.workshop.maxSkillBytes`.  
`Target skill changed after proposal creation` | Révisez la proposition par rapport à la cible actuelle, ou créez une nouvelle proposition.  
`Proposal scan failed` | Inspectez les résultats du scanner, puis révisez ou mettez la proposition en quarantaine.  
`untrusted symlink target` | Configurez `skills.load.allowSymlinkTargets` et activez `skills.workshop.allowSymlinkTargetWrites` uniquement pour les racines de skills partagées intentionnelles.  
`Support file paths must be under one of...` | Déplacez les fichiers de support sous `assets/`, `examples/`, `references/`, `scripts/` ou `templates/`.  
La proposition n’apparaît pas dans la liste | Vérifiez l’espace de travail `--agent` sélectionné et `OPENCLAW_STATE_DIR`.  
L’agent ne peut pas appeler `skill_workshop` | Vérifiez la politique d’outils active et le mode d’exécution. `coding` inclut l’outil ; les politiques `tools.allow` restrictives doivent le lister explicitement, et les exécutions sandboxées doivent utiliser une session d’agent normale côté hôte ou la CLI.  
  
## Connexe

  * [Skills](</fr/tools/skills>) pour l’ordre de chargement, la priorité et la visibilité
  * [Créer des skills](</fr/tools/creating-skills>) pour les bases d’un `SKILL.md` écrit à la main
  * [Configuration des Skills](</fr/tools/skills-config>) pour le schéma complet `skills.workshop`
  * [CLI Skills](</fr/cli/skills>) pour les commandes `openclaw skills`


Was this useful?YesNo

Open issue