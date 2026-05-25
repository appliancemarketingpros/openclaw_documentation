---
title: 音声通話
source_url: https://docs.openclaw.ai/ja-JP/cli/voicecall
scraped_at: 2026-05-25
---

# `openclaw voicecall`

`voicecall` は Plugin が提供するコマンドです。音声通話Plugin がインストールされ、有効になっている場合にのみ表示されます。

Gateway が実行中の場合、運用コマンド（`call`、`start`、`continue`、`speak`、`dtmf`、`end`、`status`）は、その Gateway の音声通話ランタイムにルーティングされます。到達可能な Gateway がない場合は、スタンドアロン CLI ランタイムにフォールバックします。

## サブコマンド

bashCopy code
[code]
    openclaw voicecall setup    [--json]openclaw voicecall smoke    [-t <phone>] [--message <text>] [--mode <m>] [--yes] [--json]openclaw voicecall call     -m <text> [-t <phone>] [--mode <m>]openclaw voicecall start    --to <phone> [--message <text>] [--mode <m>]openclaw voicecall continue --call-id <id> --message <text>openclaw voicecall speak    --call-id <id> --message <text>openclaw voicecall dtmf     --call-id <id> --digits <digits>openclaw voicecall end      --call-id <id>openclaw voicecall status   [--call-id <id>] [--json]openclaw voicecall tail     [--file <path>] [--since <n>] [--poll <ms>]openclaw voicecall latency  [--file <path>] [--last <n>]openclaw voicecall expose   [--mode <m>] [--path <p>] [--port <port>] [--serve-path <p>]
[/code]

サブコマンド | 説明  
---|---  
`setup` | プロバイダーと Webhook の準備状況チェックを表示します。  
`smoke` | 準備状況チェックを実行します。`--yes` が指定された場合にのみライブテスト通話を発信します。  
`call` | アウトバウンド音声通話を開始します。  
`start` | `call` のエイリアスです。`--to` は必須で、`--message` は任意です。  
`continue` | メッセージを読み上げ、次の応答を待ちます。  
`speak` | 応答を待たずにメッセージを読み上げます。  
`dtmf` | アクティブな通話に DTMF 桁を送信します。  
`end` | アクティブな通話を切断します。  
`status` | アクティブな通話を確認します（または `--call-id` で 1 件を確認します）。  
`tail` | `calls.jsonl` を追尾します（プロバイダーテスト中に便利です）。  
`latency` | `calls.jsonl` からターンレイテンシ指標を要約します。  
`expose` | Webhook エンドポイント用の Tailscale serve/funnel を切り替えます。  
  
## セットアップとスモーク

### `setup`

デフォルトでは人間が読める形式の準備状況チェックを出力します。スクリプト用には `--json` を渡します。

bashCopy code
[code]
    openclaw voicecall setupopenclaw voicecall setup --json
[/code]

### `smoke`

同じ準備状況チェックを実行します。`--to` と `--yes` の両方が指定されていない限り、実際の電話は発信しません。

フラグ | デフォルト | 説明  
---|---|---  
`-t, --to <phone>` | （なし） | ライブスモーク用に発信する電話番号。  
`--message <text>` | `OpenClaw voice call smoke test.` | スモーク通話中に読み上げるメッセージ。  
`--mode <mode>` | `notify` | 通話モード: `notify` または `conversation`。  
`--yes` | `false` | 実際にライブアウトバウンド通話を発信します。  
`--json` | `false` | 機械可読な JSON を出力します。  
bashCopy code
[code]
    openclaw voicecall smokeopenclaw voicecall smoke --to "+15555550123"        # dry runopenclaw voicecall smoke --to "+15555550123" --yes  # live notify call
[/code]

## 通話ライフサイクル

### `call`

アウトバウンド音声通話を開始します。

フラグ | 必須 | デフォルト | 説明  
---|---|---|---  
`-m, --message <text>` | はい | （なし） | 通話が接続されたときに読み上げるメッセージ。  
`-t, --to <phone>` | いいえ | config `toNumber` | 発信先の E.164 電話番号。  
`--mode <mode>` | いいえ | `conversation` | 通話モード: `notify`（メッセージ後に切断）または `conversation`（接続を維持）。  
bashCopy code
[code]
    openclaw voicecall call --to "+15555550123" --message "Hello"openclaw voicecall call -m "Heads up" --mode notify
[/code]

### `start`

異なるデフォルトのフラグ構成を持つ `call` のエイリアスです。

フラグ | 必須 | デフォルト | 説明  
---|---|---|---  
`--to <phone>` | はい | （なし） | 発信先の電話番号。  
`--message <text>` | いいえ | （なし） | 通話が接続されたときに読み上げるメッセージ。  
`--mode <mode>` | いいえ | `conversation` | 通話モード: `notify` または `conversation`。  
  
### `continue`

メッセージを読み上げ、応答を待ちます。

フラグ | 必須 | 説明  
---|---|---  
`--call-id <id>` | はい | 通話 ID。  
`--message <text>` | はい | 読み上げるメッセージ。  
  
### `speak`

応答を待たずにメッセージを読み上げます。

フラグ | 必須 | 説明  
---|---|---  
`--call-id <id>` | はい | 通話 ID。  
`--message <text>` | はい | 読み上げるメッセージ。  
  
### `dtmf`

アクティブな通話に DTMF 桁を送信します。

フラグ | 必須 | 説明  
---|---|---  
`--call-id <id>` | はい | 通話 ID。  
`--digits <digits>` | はい | DTMF 桁（例: 待機を含める場合は `ww123456#`）。  
  
### `end`

アクティブな通話を切断します。

フラグ | 必須 | 説明  
---|---|---  
`--call-id <id>` | はい | 通話 ID。  
  
### `status`

アクティブな通話を確認します。

フラグ | デフォルト | 説明  
---|---|---  
`--call-id <id>` | （なし） | 出力を 1 件の通話に制限します。  
`--json` | `false` | 機械可読な JSON を出力します。  
bashCopy code
[code]
    openclaw voicecall statusopenclaw voicecall status --jsonopenclaw voicecall status --call-id <id>
[/code]

## ログとメトリクス

### `tail`

音声通話 JSONL ログを追尾します。開始時に最後の `--since` 行を出力し、その後、書き込まれる新しい行をストリーミングします。

フラグ | デフォルト | 説明  
---|---|---  
`--file <path>` | Plugin ストアから解決 | `calls.jsonl` へのパス。  
`--since <n>` | `25` | 追尾前に出力する行数。  
`--poll <ms>` | `250`（最小 50） | ポーリング間隔（ミリ秒）。  
  
### `latency`

`calls.jsonl` からターンレイテンシとリッスン待機のメトリクスを要約します。出力は `recordsScanned`、`turnLatency`、`listenWait` の要約を含む JSON です。

フラグ | デフォルト | 説明  
---|---|---  
`--file <path>` | Plugin ストアから解決 | `calls.jsonl` へのパス。  
`--last <n>` | `200`（最小 1） | 分析する最近のレコード数。  
  
## Webhook の公開

### `expose`

音声 Webhook 用の Tailscale serve/funnel 設定を有効化、無効化、または変更します。

フラグ | デフォルト | 説明  
---|---|---  
`--mode <mode>` | `funnel` | `off`、`serve`（tailnet）、または `funnel`（パブリック）。  
`--path <path>` | config `tailscale.path` または `--serve-path` | 公開する Tailscale パス。  
`--port <port>` | config `serve.port` または `3334` | ローカル Webhook ポート。  
`--serve-path <path>` | config `serve.path` または `/voice/webhook` | ローカル Webhook パス。  
bashCopy code
[code]
    openclaw voicecall expose --mode serveopenclaw voicecall expose --mode funnelopenclaw voicecall expose --mode off
[/code]

## 関連項目

  * [CLI リファレンス](</ja-JP/cli>)
  * [音声通話Plugin](</ja-JP/plugins/voice-call>)


Was this useful?YesNo