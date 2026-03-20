---
title: Elevated Mode
source_url: https://docs.openclaw.ai/tools/elevated
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

Elevated Mode

# 

​

Elevated Mode

When an agent runs inside a sandbox, its `exec` commands are confined to the sandbox environment. **Elevated mode** lets the agent break out and run commands on the gateway host instead, with configurable approval gates.

Elevated mode only changes behavior when the agent is **sandboxed**. For unsandboxed agents, exec already runs on the host.

## 

​

Directives

Control elevated mode per-session with slash commands:

Directive| What it does  
---|---  
`/elevated on`| Run on the gateway host, keep exec approvals  
`/elevated ask`| Same as `on` (alias)  
`/elevated full`| Run on the gateway host **and** skip exec approvals  
`/elevated off`| Return to sandbox-confined execution  
  
Also available as `/elev on|off|ask|full`. Send `/elevated` with no argument to see the current level.

## 

​

How it works

1

Check availability

Elevated must be enabled in config and the sender must be on the allowlist:

Copy
[code]
    {
      tools: {
        elevated: {
          enabled: true,
          allowFrom: {
            discord: ["user-id-123"],
            whatsapp: ["+15555550123"],
          },
        },
      },
    }
    
[/code]

2

Set the level

Send a directive-only message to set the session default:

Copy
[code]
    /elevated full
    
[/code]

Or use it inline (applies to that message only):

Copy
[code]
    /elevated on run the deployment script
    
[/code]

3

Commands run on the host

With elevated active, `exec` calls route to the gateway host instead of the sandbox. In `full` mode, exec approvals are skipped. In `on`/`ask` mode, configured approval rules still apply.

## 

​

Resolution order

  1. **Inline directive** on the message (applies only to that message)
  2. **Session override** (set by sending a directive-only message)
  3. **Global default** (`agents.defaults.elevatedDefault` in config)


## 

​

Availability and allowlists

  * **Global gate** : `tools.elevated.enabled` (must be `true`)
  * **Sender allowlist** : `tools.elevated.allowFrom` with per-channel lists
  * **Per-agent gate** : `agents.list[].tools.elevated.enabled` (can only further restrict)
  * **Per-agent allowlist** : `agents.list[].tools.elevated.allowFrom` (sender must match both global + per-agent)
  * **Discord fallback** : if `tools.elevated.allowFrom.discord` is omitted, `channels.discord.allowFrom` is used as fallback
  * **All gates must pass** ; otherwise elevated is treated as unavailable

Allowlist entry formats:

Prefix| Matches  
---|---  
(none)| Sender ID, E.164, or From field  
`name:`| Sender display name  
`username:`| Sender username  
`tag:`| Sender tag  
`id:`, `from:`, `e164:`| Explicit identity targeting  
  
## 

​

What elevated does not control

  * **Tool policy** : if `exec` is denied by tool policy, elevated cannot override it
  * **Separate from`/exec`**: the `/exec` directive adjusts per-session exec defaults for authorized senders and does not require elevated mode


## 

​

Related

  * [Exec tool](</tools/exec>) — shell command execution
  * [Exec approvals](</tools/exec-approvals>) — approval and allowlist system
  * [Sandboxing](</gateway/sandboxing>) — sandbox configuration
  * [Sandbox vs Tool Policy vs Elevated](</gateway/sandbox-vs-tool-policy-vs-elevated>)


[Diffs](</tools/diffs>)[Exec Tool](</tools/exec>)

⌘I