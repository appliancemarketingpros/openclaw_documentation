---
title: config
source_url: https://docs.openclaw.ai/cli/config
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Configuration

config

# 

​

`openclaw config`

Config helpers for non-interactive edits in `openclaw.json`: get/set/unset/validate values by path and print the active config file. Run without a subcommand to open the configure wizard (same as `openclaw configure`).

## 

​

Examples

Copy
[code]
    openclaw config file
    openclaw config get browser.executablePath
    openclaw config set browser.executablePath "/usr/bin/google-chrome"
    openclaw config set agents.defaults.heartbeat.every "2h"
    openclaw config set agents.list[0].tools.exec.node "node-id-or-name"
    openclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN
    openclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode json
    openclaw config unset plugins.entries.brave.config.webSearch.apiKey
    openclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-run
    openclaw config validate
    openclaw config validate --json
    
[/code]

## 

​

Paths

Paths use dot or bracket notation:

Copy
[code]
    openclaw config get agents.defaults.workspace
    openclaw config get agents.list[0].id
    
[/code]

Use the agent list index to target a specific agent:

Copy
[code]
    openclaw config get agents.list
    openclaw config set agents.list[1].tools.exec.node "node-id-or-name"
    
[/code]

## 

​

Values

Values are parsed as JSON5 when possible; otherwise they are treated as strings. Use `--strict-json` to require JSON5 parsing. `--json` remains supported as a legacy alias.

Copy
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"
    openclaw config set gateway.port 19001 --strict-json
    openclaw config set channels.whatsapp.groups '["*"]' --strict-json
    
[/code]

## 

​

`config set` modes

`openclaw config set` supports four assignment styles:

  1. Value mode: `openclaw config set <path> <value>`
  2. SecretRef builder mode:


Copy
[code]
    openclaw config set channels.discord.token \
      --ref-provider default \
      --ref-source env \
      --ref-id DISCORD_BOT_TOKEN
    
[/code]

  3. Provider builder mode (`secrets.providers.<alias>` path only):


Copy
[code]
    openclaw config set secrets.providers.vault \
      --provider-source exec \
      --provider-command /usr/local/bin/openclaw-vault \
      --provider-arg read \
      --provider-arg openai/api-key \
      --provider-timeout-ms 5000
    
[/code]

  4. Batch mode (`--batch-json` or `--batch-file`):


Copy
[code]
    openclaw config set --batch-json '[
      {
        "path": "secrets.providers.default",
        "provider": { "source": "env" }
      },
      {
        "path": "channels.discord.token",
        "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }
      }
    ]'
    
[/code]

Copy
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
    
[/code]

Batch parsing always uses the batch payload (`--batch-json`/`--batch-file`) as the source of truth. `--strict-json` / `--json` do not change batch parsing behavior. JSON path/value mode remains supported for both SecretRefs and providers:

Copy
[code]
    openclaw config set channels.discord.token \
      '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \
      --strict-json
    
    openclaw config set secrets.providers.vaultfile \
      '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \
      --strict-json
    
[/code]

## 

​

Provider Builder Flags

Provider builder targets must use `secrets.providers.<alias>` as the path. Common flags:

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>` (`file`, `exec`)

Env provider (`--provider-source env`):

  * `--provider-allowlist <ENV_VAR>` (repeatable)

File provider (`--provider-source file`):

  * `--provider-path <path>` (required)
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`

Exec provider (`--provider-source exec`):

  * `--provider-command <path>` (required)
  * `--provider-arg <arg>` (repeatable)
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env <KEY=VALUE>` (repeatable)
  * `--provider-pass-env <ENV_VAR>` (repeatable)
  * `--provider-trusted-dir <path>` (repeatable)
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`

Hardened exec provider example:

Copy
[code]
    openclaw config set secrets.providers.vault \
      --provider-source exec \
      --provider-command /usr/local/bin/openclaw-vault \
      --provider-arg read \
      --provider-arg openai/api-key \
      --provider-json-only \
      --provider-pass-env VAULT_TOKEN \
      --provider-trusted-dir /usr/local/bin \
      --provider-timeout-ms 5000
    
[/code]

## 

​

Dry run

Use `--dry-run` to validate changes without writing `openclaw.json`.

Copy
[code]
    openclaw config set channels.discord.token \
      --ref-provider default \
      --ref-source env \
      --ref-id DISCORD_BOT_TOKEN \
      --dry-run
    
    openclaw config set channels.discord.token \
      --ref-provider default \
      --ref-source env \
      --ref-id DISCORD_BOT_TOKEN \
      --dry-run \
      --json
    
    openclaw config set channels.discord.token \
      --ref-provider vault \
      --ref-source exec \
      --ref-id discord/token \
      --dry-run \
      --allow-exec
    
[/code]

Dry-run behavior:

  * Builder mode: runs SecretRef resolvability checks for changed refs/providers.
  * JSON mode (`--strict-json`, `--json`, or batch mode): runs schema validation plus SecretRef resolvability checks.
  * Exec SecretRef checks are skipped by default during dry-run to avoid command side effects.
  * Use `--allow-exec` with `--dry-run` to opt in to exec SecretRef checks (this may execute provider commands).
  * `--allow-exec` is dry-run only and errors if used without `--dry-run`.

`--dry-run --json` prints a machine-readable report:

  * `ok`: whether dry-run passed
  * `operations`: number of assignments evaluated
  * `checks`: whether schema/resolvability checks ran
  * `checks.resolvabilityComplete`: whether resolvability checks ran to completion (false when exec refs are skipped)
  * `refsChecked`: number of refs actually resolved during dry-run
  * `skippedExecRefs`: number of exec refs skipped because `--allow-exec` was not set
  * `errors`: structured schema/resolvability failures when `ok=false`


### 

​

JSON Output Shape

Copy
[code]
    {
      ok: boolean,
      operations: number,
      configPath: string,
      inputModes: ["value" | "json" | "builder", ...],
      checks: {
        schema: boolean,
        resolvability: boolean,
        resolvabilityComplete: boolean,
      },
      refsChecked: number,
      skippedExecRefs: number,
      errors?: [
        {
          kind: "schema" | "resolvability",
          message: string,
          ref?: string, // present for resolvability errors
        },
      ],
    }
    
[/code]

Success example:

Copy
[code]
    {
      "ok": true,
      "operations": 1,
      "configPath": "~/.openclaw/openclaw.json",
      "inputModes": ["builder"],
      "checks": {
        "schema": false,
        "resolvability": true,
        "resolvabilityComplete": true
      },
      "refsChecked": 1,
      "skippedExecRefs": 0
    }
    
[/code]

Failure example:

Copy
[code]
    {
      "ok": false,
      "operations": 1,
      "configPath": "~/.openclaw/openclaw.json",
      "inputModes": ["builder"],
      "checks": {
        "schema": false,
        "resolvability": true,
        "resolvabilityComplete": true
      },
      "refsChecked": 1,
      "skippedExecRefs": 0,
      "errors": [
        {
          "kind": "resolvability",
          "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",
          "ref": "env:default:MISSING_TEST_SECRET"
        }
      ]
    }
    
[/code]

If dry-run fails:

  * `config schema validation failed`: your post-change config shape is invalid; fix path/value or provider/ref object shape.
  * `SecretRef assignment(s) could not be resolved`: referenced provider/ref currently cannot resolve (missing env var, invalid file pointer, exec provider failure, or provider/source mismatch).
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: dry-run skipped exec refs; rerun with `--allow-exec` if you need exec resolvability validation.
  * For batch mode, fix failing entries and rerun `--dry-run` before writing.


## 

​

Subcommands

  * `config file`: Print the active config file path (resolved from `OPENCLAW_CONFIG_PATH` or default location).

Restart the gateway after edits.

## 

​

Validate

Validate the current config against the active schema without starting the gateway.

Copy
[code]
    openclaw config validate
    openclaw config validate --json
    
[/code]

[Sandbox CLI](</cli/sandbox>)[configure](</cli/configure>)

⌘I