---
title: 外部アプリ向けの Gateway 連携
source_url: https://docs.openclaw.ai/ja-JP/gateway/external-apps
scraped_at: 2026-06-29
---

ReferenceRPC and API

外部アプリは、現時点では Gateway プロトコルを通じて OpenClaw と通信する必要があります。スクリプト、ダッシュボード、CI ジョブ、IDE 拡張機能、または別のプロセスが、エージェント実行の開始、イベントのストリーミング、結果の待機、作業のキャンセル、Gateway リソースの調査を行いたい場合は、Gateway WebSocket と RPC メソッドを使用してください。

## 現時点で利用可能なもの

サーフェス | ステータス | 用途  
---|---|---  
[Gateway プロトコル](</ja-JP/gateway/protocol>) | 利用可能 | WebSocket トランスポート、接続ハンドシェイク、認可スコープ、プロトコルのバージョニング、イベント。  
[Gateway RPC リファレンス](</ja-JP/reference/rpc>) | 利用可能 | エージェント、セッション、タスク、モデル、ツール、アーティファクト、承認のための現在の Gateway メソッド。  
[`openclaw agent`](</ja-JP/cli/agent>) | 利用可能 | CLI を呼び出すだけで十分な場合の、単発スクリプト連携。  
[`openclaw message`](</ja-JP/cli/message>) | 利用可能 | スクリプトからのメッセージまたはチャンネルアクションの送信。  
  
ソースツリーには将来のクライアントライブラリ向けの内部パッケージ作業が含まれていますが、 これは公開インストールサーフェスではありません。パッケージが公開され、バージョン管理されるまでは、プレビュー実装の詳細として扱ってください。

## 推奨パス

  1. Gateway を実行するか検出します。
  2. [Gateway プロトコル](</ja-JP/gateway/protocol>)経由で接続します。
  3. [Gateway RPC リファレンス](</ja-JP/reference/rpc>)の文書化された RPC メソッドを呼び出します。
  4. テスト対象の OpenClaw バージョンを固定します。
  5. OpenClaw をアップグレードするときは RPC リファレンスを再確認します。


エージェント実行では、`agent` RPC から始め、終端結果が必要な場合は `agent.wait` と組み合わせてください。永続的な会話状態には、`sessions.*` メソッドを使用します。UI 連携では、Gateway イベントを購読し、アプリが理解するイベントファミリーだけをレンダリングしてください。

## アプリコードと Plugin コード

コードが OpenClaw の外部にある場合は Gateway RPC を使用します。

  * エージェント実行を開始または監視する Node スクリプト
  * Gateway を呼び出す CI ジョブ
  * ダッシュボードと管理パネル
  * IDE 拡張機能
  * チャンネル Plugin になる必要のない外部ブリッジ
  * 偽または実際の Gateway トランスポートを使う連携テスト


コードが OpenClaw の内部で実行される場合は Plugin SDK を使用します。

  * プロバイダー Plugin
  * チャンネル Plugin
  * ツールまたはライフサイクルフック
  * エージェントハーネス Plugin
  * 信頼されたランタイムヘルパー


外部アプリは `openclaw/plugin-sdk/*` をインポートしないでください。これらのサブパスは OpenClaw によって読み込まれる Plugin 向けです。

## 関連

  * [Gateway プロトコル](</ja-JP/gateway/protocol>)
  * [Gateway RPC リファレンス](</ja-JP/reference/rpc>)
  * [CLI agent コマンド](</ja-JP/cli/agent>)
  * [CLI message コマンド](</ja-JP/cli/message>)
  * [エージェントループ](</ja-JP/concepts/agent-loop>)
  * [エージェントランタイム](</ja-JP/concepts/agent-runtimes>)
  * [セッション](</ja-JP/concepts/session>)
  * [バックグラウンドタスク](</ja-JP/automation/tasks>)
  * [ACP エージェント](</ja-JP/tools/acp-agents>)
  * [Plugin SDK 概要](</ja-JP/plugins/sdk-overview>)


Was this useful?YesNo

Open issue