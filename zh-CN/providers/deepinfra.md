---
title: DeepInfra
source_url: https://docs.openclaw.ai/zh-CN/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra 提供一个**统一 API** ，可通过单一端点和 API key 将请求路由到最热门的开源模型和前沿模型。它兼容 OpenAI，因此大多数 OpenAI SDK 只需切换 base URL 即可使用。

## 获取 API key

  1. 前往 <https://deepinfra.com/>
  2. 登录或创建账户
  3. 导航到 Dashboard / Keys，生成新的 API key，或使用自动创建的 API key


## CLI 设置

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

或设置环境变量：

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## 配置片段

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## 支持的 OpenClaw 表面

内置插件会注册所有符合当前 OpenClaw 提供商契约的 DeepInfra 表面：

表面 | 默认模型 | OpenClaw 配置/工具  
---|---|---  
Chat / 模型提供商 | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
图像生成/编辑 | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
媒体理解 | `moonshotai/Kimi-K2.5` 用于图像 | 入站图像理解  
语音转文本 | `openai/whisper-large-v3-turbo` | 入站音频转写  
文本转语音 | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
视频生成 | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
记忆嵌入 | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra 还公开重排序、分类、对象检测和其他原生模型类型。OpenClaw 目前还没有针对这些类别的一等提供商契约，因此此插件尚未注册它们。

## 可用模型

OpenClaw 会在启动时动态发现可用的 DeepInfra 模型。使用 `/models deepinfra` 查看完整的可用模型列表。

[DeepInfra.com](<https://deepinfra.com/>) 上的任何可用模型都可以配合 `deepinfra/` 前缀使用：

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...以及更多模型
[/code]

## 备注

  * 模型引用为 `deepinfra/<provider>/<model>`（例如 `deepinfra/Qwen/Qwen3-Max`）。
  * 默认模型：`deepinfra/deepseek-ai/DeepSeek-V3.2`
  * Base URL：`https://api.deepinfra.com/v1/openai`
  * 原生视频生成使用 `https://api.deepinfra.com/v1/inference/<model>`。


## 相关

  * [模型提供商](</zh-CN/concepts/model-providers>)
  * [所有提供商](</zh-CN/providers>)


Was this useful?YesNo