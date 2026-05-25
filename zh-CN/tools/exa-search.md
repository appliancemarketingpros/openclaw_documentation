---
title: Exa 搜索
source_url: https://docs.openclaw.ai/zh-CN/tools/exa-search
scraped_at: 2026-05-25
---

OpenClaw 支持将 [Exa AI](<https://exa.ai/>) 作为 `web_search` 提供商。Exa 提供神经、关键词和混合搜索模式，并内置内容提取 （高亮、文本、摘要）。

## 获取 API 密钥

* ### Create an account

在 [exa.ai](<https://exa.ai/>) 注册，并从你的 控制台生成 API 密钥。

* ### Store the key

在 Gateway 网关环境中设置 `EXA_API_KEY`，或通过以下方式配置：

bashCopy code
[code]
    openclaw configure --section web
[/code]

## 配置

json5Copy code
[code]
    {  plugins: {    entries: {      exa: {        config: {          webSearch: {            apiKey: "exa-...", // optional if EXA_API_KEY is set            baseUrl: "https://api.exa.ai", // optional; OpenClaw appends /search          },        },      },    },  },  tools: {    web: {      search: {        provider: "exa",      },    },  },}
[/code]

**环境替代方案：**在 Gateway 网关环境中设置 `EXA_API_KEY`。 对于 Gateway 网关安装，把它放在 `~/.openclaw/.env` 中。

## 基础 URL 覆盖

当 Exa 搜索请求需要通过兼容代理或备用 Exa 端点时，设置 `plugins.entries.exa.config.webSearch.baseUrl`。OpenClaw 会通过前置 `https://` 规范化裸主机，并追加 `/search`，除非 路径已经以它结尾。解析后的端点会包含在搜索缓存 键中，因此来自不同 Exa 端点的结果不会共享。

## 工具参数

搜索查询。

要返回的结果数量（1–100）。

搜索模式。

时间过滤器。

此日期之后的结果（`YYYY-MM-DD`）。

此日期之前的结果（`YYYY-MM-DD`）。

内容提取选项（见下文）。

### 内容提取

Exa 可以在搜索结果旁返回提取的内容。传入 `contents` 对象以启用：

javascriptCopy code
[code]
    await web_search({  query: "transformer architecture explained",  type: "neural",  contents: {    text: true, // full page text    highlights: { numSentences: 3 }, // key sentences    summary: true, // AI summary  },});
[/code]

内容选项 | 类型 | 描述  
---|---|---  
`text` | `boolean | { maxCharacters }` | 提取完整页面文本  
`highlights` | `boolean | { maxCharacters, query, numSentences, highlightsPerUrl }` | 提取关键句子  
`summary` | `boolean | { query }` | AI 生成的摘要  
  
### 搜索模式

模式 | 描述  
---|---  
`auto` | Exa 选择最佳模式（默认）  
`neural` | 基于语义/含义的搜索  
`fast` | 快速关键词搜索  
`deep` | 彻底的深度搜索  
`deep-reasoning` | 带推理的深度搜索  
`instant` | 最快结果  
  
## 注意事项

  * 如果没有提供 `contents` 选项，Exa 默认使用 `{ highlights: true }`， 因此结果会包含关键句摘录
  * 可用时，结果会保留来自 Exa API 响应的 `highlightScores` 和 `summary` 字段
  * 结果描述会优先从高亮中解析，其次是摘要，然后是 全文，以可用者为准
  * `freshness` 和 `date_after`/`date_before` 不能组合使用，请使用一种 时间过滤模式
  * 每次查询最多可返回 100 个结果（受 Exa 搜索类型 限制约束）
  * 结果默认缓存 15 分钟（可通过 `cacheTtlMinutes` 配置）
  * Exa 是一个官方 API 集成，提供结构化 JSON 响应


## 相关

  * [Web 搜索概览](</zh-CN/tools/web>) \-- 所有提供商和自动检测
  * [Brave Search](</zh-CN/tools/brave-search>) \-- 带国家/语言过滤器的结构化结果
  * [Perplexity Search](</zh-CN/tools/perplexity-search>) \-- 带域名过滤的结构化结果


Was this useful?YesNo