---
title: Agents ACP — configuration
source_url: https://docs.openclaw.ai/fr/tools/acp-agents-setup
scraped_at: 2026-05-25
---

Pour la vue d’ensemble, le runbook opérateur et les concepts, consultez [agents ACP](</fr/tools/acp-agents>).

Les sections ci-dessous couvrent la configuration du harness acpx, la configuration des plugins pour les ponts MCP et la configuration des permissions.

Utilisez cette page uniquement lorsque vous configurez la route ACP/acpx. Pour la configuration du runtime natif Codex app-server, utilisez [harness Codex](</fr/plugins/codex-harness>). Pour les clés d’API OpenAI ou la configuration du fournisseur de modèles OAuth Codex, utilisez [OpenAI](</fr/providers/openai>).

Codex dispose de deux routes OpenClaw :

Route | Config/commande | Page de configuration  
---|---|---  
Serveur d’application Codex natif | `/codex ...`, références d’agent `openai/gpt-*` | [harness Codex](</fr/plugins/codex-harness>)  
Adaptateur ACP Codex explicite | `/acp spawn codex`, `runtime: "acp", agentId: "codex"` | Cette page  
  
Préférez la route native, sauf si vous avez explicitement besoin du comportement ACP/acpx.

## Prise en charge du harness acpx (actuelle)

Alias de harness intégrés acpx actuels :

  * `claude`
  * `codex`
  * `copilot`
  * `cursor` (CLI Cursor : `cursor-agent acp`)
  * `droid`
  * `gemini`
  * `iflow`
  * `kilocode`
  * `kimi`
  * `kiro`
  * `openclaw`
  * `opencode`
  * `pi`
  * `qwen`


Quand OpenClaw utilise le backend acpx, préférez ces valeurs pour `agentId`, sauf si votre configuration acpx définit des alias d’agents personnalisés. Si votre installation locale de Cursor expose encore ACP sous la forme `agent acp`, remplacez la commande de l’agent `cursor` dans votre configuration acpx au lieu de modifier la valeur par défaut intégrée.

L’utilisation directe de la CLI acpx peut aussi cibler des adaptateurs arbitraires via `--agent <command>`, mais cette échappatoire brute est une fonctionnalité de la CLI acpx (pas le chemin `agentId` normal d’OpenClaw).

Le contrôle du modèle dépend des capacités de l’adaptateur. Les références de modèle Codex ACP sont normalisées par OpenClaw avant le démarrage. Les autres harnesses nécessitent ACP `models` plus la prise en charge de `session/set_model` ; si un harness n’expose ni cette capacité ACP ni son propre indicateur de modèle au démarrage, OpenClaw/acpx ne peut pas imposer une sélection de modèle.

## Configuration requise

Base ACP principale :

json5Copy code
[code]
    {  acp: {    enabled: true,    // Optional. Default is true; set false to pause ACP dispatch while keeping /acp controls.    dispatch: { enabled: true },    backend: "acpx",    defaultAgent: "codex",    allowedAgents: [      "claude",      "codex",      "copilot",      "cursor",      "droid",      "gemini",      "iflow",      "kilocode",      "kimi",      "kiro",      "openclaw",      "opencode",      "pi",      "qwen",    ],    maxConcurrentSessions: 8,    stream: {      coalesceIdleMs: 300,      maxChunkChars: 1200,    },    runtime: {      ttlMinutes: 120,    },  },}
[/code]

La configuration de liaison de fils est propre à l’adaptateur de canal. Exemple pour Discord :

json5Copy code
[code]
    {  session: {    threadBindings: {      enabled: true,      idleHours: 24,      maxAgeHours: 0,    },  },  channels: {    discord: {      threadBindings: {        enabled: true,        spawnSessions: true,      },    },  },}
[/code]

Si la génération ACP liée à un fil ne fonctionne pas, vérifiez d’abord le feature flag de l’adaptateur :

  * Discord : `channels.discord.threadBindings.spawnSessions=true`


Les liaisons de conversation courante ne nécessitent pas la création d’un fil enfant. Elles nécessitent un contexte de conversation actif et un adaptateur de canal qui expose les liaisons de conversation ACP.

Consultez la [référence de configuration](</fr/gateway/configuration-reference>).

## Configuration du Plugin pour le backend acpx

Les installations empaquetées utilisent le plugin de runtime ACP officiel `@openclaw/acpx`. Installez-le et activez-le avant d’utiliser des sessions de harness ACP :

bashCopy code
[code]
    openclaw plugins install @openclaw/acpxopenclaw config set plugins.entries.acpx.enabled true
[/code]

Les checkouts source peuvent aussi utiliser le plugin d’espace de travail local après `pnpm install`.

Commencez par :

textCopy code
[code]
    /acp doctor
[/code]

Si vous avez désactivé `acpx`, l’avez refusé via `plugins.allow` / `plugins.deny`, ou voulez revenir au plugin empaqueté, utilisez le chemin de paquet explicite :

bashCopy code
[code]
    openclaw plugins install @openclaw/acpxopenclaw config set plugins.entries.acpx.enabled true
[/code]

Installation de l’espace de travail local pendant le développement :

bashCopy code
[code]
    openclaw plugins install ./path/to/local/acpx-plugin
[/code]

Vérifiez ensuite l’état du backend :

textCopy code
[code]
    /acp doctor
[/code]

### Configuration de la commande et de la version acpx

Par défaut, le plugin `acpx` sonde le backend ACP embarqué pendant le démarrage du Gateway et attend cette sonde avant le signal `ready` du Gateway. Définissez `OPENCLAW_ACPX_RUNTIME_STARTUP_PROBE=0` pour ignorer la sonde de démarrage et enregistrer le backend paresseusement à la place. Exécutez `/acp doctor` pour une sonde explicite à la demande.

Remplacez la commande ou la version dans la configuration du plugin :

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "acpx": {        "enabled": true,        "config": {          "command": "../acpx/dist/cli.js",          "expectedVersion": "any"        }      }    }  }}
[/code]

  * `command` accepte un chemin absolu, un chemin relatif (résolu depuis l’espace de travail OpenClaw) ou un nom de commande.
  * `expectedVersion: "any"` désactive la correspondance stricte de version.
  * Les chemins `command` personnalisés désactivent l’installation automatique locale au plugin.


Remplacez une commande d’agent ACP individuelle par des arguments structurés lorsqu’un chemin ou une valeur d’indicateur doit rester un seul jeton argv :

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "acpx": {        "enabled": true,        "config": {          "agents": {            "claude": {              "command": "node",              "args": ["/path/to/custom adapter.mjs", "--verbose"]            }          }        }      }    }  }}
[/code]

  * `agents.<id>.command` est l’exécutable ou la chaîne de commande existante pour cet agent ACP.
  * `agents.<id>.args` est facultatif. Chaque élément de tableau est échappé pour le shell avant qu’OpenClaw le transmette au registre de chaînes de commande acpx courant.


Consultez [Plugins](</fr/tools/plugin>).

### Installation automatique des dépendances

Quand vous installez OpenClaw globalement avec `npm install -g openclaw`, les dépendances du runtime acpx (binaires propres à la plateforme) sont installées automatiquement via un hook postinstall. Si l’installation automatique échoue, le Gateway démarre quand même normalement et signale la dépendance manquante via `openclaw acp doctor`.

### Pont MCP des outils de plugin

Par défaut, les sessions ACPX n’exposent **pas** les outils enregistrés par les plugins OpenClaw au harness ACP.

Si vous voulez que des agents ACP comme Codex ou Claude Code appellent des outils de plugins OpenClaw installés, comme le rappel/stockage de mémoire, activez le pont dédié :

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.pluginToolsMcpBridge true
[/code]

Ce que cela fait :

  * Injecte un serveur MCP intégré nommé `openclaw-plugin-tools` dans l’amorçage des sessions ACPX.
  * Expose les outils de plugins déjà enregistrés par les plugins OpenClaw installés et activés.
  * Maintient la fonctionnalité explicite et désactivée par défaut.


Notes de sécurité et de confiance :

  * Cela étend la surface d’outils du harness ACP.
  * Les agents ACP n’ont accès qu’aux outils de plugins déjà actifs dans le Gateway.
  * Traitez cela comme la même frontière de confiance que le fait de laisser ces plugins s’exécuter dans OpenClaw lui-même.
  * Passez en revue les plugins installés avant de l’activer.


Les `mcpServers` personnalisés continuent de fonctionner comme auparavant. Le pont intégré des outils de plugins est une commodité opt-in supplémentaire, pas un remplacement de la configuration générique des serveurs MCP.

### Pont MCP des outils OpenClaw

Par défaut, les sessions ACPX n’exposent pas non plus les outils OpenClaw intégrés via MCP. Activez le pont séparé des outils du noyau lorsqu’un agent ACP a besoin d’outils intégrés sélectionnés comme `cron` :

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.openClawToolsMcpBridge true
[/code]

Ce que cela fait :

  * Injecte un serveur MCP intégré nommé `openclaw-tools` dans l’amorçage des sessions ACPX.
  * Expose des outils OpenClaw intégrés sélectionnés. Le serveur initial expose `cron`.
  * Maintient l’exposition des outils du noyau explicite et désactivée par défaut.


### Configuration du délai d’expiration du runtime

Le plugin `acpx` définit par défaut un délai d’expiration de 120 secondes pour les tours du runtime embarqué. Cela donne aux harnesses plus lents comme Gemini CLI assez de temps pour terminer le démarrage et l’initialisation ACP. Remplacez-le si votre hôte nécessite une limite de runtime différente :

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.timeoutSeconds 180
[/code]

Redémarrez le Gateway après avoir modifié cette valeur.

### Configuration de l’agent de sonde de santé

Quand `/acp doctor` ou la sonde de démarrage vérifie le backend, le plugin `acpx` fourni sonde un agent de harness. Si `acp.allowedAgents` est défini, il utilise par défaut le premier agent autorisé ; sinon, il utilise `codex` par défaut. Si votre déploiement nécessite un autre agent ACP pour les contrôles de santé, définissez explicitement l’agent de sonde :

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.probeAgent claude
[/code]

Redémarrez le Gateway après avoir modifié cette valeur.

## Configuration des permissions

Les sessions ACP s’exécutent de manière non interactive : il n’y a pas de TTY pour approuver ou refuser les invites de permission d’écriture de fichiers et d’exécution shell. Le plugin acpx fournit deux clés de configuration qui contrôlent la façon dont les permissions sont gérées :

Ces permissions de harness ACPX sont séparées des approbations d’exécution OpenClaw et distinctes des indicateurs de contournement de fournisseurs de backend CLI comme `--permission-mode bypassPermissions` de Claude CLI. ACPX `approve-all` est l’interrupteur de dernier recours au niveau du harness pour les sessions ACP.

### `permissionMode`

Contrôle les opérations que l’agent de harness peut effectuer sans invite.

Valeur | Comportement  
---|---  
`approve-all` | Approuve automatiquement toutes les écritures de fichiers et commandes shell.  
`approve-reads` | Approuve automatiquement les lectures uniquement ; les écritures et l’exécution nécessitent des invites.  
`deny-all` | Refuse toutes les invites de permission.  
  
### `nonInteractivePermissions`

Contrôle ce qui se passe lorsqu’une invite de permission serait affichée, mais qu’aucun TTY interactif n’est disponible (ce qui est toujours le cas pour les sessions ACP).

Valeur | Comportement  
---|---  
`fail` | Abandonne la session avec `AcpRuntimeError`. **(par défaut)**  
`deny` | Refuse silencieusement la permission et continue (dégradation progressive).  
  
### Configuration

Définissez via la configuration du plugin :

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions fail
[/code]

Redémarrez le Gateway après avoir modifié ces valeurs.

## Articles connexes

  * [agents ACP](</fr/tools/acp-agents>) — vue d’ensemble, runbook opérateur, concepts
  * [Sous-agents](</fr/tools/subagents>)
  * [Routage multi-agent](</fr/concepts/multi-agent>)


Was this useful?YesNo