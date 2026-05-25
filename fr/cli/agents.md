---
title: Agents
source_url: https://docs.openclaw.ai/fr/cli/agents
scraped_at: 2026-05-25
---

# `openclaw agents`

Gérer des agents isolés (espaces de travail + authentification + routage).

Associé :

  * [Routage multi-agent](</fr/concepts/multi-agent>)
  * [Espace de travail de l’agent](</fr/concepts/agent-workspace>)
  * [Configuration des Skills](</fr/tools/skills-config>) : configuration de la visibilité des Skills.


## Exemples

bashCopy code
[code]
    openclaw agents listopenclaw agents list --bindingsopenclaw agents add work --workspace ~/.openclaw/workspace-workopenclaw agents add ops --workspace ~/.openclaw/workspace-ops --bind telegram:ops --non-interactiveopenclaw agents bindingsopenclaw agents bind --agent work --bind telegram:opsopenclaw agents unbind --agent work --bind telegram:opsopenclaw agents set-identity --workspace ~/.openclaw/workspace --from-identityopenclaw agents set-identity --agent main --avatar avatars/openclaw.pngopenclaw agents delete work
[/code]

## Liaisons de routage

Utilisez les liaisons de routage pour associer le trafic entrant d’un canal à un agent spécifique.

Si vous voulez aussi des Skills visibles différentes par agent, configurez `agents.defaults.skills` et `agents.list[].skills` dans `openclaw.json`. Consultez [Configuration des Skills](</fr/tools/skills-config>) et [Référence de configuration](</fr/gateway/config-agents#agents-defaults-skills>).

Lister les liaisons :

bashCopy code
[code]
    openclaw agents bindingsopenclaw agents bindings --agent workopenclaw agents bindings --json
[/code]

Ajouter des liaisons :

bashCopy code
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
[/code]

Si vous omettez `accountId` (`--bind <channel>`), OpenClaw le résout à partir des valeurs par défaut du canal et des hooks de configuration du plugin lorsqu’ils sont disponibles.

Si vous omettez `--agent` pour `bind` ou `unbind`, OpenClaw cible l’agent par défaut actuel.

### Comportement de portée des liaisons

  * Une liaison sans `accountId` correspond uniquement au compte par défaut du canal.
  * `accountId: "*"` est le repli à l’échelle du canal (tous les comptes) et est moins spécifique qu’une liaison de compte explicite.
  * Si le même agent possède déjà une liaison de canal correspondante sans `accountId`, et que vous ajoutez ensuite une liaison avec un `accountId` explicite ou résolu, OpenClaw met à niveau cette liaison existante sur place au lieu d’ajouter un doublon.


Exemple :

bashCopy code
[code]
    # initial channel-only bindingopenclaw agents bind --agent work --bind telegram # later upgrade to account-scoped bindingopenclaw agents bind --agent work --bind telegram:ops
[/code]

Après la mise à niveau, le routage de cette liaison est limité à `telegram:ops`. Si vous voulez aussi le routage du compte par défaut, ajoutez-le explicitement (par exemple `--bind telegram:default`).

Supprimer des liaisons :

bashCopy code
[code]
    openclaw agents unbind --agent work --bind telegram:opsopenclaw agents unbind --agent work --all
[/code]

`unbind` accepte soit `--all`, soit une ou plusieurs valeurs `--bind`, mais pas les deux.

## Surface de commande

### `agents`

Exécuter `openclaw agents` sans sous-commande équivaut à `openclaw agents list`.

### `agents list`

Options :

  * `--json`
  * `--bindings` : inclure les règles de routage complètes, pas seulement les comptages/résumés par agent


### `agents add [name]`

Options :

  * `--workspace <dir>`
  * `--model <id>`
  * `--agent-dir <dir>`
  * `--bind <channel[:accountId]>` (répétable)
  * `--non-interactive`
  * `--json`


Notes :

  * Passer des options d’ajout explicites fait basculer la commande vers le chemin non interactif.
  * Le mode non interactif nécessite à la fois un nom d’agent et `--workspace`.
  * `main` est réservé et ne peut pas être utilisé comme nouvel identifiant d’agent.
  * En mode interactif, l’amorçage de l’authentification copie uniquement les profils statiques portables (`api_key` et `token` statique par défaut). Les profils OAuth avec jeton d’actualisation restent disponibles uniquement par héritage en lecture depuis le vrai magasin de l’agent `main`. Si l’agent par défaut configuré n’est pas `main`, connectez-vous séparément pour les profils OAuth sur le nouvel agent.


### `agents bindings`

Options :

  * `--agent <id>`
  * `--json`


### `agents bind`

Options :

  * `--agent <id>` (par défaut, l’agent par défaut actuel)
  * `--bind <channel[:accountId]>` (répétable)
  * `--json`


### `agents unbind`

Options :

  * `--agent <id>` (par défaut, l’agent par défaut actuel)
  * `--bind <channel[:accountId]>` (répétable)
  * `--all`
  * `--json`


### `agents delete <id>`

Options :

  * `--force`
  * `--json`


Notes :

  * `main` ne peut pas être supprimé.
  * Sans `--force`, une confirmation interactive est requise.
  * Les répertoires de l’espace de travail, de l’état de l’agent et des transcriptions de session sont déplacés vers la corbeille, pas supprimés définitivement.
  * Lorsque le Gateway est joignable, la suppression est envoyée via le Gateway afin que le nettoyage de la configuration et du magasin de sessions utilise le même rédacteur que le trafic d’exécution. Si le Gateway n’est pas joignable, la CLI revient au chemin local hors ligne.
  * Si l’espace de travail d’un autre agent est le même chemin, se trouve dans cet espace de travail ou contient cet espace de travail, l’espace de travail est conservé et `--json` indique `workspaceRetained`, `workspaceRetainedReason` et `workspaceSharedWith`.


## Fichiers d’identité

Chaque espace de travail d’agent peut inclure un `IDENTITY.md` à la racine de l’espace de travail :

  * Chemin d’exemple : `~/.openclaw/workspace/IDENTITY.md`
  * `set-identity --from-identity` lit depuis la racine de l’espace de travail (ou depuis un `--identity-file` explicite)


Les chemins d’avatar sont résolus relativement à la racine de l’espace de travail.

## Définir l’identité

`set-identity` écrit les champs dans `agents.list[].identity` :

  * `name`
  * `theme`
  * `emoji`
  * `avatar` (chemin relatif à l’espace de travail, URL http(s) ou URI de données)


Options :

  * `--agent <id>`
  * `--workspace <dir>`
  * `--identity-file <path>`
  * `--from-identity`
  * `--name <name>`
  * `--theme <theme>`
  * `--emoji <emoji>`
  * `--avatar <value>`
  * `--json`


Notes :

  * `--agent` ou `--workspace` peut être utilisé pour sélectionner l’agent cible.
  * Si vous vous appuyez sur `--workspace` et que plusieurs agents partagent cet espace de travail, la commande échoue et vous demande de passer `--agent`.
  * Lorsqu’aucun champ d’identité explicite n’est fourni, la commande lit les données d’identité depuis `IDENTITY.md`.


Charger depuis `IDENTITY.md` :

bashCopy code
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
[/code]

Remplacer explicitement les champs :

bashCopy code
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
[/code]

Exemple de configuration :

json5Copy code
[code]
    {  agents: {    list: [      {        id: "main",        identity: {          name: "OpenClaw",          theme: "space lobster",          emoji: "🦞",          avatar: "avatars/openclaw.png",        },      },    ],  },}
[/code]

## Associé

  * [Référence CLI](</fr/cli>)
  * [Routage multi-agent](</fr/concepts/multi-agent>)
  * [Espace de travail de l’agent](</fr/concepts/agent-workspace>)


Was this useful?YesNo