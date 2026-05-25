---
title: 推断
source_url: https://docs.openclaw.ai/zh-CN/providers/inferrs
scraped_at: 2026-05-25
---

[inferrs](<https://github.com/ericcurtin/inferrs>) 可以在 OpenAI 兼容的 `/v1` API 后提供本地模型服务。OpenClaw 通过通用的 `openai-completions` 路径与 `inferrs` 配合使用。

属性 | 值  
---|---  
提供商 ID | `inferrs`（自定义；在 `models.providers.inferrs` 下配置）  
插件 | 无 — `inferrs` 不是内置的 OpenClaw 提供商插件  
凭证环境变量 | 可选。如果你的 inferrs 服务器没有凭证，任意值都可以  
API | OpenAI 兼容（`openai-completions`）  
建议的基础 URL | `http://127.0.0.1:8080/v1`（或你的 inferrs 服务器所在位置）  
  
## 入门指南

* ### 使用模型启动 inferrs

bashCopy code
[code]
    inferrs serve google/gemma-4-E2B-it \  --host 127.0.0.1 \  --port 8080 \  --device metal
[/code]

* ### 验证服务器可访问

bashCopy code
[code]
    curl http://127.0.0.1:8080/healthcurl http://127.0.0.1:8080/v1/models
[/code]

* ### 添加 OpenClaw 提供商条目

添加一个显式的提供商条目，并将默认模型指向它。请参阅下面的完整配置示例。

## 完整配置示例

此示例在本地 `inferrs` 服务器上使用 Gemma 4。

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "inferrs/google/gemma-4-E2B-it" },      models: {        "inferrs/google/gemma-4-E2B-it": {          alias: "Gemma 4 (inferrs)",        },      },    },  },  models: {    mode: "merge",    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

## 按需启动

Inferrs 也可以仅在选择 `inferrs/...` 模型时由 OpenClaw 启动。将 `localService` 添加到同一个提供商条目中：

json5Copy code
[code]
    {  models: {    providers: {      inferrs: {        baseUrl: "http://127.0.0.1:8080/v1",        apiKey: "inferrs-local",        api: "openai-completions",        timeoutSeconds: 300,        localService: {          command: "/opt/homebrew/bin/inferrs",          args: [            "serve",            "google/gemma-4-E2B-it",            "--host",            "127.0.0.1",            "--port",            "8080",            "--device",            "metal",          ],          healthUrl: "http://127.0.0.1:8080/v1/models",          readyTimeoutMs: 180000,          idleStopMs: 0,        },        models: [          {            id: "google/gemma-4-E2B-it",            name: "Gemma 4 E2B (inferrs)",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 131072,            maxTokens: 4096,            compat: {              requiresStringContent: true,            },          },        ],      },    },  },}
[/code]

`command` 必须是绝对路径。在 Gateway 网关主机上使用 `which inferrs`，并将该路径放入配置。完整字段参考请参阅[本地模型服务](</zh-CN/gateway/local-model-services>)。

## 高级配置

为什么 requiresStringContent 很重要

某些 `inferrs` Chat Completions 路由只接受字符串 `messages[].content`，不接受结构化的内容部分数组。

json5Copy code
[code]
    compat: {  requiresStringContent: true}
[/code]

OpenClaw 会在发送请求前，将纯文本内容部分扁平化为普通字符串。

Gemma 和工具模式注意事项

某些当前的 `inferrs` \+ Gemma 组合可以接受小型直接 `/v1/chat/completions` 请求，但在完整的 OpenClaw agent 运行时轮次中仍会失败。

如果发生这种情况，请先尝试：

json5Copy code
[code]
    compat: {  requiresStringContent: true,  supportsTools: false}
[/code]

这会为该模型禁用 OpenClaw 的工具模式表面，并可降低更严格本地后端上的提示压力。

如果很小的直接请求仍然可用，但普通 OpenClaw agent 轮次继续在 `inferrs` 内部崩溃，则剩余问题通常是上游模型或服务器行为，而不是 OpenClaw 的传输层。

手动冒烟测试

配置完成后，测试两个层级：

bashCopy code
[code]
    curl http://127.0.0.1:8080/v1/chat/completions \  -H 'content-type: application/json' \  -d '{"model":"google/gemma-4-E2B-it","messages":[{"role":"user","content":"What is 2 + 2?"}],"stream":false}'
[/code]

bashCopy code
[code]
    openclaw infer model run \  --model inferrs/google/gemma-4-E2B-it \  --prompt "What is 2 + 2? Reply with one short sentence." \  --json
[/code]

如果第一个命令可用，但第二个命令失败，请查看下面的故障排除部分。

代理式行为

`inferrs` 会被视为代理式的 OpenAI 兼容 `/v1` 后端，而不是原生 OpenAI 端点。

  * 此处不适用仅限原生 OpenAI 的请求塑形
  * 没有 `service_tier`，没有 Responses `store`，没有提示缓存提示，也没有 OpenAI 推理兼容负载塑形
  * 隐藏的 OpenClaw 归因标头（`originator`、`version`、`User-Agent`）不会注入到自定义 `inferrs` 基础 URL 中


## 故障排除

curl /v1/models 失败

`inferrs` 未运行、不可访问，或未绑定到预期的主机/端口。请确保服务器已启动，并正在你配置的地址上监听。

messages[].content 预期为字符串

在模型条目中设置 `compat.requiresStringContent: true`。详情请参阅上面的 `requiresStringContent` 部分。

直接 /v1/chat/completions 调用通过，但 openclaw infer model run 失败

尝试设置 `compat.supportsTools: false` 以禁用工具模式表面。请参阅上面的 Gemma 工具模式注意事项。

inferrs 在较大的 agent 轮次上仍然崩溃

如果 OpenClaw 不再遇到模式错误，但 `inferrs` 仍然在较大的 agent 轮次上崩溃，请将其视为上游 `inferrs` 或模型限制。降低提示压力，或切换到不同的本地后端或模型。

## 相关内容

[**本地模型** 使用 OpenClaw 连接本地模型服务器。 ](</zh-CN/gateway/local-models>) [**本地模型服务** 为已配置的提供商按需启动本地模型服务器。 ](</zh-CN/gateway/local-model-services>) [**Gateway 网关故障排除** 调试探测通过但 agent 运行失败的本地 OpenAI 兼容后端。 ](</zh-CN/gateway/troubleshooting#local-openai-compatible-backend-passes-direct-probes-but-agent-runs-fail>) [**模型选择** 所有提供商、模型引用和故障转移行为概览。 ](</zh-CN/concepts/model-providers>)

Was this useful?YesNo