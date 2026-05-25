---
title: Ansible
source_url: https://docs.openclaw.ai/nl/install/ansible
scraped_at: 2026-05-25
---

Implementeer OpenClaw op productieservers met **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- een geautomatiseerd installatieprogramma met een security-first-architectuur.

## Vereisten

Vereiste | Details  
---|---  
**OS** | Debian 11+ of Ubuntu 20.04+  
**Toegang** | Root- of sudo-rechten  
**Netwerk** | Internetverbinding voor pakketinstallatie  
**Ansible** | 2.14+ (automatisch geïnstalleerd door het quickstartscript)  
  
## Wat je krijgt

  * **Firewall-first-beveiliging** \-- UFW + Docker-isolatie (alleen SSH + Tailscale toegankelijk)
  * **Tailscale VPN** \-- veilige externe toegang zonder services openbaar bloot te stellen
  * **Docker** \-- geïsoleerde sandboxcontainers, alleen localhost-bindingen
  * **Defense in depth** \-- beveiligingsarchitectuur met 4 lagen
  * **Systemd-integratie** \-- automatisch starten bij boot met hardening
  * **Installatie met één opdracht** \-- volledige implementatie in enkele minuten


## Quickstart

Installatie met één opdracht:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## Wat wordt geïnstalleerd

Het Ansible-playbook installeert en configureert:

  1. **Tailscale** \-- mesh-VPN voor veilige externe toegang
  2. **UFW-firewall** \-- alleen SSH- + Tailscale-poorten
  3. **Docker CE + Compose V2** \-- voor de standaard agentsandbox-backend
  4. **Node.js 24 + pnpm** \-- runtime-afhankelijkheden (Node 22 LTS, momenteel `22.16+`, blijft ondersteund)
  5. **OpenClaw** \-- hostgebaseerd, niet gecontaineriseerd
  6. **Systemd-service** \-- automatisch starten met security hardening


## Setup na installatie

* ### Schakel over naar de openclaw-gebruiker

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### Voer de onboardingwizard uit

Het post-installatiescript begeleidt je bij het configureren van OpenClaw-instellingen.

* ### Verbind messagingproviders

Log in bij WhatsApp, Telegram, Discord of Signal:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### Controleer de installatie

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Verbind met Tailscale

Word lid van je VPN-mesh voor veilige externe toegang.

### Snelle opdrachten

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## Beveiligingsarchitectuur

De implementatie gebruikt een verdedigingsmodel met 4 lagen:

  1. **Firewall (UFW)** \-- alleen SSH (22) + Tailscale (41641/udp) openbaar blootgesteld
  2. **VPN (Tailscale)** \-- Gateway alleen toegankelijk via VPN-mesh
  3. **Docker-isolatie** \-- DOCKER-USER iptables-chain voorkomt externe poortblootstelling
  4. **Systemd-hardening** \-- NoNewPrivileges, PrivateTmp, gebruiker zonder privileges


Om je externe aanvalsvlak te controleren:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

Alleen poort 22 (SSH) zou open moeten zijn. Alle andere services (Gateway, Docker) zijn vergrendeld.

Docker wordt geïnstalleerd voor agentsandboxes (geïsoleerde tooluitvoering), niet om de Gateway zelf te draaien. Zie [Multi-Agent Sandbox and Tools](</nl/tools/multi-agent-sandbox-tools>) voor sandboxconfiguratie.

## Handmatige installatie

Als je liever handmatige controle hebt over de automatisering:

* ### Installeer vereisten

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### Kloon de repository

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Installeer Ansible-collecties

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### Voer het playbook uit

bashCopy code
[code]
    ./run-playbook.sh
[/code]

Of voer het rechtstreeks uit en voer daarna handmatig het setupscript uit:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## Bijwerken

Het Ansible-installatieprogramma stelt OpenClaw in voor handmatige updates. Zie [Bijwerken](</nl/install/updating>) voor de standaard updateflow.

Om het Ansible-playbook opnieuw uit te voeren (bijvoorbeeld voor configuratiewijzigingen):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

Dit is idempotent en veilig om meerdere keren uit te voeren.

## Probleemoplossing

Firewall blokkeert mijn verbinding

  * Zorg ervoor dat je eerst toegang hebt via Tailscale VPN
  * SSH-toegang (poort 22) is altijd toegestaan
  * De Gateway is standaard alleen toegankelijk via Tailscale

Service start niet bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Problemen met Docker-sandbox bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

Providerlogin mislukt

Zorg ervoor dat je draait als de `openclaw`-gebruiker:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## Geavanceerde configuratie

Zie de openclaw-ansible-repo voor gedetailleerde beveiligingsarchitectuur en probleemoplossing:

  * [Beveiligingsarchitectuur](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Technische details](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Gids voor probleemoplossing](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## Gerelateerd

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- volledige implementatiegids
  * [Docker](</nl/install/docker>) \-- setup voor gecontaineriseerde Gateway
  * [Sandboxing](</nl/gateway/sandboxing>) \-- agentsandboxconfiguratie
  * [Multi-Agent Sandbox and Tools](</nl/tools/multi-agent-sandbox-tools>) \-- isolatie per agent


Was this useful?YesNo