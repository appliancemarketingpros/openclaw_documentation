---
title: フロー（リダイレクト）
source_url: https://docs.openclaw.ai/ja-JP/cli/flows
scraped_at: 2026-05-25
---

# `openclaw tasks flow`

トップレベルの `openclaw flows` コマンドはありません。永続的な TaskFlow の検査は `openclaw tasks flow` 配下にあります。

## サブコマンド

bashCopy code
[code]
    openclaw tasks flow list   [--json] [--status <name>]openclaw tasks flow show   <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

サブコマンド | 説明 | 引数 / オプション  
---|---|---  
`list` | 追跡中の TaskFlow を一覧表示します。 | `--json` 機械可読出力。`--status <name>` フィルター（下記のステータス値を参照）。  
`show` | 1 つの TaskFlow を表示します。 | `<lookup>` フロー ID またはオーナーキー。`--json` 機械可読出力。  
`cancel` | 実行中の TaskFlow をキャンセルします。 | `<lookup>` フロー ID またはオーナーキー。  
  
`<lookup>` には、フロー ID（`list` / `show` によって返されるもの）またはフローのオーナーキー（所有するサブシステムがフローを追跡するために使用する安定した識別子）のいずれかを指定できます。

### ステータスフィルター値

`list` の `--status` には、次のいずれかを指定できます。

`queued`, `running`, `waiting`, `blocked`, `succeeded`, `failed`, `cancelled`, `lost`

## 例

bashCopy code
[code]
    openclaw tasks flow listopenclaw tasks flow list --status runningopenclaw tasks flow list --jsonopenclaw tasks flow show flow_abc123openclaw tasks flow show flow_abc123 --jsonopenclaw tasks flow cancel flow_abc123
[/code]

TaskFlow の完全な概念と作成については [TaskFlow](</ja-JP/automation/taskflow>) を参照してください。親の `tasks` コマンドについては [tasks CLI リファレンス](</ja-JP/cli/tasks>) を参照してください。

## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [自動化](</ja-JP/automation>)
  * [TaskFlow](</ja-JP/automation/taskflow>)


Was this useful?YesNo