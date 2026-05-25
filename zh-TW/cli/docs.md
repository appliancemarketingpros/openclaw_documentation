---
title: 文件
source_url: https://docs.openclaw.ai/zh-TW/cli/docs
scraped_at: 2026-05-25
---

# `openclaw docs`

從終端機搜尋即時 OpenClaw docs 索引。此命令會透過 shell 呼叫公開、由 Mintlify 代管的 docs MCP 搜尋端點 `https://docs.openclaw.ai/mcp.SearchOpenClaw`，並在你的終端機中呈現結果。

## 用法

bashCopy code
[code]
    openclaw docs                       # print docs entrypoint and example searchopenclaw docs <query...>            # search the live docs index
[/code]

引數：

引數 | 說明  
---|---  
`[query...]` | 自由格式搜尋查詢。多字詞查詢會以空格串接，並作為單一查詢傳送。  
  
## 範例

bashCopy code
[code]
    openclaw docs browser existing-sessionopenclaw docs sandbox allowHostControlopenclaw docs gateway token secretref
[/code]

沒有查詢時，`openclaw docs` 會列印 docs 進入點 URL 加上一個範例搜尋命令，而不是執行搜尋。

## 運作方式

`openclaw docs` 會叫用 `mcporter` CLI 來呼叫 docs 搜尋 MCP 工具，然後將工具輸出中的 `Title: / Link: / Content:` 區塊剖析為結果清單。

為解析 `mcporter`，OpenClaw 會依序檢查：

  1. `PATH` 上的 `mcporter`（若存在則直接使用）。
  2. 若已安裝 `pnpm`，則使用 `pnpm dlx mcporter ...`。
  3. 若已安裝 `npx`，則使用 `npx -y mcporter ...`。


如果都不可用，命令會失敗，並提示安裝 `pnpm`（`npm install -g pnpm`）。

搜尋呼叫使用固定的 30 秒逾時。結果摘要會截斷為每筆約 220 個字元。

## 輸出

在豐富（TTY）終端機中，結果會呈現為標題後接項目符號清單。每個項目符號會顯示頁面標題、連結的 docs URL，以及下一行的簡短摘要。空結果會列印「沒有結果。」。

在非豐富輸出（管線、`--no-color`、腳本）中，相同資料會呈現為 Markdown：

markdownCopy code
[code]
    # Docs search: <query> - [Title](https://docs.openclaw.ai/...) - snippet- [Title](https://docs.openclaw.ai/...) - snippet
[/code]

## 結束代碼

代碼 | 意義  
---|---  
`0` | 搜尋成功（包括零結果回應）。  
`1` | MCP 工具呼叫失敗；stderr 會內嵌列印。  
  
## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [即時 docs](<https://docs.openclaw.ai>)


Was this useful?YesNo