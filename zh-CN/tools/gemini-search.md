---
title: Gemini 搜索
source_url: https://docs.openclaw.ai/zh-CN/tools/gemini-search
scraped_at: 2026-05-25
---

OpenClaw 支持内置 [Google Search grounding](<https://ai.google.dev/gemini-api/docs/grounding>) 的 Gemini 模型，这会返回由实时 Google Search 结果支持、带有引用的 AI 综合答案。

## 获取 API key

* ### 创建 key

前往 [Google AI Studio](<https://aistudio.google.com/apikey>) 并创建一个 API key。

* ### 存储 key

在 Gateway 网关环境中设置 `GEMINI_API_KEY`，复用 `models.providers.google.apiKey`，或通过以下方式配置专用 Web 搜索 key：

bashCopy code
[code]
    openclaw configure --section web
[/code]

## 配置

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // optional; falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash", // default          },        },      },    },  },  tools: {    web: {      search: {        provider: "gemini",      },    },  },}
[/code]

**凭据优先级：** Gemini Web 搜索首先使用 `plugins.entries.google.config.webSearch.apiKey`，然后是 `GEMINI_API_KEY`， 再然后是 `models.providers.google.apiKey`。对于 base URL，专用的 `plugins.entries.google.config.webSearch.baseUrl` 优先于 `models.providers.google.baseUrl`。

对于 Gateway 网关安装，请将环境 key 放在 `~/.openclaw/.env` 中。

## 工作原理

不同于返回链接和摘要列表的传统搜索提供商，Gemini 使用 Google Search grounding 来生成带有内联引用的 AI 综合答案。结果同时包含综合答案和来源 URL。

  * Gemini grounding 的引用 URL 会自动从 Google 重定向 URL 解析为直接 URL。
  * 重定向解析在返回最终引用 URL 之前，会使用 SSRF 防护路径（HEAD + 重定向检查 + http/https 校验）。
  * 重定向解析使用严格的 SSRF 默认值，因此会阻止重定向到私有/内部目标。


## 支持的参数

Gemini 搜索支持 `query`、`freshness`、`date_after` 和 `date_before`。

`count` 会被接受以兼容共享的 `web_search`，但 Gemini grounding 仍会返回一个带引用的综合答案，而不是 N 条结果的列表。

`freshness` 接受 `day`、`week`、`month`、`year`，以及共享快捷值 `pd`、`pw`、`pm` 和 `py`。OpenClaw 会将这些值，或显式的 `date_after`/`date_before` 范围，转换为 Gemini Google Search grounding 的 `timeRangeFilter`。不支持 `country`、`language` 和 `domain_filter`。

## 模型选择

默认模型是 `gemini-2.5-flash`（快速且成本效益高）。任何支持 grounding 的 Gemini 模型都可以通过 `plugins.entries.google.config.webSearch.model` 使用。

## Base URL 覆盖

当 Gemini Web 搜索必须通过运营方代理或自定义 Gemini 兼容端点路由时，设置 `plugins.entries.google.config.webSearch.baseUrl`。如果未设置，Gemini Web 搜索会复用 `models.providers.google.baseUrl`。普通的 `https://generativelanguage.googleapis.com` 值会被规范化为 `https://generativelanguage.googleapis.com/v1beta`；自定义代理路径会在去除尾随斜杠后按原样保留。

## 相关内容

  * [Web 搜索概览](</zh-CN/tools/web>) \-- 所有提供商和自动检测
  * [Brave Search](</zh-CN/tools/brave-search>) \-- 带摘要的结构化结果
  * [Perplexity Search](</zh-CN/tools/perplexity-search>) \-- 结构化结果 + 内容提取


Was this useful?YesNo