---
title: CLI をアタッチする
source_url: https://docs.openclaw.ai/ja-JP/cli/attach
scraped_at: 2026-07-06
---

ReferenceCLI commands

`openclaw attach` は、1つの Gateway セッションにバインドされた厳格な一時 MCP 設定で Claude Code を起動します。

shCopy code
[code]
    openclaw attachopenclaw attach --session agent:main:telegram:123 --ttl 600000openclaw attach --print-config
[/code]

オプション:

  * `--session <key>` は付与を Gateway セッションにバインドします。デフォルトはメインセッションです。
  * `--ttl <ms>` は正の付与 TTL をミリ秒単位で要求します。Gateway は独自の上限を適用します。
  * `--bin <path>` は Claude Code バイナリを選択します。デフォルト: `claude`。
  * `--print-config` は一時 `.mcp.json` を書き込み、起動コマンドと環境変数を出力し、TTL の期限切れまで付与を有効なままにします（Claude Code を起動せず、付与も取り消しません）。


ベアラートークンは argv ではなく環境変数経由で渡されます。OpenClaw は `--strict-mcp-config --mcp-config <path>` 付きで Claude Code を起動するため、周囲の Claude MCP サーバーはアタッチされたセッションに参加しません。通常の起動（`--print-config` なし）では、Claude Code プロセスが終了すると付与が取り消されます。

関連項目: [Gateway CLI](</ja-JP/cli/gateway>)、[MCP CLI](</ja-JP/cli/mcp>)、[ACP CLI](</ja-JP/cli/acp>)。

Was this useful?YesNo

Open issue