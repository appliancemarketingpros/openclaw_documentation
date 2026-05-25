---
title: 代理程式傳送
source_url: https://docs.openclaw.ai/zh-TW/tools/agent-send
scraped_at: 2026-05-25
---

`openclaw agent` 會從命令列執行單次代理程式回合，不需要 傳入的聊天訊息。可用於腳本化工作流程、測試與 程式化交付。

## 快速開始

* ### 執行簡單的代理程式回合

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

這會透過 Gateway 傳送訊息並列印回覆。

* ### 指定特定代理程式或工作階段

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### 將回覆交付至頻道

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## 旗標

旗標 | 說明  
---|---  
`--message \<text\>` | 要傳送的訊息（必填）  
`--to \<dest\>` | 從目標（電話、聊天 ID）衍生工作階段金鑰  
`--agent \<id\>` | 指定已設定的代理程式（使用其 `main` 工作階段）  
`--session-id \<id\>` | 依 ID 重用現有工作階段  
`--local` | 強制使用本機內嵌執行階段（略過 Gateway）  
`--deliver` | 將回覆傳送到聊天頻道  
`--channel \<name\>` | 交付頻道（whatsapp、telegram、discord、slack 等）  
`--reply-to \<target\>` | 覆寫交付目標  
`--reply-channel \<name\>` | 覆寫交付頻道  
`--reply-account \<id\>` | 覆寫交付帳戶 ID  
`--thinking \<level\>` | 設定所選模型設定檔的思考等級  
`--verbose \<on|full|off\>` | 設定詳細輸出等級  
`--timeout \<seconds\>` | 覆寫代理程式逾時時間  
`--json` | 輸出結構化 JSON  
  
## 行為

  * 預設情況下，CLI 會**透過 Gateway** 。加入 `--local` 可強制使用目前機器上的 內嵌執行階段。
  * 如果無法連線到 Gateway，CLI 會**回退** 到本機內嵌執行。
  * 工作階段選擇：`--to` 會衍生工作階段金鑰（群組/頻道目標 會保留隔離；直接聊天會合併到 `main`）。
  * 思考與詳細輸出旗標會保存在工作階段儲存區中。
  * 輸出：預設為純文字，或使用 `--json` 取得結構化承載 + 中繼資料。
  * 搭配 `--json --deliver` 時，JSON 會包含已傳送、 已抑制、部分與失敗傳送的交付狀態。請參閱 [JSON 交付狀態](</zh-TW/cli/agent#json-delivery-status>)。


## 範例

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## 相關

[**代理程式 CLI 參考** 完整的 `openclaw agent` 旗標與選項參考。 ](</zh-TW/cli/agent>) [**子代理程式** 背景子代理程式產生。 ](</zh-TW/tools/subagents>) [**工作階段** 工作階段金鑰的運作方式，以及 `--to`、`--agent` 和 `--session-id` 如何解析它們。 ](</zh-TW/concepts/session>) [**斜線指令** 代理程式工作階段內使用的原生命令目錄。 ](</zh-TW/tools/slash-commands>)

Was this useful?YesNo