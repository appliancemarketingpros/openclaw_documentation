---
title: xAI
source_url: https://docs.openclaw.ai/zh-CN/providers/xai
scraped_at: 2026-05-25
---

OpenClaw 随附一个用于 Grok 模型的 `xai` 提供商插件。

## 入门指南

* ### 创建 API 密钥

在 [xAI 控制台](<https://console.x.ai/>)中创建 API 密钥。

* ### 设置你的 API 密钥

设置 `XAI_API_KEY`，或运行：

bashCopy code
[code]
    openclaw onboard --auth-choice xai-api-key
[/code]

* ### 选择模型

json5Copy code
[code]
    {  agents: { defaults: { model: { primary: "xai/grok-4.3" } } },}
[/code]

## 内置目录

OpenClaw 开箱即用地包含这些 xAI 模型系列：

系列 | 模型 ID  
---|---  
Grok 3 | `grok-3`, `grok-3-fast`, `grok-3-mini`, `grok-3-mini-fast`  
Grok 4.3 | `grok-4.3`  
Grok 4 | `grok-4`, `grok-4-0709`  
Grok 4 Fast | `grok-4-fast`, `grok-4-fast-non-reasoning`  
Grok 4.1 Fast | `grok-4-1-fast`, `grok-4-1-fast-non-reasoning`  
Grok 4.20 Beta | `grok-4.20-beta-latest-reasoning`, `grok-4.20-beta-latest-non-reasoning`  
Grok Code | `grok-code-fast-1`  
  
当更新的 `grok-4*` 和 `grok-code-fast*` ID 遵循相同 API 形态时，该插件也会前向解析它们。

## OpenClaw 功能覆盖范围

内置插件将 xAI 当前公开 API 表面映射到 OpenClaw 的共享提供商和工具合约。 不适合共享合约的能力（例如流式 TTS 和实时语音）不会暴露；请见下表。

xAI 能力 | OpenClaw 表面 | Status  
---|---|---  
Chat / Responses | `xai/<model>` 模型提供商 | 是  
服务器端 Web 搜索 | `web_search` 提供商 `grok` | 是  
服务器端 X 搜索 | `x_search` 工具 | 是  
服务器端代码执行 | `code_execution` 工具 | 是  
图像 | `image_generate` | 是  
视频 | `video_generate` | 是  
批量文字转语音 | `messages.tts.provider: "xai"` / `tts` | 是  
流式 TTS | - | 未暴露；OpenClaw 的 TTS 合约返回完整音频缓冲区  
批量语音转文字 | `tools.media.audio` / 媒体理解 | 是  
流式语音转文字 | 语音通话 `streaming.provider: "xai"` | 是  
实时语音 | - | 尚未暴露；需要不同的会话 / WebSocket 合约  
文件 / 批处理 | 仅通用模型 API 兼容性 | 不是 OpenClaw 一等工具  
  
### 快速模式映射

`/fast on` 或 `agents.defaults.models["xai/<model>"].params.fastMode: true` 会按如下方式改写原生 xAI 请求：

源模型 | 快速模式目标  
---|---  
`grok-3` | `grok-3-fast`  
`grok-3-mini` | `grok-3-mini-fast`  
`grok-4` | `grok-4-fast`  
`grok-4-0709` | `grok-4-fast`  
  
### 旧版兼容别名

旧版别名仍会规范化为规范内置 ID：

旧版别名 | 规范 ID  
---|---  
`grok-4-fast-reasoning` | `grok-4-fast`  
`grok-4-1-fast-reasoning` | `grok-4-1-fast`  
`grok-4.20-reasoning` | `grok-4.20-beta-latest-reasoning`  
`grok-4.20-non-reasoning` | `grok-4.20-beta-latest-non-reasoning`  
  
## 功能

Web 搜索

内置 `grok` Web 搜索提供商可以使用 `XAI_API_KEY` 或插件 Web 搜索密钥：

bashCopy code
[code]
    openclaw config set tools.web.search.provider grok
[/code]

视频生成

内置 `xai` 插件通过共享 `video_generate` 工具注册视频生成。

  * 默认视频模型：`xai/grok-imagine-video`
  * 模式：文本到视频、图像到视频、参考图像生成、远程视频编辑和远程视频扩展
  * 宽高比：`1:1`、`16:9`、`9:16`、`4:3`、`3:4`、`3:2`、`2:3`
  * 分辨率：`480P`、`720P`
  * 时长：生成 / 图像到视频为 1-15 秒，使用 `reference_image` 角色时为 1-10 秒，扩展为 2-10 秒
  * 参考图像生成：为每张提供的图像将 `imageRoles` 设置为 `reference_image`；xAI 最多接受 7 张这样的图像


要将 xAI 用作默认视频提供商：

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "xai/grok-imagine-video",      },    },  },}
[/code]

图像生成

内置 `xai` 插件通过共享 `image_generate` 工具注册图像生成。

  * 默认图像模型：`xai/grok-imagine-image`
  * 附加模型：`xai/grok-imagine-image-pro`
  * 模式：文本到图像和参考图像编辑
  * 参考输入：一个 `image` 或最多五个 `images`
  * 宽高比：`1:1`、`16:9`、`9:16`、`4:3`、`3:4`、`2:3`、`3:2`
  * 分辨率：`1K`、`2K`
  * 数量：最多 4 张图像


OpenClaw 请求 xAI 返回 `b64_json` 图像响应，以便生成的媒体可以通过常规渠道附件路径存储和交付。 本地参考图像会转换为 data URL；远程 `http(s)` 引用会直接传递。

要将 xAI 用作默认图像提供商：

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "xai/grok-imagine-image",      },    },  },}
[/code]

文字转语音

内置 `xai` 插件通过共享 `tts` 提供商表面注册文字转语音。

  * 语音：`eve`、`ara`、`rex`、`sal`、`leo`、`una`
  * 默认语音：`eve`
  * 格式：`mp3`、`wav`、`pcm`、`mulaw`、`alaw`
  * 语言：BCP-47 代码或 `auto`
  * 速度：提供商原生速度覆盖
  * 不支持原生 Opus 语音便笺格式


要将 xAI 用作默认 TTS 提供商：

json5Copy code
[code]
    {  messages: {    tts: {      provider: "xai",      providers: {        xai: {          voiceId: "eve",        },      },    },  },}
[/code]

语音转文字

内置 `xai` 插件通过 OpenClaw 的媒体理解转录表面注册批量语音转文字。

  * 默认模型：`grok-stt`
  * 端点：xAI REST `/v1/stt`
  * 输入路径：multipart 音频文件上传
  * 在 OpenClaw 中，只要入站音频转录使用 `tools.media.audio` 就支持，包括 Discord 语音频道片段和渠道音频附件


要强制将 xAI 用于入站音频转录：

json5Copy code
[code]
    {  tools: {    media: {      audio: {        models: [          {            type: "provider",            provider: "xai",            model: "grok-stt",          },        ],      },    },  },}
[/code]

可以通过共享音频媒体配置或逐次调用的转录请求提供语言。共享 OpenClaw 表面会接受提示词提示，但 xAI REST STT 集成只会转发文件、模型和语言， 因为这些可以清晰映射到当前公开的 xAI 端点。

流式语音转文字

内置 `xai` 插件还为实时语音通话音频注册实时转录提供商。

  * 端点：xAI WebSocket `wss://api.x.ai/v1/stt`
  * 默认编码：`mulaw`
  * 默认采样率：`8000`
  * 默认端点检测：`800ms`
  * 中间转录：默认启用


语音通话的 Twilio 媒体流会发送 G.711 µ-law 音频帧，因此 xAI 提供商可以直接转发这些帧，无需转码：

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "xai",            providers: {              xai: {                apiKey: "${XAI_API_KEY}",                endpointingMs: 800,                language: "en",              },            },          },        },      },    },  },}
[/code]

提供商拥有的配置位于 `plugins.entries.voice-call.config.streaming.providers.xai`。支持的 键包括 `apiKey`、`baseUrl`、`sampleRate`、`encoding`（`pcm`、`mulaw` 或 `alaw`）、`interimResults`、`endpointingMs` 和 `language`。

x_search 配置

内置 xAI 插件将 `x_search` 作为 OpenClaw 工具暴露，用于通过 Grok 搜索 X（原 Twitter）内容。

配置路径：`plugins.entries.xai.config.xSearch`

键 | 类型 | 默认值 | 说明  
---|---|---|---  
`enabled` | boolean | - | 启用或禁用 x_search  
`model` | string | `grok-4-1-fast` | 用于 x_search 请求的模型  
`baseUrl` | string | - | xAI Responses 基础 URL 覆盖值  
`inlineCitations` | boolean | - | 在结果中包含内联引用  
`maxTurns` | number | - | 最大对话轮次  
`timeoutSeconds` | number | - | 请求超时时间（秒）  
`cacheTtlMinutes` | number | - | 缓存生存时间（分钟）  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          xSearch: {            enabled: true,            model: "grok-4-1-fast",            baseUrl: "https://api.x.ai/v1",            inlineCitations: true,          },        },      },    },  },}
[/code]

代码执行配置

内置 xAI 插件将 `code_execution` 作为 OpenClaw 工具暴露，用于在 xAI 的沙箱环境中 进行远程代码执行。

配置路径：`plugins.entries.xai.config.codeExecution`

键 | 类型 | 默认值 | 说明  
---|---|---|---  
`enabled` | boolean | `true`（如果密钥可用） | 启用或禁用代码执行  
`model` | string | `grok-4-1-fast` | 用于代码执行请求的模型  
`maxTurns` | number | - | 最大对话轮次  
`timeoutSeconds` | number | - | 请求超时时间（秒）  
json5Copy code
[code]
    {  plugins: {    entries: {      xai: {        config: {          codeExecution: {            enabled: true,            model: "grok-4-1-fast",          },        },      },    },  },}
[/code]

已知限制

  * 目前认证仅支持 API 密钥。API 密钥可以存储在 xAI 认证 配置文件、环境变量或插件配置中；OpenClaw 中尚无 xAI OAuth 或 设备代码流程。
  * `grok-4.20-multi-agent-experimental-beta-0304` 在 常规 xAI 提供商路径上不受支持，因为它所需的上游 API 表面不同于标准 OpenClaw xAI 传输。
  * xAI Realtime 语音尚未注册为 OpenClaw 提供商。它 需要不同于批量 STT 或流式转录的双向语音会话契约。
  * 在共享 `image_generate` 工具拥有相应的跨提供商控制之前， 不会暴露 xAI 图像 `quality`、图像 `mask` 和额外的仅原生宽高比。

高级说明

  * OpenClaw 会在共享运行器路径上自动应用 xAI 专属的工具 schema 和工具调用兼容性修复。
  * 原生 xAI 请求默认使用 `tool_stream: true`。将 `agents.defaults.models["xai/<model>"].params.tool_stream` 设置为 `false` 可将其 禁用。
  * 内置 xAI 包装器会在发送原生 xAI 请求之前移除不受支持的严格工具 schema 标志和 reasoning 负载键。
  * `web_search`、`x_search` 和 `code_execution` 作为 OpenClaw 工具暴露。OpenClaw 会在每个工具请求中启用其所需的特定 xAI 内置功能， 而不是把所有原生工具附加到每个聊天轮次。
  * Grok `web_search` 读取 `plugins.entries.xai.config.webSearch.baseUrl`。 `x_search` 读取 `plugins.entries.xai.config.xSearch.baseUrl`，然后 回退到 Grok Web 搜索基础 URL。
  * `x_search` 和 `code_execution` 由内置 xAI 插件拥有， 而不是硬编码到核心模型运行时中。
  * `code_execution` 是远程 xAI 沙箱执行，不是本地 [`exec`](</zh-CN/tools/exec>)。


## 实时测试

xAI 媒体路径由单元测试和可选启用的实时套件覆盖。实时 命令会在探测 `XAI_API_KEY` 之前，从你的登录 shell（包括 `~/.profile`）加载密钥。

bashCopy code
[code]
    pnpm test extensions/xaiOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 pnpm test:live -- extensions/xai/xai.live.test.tsOPENCLAW_LIVE_TEST=1 OPENCLAW_LIVE_TEST_QUIET=1 OPENCLAW_LIVE_IMAGE_GENERATION_PROVIDERS=xai pnpm test:live -- test/image-generation.runtime.live.test.ts
[/code]

提供商专属的实时文件会合成常规 TTS、适合电话场景的 PCM TTS，通过 xAI 批量 STT 转录音频，通过 xAI 实时 STT 流式传输相同的 PCM，生成文生图输出，并编辑一张参考图像。共享图像实时文件会通过 OpenClaw 的 运行时选择、回退、规范化和媒体附件路径验证同一个 xAI 提供商。

## 相关

[**模型选择** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**视频生成** 共享视频工具参数和提供商选择。 ](</zh-CN/tools/video-generation>) [**所有提供商** 更广泛的提供商概览。 ](</zh-CN/providers>) [**故障排除** 常见问题和修复方法。 ](</zh-CN/help/troubleshooting>)

Was this useful?YesNo