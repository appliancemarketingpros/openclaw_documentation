---
title: 火山引擎（豆包）
source_url: https://docs.openclaw.ai/zh-TW/providers/volcengine
scraped_at: 2026-05-25
---

Volcengine provider 可存取託管在 Volcano Engine 上的 Doubao 模型與第三方模型，並針對一般與程式碼工作負載提供不同端點。同一個內建 Plugin 也可以將 Volcengine Speech 註冊為 TTS provider。

詳細資訊 | 值  
---|---  
Provider | `volcengine`（一般 + TTS）+ `volcengine-plan`（程式碼）  
模型驗證 | `VOLCANO_ENGINE_API_KEY`  
TTS 驗證 | `VOLCENGINE_TTS_API_KEY` 或 `BYTEPLUS_SEED_SPEECH_API_KEY`  
API | OpenAI 相容模型、BytePlus Seed Speech TTS  
  
## 開始使用

* ### Set the API key

執行互動式 onboarding：

bashCopy code
[code]
    openclaw onboard --auth-choice volcengine-api-key
[/code]

這會使用單一 API key 註冊一般（`volcengine`）與程式碼（`volcengine-plan`）providers。

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "volcengine-plan/ark-code-latest" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider volcengineopenclaw models list --provider volcengine-plan
[/code]

## Provider 與端點

Provider | 端點 | 用例  
---|---|---  
`volcengine` | `ark.cn-beijing.volces.com/api/v3` | 一般模型  
`volcengine-plan` | `ark.cn-beijing.volces.com/api/coding/v3` | 程式碼模型  
  
## 內建目錄

### General (volcengine)

模型 ref | 名稱 | 輸入 | Context  
---|---|---|---  
`volcengine/doubao-seed-1-8-251228` | Doubao Seed 1.8 | text, image | 256,000  
`volcengine/doubao-seed-code-preview-251028` | doubao-seed-code-preview-251028 | text, image | 256,000  
`volcengine/kimi-k2-5-260127` | Kimi K2.5 | text, image | 256,000  
`volcengine/glm-4-7-251222` | GLM 4.7 | text, image | 200,000  
`volcengine/deepseek-v3-2-251201` | DeepSeek V3.2 | text, image | 128,000  
  
### Coding (volcengine-plan)

模型 ref | 名稱 | 輸入 | Context  
---|---|---|---  
`volcengine-plan/ark-code-latest` | Ark Coding Plan | text | 256,000  
`volcengine-plan/doubao-seed-code` | Doubao Seed Code | text | 256,000  
`volcengine-plan/glm-4.7` | GLM 4.7 Coding | text | 200,000  
`volcengine-plan/kimi-k2-thinking` | Kimi K2 Thinking | text | 256,000  
`volcengine-plan/kimi-k2.5` | Kimi K2.5 Coding | text | 256,000  
`volcengine-plan/doubao-seed-code-preview-251028` | Doubao Seed Code Preview | text | 256,000  
  
## 文字轉語音

Volcengine TTS 使用 BytePlus Seed Speech HTTP API，並與 OpenAI 相容 Doubao 模型 API key 分開設定。在 BytePlus 主控台中開啟 Seed Speech > Settings > API Keys 並複製 API key，然後設定：

bashCopy code
[code]
    export VOLCENGINE_TTS_API_KEY="byteplus_seed_speech_api_key"export VOLCENGINE_TTS_RESOURCE_ID="seed-tts-1.0"
[/code]

接著在 `openclaw.json` 中啟用：

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "volcengine",      providers: {        volcengine: {          apiKey: "byteplus_seed_speech_api_key",          voice: "en_female_anna_mars_bigtts",          speedRatio: 1.0,        },      },    },  },}
[/code]

針對語音訊息目標，OpenClaw 會向 Volcengine 要求 provider 原生的 `ogg_opus`。針對一般音訊附件，則會要求 `mp3`。Provider alias `bytedance` 與 `doubao` 也會解析到相同的語音 provider。

預設 resource id 是 `seed-tts-1.0`，因為這是 BytePlus 在預設專案中授予新建立 Seed Speech API keys 的項目。如果你的專案具有 TTS 2.0 entitlement，請設定 `VOLCENGINE_TTS_RESOURCE_ID=seed-tts-2.0`。

較舊 Speech Console 應用程式仍支援舊版 AppID/token 驗證：

bashCopy code
[code]
    export VOLCENGINE_TTS_APPID="speech_app_id"export VOLCENGINE_TTS_TOKEN="speech_access_token"export VOLCENGINE_TTS_CLUSTER="volcano_tts"
[/code]

## 進階設定

Default model after onboarding

`openclaw onboard --auth-choice volcengine-api-key` 目前會將 `volcengine-plan/ark-code-latest` 設為預設模型，同時也會註冊一般 `volcengine` 目錄。

Model picker fallback behavior

在 onboarding/configure 模型選取期間，Volcengine 驗證選項會優先使用 `volcengine/*` 與 `volcengine-plan/*` 列。如果這些模型尚未載入，OpenClaw 會退回未篩選的目錄，而不是顯示空的 provider 範圍選取器。

Environment variables for daemon processes

如果 Gateway 以 daemon（launchd/systemd）方式執行，請確保模型與 TTS env vars，例如 `VOLCANO_ENGINE_API_KEY`、`VOLCENGINE_TTS_API_KEY`、`BYTEPLUS_SEED_SPEECH_API_KEY`、`VOLCENGINE_TTS_APPID` 與 `VOLCENGINE_TTS_TOKEN`，可供該 process 使用（例如在 `~/.openclaw/.env` 中，或透過 `env.shellEnv`）。

## 相關

[**Model selection** 選擇 providers、模型 refs 與 failover 行為。 ](</zh-TW/concepts/model-providers>) [**Configuration** agents、models 與 providers 的完整設定參考。 ](</zh-TW/gateway/configuration>) [**Troubleshooting** 常見問題與偵錯步驟。 ](</zh-TW/help/troubleshooting>) [**FAQ** 關於 OpenClaw 設定的常見問題。 ](</zh-TW/help/faq>)

Was this useful?YesNo