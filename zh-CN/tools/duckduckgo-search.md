---
title: DuckDuckGo 搜索
source_url: https://docs.openclaw.ai/zh-CN/tools/duckduckgo-search
scraped_at: 2026-05-25
---

OpenClaw 支持将 DuckDuckGo 作为**无需密钥** 的 `web_search` 提供商。无需 API 密钥或账户。

## 设置

无需 API 密钥，只需将 DuckDuckGo 设置为你的提供商：

* ### 配置

bashCopy code
[code]
    openclaw configure --section web# Select "duckduckgo" as the provider
[/code]

## 配置

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "duckduckgo",      },    },  },}
[/code]

用于区域和 SafeSearch 的可选插件级设置：

json5Copy code
[code]
    {  plugins: {    entries: {      duckduckgo: {        config: {          webSearch: {            region: "us-en", // DuckDuckGo region code            safeSearch: "moderate", // "strict", "moderate", or "off"          },        },      },    },  },}
[/code]

## 工具参数

搜索查询。

要返回的结果数（1-10）。

DuckDuckGo 区域代码（例如 `us-en`、`uk-en`、`de-de`）。

SafeSearch 级别。

区域和 SafeSearch 也可以在插件配置中设置（见上文），工具 参数会按每个查询覆盖配置值。

## 备注

  * **无需 API 密钥** \- 开箱即用，零配置
  * **实验性** \- 从 DuckDuckGo 的非 JavaScript HTML 搜索页面收集结果，而不是官方 API 或 SDK
  * **机器人验证风险** \- 在高频或自动化使用下，DuckDuckGo 可能会提供 CAPTCHA 或阻止请求
  * **HTML 解析** \- 结果依赖页面结构，而页面结构可能会在未通知的情况下更改
  * **自动检测顺序** \- DuckDuckGo 是第一个无需密钥的回退项 （顺序 100）。已配置密钥的 API 后端提供商会先运行， 然后是 Ollama Web 搜索（顺序 110），再然后是 SearXNG（顺序 200）
  * **未配置时 SafeSearch 默认为 moderate**


## 相关

  * [Web Search 概览](</zh-CN/tools/web>) \-- 所有提供商和自动检测
  * [Brave Search](</zh-CN/tools/brave-search>) \-- 提供免费层级的结构化结果
  * [Exa Search](</zh-CN/tools/exa-search>) \-- 带内容提取的神经搜索


Was this useful?YesNo