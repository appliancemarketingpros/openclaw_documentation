---
title: Tâche LLM
source_url: https://docs.openclaw.ai/fr/tools/llm-task
scraped_at: 2026-05-25
---

`llm-task` est un **outil Plugin facultatif** qui exécute une tâche LLM exclusivement JSON et renvoie une sortie structurée (facultativement validée avec JSON Schema).

C’est idéal pour les moteurs de workflow comme Lobster : vous pouvez ajouter une seule étape LLM sans écrire de code OpenClaw personnalisé pour chaque workflow.

## Activer le Plugin

  1. Activez le Plugin :

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  }}
[/code]

  2. Autorisez l’outil facultatif :

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["llm-task"]  }}
[/code]

Utilisez `tools.allow` uniquement lorsque vous voulez un mode de liste d’autorisation restrictif.

## Configuration (facultatif)

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": {        "enabled": true,        "config": {          "defaultProvider": "openai-codex",          "defaultModel": "gpt-5.5",          "defaultAuthProfileId": "main",          "allowedModels": ["openai/gpt-5.4"],          "maxTokens": 800,          "timeoutMs": 30000        }      }    }  }}
[/code]

`allowedModels` est une liste d’autorisation de chaînes `provider/model`. Si elle est définie, toute requête hors de la liste est rejetée.

## Paramètres de l’outil

  * `prompt` (chaîne, requis)
  * `input` (tout type, facultatif)
  * `schema` (objet, JSON Schema facultatif)
  * `provider` (chaîne, facultatif)
  * `model` (chaîne, facultatif)
  * `thinking` (chaîne, facultatif)
  * `authProfileId` (chaîne, facultatif)
  * `temperature` (nombre, facultatif)
  * `maxTokens` (nombre, facultatif)
  * `timeoutMs` (nombre, facultatif)


`thinking` accepte les préréglages de raisonnement OpenClaw standard, comme `low` ou `medium`.

## Sortie

Renvoie `details.json` contenant le JSON analysé (et valide avec `schema` lorsqu’il est fourni).

## Exemple : étape de workflow Lobster

### Limitation importante

L’exemple ci-dessous suppose que la **CLI Lobster autonome** s’exécute dans un environnement où `openclaw.invoke` dispose déjà du bon contexte d’URL/authentification du Gateway.

Pour le lanceur Lobster **intégré** fourni dans OpenClaw, ce modèle de CLI imbriquée n’est **pas fiable actuellement** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

Tant que Lobster intégré ne dispose pas d’un pont pris en charge pour ce flux, privilégiez l’une des options suivantes :

  * appels directs à l’outil `llm-task` en dehors de Lobster, ou
  * étapes Lobster qui ne reposent pas sur des appels `openclaw.invoke` imbriqués.


Exemple avec la CLI Lobster autonome :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": {    "subject": "Hello",    "body": "Can you help?"  },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

## Notes de sécurité

  * L’outil est **exclusivement JSON** et demande au modèle de produire uniquement du JSON (sans clôtures de code, sans commentaire).
  * Aucun outil n’est exposé au modèle pour cette exécution.
  * Traitez la sortie comme non fiable sauf si vous la validez avec `schema`.
  * Placez les approbations avant toute étape ayant des effets de bord (envoyer, publier, exécuter).


## Associé

  * [Niveaux de raisonnement](</fr/tools/thinking>)
  * [Sous-agents](</fr/tools/subagents>)
  * [Commandes slash](</fr/tools/slash-commands>)


Was this useful?YesNo