---
title: Images and setup
source_url: https://docs.openclaw.ai/gateway/sandboxing/images-and-setup
scraped_at: 2026-09-14
---

Gateway & OpsGateway

Building the sandbox images from a source checkout or an npm install, and the network and certificate defaults that shape what an image must already contain.

## Images and setup

Default Docker image: `openclaw-sandbox:bookworm-slim`

* ### Build the default image

From a source checkout:

bashCopy code
[code]
    scripts/sandbox-setup.sh
[/code]

From an npm install (no source checkout needed):

bashCopy code
[code]
    docker build -t openclaw-sandbox:bookworm-slim - <<'DOCKERFILE'FROM debian:bookworm-slimENV DEBIAN_FRONTEND=noninteractiveRUN apt-get update && apt-get install -y --no-install-recommends \  bash ca-certificates curl git jq python3 ripgrep \  && rm -rf /var/lib/apt/lists/*RUN useradd --create-home --shell /bin/bash sandboxUSER sandboxWORKDIR /home/sandboxCMD ["sleep", "infinity"]DOCKERFILE
[/code]

The default image does **not** include Node. If a skill needs Node (or other runtimes), either bake a custom image or install via `sandbox.docker.setupCommand` (requires network egress + writable root + root user).

OpenClaw does not silently substitute plain `debian:bookworm-slim` when `openclaw-sandbox:bookworm-slim` is missing. Sandbox runs that target the default image fail fast with a build instruction until you build it, because the bundled image carries `python3` for the sandbox write/edit helpers.

* ### Optional: build the common image

For a more functional sandbox image with common tooling (for example `curl`, `jq`, Node 24, pnpm, `python3`, and `git`):

From a source checkout:

bashCopy code
[code]
    scripts/sandbox-common-setup.sh
[/code]

From an npm install, build the default image first (see above). Download [`scripts/docker/sandbox/Dockerfile.common`](<https://github.com/openclaw/openclaw/blob/main/scripts/docker/sandbox/Dockerfile.common>) and the root [`package.json`](<https://github.com/openclaw/openclaw/blob/main/package.json>) from the same OpenClaw commit or tag into an empty directory. Keep their filenames, then run from that directory:

bashCopy code
[code]
    docker build -t openclaw-sandbox-common:bookworm-slim -f Dockerfile.common .
[/code]

`package.json` supplies the pinned pnpm version and must be in the build context, even with `--build-arg INSTALL_PNPM=0`. It is a read-only build input; you do not need a source checkout or a host pnpm installation.

Then set `agents.defaults.sandbox.docker.image` to `openclaw-sandbox-common:bookworm-slim`.

* ### Optional: build the sandbox browser image

From a source checkout:

bashCopy code
[code]
    scripts/sandbox-browser-setup.sh
[/code]

The npm package does not include the browser Dockerfile or entrypoint. Use a source checkout to build this image.

By default, local container sandboxes run with **no network**. Override with `agents.defaults.sandbox.docker.network`.

The default-off [secret egress proxy](</gateway/secrets#secret-egress-proxy>) is Gateway-loopback only. Sandbox exec receives neither its proxy/CA environment nor protected sentinels. Sandbox/container proxy reachability is not implemented; do not enable sandbox networking expecting secret substitution to work in this release.

Sandbox browser Chromium defaults

The bundled sandbox browser image applies conservative Chromium startup flags for containerized workloads:

  * `--remote-debugging-address=127.0.0.1`
  * `--remote-debugging-port=<derived from OPENCLAW_BROWSER_CDP_PORT>`
  * `--user-data-dir=${HOME}/.chrome`
  * `--no-first-run`
  * `--no-default-browser-check`
  * `--disable-dev-shm-usage`
  * `--disable-background-networking`
  * `--disable-breakpad`
  * `--disable-crash-reporter`
  * `--no-zygote`
  * `--metrics-recording-only`
  * `--password-store=basic`
  * `--use-mock-keychain`
  * `--headless=new` when `browser.headless` is enabled.
  * `--no-sandbox --disable-setuid-sandbox` (always enabled in the sandbox browser container).
  * `--disable-3d-apis`, `--disable-gpu`, `--disable-software-rasterizer` by default; these graphics-hardening flags help containers without GPU support. Set `OPENCLAW_BROWSER_DISABLE_GRAPHICS_FLAGS=0` if your workload needs WebGL or other 3D features.
  * `--disable-extensions` by default; set `OPENCLAW_BROWSER_DISABLE_EXTENSIONS=0` for extension-reliant flows.
  * `--renderer-process-limit=2` by default; controlled by `OPENCLAW_BROWSER_RENDERER_PROCESS_LIMIT=<N>`, where `0` keeps Chromium's default.


If you need a different runtime profile, use a custom browser image and provide your own entrypoint. For local (non-container) Chromium profiles, use `browser.extraArgs` to append additional startup flags.

Network security defaults

  * `network: "host"` is blocked.
  * `network: "container:<id>"` is blocked by default (namespace join bypass risk).
  * Break-glass override: `agents.defaults.sandbox.docker.dangerouslyAllowContainerNamespaceJoin: true`.


Docker installs and the containerized gateway live here: [Docker](</install/docker>)

For Docker gateway deployments, `scripts/docker/setup.sh` can bootstrap sandbox config. Set `OPENCLAW_SANDBOX=1` (or `true`/`yes`/`on`) to enable that path. Override the socket location with `OPENCLAW_DOCKER_SOCKET`. Full setup and env reference: [Docker](</install/docker#agent-sandbox>).

Was this useful?YesNo

Open issue