---
title: 引導
source_url: https://docs.openclaw.ai/zh-TW/tools/steer
scraped_at: 2026-05-25
---

`/steer` 會將指引傳送給已在作用中的執行。它用於「在這次執行仍在工作時調整它」的情境，而不是用來開始新的回合。

## 目前工作階段

使用頂層 `/steer` 來指定目前工作階段的作用中執行：

textCopy code
[code]
    /steer prefer the smaller patch and keep the tests focused/tell summarize before making the next tool call
[/code]

行為：

  * 只指定目前工作階段的作用中執行。
  * 獨立於工作階段的 `/queue` 模式運作。
  * 當工作階段閒置時，不會開始新的執行。
  * 當沒有可引導的作用中執行時，會回覆警告。
  * 使用作用中 runtime 的引導路徑，因此模型會在下一個支援的 runtime 邊界看到該指引。


## 引導與佇列

`/queue steer` 會變更一般傳入訊息在執行作用中時到達的行為。`/steer <message>` 是明確命令，會嘗試在下一個支援的 runtime 邊界，將該命令的訊息注入作用中執行，不受已儲存的 `/queue` 設定影響。

使用：

  * 當你想立即引導作用中執行時，使用 `/steer <message>`。
  * 當你想讓未來的一般訊息預設引導作用中執行時，使用 `/queue steer`。
  * 當新訊息應等待稍後回合，而不是引導作用中執行時，使用 `/queue collect` 或 `/queue followup`。


如需佇列模式與備援行為，請參閱[命令佇列](</zh-TW/concepts/queue>)和[引導佇列](</zh-TW/concepts/queue-steering>)。

## 子代理

當目標是子執行時，使用 `/subagents steer`：

textCopy code
[code]
    /subagents steer 2 focus only on the API surface
[/code]

頂層 `/steer` 不會依 id 或清單索引選取子代理。它一律指定目前工作階段的作用中執行。請參閱[子代理](</zh-TW/tools/subagents>)，了解子代理 id、標籤與控制命令。

## ACP 工作階段

當目標是 ACP harness 工作階段時，使用 `/acp steer`：

textCopy code
[code]
    /acp steer --session agent:main:acp:codex tighten the repro
[/code]

請參閱 [ACP 代理](</zh-TW/tools/acp-agents>)，了解 ACP 工作階段選取與 runtime 行為。

## 相關

  * [斜線命令](</zh-TW/tools/slash-commands>)
  * [命令佇列](</zh-TW/concepts/queue>)
  * [引導佇列](</zh-TW/concepts/queue-steering>)
  * [子代理](</zh-TW/tools/subagents>)


Was this useful?YesNo