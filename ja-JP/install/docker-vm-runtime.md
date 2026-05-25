---
title: Docker VM ランタイム
source_url: https://docs.openclaw.ai/ja-JP/install/docker-vm-runtime
scraped_at: 2026-05-25
---

GCP、Hetzner、および類似の VPS プロバイダーなど、VM ベースの Docker インストール向けの共有ランタイム手順。

## 必須バイナリをイメージに焼き込む

実行中のコンテナ内でバイナリをインストールするのは落とし穴です。 ランタイムでインストールされたものは、再起動時に失われます。

Skillsが必要とするすべての外部バイナリは、イメージのビルド時にインストールする必要があります。

以下の例では、一般的な 3 つのバイナリのみを示します。

  * Gmail アクセス用の `gog`（`gogcli` から）
  * Google Places 用の `goplaces`
  * WhatsApp 用の `wacli`


これらは例であり、完全な一覧ではありません。 同じパターンを使って、必要なだけバイナリをインストールできます。

後で追加のバイナリに依存する新しい Skills を追加する場合は、次を行う必要があります。

  1. Dockerfile を更新する
  2. イメージを再ビルドする
  3. コンテナを再起動する


**Dockerfile の例**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## ビルドして起動する

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

`pnpm install --frozen-lockfile` の実行中に `Killed` または `exit code 137` でビルドが失敗する場合、VM のメモリが不足しています。 再試行する前に、より大きなマシンクラスを使用してください。

バイナリを検証します。

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

期待される出力:

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

Gateway を検証します。

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

期待される出力:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## 何がどこに永続化されるか

OpenClaw は Docker 内で実行されますが、Docker は信頼できる唯一の情報源ではありません。 すべての長期状態は、再起動、再ビルド、リブートをまたいで保持される必要があります。

コンポーネント | 場所 | 永続化メカニズム | 備考  
---|---|---|---  
Gateway 設定 | `/home/node/.openclaw/` | ホストボリュームマウント | `openclaw.json`、`.env` を含む  
モデル認証プロファイル | `/home/node/.openclaw/agents/` | ホストボリュームマウント | `agents/<agentId>/agent/auth-profiles.json`（OAuth、API キー）  
認証プロファイルキー | `/home/node/.config/openclaw/` | ホストボリュームマウント | OAuth 認証プロファイルのトークン素材用ローカル暗号化キー  
Skill 設定 | `/home/node/.openclaw/skills/` | ホストボリュームマウント | Skill レベルの状態  
エージェントワークスペース | `/home/node/.openclaw/workspace/` | ホストボリュームマウント | コードとエージェント成果物  
WhatsApp セッション | `/home/node/.openclaw/` | ホストボリュームマウント | QR ログインを保持  
Gmail キーリング | `/home/node/.openclaw/` | ホストボリューム + パスワード | `GOG_KEYRING_PASSWORD` が必要  
Plugin パッケージ | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | ホストボリュームマウント | ダウンロード可能な Plugin パッケージルート  
外部バイナリ | `/usr/local/bin/` | Docker イメージ | ビルド時に焼き込む必要がある  
Node ランタイム | コンテナファイルシステム | Docker イメージ | イメージビルドごとに再ビルドされる  
OS パッケージ | コンテナファイルシステム | Docker イメージ | ランタイムでインストールしない  
Docker コンテナ | 一時的 | 再起動可能 | 破棄しても安全  
  
## 更新

VM 上の OpenClaw を更新するには:

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## 関連

  * [Docker](</ja-JP/install/docker>)
  * [Podman](</ja-JP/install/podman>)
  * [ClawDock](</ja-JP/install/clawdock>)


Was this useful?YesNo