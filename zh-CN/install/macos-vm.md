---
title: macOS 虚拟机
source_url: https://docs.openclaw.ai/zh-CN/install/macos-vm
scraped_at: 2026-05-25
---

## 推荐默认方案（大多数用户）

  * **小型 Linux VPS** ，用于始终在线的 Gateway 网关和低成本。参见 [VPS 托管](</zh-CN/vps>)。
  * 如果你想要完全控制，并且需要用于浏览器自动化的**住宅 IP** ，使用**专用硬件** （Mac mini 或 Linux 机器）。许多网站会阻止数据中心 IP，因此本地浏览通常效果更好。
  * **混合模式：** 将 Gateway 网关放在便宜的 VPS 上，并在需要浏览器/UI 自动化时将你的 Mac 作为**节点** 连接。参见 [节点](</zh-CN/nodes>) 和 [Gateway 网关远程访问](</zh-CN/gateway/remote>)。


当你明确需要仅限 macOS 的能力（例如 iMessage），或希望与你日常使用的 Mac 严格隔离时，使用 macOS VM。

## macOS VM 选项

### 在你的 Apple Silicon Mac 上运行本地 VM（Lume）

使用 [Lume](<https://cua.ai/docs/lume>)，在你现有的 Apple Silicon Mac 上的沙箱隔离 macOS VM 中运行 OpenClaw。

这会提供：

  * 隔离的完整 macOS 环境（你的宿主机保持干净）
  * 通过 `imsg` 支持 iMessage（默认本地路径在 Linux/Windows 上不可用）
  * 通过克隆 VM 实现即时重置
  * 无需额外硬件或云成本


### 托管 Mac 提供商（云）

如果你想在云端使用 macOS，托管 Mac 提供商也可以：

  * [MacStadium](<https://www.macstadium.com/>)（托管 Mac）
  * 其他托管 Mac 厂商也可使用；遵循它们的 VM + SSH 文档


一旦你获得 macOS VM 的 SSH 访问权限，请继续执行下面的第 6 步。

* * *

## 快速路径（Lume，适合有经验的用户）

  1. 安装 Lume
  2. `lume create openclaw --os macos --ipsw latest`
  3. 完成设置助理，启用远程登录（SSH）
  4. `lume run openclaw --no-display`
  5. SSH 进入，安装 OpenClaw，配置渠道
  6. 完成


* * *

## 你需要准备什么（Lume）

  * Apple Silicon Mac（M1/M2/M3/M4）
  * 宿主机运行 macOS Sequoia 或更高版本
  * 每个 VM 约 60 GB 可用磁盘空间
  * 约 20 分钟


* * *

## 1) 安装 Lume

bashCopy code
[code]
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/trycua/cua/main/libs/lume/scripts/install.sh)"
[/code]

如果 `~/.local/bin` 不在你的 PATH 中：

bashCopy code
[code]
    echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.zshrc && source ~/.zshrc
[/code]

验证：

bashCopy code
[code]
    lume --version
[/code]

文档：[Lume 安装](<https://cua.ai/docs/lume/guide/getting-started/installation>)

* * *

## 2) 创建 macOS VM

bashCopy code
[code]
    lume create openclaw --os macos --ipsw latest
[/code]

这会下载 macOS 并创建 VM。VNC 窗口会自动打开。

* * *

## 3) 完成设置助理

在 VNC 窗口中：

  1. 选择语言和地区
  2. 跳过 Apple ID（如果你之后想使用 iMessage，也可以登录）
  3. 创建用户账号（记住用户名和密码）
  4. 跳过所有可选功能


设置完成后，启用 SSH：

  1. 打开系统设置 → 通用 → 共享
  2. 启用“远程登录”


* * *

## 4) 获取 VM IP 地址

bashCopy code
[code]
    lume get openclaw
[/code]

查找 IP 地址（通常是 `192.168.64.x`）。

* * *

## 5) SSH 进入 VM

bashCopy code
[code]
    ssh youruser@192.168.64.X
[/code]

将 `youruser` 替换为你创建的账号，并将 IP 替换为你的 VM IP。

* * *

## 6) 安装 OpenClaw

在 VM 内：

bashCopy code
[code]
    npm install -g openclaw@latestopenclaw onboard --install-daemon
[/code]

按照新手引导提示设置你的模型提供商（Anthropic、OpenAI 等）。

* * *

## 7) 配置渠道

编辑配置文件：

bashCopy code
[code]
    nano ~/.openclaw/openclaw.json
[/code]

添加你的渠道：

json5Copy code
[code]
    {  channels: {    whatsapp: {      dmPolicy: "allowlist",      allowFrom: ["+15551234567"],    },    telegram: {      botToken: "YOUR_BOT_TOKEN",    },  },}
[/code]

然后登录 WhatsApp（扫描二维码）：

bashCopy code
[code]
    openclaw channels login
[/code]

* * *

## 8) 以无头模式运行 VM

停止 VM 并在无显示模式下重启：

bashCopy code
[code]
    lume stop openclawlume run openclaw --no-display
[/code]

VM 会在后台运行。OpenClaw 的守护进程会保持 Gateway 网关运行。

检查状态：

bashCopy code
[code]
    ssh youruser@192.168.64.X "openclaw status"
[/code]

* * *

## 额外内容：iMessage 集成

这是在 macOS 上运行的杀手级功能。使用 [iMessage](</zh-CN/channels/imessage>) 和 `imsg` 将“信息”加入 OpenClaw。

在 VM 内：

  1. 登录“信息”。
  2. 安装 `imsg`。
  3. 为运行 OpenClaw/`imsg` 的进程授予完全磁盘访问权限和自动化权限。
  4. 使用 `imsg rpc --help` 验证 RPC 支持。


添加到你的 OpenClaw 配置：

json5Copy code
[code]
    {  channels: {    imessage: {      enabled: true,      cliPath: "imsg",      dbPath: "~/Library/Messages/chat.db",    },  },}
[/code]

重启 Gateway 网关。现在你的智能体可以发送和接收 iMessage。

完整设置详情：[iMessage 渠道](</zh-CN/channels/imessage>)

* * *

## 保存黄金镜像

在进一步自定义之前，快照你的干净状态：

bashCopy code
[code]
    lume stop openclawlume clone openclaw openclaw-golden
[/code]

随时重置：

bashCopy code
[code]
    lume stop openclaw && lume delete openclawlume clone openclaw-golden openclawlume run openclaw --no-display
[/code]

* * *

## 24/7 运行

通过以下方式保持 VM 运行：

  * 让你的 Mac 保持接通电源
  * 在系统设置 → 节能中禁用睡眠
  * 如有需要，使用 `caffeinate`


若要真正始终在线，请考虑使用专用 Mac mini 或小型 VPS。参见 [VPS 托管](</zh-CN/vps>)。

* * *

## 故障排除

问题 | 解决方案  
---|---  
无法 SSH 进入 VM | 检查 VM 的系统设置中是否已启用“远程登录”  
VM IP 未显示 | 等待 VM 完全启动，然后再次运行 `lume get openclaw`  
找不到 Lume 命令 | 将 `~/.local/bin` 添加到你的 PATH  
WhatsApp 二维码无法扫描 | 运行 `openclaw channels login` 时，确保你已登录到 VM（而不是宿主机）  
  
* * *

## 相关文档

  * [VPS 托管](</zh-CN/vps>)
  * [节点](</zh-CN/nodes>)
  * [Gateway 网关远程访问](</zh-CN/gateway/remote>)
  * [iMessage 渠道](</zh-CN/channels/imessage>)
  * [Lume 快速开始](<https://cua.ai/docs/lume/guide/getting-started/quickstart>)
  * [Lume CLI 参考](<https://cua.ai/docs/lume/reference/cli-reference>)
  * [无人值守 VM 设置](<https://cua.ai/docs/lume/guide/fundamentals/unattended-setup>)（高级）
  * [Docker 沙箱隔离](</zh-CN/install/docker>)（替代隔离方案）


Was this useful?YesNo