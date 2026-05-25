---
title: 沙箱 CLI
source_url: https://docs.openclaw.ai/zh-CN/cli/sandbox
scraped_at: 2026-05-25
---

管理用于隔离智能体执行的沙箱运行时。

## 概览

OpenClaw 可以在隔离的沙箱运行时中运行智能体以提高安全性。`sandbox` 命令可帮助你在更新或配置变更后检查并重新创建这些运行时。

目前这通常意味着：

  * Docker 沙箱容器
  * 当 `agents.defaults.sandbox.backend = "ssh"` 时的 SSH 沙箱运行时
  * 当 `agents.defaults.sandbox.backend = "openshell"` 时的 OpenShell 沙箱运行时


对于 `ssh` 和 OpenShell `remote`，重新创建比 Docker 更重要：

  * 初始播种后，远程工作区是规范来源
  * `openclaw sandbox recreate` 会删除所选范围的规范远程工作区
  * 下次使用时会从当前本地工作区再次播种


## 命令

### `openclaw sandbox explain`

检查**生效的** 沙箱模式/范围/工作区访问权限、沙箱工具策略，以及提权门禁（包含修复用配置键路径）。

bashCopy code
[code]
    openclaw sandbox explainopenclaw sandbox explain --session agent:main:mainopenclaw sandbox explain --agent workopenclaw sandbox explain --json
[/code]

### `openclaw sandbox list`

列出所有沙箱运行时及其状态和配置。

bashCopy code
[code]
    openclaw sandbox listopenclaw sandbox list --browser  # List only browser containersopenclaw sandbox list --json     # JSON output
[/code]

**输出包括：**

  * 运行时名称和状态
  * 后端（`docker`、`openshell` 等）
  * 配置标签，以及它是否匹配当前配置
  * 存续时间（自创建以来的时间）
  * 空闲时间（自上次使用以来的时间）
  * 关联的会话/智能体


### `openclaw sandbox recreate`

移除沙箱运行时，以强制使用更新后的配置重新创建。

bashCopy code
[code]
    openclaw sandbox recreate --all                # Recreate all containersopenclaw sandbox recreate --session main       # Specific sessionopenclaw sandbox recreate --agent mybot        # Specific agentopenclaw sandbox recreate --browser            # Only browser containersopenclaw sandbox recreate --all --force        # Skip confirmation
[/code]

**选项：**

  * `--all`：重新创建所有沙箱容器
  * `--session <key>`：为特定会话重新创建容器
  * `--agent <id>`：为特定智能体重新创建容器
  * `--browser`：仅重新创建浏览器容器
  * `--force`：跳过确认提示


## 使用场景

### 更新 Docker 镜像后

bashCopy code
[code]
    # Pull new imagedocker pull openclaw-sandbox:latestdocker tag openclaw-sandbox:latest openclaw-sandbox:bookworm-slim # Update config to use new image# Edit config: agents.defaults.sandbox.docker.image (or agents.list[].sandbox.docker.image) # Recreate containersopenclaw sandbox recreate --all
[/code]

### 更改沙箱配置后

bashCopy code
[code]
    # Edit config: agents.defaults.sandbox.* (or agents.list[].sandbox.*) # Recreate to apply new configopenclaw sandbox recreate --all
[/code]

### 更改 SSH 目标或 SSH 认证材料后

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - agents.defaults.sandbox.ssh.target# - agents.defaults.sandbox.ssh.workspaceRoot# - agents.defaults.sandbox.ssh.identityFile / certificateFile / knownHostsFile# - agents.defaults.sandbox.ssh.identityData / certificateData / knownHostsData openclaw sandbox recreate --all
[/code]

对于核心 `ssh` 后端，重新创建会删除 SSH 目标上对应范围的远程工作区根目录。下一次运行会从本地工作区再次播种。

### 更改 OpenShell 来源、策略或模式后

bashCopy code
[code]
    # Edit config:# - agents.defaults.sandbox.backend# - plugins.entries.openshell.config.from# - plugins.entries.openshell.config.mode# - plugins.entries.openshell.config.policy openclaw sandbox recreate --all
[/code]

对于 OpenShell `remote` 模式，重新创建会删除该范围的规范远程工作区。下一次运行会从本地工作区再次播种。

### 更改 setupCommand 后

bashCopy code
[code]
    openclaw sandbox recreate --all# or just one agent:openclaw sandbox recreate --agent family
[/code]

### 仅针对特定智能体

bashCopy code
[code]
    # Update only one agent's containersopenclaw sandbox recreate --agent alfred
[/code]

## 为什么需要这样做

当你更新沙箱配置时：

  * 现有运行时会继续使用旧设置运行。
  * 运行时只有在空闲 24 小时后才会被清理。
  * 经常使用的智能体会让旧运行时无限期保持存活。


使用 `openclaw sandbox recreate` 强制移除旧运行时。下次需要时，它们会使用当前设置自动重新创建。

## 注册表迁移

OpenClaw 会将沙箱运行时元数据存储为沙箱状态目录下每个容器/浏览器条目对应的一个 JSON 分片。较旧的安装可能仍有单体旧版文件：

  * `~/.openclaw/sandbox/containers.json`
  * `~/.openclaw/sandbox/browsers.json`


常规沙箱运行时读取不会重写这些文件。运行 `openclaw doctor --fix` 可将有效的旧版条目迁移到分片注册表目录中。无效的旧版文件会被隔离，避免一个损坏的旧注册表隐藏当前运行时条目。

## 配置

沙箱设置位于 `~/.openclaw/openclaw.json` 的 `agents.defaults.sandbox` 下（按智能体覆盖项放在 `agents.list[].sandbox` 中）：

jsoncCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "all", // off, non-main, all        "backend": "docker", // docker, ssh, openshell        "scope": "agent", // session, agent, shared        "docker": {          "image": "openclaw-sandbox:bookworm-slim",          "containerPrefix": "openclaw-sbx-",          // ... more Docker options        },        "prune": {          "idleHours": 24, // Auto-prune after 24h idle          "maxAgeDays": 7, // Auto-prune after 7 days        },      },    },  },}
[/code]

## 相关

  * [CLI 参考](</zh-CN/cli>)
  * [沙箱隔离](</zh-CN/gateway/sandboxing>)
  * [Agent 工作区](</zh-CN/concepts/agent-workspace>)
  * [Doctor](</zh-CN/gateway/doctor>)：检查沙箱设置。


Was this useful?YesNo