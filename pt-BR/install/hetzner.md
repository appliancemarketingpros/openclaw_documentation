---
title: Hetzner
source_url: https://docs.openclaw.ai/pt-BR/install/hetzner
scraped_at: 2026-05-25
---

## Objetivo

Execute um Gateway OpenClaw persistente em um VPS Hetzner usando Docker, com estado durável, binários incorporados e comportamento de reinicialização seguro.

Se você quer "OpenClaw 24/7 por ~$5", esta é a configuração confiável mais simples. Os preços da Hetzner mudam; escolha o menor VPS Debian/Ubuntu e escale se encontrar OOMs.

Lembrete do modelo de segurança:

  * Agentes compartilhados pela empresa são adequados quando todos estão dentro do mesmo limite de confiança e o runtime é somente empresarial.
  * Mantenha separação rígida: VPS/runtime dedicado + contas dedicadas; sem perfis pessoais da Apple/Google/navegador/gerenciador de senhas nesse host.
  * Se os usuários forem adversariais entre si, separe por gateway/host/usuário do SO.


Consulte [Segurança](</pt-BR/gateway/security>) e [Hospedagem em VPS](</pt-BR/vps>).

## O que estamos fazendo (em termos simples)?

  * Alugar um pequeno servidor Linux (VPS Hetzner)
  * Instalar o Docker (runtime de aplicativo isolado)
  * Iniciar o Gateway OpenClaw no Docker
  * Persistir `~/.openclaw` \+ `~/.openclaw/workspace` no host (sobrevive a reinicializações/rebuilds)
  * Acessar a UI de Controle do seu laptop por meio de um túnel SSH


Esse estado montado em `~/.openclaw` inclui `openclaw.json`, por agente `agents/<agentId>/agent/auth-profiles.json` e `.env`.

O Gateway pode ser acessado por meio de:

  * Encaminhamento de porta SSH a partir do seu laptop
  * Exposição direta de porta se você gerenciar firewall e tokens por conta própria


Este guia pressupõe Ubuntu ou Debian na Hetzner.  
Se você estiver em outro VPS Linux, mapeie os pacotes conforme necessário. Para o fluxo genérico do Docker, consulte [Docker](</pt-BR/install/docker>).

* * *

## Caminho rápido (operadores experientes)

  1. Provisione o VPS Hetzner
  2. Instale o Docker
  3. Clone o repositório do OpenClaw
  4. Crie diretórios persistentes no host
  5. Configure `.env` e `docker-compose.yml`
  6. Incorpore os binários necessários na imagem
  7. `docker compose up -d`
  8. Verifique a persistência e o acesso ao Gateway


* * *

## O que você precisa

  * VPS Hetzner com acesso root
  * Acesso SSH a partir do seu laptop
  * Familiaridade básica com SSH + copiar/colar
  * ~20 minutos
  * Docker e Docker Compose
  * Credenciais de autenticação do modelo
  * Credenciais opcionais de provedor 
    * QR do WhatsApp
    * Token de bot do Telegram
    * OAuth do Gmail


* * *

* ### Provisione o VPS

Crie um VPS Ubuntu ou Debian na Hetzner.

Conecte-se como root:

bashCopy code
[code]
    ssh root@YOUR_VPS_IP
[/code]

Este guia pressupõe que o VPS seja stateful. Não o trate como infraestrutura descartável.

* ### Instale o Docker (no VPS)

bashCopy code
[code]
    apt-get updateapt-get install -y git curl ca-certificatescurl -fsSL https://get.docker.com | sh
[/code]

Verifique:

bashCopy code
[code]
    docker --versiondocker compose version
[/code]

* ### Clone o repositório do OpenClaw

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclaw
[/code]

Este guia pressupõe que você criará uma imagem personalizada para garantir a persistência dos binários.

* ### Crie diretórios persistentes no host

Contêineres Docker são efêmeros. Todo estado de longa duração deve ficar no host.

bashCopy code
[code]
    mkdir -p /root/.openclaw/workspace # Set ownership to the container user (uid 1000):chown -R 1000:1000 /root/.openclaw
[/code]

* ### Configure variáveis de ambiente

Crie `.env` na raiz do repositório.

bashCopy code
[code]
    OPENCLAW_IMAGE=openclaw:latestOPENCLAW_GATEWAY_TOKEN=OPENCLAW_GATEWAY_BIND=lanOPENCLAW_GATEWAY_PORT=18789 OPENCLAW_CONFIG_DIR=/root/.openclawOPENCLAW_WORKSPACE_DIR=/root/.openclaw/workspace GOG_KEYRING_PASSWORD=XDG_CONFIG_HOME=/home/node/.openclaw
[/code]

Defina `OPENCLAW_GATEWAY_TOKEN` quando quiser gerenciar o token estável do gateway por meio de `.env`; caso contrário, configure `gateway.auth.token` antes de depender de clientes entre reinicializações. Se nenhuma das fontes existir, o OpenClaw usa um token apenas de runtime para essa inicialização. Gere uma senha de keyring e cole-a em `GOG_KEYRING_PASSWORD`:

bashCopy code
[code]
    openssl rand -hex 32
[/code]

**Não faça commit deste arquivo.**

Este arquivo `.env` é para env de contêiner/runtime, como `OPENCLAW_GATEWAY_TOKEN`. A autenticação armazenada de OAuth/chave de API de provedor fica no `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` montado.

* ### Configuração do Docker Compose

Crie ou atualize `docker-compose.yml`.

yamlCopy code
[code]
    services:  openclaw-gateway:    image: ${OPENCLAW_IMAGE}    build: .    restart: unless-stopped    env_file:      - .env    environment:      - HOME=/home/node      - NODE_ENV=production      - TERM=xterm-256color      - OPENCLAW_GATEWAY_BIND=${OPENCLAW_GATEWAY_BIND}      - OPENCLAW_GATEWAY_PORT=${OPENCLAW_GATEWAY_PORT}      - OPENCLAW_GATEWAY_TOKEN=${OPENCLAW_GATEWAY_TOKEN}      - GOG_KEYRING_PASSWORD=${GOG_KEYRING_PASSWORD}      - XDG_CONFIG_HOME=${XDG_CONFIG_HOME}      - PATH=/home/linuxbrew/.linuxbrew/bin:/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin    volumes:      - ${OPENCLAW_CONFIG_DIR}:/home/node/.openclaw      - ${OPENCLAW_WORKSPACE_DIR}:/home/node/.openclaw/workspace    ports:      # Recommended: keep the Gateway loopback-only on the VPS; access via SSH tunnel.      # To expose it publicly, remove the `127.0.0.1:` prefix and firewall accordingly.      - "127.0.0.1:${OPENCLAW_GATEWAY_PORT}:18789"    command:      [        "node",        "dist/index.js",        "gateway",        "--bind",        "${OPENCLAW_GATEWAY_BIND}",        "--port",        "${OPENCLAW_GATEWAY_PORT}",        "--allow-unconfigured",      ]
[/code]

`--allow-unconfigured` serve apenas para conveniência de bootstrap, não substitui uma configuração adequada de gateway. Ainda assim, defina autenticação (`gateway.auth.token` ou senha) e use configurações de bind seguras para sua implantação.

* ### Etapas de runtime compartilhado da VM Docker

Use o guia de runtime compartilhado para o fluxo comum de host Docker:

  * [Incorporar os binários necessários na imagem](</pt-BR/install/docker-vm-runtime#bake-required-binaries-into-the-image>)
  * [Criar e iniciar](</pt-BR/install/docker-vm-runtime#build-and-launch>)
  * [O que persiste onde](</pt-BR/install/docker-vm-runtime#what-persists-where>)
  * [Atualizações](</pt-BR/install/docker-vm-runtime#updates>)


* ### Acesso específico da Hetzner

Após as etapas compartilhadas de build e inicialização, conclua a seguinte configuração para abrir o túnel:

**Pré-requisito:** Garanta que a configuração sshd do seu VPS permita encaminhamento TCP. Se você reforçou sua configuração SSH, verifique `/etc/ssh/sshd_config` e defina:

CodeCopy code
[code]
    AllowTcpForwarding local
[/code]

`local` permite encaminhamentos locais `ssh -L` a partir do seu laptop enquanto bloqueia encaminhamentos remotos do servidor. Defini-lo como `no` fará o túnel falhar com: `channel 3: open failed: administratively prohibited: open failed`

Depois de confirmar que o encaminhamento TCP está habilitado, reinicie o serviço SSH (`systemctl restart ssh`) e execute o túnel a partir do seu laptop:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 root@YOUR_VPS_IP
[/code]

Abra:

`http://127.0.0.1:18789/`

Cole o segredo compartilhado configurado. Este guia usa o token do gateway por padrão; se você mudou para autenticação por senha, use essa senha em vez disso.

O mapa de persistência compartilhado fica em [Runtime da VM Docker](</pt-BR/install/docker-vm-runtime#what-persists-where>).

## Infraestrutura como Código (Terraform)

Para equipes que preferem fluxos de trabalho de infraestrutura como código, uma configuração Terraform mantida pela comunidade fornece:

  * Configuração Terraform modular com gerenciamento remoto de estado
  * Provisionamento automatizado via cloud-init
  * Scripts de implantação (bootstrap, deploy, backup/restore)
  * Endurecimento de segurança (firewall, UFW, acesso somente por SSH)
  * Configuração de túnel SSH para acesso ao gateway


**Repositórios:**

  * Infraestrutura: [openclaw-terraform-hetzner](<https://github.com/andreesg/openclaw-terraform-hetzner>)
  * Configuração Docker: [openclaw-docker-config](<https://github.com/andreesg/openclaw-docker-config>)


Essa abordagem complementa a configuração Docker acima com implantações reproduzíveis, infraestrutura versionada e recuperação de desastre automatizada.

## Próximos passos

  * Configure canais de mensagens: [Canais](</pt-BR/channels>)
  * Configure o Gateway: [Configuração do Gateway](</pt-BR/gateway/configuration>)
  * Mantenha o OpenClaw atualizado: [Atualização](</pt-BR/install/updating>)


## Relacionados

  * [Visão geral da instalação](</pt-BR/install>)
  * [Fly.io](</pt-BR/install/fly>)
  * [Docker](</pt-BR/install/docker>)
  * [Hospedagem em VPS](</pt-BR/vps>)


Was this useful?YesNo