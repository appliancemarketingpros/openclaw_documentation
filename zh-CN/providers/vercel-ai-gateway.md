---
title: Vercel AI 网关
source_url: https://docs.openclaw.ai/zh-CN/providers/vercel-ai-gateway
scraped_at: 2026-05-25
---

[Vercel AI Gateway](<https://vercel.com/ai-gateway>) 提供统一 API，可通过单一端点访问数百个模型。

属性 | 值  
---|---  
提供商 | `vercel-ai-gateway`  
认证 | `AI_GATEWAY_API_KEY`  
API | 兼容 Anthropic Messages  
模型目录 | 通过 `/v1/models` 自动发现  
  
## 入门指南

* ### 设置 API 密钥

运行新手引导并选择 AI Gateway 认证选项：

bashCopy code
[code]
    openclaw onboard --auth-choice ai-gateway-api-key
[/code]

* ### 设置默认模型

将模型添加到你的 OpenClaw 配置：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vercel-ai-gateway/anthropic/claude-opus-4.6" },    },  },}
[/code]

* ### 验证模型可用

bashCopy code
[code]
    openclaw models list --provider vercel-ai-gateway
[/code]

## 非交互示例

对于脚本化或 CI 设置，请在命令行传入所有值：

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice ai-gateway-api-key \  --ai-gateway-api-key "$AI_GATEWAY_API_KEY"
[/code]

## 模型 ID 简写

OpenClaw 接受 Vercel Claude 简写模型引用，并会在运行时将其规范化：

简写输入 | 规范化后的模型引用  
---|---  
`vercel-ai-gateway/claude-opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4.6`  
`vercel-ai-gateway/opus-4.6` | `vercel-ai-gateway/anthropic/claude-opus-4-6`  
  
## 高级配置

守护进程的环境变量

如果 OpenClaw Gateway 网关作为守护进程（launchd/systemd）运行，请确保 `AI_GATEWAY_API_KEY` 可供该进程使用。

提供商路由

Vercel AI Gateway 会根据模型引用前缀将请求路由到上游提供商。例如， `vercel-ai-gateway/anthropic/claude-opus-4.6` 会通过 Anthropic 路由， 而 `vercel-ai-gateway/openai/gpt-5.5` 会通过 OpenAI 路由， `vercel-ai-gateway/moonshotai/kimi-k2.6` 会通过 MoonshotAI 路由。 你的单个 `AI_GATEWAY_API_KEY` 会处理所有上游提供商的认证。

思考级别

当 OpenClaw 了解上游提供商契约时，`/think` 选项会遵循可信的上游模型前缀。 `vercel-ai-gateway/anthropic/...` 使用 Claude 思考配置，包括 Claude 4.6 模型的自适应默认值。 `vercel-ai-gateway/openai/gpt-5.4`、`gpt-5.5` 和 Codex 风格的引用会像直接的 OpenAI/OpenAI Codex 提供商一样暴露 `/think xhigh`。其他带命名空间的引用会保留普通推理级别，除非其目录元数据声明了更多级别。

## 相关内容

[**模型选择** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**故障排除** 常规故障排除和常见问题。 ](</zh-CN/help/troubleshooting>)

Was this useful?YesNo