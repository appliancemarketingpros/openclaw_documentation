---
title: Ollama Web 搜索
source_url: https://docs.openclaw.ai/zh-CN/tools/ollama-search
scraped_at: 2026-05-25
---

OpenClaw 支持 **Ollama Web 搜索** 作为内置的 `web_search` 提供商。它使用 Ollama 的网页搜索 API，并返回包含标题、URL 和摘要的结构化结果。

对于本地或自托管的 Ollama，此设置默认不需要 API 密钥。但它确实需要：

  * 一个可从 OpenClaw 访问到的 Ollama 主机
  * `ollama signin`


对于直接使用托管搜索，请将 Ollama 提供商的基础 URL 设置为 `https://ollama.com`，并提供真实的 `OLLAMA_API_KEY`。

## 设置

* ### 启动 Ollama

确保 Ollama 已安装并正在运行。

* ### 登录

运行：

bashCopy code
[code]
    ollama signin
[/code]

* ### 选择 Ollama Web 搜索

运行：

bashCopy code
[code]
    openclaw configure --section web
[/code]

然后选择 **Ollama Web 搜索** 作为提供商。

如果你已经将 Ollama 用于模型，Ollama Web 搜索会复用同一个已配置的主机。

## 配置

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

可选的 Ollama 主机覆盖：

json5Copy code
[code]
    {  plugins: {    entries: {      ollama: {        config: {          webSearch: {            baseUrl: "http://ollama-host:11434",          },        },      },    },  },}
[/code]

如果你已经将 Ollama 配置为模型提供商，则网页搜索提供商也可以改为复用该主机：

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",      },    },  },}
[/code]

Ollama 模型提供商使用 `baseUrl` 作为规范键名。为了兼容 OpenAI SDK 风格的配置示例，网页搜索提供商也支持在 `models.providers.ollama` 上使用 `baseURL`。

如果未显式设置 Ollama 基础 URL，OpenClaw 会使用 `http://127.0.0.1:11434`。

如果你的 Ollama 主机需要 bearer 认证，OpenClaw 会将 `models.providers.ollama.apiKey`（或对应由环境变量支持的提供商认证）复用于对该已配置主机的请求。

直接使用托管的 Ollama Web 搜索：

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",      },    },  },  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

## 说明

  * 此提供商不需要专用的网页搜索 API 密钥字段。
  * 如果 Ollama 主机受认证保护，OpenClaw 会在存在时复用常规 Ollama 提供商 API 密钥。
  * 如果 `baseUrl` 是 `https://ollama.com`，OpenClaw 会直接调用 `https://ollama.com/api/web_search`，并将已配置的 Ollama API 密钥作为 bearer 认证发送。
  * 如果已配置的主机未暴露网页搜索，而设置了 `OLLAMA_API_KEY`，OpenClaw 可以回退到 `https://ollama.com/api/web_search`，同时不会将该环境变量密钥发送到本地主机。
  * 如果 Ollama 无法访问或尚未登录，OpenClaw 会在设置期间发出警告，但不会阻止选择。
  * 当未配置更高优先级的、带凭证的提供商时，运行时自动检测可以回退到 Ollama Web 搜索。
  * 本地 Ollama 守护进程主机使用本地代理端点 `/api/experimental/web_search`，该端点会签名并转发到 Ollama Cloud。
  * `https://ollama.com` 主机则直接使用公共托管端点 `/api/web_search`，并采用 bearer API 密钥认证。


## 相关内容

  * [Web Search 概览](</zh-CN/tools/web>) \-- 所有提供商和自动检测
  * [Ollama](</zh-CN/providers/ollama>) \-- Ollama 模型设置以及云端/本地模式


Was this useful?YesNo