---
title: Grok 搜索
source_url: https://docs.openclaw.ai/zh-CN/tools/grok-search
scraped_at: 2026-05-25
---

OpenClaw 支持将 Grok 作为 `web_search` 提供商，使用 xAI 基于 Web grounding 的响应来生成由实时搜索结果和引用支撑的 AI 合成答案。

同一个 xAI API key 也可以驱动内置的 `x_search` 工具，用于搜索 X（原 Twitter）帖子，以及驱动 `code_execution` 工具。如果你将密钥存储在 `plugins.entries.xai.config.webSearch.apiKey` 下，OpenClaw 现在也会将其复用为内置 xAI 模型提供商的后备密钥。

对于帖子级别的 X 指标，例如转发、回复、书签或浏览量，请优先使用带有精确帖子 URL 或状态 ID 的 `x_search`，而不是宽泛的搜索查询。

## 新手引导和配置

如果你在以下流程中选择 **Grok** ：

  * `openclaw onboard`
  * `openclaw configure --section web`


OpenClaw 可以显示一个单独的后续步骤，用同一个 `XAI_API_KEY` 启用 `x_search`。该后续步骤：

  * 仅在你为 `web_search` 选择 Grok 后出现
  * 不是单独的顶级 Web 搜索提供商选项
  * 可以在同一流程中选择性设置 `x_search` 模型


如果你跳过它，可以稍后在配置中启用或更改 `x_search`。

## 获取 API key

* ### 创建密钥

从 [xAI](<https://console.x.ai/>) 获取 API key。

* ### 存储密钥

在 Gateway 网关环境中设置 `XAI_API_KEY`，或通过以下命令配置：

bashCopy code
[code]
    openclaw configure --section web
[/code]

## 配置

json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          webSearch: {            apiKey: "xai-...", // optional if XAI_API_KEY is set            baseUrl: "https://api.x.ai/v1", // optional Responses API proxy/base URL override          },        },      },    },  },  tools: {    web: {      search: {        provider: "grok",      },    },  },}
[/code]

**环境变量替代方式：** 在 Gateway 网关环境中设置 `XAI_API_KEY`。 对于 Gateway 网关安装，请将它放入 `~/.openclaw/.env`。

## 工作原理

Grok 使用 xAI 基于 Web grounding 的响应生成带有内联引用的答案，类似于 Gemini 的 Google Search grounding 方式。

## 支持的参数

Grok 搜索支持 `query`。

为了兼容共享的 `web_search`，也接受 `count`，但 Grok 仍会返回一个带引用的合成答案，而不是 N 条结果列表。

目前不支持提供商特定的筛选器。

Grok 使用提供商特定的 60 秒默认超时时间，因为 xAI Responses 的 Web grounding 搜索可能比共享的 `web_search` 默认时间运行更久。设置 `tools.web.search.timeoutSeconds` 可覆盖它。

## Base URL 覆盖

当 Grok Web 搜索需要通过操作者代理或兼容 xAI 的 Responses 端点路由时，设置 `plugins.entries.xai.config.webSearch.baseUrl`。OpenClaw 会在去除尾部斜杠后向 `<baseUrl>/responses` 发送请求。除非设置了 `plugins.entries.xai.config.xSearch.baseUrl`，否则 `x_search` 会使用同一个 `webSearch.baseUrl` 后备值。

## 相关内容

  * [Web Search 概览](</zh-CN/tools/web>) \-- 所有提供商和自动检测
  * [Web Search 中的 x_search](</zh-CN/tools/web#x_search>) \-- 通过 xAI 实现的一等 X 搜索
  * [Gemini Search](</zh-CN/tools/gemini-search>) \-- 通过 Google grounding 生成的 AI 合成答案


Was this useful?YesNo