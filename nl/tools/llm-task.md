---
title: LLM-taak
source_url: https://docs.openclaw.ai/nl/tools/llm-task
scraped_at: 2026-05-25
---

`llm-task` is een **optionele Plugin-tool** die een JSON-only LLM-taak uitvoert en gestructureerde uitvoer retourneert (optioneel gevalideerd tegen JSON Schema).

Dit is ideaal voor workflow-engines zoals Lobster: je kunt één LLM-stap toevoegen zonder voor elke workflow aangepaste OpenClaw-code te schrijven.

## De Plugin inschakelen

  1. Schakel de Plugin in:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  }}
[/code]

  2. Sta de optionele tool toe:

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["llm-task"]  }}
[/code]

Gebruik `tools.allow` alleen wanneer je de beperkende allowlist-modus wilt.

## Configuratie (optioneel)

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": {        "enabled": true,        "config": {          "defaultProvider": "openai-codex",          "defaultModel": "gpt-5.5",          "defaultAuthProfileId": "main",          "allowedModels": ["openai/gpt-5.4"],          "maxTokens": 800,          "timeoutMs": 30000        }      }    }  }}
[/code]

`allowedModels` is een allowlist van `provider/model`-strings. Als dit is ingesteld, wordt elk verzoek buiten de lijst geweigerd.

## Toolparameters

  * `prompt` (string, vereist)
  * `input` (any, optioneel)
  * `schema` (object, optioneel JSON Schema)
  * `provider` (string, optioneel)
  * `model` (string, optioneel)
  * `thinking` (string, optioneel)
  * `authProfileId` (string, optioneel)
  * `temperature` (number, optioneel)
  * `maxTokens` (number, optioneel)
  * `timeoutMs` (number, optioneel)


`thinking` accepteert de standaard redeneerpresets van OpenClaw, zoals `low` of `medium`.

## Uitvoer

Retourneert `details.json` met de geparste JSON (en valideert tegen `schema` wanneer opgegeven).

## Voorbeeld: Lobster-workflowstap

### Belangrijke beperking

Het onderstaande voorbeeld gaat ervan uit dat de **zelfstandige Lobster CLI** draait in een omgeving waar `openclaw.invoke` al de juiste Gateway-URL/auth-context heeft.

Voor de gebundelde **embedded** Lobster-runner binnen OpenClaw is dit geneste CLI-patroon **momenteel niet betrouwbaar** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

Totdat embedded Lobster een ondersteunde bridge voor deze flow heeft, geef je de voorkeur aan:

  * directe `llm-task`-toolaanroepen buiten Lobster, of
  * Lobster-stappen die niet afhankelijk zijn van geneste `openclaw.invoke`-aanroepen.


Voorbeeld voor zelfstandige Lobster CLI:

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": {    "subject": "Hello",    "body": "Can you help?"  },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

## Veiligheidsnotities

  * De tool is **JSON-only** en instrueert het model om alleen JSON uit te voeren (geen code fences, geen commentaar).
  * Er worden voor deze run geen tools aan het model blootgesteld.
  * Behandel uitvoer als niet-vertrouwd, tenzij je valideert met `schema`.
  * Plaats goedkeuringen vóór elke stap met bijwerkingen (send, post, exec).


## Gerelateerd

  * [Thinking-niveaus](</nl/tools/thinking>)
  * [Sub-agents](</nl/tools/subagents>)
  * [Slash commands](</nl/tools/slash-commands>)


Was this useful?YesNo