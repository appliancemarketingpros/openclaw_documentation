---
title: 补全
source_url: https://docs.openclaw.ai/zh-CN/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

生成 shell 补全脚本，并可选择将其安装到你的 shell 配置文件中。

## 用法

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## 选项

  * `-s, --shell <shell>`：shell 目标（`zsh`、`bash`、`powershell`、`fish`；默认值：`zsh`）
  * `-i, --install`：通过向你的 shell 配置文件添加一行 source 语句来安装补全
  * `--write-state`：将补全脚本写入 `$OPENCLAW_STATE_DIR/completions`，而不打印到 stdout
  * `-y, --yes`：跳过安装确认提示


## 说明

  * `--install` 会在你的 shell 配置文件中写入一个小型的 “OpenClaw Completion” 区块，并将其指向已缓存的脚本。
  * 不使用 `--install` 或 `--write-state` 时，该命令会将脚本打印到 stdout。
  * 补全生成会预先加载命令树，因此会包含嵌套子命令。


## 相关内容

  * [CLI 参考](</zh-CN/cli>)


Was this useful?YesNo