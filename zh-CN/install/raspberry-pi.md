---
title: Raspberry Pi
source_url: https://docs.openclaw.ai/zh-CN/install/raspberry-pi
scraped_at: 2026-05-25
---

在 Raspberry Pi 上运行持久、常驻的 OpenClaw Gateway 网关。由于 Pi 只是 Gateway 网关（模型通过 API 在云端运行），即使是配置适中的 Pi 也能很好地处理工作负载——典型硬件成本为**一次性 35–80 美元** ，没有月费。

## 硬件兼容性

Pi 型号 | RAM | 可用？ | 备注  
---|---|---|---  
Pi 5 | 4/8 GB | 最佳 | 速度最快，推荐。  
Pi 4 | 4 GB | 良好 | 适合大多数用户的最佳选择。  
Pi 4 | 2 GB | 可以 | 添加交换空间。  
Pi 4 | 1 GB | 紧张 | 可通过交换空间和最小配置运行。  
Pi 3B+ | 1 GB | 较慢 | 可用但响应迟缓。  
Pi Zero 2 W | 512 MB | 不可用 | 不推荐。  
  
**最低要求：**1 GB RAM、1 个核心、500 MB 可用磁盘空间、64 位操作系统。 **推荐配置：**2 GB+ RAM、16 GB+ SD 卡（或 USB SSD）、以太网。

## 前提条件

  * 配备 2 GB+ RAM 的 Raspberry Pi 4 或 5（推荐 4 GB）
  * MicroSD 卡（16 GB+）或 USB SSD（性能更好）
  * 官方 Pi 电源
  * 网络连接（以太网或 WiFi）
  * 64 位 Raspberry Pi OS（必需 -- 不要使用 32 位）
  * 大约 30 分钟


## 设置

* ### Flash the OS

使用 **Raspberry Pi OS Lite（64 位）** \-- 无头服务器不需要桌面环境。

  1. 下载 [Raspberry Pi Imager](<https://www.raspberrypi.com/software/>)。
  2. 选择操作系统：**Raspberry Pi OS Lite（64 位）** 。
  3. 在设置对话框中预先配置： 
     * 主机名：`gateway-host`
     * 启用 SSH
     * 设置用户名和密码
     * 配置 WiFi（如果不使用以太网）
  4. 写入到你的 SD 卡或 USB 驱动器，插入并启动 Pi。


* ### Connect via SSH

bashCopy code
[code]
    ssh user@gateway-host
[/code]

* ### Update the system

bashCopy code
[code]
    sudo apt update && sudo apt upgrade -ysudo apt install -y git curl build-essential # Set timezone (important for cron and reminders)sudo timedatectl set-timezone America/Chicago
[/code]

* ### Install Node.js 24

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt install -y nodejsnode --version
[/code]

* ### Add swap (important for 2 GB or less)

bashCopy code
[code]
    sudo fallocate -l 2G /swapfilesudo chmod 600 /swapfilesudo mkswap /swapfilesudo swapon /swapfileecho '/swapfile none swap sw 0 0' | sudo tee -a /etc/fstab # Reduce swappiness for low-RAM devicesecho 'vm.swappiness=10' | sudo tee -a /etc/sysctl.confsudo sysctl -p
[/code]

* ### Install OpenClaw

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

按照向导操作。对于无头设备，推荐使用 API key 而不是 OAuth。Telegram 是最容易开始使用的渠道。

* ### Verify

bashCopy code
[code]
    openclaw statussystemctl --user status openclaw-gateway.servicejournalctl --user -u openclaw-gateway.service -f
[/code]

* ### Access the Control UI

在你的计算机上，从 Pi 获取一个仪表板 URL：

bashCopy code
[code]
    ssh user@gateway-host 'openclaw dashboard --no-open'
[/code]

然后在另一个终端中创建 SSH 隧道：

bashCopy code
[code]
    ssh -N -L 18789:127.0.0.1:18789 user@gateway-host
[/code]

在本地浏览器中打开打印出的 URL。对于常驻远程访问，请参阅 [Tailscale 集成](</zh-CN/gateway/tailscale>)。

## 性能建议

**使用 USB SSD** \-- SD 卡速度慢且容易损耗。USB SSD 可以显著提升性能。请参阅 [Pi USB 启动指南](<https://www.raspberrypi.com/documentation/computers/raspberry-pi.html#usb-mass-storage-boot>)。

**启用模块编译缓存** \-- 加快低功耗 Pi 主机上的重复 CLI 调用：

bashCopy code
[code]
    grep -q 'NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cache' ~/.bashrc || cat >> ~/.bashrc <<'EOF' # pragma: allowlist secretexport NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cachemkdir -p /var/tmp/openclaw-compile-cacheexport OPENCLAW_NO_RESPAWN=1EOFsource ~/.bashrc
[/code]

**降低内存使用量** \-- 对于无头设置，释放 GPU 内存并禁用未使用的服务：

bashCopy code
[code]
    echo 'gpu_mem=16' | sudo tee -a /boot/config.txtsudo systemctl disable bluetooth
[/code]

**用于稳定重启的 systemd drop-in** \-- 如果这个 Pi 主要用于运行 OpenClaw，请添加一个服务 drop-in：

bashCopy code
[code]
    systemctl --user edit openclaw-gateway.service
[/code]

iniCopy code
[code]
    [Service]Environment=OPENCLAW_NO_RESPAWN=1Environment=NODE_COMPILE_CACHE=/var/tmp/openclaw-compile-cacheRestart=alwaysRestartSec=2TimeoutStartSec=90
[/code]

然后运行 `systemctl --user daemon-reload && systemctl --user restart openclaw-gateway.service`。在无头 Pi 上，还要启用一次 lingering，确保用户服务在注销后仍然存活：`sudo loginctl enable-linger "$(whoami)"`。

## 推荐模型设置

由于 Pi 只运行 Gateway 网关，请使用云托管 API 模型：

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-sonnet-4-6",        "fallbacks": ["openai/gpt-5.4-mini"]      }    }  }}
[/code]

不要在 Pi 上运行本地 LLM——即使是小模型也慢到不实用。让 Claude 或 GPT 处理模型工作。

## ARM 二进制文件说明

大多数 OpenClaw 功能无需更改即可在 ARM64 上运行（Node.js、Telegram、WhatsApp/Baileys、Chromium）。偶尔缺少 ARM 构建的二进制文件通常是由 Skills 提供的可选 Go/Rust CLI 工具。在回退到从源代码构建之前，请检查缺失二进制文件的发布页面是否提供 `linux-arm64` / `aarch64` 构件。

## 持久化和备份

OpenClaw 状态位于：

  * `~/.openclaw/` — `openclaw.json`、每个智能体的 `auth-profiles.json`、渠道/提供商状态、会话。
  * `~/.openclaw/workspace/` — Agent 工作区（[SOUL.md](<http://SOUL.md>)、记忆、构件）。


这些内容会在重启后保留。使用以下命令创建可移植快照：

bashCopy code
[code]
    openclaw backup create
[/code]

如果你将这些内容保存在 SSD 上，性能和寿命都会优于 SD 卡。

## 故障排除

**内存不足** \-- 使用 `free -h` 验证交换空间是否处于活动状态。禁用未使用的服务（`sudo systemctl disable cups bluetooth avahi-daemon`）。仅使用基于 API 的模型。

**性能缓慢** \-- 使用 USB SSD 代替 SD 卡。用 `vcgencmd get_throttled` 检查 CPU 是否降频（应返回 `0x0`）。

**服务无法启动** \-- 使用 `journalctl --user -u openclaw-gateway.service --no-pager -n 100` 查看日志，并运行 `openclaw doctor --non-interactive`。如果这是无头 Pi，还要验证 lingering 已启用：`sudo loginctl enable-linger "$(whoami)"`。

**ARM 二进制文件问题** \-- 如果某个 skill 因 “exec format error” 失败，请检查该二进制文件是否有 ARM64 构建。使用 `uname -m` 验证架构（应显示 `aarch64`）。

**WiFi 掉线** \-- 禁用 WiFi 电源管理：`sudo iwconfig wlan0 power off`。

## 后续步骤

  * [渠道](</zh-CN/channels>) \-- 连接 Telegram、WhatsApp、Discord 等
  * [Gateway 网关配置](</zh-CN/gateway/configuration>) \-- 所有配置选项
  * [更新](</zh-CN/install/updating>) \-- 让 OpenClaw 保持最新


## 相关内容

  * [安装概览](</zh-CN/install>)
  * [Linux 服务器](</zh-CN/vps>)
  * [平台](</zh-CN/platforms>)


Was this useful?YesNo