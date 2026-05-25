---
title: 火山引擎（Doubao）
source_url: https://docs.openclaw.ai/zh-CN/providers/volcengine
scraped_at: 2026-05-25
---

Volcengine 提供商可访问托管在火山引擎上的 Doubao 模型和第三方模型，并为通用工作负载和编码工作负载提供独立端点。同一个内置插件还可以将 Volcengine Speech 注册为 TTS 提供商。

详情 | 值  
---|---  
提供商 | `volcengine`（通用 + TTS）+ `volcengine-plan`（编码）  
模型凭证 | `VOLCANO_ENGINE_API_KEY`  
TTS 凭证 | `VOLCENGINE_TTS_API_KEY` 或 `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | 与 OpenAI 兼容的模型，BytePlus Seed Speech TTS  
  
## 入门指南

* ### 设置 API 密钥

运行交互式新手引导：

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

这会使用同一个 API 密钥同时注册通用提供商（`volcengine`）和编码提供商（`volcengine-plan`）。

* ### 设置默认模型

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### 验证模型可用

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## 提供商和端点

提供商 | 端点 | 用例  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | 通用模型  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | 编码模型  
  
## 内置目录

### 通用（volcengine）

模型引用 | 名称 | 输入 | 上下文  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | 文本、图像 | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | 文本、图像 | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | 文本、图像 | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | 文本、图像 | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | 文本、图像 | 128,000  
  
### 编码（volcengine-plan）

模型引用 | 名称 | 输入 | 上下文  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | 文本 | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | 文本 | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | 文本 | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | 文本 | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | 文本 | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | 文本 | 256,000  
  
## 文本转语音

Volcengine TTS 使用 BytePlus Seed Speech HTTP API，并且与兼容 OpenAI 的 Doubao 模型 API 密钥分开配置。在 BytePlus 控制台中，打开 Seed Speech > Settings > API Keys，复制 API 密钥，然后设置：

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

然后在 `openclaw.json` 中启用它：

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

对于语音便笺目标，OpenClaw 会向 Volcengine 请求提供商原生的 `ogg_opus`。对于普通音频附件，则会请求 `mp3`。提供商别名 `bytedance` 和 `doubao` 也会解析到同一个语音提供商。

默认资源 ID 是 `seed-tts-1.0`，因为 BytePlus 会将它授予默认项目中新创建的 Seed Speech API 密钥。如果你的项目具有 TTS 2.0 权限，请设置 `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`。

旧版 AppID/token 凭证方式仍然支持较早的 Speech Console 应用：

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## 高级配置

新手引导后的默认模型

`openclaw onboard --auth-choice volcengine-api-key` 目前会将 `volcengine-plan/ark-code-latest` 设置为默认模型，同时也会注册通用的 `volcengine` 目录。

模型选择器回退行为

在新手引导/配置模型选择期间，Volcengine 凭证选项会优先选择 `volcengine/*` 和 `volcengine-plan/*` 两类条目。如果这些模型尚未加载， OpenClaw 会回退到未筛选的目录，而不是显示一个空的按提供商范围筛选的选择器。

守护进程的环境变量

如果 Gateway 网关 以守护进程方式运行（launchd/systemd），请确保模型和 TTS 环境变量（如 `VOLCANO_ENGINE_API_KEY`、`VOLCENGINE_TTS_API_KEY`、 `BYTEPLUS_SEED_SPEECH_API_KEY`、`VOLCENGINE_TTS_APPID` 和 `VOLCENGINE_TTS_TOKEN`）对该进程可用（例如在 `~/.openclaw/.env` 中，或通过 `env.shellEnv` 提供）。

## 相关内容

[**模型选择** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**配置** 智能体、模型和提供商的完整配置参考。 ](</zh-CN/gateway/configuration>) [**故障排除** 常见问题和调试步骤。 ](</zh-CN/help/troubleshooting>) [**常见问题** 关于 OpenClaw 设置的常见问题解答。 ](</zh-CN/help/faq>)

Was this useful?YesNo