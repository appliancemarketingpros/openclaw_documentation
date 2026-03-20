---
title: LLM Task
source_url: https://docs.openclaw.ai/tools/llm-task
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Tools

LLM Task

# 

​

LLM Task

`llm-task` is an **optional plugin tool** that runs a JSON-only LLM task and returns structured output (optionally validated against JSON Schema). This is ideal for workflow engines like Lobster: you can add a single LLM step without writing custom OpenClaw code for each workflow.

## 

​

Enable the plugin

  1. Enable the plugin:


Copy
[code]
    {
      "plugins": {
        "entries": {
          "llm-task": { "enabled": true }
        }
      }
    }
    
[/code]

  2. Allowlist the tool (it is registered with `optional: true`):


Copy
[code]
    {
      "agents": {
        "list": [
          {
            "id": "main",
            "tools": { "allow": ["llm-task"] }
          }
        ]
      }
    }
    
[/code]

## 

​

Config (optional)

Copy
[code]
    {
      "plugins": {
        "entries": {
          "llm-task": {
            "enabled": true,
            "config": {
              "defaultProvider": "openai-codex",
              "defaultModel": "gpt-5.4",
              "defaultAuthProfileId": "main",
              "allowedModels": ["openai-codex/gpt-5.4"],
              "maxTokens": 800,
              "timeoutMs": 30000
            }
          }
        }
      }
    }
    
[/code]

`allowedModels` is an allowlist of `provider/model` strings. If set, any request outside the list is rejected.

## 

​

Tool parameters

  * `prompt` (string, required)
  * `input` (any, optional)
  * `schema` (object, optional JSON Schema)
  * `provider` (string, optional)
  * `model` (string, optional)
  * `thinking` (string, optional)
  * `authProfileId` (string, optional)
  * `temperature` (number, optional)
  * `maxTokens` (number, optional)
  * `timeoutMs` (number, optional)

`thinking` accepts the standard OpenClaw reasoning presets, such as `low` or `medium`.

## 

​

Output

Returns `details.json` containing the parsed JSON (and validates against `schema` when provided).

## 

​

Example: Lobster workflow step

Copy
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{
      "prompt": "Given the input email, return intent and draft.",
      "thinking": "low",
      "input": {
        "subject": "Hello",
        "body": "Can you help?"
      },
      "schema": {
        "type": "object",
        "properties": {
          "intent": { "type": "string" },
          "draft": { "type": "string" }
        },
        "required": ["intent", "draft"],
        "additionalProperties": false
      }
    }'
    
[/code]

## 

​

Safety notes

  * The tool is **JSON-only** and instructs the model to output only JSON (no code fences, no commentary).
  * No tools are exposed to the model for this run.
  * Treat output as untrusted unless you validate with `schema`.
  * Put approvals before any side-effecting step (send, post, exec).


[Exec Approvals](</tools/exec-approvals>)[Lobster](</tools/lobster>)

⌘I