---
title: Mode élevé
source_url: https://docs.openclaw.ai/fr/tools/elevated
scraped_at: 2026-05-25
---

Lorsqu’un agent s’exécute dans un bac à sable, ses commandes `exec` sont confinées à l’environnement du bac à sable. Le **mode élevé** permet à l’agent d’en sortir et d’exécuter des commandes hors du bac à sable, avec des étapes d’approbation configurables.

## Directives

Contrôlez le mode élevé par session avec des commandes slash :

Directive | Ce que cela fait  
---|---  
`/elevated on` | Exécute hors du bac à sable sur le chemin hôte configuré, garde les approbations  
`/elevated ask` | Identique à `on` (alias)  
`/elevated full` | Exécute hors du bac à sable sur le chemin hôte configuré et ignore les approbations  
`/elevated off` | Revient à une exécution confinée au bac à sable  
  
Également disponible sous la forme `/elev on|off|ask|full`.

Envoyez `/elevated` sans argument pour voir le niveau actuel.

## Fonctionnement

* ### Check availability

Le mode élevé doit être activé dans la configuration et l’expéditeur doit figurer dans la liste d’autorisation :

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Set the level

Envoyez un message contenant uniquement la directive pour définir la valeur par défaut de la session :

CodeCopy code
[code]
    /elevated full
[/code]

Ou utilisez-la en ligne (s’applique uniquement à ce message) :

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### Commands run outside the sandbox

Lorsque le mode élevé est actif, les appels `exec` quittent le bac à sable. L’hôte effectif est `gateway` par défaut, ou `node` lorsque la cible exec configurée/de session est `node`. En mode `full`, les approbations exec sont ignorées. En mode `on`/`ask`, les règles d’approbation configurées s’appliquent toujours.

## Ordre de résolution

  1. **Directive en ligne** dans le message (s’applique uniquement à ce message)
  2. **Remplacement de session** (défini en envoyant un message contenant uniquement la directive)
  3. **Valeur par défaut globale** (`agents.defaults.elevatedDefault` dans la configuration)


## Disponibilité et listes d’autorisation

  * **Garde globale** : `tools.elevated.enabled` (doit valoir `true`)
  * **Liste d’autorisation de l’expéditeur** : `tools.elevated.allowFrom` avec des listes par canal
  * **Garde par agent** : `agents.list[].tools.elevated.enabled` (ne peut que restreindre davantage)
  * **Liste d’autorisation par agent** : `agents.list[].tools.elevated.allowFrom` (l’expéditeur doit correspondre à la fois à la globale et à celle de l’agent)
  * **Solution de repli Discord** : si `tools.elevated.allowFrom.discord` est omis, `channels.discord.allowFrom` est utilisé comme solution de repli
  * **Toutes les gardes doivent réussir** ; sinon le mode élevé est considéré comme indisponible


Formats des entrées de liste d’autorisation :

Préfixe | Correspond à  
---|---  
(aucun) | ID d’expéditeur, E.164 ou champ From  
`name:` | Nom d’affichage de l’expéditeur  
`username:` | Nom d’utilisateur de l’expéditeur  
`tag:` | Tag de l’expéditeur  
`id:`, `from:`, `e164:` | Ciblage d’identité explicite  
  
## Ce que le mode élevé ne contrôle pas

  * **Politique d’outil** : si `exec` est refusé par la politique d’outil, le mode élevé ne peut pas la contourner.
  * **Politique de sélection de l’hôte** : le mode élevé ne transforme pas `auto` en remplacement libre entre hôtes. Il utilise les règles de cible exec configurée/de session, en choisissant `node` uniquement lorsque la cible est déjà `node`.
  * **Distinct de`/exec`** : la directive `/exec` ajuste les valeurs par défaut exec par session pour les expéditeurs autorisés et ne nécessite pas le mode élevé.


## Connexe

[**Exec tool** Exécution de commandes shell depuis l’agent. ](</fr/tools/exec>) [**Exec approvals** Système d’approbation et de liste d’autorisation pour `exec`. ](</fr/tools/exec-approvals>) [**Sandboxing** Configuration du bac à sable au niveau Gateway. ](</fr/gateway/sandboxing>) [**Sandbox vs Tool Policy vs Elevated** Comment les trois gardes se composent pendant un appel d’outil. ](</fr/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo