---
title: Configuration
source_url: https://docs.openclaw.ai/gateway/configuration
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Configuration and operations

Configuration

# 

​

Configuration

OpenClaw reads an optional **JSON5** config from `~/.openclaw/openclaw.json`. If the file is missing, OpenClaw uses safe defaults. Common reasons to add a config:

  * Connect channels and control who can message the bot
  * Set models, tools, sandboxing, or automation (cron, hooks)
  * Tune sessions, media, networking, or UI

See the [full reference](</gateway/configuration-reference>) for every available field.

**New to configuration?** Start with `openclaw onboard` for interactive setup, or check out the [Configuration Examples](</gateway/configuration-examples>) guide for complete copy-paste configs.

## 

​

Minimal config

Copy
[code]
    // ~/.openclaw/openclaw.json
    {
      agents: { defaults: { workspace: "~/.openclaw/workspace" } },
      channels: { whatsapp: { allowFrom: ["+15555550123"] } },
    }
    
[/code]

## 

​

Editing config

  * Interactive wizard

  * CLI (one-liners)

  * Control UI

  * Direct edit


Copy
[code]
    openclaw onboard       # full onboarding flow
    openclaw configure     # config wizard
    
[/code]

Copy
[code]
    openclaw config get agents.defaults.workspace
    openclaw config set agents.defaults.heartbeat.every "2h"
    openclaw config unset plugins.entries.brave.config.webSearch.apiKey
    
[/code]

Open <http://127.0.0.1:18789> and use the **Config** tab. The Control UI renders a form from the config schema, with a **Raw JSON** editor as an escape hatch.

Edit `~/.openclaw/openclaw.json` directly. The Gateway watches the file and applies changes automatically (see hot reload).

## 

​

Strict validation

OpenClaw only accepts configurations that fully match the schema. Unknown keys, malformed types, or invalid values cause the Gateway to **refuse to start**. The only root-level exception is `$schema` (string), so editors can attach JSON Schema metadata.

When validation fails:

  * The Gateway does not boot
  * Only diagnostic commands work (`openclaw doctor`, `openclaw logs`, `openclaw health`, `openclaw status`)
  * Run `openclaw doctor` to see exact issues
  * Run `openclaw doctor --fix` (or `--yes`) to apply repairs


## 

​

Common tasks

Set up a channel (WhatsApp, Telegram, Discord, etc.)

Each channel has its own config section under `channels.<provider>`. See the dedicated channel page for setup steps:

  * [WhatsApp](</channels/whatsapp>) — `channels.whatsapp`
  * [Telegram](</channels/telegram>) — `channels.telegram`
  * [Discord](</channels/discord>) — `channels.discord`
  * [Slack](</channels/slack>) — `channels.slack`
  * [Signal](</channels/signal>) — `channels.signal`
  * [iMessage](</channels/imessage>) — `channels.imessage`
  * [Google Chat](</channels/googlechat>) — `channels.googlechat`
  * [Mattermost](</channels/mattermost>) — `channels.mattermost`
  * [Microsoft Teams](</channels/msteams>) — `channels.msteams`

All channels share the same DM policy pattern:

Copy
[code]
    {
      channels: {
        telegram: {
          enabled: true,
          botToken: "123:abc",
          dmPolicy: "pairing",   // pairing | allowlist | open | disabled
          allowFrom: ["tg:123"], // only for allowlist/open
        },
      },
    }
    
[/code]

Choose and configure models

Set the primary model and optional fallbacks:

Copy
[code]
    {
      agents: {
        defaults: {
          model: {
            primary: "anthropic/claude-sonnet-4-6",
            fallbacks: ["openai/gpt-5.2"],
          },
          models: {
            "anthropic/claude-sonnet-4-6": { alias: "Sonnet" },
            "openai/gpt-5.2": { alias: "GPT" },
          },
        },
      },
    }
    
[/code]

  * `agents.defaults.models` defines the model catalog and acts as the allowlist for `/model`.
  * Model refs use `provider/model` format (e.g. `anthropic/claude-opus-4-6`).
  * `agents.defaults.imageMaxDimensionPx` controls transcript/tool image downscaling (default `1200`); lower values usually reduce vision-token usage on screenshot-heavy runs.
  * See [Models CLI](</concepts/models>) for switching models in chat and [Model Failover](</concepts/model-failover>) for auth rotation and fallback behavior.
  * For custom/self-hosted providers, see [Custom providers](</gateway/configuration-reference#custom-providers-and-base-urls>) in the reference.


Control who can message the bot

DM access is controlled per channel via `dmPolicy`:

  * `"pairing"` (default): unknown senders get a one-time pairing code to approve
  * `"allowlist"`: only senders in `allowFrom` (or the paired allow store)
  * `"open"`: allow all inbound DMs (requires `allowFrom: ["*"]`)
  * `"disabled"`: ignore all DMs

For groups, use `groupPolicy` \+ `groupAllowFrom` or channel-specific allowlists.See the [full reference](</gateway/configuration-reference#dm-and-group-access>) for per-channel details.

Set up group chat mention gating

Group messages default to **require mention**. Configure patterns per agent:

Copy
[code]
    {
      agents: {
        list: [
          {
            id: "main",
            groupChat: {
              mentionPatterns: ["@openclaw", "openclaw"],
            },
          },
        ],
      },
      channels: {
        whatsapp: {
          groups: { "*": { requireMention: true } },
        },
      },
    }
    
[/code]

  * **Metadata mentions** : native @-mentions (WhatsApp tap-to-mention, Telegram @bot, etc.)
  * **Text patterns** : safe regex patterns in `mentionPatterns`
  * See [full reference](</gateway/configuration-reference#group-chat-mention-gating>) for per-channel overrides and self-chat mode.


Tune gateway channel health monitoring

Control how aggressively the gateway restarts channels that look stale:

Copy
[code]
    {
      gateway: {
        channelHealthCheckMinutes: 5,
        channelStaleEventThresholdMinutes: 30,
        channelMaxRestartsPerHour: 10,
      },
      channels: {
        telegram: {
          healthMonitor: { enabled: false },
          accounts: {
            alerts: {
              healthMonitor: { enabled: true },
            },
          },
        },
      },
    }
    
[/code]

  * Set `gateway.channelHealthCheckMinutes: 0` to disable health-monitor restarts globally.
  * `channelStaleEventThresholdMinutes` should be greater than or equal to the check interval.
  * Use `channels.<provider>.healthMonitor.enabled` or `channels.<provider>.accounts.<id>.healthMonitor.enabled` to disable auto-restarts for one channel or account without disabling the global monitor.
  * See [Health Checks](</gateway/health>) for operational debugging and the [full reference](</gateway/configuration-reference#gateway>) for all fields.


Configure sessions and resets

Sessions control conversation continuity and isolation:

Copy
[code]
    {
      session: {
        dmScope: "per-channel-peer",  // recommended for multi-user
        threadBindings: {
          enabled: true,
          idleHours: 24,
          maxAgeHours: 0,
        },
        reset: {
          mode: "daily",
          atHour: 4,
          idleMinutes: 120,
        },
      },
    }
    
[/code]

  * `dmScope`: `main` (shared) | `per-peer` | `per-channel-peer` | `per-account-channel-peer`
  * `threadBindings`: global defaults for thread-bound session routing (Discord supports `/focus`, `/unfocus`, `/agents`, `/session idle`, and `/session max-age`).
  * See [Session Management](</concepts/session>) for scoping, identity links, and send policy.
  * See [full reference](</gateway/configuration-reference#session>) for all fields.


Enable sandboxing

Run agent sessions in isolated Docker containers:

Copy
[code]
    {
      agents: {
        defaults: {
          sandbox: {
            mode: "non-main",  // off | non-main | all
            scope: "agent",    // session | agent | shared
          },
        },
      },
    }
    
[/code]

Build the image first: `scripts/sandbox-setup.sh`See [Sandboxing](</gateway/sandboxing>) for the full guide and [full reference](</gateway/configuration-reference#agents-defaults-sandbox>) for all options.

Enable relay-backed push for official iOS builds

Relay-backed push is configured in `openclaw.json`.Set this in gateway config:

Copy
[code]
    {
      gateway: {
        push: {
          apns: {
            relay: {
              baseUrl: "https://relay.example.com",
              // Optional. Default: 10000
              timeoutMs: 10000,
            },
          },
        },
      },
    }
    
[/code]

CLI equivalent:

Copy
[code]
    openclaw config set gateway.push.apns.relay.baseUrl https://relay.example.com
    
[/code]

What this does:

  * Lets the gateway send `push.test`, wake nudges, and reconnect wakes through the external relay.
  * Uses a registration-scoped send grant forwarded by the paired iOS app. The gateway does not need a deployment-wide relay token.
  * Binds each relay-backed registration to the gateway identity that the iOS app paired with, so another gateway cannot reuse the stored registration.
  * Keeps local/manual iOS builds on direct APNs. Relay-backed sends apply only to official distributed builds that registered through the relay.
  * Must match the relay base URL baked into the official/TestFlight iOS build, so registration and send traffic reach the same relay deployment.

End-to-end flow:

  1. Install an official/TestFlight iOS build that was compiled with the same relay base URL.
  2. Configure `gateway.push.apns.relay.baseUrl` on the gateway.
  3. Pair the iOS app to the gateway and let both node and operator sessions connect.
  4. The iOS app fetches the gateway identity, registers with the relay using App Attest plus the app receipt, and then publishes the relay-backed `push.apns.register` payload to the paired gateway.
  5. The gateway stores the relay handle and send grant, then uses them for `push.test`, wake nudges, and reconnect wakes.

Operational notes:

  * If you switch the iOS app to a different gateway, reconnect the app so it can publish a new relay registration bound to that gateway.
  * If you ship a new iOS build that points at a different relay deployment, the app refreshes its cached relay registration instead of reusing the old relay origin.

Compatibility note:

  * `OPENCLAW_APNS_RELAY_BASE_URL` and `OPENCLAW_APNS_RELAY_TIMEOUT_MS` still work as temporary env overrides.
  * `OPENCLAW_APNS_RELAY_ALLOW_HTTP=true` remains a loopback-only development escape hatch; do not persist HTTP relay URLs in config.

See [iOS App](</platforms/ios#relay-backed-push-for-official-builds>) for the end-to-end flow and [Authentication and trust flow](</platforms/ios#authentication-and-trust-flow>) for the relay security model.

Set up heartbeat (periodic check-ins)

Copy
[code]
    {
      agents: {
        defaults: {
          heartbeat: {
            every: "30m",
            target: "last",
          },
        },
      },
    }
    
[/code]

  * `every`: duration string (`30m`, `2h`). Set `0m` to disable.
  * `target`: `last` | `whatsapp` | `telegram` | `discord` | `none`
  * `directPolicy`: `allow` (default) or `block` for DM-style heartbeat targets
  * See [Heartbeat](</gateway/heartbeat>) for the full guide.


Configure cron jobs

Copy
[code]
    {
      cron: {
        enabled: true,
        maxConcurrentRuns: 2,
        sessionRetention: "24h",
        runLog: {
          maxBytes: "2mb",
          keepLines: 2000,
        },
      },
    }
    
[/code]

  * `sessionRetention`: prune completed isolated run sessions from `sessions.json` (default `24h`; set `false` to disable).
  * `runLog`: prune `cron/runs/<jobId>.jsonl` by size and retained lines.
  * See [Cron jobs](</automation/cron-jobs>) for feature overview and CLI examples.


Set up webhooks (hooks)

Enable HTTP webhook endpoints on the Gateway:

Copy
[code]
    {
      hooks: {
        enabled: true,
        token: "shared-secret",
        path: "/hooks",
        defaultSessionKey: "hook:ingress",
        allowRequestSessionKey: false,
        allowedSessionKeyPrefixes: ["hook:"],
        mappings: [
          {
            match: { path: "gmail" },
            action: "agent",
            agentId: "main",
            deliver: true,
          },
        ],
      },
    }
    
[/code]

Security note:

  * Treat all hook/webhook payload content as untrusted input.
  * Keep unsafe-content bypass flags disabled (`hooks.gmail.allowUnsafeExternalContent`, `hooks.mappings[].allowUnsafeExternalContent`) unless doing tightly scoped debugging.
  * For hook-driven agents, prefer strong modern model tiers and strict tool policy (for example messaging-only plus sandboxing where possible).

See [full reference](</gateway/configuration-reference#hooks>) for all mapping options and Gmail integration.

Configure multi-agent routing

Run multiple isolated agents with separate workspaces and sessions:

Copy
[code]
    {
      agents: {
        list: [
          { id: "home", default: true, workspace: "~/.openclaw/workspace-home" },
          { id: "work", workspace: "~/.openclaw/workspace-work" },
        ],
      },
      bindings: [
        { agentId: "home", match: { channel: "whatsapp", accountId: "personal" } },
        { agentId: "work", match: { channel: "whatsapp", accountId: "biz" } },
      ],
    }
    
[/code]

See [Multi-Agent](</concepts/multi-agent>) and [full reference](</gateway/configuration-reference#multi-agent-routing>) for binding rules and per-agent access profiles.

Split config into multiple files ($include)

Use `$include` to organize large configs:

Copy
[code]
    // ~/.openclaw/openclaw.json
    {
      gateway: { port: 18789 },
      agents: { $include: "./agents.json5" },
      broadcast: {
        $include: ["./clients/a.json5", "./clients/b.json5"],
      },
    }
    
[/code]

  * **Single file** : replaces the containing object
  * **Array of files** : deep-merged in order (later wins)
  * **Sibling keys** : merged after includes (override included values)
  * **Nested includes** : supported up to 10 levels deep
  * **Relative paths** : resolved relative to the including file
  * **Error handling** : clear errors for missing files, parse errors, and circular includes


## 

​

Config hot reload

The Gateway watches `~/.openclaw/openclaw.json` and applies changes automatically — no manual restart needed for most settings.

### 

​

Reload modes

Mode| Behavior  
---|---  
**`hybrid`** (default)| Hot-applies safe changes instantly. Automatically restarts for critical ones.  
**`hot`**|  Hot-applies safe changes only. Logs a warning when a restart is needed — you handle it.  
**`restart`**|  Restarts the Gateway on any config change, safe or not.  
**`off`**|  Disables file watching. Changes take effect on the next manual restart.  
  
Copy
[code]
    {
      gateway: {
        reload: { mode: "hybrid", debounceMs: 300 },
      },
    }
    
[/code]

### 

​

What hot-applies vs what needs a restart

Most fields hot-apply without downtime. In `hybrid` mode, restart-required changes are handled automatically.

Category| Fields| Restart needed?  
---|---|---  
Channels| `channels.*`, `web` (WhatsApp) — all built-in and extension channels| No  
Agent & models| `agent`, `agents`, `models`, `routing`| No  
Automation| `hooks`, `cron`, `agent.heartbeat`| No  
Sessions & messages| `session`, `messages`| No  
Tools & media| `tools`, `browser`, `skills`, `audio`, `talk`| No  
UI & misc| `ui`, `logging`, `identity`, `bindings`| No  
Gateway server| `gateway.*` (port, bind, auth, tailscale, TLS, HTTP)| **Yes**  
Infrastructure| `discovery`, `canvasHost`, `plugins`| **Yes**  
  
`gateway.reload` and `gateway.remote` are exceptions — changing them does **not** trigger a restart.

## 

​

Config RPC (programmatic updates)

Control-plane write RPCs (`config.apply`, `config.patch`, `update.run`) are rate-limited to **3 requests per 60 seconds** per `deviceId+clientIp`. When limited, the RPC returns `UNAVAILABLE` with `retryAfterMs`.

config.apply (full replace)

Validates + writes the full config and restarts the Gateway in one step.

`config.apply` replaces the **entire config**. Use `config.patch` for partial updates, or `openclaw config set` for single keys.

Params:

  * `raw` (string) — JSON5 payload for the entire config
  * `baseHash` (optional) — config hash from `config.get` (required when config exists)
  * `sessionKey` (optional) — session key for the post-restart wake-up ping
  * `note` (optional) — note for the restart sentinel
  * `restartDelayMs` (optional) — delay before restart (default 2000)

Restart requests are coalesced while one is already pending/in-flight, and a 30-second cooldown applies between restart cycles.

Copy
[code]
    openclaw gateway call config.get --params '{}'  # capture payload.hash
    openclaw gateway call config.apply --params '{
      "raw": "{ agents: { defaults: { workspace: \"~/.openclaw/workspace\" } } }",
      "baseHash": "<hash>",
      "sessionKey": "agent:main:whatsapp:direct:+15555550123"
    }'
    
[/code]

config.patch (partial update)

Merges a partial update into the existing config (JSON merge patch semantics):

  * Objects merge recursively
  * `null` deletes a key
  * Arrays replace

Params:

  * `raw` (string) — JSON5 with just the keys to change
  * `baseHash` (required) — config hash from `config.get`
  * `sessionKey`, `note`, `restartDelayMs` — same as `config.apply`

Restart behavior matches `config.apply`: coalesced pending restarts plus a 30-second cooldown between restart cycles.

Copy
[code]
    openclaw gateway call config.patch --params '{
      "raw": "{ channels: { telegram: { groups: { \"*\": { requireMention: false } } } } }",
      "baseHash": "<hash>"
    }'
    
[/code]

## 

​

Environment variables

OpenClaw reads env vars from the parent process plus:

  * `.env` from the current working directory (if present)
  * `~/.openclaw/.env` (global fallback)

Neither file overrides existing env vars. You can also set inline env vars in config:

Copy
[code]
    {
      env: {
        OPENROUTER_API_KEY: "sk-or-...",
        vars: { GROQ_API_KEY: "gsk-..." },
      },
    }
    
[/code]

Shell env import (optional)

If enabled and expected keys aren’t set, OpenClaw runs your login shell and imports only the missing keys:

Copy
[code]
    {
      env: {
        shellEnv: { enabled: true, timeoutMs: 15000 },
      },
    }
    
[/code]

Env var equivalent: `OPENCLAW_LOAD_SHELL_ENV=1`

Env var substitution in config values

Reference env vars in any config string value with `${VAR_NAME}`:

Copy
[code]
    {
      gateway: { auth: { token: "${OPENCLAW_GATEWAY_TOKEN}" } },
      models: { providers: { custom: { apiKey: "${CUSTOM_API_KEY}" } } },
    }
    
[/code]

Rules:

  * Only uppercase names matched: `[A-Z_][A-Z0-9_]*`
  * Missing/empty vars throw an error at load time
  * Escape with `$${VAR}` for literal output
  * Works inside `$include` files
  * Inline substitution: `"${BASE}/v1"` → `"https://api.example.com/v1"`


Secret refs (env, file, exec)

For fields that support SecretRef objects, you can use:

Copy
[code]
    {
      models: {
        providers: {
          openai: { apiKey: { source: "env", provider: "default", id: "OPENAI_API_KEY" } },
        },
      },
      skills: {
        entries: {
          "image-lab": {
            apiKey: {
              source: "file",
              provider: "filemain",
              id: "/skills/entries/image-lab/apiKey",
            },
          },
        },
      },
      channels: {
        googlechat: {
          serviceAccountRef: {
            source: "exec",
            provider: "vault",
            id: "channels/googlechat/serviceAccount",
          },
        },
      },
    }
    
[/code]

SecretRef details (including `secrets.providers` for `env`/`file`/`exec`) are in [Secrets Management](</gateway/secrets>). Supported credential paths are listed in [SecretRef Credential Surface](</reference/secretref-credential-surface>).

See [Environment](</help/environment>) for full precedence and sources.

## 

​

Full reference

For the complete field-by-field reference, see **[Configuration Reference](</gateway/configuration-reference>)**.

* * *

_Related:[Configuration Examples](</gateway/configuration-examples>) · [Configuration Reference](</gateway/configuration-reference>) · [Doctor](</gateway/doctor>)_

[Gateway Runbook](</gateway>)[Configuration Reference](</gateway/configuration-reference>)

⌘I