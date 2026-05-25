---
title: 跑道
source_url: https://docs.openclaw.ai/zh-CN/providers/runway
scraped_at: 2026-05-25
---

OpenClaw 内置了一个用于托管视频生成的 `runway` 提供商。该插件默认启用，并针对 `videoGenerationProviders` 合约注册 `runway` 提供商。

属性 | 值  
---|---  
提供商 id | `runway`  
插件 | 内置，`enabledByDefault: true`  
认证环境变量 | `RUNWAYML_API_SECRET`（规范）或 `RUNWAY_API_KEY`  
新手引导标志 | `--auth-choice runway-api-key`  
直接 CLI 标志 | `--runway-api-key <key>`  
API | Runway 基于任务的视频生成（`GET /v1/tasks/{id}` 轮询）  
默认模型 | `runway/gen4.5`  
  
## 入门指南

* ### 设置 API key

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### 将 Runway 设置为默认视频提供商

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### 生成视频

让智能体生成一个视频。Runway 会被自动使用。

## 支持的模式和模型

该提供商公开七个 Runway 模型，分为三种模式。同一个模型 id 可以服务于多个模式（例如 `gen4.5` 同时适用于文本转视频和图像转视频）。

模式 | 模型 | 参考输入  
---|---|---  
文本转视频 | `gen4.5`（默认）、`veo3.1`、`veo3.1_fast`、`veo3` | 无  
图像转视频 | `gen4.5`、`gen4_turbo`、`gen3a_turbo`、`veo3.1`、`veo3.1_fast`、`veo3` | 1 个本地或远程图像  
视频转视频 | `gen4_aleph` | 1 个本地或远程视频  
  
支持通过 data URI 引用本地图像和视频。

宽高比 | 允许的值  
---|---  
文本转视频 | `16:9`、`9:16`  
图像和视频编辑 | `1:1`、`16:9`、`9:16`、`3:4`、`4:3`、`21:9`  
  
## 配置

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## 高级配置

环境变量别名

OpenClaw 同时识别 `RUNWAYML_API_SECRET`（规范）和 `RUNWAY_API_KEY`。 任一变量都可以认证 Runway 提供商。

任务轮询

Runway 使用基于任务的 API。提交生成请求后，OpenClaw 会轮询 `GET /v1/tasks/{id}`，直到视频准备就绪。该轮询行为不需要额外 配置。

## 相关内容

[**视频生成** 共享工具参数、提供商选择和异步行为。 ](</zh-CN/tools/video-generation>) [**配置参考** 智能体默认设置，包括视频生成模型。 ](</zh-CN/gateway/config-agents#agent-defaults>)

Was this useful?YesNo