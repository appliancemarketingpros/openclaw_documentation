---
title: Inworld
source_url: https://docs.openclaw.ai/zh-TW/providers/inworld
scraped_at: 2026-05-25
---

Inworld 是串流文字轉語音 (TTS) 提供者。在 OpenClaw 中，它會合成對外回覆音訊（預設為 MP3，語音備註使用 OGG_OPUS），也會為語音通話等電話通道合成 PCM 音訊。

OpenClaw 會發送請求到 Inworld 的串流 TTS 端點，將傳回的 base64 音訊區塊串接成單一緩衝區，並把結果交給標準回覆音訊管線。

屬性 | 值  
---|---  
提供者 ID | `inworld`  
Plugin | 內建，`enabledByDefault: true`  
合約 | `speechProviders`（僅 TTS）  
驗證環境變數 | `INWORLD_API_KEY`（HTTP Basic，Base64 儀表板憑證）  
基礎 URL | `https://api.inworld.ai`  
預設語音 | `Sarah`  
預設模型 | `inworld-tts-1.5-max`  
輸出 | MP3（預設）、OGG_OPUS（語音備註）、PCM 22050 Hz（電話）  
網站 | [inworld.ai](<https://inworld.ai>)  
文件 | [docs.inworld.ai/tts/tts](<https://docs.inworld.ai/tts/tts>)  
  
## 開始使用

* ### 設定你的 API 金鑰

從你的 Inworld 儀表板（Workspace > API Keys）複製憑證，並將它設定為環境變數。該值會原樣作為 HTTP Basic 憑證傳送，因此不要再次進行 Base64 編碼，也不要將它轉換為 bearer token。

CodeCopy code
[code]
    INWORLD_API_KEY=<base64-credential-from-dashboard>
[/code]

* ### 在 messages.tts 中選取 Inworld

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "inworld",      providers: {        inworld: {          voiceId: "Sarah",          modelId: "inworld-tts-1.5-max",        },      },    },  },}
[/code]

* ### 傳送訊息

透過任何已連線的通道傳送回覆。OpenClaw 會使用 Inworld 合成音訊，並以 MP3 傳送（或在通道預期語音備註時使用 OGG_OPUS）。

## 設定選項

選項 | 路徑 | 說明  
---|---|---  
`apiKey` | `messages.tts.providers.inworld.apiKey` | Base64 儀表板憑證。會退回使用 `INWORLD_API_KEY`。  
`baseUrl` | `messages.tts.providers.inworld.baseUrl` | 覆寫 Inworld API 基礎 URL（預設 `https://api.inworld.ai`）。  
`voiceId` | `messages.tts.providers.inworld.voiceId` | 語音識別碼（預設 `Sarah`）。  
`modelId` | `messages.tts.providers.inworld.modelId` | TTS 模型 ID（預設 `inworld-tts-1.5-max`）。  
`temperature` | `messages.tts.providers.inworld.temperature` | 取樣溫度 `0..2`（選用）。  
  
## 注意事項

驗證

Inworld 使用 HTTP Basic 驗證，搭配單一 Base64 編碼的憑證字串。請從 Inworld 儀表板原樣複製。提供者會以 `Authorization: Basic <apiKey>` 傳送它，不會再進行任何編碼，因此不要自行進行 Base64 編碼，也不要傳入 bearer 風格的 token。相同提醒請參閱 [TTS 驗證注意事項](</zh-TW/tools/tts#inworld-primary>)。

模型

支援的模型 ID：`inworld-tts-1.5-max`（預設）、`inworld-tts-1.5-mini`、`inworld-tts-1-max`、`inworld-tts-1`。

音訊輸出

回覆預設使用 MP3。當通道目標是 `voice-note` 時，OpenClaw 會要求 Inworld 使用 `OGG_OPUS`，讓音訊以原生語音泡泡播放。電話合成會使用 22050 Hz 的原始 `PCM` 來供給電話橋接器。

自訂端點

使用 `messages.tts.providers.inworld.baseUrl` 覆寫 API 主機。傳送請求前會移除尾端斜線。

## 相關

[**文字轉語音** TTS 概觀、提供者，以及 `messages.tts` 設定。 ](</zh-TW/tools/tts>) [**設定** 完整設定參考，包括 `messages.tts` 設定。 ](</zh-TW/gateway/configuration>) [**提供者** 所有內建 OpenClaw 提供者。 ](</zh-TW/providers>) [**疑難排解** 常見問題與除錯步驟。 ](</zh-TW/help/troubleshooting>)

Was this useful?YesNo