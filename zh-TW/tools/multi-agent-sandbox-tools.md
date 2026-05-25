---
title: 多代理沙盒與工具
source_url: https://docs.openclaw.ai/zh-TW/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

每個多代理設定中的代理都可以覆寫全域沙盒和工具政策。本頁說明每代理設定、優先順序規則與範例。

[**沙盒化** 後端與模式 — 完整沙盒參考。 ](</zh-TW/gateway/sandboxing>) [**沙盒 vs 工具政策 vs 提權** 偵錯「為什麼這被封鎖？」 ](</zh-TW/gateway/sandbox-vs-tool-policy-vs-elevated>) [**提權模式** 受信任傳送者的提權執行。 ](</zh-TW/tools/elevated>)

* * *

## 設定範例

範例 1：個人 + 受限的家庭代理 jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**結果：**

  * `main` 代理：在主機上執行，擁有完整工具存取權。
  * `family` 代理：在 Docker 中執行（每個代理一個容器），僅允許 `read` 和目前對話訊息傳送。

範例 2：使用共用沙盒的工作代理 jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

範例 2b：全域程式碼設定檔 + 僅限訊息的代理 jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**結果：**

  * 預設代理會取得程式碼工具。
  * `support` 代理僅限訊息（+ Slack 工具）。

範例 3：每個代理使用不同沙盒模式 jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## 設定優先順序

當全域（`agents.defaults.*`）和代理特定（`agents.list[].*`）設定同時存在時：

### 沙盒設定

代理特定設定會覆寫全域設定：

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### 工具限制

篩選順序如下：

* ### 工具設定檔

`tools.profile` 或 `agents.list[].tools.profile`。

* ### 提供者工具設定檔

`tools.byProvider[provider].profile` 或 `agents.list[].tools.byProvider[provider].profile`。

* ### 全域工具政策

`tools.allow` / `tools.deny`。

* ### 提供者工具政策

`tools.byProvider[provider].allow/deny`。

* ### 代理特定工具政策

`agents.list[].tools.allow/deny`。

* ### 代理提供者政策

`agents.list[].tools.byProvider[provider].allow/deny`。

* ### 沙盒工具政策

`tools.sandbox.tools` 或 `agents.list[].tools.sandbox.tools`。

* ### 子代理工具政策

`tools.subagents.tools`，如適用。

優先順序規則

  * 每個層級都可以進一步限制工具，但無法重新授予先前層級已拒絕的工具。
  * 如果設定了 `agents.list[].tools.sandbox.tools`，它會取代該代理的 `tools.sandbox.tools`。
  * 如果設定了 `agents.list[].tools.profile`，它會覆寫該代理的 `tools.profile`。
  * 提供者工具鍵可接受 `provider`（例如 `google-antigravity`）或 `provider/model`（例如 `openai/gpt-5.4`）。

空白允許清單行為

如果該鏈中的任何明確允許清單使該次執行沒有可呼叫的工具，OpenClaw 會在將提示提交給模型前停止。這是刻意設計：設定了遺失工具（例如 `agents.list[].tools.allow: ["query_db"]`）的代理應該明確失敗，直到註冊 `query_db` 的 Plugin 啟用為止，而不是繼續作為純文字代理。

工具政策支援會展開為多個工具的 `group:*` 簡寫。完整清單請參閱[工具群組](</zh-TW/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>)。

每代理提權覆寫（`agents.list[].tools.elevated`）可以進一步限制特定代理的提權執行。詳情請參閱[提權模式](</zh-TW/tools/elevated>)。

* * *

## 從單一代理遷移

### 之前（單一代理）

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### 之後（多代理）

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## 工具限制範例

### 唯讀代理

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### 停用檔案系統工具的 Shell 執行

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### 僅通訊

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

此設定檔中的 `sessions_history` 仍會傳回有界且已清理的回憶檢視，而不是原始逐字記錄傾印。助理回憶會在遮罩/截斷之前移除思考標籤、`<relevant-memories>` 鷹架、純文字工具呼叫 XML 酬載（包括 `<tool_call>...</tool_call>`、`<function_call>...</function_call>`、`<tool_calls>...</tool_calls>`、`<function_calls>...</function_calls>`，以及被截斷的工具呼叫區塊）、降級的工具呼叫鷹架、外洩的 ASCII/全形模型控制權杖，以及格式錯誤的 MiniMax 工具呼叫 XML。

* * *

## 常見陷阱："non-main"

* * *

## 測試

設定多代理沙盒和工具之後：

* ### 檢查代理解析

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### 驗證沙盒容器

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### 測試工具限制

  * 傳送需要受限工具的訊息。
  * 確認代理無法使用被拒絕的工具。


* ### 監控日誌

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## 疑難排解

儘管 `mode: 'all'`，代理仍未套用沙盒

  * 檢查是否有全域 `agents.defaults.sandbox.mode` 覆寫它。
  * 代理專屬設定優先，因此請設定 `agents.list[].sandbox.mode: "all"`。

儘管有拒絕清單，工具仍可使用

  * 檢查工具篩選順序：全域 → 代理 → 沙盒 → 子代理。
  * 每個層級只能進一步限制，不能重新授權。
  * 使用日誌驗證：`[tools] filtering tools for agent:${agentId}`。

容器未依代理隔離

  * 在代理專屬沙盒設定中設定 `scope: "agent"`。
  * 預設為 `"session"`，會為每個工作階段建立一個容器。


* * *

## 相關

  * [提權模式](</zh-TW/tools/elevated>)
  * [多代理路由](</zh-TW/concepts/multi-agent>)
  * [沙盒設定](</zh-TW/gateway/config-agents#agentsdefaultssandbox>)
  * [沙盒、工具政策與提權](</zh-TW/gateway/sandbox-vs-tool-policy-vs-elevated>) — 除錯「為什麼這被封鎖？」
  * [沙盒化](</zh-TW/gateway/sandboxing>) — 完整沙盒參考（模式、範圍、後端、映像檔）
  * [工作階段管理](</zh-TW/concepts/session>)


Was this useful?YesNo