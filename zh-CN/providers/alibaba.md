---
title: Alibaba Model Studio
source_url: https://docs.openclaw.ai/zh-CN/providers/alibaba
scraped_at: 2026-05-25
---

OpenClaw 随附一个内置的 `alibaba` 插件，该插件为 Alibaba Model Studio（DashScope 的国际名称）上的 Wan 模型注册视频生成提供商。该插件默认启用；你只需要设置 API key。

属性 | 值  
---|---  
提供商 ID | `alibaba`  
插件 | 内置，`enabledByDefault: true`  
凭证环境变量 | `MODELSTUDIO_API_KEY` → `DASHSCOPE_API_KEY` → `QWEN_API_KEY`（第一个匹配项生效）  
新手引导标志 | `--auth-choice alibaba-model-studio-api-key`  
直接 CLI 标志 | `--alibaba-model-studio-api-key <key>`  
默认模型 | `alibaba/wan2.6-t2v`  
默认 base URL | `https://dashscope-intl.aliyuncs.com`  
  
## 入门指南

* ### 设置 API key

使用新手引导将 key 存储到 `alibaba` 提供商：

bashCopy code
[code]
    openclaw onboard --auth-choice alibaba-model-studio-api-key
[/code]

或者在安装/新手引导期间直接传入 key：

bashCopy code
[code]
    openclaw onboard --alibaba-model-studio-api-key <your-key>
[/code]

或者在启动 Gateway 网关之前导出任一受支持的环境变量：

bashCopy code
[code]
    export MODELSTUDIO_API_KEY=sk-...# or DASHSCOPE_API_KEY=...# or QWEN_API_KEY=...
[/code]

* ### 设置默认视频模型

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "alibaba/wan2.6-t2v",      },    },  },}
[/code]

* ### 验证提供商已配置

bashCopy code
[code]
    openclaw models list --provider alibaba
[/code]

列表应包含全部五个内置 Wan 模型。如果 `MODELSTUDIO_API_KEY` 未解析，`openclaw models status --json` 会在 `auth.unusableProfiles` 下报告缺失的凭证。

## 内置 Wan 模型

模型引用 | 模式  
---|---  
`alibaba/wan2.6-t2v` | 文本转视频（默认）  
`alibaba/wan2.6-i2v` | 图像转视频  
`alibaba/wan2.6-r2v` | 参考转视频  
`alibaba/wan2.6-r2v-flash` | 参考转视频（快速）  
`alibaba/wan2.7-r2v` | 参考转视频  
  
## 能力和限制

内置提供商映射 DashScope 的 Wan 视频 API 限制。三种模式共享相同的每请求视频数量和时长上限；只有输入形态不同。

模式 | 最大输出视频数 | 最大输入图像数 | 最大输入视频数 | 最大时长 | 支持的控制项  
---|---|---|---|---|---  
文本转视频 | 1 | n/a | n/a | 10 秒 | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
图像转视频 | 1 | 1 | n/a | 10 秒 | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
参考转视频 | 1 | n/a | 4 | 10 秒 | `size`, `aspectRatio`, `resolution`, `audio`, `watermark`  
  
当请求省略 `durationSeconds` 时，提供商会发送 DashScope 接受的默认值 **5 秒** 。在[视频生成工具](</zh-CN/tools/video-generation>)上显式设置 `durationSeconds`，可扩展到最长 10 秒。

## 高级配置

覆盖 DashScope base URL

提供商默认使用国际版 DashScope 端点。若要指向中国区端点，请设置：

json5Copy code
[code]
    {  models: {    providers: {      alibaba: {        baseUrl: "https://dashscope.aliyuncs.com",      },    },  },}
[/code]

提供商会在构造 AIGC 任务 URL 之前移除尾部斜杠。

凭证环境变量优先级

OpenClaw 会按以下顺序从环境变量解析 Alibaba API key，并采用第一个非空值：

  1. `MODELSTUDIO_API_KEY`
  2. `DASHSCOPE_API_KEY`
  3. `QWEN_API_KEY`


已配置的 `auth.profiles` 条目（通过 `openclaw models auth login` 设置）会覆盖环境变量解析。有关配置档案轮换、冷却和覆盖机制，请参阅[模型常见问题中的凭证配置档案](</zh-CN/help/faq-models#what-is-an-auth-profile>)。

与 Qwen 插件的关系

两个内置插件都与 DashScope 通信，并接受有重叠的 API key。使用：

  * `alibaba/wan*.*` ID 来驱动本文档页面说明的专用 Wan 视频提供商。
  * `qwen/*` ID 用于 Qwen 聊天、嵌入和媒体理解（参见 [Qwen](</zh-CN/providers/qwen>)）。


只设置一次 `MODELSTUDIO_API_KEY` 即可为两个插件完成身份验证，因为凭证环境变量列表有意重叠；你不需要为每个插件分别完成新手引导。

## 相关内容

[**视频生成** 共享视频工具参数和提供商选择。 ](</zh-CN/tools/video-generation>) [**Qwen** 在同一 DashScope 凭证上设置 Qwen 聊天、嵌入和媒体理解。 ](</zh-CN/providers/qwen>) [**配置参考** 智能体默认值和模型配置。 ](</zh-CN/gateway/config-agents#agent-defaults>) [**模型常见问题** 凭证配置档案、切换模型，以及解决“no profile”错误。 ](</zh-CN/help/faq-models>)

Was this useful?YesNo