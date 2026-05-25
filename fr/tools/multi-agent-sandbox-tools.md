---
title: Bac à sable et outils multi-agents
source_url: https://docs.openclaw.ai/fr/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Chaque agent dans une configuration multi-agent peut remplacer la politique globale de sandbox et d’outils. Cette page couvre la configuration par agent, les règles de précédence et des exemples.

[**Isolation en sandbox** Backends et modes — référence complète du sandbox. ](</fr/gateway/sandboxing>) [**Sandbox vs politique d’outils vs mode élevé** Déboguer « pourquoi est-ce bloqué ? » ](</fr/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Mode élevé** Exécution élevée pour les expéditeurs approuvés. ](</fr/tools/elevated>)

* * *

## Exemples de configuration

Exemple 1 : agent personnel + agent familial restreint jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Résultat :**

  * agent `main` : s’exécute sur l’hôte, accès complet aux outils.
  * agent `family` : s’exécute dans Docker (un conteneur par agent), uniquement `read` et les envois de messages dans la conversation actuelle.

Exemple 2 : agent de travail avec sandbox partagé jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Exemple 2b : profil de codage global + agent de messagerie uniquement jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Résultat :**

  * les agents par défaut obtiennent les outils de codage.
  * l’agent `support` est limité à la messagerie (+ outil Slack).

Exemple 3 : différents modes de sandbox par agent jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Précédence de la configuration

Lorsque des configurations globales (`agents.defaults.*`) et propres à l’agent (`agents.list[].*`) existent toutes deux :

### Configuration du sandbox

Les paramètres propres à l’agent remplacent les paramètres globaux :

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Restrictions d’outils

L’ordre de filtrage est le suivant :

* ### Profil d’outils

`tools.profile` ou `agents.list[].tools.profile`.

* ### Profil d’outils du fournisseur

`tools.byProvider[provider].profile` ou `agents.list[].tools.byProvider[provider].profile`.

* ### Politique globale d’outils

`tools.allow` / `tools.deny`.

* ### Politique d’outils du fournisseur

`tools.byProvider[provider].allow/deny`.

* ### Politique d’outils propre à l’agent

`agents.list[].tools.allow/deny`.

* ### Politique de fournisseur de l’agent

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Politique d’outils du sandbox

`tools.sandbox.tools` ou `agents.list[].tools.sandbox.tools`.

* ### Politique d’outils des sous-agents

`tools.subagents.tools`, le cas échéant.

Règles de précédence

  * Chaque niveau peut restreindre davantage les outils, mais ne peut pas réautoriser des outils refusés par des niveaux précédents.
  * Si `agents.list[].tools.sandbox.tools` est défini, il remplace `tools.sandbox.tools` pour cet agent.
  * Si `agents.list[].tools.profile` est défini, il remplace `tools.profile` pour cet agent.
  * Les clés d’outils de fournisseur acceptent soit `provider` (par exemple `google-antigravity`), soit `provider/model` (par exemple `openai/gpt-5.4`).

Comportement d’une liste d’autorisation vide

Si une liste d’autorisation explicite dans cette chaîne laisse l’exécution sans aucun outil appelable, OpenClaw s’arrête avant de soumettre l’invite au modèle. C’est intentionnel : un agent configuré avec un outil manquant comme `agents.list[].tools.allow: ["query_db"]` doit échouer clairement jusqu’à ce que le Plugin qui enregistre `query_db` soit activé, au lieu de continuer comme agent texte uniquement.

Les politiques d’outils prennent en charge les raccourcis `group:*`, qui s’étendent à plusieurs outils. Consultez [Groupes d’outils](</fr/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>) pour la liste complète.

Les remplacements élevés par agent (`agents.list[].tools.elevated`) peuvent restreindre davantage l’exécution élevée pour des agents spécifiques. Consultez [Mode élevé](</fr/tools/elevated>) pour plus de détails.

* * *

## Migration depuis un agent unique

### Before (single agent)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### After (multi-agent)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## Exemples de restriction des outils

### Read-only agent

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Shell execution with filesystem tools disabled

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Communication-only

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

Dans ce profil, `sessions_history` renvoie toujours une vue de rappel bornée et assainie plutôt qu’un vidage brut de la transcription. Le rappel de l’assistant supprime les balises de raisonnement, l’échafaudage `<relevant-memories>`, les charges utiles XML d’appels d’outils en texte brut (y compris `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>` et les blocs d’appels d’outils tronqués), l’échafaudage d’appels d’outils déclassé, les jetons de contrôle du modèle ASCII/pleine largeur divulgués, ainsi que le XML d’appels d’outils MiniMax mal formé avant la caviardisation/troncature.

* * *

## Piège courant : "non-main"

* * *

## Tests

Après avoir configuré le sandbox et les outils multi-agents :

* ### Check agent resolution

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Verify sandbox containers

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Test tool restrictions

  * Envoyez un message nécessitant des outils restreints.
  * Vérifiez que l’agent ne peut pas utiliser les outils refusés.


* ### Monitor logs

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## Dépannage

Agent not sandboxed despite `mode: 'all'`

  * Vérifiez s’il existe un `agents.defaults.sandbox.mode` global qui le remplace.
  * La configuration propre à l’agent est prioritaire ; définissez donc `agents.list[].sandbox.mode: "all"`.

Tools still available despite deny list

  * Vérifiez l’ordre de filtrage des outils : global → agent → sandbox → sous-agent.
  * Chaque niveau ne peut que restreindre davantage, pas réaccorder.
  * Vérifiez avec les logs : `[tools] filtering tools for agent:${agentId}`.

Container not isolated per agent

  * Définissez `scope: "agent"` dans la configuration de sandbox propre à l’agent.
  * La valeur par défaut est `"session"`, ce qui crée un conteneur par session.


* * *

## Articles connexes

  * [Mode élevé](</fr/tools/elevated>)
  * [Routage multi-agent](</fr/concepts/multi-agent>)
  * [Configuration du bac à sable](</fr/gateway/config-agents#agentsdefaultssandbox>)
  * [Bac à sable vs politique des outils vs mode élevé](</fr/gateway/sandbox-vs-tool-policy-vs-elevated>) — débogage de « pourquoi est-ce bloqué ? »
  * [Bac à sable](</fr/gateway/sandboxing>) — référence complète du bac à sable (modes, portées, backends, images)
  * [Gestion des sessions](</fr/concepts/session>)


Was this useful?YesNo