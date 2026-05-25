---
title: 重置
source_url: https://docs.openclaw.ai/zh-CN/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

重置本地配置/状态（保留 CLI 已安装）。

选项：

  * `--scope <scope>`：`config`、`config+creds+sessions` 或 `full`
  * `--yes`：跳过确认提示
  * `--non-interactive`：禁用提示；需要同时设置 `--scope` 和 `--yes`
  * `--dry-run`：打印操作内容而不删除文件


示例：

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

说明：

  * 如果你想在删除本地状态前保留一个可恢复的快照，请先运行 `openclaw backup create`。
  * 如果你省略 `--scope`，`openclaw reset` 会使用交互式提示来选择要删除的内容。
  * `--non-interactive` 仅在同时设置 `--scope` 和 `--yes` 时有效。


## 相关内容

  * [CLI 参考](</zh-CN/cli>)


Was this useful?YesNo