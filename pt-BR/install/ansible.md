---
title: Ansible
source_url: https://docs.openclaw.ai/pt-BR/install/ansible
scraped_at: 2026-05-25
---

Implante o OpenClaw em servidores de produção com **[openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>)** \-- um instalador automatizado com arquitetura voltada à segurança.

## Pré-requisitos

Requisito | Detalhes  
---|---  
**SO** | Debian 11+ ou Ubuntu 20.04+  
**Acesso** | Privilégios de root ou sudo  
**Rede** | Conexão com a Internet para instalação de pacotes  
**Ansible** | 2.14+ (instalado automaticamente pelo script de início rápido)  
  
## O que você recebe

  * **Segurança baseada em firewall** \-- UFW + isolamento do Docker (apenas SSH + Tailscale acessíveis)
  * **VPN Tailscale** \-- acesso remoto seguro sem expor serviços publicamente
  * **Docker** \-- contêineres de sandbox isolados, vínculos somente no localhost
  * **Defesa em profundidade** \-- arquitetura de segurança em 4 camadas
  * **Integração com Systemd** \-- inicialização automática no boot com hardening
  * **Configuração com um comando** \-- implantação completa em minutos


## Início rápido

Instalação com um comando:

bashCopy code
[code]
    curl -fsSL https://raw.githubusercontent.com/openclaw/openclaw-ansible/main/install.sh | bash
[/code]

## O que é instalado

O playbook do Ansible instala e configura:

  1. **Tailscale** \-- VPN em malha para acesso remoto seguro
  2. **Firewall UFW** \-- apenas portas SSH + Tailscale
  3. **Docker CE + Compose V2** \-- para o backend padrão de sandbox de agente
  4. **Node.js 24 + pnpm** \-- dependências de runtime (Node 22 LTS, atualmente `22.16+`, continua compatível)
  5. **OpenClaw** \-- baseado no host, não conteinerizado
  6. **Serviço Systemd** \-- inicialização automática com hardening de segurança


## Configuração pós-instalação

* ### Mude para o usuário openclaw

bashCopy code
[code]
    sudo -i -u openclaw
[/code]

* ### Execute o assistente de onboarding

O script pós-instalação guia você pela configuração das definições do OpenClaw.

* ### Conecte provedores de mensagens

Faça login no WhatsApp, Telegram, Discord ou Signal:

bashCopy code
[code]
    openclaw channels login
[/code]

* ### Verifique a instalação

bashCopy code
[code]
    sudo systemctl status openclawsudo journalctl -u openclaw -f
[/code]

* ### Conecte-se ao Tailscale

Entre na sua malha VPN para acesso remoto seguro.

### Comandos rápidos

bashCopy code
[code]
    # Check service statussudo systemctl status openclaw # View live logssudo journalctl -u openclaw -f # Restart gatewaysudo systemctl restart openclaw # Provider login (run as openclaw user)sudo -i -u openclawopenclaw channels login
[/code]

## Arquitetura de segurança

A implantação usa um modelo de defesa em 4 camadas:

  1. **Firewall (UFW)** \-- apenas SSH (22) + Tailscale (41641/udp) expostos publicamente
  2. **VPN (Tailscale)** \-- Gateway acessível apenas pela malha VPN
  3. **Isolamento do Docker** \-- a cadeia iptables DOCKER-USER impede exposição externa de portas
  4. **Hardening do Systemd** \-- NoNewPrivileges, PrivateTmp, usuário sem privilégios


Para verificar sua superfície externa de ataque:

bashCopy code
[code]
    nmap -p- YOUR_SERVER_IP
[/code]

Apenas a porta 22 (SSH) deve estar aberta. Todos os outros serviços (Gateway, Docker) ficam bloqueados.

O Docker é instalado para sandboxes de agentes (execução isolada de ferramentas), não para executar o próprio Gateway. Consulte [Sandbox e ferramentas multiagente](</pt-BR/tools/multi-agent-sandbox-tools>) para configuração de sandbox.

## Instalação manual

Se você preferir controle manual sobre a automação:

* ### Instale os pré-requisitos

bashCopy code
[code]
    sudo apt update && sudo apt install -y ansible git
[/code]

* ### Clone o repositório

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw-ansible.gitcd openclaw-ansible
[/code]

* ### Instale as coleções do Ansible

bashCopy code
[code]
    ansible-galaxy collection install -r requirements.yml
[/code]

* ### Execute o playbook

bashCopy code
[code]
    ./run-playbook.sh
[/code]

Como alternativa, execute diretamente e depois execute manualmente o script de configuração:

bashCopy code
[code]
    ansible-playbook playbook.yml --ask-become-pass# Then run: /tmp/openclaw-setup.sh
[/code]

## Atualização

O instalador Ansible configura o OpenClaw para atualizações manuais. Consulte [Atualização](</pt-BR/install/updating>) para o fluxo padrão de atualização.

Para executar novamente o playbook do Ansible (por exemplo, para alterações de configuração):

bashCopy code
[code]
    cd openclaw-ansible./run-playbook.sh
[/code]

Isso é idempotente e seguro para executar várias vezes.

## Solução de problemas

O firewall bloqueia minha conexão

  * Garanta que você consiga acessar via VPN Tailscale primeiro
  * O acesso SSH (porta 22) é sempre permitido
  * O Gateway é acessível apenas via Tailscale por design

O serviço não inicia bashCopy code
[code]
    # Check logssudo journalctl -u openclaw -n 100 # Verify permissionssudo ls -la /opt/openclaw # Test manual startsudo -i -u openclawcd ~/openclawopenclaw gateway run
[/code]

Problemas no sandbox do Docker bashCopy code
[code]
    # Verify Docker is runningsudo systemctl status docker # Check sandbox imagesudo docker images | grep openclaw-sandbox # Build sandbox image if missing (requires source checkout)cd /opt/openclaw/openclawsudo -u openclaw ./scripts/sandbox-setup.sh# For npm installs without a source checkout, see# https://docs.openclaw.ai/gateway/sandboxing#images-and-setup
[/code]

Falha no login do provedor

Certifique-se de estar executando como o usuário `openclaw`:

bashCopy code
[code]
    sudo -i -u openclawopenclaw channels login
[/code]

## Configuração avançada

Para arquitetura de segurança detalhada e solução de problemas, consulte o repositório openclaw-ansible:

  * [Arquitetura de segurança](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/security.md>)
  * [Detalhes técnicos](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/architecture.md>)
  * [Guia de solução de problemas](<https://github.com/openclaw/openclaw-ansible/blob/main/docs/troubleshooting.md>)


## Relacionados

  * [openclaw-ansible](<https://github.com/openclaw/openclaw-ansible>) \-- guia completo de implantação
  * [Docker](</pt-BR/install/docker>) \-- configuração de Gateway conteinerizado
  * [Sandboxing](</pt-BR/gateway/sandboxing>) \-- configuração de sandbox de agente
  * [Sandbox e ferramentas multiagente](</pt-BR/tools/multi-agent-sandbox-tools>) \-- isolamento por agente


Was this useful?YesNo