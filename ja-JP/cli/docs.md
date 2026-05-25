---
title: ドキュメント
source_url: https://docs.openclaw.ai/ja-JP/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

ターミナルからライブの OpenClaw ドキュメントインデックスを検索します。このコマンドは、`https://docs.openclaw.ai/mcp.SearchOpenClaw` にある公開の Mintlify ホストの docs MCP 検索エンドポイントをシェル経由で呼び出し、結果をターミナルに表示します。

## 使い方

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

引数:

引数 | 説明  
---|---  
`[query...]` | 自由形式の検索クエリ。複数語のクエリはスペースで結合され、1つとして送信されます。  
  
## 例

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

クエリがない場合、`openclaw docs` は検索を実行する代わりに、ドキュメントのエントリポイント URL とサンプル検索コマンドを表示します。

## 仕組み

`openclaw docs` は `mcporter` CLI を呼び出して docs 検索 MCP ツールを実行し、その後ツール出力の `Title: / Link: / Content:` ブロックを解析して結果リストにします。

`mcporter` を解決するために、OpenClaw は次の順序で確認します。

  1. `PATH` 上の `mcporter` (存在する場合は直接使用)。
  2. `pnpm` がインストールされている場合は `pnpm dlx mcporter ...`。
  3. `npx` がインストールされている場合は `npx -y mcporter ...`。


いずれも利用できない場合、コマンドは `pnpm` (`npm install -g pnpm`) のインストールを促すヒントとともに失敗します。

検索呼び出しには固定の30秒タイムアウトが使用されます。結果スニペットは各項目あたり約220文字に切り詰められます。

## 出力

リッチな (TTY) ターミナルでは、結果は見出しに続く箇条書きリストとして表示されます。各箇条書きにはページタイトル、リンクされた docs URL、次の行に短いスニペットが表示されます。空の結果では "No results." と表示されます。

非リッチ出力 (パイプ、`--no-color`、スクリプト) では、同じデータが Markdown として表示されます。

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## 終了コード

コード | 意味  
---|---  
`0` | 検索に成功しました (結果が0件の応答を含む)。  
`1` | MCP ツール呼び出しに失敗しました。stderr はインラインで出力されます。  
  
## 関連

  * [CLI リファレンス](</ja-JP/cli>)
  * [ライブドキュメント](<https://docs.openclaw.ai>)


Was this useful?YesNo