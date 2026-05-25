---
title: Canal QA
source_url: https://docs.openclaw.ai/fr/channels/qa-channel
scraped_at: 2026-05-25
---

`qa-channel` est un transport de messages synthétique intégré pour la QA automatisée d’OpenClaw. Ce n’est pas un canal de production - il existe pour exercer la même frontière de Plugin de canal que les transports réels, tout en gardant l’état déterministe et entièrement inspectable.

## Ce qu’il fait

  * Grammaire de cibles de classe Slack : 
    * `dm:<user>`
    * `channel:<room>`
    * `group:<room>`
    * `thread:<room>/<thread>`
  * Les conversations partagées `channel:` et `group:` sont présentées aux agents comme des tours de salle de groupe/canal, afin qu’elles exercent la même politique de réponse visible et de routage des outils de message que celle utilisée par Discord, Slack, Telegram et les transports similaires.
  * Bus synthétique adossé à HTTP pour l’injection de messages entrants, la capture de transcriptions sortantes, la création de fils, les réactions, les modifications, les suppressions et les actions de recherche/lecture.
  * Exécuteur d’auto-vérification côté hôte qui écrit un rapport Markdown dans `.artifacts/qa-e2e/`.


## Configuration

jsonCopy code
[code]
    {  "channels": {    "qa-channel": {      "baseUrl": "http://127.0.0.1:43123",      "botUserId": "openclaw",      "botDisplayName": "OpenClaw QA",      "allowFrom": ["*"],      "pollTimeoutMs": 1000    }  }}
[/code]

Clés de compte :

  * `enabled` \- interrupteur principal pour ce compte.
  * `name` \- libellé d’affichage facultatif.
  * `baseUrl` \- URL du bus synthétique.
  * `botUserId` \- identifiant utilisateur du bot de style Matrix utilisé dans la grammaire de cibles.
  * `botDisplayName` \- nom d’affichage pour les messages sortants.
  * `pollTimeoutMs` \- fenêtre d’attente long-poll. Entier compris entre 100 et 30000.
  * `allowFrom` \- liste d’autorisation des expéditeurs (identifiants utilisateur ou `"*"`). Les messages directs et la politique de groupe avec liste d’autorisation utilisent tous deux ces identifiants d’expéditeurs synthétiques.
  * `groupPolicy` \- politique des salles partagées : `"open"` (par défaut), `"allowlist"` ou `"disabled"`.
  * `groupAllowFrom` \- liste d’autorisation facultative des expéditeurs en salle partagée. Lorsqu’elle est omise sous `"allowlist"`, QA Channel se rabat sur `allowFrom`.
  * `groups.<room>.requireMention` \- exiger une mention du bot avant de répondre dans une salle de groupe/canal spécifique. `groups."*"` définit la valeur par défaut.
  * `defaultTo` \- cible de repli lorsqu’aucune n’est fournie.
  * `actions.messages` / `actions.reactions` / `actions.search` / `actions.threads` \- contrôle d’accès aux outils par action.


Clés multi-comptes au niveau supérieur :

  * `accounts` \- enregistrement des surcharges nommées par compte, indexées par identifiant de compte.
  * `defaultAccount` \- identifiant de compte préféré lorsque plusieurs comptes sont configurés.


## Exécuteurs

Auto-vérification côté hôte (écrit un rapport Markdown sous `.artifacts/qa-e2e/`) :

bashCopy code
[code]
    pnpm qa:e2e
[/code]

Cela passe par `qa-lab`, démarre le bus QA intégré au dépôt, amorce la tranche d’exécution `qa-channel` intégrée et exécute une auto-vérification déterministe.

Suite complète de scénarios adossée au dépôt :

bashCopy code
[code]
    pnpm openclaw qa suite
[/code]

Exécute les scénarios en parallèle contre la voie de Gateway QA. Consultez la [vue d’ensemble QA](</fr/concepts/qa-e2e-automation>) pour les scénarios, les profils et les modes fournisseur.

Site QA adossé à Docker (Gateway + interface de débogage QA Lab dans une seule pile) :

bashCopy code
[code]
    pnpm qa:lab:up
[/code]

Construit le site QA, démarre la pile Gateway + QA Lab adossée à Docker et affiche l’URL de QA Lab. À partir de là, vous pouvez choisir des scénarios, sélectionner la voie de modèle, lancer des exécutions individuelles et regarder les résultats en direct. Le débogueur QA Lab est distinct du bundle Control UI livré.

## Liens associés

  * [Vue d’ensemble QA](</fr/concepts/qa-e2e-automation>) \- pile globale, adaptateurs de transport, création de scénarios
  * [QA Matrix](</fr/concepts/qa-matrix>) \- exemple d’exécuteur de transport réel qui pilote un vrai canal
  * [Appairage](</fr/channels/pairing>)
  * [Groupes](</fr/channels/groups>)
  * [Vue d’ensemble des canaux](</fr/channels>)


Was this useful?YesNo