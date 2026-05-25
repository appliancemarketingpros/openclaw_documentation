---
title: vLLM
source_url: https://docs.openclaw.ai/zh-TW/providers/vllm
scraped_at: 2026-05-25
---

vLLM 可以透過 **OpenAI 相容** HTTP API 提供開放原始碼（以及部分自訂）模型。OpenClaw 會使用 `openai-completions` API 連接到 vLLM。

當你選擇啟用 `VLLM_API_KEY` 時，OpenClaw 也可以從 vLLM **自動探索** 可用模型（如果你的伺服器未強制驗證，任何值都可以）。在 `agents.defaults.models` 中使用 `vllm/*`，可在同時設定自訂 vLLM 基礎 URL 時，讓探索保持動態。

OpenClaw 會將 `vllm` 視為支援串流使用量計算的本機 OpenAI 相容供應商，因此狀態/內容 Token 計數可以從 `stream_options.include_usage` 回應更新。

屬性 | 值  
---|---  
供應商 ID | `vllm`  
API | `openai-completions`（OpenAI 相容）  
驗證 | `VLLM_API_KEY` 環境變數  
預設基礎 URL | `http://127.0.0.1:8000/v1`  
  
## 開始使用

* ### 使用 OpenAI 相容伺服器啟動 vLLM

你的基礎 URL 應公開 `/v1` 端點（例如 `/v1/models`、`/v1/chat/completions`）。vLLM 通常執行於：

CodeCopy code
[code]
    http://127.0.0.1:8000/v1
[/code]

* ### 設定 API 金鑰環境變數

如果你的伺服器未強制驗證，任何值都可以：

bashCopy code
[code]
    export VLLM_API_KEY="vllm-local"
[/code]

* ### 選取模型

請替換為你的其中一個 vLLM 模型 ID：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "vllm/your-model-id" },    },  },}
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

## 模型探索（隱含供應商）

當已設定 `VLLM_API_KEY`（或存在驗證設定檔），且你**未** 定義 `models.providers.vllm` 時，OpenClaw 會查詢：

CodeCopy code
[code]
    GET http://127.0.0.1:8000/v1/models
[/code]

並將傳回的 ID 轉換為模型項目。

## 明確設定（手動模型）

在下列情況使用明確設定：

  * vLLM 執行於不同主機或連接埠
  * 你想固定 `contextWindow` 或 `maxTokens` 值
  * 你的伺服器需要真正的 API 金鑰（或你想控制標頭）
  * 你連接到受信任的迴環、LAN 或 Tailscale vLLM 端點

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://127.0.0.1:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300, // Optional: extend connect/header/body/request timeout for slow local models        models: [          {            id: "your-model-id",            name: "Local vLLM Model",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 128000,            maxTokens: 8192,          },        ],      },    },  },}
[/code]

若要讓此供應商保持動態，而不必手動列出每個模型，請將供應商萬用字元加入可見模型目錄：

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/*": {},      },    },  },}
[/code]

## 進階設定

代理樣式行為

vLLM 會被視為代理樣式的 OpenAI 相容 `/v1` 後端，而不是原生 OpenAI 端點。這表示：

行為 | 是否套用？  
---|---  
原生 OpenAI 請求塑形 | 否  
`service_tier` | 不傳送  
Responses `store` | 不傳送  
提示快取提示 | 不傳送  
OpenAI 推理相容酬載塑形 | 不套用  
隱藏的 OpenClaw 歸因標頭 | 不會注入自訂基礎 URL  
Qwen 思考控制

對於透過 vLLM 提供的 Qwen 模型，當伺服器預期使用 Qwen 聊天範本 kwargs 時，請在模型項目上設定 `params.qwenThinkingFormat: "chat-template"`。OpenClaw 會將 `/think off` 對應為：

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "preserve_thinking": true  }}
[/code]

非 `off` 的思考等級會傳送 `enable_thinking: true`。如果你的端點預期改用 DashScope 樣式的頂層旗標，請使用 `params.qwenThinkingFormat: "top-level"`，將 `enable_thinking` 傳送到請求根層級。也接受 snake-case 的 `params.qwen_thinking_format`。

Nemotron 3 思考控制

vLLM/Nemotron 3 可以使用聊天範本 kwargs 來控制推理是以隱藏推理還是可見答案文字傳回。當 OpenClaw 工作階段在關閉思考時使用 `vllm/nemotron-3-*`，隨附的 vLLM Plugin 會傳送：

jsonCopy code
[code]
    {  "chat_template_kwargs": {    "enable_thinking": false,    "force_nonempty_content": true  }}
[/code]

若要自訂這些值，請在模型參數下設定 `chat_template_kwargs`。如果你也設定 `params.extra_body.chat_template_kwargs`，該值會具有最終優先權，因為 `extra_body` 是最後的請求主體覆寫。

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/nemotron-3-super": {          params: {            chat_template_kwargs: {              enable_thinking: false,              force_nonempty_content: true,            },          },        },      },    },  },}
[/code]

Qwen 工具呼叫顯示為文字

首先確認 vLLM 已使用適合該模型的正確工具呼叫剖析器與聊天範本啟動。例如，vLLM 文件指出 Qwen2.5 模型使用 `hermes`，Qwen3-Coder 模型使用 `qwen3_xml`。

症狀：

  * Skills 或工具從未執行
  * 助理列印原始 JSON/XML，例如 `{"name":"read","arguments":...}`
  * 當 OpenClaw 傳送 `tool_choice: "auto"` 時，vLLM 傳回空的 `tool_calls` 陣列


有些 Qwen/vLLM 組合只有在請求使用 `tool_choice: "required"` 時才會傳回結構化工具呼叫。對於這些模型項目，請使用 `params.extra_body` 強制 OpenAI 相容請求欄位：

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "vllm/Qwen-Qwen2.5-Coder-32B-Instruct": {          params: {            extra_body: {              tool_choice: "required",            },          },        },      },    },  },}
[/code]

將 `Qwen-Qwen2.5-Coder-32B-Instruct` 替換為下列命令傳回的確切 ID：

bashCopy code
[code]
    openclaw models list --provider vllm
[/code]

你也可以從 CLI 套用相同覆寫：

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"vllm/Qwen-Qwen2.5-Coder-32B-Instruct":{"params":{"extra_body":{"tool_choice":"required"}}}}' --strict-json --merge
[/code]

這是一個選擇啟用的相容性因應方案。它會讓每次帶有工具的模型回合都需要工具呼叫，因此只應用於該行為可接受的專用本機模型項目。請勿將它作為所有 vLLM 模型的全域預設值，也不要使用會盲目將任意助理文字轉換為可執行工具呼叫的代理。

自訂基礎 URL

如果你的 vLLM 伺服器執行於非預設主機或連接埠，請在明確供應商設定中設定 `baseUrl`：

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:9000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [          {            id: "my-custom-model",            name: "Remote vLLM Model",            reasoning: false,            input: ["text"],            contextWindow: 64000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## 疑難排解

首次回應緩慢或遠端伺服器逾時

對於大型本機模型、遠端 LAN 主機或 tailnet 連結，請設定供應商範圍的請求逾時：

json5Copy code
[code]
    {  models: {    providers: {      vllm: {        baseUrl: "http://192.168.1.50:8000/v1",        apiKey: "${VLLM_API_KEY}",        api: "openai-completions",        request: { allowPrivateNetwork: true },        timeoutSeconds: 300,        models: [{ id: "your-model-id", name: "Local vLLM Model" }],      },    },  },}
[/code]

`timeoutSeconds` 僅套用於 vLLM 模型 HTTP 請求，包括連線設定、回應標頭、主體串流，以及整體受保護 fetch 中止。請優先使用此設定，再考慮增加控制整個 Agent 執行的 `agents.defaults.timeoutSeconds`。

無法連上伺服器

檢查 vLLM 伺服器是否正在執行且可存取：

bashCopy code
[code]
    curl http://127.0.0.1:8000/v1/models
[/code]

如果看到連線錯誤，請確認主機、連接埠，以及 vLLM 是否以 OpenAI 相容伺服器模式啟動。 對於明確的迴環、LAN 或 Tailscale 端點，也請設定 `models.providers.vllm.request.allowPrivateNetwork: true`；除非供應商被明確信任，否則供應商請求預設會封鎖私人網路 URL。

請求發生驗證錯誤

如果請求因驗證錯誤而失敗，請設定符合你伺服器設定的真實 `VLLM_API_KEY`，或在 `models.providers.vllm` 下明確設定供應商。

未探索到模型

自動探索需要設定 `VLLM_API_KEY`。如果你已定義 `models.providers.vllm`，除非 `agents.defaults.models` 包含 `"vllm/*": {}`，否則 OpenClaw 只會使用你宣告的模型。

工具呈現為原始文字

如果 Qwen 模型列印 JSON/XML 工具語法而不是執行 Skill，請查看上方進階設定中的 Qwen 指引。通常的修正方式是：

  * 使用該模型的正確剖析器/範本啟動 vLLM
  * 使用 `openclaw models list --provider vllm` 確認確切模型 ID
  * 只有在 `tool_choice: "auto"` 仍傳回空白或純文字工具呼叫時，才加入專用的個別模型 `params.extra_body.tool_choice: "required"` 覆寫


## 相關

[**模型選擇** 選擇供應商、模型參照與容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**OpenAI** 原生 OpenAI 供應商與 OpenAI 相容路由行為。 ](</zh-TW/providers/openai>) [**OAuth 和驗證** 驗證詳細資訊與憑證重用規則。 ](</zh-TW/gateway/authentication>) [**疑難排解** 常見問題及其解決方式。 ](</zh-TW/help/troubleshooting>)

Was this useful?YesNo