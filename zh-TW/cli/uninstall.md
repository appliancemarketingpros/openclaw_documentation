---
title: 解除安裝
source_url: https://docs.openclaw.ai/zh-TW/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

解除安裝 Gateway 服務 + 本機資料（CLI 保留）。

選項：

  * `--service`：移除 Gateway 服務
  * `--state`：移除狀態和設定
  * `--workspace`：移除工作區目錄
  * `--app`：移除 macOS app
  * `--all`：移除服務、狀態、工作區和 app
  * `--yes`：略過確認提示
  * `--non-interactive`：停用提示；需要 `--yes`
  * `--dry-run`：列印動作但不移除檔案


範例：

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

注意事項：

  * 如果你想在移除狀態或工作區之前建立可還原的快照，請先執行 `openclaw backup create`。
  * `--all` 是同時移除服務、狀態、工作區和 app 的簡寫。
  * `--non-interactive` 需要 `--yes`。


## 相關

  * [CLI 參考](</zh-TW/cli>)
  * [解除安裝](</zh-TW/install/uninstall>)


Was this useful?YesNo