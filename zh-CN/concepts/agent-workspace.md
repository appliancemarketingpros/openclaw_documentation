---
title: Agent 工作区
source_url: https://docs.openclaw.ai/zh-CN/concepts/agent-workspace
scraped_at: 2026-05-25
---

工作区是智能体的家。它是文件工具和工作区上下文使用的唯一工作目录。请保持其私密，并将其视为记忆。

这不同于 `~/.openclaw/`，后者存储配置、凭证和会话。

## 默认位置

  * 默认：`~/.openclaw/workspace`
  * 如果设置了 `OPENCLAW_PROFILE` 且它不是 `"default"`，默认位置会变为 `~/.openclaw/workspace-<profile>`。
  * 在 `~/.openclaw/openclaw.json` 中覆盖：

json5Copy code
[code]
    {  agents: {    defaults: {      workspace: "~/.openclaw/workspace",    },  },}
[/code]

如果缺少工作区和引导文件，`openclaw onboard`、`openclaw configure` 或 `openclaw setup` 会创建它们并写入初始内容。

如果你已经自己管理工作区文件，可以禁用引导文件创建：

json5Copy code
[code]
    { agents: { defaults: { skipBootstrap: true } } }
[/code]

## 额外工作区文件夹

较旧的安装可能创建了 `~/openclaw`。保留多个工作区目录可能导致令人困惑的身份验证或状态漂移，因为同一时间只有一个工作区处于活动状态。

## 工作区文件映射

这些是 OpenClaw 期望在工作区内存在的标准文件：

AGENTS.md - 操作指令

智能体的操作指令，以及它应如何使用记忆。每个会话开始时加载。适合放置规则、优先级和“如何表现”的细节。

SOUL.md - 人设和语气

人设、语气和边界。每个会话都会加载。指南：[SOUL.md 人格指南](</zh-CN/concepts/soul>)。

USER.md - 用户是谁

用户是谁，以及如何称呼他们。每个会话都会加载。

IDENTITY.md - 名称、气质、emoji

智能体的名称、气质和 emoji。在引导仪式期间创建/更新。

TOOLS.md - 本地工具约定

关于你的本地工具和约定的说明。它不控制工具可用性；仅提供指导。

HEARTBEAT.md - heartbeat 检查清单

用于 heartbeat 运行的可选微型检查清单。保持简短以避免 token 消耗。

BOOT.md - 启动检查清单

在 Gateway 网关重启时自动运行的可选启动检查清单（当启用[内部钩子](</zh-CN/automation/hooks>)时）。保持简短；使用消息工具发送外发消息。

BOOTSTRAP.md - 首次运行仪式

一次性首次运行仪式。只会为全新的工作区创建。仪式完成后删除它。

memory/YYYY-MM-DD.md - 每日记忆日志

每日记忆日志（每天一个文件）。建议在会话开始时读取今天 + 昨天。

MEMORY.md - 精选长期记忆（可选）

精选长期记忆：持久事实、偏好、决策和简短摘要。将详细日志保存在 `memory/YYYY-MM-DD.md` 中，这样记忆工具可以按需检索，而不会把它们注入到每个提示中。只在主私有会话中加载 `MEMORY.md`（不要在共享/群组上下文中加载）。有关工作流和自动记忆刷新，请参阅[记忆](</zh-CN/concepts/memory>)。

skills/ - 工作区 Skills（可选）

工作区专属 Skills。该工作区中优先级最高的 Skills 位置。名称冲突时会覆盖项目智能体 Skills、个人智能体 Skills、托管 Skills、内置 Skills 和 `skills.load.extraDirs`。

canvas/ - Canvas UI 文件（可选）

用于节点显示的 Canvas UI 文件（例如 `canvas/index.html`）。

## 工作区中不包含什么

以下内容位于 `~/.openclaw/` 下，不应提交到工作区仓库：

  * `~/.openclaw/openclaw.json`（配置）
  * `~/.openclaw/agents/<agentId>/agent/auth-profiles.json`（模型身份验证配置：OAuth + API 密钥）
  * `~/.openclaw/agents/<agentId>/agent/codex-home/`（每智能体的 Codex runtime 账户、配置、Skills、插件和原生线程状态）
  * `~/.openclaw/credentials/`（渠道/提供商状态以及旧版 OAuth 导入数据）
  * `~/.openclaw/agents/<agentId>/sessions/`（会话转录 + 元数据）
  * `~/.openclaw/skills/`（托管 Skills）


如果你需要迁移会话或配置，请单独复制它们，并将它们排除在版本控制之外。

## Git 备份（建议，私有）

将工作区视为私有记忆。将它放入**私有** git 仓库，以便备份和恢复。

在运行 Gateway 网关的机器上执行这些步骤（工作区就在那台机器上）。

* ### 初始化仓库

如果安装了 git，全新的工作区会自动初始化。如果此工作区还不是仓库，请运行：

bashCopy code
[code]
    cd ~/.openclaw/workspacegit initgit add AGENTS.md SOUL.md TOOLS.md IDENTITY.md USER.md HEARTBEAT.md memory/git commit -m "Add agent workspace"
[/code]

* ### 添加私有远程仓库

### GitHub Web UI

  1. 在 GitHub 上创建新的**私有** 仓库。
  2. 不要用 README 初始化（避免合并冲突）。
  3. 复制 HTTPS 远程 URL。
  4. 添加远程仓库并推送：

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

### GitHub CLI (gh)

bashCopy code
[code]
    gh auth logingh repo create openclaw-workspace --private --source . --remote origin --push
[/code]

### GitLab Web UI

  1. 在 GitLab 上创建新的**私有** 仓库。
  2. 不要用 README 初始化（避免合并冲突）。
  3. 复制 HTTPS 远程 URL。
  4. 添加远程仓库并推送：

bashCopy code
[code]
    git branch -M maingit remote add origin <https-url>git push -u origin main
[/code]

* ### 持续更新

bashCopy code
[code]
    git statusgit add .git commit -m "Update memory"git push
[/code]

## 不要提交密钥

建议的 `.gitignore` 起始内容：

gitignoreCopy code
[code]
    .DS_Store.env**/*.key**/*.pem**/secrets*
[/code]

## 将工作区迁移到新机器

* ### 克隆仓库

将仓库克隆到所需路径（默认 `~/.openclaw/workspace`）。

* ### 更新配置

在 `~/.openclaw/openclaw.json` 中将 `agents.defaults.workspace` 设置为该路径。

* ### 填充缺失文件

运行 `openclaw setup --workspace <path>` 以填充任何缺失文件。

* ### 复制会话（可选）

如果你需要会话，请从旧机器单独复制 `~/.openclaw/agents/<agentId>/sessions/`。

## 高级说明

  * 多智能体路由可以为每个智能体使用不同工作区。有关路由配置，请参阅[频道路由](</zh-CN/channels/channel-routing>)。
  * 如果启用了 `agents.defaults.sandbox`，非主会话可以使用 `agents.defaults.sandbox.workspaceRoot` 下的按会话沙箱工作区。


## 相关

  * [Heartbeat](</zh-CN/gateway/heartbeat>) \- [HEARTBEAT.md](<http://HEARTBEAT.md>) 工作区文件
  * [沙箱隔离](</zh-CN/gateway/sandboxing>) \- 沙箱隔离环境中的工作区访问
  * [会话](</zh-CN/concepts/session>) \- 会话存储路径
  * [常设指令](</zh-CN/automation/standing-orders>) \- 工作区文件中的持久指令


Was this useful?YesNo