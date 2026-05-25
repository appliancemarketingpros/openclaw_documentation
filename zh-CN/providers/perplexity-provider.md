---
title: Perplexity
source_url: https://docs.openclaw.ai/zh-CN/providers/perplexity-provider
scraped_at: 2026-05-25
---

Perplexity 插件通过 Perplexity Search API 或经由 OpenRouter 的 Perplexity Sonar 提供 Web 搜索能力。

属性 | 值  
---|---  
类型 | Web 搜索提供商（不是模型提供商）  
认证 | `PERPLEXITY_API_KEY`（直连）或 `OPENROUTER_API_KEY`（通过 OpenRouter）  
配置路径 | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## 入门指南

* ### 设置 API key

运行交互式 Web 搜索配置流程：

bashCopy code
[code]
    openclaw configure --section web
[/code]

或直接设置密钥：

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### 开始搜索

一旦配置好密钥，智能体会自动使用 Perplexity 进行 Web 搜索。 无需额外步骤。

## 搜索模式

插件会根据 API key 前缀自动选择传输方式：

### 原生 Perplexity API（pplx-）

当你的密钥以 `pplx-` 开头时，OpenClaw 会使用原生 Perplexity Search API。此传输方式会返回结构化结果，并支持域名、语言和日期过滤（见下方过滤选项）。

### OpenRouter / Sonar（sk-or-）

当你的密钥以 `sk-or-` 开头时，OpenClaw 会通过 OpenRouter 路由，并使用 Perplexity Sonar 模型。此传输方式会返回带引用的 AI 综合答案。

密钥前缀 | 传输方式 | 功能  
---|---|---  
`pplx-` | 原生 Perplexity Search API | 结构化结果、域名/语言/日期过滤  
`sk-or-` | OpenRouter（Sonar） | 带引用的 AI 综合答案  
  
## 原生 API 过滤

使用原生 Perplexity API 时，搜索支持以下过滤器：

过滤器 | 说明 | 示例  
---|---|---  
国家 | 两位国家代码 | `us`、`de`、`jp`  
语言 | ISO 639-1 语言代码 | `en`、`fr`、`zh`  
日期范围 | 最近时间窗口 | `day`、`week`、`month`、`year`  
域名过滤 | allowlist 或 denylist（最多 20 个域名） | `example.com`  
内容预算 | 每次响应 / 每页的 token 上限 | `max_tokens`、`max_tokens_per_page`  
  
## 高级配置

守护进程的环境变量

如果 OpenClaw Gateway 网关 作为守护进程运行（launchd/systemd），请确保 `PERPLEXITY_API_KEY` 对该进程可见。

OpenRouter 代理设置

如果你更希望通过 OpenRouter 路由 Perplexity 搜索，请设置 `OPENROUTER_API_KEY`（前缀为 `sk-or-`），而不是原生 Perplexity 密钥。 OpenClaw 会检测此前缀，并自动切换到 Sonar 传输方式。

## 相关

[**Perplexity 搜索工具** 智能体如何调用 Perplexity 搜索并解释结果。 ](</zh-CN/tools/perplexity-search>) [**配置参考** 完整配置参考，包括插件条目。 ](</zh-CN/gateway/configuration-reference>)

Was this useful?YesNo