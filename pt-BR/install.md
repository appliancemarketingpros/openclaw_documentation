---
title: Instalar
source_url: https://docs.openclaw.ai/pt-BR/install
scraped_at: 2026-05-25
---

## Requisitos do sistema

  * **Node 24** (recomendado) ou Node 22.16+ - o script do instalador cuida disso automaticamente
  * **macOS, Linux ou Windows** \- tanto o Windows nativo quanto o WSL2 são compatíveis; o WSL2 é mais estável. Consulte [Windows](</pt-BR/platforms/windows>).
  * `pnpm` só é necessário se você compilar a partir do código-fonte


## Recomendado: script do instalador

A forma mais rápida de instalar. Ele detecta seu SO, instala o Node se necessário, instala o OpenClaw e inicia a integração.

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

Para instalar sem executar a integração:

### macOS / Linux / WSL2

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Windows (PowerShell)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

Para todas as flags e opções de CI/automação, consulte [detalhes internos do instalador](</pt-BR/install/installer>).

## Métodos alternativos de instalação

### Instalador com prefixo local (`install-cli.sh`)

Use isto quando quiser manter o OpenClaw e o Node em um prefixo local, como `~/.openclaw`, sem depender de uma instalação do Node em todo o sistema:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

Ele oferece suporte a instalações npm por padrão, além de instalações por checkout do git no mesmo fluxo de prefixo. Referência completa: [detalhes internos do instalador](</pt-BR/install/installer#install-clish>).

Já instalado? Alterne entre instalações por pacote e git com `openclaw update --channel dev` e `openclaw update --channel stable`. Consulte [Atualização](</pt-BR/install/updating#switch-between-npm-and-git-installs>).

### npm, pnpm ou bun

Se você já gerencia o Node por conta própria:

### npm

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

### pnpm

bashCopy code
[code]
    pnpm add -g openclaw@latestpnpm approve-builds -gopenclaw onboard --install-daemon
[/code]

### bun

bashCopy code
[code]
    bun add -g openclaw@latestopenclaw onboard --install-daemon
[/code]

Solução de problemas: erros de build do sharp (npm)

Se `sharp` falhar devido a uma libvips instalada globalmente:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### A partir do código-fonte

Para colaboradores ou qualquer pessoa que queira executar a partir de um checkout local:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

Ou pule o link e use `pnpm openclaw ...` dentro do repositório. Consulte [Configuração](</pt-BR/start/setup>) para ver fluxos de desenvolvimento completos.

### Instalar a partir da main do GitHub

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### Contêineres e gerenciadores de pacotes

[**Docker** Implantações conteinerizadas ou sem interface gráfica. ](</pt-BR/install/docker>) [**Podman** Alternativa de contêiner sem root ao Docker. ](</pt-BR/install/podman>) [**Nix** Instalação declarativa via Nix flake. ](</pt-BR/install/nix>) [**Ansible** Provisionamento automatizado de frotas. ](</pt-BR/install/ansible>) [**Bun** Uso somente da CLI via runtime Bun. ](</pt-BR/install/bun>)

## Verificar a instalação

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

Se você quiser inicialização gerenciada após a instalação:

  * macOS: LaunchAgent via `openclaw onboard --install-daemon` ou `openclaw gateway install`
  * Linux/WSL2: serviço de usuário systemd via os mesmos comandos
  * Windows nativo: primeiro Tarefa Agendada, com fallback para item de login na pasta Inicializar por usuário se a criação da tarefa for negada


## Hospedagem e implantação

Implante o OpenClaw em um servidor em nuvem ou VPS:

[**VPS** [**VM Docker** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9wdC1CUi9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** Atualizar, migrar ou desinstalar [**Atualização** Mantenha o OpenClaw atualizado. ](</pt-BR/install/updating>) [**Migração** Mude para uma nova máquina. ](</pt-BR/install/migrating>) [**Desinstalar** Remova o OpenClaw completamente. ](</pt-BR/install/uninstall>) Solução de problemas: `openclaw` não encontrado Se a instalação foi concluída, mas `openclaw` não é encontrado no seu terminal: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

Se `$(npm prefix -g)/bin` não estiver no seu `$PATH`, adicione-o ao arquivo de inicialização do shell (`~/.zshrc` ou `~/.bashrc`): bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Em seguida, abra um novo terminal. Consulte [configuração do Node](</pt-BR/install/node>) para mais detalhes. ](</pt-BR/install/northflank>) Was this useful?YesNo ](</pt-BR/install/render>)](</pt-BR/install/railway>)](</pt-BR/install/azure>)](</pt-BR/install/gcp>)](</pt-BR/install/hetzner>)](</pt-BR/install/kubernetes>)](</pt-BR/install/docker-vm-runtime>)](</pt-BR/vps>)