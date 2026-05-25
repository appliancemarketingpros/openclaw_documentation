---
title: Bun (実験的)
source_url: https://docs.openclaw.ai/ja-JP/install/bun
scraped_at: 2026-05-25
---

Bun は、TypeScript を直接実行するための任意のローカルランタイムです（`bun run ...`、`bun --watch ...`）。デフォルトのパッケージマネージャーは引き続き `pnpm` であり、完全にサポートされ、ドキュメントツールで使用されています。Bun は `pnpm-lock.yaml` を使用できず、無視します。

## インストール

* ### 依存関係をインストール

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` は gitignore の対象なので、リポジトリに差分は発生しません。lockfile の書き込みを完全にスキップするには:

shCopy code
[code]
    bun install --no-save
[/code]

* ### ビルドとテスト

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## ライフサイクルスクリプト

Bun は、明示的に信頼されていない限り、依存関係のライフサイクルスクリプトをブロックします。このリポジトリでは、一般的にブロックされる次のスクリプトは不要です:

  * `baileys` `preinstall` \-- Node のメジャーバージョンが 20 以上か確認します（OpenClaw はデフォルトで Node 24 を使用し、現在 `22.16+` の Node 22 LTS も引き続きサポートしています）
  * `protobufjs` `postinstall` \-- 互換性のないバージョンスキームに関する警告を出力します（ビルド成果物はありません）


これらのスクリプトが必要なランタイム問題に遭遇した場合は、明示的に信頼してください:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## 注意点

一部のスクリプトはまだ pnpm をハードコードしています（例: `docs:build`、`ui:*`、`protocol:check`）。現時点では、それらは pnpm 経由で実行してください。

## 関連

  * [インストール概要](</ja-JP/install>)
  * [Node.js](</ja-JP/install/node>)
  * [更新](</ja-JP/install/updating>)


Was this useful?YesNo