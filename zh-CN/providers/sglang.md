---
title: SGLang
source_url: https://docs.openclaw.ai/zh-CN/providers/sglang
scraped_at: 2026-05-25
---

SGLang 通过 OpenAI 兼容的 HTTP API 提供开源权重模型。OpenClaw 使用 `openai-completions` 提供商家族连接到 SGLang，并自动发现可用模型。

属性 | 值  
---|---  
提供商 ID | `sglang`  
插件 | 内置，`enabledByDefault: true`  
认证环境变量 | `SGLANG_API_KEY`（如果服务器没有认证，可为任意非空值）  
新手引导标志 | `--auth-choice sglang`  
API | OpenAI 兼容（`openai-completions`）  
默认基础 URL | `http://127.0.0.1:30000/v1`  
默认模型占位符 | `sglang/Qwen/Qwen3-8B`  
流式传输用量 | 是（`supportsStreamingUsage: true`）  
定价 | 标记为外部免费（`modelPricing.external: false`）  
  
当你使用 `SGLANG_API_KEY` 选择启用时，OpenClaw 还会从 SGLang **自动发现** 可用模型。当你还配置了自定义 SGLang 基础 URL 时，在 `agents.defaults.models` 中使用 `sglang/*` 可保持发现动态进行。请参阅下方的模型发现（隐式提供商）。

## 入门指南

* ### 启动 SGLang

使用 OpenAI 兼容服务器启动 SGLang。你的基础 URL 应暴露 `/v1` 端点（例如 `/v1/models`、`/v1/chat/completions`）。SGLang 通常运行在：

  * `http://127.0.0.1:30000/v1`


* ### 设置 API 密钥

如果你的服务器未配置认证，则任意值都可用：

bashCopy code
[code]
    export SGLANG_API_KEY="sglang-local"
[/code]

* ### 运行新手引导或直接设置模型

bashCopy code
[code]
    openclaw onboard
[/code]

或者手动配置模型：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "sglang/your-model-id" },    },  },}
[/code]

## 模型发现（隐式提供商）

当设置了 `SGLANG_API_KEY`（或存在认证配置文件）并且你**没有** 定义 `models.providers.sglang` 时，OpenClaw 将查询：

  * `GET http://127.0.0.1:30000/v1/models`


并将返回的 ID 转换为模型条目。

## 显式配置（手动模型）

在以下情况下使用显式配置：

  * SGLang 运行在不同主机/端口上。
  * 你想固定 `contextWindow`/`maxTokens` 值。
  * 你的服务器需要真实 API 密钥（或你想控制标头）。

json5Copy code
[code]
    {  models: {    providers: {      sglang: {        baseUrl: "http://127.0.0.1:30000/v1",        apiKey: "${SGLANG_API_KEY}",        api: "openai-completions",        models: [          {            id: "your-model-id",            name: "Local SGLang Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

## 高级配置

代理式行为

SGLang 被视为代理式 OpenAI 兼容 `/v1` 后端，而不是 原生 OpenAI 端点。

行为 | SGLang  
---|---  
仅 OpenAI 的请求整形 | 不应用  
`service_tier`、Responses `store`、提示缓存提示 | 不发送  
推理兼容载荷整形 | 不应用  
隐藏归因标头（`originator`、`version`、`User-Agent`） | 在自定义 SGLang 基础 URL 上不注入  
故障排除

**服务器无法访问**

验证服务器正在运行并响应：

bashCopy code
[code]
    curl http://127.0.0.1:30000/v1/models
[/code]

**认证错误**

如果请求因认证错误失败，请设置与你的服务器配置匹配的真实 `SGLANG_API_KEY`， 或在 `models.providers.sglang` 下显式配置提供商。

## 相关内容

[**模型选择** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**配置参考** 包含提供商条目的完整配置架构。 ](</zh-CN/gateway/configuration-reference>)

Was this useful?YesNo