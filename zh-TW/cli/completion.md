---
title: 完成
source_url: https://docs.openclaw.ai/zh-TW/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

產生 shell 補全指令碼，並可選擇安裝到你的 shell 設定檔。

## 使用方式

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## 選項

  * `-s, --shell <shell>`：shell 目標（`zsh`、`bash`、`powershell`、`fish`；預設：`zsh`）
  * `-i, --install`：透過在你的 shell 設定檔加入 source 行來安裝補全
  * `--write-state`：將補全指令碼寫入 `$OPENCLAW_STATE_DIR/completions`，不輸出到標準輸出
  * `-y, --yes`：略過安裝確認提示


## 注意事項

  * `--install` 會將一個小型的「OpenClaw 補全」區塊寫入你的 shell 設定檔，並指向快取的指令碼。
  * 若未使用 `--install` 或 `--write-state`，此命令會將指令碼輸出到標準輸出。
  * 補全產生會預先載入命令樹，因此會包含巢狀子命令。


## 相關

  * [CLI 參考](</zh-TW/cli>)


Was this useful?YesNo