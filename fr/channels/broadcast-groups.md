---
title: Groupes de diffusion
source_url: https://docs.openclaw.ai/fr/channels/broadcast-groups
scraped_at: 2026-05-25
---

## Vue d’ensemble

Les groupes de diffusion permettent à plusieurs agents de traiter le même message et d’y répondre simultanément. Cela vous permet de créer des équipes d’agents spécialisées qui travaillent ensemble dans un seul groupe ou message direct WhatsApp, le tout avec un seul numéro de téléphone.

Périmètre actuel : **WhatsApp uniquement** (canal web).

Les groupes de diffusion sont évalués après les listes d’autorisation des canaux et les règles d’activation des groupes. Dans les groupes WhatsApp, cela signifie que les diffusions ont lieu lorsque OpenClaw répondrait normalement (par exemple : lors d’une mention, selon les paramètres de votre groupe).

## Cas d’utilisation

1\. Équipes d’agents spécialisées

Déployez plusieurs agents avec des responsabilités atomiques et ciblées :

CodeCopy code
[code]
    Group: "Development Team"Agents:  - CodeReviewer (reviews code snippets)  - DocumentationBot (generates docs)  - SecurityAuditor (checks for vulnerabilities)  - TestGenerator (suggests test cases)
[/code]

Chaque agent traite le même message et fournit son point de vue spécialisé.

2\. Prise en charge multilingue CodeCopy code
[code]
    Group: "International Support"Agents:  - Agent_EN (responds in English)  - Agent_DE (responds in German)  - Agent_ES (responds in Spanish)
[/code]

3\. Workflows d’assurance qualité CodeCopy code
[code]
    Group: "Customer Support"Agents:  - SupportAgent (provides answer)  - QAAgent (reviews quality, only responds if issues found)
[/code]

4\. Automatisation des tâches CodeCopy code
[code]
    Group: "Project Management"Agents:  - TaskTracker (updates task database)  - TimeLogger (logs time spent)  - ReportGenerator (creates summaries)
[/code]

## Configuration

### Configuration de base

Ajoutez une section `broadcast` de premier niveau (à côté de `bindings`). Les clés sont des identifiants de pairs WhatsApp :

  * discussions de groupe : JID de groupe (par exemple `120363403215116621@g.us`)
  * messages directs : numéro de téléphone E.164 (par exemple `+15551234567`)

jsonCopy code
[code]
    {  "broadcast": {    "120363403215116621@g.us": ["alfred", "baerbel", "assistant3"]  }}
[/code]

**Résultat :** Lorsque OpenClaw répondrait dans cette discussion, il exécutera les trois agents.

### Stratégie de traitement

Contrôlez la façon dont les agents traitent les messages :

### parallel (par défaut)

Tous les agents traitent simultanément :

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### sequential

Les agents traitent dans l’ordre (chacun attend que le précédent termine) :

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### Exemple complet

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "code-reviewer",        "name": "Code Reviewer",        "workspace": "/path/to/code-reviewer",        "sandbox": { "mode": "all" }      },      {        "id": "security-auditor",        "name": "Security Auditor",        "workspace": "/path/to/security-auditor",        "sandbox": { "mode": "all" }      },      {        "id": "docs-generator",        "name": "Documentation Generator",        "workspace": "/path/to/docs-generator",        "sandbox": { "mode": "all" }      }    ]  },  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["code-reviewer", "security-auditor", "docs-generator"],    "120363424282127706@g.us": ["support-en", "support-de"],    "+15555550123": ["assistant", "logger"]  }}
[/code]

## Fonctionnement

### Flux des messages

* ### Un message entrant arrive

Un message de groupe ou message direct WhatsApp arrive.

* ### Vérification de diffusion

Le système vérifie si l’ID du pair figure dans `broadcast`.

* ### S’il figure dans la liste de diffusion

  * Tous les agents listés traitent le message.
  * Chaque agent possède sa propre clé de session et son contexte isolé.
  * Les agents traitent en parallèle (par défaut) ou séquentiellement.


* ### S’il ne figure pas dans la liste de diffusion

Le routage normal s’applique (première liaison correspondante).

### Isolation des sessions

Chaque agent d’un groupe de diffusion conserve des éléments complètement séparés :

  * **Clés de session** (`agent:alfred:whatsapp:group:120363...` vs `agent:baerbel:whatsapp:group:120363...`)
  * **Historique de conversation** (l’agent ne voit pas les messages des autres agents)
  * **Espace de travail** (bacs à sable séparés si configurés)
  * **Accès aux outils** (listes d’autorisation/refus différentes)
  * **Mémoire/contexte** ([IDENTITY.md](<http://IDENTITY.md>), [SOUL.md](<http://SOUL.md>), etc. séparés)
  * Le **tampon de contexte de groupe** (messages de groupe récents utilisés comme contexte) est partagé par pair, ce qui permet à tous les agents de diffusion de voir le même contexte lorsqu’ils sont déclenchés


Cela permet à chaque agent d’avoir :

  * Des personnalités différentes
  * Des accès aux outils différents (par exemple, lecture seule vs lecture-écriture)
  * Des modèles différents (par exemple, opus vs sonnet)
  * Des Skills différents installés


### Exemple : sessions isolées

Dans le groupe `120363403215116621@g.us` avec les agents `["alfred", "baerbel"]` :

### Contexte d’Alfred

CodeCopy code
[code]
    Session: agent:alfred:whatsapp:group:120363403215116621@g.usHistory: [user message, alfred's previous responses]Workspace: /Users/user/openclaw-alfred/Tools: read, write, exec
[/code]

### Contexte de Bärbel

CodeCopy code
[code]
    Session: agent:baerbel:whatsapp:group:120363403215116621@g.usHistory: [user message, baerbel's previous responses]Workspace: /Users/user/openclaw-baerbel/Tools: read only
[/code]

## Bonnes pratiques

1\. Garder les agents ciblés

Concevez chaque agent avec une responsabilité unique et claire :

jsonCopy code
[code]
    {  "broadcast": {    "DEV_GROUP": ["formatter", "linter", "tester"]  }}
[/code]

✅ **Bon :** Chaque agent a une seule tâche. ❌ **Mauvais :** Un agent générique "dev-helper".

2\. Utiliser des noms descriptifs

Indiquez clairement ce que fait chaque agent :

jsonCopy code
[code]
    {  "agents": {    "security-scanner": { "name": "Security Scanner" },    "code-formatter": { "name": "Code Formatter" },    "test-generator": { "name": "Test Generator" }  }}
[/code]

3\. Configurer des accès aux outils différents

Donnez aux agents uniquement les outils dont ils ont besoin :

jsonCopy code
[code]
    {  "agents": {    "reviewer": {      "tools": { "allow": ["read", "exec"] }    },    "fixer": {      "tools": { "allow": ["read", "write", "edit", "exec"] }    }  }}
[/code]

`reviewer` est en lecture seule. `fixer` peut lire et écrire.

4\. Surveiller les performances

Avec de nombreux agents, envisagez :

  * D’utiliser `"strategy": "parallel"` (par défaut) pour la vitesse
  * De limiter les groupes de diffusion à 5 à 10 agents
  * D’utiliser des modèles plus rapides pour les agents plus simples

5\. Gérer les échecs avec élégance

Les agents échouent indépendamment. L’erreur d’un agent ne bloque pas les autres :

CodeCopy code
[code]
    Message → [Agent A ✓, Agent B ✗ error, Agent C ✓]Result: Agent A and C respond, Agent B logs error
[/code]

## Compatibilité

### Fournisseurs

Les groupes de diffusion fonctionnent actuellement avec :

  * ✅ WhatsApp (implémenté)
  * 🚧 Telegram (prévu)
  * 🚧 Discord (prévu)
  * 🚧 Slack (prévu)


### Routage

Les groupes de diffusion fonctionnent avec le routage existant :

jsonCopy code
[code]
    {  "bindings": [    {      "match": { "channel": "whatsapp", "peer": { "kind": "group", "id": "GROUP_A" } },      "agentId": "alfred"    }  ],  "broadcast": {    "GROUP_B": ["agent1", "agent2"]  }}
[/code]

  * `GROUP_A` : Seul alfred répond (routage normal).
  * `GROUP_B` : agent1 ET agent2 répondent (diffusion).


## Dépannage

Les agents ne répondent pas

**Vérifiez :**

  1. Les ID d’agents existent dans `agents.list`.
  2. Le format de l’ID du pair est correct (par exemple, `120363403215116621@g.us`).
  3. Les agents ne figurent pas dans des listes de refus.


**Débogage :**

bashCopy code
[code]
    tail -f ~/.openclaw/logs/gateway.log | grep broadcast
[/code]

Un seul agent répond

**Cause :** L’ID du pair peut figurer dans `bindings`, mais pas dans `broadcast`.

**Correction :** Ajoutez-le à la configuration de diffusion ou supprimez-le des liaisons.

Problèmes de performances

En cas de lenteur avec de nombreux agents :

  * Réduisez le nombre d’agents par groupe.
  * Utilisez des modèles plus légers (sonnet au lieu d’opus).
  * Vérifiez le temps de démarrage du bac à sable.


## Exemples

Exemple 1 : équipe de revue de code jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": [      "code-formatter",      "security-scanner",      "test-coverage",      "docs-checker"    ]  },  "agents": {    "list": [      {        "id": "code-formatter",        "workspace": "~/agents/formatter",        "tools": { "allow": ["read", "write"] }      },      {        "id": "security-scanner",        "workspace": "~/agents/security",        "tools": { "allow": ["read", "exec"] }      },      {        "id": "test-coverage",        "workspace": "~/agents/testing",        "tools": { "allow": ["read", "exec"] }      },      { "id": "docs-checker", "workspace": "~/agents/docs", "tools": { "allow": ["read"] } }    ]  }}
[/code]

**L’utilisateur envoie :** Un extrait de code.

**Réponses :**

  * code-formatter : "Fixed indentation and added type hints"
  * security-scanner : "⚠️ SQL injection vulnerability in line 12"
  * test-coverage : "Coverage is 45%, missing tests for error cases"
  * docs-checker : "Missing docstring for function `process_data`"

Exemple 2 : prise en charge multilingue jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "+15555550123": ["detect-language", "translator-en", "translator-de"]  },  "agents": {    "list": [      { "id": "detect-language", "workspace": "~/agents/lang-detect" },      { "id": "translator-en", "workspace": "~/agents/translate-en" },      { "id": "translator-de", "workspace": "~/agents/translate-de" }    ]  }}
[/code]

## Référence API

### Schéma de configuration

typescriptCopy code
[code]
    interface OpenClawConfig {  broadcast?: {    strategy?: "parallel" | "sequential";    [peerId: string]: string[];  };}
[/code]

### Champs

Comment traiter les agents. `parallel` exécute tous les agents simultanément ; `sequential` les exécute dans l’ordre du tableau.

JID de groupe WhatsApp, numéro E.164 ou autre ID de pair. La valeur est le tableau d’ID d’agents qui doivent traiter les messages.

## Limitations

  1. **Nombre maximal d’agents :** Aucune limite stricte, mais 10 agents ou plus peuvent être lents.
  2. **Contexte partagé :** Les agents ne voient pas les réponses des autres agents (par conception).
  3. **Ordre des messages :** Les réponses parallèles peuvent arriver dans n’importe quel ordre.
  4. **Limites de débit :** Tous les agents comptent dans les limites de débit de WhatsApp.


## Améliorations futures

Fonctionnalités prévues :

  * [ ] Mode de contexte partagé (les agents voient les réponses des autres)
  * [ ] Coordination des agents (les agents peuvent s’envoyer des signaux)
  * [ ] Sélection dynamique des agents (choisir les agents selon le contenu du message)
  * [ ] Priorités des agents (certains agents répondent avant les autres)


## Articles associés

  * [Routage des canaux](</fr/channels/channel-routing>)
  * [Groupes](</fr/channels/groups>)
  * [Outils de bac à sable multi-agent](</fr/tools/multi-agent-sandbox-tools>)
  * [Appairage](</fr/channels/pairing>)
  * [Gestion des sessions](</fr/concepts/session>)


Was this useful?YesNo