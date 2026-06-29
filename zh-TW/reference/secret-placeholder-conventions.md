---
title: 機密預留位置慣例
source_url: https://docs.openclaw.ai/zh-TW/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# 機密佔位符慣例

使用人類可讀、但不會像真實機密的佔位符。

## 建議風格

  * 優先使用描述性值，例如 `example-openai-key-not-real` 或 `example-discord-bot-token`。
  * 對於 shell 片段，優先使用 `${OPENAI_API_KEY}`，而不是內嵌類似權杖的字串。
  * 讓範例明顯是假的，並限定在用途範圍內（提供者、頻道、驗證類型）。


## 在文件中避免這些模式

  * 字面 PEM 私密金鑰標頭或結尾文字。
  * 類似即時憑證的前綴，例如 `sk-...`、`xoxb-...`、`AKIA...`。
  * 從執行階段記錄複製的、看起來真實的 bearer token。


## 範例

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue