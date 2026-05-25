---
title: Perplexity 搜索
source_url: https://docs.openclaw.ai/zh-CN/tools/perplexity-search
scraped_at: 2026-05-25
---

OpenClaw 支持将 Perplexity Search API 作为 `web_search` 提供商。 它会返回带有 `title`、`url` 和 `snippet` 字段的结构化结果。

为保持兼容性，OpenClaw 也支持旧版 Perplexity Sonar/OpenRouter 设置。 如果你使用 `OPENROUTER_API_KEY`、在 `plugins.entries.perplexity.config.webSearch.apiKey` 中使用 `sk-or-...` 密钥，或设置 `plugins.entries.perplexity.config.webSearch.baseUrl` / `model`，该提供商会切换到 chat-completions 路径，并返回带引用的 AI 合成答案，而不是结构化的 Search API 结果。

## 获取 Perplexity API key

  1. 在 [perplexity.ai/settings/api](<https://www.perplexity.ai/settings/api>) 创建 Perplexity 账号
  2. 在仪表板中生成 API key
  3. 将密钥存储在配置中，或在 Gateway 网关环境中设置 `PERPLEXITY_API_KEY`。


## OpenRouter 兼容性

如果你已经在为 Perplexity Sonar 使用 OpenRouter，请保留 `provider: "perplexity"`，并在 Gateway 网关环境中设置 `OPENROUTER_API_KEY`，或在 `plugins.entries.perplexity.config.webSearch.apiKey` 中存储一个 `sk-or-...` 密钥。

可选兼容性控制项：

  * `plugins.entries.perplexity.config.webSearch.baseUrl`
  * `plugins.entries.perplexity.config.webSearch.model`


## 配置示例

### 原生 Perplexity Search API

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "pplx-...",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

### OpenRouter / Sonar 兼容性

json5Copy code
[code]
    {  plugins: {    entries: {      perplexity: {        config: {          webSearch: {            apiKey: "<openrouter-api-key>",            baseUrl: "https://openrouter.ai/api/v1",            model: "perplexity/sonar-pro",          },        },      },    },  },  tools: {    web: {      search: {        provider: "perplexity",      },    },  },}
[/code]

## 在哪里设置密钥

**通过配置：**运行 `openclaw configure --section web`。它会将密钥存储在 `~/.openclaw/openclaw.json` 的 `plugins.entries.perplexity.config.webSearch.apiKey` 下。 该字段也接受 SecretRef 对象。

**通过环境：**在 Gateway 网关进程环境中设置 `PERPLEXITY_API_KEY` 或 `OPENROUTER_API_KEY`。 对于 Gateway 网关安装，请将其放入 `~/.openclaw/.env`（或你的服务环境）。参见[环境变量](</zh-CN/help/faq#env-vars-and-env-loading>)。

如果配置了 `provider: "perplexity"`，且 Perplexity 密钥 SecretRef 未解析且没有环境回退，启动/重载会快速失败。

## 工具参数

这些参数适用于原生 Perplexity Search API 路径。

搜索查询。

要返回的结果数量（1-10）。

2 字母 ISO 国家代码（例如 `US`、`DE`）。

ISO 639-1 语言代码（例如 `en`、`de`、`fr`）。

时间筛选器 - `day` 表示 24 小时。

仅返回在此日期之后发布的结果（`YYYY-MM-DD`）。

仅返回在此日期之前发布的结果（`YYYY-MM-DD`）。

域名允许列表/拒绝列表数组（最多 20 个）。

总内容预算（最大 1000000）。

每页 token 限制。

对于旧版 Sonar/OpenRouter 兼容路径：

  * 接受 `query`、`count` 和 `freshness`
  * `count` 在该路径中仅用于兼容；响应仍然是一个带引用的合成答案，而不是 N 条结果列表
  * 仅适用于 Search API 的筛选器，例如 `country`、`language`、`date_after`、`date_before`、`domain_filter`、`max_tokens` 和 `max_tokens_per_page`，会返回明确错误


**示例：**

javascriptCopy code
[code]
    // Country and language-specific searchawait web_search({  query: "renewable energy",  country: "DE",  language: "de",}); // Recent results (past week)await web_search({  query: "AI news",  freshness: "week",}); // Date range searchawait web_search({  query: "AI developments",  date_after: "2024-01-01",  date_before: "2024-06-30",}); // Domain filtering (allowlist)await web_search({  query: "climate research",  domain_filter: ["nature.com", "science.org", ".edu"],}); // Domain filtering (denylist - prefix with -)await web_search({  query: "product reviews",  domain_filter: ["-reddit.com", "-pinterest.com"],}); // More content extractionawait web_search({  query: "detailed AI research",  max_tokens: 50000,  max_tokens_per_page: 4096,});
[/code]

### 域名筛选规则

  * 每个筛选器最多 20 个域名
  * 不能在同一个请求中混用允许列表和拒绝列表
  * 对拒绝列表条目使用 `-` 前缀（例如 `["-reddit.com"]`）


## 备注

  * Perplexity Search API 返回结构化网页搜索结果（`title`、`url`、`snippet`）
  * OpenRouter 或显式设置 `plugins.entries.perplexity.config.webSearch.baseUrl` / `model` 会为了兼容性将 Perplexity 切回 Sonar chat completions
  * Sonar/OpenRouter 兼容性会返回一个带引用的合成答案，而不是结构化结果行
  * 结果默认缓存 15 分钟（可通过 `cacheTtlMinutes` 配置）


## 相关

[**Web 搜索概览** 所有提供商和自动检测规则。 ](</zh-CN/tools/web>) [**Brave 搜索** 带国家和语言筛选器的结构化结果。 ](</zh-CN/tools/brave-search>) [**Exa 搜索** 带内容提取的神经搜索。 ](</zh-CN/tools/exa-search>) [**Perplexity Search API 文档** 官方 Perplexity Search API 快速开始和参考。 ](<https://docs.perplexity.ai/docs/search/quickstart>)

Was this useful?YesNo