---
title: LiteLLM
source_url: https://docs.openclaw.ai/zh-CN/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) 是一个开源 LLM 网关，提供统一 API 以接入 100 多家模型提供商。通过 LiteLLM 路由 OpenClaw，以获得集中式成本跟踪、日志记录，以及无需更改 OpenClaw 配置即可切换后端的灵活性。

## 快速开始

### 新手引导（推荐）

**最适合：** 以最快方式完成可用的 LiteLLM 设置。

* ### 运行新手引导

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

如果要针对远程代理进行非交互式设置，请显式传入代理 URL：

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### 手动设置

**最适合：** 完全控制安装和配置。

* ### 启动 LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### 让 OpenClaw 指向 LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

就这样。OpenClaw 现在会通过 LiteLLM 路由。

## 配置

### 环境变量

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### 配置文件

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## 高级配置

### 图像生成

LiteLLM 也可以通过兼容 OpenAI 的 `/images/generations` 和 `/images/edits` 路由，为 `image_generate` 工具提供支持。在 `agents.defaults.imageGenerationModel` 下配置一个 LiteLLM 图像模型：

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

像 `http://localhost:4000` 这样的 loopback LiteLLM URL 无需全局私有网络覆盖即可工作。对于托管在局域网中的代理，请设置 `models.providers.litellm.request.allowPrivateNetwork: true`，因为 API 密钥将被发送到已配置的代理主机。

虚拟密钥

为 OpenClaw 创建一个带有支出限制的专用密钥：

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

将生成的密钥用作 `LITELLM_API_KEY`。

模型路由

LiteLLM 可以将模型请求路由到不同后端。在你的 LiteLLM `config.yaml` 中进行配置：

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw 会继续请求 `claude-opus-4-6`——由 LiteLLM 负责处理路由。

查看使用情况

查看 LiteLLM 的仪表板或 API：

bashCopy code
[code]
    # 密钥信息curl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # 支出日志curl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

代理行为说明

  * LiteLLM 默认运行在 `http://localhost:4000`
  * OpenClaw 通过 LiteLLM 的代理式、兼容 OpenAI 的 `/v1` 端点进行连接
  * 原生仅限 OpenAI 的请求整形不会通过 LiteLLM 生效： 不支持 `service_tier`、Responses `store`、prompt-cache 提示，也不支持 OpenAI reasoning 兼容载荷整形
  * 在自定义 LiteLLM base URL 上，不会注入隐藏的 OpenClaw 归因请求头（`originator`、`version`、`User-Agent`）


## 相关内容

[**LiteLLM 文档** LiteLLM 官方文档和 API 参考。 ](<https://docs.litellm.ai>) [**模型选择** 所有 provider、模型引用和故障转移行为的概览。 ](</zh-CN/concepts/model-providers>) [**配置** 完整配置参考。 ](</zh-CN/gateway/configuration>) [**模型选择** 如何选择和配置模型。 ](</zh-CN/concepts/models>)

Was this useful?YesNo