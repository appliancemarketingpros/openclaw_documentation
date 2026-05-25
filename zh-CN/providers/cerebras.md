---
title: Cerebras
source_url: https://docs.openclaw.ai/zh-CN/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) 在定制推理硬件上提供高速、OpenAI 兼容的推理服务。OpenClaw 包含一个内置的 Cerebras provider 插件，并带有静态的四模型目录。

属性 | 值  
---|---  
提供商 ID | `cerebras`  
插件 | 内置，`enabledByDefault: true`  
认证环境变量 | `CEREBRAS_API_KEY`  
新手引导标志 | `--auth-choice cerebras-api-key`  
直接 CLI 标志 | `--cerebras-api-key <key>`  
API | OpenAI 兼容（`openai-completions`）  
基础 URL | `https://api.cerebras.ai/v1`  
默认模型 | `cerebras/zai-glm-4.7`  
  
## 入门指南

* ### 获取 API key

在 [Cerebras Cloud Console](<https://cloud.cerebras.ai>) 中创建 API key。

* ### 运行新手引导

OnboardingCopy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### 验证模型可用

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

列表应包含全部四个内置模型。如果 `CEREBRAS_API_KEY` 未解析，`openclaw models status --json` 会在 `auth.unusableProfiles` 下报告缺失的凭证。

## 非交互式设置

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## 内置目录

OpenClaw 随附一个静态 Cerebras 目录，镜像公共的 OpenAI 兼容端点。全部四个模型共享 128k 上下文和 8,192 个最大输出 token。

模型引用 | 名称 | 推理 | 备注  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | 是 | 默认模型；预览版推理模型  
`cerebras/gpt-oss-120b` | GPT OSS 120B | 是 | 生产级推理模型  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | 否 | 预览版非推理模型  
`cerebras/llama3.1-8b` | Llama 3.1 8B | 否 | 面向速度优化的生产级模型  
  
## 手动配置

内置插件通常意味着你只需要 API key。当你想覆盖模型元数据，或以 `mode: "merge"` 针对静态目录运行时，请使用显式的 `models.providers.cerebras` 配置：

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## 相关内容

[**模型提供商** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**思考模式** 两个支持推理的 Cerebras 模型的推理强度等级。 ](</zh-CN/tools/thinking>) [**配置参考** Agent 默认值和模型配置。 ](</zh-CN/gateway/config-agents#agent-defaults>) [**Models 常见问题** 认证配置文件、切换模型以及解决 “no profile” 错误。 ](</zh-CN/help/faq-models>)

Was this useful?YesNo