---
title: 提高權限模式
source_url: https://docs.openclaw.ai/zh-TW/tools/elevated
scraped_at: 2026-05-25
---

當代理在沙盒內執行時，它的 `exec` 命令會被限制在沙盒環境中。**Elevated 模式** 讓代理改為跳出沙盒，並在沙盒外執行命令，同時可設定核准閘門。

## 指令

使用斜線命令依工作階段控制 elevated 模式：

指令 | 作用  
---|---  
`/elevated on` | 在設定的主機路徑上於沙盒外執行，保留核准流程  
`/elevated ask` | 與 `on` 相同（別名）  
`/elevated full` | 在設定的主機路徑上於沙盒外執行，並略過核准流程  
`/elevated off` | 回到受沙盒限制的執行方式  
  
也可使用 `/elev on|off|ask|full`。

不帶引數傳送 `/elevated` 可查看目前層級。

## 運作方式

* ### Check availability

必須在設定中啟用 Elevated，且傳送者必須在允許清單中：

json5Copy code
[code]
    {  tools: {    elevated: {      enabled: true,      allowFrom: {        discord: ["user-id-123"],        whatsapp: ["+15555550123"],      },    },  },}
[/code]

* ### Set the level

傳送只有指令的訊息來設定工作階段預設值：

CodeCopy code
[code]
    /elevated full
[/code]

或以內嵌方式使用（只套用到該訊息）：

CodeCopy code
[code]
    /elevated on run the deployment script
[/code]

* ### Commands run outside the sandbox

啟用 elevated 後，`exec` 呼叫會離開沙盒。有效主機預設為 `gateway`，或在設定/工作階段 exec 目標為 `node` 時使用 `node`。在 `full` 模式中，會略過 exec 核准流程。在 `on`/`ask` 模式中，仍會套用設定的核准規則。

## 解析順序

  1. 訊息上的**內嵌指令** （只套用到該訊息）
  2. **工作階段覆寫** （透過傳送只有指令的訊息設定）
  3. **全域預設值** （設定中的 `agents.defaults.elevatedDefault`）


## 可用性與允許清單

  * **全域閘門** ：`tools.elevated.enabled`（必須為 `true`）
  * **傳送者允許清單** ：`tools.elevated.allowFrom` 搭配各通道清單
  * **各代理閘門** ：`agents.list[].tools.elevated.enabled`（只能進一步限制）
  * **各代理允許清單** ：`agents.list[].tools.elevated.allowFrom`（傳送者必須同時符合全域與各代理條件）
  * **Discord 後援** ：如果省略 `tools.elevated.allowFrom.discord`，會使用 `channels.discord.allowFrom` 作為後援
  * **所有閘門都必須通過** ；否則 elevated 會被視為不可用


允許清單項目格式：

前綴 | 符合項目  
---|---  
（無） | 傳送者 ID、E.164 或 From 欄位  
`name:` | 傳送者顯示名稱  
`username:` | 傳送者使用者名稱  
`tag:` | 傳送者標籤  
`id:`, `from:`, `e164:` | 明確指定身分  
  
## elevated 不控制的項目

  * **工具政策** ：如果 `exec` 被工具政策拒絕，elevated 無法覆寫。
  * **主機選擇政策** ：elevated 不會將 `auto` 變成可任意跨主機覆寫的模式。它會使用設定/工作階段 exec 目標規則，只有在目標已經是 `node` 時才選擇 `node`。
  * **與`/exec` 分開**：`/exec` 指令會為已授權的傳送者調整各工作階段的 exec 預設值，且不需要 elevated 模式。


## 相關

[**Exec tool** 從代理執行 shell 命令。 ](</zh-TW/tools/exec>) [**Exec approvals** `exec` 的核准與允許清單系統。 ](</zh-TW/tools/exec-approvals>) [**Sandboxing** Gateway 層級的沙盒設定。 ](</zh-TW/gateway/sandboxing>) [**Sandbox vs Tool Policy vs Elevated** 三個閘門在工具呼叫期間如何組合。 ](</zh-TW/gateway/sandbox-vs-tool-policy-vs-elevated>)

Was this useful?YesNo