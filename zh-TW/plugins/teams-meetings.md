---
title: Microsoft Teams 會議外掛
source_url: https://docs.openclaw.ai/zh-TW/plugins/teams-meetings
scraped_at: 2026-07-20
---

CapabilitiesPlugin guides

`teams-meetings` 外掛會以訪客身分，在 OpenClaw Chrome 設定檔中加入 Microsoft Teams 連結。它接受 `teams.microsoft.com/l/meetup-join/...` 下的工作連結，以及 `teams.live.com/meet/...` 下的消費者連結。它不會建立會議、透過電話撥入、呼叫 Microsoft Graph 或錄製會議。

## 設定

語音回覆使用與 [Google Meet 外掛](</zh-TW/plugins/google-meet>)相同的本機音訊必要條件：macOS、`BlackHole 2ch` 虛擬音訊裝置和 SoX。

bashCopy code
[code]
    brew install blackhole-2ch soxsudo rebootsystem_profiler SPAudioDataType | grep -i BlackHolecommand -v sox
[/code]

啟用外掛，然後檢查設定：

json5Copy code
[code]
    {  plugins: {    entries: {      "teams-meetings": {        enabled: true,        config: {          defaultMode: "agent",          chrome: { guestName: "OpenClaw Agent" },        },      },    },  },}
[/code]

bashCopy code
[code]
    openclaw teamsmeetings setupopenclaw teamsmeetings join 'https://teams.microsoft.com/l/meetup-join/...'
[/code]

使用 `chromeNode.node` 在已配對的 macOS 節點上執行 Chrome、BlackHole 和 SoX。該節點必須允許 `teamsmeetings.chrome` 和 `browser.proxy`。

## 模式

模式 | 行為  
---|---  
`agent` | 即時轉錄會諮詢已設定的 OpenClaw 代理程式；由 TTS 回覆。  
`bidi` | 即時語音模型會直接聆聽並回覆。  
`transcribe` | 僅觀察加入，並擷取即時字幕轉錄快照。  
  
轉錄模式會在獲准加入後啟用 Teams 即時字幕，並擷取標示發言者的字幕列。`transcript` 動作會傳回目前 OpenClaw 會議工作階段中有界限的字幕緩衝區。

## 訪客加入限制

瀏覽器轉接器會關閉應用程式插頁、填入訪客名稱、關閉相機、依所選模式設定麥克風，並按一下加入按鈕。通話中狀態會使用掛斷控制項；大廳、租用戶登入和裝置權限狀態則會傳回明確的手動操作原因。支援消費者會議啟動器重新導向，以及 Chrome 顯示的 `BlackHole 2ch (Virtual)` 標籤。

Teams 租用戶原則可能要求登入、電子郵件驗證或由組織者核准加入。請在 OpenClaw Chrome 設定檔中完成該步驟，然後重新嘗試狀態查詢或語音。外掛不會繞過租用戶原則。

消費者版 Teams 網頁用戶端已針對以下項目完成實際驗證：應用程式插頁、訪客名稱輸入、加入前的麥克風／相機切換、加入、大廳准入、媒體權限、通話中偵測、即時字幕、BlackHole 輸入／輸出路由、離開，以及通話後偵測。工作租用戶可能實施不同的登入、電子郵件驗證、准入和離開確認原則；請在 OpenClaw Chrome 設定檔中完成所有回報的手動操作。

## 工具與閘道介面

`teams_meetings` 代理程式工具支援 `join`、`leave`、`status`、`transcript` 和 `speak`。閘道方法使用 `teamsmeetings.*` 前綴。節點命令為 `teamsmeetings.chrome`。

## 相關內容

  * [會議外掛概覽](</zh-TW/plugins/meeting-plugins>)
  * [Microsoft Teams 頻道](</zh-TW/channels/msteams>)


Was this useful?YesNo

Open issue