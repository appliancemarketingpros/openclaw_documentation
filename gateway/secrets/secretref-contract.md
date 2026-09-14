---
title: SecretRef contract and provider config
source_url: https://docs.openclaw.ai/gateway/secrets/secretref-contract
scraped_at: 2026-09-14
---

Gateway & OpsGateway

This page is the SecretRef reference: the accepted sources and their id grammars, the validation rules, and the provider configuration blocks that back them.

## SecretRef contract

One object shape everywhere:

json5Copy code
[code]
    { source: "env" | "file" | "exec" | "store", provider: "default", id: "..." }
[/code]

`env` and `store` refs have an implicit provider at their source's effective default alias: `secrets.defaults.env` or `secrets.defaults.store`, falling back to `default` when unset. A matching same-source `secrets.providers` entry takes precedence; otherwise, the ref uses the built-in reader without a provider entry.

Other aliases and all `file`/`exec` refs require a registered `secrets.providers` entry with the same `source`. Changing a source's default does not rewrite explicit refs: a ref that still names `default` after an override must match a registered same-source provider, or resolution fails.

### env

json5Copy code
[code]
    { source: "env", provider: "default", id: "OPENAI_API_KEY" }
[/code]

Shorthand strings are also accepted on SecretInput fields:

json5Copy code
[code]
    "${OPENAI_API_KEY}""$OPENAI_API_KEY"
[/code]

Validation:

  * `provider` must match `^[a-z][a-z0-9_-]{0,63}$`
  * `id` must match `^[A-Z][A-Z0-9_]{0,127}$`


### file

json5Copy code
[code]
    { source: "file", provider: "filemain", id: "/providers/openai/apiKey" }
[/code]

Validation:

  * `provider` must match `^[a-z][a-z0-9_-]{0,63}$`
  * `id` must be an absolute JSON pointer (`/...`), or the literal `value` for `singleValue` providers
  * RFC 6901 escaping in segments: `~` becomes `~0`, `/` becomes `~1`


### exec

json5Copy code
[code]
    { source: "exec", provider: "vault", id: "providers/openai/apiKey#value" }
[/code]

Validation:

  * `provider` must match `^[a-z][a-z0-9_-]{0,63}$`
  * `id` must match `^[A-Za-z0-9][A-Za-z0-9._:/#-]{0,255}$` (supports selectors such as `secret#json_key`)
  * `id` must not contain `.` or `..` as slash-delimited path segments (for example `a/../b` is rejected)


### store

json5Copy code
[code]
    { source: "store", provider: "default", id: "OPENAI_API_KEY" }
[/code]

Validation:

  * `provider` must match `^[a-z][a-z0-9_-]{0,63}$`
  * `id` uses the environment-name grammar `^[A-Z][A-Z0-9_]{0,127}$`
  * Only the Gateway-wide team scope is resolved


## Provider config

Define providers under `secrets.providers`:

json5Copy code
[code]
    {  secrets: {    providers: {      default: { source: "env" },      teamstore: { source: "store" },      filemain: {        source: "file",        path: "~/.openclaw/secrets.json",        mode: "json", // or "singleValue"      },      vault: {        source: "exec",        command: "/usr/local/bin/openclaw-vault-resolver",        args: ["--profile", "prod"],        passEnv: ["PATH", "VAULT_ADDR"],        jsonOnly: true,      },      "team-secrets": {        source: "exec",        pluginIntegration: {          pluginId: "acme-secrets",          integrationId: "secret-store",        },      },    },    defaults: {      env: "default",      file: "filemain",      exec: "vault",      store: "teamstore",    },  },}
[/code]

Provider aliases are source-specific. A matching explicit provider entry wins; if an `env` or `store` default alias is also used by an entry for another source, that source's built-in provider wins. Non-default aliases and `file` or `exec` providers must resolve to an explicit entry with the matching source.

Read-only inspection recognizes valid `store` bindings without opening the database. That is configuration evidence, not proof that the value exists: credential availability stays unknown until runtime resolution.

Env provider

  * Optional exact-name allowlist via `allowlist`. A matching explicit env provider enforces this list even when it is the selected default. Omit the list to allow any name; use `[]` to deny every name.
  * Missing or empty env values fail resolution. An explicit env SecretRef remains authoritative and does not fall through to another credential or auth profile.

File provider

  * Reads the local file at `path`.
  * `mode: "json"` (default) expects a JSON object payload and resolves `id` as a JSON pointer.
  * `mode: "singleValue"` expects ref id `"value"` and returns the raw file contents (trailing newline stripped).
  * Path must pass ownership/permission checks; `timeoutMs` (default 5000) and `maxBytes` (default 1 MiB) bound the read.
  * Windows fail-closed: if ACL verification is unavailable for the path, resolution fails. Move the secret to a path whose ACLs OpenClaw can verify; there is no provider-level bypass.

Exec provider

  * Runs the configured absolute binary path directly, no shell.
  * `command` must not be a symlink, must not be group- or world-writable, and on POSIX must be owned by the current user. For package-manager shims, resolve the real binary path (for example with `realpath "$(command -v vault)"`) and configure that absolute path. Use `trustedDirs` to restrict executables to approved directories.
  * [`config validate`](</cli/config#config-validate>) checks every manual exec command path without executing providers. Config writes and dry runs check only changed or newly referenced providers, so an unrelated inactive provider does not block repairs. These are path trust checks, not proof that a provider can execute or return a secret.
  * Supports `timeoutMs` (default 5000), `noOutputTimeoutMs` (default equals `timeoutMs`), `maxOutputBytes` (default 1 MiB), `env`/`passEnv` allowlist, and `trustedDirs`.
  * `jsonOnly` defaults to `true`. With `jsonOnly: false` and a single requested id, plain non-JSON stdout is accepted as that id's value.
  * Windows fail-closed: if ACL verification is unavailable for the command path, resolution fails. Use a command path whose ACLs OpenClaw can verify; there is no provider-level bypass.
  * Plugin-managed exec providers can use `pluginIntegration` instead of a copied `command`/`args`. OpenClaw resolves the current command details from the installed plugin manifest during startup/reload; if the plugin is disabled, removed, untrusted, or no longer declares the integration, active SecretRefs on that provider fail closed.


Request payload (stdin):

jsonCopy code
[code]
    { "protocolVersion": 1, "provider": "vault", "ids": ["providers/openai/apiKey"] }
[/code]

Response payload (stdout):

jsoncCopy code
[code]
    { "protocolVersion": 1, "values": { "providers/openai/apiKey": "<openai-api-key>" } }
[/code]

Optional per-id errors:

jsonCopy code
[code]
    {"protocolVersion": 1,"values": {},"errors": { "providers/openai/apiKey": { "code": "NOT_FOUND" } }}
[/code]

`code` is an optional machine-readable diagnostic. OpenClaw displays the recognized codes `NOT_FOUND` and `AMBIGUOUS_DUPLICATE_KEY` with the provider and ref id. Other codes and free-form fields such as `message` are accepted for protocol-v1 compatibility but are not displayed because resolver output can contain credential material.

Store provider

  * Reads values from OpenClaw's shared state SQLite database.
  * The provider has no connection settings. `secrets.defaults.store` selects its default alias.
  * Only team scope is resolved. Identity scope is not supported yet.


Was this useful?YesNo

Open issue