---
title: Node.js
source_url: https://docs.openclaw.ai/pt-BR/install/node
scraped_at: 2026-05-25
---

OpenClaw requer **Node 22.16 ou mais recente**. **Node 24 é o runtime padrão e recomendado** para instalações, CI e fluxos de lançamento. Node 22 continua com suporte pela linha LTS ativa. O [script de instalação](</pt-BR/install#alternative-install-methods>) detectará e instalará o Node automaticamente - esta página é para quando você quiser configurar o Node por conta própria e garantir que tudo esteja conectado corretamente (versões, PATH, instalações globais).

## Verifique sua versão

bashCopy code
[code]
    node -v
[/code]

Se isso imprimir `v24.x.x` ou superior, você está no padrão recomendado. Se imprimir `v22.16.x` ou superior, você está no caminho compatível do Node 22 LTS, mas ainda recomendamos atualizar para o Node 24 quando for conveniente. Se o Node não estiver instalado ou a versão for antiga demais, escolha um método de instalação abaixo.

## Instale o Node

### macOS

**Homebrew** (recomendado):

bashCopy code
[code]
    brew install node
[/code]

Ou baixe o instalador para macOS em [nodejs.org](<https://nodejs.org/>).

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

Ou use um gerenciador de versões (veja abaixo).

### Windows

**winget** (recomendado):

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

Ou baixe o instalador para Windows em [nodejs.org](<https://nodejs.org/>).

Using a version manager (nvm, fnm, mise, asdf)

Gerenciadores de versões permitem alternar entre versões do Node facilmente. Opções populares:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- rápido, multiplataforma
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- amplamente usado no macOS/Linux
  * [**mise**](<https://mise.jdx.dev/>) \- poliglota (Node, Python, Ruby etc.)


Exemplo com fnm:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## Solução de problemas

### `openclaw: command not found`

Isso quase sempre significa que o diretório bin global do npm não está no seu PATH.

* ### Find your global npm prefix

bashCopy code
[code]
    npm prefix -g
[/code]

* ### Check if it's on your PATH

bashCopy code
[code]
    echo "$PATH"
[/code]

Procure por `<npm-prefix>/bin` (macOS/Linux) ou `<npm-prefix>` (Windows) na saída.

* ### Add it to your shell startup file

### macOS / Linux

Adicione a `~/.zshrc` ou `~/.bashrc`:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

Depois abra um novo terminal (ou execute `rehash` no zsh / `hash -r` no bash).

### Windows

Adicione a saída de `npm prefix -g` ao PATH do sistema via Configurações → Sistema → Variáveis de Ambiente.

### Erros de permissão em `npm install -g` (Linux)

Se você vir erros `EACCES`, altere o prefixo global do npm para um diretório gravável pelo usuário:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

Adicione a linha `export PATH=...` ao seu `~/.bashrc` ou `~/.zshrc` para torná-la permanente.

## Relacionado

  * [Visão geral da instalação](</pt-BR/install>) \- todos os métodos de instalação
  * [Atualização](</pt-BR/install/updating>) \- mantendo o OpenClaw atualizado
  * [Primeiros passos](</pt-BR/start/getting-started>) \- primeiros passos após a instalação


Was this useful?YesNo