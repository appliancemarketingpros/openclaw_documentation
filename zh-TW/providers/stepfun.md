---
title: StepFun
source_url: https://docs.openclaw.ai/zh-TW/providers/stepfun
scraped_at: 2026-05-25
---

OpenClaw 包含一個內建的 StepFun 供應商 Plugin，具備兩個供應商 ID：

  * `stepfun` 用於標準端點
  * `stepfun-plan` 用於 Step Plan 端點


## 區域與端點概覽

端點 | 中國 (`.com`) | 全球 (`.ai`)  
---|---|---  
標準 | `https://api.stepfun.com/v1` | `https://api.stepfun.ai/v1`  
Step Plan | `https://api.stepfun.com/step_plan/v1` | `https://api.stepfun.ai/step_plan/v1`  
  
驗證環境變數：`STEPFUN_API_KEY`

## 內建目錄

標準 (`stepfun`)：

模型 ref | Context | 最大輸出 | 備註  
---|---|---|---  
`stepfun/step-3.5-flash` | 262,144 | 65,536 | 預設標準模型  
  
Step Plan (`stepfun-plan`)：

模型 ref | Context | 最大輸出 | 備註  
---|---|---|---  
`stepfun-plan/step-3.5-flash` | 262,144 | 65,536 | 預設 Step Plan 模型  
`stepfun-plan/step-3.5-flash-2603` | 262,144 | 65,536 | 額外的 Step Plan 模型  
  
## 開始使用

選擇你的供應商介面，並依照設定步驟操作。

### 標準

**最適合：**透過標準 StepFun 端點進行一般用途使用。

* ### 選擇你的端點區域

驗證選項 | 端點 | 區域  
---|---|---  
`stepfun-standard-api-key-intl` | `https://api.stepfun.ai/v1` | 國際  
`stepfun-standard-api-key-cn` | `https://api.stepfun.com/v1` | 中國  
* ### 執行 onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl
[/code]

或使用中國端點：

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-cn
[/code]

* ### 非互動式替代方案

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-standard-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider stepfun
[/code]

### 模型 ref

  * 預設模型：`stepfun/step-3.5-flash`


### Step Plan

**最適合：**Step Plan 推理端點。

* ### 選擇你的端點區域

驗證選項 | 端點 | 區域  
---|---|---  
`stepfun-plan-api-key-intl` | `https://api.stepfun.ai/step_plan/v1` | 國際  
`stepfun-plan-api-key-cn` | `https://api.stepfun.com/step_plan/v1` | 中國  
* ### 執行 onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl
[/code]

或使用中國端點：

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-cn
[/code]

* ### 非互動式替代方案

bashCopy code
[code]
    openclaw onboard --auth-choice stepfun-plan-api-key-intl \  --stepfun-api-key "$STEPFUN_API_KEY"
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider stepfun-plan
[/code]

### 模型 ref

  * 預設模型：`stepfun-plan/step-3.5-flash`
  * 替代模型：`stepfun-plan/step-3.5-flash-2603`


## 進階設定

完整設定：標準供應商 json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      stepfun: {        baseUrl: "https://api.stepfun.ai/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

完整設定：Step Plan 供應商 json5Copy code
[code]
    {  env: { STEPFUN_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "stepfun-plan/step-3.5-flash" } } },  models: {    mode: "merge",    providers: {      "stepfun-plan": {        baseUrl: "https://api.stepfun.ai/step_plan/v1",        api: "openai-completions",        apiKey: "${STEPFUN_API_KEY}",        models: [          {            id: "step-3.5-flash",            name: "Step 3.5 Flash",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },          {            id: "step-3.5-flash-2603",            name: "Step 3.5 Flash 2603",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 65536,          },        ],      },    },  },}
[/code]

備註

  * 此供應商已內建於 OpenClaw，因此沒有單獨的 Plugin 安裝步驟。
  * `step-3.5-flash-2603` 目前僅在 `stepfun-plan` 上公開。
  * 單一驗證流程會為 `stepfun` 與 `stepfun-plan` 寫入符合區域的設定檔，因此兩個介面可以一起被探索到。
  * 使用 `openclaw models list` 與 `openclaw models set <provider/model>` 來檢查或切換模型。


## 相關

[**模型選擇** 所有供應商、模型 ref 與容錯移轉行為的概覽。 ](</zh-TW/concepts/model-providers>) [**設定參考** 供應商、模型與 Plugin 的完整設定結構描述。 ](</zh-TW/gateway/configuration-reference>) [**模型選擇** 如何選擇與設定模型。 ](</zh-TW/concepts/models>) [**StepFun Platform** StepFun API 金鑰管理與文件。 ](<https://platform.stepfun.com>)

Was this useful?YesNo