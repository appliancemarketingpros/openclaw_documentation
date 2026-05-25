---
title: Tavily
source_url: https://docs.openclaw.ai/zh-CN/tools/tavily
scraped_at: 2026-05-25
---

[Tavily](<https://tavily.com>) 是一个面向 AI 应用设计的搜索 API。OpenClaw 以两种方式公开它：

  * 作为通用搜索工具的 `web_search` 提供商
  * 作为显式插件工具：`tavily_search` 和 `tavily_extract`


Tavily 返回针对 LLM 消费优化的结构化结果，支持可配置的搜索深度、主题过滤、域名过滤、AI 生成的答案摘要，以及从 URL 提取内容（包括 JavaScript 渲染的页面）。

属性 | 值  
---|---  
插件 id | `tavily`  
凭证 | `TAVILY_API_KEY` 或配置 `apiKey`  
基础 URL | `https://api.tavily.com`（默认）  
内置工具 | `tavily_search`, `tavily_extract`  
  
## 入门指南

* ### 获取 API key

在 [tavily.com](<https://tavily.com>) 创建 Tavily 账户，然后在控制台中生成 API key。

* ### 配置插件和提供商

json5Copy code
[code]
    {  plugins: {    entries: {      tavily: {        enabled: true,        config: {          webSearch: {            apiKey: "tvly-...", // optional if TAVILY_API_KEY is set            baseUrl: "https://api.tavily.com",          },        },      },    },  },  tools: {    web: {      search: {        provider: "tavily",      },    },  },}
[/code]

* ### 验证搜索能运行

从任意智能体触发一次 `web_search`，或直接调用 `tavily_search`。

## 工具参考

### `tavily_search`

当你需要使用 Tavily 特有的搜索控制，而不是通用的 `web_search` 时，请使用此工具。

参数 | 类型 | 约束 / 默认值 | 描述  
---|---|---|---  
`query` | string | 必填 | 搜索查询字符串。保持在 400 个字符以内。  
`search_depth` | enum | `basic`（默认）、`advanced` | `advanced` 较慢，但相关性更高。  
`topic` | enum | `general`（默认）、`news`、`finance` | 按主题类别过滤。  
`max_results` | integer | 1-20 | 结果数量。  
`include_answer` | boolean | 默认 `false` | 包含 Tavily AI 生成的答案摘要。  
`time_range` | enum | `day`、`week`、`month`、`year` | 按新近程度过滤结果。  
`include_domains` | string array | （无） | 仅包含来自这些域名的结果。  
`exclude_domains` | string array | （无） | 排除来自这些域名的结果。  
  
搜索深度权衡：

深度 | 速度 | 相关性 | 最适合  
---|---|---|---  
`basic` | 更快 | 高 | 通用查询（默认）。  
`advanced` | 更慢 | 最高 | 精确研究和事实查找。  
  
### `tavily_extract`

使用此工具从一个或多个 URL 提取干净内容。可处理 JavaScript 渲染的页面，并支持面向查询的分块，用于有针对性的提取。

参数 | 类型 | 约束 / 默认值 | 描述  
---|---|---|---  
`urls` | string array | 必填，1-20 | 要从中提取内容的 URL。  
`query` | string | （可选） | 按与此查询的相关性对提取的分块重新排序。  
`extract_depth` | enum | `basic`（默认）、`advanced` | 对 JS 较重的页面、SPA 或动态表格使用 `advanced`。  
`chunks_per_source` | integer | 1-5；**需要`query`** | 每个 URL 返回的分块数。如果未设置 `query` 则会报错。  
`include_images` | boolean | 默认 `false` | 在结果中包含图片 URL。  
  
提取深度权衡：

深度 | 何时使用  
---|---  
`basic` | 简单页面。先尝试这个。  
`advanced` | JS 渲染的 SPA、动态内容、表格。  
  
## 选择合适的工具

需求 | 工具  
---|---  
快速 Web 搜索，无特殊选项 | `web_search`  
使用深度、主题、AI 答案进行搜索 | `tavily_search`  
从特定 URL 提取内容 | `tavily_extract`  
  
## 高级配置

API key 解析顺序

Tavily 客户端按以下顺序查找其 API key：

  1. `plugins.entries.tavily.config.webSearch.apiKey`（通过 SecretRefs 解析）。
  2. Gateway 网关环境中的 `TAVILY_API_KEY`。


如果两者都不存在，`tavily_extract` 会抛出设置错误。

自定义基础 URL

如果你通过代理前置 Tavily，请覆盖 `plugins.entries.tavily.config.webSearch.baseUrl`。默认值为 `https://api.tavily.com`。

`chunks_per_source` 需要 `query`

`tavily_extract` 会拒绝传入 `chunks_per_source` 但未传入 `query` 的调用。Tavily 会按查询相关性对分块排序，因此没有查询时该参数没有意义。

## 相关

[**Web 搜索概览** 所有提供商和自动检测规则。 ](</zh-CN/tools/web>) [**Firecrawl** 搜索加内容提取式抓取。 ](</zh-CN/tools/firecrawl>) [**Exa Search** 带内容提取的神经搜索。 ](</zh-CN/tools/exa-search>) [**配置** 插件条目和工具路由的完整配置架构。 ](</zh-CN/gateway/configuration>)

Was this useful?YesNo