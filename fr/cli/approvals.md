---
title: Approbations
source_url: https://docs.openclaw.ai/fr/cli/approvals
scraped_at: 2026-05-25
---

# `openclaw approvals`

Gérez les approbations d’exécution pour **l’hôte local** , **l’hôte gateway** ou un **hôte Node**. Par défaut, les commandes ciblent le fichier d’approbations local sur disque. Utilisez `--gateway` pour cibler le gateway, ou `--node` pour cibler un Node spécifique.

Alias : `openclaw exec-approvals`

Lié :

  * Approbations d’exécution : [Approbations d’exécution](</fr/tools/exec-approvals>)
  * Nodes : [Nodes](</fr/nodes>)


## `openclaw exec-policy`

`openclaw exec-policy` est la commande pratique locale pour garder en phase, en une seule étape, la configuration demandée `tools.exec.*` et le fichier local d’approbations de l’hôte.

Utilisez-la lorsque vous voulez :

  * inspecter la politique locale demandée, le fichier d’approbations de l’hôte et la fusion effective
  * appliquer un préréglage local tel que YOLO ou deny-all
  * synchroniser `tools.exec.*` local et `~/.openclaw/exec-approvals.json` local


Exemples :

bashCopy code
[code]
    openclaw exec-policy showopenclaw exec-policy show --json openclaw exec-policy preset yoloopenclaw exec-policy preset cautious --json openclaw exec-policy set --host gateway --security full --ask off --ask-fallback full
[/code]

Modes de sortie :

  * sans `--json` : affiche la vue tabulaire lisible par l’humain
  * avec `--json` : affiche une sortie structurée lisible par machine


Périmètre actuel :

  * `exec-policy` est **local uniquement**
  * il met à jour ensemble le fichier de configuration local et le fichier d’approbations local
  * il ne pousse **pas** la politique vers l’hôte gateway ou un hôte Node
  * `--host node` est rejeté dans cette commande, car les approbations d’exécution des Nodes sont récupérées depuis le Node à l’exécution et doivent être gérées à la place via des commandes d’approbation ciblant le Node
  * `openclaw exec-policy show` marque les périmètres `host=node` comme gérés par le Node à l’exécution au lieu de dériver une politique effective depuis le fichier d’approbations local


Si vous devez modifier directement des approbations d’hôtes distants, continuez à utiliser `openclaw approvals set --gateway` ou `openclaw approvals set --node <id|name|ip>`.

## Commandes courantes

bashCopy code
[code]
    openclaw approvals getopenclaw approvals get --node <id|name|ip>openclaw approvals get --gateway
[/code]

`openclaw approvals get` affiche maintenant la politique d’exécution effective pour les cibles locales, gateway et Node :

  * politique demandée `tools.exec`
  * politique du fichier d’approbations de l’hôte
  * résultat effectif après application des règles de priorité


La priorité est intentionnelle :

  * le fichier d’approbations de l’hôte est la source de vérité applicable
  * la politique demandée `tools.exec` peut restreindre ou élargir l’intention, mais le résultat effectif est toujours dérivé des règles de l’hôte
  * `--node` combine le fichier d’approbations de l’hôte Node avec la politique `tools.exec` du gateway, car les deux s’appliquent toujours à l’exécution
  * si la configuration du gateway n’est pas disponible, la CLI se rabat sur l’instantané des approbations du Node et indique que la politique finale d’exécution n’a pas pu être calculée


## Remplacer les approbations depuis un fichier

bashCopy code
[code]
    openclaw approvals set --file ./exec-approvals.jsonopenclaw approvals set --stdin <<'EOF'{ version: 1, defaults: { security: "full", ask: "off" } }EOFopenclaw approvals set --node <id|name|ip> --file ./exec-approvals.jsonopenclaw approvals set --gateway --file ./exec-approvals.json
[/code]

`set` accepte JSON5, pas seulement du JSON strict. Utilisez soit `--file`, soit `--stdin`, pas les deux.

## Exemple « ne jamais demander » / YOLO

Pour un hôte qui ne doit jamais s’arrêter sur des approbations d’exécution, définissez les valeurs par défaut des approbations de l’hôte sur `full` \+ `off` :

bashCopy code
[code]
    openclaw approvals set --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

Variante Node :

bashCopy code
[code]
    openclaw approvals set --node <id|name|ip> --stdin <<'EOF'{  version: 1,  defaults: {    security: "full",    ask: "off",    askFallback: "full"  }}EOF
[/code]

Cela modifie uniquement le **fichier d’approbations de l’hôte**. Pour garder la politique OpenClaw demandée alignée, définissez aussi :

bashCopy code
[code]
    openclaw config set tools.exec.host gatewayopenclaw config set tools.exec.security fullopenclaw config set tools.exec.ask off
[/code]

Pourquoi `tools.exec.host=gateway` dans cet exemple :

  * `host=auto` signifie toujours « sandbox si disponible, sinon gateway ».
  * YOLO concerne les approbations, pas le routage.
  * Si vous voulez une exécution sur l’hôte même lorsqu’un sandbox est configuré, rendez le choix de l’hôte explicite avec `gateway` ou `/exec host=gateway`.


Cela correspond au comportement actuel YOLO par défaut de l’hôte. Renforcez-le si vous voulez des approbations.

Raccourci local :

bashCopy code
[code]
    openclaw exec-policy preset yolo
[/code]

Ce raccourci local met à jour à la fois la configuration locale demandée `tools.exec.*` et les valeurs par défaut des approbations locales. Il est équivalent en intention à la configuration manuelle en deux étapes ci-dessus, mais uniquement pour la machine locale.

## Assistants de liste blanche

bashCopy code
[code]
    openclaw approvals allowlist add "~/Projects/**/bin/rg"openclaw approvals allowlist add --agent main --node <id|name|ip> "/usr/bin/uptime"openclaw approvals allowlist add --agent "*" "/usr/bin/uname" openclaw approvals allowlist remove "~/Projects/**/bin/rg"
[/code]

## Options courantes

`get`, `set` et `allowlist add|remove` prennent tous en charge :

  * `--node <id|name|ip>`
  * `--gateway`
  * options RPC Node partagées : `--url`, `--token`, `--timeout`, `--json`


Remarques de ciblage :

  * sans indicateur de cible, cela vise le fichier d’approbations local sur disque
  * `--gateway` vise le fichier d’approbations de l’hôte gateway
  * `--node` vise un hôte Node après résolution de l’id, du nom, de l’IP ou d’un préfixe d’id


`allowlist add|remove` prend aussi en charge :

  * `--agent <id>` (par défaut `*`)


## Remarques

  * `--node` utilise le même résolveur que `openclaw nodes` (id, nom, ip ou préfixe d’id).
  * `--agent` vaut par défaut `"*"`, ce qui s’applique à tous les agents.
  * L’hôte Node doit annoncer `system.execApprovals.get/set` (application macOS ou hôte Node headless).
  * Les fichiers d’approbations sont stockés par hôte dans `~/.openclaw/exec-approvals.json`.


## Lié

  * [Référence CLI](</fr/cli>)
  * [Approbations d’exécution](</fr/tools/exec-approvals>)


Was this useful?YesNo