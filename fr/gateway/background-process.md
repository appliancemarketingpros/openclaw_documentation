---
title: Outil d’exécution en arrière-plan et de processus
source_url: https://docs.openclaw.ai/fr/gateway/background-process
scraped_at: 2026-05-25
---

OpenClaw exécute les commandes shell via l’outil `exec` et conserve les tâches longues en mémoire. L’outil `process` gère ces sessions en arrière-plan.

## Outil exec

Paramètres clés :

  * `command` (obligatoire)
  * `yieldMs` (par défaut 10000) : passage automatique en arrière-plan après ce délai
  * `background` (booléen) : passage immédiat en arrière-plan
  * `timeout` (secondes, par défaut `tools.exec.timeoutSec`) : tue le processus après ce délai d’expiration ; définissez `timeout: 0` uniquement pour désactiver le délai d’expiration du processus exec pour cet appel
  * `elevated` (booléen) : exécute hors du bac à sable si le mode élevé est activé/autorisé (`gateway` par défaut, ou `node` quand la cible exec est `node`)
  * Besoin d’un vrai TTY ? Définissez `pty: true`.
  * `workdir`, `env`


Comportement :

  * Les exécutions au premier plan renvoient directement la sortie.
  * Lors du passage en arrière-plan (explicite ou par délai), l’outil renvoie `status: "running"` \+ `sessionId` et un court extrait final.
  * Les exécutions en arrière-plan et `yieldMs` héritent de `tools.exec.timeoutSec`, sauf si l’appel fournit un `timeout` explicite.
  * La sortie est conservée en mémoire jusqu’à ce que la session soit interrogée ou effacée.
  * Si l’outil `process` est interdit, `exec` s’exécute de manière synchrone et ignore `yieldMs`/`background`.
  * Les commandes exec lancées reçoivent `OPENCLAW_SHELL=exec` pour les règles shell/profil sensibles au contexte.
  * Pour un travail long qui démarre maintenant, lancez-le une seule fois et comptez sur le réveil automatique de fin lorsqu’il est activé et que la commande émet une sortie ou échoue.
  * Si le réveil automatique de fin n’est pas disponible, ou si vous avez besoin d’une confirmation de réussite silencieuse pour une commande qui s’est terminée proprement sans sortie, utilisez `process` pour confirmer la fin.
  * N’émulez pas les rappels ou les suivis différés avec des boucles `sleep` ou des interrogations répétées ; utilisez cron pour les travaux futurs.


## Pontage des processus enfants

Lors du lancement de processus enfants longue durée hors des outils exec/process (par exemple des relances de CLI ou des assistants gateway), attachez l’aide de pontage de processus enfant afin que les signaux de terminaison soient transmis et que les écouteurs soient détachés à la sortie/en cas d’erreur. Cela évite les processus orphelins sous systemd et maintient un comportement d’arrêt cohérent sur toutes les plateformes.

Surcharges d’environnement :

  * `PI_BASH_YIELD_MS` : délai yield par défaut (ms)
  * `PI_BASH_MAX_OUTPUT_CHARS` : plafond de sortie en mémoire (caractères)
  * `OPENCLAW_BASH_PENDING_MAX_OUTPUT_CHARS` : plafond stdout/stderr en attente par flux (caractères)
  * `PI_BASH_JOB_TTL_MS` : TTL pour les sessions terminées (ms, borné de 1 min à 3 h)
  * `OPENCLAW_PROCESS_INPUT_WAIT_IDLE_MS` : seuil de sortie inactive avant que les sessions en arrière-plan inscriptibles soient marquées comme probablement en attente d’entrée (par défaut 15000 ms)


Configuration (préférée) :

  * `tools.exec.backgroundMs` (par défaut 10000)
  * `tools.exec.timeoutSec` (par défaut 1800)
  * `tools.exec.cleanupMs` (par défaut 1800000)
  * `tools.exec.notifyOnExit` (par défaut true) : met en file un événement système + demande un heartbeat lorsqu’un exec en arrière-plan se termine.
  * `tools.exec.notifyOnExitEmptySuccess` (par défaut false) : lorsque true, met aussi en file des événements de fin pour les exécutions en arrière-plan réussies qui n’ont produit aucune sortie.


## Outil process

Actions :

  * `list` : sessions en cours + terminées
  * `poll` : vider la nouvelle sortie d’une session (signale aussi l’état de sortie)
  * `log` : lire la sortie agrégée et afficher les indications de récupération d’entrée (prend en charge `offset` \+ `limit`)
  * `write` : envoyer stdin (`data`, `eof` optionnel)
  * `send-keys` : envoyer des jetons de touches explicites ou des octets à une session soutenue par un PTY
  * `submit` : envoyer Entrée / retour chariot à une session soutenue par un PTY
  * `paste` : envoyer du texte littéral, éventuellement enveloppé en mode collage entre crochets
  * `kill` : terminer une session en arrière-plan
  * `clear` : retirer de la mémoire une session terminée
  * `remove` : tuer si en cours, sinon effacer si terminée


Notes :

  * Seules les sessions passées en arrière-plan sont listées/conservées en mémoire.
  * Les sessions sont perdues au redémarrage du processus (pas de persistance disque).
  * Les journaux de session ne sont enregistrés dans l’historique de chat que si vous exécutez `process poll/log` et que le résultat de l’outil est enregistré.
  * `process` est limité à chaque agent ; il ne voit que les sessions démarrées par cet agent.
  * Utilisez `poll` / `log` pour l’état, les journaux, la confirmation de réussite silencieuse ou la confirmation de fin lorsque le réveil automatique de fin n’est pas disponible.
  * Utilisez `log` avant de récupérer une CLI interactive afin que le transcript actuel, l’état de stdin et l’indication d’attente d’entrée soient visibles ensemble.
  * Utilisez `write` / `send-keys` / `submit` / `paste` / `kill` lorsque vous avez besoin d’une entrée ou d’une intervention.
  * `process list` inclut un `name` dérivé (verbe de commande + cible) pour des parcours rapides.
  * `process list`, `poll` et `log` signalent `waitingForInput` uniquement lorsque la session dispose encore d’un stdin inscriptible et est restée inactive plus longtemps que le seuil d’attente d’entrée.
  * `process log` utilise `offset`/`limit` par lignes.
  * Lorsque `offset` et `limit` sont tous deux omis, il renvoie les 200 dernières lignes et inclut une indication de pagination.
  * Lorsque `offset` est fourni et que `limit` est omis, il renvoie depuis `offset` jusqu’à la fin (sans plafonnement à 200).
  * L’interrogation sert à obtenir l’état à la demande, pas à planifier une boucle d’attente. Si le travail doit se produire plus tard, utilisez plutôt cron.


## Exemples

Exécuter une tâche longue et l’interroger plus tard :

jsonCopy code
[code]
    { "tool": "exec", "command": "sleep 5 && echo done", "yieldMs": 1000 }
[/code]

jsonCopy code
[code]
    { "tool": "process", "action": "poll", "sessionId": "<id>" }
[/code]

Inspecter une session interactive avant d’envoyer une entrée :

jsonCopy code
[code]
    { "tool": "process", "action": "log", "sessionId": "<id>" }
[/code]

Démarrer immédiatement en arrière-plan :

jsonCopy code
[code]
    { "tool": "exec", "command": "npm run build", "background": true }
[/code]

Envoyer stdin :

jsonCopy code
[code]
    { "tool": "process", "action": "write", "sessionId": "<id>", "data": "y\n" }
[/code]

Envoyer des touches PTY :

jsonCopy code
[code]
    { "tool": "process", "action": "send-keys", "sessionId": "<id>", "keys": ["C-c"] }
[/code]

Soumettre la ligne actuelle :

jsonCopy code
[code]
    { "tool": "process", "action": "submit", "sessionId": "<id>" }
[/code]

Coller du texte littéral :

jsonCopy code
[code]
    { "tool": "process", "action": "paste", "sessionId": "<id>", "text": "line1\nline2\n" }
[/code]

## Connexe

  * [Outil exec](</fr/tools/exec>)
  * [Approbations exec](</fr/tools/exec-approvals>)


Was this useful?YesNo