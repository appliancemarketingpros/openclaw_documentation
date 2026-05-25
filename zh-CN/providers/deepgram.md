---
title: Deepgram
source_url: https://docs.openclaw.ai/zh-CN/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram 是一个语音转文本 API。在 OpenClaw 中，它用于通过 `tools.media.audio` 对入站音频 / 语音消息进行转写，也用于通过 `plugins.entries.voice-call.config.streaming` 为 Voice Call 提供流式 STT。

对于批量转写，OpenClaw 会将完整音频文件上传到 Deepgram，并将转写结果注入回复流水线（`{{Transcript}}` \+ `[Audio]` 块）。对于 Voice Call 流式场景，OpenClaw 会通过 Deepgram 的 WebSocket `listen` 端点转发实时 G.711 u-law 帧，并在 Deepgram 返回时发出部分或最终转写结果。

详情 | 值  
---|---  
网站 | [deepgram.com](<https://deepgram.com>)  
文档 | [developers.deepgram.com](<https://developers.deepgram.com>)  
认证 | `DEEPGRAM_API_KEY`  
默认模型 | `nova-3`  
  
## 入门指南

* ### 设置你的 API 密钥

将你的 Deepgram API 密钥添加到环境变量中：

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### 启用音频提供商

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### 发送语音消息

通过任意已连接渠道发送一条音频消息。OpenClaw 会通过 Deepgram 对其进行转写，并将转写结果注入回复流水线。

## 配置选项

选项 | 路径 | 说明  
---|---|---  
`model` | `tools.media.audio.models[].model` | Deepgram 模型 id（默认：`nova-3`）  
`language` | `tools.media.audio.models[].language` | 语言提示（可选）  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | 启用语言检测（可选）  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | 启用标点（可选）  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | 启用智能格式化（可选）  
  
### 使用语言提示

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### 使用 Deepgram 选项

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Voice Call 流式 STT

内置的 `deepgram` 插件也为 Voice Call 插件注册了一个实时转写提供商。

设置 | 配置路径 | 默认值  
---|---|---  
API 密钥 | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | 回退到 `DEEPGRAM_API_KEY`  
模型 | `...deepgram.model` | `nova-3`  
语言 | `...deepgram.language` | （未设置）  
编码 | `...deepgram.encoding` | `mulaw`  
采样率 | `...deepgram.sampleRate` | `8000`  
端点检测 | `...deepgram.endpointingMs` | `800`  
中间结果 | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## 说明

认证

认证遵循标准提供商认证顺序。`DEEPGRAM_API_KEY` 是最简单的方式。

代理和自定义端点

使用代理时，可通过 `tools.media.audio.baseUrl` 和 `tools.media.audio.headers` 覆盖端点或请求头。

输出行为

输出遵循与其他提供商相同的音频规则（大小上限、超时、转写注入）。

## 相关内容

[**媒体工具** 音频、图像和视频处理流水线概览。 ](</zh-CN/tools/media-overview>) [**配置** 完整的配置参考，包括媒体工具设置。 ](</zh-CN/gateway/configuration>) [**故障排除** 常见问题和调试步骤。 ](</zh-CN/help/troubleshooting>) [**常见问题** 关于 OpenClaw 设置的常见问题。 ](</zh-CN/help/faq>)

Was this useful?YesNo