---
title: agents
source_url: https://docs.openclaw.ai/cli/agents
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Agents and sessions

agents

# 

​

`openclaw agents`

Manage isolated agents (workspaces + auth + routing). Related:

  * Multi-agent routing: [Multi-Agent Routing](</concepts/multi-agent>)
  * Agent workspace: [Agent workspace](</concepts/agent-workspace>)


## 

​

Examples

Copy
[code]
    openclaw agents list
    openclaw agents add work --workspace ~/.openclaw/workspace-work
    openclaw agents bindings
    openclaw agents bind --agent work --bind telegram:ops
    openclaw agents unbind --agent work --bind telegram:ops
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
    openclaw agents set-identity --agent main --avatar avatars/openclaw.png
    openclaw agents delete work
    
[/code]

## 

​

Routing bindings

Use routing bindings to pin inbound channel traffic to a specific agent. List bindings:

Copy
[code]
    openclaw agents bindings
    openclaw agents bindings --agent work
    openclaw agents bindings --json
    
[/code]

Add bindings:

Copy
[code]
    openclaw agents bind --agent work --bind telegram:ops --bind discord:guild-a
    
[/code]

If you omit `accountId` (`--bind <channel>`), OpenClaw resolves it from channel defaults and plugin setup hooks when available.

### 

​

Binding scope behavior

  * A binding without `accountId` matches the channel default account only.
  * `accountId: "*"` is the channel-wide fallback (all accounts) and is less specific than an explicit account binding.
  * If the same agent already has a matching channel binding without `accountId`, and you later bind with an explicit or resolved `accountId`, OpenClaw upgrades that existing binding in place instead of adding a duplicate.

Example:

Copy
[code]
    # initial channel-only binding
    openclaw agents bind --agent work --bind telegram
    
    # later upgrade to account-scoped binding
    openclaw agents bind --agent work --bind telegram:ops
    
[/code]

After the upgrade, routing for that binding is scoped to `telegram:ops`. If you also want default-account routing, add it explicitly (for example `--bind telegram:default`). Remove bindings:

Copy
[code]
    openclaw agents unbind --agent work --bind telegram:ops
    openclaw agents unbind --agent work --all
    
[/code]

## 

​

Identity files

Each agent workspace can include an `IDENTITY.md` at the workspace root:

  * Example path: `~/.openclaw/workspace/IDENTITY.md`
  * `set-identity --from-identity` reads from the workspace root (or an explicit `--identity-file`)

Avatar paths resolve relative to the workspace root.

## 

​

Set identity

`set-identity` writes fields into `agents.list[].identity`:

  * `name`
  * `theme`
  * `emoji`
  * `avatar` (workspace-relative path, http(s) URL, or data URI)

Load from `IDENTITY.md`:

Copy
[code]
    openclaw agents set-identity --workspace ~/.openclaw/workspace --from-identity
    
[/code]

Override fields explicitly:

Copy
[code]
    openclaw agents set-identity --agent main --name "OpenClaw" --emoji "🦞" --avatar avatars/openclaw.png
    
[/code]

Config sample:

Copy
[code]
    {
      agents: {
        list: [
          {
            id: "main",
            identity: {
              name: "OpenClaw",
              theme: "space lobster",
              emoji: "🦞",
              avatar: "avatars/openclaw.png",
            },
          },
        ],
      },
    }
    
[/code]

[agent](</cli/agent>)[hooks](</cli/hooks>)

⌘I