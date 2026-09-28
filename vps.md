---
title: Linux server
source_url: https://docs.openclaw.ai/vps
scraped_at: 2026-09-28
---

InstallHosting

Run the OpenClaw Gateway on any Linux server or cloud VPS. This page helps you pick a provider, explains how cloud deployments work, and covers generic Linux tuning that applies everywhere.

## Pick a provider

[**Azure** Linux VM ](</install/azure>) [**Daytona** Cloud sandbox with preview URLs ](</install/daytona>) [**DigitalOcean** Simple paid VPS ](</install/digitalocean>) [**exe.dev** VM with HTTPS proxy ](</install/exe-dev>) [**Fly.io** Fly Machines ](</install/fly>) [**GCP** Compute Engine ](</install/gcp>) [**Hetzner** Docker on Hetzner VPS ](</install/hetzner>) [**Hostinger** VPS with one-click setup ](</install/hostinger>) [**Northflank** One-click, browser setup ](</install/northflank>) [**Oracle Cloud** Always Free ARM tier ](</install/oracle>) [**Railway** One-click, browser setup ](</install/railway>) [**Render** Managed web service ](</install/render>) [**Raspberry Pi** ARM self-hosted ](</install/raspberry-pi>) [**Upstash Box** SSH-managed sandbox box ](</install/upstash>)

**AWS (EC2 / Lightsail / free tier)** also works well. A community video walkthrough is available at [x.com/techfrenAJ/status/2014934471095812547](<https://x.com/techfrenAJ/status/2014934471095812547>) (community resource -- may become unavailable).

## How cloud setups work

  * The **Gateway runs on the VPS** and owns state + workspace.
  * You connect from your laptop or phone via the **Control UI** or **Tailscale/SSH**.
  * Treat the VPS as the source of truth and **back up** the state + workspace regularly.
  * Secure default: keep the Gateway on loopback and access it via SSH tunnel or Tailscale Serve. If you bind to `lan` or `tailnet`, the Gateway requires a shared secret (`gateway.auth.token` or `gateway.auth.password`) unless auth is delegated to a trusted proxy.


Related pages: [Gateway remote access](</gateway/remote>), [Platforms hub](</platforms>).

## Harden admin access first

Before you install OpenClaw on a public VPS, decide how you want to administer the box itself.

  * For Tailnet-only admin access: install Tailscale first, join the VPS to your tailnet, verify a second SSH session over the Tailscale IP or MagicDNS name, then restrict public SSH.
  * Without Tailscale: apply the equivalent hardening for your SSH path before exposing more services.
  * This is separate from Gateway access. You can still keep OpenClaw bound to loopback and use an SSH tunnel or Tailscale Serve for the dashboard.


Tailscale-specific Gateway options live in [Tailscale](</gateway/tailscale>).

## Shared company agent on a VPS

Running a single agent for a team is a valid setup when every user is in the same trust boundary and the agent is business-only.

  * Keep it on a dedicated runtime (VPS/VM/container + dedicated OS user/accounts).
  * Do not sign that runtime into personal Apple/Google accounts or personal browser/password-manager profiles.
  * If users are adversarial to each other, split by gateway/host/OS user.


Security model details: [Security](</gateway/security>).

## Using nodes with a VPS

You can keep the Gateway in the cloud and pair **nodes** on your local devices (Mac/iOS/Android/headless). Nodes provide local screen/camera and `system.run` capabilities while the Gateway stays in the cloud. A paired Mac can also present hosted widgets in its native panel.

Docs: [Nodes](</nodes>), [Nodes CLI](</cli/nodes>).

## Startup tuning for small VMs and ARM hosts

If CLI commands feel slow on low-power VMs (or ARM hosts), enable Node's module compile cache:

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF'export NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

  * `NODE_COMPILE_CACHE` improves repeated command startup times; the first run warms the cache.
  * `OPENCLAW_NO_RESPAWN=1` keeps routine Gateway restarts in-process, which avoids extra process handoffs and keeps PID tracking simple on small hosts.
  * For Raspberry Pi specifics, see [Raspberry Pi](</install/raspberry-pi>).


### systemd tuning checklist (optional)

For VM hosts using `systemd`, consider:

  * Service env for a stable startup path: `OPENCLAW_NO_RESPAWN=1` and `NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache`
  * A longer startup timeout for slow hosts: `TimeoutStartSec=90`.
  * The managed unit owns the generic restart policy: `Restart=always`, `RestartSec=5`.
  * SSD-backed disks for state/cache paths to reduce random-I/O cold-start penalties.


The standard `openclaw onboard --install-daemon` path installs a systemd user unit; customize only host-specific startup settings with:

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheTimeoutStartSec=90
[/code]

If you deliberately installed a system unit instead, edit it via `sudo systemctl edit openclaw-gateway.service`.

For the canonical managed unit body and its restart policy, see the [Gateway runbook](</gateway>).

For Linux OOM behavior, child process victim selection, and `exit 137` diagnostics, see [Linux memory pressure and OOM kills](</platforms/linux#memory-pressure-and-oom-kills>).

## Related

  * [Install overview](</install>)
  * [DigitalOcean](</install/digitalocean>)
  * [Fly.io](</install/fly>)
  * [Hetzner](</install/hetzner>)
  * [Ansible](</install/ansible>) — automated deployment to remote Debian/Ubuntu servers with Tailscale VPN and firewall isolation
  * [Kubernetes](</install/kubernetes>) — a minimal Kustomize starting point when you run the Gateway on a cluster instead of a single VPS
  * [macOS VMs](</install/macos-vm>) — a sandboxed macOS VM when you need macOS itself (iMessage) rather than a Linux host


Was this useful?YesNo

Open issue