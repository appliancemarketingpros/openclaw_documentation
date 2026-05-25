---
title: Windows
source_url: https://docs.openclaw.ai/zh-CN/platforms/windows
scraped_at: 2026-05-25
---

OpenClaw 同时支持 **原生 Windows** 和 **WSL2** 。WSL2 是更稳定的路径，也推荐用于完整体验：CLI、Gateway 网关和工具链都在 Linux 内运行，具备完整兼容性。原生 Windows 可用于核心 CLI 和 Gateway 网关使用，但有下面提到的一些注意事项。

原生 Windows 配套应用正在规划中。

## WSL2（推荐）

  * [入门指南](</zh-CN/start/getting-started>)（在 WSL 内使用）
  * [安装与更新](</zh-CN/install/updating>)
  * 官方 WSL2 指南（Microsoft）：<https://learn.microsoft.com/windows/wsl/install>


## 原生 Windows 状态

原生 Windows CLI 流程正在改进，但 WSL2 仍然是推荐路径。

目前在原生 Windows 上运行良好的内容：

  * 通过 `install.ps1` 使用网站安装器
  * 本地 CLI 使用，例如 `openclaw --version`、`openclaw doctor` 和 `openclaw plugins list --json`
  * 嵌入式本地智能体/提供商冒烟测试，例如：

powershellCopy code
[code]
    openclaw agent --local --agent main --thinking low -m "Reply with exactly WINDOWS-HATCH-OK."
[/code]

当前注意事项：

  * `openclaw onboard --non-interactive` 仍然要求有可访问的本地 Gateway 网关，除非你传入 `--skip-health`
  * `openclaw onboard --non-interactive --install-daemon` 和 `openclaw gateway install` 会优先尝试 Windows 计划任务
  * 如果计划任务创建被拒绝，OpenClaw 会回退到每用户 Startup 文件夹登录项，并立即启动 Gateway 网关
  * 如果 `schtasks` 本身卡住或停止响应，OpenClaw 现在会快速中止该路径并改用回退方式，而不是永远挂起
  * 计划任务在可用时仍然是首选，因为它们能提供更好的 supervisor 状态


如果你只需要原生 CLI，不安装 Gateway 网关服务，请使用以下命令之一：

powershellCopy code
[code]
    openclaw onboard --non-interactive --skip-healthopenclaw gateway run
[/code]

如果你确实想在原生 Windows 上使用托管启动：

powershellCopy code
[code]
    openclaw gateway installopenclaw gateway status --json
[/code]

如果计划任务创建被阻止，回退服务模式仍会在当前用户登录后通过 Startup 文件夹自动启动。

## Gateway 网关

  * [Gateway 网关运行手册](</zh-CN/gateway>)
  * [配置](</zh-CN/gateway/configuration>)


## Gateway 网关服务安装（CLI）

在 WSL2 内：

CodeCopy code
[code]
    openclaw onboard --install-daemon
[/code]

或者：

CodeCopy code
[code]
    openclaw gateway install
[/code]

或者：

CodeCopy code
[code]
    openclaw configure
[/code]

在提示时选择 **Gateway 网关服务** 。

修复/迁移：

CodeCopy code
[code]
    openclaw doctor
[/code]

## Windows 登录前自动启动 Gateway 网关

对于无头设置，确保即使无人登录 Windows，完整启动链也会运行。

### 1) 保持用户服务在未登录时运行

在 WSL 内：

bashCopy code
[code]
    sudo loginctl enable-linger "$(whoami)"
[/code]

### 2) 安装 OpenClaw Gateway 网关用户服务

在 WSL 内：

bashCopy code
[code]
    openclaw gateway install
[/code]

### 3) 在 Windows 启动时自动启动 WSL

在以管理员身份运行的 PowerShell 中：

powershellCopy code
[code]
    schtasks /create /tn "WSL Boot" /tr "wsl.exe -d Ubuntu --exec /bin/true" /sc onstart /ru SYSTEM
[/code]

将 `Ubuntu` 替换为以下命令显示的你的发行版名称：

powershellCopy code
[code]
    wsl --list --verbose
[/code]

### 验证启动链

重启后（Windows 登录前），从 WSL 检查：

bashCopy code
[code]
    systemctl --user is-enabled openclaw-gateway.servicesystemctl --user status openclaw-gateway.service --no-pager
[/code]

## 高级：通过 LAN 暴露 WSL 服务（portproxy）

WSL 有自己的虚拟网络。如果另一台机器需要访问 **WSL 内部** 运行的服务（SSH、本地 TTS 服务器或 Gateway 网关），你必须将 Windows 端口转发到当前 WSL IP。WSL IP 会在重启后变化，因此你可能需要刷新转发规则。

示例（**以管理员身份** 运行 PowerShell）：

powershellCopy code
[code]
    $Distro = "Ubuntu-24.04"$ListenPort = 2222$TargetPort = 22 $WslIp = (wsl -d $Distro -- hostname -I).Trim().Split(" ")[0]if (-not $WslIp) { throw "WSL IP not found." } netsh interface portproxy add v4tov4 listenaddress=0.0.0.0 listenport=$ListenPort `  connectaddress=$WslIp connectport=$TargetPort
[/code]

允许该端口通过 Windows 防火墙（一次性操作）：

powershellCopy code
[code]
    New-NetFirewallRule -DisplayName "WSL SSH $ListenPort" -Direction Inbound `  -Protocol TCP -LocalPort $ListenPort -Action Allow
[/code]

WSL 重启后刷新 portproxy：

powershellCopy code
[code]
    netsh interface portproxy delete v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 | Out-Nullnetsh interface portproxy add v4tov4 listenport=$ListenPort listenaddress=0.0.0.0 `  connectaddress=$WslIp connectport=$TargetPort | Out-Null
[/code]

注意：

  * 从另一台机器发起 SSH 时，目标是 **Windows 主机 IP** （示例：`ssh user@windows-host -p 2222`）。
  * 远程节点必须指向一个**可访问的** Gateway 网关 URL（而不是 `127.0.0.1`）；使用 `openclaw status --all` 确认。
  * 对 LAN 访问使用 `listenaddress=0.0.0.0`；`127.0.0.1` 会将其限制为仅本地访问。
  * 如果你希望自动执行此操作，请注册一个计划任务，在登录时运行刷新步骤。


## WSL2 分步安装

### 1) 安装 WSL2 + Ubuntu

打开 PowerShell（管理员）：

powershellCopy code
[code]
    wsl --install# Or pick a distro explicitly:wsl --list --onlinewsl --install -d Ubuntu-24.04
[/code]

如果 Windows 要求，请重启。

### 2) 启用 systemd（安装 Gateway 网关所需）

在你的 WSL 终端中：

bashCopy code
[code]
    sudo tee /etc/wsl.conf >/dev/null <<'EOF'[boot]systemd=trueEOF
[/code]

然后从 PowerShell 运行：

powershellCopy code
[code]
    wsl --shutdown
[/code]

重新打开 Ubuntu，然后验证：

bashCopy code
[code]
    systemctl --user status
[/code]

### 3) 安装 OpenClaw（在 WSL 内）

对于 WSL 内的常规首次设置，请遵循 Linux 入门指南流程：

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm installpnpm buildpnpm ui:buildpnpm openclaw onboard --install-daemon
[/code]

如果你是从源码进行开发，而不是首次新手引导，请使用 [设置](</zh-CN/start/setup>) 中的源码开发循环：

bashCopy code
[code]
    pnpm install# First run only (or after resetting local OpenClaw config/workspace)pnpm openclaw setuppnpm gateway:watch
[/code]

完整指南：[入门指南](</zh-CN/start/getting-started>)

## Windows 配套应用

我们还没有 Windows 配套应用。如果你想帮助实现它，欢迎贡献。

## Git 和 GitHub 连接性（贡献者）

某些网络会阻止或限制到 GitHub 的 HTTPS。如果 `git clone` 因超时或连接重置而失败，请尝试其他网络、VPN，或你的组织提供的 HTTP/HTTPS 代理。

如果 `gh auth login` 在浏览器设备流程中失败（例如访问 `github.com:443` 超时），请改用个人访问令牌进行身份验证：

  1. 创建一个至少包含 `repo` 范围（经典 PAT）或等效精细粒度访问权限的令牌。
  2. 在当前会话的 PowerShell 中：

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token>"gh auth statusgh auth setup-git
[/code]

  3. 如果 `gh auth status` 警告缺少 `read:org`，请生成一个包含该范围的令牌并重新赋值变量：

powershellCopy code
[code]
    $env:GH_TOKEN="<your-token-with-repo-and-read:org>"gh auth status
[/code]

`gh auth refresh -s read:org` 只适用于你通过 `gh auth login` 进行身份验证并已存储可刷新的凭据时（不适用于使用 `GH_TOKEN` 的情况）。

切勿提交令牌，或将令牌粘贴到 issue 或 pull request 中。

## 相关

  * [安装概览](</zh-CN/install>)
  * [平台](</zh-CN/platforms>)


Was this useful?YesNo