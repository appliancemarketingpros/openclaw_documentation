---
title: LLM 任务
source_url: https://docs.openclaw.ai/zh-CN/tools/llm-task
scraped_at: 2026-05-25
---

`llm-task` 是一个**可选插件工具** ，用于运行仅 JSON 的 LLM 任务，并返回结构化输出（可选地根据 JSON Schema 验证）。

这非常适合像 Lobster 这样的工作流引擎：你可以添加单个 LLM 步骤，而不必为每个工作流编写自定义 OpenClaw 代码。

## 启用插件

  1. 启用插件：

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": { "enabled": true }    }  }}
[/code]

  2. 允许可选工具：

jsonCopy code
[code]
    {  "tools": {    "alsoAllow": ["llm-task"]  }}
[/code]

仅当你想使用限制性允许列表模式时，才使用 `tools.allow`。

## 配置（可选）

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "llm-task": {        "enabled": true,        "config": {          "defaultProvider": "openai-codex",          "defaultModel": "gpt-5.5",          "defaultAuthProfileId": "main",          "allowedModels": ["openai/gpt-5.4"],          "maxTokens": 800,          "timeoutMs": 30000        }      }    }  }}
[/code]

`allowedModels` 是 `provider/model` 字符串的允许列表。如果设置了它，列表之外的任何请求都会被拒绝。

## 工具参数

  * `prompt`（字符串，必需）
  * `input`（任意，可选）
  * `schema`（对象，可选 JSON Schema）
  * `provider`（字符串，可选）
  * `model`（字符串，可选）
  * `thinking`（字符串，可选）
  * `authProfileId`（字符串，可选）
  * `temperature`（数字，可选）
  * `maxTokens`（数字，可选）
  * `timeoutMs`（数字，可选）


`thinking` 接受标准 OpenClaw 推理预设，例如 `low` 或 `medium`。

## 输出

返回包含已解析 JSON 的 `details.json`（并在提供 `schema` 时对其进行验证）。

## 示例：Lobster 工作流步骤

### 重要限制

下面的示例假设**独立版 Lobster CLI** 正在一个环境中运行，其中 `openclaw.invoke` 已经具有正确的 Gateway 网关 URL/认证上下文。

对于 OpenClaw 内置的**嵌入式** Lobster 运行器，这种嵌套 CLI 模式**目前并不可靠** ：

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{ ... }'
[/code]

在嵌入式 Lobster 为此流程提供受支持的桥接之前，请优先使用以下任一方式：

  * 在 Lobster 外部直接调用 `llm-task` 工具，或
  * 使用不依赖嵌套 `openclaw.invoke` 调用的 Lobster 步骤。


独立版 Lobster CLI 示例：

lobsterCopy code
[code]
    openclaw.invoke --tool llm-task --action json --args-json '{  "prompt": "Given the input email, return intent and draft.",  "thinking": "low",  "input": {    "subject": "Hello",    "body": "Can you help?"  },  "schema": {    "type": "object",    "properties": {      "intent": { "type": "string" },      "draft": { "type": "string" }    },    "required": ["intent", "draft"],    "additionalProperties": false  }}'
[/code]

## 安全说明

  * 该工具**仅限 JSON** ，并指示模型只输出 JSON（没有代码围栏，没有评论）。
  * 本次运行不会向模型暴露任何工具。
  * 除非你使用 `schema` 进行验证，否则应将输出视为不可信。
  * 在任何会产生副作用的步骤（发送、发布、执行）之前放置审批。


## 相关内容

  * [Thinking 级别](</zh-CN/tools/thinking>)
  * [子智能体](</zh-CN/tools/subagents>)
  * [斜杠命令](</zh-CN/tools/slash-commands>)


Was this useful?YesNo