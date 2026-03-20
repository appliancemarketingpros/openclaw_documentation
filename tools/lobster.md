---
title: Lobster
source_url: https://docs.openclaw.ai/tools/lobster
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

Lobster

# 

​

Lobster

Lobster is a workflow shell that lets OpenClaw run multi-step tool sequences as a single, deterministic operation with explicit approval checkpoints.

## 

​

Hook

Your assistant can build the tools that manage itself. Ask for a workflow, and 30 minutes later you have a CLI plus pipelines that run as one call. Lobster is the missing piece: deterministic pipelines, explicit approvals, and resumable state.

## 

​

Why

Today, complex workflows require many back-and-forth tool calls. Each call costs tokens, and the LLM has to orchestrate every step. Lobster moves that orchestration into a typed runtime:

  * **One call instead of many** : OpenClaw runs one Lobster tool call and gets a structured result.
  * **Approvals built in** : Side effects (send email, post comment) halt the workflow until explicitly approved.
  * **Resumable** : Halted workflows return a token; approve and resume without re-running everything.


## 

​

Why a DSL instead of plain programs?

Lobster is intentionally small. The goal is not “a new language,” it’s a predictable, AI-friendly pipeline spec with first-class approvals and resume tokens.

  * **Approve/resume is built in** : A normal program can prompt a human, but it can’t _pause and resume_ with a durable token without you inventing that runtime yourself.
  * **Determinism + auditability** : Pipelines are data, so they’re easy to log, diff, replay, and review.
  * **Constrained surface for AI** : A tiny grammar + JSON piping reduces “creative” code paths and makes validation realistic.
  * **Safety policy baked in** : Timeouts, output caps, sandbox checks, and allowlists are enforced by the runtime, not each script.
  * **Still programmable** : Each step can call any CLI or script. If you want JS/TS, generate `.lobster` files from code.


## 

​

How it works

OpenClaw launches the local `lobster` CLI in **tool mode** and parses a JSON envelope from stdout. If the pipeline pauses for approval, the tool returns a `resumeToken` so you can continue later.

## 

​

Pattern: small CLI + JSON pipes + approvals

Build tiny commands that speak JSON, then chain them into a single Lobster call. (Example command names below — swap in your own.)

Copy
[code]
    inbox list --json
    inbox categorize --json
    inbox apply --json
    
[/code]

Copy
[code]
    {
      "action": "run",
      "pipeline": "exec --json --shell 'inbox list --json' | exec --stdin json --shell 'inbox categorize --json' | exec --stdin json --shell 'inbox apply --json' | approve --preview-from-stdin --limit 5 --prompt 'Apply changes?'",
      "timeoutMs": 30000
    }
    
[/code]

If the pipeline requests approval, resume with the token:

Copy
[code]
    {
      "action": "resume",
      "token": "<resumeToken>",
      "approve": true
    }
    
[/code]

AI triggers the workflow; Lobster executes the steps. Approval gates keep side effects explicit and auditable. Example: map input items into tool calls:

Copy
[code]
    gog.gmail.search --query 'newer_than:1d' \
      | openclaw.invoke --tool message --action send --each --item-key message --args-json '{"provider":"telegram","to":"..."}'
    
[/code]

## 

​

JSON-only LLM steps (llm-task)

For workflows that need a **structured LLM step** , enable the optional `llm-task` plugin tool and call it from Lobster. This keeps the workflow deterministic while still letting you classify/summarize/draft with a model. Enable the tool:

Copy
[code]
    {
      "plugins": {
        "entries": {
          "llm-task": { "enabled": true }
        }
      },
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

Use it in a pipeline:

Copy
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{
      "prompt": "Given the input email, return intent and draft.",
      "thinking": "low",
      "input": { "subject": "Hello", "body": "Can you help?" },
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

See [LLM Task](</tools/llm-task>) for details and configuration options.

## 

​

Workflow files (.lobster)

Lobster can run YAML/JSON workflow files with `name`, `args`, `steps`, `env`, `condition`, and `approval` fields. In OpenClaw tool calls, set `pipeline` to the file path.

Copy
[code]
    name: inbox-triage
    args:
      tag:
        default: "family"
    steps:
      - id: collect
        command: inbox list --json
      - id: categorize
        command: inbox categorize --json
        stdin: $collect.stdout
      - id: approve
        command: inbox apply --approve
        stdin: $categorize.stdout
        approval: required
      - id: execute
        command: inbox apply --execute
        stdin: $categorize.stdout
        condition: $approve.approved
    
[/code]

Notes:

  * `stdin: $step.stdout` and `stdin: $step.json` pass a prior step’s output.
  * `condition` (or `when`) can gate steps on `$step.approved`.


## 

​

Install Lobster

Install the Lobster CLI on the **same host** that runs the OpenClaw Gateway (see the [Lobster repo](<https://github.com/openclaw/lobster>)), and ensure `lobster` is on `PATH`.

## 

​

Enable the tool

Lobster is an **optional** plugin tool (not enabled by default). Recommended (additive, safe):

Copy
[code]
    {
      "tools": {
        "alsoAllow": ["lobster"]
      }
    }
    
[/code]

Or per-agent:

Copy
[code]
    {
      "agents": {
        "list": [
          {
            "id": "main",
            "tools": {
              "alsoAllow": ["lobster"]
            }
          }
        ]
      }
    }
    
[/code]

Avoid using `tools.allow: ["lobster"]` unless you intend to run in restrictive allowlist mode. Note: allowlists are opt-in for optional plugins. If your allowlist only names plugin tools (like `lobster`), OpenClaw keeps core tools enabled. To restrict core tools, include the core tools or groups you want in the allowlist too.

## 

​

Example: Email triage

Without Lobster:

Copy
[code]
    User: "Check my email and draft replies"
    → openclaw calls gmail.list
    → LLM summarizes
    → User: "draft replies to #2 and #5"
    → LLM drafts
    → User: "send #2"
    → openclaw calls gmail.send
    (repeat daily, no memory of what was triaged)
    
[/code]

With Lobster:

Copy
[code]
    {
      "action": "run",
      "pipeline": "email.triage --limit 20",
      "timeoutMs": 30000
    }
    
[/code]

Returns a JSON envelope (truncated):

Copy
[code]
    {
      "ok": true,
      "status": "needs_approval",
      "output": [{ "summary": "5 need replies, 2 need action" }],
      "requiresApproval": {
        "type": "approval_request",
        "prompt": "Send 2 draft replies?",
        "items": [],
        "resumeToken": "..."
      }
    }
    
[/code]

User approves → resume:

Copy
[code]
    {
      "action": "resume",
      "token": "<resumeToken>",
      "approve": true
    }
    
[/code]

One workflow. Deterministic. Safe.

## 

​

Tool parameters

### 

​

`run`

Run a pipeline in tool mode.

Copy
[code]
    {
      "action": "run",
      "pipeline": "gog.gmail.search --query 'newer_than:1d' | email.triage",
      "cwd": "workspace",
      "timeoutMs": 30000,
      "maxStdoutBytes": 512000
    }
    
[/code]

Run a workflow file with args:

Copy
[code]
    {
      "action": "run",
      "pipeline": "/path/to/inbox-triage.lobster",
      "argsJson": "{\"tag\":\"family\"}"
    }
    
[/code]

### 

​

`resume`

Continue a halted workflow after approval.

Copy
[code]
    {
      "action": "resume",
      "token": "<resumeToken>",
      "approve": true
    }
    
[/code]

### 

​

Optional inputs

  * `cwd`: Relative working directory for the pipeline (must stay within the current process working directory).
  * `timeoutMs`: Kill the subprocess if it exceeds this duration (default: 20000).
  * `maxStdoutBytes`: Kill the subprocess if stdout exceeds this size (default: 512000).
  * `argsJson`: JSON string passed to `lobster run --args-json` (workflow files only).


## 

​

Output envelope

Lobster returns a JSON envelope with one of three statuses:

  * `ok` → finished successfully
  * `needs_approval` → paused; `requiresApproval.resumeToken` is required to resume
  * `cancelled` → explicitly denied or cancelled

The tool surfaces the envelope in both `content` (pretty JSON) and `details` (raw object).

## 

​

Approvals

If `requiresApproval` is present, inspect the prompt and decide:

  * `approve: true` → resume and continue side effects
  * `approve: false` → cancel and finalize the workflow

Use `approve --preview-from-stdin --limit N` to attach a JSON preview to approval requests without custom jq/heredoc glue. Resume tokens are now compact: Lobster stores workflow resume state under its state dir and hands back a small token key.

## 

​

OpenProse

OpenProse pairs well with Lobster: use `/prose` to orchestrate multi-agent prep, then run a Lobster pipeline for deterministic approvals. If a Prose program needs Lobster, allow the `lobster` tool for sub-agents via `tools.subagents.tools`. See [OpenProse](</prose>).

## 

​

Safety

  * **Local subprocess only** — no network calls from the plugin itself.
  * **No secrets** — Lobster doesn’t manage OAuth; it calls OpenClaw tools that do.
  * **Sandbox-aware** — disabled when the tool context is sandboxed.
  * **Hardened** — fixed executable name (`lobster`) on `PATH`; timeouts and output caps enforced.


## 

​

Troubleshooting

  * **`lobster subprocess timed out`** → increase `timeoutMs`, or split a long pipeline.
  * **`lobster output exceeded maxStdoutBytes`** → raise `maxStdoutBytes` or reduce output size.
  * **`lobster returned invalid JSON`** → ensure the pipeline runs in tool mode and prints only JSON.
  * **`lobster failed (code …)`** → run the same pipeline in a terminal to inspect stderr.


## 

​

Learn more

  * [Plugins](</tools/plugin>)
  * [Plugin tool authoring](</plugins/agent-tools>)


## 

​

Case study: community workflows

One public example: a “second brain” CLI + Lobster pipelines that manage three Markdown vaults (personal, partner, shared). The CLI emits JSON for stats, inbox listings, and stale scans; Lobster chains those commands into workflows like `weekly-review`, `inbox-triage`, `memory-consolidation`, and `shared-task-sync`, each with approval gates. AI handles judgment (categorization) when available and falls back to deterministic rules when not.

  * Thread: <https://x.com/plattenschieber/status/2014508656335770033>
  * Repo: <https://github.com/bloomedai/brain-cli>


[LLM Task](</tools/llm-task>)[Tool-loop detection](</tools/loop-detection>)

⌘I