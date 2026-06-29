---
title: トランスクリプト CLI
source_url: https://docs.openclaw.ai/ja-JP/cli/transcripts
scraped_at: 2026-06-29
---

Get started

# `openclaw transcripts`

OpenClaw のコア `transcripts` ツールによって書き込まれたトランスクリプトを調べます。この CLI は読み取り専用です。キャプチャ、インポート、要約はエージェントツールと、設定済みの自動開始ソースが所有します。

昨日のメモを探す、Markdown ファイルをエディタで開く、トランスクリプトを別のツールに渡す、またはセッションがディスク上のどこに保存されたかをデバッグする場合に、この CLI を使用します。キャプチャの開始や停止は行いません。

成果物は OpenClaw の状態ディレクトリ配下に保存されます。

textCopy code
[code]
    $OPENCLAW_STATE_DIR/transcripts/YYYY-MM-DD/<session>/  metadata.json  transcript.jsonl  summary.json  summary.md
[/code]

デフォルトの状態ディレクトリは `~/.openclaw` です。別のディレクトリを使用するには `OPENCLAW_STATE_DIR` を設定します。日付ディレクトリはセッション開始時刻から決まり、セッションディレクトリはセッション ID から派生した安全なファイルシステムセグメントです。

## コマンド

bashCopy code
[code]
    openclaw transcripts listopenclaw transcripts show <session>openclaw transcripts show YYYY-MM-DD/<session>openclaw transcripts path <session>openclaw transcripts path YYYY-MM-DD/<session>openclaw transcripts path <session> --diropenclaw transcripts path <session> --metadataopenclaw transcripts path <session> --transcriptopenclaw transcripts list --jsonopenclaw transcripts show <session> --jsonopenclaw transcripts path <session> --json
[/code]

  * `list`: 保存されたセッション、日付付きセレクタ、開始時刻、タイトル、`summary.md` パスを一覧表示します。
  * `show <session>`: 保存された `summary.md` を出力します。
  * `path <session>`: `summary.md` パスを出力します。
  * `path <session> --dir`: セッションディレクトリを出力します。
  * `path <session> --metadata`: `metadata.json` を出力します。
  * `path <session> --transcript`: `transcript.jsonl` を出力します。
  * `--json`: 機械可読な出力を表示します。


人間が指定したセッション ID が複数の日にまたがって繰り返される場合は、`list` の日付付きセレクタを使用します。例: `openclaw transcripts show 2026-05-22/standup`。デフォルトのセッション ID にはタイムスタンプとランダムなサフィックスが含まれます。固定セッション ID は、その日の中で一意である場合にのみ設定してください。

## 出力

`list` は 1 行に 1 セッションを出力します。

textCopy code
[code]
    2026-05-22/standup  2026-05-22T09:00:00.000Z  Weekly standup  /Users/alex/.openclaw/transcripts/2026-05-22/standup/summary.md
[/code]

出力はタブ区切りです。列はセレクタ、開始時刻、タイトル、要約パスです。セレクタは、`show` または `path` に渡し直す最も安全な値です。

`list --json` は次を含むオブジェクトを出力します。

  * `sessionId`
  * `selector`
  * `date`
  * `title`
  * `startedAt`
  * `stoppedAt`
  * `source`
  * `path`
  * `summaryPath`
  * `hasSummary`


`show --json` は、保存されたセッションメタデータ、セレクタ、セッションディレクトリ、要約パス、要約の Markdown テキストを返します。`path --json` は、選択されたパスとそのファイルが存在するかどうかを返します。

## 1日に多数のミーティング

Transcripts はセッションを日付ごとにグループ化し、その下でセッション ID ごとにグループ化します。1 日に 10 件のミーティングがある場合、10 個の兄弟フォルダになります。

textCopy code
[code]
    ~/.openclaw/transcripts/2026-05-22/  transcript-2026-05-22T09-00-00-000Z-a1b2c3d4/  transcript-2026-05-22T10-30-00-000Z-b2c3d4e5/  standup/
[/code]

ほとんどの自動化では、デフォルトで生成される ID を使用してください。`standup` のような固定 ID は、同じ日付に同じ ID が 2 回使われない場合にのみ使用します。

## 欠落した要約

ライブセッションは、セッションが停止したときに `summary.md` を書き込みます。インポートされたトランスクリプトは、インポート直後に `summary.md` を書き込みます。キャプチャがアクティブな場合、停止中にプロバイダが失敗した場合、または発話が到着する前にメタデータが書き込まれた場合、セッションは要約なしで `list` に表示されることがあります。

追加専用のトランスクリプトを調べるには `path <session> --transcript` を使用し、Markdown 要約を再生成するには `transcripts` ツールアクション `summarize` を使用します。

## 設定

ライブソースがミーティング音声に参加して録音できるため、トランスクリプトキャプチャはオプトインです。トップレベルの `transcripts.enabled` でツールを有効にします。

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "maxUtterances": 2000  }}
[/code]

`openclaw.json` の `transcripts.autoStart` で自動開始ソースを設定します。各エントリは存在することで有効になります。そのソースを無効にするには、エントリを省略します。

jsonCopy code
[code]
    {  "transcripts": {    "enabled": true,    "autoStart": [      {        "providerId": "discord-voice",        "guildId": "1234567890",        "channelId": "2345678901"      },      {        "providerId": "slack-huddle",        "accountId": "workspace",        "channelId": "C123"      }    ]  }}
[/code]

Was this useful?YesNo

Open issue