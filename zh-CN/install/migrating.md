---
title: 迁移指南
source_url: https://docs.openclaw.ai/zh-CN/install/migrating
scraped_at: 2026-05-25
---

OpenClaw 支持三种迁移路径：从另一个智能体系统导入、将现有安装移到新机器，以及就地升级插件。

## 从另一个智能体系统导入

使用内置迁移提供商将指令、MCP 服务器、Skills、模型配置和（可选）API 密钥导入 OpenClaw。任何更改前都会先预览计划，报告中会遮蔽密钥，应用更改时会有经过验证的备份作为支撑。

[**从 Claude 迁移** 导入 Claude Code 和 Claude Desktop 状态，包括 `CLAUDE.md`、MCP 服务器、Skills 和项目命令。 ](</zh-CN/install/migrating-claude>) [**从 Hermes 迁移** 导入 Hermes 配置、提供商、MCP 服务器、记忆、Skills 和受支持的 `.env` 键。 ](</zh-CN/install/migrating-hermes>)

CLI 入口点是 [`openclaw migrate`](</zh-CN/cli/migrate>)。当新手引导检测到已知来源时，也可以提供迁移（`openclaw onboard --flow import`）。

## 将 OpenClaw 移到新机器

复制**状态目录** （默认是 `~/.openclaw/`）和你的**工作区** ，以保留：

  * **配置** — `openclaw.json` 和所有 Gateway 网关设置。
  * **凭证** — 每个智能体的 `auth-profiles.json`（API 密钥和 OAuth），以及 `credentials/` 下的任何渠道或提供商状态。
  * **会话** — 对话历史和智能体状态。
  * **渠道状态** — WhatsApp 登录、Telegram 会话，以及类似内容。
  * **工作区文件** — `MEMORY.md`、`USER.md`、Skills 和提示词。


### 迁移步骤

* ### 停止 Gateway 网关并备份

在**旧** 机器上停止 Gateway 网关，避免文件在复制过程中发生变化，然后归档：

bashCopy code
[code]
    openclaw gateway stopcd ~tar -czf openclaw-state.tgz .openclaw
[/code]

如果你使用多个配置（例如 `~/.openclaw-work`），请分别归档每一个。

* ### 在新机器上安装 OpenClaw

在新机器上[安装](</zh-CN/install>) CLI（如有需要也安装 Node）。如果新手引导创建了新的 `~/.openclaw/`，也没有问题。下一步会覆盖它。

* ### 复制状态目录和工作区

通过 `scp`、`rsync -a` 或外部硬盘传输归档，然后解压：

bashCopy code
[code]
    cd ~tar -xzf openclaw-state.tgz
[/code]

确保隐藏目录已包含在内，并且文件所有权与将运行 Gateway 网关的用户一致。

* ### 运行 Doctor 并验证

在新机器上运行 [Doctor](</zh-CN/gateway/doctor>)，应用配置迁移并修复服务：

bashCopy code
[code]
    openclaw doctoropenclaw gateway restartopenclaw status
[/code]

如果 Telegram 或 Discord 使用默认环境变量回退（`TELEGRAM_BOT_TOKEN` 或 `DISCORD_BOT_TOKEN`），请验证迁移后的状态目录 `.env` 是否包含这些键，同时不要打印密钥值：

bashCopy code
[code]
    awk -F= '/^(TELEGRAM_BOT_TOKEN|DISCORD_BOT_TOKEN)=/ { print $1 "=present" }' ~/.openclaw/.env
[/code]

当已启用的默认 Telegram 或 Discord 账号没有配置令牌，并且 Doctor 进程无法使用匹配的环境变量时，`openclaw doctor` 也会发出警告。

### 常见陷阱

配置或状态目录不匹配

如果旧 Gateway 网关使用了 `--profile` 或 `OPENCLAW_STATE_DIR`，而新的没有使用，渠道会显示为已登出，会话也会为空。用你迁移的**同一个** 配置或状态目录启动 Gateway 网关，然后重新运行 `openclaw doctor`。

只复制 openclaw.json

仅配置文件还不够。模型凭证配置文件位于 `agents/<agentId>/agent/auth-profiles.json` 下，渠道和提供商状态位于 `credentials/` 下。请始终迁移**整个** 状态目录。

权限和所有权

如果你以 root 身份复制，或切换了用户，Gateway 网关可能无法读取凭证。确保状态目录和工作区归运行 Gateway 网关的用户所有。

远程模式

如果你的 UI 指向**远程** Gateway 网关，会话和工作区归远程主机所有。迁移 Gateway 网关主机本身，而不是你的本地笔记本电脑。参见[常见问题](</zh-CN/help/faq#where-things-live-on-disk>)。

备份中的密钥

状态目录包含凭证配置文件、渠道凭证和其他提供商状态。请加密存储备份，避免使用不安全的传输渠道；如果你怀疑发生暴露，请轮换密钥。

### 验证清单

在新机器上确认：

  * [ ] `openclaw status` 显示 Gateway 网关正在运行。
  * [ ] 渠道仍保持连接（无需重新配对）。
  * [ ] 仪表盘可以打开，并显示现有会话。
  * [ ] 工作区文件（记忆、配置）存在。


## 就地升级插件

就地插件升级会保留相同的插件 ID 和配置键，但可能会把磁盘上的状态移入当前布局。插件专属升级指南与其渠道放在一起：

  * [Matrix 迁移](</zh-CN/channels/matrix-migration>)：加密状态恢复限制、自动快照行为和手动恢复命令。


## 相关内容

  * [`openclaw migrate`](</zh-CN/cli/migrate>)：跨系统导入的 CLI 参考。
  * [安装概览](</zh-CN/install>)：所有安装方法。
  * [Doctor](</zh-CN/gateway/doctor>)：迁移后的健康检查。
  * [卸载](</zh-CN/install/uninstall>)：干净地移除 OpenClaw。


Was this useful?YesNo