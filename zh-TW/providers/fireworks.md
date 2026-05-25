---
title: Fireworks
source_url: https://docs.openclaw.ai/zh-TW/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) 透過 OpenAI 相容 API 提供開放權重與路由模型。OpenClaw 內含一個內建 Fireworks provider plugin，隨附兩個已預先編入目錄的 Kimi 模型，並可在執行階段接受任何 Fireworks 模型或 router id。

屬性 | 值  
---|---  
Provider id | `fireworks`（別名：`fireworks-ai`）  
Plugin | 內建，`enabledByDefault: true`  
驗證環境變數 | `FIREWORKS_API_KEY`  
Onboarding 旗標 | `--auth-choice fireworks-api-key`  
直接 CLI 旗標 | `--fireworks-api-key <key>`  
API | OpenAI 相容（`openai-completions`）  
基底 URL | `https://api.fireworks.ai/inference/v1`  
預設模型 | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
預設別名 | `Kimi K2.5 Turbo`  
  
## 開始使用

* ### Set the Fireworks API key

OnboardingCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Env onlyCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

Onboarding 會將金鑰儲存在你的驗證設定檔中的 `fireworks` provider，並將 **Fire Pass** Kimi K2.5 Turbo router 設為預設模型。

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

清單應包含 `Kimi K2.6` 和 `Kimi K2.5 Turbo (Fire Pass)`。如果 `FIREWORKS_API_KEY` 無法解析，`openclaw models status --json` 會在 `auth.unusableProfiles` 下回報缺少的憑證。

## 非互動式設定

對於腳本化或 CI 安裝，請在命令列傳入所有內容：

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## 內建目錄

模型參照 | 名稱 | 輸入 | Context | 最大輸出 | Thinking  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | 文字 + 圖片 | 262,144 | 262,144 | 強制關閉  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | 文字 + 圖片 | 256,000 | 256,000 | 強制關閉（預設）  
  
## 自訂 Fireworks 模型 id

OpenClaw 可在執行階段接受任何 Fireworks 模型或 router id。使用 Fireworks 顯示的確切 id，並加上 `fireworks/` 前綴。動態解析會複製 Fire Pass 範本（文字 + 圖片輸入、OpenAI 相容 API、預設成本為零），並在 id 符合 Kimi 模式時自動停用 thinking。

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

How model id prefixing works

OpenClaw 中的每個 Fireworks 模型參照都以 `fireworks/` 開頭，後接 Fireworks 平台上的確切 id 或 router 路徑。例如：

  * Router 模型：`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * 直接模型：`fireworks/accounts/fireworks/models/<model-name>`


OpenClaw 在建構 API 請求時會移除 `fireworks/` 前綴，並將剩餘路徑作為 OpenAI 相容的 `model` 欄位傳送至 Fireworks 端點。

Why thinking is forced off for Kimi

如果請求帶有 `reasoning_*` 參數，Fireworks K2.6 會回傳 400，即使 Kimi 透過 Moonshot 自有 API 支援 thinking。內建政策（`extensions/fireworks/thinking-policy.ts`）僅為 Kimi 模型 id 宣告 `off` thinking 等級，因此手動 `/think` 切換與 provider-policy 介面會與執行階段合約保持一致。

若要端到端使用 Kimi reasoning，請設定 [Moonshot provider](</zh-TW/providers/moonshot>)，並透過它路由相同模型。

Environment availability for the daemon

如果 Gateway 以受管理服務執行（launchd、systemd、Docker），Fireworks 金鑰必須能被該程序看見，而不只是你的互動式 shell。

在 macOS 上，`openclaw gateway install` 已經會將 `~/.openclaw/.env` 接入 LaunchAgent 環境檔。輪替金鑰後，請重新執行安裝（或 `openclaw doctor --fix`）。

## 相關

[**Model providers** 選擇 provider、模型參照與容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**Thinking modes** `/think` 等級、provider 政策，以及路由具備 reasoning 能力的模型。 ](</zh-TW/tools/thinking>) [**Moonshot** 透過 Moonshot 自有 API 執行 Kimi 並取得原生 thinking 輸出。 ](</zh-TW/providers/moonshot>) [**Troubleshooting** 一般疑難排解與常見問題。 ](</zh-TW/help/troubleshooting>)

Was this useful?YesNo