---
title: Vydra
source_url: https://docs.openclaw.ai/zh-TW/providers/vydra
scraped_at: 2026-05-25
---

隨附的 Vydra Plugin 會加入：

  * 透過 `vydra/grok-imagine` 產生圖片
  * 透過 `vydra/veo3` 和 `vydra/kling` 產生影片
  * 透過 Vydra 由 ElevenLabs 支援的 TTS 路由進行語音合成


OpenClaw 對這三項功能使用相同的 `VYDRA_API_KEY`。

屬性 | 值  
---|---  
提供者 ID | `vydra`  
Plugin | 隨附，`enabledByDefault: true`  
驗證環境變數 | `VYDRA_API_KEY`  
Onboarding 旗標 | `--auth-choice vydra-api-key`  
直接 CLI 旗標 | `--vydra-api-key <key>`  
契約 | `imageGenerationProviders`, `videoGenerationProviders`, `speechProviders`  
基礎 URL | `https://www.vydra.ai/api/v1`（使用 `www` 主機）  
  
## 設定

* ### 執行互動式 onboarding

bashCopy code
[code]
    openclaw onboard --auth-choice vydra-api-key
[/code]

或直接設定環境變數：

bashCopy code
[code]
    export VYDRA_API_KEY="vydra_live_..."
[/code]

* ### 選擇預設功能

在下方功能中選擇一或多項（圖片、影片或語音），並套用相符的設定。

## 功能

圖片生成

預設圖片模型：

  * `vydra/grok-imagine`


將其設為預設圖片提供者：

json5Copy code
[code]
    {  agents: {    defaults: {      imageGenerationModel: {        primary: "vydra/grok-imagine",      },    },  },}
[/code]

目前的隨附支援僅限文字轉圖片。Vydra 託管的編輯路由預期使用遠端圖片 URL，而 OpenClaw 尚未在隨附的 Plugin 中加入 Vydra 專用的上傳橋接。

影片生成

已註冊的影片模型：

  * `vydra/veo3` 用於文字轉影片
  * `vydra/kling` 用於圖片轉影片


將 Vydra 設為預設影片提供者：

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "vydra/veo3",      },    },  },}
[/code]

注意事項：

  * `vydra/veo3` 隨附為僅限文字轉影片。
  * `vydra/kling` 目前需要遠端圖片 URL 參照。本機檔案上傳會預先遭到拒絕。
  * Vydra 目前的 `kling` HTTP 路由在是否需要 `image_url` 或 `video_url` 方面一直不一致；隨附的提供者會將相同的遠端圖片 URL 對應到這兩個欄位。
  * 隨附的 Plugin 維持保守，不會轉送未記載的風格旋鈕，例如外觀比例、解析度、浮水印或生成音訊。

影片即時測試

提供者專屬的即時涵蓋範圍：

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 \OPENCLAW_LIVE_VYDRA_VIDEO=1 \pnpm test:live -- extensions/vydra/vydra.live.test.ts
[/code]

隨附的 Vydra 即時檔案現在涵蓋：

  * `vydra/veo3` 文字轉影片
  * `vydra/kling` 使用遠端圖片 URL 進行圖片轉影片


需要時覆寫遠端圖片 fixture：

bashCopy code
[code]
    export OPENCLAW_LIVE_VYDRA_KLING_IMAGE_URL="https://example.com/reference.png"
[/code]

語音合成

將 Vydra 設為語音提供者：

json5Copy code
[code]
    {  messages: {    tts: {      provider: "vydra",      providers: {        vydra: {          apiKey: "${VYDRA_API_KEY}",          voiceId: "21m00Tcm4TlvDq8ikWAM",        },      },    },  },}
[/code]

預設值：

  * 模型：`elevenlabs/tts`
  * 語音 ID：`21m00Tcm4TlvDq8ikWAM`


隨附的 Plugin 目前公開一個已知良好的預設語音，並傳回 MP3 音訊檔案。

## 相關

[**提供者目錄** 瀏覽所有可用的提供者。 ](</zh-TW/providers>) [**圖片生成** 共用圖片工具參數和提供者選擇。 ](</zh-TW/tools/image-generation>) [**影片生成** 共用影片工具參數和提供者選擇。 ](</zh-TW/tools/video-generation>) [**設定參考** Agent 預設值和模型設定。 ](</zh-TW/gateway/config-agents#agent-defaults>)

Was this useful?YesNo