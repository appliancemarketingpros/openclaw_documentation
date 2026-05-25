---
title: Azure Speech
source_url: https://docs.openclaw.ai/zh-CN/providers/azure-speech
scraped_at: 2026-05-25
---

Azure Speech 是一个 Azure AI Speech 文本转语音提供商。在 OpenClaw 中，它默认将外发回复音频合成为 MP3，为语音消息使用原生 Ogg/Opus，并为诸如 Voice Call 之类的电话渠道生成 8 kHz mulaw 音频。

OpenClaw 直接使用带有 SSML 的 Azure Speech REST API，并通过 `X-Microsoft-OutputFormat` 发送由提供商控制的输出格式。

详细信息 | 值  
---|---  
网站 | [Azure AI Speech](<https://azure.microsoft.com/products/ai-services/ai-speech>)  
文档 | [Speech REST 文本转语音](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)  
认证 | `AZURE_SPEECH_KEY` 加 `AZURE_SPEECH_REGION`  
默认语音 | `en-US-JennyNeural`  
默认文件输出 | `audio-24khz-48kbitrate-mono-mp3`  
默认语音消息文件 | `ogg-24khz-16bit-mono-opus`  
  
## 入门指南

* ### 创建 Azure Speech 资源

在 Azure 门户中，创建一个 Speech 资源。复制“KEY 1”（位于“Resource Management > Keys and Endpoint”），并复制资源位置，例如 `eastus`。

CodeCopy code
[code]
    AZURE_SPEECH_KEY=<speech-resource-key>AZURE_SPEECH_REGION=eastus
[/code]

* ### 在 messages.tts 中选择 Azure Speech

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "azure-speech",      providers: {        "azure-speech": {          voice: "en-US-JennyNeural",          lang: "en-US",        },      },    },  },}
[/code]

* ### 发送消息

通过任意已连接的渠道发送回复。OpenClaw 会使用 Azure Speech 合成音频，并为标准音频传送 MP3，或者当渠道需要语音消息时传送 Ogg/Opus。

## 配置选项

选项 | 路径 | 说明  
---|---|---  
`apiKey` | `messages.tts.providers.azure-speech.apiKey` | Azure Speech 资源密钥。回退到 `AZURE_SPEECH_KEY`、`AZURE_SPEECH_API_KEY` 或 `SPEECH_KEY`。  
`region` | `messages.tts.providers.azure-speech.region` | Azure Speech 资源区域。回退到 `AZURE_SPEECH_REGION` 或 `SPEECH_REGION`。  
`endpoint` | `messages.tts.providers.azure-speech.endpoint` | 可选的 Azure Speech endpoint / 基础 URL 覆盖。  
`baseUrl` | `messages.tts.providers.azure-speech.baseUrl` | 可选的 Azure Speech 基础 URL 覆盖。  
`voice` | `messages.tts.providers.azure-speech.voice` | Azure 语音 `ShortName`（默认 `en-US-JennyNeural`）。  
`lang` | `messages.tts.providers.azure-speech.lang` | SSML 语言代码（默认 `en-US`）。  
`outputFormat` | `messages.tts.providers.azure-speech.outputFormat` | 音频文件输出格式（默认 `audio-24khz-48kbitrate-mono-mp3`）。  
`voiceNoteOutputFormat` | `messages.tts.providers.azure-speech.voiceNoteOutputFormat` | 语音消息输出格式（默认 `ogg-24khz-16bit-mono-opus`）。  
  
## 说明

身份验证

Azure Speech 使用的是 Speech 资源密钥，而不是 Azure OpenAI 密钥。该密钥通过 `Ocp-Apim-Subscription-Key` 发送；除非你提供 `endpoint` 或 `baseUrl`，否则 OpenClaw 会根据 `region` 推导出 `https://<region>.tts.speech.microsoft.com`。

语音名称

请使用 Azure Speech 语音的 `ShortName` 值，例如 `en-US-JennyNeural`。内置提供商可以通过同一个 Speech 资源列出语音，并过滤掉标记为 deprecated 或 retired 的语音。

音频输出

Azure 接受诸如 `audio-24khz-48kbitrate-mono-mp3`、`ogg-24khz-16bit-mono-opus` 和 `riff-24khz-16bit-mono-pcm` 之类的输出格式。OpenClaw 会为 `voice-note` 目标请求 Ogg/Opus，这样渠道就能发送原生语音气泡，而无需额外进行 MP3 转换。

别名

为兼容现有 PR 和用户配置，`azure` 可作为提供商别名使用，但新配置应使用 `azure-speech`，以避免与 Azure OpenAI 模型提供商混淆。

## 相关内容

[**文本转语音** TTS 概览、提供商以及 `messages.tts` 配置。 ](</zh-CN/tools/tts>) [**配置** 完整的配置参考，包括 `messages.tts` 设置。 ](</zh-CN/gateway/configuration>) [**提供商** 所有内置的 OpenClaw 提供商。 ](</zh-CN/providers>) [**故障排除** 常见问题和调试步骤。 ](</zh-CN/help/troubleshooting>)

Was this useful?YesNo