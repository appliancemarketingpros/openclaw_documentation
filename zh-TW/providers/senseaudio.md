---
title: SenseAudio
source_url: https://docs.openclaw.ai/zh-TW/providers/senseaudio
scraped_at: 2026-05-25
---

SenseAudio 可透過 OpenClaw 共享的 `tools.media.audio` 管線，轉錄傳入的音訊與語音留言附件。OpenClaw 會將 multipart 音訊傳送到相容於 OpenAI 的轉錄端點，並將傳回的文字注入為 `{{Transcript}}` 加上一個 `[Audio]` 區塊。

屬性 | 值  
---|---  
提供者 ID | `senseaudio`  
Plugin | 內建，`enabledByDefault: true`  
合約 | `mediaUnderstandingProviders`（音訊）  
驗證環境變數 | `SENSEAUDIO_API_KEY`  
預設模型 | `senseaudio-asr-pro-1.5-260319`  
預設 URL | `https://api.senseaudio.cn/v1`  
網站 | [senseaudio.cn](<https://senseaudio.cn>)  
文件 | [senseaudio.cn/docs](<https://senseaudio.cn/docs>)  
  
## 開始使用

* ### 設定您的 API 金鑰

bashCopy code
[code]
    export SENSEAUDIO_API_KEY="..."
[/code]

* ### 啟用音訊提供者

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "senseaudio", model: "senseaudio-asr-pro-1.5-260319" }],      },    },  },}
[/code]

* ### 傳送語音留言

透過任何已連接的頻道傳送音訊訊息。OpenClaw 會將音訊上傳至 SenseAudio，並在回覆管線中使用該轉錄稿。

## 選項

選項 | 路徑 | 說明  
---|---|---  
`model` | `tools.media.audio.models[].model` | SenseAudio ASR 模型 ID  
`language` | `tools.media.audio.models[].language` | 選用的語言提示  
`prompt` | `tools.media.audio.prompt` | 選用的轉錄提示  
`baseUrl` | `tools.media.audio.baseUrl` or model | 覆寫相容於 OpenAI 的基底  
`headers` | `tools.media.audio.request.headers` | 額外的要求標頭  
  
## 相關

  * [媒體理解（音訊）](</zh-TW/nodes/audio>)
  * [模型提供者](</zh-TW/concepts/model-providers>)


Was this useful?YesNo