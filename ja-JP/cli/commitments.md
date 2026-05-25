---
title: `openclaw commitments`
source_url: https://docs.openclaw.ai/ja-JP/cli/commitments
scraped_at: 2026-05-25
---

推論されたフォローアップのコミットメントを一覧表示し、管理します。

コミットメントは、会話コンテキストから作成される、オプトインで短期間だけ保持されるフォローアップメモリーです。 概念ガイドについては、[推論されたコミットメント](</ja-JP/concepts/commitments>)を参照してください。

サブコマンドなしの場合、`openclaw commitments` は保留中のコミットメントを一覧表示します。

## 使用法

bashCopy code
[code]
    openclaw commitments [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments list [--all] [--agent <id>] [--status <status>] [--json]openclaw commitments dismiss <id...> [--json]
[/code]

## オプション

  * `--all`: 保留中のコミットメントだけでなく、すべてのステータスを表示します。
  * `--agent <id>`: 1つのエージェント id に絞り込みます。
  * `--status <status>`: ステータスで絞り込みます。値: `pending`、`sent`、 `dismissed`、`snoozed`、または `expired`。
  * `--json`: 機械可読な JSON を出力します。


## 例

保留中のコミットメントを一覧表示します。

bashCopy code
[code]
    openclaw commitments
[/code]

保存済みのすべてのコミットメントを一覧表示します。

bashCopy code
[code]
    openclaw commitments --all
[/code]

1つのエージェントに絞り込みます。

bashCopy code
[code]
    openclaw commitments --agent main
[/code]

スヌーズ中のコミットメントを探します。

bashCopy code
[code]
    openclaw commitments --status snoozed
[/code]

1つ以上のコミットメントを却下します。

bashCopy code
[code]
    openclaw commitments dismiss cm_abc123 cm_def456
[/code]

JSON としてエクスポートします。

bashCopy code
[code]
    openclaw commitments --all --json
[/code]

## 出力

テキスト出力には次が含まれます。

  * コミットメント id
  * ステータス
  * 種類
  * 最も早い期限時刻
  * スコープ
  * 推奨される確認テキスト


JSON 出力には、コミットメントストアのパスと、保存済みレコード全体も含まれます。

## 関連

  * [推論されたコミットメント](</ja-JP/concepts/commitments>)
  * [メモリーの概要](</ja-JP/concepts/memory>)
  * [Heartbeat](</ja-JP/gateway/heartbeat>)
  * [スケジュール済みタスク](</ja-JP/automation/cron-jobs>)


Was this useful?YesNo