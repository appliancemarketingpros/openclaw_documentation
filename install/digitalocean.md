---
title: DigitalOcean
source_url: https://docs.openclaw.ai/install/digitalocean
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Hosting

DigitalOcean

# 

​

DigitalOcean

Run a persistent OpenClaw Gateway on a DigitalOcean Droplet.

## 

​

Prerequisites

  * DigitalOcean account ([signup](<https://cloud.digitalocean.com/registrations/new>))
  * SSH key pair (or willingness to use password auth)
  * About 20 minutes


## 

​

Setup

1

Create a Droplet

Use a clean base image (Ubuntu 24.04 LTS). Avoid third-party Marketplace 1-click images unless you have reviewed their startup scripts and firewall defaults.

  1. Log into [DigitalOcean](<https://cloud.digitalocean.com/>).
  2. Click **Create > Droplets**.
  3. Choose:
     * **Region:** Closest to you
     * **Image:** Ubuntu 24.04 LTS
     * **Size:** Basic, Regular, 1 vCPU / 1 GB RAM / 25 GB SSD
     * **Authentication:** SSH key (recommended) or password
  4. Click **Create Droplet** and note the IP address.


2

Connect and install

Copy
[code]
    ssh root@YOUR_DROPLET_IP
    
    apt update && apt upgrade -y
    
    # Install Node.js 24
    curl -fsSL https://deb.nodesource.com/setup_24.x | bash -
    apt install -y nodejs
    
    # Install OpenClaw
    curl -fsSL https://openclaw.ai/install.sh | bash
    openclaw --version
    
[/code]

3

Run onboarding

Copy
[code]
    openclaw onboard --install-daemon
    
[/code]

The wizard walks you through model auth, channel setup, gateway token generation, and daemon installation (systemd).

4

Add swap (recommended for 1 GB Droplets)

Copy
[code]
    fallocate -l 2G /swapfile
    chmod 600 /swapfile
    mkswap /swapfile
    swapon /swapfile
    echo '/swapfile none swap sw 0 0' >> /etc/fstab
    
[/code]

5

Verify the gateway

Copy
[code]
    openclaw status
    systemctl --user status openclaw-gateway.service
    journalctl --user -u openclaw-gateway.service -f
    
[/code]

6

Access the Control UI

The gateway binds to loopback by default. Pick one of these options.**Option A: SSH tunnel (simplest)**

Copy
[code]
    # From your local machine
    ssh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
    
[/code]

Then open `http://localhost:18789`.**Option B: Tailscale Serve**

Copy
[code]
    curl -fsSL https://tailscale.com/install.sh | sh
    tailscale up
    openclaw config set gateway.tailscale.mode serve
    openclaw gateway restart
    
[/code]

Then open `https://<magicdns>/` from any device on your tailnet.**Option C: Tailnet bind (no Serve)**

Copy
[code]
    openclaw config set gateway.bind tailnet
    openclaw gateway restart
    
[/code]

Then open `http://<tailscale-ip>:18789` (token required).

## 

​

Troubleshooting

**Gateway will not start** — Run `openclaw doctor --non-interactive` and check logs with `journalctl --user -u openclaw-gateway.service -n 50`. **Port already in use** — Run `lsof -i :18789` to find the process, then stop it. **Out of memory** — Verify swap is active with `free -h`. If still hitting OOM, use API-based models (Claude, GPT) rather than local models, or upgrade to a 2 GB Droplet.

## 

​

Next steps

  * [Channels](</channels>) — connect Telegram, WhatsApp, Discord, and more
  * [Gateway configuration](</gateway/configuration>) — all config options
  * [Updating](</install/updating>) — keep OpenClaw up to date


[Azure](</install/azure>)[Docker VM Runtime](</install/docker-vm-runtime>)

⌘I