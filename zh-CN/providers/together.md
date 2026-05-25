---
title: Together AI
source_url: https://docs.openclaw.ai/zh-CN/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) 通过统一的 API 提供对领先开源模型的访问，包括 Llama、DeepSeek、Kimi 等。

属性 | 值  
---|---  
提供商 | `together`  
凭证 | `TOGETHER_API_KEY`  
API | OpenAI 兼容  
基础 URL | `https://api.together.xyz/v1`  
  
## 入门指南

* ### 获取 API 密钥

在 [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>) 创建 API 密钥。

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### 设置默认模型

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### 非交互式示例

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## 内置目录

OpenClaw 随附此内置 Together 目录：

模型引用 | 名称 | 输入 | 上下文 | 说明  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | 文本、图像 | 262,144 | 默认模型；已启用推理  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | 文本 | 202,752 | 通用文本模型  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | 文本 | 131,072 | 快速指令模型  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | 文本、图像 | 10,000,000 | 多模态  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | 文本、图像 | 20,000,000 | 多模态  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | 文本 | 131,072 | 通用文本模型  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | 文本 | 131,072 | 推理模型  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | 文本 | 262,144 | 辅助 Kimi 文本模型  
  
## 视频生成

内置 `together` 插件还会通过共享的 `video_generate` 工具注册视频生成能力。

属性 | 值  
---|---  
默认视频模型 | `together/Wan-AI/Wan2.2-T2V-A14B`  
模式 | 文本转视频、单图参考  
支持的参数 | `aspectRatio`, `resolution`  
  
要将 Together 用作默认视频提供商：

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

环境说明

如果 Gateway 网关 作为守护进程（launchd/systemd）运行，请确保 `TOGETHER_API_KEY` 可供该进程使用（例如在 `~/.openclaw/.env` 中，或通过 `env.shellEnv`）。

故障排除

  * 验证你的密钥可用：`openclaw models list --provider together`
  * 如果模型没有出现，请确认 API 密钥已在你的 Gateway 网关进程所用的正确环境中设置。
  * 模型引用使用 `together/<model-id>` 形式。


## 相关内容

[**模型选择** 提供商规则、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**视频生成** 共享视频生成工具参数和提供商选择。 ](</zh-CN/tools/video-generation>) [**配置参考** 完整配置 schema，包括提供商设置。 ](</zh-CN/gateway/configuration-reference>) [**Together AI** Together AI 仪表板、API 文档和定价。 ](<https://together.ai>)

Was this useful?YesNo