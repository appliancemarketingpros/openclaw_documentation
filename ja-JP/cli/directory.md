---
title: ディレクトリ
source_url: https://docs.openclaw.ai/ja-JP/cli/directory
scraped_at: 2026-05-25
---

# `openclaw directory`

対応しているチャネル向けのディレクトリ検索（連絡先/ピア、グループ、および "me"）。

## 共通フラグ

  * `--channel <name>`: チャネル ID/エイリアス（複数のチャネルが設定されている場合は必須。1 つだけ設定されている場合は自動）
  * `--account <id>`: アカウント ID（デフォルト: チャネルのデフォルト）
  * `--json`: JSON を出力


## 注記

  * `directory` は、他のコマンド（特に `openclaw message send --target ...`）に貼り付けられる ID を見つけるためのものです。
  * 多くのチャネルでは、結果はライブのプロバイダーディレクトリではなく、設定ベース（許可リスト / 設定済みグループ）です。
  * インストール済みのチャネルプラグインでもディレクトリ対応を省略できます。その場合、コマンドはプラグインを再インストールするのではなく、未対応のディレクトリ操作を報告します。
  * デフォルト出力は、タブで区切られた `id`（場合によっては `name` も）です。スクリプト用途には `--json` を使用してください。


## `message send` で結果を使用する

bashCopy code
[code]
    openclaw directory peers list --channel slack --query "U0"openclaw message send --channel slack --target user:U012ABCDEF --message "hello"
[/code]

## ID 形式（チャネル別）

  * WhatsApp: `+15551234567`（DM）、`1234567890-1234567890@g.us`（グループ）、`120363123456789@newsletter`（チャネル/ニュースレターの送信先ターゲット）
  * Telegram: `@username` または数値チャット ID。グループは数値 ID
  * Slack: `user:U…` と `channel:C…`
  * Discord: `user:<id>` と `channel:<id>`
  * Matrix（Plugin）: `user:@user:server`、`room:!roomId:server`、または `#alias:server`
  * Microsoft Teams（Plugin）: `user:<id>` と `conversation:<id>`
  * Zalo（Plugin）: ユーザー ID（Bot API）
  * Zalo Personal / `zalouser`（Plugin）: `zca` からのスレッド ID（DM/グループ）（`me`、`friend list`、`group list`）


## 自分（"me"）

bashCopy code
[code]
    openclaw directory self --channel zalouser
[/code]

## ピア（連絡先/ユーザー）

bashCopy code
[code]
    openclaw directory peers list --channel zalouseropenclaw directory peers list --channel zalouser --query "name"openclaw directory peers list --channel zalouser --limit 50
[/code]

## グループ

bashCopy code
[code]
    openclaw directory groups list --channel zalouseropenclaw directory groups list --channel zalouser --query "work"openclaw directory groups members --channel zalouser --group-id <id>
[/code]

## 関連

  * [CLI リファレンス](</ja-JP/cli>)


Was this useful?YesNo