---
title: 成熟度分類
source_url: https://docs.openclaw.ai/ja-JP/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# 成熟度タクソノミー

スコアカードの背後にあるモデル

サーフェス > カテゴリ > ケイパビリティ > エビデンス。

50 個のサーフェスを 4 つのファミリーに分類し、すべてのカテゴリを正規ドキュメントと QA カバレッジ ID に結び付けています。

プロダクト領域を見る / 詳細なタクソノミーを開く / [スコアを見る](</ja-JP/maturity/scorecard>)

## このページの読み方

サーフェスとは、Gateway ランタイム、Discord、macOS アプリなどのプロダクト領域です。各サーフェスにはカテゴリが含まれ、各カテゴリには QA シナリオがカバーするケイパビリティレベルのチェックが含まれます。リリースレベルの判断にはスコアカードを使い、このページではその下にあるモデルを確認します。

## 成熟度レベル

M0計画中方向性は分かっているものの、サポートされるユーザーパスはまだありません。昇格: 設計 Issue、オーナー、対象サーフェスが存在する。

M1実験的注意事項、フラグ、ソースビルド、またはメンテナー専用フローの背後で実装されています。昇格: メンテナーが現在の main からシナリオを実行できる。

M2アルファ実ユーザーが試せますが、破壊的変更や未完成の UX が想定されます。昇格: 文書化されたセットアップ、基本テスト、既知の注意事項、少なくとも 1 つの実環境での証明。

M3ベータ公開パスがあり、主要ワークフローは限定的な注意事項の範囲で利用できます。昇格: インストール/更新ドキュメント、回帰テスト、サポート Runbook、想定環境全体で成功したシナリオ証明。

M4安定通常ユーザー向けの推奨パスです。失敗は回帰として扱われます。昇格: リリースゲート、doctor/トラブルシューティングパス、幅広いドキュメント、反復された実環境での証明。

M5Clawesome洗練され、快適で、十分に計測され、最良の同等ワークフローと競争できます。昇格: 安定に加え、代表的なユーザー全体でユーザースコアカードに合格。

## プロダクト領域

### Core

CLI M4安定7 領域 - 90% 完了 Gateway ランタイム M4安定13 領域 - 89% 完了 エージェントランタイム M3ベータ9 領域 - 79% 完了 セッション、メモリ、コンテキストエンジン M3ベータ9 領域 - 79% 完了 チャネルフレームワーク M3ベータ8 領域 - 79% 完了 オブザーバビリティ M3ベータ5 領域 - 79% 完了 Gateway ウェブアプリ M3ベータ6 領域 - 79% 完了 Plugin M3ベータ9 領域 - 79% 完了 セキュリティ、認証、ペアリング、シークレット M3ベータ6 領域 - 79% 完了 自動化: Cron、フック、タスク、ポーリング M3ベータ6 領域 - 79% 完了 メディア理解とメディア生成 M2アルファ6 領域 - 68% 完了 音声とリアルタイム会話 M2アルファ6 領域 - 68% 完了 TUI M2アルファ5 領域 - 66% 完了 ClawHub M2アルファ4 領域 - 62% 完了 OpenClaw App SDK M2アルファ6 領域 - 53% 完了

### プラットフォーム

Linux Gateway ホスト M4安定5 領域 - 89% 完了 macOS Gateway ホスト M4安定7 領域 - 88% 完了 Docker と Podman のホスティング M3ベータ4 領域 - 79% 完了 WSL2 経由の Windows M3ベータ6 領域 - 79% 完了 Raspberry Pi と小型 Linux デバイス M3ベータ4 領域 - 79% 完了 macOS コンパニオンアプリ M3ベータ8 領域 - 78% 完了 Android アプリ M2アルファ7 領域 - 66% 完了 ネイティブ Windows M2アルファ4 領域 - 66% 完了 Kubernetes ホスティング M2アルファ4 領域 - 61% 完了 iOS アプリ M1実験的8 領域 - 44% 完了 Nix インストールパス M1実験的5 領域 - 44% 完了 watchOS コンパニオンサーフェス M1実験的5 領域 - 44% 完了 Linux コンパニオンアプリ M0計画済み5 領域 - 21% 完了 ネイティブ Windows コンパニオンアプリ M0計画済み5 領域 - 21% 完了

### チャネル

Discord M4安定版6 領域 - 87% 完了 Telegram M3ベータ5 領域 - 78% 完了 Slack M3ベータ5 領域 - 78% 完了 iMessage と BlueBubbles M3ベータ5 領域 - 78% 完了 WhatsApp M3ベータ5 領域 - 78% 完了 Matrix M2アルファ6 領域 - 67% 完了 Google Chat M2アルファ5 領域 - 66% 完了 Microsoft Teams M2アルファ5 領域 - 66% 完了 Signal M2アルファ5 領域 - 66% 完了 Feishu、QQ Bot、WeChat、Yuanbao、Zalo、Zalo Personal、地域チャネル M2アルファ4 領域 - 58% 完了 Mattermost、LINE、IRC、Nextcloud Talk、Nostr、Twitch、Tlon、Synology Chat M2アルファ4 領域 - 54% 完了 音声通話チャネル M1実験的5 領域 - 44% 完了

### プロバイダーとツール

ブラウザー自動化、exec、サンドボックスツール M3ベータ3 領域 - 79% 完了 OpenAI と Codex のプロバイダーパス M3ベータ5 領域 - 79% 完了 Web 検索ツール M3ベータ4 領域 - 79% 完了 Anthropic プロバイダーパス M3ベータ5 領域 - 78% 完了 Google プロバイダーパス M3ベータ5 領域 - 78% 完了 OpenRouter プロバイダーパス M3ベータ4 領域 - 78% 完了 画像、動画、音楽生成ツール M2アルファ5 領域 - 68% 完了 ローカルモデルプロバイダー: Ollama、vLLM、SGLang、LM Studio M2アルファ5 領域 - 68% 完了 ロングテールのホスト型プロバイダー M2アルファ3 領域 - 68% 完了

## 詳細

### コア

CLI - M4 安定版 - 7 領域

通常のセットアップと修復のパスは、インストール、CLI、Gateway ドキュメント全体で文書化されています。プラットフォーム固有の Windows パスは、WSL2 経由の Windows とネイティブ Windows の行で追跡されています。

カバレッジ 実験的 - 4%品質 安定版 - 83%完全性 安定版 - 90%部分的 - 6

CLIセットアップ 6個の機能 / LTSサポート対象

実験的17%

安定89%

安定90%

[索引](</ja-JP/install>), [インストーラー](</ja-JP/install/installer>), [Node](</ja-JP/install/node>), [更新](</ja-JP/install/updating>)

オンボーディングと認証セットアップ 5個の機能 / LTSサポート対象

実験的0%

ベータ75%

安定89%

[オンボード](</ja-JP/cli/onboard>), [設定](</ja-JP/cli/configure>), [オンボーディング概要](</ja-JP/start/onboarding-overview>)

Pluginとチャンネルのセットアップ 5個の機能

実験的0%

ベータ75%

安定89%

[オンボード](</ja-JP/cli/onboard>), [Plugin](</ja-JP/cli/plugins>), [チャンネル](</ja-JP/cli/channels>)

Gatewayサービス管理 5個の機能 / LTSサポート対象

実験的14%

安定87%

安定90%

[Gateway](</ja-JP/cli/gateway>), [更新](</ja-JP/install/updating>), [トラブルシューティング](</ja-JP/gateway/troubleshooting>)

CLIオブザーバビリティ 5個の機能 / LTSサポート対象

実験的0%

安定89%

安定90%

[ステータス](</ja-JP/cli/status>), [ヘルス](</ja-JP/cli/health>), [ログ](</ja-JP/cli/logs>), [診断](</ja-JP/gateway/diagnostics>)

診断 10個の機能 / LTSサポート対象

実験的0%

安定89%

安定90%

[診断](</ja-JP/cli/doctor>), [診断](</ja-JP/gateway/doctor>), [シークレット](</ja-JP/gateway/secrets>), [トラブルシューティング](</ja-JP/gateway/troubleshooting>)

更新とアップグレード 5個の機能 / LTSサポート対象

実験的0%

ベータ75%

安定89%

[更新](</ja-JP/install/updating>), [更新](</ja-JP/cli/update>), [トラブルシューティング](</ja-JP/gateway/troubleshooting>)

Gatewayランタイム - M4 安定 - 13領域

コアアーキテクチャ、認証、ペアリング、プロトコルドキュメント、デーモンドキュメント、CLIランブックは幅広く最新です。

カバレッジ 実験的 - 6%品質 安定 - 81%完全性 安定 - 89%部分的 - 12

承認とリモート実行 6 機能 / LTS 対応

実験的0%

ベータ75%

安定版89%

[プロトコル](</ja-JP/gateway/protocol>), [インデックス](</ja-JP/gateway/security>)

HTTP API 4 機能 / LTS 対応

実験的25%

安定版90%

安定版90%

[インデックス](</ja-JP/gateway>), [Openai HTTP API](</ja-JP/gateway/openai-http-api>), [OpenResponses HTTP API](</ja-JP/gateway/openresponses-http-api>), [ツール呼び出し HTTP API](</ja-JP/gateway/tools-invoke-http-api>), [フック](</ja-JP/automation/hooks>), [インデックス](</ja-JP/web>)

ホスト型 Web サーフェス 4 機能 / LTS 対応

実験的0%

安定版89%

安定版90%

[インデックス](</ja-JP/gateway>), [アーキテクチャ](</ja-JP/concepts/architecture>), [コントロール UI](</ja-JP/web/control-ui>), [Webchat](</ja-JP/web/webchat>), [Canvas](</ja-JP/refactor/canvas>)

Gateway RPC API とイベント 20 機能 / LTS 対応

実験的9%

安定版90%

安定版90%

[プロトコル](</ja-JP/gateway/protocol>), [インデックス](</ja-JP/gateway>), [アーキテクチャ](</ja-JP/concepts/architecture>)

デバイス認証とペアリング 10 機能 / LTS 対応

実験的0%

ベータ75%

安定版89%

[プロトコル](</ja-JP/gateway/protocol>), [ペアリング](</ja-JP/gateway/pairing>), [インデックス](</ja-JP/gateway/security>)

ネットワークアクセスと検出 6 機能 / LTS 対応

実験的0%

ベータ75%

安定版89%

[インデックス](</ja-JP/gateway>), [検出](</ja-JP/gateway/discovery>), [プロトコル](</ja-JP/gateway/protocol>)

Node とリモート機能 8 機能

実験的0%

ベータ75%

安定版89%

[プロトコル](</ja-JP/gateway/protocol>), [アーキテクチャ](</ja-JP/concepts/architecture>), [インデックス](</ja-JP/nodes>)

ヘルス、診断、修復 7 機能 / LTS 対応

実験的0%

ベータ75%

安定版89%

[インデックス](</ja-JP/gateway>), [診断](</ja-JP/gateway/diagnostics>), [Doctor](</ja-JP/gateway/doctor>)

プロトコル互換性 7 個の機能 / LTS サポート対象

実験的0%

ベータ75%

安定版89%

[プロトコル](</ja-JP/gateway/protocol>), [アーキテクチャ](</ja-JP/concepts/architecture>), [Typebox](</ja-JP/concepts/typebox>), [ブリッジプロトコル](</ja-JP/gateway/bridge-protocol>)

ロールと権限 5 個の機能 / LTS サポート対象

実験的0%

ベータ75%

安定版89%

[プロトコル](</ja-JP/gateway/protocol>), [インデックス](</ja-JP/gateway/security>)

Gateway ライフサイクル 7 個の機能 / LTS サポート対象

実験的33%

安定版90%

安定版90%

[インデックス](</ja-JP/gateway>), [アーキテクチャ](</ja-JP/concepts/architecture>)

セキュリティ制御 6 個の機能 / LTS サポート対象

実験的0%

ベータ75%

安定版89%

[インデックス](</ja-JP/gateway/security>), [プロトコル](</ja-JP/gateway/protocol>), [検出](</ja-JP/gateway/discovery>)

WebSocket 接続 8 個の機能 / LTS サポート対象

実験的13%

安定版90%

安定版90%

[プロトコル](</ja-JP/gateway/protocol>), [アーキテクチャ](</ja-JP/concepts/architecture>)

Agent Runtime - M3 ベータ - 9領域

メインループ、モデル、プロバイダールーティング、ツールストリーミングは第一級の機能ですが、プロバイダーの動作は週ごとに変化するため、リリースごとにシナリオ証明が必要です。

カバレッジ 実験的 - 33%品質 ベータ - 78%完成度 ベータ - 79%部分的 - 6

エージェントターン実行 3 機能 / LTS 対応

実験的29%

ベータ79%

ベータ79%

[エージェントループ](</ja-JP/concepts/agent-loop>), [エージェント](</ja-JP/cli/agent>), [エージェントランタイム](</ja-JP/concepts/agent-runtimes>)

外部ランタイムとサブエージェント 4 機能

実験的30%

ベータ79%

ベータ79%

[エージェントランタイム](</ja-JP/concepts/agent-runtimes>), [Anthropic](</ja-JP/providers/anthropic>), [Google](</ja-JP/providers/google>), [サブエージェント](</ja-JP/tools/subagents>)

ホスト型プロバイダー実行 5 機能 / LTS 対応

実験的20%

ベータ79%

ベータ79%

[Openai](</ja-JP/providers/openai>), [Anthropic](</ja-JP/providers/anthropic>), [Google](</ja-JP/providers/google>), [モデル](</ja-JP/concepts/models>)

ローカルおよびセルフホスト型プロバイダー 5 機能

実験的0%

アルファ68%

ベータ79%

[Ollama](</ja-JP/providers/ollama>), [モデル](</ja-JP/concepts/models>), [エージェント](</ja-JP/cli/agent>)

モデルとランタイムの選択 4 機能 / LTS 対応

実験的25%

ベータ79%

ベータ79%

[モデル](</ja-JP/concepts/models>), [モデル](</ja-JP/cli/models>), [Openai](</ja-JP/providers/openai>), [エージェントランタイム](</ja-JP/concepts/agent-runtimes>)

プロバイダー認証 10 機能 / LTS 対応

実験的24%

ベータ79%

ベータ79%

[モデル](</ja-JP/concepts/models>), [エージェント](</ja-JP/cli/agent>), [モデル](</ja-JP/cli/models>), [Openai](</ja-JP/providers/openai>), [Anthropic](</ja-JP/providers/anthropic>), [Google](</ja-JP/providers/google>), [サブエージェント](</ja-JP/tools/subagents>)

ストリーミングと進行状況 2 機能

アルファ56%

ベータ79%

ベータ79%

[ストリーミング](</ja-JP/concepts/streaming>), [エージェントループ](</ja-JP/concepts/agent-loop>)

ツール呼び出しとレスポンス処理 3 機能 / LTS 対応

アルファ65%

ベータ79%

ベータ79%

[エージェントループ](</ja-JP/concepts/agent-loop>), [Ollama](</ja-JP/providers/ollama>)

ツール実行制御 6個の機能 / LTSサポート対象

Alpha50%

Beta79%

Beta79%

[サンドボックス Vs ツールポリシー Vs 昇格](</ja-JP/gateway/sandbox-vs-tool-policy-vs-elevated>), [エージェントループ](</ja-JP/concepts/agent-loop>), [サブエージェント](</ja-JP/tools/subagents>)

セッション、メモリ、コンテキストエンジン - M3 ベータ - 9 領域

ドキュメントは充実しており、実装も活発です。成熟度は、トランスクリプトの耐久性、Compaction の品質、クロスクライアントの同等性に依存します。

カバレッジ 実験的 - 30%品質 ベータ - 77%完全性 ベータ - 79%部分的 - 6

CLI セッションとトランスクリプト管理 2 機能 / LTSサポート対象

実験的0%

アルファ68%

ベータ79%

[セッション](</ja-JP/concepts/session>), [セッション管理 Compaction](</ja-JP/reference/session-management-compaction>), [セッション](</ja-JP/cli/sessions>)

トークン管理 3 機能 / LTSサポート対象

実験的20%

ベータ79%

ベータ79%

[Compaction](</ja-JP/concepts/compaction>), [コンテキスト](</ja-JP/concepts/context>), [セッション管理 Compaction](</ja-JP/reference/session-management-compaction>)

コンテキストエンジン 2 機能 / LTSサポート対象

アルファ57%

ベータ79%

ベータ79%

[コンテキスト](</ja-JP/concepts/context>), [コンテキストエンジン](</ja-JP/concepts/context-engine>), [Codex コンテキストエンジンハーネス](</ja-JP/plan/codex-context-engine-harness>)

クライアント横断の履歴とセッション同等性 2 機能

実験的40%

ベータ79%

ベータ79%

[ウェブチャット](</ja-JP/web/webchat>), [Android](</ja-JP/platforms/android>), [チャネルルーティング](</ja-JP/channels/channel-routing>)

診断、保守、復旧 3 機能

実験的40%

ベータ79%

ベータ79%

[診断](</ja-JP/gateway/diagnostics>), [セッション管理 Compaction](</ja-JP/reference/session-management-compaction>), [フラグ](</ja-JP/diagnostics/flags>)

コアプロンプトとコンテキスト 2 機能 / LTSサポート対象

実験的38%

ベータ79%

ベータ79%

[コンテキスト](</ja-JP/concepts/context>), [トランスクリプト衛生管理](</ja-JP/reference/transcript-hygiene>), [Discord](</ja-JP/channels/discord>)

メモリ 5 機能

実験的46%

ベータ79%

ベータ79%

[メモリ設定](</ja-JP/reference/memory-config>), [Memory Qmd](</ja-JP/concepts/memory-qmd>), [メモリ](</ja-JP/concepts/memory>), [Discord](</ja-JP/channels/discord>)

セッションルーティング 2 機能 / LTSサポート対象

実験的25%

ベータ79%

ベータ79%

[セッション](</ja-JP/concepts/session>), [チャネルルーティング](</ja-JP/channels/channel-routing>), [Discord](</ja-JP/channels/discord>)

トランスクリプトの永続化 2 機能 / LTS 対応

実験的0%

アルファ68%

ベータ79%

[セッション管理 Compaction](</ja-JP/reference/session-management-compaction>), [トランスクリプト衛生管理](</ja-JP/reference/transcript-hygiene>)

チャネルフレームワーク - M3 ベータ - 8 領域

多くのチャネルは Gateway の配信およびルーティング契約を共有しますが、チャネルの動作は上流 API とアカウントポリシーの制約によって異なります。

カバレッジ 実験的 - 13%品質 ベータ - 76%完全性 ベータ - 79%部分的 - 5

チャンネルアクション、コマンド、承認 5 機能

実験的0%

ベータ79%

ベータ79%

[グループ](</ja-JP/channels/groups>), [Discord](</ja-JP/channels/discord>), [Google Chat](</ja-JP/channels/googlechat>), [Signal](</ja-JP/channels/signal>), [Matrix](</ja-JP/channels/matrix>)

チャンネル設定 5 機能 / LTS サポート対象

実験的14%

ベータ79%

ベータ79%

[索引](</ja-JP/channels>), [ペアリング](</ja-JP/channels/pairing>), [トラブルシューティング](</ja-JP/channels/troubleshooting>), [SDK チャンネル Plugin](</ja-JP/plugins/sdk-channel-plugins>)

グループスレッドとアンビエントルームの動作 5 機能

実験的36%

ベータ79%

ベータ79%

[グループ](</ja-JP/channels/groups>), [グループメッセージ](</ja-JP/channels/group-messages>), [アンビエントルームイベント](</ja-JP/channels/ambient-room-events>), [ブロードキャストグループ](</ja-JP/channels/broadcast-groups>), [Discord](</ja-JP/channels/discord>)

受信アクセスとアイデンティティゲート 5 機能 / LTS サポート対象

実験的0%

アルファ68%

ベータ79%

[アクセスグループ](</ja-JP/channels/access-groups>), [グループ](</ja-JP/channels/groups>), [Discord](</ja-JP/channels/discord>), [LINE](</ja-JP/channels/line>)

メディア添付とリッチチャンネルデータ 4 機能

実験的0%

アルファ68%

ベータ79%

[LINE](</ja-JP/channels/line>), [Signal](</ja-JP/channels/signal>), [Google Chat](</ja-JP/channels/googlechat>), [Matrix](</ja-JP/channels/matrix>), [Discord](</ja-JP/channels/discord>)

送信配信と返信パイプライン 4 機能 / LTS サポート対象

実験的38%

ベータ79%

ベータ79%

[グループ](</ja-JP/channels/groups>), [アンビエントルームイベント](</ja-JP/channels/ambient-room-events>), [Discord](</ja-JP/channels/discord>), [Matrix](</ja-JP/channels/matrix>), [設定チャンネル](</ja-JP/gateway/config-channels>)

会話ルーティングと配信 10 機能 / LTS サポート対象

実験的19%

ベータ79%

ベータ79%

[チャンネルルーティング](</ja-JP/channels/channel-routing>), [グループ](</ja-JP/channels/groups>), [Discord](</ja-JP/channels/discord>), [Matrix](</ja-JP/channels/matrix>), [トラブルシューティング](</ja-JP/channels/troubleshooting>), [設定リファレンス](</ja-JP/gateway/configuration-reference>)

ステータス健全性とオペレーター制御 4 機能 / LTS サポート対象

実験的0%

ベータ79%

ベータ79%

[ヘルス](</ja-JP/gateway/health>), [設定リファレンス](</ja-JP/gateway/configuration-reference>), [トラブルシューティング](</ja-JP/channels/troubleshooting>), [Discord](</ja-JP/channels/discord>)

オブザーバビリティ - M3 ベータ - 5 領域

OTel、Prometheus、ロギング、診断のドキュメントがあります。公開向けの「オペレーターが最初に見るべきもの」の成熟度見直しが必要です。

カバレッジ Experimental - 18%品質 Beta - 75%完全性 Beta - 79%一部 - 3

健全性と修復 12 件の機能 / LTS 対応

Experimental28%

Beta79%

Beta79%

[健全性](</ja-JP/gateway/health>), [Telegram](</ja-JP/channels/telegram>), [Doctor](</ja-JP/cli/doctor>), [Doctor](</ja-JP/gateway/doctor>), [SDK サブパス](</ja-JP/plugins/sdk-subpaths>), [健全性](</ja-JP/cli/health>), [プロトコル](</ja-JP/gateway/protocol>)

ログ記録 5 件の機能 / LTS 対応

Experimental0%

Alpha68%

Beta79%

[ログ記録](</ja-JP/logging>), [ログ記録](</ja-JP/gateway/logging>), [ログ](</ja-JP/cli/logs>)

診断収集 8 件の機能

Experimental30%

Beta79%

Beta79%

[診断](</ja-JP/gateway/diagnostics>), [健全性](</ja-JP/gateway/health>), [Codex ハーネス](</ja-JP/plugins/codex-harness>), [プロトコル](</ja-JP/gateway/protocol>)

テレメトリのエクスポート 13 件の機能

Experimental33%

Beta79%

Beta79%

[フック](</ja-JP/plugins/hooks>), [OpenTelemetry](</ja-JP/gateway/opentelemetry>), [ログ記録](</ja-JP/logging>), [SDK サブパス](</ja-JP/plugins/sdk-subpaths>), [診断 OTEL](</ja-JP/plugins/reference/diagnostics-otel>), [Prometheus](</ja-JP/gateway/prometheus>), [診断 Prometheus](</ja-JP/plugins/reference/diagnostics-prometheus>)

セッション診断 4 件の機能 / LTS 対応

Experimental0%

Alpha68%

Beta79%

[OpenTelemetry](</ja-JP/gateway/opentelemetry>), [Prometheus](</ja-JP/gateway/prometheus>), [診断](</ja-JP/gateway/diagnostics>), [プロトコル](</ja-JP/gateway/protocol>)

Gateway Web アプリ - M3 Beta - 6 領域

Web UI は、ペアリング、チャット、PWA、Talk、プッシュ、リモート Gateway フローとともに文書化されています。クロスブラウザーおよびモバイル PWA のスコアカード後に昇格します。

カバレッジ Experimental - 4%品質 Beta - 74%完全性 Beta - 79%なし

ブラウザーリアルタイムトーク 5 件のケイパビリティ

実験的0%

アルファ68%

ベータ79%

[コントロール UI](</ja-JP/web/control-ui>), [プロトコル](</ja-JP/gateway/protocol>), [トーク](</ja-JP/nodes/talk>)

ブラウザーアクセスと信頼 5 件のケイパビリティ

実験的0%

アルファ68%

ベータ79%

[コントロール UI](</ja-JP/web/control-ui>), [ダッシュボード](</ja-JP/web/dashboard>), [Tailscale](</ja-JP/gateway/tailscale>), [リモート](</ja-JP/gateway/remote>)

設定 5 件のケイパビリティ

実験的0%

アルファ68%

ベータ79%

[コントロール UI](</ja-JP/web/control-ui>), [設定](</ja-JP/gateway/configuration>)

ブラウザー UI 10 件のケイパビリティ

実験的8%

ベータ79%

ベータ79%

[コントロール UI](</ja-JP/web/control-ui>), [インデックス](</ja-JP/web>), [ダッシュボード](</ja-JP/web/dashboard>), [プロトコル](</ja-JP/gateway/protocol>)

WebChat 会話 15 件のケイパビリティ

実験的10%

ベータ79%

ベータ79%

[コントロール UI](</ja-JP/web/control-ui>), [Webchat](</ja-JP/web/webchat>), [はじめに](</ja-JP/start/getting-started>), [チャネルルーティング](</ja-JP/channels/channel-routing>), [セキュアファイル操作](</ja-JP/gateway/security/secure-file-operations>)

オペレーターコンソール 10 件のケイパビリティ

実験的8%

ベータ79%

ベータ79%

[コントロール UI](</ja-JP/web/control-ui>), [ヘルス](</ja-JP/gateway/health>), [プロトコル](</ja-JP/gateway/protocol>), [ダッシュボード](</ja-JP/web/dashboard>)

Plugins - M3 ベータ - 9 領域

マニフェスト、検出、読み込み、プロバイダー/ツールアーキテクチャ、承認境界にわたって、広範なドキュメントと強力な内部ランタイム証拠があります。公開 SDK API/サブパスと外部配布の証拠がさらに強くなるまで、この行はベータのままにしてください。

カバレッジ 実験的 - 12%品質 ベータ - 72%完成度 ベータ - 79%部分的 - 7

Plugin の作成とパッケージ化 8 機能 / LTS サポート対象

実験的0%

アルファ68%

ベータ79%

[Plugin の構築](</ja-JP/plugins/building-plugins>), [SDK 概要](</ja-JP/plugins/sdk-overview>), [SDK エントリポイント](</ja-JP/plugins/sdk-entrypoints>), [SDK サブパス](</ja-JP/plugins/sdk-subpaths>), [マニフェスト](</ja-JP/plugins/manifest>), [リファレンス](</ja-JP/plugins/reference>)

バンドル済み Plugin 5 機能 / LTS サポート対象

実験的0%

アルファ68%

ベータ79%

[Plugin インベントリ](</ja-JP/plugins/plugin-inventory>), [Plugin](</ja-JP/cli/plugins>), [アーキテクチャ内部](</ja-JP/plugins/architecture-internals>)

Canvas Plugin 6 機能

実験的0%

アルファ68%

ベータ79%

[Canvas](</ja-JP/plugins/reference/canvas>), [Canvas](</ja-JP/refactor/canvas>), [設定リファレンス](</ja-JP/gateway/configuration-reference>)

Plugin のインストールと実行 6 機能 / LTS サポート対象

実験的35%

ベータ79%

ベータ79%

[アーキテクチャ](</ja-JP/plugins/architecture>), [アーキテクチャ内部](</ja-JP/plugins/architecture-internals>), [Plugin](</ja-JP/cli/plugins>)

チャンネル Plugin 5 機能 / LTS サポート対象

実験的0%

アルファ68%

ベータ79%

[SDK チャンネル Plugin](</ja-JP/plugins/sdk-channel-plugins>), [SDK チャンネルインバウンド](</ja-JP/plugins/sdk-channel-inbound>), [SDK チャンネルアウトバウンド](</ja-JP/plugins/sdk-channel-outbound>)

プロバイダーとツールの Plugin 6 機能 / LTS サポート対象

実験的43%

ベータ79%

ベータ79%

[SDK プロバイダー Plugin](</ja-JP/plugins/sdk-provider-plugins>), [ツール Plugin](</ja-JP/plugins/tool-plugins>), [機能の追加](</ja-JP/plugins/adding-capabilities>)

Plugin の承認 6 機能 / LTS サポート対象

実験的0%

アルファ68%

ベータ79%

[Plugin 権限リクエスト](</ja-JP/plugins/plugin-permission-requests>), [実行承認](</ja-JP/tools/exec-approvals>), [SDK チャンネル Plugin](</ja-JP/plugins/sdk-channel-plugins>)

Plugin の公開 6 機能 / LTS サポート対象

実験的0%

アルファ68%

ベータ79%

[Plugin](</ja-JP/cli/plugins>), [互換性](</ja-JP/plugins/compatibility>), [公開](</ja-JP/clawhub/publishing>)

Pluginのテスト 6 個の機能

実験的27%

ベータ79%

ベータ79%

[SDKテスト](</ja-JP/plugins/sdk-testing>), [SDKセットアップ](</ja-JP/plugins/sdk-setup>), [Codex Harness](</ja-JP/plugins/codex-harness>)

セキュリティ、認証、ペアリング、シークレット - M3 ベータ - 6 領域

良好なドキュメントと強化対象のサーフェスは存在します。定期的なアップグレード/セキュリティシナリオの実行でセットアップの回帰がないことを証明した後に昇格してください。

カバレッジ 実験的 - 16%品質 ベータ - 72%完成度 ベータ - 79%一部 - 5

承認ポリシーとツール保護策 2 機能 / LTS 対応

アルファ50%

ベータ79%

ベータ79%

[実行承認](</ja-JP/tools/exec-approvals>), [承認](</ja-JP/cli/approvals>), [Plugin 権限リクエスト](</ja-JP/plugins/plugin-permission-requests>), [監査チェック](</ja-JP/gateway/security/audit-checks>)

Gateway 認証とリモートアクセス 9 機能 / LTS 対応

実験的0%

アルファ68%

ベータ79%

[インデックス](</ja-JP/gateway/security>), [公開ランブック](</ja-JP/gateway/security/exposure-runbook>), [信頼済みプロキシ認証](</ja-JP/gateway/trusted-proxy-auth>), [Tailscale](</ja-JP/gateway/tailscale>), [リモート](</ja-JP/gateway/remote>), [設定リファレンス](</ja-JP/gateway/configuration-reference>), [Gateway](</ja-JP/cli/gateway>), [Doctor](</ja-JP/cli/doctor>), [Control UI](</ja-JP/web/control-ui>), [ブラウザー制御](</ja-JP/tools/browser-control>), [監査チェック](</ja-JP/gateway/security/audit-checks>)

チャネルアクセス制御 3 機能 / LTS 対応

実験的0%

アルファ68%

ベータ79%

[ペアリング](</ja-JP/channels/pairing>), [Telegram](</ja-JP/channels/telegram>), [アクセスグループ](</ja-JP/channels/access-groups>), [監査チェック](</ja-JP/gateway/security/audit-checks>)

デバイスと Node のペアリング 11 機能 / LTS 対応

実験的0%

アルファ68%

ベータ79%

[プロトコル](</ja-JP/gateway/protocol>), [デバイス](</ja-JP/cli/devices>), [ペアリング](</ja-JP/channels/pairing>), [ペアリング](</ja-JP/gateway/pairing>), [オペレータースコープ](</ja-JP/gateway/operator-scopes>), [Control UI](</ja-JP/web/control-ui>), [Webchat](</ja-JP/web/webchat>), [承認](</ja-JP/cli/approvals>)

Plugin の信頼 2 機能

実験的0%

アルファ68%

ベータ79%

[マニフェスト](</ja-JP/plugins/manifest>), [Plugin 権限リクエスト](</ja-JP/plugins/plugin-permission-requests>), [Plugin の管理](</ja-JP/plugins/manage-plugins>), [監査チェック](</ja-JP/gateway/security/audit-checks>)

認証情報とシークレットの衛生管理 5 機能 / LTS 対応

実験的46%

ベータ79%

ベータ79%

[認証](</ja-JP/gateway/authentication>), [モデル](</ja-JP/cli/models>), [Openai](</ja-JP/providers/openai>), [Oauth](</ja-JP/concepts/oauth>), [シークレット](</ja-JP/gateway/secrets>), [シークレット](</ja-JP/cli/secrets>), [Secretref 認証情報サーフェス](</ja-JP/reference/secretref-credential-surface>), [監査チェック](</ja-JP/gateway/security/audit-checks>)

自動化: Cron、フック、タスク、ポーリング - M3 ベータ - 6 領域

ドキュメント化され利用可能ですが、シナリオ証明では無人配信、再試行、失敗の可視性をカバーする必要があります。

カバレッジ 実験的 - 2%品質 ベータ - 72%完成度 ベータ - 79%なし

Cronジョブ 15個の機能

実験的0%

ベータ79%

ベータ79%

[Cronジョブ](</ja-JP/automation/cron-jobs>), [Cron](</ja-JP/cli/cron>), [プロトコル](</ja-JP/gateway/protocol>), [タスク](</ja-JP/automation/tasks>), [Discord](</ja-JP/channels/discord>)

イベント取り込み 15個の機能

実験的0%

アルファ68%

ベータ79%

[Telegram](</ja-JP/channels/telegram>), [Zalo](</ja-JP/channels/zalo>), [トラブルシューティング](</ja-JP/channels/troubleshooting>), [BlueBubblesからのiMessage](</ja-JP/channels/imessage-from-bluebubbles>), [Gmail Pub/Sub連携](</ja-JP/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pub/Sub](</ja-JP/automation/cron-jobs>), [Webhook](</ja-JP/cli/webhooks>), [Webhook](</ja-JP/automation/cron-jobs#webhooks>), [Webhook](</ja-JP/automation/cron-jobs>)

自動化フック 11個の機能

実験的0%

アルファ68%

ベータ79%

[フック](</ja-JP/automation/hooks>), [フック](</ja-JP/cli/hooks>), [フック](</ja-JP/plugins/hooks>), [Plugin権限リクエスト](</ja-JP/plugins/plugin-permission-requests>), [SDKサブパス](</ja-JP/plugins/sdk-subpaths>)

バックグラウンドタスクとフロー 10個の機能

実験的0%

アルファ68%

ベータ79%

[タスク](</ja-JP/automation/tasks>), [インデックス](</ja-JP/automation>), [タスク](</ja-JP/cli/tasks>), [TaskFlow](</ja-JP/automation/taskflow>), [SDKランタイム](</ja-JP/plugins/sdk-runtime>)

Heartbeat 5個の機能

実験的14%

ベータ79%

ベータ79%

[インデックス](</ja-JP/automation>), [Heartbeat](</ja-JP/gateway/heartbeat>), [コミットメント](</ja-JP/concepts/commitments>)

ポーリング制御 10個の機能

実験的0%

アルファ68%

ベータ79%

[ポーリング](</ja-JP/cli/message>), [メッセージ](</ja-JP/cli/message>), [Telegram](</ja-JP/channels/telegram>), [Microsoft Teams](</ja-JP/channels/msteams>), [バックグラウンドプロセス](</ja-JP/gateway/background-process>)

メディア理解とメディア生成 - M2 アルファ - 6領域

幅広い機能面は存在しますが、プロバイダー差異、ファイル制限、Node/アプリ間の同等性により、まだ安定していません。

カバレッジ 実験的 - 2%品質 アルファ - 64%完全性 アルファ - 68%なし

メディア取り込みとアクセス 8 件の機能

実験的0%

アルファ61%

アルファ68%

[メディアの概要](</ja-JP/tools/media-overview>), [メディア理解](</ja-JP/nodes/media-understanding>), [安全なファイル操作](</ja-JP/gateway/security/secure-file-operations>), [Pdf](</ja-JP/tools/pdf>), [画像生成](</ja-JP/tools/image-generation>), [Qr](</ja-JP/cli/qr>), [Line](</ja-JP/channels/line>), [Whatsapp](</ja-JP/channels/whatsapp>)

チャネルのメディア処理 5 件の機能

実験的0%

アルファ61%

アルファ68%

[画像](</ja-JP/nodes/images>), [メディアの概要](</ja-JP/tools/media-overview>), [Discord](</ja-JP/channels/discord>)

メディア設定 1 件の機能

実験的0%

アルファ61%

アルファ68%

[メディアの概要](</ja-JP/tools/media-overview>), [画像生成](</ja-JP/tools/image-generation>), [Manifest](</ja-JP/plugins/manifest>), [Codex Harness](</ja-JP/plugins/codex-harness>)

テキスト読み上げ配信 2 件の機能

実験的0%

アルファ61%

アルファ68%

[Tts](</ja-JP/tools/tts>), [メディアの概要](</ja-JP/tools/media-overview>), [Discord](</ja-JP/channels/discord>)

メディア理解 12 件の機能

実験的7%

アルファ69%

アルファ69%

[音声](</ja-JP/nodes/audio>), [メディア理解](</ja-JP/nodes/media-understanding>), [メディアの概要](</ja-JP/tools/media-overview>), [Whatsapp](</ja-JP/channels/whatsapp>), [画像](</ja-JP/nodes/images>), [Infer](</ja-JP/cli/infer>), [Pdf](</ja-JP/tools/pdf>)

メディア生成 17 件の機能

実験的5%

アルファ69%

アルファ69%

[画像生成](</ja-JP/tools/image-generation>), [メディアの概要](</ja-JP/tools/media-overview>), [Skills](</ja-JP/tools/skills>), [音楽生成](</ja-JP/tools/music-generation>), [動画生成](</ja-JP/tools/video-generation>)

音声とリアルタイム会話 - M2 アルファ - 6 領域

Control UI、アプリ、プロバイダーに複数の実装があります。ベータに進む前に、レイテンシ、障害モード、セットアップのスコアカードが必要です。

カバレッジ 実験的 - 0%品質 アルファ - 61%完全性 アルファ - 68%なし

Talkプロバイダー 7件の機能

実験的0%

アルファ61%

アルファ68%

[Openai](</ja-JP/providers/openai>), [Google](</ja-JP/providers/google>), [SdkプロバイダーPlugin](</ja-JP/plugins/sdk-provider-plugins>), [Talk](</ja-JP/nodes/talk>), [Control Ui](</ja-JP/web/control-ui>)

リアルタイムTalkセッション 11件の機能

実験的0%

アルファ61%

アルファ68%

[Talk](</ja-JP/nodes/talk>), [Control Ui](</ja-JP/web/control-ui>)

音声と文字起こし 5件の機能

実験的0%

アルファ61%

アルファ68%

[Talk](</ja-JP/nodes/talk>), [Openai](</ja-JP/providers/openai>), [Google](</ja-JP/providers/google>)

ネイティブアプリTalk 4件の機能

実験的0%

アルファ61%

アルファ68%

[Talk](</ja-JP/nodes/talk>), [Voicewake](</ja-JP/platforms/mac/voicewake>)

音声ウェイクとルーティング 4件の機能

実験的0%

アルファ61%

アルファ68%

[Voicewake](</ja-JP/nodes/voicewake>), [Voicewake](</ja-JP/platforms/mac/voicewake>), [音声オーバーレイ](</ja-JP/platforms/mac/voice-overlay>)

Talkの可観測性 5件の機能

実験的0%

アルファ61%

アルファ68%

[Control Ui](</ja-JP/web/control-ui>), [音声オーバーレイ](</ja-JP/platforms/mac/voice-overlay>), [Talk](</ja-JP/nodes/talk>)

TUI - M2アルファ - 5領域

ドキュメントとソースには存在するが、主要なユーザーワークフローとしては目立ちにくい。明示的なシナリオ定義が必要。

カバレッジ 実験的 - 0%品質 アルファ - 59%完全性 アルファ - 66%なし

ランタイムモード 14個の機能

実験的0%

Alpha59%

Alpha66%

[Tui](</ja-JP/cli/tui>), [Tui](</ja-JP/web/tui>), [索引](</ja-JP/cli>)

入力とコマンド 8個の機能

実験的0%

Alpha59%

Alpha66%

[Tui](</ja-JP/web/tui>)

セッション管理 3個の機能

実験的0%

Alpha59%

Alpha66%

[Tui](</ja-JP/web/tui>), [セッション](</ja-JP/cli/sessions>)

ローカルシェル実行 4個の機能

実験的0%

Alpha59%

Alpha66%

[Tui](</ja-JP/web/tui>), [Tui](</ja-JP/cli/tui>)

レンダリングと出力の安全性 4個の機能

実験的0%

Alpha59%

Alpha66%

[Tui](</ja-JP/web/tui>), [Qr](</ja-JP/cli/qr>), [ログ](</ja-JP/cli/logs>), [補完](</ja-JP/cli/completion>)

ClawHub - M2 Alpha - 4領域

公開ドキュメントとエコシステムの概念は存在します。インストール、信頼、更新、ロールバック、互換性スコアカードが必要です。

カバレッジ 実験的 - 0%品質 Alpha - 58%完全性 Alpha - 62%なし

公開 7 個の機能

実験的0%

アルファ54%

アルファ55%

[公開](</ja-JP/clawhub/publishing>), [Skills の作成](</ja-JP/tools/creating-skills>), [コミュニティ](</ja-JP/plugins/community>)

カタログ検出 5 個の機能

実験的0%

アルファ61%

アルファ68%

[Plugin](</ja-JP/tools/plugin>), [Plugins](</ja-JP/cli/plugins>), [Skills](</ja-JP/cli/skills>), [Skills](</ja-JP/tools/skills>), [コミュニティ](</ja-JP/plugins/community>)

互換性と信頼性 12 個の機能

実験的0%

アルファ55%

アルファ56%

[Plugin](</ja-JP/tools/plugin>), [Plugins](</ja-JP/cli/plugins>), [互換性](</ja-JP/plugins/compatibility>), [Plugin インベントリ](</ja-JP/plugins/plugin-inventory>), [公開](</ja-JP/clawhub/publishing>), [Skills](</ja-JP/tools/skills>), [Skills 設定](</ja-JP/tools/skills-config>)

Plugin ライフサイクルと健全性 26 個の機能

実験的0%

アルファ61%

アルファ68%

[Plugin](</ja-JP/tools/plugin>), [Plugins](</ja-JP/cli/plugins>), [Skills](</ja-JP/cli/skills>), [Skills](</ja-JP/tools/skills>), [プロトコル](</ja-JP/gateway/protocol>), [バンドル](</ja-JP/plugins/bundles>), [依存関係の解決](</ja-JP/plugins/dependency-resolution>)

OpenClaw アプリ SDK - M2 アルファ - 6 領域

OpenClaw アプリ SDK は、Gateway ランタイムおよび Plugin SDK とは別個の外部アプリ契約です。現在のスコアリングでは、公開パッケージ化、自動検出、承認、ヘルパー、互換性の周辺にギャップがある実際の `@openclaw/sdk` パスが示されています。

カバレッジ 実験的 - 3%品質 アルファ - 54%完成度 アルファ - 53%なし

クライアント API 4 機能

実験的0%

アルファ51%

アルファ50%

[OpenClaw SDK](</ja-JP/gateway/external-apps>), [OpenClaw SDK API 設計](</ja-JP/gateway/external-apps>)

Gateway アクセス 5 機能

実験的0%

アルファ53%

アルファ54%

[OpenClaw SDK](</ja-JP/gateway/external-apps>), [OpenClaw SDK API 設計](</ja-JP/gateway/external-apps>), [プロトコル](</ja-JP/gateway/protocol>), [インデックス](</ja-JP/gateway/security>)

エージェント会話 6 機能

実験的0%

アルファ52%

アルファ52%

[OpenClaw SDK](</ja-JP/gateway/external-apps>), [OpenClaw SDK API 設計](</ja-JP/gateway/external-apps>), [プロトコル](</ja-JP/gateway/protocol>)

イベントと承認 5 機能

実験的0%

アルファ52%

アルファ52%

[OpenClaw SDK](</ja-JP/gateway/external-apps>), [OpenClaw SDK API 設計](</ja-JP/gateway/external-apps>), [プロトコル](</ja-JP/gateway/protocol>)

リソースヘルパー 5 機能

実験的17%

アルファ62%

アルファ53%

[OpenClaw SDK](</ja-JP/gateway/external-apps>), [OpenClaw SDK API 設計](</ja-JP/gateway/external-apps>)

互換性 5 機能

実験的0%

アルファ54%

アルファ55%

[OpenClaw SDK API 設計](</ja-JP/gateway/external-apps>), [Typebox](</ja-JP/concepts/typebox>), [プロトコル](</ja-JP/gateway/protocol>)

### プラットフォーム

Linux Gateway ホスト - M4 安定版 - 5 領域

Node ランタイムが推奨され、systemd ユーザーサービスが文書化されており、VPS/container ガイダンスは幅広く用意されています。

カバレッジ 実験的 - 0%品質 ベータ - 75%完全性 安定 - 89%部分的 - 4

ホストセットアップと更新 4 機能 / LTS 対応

実験的0%

ベータ75%

安定版89%

[索引](</ja-JP/install>), [更新](</ja-JP/install/updating>), [Linux](</ja-JP/platforms/linux>), [索引](</ja-JP/platforms>)

Gateway ランタイムとサービス制御 6 機能 / LTS 対応

実験的0%

ベータ75%

安定版89%

[索引](</ja-JP/gateway>), [Gateway](</ja-JP/cli/gateway>), [Linux](</ja-JP/platforms/linux>), [Vps](</ja-JP/vps>)

リモートアクセスとセキュリティ 6 機能 / LTS 対応

実験的0%

ベータ75%

安定版89%

[リモート](</ja-JP/gateway/remote>), [Tailscale](</ja-JP/gateway/tailscale>), [公開 Runbook](</ja-JP/gateway/security/exposure-runbook>), [認証](</ja-JP/gateway/authentication>), [シークレット](</ja-JP/gateway/secrets>)

診断と修復 4 機能 / LTS 対応

実験的0%

ベータ75%

安定版89%

[ステータス](</ja-JP/cli/status>), [ログ](</ja-JP/cli/logs>), [Doctor](</ja-JP/cli/doctor>), [診断](</ja-JP/gateway/diagnostics>), [索引](</ja-JP/gateway>)

デプロイ対象 3 機能

実験的0%

ベータ75%

安定版89%

[Vps](</ja-JP/vps>), [Docker](</ja-JP/install/docker>), [Hetzner](</ja-JP/install/hetzner>), [Digitalocean](</ja-JP/install/digitalocean>), [Kubernetes](</ja-JP/install/kubernetes>), [Podman](</ja-JP/install/podman>)

macOS Gateway ホスト - M4 安定版 - 7 領域

LaunchAgent サービスパス、ローカル/リモート Gateway モード、CLI インストール、アプリ連携が文書化されています。

カバレッジ 実験的 - 0%品質 ベータ - 74%完全性 安定版 - 88%なし

CLI セットアップ 4 件の機能

実験的0%

ベータ74%

安定版88%

[Macos](</ja-JP/platforms/macos>), [同梱 Gateway](</ja-JP/platforms/mac/bundled-gateway>), [インストーラー](</ja-JP/install/installer>), [Node](</ja-JP/install/node>)

ローカル Gateway 統合 9 件の機能

実験的0%

ベータ74%

安定版88%

[Macos](</ja-JP/platforms/macos>), [同梱 Gateway](</ja-JP/platforms/mac/bundled-gateway>), [リモート](</ja-JP/platforms/mac/remote>), [索引](</ja-JP/gateway>), [Gateway](</ja-JP/cli/gateway>), [Bonjour](</ja-JP/gateway/bonjour>)

リモート Gateway モード 5 件の機能

実験的0%

ベータ74%

安定版88%

[リモート](</ja-JP/platforms/mac/remote>), [リモート](</ja-JP/gateway/remote>), [Tailscale](</ja-JP/gateway/tailscale>)

Gateway サービスライフサイクル 10 件の機能

実験的0%

ベータ74%

安定版88%

[Macos](</ja-JP/platforms/macos>), [同梱 Gateway](</ja-JP/platforms/mac/bundled-gateway>), [Gateway](</ja-JP/cli/gateway>), [索引](</ja-JP/gateway>), [更新](</ja-JP/cli/update>), [更新](</ja-JP/install/updating>), [アンインストール](</ja-JP/install/uninstall>), [トラブルシューティング](</ja-JP/gateway/troubleshooting>)

診断とオブザーバビリティ 4 件の機能

実験的0%

ベータ74%

安定版88%

[同梱 Gateway](</ja-JP/platforms/mac/bundled-gateway>), [Macos](</ja-JP/platforms/macos>), [Gateway](</ja-JP/cli/gateway>), [Doctor](</ja-JP/gateway/doctor>), [トラブルシューティング](</ja-JP/gateway/troubleshooting>)

権限とネイティブ機能 4 件の機能

実験的0%

ベータ74%

安定版88%

[Macos](</ja-JP/platforms/macos>), [リモート](</ja-JP/platforms/mac/remote>)

プロファイルと分離 5 件の機能

実験的0%

ベータ74%

安定版88%

[複数 Gateway](</ja-JP/gateway/multiple-gateways>), [索引](</ja-JP/gateway>), [Gateway](</ja-JP/cli/gateway>)

Docker と Podman ホスティング - M3 ベータ - 4 領域

インストールドキュメントが存在し、一般的なデプロイパスです。継続的なリリーススモークでアップグレードとボリュームの動作を取得した後に昇格します。

カバレッジ 実験的 - 7%品質 ベータ - 71%完全性 ベータ - 79%なし

コンテナセットアップ 6 件の機能

実験的0%

アルファ68%

ベータ79%

[Docker](</ja-JP/install/docker>), [Podman](</ja-JP/install/podman>)

コンテナ運用 11 件の機能

実験的0%

アルファ68%

ベータ79%

[Podman](</ja-JP/install/podman>), [Docker Vm Runtime](</ja-JP/install/docker-vm-runtime>), [Docker](</ja-JP/install/docker>), [Hetzner](</ja-JP/install/hetzner>), [Hostinger](</ja-JP/install/hostinger>)

イメージリリースと検証 5 件の機能

実験的29%

ベータ79%

ベータ79%

[Docker](</ja-JP/install/docker>), [Docker Vm Runtime](</ja-JP/install/docker-vm-runtime>), [Full Release Validation](</ja-JP/reference/full-release-validation>)

エージェントサンドボックスとツール 3 件の機能

実験的0%

アルファ68%

ベータ79%

[Docker](</ja-JP/install/docker>), [Docker Vm Runtime](</ja-JP/install/docker-vm-runtime>)

WSL2 経由の Windows - M3 ベータ - 6 領域

systemd/ユーザーサービスのガイダンスとブートチェーンのドキュメントを備えた、推奨される Windows パス。インストール/更新のスコアカードを繰り返した後に昇格します。

カバレッジ 実験的 - 6%品質 アルファ - 69%完全性 ベータ - 79%部分的 - 5

WSL セットアップ 6 個の機能 / LTS 対応

実験的0%

Alpha67%

Beta79%

[Windows](</ja-JP/platforms/windows>), [はじめに](</ja-JP/start/getting-started>)

CLI 8 個の機能 / LTS 対応

実験的0%

Alpha67%

Beta79%

[Windows](</ja-JP/platforms/windows>), [はじめに](</ja-JP/start/getting-started>), [更新](</ja-JP/install/updating>), [オンボード](</ja-JP/cli/onboard>), [Doctor](</ja-JP/cli/doctor>), [ステータス](</ja-JP/cli/status>), [ログ](</ja-JP/cli/logs>)

Gateway サービスライフサイクル 10 個の機能 / LTS 対応

実験的0%

Alpha67%

Beta79%

[Windows](</ja-JP/platforms/windows>), [インデックス](</ja-JP/gateway>), [Doctor](</ja-JP/gateway/doctor>)

Gateway アクセスと公開 11 個の機能 / LTS 対応

実験的0%

Alpha67%

Beta79%

[認証](</ja-JP/gateway/authentication>), [シークレット](</ja-JP/gateway/secrets>), [リモート](</ja-JP/gateway/remote>), [公開ランブック](</ja-JP/gateway/security/exposure-runbook>), [Windows](</ja-JP/platforms/windows>)

診断と修復 6 個の機能 / LTS 対応

実験的38%

Beta79%

Beta79%

[Windows](</ja-JP/platforms/windows>), [ステータス](</ja-JP/cli/status>), [ログ](</ja-JP/cli/logs>), [Doctor](</ja-JP/cli/doctor>), [Doctor](</ja-JP/gateway/doctor>)

ブラウザーと Control UI 6 個の機能

実験的0%

Alpha67%

Beta79%

[ブラウザー WSL2 Windows リモート CDP トラブルシューティング](</ja-JP/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [ブラウザー](</ja-JP/tools/browser>), [Control UI](</ja-JP/web/control-ui>)

Raspberry Pi と小型 Linux デバイス - M3 Beta - 4 領域

プラットフォームドキュメントは存在し、Gateway パスは Linux ベースです。さらに上位へ進めるには、ハードウェア固有のリリーススモーク証明が必要です。

カバレッジ 実験的 - 0%品質 Alpha - 67%完全性 Beta - 79%なし

セットアップと互換性 12 個の機能

実験的0%

アルファ67%

ベータ79%

[Raspberry Pi](</ja-JP/install/raspberry-pi>), [インデックス](</ja-JP/install>), [初回実行のFAQ](</ja-JP/help/faq-first-run>), [FAQ](</ja-JP/help/faq>), [Linux](</ja-JP/platforms/linux>), [インストーラー](</ja-JP/install/installer>)

リモートアクセスと認証 9 個の機能

実験的0%

アルファ67%

ベータ79%

[Raspberry Pi](</ja-JP/install/raspberry-pi>), [認証](</ja-JP/gateway/authentication>), [シークレット](</ja-JP/gateway/secrets>), [ペアリング](</ja-JP/gateway/pairing>), [デバイス](</ja-JP/cli/devices>), [リモート](</ja-JP/gateway/remote>), [Tailscale](</ja-JP/gateway/tailscale>)

Gateway ランタイム 10 個の機能

実験的0%

アルファ67%

ベータ79%

[インデックス](</ja-JP/gateway>), [Gateway](</ja-JP/cli/gateway>), [Raspberry Pi](</ja-JP/install/raspberry-pi>), [Linux](</ja-JP/platforms/linux>), [VPS](</ja-JP/vps>)

パフォーマンスと診断 5 個の機能

実験的0%

アルファ67%

ベータ79%

[Raspberry Pi](</ja-JP/install/raspberry-pi>), [Linux](</ja-JP/platforms/linux>), [ヘルス](</ja-JP/gateway/health>), [診断](</ja-JP/gateway/diagnostics>)

macOS コンパニオンアプリ - M3 ベータ - 8 領域

高機能なメニューバーアプリ、権限、Node モード、Canvas、音声ウェイク、WebChat、リモートモードが存在します。まだ変化が速いため、安定版は避けています。

カバレッジ 実験的 - 0%品質 アルファ - 66%完全性 ベータ - 78%なし

キャンバス 4 個の機能

実験的0%

アルファ66%

ベータ78%

[キャンバス](</ja-JP/platforms/mac/canvas>), [macOS](</ja-JP/platforms/macos>), [Webchat](</ja-JP/web/webchat>)

ローカルセットアップ 7 個の機能

実験的0%

アルファ66%

ベータ78%

[バンドル版 Gateway](</ja-JP/platforms/mac/bundled-gateway>), [macOS](</ja-JP/platforms/macos>), [子プロセス](</ja-JP/platforms/mac/child-process>), [開発セットアップ](</ja-JP/platforms/mac/dev-setup>)

ステータスと設定 5 個の機能

実験的0%

アルファ66%

ベータ78%

[メニューバー](</ja-JP/platforms/mac/menu-bar>), [アイコン](</ja-JP/platforms/mac/icon>), [macOS](</ja-JP/platforms/macos>), [ヘルス](</ja-JP/platforms/mac/health>), [ロギング](</ja-JP/platforms/mac/logging>), [リモート](</ja-JP/platforms/mac/remote>)

ネイティブ機能 5 個の機能

実験的0%

アルファ66%

ベータ78%

[macOS](</ja-JP/platforms/macos>), [XPC](</ja-JP/platforms/mac/xpc>), [権限](</ja-JP/platforms/mac/permissions>), [署名](</ja-JP/platforms/mac/signing>), [Peekaboo](</ja-JP/platforms/mac/peekaboo>)

リモート接続 3 個の機能

実験的0%

アルファ66%

ベータ78%

[リモート](</ja-JP/platforms/mac/remote>), [macOS](</ja-JP/platforms/macos>), [リモート](</ja-JP/gateway/remote>)

音声と Talk 3 個の機能

実験的0%

アルファ66%

ベータ78%

[Voicewake](</ja-JP/platforms/mac/voicewake>), [音声オーバーレイ](</ja-JP/platforms/mac/voice-overlay>), [Talk](</ja-JP/nodes/talk>), [macOS](</ja-JP/platforms/macos>)

WebChat 3 個の機能

実験的0%

アルファ66%

ベータ78%

[Webchat](</ja-JP/platforms/mac/webchat>), [macOS](</ja-JP/platforms/macos>), [Webchat](</ja-JP/web/webchat>)

リモート WebChat 5 個の機能

実験的0%

アルファ66%

ベータ78%

[Webchat](</ja-JP/platforms/mac/webchat>), [リモート](</ja-JP/gateway/remote>), [リモート](</ja-JP/platforms/mac/remote>)

Android app - M2 Alpha - 7 areas

公開 Google Play パスは存在しますが、アプリのドキュメントでは再ビルドをまだ極めてアルファ段階と説明し、リリース強化作業を明記しています。

カバレッジ 実験的 - 0%品質 アルファ - 59%完全性 アルファ - 66%なし

メディアキャプチャ 1 件の機能

実験的0%

アルファ59%

アルファ66%

[Android](</ja-JP/platforms/android>), [カメラ](</ja-JP/nodes/camera>)

モバイルチャット 1 件の機能

実験的0%

アルファ59%

アルファ66%

[Android](</ja-JP/platforms/android>)

接続セットアップ 1 件の機能

実験的0%

アルファ59%

アルファ66%

[Android](</ja-JP/platforms/android>), [Bonjour](</ja-JP/gateway/bonjour>), [ペアリング](</ja-JP/gateway/pairing>)

配布 3 件の機能

実験的0%

アルファ59%

アルファ66%

[Android](</ja-JP/platforms/android>)

設定 1 件の機能

実験的0%

アルファ59%

アルファ66%

[Android](</ja-JP/platforms/android>)

音声 1 件の機能

実験的0%

アルファ59%

アルファ66%

[Android](</ja-JP/platforms/android>), [トーク](</ja-JP/nodes/talk>)

デバイスランタイム 2 件の機能

実験的0%

アルファ59%

アルファ66%

[Android](</ja-JP/platforms/android>), [トラブルシューティング](</ja-JP/nodes/troubleshooting>), [プロトコル](</ja-JP/gateway/protocol>)

ネイティブ Windows - M2 アルファ - 4 領域

コア CLI/Gateway フローは動作しますが、ドキュメントでは引き続き完全な体験には WSL2 を推奨し、ネイティブ実行時の注意点を列挙しています。

カバレッジ 実験的 - 0%品質 アルファ - 58%完成度 アルファ - 66%部分的 - 1

CLI 9 個の機能 / LTS 対応

実験的0%

アルファ54%

アルファ64%

[索引](</ja-JP/install>), [インストーラー](</ja-JP/install/installer>), [Windows](</ja-JP/platforms/windows>), [はじめに](</ja-JP/start/getting-started>), [オンボード](</ja-JP/cli/onboard>)

Gateway 管理 11 個の機能

実験的0%

アルファ59%

アルファ66%

[Windows](</ja-JP/platforms/windows>), [索引](</ja-JP/gateway>), [Gateway](</ja-JP/cli/gateway>), [Doctor](</ja-JP/cli/doctor>)

ネットワーキング 4 個の機能

実験的0%

アルファ59%

アルファ66%

[Windows](</ja-JP/platforms/windows>), [索引](</ja-JP/gateway>), [Gateway](</ja-JP/cli/gateway>)

更新 4 個の機能

実験的0%

アルファ59%

アルファ66%

[更新](</ja-JP/install/updating>), [CI](</ja-JP/ci>)

Kubernetes ホスティング - M2 アルファ - 4 領域

Kubernetes ホスティングは、Kustomize ベースの独立したクラスター展開パスです。現在のスコアリングでは、Kubernetes 固有の CI、ingress/TLS/NetworkPolicy パッケージング、バックアップ/復元、本番公開の堅牢化に関するギャップを伴う、実際の最小限の展開パスが示されています。

カバレッジ 試験的 - 0%品質 アルファ - 55%完成度 アルファ - 61%なし

デプロイ設定 5 件のケイパビリティ

試験的0%

アルファ55%

アルファ61%

[Kubernetes](</ja-JP/install/kubernetes>), [インデックス](</ja-JP/install>)

設定とシークレット 5 件のケイパビリティ

試験的0%

アルファ55%

アルファ61%

[Kubernetes](</ja-JP/install/kubernetes>), [シークレット](</ja-JP/gateway/secrets>), [環境](</ja-JP/help/environment>)

アクセスと公開 5 件のケイパビリティ

試験的0%

アルファ55%

アルファ61%

[Kubernetes](</ja-JP/install/kubernetes>), [認証](</ja-JP/gateway/authentication>), [リモート](</ja-JP/gateway/remote>), [公開ランブック](</ja-JP/gateway/security/exposure-runbook>)

クラスターライフサイクル 5 件のケイパビリティ

試験的0%

アルファ55%

アルファ61%

[Kubernetes](</ja-JP/install/kubernetes>), [インデックス](</ja-JP/gateway>)

iOS アプリ - M1 試験的 - 8 領域

内部プレビュー / 超アルファ版。TestFlight とリレー支援のプッシュフローは存在しますが、公開配布はまだありません。

カバレッジ 実験的 - 0%品質 実験的 - 41%完全性 実験的 - 44%なし

メディアと共有 1 件の機能

実験的0%

実験的41%

実験的44%

[Ios](</ja-JP/platforms/ios>), [カメラ](</ja-JP/nodes/camera>)

キャンバスと画面 1 件の機能

実験的0%

実験的41%

実験的44%

[Ios](</ja-JP/platforms/ios>), [キャンバス](</ja-JP/plugins/reference/canvas>)

チャットとセッション 1 件の機能

実験的0%

実験的41%

実験的44%

[Ios](</ja-JP/platforms/ios>), [ウェブチャット](</ja-JP/web/webchat>), [プロトコル](</ja-JP/gateway/protocol>)

Gateway のセットアップと診断 7 件の機能

実験的0%

実験的41%

実験的44%

[Ios](</ja-JP/platforms/ios>), [ペアリング](</ja-JP/channels/pairing>)

配布 1 件の機能

実験的0%

実験的41%

実験的44%

[Ios](</ja-JP/platforms/ios>)

デバイスコマンド 2 件の機能

実験的0%

実験的41%

実験的44%

[Ios](</ja-JP/platforms/ios>), [プロトコル](</ja-JP/gateway/protocol>)

通知とバックグラウンド 1 件の機能

実験的0%

実験的41%

実験的44%

[Ios](</ja-JP/platforms/ios>), [設定](</ja-JP/gateway/configuration>)

音声 1 件の機能

実験的0%

実験的41%

実験的44%

[Ios](</ja-JP/platforms/ios>), [トーク](</ja-JP/nodes/talk>)

Nix install path - M1 Experimental - 5 areas

任意のインストールフロー。アルファ/ベータへの昇格前に、サポート保証をより明確にする必要があります。

カバレッジ 実験的 - 0%品質 実験的 - 41%完全性 実験的 - 44%なし

インストールの引き継ぎ 4 機能

実験的0%

実験的41%

実験的44%

[Nix](</ja-JP/install/nix>), [インデックス](</ja-JP/install>), [ドキュメントディレクトリ](</ja-JP/start/docs-directory>)

Plugin ライフサイクル 4 機能

実験的0%

実験的41%

実験的44%

[Plugin を管理](</ja-JP/plugins/manage-plugins>), [Plugin](</ja-JP/tools/plugin>), [Nix](</ja-JP/install/nix>)

アクティベーションとアプリ UX 7 機能

実験的0%

実験的41%

実験的44%

[Nix](</ja-JP/install/nix>)

設定と状態 7 機能

実験的0%

実験的41%

実験的44%

[Nix](</ja-JP/install/nix>), [セットアップ](</ja-JP/cli/setup>), [環境](</ja-JP/help/environment>)

サービスランタイムとガード 8 機能

実験的0%

実験的41%

実験的44%

[Nix](</ja-JP/install/nix>), [セットアップ](</ja-JP/cli/setup>), [Doctor](</ja-JP/cli/doctor>), [更新](</ja-JP/cli/update>)

watchOS コンパニオン サーフェス - M1 実験的 - 5 領域

ソースには Watch アプリ/拡張機能のサーフェスがありますが、公開ドキュメントではこれをまだユーザー向け機能として提示していません。

カバレッジ 実験的 - 0%品質 実験的 - 41%完全性 実験的 - 44%なし

配信とリカバリー 7 個の機能

実験的0%

実験的41%

実験的44%

[iOS](</ja-JP/platforms/ios>)

実行承認 3 個の機能

実験的0%

実験的41%

実験的44%

[実行承認](</ja-JP/tools/exec-approvals>), [iOS](</ja-JP/platforms/ios>)

配布とサポート 6 個の機能

実験的0%

実験的41%

実験的44%

[iOS](</ja-JP/platforms/ios>)

通知と返信 7 個の機能

実験的0%

実験的41%

実験的44%

[iOS](</ja-JP/platforms/ios>)

Watch App UI 3 個の機能

実験的0%

実験的41%

実験的44%

[iOS](</ja-JP/platforms/ios>)

Linux コンパニオンアプリ - M0 計画中 - 5 領域

ドキュメントではネイティブの Linux コンパニオンアプリは計画中とされており、現在 Linux でサポートされているパスは Gateway です。

カバレッジ 実験的 - 0%品質 実験的 - 19%完全性 実験的 - 21%なし

アプリ配布 3つの機能

実験的0%

実験的19%

実験的21%

[Linux](</ja-JP/platforms/linux>), [インデックス](</ja-JP/platforms>), [インデックス](</ja-JP/install>)

Gateway 接続 4つの機能

実験的0%

実験的19%

実験的21%

[Linux](</ja-JP/platforms/linux>), [インデックス](</ja-JP/gateway>), [ペアリング](</ja-JP/gateway/pairing>), [リモート](</ja-JP/gateway/remote>)

チャットとセッション 3つの機能

実験的0%

実験的19%

実験的21%

[Linux](</ja-JP/platforms/linux>), [プロトコル](</ja-JP/gateway/protocol>), [Webchat](</ja-JP/web/webchat>)

デスクトップ機能 9つの機能

実験的0%

実験的19%

実験的21%

[Linux](</ja-JP/platforms/linux>), [Exec 承認](</ja-JP/tools/exec-approvals>), [シークレット](</ja-JP/gateway/secrets>), [インデックス](</ja-JP/nodes>), [Exec](</ja-JP/tools/exec>), [Talk](</ja-JP/nodes/talk>), [カメラ](</ja-JP/nodes/camera>)

ステータスと診断 7つの機能

実験的0%

実験的19%

実験的21%

[Linux](</ja-JP/platforms/linux>), [Openclaw](</ja-JP/start/openclaw>), [Doctor](</ja-JP/gateway/doctor>)

ネイティブ Windows コンパニオンアプリ - M0 計画中 - 5領域

計画中のみ。

カバレッジ 実験的 - 0%品質 実験的 - 19%完全性 実験的 - 21%なし

インストールと更新 4 機能

実験的0%

実験的19%

実験的21%

[Windows](</ja-JP/platforms/windows>), [インデックス](</ja-JP/install>)

Gateway 接続 3 機能

実験的0%

実験的19%

実験的21%

[Windows](</ja-JP/platforms/windows>), [インデックス](</ja-JP/gateway>), [ペアリング](</ja-JP/gateway/pairing>), [リモート](</ja-JP/gateway/remote>)

チャットセッション 2 機能

実験的0%

実験的19%

実験的21%

[Windows](</ja-JP/platforms/windows>), [プロトコル](</ja-JP/gateway/protocol>)

ステータスと修復 5 機能

実験的0%

実験的19%

実験的21%

[Windows](</ja-JP/platforms/windows>), [Doctor](</ja-JP/gateway/doctor>), [インデックス](</ja-JP/gateway>)

デスクトップツールと権限 10 機能

実験的0%

実験的19%

実験的21%

[Windows](</ja-JP/platforms/windows>), [インデックス](</ja-JP/nodes>), [Exec](</ja-JP/tools/exec>), [Exec 承認](</ja-JP/tools/exec-approvals>), [インデックス](</ja-JP/gateway/security>)

### チャンネル

Discord - M4 安定版 - 6 領域

詳細なドキュメントと幅広い機能カバレッジ。音声/委任パスは、ベータ/アルファとして別途スコアリングする必要があります。

カバレッジ 実験的 - 0%品質 ベータ - 73%完成度 安定版 - 87%部分的 - 4

チャンネルのセットアップと運用 10 件の機能 / LTS サポート対象

実験的0%

ベータ73%

安定版87%

[Discord](</ja-JP/channels/discord>), [Discord](</ja-JP/plugins/reference/discord>), [Fly](</ja-JP/install/fly>), [スラッシュコマンド](</ja-JP/tools/slash-commands>), [ヘルス](</ja-JP/gateway/health>), [チャンネル](</ja-JP/cli/channels>), [設定チャンネル](</ja-JP/gateway/config-channels>)

アクセスとアイデンティティ 6 件の機能 / LTS サポート対象

実験的0%

ベータ73%

安定版87%

[Discord](</ja-JP/channels/discord>), [ペアリング](</ja-JP/channels/pairing>), [アクセスグループ](</ja-JP/channels/access-groups>), [グループ](</ja-JP/channels/groups>)

会話のルーティングと配信 12 件の機能 / LTS サポート対象

実験的0%

ベータ73%

安定版87%

[Discord](</ja-JP/channels/discord>), [チャンネルルーティング](</ja-JP/channels/channel-routing>), [グループ](</ja-JP/channels/groups>), [アクセスグループ](</ja-JP/channels/access-groups>), [ACP エージェント](</ja-JP/tools/acp-agents>), [サブエージェント](</ja-JP/tools/subagents>)

メディアとリッチコンテンツ 1 件の機能 / LTS サポート対象

実験的0%

ベータ73%

安定版87%

[Discord](</ja-JP/channels/discord>)

ネイティブコントロールと承認 5 件の機能

実験的0%

ベータ73%

安定版87%

[Discord](</ja-JP/channels/discord>), [スラッシュコマンド](</ja-JP/tools/slash-commands>)

リアルタイム音声と通話 5 件の機能

実験的0%

ベータ73%

安定版87%

[Discord](</ja-JP/channels/discord>), [Openai](</ja-JP/providers/openai>), [Elevenlabs](</ja-JP/providers/elevenlabs>), [QA E2E 自動化](</ja-JP/concepts/qa-e2e-automation>), [設定チャンネル](</ja-JP/gateway/config-channels>)

Telegram - M3 ベータ - 5 領域

コアチャンネルは通常利用には十分成熟していますが、ばらつきの大きい UX とメディアのエッジケースには、継続的なシナリオ証明が必要です。

カバレッジ 実験的 - 0%品質 アルファ - 68%完全性 ベータ - 78%完全 - 5

チャネルのセットアップと運用 10 個の機能 / LTS 対応

実験的0%

Alpha66%

Beta78%

[Telegram](</ja-JP/channels/telegram>), [設定チャネル](</ja-JP/gateway/config-channels>), [チャネル](</ja-JP/cli/channels>)

アクセスとアイデンティティ 10 個の機能 / LTS 対応

実験的0%

Alpha66%

Beta78%

[Telegram](</ja-JP/channels/telegram>), [ペアリング](</ja-JP/channels/pairing>), [アクセスグループ](</ja-JP/channels/access-groups>), [グループ](</ja-JP/channels/groups>), [マルチエージェント](</ja-JP/concepts/multi-agent>)

会話のルーティングと配信 1 個の機能 / LTS 対応

実験的0%

Alpha66%

Beta78%

[Telegram](</ja-JP/channels/telegram>), [グループ](</ja-JP/channels/groups>), [マルチエージェント](</ja-JP/concepts/multi-agent>)

メディアとリッチコンテンツ 1 個の機能 / LTS 対応

実験的0%

Alpha66%

Beta78%

[Telegram](</ja-JP/channels/telegram>), [位置情報](</ja-JP/channels/location>)

ネイティブコントロールと承認 9 個の機能 / LTS 対応

実験的0%

Beta77%

Beta79%

[Telegram](</ja-JP/channels/telegram>), [実行承認](</ja-JP/tools/exec-approvals>), [リアクション](</ja-JP/tools/reactions>)

Slack - M3 Beta - 5 領域

第一級のチャネルドキュメントとルーティングサーフェス。ワークスペースのインストール/管理シナリオのスコアカードが必要です。

カバレッジ 実験的 - 0%品質 Alpha - 66%完成度 Beta - 78%完全 - 5

チャネル設定と運用 10 機能 / LTS サポート対象

実験的0%

アルファ66%

ベータ78%

[Slack](</ja-JP/channels/slack>), [Slack](</ja-JP/plugins/reference/slack>), [シークレット](</ja-JP/gateway/secrets>), [QA E2E 自動化](</ja-JP/concepts/qa-e2e-automation>), [トラブルシューティング](</ja-JP/channels/troubleshooting>)

アクセスと ID 1 機能 / LTS サポート対象

実験的0%

アルファ66%

ベータ78%

[Slack](</ja-JP/channels/slack>), [ペアリング](</ja-JP/channels/pairing>)

会話ルーティングと配信 5 機能 / LTS サポート対象

実験的0%

アルファ66%

ベータ78%

[Slack](</ja-JP/channels/slack>), [ボットループ保護](</ja-JP/channels/bot-loop-protection>), [ペアリング](</ja-JP/channels/pairing>)

メディアとリッチコンテンツ 1 機能 / LTS サポート対象

実験的0%

アルファ66%

ベータ78%

[Slack](</ja-JP/channels/slack>), [QA E2E 自動化](</ja-JP/concepts/qa-e2e-automation>)

ネイティブコントロールと承認 8 機能 / LTS サポート対象

実験的0%

アルファ66%

ベータ78%

[Slack](</ja-JP/channels/slack>), [スラッシュコマンド](</ja-JP/tools/slash-commands>), [実行承認](</ja-JP/tools/exec-approvals>)

iMessage と BlueBubbles - M3 ベータ - 5 領域

サポート対象の iMessage は、サインイン済みの macOS Messages ホスト上の imsg 経由で動作します。レガシー BlueBubbles 設定には移行が必要です。macOS 権限、SSH ラッパー、SIP/プライベート API、移行時の注意点を見える状態にしておいてください。

カバレッジ 実験的 - 0%品質 アルファ - 66%完全性 ベータ - 78%なし

チャンネル設定と運用 11 機能

実験的0%

アルファ66%

ベータ78%

[Bluebubbles iMessage](</ja-JP/announcements/bluebubbles-imessage>), [Bluebubbles からの iMessage](</ja-JP/channels/imessage-from-bluebubbles>), [チャンネル設定](</ja-JP/gateway/config-channels>), [iMessage](</ja-JP/channels/imessage>)

アクセスと ID 6 機能

実験的0%

アルファ66%

ベータ78%

[iMessage](</ja-JP/channels/imessage>), [Bluebubbles からの iMessage](</ja-JP/channels/imessage-from-bluebubbles>), [チャンネル設定](</ja-JP/gateway/config-channels>)

会話ルーティングと配信 4 機能

実験的0%

アルファ66%

ベータ78%

[iMessage](</ja-JP/channels/imessage>)

メディアとリッチコンテンツ 7 機能

実験的0%

アルファ66%

ベータ78%

[iMessage](</ja-JP/channels/imessage>), [Bluebubbles からの iMessage](</ja-JP/channels/imessage-from-bluebubbles>), [チャンネル設定](</ja-JP/gateway/config-channels>)

ネイティブ制御と承認 3 機能

実験的0%

アルファ66%

ベータ78%

[iMessage](</ja-JP/channels/imessage>)

WhatsApp - M3 ベータ - 5 領域

コアパスは重要でドキュメント化されています。アップストリームの Baileys/セッションの変動性により、Stable 未満に留まっています。

カバレッジ 実験的 - 0%品質 アルファ - 66%完全性 ベータ - 78%なし

チャネル設定と運用 5 個の機能

実験的0%

アルファ66%

ベータ78%

[WhatsApp](</ja-JP/channels/whatsapp>), [設定チャネル](</ja-JP/gateway/config-channels>), [WhatsApp](</ja-JP/plugins/reference/whatsapp>), [QA E2E 自動化](</ja-JP/concepts/qa-e2e-automation>), [Doctor](</ja-JP/gateway/doctor>)

アクセスとアイデンティティ 7 個の機能

実験的0%

アルファ66%

ベータ78%

[WhatsApp](</ja-JP/channels/whatsapp>), [設定チャネル](</ja-JP/gateway/config-channels>), [QA E2E 自動化](</ja-JP/concepts/qa-e2e-automation>), [ペアリング](</ja-JP/channels/pairing>)

会話のルーティングと配信 4 個の機能

実験的0%

アルファ66%

ベータ78%

[WhatsApp](</ja-JP/channels/whatsapp>), [グループメッセージ](</ja-JP/channels/group-messages>)

メディアとリッチコンテンツ 2 個の機能

実験的0%

アルファ66%

ベータ78%

[WhatsApp](</ja-JP/channels/whatsapp>)

ネイティブコントロールと承認 2 個の機能

実験的0%

アルファ66%

ベータ78%

[WhatsApp](</ja-JP/channels/whatsapp>)

Matrix - M2 アルファ - 6 領域

バンドルされた plugin を介してサポートされます。ブリッジ、認証、ルームライフサイクルのスコアカードが必要です。

カバレッジ 実験的 - 0%品質 アルファ - 60%完成度 アルファ - 67%なし

チャネル設定と運用 5個の機能

実験的0%

Alpha60%

Alpha67%

[Matrix](</ja-JP/channels/matrix>), [Matrix 移行](</ja-JP/channels/matrix-migration>)

アクセスとアイデンティティ 7個の機能

実験的0%

Alpha60%

Alpha67%

[Matrix](</ja-JP/channels/matrix>), [グループ](</ja-JP/channels/groups>), [ボットループ保護](</ja-JP/channels/bot-loop-protection>)

会話ルーティングと配信 1個の機能

実験的0%

Alpha60%

Alpha67%

[Matrix](</ja-JP/channels/matrix>)

メディアとリッチコンテンツ 1個の機能

実験的0%

Alpha60%

Alpha67%

[Matrix](</ja-JP/channels/matrix>)

ネイティブコントロールと承認 6個の機能

実験的0%

Alpha60%

Alpha67%

[Matrix](</ja-JP/channels/matrix>)

暗号化と検証 3個の機能

実験的0%

Alpha60%

Alpha67%

[Matrix](</ja-JP/channels/matrix>), [Matrix 移行](</ja-JP/channels/matrix-migration>)

Google Chat - M2 Alpha - 5領域

ドキュメント化されたチャネルですが、エンタープライズ/管理者向け設定により成熟度リスクが高まります。

カバレッジ 実験的 - 0%品質 Alpha - 59%完全性 Alpha - 66%なし

チャンネルのセットアップと運用 16個の機能

実験的0%

Alpha59%

Alpha66%

[Googlechat](</ja-JP/channels/googlechat>), [Googlechat](</ja-JP/plugins/reference/googlechat>), [チャンネル設定](</ja-JP/gateway/config-channels>), [ウィザード CLI リファレンス](</ja-JP/start/wizard-cli-reference>), [シークレット](</ja-JP/gateway/secrets>), [Secretref 認証情報サーフェス](</ja-JP/reference/secretref-credential-surface>), [ヘルス](</ja-JP/gateway/health>), [Plugin インベントリ](</ja-JP/plugins/plugin-inventory>), [インデックス](</ja-JP/channels>)

アクセスとアイデンティティ 11個の機能

実験的0%

Alpha59%

Alpha66%

[Googlechat](</ja-JP/channels/googlechat>), [ペアリング](</ja-JP/channels/pairing>), [アクセスグループ](</ja-JP/channels/access-groups>), [チャンネル設定](</ja-JP/gateway/config-channels>), [ボットループ保護](</ja-JP/channels/bot-loop-protection>), [チャンネルルーティング](</ja-JP/channels/channel-routing>)

会話のルーティングと配信 1個の機能

実験的0%

Alpha59%

Alpha66%

[Googlechat](</ja-JP/channels/googlechat>), [ボットループ保護](</ja-JP/channels/bot-loop-protection>), [アクセスグループ](</ja-JP/channels/access-groups>), [チャンネルルーティング](</ja-JP/channels/channel-routing>)

メディアとリッチコンテンツ 1個の機能

実験的0%

Alpha59%

Alpha66%

[Googlechat](</ja-JP/channels/googlechat>), [メッセージ](</ja-JP/cli/message>), [メディア理解](</ja-JP/nodes/media-understanding>), [Secretref 認証情報サーフェス](</ja-JP/reference/secretref-credential-surface>)

ネイティブコントロールと承認 16個の機能

実験的0%

Alpha59%

Alpha66%

[Googlechat](</ja-JP/channels/googlechat>), [メッセージ](</ja-JP/cli/message>), [メディア理解](</ja-JP/nodes/media-understanding>), [Secretref 認証情報サーフェス](</ja-JP/reference/secretref-credential-surface>), [リアクション](</ja-JP/tools/reactions>), [スラッシュコマンド](</ja-JP/tools/slash-commands>), [エージェント設定](</ja-JP/gateway/config-agents>), [メッセージライフサイクルリファクタリング](</ja-JP/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5領域

エンタープライズ認証/管理者フローには、明示的なシナリオ証明が必要です。

カバレッジ 実験的 - 0%品質 Alpha - 59%完全性 Alpha - 66%なし

チャンネル設定と運用 9 機能

実験的0%

アルファ59%

アルファ66%

[Msteams](</ja-JP/channels/msteams>), [Msteams](</ja-JP/plugins/reference/msteams>), [設定チャンネル](</ja-JP/gateway/config-channels>), [健全性](</ja-JP/gateway/health>)

アクセスとアイデンティティ 9 機能

実験的0%

アルファ59%

アルファ66%

[Msteams](</ja-JP/channels/msteams>), [ペアリング](</ja-JP/channels/pairing>), [アクセスグループ](</ja-JP/channels/access-groups>)

会話のルーティングと配信 5 機能

実験的0%

アルファ59%

アルファ66%

[Msteams](</ja-JP/channels/msteams>), [グループ](</ja-JP/channels/groups>), [チャンネルルーティング](</ja-JP/channels/channel-routing>)

メディアとリッチコンテンツ 5 機能

実験的0%

アルファ59%

アルファ66%

[Msteams](</ja-JP/channels/msteams>)

ネイティブコントロールと承認 5 機能

実験的0%

アルファ59%

アルファ66%

[Msteams](</ja-JP/channels/msteams>), [高度な Exec 承認](</ja-JP/tools/exec-approvals-advanced>)

Signal - M2 アルファ - 5 領域

対応チャンネルのドキュメントは存在します。インストールと再接続の証明をより強化する必要があります。

カバレッジ 実験的 - 0%品質 アルファ - 59%完成度 アルファ - 66%なし

チャンネル設定と運用 7 個の機能

実験的0%

アルファ59%

アルファ66%

[Signal](</ja-JP/channels/signal>), [Signal](</ja-JP/plugins/reference/signal>)

アクセスとアイデンティティ 6 個の機能

実験的0%

アルファ59%

アルファ66%

[Signal](</ja-JP/channels/signal>)

会話ルーティングと配信 1 個の機能

実験的0%

アルファ59%

アルファ66%

[Signal](</ja-JP/channels/signal>)

メディアとリッチコンテンツ 7 個の機能

実験的0%

アルファ59%

アルファ66%

[Signal](</ja-JP/channels/signal>)

ネイティブコントロールと承認 3 個の機能

実験的0%

アルファ59%

アルファ66%

[Signal](</ja-JP/channels/signal>)

Feishu、QQ Bot、WeChat、Yuanbao、Zalo、Zalo Personal、地域チャンネル - M2 アルファ - 4 領域

重要な地域カバレッジだが、公開サポートレベルはアカウント種別、上流の承認、メンテナーの証明に応じて調整する必要がある。

カバレッジ 実験的 - 0%品質 アルファ - 55%完成度 アルファ - 58%なし

チャンネルのセットアップと運用 6 個の機能

実験的0%

アルファ61%

アルファ68%

[インデックス](</ja-JP/channels>), [ペアリング](</ja-JP/channels/pairing>), [Feishu](</ja-JP/plugins/reference/feishu>), [アーキテクチャ内部](</ja-JP/plugins/architecture-internals>)

アクセスとアイデンティティ 1 個の機能

実験的0%

アルファ53%

アルファ54%

リンクされたドキュメントはありません

会話のルーティングと配信 1 個の機能

実験的0%

アルファ53%

アルファ54%

リンクされたドキュメントはありません

メディアとリッチコンテンツ 1 個の機能

実験的0%

アルファ53%

アルファ54%

リンクされたドキュメントはありません

Mattermost、LINE、IRC、Nextcloud Talk、Nostr、Twitch、Tlon、Synology Chat - M2 アルファ - 4 領域

サポート対象のサーフェスは存在しますが、成熟度はアップストリームとメンテナーのカバレッジによって異なる可能性があります。後で個別にスコアを付けてください。

カバレッジ 実験的 - 0%品質 アルファ - 53%完全性 アルファ - 54%なし

チャネル設定と運用 1件の機能

実験的0%

アルファ53%

アルファ54%

リンクされたドキュメントなし

アクセスとアイデンティティ 1件の機能

実験的0%

アルファ53%

アルファ54%

リンクされたドキュメントなし

会話ルーティングと配信 1件の機能

実験的0%

アルファ53%

アルファ54%

リンクされたドキュメントなし

メディアとリッチコンテンツ 1件の機能

実験的0%

アルファ53%

アルファ54%

リンクされたドキュメントなし

音声通話チャネル - M1 実験的 - 5領域

複雑なリアルタイム動作を伴う任意のPluginパス。パブリックベータの前にシナリオスコアカードが必要です。

カバレッジ 実験的 - 0%品質 実験的 - 41%完全性 実験的 - 44%なし

チャネル設定と運用 2 機能

実験的0%

実験的41%

実験的44%

[音声通話](</ja-JP/cli/voicecall>), [音声通話](</ja-JP/plugins/voice-call>), [プロトコル](</ja-JP/gateway/protocol>)

アクセスとアイデンティティ 1 機能

実験的0%

実験的41%

実験的44%

[音声通話](</ja-JP/plugins/voice-call>), [音声通話](</ja-JP/cli/voicecall>)

会話ルーティングと配信 1 機能

実験的0%

実験的41%

実験的44%

[音声通話](</ja-JP/plugins/voice-call>)

メディアとリッチコンテンツ 2 機能

実験的0%

実験的41%

実験的44%

[音声通話](</ja-JP/plugins/voice-call>), [Plugin インベントリ](</ja-JP/plugins/plugin-inventory>)

リアルタイム音声と通話 2 機能

実験的0%

実験的41%

実験的44%

[音声通話](</ja-JP/plugins/voice-call>)

### プロバイダーとツール

ブラウザー自動化、exec、サンドボックスツール - M3 ベータ - 3 領域

コアツールは文書化されていますが、ホストのセキュリティと権限 UX はアクティブなスコアカードレビューの対象にし続ける必要があります。

カバレッジ 実験的 - 21%品質 ベータ - 75%完全性 ベータ - 79%部分的 - 2

ブラウザー自動化 8個の機能

実験的13%

ベータ79%

ベータ79%

[ブラウザー制御](</ja-JP/tools/browser-control>), [テスト](</ja-JP/help/testing>), [ブラウザー](</ja-JP/tools/browser>), [インデックス](</ja-JP/gateway/security>), [監査チェック](</ja-JP/gateway/security/audit-checks>)

ツール呼び出しと実行 6個の機能 / LTSサポート対象

アルファ50%

ベータ79%

ベータ79%

[Exec](</ja-JP/tools/exec>), [バックグラウンドプロセス](</ja-JP/gateway/background-process>), [ツール呼び出し HTTP API](</ja-JP/gateway/tools-invoke-http-api>), [オペレータースコープ](</ja-JP/gateway/operator-scopes>), [プロトコル](</ja-JP/gateway/protocol>), [Exec 承認](</ja-JP/tools/exec-approvals>), [高度な Exec 承認](</ja-JP/tools/exec-approvals-advanced>), [昇格](</ja-JP/tools/elevated>)

サンドボックスとツールポリシー 6個の機能 / LTSサポート対象

実験的0%

アルファ68%

ベータ79%

[サンドボックス化](</ja-JP/gateway/sandboxing>), [サンドボックス対ツールポリシー対昇格](</ja-JP/gateway/sandbox-vs-tool-policy-vs-elevated>), [マルチエージェントサンドボックスツール](</ja-JP/tools/multi-agent-sandbox-tools>), [Codex ハーネスリファレンス](</ja-JP/plugins/codex-harness-reference>), [設定ツール](</ja-JP/gateway/config-tools>)

OpenAI と Codex のプロバイダーパス - M3 ベータ - 5領域

詳細なドキュメント、OAuth/サブスクリプションパス、リアルタイム音声、画像、互換性の挙動。プロバイダーの変動があるため、リリーススコアカードの証明なしでは安定版になりません。

カバレッジ 実験的 - 26%品質 ベータ - 74%完成度 ベータ - 79%部分的 - 3

モデルと認証 6 機能 / LTS対応

実験的44%

ベータ79%

ベータ79%

[OpenAI](</ja-JP/providers/openai>), [Codex ハーネス](</ja-JP/plugins/codex-harness>), [モデル](</ja-JP/concepts/models>), [OAuth](</ja-JP/concepts/oauth>), [Codex ハーネスリファレンス](</ja-JP/plugins/codex-harness-reference>), [認証モニタリング](</ja-JP/gateway/authentication>)

レスポンスとツール互換性 4 機能 / LTS対応

実験的40%

ベータ79%

ベータ79%

[OpenAI](</ja-JP/providers/openai>), [OpenResponses HTTP API](</ja-JP/gateway/openresponses-http-api>), [OpenAI HTTP API](</ja-JP/gateway/openai-http-api>), [Codex ネイティブプラグイン](</ja-JP/plugins/codex-native-plugins>)

ネイティブ Codex ハーネス 2 機能 / LTS対応

実験的44%

ベータ79%

ベータ79%

[Codex ハーネス](</ja-JP/plugins/codex-harness>), [Codex ハーネスランタイム](</ja-JP/plugins/codex-harness-runtime>), [Codex ハーネスリファレンス](</ja-JP/plugins/codex-harness-reference>), [Codex ネイティブプラグイン](</ja-JP/plugins/codex-native-plugins>)

画像とマルチモーダル入力 2 機能

実験的0%

アルファ67%

ベータ79%

[OpenAI](</ja-JP/providers/openai>), [画像生成](</ja-JP/tools/image-generation>), [画像](</ja-JP/nodes/images>)

音声とリアルタイム音声 2 機能

実験的0%

アルファ67%

ベータ79%

[OpenAI](</ja-JP/providers/openai>), [Discord](</ja-JP/channels/discord>), [音声通話](</ja-JP/plugins/voice-call>)

Web検索ツール - M3 ベータ - 4 領域

複数のプロバイダーとドキュメントが存在します。プロバイダーファミリーごとにクォータ、エラー、SSRF の証明が必要です。

カバレッジ 実験的 - 9%品質 ベータ - 74%完全性 ベータ - 79%なし

検索プロバイダー 19個の機能

実験的11%

ベータ79%

ベータ79%

[Web](</ja-JP/tools/web>), [Brave Search](</ja-JP/tools/brave-search>), [Tavily](</ja-JP/tools/tavily>), [Exa Search](</ja-JP/tools/exa-search>), [Firecrawl](</ja-JP/tools/firecrawl>), [Perplexity Search](</ja-JP/tools/perplexity-search>), [Duckduckgo Search](</ja-JP/tools/duckduckgo-search>), [Searxng Search](</ja-JP/tools/searxng-search>), [Gemini Search](</ja-JP/tools/gemini-search>), [Grok Search](</ja-JP/tools/grok-search>), [Kimi Search](</ja-JP/tools/kimi-search>), [Minimax Search](</ja-JP/tools/minimax-search>), [Ollama Search](</ja-JP/tools/ollama-search>), [SDK サブパス](</ja-JP/plugins/sdk-subpaths>), [SDK 概要](</ja-JP/plugins/sdk-overview>), [マニフェスト](</ja-JP/plugins/manifest>)

セットアップと診断 9個の機能

実験的0%

アルファ68%

ベータ79%

[Web](</ja-JP/tools/web>), [Web Fetch](</ja-JP/tools/web-fetch>), [FAQ](</ja-JP/help/faq>), [API 使用コスト](</ja-JP/reference/api-usage-costs>), [Brave Search](</ja-JP/tools/brave-search>), [Perplexity Search](</ja-JP/tools/perplexity-search>), [Tavily](</ja-JP/tools/tavily>), [Firecrawl](</ja-JP/tools/firecrawl>)

ネットワーク安全性 4個の機能

実験的0%

アルファ68%

ベータ79%

[Web](</ja-JP/tools/web>), [Web Fetch](</ja-JP/tools/web-fetch>), [Firecrawl](</ja-JP/tools/firecrawl>), [Searxng Search](</ja-JP/tools/searxng-search>)

ツールの可用性と取得 11個の機能

実験的25%

ベータ79%

ベータ79%

[設定ツール](</ja-JP/gateway/config-tools>), [Web Fetch](</ja-JP/tools/web-fetch>), [Web](</ja-JP/tools/web>), [FAQ](</ja-JP/help/faq>)

Anthropic プロバイダーパス - M3 ベータ - 5領域

第一級のモデルプロバイダー。定期的な auth/catalog/tool-call シナリオ証明が必要です。

カバレッジ 実験的 - 0%品質 ベータ - 71%完全性 ベータ - 78%なし

プロバイダー認証と復旧 9 機能

実験的0%

アルファ66%

ベータ78%

[Anthropic](</ja-JP/providers/anthropic>), [Doctor](</ja-JP/gateway/doctor>), [構成例](</ja-JP/gateway/configuration-examples>), [トラブルシューティング](</ja-JP/gateway/troubleshooting>), [プロンプトキャッシュ](</ja-JP/reference/prompt-caching>)

モデルとランタイムの選択 10 機能

実験的0%

ベータ78%

ベータ79%

[Anthropic](</ja-JP/providers/anthropic>), [エージェント設定](</ja-JP/gateway/config-agents>), [モデル](</ja-JP/concepts/models>), [CLI バックエンド](</ja-JP/gateway/cli-backends>)

リクエスト転送とターンセマンティクス 10 機能

実験的0%

ベータ77%

ベータ79%

[Anthropic](</ja-JP/providers/anthropic>), [プロンプトキャッシュ](</ja-JP/reference/prompt-caching>), [トラブルシューティング](</ja-JP/gateway/troubleshooting>), [CLI バックエンド](</ja-JP/gateway/cli-backends>), [モデルプロバイダー](</ja-JP/concepts/model-providers>)

プロンプトキャッシュとコンテキスト 5 機能

実験的0%

アルファ66%

ベータ78%

[Anthropic](</ja-JP/providers/anthropic>), [プロンプトキャッシュ](</ja-JP/reference/prompt-caching>), [トラブルシューティング](</ja-JP/gateway/troubleshooting>), [Heartbeat](</ja-JP/gateway/heartbeat>)

メディア入力 4 機能

実験的0%

アルファ66%

ベータ78%

[Anthropic](</ja-JP/providers/anthropic>), [エージェント設定](</ja-JP/gateway/config-agents>)

Google プロバイダーパス - M3 ベータ - 5 領域

モデルとリアルタイムサーフェスを備えた第一級プロバイダー。Live/Talk の個別スコアリングが必要。

カバレッジ 実験的 - 0%品質 アルファ - 66%完全性 ベータ - 78%なし

プロバイダー設定と認証情報 10 個の機能

実験的0%

アルファ66%

ベータ78%

[Google](</ja-JP/providers/google>), [モデルプロバイダー](</ja-JP/concepts/model-providers>)

モデルルーティングとエンドポイント 10 個の機能

実験的0%

アルファ66%

ベータ78%

[Google](</ja-JP/providers/google>), [モデルプロバイダー](</ja-JP/concepts/model-providers>), [Google](</ja-JP/plugins/reference/google>), [Gemini 検索](</ja-JP/tools/gemini-search>)

直接 Gemini ランタイム 9 個の機能

実験的0%

アルファ66%

ベータ78%

[Google](</ja-JP/providers/google>), [モデルプロバイダー](</ja-JP/concepts/model-providers>), [FAQ モデル](</ja-JP/help/faq-models>), [ライブテスト](</ja-JP/help/testing-live>)

メディア、検索、リアルタイム 10 個の機能

実験的0%

アルファ66%

ベータ78%

[Google](</ja-JP/plugins/reference/google>), [Google](</ja-JP/providers/google>)

プロンプトキャッシュ 5 個の機能

実験的0%

アルファ66%

ベータ78%

[プロンプトキャッシュ](</ja-JP/reference/prompt-caching>), [Google](</ja-JP/providers/google>), [モデルプロバイダー](</ja-JP/concepts/model-providers>), [トークン使用量](</ja-JP/reference/token-use>)

OpenRouter プロバイダーパス - M3 ベータ - 4 領域

統合プロバイダーパスは文書化されており有用ですが、モデル固有の動作はさまざまです。

カバレッジ 実験的 - 0%品質 アルファ - 66%完成度 ベータ - 78%なし

プロバイダーのセットアップと認証 14 個の機能

実験的0%

アルファ66%

ベータ78%

[Openrouter](</ja-JP/providers/openrouter>), [モデルプロバイダー](</ja-JP/concepts/model-providers>), [設定](</ja-JP/cli/configure>), [認証](</ja-JP/gateway/authentication>), [環境](</ja-JP/help/environment>), [モデル](</ja-JP/cli/models>), [モデル](</ja-JP/concepts/models>)

チャットランタイムと正規化 15 個の機能

実験的0%

アルファ66%

ベータ78%

[Openrouter](</ja-JP/providers/openrouter>), [モデルプロバイダー](</ja-JP/concepts/model-providers>), [プロンプトキャッシュ](</ja-JP/reference/prompt-caching>)

プロバイダーの復旧と診断 5 個の機能

実験的0%

アルファ66%

ベータ78%

[モデルフェイルオーバー](</ja-JP/concepts/model-failover>), [Openrouter](</ja-JP/providers/openrouter>), [モデル](</ja-JP/cli/models>)

メディア生成と音声 7 個の機能

実験的0%

アルファ66%

ベータ78%

[Openrouter](</ja-JP/providers/openrouter>), [画像生成](</ja-JP/tools/image-generation>), [音楽生成](</ja-JP/tools/music-generation>), [メディア概要](</ja-JP/tools/media-overview>), [動画生成](</ja-JP/tools/video-generation>), [Tts](</ja-JP/tools/tts>)

画像、動画、音楽生成ツール - M2 アルファ - 5 領域

機能は複数のプロバイダーに存在しますが、品質、レイテンシー、パラメーター互換性はプロバイダーごとの証明なしでベータとするにはばらつきが大きすぎます。

カバレッジ 実験的 - 0%品質 アルファ - 61%完全性 アルファ - 68%なし

メディアルーティングと検出 4機能

試験的0%

アルファ61%

アルファ68%

[設定エージェント](</ja-JP/gateway/config-agents>), [画像生成](</ja-JP/tools/image-generation>), [動画生成](</ja-JP/tools/video-generation>), [音楽生成](</ja-JP/tools/music-generation>)

タスクライフサイクルと配信 12機能

試験的0%

アルファ61%

アルファ68%

[メディア概要](</ja-JP/tools/media-overview>), [画像生成](</ja-JP/tools/image-generation>), [動画生成](</ja-JP/tools/video-generation>), [音楽生成](</ja-JP/tools/music-generation>)

画像生成 9機能

試験的0%

アルファ61%

アルファ68%

[画像生成](</ja-JP/tools/image-generation>), [推論](</ja-JP/cli/infer>), [メディア概要](</ja-JP/tools/media-overview>)

動画生成 11機能

試験的0%

アルファ61%

アルファ68%

[動画生成](</ja-JP/tools/video-generation>), [Runway](</ja-JP/providers/runway>), [Pixverse](</ja-JP/providers/pixverse>), [Fal](</ja-JP/providers/fal>), [Openrouter](</ja-JP/providers/openrouter>)

音楽生成 6機能

試験的0%

アルファ61%

アルファ68%

[音楽生成](</ja-JP/tools/music-generation>)

ローカルモデルプロバイダー: Ollama, vLLM, SGLang, LM Studio - M2 アルファ - 5領域

有用でドキュメント化されていますが、環境によるばらつきが大きいです。

カバレッジ 試験的 - 0%品質 アルファ - 61%完成度 アルファ - 68%なし

プロバイダーのセットアップ、ライフサイクル、診断 12個の機能

実験的0%

アルファ61%

アルファ68%

[ローカルモデル](</ja-JP/gateway/local-models>), [Lmstudio](</ja-JP/providers/lmstudio>), [Ollama](</ja-JP/providers/ollama>), [Vllm](</ja-JP/providers/vllm>), [ローカルモデルサービス](</ja-JP/gateway/local-model-services>), [エージェント設定](</ja-JP/gateway/config-agents>), [トラブルシューティング](</ja-JP/gateway/troubleshooting>), [Doctor](</ja-JP/gateway/doctor>)

ネイティブプロバイダーPlugin 10個の機能

実験的0%

アルファ61%

アルファ68%

[Ollama](</ja-JP/providers/ollama>), [Lmstudio](</ja-JP/providers/lmstudio>)

OpenAI互換ランタイムの互換性 8個の機能

実験的0%

アルファ61%

アルファ68%

[Vllm](</ja-JP/providers/vllm>), [Sglang](</ja-JP/providers/sglang>), [ローカルモデル](</ja-JP/gateway/local-models>), [Lmstudio](</ja-JP/providers/lmstudio>)

ローカルメモリと埋め込み 5個の機能

実験的0%

アルファ61%

アルファ68%

[メモリ](</ja-JP/concepts/memory>), [Doctor](</ja-JP/gateway/doctor>)

ネットワーク安全性とプロンプト制御 2個の機能

実験的0%

アルファ61%

アルファ68%

[インデックス](</ja-JP/gateway/security>), [ツール設定](</ja-JP/gateway/config-tools>), [ローカルモデル](</ja-JP/gateway/local-models>)

ロングテールのホスト型プロバイダー - M2アルファ - 3領域

多くのドキュメント/リファレンスページが存在します。スコアはプロバイダーメタデータとライブスモークカバレッジから生成する必要があります。

カバレッジ 実験的 - 0%品質 アルファ - 61%完全性 アルファ - 68%なし

ホスト型 LLM プロバイダー 12 個の機能

実験的0%

アルファ61%

アルファ68%

[索引](</ja-JP/providers>), [モデルプロバイダー](</ja-JP/concepts/model-providers>), [ライブテスト](</ja-JP/help/testing-live>), [オンボード](</ja-JP/cli/onboard>)

ホスト型メディアプロバイダー 8 個の機能

実験的0%

アルファ61%

アルファ68%

[マニフェスト](</ja-JP/plugins/manifest>), [ライブテスト](</ja-JP/help/testing-live>), [索引](</ja-JP/providers>)

プロバイダー運用 12 個の機能

実験的0%

アルファ61%

アルファ68%

[索引](</ja-JP/providers>), [モデルプロバイダー](</ja-JP/concepts/model-providers>), [マニフェスト](</ja-JP/plugins/manifest>), [ライブテスト](</ja-JP/help/testing-live>), [モデル](</ja-JP/cli/models>)

Was this useful?YesNo

Open issue