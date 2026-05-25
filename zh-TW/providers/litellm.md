---
title: LiteLLM
source_url: https://docs.openclaw.ai/zh-TW/providers/litellm
scraped_at: 2026-05-25
---

[LiteLLM](<https://litellm.ai>) 是一個開源 LLM Gateway，提供統一 API，可連接 100 多個模型供應商。透過 LiteLLM 路由 OpenClaw，即可取得集中式成本追蹤、記錄功能，以及在不變更 OpenClaw 設定的情況下切換後端的彈性。

## 快速開始

### Onboarding (recommended)

**最適合：**最快完成可用 LiteLLM 設定的路徑。

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice litellm-api-key
[/code]

若要針對遠端 Proxy 進行非互動式設定，請明確傳入 Proxy URL：

bashCopy code
[code]
    openclaw onboard --non-interactive --auth-choice litellm-api-key --litellm-api-key "$LITELLM_API_KEY" --custom-base-url "https://litellm.example/v1"
[/code]

### Manual setup

**最適合：**完整掌控安裝與設定。

* ### Start LiteLLM Proxy

bashCopy code
[code]
    pip install 'litellm[proxy]'litellm --model claude-opus-4-6
[/code]

* ### Point OpenClaw to LiteLLM

bashCopy code
[code]
    export LITELLM_API_KEY="your-litellm-key" openclaw
[/code]

就這樣。OpenClaw 現在會透過 LiteLLM 路由。

## 設定

### 環境變數

bashCopy code
[code]
    export LITELLM_API_KEY="sk-litellm-key"
[/code]

### 設定檔

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",        api: "openai-completions",        models: [          {            id: "claude-opus-4-6",            name: "Claude Opus 4.6",            reasoning: true,            input: ["text", "image"],            contextWindow: 200000,            maxTokens: 64000,          },          {            id: "gpt-4o",            name: "GPT-4o",            reasoning: false,            input: ["text", "image"],            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "litellm/claude-opus-4-6" },    },  },}
[/code]

## 進階設定

### 圖片生成

LiteLLM 也可以透過 OpenAI 相容的 `/images/generations` 和 `/images/edits` 路由，支援 OpenClaw 的 `image_generate` 工具。請在 `agents.defaults.imageGenerationModel` 下設定 LiteLLM 圖片模型：

json5Copy code
[code]
    {  models: {    providers: {      litellm: {        baseUrl: "http://localhost:4000",        apiKey: "${LITELLM_API_KEY}",      },    },  },  agents: {    defaults: {      imageGenerationModel: {        primary: "litellm/gpt-image-2",        timeoutMs: 180_000,      },    },  },}
[/code]

像 `http://localhost:4000` 這類 Loopback LiteLLM URL 無需全域 私有網路覆寫即可運作。若是 LAN 託管的 Proxy，請設定 `models.providers.litellm.request.allowPrivateNetwork: true`，因為 API 金鑰 會被送到已設定的 Proxy 主機。

Virtual keys

為 OpenClaw 建立具有花費上限的專用金鑰：

bashCopy code
[code]
    curl -X POST "http://localhost:4000/key/generate" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY" \  -H "Content-Type: application/json" \  -d '{    "key_alias": "openclaw",    "max_budget": 50.00,    "budget_duration": "monthly"  }'
[/code]

將產生的金鑰用作 `LITELLM_API_KEY`。

Model routing

LiteLLM 可以將模型請求路由到不同後端。請在你的 LiteLLM `config.yaml` 中設定：

yamlCopy code
[code]
    model_list:  - model_name: claude-opus-4-6    litellm_params:      model: claude-opus-4-6      api_key: os.environ/ANTHROPIC_API_KEY   - model_name: gpt-4o    litellm_params:      model: gpt-4o      api_key: os.environ/OPENAI_API_KEY
[/code]

OpenClaw 會持續請求 `claude-opus-4-6` — LiteLLM 負責處理路由。

Viewing usage

查看 LiteLLM 的儀表板或 API：

bashCopy code
[code]
    # Key infocurl "http://localhost:4000/key/info" \  -H "Authorization: Bearer sk-litellm-key" # Spend logscurl "http://localhost:4000/spend/logs" \  -H "Authorization: Bearer $LITELLM_MASTER_KEY"
[/code]

Proxy behavior notes

  * LiteLLM 預設在 `http://localhost:4000` 上執行
  * OpenClaw 會透過 LiteLLM Proxy 風格、OpenAI 相容的 `/v1` 端點連線
  * 原生 OpenAI 專用的請求塑形不會透過 LiteLLM 套用： 沒有 `service_tier`、沒有 Responses `store`、沒有提示快取提示，也沒有 OpenAI reasoning 相容酬載塑形
  * 自訂 LiteLLM base URL 不會注入隱藏的 OpenClaw 歸因標頭（`originator`、`version`、`User-Agent`）


## 相關

[**LiteLLM Docs** 官方 LiteLLM 文件與 API 參考。 ](<https://docs.litellm.ai>) [**Model selection** 所有供應商、模型參照與故障轉移行為的概覽。 ](</zh-TW/concepts/model-providers>) [**Configuration** 完整設定參考。 ](</zh-TW/gateway/configuration>) [**Model selection** 如何選擇並設定模型。 ](</zh-TW/concepts/models>)

Was this useful?YesNo