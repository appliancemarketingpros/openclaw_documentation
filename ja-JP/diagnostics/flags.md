---
title: 診断フラグ
source_url: https://docs.openclaw.ai/ja-JP/diagnostics/flags
scraped_at: 2026-05-25
---

診断フラグを使うと、全体の詳細ログを有効にせずに、対象を絞ったデバッグログを有効化できます。フラグはオプトインであり、サブシステムがそれをチェックしない限り効果はありません。

## 仕組み

  * フラグは文字列です (大文字と小文字は区別されません)。
  * フラグは config または env override で有効化できます。
  * ワイルドカードがサポートされています: 
    * `telegram.*` は `telegram.http` にマッチします
    * `*` はすべてのフラグを有効化します


## config で有効化する

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http"]  }}
[/code]

複数のフラグ:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["telegram.http", "brave.http", "gateway.*"]  }}
[/code]

フラグを変更した後は Gateway を再起動してください。

## Env override (一回限り)

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=telegram.http,telegram.payload
[/code]

すべてのフラグを無効化します:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=0
[/code]

## タイムラインアーティファクト

`timeline` フラグは、外部 QA ハーネス向けに構造化された起動時および実行時のタイミングイベントを書き込みます:

bashCopy code
[code]
    OPENCLAW_DIAGNOSTICS=timeline \OPENCLAW_DIAGNOSTICS_TIMELINE_PATH=/tmp/openclaw-timeline.jsonl \openclaw gateway run
[/code]

config で有効化することもできます:

jsonCopy code
[code]
    {  "diagnostics": {    "flags": ["timeline"]  }}
[/code]

タイムラインファイルのパスは引き続き `OPENCLAW_DIAGNOSTICS_TIMELINE_PATH` から取得されます。`timeline` が config からのみ有効化されている場合、OpenClaw はまだ config を読み込んでいないため、最初期の config 読み込みスパンは出力されません。その後の起動スパンでは config フラグが使われます。

`OPENCLAW_DIAGNOSTICS=1`、`OPENCLAW_DIAGNOSTICS=all`、および `OPENCLAW_DIAGNOSTICS=*` も、すべての診断フラグを有効化するため、タイムラインを有効化します。JSONL タイミングアーティファクトだけが必要な場合は `timeline` を優先してください。

タイムラインレコードは `openclaw.diagnostics.v1` エンベロープを使用します。イベントには、プロセス ID、フェーズ名、スパン名、所要時間、plugin ID、依存関係数、イベントループ遅延サンプル、プロバイダー操作名、子プロセスの終了状態、起動エラーの名前/メッセージを含めることができます。タイムラインファイルはローカル診断アーティファクトとして扱い、マシンの外部で共有する前に確認してください。

## ログの出力先

フラグは標準の診断ログファイルにログを出力します。デフォルトでは次の場所です:

CodeCopy code
[code]
    /tmp/openclaw/openclaw-YYYY-MM-DD.log
[/code]

`logging.file` を設定した場合は、代わりにそのパスを使用してください。ログは JSONL (1 行につき 1 つの JSON オブジェクト) です。`logging.redactSensitive` に基づくリダクションは引き続き適用されます。

## ログを抽出する

最新のログファイルを選びます:

bashCopy code
[code]
    ls -t /tmp/openclaw/openclaw-*.log | head -n 1
[/code]

Telegram HTTP 診断でフィルターします:

bashCopy code
[code]
    rg "telegram http error" /tmp/openclaw/openclaw-*.log
[/code]

Brave Search HTTP 診断でフィルターします:

bashCopy code
[code]
    rg "brave http" /tmp/openclaw/openclaw-*.log
[/code]

または、再現しながら tail します:

bashCopy code
[code]
    tail -f /tmp/openclaw/openclaw-$(date +%F).log | rg "telegram http error"
[/code]

リモート Gateway の場合は、`openclaw logs --follow` も使用できます ([/cli/logs](</ja-JP/cli/logs>) を参照)。

## 注意

  * `logging.level` が `warn` より高く設定されている場合、これらのログは抑制されることがあります。デフォルトの `info` で問題ありません。
  * `brave.http` は Brave Search のリクエスト URL/クエリパラメーター、レスポンスステータス/タイミング、キャッシュのヒット/ミス/書き込みイベントをログに記録します。API キーやレスポンス本文はログに記録しませんが、検索クエリは機密情報になり得ます。
  * フラグは有効化したままでも安全です。特定のサブシステムのログ量にのみ影響します。
  * ログの出力先、レベル、リダクションを変更するには [/logging](</ja-JP/logging>) を使用してください。


## 関連

  * [Gateway 診断](</ja-JP/gateway/diagnostics>)
  * [Gateway トラブルシューティング](</ja-JP/gateway/troubleshooting>)


Was this useful?YesNo