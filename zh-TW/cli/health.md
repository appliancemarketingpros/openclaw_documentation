---
title: 健康狀態
source_url: https://docs.openclaw.ai/zh-TW/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

從執行中的 Gateway 擷取健康狀態。

## 選項

旗標 | 預設值 | 說明  
---|---|---  
`--json` | `false` | 印出機器可讀的 JSON，而非文字。  
`--timeout <ms>` | `10000` | 連線逾時時間，以毫秒為單位。  
`--verbose` | `false` | 詳細記錄。強制執行即時探測，並展開每個代理程式的輸出。  
`--debug` | `false` | `--verbose` 的別名。  
  
範例：

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

注意事項：

  * 預設的 `openclaw health` 會向執行中的 Gateway 要求其健康狀態快照。當 Gateway 已有新鮮的快取快照時，它可以傳回該快取酬載，並在 背景重新整理。
  * `--verbose` 會強制執行即時探測、印出 Gateway 連線詳細資料，並展開 所有已設定帳號與代理程式的人類可讀輸出。
  * 當設定了多個代理程式時，輸出會包含每個代理程式的工作階段儲存區。


## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [Gateway 健康狀態](</zh-TW/gateway/health>)


Was this useful?YesNo