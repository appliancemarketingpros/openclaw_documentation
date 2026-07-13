---
title: ウィジェットを表示
source_url: https://docs.openclaw.ai/ja-JP/tools/show-widget
scraped_at: 2026-07-13
---

CapabilitiesTools

`show_widget` は、自己完結型の SVG または HTML フラグメントを Control UI のチャットトランスクリプト内にインラインでレンダリングします。同梱の Canvas Plugin がこのツールを所有し、各結果を同一オリジンの Canvas ドキュメントとしてホストします。

このツールは、呼び出し元の Gateway クライアントが `inline-widgets` ケイパビリティを宣言している場合にのみ使用できます。Control UI はこのケイパビリティを自動的に宣言します。Telegram や WhatsApp などのチャネル実行では `show_widget` を利用できません。

ケイパビリティの伝達は、組み込み、Codex app-server、および CLI ベースのモデルバックエンドに対応しています。権限付与によって認証された MCP 呼び出し元と、直接 HTTP でツールを呼び出す呼び出し元は、クライアントケイパビリティを宣言しないため、引き続きフェイルクローズとなります。

## ツールを使用する

エージェントは、次の 2 つの必須文字列を指定します。

インラインプレビューと、ホストされるドキュメントのタイトルに表示される短いタイトル。

自己完結型の SVG または HTML フラグメント。前後の空白を除去した後に `<svg` で始まる入力は SVG モードでレンダリングされ、それ以外の入力はすべて HTML フラグメントとして扱われます。最大長: 262,144 文字。

ツールの結果には Canvas プレビューハンドルが含まれるため、Web チャットはツール呼び出しからウィジェットを直接レンダリングし、履歴の再読み込み後にも復元します。プレビューをレンダリングしないトランスクリプトでも、ホストされている Canvas パスは表示されます。

## セキュリティとストレージ

ウィジェットドキュメントは、制限の厳しい Content Security Policy を使用します。インラインのスタイルとスクリプトは許可され、画像では `data:` URL を使用できますが、外部へのフェッチとリソースの読み込みはブロックされます。すべてのマークアップ、スタイル、スクリプト、画像データを `widget_code` 内に含めてください。

Control UI のグローバル埋め込みモードが `trusted` の場合でも、iframe では常に `allow-same-origin` が省略されるため、ウィジェットのスクリプトは親アプリケーションのオリジンを読み取れません。また、Canvas ホストは `Content-Security-Policy: sandbox allow-scripts` レスポンスヘッダーを付けてウィジェットドキュメントを配信するため、ホストされた URL を直接開いた場合でも、ウィジェットは Control UI のオリジンではなく不透明なオリジンで実行されます。ブラウザーのサンドボックス化では、スクリプトが自身の iframe をナビゲートすることは防げません。その隔離されたフレーム内で実行してもよいウィジェットコードのみをレンダリングしてください。

iframe は [`gateway.controlUi.embedSandbox`](</ja-JP/web/control-ui#hosted-embeds>) にも従います。デフォルトの `scripts` ティアでは、オリジンの隔離を維持しながらインタラクティブなウィジェットを利用できます。

Canvas は、セッションごとに最大 32 個のウィジェットを保持します（セッションがない場合はエージェントごと）。さらにウィジェットを作成すると、そのスコープ内で最も古いドキュメントが削除されます。

## 関連項目

  * [Control UI のホスト型埋め込み](</ja-JP/web/control-ui#hosted-embeds>)
  * [Canvas Plugin](</ja-JP/plugins/reference/canvas>)
  * [Gateway プロトコルのクライアントケイパビリティ](</ja-JP/gateway/protocol#client-capabilities>)


Was this useful?YesNo

Open issue