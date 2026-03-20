---
title: Ansible
source_url: https://docs.openclaw.ai/install/ansible
scraped_at: 2026-03-20
---

[OpenClaw home page](</>)

![US](https://d3gk2c5xim1je2.cloudfront.net/flags/US.svg)

English

Search...

⌘K

Search...

Navigation

Containers

Ansible

# 

​

Ansible Installation

Deploy OpenClaw to production servers with **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** — an automated installer with security-first architecture.

The [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) repo is the source of truth for Ansible deployment. This page is a quick overview.

## 

​

Prerequisites

Requirement| Details  
---|---  
**OS**|  Debian 11+ or Ubuntu 20.04+  
**Access**|  Root or sudo privileges  
**Network**|  Internet connection for package installation  
**Ansible**|  2.14+ (installed automatically by the quick-start script)  
  
## 

​

What You Get

  * **Firewall-first security** — UFW + Docker isolation (only SSH + Tailscale accessible)
  * **Tailscale VPN** — secure remote access without exposing services publicly
  * **Docker** — isolated sandbox containers, localhost-only bindings
  * **Defense in depth** — 4-layer security architecture
  * **Systemd integration** — auto-start on boot with hardening
  * **One-command setup** — complete deployment in minutes


## 

​

Quick Start

One-command install:

Copy
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
    
[/code]

## 

​

What Gets Installed

The Ansible playbook installs and configures:

  1. **Tailscale** — mesh VPN for secure remote access
  2. **UFW firewall** — SSH + Tailscale ports only
  3. **Docker CE + Compose V2** — for agent sandboxes
  4. **Node.js 24 + pnpm** — runtime dependencies (Node 22 LTS, currently `22.16+`, remains supported)
  5. **OpenClaw** — host-based, not containerized
  6. **Systemd service** — auto-start with security hardening


The gateway runs directly on the host (not in Docker), but agent sandboxes use Docker for isolation. See [Sandboxing](</gateway/sandboxing>) for details.

## 

​

Post-Install Setup

1

Switch to the openclaw user

Copy
[code]
    sudo -i -u openclaw
    
[/code]

2

Run the onboarding wizard

The post-install script guides you through configuring OpenClaw settings.

3

Connect messaging providers

Log in to WhatsApp, Telegram, Discord, or Signal:

Copy
[code]
    openclaw channels login
    
[/code]

4

Verify the installation

Copy
[code]
    sudo systemctl status openclaw
    sudo journalctl -u openclaw -f
    
[/code]

5

Connect to Tailscale

Join your VPN mesh for secure remote access.

### 

​

Quick Commands

Copy
[code]
    # Check service status
    sudo systemctl status openclaw
    
    # View live logs
    sudo journalctl -u openclaw -f
    
    # Restart gateway
    sudo systemctl restart openclaw
    
    # Provider login (run as openclaw user)
    sudo -i -u openclaw
    openclaw channels login
    
[/code]

## 

​

Security Architecture

The deployment uses a 4-layer defense model:

  1. **Firewall (UFW)** — only SSH (22) + Tailscale (41641/udp) exposed publicly
  2. **VPN (Tailscale)** — gateway accessible only via VPN mesh
  3. **Docker isolation** — DOCKER-USER iptables chain prevents external port exposure
  4. **Systemd hardening** — NoNewPrivileges, PrivateTmp, unprivileged user

To verify your external attack surface:

Copy
[code]
    nmap -p- YOUR_SERVER_IP
    
[/code]

Only port 22 (SSH) should be open. All other services (gateway, Docker) are locked down. Docker is installed for agent sandboxes (isolated tool execution), not for running the gateway itself. See [Multi-Agent Sandbox and Tools](</tools/multi-agent-sandbox-tools>) for sandbox configuration.

## 

​

Manual Installation

If you prefer manual control over the automation:

1

Install prerequisites

Copy
[code]
    sudo apt update && sudo apt install -y ansible git
    
[/code]

2

Clone the repository

Copy
[code]
    git clone https://github.com/openclaw/openclaw-ansible.git
    cd openclaw-ansible
    
[/code]

3

Install Ansible collections

Copy
[code]
    ansible-galaxy collection install -r requirements.yml
    
[/code]

4

Run the playbook

Copy
[code]
    ./run-playbook.sh
    
[/code]

Alternatively, run directly and then manually execute the setup script afterward:

Copy
[code]
    ansible-playbook playbook.yml --ask-become-pass
    # Then run: /tmp/openclaw-setup.sh
    
[/code]

## 

​

Updating

The Ansible installer sets up OpenClaw for manual updates. See [Updating](</install/updating>) for the standard update flow. To re-run the Ansible playbook (for example, for configuration changes):

Copy
[code]
    cd openclaw-ansible
    ./run-playbook.sh
    
[/code]

This is idempotent and safe to run multiple times.

## 

​

Troubleshooting

Firewall blocks my connection

  * Ensure you can access via Tailscale VPN first
  * SSH access (port 22) is always allowed
  * The gateway is only accessible via Tailscale by design


Service will not start

Copy
[code]
    # Check logs
    sudo journalctl -u openclaw -n 100
    
    # Verify permissions
    sudo ls -la /opt/openclaw
    
    # Test manual start
    sudo -i -u openclaw
    cd ~/openclaw
    openclaw gateway run
    
[/code]

Docker sandbox issues

Copy
[code]
    # Verify Docker is running
    sudo systemctl status docker
    
    # Check sandbox image
    sudo docker images | grep openclaw-sandbox
    
    # Build sandbox image if missing
    cd /opt/openclaw/openclaw
    sudo -u openclaw ./scripts/sandbox-setup.sh
    
[/code]

Provider login fails

Make sure you are running as the `openclaw` user:

Copy
[code]
    sudo -i -u openclaw
    openclaw channels login
    
[/code]

## 

​

Advanced Configuration

For detailed security architecture and troubleshooting, see the openclaw-ansible repo:

  * [Security Architecture](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Technical Details](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Troubleshooting Guide](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## 

​

Related

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) — full deployment guide
  * [Docker](</install/docker>) — containerized gateway setup
  * [Sandboxing](</gateway/sandboxing>) — agent sandbox configuration
  * [Multi-Agent Sandbox and Tools](</tools/multi-agent-sandbox-tools>) — per-agent isolation


[Node.js](</install/node>)[Bun (Experimental)](</install/bun>)

⌘I