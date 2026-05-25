---
title: OpenClaw
source_url: https://docs.openclaw.ai/ja-JP
scraped_at: 2026-05-25
---

# OpenClaw 🦞

![OpenClaw](/assets/openclaw-logo-text-dark.png) ![OpenClaw](/assets/openclaw-logo-text.png)

> _「EXFOLIATE! EXFOLIATE!」_ — たぶん宇宙ロブスター

**Discord、Google Chat、iMessage、Matrix、Microsoft Teams、Signal、Slack、Telegram、WhatsApp、Zalo などを横断してAIエージェントを利用するための、任意のOSで動く Gateway。**

メッセージを送ると、ポケットの中からエージェントの応答を受け取れます。組み込みチャネル、同梱チャネル Plugin、WebChat、モバイルノードをまたいで、1つの Gateway を実行します。

[**開始する** OpenClaw をインストールし、数分で Gateway を起動します。 ](</ja-JP/start/getting-started>) [**オンボーディングを実行** `openclaw onboard` とペアリングフローによるガイド付きセットアップ。 ](</ja-JP/start/wizard>) [**コントロールUIを開く** チャット、設定、セッション用のブラウザダッシュボードを起動します。 ](</ja-JP/web/control-ui>)

## OpenClaw とは？

OpenClaw は、好みのチャットアプリやチャネルサーフェス（組み込みチャネルに加え、Discord、Google Chat、iMessage、Matrix、Microsoft Teams、Signal、Slack、Telegram、WhatsApp、Zalo などの同梱または外部チャネル Plugin）を、Pi のようなAIコーディングエージェントにつなぐ **セルフホスト型 Gateway** です。自分のマシン（またはサーバー）で単一の Gateway プロセスを実行すると、それがメッセージングアプリと常時利用可能なAIアシスタントの橋渡しになります。

**誰向けですか？** データの制御を手放したりホスト型サービスに依存したりせずに、どこからでもメッセージを送れる個人用AIアシスタントが欲しい開発者とパワーユーザー向けです。

**何が違いますか？**

  * **セルフホスト型** : 自分のハードウェア上で、自分のルールで動作
  * **マルチチャネル** : 1つの Gateway が組み込みチャネルに加え、同梱または外部チャネル Plugin を同時に提供
  * **エージェントネイティブ** : ツール利用、セッション、メモリ、マルチエージェントルーティングを備えたコーディングエージェント向けに構築
  * **オープンソース** : MITライセンス、コミュニティ主導


**何が必要ですか？** Node 24（推奨）、または互換性のための Node 22 LTS (`22.16+`)、選択したプロバイダーのAPIキー、そして5分です。品質とセキュリティを最良にするには、利用可能な最新世代の最も強力なモデルを使用してください。

## 仕組み
[code] 
    flowchart LR
      A["Chat apps + plugins"] --> B["Gateway"]
      B --> C["Pi agent"]
      B --> D["CLI"]
      B --> E["Web Control UI"]
      B --> F["macOS app"]
      B --> G["iOS and Android nodes"]
[/code]

Gateway は、セッション、ルーティング、チャネル接続における唯一の信頼できる情報源です。

## 主な機能

[**マルチチャネル Gateway** Discord、iMessage、Signal、Slack、Telegram、WhatsApp、WebChat などを単一の Gateway プロセスで利用できます。 ](</ja-JP/channels>) [**Plugin チャネル** 同梱 Plugin は、通常の現在リリースで Matrix、Nostr、Twitch、Zalo などを追加します。 ](</ja-JP/tools/plugin>) [**マルチエージェントルーティング** エージェント、ワークスペース、送信者ごとの分離されたセッション。 ](</ja-JP/concepts/multi-agent>) [**メディアサポート** 画像、音声、ドキュメントを送受信します。 ](</ja-JP/nodes/images>) [**Web コントロールUI** チャット、設定、セッション、ノード用のブラウザダッシュボード。 ](</ja-JP/web/control-ui>) [**モバイルノード** Canvas、カメラ、音声対応ワークフロー向けに iOS と Android のノードをペアリングします。 ](</ja-JP/nodes>)

## クイックスタート

* ### OpenClaw をインストール

bashCopy code
[code]
    npm install -g openclaw@latest
[/code]

* ### オンボーディングしてサービスをインストール

bashCopy code
[code]
    openclaw onboard --install-daemon
[/code]

* ### チャット

ブラウザでコントロールUIを開き、メッセージを送信します。

bashCopy code
[code]
    openclaw dashboard
[/code]

またはチャネル（[Telegram](</ja-JP/channels/telegram>) が最速）を接続して、スマートフォンからチャットします。

完全なインストール手順と開発セットアップが必要ですか？[はじめに](</ja-JP/start/getting-started>) を参照してください。

## ダッシュボード

Gateway の起動後にブラウザのコントロールUIを開きます。

  * ローカルのデフォルト: <http://127.0.0.1:18789/>
  * リモートアクセス: [Webサーフェス](</ja-JP/web>) と [Tailscale](</ja-JP/gateway/tailscale>)


![OpenClaw](/whatsapp-openclaw.jpg)

## 設定（任意）

設定は `~/.openclaw/openclaw.json` にあります。

  * **何もしない** 場合、OpenClaw は同梱の Pi バイナリをRPCモードで使用し、送信者ごとのセッションを使います。
  * 制限を強めたい場合は、`channels.whatsapp.allowFrom` と（グループの場合は）メンションルールから始めます。


例:

json5Copy code
[code]
    {  channels: {    whatsapp: {      allowFrom: ["+15555550123"],      groups: { "*": { requireMention: true } },    },  },  messages: { groupChat: { mentionPatterns: ["@openclaw"] } },}
[/code]

## ここから始める

[**ドキュメントハブ** すべてのドキュメントとガイドを、ユースケース別に整理しています。 ](</ja-JP/start/hubs>) [**設定** コア Gateway 設定、トークン、プロバイダー設定。 ](</ja-JP/gateway/configuration>) [**リモートアクセス** SSH と tailnet のアクセスパターン。 ](</ja-JP/gateway/remote>) [**チャネル** Feishu、Microsoft Teams、WhatsApp、Telegram、Discord などのチャネル固有セットアップ。 ](</ja-JP/channels/telegram>) [**ノード** ペアリング、Canvas、カメラ、デバイスアクションに対応した iOS と Android のノード。 ](</ja-JP/nodes>) [**ヘルプ** よくある修正とトラブルシューティングの入口。 ](</ja-JP/help>)

## さらに学ぶ

[**完全な機能一覧** チャネル、ルーティング、メディア機能の完全な一覧。 ](</ja-JP/concepts/features>) [**マルチエージェントルーティング** ワークスペース分離とエージェントごとのセッション。 ](</ja-JP/concepts/multi-agent>) [**セキュリティ** トークン、許可リスト、安全制御。 ](</ja-JP/gateway/security>) [**トラブルシューティング** Gateway の診断と一般的なエラー。 ](</ja-JP/gateway/troubleshooting>) [**概要とクレジット** プロジェクトの起源、コントリビューター、ライセンス。 ](</ja-JP/reference/credits>)

Was this useful?YesNo