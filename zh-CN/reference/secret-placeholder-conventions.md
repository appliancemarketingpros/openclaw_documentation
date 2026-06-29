---
title: 密钥占位符约定
source_url: https://docs.openclaw.ai/zh-CN/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

快速开始

# 密钥占位符约定

使用人类可读但不像真实密钥的占位符。

## 推荐风格

  * 优先使用描述性值，例如 `example-openai-key-not-real` 或 `example-discord-bot-token`。
  * 对于 shell 片段，优先使用 `${OPENAI_API_KEY}`，而不是内联类似 token 的字符串。
  * 让示例明显是假的，并限定在用途范围内（提供商、渠道、凭证类型）。


## 在文档中避免这些模式

  * 字面量 PEM 私钥头部或尾部文本。
  * 类似真实凭证的前缀，例如 `sk-...`、`xoxb-...`、`AKIA...`。
  * 从运行时日志复制的看起来真实的 bearer tokens。


## 示例

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue