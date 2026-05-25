---
title: 文字轉語音
source_url: https://docs.openclaw.ai/zh-TW/tools/tts
scraped_at: 2026-05-25
---

OpenClaw 可將傳出回覆轉換為音訊，支援 **14 個語音提供者** ， 並在 Feishu、Matrix、Telegram 和 WhatsApp 上傳送原生語音訊息， 在其他地方傳送音訊附件，並為電話系統和 Talk 提供 PCM/Ulaw 串流。

TTS 是 Talk 的 `stt-tts` 模式中的語音輸出部分。提供者原生的 `realtime` Talk 工作階段會在即時提供者內合成語音， 而不是呼叫這條 TTS 路徑；`transcription` 工作階段則不會合成 助理語音回應。

## 快速開始

* ### 選擇提供者

OpenAI 和 ElevenLabs 是最可靠的託管選項。Microsoft 和 Local CLI 不需要 API 金鑰即可運作。完整清單請參閱提供者矩陣。

* ### 設定 API 金鑰

匯出你的提供者所需的環境變數（例如 `OPENAI_API_KEY`、 `ELEVENLABS_API_KEY`）。Microsoft 和 Local CLI 不需要金鑰。

* ### 在設定中啟用

設定 `messages.tts.auto: "always"` 和 `messages.tts.provider`：

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",    },  },}
[/code]

* ### 在聊天中試用

`/tts status` 會顯示目前狀態。`/tts audio Hello from OpenClaw` 會傳送一次性的音訊回覆。

## 支援的提供者

提供者 | 驗證 | 備註  
---|---|---  
**Azure Speech** | `AZURE_SPEECH_KEY` \+ `AZURE_SPEECH_REGION`（另支援 `AZURE_SPEECH_API_KEY`、`SPEECH_KEY`、`SPEECH_REGION`） | 原生 Ogg/Opus 語音記事輸出和電話系統。  
**DeepInfra** | `DEEPINFRA_API_KEY` | OpenAI 相容 TTS。預設為 `hexgrad/Kokoro-82M`。  
**ElevenLabs** | `ELEVENLABS_API_KEY` 或 `XI_API_KEY` | 語音複製、多語言，透過 `seed` 決定性輸出；為 Discord 語音播放提供串流。  
**Google Gemini** | `GEMINI_API_KEY` 或 `GOOGLE_API_KEY` | Gemini API 批次 TTS；可透過 `promptTemplate: "audio-profile-v1"` 感知 persona。  
**Gradium** | `GRADIUM_API_KEY` | 語音記事和電話系統輸出。  
**Inworld** | `INWORLD_API_KEY` | 串流 TTS API。原生 Opus 語音記事和 PCM 電話系統。  
**Local CLI** | 無 | 執行已設定的本機 TTS 命令。  
**Microsoft** | 無 | 透過 `node-edge-tts` 使用公開 Edge 神經 TTS。盡力提供，無 SLA。  
**MiniMax** | `MINIMAX_API_KEY`（或權杖方案：`MINIMAX_OAUTH_TOKEN`、`MINIMAX_CODE_PLAN_KEY`、`MINIMAX_CODING_API_KEY`） | T2A v2 API。預設為 `speech-2.8-hd`。  
**OpenAI** | `OPENAI_API_KEY` | 也用於自動摘要；支援 persona `instructions`。  
**OpenRouter** | `OPENROUTER_API_KEY`（可重用 `models.providers.openrouter.apiKey`） | 預設模型 `hexgrad/kokoro-82m`。  
**Volcengine** | `VOLCENGINE_TTS_API_KEY` 或 `BYTEPLUS_SEED_SPEECH_API_KEY`（舊版 AppID/權杖：`VOLCENGINE_TTS_APPID`/`_TOKEN`） | BytePlus Seed Speech HTTP API。  
**Vydra** | `VYDRA_API_KEY` | 共用的影像、影片和語音提供者。  
**xAI** | `XAI_API_KEY` | xAI 批次 TTS。**不** 支援原生 Opus 語音記事。  
**Xiaomi MiMo** | `XIAOMI_API_KEY` | 透過 Xiaomi chat completions 提供 MiMo TTS。  
  
如果設定了多個提供者，會先使用所選的提供者，其餘則作為備援選項。 自動摘要會使用 `summaryModel`（或 `agents.defaults.model.primary`）， 因此若你保持摘要啟用，該提供者也必須完成驗證。

## 設定

TTS 設定位於 `~/.openclaw/openclaw.json` 的 `messages.tts` 之下。選擇一個 預設組合，並調整提供者區塊：

### Azure Speech

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "azure-speech",  providers: {    "azure-speech": {      apiKey: "${AZURE_SPEECH_KEY}",      region: "eastus",      voice: "en-US-JennyNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      voiceNoteOutputFormat: "ogg-24khz-16bit-mono-opus",    },  },},},}
[/code]

### ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "elevenlabs",  providers: {    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",    },  },},},}
[/code]

### Google Gemini

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "google",  providers: {    google: {      apiKey: "${GEMINI_API_KEY}",      model: "gemini-3.1-flash-tts-preview",      voiceName: "Kore",      // Optional natural-language style prompts:      // audioProfile: "Speak in a calm, podcast-host tone.",      // speakerName: "Alex",    },  },},},}
[/code]

### Gradium

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "gradium",  providers: {    gradium: {      apiKey: "${GRADIUM_API_KEY}",      voiceId: "YTpq7expH9539ERJ",    },  },},},}
[/code]

### Inworld

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "inworld",  providers: {    inworld: {      apiKey: "${INWORLD_API_KEY}",      modelId: "inworld-tts-1.5-max",      voiceId: "Sarah",      temperature: 0.7,    },  },},},}
[/code]

### Local CLI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "tts-local-cli",  providers: {    "tts-local-cli": {      command: "say",      args: ["-o", "{{OutputPath}}", "{{Text}}"],      outputFormat: "wav",      timeoutMs: 120000,    },  },},},}
[/code]

### Microsoft (no key)

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "microsoft",  providers: {    microsoft: {      enabled: true,      voice: "en-US-MichelleNeural",      lang: "en-US",      outputFormat: "audio-24khz-48kbitrate-mono-mp3",      rate: "+0%",      pitch: "+0%",    },  },},},}
[/code]

### MiniMax

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "minimax",  providers: {    minimax: {      apiKey: "${MINIMAX_API_KEY}",      model: "speech-2.8-hd",      voiceId: "English_expressive_narrator",      speed: 1.0,      vol: 1.0,      pitch: 0,    },  },},},}
[/code]

### OpenAI + ElevenLabs

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openai",  summaryModel: "openai/gpt-4.1-mini",  modelOverrides: { enabled: true },  providers: {    openai: {      apiKey: "${OPENAI_API_KEY}",      model: "gpt-4o-mini-tts",      voice: "alloy",    },    elevenlabs: {      apiKey: "${ELEVENLABS_API_KEY}",      model: "eleven_multilingual_v2",      voiceId: "EXAVITQu4vr4xnSDxMaL",      voiceSettings: { stability: 0.5, similarityBoost: 0.75, style: 0.0, useSpeakerBoost: true, speed: 1.0 },      applyTextNormalization: "auto",      languageCode: "en",    },  },},},}
[/code]

### OpenRouter

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "openrouter",  providers: {    openrouter: {      apiKey: "${OPENROUTER_API_KEY}",      model: "hexgrad/kokoro-82m",      voice: "af_alloy",      responseFormat: "mp3",    },  },},},}
[/code]

### Volcengine

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "volcengine",  providers: {    volcengine: {      apiKey: "${VOLCENGINE_TTS_API_KEY}",      resourceId: "seed-tts-1.0",      voice: "en_female_anna_mars_bigtts",    },  },},},}
[/code]

### xAI

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xai",  providers: {    xai: {      apiKey: "${XAI_API_KEY}",      voiceId: "eve",      language: "en",      responseFormat: "mp3",    },  },},},}
[/code]

### Xiaomi MiMo

json5Copy code
[code]
    {messages: {tts: {  auto: "always",  provider: "xiaomi",  providers: {    xiaomi: {      apiKey: "${XIAOMI_API_KEY}",      model: "mimo-v2.5-tts",      voice: "mimo_default",      format: "mp3",    },  },},},}
[/code]

### 每代理語音覆寫

當某個代理需要使用不同的提供者、語音、模型、persona 或 Auto-TTS 模式時， 請使用 `agents.list[].tts`。代理區塊會深度合併到 `messages.tts` 之上， 因此提供者憑證可以保留在全域提供者設定中：

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      provider: "elevenlabs",      providers: {        elevenlabs: { apiKey: "${ELEVENLABS_API_KEY}", model: "eleven_multilingual_v2" },      },    },  },  agents: {    list: [      {        id: "reader",        tts: {          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL" },          },        },      },    ],  },}
[/code]

若要固定每個代理程式的人格，請在提供者設定旁設定 `agents.list[].tts.persona`，它只會為該代理程式覆寫全域的 `messages.tts.persona`。

自動回覆、`/tts audio`、`/tts status` 與 `tts` 代理程式工具的優先順序：

  1. `messages.tts`
  2. 作用中的 `agents.list[].tts`
  3. 頻道覆寫，當頻道支援 `channels.<channel>.tts` 時
  4. 帳號覆寫，當頻道傳遞 `channels.<channel>.accounts.<id>.tts` 時
  5. 此主機的本機 `/tts` 偏好設定
  6. 啟用模型覆寫時的行內 `[[tts:...]]` 指令


頻道與帳號覆寫使用與 `messages.tts` 相同的形狀，並在較早的層之上進行深度合併，因此共用的提供者憑證可以保留在 `messages.tts` 中，而頻道或機器人帳號只變更語音、模型、人格或自動模式：

json5Copy code
[code]
    {  messages: {    tts: {      provider: "openai",      providers: {        openai: { apiKey: "${OPENAI_API_KEY}", model: "gpt-4o-mini-tts" },      },    },  },  channels: {    feishu: {      accounts: {        english: {          tts: {            providers: {              openai: { voice: "shimmer" },            },          },        },      },    },  },}
[/code]

## 人格

**人格** 是穩定的語音身分，可跨提供者以確定性方式套用。它可以偏好某個提供者、定義與提供者無關的提示意圖，並攜帶語音、模型、提示範本、種子與語音設定的提供者專屬繫結。

### 最小人格

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "narrator",      personas: {        narrator: {          label: "Narrator",          provider: "elevenlabs",          providers: {            elevenlabs: { voiceId: "EXAVITQu4vr4xnSDxMaL", modelId: "eleven_multilingual_v2" },          },        },      },    },  },}
[/code]

### 完整人格（提供者中立提示）

json5Copy code
[code]
    {  messages: {    tts: {      auto: "always",      persona: "alfred",      personas: {        alfred: {          label: "Alfred",          description: "Dry, warm British butler narrator.",          provider: "google",          fallbackPolicy: "preserve-persona",          prompt: {            profile: "A brilliant British butler. Dry, witty, warm, charming, emotionally expressive, never generic.",            scene: "A quiet late-night study. Close-mic narration for a trusted operator.",            sampleContext: "The speaker is answering a private technical request with concise confidence and dry warmth.",            style: "Refined, understated, lightly amused.",            accent: "British English.",            pacing: "Measured, with short dramatic pauses.",            constraints: ["Do not read configuration values aloud.", "Do not explain the persona."],          },          providers: {            google: {              model: "gemini-3.1-flash-tts-preview",              voiceName: "Algieba",              promptTemplate: "audio-profile-v1",            },            openai: { model: "gpt-4o-mini-tts", voice: "cedar" },            elevenlabs: {              voiceId: "voice_id",              modelId: "eleven_multilingual_v2",              seed: 42,              voiceSettings: {                stability: 0.65,                similarityBoost: 0.8,                style: 0.25,                useSpeakerBoost: true,                speed: 0.95,              },            },          },        },      },    },  },}
[/code]

### 人格解析

作用中人格會以確定性方式選取：

  1. `/tts persona <id>` 本機偏好設定（若已設定）。
  2. `messages.tts.persona`（若已設定）。
  3. 無人格。


提供者選取採用明確優先：

  1. 直接覆寫（CLI、Gateway、Talk、允許的 TTS 指令）。
  2. `/tts provider <id>` 本機偏好設定。
  3. 作用中人格的 `provider`。
  4. `messages.tts.provider`。
  5. 登錄檔自動選取。


對於每次提供者嘗試，OpenClaw 會依下列順序合併設定：

  1. `messages.tts.providers.<id>`
  2. `messages.tts.personas.<persona>.providers.<id>`
  3. 受信任的請求覆寫
  4. 允許的模型發出 TTS 指令覆寫


### 提供者如何使用人格提示

人格提示欄位（`profile`、`scene`、`sampleContext`、`style`、`accent`、`pacing`、`constraints`）是**提供者中立** 的。每個提供者會自行決定如何使用它們：

Google Gemini

只有在有效的 Google 提供者設定設為 `promptTemplate: "audio-profile-v1"` 或 `personaPrompt` 時，才會將人格提示欄位包裝到 Gemini TTS 提示結構中。較舊的 `audioProfile` 與 `speakerName` 欄位仍會作為 Google 專屬提示文字前置加入。`[[tts:text]]` 區塊內的行內音訊標籤（例如 `[whispers]` 或 `[laughs]`）會保留在 Gemini 逐字稿內；OpenClaw 不會產生這些標籤。

OpenAI

只有在未設定明確的 OpenAI `instructions` 時，才會將人格提示欄位對應到請求的 `instructions` 欄位。明確的 `instructions` 永遠優先。

其他提供者

只使用 `personas.<id>.providers.<provider>` 底下的提供者專屬人格繫結。人格提示欄位會被忽略，除非提供者實作自己的個性提示對應。

### 後援政策

`fallbackPolicy` 控制當某個人格對嘗試的提供者**沒有繫結** 時的行為：

政策 | 行為  
---|---  
`preserve-persona` | **預設。** 提供者中立提示欄位仍可使用；提供者可以使用或忽略它們。  
`provider-defaults` | 該次嘗試的提示準備會省略人格；提供者會使用其中立預設值，同時繼續後援到其他提供者。  
`fail` | 以 `reasonCode: "not_configured"` 與 `personaBinding: "missing"` 跳過該提供者嘗試。仍會嘗試後援提供者。  
  
只有當**所有** 嘗試的提供者都被跳過或失敗時，整個 TTS 請求才會失敗。

Talk 工作階段的提供者選取以工作階段為範圍。Talk 用戶端應從 `talk.catalog` 選擇提供者 ID、模型 ID、語音 ID 與語言地區，並透過 Talk 工作階段或交接請求傳遞。開啟語音工作階段不應改變 `messages.tts` 或全域 Talk 提供者預設值。

## 模型驅動指令

預設情況下，助理**可以** 發出 `[[tts:...]]` 指令，為單一回覆覆寫語音、模型或速度，也可以加上一個選用的 `[[tts:text]]...[[/tts:text]]` 區塊，用於只應出現在音訊中的表現提示：

textCopy code
[code]
    Here you go. [[tts:voiceId=pMsXgVXv3BLzUgSXRplE model=eleven_v3 speed=1.1]][[tts:text]](laughs) Read the song once more.[[/tts:text]]
[/code]

當 `messages.tts.auto` 為 `"tagged"` 時，**必須有指令** 才會觸發音訊。串流區塊傳送會在頻道看到之前，從可見文字中移除指令，即使指令被拆分到相鄰區塊之間也是如此。

除非 `modelOverrides.allowProvider: true`，否則會忽略 `provider=...`。當回覆宣告 `provider=...` 時，該指令中的其他鍵只會由該提供者解析；不支援的鍵會被移除，並回報為 TTS 指令警告。

**可用的指令鍵：**

  * `provider`（已註冊的提供者 ID；需要 `allowProvider: true`）
  * `voice` / `voiceName` / `voice_name` / `google_voice` / `voiceId`
  * `model` / `google_model`
  * `stability`, `similarityBoost`, `style`, `speed`, `useSpeakerBoost`
  * `vol` / `volume`（MiniMax 音量，0–10）
  * `pitch`（MiniMax 整數音高，−12 到 12；小數值會被截斷）
  * `emotion`（Volcengine 情緒標籤）
  * `applyTextNormalization` (`auto|on|off`)
  * `languageCode` (ISO 639-1)
  * `seed`


**完全停用模型覆寫：**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: false } } } }
[/code]

**允許切換提供者，同時讓其他旋鈕保持可設定：**

json5Copy code
[code]
    { messages: { tts: { modelOverrides: { enabled: true, allowProvider: true, allowSeed: false } } } }
[/code]

## Slash 指令

單一指令 `/tts`。在 Discord 上，OpenClaw 也會註冊 `/voice`，因為 `/tts` 是內建 Discord 指令，文字 `/tts ...` 仍可運作。

textCopy code
[code]
    /tts off | on | status/tts chat on | off | default/tts latest/tts provider <id>/tts persona <id> | off/tts limit <chars>/tts summary off/tts audio <text>
[/code]

行為備註：

  * `/tts on` 會將本機 TTS 偏好寫入 `always`；`/tts off` 會將其寫入 `off`。
  * `/tts chat on|off|default` 會為目前聊天寫入以工作階段為範圍的自動 TTS 覆寫。
  * `/tts persona <id>` 會寫入本機人格偏好；`/tts persona off` 會清除它。
  * `/tts latest` 會從目前工作階段逐字稿讀取最新的助理回覆，並將其傳送為一次音訊。它只會在工作階段項目上儲存該回覆的雜湊，以避免重複傳送語音。
  * `/tts audio` 會產生一次性的音訊回覆（**不會** 開啟 TTS）。
  * `limit` 與 `summary` 會儲存在**本機偏好設定** 中，而不是主要設定中。
  * `/tts status` 會包含最新嘗試的後援診斷：`Fallback: <primary> -> <used>`、`Attempts: ...`，以及每次嘗試的詳細資料（`provider:outcome(reasonCode) latency`）。
  * `/status` 會在啟用 TTS 時顯示作用中的 TTS 模式，以及已設定的提供者、模型、語音與已清理的自訂端點中繼資料。


## 個別使用者偏好設定

Slash 指令會將本機覆寫寫入 `prefsPath`。預設值為 `~/.openclaw/settings/tts.json`；可使用 `OPENCLAW_TTS_PREFS` 環境變數或 `messages.tts.prefsPath` 覆寫。

儲存欄位 | 影響  
---|---  
`auto` | 本機自動 TTS 覆寫（`always`、`off`、…）  
`provider` | 本機主要提供者覆寫  
`persona` | 本機人格覆寫  
`maxLength` | 摘要閾值（預設 `1500` 字元）  
`summarize` | 摘要切換（預設 `true`）  
  
這些會覆寫來自 `messages.tts` 加上該主機作用中 `agents.list[].tts` 區塊的有效設定。

## 輸出格式（固定）

TTS 語音傳送由頻道能力驅動。頻道 Plugin 會宣告語音風格 TTS 是否應要求提供者產生原生 `voice-note` 目標，或保留一般 `audio-file` 合成，並只為語音傳送標記相容輸出。

  * **支援語音留言的頻道** ：語音留言回覆偏好使用 Opus（ElevenLabs 的 `opus_48000_64`，OpenAI 的 `opus`）。 
    * 48kHz / 64kbps 是語音訊息的良好取捨。
  * **Feishu / WhatsApp** ：當語音留言回覆產生為 MP3/WebM/WAV/M4A 或其他可能的音訊檔時，頻道 Plugin 會先用 `ffmpeg` 將其轉碼為 48kHz Ogg/Opus，再傳送原生語音訊息。WhatsApp 會透過 Baileys `audio` 酬載傳送 結果，並帶有 `ptt: true` 和 `audio/ogg; codecs=opus`。如果轉換失敗，Feishu 會收到原始 檔案作為附件；WhatsApp 傳送會失敗，而不是發布不相容的 PTT 酬載。
  * **其他頻道** ：MP3（ElevenLabs 的 `mp3_44100_128`，OpenAI 的 `mp3`）。 
    * 44.1kHz / 128kbps 是語音清晰度的預設平衡。
  * **MiniMax** ：一般音訊附件使用 MP3（`speech-2.8-hd` 模型，32kHz 取樣率）。對於頻道宣告的語音留言目標，當頻道宣告支援轉碼時，OpenClaw 會在傳遞前用 `ffmpeg` 將 MiniMax MP3 轉碼為 48kHz Opus。
  * **Xiaomi MiMo** ：預設使用 MP3，設定後也可使用 WAV。對於頻道宣告的語音留言目標，當頻道宣告支援轉碼時，OpenClaw 會在傳遞前用 `ffmpeg` 將 Xiaomi 輸出轉碼為 48kHz Opus。
  * **本機 CLI** ：使用已設定的 `outputFormat`。語音留言目標會 轉換為 Ogg/Opus，而電話語音輸出會用 `ffmpeg` 轉換為原始 16 kHz 單聲道 PCM。
  * **Google Gemini** ：Gemini API TTS 會回傳原始 24kHz PCM。OpenClaw 會將其包裝為 WAV 供音訊附件使用，為語音留言目標轉碼為 48kHz Opus，並為 Talk/電話語音直接回傳 PCM。
  * **Gradium** ：音訊附件使用 WAV，語音留言目標使用 Opus，電話語音使用 8 kHz 的 `ulaw_8000`。
  * **Inworld** ：一般音訊附件使用 MP3，語音留言目標使用原生 `OGG_OPUS`，Talk/電話語音使用 22050 Hz 的原始 `PCM`。
  * **xAI** ：預設使用 MP3；`responseFormat` 可以是 `mp3`、`wav`、`pcm`、`mulaw` 或 `alaw`。OpenClaw 使用 xAI 的批次 REST TTS 端點，並回傳完整的音訊附件；此提供者路徑不使用 xAI 的串流 TTS WebSocket。此路徑不支援原生 Opus 語音留言格式。
  * **Microsoft** ：使用 `microsoft.outputFormat`（預設 `audio-24khz-48kbitrate-mono-mp3`）。 
    * 隨附的傳輸層接受 `outputFormat`，但並非所有格式都可由服務提供。
    * 輸出格式值遵循 Microsoft Speech 輸出格式（包含 Ogg/WebM Opus）。
    * Telegram `sendVoice` 接受 OGG/MP3/M4A；如果你需要 保證使用 Opus 語音訊息，請使用 OpenAI/ElevenLabs。
    * 如果已設定的 Microsoft 輸出格式失敗，OpenClaw 會以 MP3 重試。


OpenAI/ElevenLabs 輸出格式依頻道固定（見上方）。

## 自動 TTS 行為

啟用 `messages.tts.auto` 時，OpenClaw 會：

  * 如果回覆已包含媒體或 `MEDIA:` 指示詞，則略過 TTS。
  * 略過非常短的回覆（少於 10 個字元）。
  * 啟用摘要時，使用 `summaryModel`（或 `agents.defaults.model.primary`）摘要長回覆。
  * 將產生的音訊附加到回覆。
  * 在 `mode: "final"` 中，對於串流最終回覆，仍會在文字串流完成後 傳送純音訊 TTS；產生的媒體會經過與一般回覆附件相同的 頻道媒體正規化處理。


如果回覆超過 `maxLength` 且摘要關閉（或摘要模型沒有 API 金鑰）， 音訊會被略過，並傳送一般文字回覆。

textCopy code
[code]
    Reply -> TTS enabled?  no  -> send text  yes -> has media / MEDIA: / short?          yes -> send text          no  -> length > limit?                   no  -> TTS -> attach audio                   yes -> summary enabled?                            no  -> send text                            yes -> summarize -> TTS -> attach audio
[/code]

## 依頻道劃分的輸出格式

目標 | 格式  
---|---  
Feishu / Matrix / Telegram / WhatsApp | 語音訊息回覆偏好 **Opus** （ElevenLabs 的 `opus_48000_64`，OpenAI 的 `opus`）。48 kHz / 64 kbps 可在清晰度與大小之間取得平衡。  
其他頻道 | **MP3** （ElevenLabs 的 `mp3_44100_128`，OpenAI 的 `mp3`）。44.1 kHz / 128 kbps 為語音預設值。  
Talk / 電話語音 | 供應商原生 **PCM** （Inworld 22050 Hz、Google 24 kHz），或用於電話語音的 Gradium `ulaw_8000`。  
  
各供應商注意事項：

  * **Feishu / WhatsApp 轉碼：** 當語音訊息回覆以 MP3/WebM/WAV/M4A 抵達時，頻道 Plugin 會使用 `ffmpeg` 轉碼為 48 kHz Ogg/Opus。WhatsApp 會透過 Baileys 以 `ptt: true` 和 `audio/ogg; codecs=opus` 傳送。如果轉換失敗：Feishu 會退回為附加原始檔案；WhatsApp 則會傳送失敗，而不是發布不相容的 PTT 承載。
  * **MiniMax / Xiaomi MiMo：** 預設 MP3（MiniMax `speech-2.8-hd` 為 32 kHz）；會透過 `ffmpeg` 為語音訊息目標轉碼為 48 kHz Opus。
  * **本機 CLI：** 使用已設定的 `outputFormat`。語音訊息目標會轉換為 Ogg/Opus，電話語音輸出會轉換為原始 16 kHz 單聲道 PCM。
  * **Google Gemini：** 回傳原始 24 kHz PCM。OpenClaw 會包裝為 WAV 以供附件使用，為語音訊息目標轉碼為 48 kHz Opus，並直接為 Talk/電話語音回傳 PCM。
  * **Inworld：** MP3 附件、原生 `OGG_OPUS` 語音訊息、Talk/電話語音用的原始 `PCM` 22050 Hz。
  * **xAI：** 預設為 MP3；`responseFormat` 可以是 `mp3|wav|pcm|mulaw|alaw`。使用 xAI 的批次 REST 端點 — **不** 使用串流 WebSocket TTS。**不** 支援原生 Opus 語音訊息格式。
  * **Microsoft：** 使用 `microsoft.outputFormat`（預設 `audio-24khz-48kbitrate-mono-mp3`）。Telegram `sendVoice` 接受 OGG/MP3/M4A；如果你需要保證為 Opus 語音訊息，請使用 OpenAI/ElevenLabs。如果設定的 Microsoft 格式失敗，OpenClaw 會以 MP3 重試。


OpenAI 和 ElevenLabs 輸出格式會依照上方列出的各頻道固定。

## 欄位參考

Top-level messages.tts.*

自動 TTS 模式。`inbound` 只會在收到傳入語音訊息後傳送音訊；`tagged` 只會在回覆包含 `[[tts:...]]` 指令或 `[[tts:text]]` 區塊時傳送音訊。

舊版切換。`openclaw doctor --fix` 會將此遷移到 `auto`。

`"all"` 除了最終回覆外，也包含工具/區塊回覆。

語音供應商 ID。未設定時，OpenClaw 會依照登錄檔自動選取順序使用第一個已設定的供應商。舊版 `provider: "edge"` 會由 `openclaw doctor --fix` 改寫為 `"microsoft"`。

來自 `personas` 的作用中 persona ID。會正規化為小寫。

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBlcnNvbmFzLjxpZA " type="object"> 穩定的口語身分。欄位：`label`、`description`、`provider`、`fallbackPolicy`、`prompt`、`providers.<provider>`。請參閱 Personas。

自動摘要用的便宜模型；預設為 `agents.defaults.model.primary`。接受 `provider/model` 或已設定的模型別名。

允許模型發出 TTS 指令。`enabled` 預設為 `true`；`allowProvider` 預設為 `false`。

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb3ZpZGVycy48aWQ " type="object"> 由供應商擁有、以語音供應商 ID 作為鍵的設定。舊版直接區塊（`messages.tts.openai`、`.elevenlabs`、`.microsoft`、`.edge`）會由 `openclaw doctor --fix` 改寫；只提交 `messages.tts.providers.<id>`。

TTS 輸入字元的硬性上限。如果超過，`/tts audio` 會失敗。

請求逾時時間，以毫秒為單位。

覆寫本機偏好設定 JSON 路徑（供應商/限制/摘要）。預設 `~/.openclaw/settings/tts.json`。

Azure Speech

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg Env：`AZURE_SPEECH_KEY`、`AZURE_SPEECH_API_KEY` 或 `SPEECH_KEY`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlZ2lvbiIgdHlwZT0ic3RyaW5nIg Azure Speech 區域（例如 `eastus`）。Env：`AZURE_SPEECH_REGION` 或 `SPEECH_REGION`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVuZHBvaW50IiB0eXBlPSJzdHJpbmci 選用的 Azure Speech 端點覆寫（別名 `baseUrl`）。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Azure 語音 ShortName。預設 `en-US-JennyNeural`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI SSML 語言代碼。預設 `en-US`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg 標準音訊用的 Azure `X-Microsoft-OutputFormat`。預設 `audio-24khz-48kbitrate-mono-mp3`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTm90ZU91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg 語音訊息輸出用的 Azure `X-Microsoft-OutputFormat`。預設 `ogg-24khz-16bit-mono-opus`。 OPENCLAW_DOCS_MARKER:paramClose:

ElevenLabs

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg 退回使用 `ELEVENLABS_API_KEY` 或 `XI_API_KEY`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci 模型 ID（例如 `eleven_multilingual_v2`、`eleven_v3`）。 OPENCLAW_DOCS_MARKER:paramClose:

`stability`、`similarityBoost`、`style`（各為 `0..1`）、`useSpeakerBoost`（`true|false`）、`speed`（`0.5..2.0`，`1.0` = 正常）。

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlQ29kZSIgdHlwZT0ic3RyaW5nIg 2 字母 ISO 639-1（例如 `en`、`de`）。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNlZWQiIHR5cGU9Im51bWJlciI 整數 `0..4294967295`，用於盡力達成確定性。 OPENCLAW_DOCS_MARKER:paramClose:

Google Gemini

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg 退回使用 `GEMINI_API_KEY` / `GOOGLE_API_KEY`。如果省略，TTS 可以先重用 `models.providers.google.apiKey`，再退回使用 Env。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci Gemini TTS 模型。預設 `gemini-3.1-flash-tts-preview`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlTmFtZSIgdHlwZT0ic3RyaW5nIg Gemini 預建語音名稱。預設 `Kore`。別名：`voice`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InByb21wdFRlbXBsYXRlIiB0eXBlPSciYXVkaW8tcHJvZmlsZS12MSIn 設定為 `audio-profile-v1`，以確定性的 Gemini TTS 提示結構包裝作用中 persona 提示欄位。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI 只接受 `https://generativelanguage.googleapis.com`。 OPENCLAW_DOCS_MARKER:paramClose:

Gradium

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg 環境變數：`GRADIUM_API_KEY`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI 預設值 `https://api.gradium.ai`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI 預設 Emma (`YTpq7expH9539ERJ`)。 OPENCLAW_DOCS_MARKER:paramClose:

Inworld

### Inworld 主要設定

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg 環境變數：`INWORLD_API_KEY`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI 預設值 `https://api.inworld.ai`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsSWQiIHR5cGU9InN0cmluZyI 預設值 `inworld-tts-1.5-max`。另有：`inworld-tts-1.5-mini`、`inworld-tts-1-max`、`inworld-tts-1`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI 預設值 `Sarah`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRlbXBlcmF0dXJlIiB0eXBlPSJudW1iZXIi 取樣溫度 `0..2`。 OPENCLAW_DOCS_MARKER:paramClose:

本機 CLI (tts-local-cli)

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFyZ3MiIHR5cGU9InN0cmluZ1tdIg 命令引數。支援 `{{Text}}`、`{{OutputPath}}`、`{{OutputDir}}`、`{{OutputBase}}` 預留位置。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0nIm1wMyIgfCAib3B1cyIgfCAid2F2Iic 預期的 CLI 輸出格式。音訊附件預設為 `mp3`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InRpbWVvdXRNcyIgdHlwZT0ibnVtYmVyIg 命令逾時時間，單位為毫秒。預設值 `120000`。 OPENCLAW_DOCS_MARKER:paramClose:

Microsoft（無 API 金鑰）

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci Microsoft 類神經語音名稱（例如 `en-US-MichelleNeural`）。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImxhbmciIHR5cGU9InN0cmluZyI 語言代碼（例如 `en-US`）。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im91dHB1dEZvcm1hdCIgdHlwZT0ic3RyaW5nIg Microsoft 輸出格式。預設值 `audio-24khz-48kbitrate-mono-mp3`。隨附的 Edge 後端傳輸並不支援所有格式。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJhdGUgLyBwaXRjaCAvIHZvbHVtZSIgdHlwZT0ic3RyaW5nIg 百分比字串（例如 `+10%`、`-5%`）。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImVkZ2UuKiIgdHlwZT0ib2JqZWN0IiBkZXByZWNhdGVk 舊版別名。執行 `openclaw doctor --fix`，將已保存的設定重寫為 `providers.microsoft`。 OPENCLAW_DOCS_MARKER:paramClose:

MiniMax

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg 退回使用 `MINIMAX_API_KEY`。Token Plan 驗證可透過 `MINIMAX_OAUTH_TOKEN`、`MINIMAX_CODE_PLAN_KEY` 或 `MINIMAX_CODING_API_KEY`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI 預設值 `https://api.minimax.io`。環境變數：`MINIMAX_API_HOST`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci 預設值 `speech-2.8-hd`。環境變數：`MINIMAX_TTS_MODEL`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI 預設值 `English_expressive_narrator`。環境變數：`MINIMAX_TTS_VOICE_ID`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InNwZWVkIiB0eXBlPSJudW1iZXIi `0.5..2.0`。預設值 `1.0`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvbCIgdHlwZT0ibnVtYmVyIg `(0, 10]`。預設值 `1.0`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InBpdGNoIiB0eXBlPSJudW1iZXIi 整數 `-12..12`。預設值 `0`。請求前會截斷小數值。 OPENCLAW_DOCS_MARKER:paramClose:

OpenAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg 退回使用 `OPENAI_API_KEY`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci OpenAI TTS 模型 ID（例如 `gpt-4o-mini-tts`）。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci 語音名稱（例如 `alloy`、`cedar`）。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imluc3RydWN0aW9ucyIgdHlwZT0ic3RyaW5nIg 明確的 OpenAI `instructions` 欄位。設定後，角色提示欄位**不會** 自動對應。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImV4dHJhQm9keSAvIGV4dHJhX2JvZHkiIHR5cGU9IlJlY29yZDxzdHJpbmcsIHVua25vd24 ">在產生的 OpenAI TTS 欄位之後，合併到 `/audio/speech` 請求主體中的額外 JSON 欄位。適用於 OpenAI 相容端點，例如需要 `lang` 等供應商專屬鍵的 Kokoro；不安全的原型鍵會被忽略。 OPENCLAW_DOCS_MARKER:paramClose:

覆寫 OpenAI TTS 端點。解析順序：設定 → `OPENAI_TTS_BASE_URL` → `https://api.openai.com/v1`。非預設值會被視為 OpenAI 相容的 TTS 端點，因此可接受自訂模型與語音名稱。

OpenRouter

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg 環境變數：`OPENROUTER_API_KEY`。可重用 `models.providers.openrouter.apiKey`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI 預設值 `https://openrouter.ai/api/v1`。舊版 `https://openrouter.ai/v1` 會被正規化。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci 預設值 `hexgrad/kokoro-82m`。別名：`modelId`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci 預設值 `af_alloy`。別名：`voiceId`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJwY20iJw 預設值 `mp3`。 OPENCLAW_DOCS_MARKER:paramClose:

Volcengine（BytePlus Seed Speech）

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg 環境變數：`VOLCENGINE_TTS_API_KEY` 或 `BYTEPLUS_SEED_SPEECH_API_KEY`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc291cmNlSWQiIHR5cGU9InN0cmluZyI 預設值 `seed-tts-1.0`。環境變數：`VOLCENGINE_TTS_RESOURCE_ID`。當你的專案有 TTS 2.0 權益時，使用 `seed-tts-2.0`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcEtleSIgdHlwZT0ic3RyaW5nIg App 金鑰標頭。預設值 `aGjiRDfUWi`。環境變數：`VOLCENGINE_TTS_APP_KEY`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI 覆寫 Seed Speech TTS HTTP 端點。環境變數：`VOLCENGINE_TTS_BASE_URL`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci 語音類型。預設值 `en_female_anna_mars_bigtts`。環境變數：`VOLCENGINE_TTS_VOICE`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwcElkIC8gdG9rZW4gLyBjbHVzdGVyIiB0eXBlPSJzdHJpbmciIGRlcHJlY2F0ZWQ 舊版 Volcengine Speech Console 欄位。環境變數：`VOLCENGINE_TTS_APPID`、`VOLCENGINE_TTS_TOKEN`、`VOLCENGINE_TTS_CLUSTER`（預設值 `volcano_tts`）。 OPENCLAW_DOCS_MARKER:paramClose:

xAI

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg 環境變數：`XAI_API_KEY`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI 預設值 `https://api.x.ai/v1`。環境變數：`XAI_BASE_URL`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlSWQiIHR5cGU9InN0cmluZyI 預設值 `eve`。可用語音：`ara`、`eve`、`leo`、`rex`、`sal`、`una`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Imxhbmd1YWdlIiB0eXBlPSJzdHJpbmci BCP-47 語言代碼或 `auto`。預設值 `en`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InJlc3BvbnNlRm9ybWF0IiB0eXBlPScibXAzIiB8ICJ3YXYiIHwgInBjbSIgfCAibXVsYXciIHwgImFsYXciJw 預設值 `mp3`。 OPENCLAW_DOCS_MARKER:paramClose:

Xiaomi MiMo

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImFwaUtleSIgdHlwZT0ic3RyaW5nIg 環境變數：`XIAOMI_API_KEY`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImJhc2VVcmwiIHR5cGU9InN0cmluZyI 預設值 `https://api.xiaomimimo.com/v1`。環境變數：`XIAOMI_BASE_URL`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Im1vZGVsIiB0eXBlPSJzdHJpbmci 預設值 `mimo-v2.5-tts`。環境變數：`XIAOMI_TTS_MODEL`。也支援 `mimo-v2-tts`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9InZvaWNlIiB0eXBlPSJzdHJpbmci 預設值 `mimo_default`。環境變數：`XIAOMI_TTS_VOICE`。 OPENCLAW_DOCS_MARKER:paramClose:

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9ImZvcm1hdCIgdHlwZT0nIm1wMyIgfCAid2F2Iic 預設值 `mp3`。環境變數：`XIAOMI_TTS_FORMAT`。 OPENCLAW_DOCS_MARKER:paramClose:

## 代理工具

`tts` 工具會將文字轉換為語音，並回傳音訊附件以供回覆傳送。在 Feishu、Matrix、Telegram 和 WhatsApp 上，音訊會以語音訊息而非檔案附件傳送。當 `ffmpeg` 可用時，Feishu 和 WhatsApp 可在此路徑上轉碼非 Opus 的 TTS 輸出。

WhatsApp 會透過 Baileys 將音訊作為 PTT 語音備註（`audio` 搭配 `ptt: true`）傳送，並將可見文字與 PTT 音訊**分開** 傳送，因為用戶端不一定會一致地在語音備註上顯示字幕。

此工具接受選用的 `channel` 和 `timeoutMs` 欄位；`timeoutMs` 是每次呼叫的供應商請求逾時時間，單位為毫秒。

## Gateway RPC

方法 | 用途  
---|---  
`tts.status` | 讀取目前 TTS 狀態與上次嘗試。  
`tts.enable` | 將本機自動偏好設定為 `always`。  
`tts.disable` | 將本機自動偏好設定為 `off`。  
`tts.convert` | 一次性文字 → 音訊。  
`tts.setProvider` | 設定本機供應商偏好。  
`tts.setPersona` | 設定本機角色偏好。  
`tts.providers` | 列出已設定的供應商與狀態。  
  
## 服務連結

  * [OpenAI 文字轉語音指南](<https://platform.openai.com/docs/guides/text-to-speech>)
  * [OpenAI Audio API 參考](<https://platform.openai.com/docs/api-reference/audio>)
  * [Azure Speech REST 文字轉語音](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech>)
  * [Azure Speech 供應商](</zh-TW/providers/azure-speech>)
  * [ElevenLabs 文字轉語音](<https://elevenlabs.io/docs/api-reference/text-to-speech>)
  * [ElevenLabs 驗證](<https://elevenlabs.io/docs/api-reference/authentication>)
  * [Gradium](</zh-TW/providers/gradium>)
  * [Inworld TTS API](<https://docs.inworld.ai/tts/tts>)
  * [MiniMax T2A v2 API](<https://platform.minimaxi.com/document/T2A%20V2>)
  * [Volcengine TTS HTTP API](</zh-TW/providers/volcengine#text-to-speech>)
  * [Xiaomi MiMo 語音合成](</zh-TW/providers/xiaomi#text-to-speech>)
  * [node-edge-tts](<https://github.com/SchneeHertz/node-edge-tts>)
  * [Microsoft Speech 輸出格式](<https://learn.microsoft.com/azure/ai-services/speech-service/rest-text-to-speech#audio-outputs>)
  * [xAI 文字轉語音](<https://docs.x.ai/developers/rest-api-reference/inference/voice#text-to-speech-rest>)


## 相關

  * [媒體概覽](</zh-TW/tools/media-overview>)
  * [音樂生成](</zh-TW/tools/music-generation>)
  * [影片生成](</zh-TW/tools/video-generation>)
  * [斜線命令](</zh-TW/tools/slash-commands>)
  * [語音通話 Plugin](</zh-TW/plugins/voice-call>)


Was this useful?YesNo