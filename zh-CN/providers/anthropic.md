---
title: Anthropic
source_url: https://docs.openclaw.ai/zh-CN/providers/anthropic
scraped_at: 2026-05-25
---

Anthropic 构建 **Claude** 模型系列。OpenClaw 支持两种认证路径：

  * **API 密钥** — 使用基于用量计费的 Anthropic API 直接访问（`anthropic/*` 模型）
  * **Claude CLI** — 在同一主机上复用已有的 Claude CLI 登录


## 入门指南

### API 密钥

**最适合：** 标准 API 访问和基于用量的计费。

* ### 获取你的 API 密钥

在 [Anthropic Console](<https://console.anthropic.com/>) 中创建 API 密钥。

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard# choose: Anthropic API key
[/code]

或者直接传入密钥：

bashCopy code
[code]
    openclaw onboard --anthropic-api-key "$ANTHROPIC_API_KEY"
[/code]

* ### 验证模型可用

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### 配置示例

json5Copy code
[code]
    {  env: { ANTHROPIC_API_KEY: "sk-ant-..." },  agents: { defaults: { model: { primary: "anthropic/claude-opus-4-6" } } },}
[/code]

### Claude CLI

**最适合：** 在没有单独 API 密钥的情况下复用已有的 Claude CLI 登录。

* ### 确认 Claude CLI 已安装并已登录

使用以下命令验证：

bashCopy code
[code]
    claude --version
[/code]

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard# choose: Claude CLI
[/code]

OpenClaw 会检测并复用现有 Claude CLI 凭证。

* ### 验证模型可用

bashCopy code
[code]
    openclaw models list --provider anthropic
[/code]

### 配置示例

推荐使用规范的 Anthropic 模型引用，并加上 CLI 运行时覆盖：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-7" },      models: {        "anthropic/claude-opus-4-7": {          agentRuntime: { id: "claude-cli" },        },      },    },  },}
[/code]

旧版 `claude-cli/claude-opus-4-7` 模型引用仍可用于 兼容性，但新配置应将提供商/模型选择保留为 `anthropic/*`，并将执行后端放在提供商/模型运行时策略中。

## 思考默认值（Claude 4.6）

当未设置显式思考级别时，Claude 4.6 模型在 OpenClaw 中默认使用 `adaptive` 思考。

可用 `/think:<level>` 按消息覆盖，或在模型参数中覆盖：

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { thinking: "adaptive" },        },      },    },  },}
[/code]

## 提示词缓存

OpenClaw 对 API 密钥认证支持 Anthropic 的提示词缓存功能。

值 | 缓存时长 | 描述  
---|---|---  
`"short"`（默认） | 5 分钟 | 对 API 密钥认证自动应用  
`"long"` | 1 小时 | 扩展缓存  
`"none"` | 不缓存 | 禁用提示词缓存  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },  },}
[/code]

按智能体覆盖缓存

使用模型级参数作为基线，然后通过 `agents.list[].params` 覆盖特定智能体：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "anthropic/claude-opus-4-6" },      models: {        "anthropic/claude-opus-4-6": {          params: { cacheRetention: "long" },        },      },    },    list: [      { id: "research", default: true },      { id: "alerts", params: { cacheRetention: "none" } },    ],  },}
[/code]

配置合并顺序：

  1. `agents.defaults.models["provider/model"].params`
  2. `agents.list[].params`（匹配 `id`，按键覆盖）


这允许一个智能体保持长期缓存，同时让同一模型上的另一个智能体为突发性/低复用流量禁用缓存。

Bedrock Claude 注意事项

  * Bedrock 上的 Anthropic Claude 模型（`amazon-bedrock/*anthropic.claude*`）在配置后接受 `cacheRetention` 透传。
  * 非 Anthropic 的 Bedrock 模型会在运行时被强制设为 `cacheRetention: "none"`。
  * 当未设置显式值时，API 密钥智能默认值也会为 Claude-on-Bedrock 引用填入 `cacheRetention: "short"`。


## 高级配置

快速模式

OpenClaw 的共享 `/fast` 开关支持 Anthropic 直连流量（API 密钥和 OAuth 到 `api.anthropic.com`）。

命令 | 映射到  
---|---  
`/fast on` | `service_tier: "auto"`  
`/fast off` | `service_tier: "standard_only"`  
json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-sonnet-4-6": {          params: { fastMode: true },        },      },    },  },}
[/code]

媒体理解（图像和 PDF）

内置 Anthropic 插件会注册图像和 PDF 理解。OpenClaw 会根据配置的 Anthropic 认证自动解析媒体能力，无需 额外配置。

属性 | 值  
---|---  
默认模型 | `claude-opus-4-7`  
支持的输入 | 图像、PDF 文档  
  
当图像或 PDF 附加到对话时，OpenClaw 会自动 通过 Anthropic 媒体理解提供商进行路由。

1M 上下文窗口（beta）

Anthropic 的 1M 上下文窗口受 beta 门控。按模型启用：

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "anthropic/claude-opus-4-6": {          params: { context1m: true },        },      },    },  },}
[/code]

OpenClaw 会在请求上将其映射为 `anthropic-beta: context-1m-2025-08-07`。

`params.context1m: true` 也适用于符合条件的 Opus 和 Sonnet 模型的 Claude CLI 后端 （`claude-cli/*`），将这些 CLI 会话的运行时 上下文窗口扩展到与直连 API 行为一致。

Claude Opus 4.7 1M 上下文

`anthropic/claude-opus-4.7` 及其 `claude-cli` 变体默认具有 1M 上下文 窗口，无需 `params.context1m: true`。

## 故障排除

401 错误 / 令牌突然无效

Anthropic 令牌认证会过期，也可能被撤销。对于新设置，请改用 Anthropic API 密钥。

未找到提供商 "anthropic" 的 API 密钥

Anthropic 认证是**按智能体** 配置的，新智能体不会继承主智能体的密钥。为该智能体重新运行新手引导（或在 Gateway 网关主机上配置 API 密钥），然后用 `openclaw models status` 验证。

未找到配置文件 "anthropic:default" 的凭证

运行 `openclaw models status` 查看当前活动的认证配置文件。重新运行新手引导，或为该配置文件路径配置 API 密钥。

没有可用的认证配置文件（全部处于冷却中）

检查 `openclaw models status --json` 中的 `auth.unusableProfiles`。Anthropic 速率限制冷却可能按模型限定，因此同级 Anthropic 模型可能仍可使用。添加另一个 Anthropic 配置文件，或等待冷却结束。

## 相关内容

[**模型选择** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**CLI 后端** Claude CLI 后端设置和运行时细节。 ](</zh-CN/gateway/cli-backends>) [**提示词缓存** 提示词缓存在不同提供商之间的工作方式。 ](</zh-CN/reference/prompt-caching>) [**OAuth 和认证** 认证细节和凭证复用规则。 ](</zh-CN/gateway/authentication>)

Was this useful?YesNo