---
title: 画面
source_url: https://docs.openclaw.ai/ja-JP/tools/screen
scraped_at: 2026-10-12
---

CapabilitiesTools

`screen` ツールを使用すると、エージェントはブラウザベースの Control UI を配置できます。これは型付きのレイアウトおよびナビゲーションサーフェスであり、スクリーンショットの取得やブラウザの自動操作を行うものではありません。

このツールは、接続元のクライアントが `ui-commands` ケイパビリティを通知している場合にのみ公開されます。ツールの実行時にも、対応する Control UI が少なくとも 1 つ接続されている必要があります。それ以外の場合、Gateway は `UNAVAILABLE` を返します。

## アクション

アクション | 効果 | オプション入力  
---|---|---  
`split_right` | 対象セッションペインを右方向に分割する | `sessionKey`（デフォルトは現在のセッション）  
`split_down` | 対象セッションペインを下方向に分割する | `sessionKey`（デフォルトは現在のセッション）  
`close_pane` | 対象セッションペインを閉じる | `sessionKey`（デフォルトは現在のセッション）  
`focus` | 対象セッションペインにフォーカスする | `sessionKey`（デフォルトは現在のセッション）  
`navigate` | 対象セッションを開く | `sessionKey`（デフォルトは現在のセッション）  
`sidebar_show` / `sidebar_hide` | メインサイドバーを表示または非表示にする | -  
`terminal_show` / `terminal_hide` | オペレーター用ターミナルパネルを表示または非表示にする | 表示時は `dock`（`bottom` または `right`）  
`browser_show` / `browser_hide` | ブラウザパネルを表示または非表示にする | 表示時は `dock`（`bottom` または `right`）  
  
コマンドが成功すると、Gateway が型付きの `ui.command` イベントをブロードキャストした後、`{ "ok": true }` が返されます。

## ルーティングとセキュリティ

プロトコル v1 では、意図的に `ui-commands` を通知する接続済みのすべての Control UI にコマンドを送信します。特定のブラウザタブを対象にすることはありません。これは、同じオペレーターが複数のダッシュボードを開いている場合に重要です。

Gateway RPC には `operator.write` が必要です。このツールで変更できるのは表示状態のみです。ピクセルの読み取り、スクリーンショットの取得、ページ上の任意のコンテンツのクリック、選択したセッションおよびオペレーターパネルの権限の回避はできません。

## 関連項目

  * [Control UI](</web/control-ui>)
  * [Gateway プロトコル](</ja-JP/gateway/protocol#method-families>)
  * [ブラウザツール](</ja-JP/tools/browser>)


Was this useful?YesNo

Open issue