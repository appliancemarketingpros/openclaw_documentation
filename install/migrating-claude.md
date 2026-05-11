---
title: Migrating from Claude
source_url: https://docs.openclaw.ai/install/migrating-claude
scraped_at: 2026-05-11
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Migrating

Migrating from Claude

> ## Documentation Index
> 
> Fetch the complete documentation index at: <https://docs.openclaw.ai/llms.txt>
> 
> Use this file to discover all available pages before exploring further.

OpenClaw imports local Claude state through the bundled Claude migration provider. The provider previews every item before changing state, redacts secrets in plans and reports, and creates a verified backup before apply.

Onboarding imports require a fresh OpenClaw setup. If you already have local OpenClaw state, reset config, credentials, sessions, and the workspace first, or use `openclaw migrate` directly with `--overwrite` after reviewing the plan.

## 

​

Two ways to import

  * Onboarding wizard

  * CLI


The wizard offers Claude when it detects local Claude state.
[code]
    openclaw onboard --flow import
    
[/code]

Or point at a specific source:
[code]
    openclaw onboard --import-from claude --import-source ~/.claude
    
[/code]

Use `openclaw migrate` for scripted or repeatable runs. See [`openclaw migrate`](</cli/migrate>) for the full reference.
[code]
    openclaw migrate claude --dry-run
    openclaw migrate apply claude --yes
    
[/code]

Add `--from <path>` to import a specific Claude Code home or project root.

## 

​

What gets imported

Instructions and memory

  * Project `CLAUDE.md` and `.claude/CLAUDE.md` content is copied or appended into the OpenClaw agent workspace `AGENTS.md`.
  * User `~/.claude/CLAUDE.md` content is appended into workspace `USER.md`.


MCP servers

MCP server definitions are imported from project `.mcp.json`, Claude Code `~/.claude.json`, and Claude Desktop `claude_desktop_config.json` when present.

Skills and commands

  * Claude skills with a `SKILL.md` file are copied into the OpenClaw workspace skills directory.
  * Claude command Markdown files under `.claude/commands/` or `~/.claude/commands/` are converted into OpenClaw skills with `disable-model-invocation: true`.


## 

​

What stays archive-only

The provider copies these into the migration report for manual review, but does **not** load them into live OpenClaw config:

  * Claude hooks
  * Claude permissions and broad tool allowlists
  * Claude environment defaults
  * `CLAUDE.local.md`
  * `.claude/rules/`
  * Claude subagents under `.claude/agents/` or `~/.claude/agents/`
  * Claude Code caches, plans, and project history directories
  * Claude Desktop extensions and OS-stored credentials

OpenClaw refuses to execute hooks, trust permission allowlists, or decode opaque OAuth and Desktop credential state automatically. Move what you need by hand after reviewing the archive.

## 

​

Source selection

Without `--from`, OpenClaw inspects the default Claude Code home at `~/.claude`, the sampled Claude Code `~/.claude.json` state file, and the Claude Desktop MCP config on macOS. When `--from` points at a project root, OpenClaw imports only that project’s Claude files such as `CLAUDE.md`, `.claude/settings.json`, `.claude/commands/`, `.claude/skills/`, and `.mcp.json`. It does not read your global Claude home during a project-root import.

## 

​

Recommended flow

1

Preview the plan
[code]
    openclaw migrate claude --dry-run
    
[/code]

The plan lists everything that will change, including conflicts, skipped items, and sensitive values redacted from nested MCP `env` or `headers` fields.

2

Apply with backup
[code]
    openclaw migrate apply claude --yes
    
[/code]

OpenClaw creates and verifies a backup before applying.

3

Run doctor
[code]
    openclaw doctor
    
[/code]

[Doctor](</gateway/doctor>) checks for config or state issues after the import.

4

Restart and verify
[code]
    openclaw gateway restart
    openclaw status
    
[/code]

Confirm the gateway is healthy and your imported instructions, MCP servers, and skills are loaded.

## 

​

Conflict handling

Apply refuses to continue when the plan reports conflicts (a file or config value already exists at the target).

Rerun with `--overwrite` only when replacing the existing target is intentional. Providers may still write item-level backups for overwritten files in the migration report directory.

For a fresh OpenClaw install, conflicts are unusual. They typically appear when you re-run the import on a setup that already has user edits.

## 

​

JSON output for automation
[code] 
    openclaw migrate claude --dry-run --json
    openclaw migrate apply claude --json --yes
    
[/code]

With `--json` and no `--yes`, apply prints the plan and does not mutate state. This is the safest mode for CI and shared scripts.

## 

​

Troubleshooting

Claude state lives outside ~/.claude

Pass `--from /actual/path` (CLI) or `--import-source /actual/path` (onboarding).

Onboarding refuses to import on an existing setup

Onboarding imports require a fresh setup. Either reset state and re-onboard, or use `openclaw migrate apply claude` directly, which supports `--overwrite` and explicit backup control.

MCP servers from Claude Desktop did not import

Claude Desktop reads `claude_desktop_config.json` from a platform-specific path. Point `--from` at that file’s directory if OpenClaw did not detect it automatically.

Claude commands became skills with model invocation disabled

By design. Claude commands are user-triggered, so OpenClaw imports them as skills with `disable-model-invocation: true`. Edit each skill’s frontmatter if you want the agent to invoke them automatically.

## 

​

Related

  * [`openclaw migrate`](</cli/migrate>): full CLI reference, plugin contract, and JSON shapes.
  * [Migration guide](</install/migrating>): all migration paths.
  * [Migrating from Hermes](</install/migrating-hermes>): the other cross-system import path.
  * [Onboarding](</cli/onboard>): wizard flow and non-interactive flags.
  * [Doctor](</gateway/doctor>): post-migration health check.
  * [Agent workspace](</concepts/agent-workspace>): where `AGENTS.md`, `USER.md`, and skills live.


[Migration guide](</install/migrating>)[Migrating from Hermes](</install/migrating-hermes>)

⌘I