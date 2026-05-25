---
title: Fly.io
source_url: https://docs.openclaw.ai/ja-JP/install/fly
scraped_at: 2026-05-25
---

**目標:** 永続ストレージ、自動 HTTPS、Discord/チャネルアクセスを備えた OpenClaw Gateway を [Fly.io](<https://fly.io>) マシン上で実行する。

## 必要なもの

  * [flyctl CLI](<https://fly.io/docs/hands-on/install-flyctl/>) のインストール
  * [Fly.io](<http://Fly.io>) アカウント（無料枠で可）
  * モデル認証: 選択したモデルプロバイダーの API キー
  * チャネル資格情報: Discord bot トークン、Telegram トークンなど


## 初心者向けの簡単な手順

  1. リポジトリをクローン → `fly.toml` をカスタマイズ
  2. アプリ + ボリュームを作成 → シークレットを設定
  3. `fly deploy` でデプロイ
  4. SSH で入って設定を作成するか、Control UI を使用


* ### Fly アプリを作成

bashCopy code
[code]
    # Clone the repogit clone https://github.com/openclaw/openclaw.gitcd openclaw # Create a new Fly app (pick your own name)fly apps create my-openclaw # Create a persistent volume (1GB is usually enough)fly volumes create openclaw_data --size 1 --region iad
[/code]

**ヒント:** 自分に近いリージョンを選択してください。一般的な選択肢: `lhr`（ロンドン）、`iad`（バージニア）、`sjc`（サンノゼ）。

* ### fly.toml を設定

`fly.toml` を編集して、アプリ名と要件に合わせます。

**セキュリティ注記:** デフォルト設定では公開 URL が公開されます。公開 IP なしの強化されたデプロイについては、プライベートデプロイ を参照するか、`deploy/fly.private.toml` を使用してください。

tomlCopy code
[code]
    app = "my-openclaw"  # Your app nameprimary_region = "iad" [build]  dockerfile = "Dockerfile" [env]  NODE_ENV = "production"  OPENCLAW_PREFER_PNPM = "1"  OPENCLAW_STATE_DIR = "/data"  NODE_OPTIONS = "--max-old-space-size=1536" [processes]  app = "node dist/index.js gateway --allow-unconfigured --port 3000 --bind lan" [http_service]  internal_port = 3000  force_https = true  auto_stop_machines = false  auto_start_machines = true  min_machines_running = 1  processes = ["app"] [[vm]]  size = "shared-cpu-2x"  memory = "2048mb" [mounts]  source = "openclaw_data"  destination = "/data"
[/code]

OpenClaw Docker イメージは `tini` を entrypoint として使用します。Fly のプロセスコマンドは Docker の `ENTRYPOINT` を置き換えずに `CMD` を置き換えるため、プロセスは引き続き `tini` の下で実行されます。

**主要な設定:**

設定 | 理由  
---|---  
`--bind lan` | Fly のプロキシが Gateway に到達できるように `0.0.0.0` にバインドします  
`--allow-unconfigured` | 設定ファイルなしで起動します（後で作成します）  
`internal_port = 3000` | Fly のヘルスチェック用に `--port 3000`（または `OPENCLAW_GATEWAY_PORT`）と一致させる必要があります  
`memory = "2048mb"` | 512MB は小さすぎます。2GB を推奨します  
`OPENCLAW_STATE_DIR = "/data"` | ボリューム上に状態を永続化します  
* ### シークレットを設定

bashCopy code
[code]
    # Required: Gateway token (for non-loopback binding)fly secrets set OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 32) # Model provider API keysfly secrets set ANTHROPIC_API_KEY=sk-ant-... # Optional: Other providersfly secrets set OPENAI_API_KEY=sk-...fly secrets set GOOGLE_API_KEY=... # Channel tokensfly secrets set DISCORD_BOT_TOKEN=MTQ...
[/code]

**注記:**

  * 非 loopback バインド（`--bind lan`）には有効な Gateway 認証パスが必要です。この [Fly.io](<http://Fly.io>) の例では `OPENCLAW_GATEWAY_TOKEN` を使用していますが、`gateway.auth.password` または正しく設定された非 loopback の `trusted-proxy` デプロイでも要件を満たします。
  * これらのトークンはパスワードのように扱ってください。
  * **すべての API キーとトークンには、設定ファイルよりも環境変数を優先してください** 。これにより、誤って公開またはログ出力される可能性がある `openclaw.json` にシークレットを入れずに済みます。


* ### デプロイ

bashCopy code
[code]
    fly deploy
[/code]

初回デプロイでは Docker イメージをビルドします（約 2〜3 分）。以降のデプロイはより高速です。

デプロイ後、確認します。

bashCopy code
[code]
    fly statusfly logs
[/code]

次のように表示されるはずです。

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:3000 (PID xxx)[discord] logged in to discord as xxx
[/code]

* ### 設定ファイルを作成

マシンに SSH で入り、適切な設定を作成します。

bashCopy code
[code]
    fly ssh console
[/code]

設定ディレクトリとファイルを作成します。

bashCopy code
[code]
    mkdir -p /datacat > /data/openclaw.json << 'EOF'{  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-opus-4-6",        "fallbacks": ["anthropic/claude-sonnet-4-6", "openai/gpt-5.4"]      },      "maxConcurrent": 4    },    "list": [      {        "id": "main",        "default": true      }    ]  },  "auth": {    "profiles": {      "anthropic:default": { "mode": "token", "provider": "anthropic" },      "openai:default": { "mode": "token", "provider": "openai" }    }  },  "bindings": [    {      "agentId": "main",      "match": { "channel": "discord" }    }  ],  "channels": {    "discord": {      "enabled": true,      "groupPolicy": "allowlist",      "guilds": {        "YOUR_GUILD_ID": {          "channels": { "general": { "allow": true } },          "requireMention": false        }      }    }  },  "gateway": {    "mode": "local",    "bind": "auto",    "controlUi": {      "allowedOrigins": [        "https://my-openclaw.fly.dev",        "http://localhost:3000",        "http://127.0.0.1:3000"      ]    }  },  "meta": {}}EOF
[/code]

**注記:** `OPENCLAW_STATE_DIR=/data` の場合、設定パスは `/data/openclaw.json` です。

**注記:** `https://my-openclaw.fly.dev` を実際の Fly アプリの origin に置き換えてください。Gateway の起動時には、ランタイムの `--bind` と `--port` の値からローカル Control UI の origin がシードされるため、 設定が存在する前でも初回起動を進められますが、 Fly 経由でブラウザアクセスするには、正確な HTTPS origin が `gateway.controlUi.allowedOrigins` に含まれている必要があります。

**注記:** Discord トークンは次のいずれかから取得できます。

  * 環境変数: `DISCORD_BOT_TOKEN`（シークレットには推奨）
  * 設定ファイル: `channels.discord.token`


環境変数を使用する場合、設定にトークンを追加する必要はありません。Gateway は `DISCORD_BOT_TOKEN` を自動的に読み取ります。

適用するために再起動します。

bashCopy code
[code]
    exitfly machine restart <machine-id>
[/code]

* ### Gateway にアクセス

### Control UI

ブラウザで開きます。

bashCopy code
[code]
    fly open
[/code]

または `https://my-openclaw.fly.dev/` にアクセスします。

設定済みの共有シークレットで認証します。このガイドでは `OPENCLAW_GATEWAY_TOKEN` の Gateway トークンを使用します。パスワード認証に切り替えた場合は、 代わりにそのパスワードを使用してください。

### ログ

bashCopy code
[code]
    fly logs              # Live logsfly logs --no-tail    # Recent logs
[/code]

### SSH コンソール

bashCopy code
[code]
    fly ssh console
[/code]

## トラブルシューティング

### 「App is not listening on expected address」

Gateway が `0.0.0.0` ではなく `127.0.0.1` にバインドしています。

**修正:** `fly.toml` のプロセスコマンドに `--bind lan` を追加します。

### ヘルスチェックの失敗 / 接続拒否

Fly が設定済みポートで Gateway に到達できません。

**修正:** `internal_port` が Gateway ポートと一致していることを確認してください（`--port 3000` または `OPENCLAW_GATEWAY_PORT=3000` を設定）。

### OOM / メモリ問題

コンテナが再起動し続ける、または強制終了されます。兆候: `SIGABRT`、`v8::internal::Runtime_AllocateInYoungGeneration`、または無言の再起動。

**修正:** `fly.toml` でメモリを増やします。

tomlCopy code
[code]
    [[vm]]  memory = "2048mb"
[/code]

または既存のマシンを更新します。

bashCopy code
[code]
    fly machine update <machine-id> --vm-memory 2048 -y
[/code]

**注記:** 512MB は小さすぎます。1GB でも動作する可能性はありますが、負荷時や詳細ログ有効時に OOM になることがあります。**2GB を推奨します。**

### Gateway ロックの問題

Gateway が「already running」エラーで起動を拒否します。

これはコンテナが再起動しても PID ロックファイルがボリューム上に残る場合に発生します。

**修正:** ロックファイルを削除します。

bashCopy code
[code]
    fly ssh console --command "rm -f /data/gateway.*.lock"fly machine restart <machine-id>
[/code]

ロックファイルは `/data/gateway.*.lock` にあります（サブディレクトリ内ではありません）。

### 設定が読み込まれない

`--allow-unconfigured` は起動ガードを迂回するだけです。`/data/openclaw.json` を作成または修復するわけではないため、通常のローカル Gateway 起動を行いたい場合は、実際の設定が存在し、`gateway.mode="local"` が含まれていることを確認してください。

設定が存在することを確認します。

bashCopy code
[code]
    fly ssh console --command "cat /data/openclaw.json"
[/code]

### SSH 経由で設定を書き込む

`fly ssh console -C` コマンドはシェルリダイレクトをサポートしていません。設定ファイルを書き込むには、次のようにします。

bashCopy code
[code]
    # Use echo + tee (pipe from local to remote)echo '{"your":"config"}' | fly ssh console -C "tee /data/openclaw.json" # Or use sftpfly sftp shell> put /local/path/config.json /data/openclaw.json
[/code]

**注記:** ファイルがすでに存在する場合、`fly sftp` が失敗することがあります。先に削除してください。

bashCopy code
[code]
    fly ssh console --command "rm /data/openclaw.json"
[/code]

### 状態が永続化されない

再起動後に認証プロファイル、チャネル/プロバイダー状態、またはセッションが失われる場合、 状態ディレクトリがコンテナファイルシステムに書き込まれています。

**修正:** `OPENCLAW_STATE_DIR=/data` が `fly.toml` に設定されていることを確認し、再デプロイします。

## 更新

bashCopy code
[code]
    # Pull latest changesgit pull # Redeployfly deploy # Check healthfly statusfly logs
[/code]

### マシンコマンドの更新

完全な再デプロイなしで起動コマンドを変更する必要がある場合:

bashCopy code
[code]
    # Get machine IDfly machines list # Update commandfly machine update <machine-id> --command "node dist/index.js gateway --port 3000 --bind lan" -y # Or with memory increasefly machine update <machine-id> --vm-memory 2048 --command "node dist/index.js gateway --port 3000 --bind lan" -y
[/code]

**注記:** `fly deploy` の後、マシンコマンドは `fly.toml` の内容にリセットされることがあります。手動変更を行った場合は、デプロイ後に再適用してください。

## プライベートデプロイ（強化）

デフォルトでは、Fly は公開 IP を割り当てるため、Gateway は `https://your-app.fly.dev` でアクセス可能になります。これは便利ですが、デプロイがインターネットスキャナー（Shodan、Censys など）から発見可能になることを意味します。

**公開露出なし** の強化されたデプロイには、プライベートテンプレートを使用してください。

### プライベートデプロイを使用する場合

  * **送信** の呼び出し/メッセージのみを行う（受信 Webhook なし）
  * Webhook コールバックに **ngrok または Tailscale** トンネルを使用する
  * ブラウザではなく **SSH、プロキシ、または WireGuard** 経由で Gateway にアクセスする
  * デプロイを **インターネットスキャナーから隠したい**


### セットアップ

標準設定の代わりに `deploy/fly.private.toml` を使用します。

bashCopy code
[code]
    # Deploy with private configfly deploy -c deploy/fly.private.toml
[/code]

または既存のデプロイを変換します。

bashCopy code
[code]
    # List current IPsfly ips list -a my-openclaw # Release public IPsfly ips release <public-ipv4> -a my-openclawfly ips release <public-ipv6> -a my-openclaw # Switch to private config so future deploys don't re-allocate public IPs# (remove [http_service] or deploy with the private template)fly deploy -c deploy/fly.private.toml # Allocate private-only IPv6fly ips allocate-v6 --private -a my-openclaw
[/code]

この後、`fly ips list` には `private` タイプの IP のみが表示されるはずです。

CodeCopy code
[code]
    VERSION  IP                   TYPE             REGIONv6       fdaa:x:x:x:x::x      private          global
[/code]

### プライベートデプロイへのアクセス

公開 URL がないため、次のいずれかの方法を使用します。

**オプション 1: ローカルプロキシ（最も簡単）**

bashCopy code
[code]
    # Forward local port 3000 to the appfly proxy 3000:3000 -a my-openclaw # Then open http://localhost:3000 in browser
[/code]

**オプション 2: WireGuard VPN**

bashCopy code
[code]
    # Create WireGuard config (one-time)fly wireguard create # Import to WireGuard client, then access via internal IPv6# Example: http://[fdaa:x:x:x:x::x]:3000
[/code]

**オプション 3: SSH のみ**

bashCopy code
[code]
    fly ssh console -a my-openclaw
[/code]

### プライベートデプロイでの Webhook

公開せずに Webhook コールバック (Twilio、Telnyx など) が必要な場合:

  1. **ngrok トンネル** \- コンテナ内またはサイドカーとして ngrok を実行
  2. **Tailscale Funnel** \- Tailscale 経由で特定のパスを公開
  3. **送信専用** \- 一部のプロバイダー (Twilio) は Webhook なしでも発信通話で問題なく動作します


ngrok を使った音声通話設定の例:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio",          tunnel: { provider: "ngrok" },          webhookSecurity: {            allowedHosts: ["example.ngrok.app"],          },        },      },    },  },}
[/code]

ngrok トンネルはコンテナ内で動作し、Fly アプリ自体を公開せずに公開 Webhook URL を提供します。転送されたホストヘッダーが受け入れられるように、`webhookSecurity.allowedHosts` を公開トンネルのホスト名に設定します。

### セキュリティ上の利点

観点 | パブリック | プライベート  
---|---|---  
インターネットスキャナー | 検出可能 | 非公開  
直接攻撃 | 可能 | ブロック  
コントロール UI アクセス | ブラウザ | プロキシ/VPN  
Webhook 配信 | 直接 | トンネル経由  
  
## メモ

  * [Fly.io](<http://Fly.io>) は **x86 アーキテクチャ** を使用します (ARM ではありません)
  * Dockerfile は両方のアーキテクチャに対応しています
  * WhatsApp/Telegram のオンボーディングには、`fly ssh console` を使用します
  * 永続データは `/data` のボリューム上にあります
  * Signal には Java + signal-cli が必要です。カスタムイメージを使用し、メモリは 2GB 以上に保ってください。


## コスト

推奨設定 (`shared-cpu-2x`、2GB RAM) の場合:

  * 使用量に応じて月額約 $10-15
  * 無料枠には一定の利用枠が含まれます


詳細は [Fly.io の料金](<https://fly.io/docs/about/pricing/>) を参照してください。

## 次のステップ

  * メッセージングチャネルを設定する: [チャネル](</ja-JP/channels>)
  * Gateway を設定する: [Gateway 設定](</ja-JP/gateway/configuration>)
  * OpenClaw を最新の状態に保つ: [更新](</ja-JP/install/updating>)


## 関連

  * [インストール概要](</ja-JP/install>)
  * [Hetzner](</ja-JP/install/hetzner>)
  * [Docker](</ja-JP/install/docker>)
  * [VPS ホスティング](</ja-JP/vps>)


Was this useful?YesNo