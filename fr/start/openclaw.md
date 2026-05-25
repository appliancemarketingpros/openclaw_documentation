---
title: Configuration de l’assistant personnel
source_url: https://docs.openclaw.ai/fr/start/openclaw
scraped_at: 2026-05-25
---

OpenClaw est une passerelle auto-hébergée qui connecte Discord, Google Chat, iMessage, Matrix, Microsoft Teams, Signal, Slack, Telegram, WhatsApp, Zalo et d’autres services à des agents IA. Ce guide couvre la configuration « assistant personnel » : un numéro WhatsApp dédié qui se comporte comme votre assistant IA toujours actif.

## ⚠️ La sécurité d’abord

Vous placez un agent en position de :

  * exécuter des commandes sur votre machine (selon votre politique d’outils)
  * lire/écrire des fichiers dans votre espace de travail
  * renvoyer des messages via WhatsApp/Telegram/Discord/Mattermost et d’autres canaux intégrés


Commencez de manière prudente :

  * Définissez toujours `channels.whatsapp.allowFrom` (n’exécutez jamais une configuration ouverte à tout Internet sur votre Mac personnel).
  * Utilisez un numéro WhatsApp dédié pour l’assistant.
  * Les Heartbeats utilisent désormais par défaut un intervalle de 30 minutes. Désactivez-les jusqu’à ce que vous fassiez confiance à la configuration en définissant `agents.defaults.heartbeat.every: "0m"`.


## Prérequis

  * OpenClaw installé et initialisé - consultez [Bien démarrer](</fr/start/getting-started>) si ce n’est pas encore fait
  * Un deuxième numéro de téléphone (SIM/eSIM/prépayé) pour l’assistant


## La configuration avec deux téléphones (recommandée)

Vous voulez ceci :
[code] 
    flowchart TB
        A["<b>Your Phone (personal)
    </b>
    Your WhatsApp
    +1-555-YOU"] -- message --> B["<b>Second Phone (assistant)
    </b>
    Assistant WA
    +1-555-ASSIST"]
        B -- linked via QR --> C["<b>Your Mac (openclaw)
    </b>
    AI agent"]
[/code]

Si vous liez votre WhatsApp personnel à OpenClaw, chaque message qui vous est adressé devient une « entrée de l’agent ». C’est rarement ce que vous voulez.

## Démarrage rapide en 5 minutes

  1. Associez WhatsApp Web (affiche un QR ; scannez-le avec le téléphone de l’assistant) :

bashCopy code
[code]
    openclaw channels login
[/code]

  2. Démarrez le Gateway (laissez-le tourner) :

bashCopy code
[code]
    openclaw gateway --port 18789
[/code]

  3. Placez une configuration minimale dans `~/.openclaw/openclaw.json` :

json5Copy code
[code]
    {  gateway: { mode: "local" },  channels: { whatsapp: { allowFrom: ["+15555550123"] } },}
[/code]

Envoyez maintenant un message au numéro de l’assistant depuis votre téléphone autorisé.

Lorsque l’initialisation se termine, OpenClaw ouvre automatiquement le tableau de bord et affiche un lien propre (non tokenisé). Si le tableau de bord demande une authentification, collez le secret partagé configuré dans les paramètres de l’interface de contrôle. L’initialisation utilise un jeton par défaut (`gateway.auth.token`), mais l’authentification par mot de passe fonctionne aussi si vous avez passé `gateway.auth.mode` à `password`. Pour rouvrir plus tard : `openclaw dashboard`.

## Donner un espace de travail à l’agent (AGENTS)

OpenClaw lit les instructions de fonctionnement et la « mémoire » depuis son répertoire d’espace de travail.

Par défaut, OpenClaw utilise `~/.openclaw/workspace` comme espace de travail de l’agent, et le crée automatiquement (avec les fichiers de démarrage `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md`) lors de la configuration ou de la première exécution de l’agent. `BOOTSTRAP.md` n’est créé que lorsque l’espace de travail est entièrement nouveau (il ne doit pas réapparaître après sa suppression). `MEMORY.md` est facultatif (il n’est pas créé automatiquement) ; lorsqu’il est présent, il est chargé pour les sessions normales. Les sessions de sous-agent injectent uniquement `AGENTS.md` et `TOOLS.md`.

bashCopy code
[code]
    openclaw setup
[/code]

Disposition complète de l’espace de travail + guide de sauvegarde : [Espace de travail de l’agent](</fr/concepts/agent-workspace>) Workflow de mémoire : [Mémoire](</fr/concepts/memory>)

Facultatif : choisissez un autre espace de travail avec `agents.defaults.workspace` (prend en charge `~`).

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

Si vous livrez déjà vos propres fichiers d’espace de travail depuis un dépôt, vous pouvez désactiver entièrement la création des fichiers d’amorçage :

json5Copy code
[code]
    {  agents: {    defaults: {      skipBootstrap: true,    },  },}
[/code]

## La configuration qui le transforme en « assistant »

OpenClaw utilise par défaut une bonne configuration d’assistant, mais vous voudrez généralement ajuster :

  * la personnalité/les instructions dans [`SOUL.md`](</fr/concepts/soul>)
  * les paramètres de réflexion par défaut (si souhaité)
  * les Heartbeats (une fois que vous lui faites confiance)


Exemple :

json5Copy code
[code]
    {  logging: { level: "info" },  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      workspace: "~/.openclaw/workspace",      thinkingDefault: "high",      timeoutSeconds: 1800,      // Start with 0; enable later.      heartbeat: { every: "0m" },    },    list: [      {        id: "main",        default: true,        groupChat: {          mentionPatterns: ["@openclaw", "openclaw"],        },      },    ],  },  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: {        "*": { requireMention: true },      },    },  },  session: {    scope: "per-sender",    resetTriggers: ["/new", "/reset"],    reset: {      mode: "daily",      atHour: 4,      idleMinutes: 10080,    },  },}
[/code]

## Sessions et mémoire

  * Fichiers de session : `~/.openclaw/agents/<agentId>/sessions/{{SessionId}}.jsonl`
  * Métadonnées de session (utilisation des jetons, dernière route, etc.) : `~/.openclaw/agents/<agentId>/sessions/sessions.json` (hérité : `~/.openclaw/sessions/sessions.json`)
  * `/new` ou `/reset` démarre une nouvelle session pour cette conversation (configurable via `resetTriggers`). S’il est envoyé seul, OpenClaw confirme la réinitialisation sans invoquer le modèle.
  * `/compact [instructions]` compacte le contexte de session et indique le budget de contexte restant.


## Heartbeats (mode proactif)

Par défaut, OpenClaw exécute un Heartbeat toutes les 30 minutes avec le prompt : `Read HEARTBEAT.md if it exists (workspace context). Follow it strictly. Do not infer or repeat old tasks from prior chats. If nothing needs attention, reply HEARTBEAT_OK.` Définissez `agents.defaults.heartbeat.every: "0m"` pour le désactiver.

  * Si `HEARTBEAT.md` existe mais est effectivement vide (uniquement des lignes vides et des en-têtes Markdown comme `# Heading`), OpenClaw ignore l’exécution du Heartbeat pour économiser des appels API.
  * Si le fichier est absent, le Heartbeat s’exécute quand même et le modèle décide quoi faire.
  * Si l’agent répond avec `HEARTBEAT_OK` (éventuellement avec un court remplissage ; voir `agents.defaults.heartbeat.ackMaxChars`), OpenClaw supprime l’envoi sortant pour ce Heartbeat.
  * Par défaut, la livraison des Heartbeats vers les cibles de type message direct `user:<id>` est autorisée. Définissez `agents.defaults.heartbeat.directPolicy: "block"` pour supprimer la livraison vers des cibles directes tout en gardant les exécutions de Heartbeat actives.
  * Les Heartbeats exécutent des tours d’agent complets - des intervalles plus courts consomment davantage de jetons.

json5Copy code
[code]
    {  agents: {    defaults: {      heartbeat: { every: "30m" },    },  },}
[/code]

## Médias entrants et sortants

Les pièces jointes entrantes (images/audio/documents) peuvent être exposées à votre commande via des modèles :

  * `{{MediaPath}}` (chemin du fichier temporaire local)
  * `{{MediaUrl}}` (pseudo-URL)
  * `{{Transcript}}` (si la transcription audio est activée)


Pièces jointes sortantes depuis l’agent : incluez `MEDIA:<path-or-url>` sur sa propre ligne (sans espaces). Exemple :

CodeCopy code
[code]
    Here's the screenshot.MEDIA:https://example.com/screenshot.png
[/code]

OpenClaw les extrait et les envoie comme médias avec le texte.

Le comportement des chemins locaux suit le même modèle de confiance pour la lecture de fichiers que l’agent :

  * Si `tools.fs.workspaceOnly` vaut `true`, les chemins locaux `MEDIA:` sortants restent limités à la racine temporaire d’OpenClaw, au cache média, aux chemins de l’espace de travail de l’agent et aux fichiers générés par le bac à sable.
  * Si `tools.fs.workspaceOnly` vaut `false`, les `MEDIA:` sortants peuvent utiliser des fichiers locaux de l’hôte que l’agent est déjà autorisé à lire.
  * Les chemins locaux peuvent être absolus, relatifs à l’espace de travail ou relatifs au répertoire personnel avec `~/`.
  * Les envois locaux depuis l’hôte n’autorisent toujours que les médias et les types de documents sûrs (images, audio, vidéo, PDF et documents Office). Les fichiers texte brut et les fichiers ressemblant à des secrets ne sont pas traités comme des médias envoyables.


Cela signifie que les images/fichiers générés en dehors de l’espace de travail peuvent désormais être envoyés lorsque votre politique fs autorise déjà ces lectures, sans rouvrir l’exfiltration arbitraire de pièces jointes texte de l’hôte.

## Checklist des opérations

bashCopy code
[code]
    openclaw status          # local status (creds, sessions, queued events)openclaw status --all    # full diagnosis (read-only, pasteable)openclaw status --deep   # asks the gateway for a live health probe with channel probes when supportedopenclaw health --json   # gateway health snapshot (WS; default can return a fresh cached snapshot)
[/code]

Les journaux se trouvent sous `/tmp/openclaw/` (par défaut : `openclaw-YYYY-MM-DD.log`).

## Étapes suivantes

  * WebChat : [WebChat](</fr/web/webchat>)
  * Opérations Gateway : [Guide d’exploitation Gateway](</fr/gateway>)
  * Cron + réveils : [Tâches Cron](</fr/automation/cron-jobs>)
  * Compagnon de barre de menus macOS : [App macOS OpenClaw](</fr/platforms/macos>)
  * App de nœud iOS : [App iOS](</fr/platforms/ios>)
  * App de nœud Android : [App Android](</fr/platforms/android>)
  * Statut Windows : [Windows (WSL2)](</fr/platforms/windows>)
  * Statut Linux : [App Linux](</fr/platforms/linux>)
  * Sécurité : [Sécurité](</fr/gateway/security>)


## Associé

  * [Bien démarrer](</fr/start/getting-started>)
  * [Configuration](</fr/start/setup>)
  * [Vue d’ensemble des canaux](</fr/channels>)


Was this useful?YesNo