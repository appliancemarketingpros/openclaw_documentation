---
title: Z.AI
source_url: https://docs.openclaw.ai/zh-CN/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) 是 **GLM** 模型的 API 平台。它为 GLM 提供 REST API，并使用 API key 进行身份验证。请在 [Z.AI](<http://Z.AI>) 控制台创建你的 API key。OpenClaw 使用带有 [Z.AI](<http://Z.AI>) API key 的 `zai` provider。

  * 提供商：`zai`
  * 身份验证：`ZAI_API_KEY`
  * API：[Z.AI](<http://Z.AI>) Chat Completions（Bearer 身份验证）


## 入门指南

### 自动检测端点

**最适合：** 大多数用户。OpenClaw 会根据密钥检测匹配的 [Z.AI](<http://Z.AI>) 端点，并自动应用正确的 base URL。

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### 设置默认模型

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### 验证模型已列出

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### 显式区域端点

**最适合：** 想要强制使用特定 Coding Plan 或通用 API 表面的用户。

* ### 选择正确的新手引导选项

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### 设置默认模型

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### 验证模型已列出

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## 内置目录

OpenClaw 会在插件清单中随附内置的 `zai` provider 目录，因此只读列表可以在不加载提供商运行时的情况下显示已知的 GLM 行：

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

基于清单的目录当前包含：

模型引用 | 备注  
---|---  
`zai/glm-5.1` | 默认模型  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## 高级配置

向前解析未知 GLM-5 模型

未知的 `glm-5*` ID 仍会在内置提供商路径上向前解析：当 ID 匹配当前 GLM-5 系列形态时，会从 `glm-4.7` 模板合成提供商拥有的元数据。

工具调用流式传输

[Z.AI](<http://Z.AI>) 工具调用流式传输默认启用 `tool_stream`。若要禁用它：

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

思考和保留思考

[Z.AI](<http://Z.AI>) 思考遵循 OpenClaw 的 `/think` 控制。关闭思考时，OpenClaw 会发送 `thinking: { type: "disabled" }`，以避免响应在可见文本之前将输出预算消耗在 `reasoning_content` 上。

保留思考是选择启用的，因为 [Z.AI](<http://Z.AI>) 要求重放完整的历史 `reasoning_content`，这会增加提示词 token。请按模型启用：

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

启用后且思考处于开启状态时，OpenClaw 会发送 `thinking: { type: "enabled", clear_thinking: false }`，并为同一个 OpenAI 兼容对话记录重放先前的 `reasoning_content`。

高级用户仍可使用 `params.extra_body.thinking` 覆盖确切的提供商载荷。

图像理解

内置的 [Z.AI](<http://Z.AI>) 插件会注册图像理解。

属性 | 值  
---|---  
模型 | `glm-4.6v`  
  
图像理解会从已配置的 [Z.AI](<http://Z.AI>) 身份验证自动解析，无需额外配置。

身份验证详情

  * [Z.AI](<http://Z.AI>) 使用你的 API key 进行 Bearer 身份验证。
  * `zai-api-key` 新手引导选项会根据密钥前缀自动检测匹配的 [Z.AI](<http://Z.AI>) 端点。
  * 当你想要强制使用特定 API 表面时，请使用显式区域选项（`zai-coding-global`、`zai-coding-cn`、`zai-global`、`zai-cn`）。


## 相关内容

[**GLM 模型系列** GLM 的模型系列概览。 ](</zh-CN/providers/glm>) [**模型选择** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>)

Was this useful?YesNo