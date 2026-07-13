---
title: 中繼資料
source_url: https://docs.openclaw.ai/zh-TW/providers/meta
scraped_at: 2026-07-13
---

ModelsProviders

**Meta API** 使用與 OpenAI 相容的 **Responses API** （`POST /v1/responses`） 來支援 `muse-spark-1.1` 推理模型。此供應商隨附為 OpenClaw 內建外掛。

屬性 | 值  
---|---  
供應商 ID | `meta`  
外掛 | 內建供應商  
驗證環境變數 | `MODEL_API_KEY`  
初始設定旗標 | `--auth-choice meta-api-key`  
直接命令列介面旗標 | `--meta-api-key <key>`  
API | Responses API (`openai-responses`)  
基底 URL | `https://api.meta.ai/v1`  
預設模型 | `meta/muse-spark-1.1`  
預設推理強度 | `high` (`reasoning.effort`)  
  
## 開始使用

* ### 設定 API 金鑰

初始設定Copy code
[code]
    openclaw onboard --auth-choice meta-api-key
[/code]

直接旗標Copy code
[code]
    openclaw onboard --non-interactive --accept-risk \--auth-choice meta-api-key \--meta-api-key "$MODEL_API_KEY"
[/code]

僅使用環境變數Copy code
[code]
    export MODEL_API_KEY=<key>
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider meta
[/code]

列出靜態的 `muse-spark-1.1` 目錄項目。如果無法解析 `MODEL_API_KEY`， `openclaw models status --json` 會在 `auth.unusableProfiles` 下回報缺少的憑證。

## 非互動式設定

bashCopy code
[code]
    openclaw onboard --non-interactive --accept-risk \  --mode local \  --auth-choice meta-api-key \  --meta-api-key "$MODEL_API_KEY"
[/code]

## 內建目錄

模型參照 | 名稱 | 推理 | 上下文視窗 | 最大輸出  
---|---|---|---|---  
`meta/muse-spark-1.1` | Muse Spark 1.1 | 是 | 1,048,576 | 131,072  
  
功能：

  * 文字與圖片輸入
  * 工具呼叫與串流
  * 推理強度：`minimal`、`low`、`medium`、`high`、`xhigh`（預設：`high`）
  * 無狀態加密推理重播（`store: false`、`include: ["reasoning.encrypted_content"]`）


## 手動設定

json5Copy code
[code]
    {  env: { MODEL_API_KEY: "<key>" },  agents: {    defaults: {      model: { primary: "meta/muse-spark-1.1" },      models: {        "meta/muse-spark-1.1": { alias: "Muse Spark 1.1" },      },    },  },}
[/code]

## 冒煙測試

bashCopy code
[code]
    export MODEL_API_KEY=<key>pnpm test:live -- extensions/meta/meta.live.test.ts
[/code]

即時測試會使用 `muse-spark-1.1` 對 `POST /v1/responses` 執行測試。

## 相關內容

[**模型供應商** 選擇供應商、模型參照與容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**思考模式** muse-spark-1.1 的推理強度等級。 ](</zh-TW/tools/thinking>) [**設定參考** 代理程式預設值與模型設定。 ](</zh-TW/gateway/config-agents#agent-defaults>)

Was this useful?YesNo

Open issue