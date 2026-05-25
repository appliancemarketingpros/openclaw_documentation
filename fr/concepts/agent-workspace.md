---
title: Espace de travail de l’agent
source_url: https://docs.openclaw.ai/fr/concepts/agent-workspace
scraped_at: 2026-05-25
---

L’espace de travail est le domicile de l’agent. C’est le seul répertoire de travail utilisé pour les outils de fichiers et pour le contexte de l’espace de travail. Gardez-le privé et traitez-le comme de la mémoire.

Il est distinct de `~/.openclaw/`, qui stocke la configuration, les identifiants et les sessions.

## Emplacement par défaut

  * Par défaut : `~/.openclaw/workspace`
  * Si `OPENCLAW_PROFILE` est défini et n’est pas `"default"`, la valeur par défaut devient `~/.openclaw/workspace-<profile>`.
  * Remplacement dans `~/.openclaw/openclaw.json` :

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

`openclaw onboard`, `openclaw configure` ou `openclaw setup` créeront l’espace de travail et amorceront les fichiers de démarrage s’ils sont absents.

Si vous gérez déjà vous-même les fichiers de l’espace de travail, vous pouvez désactiver la création des fichiers de démarrage :

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## Dossiers d’espace de travail supplémentaires

Des installations plus anciennes peuvent avoir créé `~/openclaw`. Conserver plusieurs répertoires d’espace de travail peut entraîner une dérive déroutante de l’authentification ou de l’état, car un seul espace de travail est actif à la fois.

## Carte des fichiers de l’espace de travail

Voici les fichiers standards qu’OpenClaw attend dans l’espace de travail :

AGENTS.md - instructions de fonctionnement

Instructions de fonctionnement pour l’agent et la manière dont il doit utiliser la mémoire. Chargées au début de chaque session. Bon emplacement pour les règles, les priorités et les détails de type « comment se comporter ».

SOUL.md - persona et ton

Persona, ton et limites. Chargé à chaque session. Guide : [guide de personnalité SOUL.md](</fr/concepts/soul>).

USER.md - identité de l’utilisateur

Qui est l’utilisateur et comment s’adresser à lui. Chargé à chaque session.

IDENTITY.md - nom, ambiance, emoji

Le nom, l’ambiance et l’emoji de l’agent. Créé/mis à jour pendant le rituel de démarrage.

TOOLS.md - conventions des outils locaux

Notes sur vos outils locaux et leurs conventions. Ne contrôle pas la disponibilité des outils ; il s’agit uniquement de conseils.

HEARTBEAT.md - liste de vérification Heartbeat

Petite liste de vérification facultative pour les exécutions Heartbeat. Gardez-la courte pour éviter la consommation de tokens.

BOOT.md - liste de vérification de démarrage

Liste de vérification de démarrage facultative exécutée automatiquement au redémarrage du Gateway (lorsque les [hooks internes](</fr/automation/hooks>) sont activés). Gardez-la courte ; utilisez l’outil de message pour les envois sortants.

BOOTSTRAP.md - rituel de première exécution

Rituel unique de première exécution. Créé uniquement pour un tout nouvel espace de travail. Supprimez-le une fois le rituel terminé.

memory/YYYY-MM-DD.md - journal de mémoire quotidien

Journal de mémoire quotidien (un fichier par jour). Il est recommandé de lire aujourd’hui + hier au démarrage de la session.

MEMORY.md - mémoire à long terme organisée (facultatif)

Mémoire à long terme organisée : faits durables, préférences, décisions et courts résumés. Conservez les journaux détaillés dans `memory/YYYY-MM-DD.md` afin que les outils de mémoire puissent les récupérer à la demande sans les injecter dans chaque prompt. Ne chargez `MEMORY.md` que dans la session principale privée (pas dans les contextes partagés/de groupe). Consultez [Mémoire](</fr/concepts/memory>) pour le workflow et le vidage automatique de la mémoire.

skills/ - Skills d’espace de travail (facultatif)

Skills propres à l’espace de travail. Emplacement de Skill avec la priorité la plus élevée pour cet espace de travail. Remplace les Skills d’agent de projet, les Skills d’agent personnelles, les Skills gérées, les Skills intégrées et `skills.load.extraDirs` lorsque les noms entrent en collision.

canvas/ - fichiers d’interface Canvas (facultatif)

Fichiers d’interface Canvas pour les affichages de nœuds (par exemple `canvas/index.html`).

## Ce qui n’est PAS dans l’espace de travail

Ces éléments se trouvent sous `~/.openclaw/` et ne doivent PAS être commités dans le dépôt de l’espace de travail :

  * `~/.openclaw/openclaw.json` (configuration)
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (profils d’authentification de modèle : OAuth + clés API)
  * `~/.openclaw/agents/<agentId>/agent/codex-home/` (compte d’exécution Codex par agent, configuration, Skills, plugins et état de thread natif)
  * `~/.openclaw/credentials/` (état des canaux/fournisseurs plus données d’import OAuth héritées)
  * `~/.openclaw/agents/<agentId>/sessions/` (transcriptions de session + métadonnées)
  * `~/.openclaw/skills/` (Skills gérées)


Si vous devez migrer des sessions ou une configuration, copiez-les séparément et gardez-les hors du contrôle de version.

## Sauvegarde Git (recommandée, privée)

Traitez l’espace de travail comme une mémoire privée. Placez-le dans un dépôt git **privé** afin qu’il soit sauvegardé et récupérable.

Exécutez ces étapes sur la machine où le Gateway s’exécute (c’est là que se trouve l’espace de travail).

* ### Initialiser le dépôt

Si git est installé, les tout nouveaux espaces de travail sont initialisés automatiquement. Si cet espace de travail n’est pas déjà un dépôt, exécutez :

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### Ajouter un dépôt distant privé

### Interface web GitHub

  1. Créez un nouveau dépôt **privé** sur GitHub.
  2. Ne l’initialisez pas avec un README (évite les conflits de fusion).
  3. Copiez l’URL distante HTTPS.
  4. Ajoutez le dépôt distant et poussez :

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### Interface web GitLab

  1. Créez un nouveau dépôt **privé** sur GitLab.
  2. Ne l’initialisez pas avec un README (évite les conflits de fusion).
  3. Copiez l’URL distante HTTPS.
  4. Ajoutez le dépôt distant et poussez :

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### Mises à jour continues

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## Ne commitez pas de secrets

Début de `.gitignore` suggéré :

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## Déplacer l’espace de travail vers une nouvelle machine

* ### Cloner le dépôt

Clonez le dépôt vers le chemin souhaité (par défaut `~/.openclaw/workspace`).

* ### Mettre à jour la configuration

Définissez `agents.defaults.workspace` sur ce chemin dans `~/.openclaw/openclaw.json`.

* ### Amorcer les fichiers manquants

Exécutez `openclaw setup --workspace <path>` pour amorcer tous les fichiers manquants.

* ### Copier les sessions (facultatif)

Si vous avez besoin des sessions, copiez séparément `~/.openclaw/agents/<agentId>/sessions/` depuis l’ancienne machine.

## Notes avancées

  * Le routage multi-agent peut utiliser différents espaces de travail par agent. Consultez [Routage des canaux](</fr/channels/channel-routing>) pour la configuration du routage.
  * Si `agents.defaults.sandbox` est activé, les sessions non principales peuvent utiliser des espaces de travail sandbox par session sous `agents.defaults.sandbox.workspaceRoot`.


## Connexe

  * [Heartbeat](</fr/gateway/heartbeat>) \- fichier d’espace de travail [HEARTBEAT.md](<http://HEARTBEAT.md>)
  * [Sandboxing](</fr/gateway/sandboxing>) \- accès à l’espace de travail dans les environnements sandboxés
  * [Session](</fr/concepts/session>) \- chemins de stockage des sessions
  * [Ordres permanents](</fr/automation/standing-orders>) \- instructions persistantes dans les fichiers de l’espace de travail


Was this useful?YesNo