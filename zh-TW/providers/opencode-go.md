---
title: OpenCode Go
source_url: https://docs.openclaw.ai/zh-TW/providers/opencode-go
scraped_at: 2026-05-25
---

OpenCode Go 是 [OpenCode](</zh-TW/providers/opencode>) 內的 Go 目錄。 它使用與 Zen 目錄相同的 `OPENCODE_API_KEY`，但保留執行階段 提供者 ID `opencode-go`，讓上游逐模型路由保持正確。

屬性 | 值  
---|---  
執行階段提供者 | `opencode-go`  
驗證 | `OPENCODE_API_KEY`  
上層設定 | [OpenCode](</zh-TW/providers/opencode>)  
  
## 內建目錄

OpenClaw 從隨附的 Pi 模型登錄檔取得大多數 Go 目錄列，並在登錄檔追上前 補充目前的上游列。執行 `openclaw models list --provider opencode-go` 以查看目前的模型清單。

此提供者包含：

模型參照 | 名稱  
---|---  
`opencode-go/glm-5` | GLM-5  
`opencode-go/glm-5.1` | GLM-5.1  
`opencode-go/kimi-k2.5` | Kimi K2.5  
`opencode-go/kimi-k2.6` | Kimi K2.6（3 倍限制）  
`opencode-go/deepseek-v4-pro` | DeepSeek V4 Pro  
`opencode-go/deepseek-v4-flash` | DeepSeek V4 Flash  
`opencode-go/mimo-v2-omni` | MiMo V2 Omni  
`opencode-go/mimo-v2-pro` | MiMo V2 Pro  
`opencode-go/minimax-m2.5` | MiniMax M2.5  
`opencode-go/minimax-m2.7` | MiniMax M2.7  
`opencode-go/qwen3.5-plus` | Qwen3.5 Plus  
`opencode-go/qwen3.6-plus` | Qwen3.6 Plus  
  
## 開始使用

### 互動式

* ### 執行初始設定

bashCopy code
[code]
    openclaw onboard --auth-choice opencode-go
[/code]

* ### 將 Go 模型設為預設值

bashCopy code
[code]
    openclaw config set agents.defaults.model.primary "opencode-go/kimi-k2.6"
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

### 非互動式

* ### 直接傳入金鑰

bashCopy code
[code]
    openclaw onboard --opencode-go-api-key "$OPENCODE_API_KEY"
[/code]

* ### 確認模型可用

bashCopy code
[code]
    openclaw models list --provider opencode-go
[/code]

## 設定範例

json5Copy code
[code]
    {  env: { OPENCODE_API_KEY: "YOUR_API_KEY_HERE" }, // pragma: allowlist secret  agents: { defaults: { model: { primary: "opencode-go/kimi-k2.6" } } },}
[/code]

## 進階設定

路由行為

當模型參照使用 `opencode-go/...` 時，OpenClaw 會自動處理逐模型路由。 不需要額外的提供者設定。

執行階段參照慣例

執行階段參照會保持明確：Zen 使用 `opencode/...`，Go 使用 `opencode-go/...`。 這會讓兩個目錄的上游逐模型路由都保持正確。

共用憑證

Zen 和 Go 目錄都使用相同的 `OPENCODE_API_KEY`。在設定期間輸入 金鑰會為兩個執行階段提供者儲存憑證。

## 相關

[**OpenCode（上層）** 共用的初始設定、目錄概觀與進階備註。 ](</zh-TW/providers/opencode>) [**模型選擇** 選擇提供者、模型參照與容錯移轉行為。 ](</zh-TW/concepts/model-providers>)

Was this useful?YesNo