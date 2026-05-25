---
title: リッチ出力プロトコル
source_url: https://docs.openclaw.ai/ja-JP/reference/rich-output-protocol
scraped_at: 2026-05-25
---

アシスタント出力には、少数の配信/レンダリングディレクティブを含めることができます。

  * 添付ファイル配信用の `MEDIA:`
  * 音声表示ヒント用の `[[audio_as_voice]]`
  * 返信メタデータ用の `[[reply_to_current]]` / `[[reply_to:<id>]]`
  * Control UI のリッチレンダリング用の `[embed ...]`


リモートの `MEDIA:` 添付ファイルは、公開 `https:` URL である必要があります。プレーンな `http:`、 ループバック、リンクローカル、プライベート、および内部ホスト名は添付ファイル ディレクティブとして無視されます。サーバー側のメディア取得機能は、引き続き独自のネットワークガードを適用します。

ローカルの `MEDIA:` 添付ファイルでは、絶対パス、ワークスペース相対パス、または ホーム相対の `~/` パスを使用できます。配信前に、引き続きエージェントのファイル読み取りポリシーと メディアタイプチェックを通過します。

プレーンな Markdown 画像構文は、デフォルトではテキストのままです。Markdown 画像返信を意図的にメディア添付ファイルへマップするチャネルは、送信 アダプターでオプトインします。Telegram はこれを行うため、`![alt](url)` は引き続きメディア返信になり得ます。

これらのディレクティブは別々のものです。`MEDIA:` と返信/音声タグは配信メタデータのままです。`[embed ...]` は Web 専用のリッチレンダリングパスです。 信頼済みツール結果のメディアは、配信前に同じ `MEDIA:` / `[[audio_as_voice]]` パーサーを使用するため、テキストツール出力でも音声添付ファイルをボイスメモとしてマークできます。

ブロックストリーミングが有効な場合、`MEDIA:` はターンに対する単一配信メタデータのままです。同じメディア URL がストリーミングされたブロックで送信され、最終 アシスタントペイロードで繰り返された場合、OpenClaw は添付ファイルを一度だけ配信し、最終ペイロードから重複を取り除きます。

## `[embed ...]`

`[embed ...]` は、Control UI 向けの唯一のエージェント向けリッチレンダリング構文です。

自己終了の例:

textCopy code
[code]
    [embed ref="cv_123" title="Status" /]
[/code]

ルール:

  * `[view ...]` は新しい出力では有効ではありません。
  * Embed ショートコードは、アシスタントメッセージサーフェスでのみレンダリングされます。
  * URL に基づく Embed のみがレンダリングされます。`ref="..."` または `url="..."` を使用してください。
  * ブロック形式のインライン HTML Embed ショートコードはレンダリングされません。
  * Web UI は表示テキストからショートコードを取り除き、Embed をインラインでレンダリングします。
  * `MEDIA:` は Embed のエイリアスではなく、リッチ Embed レンダリングに使用すべきではありません。


## 保存されるレンダリング形状

正規化/保存されるアシスタントコンテンツブロックは、構造化された `canvas` アイテムです。

jsonCopy code
[code]
    {  "type": "canvas",  "preview": {    "kind": "canvas",    "surface": "assistant_message",    "render": "url",    "viewId": "cv_123",    "url": "/__openclaw__/canvas/documents/cv_123/index.html",    "title": "Status",    "preferredHeight": 320  }}
[/code]

保存/レンダリングされるリッチブロックは、この `canvas` 形状を直接使用します。`present_view` は認識されません。

## 関連

  * [RPC アダプター](</ja-JP/reference/rpc>)
  * [Typebox](</ja-JP/concepts/typebox>)


Was this useful?YesNo