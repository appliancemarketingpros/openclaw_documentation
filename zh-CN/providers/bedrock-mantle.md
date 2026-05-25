---
title: Amazon Bedrock Mantle
source_url: https://docs.openclaw.ai/zh-CN/providers/bedrock-mantle
scraped_at: 2026-05-25
---

OpenClaw 包含一个内置的 **Amazon Bedrock Mantle** 提供商，用于连接到 Mantle 的 OpenAI 兼容端点。Mantle 通过由 Bedrock 基础设施支持的标准 `/v1/chat/completions` 表面托管开源和第三方模型（GPT-OSS、Qwen、Kimi、GLM 及类似模型）。

属性 | 值  
---|---  
提供商 ID | `amazon-bedrock-mantle`  
API | `openai-completions`（OpenAI 兼容）或 `anthropic-messages`（Anthropic Messages 路由）  
认证 | 显式 `AWS_BEARER_TOKEN_BEDROCK` 或 IAM 凭证链 bearer-token 生成  
默认区域 | `us-east-1`（用 `AWS_REGION` 或 `AWS_DEFAULT_REGION` 覆盖）  
  
## 入门指南

选择你偏好的认证方式并按照设置步骤操作。

### 显式 bearer token

**最适合：** 已经有 Mantle bearer token 的环境。

* ### 在 Gateway 网关主机上设置 bearer token

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

可以选择设置区域（默认为 `us-east-1`）：

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### 验证模型已被发现

bashCopy code
[code]
    openclaw models list
[/code]

发现的模型会出现在 `amazon-bedrock-mantle` 提供商下。除非你想覆盖默认值， 否则无需额外配置。

### IAM 凭证

**最适合：** 使用 AWS SDK 兼容凭证（共享配置、SSO、Web 身份、实例或任务角色）。

* ### 在 Gateway 网关主机上配置 AWS 凭证

任何 AWS SDK 兼容认证源都可使用：

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### 验证模型已被发现

bashCopy code
[code]
    openclaw models list
[/code]

OpenClaw 会自动从凭证链生成 Mantle bearer token。

## 自动模型发现

设置 `AWS_BEARER_TOKEN_BEDROCK` 时，OpenClaw 会直接使用它。否则， OpenClaw 会尝试从 AWS 默认凭证链生成 Mantle bearer token。随后，它会通过查询该区域的 `/v1/models` 端点来发现可用的 Mantle 模型。

行为 | 详情  
---|---  
发现缓存 | 结果缓存 1 小时  
IAM token 刷新 | 每小时  
  
要保持 Mantle 插件启用，但禁止自动发现和 IAM bearer-token 生成，请禁用插件拥有的发现开关：

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### 支持的区域

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## 手动配置

如果你更偏好显式配置而不是自动发现：

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## 高级配置

推理支持

推理支持会从包含类似 `thinking`、`reasoner` 或 `gpt-oss-120b` 的模式的模型 ID 推断出来。 OpenClaw 会在发现期间为匹配的模型自动设置 `reasoning: true`。

端点不可用

如果 Mantle 端点不可用或未返回任何模型，该提供商会被静默跳过。OpenClaw 不会报错； 其他已配置的提供商会继续正常工作。

通过 Anthropic Messages 路由使用 Claude Opus 4.7

Mantle 还暴露了一个 Anthropic Messages 路由，可通过相同的 bearer 认证流式路径承载 Claude 模型。Claude Opus 4.7（`amazon-bedrock-mantle/claude-opus-4.7`）可通过此路由调用，并使用提供商拥有的流式传输，因此 AWS bearer token 不会被当作 Anthropic API keys 处理。

当你在 Mantle 提供商上固定一个 Anthropic Messages 模型时，OpenClaw 会为该模型使用 `anthropic-messages` API 表面，而不是 `openai-completions`。认证仍来自 `AWS_BEARER_TOKEN_BEDROCK`（或签发的 IAM bearer token）。

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

与 Amazon Bedrock 提供商的关系

Bedrock Mantle 是不同于标准 [Amazon Bedrock](</zh-CN/providers/bedrock>) 提供商的单独提供商。Mantle 使用 OpenAI 兼容的 `/v1` 表面，而标准 Bedrock 提供商使用原生 Bedrock API。

两个提供商在存在 `AWS_BEARER_TOKEN_BEDROCK` 凭证时会共享同一个凭证。

## 相关内容

[**Amazon Bedrock** 面向 Anthropic Claude、Titan 和其他模型的原生 Bedrock 提供商。 ](</zh-CN/providers/bedrock>) [**模型选择** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**OAuth 和认证** 认证详情和凭证复用规则。 ](</zh-CN/gateway/authentication>) [**故障排除** 常见问题以及如何解决。 ](</zh-CN/help/troubleshooting>)

Was this useful?YesNo