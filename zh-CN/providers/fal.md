---
title: Fal
source_url: https://docs.openclaw.ai/zh-CN/providers/fal
scraped_at: 2026-05-25
---

OpenClaw 内置了一个 `fal` 提供商，用于托管式图像和视频生成。

属性 | 值  
---|---  
提供商 | `fal`  
凭证 | `FAL_KEY`（规范；`FAL_API_KEY` 也可作为备用）  
API | fal 模型端点  
  
## 入门指南

* ### 设置 API 密钥

bashCopy code
[code]
    openclaw onboard --auth-choice fal-api-key
[/code]

* ### 设置默认图像模型

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## 图像生成

内置的 `fal` 图像生成提供商默认使用 `fal/fal-ai/flux/dev`。

能力 | 值  
---|---  
最大图像数 | 每次请求 4 张  
编辑模式 | Flux：1 张参考图像；GPT Image 2：10；Nano Banana 2：14  
尺寸覆盖 | 支持  
宽高比 | 支持生成以及 GPT Image 2/Nano Banana 2 编辑  
分辨率 | 支持  
输出格式 | `png` 或 `jpeg`  
  
当你需要 PNG 输出时，请使用 `outputFormat: "png"`。fal 在 OpenClaw 中没有声明显式的透明背景控制，因此 `background: "transparent"` 会被报告为 fal 模型中被忽略的覆盖项。

要将 fal 用作默认图像提供商：

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "fal/fal-ai/flux/dev",      },    },  },}
[/code]

## 视频生成

内置的 `fal` 视频生成提供商默认使用 `fal/fal-ai/minimax/video-01-live`。

能力 | 值  
---|---  
模式 | 文本转视频、单图参考、Seedance 参考转视频  
运行时 | 用于长时间运行任务的队列支持提交/状态/结果流程  
  
可用视频模型

**HeyGen video-agent：**

  * `fal/fal-ai/heygen/v2/video-agent`


**Seedance 2.0：**

  * `fal/bytedance/seedance-2.0/fast/text-to-video`
  * `fal/bytedance/seedance-2.0/fast/image-to-video`
  * `fal/bytedance/seedance-2.0/fast/reference-to-video`
  * `fal/bytedance/seedance-2.0/text-to-video`
  * `fal/bytedance/seedance-2.0/image-to-video`
  * `fal/bytedance/seedance-2.0/reference-to-video`

Seedance 2.0 配置示例 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/text-to-video",      },    },  },}
[/code]

Seedance 2.0 参考转视频配置示例 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/bytedance/seedance-2.0/fast/reference-to-video",      },    },  },}
[/code]

参考转视频最多接受 9 张图像、3 个视频和 3 个音频参考， 通过共享的 `video_generate` `images`、`videos` 和 `audioRefs` 参数传入，总参考文件数最多为 12 个。

HeyGen video-agent 配置示例 json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "fal/fal-ai/heygen/v2/video-agent",      },    },  },}
[/code]

## 相关

[**图像生成** 共享图像工具参数和提供商选择。 ](</zh-CN/tools/image-generation>) [**视频生成** 共享视频工具参数和提供商选择。 ](</zh-CN/tools/video-generation>) [**配置参考** Agent 默认值，包括图像和视频模型选择。 ](</zh-CN/gateway/config-agents#agent-defaults>)

Was this useful?YesNo