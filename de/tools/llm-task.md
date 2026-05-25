---
title: LLM-Aufgabe
source_url: https://docs.openclaw.ai/de/tools/llm-task
scraped_at: 2026-05-25
---

`llm-task` ist ein **optionales Plugin-Tool** , das eine reine JSON-LLM-Aufgabe ausführt und strukturierte Ausgabe zurückgibt (optional gegen JSON Schema validiert).

Dies ist ideal für Workflow-Engines wie Lobster: Sie können einen einzelnen LLM-Schritt hinzufügen, ohne für jeden Workflow eigenen OpenClaw-Code zu schreiben.

## Plugin aktivieren

  1. Aktivieren Sie das Plugin:

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  }}
[/code]

  2. Erlauben Sie das optionale Tool:

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["llm-task"]  }}
[/code]

Verwenden Sie `tools.allow` nur, wenn Sie den restriktiven Allowlist-Modus möchten.

## Konfiguration (optional)

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": {        "enabled": true,        "config": {          "defaultProvider": "openai-codex",          "defaultModel": "gpt-5.5",          "defaultAuthProfileId": "main",          "allowedModels": ["openai/gpt-5.4"],          "maxTokens": 800,          "timeoutMs": 30000        }      }    }  }}
[/code]

`allowedModels` ist eine Allowlist von `provider/model`-Strings. Wenn sie festgelegt ist, wird jede Anfrage außerhalb der Liste abgelehnt.

## Tool-Parameter

  * `prompt` (String, erforderlich)
  * `input` (beliebig, optional)
  * `schema` (Objekt, optionales JSON Schema)
  * `provider` (String, optional)
  * `model` (String, optional)
  * `thinking` (String, optional)
  * `authProfileId` (String, optional)
  * `temperature` (Zahl, optional)
  * `maxTokens` (Zahl, optional)
  * `timeoutMs` (Zahl, optional)


`thinking` akzeptiert die standardmäßigen OpenClaw-Reasoning-Voreinstellungen, etwa `low` oder `medium`.

## Ausgabe

Gibt `details.json` zurück, das das geparste JSON enthält (und gegen `schema` validiert, wenn angegeben).

## Beispiel: Lobster-Workflow-Schritt

### Wichtige Einschränkung

Das folgende Beispiel setzt voraus, dass die **eigenständige Lobster CLI** in einer Umgebung ausgeführt wird, in der `openclaw.invoke` bereits den korrekten Gateway-URL-/Auth-Kontext hat.

Für den gebündelten **eingebetteten** Lobster-Runner innerhalb von OpenClaw ist dieses verschachtelte CLI-Muster **derzeit nicht zuverlässig** :

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

Bis eingebettetes Lobster eine unterstützte Bridge für diesen Ablauf hat, bevorzugen Sie entweder:

  * direkte `llm-task`-Tool-Aufrufe außerhalb von Lobster oder
  * Lobster-Schritte, die nicht auf verschachtelte `openclaw.invoke`-Aufrufe angewiesen sind.


Beispiel für eigenständige Lobster CLI:

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": {    "subject": "Hello",    "body": "Can you help?"  },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

## Sicherheitshinweise

  * Das Tool ist **ausschließlich JSON** und weist das Modell an, nur JSON auszugeben (keine Code-Fences, keine Kommentare).
  * Dem Modell werden für diesen Lauf keine Tools bereitgestellt.
  * Behandeln Sie die Ausgabe als nicht vertrauenswürdig, sofern Sie sie nicht mit `schema` validieren.
  * Platzieren Sie Genehmigungen vor jedem Schritt mit Seiteneffekten (senden, posten, ausführen).


## Siehe auch

  * [Thinking-Stufen](</de/tools/thinking>)
  * [Sub-Agents](</de/tools/subagents>)
  * [Slash-Befehle](</de/tools/slash-commands>)


Was this useful?YesNo