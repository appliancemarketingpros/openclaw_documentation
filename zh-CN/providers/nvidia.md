---
title: NVIDIA
source_url: https://docs.openclaw.ai/zh-CN/providers/nvidia
scraped_at: 2026-05-25
---

NVIDIA 在 `https://integrate.api.nvidia.com/v1` 提供 OpenAI 兼容 API，可免费使用开放模型。使用来自 [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>) 的 API key 进行身份验证。

## 入门指南

* ### 获取你的 API key

在 [build.nvidia.com](<https://build.nvidia.com/settings/api-keys>) 创建 API key。

* ### 导出密钥并运行新手引导

bashCopy code
[code]
    export NVIDIA_API_KEY="nvapi-..."openclaw onboard --auth-choice nvidia-api-key
[/code]

* ### 设置 NVIDIA 模型

bashCopy code
[code]
    openclaw models set nvidia/nvidia/nemotron-3-super-120b-a12b
[/code]

对于非交互式设置，你也可以直接传入密钥：

bashCopy code
[code]
    openclaw onboard --auth-choice nvidia-api-key --nvidia-api-key "nvapi-..."
[/code]

## 配置示例

json5Copy code
[code]
    {  env: { NVIDIA_API_KEY: "nvapi-..." },  models: {    providers: {      nvidia: {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",      },    },  },  agents: {    defaults: {      model: { primary: "nvidia/nvidia/nemotron-3-super-120b-a12b" },    },  },}
[/code]

## 内置目录

模型引用 | 名称 | 上下文 | 最大输出  
---|---|---|---  
`nvidia/nvidia/nemotron-3-super-120b-a12b` | NVIDIA Nemotron 3 Super 120B | 262,144 | 8,192  
`nvidia/moonshotai/kimi-k2.5` | Kimi K2.5 | 262,144 | 8,192  
`nvidia/minimaxai/minimax-m2.5` | Minimax M2.5 | 196,608 | 8,192  
`nvidia/z-ai/glm5` | GLM 5 | 202,752 | 8,192  
  
## 高级配置

自动启用行为

设置 `NVIDIA_API_KEY` 环境变量后，提供商会自动启用。除了该密钥之外，不需要显式提供商配置。

目录和定价

内置目录是静态的。由于 NVIDIA 目前为列出的模型提供免费 API 访问，源代码中的费用默认值为 `0`。

OpenAI 兼容端点

NVIDIA 使用标准的 `/v1` completions 端点。任何 OpenAI 兼容工具都应能与 NVIDIA base URL 开箱即用地配合使用。

较慢的自定义提供商响应

一些由 NVIDIA 托管的自定义模型在发出首个响应分块之前，可能会比默认模型空闲看门狗等待更长时间。对于自定义 NVIDIA 提供商条目，请提高提供商超时时间，而不是提高整个智能体运行时超时时间：

json5Copy code
[code]
    {  models: {    providers: {      "custom-integrate-api-nvidia-com": {        baseUrl: "https://integrate.api.nvidia.com/v1",        api: "openai-completions",        apiKey: "NVIDIA_API_KEY",        timeoutSeconds: 300,      },    },  },  agents: {    defaults: {      models: {        "custom-integrate-api-nvidia-com/meta/llama-3.1-70b-instruct": {          params: { thinking: "off" },        },      },    },  },}
[/code]

## 相关内容

[**模型选择** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**配置参考** 智能体、模型和提供商的完整配置参考。 ](</zh-CN/gateway/configuration-reference>)

Was this useful?YesNo