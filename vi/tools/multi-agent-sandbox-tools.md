---
title: Môi trường cách ly và công cụ đa tác nhân
source_url: https://docs.openclaw.ai/vi/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Mỗi agent trong một thiết lập đa agent có thể ghi đè sandbox và chính sách công cụ toàn cục. Trang này trình bày cấu hình theo từng agent, quy tắc ưu tiên và ví dụ.

[**Sandboxing** Backend và chế độ — tài liệu tham chiếu đầy đủ về sandbox. ](</vi/gateway/sandboxing>) [**Sandbox vs tool policy vs elevated** Gỡ lỗi "tại sao nội dung này bị chặn?" ](</vi/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Elevated mode** Exec nâng quyền cho người gửi đáng tin cậy. ](</vi/tools/elevated>)

* * *

## Ví dụ cấu hình

Example 1: Personal + restricted family agent jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Kết quả:**

  * Agent `main`: chạy trên máy chủ, có toàn quyền truy cập công cụ.
  * Agent `family`: chạy trong Docker (một container cho mỗi agent), chỉ có `read` và gửi tin nhắn trong cuộc trò chuyện hiện tại.

Example 2: Work agent with shared sandbox jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Example 2b: Global coding profile + messaging-only agent jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Kết quả:**

  * agent mặc định nhận các công cụ lập trình.
  * agent `support` chỉ dành cho nhắn tin (+ công cụ Slack).

Example 3: Different sandbox modes per agent jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Thứ tự ưu tiên cấu hình

Khi cả cấu hình toàn cục (`agents.defaults.*`) và cấu hình riêng cho agent (`agents.list[].*`) cùng tồn tại:

### Cấu hình sandbox

Thiết lập riêng cho agent ghi đè thiết lập toàn cục:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Hạn chế công cụ

Thứ tự lọc là:

* ### Tool profile

`tools.profile` hoặc `agents.list[].tools.profile`.

* ### Provider tool profile

`tools.byProvider[provider].profile` hoặc `agents.list[].tools.byProvider[provider].profile`.

* ### Global tool policy

`tools.allow` / `tools.deny`.

* ### Provider tool policy

`tools.byProvider[provider].allow/deny`.

* ### Agent-specific tool policy

`agents.list[].tools.allow/deny`.

* ### Agent provider policy

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Sandbox tool policy

`tools.sandbox.tools` hoặc `agents.list[].tools.sandbox.tools`.

* ### Subagent tool policy

`tools.subagents.tools`, nếu áp dụng.

Precedence rules

  * Mỗi cấp có thể hạn chế thêm công cụ, nhưng không thể cấp lại các công cụ đã bị từ chối ở các cấp trước.
  * Nếu `agents.list[].tools.sandbox.tools` được đặt, nó sẽ thay thế `tools.sandbox.tools` cho agent đó.
  * Nếu `agents.list[].tools.profile` được đặt, nó sẽ ghi đè `tools.profile` cho agent đó.
  * Khóa công cụ của provider chấp nhận `provider` (ví dụ `google-antigravity`) hoặc `provider/model` (ví dụ `openai/gpt-5.4`).

Empty allowlist behavior

Nếu bất kỳ allowlist rõ ràng nào trong chuỗi đó khiến lượt chạy không còn công cụ nào có thể gọi, OpenClaw sẽ dừng trước khi gửi prompt cho model. Đây là hành vi có chủ đích: một agent được cấu hình với công cụ bị thiếu như `agents.list[].tools.allow: ["query_db"]` nên thất bại rõ ràng cho đến khi Plugin đăng ký `query_db` được bật, thay vì tiếp tục như một agent chỉ dùng văn bản.

Chính sách công cụ hỗ trợ các dạng viết tắt `group:*` mở rộng thành nhiều công cụ. Xem [Nhóm công cụ](</vi/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>) để biết danh sách đầy đủ.

Ghi đè nâng quyền theo từng agent (`agents.list[].tools.elevated`) có thể hạn chế thêm exec nâng quyền cho các agent cụ thể. Xem [Chế độ nâng quyền](</vi/tools/elevated>) để biết chi tiết.

* * *

## Di chuyển từ một tác tử

### Trước (một tác tử)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### Sau (đa tác tử)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## Ví dụ về hạn chế công cụ

### Tác tử chỉ đọc

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### Thực thi shell khi công cụ hệ thống tệp bị tắt

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### Chỉ giao tiếp

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

`sessions_history` trong hồ sơ này vẫn trả về một chế độ xem nhớ lại có giới hạn và đã được làm sạch, thay vì bản đổ transcript thô. Việc nhớ lại của trợ lý loại bỏ các thẻ suy nghĩ, khung `<relevant-memories>`, payload XML gọi công cụ dạng văn bản thuần (bao gồm `<tool_call>...</tool_call>`, `<function_call>...</function_call>`, `<tool_calls>...</tool_calls>`, `<function_calls>...</function_calls>`, và các khối gọi công cụ đã bị cắt ngắn), khung gọi công cụ bị hạ cấp, token điều khiển mô hình ASCII/toàn chiều rộng bị rò rỉ, và XML gọi công cụ MiniMax sai định dạng trước khi biên tập/cắt ngắn.

* * *

## Lỗi thường gặp: "non-main"

* * *

## Kiểm thử

Sau khi cấu hình sandbox và công cụ đa tác tử:

* ### Kiểm tra phân giải tác tử

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### Xác minh container sandbox

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### Kiểm tra hạn chế công cụ

  * Gửi một tin nhắn yêu cầu các công cụ bị hạn chế.
  * Xác minh tác tử không thể dùng các công cụ bị từ chối.


* ### Theo dõi log

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## Khắc phục sự cố

Tác tử không bị sandbox dù có `mode: 'all'`

  * Kiểm tra xem có `agents.defaults.sandbox.mode` toàn cục ghi đè nó không.
  * Cấu hình riêng của tác tử được ưu tiên, nên hãy đặt `agents.list[].sandbox.mode: "all"`.

Công cụ vẫn khả dụng dù có danh sách từ chối

  * Kiểm tra thứ tự lọc công cụ: toàn cục → tác tử → sandbox → tác tử con.
  * Mỗi cấp chỉ có thể hạn chế thêm, không thể cấp lại.
  * Xác minh bằng log: `[tools] filtering tools for agent:${agentId}`.

Container không được cô lập theo từng tác tử

  * Đặt `scope: "agent"` trong cấu hình sandbox riêng của tác tử.
  * Mặc định là `"session"`, tạo một container cho mỗi phiên.


* * *

## Liên quan

  * [Chế độ nâng quyền](</vi/tools/elevated>)
  * [Định tuyến đa tác nhân](</vi/concepts/multi-agent>)
  * [Cấu hình hộp cát](</vi/gateway/config-agents#agentsdefaultssandbox>)
  * [Hộp cát so với chính sách công cụ so với nâng quyền](</vi/gateway/sandbox-vs-tool-policy-vs-elevated>) — gỡ lỗi "tại sao điều này bị chặn?"
  * [Cơ chế hộp cát](</vi/gateway/sandboxing>) — tài liệu tham chiếu đầy đủ về hộp cát (chế độ, phạm vi, phần phụ trợ, ảnh)
  * [Quản lý phiên](</vi/concepts/session>)


Was this useful?YesNo