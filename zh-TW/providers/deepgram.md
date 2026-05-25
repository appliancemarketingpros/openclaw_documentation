---
title: Deepgram
source_url: https://docs.openclaw.ai/zh-TW/providers/deepgram
scraped_at: 2026-05-25
---

Deepgram 是語音轉文字 API。在 OpenClaw 中，它透過 `tools.media.audio` 用於傳入音訊/語音訊息轉錄，並透過 `plugins.entries.voice-call.config.streaming` 用於 Voice Call 串流 STT。

對於批次轉錄，OpenClaw 會將完整音訊檔案上傳到 Deepgram，並將轉錄稿注入回覆管線（`{{Transcript}}` \+ `[Audio]` 區塊）。對於 Voice Call 串流，OpenClaw 會透過 Deepgram 的 WebSocket `listen` 端點轉送即時 G.711 u-law 影格，並在 Deepgram 傳回時發出部分或最終轉錄稿。

詳細資訊 | 值  
---|---  
網站 | [deepgram.com](<https://deepgram.com>)  
文件 | [developers.deepgram.com](<https://developers.deepgram.com>)  
驗證 | `DEEPGRAM_API_KEY`  
預設模型 | `nova-3`  
  
## 開始使用

* ### 設定你的 API 金鑰

將你的 Deepgram API 金鑰加入環境：

CodeCopy code
[code]
    DEEPGRAM_API_KEY=dg_...
[/code]

* ### 啟用音訊供應商

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

* ### 傳送語音訊息

透過任何已連線的通道傳送音訊訊息。OpenClaw 會透過 Deepgram 轉錄它，並將轉錄稿注入回覆管線。

## 設定選項

選項 | 路徑 | 說明  
---|---|---  
`model` | `tools.media.audio.models[].model` | Deepgram 模型 ID（預設：`nova-3`）  
`language` | `tools.media.audio.models[].language` | 語言提示（選用）  
`detect_language` | `tools.media.audio.providerOptions.deepgram.detect_language` | 啟用語言偵測（選用）  
`punctuate` | `tools.media.audio.providerOptions.deepgram.punctuate` | 啟用標點符號（選用）  
`smart_format` | `tools.media.audio.providerOptions.deepgram.smart_format` | 啟用智慧格式化（選用）  
  
### 含語言提示

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "deepgram", model: "nova-3", language: "en" }],      },    },  },}
[/code]

### 含 Deepgram 選項

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        providerOptions: {          deepgram: {            detect_language: true,            punctuate: true,            smart_format: true,          },        },        models: [{ provider: "deepgram", model: "nova-3" }],      },    },  },}
[/code]

## Voice Call 串流 STT

隨附的 `deepgram` Plugin 也會為 Voice Call Plugin 註冊即時轉錄供應商。

設定 | 設定路徑 | 預設值  
---|---|---  
API 金鑰 | `plugins.entries.voice-call.config.streaming.providers.deepgram.apiKey` | 回退至 `DEEPGRAM_API_KEY`  
模型 | `...deepgram.model` | `nova-3`  
語言 | `...deepgram.language` | （未設定）  
編碼 | `...deepgram.encoding` | `mulaw`  
取樣率 | `...deepgram.sampleRate` | `8000`  
端點偵測 | `...deepgram.endpointingMs` | `800`  
暫時結果 | `...deepgram.interimResults` | `true`  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "deepgram",            providers: {              deepgram: {                apiKey: "${DEEPGRAM_API_KEY}",                model: "nova-3",                endpointingMs: 800,                language: "en-US",              },            },          },        },      },    },  },}
[/code]

## 備註

驗證

驗證會遵循標準供應商驗證順序。`DEEPGRAM_API_KEY` 是最簡單的路徑。

Proxy 和自訂端點

使用 Proxy 時，可透過 `tools.media.audio.baseUrl` 和 `tools.media.audio.headers` 覆寫端點或標頭。

輸出行為

輸出會遵循與其他供應商相同的音訊規則（大小上限、逾時、轉錄稿注入）。

## 相關

[**媒體工具** 音訊、影像和影片處理管線概觀。 ](</zh-TW/tools/media-overview>) [**設定** 包含媒體工具設定的完整設定參考。 ](</zh-TW/gateway/configuration>) [**疑難排解** 常見問題和偵錯步驟。 ](</zh-TW/help/troubleshooting>) [**FAQ** 關於 OpenClaw 設定的常見問題。 ](</zh-TW/help/faq>)

Was this useful?YesNo