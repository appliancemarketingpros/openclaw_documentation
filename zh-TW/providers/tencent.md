---
title: 騰訊雲 (TokenHub)
source_url: https://docs.openclaw.ai/zh-TW/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud 在 OpenClaw 中作為隨附的供應商 Plugin 提供。它透過 TokenHub 端點（`tencent-tokenhub`），使用 OpenAI 相容 API 存取 Tencent Hy3 preview。

屬性 | 值  
---|---  
供應商 ID | `tencent-tokenhub`  
Plugin | 隨附，`enabledByDefault: true`  
驗證環境變數 | `TOKENHUB_API_KEY`  
入門設定旗標 | `--auth-choice tokenhub-api-key`  
直接 CLI 旗標 | `--tokenhub-api-key <key>`  
API | OpenAI 相容（`openai-completions`）  
預設基底 URL | `https://tokenhub.tencentmaas.com/v1`  
全域基底 URL | `https://tokenhub-intl.tencentmaas.com/v1`（覆寫）  
預設模型 | `tencent-tokenhub/hy3-preview`  
  
## 快速開始

* ### 建立 TokenHub API 金鑰

在 Tencent Cloud TokenHub 中建立 API 金鑰。如果你為金鑰選擇有限的存取範圍，請在允許的模型中包含 **Hy3 preview** 。

* ### 執行入門設定

入門設定Copy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

直接旗標Copy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

僅環境變數Copy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### 驗證模型

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## 非互動式設定

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## 內建目錄

模型參照 | 名稱 | 輸入 | Context | 最大輸出 | 備註  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | text | 256,000 | 64,000 | 預設；已啟用推理功能  
  
Hy3 preview 是 Tencent Hunyuan 的大型 MoE 語言模型，適用於推理、長 Context 指令遵循、程式碼與代理工作流程。Tencent 的 OpenAI 相容範例使用 `hy3-preview` 作為模型 ID，並支援標準 chat-completions 工具呼叫以及 `reasoning_effort`。

## 分級定價

隨附目錄提供依輸入視窗長度調整的分級成本中繼資料，因此無需手動覆寫即可填入成本估算。

輸入 Token 範圍 | 輸入費率 | 輸出費率 | 快取讀取  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
費率以 Tencent 公告的每百萬 Token 美元價格計算。只有在你需要不同介面時，才在 `models.providers.tencent-tokenhub` 下覆寫定價。

## 進階設定

端點覆寫

OpenClaw 預設使用 Tencent Cloud 的 `https://tokenhub.tencentmaas.com/v1` 端點。Tencent 也記載了國際 TokenHub 端點：

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

只有在你的 TokenHub 帳戶或區域需要時，才覆寫端點。

Daemon 的環境可用性

如果 Gateway 以受管理服務執行（launchd、systemd、Docker），`TOKENHUB_API_KEY` 必須對該程序可見。請在 `~/.openclaw/.env` 中設定，或透過 `env.shellEnv` 設定，讓 launchd、systemd 或 Docker exec 環境可以讀取。

## 相關

[**模型供應商** 選擇供應商、模型參照與容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**設定參考** 完整設定結構描述，包含供應商設定。 ](</zh-TW/gateway/configuration>) [**Tencent TokenHub** Tencent Cloud 的 TokenHub 產品頁面。 ](<https://cloud.tencent.com/product/tokenhub>) [**Hy3 preview 模型卡** Tencent Hunyuan Hy3 preview 詳細資訊與基準測試。 ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo