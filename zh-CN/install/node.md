---
title: Node.js
source_url: https://docs.openclaw.ai/zh-CN/install/node
scraped_at: 2026-05-25
---

OpenClaw 要求使用 **Node 22.16 或更新版本** 。**Node 24 是安装、CI 和发布工作流的默认且推荐的运行时** 。Node 22 仍通过 active LTS 系列受支持。[安装脚本](</zh-CN/install#alternative-install-methods>)会自动检测并安装 Node - 本页适用于你想自行设置 Node，并确保所有内容正确连接时（版本、PATH、全局安装）。

## 检查你的版本

bashCopy code
[code]
    node -v
[/code]

如果输出 `v24.x.x` 或更高版本，说明你正在使用推荐的默认版本。如果输出 `v22.16.x` 或更高版本，说明你正在使用受支持的 Node 22 LTS 路径，但我们仍建议在方便时升级到 Node 24。如果未安装 Node，或版本太旧，请从下面选择一种安装方法。

## 安装 Node

### macOS

**Homebrew** （推荐）：

bashCopy code
[code]
    brew install node
[/code]

或从 [nodejs.org](<https://nodejs.org/>) 下载 macOS 安装程序。

### Linux

**Ubuntu / Debian：**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL：**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

或使用版本管理器（见下文）。

### Windows

**winget** （推荐）：

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey：**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

或从 [nodejs.org](<https://nodejs.org/>) 下载 Windows 安装程序。

Using a version manager (nvm, fnm, mise, asdf)

版本管理器可让你轻松在多个 Node 版本之间切换。常用选项：

  * [**fnm**](<https://github.com/Schniz/fnm>) \- 快速、跨平台
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- 在 macOS/Linux 上广泛使用
  * [**mise**](<https://mise.jdx.dev/>) \- 多语言（Node、Python、Ruby 等）


fnm 示例：

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## 故障排除

### `openclaw: command not found`

这几乎总是表示 npm 的全局 bin 目录不在你的 PATH 中。

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

在输出中查找 `<npm-prefix>/bin`（macOS/Linux）或 `<npm-prefix>`（Windows）。

* ### Add it to your shell startup file

### macOS / Linux

添加到 `~/.zshrc` 或 `~/.bashrc`：

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

然后打开一个新终端（或在 zsh 中运行 `rehash` / 在 bash 中运行 `hash -r`）。

### Windows

通过 Settings → System → Environment Variables，将 `npm prefix -g` 的输出添加到系统 PATH。

### `npm install -g` 上的权限错误（Linux）

如果你看到 `EACCES` 错误，请将 npm 的全局前缀切换到用户可写目录：

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

将 `export PATH=...` 这一行添加到你的 `~/.bashrc` 或 `~/.zshrc`，使其永久生效。

## 相关内容

  * [安装概览](</zh-CN/install>) \- 所有安装方法
  * [更新](</zh-CN/install/updating>) \- 让 OpenClaw 保持最新
  * [入门指南](</zh-CN/start/getting-started>) \- 安装后的第一步


Was this useful?YesNo