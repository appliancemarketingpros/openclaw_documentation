---
title: exe.dev
source_url: https://docs.openclaw.ai/zh-CN/install/exe-dev
scraped_at: 2026-05-25
---

目标：OpenClaw Gateway 网关在 exe.dev VM 上运行，并可从你的笔记本电脑通过以下地址访问：`https://<vm-name>.exe.xyz`

本页假设使用 exe.dev 默认的 **exeuntu** 镜像。如果你选择了其他发行版，请相应映射软件包。

## 初学者快速路径

  1. <https://exe.new/openclaw>
  2. 按需填写你的认证密钥/token
  3. 点击 VM 旁边的“智能体”，并等待 Shelley 完成预配
  4. 打开 `https://<vm-name>.exe.xyz/`，并使用配置的共享密钥进行认证（本指南默认使用 token 认证，但如果你切换 `gateway.auth.mode`，密码认证也可用）
  5. 使用 `openclaw devices approve <requestId>` 批准任何待处理的设备配对请求


## 你需要准备

  * exe.dev 账户
  * 对 [exe.dev](<https://exe.dev>) 虚拟机的 `ssh exe.dev` 访问权限（可选）


## 使用 Shelley 自动安装

Shelley 是 [exe.dev](<https://exe.dev>) 的智能体，可以使用我们的提示词即时安装 OpenClaw。使用的提示词如下：

CodeCopy code
[code]
    Set up OpenClaw (https://docs.openclaw.ai/install) on this VM. Use the non-interactive and accept-risk flags for openclaw onboarding. Add the supplied auth or token as needed. Configure nginx to forward from the default port 18789 to the root location on the default enabled site config, making sure to enable Websocket support. Pairing is done by "openclaw devices list" and "openclaw devices approve <request id>". Make sure the dashboard shows that OpenClaw's health is OK. exe.dev handles forwarding from port 8000 to port 80/443 and HTTPS for us, so the final "reachable" should be <vm-name>.exe.xyz, without port specification.
[/code]

## 手动安装

## 1) 创建 VM

从你的设备运行：

bashCopy code
[code]
    ssh exe.dev new
[/code]

然后连接：

bashCopy code
[code]
    ssh <vm-name>.exe.xyz
[/code]

## 2) 安装前置依赖（在 VM 上）

bashCopy code
[code]
    sudo apt-get updatesudo apt-get install -y git curl jq ca-certificates openssl
[/code]

## 3) 安装 OpenClaw

运行 OpenClaw 安装脚本：

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

## 4) 设置 nginx，将 OpenClaw 代理到端口 8000

使用以下内容编辑 `/etc/nginx/sites-enabled/default`

CodeCopy code
[code]
    server {    listen 80 default_server;    listen [::]:80 default_server;    listen 8000;    listen [::]:8000;     server_name _;     location / {        proxy_pass http://127.0.0.1:18789;        proxy_http_version 1.1;         # WebSocket support        proxy_set_header Upgrade $http_upgrade;        proxy_set_header Connection "upgrade";         # Standard proxy headers        proxy_set_header Host $host;        proxy_set_header X-Real-IP $remote_addr;        proxy_set_header X-Forwarded-For $remote_addr;        proxy_set_header X-Forwarded-Proto $scheme;         # Timeout settings for long-lived connections        proxy_read_timeout 86400s;        proxy_send_timeout 86400s;    }}
[/code]

覆盖转发标头，而不是保留客户端提供的链。 OpenClaw 只信任来自显式配置代理的转发 IP 元数据， 而追加式 `X-Forwarded-For` 链会被视为强化安全风险。

## 5) 访问 OpenClaw 并授予权限

访问 `https://<vm-name>.exe.xyz/`（参见新手引导中的 Control UI 输出）。如果它提示认证，请粘贴来自 VM 的已配置共享密钥。本指南使用 token 认证，因此使用 `openclaw config get gateway.auth.token` 获取 `gateway.auth.token`（或使用 `openclaw doctor --generate-gateway-token` 生成一个）。 如果你已将 Gateway 网关改为密码认证，请改用 `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD`。 使用 `openclaw devices list` 和 `openclaw devices approve <requestId>` 批准设备。不确定时，就从浏览器使用 Shelley！

## 远程渠道设置

对于远程主机，优先使用一次 `config patch` 调用，而不是多次 SSH 调用 `config set`。将真实 token 保存在 VM 环境或 `~/.openclaw/.env` 中，并且只在 `openclaw.json` 中放置 SecretRefs。

在 VM 上，让服务环境包含它所需的机密：

bashCopy code
[code]
    cat >> ~/.openclaw/.env <<'EOF'SLACK_BOT_TOKEN=xoxb-...SLACK_APP_TOKEN=xapp-...DISCORD_BOT_TOKEN=...OPENAI_API_KEY=sk-...EOF
[/code]

从你的本地机器创建补丁文件，并将其通过管道传给 VM：

json5Copy code
[code]
    // openclaw.remote.patch.json5{  secrets: {    providers: {      default: { source: "env" },    },  },  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --dry-run' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw config patch --stdin' < ./openclaw.remote.patch.json5ssh <vm-name>.exe.xyz 'openclaw gateway restart && openclaw health'
[/code]

当嵌套允许列表应当精确变为补丁值时，使用 `--replace-path`，例如替换 Discord 渠道允许列表时：

bashCopy code
[code]
    ssh <vm-name>.exe.xyz 'openclaw config patch --stdin --replace-path "channels.discord.guilds[\"123\"].channels"' < ./discord.patch.json5
[/code]

## 远程访问

远程访问由 [exe.dev](<https://exe.dev>) 的认证处理。默认情况下，来自端口 8000 的 HTTP 流量会通过电子邮件认证转发到 `https://<vm-name>.exe.xyz`。

## 更新

bashCopy code
[code]
    npm i -g openclaw@latestopenclaw doctoropenclaw gateway restartopenclaw health
[/code]

指南：[更新](</zh-CN/install/updating>)

## 相关内容

  * [远程 Gateway 网关](</zh-CN/gateway/remote>)
  * [安装概览](</zh-CN/install>)


Was this useful?YesNo