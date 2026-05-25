---
title: IPC macOS
source_url: https://docs.openclaw.ai/fr/platforms/mac/xpc
scraped_at: 2026-05-25
---

# Architecture IPC macOS d’OpenClaw

**Modèle actuel :** un socket Unix local connecte le **service hôte de nœud** à l’**app macOS** pour les approbations exec et `system.run`. Une CLI de débogage `openclaw-mac` existe pour les vérifications de découverte/connexion ; les actions d’agent passent toujours par le WebSocket Gateway et `node.invoke`. L’automatisation d’interface utilise PeekabooBridge.

## Objectifs

  * Une seule instance d’app GUI qui possède tout le travail lié à TCC (notifications, enregistrement d’écran, micro, parole, AppleScript).
  * Une petite surface pour l’automatisation : Gateway + commandes de nœud, plus PeekabooBridge pour l’automatisation d’interface.
  * Des autorisations prévisibles : toujours le même identifiant de bundle signé, lancé par launchd, afin que les autorisations TCC persistent.


## Fonctionnement

### Gateway + transport de nœud

  * L’app exécute la Gateway (mode local) et s’y connecte comme nœud.
  * Les actions d’agent sont exécutées via `node.invoke` (par ex. `system.run`, `system.notify`, `canvas.*`).


### Service de nœud + IPC app

  * Un service hôte de nœud headless se connecte au WebSocket Gateway.
  * Les requêtes `system.run` sont transférées à l’app macOS via un socket Unix local.
  * L’app exécute l’exec dans le contexte UI, demande une confirmation si nécessaire et renvoie la sortie.


Diagramme (SCI) :

CodeCopy code
[code]
    Agent -> Gateway -> Node Service (WS)                      |  IPC (UDS + token + HMAC + TTL)                      v                  Mac App (UI + TCC + system.run)
[/code]

### PeekabooBridge (automatisation d’interface)

  * L’automatisation d’interface utilise un socket UNIX distinct nommé `bridge.sock` et le protocole JSON PeekabooBridge.
  * Ordre de préférence de l’hôte (côté client) : Peekaboo.app → Claude.app → OpenClaw.app → exécution locale.
  * Sécurité : les hôtes du pont exigent un TeamID autorisé ; l’échappatoire même UID uniquement en DEBUG est protégée par `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` (convention Peekaboo).
  * Voir : [utilisation de PeekabooBridge](</fr/platforms/mac/peekaboo>) pour les détails.


## Flux opérationnels

  * Redémarrage/reconstruction : `SIGN_IDENTITY="Apple Development: &lt;Developer Name&gt; (&lt;TEAMID&gt;)" scripts/restart-mac.sh`
    * Tue les instances existantes
    * Build Swift + packaging
    * Écrit/initialise/lance le LaunchAgent
  * Instance unique : l’app se ferme immédiatement si une autre instance avec le même identifiant de bundle est en cours d’exécution.


## Remarques de durcissement

  * Préférez exiger une correspondance de TeamID pour toutes les surfaces privilégiées.
  * PeekabooBridge : `PEEKABOO_ALLOW_UNSIGNED_SOCKET_CLIENTS=1` (DEBUG uniquement) peut autoriser des appelants de même UID pour le développement local.
  * Toute la communication reste locale uniquement ; aucun socket réseau n’est exposé.
  * Les invites TCC proviennent uniquement du bundle de l’app GUI ; gardez l’identifiant de bundle signé stable entre les reconstructions.
  * Durcissement IPC : mode du socket `0600`, jeton, vérifications d’UID pair, défi/réponse HMAC, TTL court.


## Liens associés

  * [app macOS](</fr/platforms/macos>)
  * [Flux IPC macOS (approbations Exec)](</fr/tools/exec-approvals-advanced#macos-ipc-flow>)


Was this useful?YesNo