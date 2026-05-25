---
title: 卸载
source_url: https://docs.openclaw.ai/zh-CN/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

卸载 Gateway 网关服务和本地数据（CLI 会保留）。

选项：

  * `--service`：移除 Gateway 网关服务
  * `--state`：移除状态和配置
  * `--workspace`：移除工作区目录
  * `--app`：移除 macOS 应用
  * `--all`：移除服务、状态、工作区和应用
  * `--yes`：跳过确认提示
  * `--non-interactive`：禁用提示；需要配合 `--yes`
  * `--dry-run`：打印将执行的操作而不删除文件


示例：

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

说明：

  * 如果你想在移除状态或工作区之前保留一个可恢复的快照，请先运行 `openclaw backup create`。
  * `--all` 是同时移除服务、状态、工作区和应用的简写。
  * `--non-interactive` 需要配合 `--yes`。


## 相关内容

  * [CLI 参考](</zh-CN/cli>)
  * [卸载](</zh-CN/install/uninstall>)


Was this useful?YesNo