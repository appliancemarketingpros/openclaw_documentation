---
title: 跑道
source_url: https://docs.openclaw.ai/zh-TW/providers/runway
scraped_at: 2026-05-25
---

OpenClaw 隨附一個用於託管影片生成的 `runway` 提供者。此 Plugin 預設啟用，並針對 `videoGenerationProviders` 合約註冊 `runway` 提供者。

屬性 | 值  
---|---  
提供者 id | `runway`  
Plugin | 隨附，`enabledByDefault: true`  
驗證環境變數 | `RUNWAYML_API_SECRET`（標準）或 `RUNWAY_API_KEY`  
入門設定旗標 | `--auth-choice runway-api-key`  
直接 CLI 旗標 | `--runway-api-key <key>`  
API | Runway 以任務為基礎的影片生成（`GET /v1/tasks/{id}` 輪詢）  
預設模型 | `runway/gen4.5`  
  
## 開始使用

* ### 設定 API 金鑰

bashCopy code
[code]
    openclaw onboard --auth-choice runway-api-key
[/code]

* ### 將 Runway 設為預設影片提供者

bashCopy code
[code]
    openclaw config set agents.defaults.videoGenerationModel.primary "runway/gen4.5"
[/code]

* ### 生成影片

要求代理生成影片。Runway 將會自動使用。

## 支援的模式與模型

此提供者公開七個 Runway 模型，分布於三種模式。同一個模型 id 可支援多種模式（例如 `gen4.5` 同時適用於文字轉影片與圖片轉影片）。

模式 | 模型 | 參考輸入  
---|---|---  
文字轉影片 | `gen4.5`（預設）、`veo3.1`、`veo3.1_fast`、`veo3` | 無  
圖片轉影片 | `gen4.5`、`gen4_turbo`、`gen3a_turbo`、`veo3.1`、`veo3.1_fast`、`veo3` | 1 張本機或遠端圖片  
影片轉影片 | `gen4_aleph` | 1 段本機或遠端影片  
  
本機圖片與影片參考支援透過 data URIs 使用。

長寬比 | 允許的值  
---|---  
文字轉影片 | `16:9`、`9:16`  
圖片與影片編輯 | `1:1`、`16:9`、`9:16`、`3:4`、`4:3`、`21:9`  
  
## 設定

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "runway/gen4.5",      },    },  },}
[/code]

## 進階設定

環境變數別名

OpenClaw 可辨識 `RUNWAYML_API_SECRET`（標準）與 `RUNWAY_API_KEY`。 任一變數都可驗證 Runway 提供者。

任務輪詢

Runway 使用以任務為基礎的 API。提交生成請求後，OpenClaw 會輪詢 `GET /v1/tasks/{id}`，直到影片準備完成。輪詢行為不需要額外 設定。

## 相關

[**影片生成** 共用工具參數、提供者選擇與非同步行為。 ](</zh-TW/tools/video-generation>) [**設定參考** 包含影片生成模型在內的代理預設設定。 ](</zh-TW/gateway/config-agents#agent-defaults>)

Was this useful?YesNo