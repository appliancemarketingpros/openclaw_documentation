---
title: macOS 開発環境セットアップ
source_url: https://docs.openclaw.ai/ja-JP/platforms/mac/dev-setup
scraped_at: 2026-05-25
---

# macOS 開発者セットアップ

ソースから OpenClaw macOS アプリケーションをビルドして実行します。

## 前提条件

アプリをビルドする前に、以下がインストールされていることを確認してください。

  1. **Xcode 26.2+** : Swift 開発に必要です。
  2. **Node.js 24 & pnpm**: Gateway、CLI、パッケージングスクリプトに推奨されます。Node 22 LTS、現在は `22.16+`、も互換性のため引き続きサポートされています。


## 1\. 依存関係をインストールする

プロジェクト全体の依存関係をインストールします。

bashCopy code
[code]
    pnpm install
[/code]

## 2\. アプリをビルドしてパッケージ化する

macOS アプリをビルドし、`dist/OpenClaw.app` にパッケージ化するには、次を実行します。

bashCopy code
[code]
    ./scripts/package-mac-app.sh
[/code]

Apple Developer ID 証明書がない場合、スクリプトは自動的に **ad-hoc 署名** （`-`）を使用します。

開発実行モード、署名フラグ、Team ID のトラブルシューティングについては、macOS アプリの README を参照してください。 <https://github.com/openclaw/openclaw/blob/main/apps/macos/README.md>

> **注記** : ad-hoc 署名されたアプリでは、セキュリティプロンプトが表示される場合があります。アプリが「Abort trap 6」で即座にクラッシュする場合は、トラブルシューティングセクションを参照してください。

## 3\. CLI をインストールする

macOS アプリは、バックグラウンドタスクを管理するためにグローバルな `openclaw` CLI インストールを想定しています。

**インストール方法（推奨）:**

  1. OpenClaw アプリを開きます。
  2. **General** 設定タブに移動します。
  3. **「Install CLI」**をクリックします。


または、手動でインストールします。

bashCopy code
[code]
    npm install -g openclaw@<version>
[/code]

`pnpm add -g openclaw@<version>` と `bun add -g openclaw@<version>` も動作します。 Gateway ランタイムには、Node が引き続き推奨される方法です。

## トラブルシューティング

### ビルド失敗: ツールチェーンまたは SDK の不一致

macOS アプリのビルドは、最新の macOS SDK と Swift 6.2 ツールチェーンを想定しています。

**システム依存関係（必須）:**

  * **ソフトウェアアップデートで利用可能な最新の macOS バージョン** （Xcode 26.2 SDK で必要）
  * **Xcode 26.2** （Swift 6.2 ツールチェーン）


**確認:**

bashCopy code
[code]
    xcodebuild -versionxcrun swift --version
[/code]

バージョンが一致しない場合は、macOS/Xcode を更新してからビルドを再実行してください。

### 権限付与時にアプリがクラッシュする

**Speech Recognition** または **Microphone** アクセスを許可しようとしたときにアプリがクラッシュする場合、TCC キャッシュの破損または署名の不一致が原因である可能性があります。

**修正:**

  1. TCC 権限をリセットします。

bashCopy code
[code]tccutil reset All ai.openclaw.mac.debug
[/code]

  2. それでも失敗する場合は、[`scripts/package-mac-app.sh`](<https://github.com/openclaw/openclaw/blob/main/scripts/package-mac-app.sh>) の `BUNDLE_ID` を一時的に変更し、macOS から「clean slate」として扱われるようにします。


### Gateway が「Starting...」のままになる

Gateway のステータスが「Starting...」のままの場合は、ゾンビプロセスがポートを保持していないか確認してください。

bashCopy code
[code]
    openclaw gateway statusopenclaw gateway stop # LaunchAgent を使用していない場合（開発モード / 手動実行）、リスナーを探します。lsof -nP -iTCP:18789 -sTCP:LISTEN
[/code]

手動実行がポートを保持している場合は、そのプロセスを停止します（Ctrl+C）。最後の手段として、上で見つけた PID を kill します。

## 関連

  * [macOS アプリ](</ja-JP/platforms/macos>)
  * [インストール概要](</ja-JP/install>)


Was this useful?YesNo