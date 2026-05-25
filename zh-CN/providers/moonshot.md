---
title: Moonshot AI
source_url: https://docs.openclaw.ai/zh-CN/providers/moonshot
scraped_at: 2026-05-25
---

Moonshot 提供具有 OpenAI 兼容端点的 Kimi API。配置 provider，并将默认模型设置为 `moonshot/kimi-k2.6`，或通过 `kimi/kimi-for-coding` 使用 Kimi Coding。

## 内置模型目录

模型引用 | 名称 | 推理 | 输入 | 上下文 | 最大输出  
---|---|---|---|---|---  
`moonshot/kimi-k2.6` | Kimi K2.6 | 否 | 文本，图像 | 262,144 | 262,144  
`moonshot/kimi-k2.5` | Kimi K2.5 | 否 | 文本，图像 | 262,144 | 262,144  
`moonshot/kimi-k2-thinking` | Kimi K2 Thinking | 是 | 文本 | 262,144 | 262,144  
`moonshot/kimi-k2-thinking-turbo` | Kimi K2 Thinking Turbo | 是 | 文本 | 262,144 | 262,144  
`moonshot/kimi-k2-turbo` | Kimi K2 Turbo | 否 | 文本 | 256,000 | 16,384  
  
当前由 Moonshot 托管的 K2 模型的内置成本估算使用 Moonshot 发布的按量付费费率：Kimi K2.6 为缓存命中 $0.16/MTok、 输入 $0.95/MTok、输出 $4.00/MTok；Kimi K2.5 为缓存命中 $0.10/MTok、 输入 $0.60/MTok、输出 $3.00/MTok。其他旧版目录条目会保留 零成本占位符，除非你在配置中覆盖它们。

## 入门指南

选择你的提供商并按照设置步骤操作。

### Moonshot API

**最适合：** 通过 Moonshot Open Platform 使用 Kimi K2 模型。

* ### Choose your endpoint region

凭证选择 | 端点 | 地区  
---|---|---  
`moonshot-api-key` | `https://api.moonshot.ai/v1` | 国际版  
`moonshot-api-key-cn` | `https://api.moonshot.cn/v1` | 中国  
* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key
[/code]

或者使用中国端点：

bashCopy code
[code]
    openclaw onboard --auth-choice moonshot-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },    },  },}
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list --provider moonshot
[/code]

* ### Run a live smoke test

当你想验证模型访问和成本跟踪，同时不影响你的常规会话时， 使用隔离的状态目录：

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=/tmp/openclaw-kimi/openclaw.json \OPENCLAW_STATE_DIR=/tmp/openclaw-kimi \openclaw agent --local \  --session-id live-kimi-cost \  --message 'Reply exactly: KIMI_LIVE_OK' \  --thinking off \  --json
[/code]

JSON 响应应报告 `provider: "moonshot"` 和 `model: "kimi-k2.6"`。当 Moonshot 返回使用量元数据时， assistant 转录条目会在 `usage.cost` 下存储规范化的 token 使用量以及估算成本。

### 配置示例

json5Copy code
[code]
    {  env: { MOONSHOT_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "moonshot/kimi-k2.6" },      models: {        // moonshot-kimi-k2-aliases:start        "moonshot/kimi-k2.6": { alias: "Kimi K2.6" },        "moonshot/kimi-k2.5": { alias: "Kimi K2.5" },        "moonshot/kimi-k2-thinking": { alias: "Kimi K2 Thinking" },        "moonshot/kimi-k2-thinking-turbo": { alias: "Kimi K2 Thinking Turbo" },        "moonshot/kimi-k2-turbo": { alias: "Kimi K2 Turbo" },        // moonshot-kimi-k2-aliases:end      },    },  },  models: {    mode: "merge",    providers: {      moonshot: {        baseUrl: "https://api.moonshot.ai/v1",        apiKey: "${MOONSHOT_API_KEY}",        api: "openai-completions",        models: [          // moonshot-kimi-k2-models:start          {            id: "kimi-k2.6",            name: "Kimi K2.6",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.95, output: 4, cacheRead: 0.16, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2.5",            name: "Kimi K2.5",            reasoning: false,            input: ["text", "image"],            cost: { input: 0.6, output: 3, cacheRead: 0.1, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking",            name: "Kimi K2 Thinking",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-thinking-turbo",            name: "Kimi K2 Thinking Turbo",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 262144,          },          {            id: "kimi-k2-turbo",            name: "Kimi K2 Turbo",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 256000,            maxTokens: 16384,          },          // moonshot-kimi-k2-models:end        ],      },    },  },}
[/code]

### Kimi Coding

**最适合：** 通过 Kimi Coding 端点执行以代码为中心的任务。

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice kimi-code-api-key
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider kimi
[/code]

### 配置示例

json5Copy code
[code]
    {  env: { KIMI_API_KEY: "sk-..." },  agents: {    defaults: {      model: { primary: "kimi/kimi-for-coding" },      models: {        "kimi/kimi-for-coding": { alias: "Kimi" },      },    },  },}
[/code]

## Kimi Web 搜索

OpenClaw 还将 **Kimi** 作为 `web_search` 提供商随附提供，由 Moonshot Web 搜索支持。

* ### 运行交互式 Web 搜索设置

bashCopy code
[code]
    openclaw configure --section web
[/code]

在 Web 搜索部分选择 **Kimi** ，以存储 `plugins.entries.moonshot.config.webSearch.*`。

* ### 配置 Web 搜索区域和模型

交互式设置会提示：

设置 | 选项  
---|---  
API 区域 | `https://api.moonshot.ai/v1`（国际版）或 `https://api.moonshot.cn/v1`（中国）  
Web 搜索模型 | 默认为 `kimi-k2.6`  
  
配置位于 `plugins.entries.moonshot.config.webSearch` 下：

json5Copy code
[code]
    {  plugins: {    entries: {      moonshot: {        config: {          webSearch: {            apiKey: "sk-...", // or use KIMI_API_KEY / MOONSHOT_API_KEY            baseUrl: "https://api.moonshot.ai/v1",            model: "kimi-k2.6",          },        },      },    },  },  tools: {    web: {      search: {        provider: "kimi",      },    },  },}
[/code]

## 高级配置

原生思考模式

Moonshot Kimi 支持二进制原生思考：

  * `thinking: { type: "enabled" }`
  * `thinking: { type: "disabled" }`


通过 `agents.defaults.models.<provider/model>.params` 按模型配置：

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "disabled" },          },        },      },    },  },}
[/code]

OpenClaw 还会为 Moonshot 映射运行时 `/think` 级别：

`/think` 级别 | Moonshot 行为  
---|---  
`/think off` | `thinking.type=disabled`  
任何非 off 级别 | `thinking.type=enabled`  
  
Kimi K2.6 还接受可选的 `thinking.keep` 字段，用于控制 `reasoning_content` 的多轮保留。将其设置为 `"all"` 可在轮次之间保留完整 推理；省略它（或将其保留为 `null`）则使用服务器 默认策略。OpenClaw 只会为 `moonshot/kimi-k2.6` 转发 `thinking.keep`，并会从其他模型中移除它。

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "moonshot/kimi-k2.6": {          params: {            thinking: { type: "enabled", keep: "all" },          },        },      },    },  },}
[/code]

工具调用 ID 清理

Moonshot Kimi 提供的 tool_call ID 形如 `functions.<name>:<index>`。OpenClaw 会原样保留它们，因此多轮工具调用可以继续正常工作。

若要在自定义 OpenAI 兼容提供商上强制严格清理，请设置 `sanitizeToolCallIds: true`：

json5Copy code
[code]
    {  models: {    providers: {      "my-kimi-proxy": {        api: "openai-completions",        sanitizeToolCallIds: true,      },    },  },}
[/code]

流式用量兼容性

原生 Moonshot 端点（`https://api.moonshot.ai/v1` 和 `https://api.moonshot.cn/v1`）会在共享的 `openai-completions` 传输协议上声明流式用量兼容性。OpenClaw 会基于端点 能力启用该行为，因此面向相同原生 Moonshot 主机的兼容自定义提供商 ID 会继承相同的流式用量行为。

使用内置 K2.6 定价时，包含输入、输出 和缓存读取 token 的流式用量也会转换为本地估算的美元费用，用于 `/status`、`/usage full`、`/usage cost`，以及基于转录记录的会话 计费。

Endpoint and model ref reference 提供商 | 模型引用前缀 | 端点 | 认证环境变量  
---|---|---|---  
Moonshot | `moonshot/` | `https://api.moonshot.ai/v1` | `MOONSHOT_API_KEY`  
Moonshot CN | `moonshot/` | `https://api.moonshot.cn/v1` | `MOONSHOT_API_KEY`  
Kimi Coding | `kimi/` | Kimi Coding 端点 | `KIMI_API_KEY`  
Web 搜索 | N/A | 与 Moonshot API 区域相同 | `KIMI_API_KEY` 或 `MOONSHOT_API_KEY`  
  
  * Kimi Web 搜索使用 `KIMI_API_KEY` 或 `MOONSHOT_API_KEY`，并默认使用 `https://api.moonshot.ai/v1` 和模型 `kimi-k2.6`。
  * 如有需要，可在 `models.providers` 中覆盖定价和上下文元数据。
  * 如果 Moonshot 为某个模型发布了不同的上下文限制，请相应调整 `contextWindow`。


## 相关

[**Model selection** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**Web search** 配置包括 Kimi 在内的 Web 搜索提供商。 ](</zh-CN/tools/web>) [**Configuration reference** 提供商、模型和插件的完整配置架构。 ](</zh-CN/gateway/configuration-reference>) [**Moonshot Open Platform** Moonshot API 密钥管理和文档。 ](<https://platform.moonshot.ai>)

Was this useful?YesNo