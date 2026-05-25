---
title: OpenCode
source_url: https://docs.openclaw.ai/zh-CN/providers/opencode
scraped_at: 2026-05-25
---

OpenCode 在 OpenClaw 中提供两个托管目录：

目录 | 前缀 | 运行时提供商  
---|---|---  
**Zen** | `opencode/...` | `opencode`  
**Go** | `opencode-go/...` | `opencode-go`  
  
这两个目录使用同一个 OpenCode API 密钥。OpenClaw 会将运行时提供商 id 分开保留， 以确保上游按模型进行的路由保持正确，但新手引导和文档会将它们视为同一个 OpenCode 设置。

## 入门指南

### Zen 目录

**最适合：** 精选的 OpenCode 多模型代理（Claude、GPT、Gemini）。

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-zen
[/code]

或者直接传入密钥：

bashCopy code
[code]
    openclaw onboard --opencode-zen-api-key "$OPENCODE_API_KEY"
[/code]

* ### 将 Zen 模型设为默认值

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode/claude-opus-4-6"
[/code]

* ### 验证模型可用

bashCopy code
[code]
    openclaw models list --provider opencode
[/code]

### Go 目录

**最适合：** OpenCode 托管的 Kimi、GLM 和 MiniMax 阵容。

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

或者直接传入密钥：

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### 将 Go 模型设为默认值

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### 验证模型可用

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## 配置示例

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "opencode/claude-opus-4-6" } } },}
[/code]

## 内置目录

### Zen

属性 | 值  
---|---  
运行时提供商 | `opencode`  
示例模型 | `opencode/claude-opus-4-6`, `opencode/gpt-5.5`, `opencode/gemini-3-pro`  
  
### Go

属性 | 值  
---|---  
运行时提供商 | `opencode-go`  
示例模型 | `opencode-go/kimi-k2.6`, `opencode-go/glm-5`, `opencode-go/minimax-m2.5`  
  
## 高级配置

API 密钥别名

`OPENCODE_ZEN_API_KEY` 也支持作为 `OPENCODE_API_KEY` 的别名。

共享凭证

在设置期间输入一个 OpenCode 密钥后，会为两个运行时提供商都存储凭证。你不需要分别为每个目录进行新手引导。

计费和控制台

你需要登录 OpenCode，添加计费信息，并复制你的 API 密钥。计费和目录可用性都在 OpenCode 控制台中管理。

Gemini 重放行为

由 Gemini 支持的 OpenCode 引用会继续走代理 Gemini 路径，因此 OpenClaw 会在该路径上保留 Gemini thought-signature 清理，而不会启用原生 Gemini 重放验证或 bootstrap 重写。

非 Gemini 重放行为

非 Gemini 的 OpenCode 引用会保留最小化的 OpenAI 兼容重放策略。

## 相关内容

[**模型选择** 选择提供商、模型引用和故障切换行为。 ](</zh-CN/concepts/model-providers>) [**配置参考** 智能体、模型和提供商的完整配置参考。 ](</zh-CN/gateway/configuration-reference>)

Was this useful?YesNo