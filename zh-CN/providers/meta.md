---
title: Meta
source_url: https://docs.openclaw.ai/zh-CN/providers/meta
scraped_at: 2026-07-13
---

快速开始

**Meta API** 对 `muse-spark-1.1` 推理模型使用兼容 OpenAI 的 **Responses API** （`POST /v1/responses`）。该提供商以 OpenClaw 内置插件的形式发布。

属性 | 值  
---|---  
提供商 ID | `meta`  
插件 | 内置提供商  
身份验证环境变量 | `MODEL_API_KEY`  
新手引导标志 | `--auth-choice meta-api-key`  
直接 CLI 标志 | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
基础 URL | `https://api.meta.ai/v1`  
默认模型 | `meta/muse-spark-1.1`  
默认推理强度 | `high` (`reasoning.effort`)  
  
## 入门指南

* ### 设置 API key

新手引导Copy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

直接标志Copy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

仅环境变量Copy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### 验证模型是否可用

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

列出静态的 `muse-spark-1.1` 目录条目。如果无法解析 `MODEL_API_KEY`，`openclaw models status --json` 会在 `auth.unusableProfiles` 下报告缺失的凭据。

## 非交互式设置

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## 内置目录

模型引用 | 名称 | 推理 | 上下文窗口 | 最大输出  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | 是 | 1,048,576 | 131,072  
  
能力：

  * 文本和图像输入
  * 工具调用和流式传输
  * 推理强度：`minimal`、`low`、`medium`、`high`、`xhigh`（默认：`high`）
  * 无状态加密推理重放（`store: false`、`include: ["reasoning.encrypted_content"]`）


## 手动配置

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## 冒烟测试

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

实时测试使用 `muse-spark-1.1` 调用 `POST /v1/responses`。

## 相关内容

[**模型提供商** 选择提供商、模型引用和故障转移行为。 ](</zh-CN/concepts/model-providers>) [**思考模式** muse-spark-1.1 的推理强度级别。 ](</zh-CN/tools/thinking>) [**配置参考** Agent 默认设置和模型配置。 ](</zh-CN/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue