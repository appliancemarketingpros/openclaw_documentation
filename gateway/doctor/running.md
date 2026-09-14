---
title: Run doctor
source_url: https://docs.openclaw.ai/gateway/doctor/running
scraped_at: 2026-09-14
---

Gateway & OpsGateway

Run `openclaw doctor` to repair and migrate an OpenClaw install. This page covers the command, its automation flags, and the read-only lint mode.

## Quick start

bashCopy code
[code]
    openclaw doctor
[/code]

### Headless and automation modes

### \--yes

bashCopy code
[code]
    openclaw doctor --yes
[/code]

Accept default non-service repairs without prompting and enter maintenance while preserving the installed gateway service definition.

### \--fix

bashCopy code
[code]
    openclaw doctor --fix
[/code]

Apply recommended non-service repairs without prompting (`--repair` is an alias) and enter maintenance while preserving the installed gateway service definition.

### \--lint

bashCopy code
[code]
    openclaw doctor --lintopenclaw doctor --lint --json
[/code]

Run structured health checks for CI or preflight automation. Read-only: no prompts, repairs, migrations, restarts, or state writes.

### \--fix --force

bashCopy code
[code]
    openclaw doctor --fix --force
[/code]

Apply aggressive config/state repairs too. Repair maintenance preserves the installed service definition; use `openclaw gateway install --force` from the intended installation to replace its launcher and managed environment.

### \--non-interactive

bashCopy code
[code]
    openclaw doctor --non-interactive
[/code]

Run without prompts, applying only safe migrations (config normalization + on-disk state moves). Skips restart/service/sandbox actions that need human confirmation. Legacy state migrations still run automatically when detected. Add `--fix` for all supported startup-blocking repairs without prompts, including workspace setup, session stores, exec approvals, and audit schema migrations. Explicit repair checks ownership before database snapshots; another live owner must stop before repair can proceed. Malformed or conflicting retained files require the manual recovery named in the error.

### \--deep

bashCopy code
[code]
    openclaw doctor --deep
[/code]

Scan system services for extra gateway installs (launchd/systemd/schtasks).

To review changes before writing, open the config file first:

bashCopy code
[code]
    cat ~/.openclaw/openclaw.json
[/code]

## Read-only lint mode

`openclaw doctor --lint` is the automation-friendly sibling of `openclaw doctor --fix`. They share the same Doctor rule registry, but they do not select or act on rules in the same way:

Mode | Prompts | Writes config/state | Output | Use it for  
---|---|---|---|---  
`openclaw doctor` | yes | yes, safe migrations and confirmed repairs | friendly health report | guided checks and repairs  
`openclaw doctor --json` | no | no | JSON advisory report | machine-readable operator checks  
`openclaw doctor --fix` | sometimes | yes, with repair policy | friendly repair log | applying approved repairs  
`openclaw doctor --lint` | no | no | structured findings | CI, preflight, and review gates  
  
Default `doctor --lint` runs the broad-safe automation profile: checks that are static, local, and useful in CI or preflight output. It skips opt-in checks that are advisory, environment-sensitive, live-service dependent, account/workspace inventory, or historical cleanup. Use `doctor --lint --all` when you want the full registered lint audit, including those opt-in checks, or `--only <id>` for a targeted check.

`doctor --fix` does not use the lint default profile and does not accept `--all`. It runs Doctor's ordered repair path: modern health checks may provide an optional `repair()` implementation, and older areas still use their legacy Doctor repair flow. Some lint findings are intentionally diagnostic only, so a check appearing in `--lint --all` does not mean `--fix` will mutate that area. The contract separates `detect()` (reports findings) from `repair()` (reports changes/diffs/side effects), which keeps a path open for a future `doctor --fix --dry-run` without turning lint checks into mutation planners.

Some built-in checks are default-disabled internally so they stay available to `--all`, `--only`, and Doctor repair flows without becoming part of the default `doctor --lint` automation profile. Finding severity is still emitted per finding (`info`, `warning`, or `error`); default selection is not a severity level.

bashCopy code
[code]
    openclaw doctor --lintopenclaw doctor --lint --severity-min warningopenclaw doctor --lint --jsonopenclaw doctor --lint --allopenclaw doctor --lint --only core/doctor/gateway-config --json
[/code]

JSON output fields:

  * `ok`: whether any finding met the selected severity threshold
  * `checksRun` / `checksSkipped`: counts (skipped by profile, `--only`, or `--skip`)
  * `findings`: structured diagnostics with `checkId`, `severity`, `message`, and optional `path`, `line`, `column`, `ocPath`, `source`, `target`, `requirement`, `fixHint`


Exit codes:

Code | Meaning  
---|---  
`0` | no findings at or above the selected threshold  
`1` | one or more findings met the selected threshold  
`2` | command/runtime failure before findings could be emitted  
  
These threshold-based exit codes belong to explicit `--lint` mode, with or without `--json`. Bare `openclaw doctor --json` preserves ordinary Doctor's advisory exit `0` after producing its payload; machine consumers should read `ok` and `findings`. Fatal errors before output remain nonzero.

Flags:

  * `--severity-min info|warning|error` (default `warning`): controls both what prints and what causes a non-zero exit.
  * `--all`: runs every registered lint check, including opt-in checks excluded from the default automation set.
  * `--only <id>` (repeatable): run only the named check id(s); an unknown id is reported as an error finding.
  * `--skip <id>` (repeatable): exclude a check while keeping the rest of the run active.
  * `--severity-min`, `--all`, `--only`, and `--skip` require `--lint`. Bare `--json` is allowed for an advisory machine-readable report; `--fix` rejects it unless another machine mode owns the output.


Was this useful?YesNo

Open issue