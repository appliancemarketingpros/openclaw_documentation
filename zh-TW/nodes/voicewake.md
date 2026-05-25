---
title: 語音喚醒
source_url: https://docs.openclaw.ai/zh-TW/nodes/voicewake
scraped_at: 2026-05-25
---

OpenClaw 將**喚醒詞視為單一全域清單** ，由 **Gateway** 擁有。

  * **沒有每個節點各自的自訂喚醒詞** 。
  * **任何節點/應用程式 UI 都可以編輯** 此清單；變更會由 Gateway 持久化並廣播給所有人。
  * macOS 和 iOS 保留本機的**語音喚醒啟用/停用** 切換（本機 UX 與權限不同）。
  * Android 目前維持關閉語音喚醒，並在語音分頁中使用手動麥克風流程。


## 儲存（Gateway 主機）

喚醒詞儲存在 Gateway 機器上的：

  * `~/.openclaw/settings/voicewake.json`


形狀：

jsonCopy code
[code]
    { "triggers": ["openclaw", "claude", "computer"], "updatedAtMs": 1730000000000 }
[/code]

## 協定

### 方法

  * `voicewake.get` → `{ triggers: string[] }`
  * `voicewake.set` 搭配參數 `{ triggers: string[] }` → `{ triggers: string[] }`


注意事項：

  * 觸發詞會正規化（修剪空白、移除空值）。空清單會回退到預設值。
  * 會強制執行安全限制（數量/長度上限）。


### 路由方法（觸發詞 → 目標）

  * `voicewake.routing.get` → `{ config: VoiceWakeRoutingConfig }`
  * `voicewake.routing.set` 搭配參數 `{ config: VoiceWakeRoutingConfig }` → `{ config: VoiceWakeRoutingConfig }`


`VoiceWakeRoutingConfig` 形狀：

jsonCopy code
[code]
    {  "version": 1,  "defaultTarget": { "mode": "current" },  "routes": [{ "trigger": "robot wake", "target": { "sessionKey": "agent:main:main" } }],  "updatedAtMs": 1730000000000}
[/code]

路由目標僅支援以下其中一種：

  * `{ "mode": "current" }`
  * `{ "agentId": "main" }`
  * `{ "sessionKey": "agent:main:main" }`


### 事件

  * `voicewake.changed` 酬載 `{ triggers: string[] }`
  * `voicewake.routing.changed` 酬載 `{ config: VoiceWakeRoutingConfig }`


接收者：

  * 所有 WebSocket 用戶端（macOS 應用程式、WebChat 等）
  * 所有已連線的節點（iOS/Android），且在節點連線時也會推送初始的「目前狀態」。


## 用戶端行為

### macOS 應用程式

  * 使用全域清單來控管 `VoiceWakeRuntime` 觸發詞。
  * 在語音喚醒設定中編輯「觸發詞」會呼叫 `voicewake.set`，然後依靠廣播讓其他用戶端保持同步。


### iOS 節點

  * 使用全域清單供 `VoiceWakeManager` 偵測觸發詞。
  * 在設定中編輯喚醒詞會呼叫 `voicewake.set`（透過 Gateway WS），也會讓本機喚醒詞偵測保持即時回應。


### Android 節點

  * Android 執行階段/設定目前已停用語音喚醒。
  * Android 語音使用語音分頁中的手動麥克風擷取，而不是喚醒詞觸發。


## 相關

  * [對話模式](</zh-TW/nodes/talk>)
  * [音訊與語音備註](</zh-TW/nodes/audio>)
  * [媒體理解](</zh-TW/nodes/media-understanding>)


Was this useful?YesNo