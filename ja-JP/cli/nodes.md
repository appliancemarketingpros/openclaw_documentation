---
title: Node
source_url: https://docs.openclaw.ai/ja-JP/cli/nodes
scraped_at: 2026-05-25
---

# `openclaw nodes`

ペアリング済みノード（デバイス）を管理し、ノード機能を呼び出します。

関連:

  * ノード概要: [ノード](</ja-JP/nodes>)
  * カメラ: [カメラノード](</ja-JP/nodes/camera>)
  * 画像: [画像ノード](</ja-JP/nodes/images>)


共通オプション:

  * `--url`, `--token`, `--timeout`, `--json`


## 共通コマンド

bashCopy code
[code]
    openclaw nodes listopenclaw nodes list --connectedopenclaw nodes list --last-connected 24hopenclaw nodes pendingopenclaw nodes approve <requestId>openclaw nodes reject <requestId>openclaw nodes remove --node <id|name|ip>openclaw nodes rename --node <id|name|ip> --name <displayName>openclaw nodes statusopenclaw nodes status --connectedopenclaw nodes status --last-connected 24h
[/code]

`nodes list` は、保留中/ペアリング済みの表を出力します。ペアリング済みの行には、直近の接続からの経過時間（Last Connect）が含まれます。 現在接続中のノードだけを表示するには `--connected` を使用します。指定した期間内（例: `24h`, `7d`）に接続したノードに 絞り込むには `--last-connected <duration>` を使用します。 古い Gateway 所有のノードペアリングレコードを削除するには、`nodes remove --node <id|name|ip>` を使用します。

承認に関する注記:

  * `openclaw nodes pending` に必要なのはペアリングスコープだけです。
  * `gateway.nodes.pairing.autoApproveCidrs` は、明示的に信頼された初回の `role: node` デバイスペアリングに限り、 保留中ステップをスキップできます。これはデフォルトでオフであり、アップグレードは承認しません。
  * `openclaw nodes approve <requestId>` は、保留中のリクエストから追加のスコープ要件を継承します: 
    * コマンドなしのリクエスト: ペアリングのみ
    * 非 exec ノードコマンド: ペアリング + 書き込み
    * `system.run` / `system.run.prepare` / `system.which`: ペアリング + 管理者


## 呼び出し

bashCopy code
[code]
    openclaw nodes invoke --node <id|name|ip> --command <command> --params <json>
[/code]

呼び出しフラグ:

  * `--params <json>`: JSON オブジェクト文字列（デフォルト `{}`）。
  * `--invoke-timeout <ms>`: ノード呼び出しタイムアウト（デフォルト `15000`）。
  * `--idempotency-key <key>`: 任意の冪等性キー。
  * `system.run` と `system.run.prepare` はここではブロックされます。シェル実行には `host=node` 付きの `exec` ツールを使用してください。


ノード上でシェルを実行するには、`openclaw nodes run` ではなく `host=node` 付きの `exec` ツールを使用します。 `nodes` CLI は現在、機能を中心にしています。`nodes invoke` による直接 RPC に加え、ペアリング、カメラ、 画面、位置情報、Canvas、通知を扱います。Canvas コマンドは同梱の実験的な Canvas Plugin によって実装されます。core は互換性フックを保持しているため、これらは引き続き `openclaw nodes canvas` 配下に残ります。

## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [ノード](</ja-JP/nodes>)


Was this useful?YesNo