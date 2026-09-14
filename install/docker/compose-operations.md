---
title: Docker Compose operations and image maintenance
source_url: https://docs.openclaw.ai/install/docker/compose-operations
scraped_at: 2026-09-14
---

InstallContainers

The Compose command table that replaced ClawDock, the operational accordions, and how published images are refreshed. Part of the [Docker](</install/docker>) guide.

## ClawDock migration

ClawDock has been removed. Use Docker Compose directly for day-to-day operations. Existing copies downloaded with `curl` are not automatically uninstalled. Remove the `source ~/.clawdock/clawdock-helpers.sh` line from your shell startup file (`~/.zshrc` or `~/.bashrc`), then start a new shell. If you sourced a checkout copy from `scripts/clawdock/` or the older `scripts/shell-helpers/` path, remove that source line instead. Keep your OpenClaw state, credentials, workspace, project `.env`, and volumes.

Run commands from the directory containing your `docker-compose.yml`. **Keep the same Compose file set and order on every command** so mounts and settings remain intact. With default file discovery, Compose loads `docker-compose.override.yml` automatically when present. Extra and sandbox files need explicit `-f` options; when using `-f`, include the standard override too if you use one. For example, if your deployment uses all four files:

bashCopy code
[code]
    docker compose -f docker-compose.yml -f docker-compose.override.yml \  -f docker-compose.extra.yml -f docker-compose.sandbox.yml ps
[/code]

Use only the files your deployment already uses. The commands below show the default file set; insert your existing `-f` options after `docker compose` when needed. See [Manual flow](</install/docker#manual-flow>) for setup and extra mounts.

Task | Command  
---|---  
Start | `docker compose up -d openclaw-gateway`  
Stop the stack | `docker compose down`  
Restart | `docker compose restart openclaw-gateway`  
Container status | `docker compose ps`  
Follow logs | `docker compose logs -f openclaw-gateway`  
Gateway shell | `docker compose exec openclaw-gateway bash`  
CLI | `docker compose run --rm openclaw-cli <command>`  
Dashboard URL | `docker compose run --rm openclaw-cli dashboard --no-open`  
List devices | `docker compose run --rm openclaw-cli devices list`  
Approve a device | `docker compose run --rm openclaw-cli devices approve <requestId>`  
Inspect config | `docker compose run --rm openclaw-cli config get <path>`  
  
Start the gateway before using the shell or CLI commands. For a custom host port, adjust the printed dashboard URL as described in [Containerized Gateway](</install/docker#containerized-gateway>). Use [Health checks](</install/docker#health-checks>) to verify the gateway and [Update OpenClaw](</install/docker-vm-runtime#update-openclaw>) for image updates.

Token setup belongs to the [Docker setup flow](</install/docker#containerized-gateway>). If you need the Control UI token, read `OPENCLAW_GATEWAY_TOKEN` privately from the project `.env`. [`config get <path>`](</cli/config>) redacts sensitive values; it does not reveal the full token.

Enable agent sandbox for Docker gateway bashCopy code
[code]
    export OPENCLAW_SANDBOX=1./scripts/docker/setup.sh
[/code]

Custom socket path (e.g. rootless Docker):

bashCopy code
[code]
    export OPENCLAW_SANDBOX=1export OPENCLAW_DOCKER_SOCKET=/run/user/1000/docker.sock./scripts/docker/setup.sh
[/code]

The script mounts `docker.sock` only after sandbox prerequisites pass. If sandbox setup can't complete, it resets `agents.defaults.sandbox.mode` to `off`. Codex code mode is disabled for turns where the OpenClaw sandbox is active (see [Sandboxing § Docker backend](</gateway/sandboxing#docker-backend>)); never mount the host Docker socket into agent sandbox containers.

Automation / CI (non-interactive)

Disable Compose pseudo-TTY allocation with `-T`:

bashCopy code
[code]
    docker compose run -T --rm openclaw-cli gateway probedocker compose run -T --rm openclaw-cli devices list --json
[/code]

Shared-network security note

`openclaw-cli` uses `network_mode: "service:openclaw-gateway"` so CLI commands can reach the gateway over `127.0.0.1`. Treat this as a shared trust boundary. The compose config drops `NET_RAW`/`NET_ADMIN` and enables `no-new-privileges` on both `openclaw-gateway` and `openclaw-cli`.

Docker Desktop DNS failures in openclaw-cli

Some Docker Desktop setups fail DNS lookups from the shared-network `openclaw-cli` sidecar after `NET_RAW` is dropped, showing up as `EAI_AGAIN` during npm-backed commands like `openclaw plugins install`. Keep the default hardened compose file for normal operation. The override below restores default capabilities for the `openclaw-cli` container only — use it for the one-off command that needs registry access, not as your default invocation:

bashCopy code
[code]
    printf '%s\n' \  'services:' \  '  openclaw-cli:' \  '    cap_drop: !reset []' \  > docker-compose.cli-no-dropped-caps.local.yml docker compose -f docker-compose.yml -f docker-compose.cli-no-dropped-caps.local.yml run --rm openclaw-cli plugins install <package>
[/code]

If you already created a long-running `openclaw-cli` container, recreate it with the same override — `docker compose exec`/`docker exec` can't change Linux capabilities on an already-created container.

Permissions and EACCES

The image runs as `node` (uid 1000). If you see permission errors on `/home/node/.openclaw`, make sure your host bind mounts are owned by uid 1000:

bashCopy code
[code]
    sudo chown -R 1000:1000 /path/to/openclaw-config /path/to/openclaw-workspace
[/code]

The same mismatch can show up as `blocked plugin candidate: suspicious ownership (... uid=1000, expected uid=0 or root)` followed by `plugin present but blocked` — the process uid and the mounted plugin directory owner disagree. Prefer running as the default uid 1000 and fixing the bind mount ownership. Only chown `/path/to/openclaw-config/npm` to `root:root` if you intentionally run OpenClaw as root long term.

Faster rebuilds

Use the repo-root `Dockerfile` instead of replacing it with a shortened single-stage example. Its `workspace-deps` stage extracts the package manifests required by `pnpm-workspace.yaml`. Build and production dependency stages share those inputs and run separate frozen-lockfile installs. This keeps both dependency layers cacheable without omitting `packages/*`, selected `extensions/*`, or other required workspace metadata.

The `runtime-assets` stage inherits `production-deps` and overlays `/app` from `runtime-build-output`, a copy of `build` with dependency trees removed. This reuses the fresh production install's layers while preserving compiled workspace packages and native addon outputs. It does not run `pnpm prune` on dependencies inherited from an image layer; pnpm 12 can fail that operation with `EXDEV` on OverlayFS. The `build` target retains development dependencies for live-test containers.

The same Dockerfile preserves the production runtime contract: digest-pinned Node and Bun bases, non-root uid 1000, `tini`, the built-in health check, and the `/usr/local/bin/openclaw` symlink. Dependabot refreshes the reviewed base digests; do not replace them with floating `FROM node:24-bookworm` tags.

Power-user container options

The default image is security-first and runs as non-root `node`. For a more full-featured container:

  1. **Persist`/home/node`**: `export OPENCLAW_HOME_VOLUME="openclaw_home"`
  2. **Bake system deps** : `export OPENCLAW_IMAGE_APT_PACKAGES="git curl jq"`
  3. **Bake Python deps** : `export OPENCLAW_IMAGE_PIP_PACKAGES="requests==2.32.5 humanize==4.14.0"`
  4. **Bake Playwright Chromium** : `export OPENCLAW_INSTALL_BROWSER=1`, or use the official `-browser` image tag
  5. **Persist browser downloads and caches** : use `OPENCLAW_HOME_VOLUME` or `OPENCLAW_EXTRA_MOUNTS`. OpenClaw auto-detects the image's Playwright-managed Chromium on Linux.

OpenAI Codex OAuth (headless Docker)

If you pick OpenAI Codex OAuth in the wizard, it opens a browser URL. In Docker or headless setups, copy the full redirect URL you land on and paste it back into the wizard to finish auth.

Base image metadata

The runtime image uses `node:24-bookworm-slim` and runs `tini` as PID 1 so zombie processes are reaped and signals handled correctly in long-running containers. It publishes OCI base-image annotations including `org.opencontainers.image.base.name` and `org.opencontainers.image.source`. Dependabot refreshes the pinned Node base digest, and each build applies current Debian point-release updates. See [OCI image annotations](<https://github.com/opencontainers/image-spec/blob/main/annotations.md>).

## Image contents and security scanning

Runtime images contain production Node.js dependencies only. Release builds pin the base image by digest and apply current Debian security updates with `apt-get dist-upgrade`; the `-browser` variant installs the Chromium version pinned by its Playwright release.

Scanner totals can include Debian findings that the distribution marks `wont-fix`. To rebuild locally against current base and package metadata, run `docker build --pull -t openclaw:local .`.

## Weekly image refreshes

The `latest*`, `main*`, and `extended-stable*` moving tags are rebuilt weekly from the same tagged release source so they pick up current OS security updates between OpenClaw releases. Stable and extended-stable refreshes remain separate, and beta images are not rebuilt on this schedule.

Each refresh also publishes a dated tag such as `2026.8.1-r20260820` (plus `-slim` and `-browser` variants). Plain version tags and dated `-rYYYYMMDD` tags are immutable; pin either form when you do not want a deployment to follow a moving tag.

## Running on a VPS?

See [Hetzner (Docker VPS)](</install/hetzner>) and [Docker VM Runtime](</install/docker-vm-runtime>) for shared VM deployment steps including binary baking, persistence, and updates.

Was this useful?YesNo

Open issue