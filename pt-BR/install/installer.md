---
title: Detalhes internos do instalador
source_url: https://docs.openclaw.ai/pt-BR/install/installer
scraped_at: 2026-05-25
---

O OpenClaw fornece três scripts de instalação, servidos por `openclaw.ai`.

Script | Plataforma | O que ele faz  
---|---|---  
`install.sh` | macOS / Linux / WSL | Instala o Node se necessário, instala o OpenClaw via npm (padrão) ou git, e pode executar a integração inicial.  
`install-cli.sh` | macOS / Linux / WSL | Instala Node + OpenClaw em um prefixo local (`~/.openclaw`) com modos npm ou checkout git. Não requer root.  
`install.ps1` | Windows (PowerShell) | Instala o Node se necessário, instala o OpenClaw via npm (padrão) ou git, e pode executar a integração inicial.  
  
## Comandos rápidos

### install.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --help
[/code]

### install-cli.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --help
[/code]

### install.ps1

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag beta -NoOnboard -DryRun
[/code]

* * *

## [install.sh](<http://install.sh>)

### Fluxo ([install.sh](<http://install.sh>))

* ### Detectar SO

Compatível com macOS e Linux (incluindo WSL). Se o macOS for detectado, instala o Homebrew se estiver ausente.

* ### Garantir Node.js 24 por padrão

Verifica a versão do Node e instala o Node 24 se necessário (Homebrew no macOS, scripts de configuração NodeSource no Linux apt/dnf/yum). O OpenClaw ainda oferece suporte ao Node 22 LTS, atualmente `22.16+`, para compatibilidade.

* ### Garantir Git

Instala o Git se estiver ausente.

* ### Instalar OpenClaw

  * método `npm` (padrão): instalação npm global
  * método `git`: clona/atualiza o repositório, instala dependências com pnpm, compila e então instala o wrapper em `~/.local/bin/openclaw`


* ### Tarefas pós-instalação

  * Atualiza um serviço Gateway carregado na medida do possível (`openclaw gateway install --force`, depois reinicia)
  * Executa `openclaw doctor --non-interactive` em upgrades e instalações git (na medida do possível)
  * Tenta a integração inicial quando apropriado (TTY disponível, integração inicial não desabilitada e verificações de bootstrap/configuração aprovadas)
  * Define `SHARP_IGNORE_GLOBAL_LIBVIPS=1` por padrão


### Detecção de checkout do código-fonte

Se executado dentro de um checkout do OpenClaw (`package.json` \+ `pnpm-workspace.yaml`), o script oferece:

  * usar checkout (`git`), ou
  * usar instalação global (`npm`)


Se nenhuma TTY estiver disponível e nenhum método de instalação estiver definido, o padrão será `npm` e um aviso será exibido.

O script sai com o código `2` para seleção de método inválida ou valores de `--install-method` inválidos.

### Exemplos ([install.sh](<http://install.sh>))

### Padrão

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Ignorar integração inicial

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Instalação Git

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### GitHub main via npm

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### Execução de teste

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Referência de flags Flag | Descrição  
---|---  
`--install-method npm|git` | Escolha o método de instalação (padrão: `npm`). Alias: `--method`  
`--npm` | Atalho para o método npm  
`--git` | Atalho para o método git. Alias: `--github`  
`--version <version|dist-tag|spec>` | versão npm, dist-tag ou especificação de pacote (padrão: `latest`)  
`--beta` | Use a dist-tag beta se disponível; caso contrário, faça fallback para `latest`  
`--git-dir <path>` | Diretório de checkout (padrão: `~/openclaw`). Alias: `--dir`  
`--no-git-update` | Ignora `git pull` para checkout existente  
`--no-prompt` | Desabilita prompts  
`--no-onboard` | Ignora a integração inicial  
`--onboard` | Habilita a integração inicial  
`--dry-run` | Imprime ações sem aplicar alterações  
`--verbose` | Habilita saída de depuração (`set -x`, logs npm em nível notice)  
`--help` | Mostra o uso (`-h`)  
Referência de variáveis de ambiente Variável | Descrição  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Método de instalação  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | versão npm, dist-tag ou especificação de pacote  
`OPENCLAW_BETA=0|1` | Usa beta se disponível  
`OPENCLAW_GIT_DIR=<path>` | Diretório de checkout  
`OPENCLAW_GIT_UPDATE=0|1` | Alterna atualizações git  
`OPENCLAW_NO_PROMPT=1` | Desabilita prompts  
`OPENCLAW_NO_ONBOARD=1` | Ignora a integração inicial  
`OPENCLAW_DRY_RUN=1` | Modo de execução de teste  
`OPENCLAW_VERBOSE=1` | Modo de depuração  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Nível de log do npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Controla o comportamento sharp/libvips (padrão: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### Fluxo ([install-cli.sh](<http://install-cli.sh>))

* ### Instalar runtime local do Node

Baixa um tarball Node LTS compatível e fixado (a versão é incorporada no script e atualizada de forma independente) para `<prefix>/tools/node-v<version>` e verifica SHA-256.

* ### Garantir Git

Se o Git estiver ausente, tenta instalar via apt/dnf/yum no Linux ou Homebrew no macOS.

* ### Instalar OpenClaw sob o prefixo

  * método `npm` (padrão): instala sob o prefixo com npm e então grava o wrapper em `<prefix>/bin/openclaw`
  * método `git`: clona/atualiza um checkout (padrão `~/openclaw`) e ainda grava o wrapper em `<prefix>/bin/openclaw`


* ### Atualizar serviço Gateway carregado

Se um serviço Gateway já estiver carregado a partir desse mesmo prefixo, o script executa `openclaw gateway install --force`, depois `openclaw gateway restart`, e verifica a integridade do Gateway na medida do possível.

### Exemplos ([install-cli.sh](<http://install-cli.sh>))

### Padrão

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Prefixo personalizado + versão

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Instalação Git

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### Saída JSON para automação

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Executar integração inicial

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Referência de flags Flag | Descrição  
---|---  
`--prefix <path>` | Prefixo de instalação (padrão: `~/.openclaw`)  
`--install-method npm|git` | Escolha o método de instalação (padrão: `npm`). Alias: `--method`  
`--npm` | Atalho para o método npm  
`--git`, `--github` | Atalho para o método git  
`--git-dir <path>` | Diretório de checkout Git (padrão: `~/openclaw`). Alias: `--dir`  
`--version <ver>` | Versão ou dist-tag do OpenClaw (padrão: `latest`)  
`--node-version <ver>` | Versão do Node (padrão: `22.22.0`)  
`--json` | Emite eventos NDJSON  
`--onboard` | Executa `openclaw onboard` após a instalação  
`--no-onboard` | Ignora a integração inicial (padrão)  
`--set-npm-prefix` | No Linux, força o prefixo npm para `~/.npm-global` se o prefixo atual não for gravável  
`--help` | Mostra o uso (`-h`)  
Referência de variáveis de ambiente Variável | Descrição  
---|---  
`OPENCLAW_PREFIX=<path>` | Prefixo de instalação  
`OPENCLAW_INSTALL_METHOD=git|npm` | Método de instalação  
`OPENCLAW_VERSION=<ver>` | Versão do OpenClaw ou dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Versão do Node  
`OPENCLAW_GIT_DIR=<path>` | Diretório de checkout do Git para instalações via git  
`OPENCLAW_GIT_UPDATE=0|1` | Alternar atualizações do git para checkouts existentes  
`OPENCLAW_NO_ONBOARD=1` | Pular integração inicial  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | Nível de log do npm  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | Controlar o comportamento de sharp/libvips (padrão: `1`)  
  
* * *

## install.ps1

### Fluxo (install.ps1)

* ### Garantir o ambiente PowerShell + Windows

Requer PowerShell 5+.

* ### Garantir Node.js 24 por padrão

Se estiver ausente, tenta instalar via winget, depois Chocolatey e depois Scoop. Node 22 LTS, atualmente `22.16+`, continua compatível.

* ### Instalar o OpenClaw

  * Método `npm` (padrão): instalação global do npm usando a `-Tag` selecionada, iniciada de um diretório temporário de instalação gravável para que shells abertos em pastas protegidas, como `C:\`, ainda funcionem
  * Método `git`: clona/atualiza o repositório, instala/compila com pnpm e instala o wrapper em `%USERPROFILE%\.local\bin\openclaw.cmd`


* ### Tarefas pós-instalação

  * Adiciona o diretório bin necessário ao PATH do usuário quando possível
  * Atualiza um serviço de Gateway carregado em modo de melhor esforço (`openclaw gateway install --force`, depois reinicia)
  * Executa `openclaw doctor --non-interactive` em atualizações e instalações via git (melhor esforço)


* ### Lidar com falhas

Instalações com `iwr ... | iex` e scriptblock relatam um erro terminante sem fechar a sessão atual do PowerShell. Instalações diretas com `powershell -File` / `pwsh -File` ainda saem com código diferente de zero para automação.

### Exemplos (install.ps1)

### Padrão

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Instalação via Git

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### main do GitHub via npm

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### Diretório git personalizado

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### Simulação

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### Rastreamento de depuração

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

Referência de flags Flag | Descrição  
---|---  
`-InstallMethod npm|git` | Método de instalação (padrão: `npm`)  
`-Tag <tag|version|spec>` | dist-tag, versão ou especificação de pacote do npm (padrão: `latest`)  
`-GitDir <path>` | Diretório de checkout (padrão: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | Pular integração inicial  
`-NoGitUpdate` | Pular `git pull`  
`-DryRun` | Apenas imprimir ações  
Referência de variáveis de ambiente Variável | Descrição  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | Método de instalação  
`OPENCLAW_GIT_DIR=<path>` | Diretório de checkout  
`OPENCLAW_NO_ONBOARD=1` | Pular integração inicial  
`OPENCLAW_GIT_UPDATE=0` | Desabilitar git pull  
`OPENCLAW_DRY_RUN=1` | Modo de simulação  
  
* * *

## CI e automação

Use flags/variáveis de ambiente não interativas para execuções previsíveis.

### install.sh (npm não interativo)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (git não interativo)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (pular integração inicial)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## Solução de problemas

Por que o Git é obrigatório?

O Git é obrigatório para o método de instalação `git`. Para instalações `npm`, o Git ainda é verificado/instalado para evitar falhas `spawn git ENOENT` quando dependências usam URLs git.

Por que o npm encontra EACCES no Linux?

Algumas configurações do Linux apontam o prefixo global do npm para caminhos pertencentes ao root. `install.sh` pode trocar o prefixo para `~/.npm-global` e anexar exportações de PATH aos arquivos rc do shell (quando esses arquivos existem).

Problemas com sharp/libvips

Os scripts usam `SHARP_IGNORE_GLOBAL_LIBVIPS=1` por padrão para evitar que sharp seja compilado contra a libvips do sistema. Para substituir:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Instale o Git for Windows, reabra o PowerShell e execute novamente o instalador.

Windows: "openclaw is not recognized"

Execute `npm config get prefix` e adicione esse diretório ao PATH do usuário (não é necessário o sufixo `\bin` no Windows), depois reabra o PowerShell.

Windows: como obter saída detalhada do instalador

`install.ps1` atualmente não expõe uma opção `-Verbose`. Use o rastreamento do PowerShell para diagnósticos no nível do script:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

openclaw não encontrado após a instalação

Geralmente é um problema de PATH. Consulte [solução de problemas do Node.js](</pt-BR/install/node#troubleshooting>).

## Relacionado

  * [Visão geral da instalação](</pt-BR/install>)
  * [Atualização](</pt-BR/install/updating>)
  * [Desinstalação](</pt-BR/install/uninstall>)


Was this useful?YesNo