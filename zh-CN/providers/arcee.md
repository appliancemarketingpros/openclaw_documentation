---
title: Arcee AI
source_url: https://docs.openclaw.ai/zh-CN/providers/arcee
scraped_at: 2026-05-25
---

[Arcee AI](<https://arcee.ai>) 通过 OpenAI 兼容 API 提供对 Trinity 混合专家模型系列的访问。所有 Trinity 模型均采用 Apache 2.0 许可证。

可以直接通过 Arcee 平台或通过 [OpenRouter](</zh-CN/providers/openrouter>) 访问 Arcee AI 模型。

属性 | 值  
---|---  
提供商 | `arcee`  
认证 | `ARCEEAI_API_KEY`（直接）或 `OPENROUTER_API_KEY`（通过 OpenRouter）  
API | OpenAI 兼容  
基础 URL | `https://api.arcee.ai/api/v1`（直接）或 `https://openrouter.ai/api/v1`（OpenRouter）  
  
## 入门指南

### 直接（Arcee 平台）

* ### 获取 API key

在 [Arcee AI](<https://chat.arcee.ai/>) 创建 API key。

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-api-key
[/code]

* ### 设置默认模型

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

### 通过 OpenRouter

* ### 获取 API key

在 [OpenRouter](<https://openrouter.ai/keys>) 创建 API key。

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard --auth-choice arceeai-openrouter
[/code]

* ### 设置默认模型

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "arcee/trinity-large-thinking" },    },  },}
[/code]

相同的模型引用同时适用于直接设置和 OpenRouter 设置（例如 `arcee/trinity-large-thinking`）。

## 非交互式设置

### 直接（Arcee 平台）

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-api-key \  --arceeai-api-key "$ARCEEAI_API_KEY"
[/code]

### 通过 OpenRouter

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice arceeai-openrouter \  --openrouter-api-key "$OPENROUTER_API_KEY"
[/code]

## 内置目录

OpenClaw 当前随附以下内置 Arcee 目录：

模型引用 | 名称 | 输入 | 上下文 | 成本（每 1M 输入/输出） | 备注  
---|---|---|---|---|---  
`arcee/trinity-large-thinking` | Trinity Large Thinking | text | 256K | $0.25 / $0.90 | 默认模型；已启用推理  
`arcee/trinity-large-preview` | Trinity Large Preview | text | 128K | $0.25 / $1.00 | 通用用途；400B 参数，13B 激活  
`arcee/trinity-mini` | Trinity Mini 26B | text | 128K | $0.045 / $0.15 | 快速且成本高效；函数调用  
  
## 支持的功能

功能 | 支持  
---|---  
流式传输 | 是  
工具使用 / 函数调用 | 是（Trinity Mini、Trinity Large Preview）  
结构化输出（JSON 模式和 JSON schema） | 是  
扩展思考 | 是（Trinity Large Thinking；工具已禁用）  
  
环境说明

如果 Gateway 网关作为守护进程运行（launchd/systemd），请确保 `ARCEEAI_API_KEY` （或 `OPENROUTER_API_KEY`）可供该进程使用（例如，在 `~/.openclaw/.env` 中或通过 `env.shellEnv`）。

OpenRouter 路由

通过 OpenRouter 使用 Arcee 模型时，同样适用 `arcee/*` 模型引用。 OpenClaw 会根据你的认证选择透明地处理路由。请参阅 [OpenRouter 提供商文档](</zh-CN/providers/openrouter>)，了解 OpenRouter 专用的 配置详情。

## 相关

[**OpenRouter** 通过一个 API key 访问 Arcee 模型以及许多其他模型。 ](</zh-CN/providers/openrouter>) [**模型选择** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>)

Was this useful?YesNo