---
title: インストール
source_url: https://docs.openclaw.ai/ja-JP/install
scraped_at: 2026-05-25
---

## システム要件

  * **Node 24** （推奨）または Node 22.16+ - インストーラースクリプトがこれを自動的に処理します
  * **macOS、Linux、または Windows** \- ネイティブ Windows と WSL2 の両方に対応しています。WSL2 のほうが安定しています。[Windows](</ja-JP/platforms/windows>) を参照してください。
  * ソースからビルドする場合のみ `pnpm` が必要です


## 推奨: インストーラースクリプト

最速のインストール方法です。OS を検出し、必要に応じて Node をインストールし、OpenClaw をインストールして、オンボーディングを起動します。

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

オンボーディングを実行せずにインストールするには:

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

すべてのフラグと CI/自動化オプションについては、[インストーラー内部](</ja-JP/install/installer>) を参照してください。

## 代替インストール方法

### ローカルプレフィックスインストーラー (`install-cli.sh`)

システム全体の Node インストールに依存せず、OpenClaw と Node を `~/.openclaw` のようなローカルプレフィックスの下に保持したい場合に使用します:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install-cli.sh | bash
[/code]

デフォルトで npm インストールに対応し、同じプレフィックスフローの下での git チェックアウトインストールにも対応しています。完全なリファレンス: [インストーラー内部](</ja-JP/install/installer#install-clish>)。

すでにインストール済みですか? `openclaw update --channel dev` と `openclaw update --channel stable` でパッケージインストールと git インストールを切り替えられます。 [更新](</ja-JP/install/updating#switch-between-npm-and-git-installs>) を参照してください。

### npm、pnpm、または bun

Node を自分で管理している場合:

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

Troubleshooting: sharp build errors (npm)

グローバルにインストールされた libvips が原因で `sharp` が失敗する場合:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=1 npm install -g openclaw@latest
[/code]

### ソースから

コントリビューター、またはローカルチェックアウトから実行したい場合:

bashCopy code
[code]
    git clone https://github.com/openclaw/openclaw.gitcd openclawpnpm install && pnpm build && pnpm ui:buildpnpm link --globalopenclaw onboard --install-daemon
[/code]

またはリンクを省略し、リポジトリ内から `pnpm openclaw ...` を使用します。完全な開発ワークフローについては [セットアップ](</ja-JP/start/setup>) を参照してください。

### GitHub main からインストール

bashCopy code
[code]
    npm install -g github:openclaw/openclaw#main
[/code]

### コンテナとパッケージマネージャー

[**Docker** コンテナ化された、またはヘッドレスなデプロイ。 ](</ja-JP/install/docker>) [**Podman** Docker に代わるルートレスコンテナ。 ](</ja-JP/install/podman>) [**Nix** Nix flake による宣言的インストール。 ](</ja-JP/install/nix>) [**Ansible** 自動化されたフリートプロビジョニング。 ](</ja-JP/install/ansible>) [**Bun** Bun ランタイムによる CLI のみの使用。 ](</ja-JP/install/bun>)

## インストールを確認する

bashCopy code
[code]
    openclaw --version      # confirm the CLI is availableopenclaw doctor         # check for config issuesopenclaw gateway status # verify the Gateway is running
[/code]

インストール後に管理された起動を使いたい場合:

  * macOS: `openclaw onboard --install-daemon` または `openclaw gateway install` による LaunchAgent
  * Linux/WSL2: 同じコマンドによる systemd ユーザーサービス
  * ネイティブ Windows: まず Scheduled Task を使用し、タスク作成が拒否された場合はユーザーごとの Startup フォルダーのログイン項目にフォールバック


## ホスティングとデプロイ

OpenClaw をクラウドサーバーまたは VPS にデプロイします:

[**VPS** [**Docker VM** [**Kubernetes** OPENCLAW_DOCS_MARKER:cardOpen:IHRpdGxlPSJGbHkuaW8iIGhyZWY9Ii9qYS1KUC9pbnN0YWxsL2ZseSI [Fly.io](<http://Fly.io>) OPENCLAW_DOCS_MARKER:cardClose: [**Hetzner** [**GCP** [**Azure** [**Railway** [**Render** [**Northflank** 更新、移行、またはアンインストール [**Updating** OpenClaw を最新の状態に保ちます。 ](</ja-JP/install/updating>) [**Migrating** 新しいマシンへ移動します。 ](</ja-JP/install/migrating>) [**Uninstall** OpenClaw を完全に削除します。 ](</ja-JP/install/uninstall>) トラブルシューティング: `openclaw` が見つからない インストールは成功したが、ターミナルで `openclaw` が見つからない場合: bashCopy code
[code]
    node -v           # Node installed?npm prefix -g     # Where are global packages?echo "$PATH"      # Is the global bin dir in PATH?
[/code]

`$(npm prefix -g)/bin` が `$PATH` に含まれていない場合は、シェル起動ファイル（`~/.zshrc` または `~/.bashrc`）に追加してください: bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

その後、新しいターミナルを開きます。詳細については [Node セットアップ](</ja-JP/install/node>) を参照してください。 ](</ja-JP/install/northflank>) Was this useful?YesNo ](</ja-JP/install/render>)](</ja-JP/install/railway>)](</ja-JP/install/azure>)](</ja-JP/install/gcp>)](</ja-JP/install/hetzner>)](</ja-JP/install/kubernetes>)](</ja-JP/install/docker-vm-runtime>)](</ja-JP/vps>)