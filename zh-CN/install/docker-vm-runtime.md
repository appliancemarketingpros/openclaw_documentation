---
title: Docker VM 运行时
source_url: https://docs.openclaw.ai/zh-CN/install/docker-vm-runtime
scraped_at: 2026-05-25
---

基于 VM 的 Docker 安装（例如 GCP、Hetzner 和类似 VPS 提供商）的共享运行时步骤。

## 将所需二进制文件烘焙进镜像

在运行中的容器内安装二进制文件是一个陷阱。 运行时安装的任何内容都会在重启后丢失。

Skills 所需的所有外部二进制文件都必须在镜像构建时安装。

下面的示例只展示三个常见二进制文件：

  * `gog`（来自 `gogcli`），用于 Gmail 访问
  * `goplaces`，用于 Google Places
  * `wacli`，用于 WhatsApp


这些是示例，不是完整列表。 你可以使用相同模式安装所需数量的二进制文件。

如果你之后添加依赖额外二进制文件的新 Skills，必须：

  1. 更新 Dockerfile
  2. 重建镜像
  3. 重启容器


**Dockerfile 示例**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## 构建并启动

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

如果构建在 `pnpm install --frozen-lockfile` 期间因 `Killed` 或 `exit code 137` 失败，说明 VM 内存不足。 请使用更大的机器规格后再重试。

验证二进制文件：

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

预期输出：

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

验证 Gateway 网关：

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

预期输出：

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## 什么内容持久化在哪里

OpenClaw 在 Docker 中运行，但 Docker 不是事实来源。 所有长期状态都必须在重启、重建和重新启动系统后保留。

组件 | 位置 | 持久化机制 | 备注  
---|---|---|---  
Gateway 网关配置 | `/home/node/.openclaw/` | 主机卷挂载 | 包括 `openclaw.json`、`.env`  
模型认证配置文件 | `/home/node/.openclaw/agents/` | 主机卷挂载 | `agents/<agentId>/agent/auth-profiles.json`（OAuth、API 密钥）  
认证配置文件密钥 | `/home/node/.config/openclaw/` | 主机卷挂载 | OAuth 认证配置文件令牌材料的本地加密密钥  
Skill 配置 | `/home/node/.openclaw/skills/` | 主机卷挂载 | Skill 级状态  
Agent 工作区 | `/home/node/.openclaw/workspace/` | 主机卷挂载 | 代码和智能体工件  
WhatsApp 会话 | `/home/node/.openclaw/` | 主机卷挂载 | 保留二维码登录  
Gmail 密钥环 | `/home/node/.openclaw/` | 主机卷 + 密码 | 需要 `GOG_KEYRING_PASSWORD`  
插件包 | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | 主机卷挂载 | 可下载插件包根目录  
外部二进制文件 | `/usr/local/bin/` | Docker 镜像 | 必须在构建时烘焙  
Node 运行时 | 容器文件系统 | Docker 镜像 | 每次镜像构建都会重建  
OS 包 | 容器文件系统 | Docker 镜像 | 不要在运行时安装  
Docker 容器 | 临时性 | 可重启 | 可以安全销毁  
  
## 更新

要在 VM 上更新 OpenClaw：

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## 相关

  * [Docker](</zh-CN/install/docker>)
  * [Podman](</zh-CN/install/podman>)
  * [ClawDock](</zh-CN/install/clawdock>)


Was this useful?YesNo