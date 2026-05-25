---
title: Node.js
source_url: https://docs.openclaw.ai/ja-JP/install/node
scraped_at: 2026-05-25
---

OpenClaw には **Node 22.16 以降** が必要です。インストール、CI、リリースワークフローでは、**Node 24 がデフォルトかつ推奨ランタイム** です。Node 22 はアクティブな LTS 系列を通じて引き続きサポートされます。[インストーラースクリプト](</ja-JP/install#alternative-install-methods>)は Node を自動的に検出してインストールします。このページは、Node を自分でセットアップし、すべてが正しく接続されていること（バージョン、PATH、グローバルインストール）を確認したい場合のためのものです。

## バージョンを確認する

bashCopy code
[code]
    node -v
[/code]

これが `v24.x.x` 以上を出力する場合、推奨デフォルトを使用しています。`v22.16.x` 以上を出力する場合、サポート対象の Node 22 LTS パスを使用していますが、都合のよいタイミングで Node 24 へアップグレードすることを引き続き推奨します。Node がインストールされていない、またはバージョンが古すぎる場合は、以下からインストール方法を選んでください。

## Node をインストールする

### macOS

**Homebrew** （推奨）:

bashCopy code
[code]
    brew install node
[/code]

または [nodejs.org](<https://nodejs.org/>) から macOS インストーラーをダウンロードします。

### Linux

**Ubuntu / Debian:**

bashCopy code
[code]
    curl -fsSL https://deb.nodesource.com/setup_24.x | sudo -E bash -sudo apt-get install -y nodejs
[/code]

**Fedora / RHEL:**

bashCopy code
[code]
    sudo dnf install nodejs
[/code]

またはバージョンマネージャーを使用します（下記参照）。

### Windows

**winget** （推奨）:

powershellCopy code
[code]
    winget install OpenJS.NodeJS.LTS
[/code]

**Chocolatey:**

powershellCopy code
[code]
    choco install nodejs-lts
[/code]

または [nodejs.org](<https://nodejs.org/>) から Windows インストーラーをダウンロードします。

バージョンマネージャー（nvm、fnm、mise、asdf）を使用する

バージョンマネージャーを使うと、Node のバージョンを簡単に切り替えられます。よく使われる選択肢:

  * [**fnm**](<https://github.com/Schniz/fnm>) \- 高速でクロスプラットフォーム
  * [**nvm**](<https://github.com/nvm-sh/nvm>) \- macOS/Linux で広く使用されている
  * [**mise**](<https://mise.jdx.dev/>) \- ポリグロット（Node、Python、Ruby など）


fnm の例:

bashCopy code
[code]
    fnm install 24fnm use 24
[/code]

## トラブルシューティング

### `openclaw: command not found`

これはほとんどの場合、npm のグローバル bin ディレクトリが PATH に含まれていないことを意味します。

* ### グローバル npm prefix を見つける

bashCopy code
[code]
    npm prefix -g
[/code]

* ### PATH に含まれているか確認する

bashCopy code
[code]
    echo "$PATH"
[/code]

出力に `<npm-prefix>/bin`（macOS/Linux）または `<npm-prefix>`（Windows）があるか確認します。

* ### シェルの起動ファイルに追加する

### macOS / Linux

`~/.zshrc` または `~/.bashrc` に追加します:

bashCopy code
[code]
    export PATH="$(npm prefix -g)/bin:$PATH"
[/code]

その後、新しいターミナルを開きます（または zsh では `rehash`、bash では `hash -r` を実行します）。

### Windows

設定 → システム → 環境変数から、`npm prefix -g` の出力をシステム PATH に追加します。

### `npm install -g` での権限エラー（Linux）

`EACCES` エラーが表示される場合は、npm のグローバル prefix をユーザーが書き込み可能なディレクトリに切り替えます:

bashCopy code
[code]
    mkdir -p "$HOME/.npm-global"npm config set prefix "$HOME/.npm-global"export PATH="$HOME/.npm-global/bin:$PATH"
[/code]

永続化するには、`export PATH=...` 行を `~/.bashrc` または `~/.zshrc` に追加します。

## 関連

  * [インストール概要](</ja-JP/install>) \- すべてのインストール方法
  * [更新](</ja-JP/install/updating>) \- OpenClaw を最新の状態に保つ
  * [はじめに](</ja-JP/start/getting-started>) \- インストール後の最初の手順


Was this useful?YesNo