---
title: 重設
source_url: https://docs.openclaw.ai/zh-TW/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

重設本機設定/狀態（保留已安裝的 CLI）。

選項：

  * `--scope <scope>`：`config`、`config+creds+sessions` 或 `full`
  * `--yes`：略過確認提示
  * `--non-interactive`：停用提示；需要 `--scope` 和 `--yes`
  * `--dry-run`：印出動作而不移除檔案


範例：

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

備註：

  * 如果你想在移除本機狀態前取得可還原的快照，請先執行 `openclaw backup create`。
  * 如果省略 `--scope`，`openclaw reset` 會使用互動式提示來選擇要移除的項目。
  * `--non-interactive` 只有在同時設定 `--scope` 和 `--yes` 時才有效。


## 相關

  * [CLI 參考](</zh-TW/cli>)


Was this useful?YesNo