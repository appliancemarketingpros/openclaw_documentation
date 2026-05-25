---
title: Ansible
source_url: https://docs.openclaw.ai/it/install/ansible
scraped_at: 2026-05-25
---

Distribuisci OpenClaw su server di produzione con **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- un programma di installazione automatizzato con architettura incentrata sulla sicurezza.

## Prerequisiti

Requisito | Dettagli  
---|---  
**OS** | Debian 11+ o Ubuntu 20.04+  
**Accesso** | Privilegi root o sudo  
**Rete** | Connessione Internet per l'installazione dei pacchetti  
**Ansible** | 2.14+ (installato automaticamente dallo script quick-start)  
  
## Cosa ottieni

  * **Sicurezza firewall-first** \-- UFW + isolamento Docker (accessibili solo SSH + Tailscale)
  * **VPN Tailscale** \-- accesso remoto sicuro senza esporre pubblicamente i servizi
  * **Docker** \-- contenitori sandbox isolati, binding solo su localhost
  * **Difesa in profondità** \-- architettura di sicurezza a 4 livelli
  * **Integrazione Systemd** \-- avvio automatico al boot con hardening
  * **Configurazione con un solo comando** \-- distribuzione completa in pochi minuti


## Avvio rapido

Installazione con un solo comando:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## Cosa viene installato

Il playbook Ansible installa e configura:

  1. **Tailscale** \-- VPN mesh per accesso remoto sicuro
  2. **Firewall UFW** \-- solo porte SSH + Tailscale
  3. **Docker CE + Compose V2** \-- per il backend sandbox predefinito degli agenti
  4. **Node.js 24 + pnpm** \-- dipendenze runtime (Node 22 LTS, attualmente `22.16+`, rimane supportato)
  5. **OpenClaw** \-- basato sull'host, non containerizzato
  6. **Servizio Systemd** \-- avvio automatico con hardening di sicurezza


## Configurazione post-installazione

* ### Passa all'utente openclaw

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### Esegui la procedura guidata di onboarding

Lo script post-installazione ti guida nella configurazione delle impostazioni di OpenClaw.

* ### Connetti i provider di messaggistica

Accedi a WhatsApp, Telegram, Discord o Signal:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### Verifica l'installazione

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Connettiti a Tailscale

Unisciti alla tua mesh VPN per un accesso remoto sicuro.

### Comandi rapidi

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## Architettura di sicurezza

La distribuzione usa un modello di difesa a 4 livelli:

  1. **Firewall (UFW)** \-- solo SSH (22) + Tailscale (41641/udp) esposti pubblicamente
  2. **VPN (Tailscale)** \-- Gateway accessibile solo tramite mesh VPN
  3. **Isolamento Docker** \-- la chain iptables DOCKER-USER impedisce l'esposizione di porte esterne
  4. **Hardening Systemd** \-- NoNewPrivileges, PrivateTmp, utente senza privilegi


Per verificare la tua superficie di attacco esterna:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

Dovrebbe essere aperta solo la porta 22 (SSH). Tutti gli altri servizi (Gateway, Docker) sono bloccati.

Docker viene installato per le sandbox degli agenti (esecuzione isolata degli strumenti), non per eseguire il Gateway stesso. Consulta [Multi-Agent Sandbox and Tools](</it/tools/multi-agent-sandbox-tools>) per la configurazione della sandbox.

## Installazione manuale

Se preferisci il controllo manuale rispetto all'automazione:

* ### Installa i prerequisiti

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### Clona il repository

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Installa le collection Ansible

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### Esegui il playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

In alternativa, eseguilo direttamente e poi esegui manualmente lo script di configurazione:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## Aggiornamento

Il programma di installazione Ansible configura OpenClaw per aggiornamenti manuali. Consulta [Aggiornamento](</it/install/updating>) per il flusso di aggiornamento standard.

Per rieseguire il playbook Ansible (ad esempio, per modifiche di configurazione):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

È idempotente e sicuro da eseguire più volte.

## Risoluzione dei problemi

Il firewall blocca la mia connessione

  * Assicurati prima di poter accedere tramite VPN Tailscale
  * L'accesso SSH (porta 22) è sempre consentito
  * Il Gateway è accessibile solo tramite Tailscale per progettazione

Il servizio non si avvia bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Problemi con la sandbox Docker bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

L'accesso al provider non riesce

Assicurati di eseguire come utente `openclaw`:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## Configurazione avanzata

Per l'architettura di sicurezza dettagliata e la risoluzione dei problemi, consulta il repo openclaw-ansible:

  * [Architettura di sicurezza](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Dettagli tecnici](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Guida alla risoluzione dei problemi](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## Correlati

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- guida completa alla distribuzione
  * [Docker](</it/install/docker>) \-- configurazione del Gateway containerizzato
  * [Sandboxing](</it/gateway/sandboxing>) \-- configurazione della sandbox degli agenti
  * [Multi-Agent Sandbox and Tools](</it/tools/multi-agent-sandbox-tools>) \-- isolamento per agente


Was this useful?YesNo