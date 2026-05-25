---
title: Xiaomi MiMo
source_url: https://docs.openclaw.ai/zh-TW/providers/xiaomi
scraped_at: 2026-05-25
---

Xiaomi MiMo 是 **MiMo** 模型的 API 平台。OpenClaw 包含一個內建的 `xiaomi` Plugin，會針對相同的 `XIAOMI_API_KEY` 註冊 OpenAI 相容的聊天提供者與語音 (TTS) 提供者。

屬性 | 值  
---|---  
提供者 ID | `xiaomi`  
Plugin | 內建，`enabledByDefault: true`  
驗證環境變數 | `XIAOMI_API_KEY`  
新手設定旗標 | `--auth-choice xiaomi-api-key`  
直接 CLI 旗標 | `--xiaomi-api-key <key>`  
合約 | 聊天補全 + `speechProviders`  
API | OpenAI 相容 (`openai-completions`)  
基底 URL | `https://api.xiaomimimo.com/v1`  
預設模型 | `xiaomi/mimo-v2-flash`  
TTS 預設值 | `mimo-v2.5-tts`，語音 `mimo_default`  
  
## 開始使用

* ### Get an API key

在 [Xiaomi MiMo 主控台](<https://platform.xiaomimimo.com/#/console/api-keys>)建立 API 金鑰。

* ### Run onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key
[/code]

或直接傳入金鑰：

bashCopy code
[code]
    openclaw onboard --auth-choice xiaomi-api-key --xiaomi-api-key "$XIAOMI_API_KEY"
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider xiaomi
[/code]

## 內建目錄

模型參照 | 輸入 | 語境 | 最大輸出 | 推理 | 備註  
---|---|---|---|---|---  
`xiaomi/mimo-v2-flash` | text | 262,144 | 8,192 | 否 | 預設模型  
`xiaomi/mimo-v2-pro` | text | 1,048,576 | 32,000 | 是 | 大語境  
`xiaomi/mimo-v2-omni` | text, image | 262,144 | 32,000 | 是 | 多模態  
  
## 文字轉語音

內建的 `xiaomi` Plugin 也會將 Xiaomi MiMo 註冊為 `messages.tts` 的語音提供者。它會呼叫 Xiaomi 的聊天補全 TTS 合約，將文字作為 `assistant` 訊息，並將選用的風格指引作為 `user` 訊息。

屬性 | 值  
---|---  
TTS ID | `xiaomi`（`mimo` 別名）  
驗證 | `XIAOMI_API_KEY`  
API | 使用 `audio` 的 `POST /v1/chat/completions`  
預設 | `mimo-v2.5-tts`，語音 `mimo_default`  
輸出 | 預設為 MP3；設定後可使用 WAV  
json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "xiaomi",      providers: {        xiaomi: {          apiKey: "xiaomi_api_key",          model: "mimo-v2.5-tts",          voice: "mimo_default",          format: "mp3",          style: "Bright, natural, conversational tone.",        },      },    },  },}
[/code]

支援的內建語音包含 `mimo_default`、`default_zh`、`default_en`、`Mia`、`Chloe`、`Milo` 和 `Dean`。`mimo-v2-tts` 支援較舊的 MiMo TTS 帳戶；預設值使用目前的 MiMo-V2.5 TTS 模型。對於 Feishu 和 Telegram 等語音記事目標，OpenClaw 會在傳送前使用 `ffmpeg` 將 Xiaomi 輸出轉碼為 48kHz Opus。

## 設定範例

json5Copy code
[code]
    {  env: { XIAOMI_API_KEY: "your-key" },  agents: { defaults: { model: { primary: "xiaomi/mimo-v2-flash" } } },  models: {    mode: "merge",    providers: {      xiaomi: {        baseUrl: "https://api.xiaomimimo.com/v1",        api: "openai-completions",        apiKey: "XIAOMI_API_KEY",        models: [          {            id: "mimo-v2-flash",            name: "Xiaomi MiMo V2 Flash",            reasoning: false,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 8192,          },          {            id: "mimo-v2-pro",            name: "Xiaomi MiMo V2 Pro",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 1048576,            maxTokens: 32000,          },          {            id: "mimo-v2-omni",            name: "Xiaomi MiMo V2 Omni",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 262144,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Auto-injection behavior

當環境中設定了 `XIAOMI_API_KEY` 或存在驗證設定檔時，`xiaomi` 提供者會自動注入。除非你想覆寫模型中繼資料或基底 URL，否則不需要手動設定提供者。

Model details

  * **mimo-v2-flash** — 輕量且快速，適合一般文字任務。不支援推理。
  * **mimo-v2-pro** — 支援推理，具備 1M token 語境視窗，適合長文件工作負載。
  * **mimo-v2-omni** — 啟用推理的多模態模型，同時接受文字與圖片輸入。

Troubleshooting

  * 如果模型沒有出現，請確認 `XIAOMI_API_KEY` 已設定且有效。
  * 當 Gateway 以守護程式形式執行時，請確保該程序可使用金鑰（例如在 `~/.openclaw/.env` 中，或透過 `env.shellEnv`）。


## 相關

[**Model selection** 選擇提供者、模型參照與容錯移轉行為。 ](</zh-TW/concepts/model-providers>) [**Configuration reference** 完整的 OpenClaw 設定參考。 ](</zh-TW/gateway/configuration-reference>) [**Xiaomi MiMo console** Xiaomi MiMo 儀表板與 API 金鑰管理。 ](<https://platform.xiaomimimo.com>)

Was this useful?YesNo