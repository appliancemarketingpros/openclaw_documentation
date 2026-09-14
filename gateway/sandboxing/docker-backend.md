---
title: Docker backend
source_url: https://docs.openclaw.ai/gateway/sandboxing/docker-backend
scraped_at: 2026-09-14
---

Gateway & OpsGateway

The default local backend: its restricted defaults, GPU and Docker-out-of-Docker constraints, and the sandboxed browser container.

## Docker backend

The Docker backend runs tools locally through the `docker` CLI. Its selection and error behavior are unchanged; it does not probe or fall back to Podman.

Defaults: `network: "none"` (no egress), `readOnlyRoot: true`, `capDrop: ["ALL"]`, image `openclaw-sandbox:bookworm-slim`.

This explicit configuration keeps the agent workspace read-only and preserves the default restricted runtime posture:

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "docker",        scope: "session",        workspaceAccess: "ro",        docker: {          image: "openclaw-sandbox:bookworm-slim",          readOnlyRoot: true,          tmpfs: ["/tmp", "/var/tmp", "/run"],          network: "none",          capDrop: ["ALL"],        },      },    },  },}
[/code]

OpenClaw also creates Docker sandbox containers with an init process and `no-new-privileges`. With `workspaceAccess: "ro"`, the agent workspace is mounted read-only at `/agent`; write operations to the agent workspace are rejected, while the configured tmpfs paths remain writable.

To expose host GPUs, set `agents.defaults.sandbox.docker.gpus` (or the per-agent override) to a value like `"all"` or `"device=GPU-uuid"`. This is passed to the selected container engine's Docker-compatible `--gpus` flag and requires compatible host GPU setup. Podman requires version 5.0 or newer for this option.

### Sandboxed browser

  * The sandbox browser auto-starts (ensures CDP is reachable) when the browser tool needs it. Configure via `agents.defaults.sandbox.browser.autoStart` (default `true`) and `autoStartTimeoutMs` (default 12s).
  * Sandbox browser containers use a dedicated Docker network (`openclaw-sandbox-browser`) instead of the global `bridge` network. Configure with `agents.defaults.sandbox.browser.network`.
  * Sandbox browser network mode `"none"` is unsupported because browser control requires host-published CDP ports. Use the dedicated default, `bridge`, or another custom bridge network. `openclaw doctor --fix` disables affected persisted sidecars and restores the dedicated network without silently enabling egress.
  * `agents.defaults.sandbox.browser.cdpSourceRange` restricts container-edge CDP ingress with a CIDR allowlist (for example `172.21.0.1/32`).
  * noVNC observer access is password-protected by default; OpenClaw emits a short-lived token URL that serves a local bootstrap page and opens noVNC with the password in the URL fragment (not query string or header logs).
  * `agents.defaults.sandbox.browser.allowHostControl` (default `false`) lets sandboxed sessions target the host browser explicitly.
  * Optional allowlists gate `target: "custom"`: `allowedControlUrls`, `allowedControlHosts`, `allowedControlPorts`.


Was this useful?YesNo

Open issue