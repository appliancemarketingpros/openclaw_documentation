---
title: Onboarding (CLI)
source_url: https://docs.openclaw.ai/start/wizard
scraped_at: 2026-06-02
---

CLI onboarding is the **recommended** way to set up OpenClaw on macOS, Linux, or Windows (via WSL2; strongly recommended). It configures a local Gateway or a remote Gateway connection, plus channels, skills, and workspace defaults in one guided flow.

bashCopy code
[code]
    openclaw onboard
[/code]

## Locale

The CLI wizard localizes fixed onboarding copy. It resolves locale from `OPENCLAW_LOCALE`, then `LC_ALL`, then `LC_MESSAGES`, then `LANG`, and falls back to English. Supported wizard locales are `en`, `zh-CN`, and `zh-TW`.

bashCopy code
[code]
    OPENCLAW_LOCALE=zh-CN openclaw onboard
[/code]

Names and stable identifiers stay literal: `OpenClaw`, `Gateway`, `Tailscale`, commands, config keys, URLs, provider IDs, model IDs, and plugin/channel labels are not translated.

To reconfigure later:

bashCopy code
[code]
    openclaw configureopenclaw agents add <name>
[/code]

## QuickStart vs Advanced

Onboarding starts with **QuickStart** (defaults) vs **Advanced** (full control).

### QuickStart (defaults)

  * Local gateway (loopback)
  * Workspace default (or existing workspace)
  * Gateway port **18789**
  * Gateway auth **Token** (auto-generated, even on loopback)
  * Tool policy default for new local setups: `tools.profile: "coding"` (existing explicit profile is preserved)
  * DM isolation default: local onboarding writes `session.dmScope: "per-channel-peer"` when unset. Details: [CLI Setup Reference](</start/wizard-cli-reference#outputs-and-internals>)
  * Tailscale exposure **Off**
  * Telegram + WhatsApp DMs default to **allowlist** (you'll be prompted for your phone number)


### Advanced (full control)

  * Exposes every step (mode, workspace, gateway, channels, daemon, skills).


## What onboarding configures

**Local mode (default)** walks you through these steps:

  1. **Model/Auth** — choose any supported provider/auth flow (API key, OAuth, or provider-specific manual auth), including Custom Provider (OpenAI-compatible, Anthropic-compatible, or Unknown auto-detect). Pick a default model. Security note: if this agent will run tools or process webhook/hooks content, prefer the strongest latest-generation model available and keep tool policy strict. Weaker/older tiers are easier to prompt-inject. For non-interactive runs, `--secret-input-mode ref` stores env-backed refs in auth profiles instead of plaintext API key values. In non-interactive `ref` mode, the provider env var must be set; passing inline key flags without that env var fails fast. In interactive runs, choosing secret reference mode lets you point at either an environment variable or a configured provider ref (`file` or `exec`), with a fast preflight validation before saving. For Anthropic, interactive onboarding/configure offers **Anthropic Claude CLI** as the preferred local path and **Anthropic API key** as the recommended production path. Anthropic setup-token also remains available as a supported token-auth path.
  2. **Workspace** — Location for agent files (default `~/.openclaw/workspace`). Seeds bootstrap files.
  3. **Gateway** — Port, bind address, auth mode, Tailscale exposure. In interactive token mode, choose default plaintext token storage or opt into SecretRef. Non-interactive token SecretRef path: `--gateway-token-ref-env &lt;ENV_VAR&gt;`.
  4. **Channels** — built-in and official plugin chat channels such as iMessage, Discord, Feishu, Google Chat, Mattermost, Microsoft Teams, QQ Bot, Signal, Slack, Telegram, WhatsApp, and more.
  5. **Daemon** — Installs a LaunchAgent (macOS), systemd user unit (Linux/WSL2), or native Windows Scheduled Task with per-user Startup-folder fallback. If token auth requires a token and `gateway.auth.token` is SecretRef-managed, daemon install validates it but does not persist the resolved token into supervisor service environment metadata. If token auth requires a token and the configured token SecretRef is unresolved, daemon install is blocked with actionable guidance. If both `gateway.auth.token` and `gateway.auth.password` are configured and `gateway.auth.mode` is unset, daemon install is blocked until mode is set explicitly.
  6. **Health check** — Starts the Gateway and verifies it's running.
  7. **Skills** — Installs recommended skills and optional dependencies.


**Remote mode** only configures the local client to connect to a Gateway elsewhere. It does **not** install or change anything on the remote host.

## Add another agent

Use `openclaw agents add <name>` to create a separate agent with its own workspace, sessions, and auth profiles. Running without `--workspace` launches onboarding.

What it sets:

  * `agents.list[].name`
  * `agents.list[].workspace`
  * `agents.list[].agentDir`


Notes:

  * Default workspaces follow `~/.openclaw/workspace-<agentId>`.
  * Add `bindings` to route inbound messages (onboarding can do this).
  * Non-interactive flags: `--model`, `--agent-dir`, `--bind`, `--non-interactive`.


## Full reference

For detailed step-by-step breakdowns and config outputs, see [CLI Setup Reference](</start/wizard-cli-reference>). For non-interactive examples, see [CLI Automation](</start/wizard-cli-automation>). For the deeper technical reference, including RPC details, see [Onboarding Reference](</reference/wizard>).

## Related docs

  * CLI command reference: [`openclaw onboard`](</cli/onboard>)
  * Onboarding overview: [Onboarding Overview](</start/onboarding-overview>)
  * macOS app onboarding: [Onboarding](</start/onboarding>)
  * Agent first-run ritual: [Agent Bootstrapping](</start/bootstrapping>)


Was this useful?YesNo