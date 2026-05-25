---
title: 多 Agent 沙盒和工具
source_url: https://docs.openclaw.ai/zh-CN/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Each agent in a multi-agent setup can override the global sandbox and tool policy. This page covers per-agent configuration, precedence rules, and examples.

[**Sandboxing** 后端和模式 — 完整的沙箱参考。 ](</zh-CN/gateway/sandboxing>) [**Sandbox vs tool policy vs elevated** 调试“为什么这被阻止了？” ](</zh-CN/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Elevated mode** 面向受信任发送者的 elevated exec。 ](</zh-CN/tools/elevated>)

* * *

## 配置示例

Example 1: Personal + restricted family agent jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**结果：**

  * `main` agent：在主机上运行，拥有完整工具访问权限。
  * `family` agent：在 Docker 中运行（每个 agent 一个容器），仅允许 `read` 和当前对话消息发送。

Example 2: Work agent with shared sandbox jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Example 2b: Global coding profile + messaging-only agent jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**结果：**

  * 默认 agent 获得编码工具。
  * `support` agent 仅支持消息传递（+ Slack 工具）。

Example 3: Different sandbox modes per agent jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## 配置优先级

当同时存在全局配置（`agents.defaults.*`）和 agent 专属配置（`agents.list[].*`）时：

### 沙箱配置

agent 专属设置会覆盖全局设置：

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### 工具限制

过滤顺序如下：

* ### Tool profile

`tools.profile` 或 `agents.list[].tools.profile`。

* ### Provider tool profile

`tools.byProvider[provider].profile` 或 `agents.list[].tools.byProvider[provider].profile`。

* ### Global tool policy

`tools.allow` / `tools.deny`。

* ### Provider tool policy

`tools.byProvider[provider].allow/deny`。

* ### Agent-specific tool policy

`agents.list[].tools.allow/deny`。

* ### Agent provider policy

`agents.list[].tools.byProvider[provider].allow/deny`。

* ### Sandbox tool policy

`tools.sandbox.tools` 或 `agents.list[].tools.sandbox.tools`。

* ### Subagent tool policy

`tools.subagents.tools`，如适用。

Precedence rules

  * 每一层都可以进一步限制工具，但不能把前面层级已拒绝的工具重新授予回来。
  * 如果设置了 `agents.list[].tools.sandbox.tools`，它会替换该 agent 的 `tools.sandbox.tools`。
  * 如果设置了 `agents.list[].tools.profile`，它会覆盖该 agent 的 `tools.profile`。
  * 提供商工具键既可以接受 `provider`（例如 `google-antigravity`），也可以接受 `provider/model`（例如 `openai/gpt-5.4`）。

Empty allowlist behavior

如果该链路中的任何显式允许列表让本次运行没有任何可调用工具，OpenClaw 会在把 prompt 提交给模型之前停止。这是有意设计的：配置了缺失工具的 agent，例如 `agents.list[].tools.allow: ["query_db"]`，应当在注册 `query_db` 的插件启用之前明确失败，而不是作为纯文本 agent 继续运行。

工具策略支持 `group:*` 简写，它们会展开为多个工具。完整列表见 [工具组](</zh-CN/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>)。

每个 agent 的 elevated 覆盖项（`agents.list[].tools.elevated`）可以进一步限制特定 agent 的 elevated exec。详情见 [Elevated mode](</zh-CN/tools/elevated>)。

* * *

## 从单 Agent 迁移

### 迁移前（单 Agent）

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### 迁移后（多 Agent）

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## 工具限制示例

### 只读 Agent

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### 启用 Shell 执行但禁用文件系统工具

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### 仅通信

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

此配置文件中的 `sessions_history` 仍会返回一个有界且已清理的回忆视图，而不是原始转录转储。助手回忆会在编辑/截断之前剥离思考标签、`<relevant-memories>` 脚手架、纯文本工具调用 XML 负载（包括 `<tool_call>...</tool_call>`、`<function_call>...</function_call>`、`<tool_calls>...</tool_calls>`、`<function_calls>...</function_calls>` 和被截断的工具调用块）、降级的工具调用脚手架、泄漏的 ASCII/全角模型控制令牌，以及格式错误的 MiniMax 工具调用 XML。

* * *

## 常见陷阱："non-main"

* * *

## 测试

配置多 Agent 沙箱和工具后：

* ### 检查 Agent 解析

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### 验证沙箱容器

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### 测试工具限制

  * 发送一条需要受限工具的消息。
  * 验证 Agent 无法使用被拒绝的工具。


* ### 监控日志

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## 故障排除

尽管设置了 `mode: 'all'`，Agent 仍未被沙箱隔离

  * 检查是否存在覆盖它的全局 `agents.defaults.sandbox.mode`。
  * Agent 专用配置优先级更高，因此请设置 `agents.list[].sandbox.mode: "all"`。

尽管存在拒绝列表，工具仍然可用

  * 检查工具过滤顺序：全局 → Agent → 沙箱 → 子 Agent。
  * 每一层只能进一步限制，不能重新授予权限。
  * 使用日志验证：`[tools] filtering tools for agent:${agentId}`。

容器未按 Agent 隔离

  * 在 Agent 专用沙箱配置中设置 `scope: "agent"`。
  * 默认值是 `"session"`，即每个会话创建一个容器。


* * *

## 相关

  * [提权模式](</zh-CN/tools/elevated>)
  * [多 Agent 路由](</zh-CN/concepts/multi-agent>)
  * [沙箱配置](</zh-CN/gateway/config-agents#agentsdefaultssandbox>)
  * [沙箱与工具策略与提权](</zh-CN/gateway/sandbox-vs-tool-policy-vs-elevated>) — 调试“为什么这被阻止了？”
  * [沙箱隔离](</zh-CN/gateway/sandboxing>) — 完整沙箱参考（模式、范围、后端、镜像）
  * [会话管理](</zh-CN/concepts/session>)


Was this useful?YesNo