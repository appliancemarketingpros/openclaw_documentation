---
title: Raspberry Pi
source_url: https://docs.openclaw.ai/pt-BR/install/raspberry-pi
scraped_at: 2026-05-25
---

Execute um Gateway OpenClaw persistente e sempre ativo em um Raspberry Pi. Como o Pi é apenas o gateway (os modelos são executados na nuvem via API), até um Pi modesto lida bem com a carga de trabalho — o custo típico de hardware é **US$ 35–80 uma única vez** , sem mensalidades.

## Compatibilidade de hardware

Modelo de Pi | RAM | Funciona? | Observações  
---|---|---|---  
Pi 5 | 4/8 GB | Melhor | Mais rápido, recomendado.  
Pi 4 | 4 GB | Bom | Ponto ideal para a maioria dos usuários.  
Pi 4 | 2 GB | OK | Adicione swap.  
Pi 4 | 1 GB | Apertado | Possível com swap, configuração mínima.  
Pi 3B+ | 1 GB | Lento | Funciona, mas com lentidão.  
Pi Zero 2 W | 512 MB | Não | Não recomendado.  
  
**Mínimo:** 1 GB de RAM, 1 núcleo, 500 MB de disco livre, sistema operacional de 64 bits. **Recomendado:** 2 GB+ de RAM, cartão SD de 16 GB+ (ou SSD USB), Ethernet.

## Pré-requisitos

  * Raspberry Pi 4 ou 5 com 2 GB+ de RAM (4 GB recomendado)
  * Cartão MicroSD (16 GB+) ou SSD USB (melhor desempenho)
  * Fonte de alimentação oficial do Pi
  * Conexão de rede (Ethernet ou WiFi)
  * Raspberry Pi OS de 64 bits (obrigatório -- não use 32 bits)
  * Cerca de 30 minutos


## Configuração

* ### Grave o sistema operacional

Use **Raspberry Pi OS Lite (64-bit)** \-- não é necessário desktop para um servidor sem monitor.

  1. Baixe o [Raspberry Pi Imager](<https://www.raspberrypi.com/software/>).
  2. Escolha o sistema operacional: **Raspberry Pi OS Lite (64-bit)**.
  3. Na caixa de diálogo de configurações, pré-configure: 
     * Nome do host: `gateway-host`
     * Habilite SSH
     * Defina nome de usuário e senha
     * Configure WiFi (se não estiver usando Ethernet)
  4. Grave no seu cartão SD ou unidade USB, insira-o e inicialize o Pi.


* ### Conecte via SSH

bashCopy code
[code]
    ssh user@gateway-host
[/code]

* ### Atualize o sistema

bashCopy code
[code]
    sudo apt update && sudo apt upgrade -ysudo apt install -y git curl build-essential # Set timezone (important for cron and reminders)sudo timedatectl set-timezone America/Chicago
[/code]

* ### Instale o Node.js 24

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt install -y nodejsnode --version
[/code]

* ### Adicione swap (importante para 2 GB ou menos)

bashCopy code
[code]
    sudo fallocate -l 2G /swapfilesudo chmod 600 /swapfilesudo mkswap /swapfilesudo swapon /swapfileecho '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # Reduce swappiness for low-RAM devicesecho 'vm.swappiness=10' | sudo tee -a /etc/sysctl.confsudo sysctl -p
[/code]

* ### Instale o OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

* ### Execute a configuração inicial

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Siga o assistente. Chaves de API são recomendadas em vez de OAuth para dispositivos sem monitor. Telegram é o canal mais fácil para começar.

* ### Verifique

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Acesse a Control UI

No seu computador, obtenha uma URL do painel a partir do Pi:

bashCopy code
[code]
    ssh user@gateway-host 'openclaw dashboard --no-open'
[/code]

Em seguida, crie um túnel SSH em outro terminal:

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@gateway-host
[/code]

Abra a URL exibida no seu navegador local. Para acesso remoto sempre ativo, consulte a [integração com Tailscale](</pt-BR/gateway/tailscale>).

## Dicas de desempenho

**Use um SSD USB** \-- Cartões SD são lentos e se desgastam. Um SSD USB melhora drasticamente o desempenho. Consulte o [guia de inicialização USB do Pi](<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot>).

**Habilite o cache de compilação de módulos** \-- Acelera invocações repetidas da CLI em hosts Pi de menor potência:

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF' # pragma: allowlist secretexport NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

**Reduza o uso de memória** \-- Para configurações sem monitor, libere memória da GPU e desabilite serviços não usados:

bashCopy code
[code]
    echo 'gpu_mem=16' | sudo tee -a /boot/config.txtsudo systemctl disable bluetooth
[/code]

**Drop-in do systemd para reinicializações estáveis** \-- Se este Pi executa principalmente o OpenClaw, adicione um drop-in de serviço:

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

Em seguida, `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service`. Em um Pi sem monitor, também habilite lingering uma vez para que o serviço de usuário sobreviva ao logout: `sudo loginctl enable-linger "$(whoami)"`.

## Configuração de modelo recomendada

Como o Pi executa apenas o gateway, use modelos de API hospedados na nuvem:

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-sonnet-4-6",        "fallbacks": ["openai/gpt-5.4-mini"]      }    }  }}
[/code]

Não execute LLMs locais em um Pi — até modelos pequenos são lentos demais para serem úteis. Deixe Claude ou GPT fazerem o trabalho do modelo.

## Observações sobre binários ARM

A maioria dos recursos do OpenClaw funciona em ARM64 sem alterações (Node.js, Telegram, WhatsApp/Baileys, Chromium). Os binários que ocasionalmente não têm builds ARM normalmente são ferramentas CLI opcionais em Go/Rust enviadas por Skills. Verifique a página de release de um binário ausente em busca de artefatos `linux-arm64` / `aarch64` antes de recorrer à compilação a partir do código-fonte.

## Persistência e backups

O estado do OpenClaw fica em:

  * `~/.openclaw/` — `openclaw.json`, `auth-profiles.json` por agente, estado de canais/provedores, sessões.
  * `~/.openclaw/workspace/` — workspace do agente ([SOUL.md](<http://SOUL.md>), memória, artefatos).


Eles sobrevivem a reinicializações. Faça um snapshot portátil com:

bashCopy code
[code]
    openclaw backup create
[/code]

Se você mantiver esses arquivos em um SSD, tanto o desempenho quanto a durabilidade melhoram em comparação com o cartão SD.

## Solução de problemas

**Sem memória** \-- Verifique se o swap está ativo com `free -h`. Desabilite serviços não usados (`sudo systemctl disable cups bluetooth avahi-daemon`). Use apenas modelos baseados em API.

**Desempenho lento** \-- Use um SSD USB em vez de um cartão SD. Verifique se há limitação de CPU com `vcgencmd get_throttled` (deve retornar `0x0`).

**O serviço não inicia** \-- Verifique os logs com `journalctl --user -u openclaw-gateway.service --no-pager -n 100` e execute `openclaw doctor --non-interactive`. Se este for um Pi sem monitor, também verifique se lingering está habilitado: `sudo loginctl enable-linger "$(whoami)"`.

**Problemas com binários ARM** \-- Se uma skill falhar com "exec format error", verifique se o binário tem um build ARM64. Verifique a arquitetura com `uname -m` (deve mostrar `aarch64`).

**Quedas de WiFi** \-- Desabilite o gerenciamento de energia do WiFi: `sudo iwconfig wlan0 power off`.

## Próximos passos

  * [Canais](</pt-BR/channels>) \-- conecte Telegram, WhatsApp, Discord e outros
  * [Configuração do Gateway](</pt-BR/gateway/configuration>) \-- todas as opções de configuração
  * [Atualização](</pt-BR/install/updating>) \-- mantenha o OpenClaw atualizado


## Relacionado

  * [Visão geral da instalação](</pt-BR/install>)
  * [Servidor Linux](</pt-BR/vps>)
  * [Plataformas](</pt-BR/platforms>)


Was this useful?YesNo