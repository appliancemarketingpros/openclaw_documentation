---
title: GCP
source_url: https://docs.openclaw.ai/install/gcp
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

GCP

# 

​

OpenClaw on GCP Compute Engine (Docker, Production VPS Guide)

## 

​

Goal

Run a persistent OpenClaw Gateway on a GCP Compute Engine VM using Docker, with durable state, baked-in binaries, and safe restart behavior. If you want “OpenClaw 24/7 for ~$5-12/mo”, this is a reliable setup on Google Cloud. Pricing varies by machine type and region; pick the smallest VM that fits your workload and scale up if you hit OOMs.

## 

​

What are we doing (simple terms)?

  * Create a GCP project and enable billing
  * Create a Compute Engine VM
  * Install Docker (isolated app runtime)
  * Start the OpenClaw Gateway in Docker
  * Persist `~/.openclaw` \+ `~/.openclaw/workspace` on the host (survives restarts/rebuilds)
  * Access the Control UI from your laptop via an SSH tunnel

The Gateway can be accessed via:

  * SSH port forwarding from your laptop
  * Direct port exposure if you manage firewalling and tokens yourself

This guide uses Debian on GCP Compute Engine. Ubuntu also works; map packages accordingly. For the generic Docker flow, see [Docker](</install/docker>).

* * *

## 

​

Quick path (experienced operators)

  1. Create GCP project + enable Compute Engine API
  2. Create Compute Engine VM (e2-small, Debian 12, 20GB)
  3. SSH into the VM
  4. Install Docker
  5. Clone OpenClaw repository
  6. Create persistent host directories
  7. Configure `.env` and `docker-compose.yml`
  8. Bake required binaries, build, and launch


* * *

## 

​

What you need

  * GCP account (free tier eligible for e2-micro)
  * gcloud CLI installed (or use Cloud Console)
  * SSH access from your laptop
  * Basic comfort with SSH + copy/paste
  * ~20-30 minutes
  * Docker and Docker Compose
  * Model auth credentials
  * Optional provider credentials
    * WhatsApp QR
    * Telegram bot token
    * Gmail OAuth


* * *

1

Install gcloud CLI (or use Console)

**Option A: gcloud CLI** (recommended for automation)Install from <https://cloud.google.com/sdk/docs/install>Initialize and authenticate:

Copy
[code]
    gcloud init
    gcloud auth login
    
[/code]

**Option B: Cloud Console** All steps can be done via the web UI at <https://console.cloud.google.com>

2

Create a GCP project

**CLI:**

Copy
[code]
    gcloud projects create my-openclaw-project --name="OpenClaw Gateway"
    gcloud config set project my-openclaw-project
    
[/code]

Enable billing at <https://console.cloud.google.com/billing> (required for Compute Engine).Enable the Compute Engine API:

Copy
[code]
    gcloud services enable compute.googleapis.com
    
[/code]

**Console:**

  1. Go to IAM & Admin > Create Project
  2. Name it and create
  3. Enable billing for the project
  4. Navigate to APIs & Services > Enable APIs > search “Compute Engine API” > Enable


3

Create the VM

**Machine types:**

Type| Specs| Cost| Notes  
---|---|---|---  
e2-medium| 2 vCPU, 4GB RAM| ~$25/mo| Most reliable for local Docker builds  
e2-small| 2 vCPU, 2GB RAM| ~$12/mo| Minimum recommended for Docker build  
e2-micro| 2 vCPU (shared), 1GB RAM| Free tier eligible| Often fails with Docker build OOM (exit 137)  
  
**CLI:**

Copy
[code]
    gcloud compute instances create openclaw-gateway \
      --zone=us-central1-a \
      --machine-type=e2-small \
      --boot-disk-size=20GB \
      --image-family=debian-12 \
      --image-project=debian-cloud
    
[/code]

**Console:**

  1. Go to Compute Engine > VM instances > Create instance
  2. Name: `openclaw-gateway`
  3. Region: `us-central1`, Zone: `us-central1-a`
  4. Machine type: `e2-small`
  5. Boot disk: Debian 12, 20GB
  6. Create


4

SSH into the VM

**CLI:**

Copy
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
    
[/code]

**Console:** Click the “SSH” button next to your VM in the Compute Engine dashboard.Note: SSH key propagation can take 1-2 minutes after VM creation. If connection is refused, wait and retry.

5

Install Docker (on the VM)

Copy
[code]
    sudo apt-get update
    sudo apt-get install -y git curl ca-certificates
    curl -fsSL https://get.docker.com | sudo sh
    sudo usermod -aG docker $USER
    
[/code]

Log out and back in for the group change to take effect:

Copy
[code]
    exit
    
[/code]

Then SSH back in:

Copy
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a
    
[/code]

Verify:

Copy
[code]
    docker --version
    docker compose version
    
[/code]

6

Clone the OpenClaw repository

Copy
[code]
    git clone https://github.com/openclaw/openclaw.git
    cd openclaw
    
[/code]

This guide assumes you will build a custom image to guarantee binary persistence.

7

Create persistent host directories

Docker containers are ephemeral. All long-lived state must live on the host.

Copy
[code]
    mkdir -p ~/.openclaw
    mkdir -p ~/.openclaw/workspace
    
[/code]

8

Configure environment variables

Create `.env` in the repository root.

Copy
[code]
    OPENCLAW_IMAGE=openclaw:latest
    OPENCLAW_GATEWAY_TOKEN=change-me-now
    OPENCLAW_GATEWAY_BIND=lan
    OPENCLAW_GATEWAY_PORT=18789
    
    OPENCLAW_CONFIG_DIR=/home/$USER/.openclaw
    OPENCLAW_WORKSPACE_DIR=/home/$USER/.openclaw/workspace
    
    GOG_KEYRING_PASSWORD=change-me-now
    XDG_CONFIG_HOME=/home/node/.openclaw
    
[/code]

Generate strong secrets:

Copy
[code]
    openssl rand -hex 32
    
[/code]

**Do not commit this file.**

9

Docker Compose configuration

Create or update `docker-compose.yml`.

Copy
[code]
    services:
      openclaw-gateway:
        image: ${OPENCLAW_IMAGE}
        build: .
        restart: unless-stopped
        env_file:
          - .env
        environment:
          - HOME=/home/node
          - NODE_ENV=production
          - TERM=xterm-256color
          - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}
          - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}
          - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}
          - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}
          - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}
          - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin
        volumes:
          - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw
          - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace
        ports:
          # Recommended: keep the Gateway loopback-only on the VM; access via SSH tunnel.
          # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.
          - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"
        command:
          [
            "node",
            "dist/index.js",
            "gateway",
            "--bind",
            "${OPENCLAW_GATEWAY_BIND}",
            "--port",
            "${OPENCLAW_GATEWAY_PORT}",
            "--allow-unconfigured",
          ]
    
[/code]

`--allow-unconfigured` is only for bootstrap convenience, it is not a replacement for a proper gateway configuration. Still set auth (`gateway.auth.token` or password) and use safe bind settings for your deployment.

10

Shared Docker VM runtime steps

Use the shared runtime guide for the common Docker host flow:

  * [Bake required binaries into the image](</install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Build and launch](</install/docker-vm-runtime#build-and-launch>)
  * [What persists where](</install/docker-vm-runtime#what-persists-where>)
  * [Updates](</install/docker-vm-runtime#updates>)


11

GCP-specific launch notes

On GCP, if build fails with `Killed` or `exit code 137` during `pnpm install --frozen-lockfile`, the VM is out of memory. Use `e2-small` minimum, or `e2-medium` for more reliable first builds.When binding to LAN (`OPENCLAW_GATEWAY_BIND=lan`), configure a trusted browser origin before continuing:

Copy
[code]
    docker compose run --rm openclaw-cli config set gateway.controlUi.allowedOrigins '["http://127.0.0.1:18789"]' --strict-json
    
[/code]

If you changed the gateway port, replace `18789` with your configured port.

12

Access from your laptop

Create an SSH tunnel to forward the Gateway port:

Copy
[code]
    gcloud compute ssh openclaw-gateway --zone=us-central1-a -- -L 18789:127.0.0.1:18789
    
[/code]

Open in your browser:`http://127.0.0.1:18789/`Fetch a fresh tokenized dashboard link:

Copy
[code]
    docker compose run --rm openclaw-cli dashboard --no-open
    
[/code]

Paste the token from that URL.If Control UI shows `unauthorized` or `disconnected (1008): pairing required`, approve the browser device:

Copy
[code]
    docker compose run --rm openclaw-cli devices list
    docker compose run --rm openclaw-cli devices approve <requestId>
    
[/code]

Need the shared persistence and update reference again? See [Docker VM Runtime](</install/docker-vm-runtime#what-persists-where>) and [Docker VM Runtime updates](</install/docker-vm-runtime#updates>).

* * *

## 

​

Troubleshooting

**SSH connection refused** SSH key propagation can take 1-2 minutes after VM creation. Wait and retry. **OS Login issues** Check your OS Login profile:

Copy
[code]
    gcloud compute os-login describe-profile
    
[/code]

Ensure your account has the required IAM permissions (Compute OS Login or Compute OS Admin Login). **Out of memory (OOM)** If Docker build fails with `Killed` and `exit code 137`, the VM was OOM-killed. Upgrade to e2-small (minimum) or e2-medium (recommended for reliable local builds):

Copy
[code]
    # Stop the VM first
    gcloud compute instances stop openclaw-gateway --zone=us-central1-a
    
    # Change machine type
    gcloud compute instances set-machine-type openclaw-gateway \
      --zone=us-central1-a \
      --machine-type=e2-small
    
    # Start the VM
    gcloud compute instances start openclaw-gateway --zone=us-central1-a
    
[/code]

* * *

## 

​

Service accounts (security best practice)

For personal use, your default user account works fine. For automation or CI/CD pipelines, create a dedicated service account with minimal permissions:

  1. Create a service account:

Copy
[code]gcloud iam service-accounts create openclaw-deploy \
           --display-name="OpenClaw Deployment"
         
[/code]

  2. Grant Compute Instance Admin role (or narrower custom role):

Copy
[code]gcloud projects add-iam-policy-binding my-openclaw-project \
           --member="serviceAccount:openclaw-deploy@my-openclaw-project.iam.gserviceaccount.com" \
           --role="roles/compute.instanceAdmin.v1"
         
[/code]


Avoid using the Owner role for automation. Use the principle of least privilege. See <https://cloud.google.com/iam/docs/understanding-roles> for IAM role details.

* * *

## 

​

Next steps

  * Set up messaging channels: [Channels](</channels>)
  * Pair local devices as nodes: [Nodes](</nodes>)
  * Configure the Gateway: [Gateway configuration](</gateway/configuration>)


[Fly.io](</install/fly>)[Hetzner](</install/hetzner>)

⌘I