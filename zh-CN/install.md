---
title: 安装
source_url: https://docs.openclaw.ai/zh-CN/install
scraped_at: 2026-05-25
---

## 系统要求

  * **Node 24** （推荐）或 Node 22.16+ - 安装脚本会自动处理这一点
  * **macOS、Linux 或 Windows** \- 支持原生 Windows 和 WSL2；WSL2 更稳定。参见 [Windows](</zh-CN/platforms/windows>)。
  * 只有从源码构建时才需要 `pnpm`


## 推荐：安装脚本

最快的安装方式。它会检测你的 OS，在需要时安装 Node，安装 OpenClaw，并启动新手引导。

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

安装但不运行新手引导：

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

有关所有标志和 CI/自动化选项，请参见[安装器内部机制](</zh-CN/install/installer>)。

## 替代安装方法

### 本地前缀安装器（`install-cli.sh`）

当你希望将 OpenClaw 和 Node 保存在本地前缀（例如 `~/.openclaw`）下，而不依赖系统范围的 Node 安装时，请使用此方法：

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

它默认支持 npm 安装，也支持在同一个 前缀流程下进行 git-checkout 安装。完整参考：[安装器内部机制](</zh-CN/install/installer#install-clish>)。

已经安装了？使用 `openclaw update --channel dev` 和 `openclaw update --channel stable` 在 package 和 git 安装之间切换。参见 [更新](</zh-CN/install/updating#switch-between-npm-and-git-installs>)。

### npm、pnpm 或 bun

如果你已经自行管理 Node：

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

故障排除：sharp 构建错误（npm）

如果 `sharp` 因全局安装的 libvips 而失败：

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### 从源码安装

适用于贡献者或任何想从本地 checkout 运行的人：

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

或者跳过链接，在 repo 内部使用 `pnpm openclaw ...`。完整开发工作流请参见[设置](</zh-CN/start/setup>)。

### 从 GitHub main 安装

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### 容器和 package manager

[**Docker** 容器化或无头部署。 ](</zh-CN/install/docker>) [**Podman** Docker 的无 root 容器替代方案。 ](</zh-CN/install/podman>) [**Nix** 通过 Nix flake 进行声明式安装。 ](</zh-CN/install/nix>) [**Ansible** 自动化集群预配。 ](</zh-CN/install/ansible>) [**Bun** 通过 Bun 运行时进行仅 CLI 使用。 ](</zh-CN/install/bun>)

## 验证安装

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

如果你希望安装后启用托管启动：

  * macOS：通过 `openclaw onboard --install-daemon` 或 `openclaw gateway install` 使用 LaunchAgent
  * Linux/WSL2：通过相同命令使用 systemd 用户服务
  * 原生 Windows：优先使用计划任务；如果任务创建被拒绝，则回退到按用户的 Startup 文件夹登录项


## 托管和部署

在云服务器或 VPS 上部署 OpenClaw：

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii96aC1DTi9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** 更新、迁移或卸载 [**Updating** 让 OpenClaw 保持最新。 ](</zh-CN/install/updating>) [**Migrating** 迁移到新机器。 ](</zh-CN/install/migrating>) [**Uninstall** 完全移除 OpenClaw。 ](</zh-CN/install/uninstall>) 故障排除：找不到 `openclaw` 如果安装成功但你的终端中找不到 `openclaw`： bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

如果 `$(npm prefix -g)/bin` 不在你的 `$PATH` 中，请将它添加到你的 shell 启动文件（`~/.zshrc` 或 `~/.bashrc`）： bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

然后打开新的终端。更多详情请参见 [Node 设置](</zh-CN/install/node>)。 ](</zh-CN/install/northflank>) Was this useful?YesNo ](</zh-CN/install/render>)](</zh-CN/install/railway>)](</zh-CN/install/azure>)](</zh-CN/install/gcp>)](</zh-CN/install/hetzner>)](</zh-CN/install/kubernetes>)](</zh-CN/install/docker-vm-runtime>)](</zh-CN/vps>)