---
title: Tokenjuice
source_url: https://docs.openclaw.ai/ja-JP/tools/tokenjuice
scraped_at: 2026-05-25
---

`tokenjuice` は、コマンド実行後にノイズの多い `exec` および `bash` ツール結果をコンパクト化する、オプションのバンドル済み Plugin です。

変更するのは返される `tool_result` であり、コマンド自体ではありません。Tokenjuice は シェル入力を書き換えたり、コマンドを再実行したり、終了コードを変更したりしません。

現在これは、PI 埋め込み実行と、Codex app-server ハーネス内の OpenClaw 動的ツールに適用されます。Tokenjuice は OpenClaw の tool-result ミドルウェアにフックし、アクティブなハーネスセッションに戻る前に 出力をトリムします。

## Plugin を有効化する

最短手順:

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled true
[/code]

同等:

bashCopy code
[code]
    openclaw plugins enable tokenjuice
[/code]

OpenClaw にはすでにこの Plugin が同梱されています。別途 `plugins install` や `tokenjuice install openclaw` の手順はありません。

config を直接編集したい場合:

json5Copy code
[code]
    {  plugins: {    entries: {      tokenjuice: {        enabled: true,      },    },  },}
[/code]

## tokenjuice が変更する内容

  * ノイズの多い `exec` および `bash` の結果を、セッションに戻される前にコンパクト化します。
  * 元のコマンド実行には手を加えません。
  * 正確なファイル内容の読み取りや、tokenjuice が生のまま残すべきその他のコマンドは保持します。
  * オプトインのままです。どこでも逐語的な出力がほしい場合は Plugin を無効にしてください。


## 動作確認

  1. Plugin を有効化します。
  2. `exec` を呼び出せるセッションを開始します。
  3. `git status` のようなノイズの多いコマンドを実行します。
  4. 返されたツール結果が、生のシェル出力より短く、より構造化されていることを確認します。


## Plugin を無効化する

bashCopy code
[code]
    openclaw config set plugins.entries.tokenjuice.enabled false
[/code]

または:

bashCopy code
[code]
    openclaw plugins disable tokenjuice
[/code]

## 関連

  * [Exec tool](</ja-JP/tools/exec>)
  * [Thinking levels](</ja-JP/tools/thinking>)
  * [Context engine](</ja-JP/concepts/context-engine>)


Was this useful?YesNo