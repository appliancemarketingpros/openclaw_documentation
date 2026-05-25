---
title: インストーラー内部
source_url: https://docs.openclaw.ai/ja-JP/install/installer
scraped_at: 2026-05-25
---

OpenClaw は、`openclaw.ai` から提供される 3 つのインストーラースクリプトを同梱しています。

スクリプト | プラットフォーム | 実行内容  
---|---|---  
`install.sh` | macOS / Linux / WSL | 必要に応じて Node をインストールし、npm (デフォルト) または git 経由で OpenClaw をインストールし、オンボーディングを実行できます。  
`install-cli.sh` | macOS / Linux / WSL | npm または git checkout モードで、Node + OpenClaw をローカルプレフィックス (`~/.openclaw`) にインストールします。root は不要です。  
`install.ps1` | Windows (PowerShell) | 必要に応じて Node をインストールし、npm (デフォルト) または git 経由で OpenClaw をインストールし、オンボーディングを実行できます。  
  
## クイックコマンド

### install.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --help
[/code]

### install-cli.sh

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --help
[/code]

### install.ps1

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag beta -NoOnboard -DryRun
[/code]

* * *

## [install.sh](<http://install.sh>)

### フロー ([install.sh](<http://install.sh>))

* ### Detect OS

macOS と Linux (WSL を含む) をサポートします。macOS が検出され、Homebrew がない場合はインストールします。

* ### Ensure Node.js 24 by default

Node バージョンを確認し、必要に応じて Node 24 をインストールします (macOS では Homebrew、Linux apt/dnf/yum では NodeSource セットアップスクリプト)。OpenClaw は互換性のため、現在 `22.16+` の Node 22 LTS も引き続きサポートします。

* ### Ensure Git

Git がない場合はインストールします。

* ### Install OpenClaw

  * `npm` メソッド (デフォルト): グローバル npm インストール
  * `git` メソッド: リポジトリを clone/update し、pnpm で依存関係をインストールし、build してから `~/.local/bin/openclaw` にラッパーをインストール


* ### Post-install tasks

  * 読み込み済みの gateway サービスをベストエフォートで更新します (`openclaw gateway install --force` の後に restart)
  * アップグレード時と git インストール時に `openclaw doctor --non-interactive` を実行します (ベストエフォート)
  * 条件が適切な場合にオンボーディングを試行します (TTY が利用可能、オンボーディングが無効化されていない、bootstrap/config チェックに合格)
  * デフォルトで `SHARP_IGNORE_GLOBAL_LIBVIPS=1` にします


### ソース checkout の検出

OpenClaw checkout (`package.json` \+ `pnpm-workspace.yaml`) 内で実行された場合、スクリプトは次を提示します。

  * checkout (`git`) を使用、または
  * グローバルインストール (`npm`) を使用


TTY が利用できず、インストールメソッドも設定されていない場合、デフォルトで `npm` になり、警告します。

無効なメソッド選択または無効な `--install-method` 値の場合、スクリプトはコード `2` で終了します。

### 例 ([install.sh](<http://install.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### Skip onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-onboard
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --install-method git
[/code]

### GitHub main via npm

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --version main
[/code]

### Dry run

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --dry-run
[/code]

Flags reference フラグ | 説明  
---|---  
`--install-method npm|git` | インストールメソッドを選択します (デフォルト: `npm`)。エイリアス: `--method`  
`--npm` | npm メソッドのショートカット  
`--git` | git メソッドのショートカット。エイリアス: `--github`  
`--version <version|dist-tag|spec>` | npm バージョン、dist-tag、またはパッケージ仕様 (デフォルト: `latest`)  
`--beta` | 利用可能な場合は beta dist-tag を使用し、それ以外は `latest` にフォールバック  
`--git-dir <path>` | Checkout ディレクトリ (デフォルト: `~/openclaw`)。エイリアス: `--dir`  
`--no-git-update` | 既存の checkout に対する `git pull` をスキップ  
`--no-prompt` | プロンプトを無効化  
`--no-onboard` | オンボーディングをスキップ  
`--onboard` | オンボーディングを有効化  
`--dry-run` | 変更を適用せずにアクションを出力  
`--verbose` | デバッグ出力を有効化 (`set -x`、npm notice レベルのログ)  
`--help` | 使用方法を表示 (`-h`)  
Environment variables reference 変数 | 説明  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | インストールメソッド  
`OPENCLAW_VERSION=latest|next|main|<semver>|<spec>` | npm バージョン、dist-tag、またはパッケージ仕様  
`OPENCLAW_BETA=0|1` | 利用可能な場合は beta を使用  
`OPENCLAW_GIT_DIR=<path>` | Checkout ディレクトリ  
`OPENCLAW_GIT_UPDATE=0|1` | git 更新を切り替え  
`OPENCLAW_NO_PROMPT=1` | プロンプトを無効化  
`OPENCLAW_NO_ONBOARD=1` | オンボーディングをスキップ  
`OPENCLAW_DRY_RUN=1` | ドライランモード  
`OPENCLAW_VERBOSE=1` | デバッグモード  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | npm ログレベル  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | sharp/libvips の動作を制御 (デフォルト: `1`)  
  
* * *

## [install-cli.sh](<http://install-cli.sh>)

### フロー ([install-cli.sh](<http://install-cli.sh>))

* ### Install local Node runtime

ピン留めされたサポート対象の Node LTS tarball (バージョンはスクリプトに埋め込まれ、独立して更新されます) を `<prefix>/tools/node-v<version>` にダウンロードし、SHA-256 を検証します。

* ### Ensure Git

Git がない場合、Linux では apt/dnf/yum、macOS では Homebrew 経由でインストールを試行します。

* ### Install OpenClaw under prefix

  * `npm` メソッド (デフォルト): プレフィックス配下に npm でインストールし、その後 `<prefix>/bin/openclaw` にラッパーを書き込みます
  * `git` メソッド: checkout (デフォルト `~/openclaw`) を clone/update し、引き続き `<prefix>/bin/openclaw` にラッパーを書き込みます


* ### Refresh loaded gateway service

Gateway サービスが同じプレフィックスからすでに読み込まれている場合、スクリプトは `openclaw gateway install --force`、続いて `openclaw gateway restart` を実行し、 ベストエフォートで Gateway のヘルスを調べます。

### 例 ([install-cli.sh](<http://install-cli.sh>))

### Default

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash
[/code]

### Custom prefix + version

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --prefix /opt/openclaw --version latest
[/code]

### Git install

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --install-method git --git-dir ~/openclaw
[/code]

### Automation JSON output

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### Run onboarding

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --onboard
[/code]

Flags reference フラグ | 説明  
---|---  
`--prefix <path>` | インストールプレフィックス (デフォルト: `~/.openclaw`)  
`--install-method npm|git` | インストールメソッドを選択します (デフォルト: `npm`)。エイリアス: `--method`  
`--npm` | npm メソッドのショートカット  
`--git`, `--github` | git メソッドのショートカット  
`--git-dir <path>` | Git checkout ディレクトリ (デフォルト: `~/openclaw`)。エイリアス: `--dir`  
`--version <ver>` | OpenClaw バージョンまたは dist-tag (デフォルト: `latest`)  
`--node-version <ver>` | Node バージョン (デフォルト: `22.22.0`)  
`--json` | NDJSON イベントを出力  
`--onboard` | インストール後に `openclaw onboard` を実行  
`--no-onboard` | オンボーディングをスキップ (デフォルト)  
`--set-npm-prefix` | Linux で、現在のプレフィックスが書き込み可能でない場合に npm プレフィックスを `~/.npm-global` に強制  
`--help` | 使用方法を表示 (`-h`)  
Environment variables reference 変数 | 説明  
---|---  
`OPENCLAW_PREFIX=<path>` | インストールプレフィックス  
`OPENCLAW_INSTALL_METHOD=git|npm` | インストール方法  
`OPENCLAW_VERSION=<ver>` | OpenClaw バージョンまたは dist-tag  
`OPENCLAW_NODE_VERSION=<ver>` | Node バージョン  
`OPENCLAW_GIT_DIR=<path>` | git インストール用の Git チェックアウトディレクトリ  
`OPENCLAW_GIT_UPDATE=0|1` | 既存チェックアウトの git 更新を切り替え  
`OPENCLAW_NO_ONBOARD=1` | オンボーディングをスキップ  
`OPENCLAW_NPM_LOGLEVEL=error|warn|notice` | npm ログレベル  
`SHARP_IGNORE_GLOBAL_LIBVIPS=0|1` | sharp/libvips の動作を制御 (デフォルト: `1`)  
  
* * *

## install.ps1

### フロー (install.ps1)

* ### PowerShell + Windows 環境を確認

PowerShell 5+ が必要です。

* ### デフォルトで Node.js 24 を確認

見つからない場合は、winget、次に Chocolatey、次に Scoop 経由でインストールを試みます。Node 22 LTS、現在は `22.16+` も互換性のため引き続きサポートされます。

* ### OpenClaw をインストール

  * `npm` 方法 (デフォルト): 選択した `-Tag` を使用してグローバル npm インストールを行います。`C:\` などの保護されたフォルダーで開いたシェルでも動作するよう、書き込み可能なインストーラー一時ディレクトリから起動されます
  * `git` 方法: リポジトリを clone/update し、pnpm で install/build して、`%USERPROFILE%\.local\bin\openclaw.cmd` にラッパーをインストールします


* ### インストール後のタスク

  * 可能な場合、必要な bin ディレクトリをユーザー PATH に追加します
  * 読み込まれている Gateway サービスをベストエフォートで更新します (`openclaw gateway install --force`、その後 restart)
  * アップグレードおよび git インストール時に `openclaw doctor --non-interactive` を実行します (ベストエフォート)


* ### 失敗の処理

`iwr ... | iex` と scriptblock インストールは、現在の PowerShell セッションを閉じずに終了エラーを報告します。直接の `powershell -File` / `pwsh -File` インストールは、自動化向けに引き続き非ゼロで終了します。

### 例 (install.ps1)

### デフォルト

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

### Git インストール

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git
[/code]

### npm 経由の GitHub main

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -Tag main
[/code]

### カスタム git ディレクトリ

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -InstallMethod git -GitDir "C:\openclaw"
[/code]

### ドライラン

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -DryRun
[/code]

### デバッグトレース

powershellCopy code
[code]
    # install.ps1 has no dedicated -Verbose flag yet.Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

フラグリファレンス フラグ | 説明  
---|---  
`-InstallMethod npm|git` | インストール方法 (デフォルト: `npm`)  
`-Tag <tag|version|spec>` | npm dist-tag、バージョン、またはパッケージ仕様 (デフォルト: `latest`)  
`-GitDir <path>` | チェックアウトディレクトリ (デフォルト: `%USERPROFILE%\openclaw`)  
`-NoOnboard` | オンボーディングをスキップ  
`-NoGitUpdate` | `git pull` をスキップ  
`-DryRun` | アクションのみを出力  
環境変数リファレンス 変数 | 説明  
---|---  
`OPENCLAW_INSTALL_METHOD=git|npm` | インストール方法  
`OPENCLAW_GIT_DIR=<path>` | チェックアウトディレクトリ  
`OPENCLAW_NO_ONBOARD=1` | オンボーディングをスキップ  
`OPENCLAW_GIT_UPDATE=0` | git pull を無効化  
`OPENCLAW_DRY_RUN=1` | ドライランモード  
  
* * *

## CI と自動化

予測可能な実行のため、非対話フラグ/環境変数を使用します。

### install.sh (非対話 npm)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash -s -- --no-prompt --no-onboard
[/code]

### install.sh (非対話 git)

bashCopy code
[code]
    OPENCLAW_INSTALL_METHOD=git OPENCLAW_NO_PROMPT=1 \  curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

### install-cli.sh (JSON)

bashCopy code
[code]
    curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install-cli.sh | bash -s -- --json --prefix /opt/openclaw
[/code]

### install.ps1 (オンボーディングをスキップ)

powershellCopy code
[code]
    & ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboard
[/code]

* * *

## トラブルシューティング

なぜ Git が必要ですか？

Git は `git` インストール方法に必要です。`npm` インストールでも、依存関係が git URL を使用するときの `spawn git ENOENT` 失敗を避けるため、Git は引き続き確認/インストールされます。

Linux で npm が EACCES になるのはなぜですか？

一部の Linux 環境では、npm グローバルプレフィックスが root 所有のパスを指しています。`install.sh` はプレフィックスを `~/.npm-global` に切り替え、シェル rc ファイルに PATH export を追記できます (それらのファイルが存在する場合)。

sharp/libvips の問題

スクリプトは、sharp がシステム libvips に対してビルドされるのを避けるため、デフォルトで `SHARP_IGNORE_GLOBAL_LIBVIPS=1` を使用します。上書きするには:

bashCopy code
[code]
    SHARP_IGNORE_GLOBAL_LIBVIPS=0 curl -fsSL --proto '=https' --tlsv1.2 https://openclaw.ai/install.sh | bash
[/code]

Windows: "npm error spawn git / ENOENT"

Git for Windows をインストールし、PowerShell を開き直して、インストーラーを再実行してください。

Windows: "openclaw is not recognized"

`npm config get prefix` を実行し、そのディレクトリをユーザー PATH に追加してください (Windows では `\bin` サフィックスは不要です)。その後、PowerShell を開き直してください。

Windows: 詳細なインストーラー出力を取得する方法

`install.ps1` は現在 `-Verbose` スイッチを公開していません。 スクリプトレベルの診断には PowerShell トレースを使用します:

powershellCopy code
[code]
    Set-PSDebug -Trace 1& ([scriptblock]::Create((iwr -useb https://openclaw.ai/install.ps1))) -NoOnboardSet-PSDebug -Trace 0
[/code]

インストール後に openclaw が見つからない

通常は PATH の問題です。[Node.js トラブルシューティング](</ja-JP/install/node#troubleshooting>)を参照してください。

## 関連

  * [インストール概要](</ja-JP/install>)
  * [更新](</ja-JP/install/updating>)
  * [アンインストール](</ja-JP/install/uninstall>)


Was this useful?YesNo