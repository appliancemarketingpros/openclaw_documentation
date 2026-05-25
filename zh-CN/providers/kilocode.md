---
title: Kilo Gateway 网关
source_url: https://docs.openclaw.ai/zh-CN/providers/kilocode
scraped_at: 2026-05-25
---

Kilo Gateway 提供一个**统一 API** ，可将请求路由到单个端点和 API key 背后的多个模型。它兼容 OpenAI，因此大多数 OpenAI SDK 只需切换基础 URL 即可使用。

属性 | 值  
---|---  
提供商 | `kilocode`  
凭证 | `KILOCODE_API_KEY`  
API | OpenAI 兼容  
基础 URL | `https://api.kilo.ai/api/gateway/`  
  
## 入门指南

* ### 创建账号

前往 [app.kilo.ai](<https://app.kilo.ai>)，登录或创建账号，然后导航到 API Keys 并生成一个新密钥。

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard --auth-choice kilocode-api-key
[/code]

或者直接设置环境变量：

bashCopy code
[code]
    export KILOCODE_API_KEY="<your-kilocode-api-key>" # pragma: allowlist secret
[/code]

* ### 验证模型可用

bashCopy code
[code]
    openclaw models list --provider kilocode
[/code]

## 默认模型

默认模型是 `kilocode/kilo/auto`，这是一个由提供商拥有并由 Kilo Gateway 管理的智能路由模型。

## 内置目录

OpenClaw 会在启动时从 Kilo Gateway 动态发现可用模型。使用 `/models kilocode` 查看你的账号可用的完整模型列表。

Gateway 网关上可用的任何模型都可以使用 `kilocode/` 前缀：

模型引用 | 说明  
---|---  
`kilocode/kilo/auto` | 默认 — 智能路由  
`kilocode/anthropic/claude-sonnet-4` | 通过 Kilo 使用 Anthropic  
`kilocode/openai/gpt-5.5` | 通过 Kilo 使用 OpenAI  
`kilocode/google/gemini-3.1-pro-preview` | 通过 Kilo 使用 Google  
...以及更多 | 使用 `/models kilocode` 列出全部  
  
## 配置示例

json5Copy code
[code]
    {  env: { KILOCODE_API_KEY: "<your-kilocode-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "kilocode/kilo/auto" },    },  },}
[/code]

传输协议和兼容性

Kilo Gateway 在源码中记录为兼容 OpenRouter，因此它会保留在代理风格的 OpenAI 兼容路径上，而不是使用原生 OpenAI 请求整形。

  * Gemini 后端的 Kilo 引用会保留在代理 Gemini 路径上，因此 OpenClaw 会继续在那里执行 Gemini 思维签名清理，而不会启用原生 Gemini 重放验证或引导重写。
  * Kilo Gateway 底层会使用带有你的 API key 的 Bearer token。

流包装器和推理

Kilo 的共享流包装器会添加提供商应用标头，并为受支持的具体模型引用规范化代理推理载荷。

故障排除

  * 如果启动时模型发现失败，OpenClaw 会回退到包含 `kilocode/kilo/auto` 的内置静态目录。
  * 确认你的 API key 有效，并且你的 Kilo 账号已启用所需模型。
  * 当 Gateway 网关以守护进程运行时，请确保 `KILOCODE_API_KEY` 可供该进程使用（例如在 `~/.openclaw/.env` 中，或通过 `env.shellEnv`）。


## 相关

[**模型选择** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**配置参考** 完整的 OpenClaw 配置参考。 ](</zh-CN/gateway/configuration-reference>) [**Kilo Gateway** Kilo Gateway 仪表板、API keys 和账号管理。 ](<https://app.kilo.ai>)

Was this useful?YesNo