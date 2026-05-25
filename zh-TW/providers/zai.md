---
title: Z.AI
source_url: https://docs.openclaw.ai/zh-TW/providers/zai
scraped_at: 2026-05-25
---

[Z.AI](<http://Z.AI>) 是 **GLM** 模型的 API 平台。它為 GLM 提供 REST API，並使用 API 金鑰 進行驗證。請在 [Z.AI](<http://Z.AI>) 主控台中建立你的 API 金鑰。OpenClaw 會搭配 [Z.AI](<http://Z.AI>) API 金鑰使用 `zai` 提供者。

  * 提供者：`zai`
  * 驗證：`ZAI_API_KEY`
  * API：[Z.AI](<http://Z.AI>) Chat Completions（Bearer 驗證）


## 開始使用

### 自動偵測端點

**最適合：**大多數使用者。OpenClaw 會從金鑰偵測相符的 [Z.AI](<http://Z.AI>) 端點，並自動套用正確的基底 URL。

* ### 執行初始設定

bashCopy code
[code]
    openclaw onboard --auth-choice zai-api-key
[/code]

* ### 設定預設模型

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### 確認模型已列出

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

### 明確指定區域端點

**最適合：**想要強制使用特定 Coding Plan 或一般 API 介面的使用者。

* ### 選擇正確的初始設定選項

bashCopy code
[code]
    # Coding Plan Global (recommended for Coding Plan users)openclaw onboard --auth-choice zai-coding-global # Coding Plan CN (China region)openclaw onboard --auth-choice zai-coding-cn # General APIopenclaw onboard --auth-choice zai-global # General API CN (China region)openclaw onboard --auth-choice zai-cn
[/code]

* ### 設定預設模型

json5Copy code
[code]
    {  env: { ZAI_API_KEY: "sk-..." },  agents: { defaults: { model: { primary: "zai/glm-5.1" } } },}
[/code]

* ### 確認模型已列出

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

## 內建目錄

OpenClaw 會在 Plugin manifest 中隨附內建的 `zai` 提供者目錄，因此唯讀 清單可以在不載入提供者執行階段的情況下顯示已知的 GLM 列：

bashCopy code
[code]
    openclaw models list --all --provider zai
[/code]

目前由 manifest 支援的目錄包含：

模型參照 | 備註  
---|---  
`zai/glm-5.1` | 預設模型  
`zai/glm-5` |   
`zai/glm-5-turbo` |   
`zai/glm-5v-turbo` |   
`zai/glm-4.7` |   
`zai/glm-4.7-flash` |   
`zai/glm-4.7-flashx` |   
`zai/glm-4.6` |   
`zai/glm-4.6v` |   
`zai/glm-4.5` |   
`zai/glm-4.5-air` |   
`zai/glm-4.5-flash` |   
`zai/glm-4.5v` |   
  
## 進階設定

向前解析未知的 GLM-5 模型

未知的 `glm-5*` ID 仍會在內建提供者路徑上向前解析；當 ID 符合目前 GLM-5 系列形態時，會從 `glm-4.7` 範本合成提供者擁有的中繼資料。

工具呼叫串流

[Z.AI](<http://Z.AI>) 工具呼叫串流預設啟用 `tool_stream`。若要停用它：

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/<model>": {          params: { tool_stream: false },        },      },    },  },}
[/code]

思考與保留思考

[Z.AI](<http://Z.AI>) 思考會遵循 OpenClaw 的 `/think` 控制。關閉思考時， OpenClaw 會傳送 `thinking: { type: "disabled" }`，避免回應在顯示文字前 將輸出預算花在 `reasoning_content` 上。

保留思考需要選擇啟用，因為 [Z.AI](<http://Z.AI>) 要求重播完整歷史 `reasoning_content`，這會增加提示 token。請依模型啟用：

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "zai/glm-5.1": {          params: { preserveThinking: true },        },      },    },  },}
[/code]

啟用後且思考開啟時，OpenClaw 會傳送 `thinking: { type: "enabled", clear_thinking: false }`，並為相同的 OpenAI 相容逐字稿重播先前的 `reasoning_content`。

進階使用者仍可使用 `params.extra_body.thinking` 覆寫確切的提供者酬載。

影像理解

內建的 [Z.AI](<http://Z.AI>) Plugin 會註冊影像理解。

屬性 | 值  
---|---  
模型 | `glm-4.6v`  
  
影像理解會從已設定的 [Z.AI](<http://Z.AI>) 驗證自動解析，不需要 額外設定。

驗證詳細資料

  * [Z.AI](<http://Z.AI>) 會使用你的 API 金鑰進行 Bearer 驗證。
  * `zai-api-key` 初始設定選項會從金鑰前綴自動偵測相符的 [Z.AI](<http://Z.AI>) 端點。
  * 當你想強制使用特定 API 介面時，請使用明確的區域選項（`zai-coding-global`、`zai-coding-cn`、`zai-global`、`zai-cn`）。


## 相關

[**GLM 模型系列** GLM 的模型系列概覽。 ](</zh-TW/providers/glm>) [**模型選擇** 選擇提供者、模型參照與容錯移轉行為。 ](</zh-TW/concepts/model-providers>)

Was this useful?YesNo