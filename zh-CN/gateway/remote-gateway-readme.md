---
title: 远程 Gateway 网关设置
source_url: https://docs.openclaw.ai/zh-CN/gateway/remote-gateway-readme
scraped_at: 2026-05-25
---

> 此内容已合并到 [远程访问](</zh-CN/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>)。当前指南请参见该页面。

# 使用远程 Gateway 网关运行 OpenClaw.app

OpenClaw.app 使用 SSH 隧道连接到远程 Gateway 网关。本指南将向你展示如何进行设置。

## 概览
[code] 
    flowchart TB
        subgraph Client["客户端机器"]
            direction TB
            A["OpenClaw.app"]
            B["ws://127.0.0.1:18789\n（本地端口）"]
            T["SSH 隧道"]
    
            A --> B
            B --> T
        end
        subgraph Remote["远程机器"]
            direction TB
            C["Gateway 网关 WebSocket"]
            D["ws://127.0.0.1:18789"]
    
            C --> D
        end
        T --> C
[/code]

## 快速开始

### 第 1 步：添加 SSH 配置

编辑 `~/.ssh/config` 并添加：

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # 例如：172.27.187.184    User &lt;REMOTE_USER&gt;            # 例如：jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

将 `&lt;REMOTE_IP&gt;` 和 `&lt;REMOTE_USER&gt;` 替换为你的实际值。

### 第 2 步：复制 SSH 密钥

将你的公钥复制到远程机器（输入一次密码）：

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### 第 3 步：配置远程 Gateway 网关认证

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

如果你的远程 Gateway 网关使用密码认证，请改用 `gateway.remote.password`。 `OPENCLAW_GATEWAY_TOKEN` 仍然可作为 shell 级覆盖使用，但持久化的远程客户端设置应使用 `gateway.remote.token` / `gateway.remote.password`。

### 第 4 步：启动 SSH 隧道

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### 第 5 步：重启 OpenClaw.app

bashCopy code
[code]
    # 退出 OpenClaw.app（⌘Q），然后重新打开：open /path/to/OpenClaw.app
[/code]

应用现在将通过 SSH 隧道连接到远程 Gateway 网关。

* * *

## 登录时自动启动隧道

如果你希望 SSH 隧道在登录时自动启动，可以创建一个 Launch Agent。

### 创建 PLIST 文件

将以下内容保存为 `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`：

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### 加载 Launch Agent

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

现在，该隧道将会：

  * 在你登录时自动启动
  * 如果崩溃会自动重启
  * 在后台持续运行


旧版说明：如果存在残留的 `com.openclaw.ssh-tunnel` LaunchAgent，请将其移除。

* * *

## 故障排除

**检查隧道是否正在运行：**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**重启隧道：**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**停止隧道：**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## 工作原理

组件 | 作用  
---|---  
`LocalForward 18789 127.0.0.1:18789` | 将本地端口 18789 转发到远程端口 18789  
`ssh -N` | SSH 连接但不执行远程命令（仅进行端口转发）  
`KeepAlive` | 如果隧道崩溃则自动重启  
`RunAtLoad` | 在代理加载时启动隧道  
  
OpenClaw.app 会连接到你客户端机器上的 `ws://127.0.0.1:18789`。SSH 隧道会将该连接转发到远程机器上的 18789 端口，也就是 Gateway 网关运行的端口。

## 相关内容

  * [远程访问](</zh-CN/gateway/remote>)
  * [Tailscale](</zh-CN/gateway/tailscale>)


Was this useful?YesNo