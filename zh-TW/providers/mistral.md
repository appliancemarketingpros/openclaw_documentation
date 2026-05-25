---
title: Mistral
source_url: https://docs.openclaw.ai/zh-TW/providers/mistral
scraped_at: 2026-05-25
---

OpenClaw 包含一個內建的 Mistral Plugin，會註冊四種合約：聊天補全、媒體理解（Voxtral 批次轉錄）、Voice Call 即時 STT（Voxtral Realtime），以及記憶嵌入（`mistral-embed`）。

屬性 | 值  
---|---  
Provider id | `mistral`  
Plugin | 內建，`enabledByDefault: true`  
驗證環境變數 | `MISTRAL_API_KEY`  
Onboarding 旗標 | `--auth-choice mistral-api-key`  
直接 CLI 旗標 | `--mistral-api-key <key>`  
API | OpenAI 相容（`openai-completions`）  
基礎 URL | `https://api.mistral.ai/v1`  
預設模型 | `mistral/mistral-large-latest`  
嵌入模型 | `mistral-embed`  
Voxtral 批次 | `voxtral-mini-latest`（音訊轉錄）  
Voxtral 即時 | `voxtral-mini-transcribe-realtime-2602`  
  
## 開始使用

* ### 取得你的 API 金鑰

在 [Mistral Console](<https://console.mistral.ai/>) 建立 API 金鑰。

* ### 執行 onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice mistral-api-key
[/code]

或直接傳入金鑰：

bashCopy code
[code]
    openclaw onboard --mistral-api-key "$MISTRAL_API_KEY"
[/code]

* ### 設定預設模型

json5Copy code
[code]
    {  env: { MISTRAL_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "mistral/mistral-large-latest" } } },}
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider mistral
[/code]

## 內建 LLM 目錄

[Mistral Medium 3.5](<https://docs.mistral.ai/models/model-cards/mistral-medium-3-5-26-04>) 是內建目錄中目前的混合 Medium 模型：128B 密集權重、 文字與影像輸入、256K 上下文、函式呼叫、結構化輸出、程式編寫， 並可透過 Chat Completions API 調整推理。當你想使用 Mistral 較新的統一 代理式/程式編寫模型，而不是預設的 `mistral/mistral-large-latest` 時，請使用 `mistral/mistral-medium-3-5`。

OpenClaw 目前隨附這個內建 Mistral 目錄：

模型參照 | 輸入 | 上下文 | 最大輸出 | 備註  
---|---|---|---|---  
`mistral/mistral-large-latest` | 文字、影像 | 262,144 | 16,384 | 預設模型  
`mistral/mistral-medium-2508` | 文字、影像 | 262,144 | 8,192 | Mistral Medium 3.1  
`mistral/mistral-medium-3-5` | 文字、影像 | 262,144 | 8,192 | Mistral Medium 3.5；可調整推理  
`mistral/mistral-small-latest` | 文字、影像 | 128,000 | 16,384 | Mistral Small 4；透過 API `reasoning_effort` 可調整推理  
`mistral/pixtral-large-latest` | 文字、影像 | 128,000 | 32,768 | Pixtral  
`mistral/codestral-latest` | 文字 | 256,000 | 4,096 | 程式編寫  
`mistral/devstral-medium-latest` | 文字 | 262,144 | 32,768 | Devstral 2  
`mistral/magistral-small` | 文字 | 128,000 | 40,000 | 已啟用推理  
  
Onboarding 後，在不啟動 Gateway 的情況下對 Medium 3.5 執行煙霧測試：

bashCopy code
[code]
    openclaw infer model run --local \  --model mistral/mistral-medium-3-5 \  --prompt "Reply with exactly: mistral-ok" \  --json
[/code]

在變更設定前瀏覽內建目錄列：

bashCopy code
[code]
    openclaw models list --all --provider mistral --plain
[/code]

## 音訊轉錄（Voxtral）

透過媒體理解管線使用 Voxtral 進行批次音訊轉錄。

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "mistral", model: "voxtral-mini-latest" }],      },    },  },}
[/code]

## Voice Call 串流 STT

內建的 `mistral` Plugin 會將 Voxtral Realtime 註冊為 Voice Call 串流 STT 提供者。

設定 | 設定路徑 | 預設  
---|---|---  
API 金鑰 | `plugins.entries.voice-call.config.streaming.providers.mistral.apiKey` | 退回使用 `MISTRAL_API_KEY`  
模型 | `...mistral.model` | `voxtral-mini-transcribe-realtime-2602`  
編碼 | `...mistral.encoding` | `pcm_mulaw`  
取樣率 | `...mistral.sampleRate` | `8000`  
目標延遲 | `...mistral.targetStreamingDelayMs` | `800`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "mistral",            providers: {              mistral: {                apiKey: "${MISTRAL_API_KEY}",                targetStreamingDelayMs: 800,              },            },          },        },      },    },  },}
[/code]

## 進階設定

可調整推理

`mistral/mistral-small-latest`（Mistral Small 4）和 `mistral/mistral-medium-3-5` 支援在 Chat Completions API 上透過 `reasoning_effort` 使用[可調整推理](<https://docs.mistral.ai/studio-api/conversations/reasoning/adjustable>)（`none` 會盡量減少輸出中的額外思考；`high` 會在最終答案前顯示完整思考軌跡）。Mistral 建議在 Medium 3.5 代理式和程式碼使用案例中使用 `reasoning_effort="high"`。

OpenClaw 會將工作階段的 **thinking** 等級對應到 Mistral 的 API：

OpenClaw thinking 等級 | Mistral `reasoning_effort`  
---|---  
**off** / **minimal** | `none`  
**low** / **medium** / **high** / **xhigh** / **adaptive** / **max** | `high`  
  
Medium 3.5 推理的模型範圍設定範例：

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "mistral/mistral-medium-3-5" },      models: {        "mistral/mistral-medium-3-5": {          params: { thinking: "high" },        },      },    },  },}
[/code]

記憶嵌入

Mistral 可以透過 `/v1/embeddings` 提供記憶嵌入（預設模型：`mistral-embed`）。

json5Copy code
[code]
    {  memorySearch: { provider: "mistral" },}
[/code]

驗證與基礎 URL

  * Mistral 驗證使用 `MISTRAL_API_KEY`（Bearer 標頭）。
  * 提供者基礎 URL 預設為 `https://api.mistral.ai/v1`，並接受標準 OpenAI 相容的 chat-completions 請求形狀。
  * Onboarding 預設模型是 `mistral/mistral-large-latest`。
  * 只有在 Mistral 明確發布你需要的區域端點時，才覆寫 `models.providers.mistral.baseUrl` 底下的基礎 URL。


## 相關

[**模型選擇** 選擇提供者、模型參照與容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**媒體理解** 音訊轉錄設定與提供者選擇。 ](</zh-TW/nodes/media-understanding>)

Was this useful?YesNo