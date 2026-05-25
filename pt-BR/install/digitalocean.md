---
title: DigitalOcean
source_url: https://docs.openclaw.ai/pt-BR/install/digitalocean
scraped_at: 2026-05-25
---

Execute um Gateway persistente do OpenClaw em um Droplet da DigitalOcean (~US$6/mês para o plano Basic de 1 GB).

A DigitalOcean é o caminho mais simples de VPS paga. Se você preferir opções mais baratas ou gratuitas:

  * [Hetzner](</pt-BR/install/hetzner>) — €3,79/mês, mais núcleos/RAM por dólar.
  * [Oracle Cloud](</pt-BR/install/oracle>) — ARM Sempre Gratuito (até 4 OCPU, 24 GB de RAM), mas o cadastro pode ser instável e é somente ARM.


## Pré-requisitos

  * Conta da DigitalOcean ([cadastro](<https://cloud.digitalocean.com/registrations/new>))
  * Par de chaves SSH (ou disposição para usar autenticação por senha)
  * Cerca de 20 minutos


## Configuração

* ### Create a Droplet

  1. Entre na [DigitalOcean](<https://cloud.digitalocean.com/>).
  2. Clique em **Create > Droplets**.
  3. Escolha: 
     * **Região:** A mais próxima de você
     * **Imagem:** Ubuntu 24.04 LTS
     * **Tamanho:** Basic, Regular, 1 vCPU / 1 GB de RAM / 25 GB SSD
     * **Autenticação:** Chave SSH (recomendado) ou senha
  4. Clique em **Create Droplet** e anote o endereço IP.


* ### Connect and install

bashCopy code
[code]
    ssh root@YOUR_DROPLET_IP apt update && apt upgrade -y # Install Node.js 24curl -fsSL https://deb.nodesource.com/setup_24.x | bash -apt install -y nodejs # Install OpenClawcurl -fsSL https://openclaw.ai/install.sh | bash # Create the non-root user that will own OpenClaw state and services.adduser openclawusermod -aG sudo openclawloginctl enable-linger openclaw su - openclawopenclaw --version
[/code]

Use o shell root somente para o bootstrap do sistema. Execute comandos do OpenClaw como o usuário não root `openclaw`, para que o estado fique em `/home/openclaw/.openclaw/` e o Gateway seja instalado como o serviço systemd desse usuário.

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

O assistente orienta você pela autenticação do modelo, configuração de canais, geração de token do Gateway e instalação do daemon (systemd).

* ### Add swap (recommended for 1 GB Droplets)

bashCopy code
[code]
    fallocate -l 2G /swapfilechmod 600 /swapfilemkswap /swapfileswapon /swapfileecho '/swapfile none swap sw 0 0' >> /etc/fstab
[/code]

* ### Verify the gateway

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Access the Control UI

O Gateway faz bind em loopback por padrão. Escolha uma destas opções.

**Opção A: túnel SSH (mais simples)**

bashCopy code
[code]
    # From your local machinessh -L 18789:localhost:18789 root@YOUR_DROPLET_IP
[/code]

Em seguida, abra `http://localhost:18789`.

**Opção B: Tailscale Serve**

bashCopy code
[code]
    curl -fsSL https://tailscale.com/install.sh | sudo shsudo tailscale upopenclaw config set gateway.tailscale.mode serveopenclaw gateway restart
[/code]

Em seguida, abra `https://<magicdns>/` a partir de qualquer dispositivo na sua tailnet.

O Tailscale Serve autentica o tráfego da UI de Controle e do WebSocket por meio de cabeçalhos de identidade da tailnet, o que pressupõe que o próprio host do Gateway seja confiável. Os endpoints da API HTTP seguem o modo normal de autenticação do Gateway (token/senha) independentemente disso. Para exigir credenciais explícitas de segredo compartilhado pelo Serve, defina `gateway.auth.allowTailscale: false` e use `gateway.auth.mode: "token"` ou `"password"`.

**Opção C: bind de tailnet (sem Serve)**

bashCopy code
[code]
    openclaw config set gateway.bind tailnetopenclaw gateway restart
[/code]

Em seguida, abra `http://<tailscale-ip>:18789` (token obrigatório).

## Persistência e backups

O estado do OpenClaw fica em:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` por agente, estado de canal/provedor e dados de sessão.
  * `~/.openclaw/workspace/` — o workspace do agente ([SOUL.md](<http://SOUL.md>), memória, artefatos).


Eles sobrevivem a reinicializações do Droplet. Para criar um snapshot portátil:

bashCopy code
[code]
    openclaw backup create
[/code]

Os snapshots da DigitalOcean fazem backup do Droplet inteiro; `openclaw backup create` é portátil entre hosts.

## Dicas para 1 GB de RAM

O Droplet de US$6 tem apenas 1 GB de RAM. Para manter tudo fluido:

  * Certifique-se de que a etapa de swap acima esteja em `/etc/fstab`, para que ela sobreviva a reinicializações.
  * Prefira modelos baseados em API (Claude, GPT) em vez de modelos locais — a inferência de LLM local não cabe em 1 GB.
  * Defina `agents.defaults.model.primary` para um modelo menor se você encontrar OOMs em prompts grandes.
  * Monitore com `free -h` e `htop`.


## Solução de problemas

**O Gateway não inicia** \-- Execute `openclaw doctor --non-interactive` e confira os logs com `journalctl --user -u openclaw-gateway.service -n 50`.

**Porta já em uso** \-- Execute `lsof -i :18789` para encontrar o processo e, em seguida, pare-o.

**Sem memória** \-- Verifique se o swap está ativo com `free -h`. Se ainda houver OOM, use modelos baseados em API (Claude, GPT) em vez de modelos locais, ou faça upgrade para um Droplet de 2 GB.

## Próximos passos

  * [Canais](</pt-BR/channels>) \-- conecte Telegram, WhatsApp, Discord e outros
  * [Configuração do Gateway](</pt-BR/gateway/configuration>) \-- todas as opções de configuração
  * [Atualização](</pt-BR/install/updating>) \-- mantenha o OpenClaw atualizado


## Relacionado

  * [Visão geral da instalação](</pt-BR/install>)
  * [Fly.io](</pt-BR/install/fly>)
  * [Hetzner](</pt-BR/install/hetzner>)
  * [Hospedagem VPS](</pt-BR/vps>)


Was this useful?YesNo