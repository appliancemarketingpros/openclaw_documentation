---
title: SenseAudio
source_url: https://docs.openclaw.ai/zh-CN/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio 可以通过 OpenClaw 共享的 `tools.media.audio` 管道转录传入音频和语音备注附件。OpenClaw 会将 multipart 音频发布到 OpenAI 兼容的转录端点，并将返回的文本作为 `{{Transcript}}` 以及一个 `[Audio]` 块注入。

属性 | 值  
---|---  
提供商 id | `senseaudio`  
插件 | 内置，`enabledByDefault: true`  
契约 | `mediaUnderstandingProviders`（音频）  
凭证环境变量 | `SENSEAUDIO_API_KEY`  
默认模型 | `senseaudio-asr-pro-1.5-260319`  
默认 URL | `https://api.senseaudio.cn/v1`  
网站 | [senseaudio.cn](<https://senseaudio.cn>)  
文档 | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## 入门指南

* ### 设置你的 API key

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### 启用音频提供商

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### 发送语音备注

通过任何已连接的渠道发送音频消息。OpenClaw 会将音频上传到 SenseAudio，并在回复管道中使用转录文本。

## 选项

选项 | 路径 | 描述  
---|---|---  
`model` | `tools.media.audio.models[].model` | SenseAudio ASR 模型 id  
`language` | `tools.media.audio.models[].language` | 可选语言提示  
`prompt` | `tools.media.audio.prompt` | 可选转录提示  
`baseUrl` | `tools.media.audio.baseUrl` or model | 覆盖 OpenAI 兼容的 base  
`headers` | `tools.media.audio.request.headers` | 额外请求头  
  
## 相关内容

  * [媒体理解（音频）](</zh-CN/nodes/audio>)
  * [模型提供商](</zh-CN/concepts/model-providers>)


Was this useful?YesNo