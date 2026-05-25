---
title: Google (Gemini)
source_url: https://docs.openclaw.ai/zh-CN/providers/google
scraped_at: 2026-05-25
---

Google 插件通过 Google AI Studio 提供对 Gemini 模型的访问，并支持 图像生成、媒体理解（图像/音频/视频）、文本转语音，以及通过 Gemini Grounding 进行 Web 搜索。

  * 提供商：`google`
  * 凭证：`GEMINI_API_KEY` 或 `GOOGLE_API_KEY`
  * API：Google Gemini API
  * 运行时选项：provider/model `agentRuntime.id: "google-gemini-cli"` 会复用 Gemini CLI OAuth，同时将模型引用保持为规范的 `google/*`。


## 入门指南

选择你偏好的凭证方法并按照设置步骤操作。

### API key

**最适合：** 通过 Google AI Studio 进行标准 Gemini API 访问。

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard --auth-choice gemini-api-key
[/code]

或直接传入密钥：

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice gemini-api-key \  --gemini-api-key "$GEMINI_API_KEY"
[/code]

* ### 设置默认模型

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "google/gemini-3.1-pro-preview" },    },  },}
[/code]

* ### 验证模型可用

bashCopy code
[code]
    openclaw models list --provider google
[/code]

### Gemini CLI (OAuth)

**最适合：** 通过 PKCE OAuth 复用现有 Gemini CLI 登录，而不是使用单独的 API 密钥。

* ### 安装 Gemini CLI

本地 `gemini` 命令必须在 `PATH` 上可用。

bashCopy code
[code]
    # Homebrewbrew install gemini-cli # or npmnpm install -g @google/gemini-cli
[/code]

OpenClaw 支持 Homebrew 安装和全局 npm 安装，包括 常见的 Windows/npm 布局。

* ### 通过 OAuth 登录

bashCopy code
[code]
    openclaw models auth login --provider google-gemini-cli --set-default
[/code]

* ### 验证模型可用

bashCopy code
[code]
    openclaw models list --provider google
[/code]

  * 默认模型：`google/gemini-3.1-pro-preview`
  * 运行时：`google-gemini-cli`
  * 别名：`gemini-cli`


Gemini 3.1 Pro 的 Gemini API 模型 ID 是 `gemini-3.1-pro-preview`。OpenClaw 接受较短的 `google/gemini-3.1-pro` 作为便捷别名，并在调用提供商之前将其规范化。

**环境变量：**

  * `OPENCLAW_GEMINI_OAUTH_CLIENT_ID`
  * `OPENCLAW_GEMINI_OAUTH_CLIENT_SECRET`


（或 `GEMINI_CLI_*` 变体。）

`google-gemini-cli/*` 模型引用是旧版兼容别名。新 配置应使用 `google/*` 模型引用，并在需要本地 Gemini CLI 执行时配合使用 `google-gemini-cli` 运行时。

## 能力

能力 | 支持  
---|---  
聊天补全 | 是  
图像生成 | 是  
音乐生成 | 是  
文本转语音 | 是  
实时语音 | 是（Google Live API）  
图像理解 | 是  
音频转录 | 是  
视频理解 | 是  
Web 搜索（Grounding） | 是  
思考/推理 | 是（Gemini 2.5+ / Gemini 3+）  
Gemma 4 模型 | 是  
  
## Web 搜索

内置的 `gemini` Web 搜索提供商使用 Gemini Google Search grounding。 在 `plugins.entries.google.config.webSearch` 下配置专用搜索密钥， 或者让它在 `GEMINI_API_KEY` 之后复用 `models.providers.google.apiKey`：

json5Copy code
[code]
    {  plugins: {    entries: {      google: {        config: {          webSearch: {            apiKey: "AIza...", // optional if GEMINI_API_KEY or models.providers.google.apiKey is set            baseUrl: "https://generativelanguage.googleapis.com/v1beta", // falls back to models.providers.google.baseUrl            model: "gemini-2.5-flash",          },        },      },    },  },}
[/code]

凭据优先级依次为专用的 `webSearch.apiKey`、`GEMINI_API_KEY`， 然后是 `models.providers.google.apiKey`。`webSearch.baseUrl` 是可选项， 用于运维代理或兼容的 Gemini API 端点；省略时， Gemini Web 搜索会复用 `models.providers.google.baseUrl`。请参阅 [Gemini 搜索](</zh-CN/tools/gemini-search>) 了解提供商特定的工具行为。

## 图像生成

内置的 `google` 图像生成提供商默认使用 `google/gemini-3.1-flash-image-preview`。

  * 还支持 `google/gemini-3-pro-image-preview`
  * 生成：每个请求最多 4 张图像
  * 编辑模式：已启用，最多 5 张输入图像
  * 几何控制：`size`、`aspectRatio` 和 `resolution`


将 Google 用作默认图像提供商：

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "google/gemini-3.1-flash-image-preview",      },    },  },}
[/code]

## 视频生成

内置的 `google` 插件还会通过共享的 `video_generate` 工具注册视频生成。

  * 默认视频模型：`google/veo-3.1-fast-generate-preview`
  * 模式：文本转视频、图像转视频和单视频引用流程
  * 支持 `aspectRatio`（`16:9`、`9:16`）和 `resolution`（`720P`、`1080P`）；Veo 目前不支持音频输出
  * 支持的时长：**4、6 或 8 秒** （其他值会贴合到最近的允许值）


将 Google 用作默认视频提供商：

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "google/veo-3.1-fast-generate-preview",      },    },  },}
[/code]

## 音乐生成

内置的 `google` 插件还会通过共享的 `music_generate` 工具注册音乐生成。

  * 默认音乐模型：`google/lyria-3-clip-preview`
  * 还支持 `google/lyria-3-pro-preview`
  * 提示词控制：`lyrics` 和 `instrumental`
  * 输出格式：默认 `mp3`，在 `google/lyria-3-pro-preview` 上还支持 `wav`
  * 参考输入：最多 10 张图像
  * 会话支持的运行会通过共享任务/Status 流程分离，包括 `action: "status"`


将 Google 用作默认音乐提供商：

json5Copy code
[code]
    {  agents: {    defaults: {      musicGenerationModel: {        primary: "google/lyria-3-clip-preview",      },    },  },}
[/code]

## 文本转语音

内置的 `google` 语音提供商使用 Gemini API TTS 路径，并使用 `gemini-3.1-flash-tts-preview`。

  * 默认语音：`Kore`
  * 凭证：`messages.tts.providers.google.apiKey`、`models.providers.google.apiKey`、`GEMINI_API_KEY` 或 `GOOGLE_API_KEY`
  * 输出：常规 TTS 附件使用 WAV，语音笔记目标使用 Opus，Talk/电话使用 PCM
  * 语音笔记输出：Google PCM 会封装为 WAV，并通过 `ffmpeg` 转码为 48 kHz Opus


Google 的批量 Gemini TTS 路径会在完成的 `generateContent` 响应中返回生成的音频。若要获得最低延迟的语音对话，请使用 由 Gemini Live API 支持的 Google 实时语音提供商，而不是批量 TTS。

将 Google 用作默认 TTS 提供商：

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "google",      providers: {        google: {          model: "gemini-3.1-flash-tts-preview",          voiceName: "Kore",          audioProfile: "Speak professionally with a calm tone.",        },      },    },  },}
[/code]

Gemini API TTS 使用自然语言提示词进行风格控制。设置 `audioProfile` 可在朗读文本前追加可复用的风格提示词。当你的提示词文本引用具名说话人时，设置 `speakerName`。

Gemini API TTS 还接受文本中的富表现力方括号音频标签， 例如 `[whispers]` 或 `[laughs]`。若要在将标签发送给 TTS 的同时避免其出现在可见聊天回复中， 请将它们放在 `[[tts:text]]...[[/tts:text]]` 块内：

textCopy code
[code]
    Here is the clean reply text. [[tts:text]][whispers] Here is the spoken version.[[/tts:text]]
[/code]

## 实时语音

内置的 `google` 插件注册了一个由 Gemini Live API 支持的实时语音提供商，用于 Voice Call 和 Google Meet 等后端音频桥接。

设置 | 配置路径 | 默认值  
---|---|---  
模型 | `plugins.entries.voice-call.config.realtime.providers.google.model` | `gemini-2.5-flash-native-audio-preview-12-2025`  
语音 | `...google.voice` | `Kore`  
温度 | `...google.temperature` | （未设置）  
VAD 开始敏感度 | `...google.startSensitivity` | （未设置）  
VAD 结束敏感度 | `...google.endSensitivity` | （未设置）  
静音持续时间 | `...google.silenceDurationMs` | （未设置）  
活动处理 | `...google.activityHandling` | Google 默认值，`start-of-activity-interrupts`  
轮次覆盖 | `...google.turnCoverage` | Google 默认值，`only-activity`  
禁用自动 VAD | `...google.automaticActivityDetectionDisabled` | `false`  
会话恢复 | `...google.sessionResumption` | `true`  
上下文压缩 | `...google.contextWindowCompression` | `true`  
API 密钥 | `...google.apiKey` | 回退到 `models.providers.google.apiKey`、`GEMINI_API_KEY` 或 `GOOGLE_API_KEY`  
  
Voice Call 实时配置示例：

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          realtime: {            enabled: true,            provider: "google",            providers: {              google: {                model: "gemini-2.5-flash-native-audio-preview-12-2025",                voice: "Kore",                activityHandling: "start-of-activity-interrupts",                turnCoverage: "only-activity",              },            },          },        },      },    },  },}
[/code]

对于维护者实时验证，请运行 `OPENAI_API_KEY=... GEMINI_API_KEY=... node --import tsx scripts/dev/realtime-talk-live-smoke.ts`。 该冒烟测试还覆盖 OpenAI 后端/WebRTC 路径；Google 分支会铸造与 Control UI Talk 使用的相同受限 Live API 令牌形态，打开浏览器 WebSocket 端点，发送初始设置载荷，并等待 `setupComplete`。

## 高级配置

直接复用 Gemini 缓存

对于直接 Gemini API 运行（`api: "google-generative-ai"`），OpenClaw 会将配置的 `cachedContent` 句柄传递给 Gemini 请求。

  * 使用 `cachedContent` 或旧版 `cached_content` 配置按模型或全局参数
  * 如果两者都存在，`cachedContent` 优先
  * 示例值：`cachedContents/prebuilt-context`
  * Gemini 缓存命中用量会从上游 `cachedContentTokenCount` 规范化为 OpenClaw `cacheRead`

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "google/gemini-2.5-pro": {          params: {            cachedContent: "cachedContents/prebuilt-context",          },        },      },    },  },}
[/code]

Gemini CLI JSON 用量说明

使用 `google-gemini-cli` OAuth 提供商时，OpenClaw 会按如下方式规范化 CLI JSON 输出：

  * 回复文本来自 CLI JSON `response` 字段。
  * 当 CLI 将 `usage` 留空时，用量会回退到 `stats`。
  * `stats.cached` 会规范化为 OpenClaw `cacheRead`。
  * 如果缺少 `stats.input`，OpenClaw 会从 `stats.input_tokens - stats.cached` 推导输入 token。

环境和守护进程设置

如果 Gateway 网关作为守护进程运行（launchd/systemd），请确保 `GEMINI_API_KEY` 可用于该进程（例如，在 `~/.openclaw/.env` 中，或通过 `env.shellEnv`）。

## 相关内容

[**模型选择** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**图像生成** 共享图像工具参数和提供商选择。 ](</zh-CN/tools/image-generation>) [**视频生成** 共享视频工具参数和提供商选择。 ](</zh-CN/tools/video-generation>) [**音乐生成** 共享音乐工具参数和提供商选择。 ](</zh-CN/tools/music-generation>)

Was this useful?YesNo