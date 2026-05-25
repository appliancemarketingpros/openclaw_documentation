---
title: ElevenLabs
source_url: https://docs.openclaw.ai/zh-TW/providers/elevenlabs
scraped_at: 2026-05-25
---

OpenClaw 使用 ElevenLabs 進行文字轉語音、透過 Scribe v2 進行批次語音轉文字，以及透過 Scribe v2 Realtime 進行串流 STT。

功能 | OpenClaw 介面 | 預設值  
---|---|---  
文字轉語音 | `messages.tts` / `talk` | `eleven_multilingual_v2`  
批次語音轉文字 | `tools.media.audio` | `scribe_v2`  
串流語音轉文字 | Voice Call 串流或 Google Meet `realtime.transcriptionProvider` | `scribe_v2_realtime`  
  
## 驗證

在環境中設定 `ELEVENLABS_API_KEY`。也接受 `XI_API_KEY`，以相容既有的 ElevenLabs 工具。

bashCopy code
[code]
    export ELEVENLABS_API_KEY="..."
[/code]

## 文字轉語音

json5Copy code
[code]
    {  messages: {    tts: {      providers: {        elevenlabs: {          apiKey: "${ELEVENLABS_API_KEY}",          voiceId: "pMsXgVXv3BLzUgSXRplE",          modelId: "eleven_multilingual_v2",        },      },    },  },}
[/code]

將 `modelId` 設為 `eleven_v3` 即可使用 ElevenLabs v3 TTS。OpenClaw 仍將 `eleven_multilingual_v2` 保留為既有安裝的預設值。

當 ElevenLabs 是選定的 `voice.tts`/`messages.tts` 提供者時，Discord 語音頻道會使用 ElevenLabs 的串流 TTS 端點。播放會從傳回的音訊串流開始，而不是先等待 OpenClaw 下載並寫入整個音訊檔案。對於接受該參數的模型，`latencyTier` 會對應至 ElevenLabs 的 `optimize_streaming_latency` 查詢參數；OpenClaw 會針對 `eleven_v3` 省略該參數，因為它會拒絕該參數。

## 語音轉文字

針對傳入音訊附件和短錄音語音片段使用 Scribe v2：

json5Copy code
[code]
    {  tools: {    media: {      audio: {        enabled: true,        models: [{ provider: "elevenlabs", model: "scribe_v2" }],      },    },  },}
[/code]

OpenClaw 會將多部分音訊傳送至 ElevenLabs `/v1/speech-to-text`，並使用 `model_id: "scribe_v2"`。語言提示存在時會對應至 `language_code`。

## 串流 STT

內建的 `elevenlabs` Plugin 會為 Voice Call 和 Google Meet agent 模式串流轉錄註冊 Scribe v2 Realtime。

設定 | 設定路徑 | 預設值  
---|---|---  
API 金鑰 | `plugins.entries.voice-call.config.streaming.providers.elevenlabs.apiKey` | 回退至 `ELEVENLABS_API_KEY` / `XI_API_KEY`  
模型 | `...elevenlabs.modelId` | `scribe_v2_realtime`  
音訊格式 | `...elevenlabs.audioFormat` | `ulaw_8000`  
取樣率 | `...elevenlabs.sampleRate` | `8000`  
提交策略 | `...elevenlabs.commitStrategy` | `vad`  
語言 | `...elevenlabs.languageCode` | （未設定）  
json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        config: {          streaming: {            enabled: true,            provider: "elevenlabs",            providers: {              elevenlabs: {                apiKey: "${ELEVENLABS_API_KEY}",                audioFormat: "ulaw_8000",                commitStrategy: "vad",                languageCode: "en",              },            },          },        },      },    },  },}
[/code]

若使用 Google Meet agent 模式，請將 `plugins.entries.google-meet.config.realtime.transcriptionProvider` 設為 `"elevenlabs"`，並在 `plugins.entries.google-meet.config.realtime.providers.elevenlabs` 下設定相同的提供者區塊。

## 相關

  * [文字轉語音](</zh-TW/tools/tts>)
  * [Google Meet](</zh-TW/plugins/google-meet>)
  * [模型選擇](</zh-TW/concepts/model-providers>)


Was this useful?YesNo