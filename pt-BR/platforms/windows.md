---
title: Windows
source_url: https://docs.openclaw.ai/pt-BR/platforms/windows
scraped_at: 2026-05-25
---

OpenClaw é compatível com **Windows nativo** e **WSL2**. WSL2 é o caminho mais estável e recomendado para a experiência completa: a CLI, o Gateway e as ferramentas rodam dentro do Linux com compatibilidade total. O Windows nativo funciona para uso básico da CLI e do Gateway, com algumas ressalvas indicadas abaixo.

Aplicativos complementares nativos para Windows estão planejados.

## WSL2 (recomendado)

  * [Introdução](</pt-BR/start/getting-started>) (use dentro do WSL)
  * [Instalação e atualizações](</pt-BR/install/updating>)
  * Guia oficial do WSL2 (Microsoft): <https://learn.microsoft.com/windows/wsl/install>


## Status do Windows nativo

Os fluxos da CLI no Windows nativo estão melhorando, mas o WSL2 ainda é o caminho recomendado.

O que funciona bem no Windows nativo hoje:

  * instalador do site via `install.ps1`
  * uso local da CLI, como `openclaw --version`, `openclaw doctor` e `openclaw plugins list --json`
  * teste smoke integrado de agente local/provedor, como:

powershellCopy code
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
[/code]

Ressalvas atuais:

  * `openclaw onboard --non-interactive` ainda espera um gateway local acessível, a menos que você passe `--skip-health`
  * `openclaw onboard --non-interactive --install-daemon` e `openclaw gateway install` tentam primeiro usar Tarefas Agendadas do Windows
  * se a criação da Tarefa Agendada for negada, o OpenClaw recorre a um item de login na pasta Inicializar do usuário e inicia o gateway imediatamente
  * se o próprio `schtasks` travar ou parar de responder, o OpenClaw agora aborta esse caminho rapidamente e usa o fallback em vez de ficar travado indefinidamente
  * Tarefas Agendadas ainda são preferidas quando disponíveis porque fornecem um status de supervisor melhor


Se você quiser apenas a CLI nativa, sem instalar o serviço do gateway, use um destes:

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

Se você quiser inicialização gerenciada no Windows nativo:

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

Se a criação da Tarefa Agendada for bloqueada, o modo de serviço fallback ainda inicia automaticamente após o login por meio da pasta Inicializar do usuário atual.

## Gateway

  * [Runbook do Gateway](</pt-BR/gateway>)
  * [Configuração](</pt-BR/gateway/configuration>)


## Instalação do serviço Gateway (CLI)

Dentro do WSL2:

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

Ou:

CodeCopy code
[code]
    openclaw gateway install
[/code]

Ou:

CodeCopy code
[code]
    openclaw configure
[/code]

Selecione **Serviço Gateway** quando solicitado.

Reparar/migrar:

CodeCopy code
[code]
    openclaw doctor
[/code]

## Inicialização automática do Gateway antes do login do Windows

Para configurações headless, garanta que toda a cadeia de inicialização rode mesmo quando ninguém fizer login no Windows.

### 1) Mantenha os serviços de usuário em execução sem login

Dentro do WSL:

bashCopy code
[code]
    sudo loginctl enable-linger "$(whoami)"
[/code]

### 2) Instale o serviço de usuário do gateway OpenClaw

Dentro do WSL:

bashCopy code
[code]
    openclaw gateway install
[/code]

### 3) Inicie o WSL automaticamente na inicialização do Windows

No PowerShell como Administrador:

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
[/code]

Substitua `Ubuntu` pelo nome da sua distro em:

powershellCopy code
[code]
    wsl --list --verbose
[/code]

### Verifique a cadeia de inicialização

Após reiniciar (antes do login no Windows), verifique a partir do WSL:

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## Avançado: expor serviços do WSL pela LAN (portproxy)

O WSL tem sua própria rede virtual. Se outra máquina precisar acessar um serviço rodando **dentro do WSL** (SSH, um servidor TTS local ou o Gateway), você precisa encaminhar uma porta do Windows para o IP atual do WSL. O IP do WSL muda após reinicializações, então talvez seja necessário atualizar a regra de encaminhamento.

Exemplo (PowerShell **como Administrador**):

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort
[/code]

Permita a porta pelo Firewall do Windows (uma vez):

powershellCopy code
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

Atualize o portproxy após o WSL reiniciar:

powershellCopy code
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Nullnetsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `  connectaddress=$WslIp connectport=$TargetPort | Out-Null
[/code]

Observações:

  * SSH de outra máquina aponta para o **IP do host Windows** (exemplo: `ssh user@windows-host -p 2222`).
  * Nós remotos devem apontar para uma URL de Gateway **acessível** (não `127.0.0.1`); use `openclaw status --all` para confirmar.
  * Use `listenaddress=0.0.0.0` para acesso pela LAN; `127.0.0.1` mantém o acesso somente local.
  * Se quiser automatizar isso, registre uma Tarefa Agendada para executar a etapa de atualização no login.


## Instalação passo a passo do WSL2

### 1) Instale WSL2 + Ubuntu

Abra o PowerShell (Admin):

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

Reinicie se o Windows solicitar.

### 2) Habilite systemd (obrigatório para instalar o gateway)

No seu terminal WSL:

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

Depois, a partir do PowerShell:

powershellCopy code
[code]
    wsl --shutdown
[/code]

Reabra o Ubuntu e verifique:

bashCopy code
[code]
    systemctl --user status
[/code]

### 3) Instale o OpenClaw (dentro do WSL)

Para uma configuração inicial normal dentro do WSL, siga o fluxo de Introdução do Linux:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm installpnpm buildpnpm ui:buildpnpm openclaw onboard --install-daemon
[/code]

Se você estiver desenvolvendo a partir do código-fonte em vez de fazer o onboarding inicial, use o local loopback de desenvolvimento a partir de [Configuração](</pt-BR/start/setup>):

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

Guia completo: [Introdução](</pt-BR/start/getting-started>)

## Aplicativo complementar para Windows

Ainda não temos um aplicativo complementar para Windows. Contribuições são bem-vindas se você quiser ajudar a torná-lo realidade.

## Conectividade com Git e GitHub (colaboradores)

Algumas redes bloqueiam ou limitam HTTPS para o GitHub. Se `git clone` falhar com timeouts ou redefinições de conexão, tente outra rede, uma VPN ou um proxy HTTP/HTTPS fornecido pela sua organização.

Se `gh auth login` falhar durante o fluxo de dispositivo no navegador (por exemplo, um timeout ao acessar `github.com:443`), autentique com um token de acesso pessoal:

  1. Crie um token com pelo menos o escopo `repo` (PAT clássico) ou acesso detalhado equivalente.
  2. No PowerShell para a sessão atual:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

  3. Se `gh auth status` avisar sobre `read:org` ausente, gere um token que inclua esse escopo e reatribua a variável:

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token-with-repo-and-read:org>"gh auth status
[/code]

`gh auth refresh -s read:org` só se aplica quando você se autenticou via `gh auth login` e tem credenciais armazenadas para atualizar (não ao usar `GH_TOKEN`).

Nunca faça commit de tokens nem cole-os em issues ou pull requests.

## Relacionado

  * [Visão geral da instalação](</pt-BR/install>)
  * [Plataformas](</pt-BR/platforms>)


Was this useful?YesNo