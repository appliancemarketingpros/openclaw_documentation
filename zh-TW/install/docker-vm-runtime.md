---
title: Docker 虛擬機執行環境
source_url: https://docs.openclaw.ai/zh-TW/install/docker-vm-runtime
scraped_at: 2026-05-25
---

以 VM 為基礎的 Docker 安裝共用執行階段步驟，例如 GCP、Hetzner，以及類似的 VPS 供應商。

## 將必要的二進位檔烘焙進映像檔

在執行中的容器內安裝二進位檔是一個陷阱。 任何在執行階段安裝的內容，都會在重新啟動後遺失。

Skills 所需的所有外部二進位檔，都必須在映像檔建置時安裝。

以下範例只展示三個常見二進位檔：

  * `gog`（來自 `gogcli`）用於 Gmail 存取
  * `goplaces` 用於 Google Places
  * `wacli` 用於 WhatsApp


這些是範例，不是完整清單。 你可以使用相同模式安裝所需的任意數量二進位檔。

如果你之後新增依賴其他二進位檔的 Skills，必須：

  1. 更新 Dockerfile
  2. 重新建置映像檔
  3. 重新啟動容器


**Dockerfile 範例**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## 建置並啟動

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

如果建置在 `pnpm install --frozen-lockfile` 期間因 `Killed` 或 `exit code 137` 失敗，表示 VM 記憶體不足。 請先使用更大的機器類型，再重試。

驗證二進位檔：

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

預期輸出：

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

驗證 Gateway：

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

預期輸出：

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## 什麼會持久化到哪裡

OpenClaw 在 Docker 中執行，但 Docker 不是事實來源。 所有長期狀態都必須在重新啟動、重新建置和重新開機後保留下來。

元件 | 位置 | 持久化機制 | 備註  
---|---|---|---  
Gateway 設定 | `/home/node/.openclaw/` | 主機磁碟區掛載 | 包含 `openclaw.json`、`.env`  
模型驗證設定檔 | `/home/node/.openclaw/agents/` | 主機磁碟區掛載 | `agents/<agentId>/agent/auth-profiles.json`（OAuth、API 金鑰）  
驗證設定檔金鑰 | `/home/node/.config/openclaw/` | 主機磁碟區掛載 | OAuth 驗證設定檔權杖材料的本機加密金鑰  
Skill 設定 | `/home/node/.openclaw/skills/` | 主機磁碟區掛載 | Skill 層級狀態  
Agent 工作區 | `/home/node/.openclaw/workspace/` | 主機磁碟區掛載 | 程式碼與 agent 成品  
WhatsApp 工作階段 | `/home/node/.openclaw/` | 主機磁碟區掛載 | 保留 QR 登入  
Gmail keyring | `/home/node/.openclaw/` | 主機磁碟區 + 密碼 | 需要 `GOG_KEYRING_PASSWORD`  
Plugin 套件 | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | 主機磁碟區掛載 | 可下載 Plugin 套件根目錄  
外部二進位檔 | `/usr/local/bin/` | Docker 映像檔 | 必須在建置時烘焙  
Node 執行階段 | 容器檔案系統 | Docker 映像檔 | 每次映像檔建置都會重新建置  
OS 套件 | 容器檔案系統 | Docker 映像檔 | 不要在執行階段安裝  
Docker 容器 | 暫時性 | 可重新啟動 | 可安全銷毀  
  
## 更新

若要在 VM 上更新 OpenClaw：

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## 相關

  * [Docker](</zh-TW/install/docker>)
  * [Podman](</zh-TW/install/podman>)
  * [ClawDock](</zh-TW/install/clawdock>)


Was this useful?YesNo