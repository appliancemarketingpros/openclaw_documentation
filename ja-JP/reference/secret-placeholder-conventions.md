---
title: シークレットプレースホルダーの規則
source_url: https://docs.openclaw.ai/ja-JP/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# シークレットプレースホルダーの規約

実際のシークレットに見えない、人間が読めるプレースホルダーを使用します。

## 推奨スタイル

  * `example-openai-key-not-real` や `example-discord-bot-token` のような説明的な値を優先します。
  * シェルスニペットでは、インラインのトークン風文字列よりも `${OPENAI_API_KEY}` を優先します。
  * 例は明らかに偽物で、目的（プロバイダー、チャンネル、認証タイプ）に限定します。


## ドキュメントで避けるべきパターン

  * PEM 秘密鍵のヘッダーまたはフッターのリテラルテキスト。
  * `sk-...`、`xoxb-...`、`AKIA...` など、実際の認証情報に似たプレフィックス。
  * ランタイムログからコピーされた、本物らしく見えるベアラートークン。


## 例

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue