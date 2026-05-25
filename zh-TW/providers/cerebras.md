---
title: Cerebras
source_url: https://docs.openclaw.ai/zh-TW/providers/cerebras
scraped_at: 2026-05-25
---

[Cerebras](<https://www.cerebras.ai>) 在自訂推論硬體上提供高速、與 OpenAI 相容的推論。OpenClaw 包含一個內建的 Cerebras 提供者 Plugin，並附有靜態四模型目錄。

屬性 | 值  
---|---  
提供者 ID | `cerebras`  
Plugin | 內建，`enabledByDefault: true`  
驗證環境變數 | `CEREBRAS_API_KEY`  
入門設定旗標 | `--auth-choice cerebras-api-key`  
直接 CLI 旗標 | `--cerebras-api-key <key>`  
API | 與 OpenAI 相容 (`openai-completions`)  
基底 URL | `https://api.cerebras.ai/v1`  
預設模型 | `cerebras/zai-glm-4.7`  
  
## 開始使用

* ### 取得 API 金鑰

在 [Cerebras Cloud Console](<https://cloud.cerebras.ai>) 建立 API 金鑰。

* ### 執行入門設定

入門設定Copy code
[code]
    openclaw onboard --auth-choice cerebras-api-key
[/code]

直接旗標Copy code
[code]
    openclaw onboard --non-interactive \--auth-choice cerebras-api-key \--cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

僅環境變數Copy code
[code]
    export CEREBRAS_API_KEY=csk-...
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider cerebras
[/code]

清單應包含全部四個內建模型。如果無法解析 `CEREBRAS_API_KEY`，`openclaw models status --json` 會在 `auth.unusableProfiles` 下回報缺少的認證。

## 非互動式設定

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice cerebras-api-key \  --cerebras-api-key "$CEREBRAS_API_KEY"
[/code]

## 內建目錄

OpenClaw 隨附靜態 Cerebras 目錄，對應公開的 OpenAI 相容端點。全部四個模型都共用 128k 上下文和 8,192 個最大輸出 Token。

模型參照 | 名稱 | 推理 | 備註  
---|---|---|---  
`cerebras/zai-glm-4.7` | [Z.ai](<http://Z.ai>) GLM 4.7 | 是 | 預設模型；預覽版推理模型  
`cerebras/gpt-oss-120b` | GPT OSS 120B | 是 | 生產用推理模型  
`cerebras/qwen-3-235b-a22b-instruct-2507` | Qwen 3 235B Instruct | 否 | 預覽版非推理模型  
`cerebras/llama3.1-8b` | Llama 3.1 8B | 否 | 生產用速度導向模型  
  
## 手動設定

內建 Plugin 通常表示你只需要 API 金鑰。當你想覆寫模型中繼資料，或在 `mode: "merge"` 下搭配靜態目錄執行時，請使用明確的 `models.providers.cerebras` 設定：

json5Copy code
[code]
    {  env: { CEREBRAS_API_KEY: "csk-..." },  agents: {    defaults: {      model: { primary: "cerebras/zai-glm-4.7" },    },  },  models: {    mode: "merge",    providers: {      cerebras: {        baseUrl: "https://api.cerebras.ai/v1",        apiKey: "${CEREBRAS_API_KEY}",        api: "openai-completions",        models: [          { id: "zai-glm-4.7", name: "Z.ai GLM 4.7" },          { id: "gpt-oss-120b", name: "GPT OSS 120B" },        ],      },    },  },}
[/code]

## 相關

[**模型提供者** 選擇提供者、模型參照和容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**思考模式** 適用於兩個支援推理的 Cerebras 模型的推理投入等級。 ](</zh-TW/tools/thinking>) [**設定參考** Agent 預設值和模型設定。 ](</zh-TW/gateway/config-agents#agent-defaults>) [**模型常見問題** 驗證設定檔、切換模型，以及解決「沒有設定檔」錯誤。 ](</zh-TW/help/faq-models>)

Was this useful?YesNo