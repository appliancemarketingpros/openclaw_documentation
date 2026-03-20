---
title: hooks
source_url: https://docs.openclaw.ai/cli/hooks
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

hooks

# 

​

`openclaw hooks`

Manage agent hooks (event-driven automations for commands like `/new`, `/reset`, and gateway startup). Related:

  * Hooks: [Hooks](</automation/hooks>)
  * Plugin hooks: [Plugin hooks](</plugins/architecture#provider-runtime-hooks>)


## 

​

List All Hooks

Copy
[code]
    openclaw hooks list
    
[/code]

List all discovered hooks from workspace, managed, and bundled directories. **Options:**

  * `--eligible`: Show only eligible hooks (requirements met)
  * `--json`: Output as JSON
  * `-v, --verbose`: Show detailed information including missing requirements

**Example output:**

Copy
[code]
    Hooks (4/4 ready)
    
    Ready:
      🚀 boot-md ✓ - Run BOOT.md on gateway startup
      📎 bootstrap-extra-files ✓ - Inject extra workspace bootstrap files during agent bootstrap
      📝 command-logger ✓ - Log all command events to a centralized audit file
      💾 session-memory ✓ - Save session context to memory when /new command is issued
    
[/code]

**Example (verbose):**

Copy
[code]
    openclaw hooks list --verbose
    
[/code]

Shows missing requirements for ineligible hooks. **Example (JSON):**

Copy
[code]
    openclaw hooks list --json
    
[/code]

Returns structured JSON for programmatic use.

## 

​

Get Hook Information

Copy
[code]
    openclaw hooks info <name>
    
[/code]

Show detailed information about a specific hook. **Arguments:**

  * `<name>`: Hook name (e.g., `session-memory`)

**Options:**

  * `--json`: Output as JSON

**Example:**

Copy
[code]
    openclaw hooks info session-memory
    
[/code]

**Output:**

Copy
[code]
    💾 session-memory ✓ Ready
    
    Save session context to memory when /new command is issued
    
    Details:
      Source: openclaw-bundled
      Path: /path/to/openclaw/hooks/bundled/session-memory/HOOK.md
      Handler: /path/to/openclaw/hooks/bundled/session-memory/handler.ts
      Homepage: https://docs.openclaw.ai/automation/hooks#session-memory
      Events: command:new
    
    Requirements:
      Config: ✓ workspace.dir
    
[/code]

## 

​

Check Hooks Eligibility

Copy
[code]
    openclaw hooks check
    
[/code]

Show summary of hook eligibility status (how many are ready vs. not ready). **Options:**

  * `--json`: Output as JSON

**Example output:**

Copy
[code]
    Hooks Status
    
    Total hooks: 4
    Ready: 4
    Not ready: 0
    
[/code]

## 

​

Enable a Hook

Copy
[code]
    openclaw hooks enable <name>
    
[/code]

Enable a specific hook by adding it to your config (`~/.openclaw/config.json`). **Note:** Hooks managed by plugins show `plugin:<id>` in `openclaw hooks list` and can’t be enabled/disabled here. Enable/disable the plugin instead. **Arguments:**

  * `<name>`: Hook name (e.g., `session-memory`)

**Example:**

Copy
[code]
    openclaw hooks enable session-memory
    
[/code]

**Output:**

Copy
[code]
    ✓ Enabled hook: 💾 session-memory
    
[/code]

**What it does:**

  * Checks if hook exists and is eligible
  * Updates `hooks.internal.entries.<name>.enabled = true` in your config
  * Saves config to disk

**After enabling:**

  * Restart the gateway so hooks reload (menu bar app restart on macOS, or restart your gateway process in dev).


## 

​

Disable a Hook

Copy
[code]
    openclaw hooks disable <name>
    
[/code]

Disable a specific hook by updating your config. **Arguments:**

  * `<name>`: Hook name (e.g., `command-logger`)

**Example:**

Copy
[code]
    openclaw hooks disable command-logger
    
[/code]

**Output:**

Copy
[code]
    ⏸ Disabled hook: 📝 command-logger
    
[/code]

**After disabling:**

  * Restart the gateway so hooks reload


## 

​

Install Hooks

Copy
[code]
    openclaw hooks install <path-or-spec>
    openclaw hooks install <npm-spec> --pin
    
[/code]

Install a hook pack from a local folder/archive or npm. Npm specs are **registry-only** (package name + optional **exact version** or **dist-tag**). Git/URL/file specs and semver ranges are rejected. Dependency installs run with `--ignore-scripts` for safety. Bare specs and `@latest` stay on the stable track. If npm resolves either of those to a prerelease, OpenClaw stops and asks you to opt in explicitly with a prerelease tag such as `@beta`/`@rc` or an exact prerelease version. **What it does:**

  * Copies the hook pack into `~/.openclaw/hooks/<id>`
  * Enables the installed hooks in `hooks.internal.entries.*`
  * Records the install under `hooks.internal.installs`

**Options:**

  * `-l, --link`: Link a local directory instead of copying (adds it to `hooks.internal.load.extraDirs`)
  * `--pin`: Record npm installs as exact resolved `name@version` in `hooks.internal.installs`

**Supported archives:** `.zip`, `.tgz`, `.tar.gz`, `.tar` **Examples:**

Copy
[code]
    # Local directory
    openclaw hooks install ./my-hook-pack
    
    # Local archive
    openclaw hooks install ./my-hook-pack.zip
    
    # NPM package
    openclaw hooks install @openclaw/my-hook-pack
    
    # Link a local directory without copying
    openclaw hooks install -l ./my-hook-pack
    
[/code]

## 

​

Update Hooks

Copy
[code]
    openclaw hooks update <id>
    openclaw hooks update --all
    
[/code]

Update installed hook packs (npm installs only). **Options:**

  * `--all`: Update all tracked hook packs
  * `--dry-run`: Show what would change without writing

When a stored integrity hash exists and the fetched artifact hash changes, OpenClaw prints a warning and asks for confirmation before proceeding. Use global `--yes` to bypass prompts in CI/non-interactive runs.

## 

​

Bundled Hooks

### 

​

session-memory

Saves session context to memory when you issue `/new`. **Enable:**

Copy
[code]
    openclaw hooks enable session-memory
    
[/code]

**Output:** `~/.openclaw/workspace/memory/YYYY-MM-DD-slug.md` **See:** [session-memory documentation](</automation/hooks#session-memory>)

### 

​

bootstrap-extra-files

Injects additional bootstrap files (for example monorepo-local `AGENTS.md` / `TOOLS.md`) during `agent:bootstrap`. **Enable:**

Copy
[code]
    openclaw hooks enable bootstrap-extra-files
    
[/code]

**See:** [bootstrap-extra-files documentation](</automation/hooks#bootstrap-extra-files>)

### 

​

command-logger

Logs all command events to a centralized audit file. **Enable:**

Copy
[code]
    openclaw hooks enable command-logger
    
[/code]

**Output:** `~/.openclaw/logs/commands.log` **View logs:**

Copy
[code]
    # Recent commands
    tail -n 20 ~/.openclaw/logs/commands.log
    
    # Pretty-print
    cat ~/.openclaw/logs/commands.log | jq .
    
    # Filter by action
    grep '"action":"new"' ~/.openclaw/logs/commands.log | jq .
    
[/code]

**See:** [command-logger documentation](</automation/hooks#command-logger>)

### 

​

boot-md

Runs `BOOT.md` when the gateway starts (after channels start). **Events** : `gateway:startup` **Enable** :

Copy
[code]
    openclaw hooks enable boot-md
    
[/code]

**See:** [boot-md documentation](</automation/hooks#boot-md>)

[agents](</cli/agents>)[memory](</cli/memory>)

⌘I