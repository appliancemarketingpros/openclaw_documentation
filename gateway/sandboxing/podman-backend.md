---
title: Podman backend
source_url: https://docs.openclaw.ai/gateway/sandboxing/podman-backend
scraped_at: 2026-09-14
---

Gateway & OpsGateway

Selecting the native Podman CLI as a built-in backend, the Docker settings it reuses, and its rootless user-mapping rules.

This page covers Podman as the sandbox backend for agent tool execution. Running the Gateway itself in a rootless Podman container is a separate setup: see [Podman](</install/podman>).

## Podman backend

Use `sandbox.backend: "podman"` to select the native `podman` CLI directly. This is a built-in backend, not a plugin. It does not probe or select Docker, even when the `docker` executable is installed.

Podman reuses the existing `sandbox.docker.*` settings and the active native `podman` CLI context; it adds no separate connection configuration surface.

Rootless Podman defaults to `--userns=keep-id` for writable workspace mounts. A long-lived sandbox can reserve subordinate IDs and block unrelated `--userns=auto` workloads; remove it before starting those workloads. Set `sandbox.docker.user` to a nonzero numeric UID or UID:GID to control the container user. Rootless Podman rejects UID or GID 0 because Podman 4.x cannot remap namespace root while preserving workspace bind ownership; bake root-required setup into the image or use rootful Podman. Rootful Podman otherwise uses the workspace owner when available.

json5Copy code
[code]
    {  agents: {    defaults: {      sandbox: {        mode: "all",        backend: "podman",        scope: "session",        workspaceAccess: "rw",        docker: {          image: "openclaw-sandbox:bookworm-slim",          network: "none",          readOnlyRoot: true,          capDrop: ["ALL"],        },      },    },  },}
[/code]

Build or pull the sandbox image into the selected Podman store before enabling the backend. From a source checkout, build the same sandbox Dockerfile with Podman:

bashCopy code
[code]
    podman build -t openclaw-sandbox:bookworm-slim -f scripts/docker/sandbox/Dockerfile .
[/code]

Podman notes:

  * Browser sandboxing is not supported by Podman; keep `sandbox.browser.enabled` off, or install Docker and select `backend: "docker"`.
  * Local Podman engines and Podman Machine are supported. Podman Machine bind sources must be under the host home directory, which is its default shared volume. Arbitrary remote Podman connections are rejected; use the SSH backend for remote execution.
  * Custom `tmpfs` or bind mounts must not cover `/run/podman-init`; OpenClaw rejects them so sandbox cleanup continues to work.


Was this useful?YesNo

Open issue