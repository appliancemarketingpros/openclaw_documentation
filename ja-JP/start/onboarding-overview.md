---
title: オンボーディングの概要
source_url: https://docs.openclaw.ai/ja-JP/start/onboarding-overview
scraped_at: 2026-05-25
---

OpenClaw には 2 つのオンボーディング経路があります。どちらも認証、Gateway、 任意のチャットチャンネルを設定します。違いはセットアップとのやり取りの方法だけです。

## どちらの経路を使うべきですか？

| CLI オンボーディング | macOS アプリのオンボーディング  
---|---|---  
**プラットフォーム** | macOS、Linux、Windows (ネイティブまたは WSL2) | macOS のみ  
**インターフェイス** | ターミナルウィザード | アプリ内のガイド付き UI  
**最適な用途** | サーバー、ヘッドレス、完全な制御 | デスクトップ Mac、視覚的なセットアップ  
**自動化** | スクリプト向けの `--non-interactive` | 手動のみ  
**コマンド** | `openclaw onboard` | アプリを起動  
  
ほとんどのユーザーは **CLI オンボーディング** から始めるべきです。どこでも動作し、 最も細かく制御できます。

## オンボーディングで設定されるもの

選択した経路にかかわらず、オンボーディングでは次をセットアップします。

  1. **モデルプロバイダーと認証** — 選択したプロバイダーの API キー、OAuth、またはセットアップトークン
  2. **ワークスペース** — エージェントファイル、ブートストラップテンプレート、メモリ用のディレクトリ
  3. **Gateway** — ポート、バインドアドレス、認証モード
  4. **チャンネル** (任意) — iMessage、Discord、Feishu、Google Chat、Mattermost、Microsoft Teams、 Telegram、WhatsApp などの組み込みおよびバンドルされたチャットチャンネル
  5. **デーモン** (任意) — Gateway が自動的に起動するようにするバックグラウンドサービス


## CLI オンボーディング

任意のターミナルで実行します。

bashCopy code
[code]
    openclaw onboard
[/code]

バックグラウンドサービスも 1 ステップでインストールするには、`--install-daemon` を追加します。

完全なリファレンス: [オンボーディング (CLI)](</ja-JP/start/wizard>) CLI コマンドドキュメント: [`openclaw onboard`](</ja-JP/cli/onboard>)

## macOS アプリのオンボーディング

OpenClaw アプリを開きます。初回起動時のウィザードが、同じ手順を 視覚的なインターフェイスで案内します。

完全なリファレンス: [オンボーディング (macOS アプリ)](</ja-JP/start/onboarding>)

## カスタムまたは未掲載のプロバイダー

プロバイダーがオンボーディングに表示されていない場合は、**カスタムプロバイダー** を選択して 次を入力します。

  * API 互換モード (OpenAI 互換、Anthropic 互換、または自動検出)
  * ベース URL と API キー
  * モデル ID と任意のエイリアス


複数のカスタムエンドポイントは共存できます。それぞれに独自のエンドポイント ID が割り当てられます。

## 関連

  * [はじめに](</ja-JP/start/getting-started>)
  * [CLI セットアップリファレンス](</ja-JP/start/wizard-cli-reference>)


Was this useful?YesNo