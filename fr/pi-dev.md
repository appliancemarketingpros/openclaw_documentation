---
title: Flux de travail de développement Pi
source_url: https://docs.openclaw.ai/fr/pi-dev
scraped_at: 2026-05-25
---

Un flux de travail sain pour travailler sur l’intégration Pi dans OpenClaw.

## Vérification des types et linting

  * Porte locale par défaut : `pnpm check`
  * Porte de build : `pnpm build` lorsque le changement peut affecter la sortie de build, le packaging ou les limites de chargement différé/modules
  * Porte complète avant intégration pour les changements fortement liés à Pi : `pnpm check && pnpm test`


## Exécuter les tests Pi

Exécutez directement l’ensemble de tests centrés sur Pi avec Vitest :

bashCopy code
[code]
    pnpm test \  "src/agents/pi-*.test.ts" \  "src/agents/pi-embedded-*.test.ts" \  "src/agents/pi-tools*.test.ts" \  "src/agents/pi-settings.test.ts" \  "src/agents/pi-tool-definition-adapter*.test.ts" \  "src/agents/pi-hooks/**/*.test.ts"
[/code]

Pour inclure l’exercice du provider live :

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/pi-embedded-runner-extraparams.live.test.ts
[/code]

Cela couvre les principales suites de tests unitaires Pi :

  * `src/agents/pi-*.test.ts`
  * `src/agents/pi-embedded-*.test.ts`
  * `src/agents/pi-tools*.test.ts`
  * `src/agents/pi-settings.test.ts`
  * `src/agents/pi-tool-definition-adapter.test.ts`
  * `src/agents/pi-hooks/*.test.ts`


## Tests manuels

Flux recommandé :

  * Exécutez le Gateway en mode développement : 
    * `pnpm gateway:dev`
  * Déclenchez l’agent directement : 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Utilisez le TUI pour le débogage interactif : 
    * `pnpm tui`


Pour le comportement des appels d’outils, demandez une action `read` ou `exec` afin de voir le streaming des outils et le traitement des charges utiles.

## Réinitialisation complète

L’état se trouve dans le répertoire d’état OpenClaw. La valeur par défaut est `~/.openclaw`. Si `OPENCLAW_STATE_DIR` est défini, utilisez ce répertoire à la place.

Pour tout réinitialiser :

  * `openclaw.json` pour la configuration
  * `agents/<agentId>/agent/auth-profiles.json` pour les profils d’authentification du modèle (clés d’API + OAuth)
  * `credentials/` pour l’état des providers/canaux qui se trouve encore en dehors du magasin de profils d’authentification
  * `agents/<agentId>/sessions/` pour l’historique des sessions de l’agent
  * `agents/<agentId>/sessions/sessions.json` pour l’index des sessions
  * `sessions/` si des chemins hérités existent
  * `workspace/` si vous voulez un espace de travail vierge


Si vous souhaitez uniquement réinitialiser les sessions, supprimez `agents/<agentId>/sessions/` pour cet agent. Si vous souhaitez conserver l’authentification, laissez `agents/<agentId>/agent/auth-profiles.json` et tout état de provider sous `credentials/` en place.

## Références

  * [Tests](</fr/help/testing>)
  * [Premiers pas](</fr/start/getting-started>)


## Associé

  * [Architecture de l’intégration Pi](</fr/pi>)


Was this useful?YesNo