---
title: Skills
source_url: https://docs.openclaw.ai/zh-CN/cli/skills
scraped_at: 2026-05-25
---

# `openclaw skills`

检查本地 Skills，并从 ClawHub 安装/更新 Skills。

相关：

  * Skills 系统：[Skills](</zh-CN/tools/skills>)
  * Skills 配置：[Skills 配置](</zh-CN/tools/skills-config>)
  * ClawHub 安装：[ClawHub](</zh-CN/clawhub/cli>)


## 命令

bashCopy code
[code]
    openclaw skills search "calendar"openclaw skills search --limit 20 --jsonopenclaw skills install <slug>openclaw skills install <slug> --version <version>openclaw skills install <slug> --forceopenclaw skills install <slug> --agent <id>openclaw skills update <slug>openclaw skills update --allopenclaw skills update --all --agent <id>openclaw skills listopenclaw skills list --eligibleopenclaw skills list --jsonopenclaw skills list --verboseopenclaw skills list --agent <id>openclaw skills info <name>openclaw skills info <name> --jsonopenclaw skills info <name> --agent <id>openclaw skills checkopenclaw skills check --agent <id>openclaw skills check --json
[/code]

`search`/`install`/`update` 直接使用 ClawHub，并安装到当前 workspace 的 `skills/` 目录。`list`/`info`/`check` 仍会检查当前 workspace 和配置可见的本地 Skills。基于 workspace 的命令会先从 `--agent <id>` 解析目标 workspace，然后在当前工作目录位于已配置的 agent workspace 内时使用当前工作目录，最后使用默认 agent。

这个 CLI `install` 命令会从 ClawHub 下载技能文件夹。从新手引导或 Skills 设置触发的、由 Gateway 网关支持的技能依赖安装改用单独的 `skills.install` 请求路径。

注意：

  * `search [query...]` 接受可选查询；省略它即可浏览默认的 ClawHub 搜索动态。
  * `search --limit <n>` 会限制返回结果数量。
  * `install --force` 会覆盖同一 slug 已存在的 workspace 技能文件夹。
  * `--agent <id>` 以一个已配置的 agent workspace 为目标，并覆盖当前 工作目录推断。
  * `update --all` 只更新当前 workspace 中已跟踪的 ClawHub 安装。
  * `check --agent <id>` 会检查所选 agent 的 workspace，并报告哪些 已就绪的 Skills 实际可见于该 agent 的提示词或命令界面。
  * 未提供子命令时，`list` 是默认操作。
  * `list`、`info` 和 `check` 会将其渲染后的输出写入 stdout。使用 `--json` 时，这意味着机器可读的载荷会保留在 stdout，供管道和脚本使用。


## 相关

  * [CLI 参考](</zh-CN/cli>)
  * [Skills](</zh-CN/tools/skills>)


Was this useful?YesNo