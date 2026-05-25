---
title: はじめに
source_url: https://docs.openclaw.ai/ja-JP/start/getting-started
scraped_at: 2026-05-25
---

OpenClaw をインストールし、オンボーディングを実行して、AI アシスタントとチャットします — すべて 約 5 分で完了します。最後には、実行中の Gateway、設定済みの認証、 そして動作するチャットセッションが手に入ります。

## 必要なもの

  * **Node.js** — Node 24 推奨（Node 22.16+ もサポート）
  * モデルプロバイダー（Anthropic、OpenAI、Google など）の **API キー** — オンボーディングで入力を求められます


## クイックセットアップ

* ### OpenClaw をインストール

### macOS / Linux

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

![Install Script Process](/assets/install-script.svg)

### Windows (PowerShell)

powershellCopy code
[code]
    iwr -useb https://openclaw.ai/install.ps1 | iex
[/code]

* ### オンボーディングを実行

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

ウィザードは、モデルプロバイダーの選択、API キーの設定、 Gateway の設定を順に案内します。所要時間は約 2 分です。

完全なリファレンスは [オンボーディング（CLI）](</ja-JP/start/wizard>) を参照してください。

* ### Gateway が実行中であることを確認

bashCopy code
[code]
    openclaw gateway status
[/code]

Gateway がポート 18789 で待ち受けていることが表示されます。

* ### ダッシュボードを開く

bashCopy code
[code]
    openclaw dashboard
[/code]

これにより、ブラウザーで Control UI が開きます。読み込まれれば、すべて正常に動作しています。

* ### 最初のメッセージを送信

Control UI のチャットにメッセージを入力すると、AI から返信が届くはずです。

代わりにスマートフォンからチャットしたいですか？最速で設定できるチャンネルは [Telegram](</ja-JP/channels/telegram>)（ボットトークンだけ）です。すべての選択肢は [チャンネル](</ja-JP/channels>) を参照してください。

高度: カスタム Control UI ビルドをマウント

ローカライズまたはカスタマイズしたダッシュボードビルドを管理している場合は、 `gateway.controlUi.root` に、ビルド済みの静的 アセットと `index.html` を含むディレクトリを指定します。

bashCopy code
[code]
    mkdir -p "$HOME/.openclaw/control-ui-custom"# Copy your built static files into that directory.
[/code]

次に設定します。

jsonCopy code
[code]
    {"gateway": {  "controlUi": {    "enabled": true,    "root": "$HOME/.openclaw/control-ui-custom"  }}}
[/code]

Gateway を再起動し、ダッシュボードを開き直します。

bashCopy code
[code]
    openclaw gateway restartopenclaw dashboard
[/code]

## 次にやること

[**チャンネルに接続** Discord、Feishu、iMessage、Matrix、Microsoft Teams、Signal、Slack、Telegram、WhatsApp、Zalo など。 ](</ja-JP/channels>) [**ペアリングと安全性** エージェントにメッセージを送信できるユーザーを制御します。 ](</ja-JP/channels/pairing>) [**Gateway を設定** モデル、ツール、サンドボックス、高度な設定。 ](</ja-JP/gateway/configuration>) [**ツールを閲覧** ブラウザー、exec、Web 検索、Skills、Plugin。 ](</ja-JP/tools>)

高度: 環境変数

OpenClaw をサービスアカウントとして実行する場合や、カスタムパスを使いたい場合:

  * `OPENCLAW_HOME` — 内部パス解決のホームディレクトリ
  * `OPENCLAW_STATE_DIR` — 状態ディレクトリを上書き
  * `OPENCLAW_CONFIG_PATH` — 設定ファイルパスを上書き


完全なリファレンス: [環境変数](</ja-JP/help/environment>)。

## 関連

  * [インストール概要](</ja-JP/install>)
  * [チャンネル概要](</ja-JP/channels>)
  * [セットアップ](</ja-JP/start/setup>)


Was this useful?YesNo