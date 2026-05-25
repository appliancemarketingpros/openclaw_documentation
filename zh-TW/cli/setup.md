---
title: 設定
source_url: https://docs.openclaw.ai/zh-TW/cli/setup
scraped_at: 2026-05-25
---

# `openclaw setup`

初始化基準設定和代理程式工作區。若存在任何入門設定旗標，也會執行精靈。

## 選項

旗標 | 說明  
---|---  
`--workspace <dir>` | 代理程式工作區目錄（預設為 `~/.openclaw/workspace`；儲存為 `agents.defaults.workspace`）。  
`--wizard` | 執行互動式入門設定。  
`--non-interactive` | 不顯示提示並執行入門設定。  
`--mode <mode>` | 入門設定模式：`local` 或 `remote`。  
`--import-from <provider>` | 入門設定期間要執行的遷移提供者。  
`--import-source <path>` | `--import-from` 的來源代理程式主目錄。  
`--import-secrets` | 在入門設定遷移期間匯入支援的機密。  
`--remote-url <url>` | 遠端 Gateway WebSocket URL。  
`--remote-token <token>` | 遠端 Gateway 權杖（選用）。  
  
### 精靈自動觸發

當明確存在以下任一旗標時，即使沒有 `--wizard`，`openclaw setup` 也會執行精靈：

`--wizard`、`--non-interactive`、`--mode`、`--import-from`、`--import-source`、`--import-secrets`、`--remote-url`、`--remote-token`。

## 範例

bashCopy code
[code]
    openclaw setupopenclaw setup --workspace ~/.openclaw/workspaceopenclaw setup --wizardopenclaw setup --wizard --import-from hermes --import-source ~/.hermesopenclaw setup --non-interactive --mode remote --remote-url wss://gateway-host:18789 --remote-token <token>
[/code]

## 注意事項

  * 一般的 `openclaw setup` 會初始化設定和工作區，而不會執行完整的入門設定流程。
  * 完成一般 setup 後，執行 `openclaw onboard` 進行完整引導流程，執行 `openclaw configure` 進行目標式變更，或執行 `openclaw channels add` 新增頻道帳戶。
  * 如果偵測到 Hermes 狀態，互動式入門設定可以自動提供遷移選項。匯入入門設定需要全新的 setup；若要在入門設定之外產生試跑計畫、備份和使用覆寫模式，請使用 [遷移](</zh-TW/cli/migrate>)。


## 相關內容

  * [CLI 參考](</zh-TW/cli>)
  * [入門設定 (CLI)](</zh-TW/start/wizard>)
  * [開始使用](</zh-TW/start/getting-started>)
  * [安裝概覽](</zh-TW/install>)


Was this useful?YesNo