---
title: 機能
source_url: https://docs.openclaw.ai/ja-JP/concepts/features
scraped_at: 2026-05-25
---

## ハイライト

[**チャンネル** 単一の Gateway で Discord、iMessage、Signal、Slack、Telegram、WhatsApp、WebChat などを利用できます。 ](</ja-JP/channels>) [**Plugins** バンドル済み plugins により、通常の現行リリースでは個別インストールなしで Matrix、Nextcloud Talk、Nostr、Twitch、Zalo などを追加できます。 ](</ja-JP/tools/plugin>) [**ルーティング** 分離されたセッションによるマルチエージェントルーティング。 ](</ja-JP/concepts/multi-agent>) [**メディア** 画像、音声、動画、ドキュメント、および画像/動画生成。 ](</ja-JP/nodes/images>) [**アプリと UI** Web Control UI と macOS コンパニオンアプリ。 ](</ja-JP/web/control-ui>) [**モバイルノード** ペアリング、音声/チャット、豊富なデバイスコマンドを備えた iOS と Android ノード。 ](</ja-JP/nodes>)

## 完全な一覧

**チャンネル:**

  * 組み込みチャンネルには Discord、Google Chat、iMessage、IRC、Signal、Slack、Telegram、WebChat、WhatsApp が含まれます
  * バンドル済み plugin チャンネルには Feishu、LINE、Matrix、Mattermost、Microsoft Teams、Nextcloud Talk、Nostr、QQ Bot、Synology Chat、Tlon、Twitch、Zalo、Zalo Personal が含まれます
  * 任意で個別にインストールするチャンネル plugins には Voice Call や WeChat などのサードパーティパッケージが含まれます
  * サードパーティのチャンネル plugins は、WeChat などにより Gateway をさらに拡張できます
  * メンションベースの有効化によるグループチャット対応
  * 許可リストとペアリングによる DM の安全性


**エージェント:**

  * ツールストリーミングを備えた組み込みエージェントランタイム
  * ワークスペースまたは送信者ごとに分離されたセッションによるマルチエージェントルーティング
  * セッション: ダイレクトチャットは共有 `main` に集約され、グループは分離されます
  * 長い応答向けのストリーミングとチャンク分割


**認証とプロバイダー:**

  * 35 以上のモデルプロバイダー (Anthropic、OpenAI、Google など)
  * OAuth 経由のサブスクリプション認証 (例: OpenAI Codex)
  * カスタムおよびセルフホストのプロバイダー対応 (vLLM、SGLang、Ollama、および任意の OpenAI 互換または Anthropic 互換エンドポイント)


**メディア:**

  * 画像、音声、動画、ドキュメントの入出力
  * 共有の画像生成および動画生成機能サーフェス
  * ボイスメモの文字起こし
  * 複数プロバイダーによるテキスト読み上げ


**アプリとインターフェイス:**

  * WebChat とブラウザー Control UI
  * macOS メニューバーコンパニオンアプリ
  * ペアリング、Canvas、カメラ、画面録画、位置情報、音声を備えた iOS ノード
  * ペアリング、チャット、音声、Canvas、カメラ、デバイスコマンドを備えた Android ノード


**ツールと自動化:**

  * ブラウザー自動化、exec、サンドボックス化
  * Web 検索 (Brave、DuckDuckGo、Exa、Firecrawl、Gemini、Grok、Kimi、MiniMax Search、Ollama Web Search、Perplexity、SearXNG、Tavily)
  * Cron ジョブと Heartbeat スケジューリング
  * Skills、plugins、ワークフローパイプライン (Lobster)


## 関連

[**実験的機能** まだデフォルトのサーフェスには出荷されていないオプトイン機能。 ](</ja-JP/concepts/experimental-features>) [**エージェントランタイム** エージェントランタイムモデルと実行のディスパッチ方法。 ](</ja-JP/concepts/agent>) [**チャンネル** 1 つの Gateway から Telegram、WhatsApp、Discord、Slack などに接続します。 ](</ja-JP/channels>) [**Plugins** OpenClaw を拡張するバンドル済みおよびサードパーティの plugins。 ](</ja-JP/tools/plugin>)

Was this useful?YesNo