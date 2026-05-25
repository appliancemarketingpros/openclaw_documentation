---
title: ログ
source_url: https://docs.openclaw.ai/ja-JP/cli/logs
scraped_at: 2026-05-25
---

# `openclaw logs`

Gateway のファイルログを RPC 経由で追尾表示します（リモートモードで動作します）。

関連:

  * ログ記録の概要: [ログ記録](</ja-JP/logging>)
  * Gateway CLI: [gateway](</ja-JP/cli/gateway>)


## オプション

  * `--limit <n>`: 返すログ行の最大数（デフォルトは `200`）
  * `--max-bytes <n>`: ログファイルから読み取る最大バイト数（デフォルトは `250000`）
  * `--follow`: ログストリームを追尾する
  * `--interval <ms>`: 追尾中のポーリング間隔（デフォルトは `1000`）
  * `--json`: 行区切りの JSON イベントを出力する
  * `--plain`: スタイル付き書式なしのプレーンテキスト出力
  * `--no-color`: ANSI カラーを無効化する
  * `--local-time`: タイムスタンプをローカルタイムゾーンで表示する


## 共有 Gateway RPC オプション

`openclaw logs` は標準の Gateway クライアントフラグも受け付けます:

  * `--url <url>`: Gateway WebSocket URL
  * `--token <token>`: Gateway トークン
  * `--timeout <ms>`: ms 単位のタイムアウト（デフォルトは `30000`）
  * `--expect-final`: Gateway 呼び出しがエージェントによって処理される場合、最終応答を待機する


`--url` を渡すと、CLI は設定や環境認証情報を自動適用しません。対象の Gateway で認証が必要な場合は、`--token` を明示的に含めてください。

## 例

bashCopy code
[code]
    openclaw logsopenclaw logs --followopenclaw logs --follow --interval 2000openclaw logs --limit 500 --max-bytes 500000openclaw logs --jsonopenclaw logs --plainopenclaw logs --no-coloropenclaw logs --limit 500openclaw logs --local-timeopenclaw logs --follow --local-timeopenclaw logs --url ws://127.0.0.1:18789 --token "$OPENCLAW_GATEWAY_TOKEN"
[/code]

## 注記

  * `--local-time` を使用すると、タイムスタンプをローカルタイムゾーンで表示できます。
  * 暗黙の local loopback Gateway がペアリングを要求した場合、接続中に閉じた場合、または `logs.tail` が応答する前にタイムアウトした場合、`openclaw logs` は設定済みの Gateway ファイルログに自動的にフォールバックします。明示的な `--url` ターゲットでは、このフォールバックは使用されません。
  * `--follow` を使用している場合、一時的な gateway 切断（WebSocket クローズ、タイムアウト、接続切断）は指数バックオフによる自動再接続をトリガーします（最大 8 回の再試行、試行間隔は最大 30 秒）。各再試行時に警告が stderr に出力され、ポーリングが成功すると `[logs] gateway reconnected` 通知が一度出力されます。`--json` モードでは、再試行警告と再接続遷移の両方が stderr に `{"type":"notice"}` レコードとして出力されます。回復不能なエラー（認証失敗、不正な設定）は引き続き即座に終了します。


## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [Gateway ログ記録](</ja-JP/gateway/logging>)


Was this useful?YesNo