---
title: بيئة معزولة وأدوات متعددة الوكلاء
source_url: https://docs.openclaw.ai/ar/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

Each agent in a multi-agent setup can override the global sandbox and tool policy. This page covers per-agent configuration, precedence rules, and examples.

[**Sandboxing** Backends and modes — full sandbox reference. ](</ar/gateway/sandboxing>) [**Sandbox vs tool policy vs elevated** Debug "why is this blocked?" ](</ar/gateway/sandbox-vs-tool-policy-vs-elevated>) [**Elevated mode** Elevated exec for trusted senders. ](</ar/tools/elevated>)

* * *

## Configuration examples

Example 1: Personal + restricted family agent jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**Result:**

  * `main` agent: runs on host, full tool access.
  * `family` agent: runs in Docker (one container per agent), only `read` and current-conversation message sends.

Example 2: Work agent with shared sandbox jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

Example 2b: Global coding profile + messaging-only agent jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**Result:**

  * default agents get coding tools.
  * `support` agent is messaging-only (+ Slack tool).

Example 3: Different sandbox modes per agent jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## Configuration precedence

When both global (`agents.defaults.*`) and agent-specific (`agents.list[].*`) configs exist:

### Sandbox config

Agent-specific settings override global:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### Tool restrictions

The filtering order is:

* ### Tool profile

`tools.profile` or `agents.list[].tools.profile`.

* ### Provider tool profile

`tools.byProvider[provider].profile` or `agents.list[].tools.byProvider[provider].profile`.

* ### Global tool policy

`tools.allow` / `tools.deny`.

* ### Provider tool policy

`tools.byProvider[provider].allow/deny`.

* ### Agent-specific tool policy

`agents.list[].tools.allow/deny`.

* ### Agent provider policy

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### Sandbox tool policy

`tools.sandbox.tools` or `agents.list[].tools.sandbox.tools`.

* ### Subagent tool policy

`tools.subagents.tools`, if applicable.

Precedence rules

  * Each level can further restrict tools, but cannot grant back denied tools from earlier levels.
  * If `agents.list[].tools.sandbox.tools` is set, it replaces `tools.sandbox.tools` for that agent.
  * If `agents.list[].tools.profile` is set, it overrides `tools.profile` for that agent.
  * Provider tool keys accept either `provider` (e.g. `google-antigravity`) or `provider/model` (e.g. `openai/gpt-5.4`).

Empty allowlist behavior

If any explicit allowlist in that chain leaves the run with no callable tools, OpenClaw stops before submitting the prompt to the model. This is intentional: an agent configured with a missing tool such as `agents.list[].tools.allow: ["query_db"]` should fail loudly until the plugin that registers `query_db` is enabled, not continue as a text-only agent.

Tool policies support `group:*` shorthands that expand to multiple tools. See [Tool groups](</ar/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>) for the full list.

Per-agent elevated overrides (`agents.list[].tools.elevated`) can further restrict elevated exec for specific agents. See [Elevated mode](</ar/tools/elevated>) for details.

* * *

## الترحيل من وكيل واحد

### قبل (وكيل واحد)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### بعد (وكلاء متعددون)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## أمثلة تقييد الأدوات

### وكيل للقراءة فقط

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### تنفيذ Shell مع تعطيل أدوات نظام الملفات

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### الاتصال فقط

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

لا يزال `sessions_history` في هذا الملف الشخصي يعيد عرض استدعاء محدودًا ومنقحًا بدلًا من تفريغ نصي خام. يزيل استدعاء المساعد وسوم التفكير، وبنية `<relevant-memories>`، وحمولات XML لاستدعاءات الأدوات بنص عادي (بما في ذلك `<tool_call>...</tool_call>` و`<function_call>...</function_call>` و`<tool_calls>...</tool_calls>` و`<function_calls>...</function_calls>` وكتل استدعاء الأدوات المقتطعة)، وبنية استدعاءات الأدوات المخفّضة، ورموز تحكم النموذج المسرّبة بنمط ASCII/العرض الكامل، وXML استدعاءات أدوات MiniMax غير الصالح قبل التنقيح/الاقتطاع.

* * *

## خطأ شائع: "non-main"

* * *

## الاختبار

بعد تكوين صندوق العزل والأدوات للوكلاء المتعددين:

* ### تحقق من حلّ الوكيل

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### تحقق من حاويات صندوق العزل

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### اختبر قيود الأدوات

  * أرسل رسالة تتطلب أدوات مقيدة.
  * تحقق من أن الوكيل لا يستطيع استخدام الأدوات الممنوعة.


* ### راقب السجلات

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## استكشاف الأخطاء وإصلاحها

الوكيل غير موضوع في صندوق العزل رغم `mode: 'all'`

  * تحقق مما إذا كان هناك `agents.defaults.sandbox.mode` عام يتجاوزه.
  * تكون للإعدادات الخاصة بالوكيل الأولوية، لذلك اضبط `agents.list[].sandbox.mode: "all"`.

الأدوات لا تزال متاحة رغم قائمة المنع

  * تحقق من ترتيب تصفية الأدوات: عام → وكيل → صندوق عزل → وكيل فرعي.
  * يمكن لكل مستوى أن يزيد التقييد فقط، ولا يمكنه إعادة المنح.
  * تحقق من ذلك عبر السجلات: `[tools] filtering tools for agent:${agentId}`.

الحاوية غير معزولة لكل وكيل

  * اضبط `scope: "agent"` في تكوين صندوق العزل الخاص بالوكيل.
  * الافتراضي هو `"session"`، وهو ما ينشئ حاوية واحدة لكل جلسة.


* * *

## ذات صلة

  * [وضع الامتيازات المرتفعة](</ar/tools/elevated>)
  * [التوجيه متعدد الوكلاء](</ar/concepts/multi-agent>)
  * [تكوين بيئة العزل](</ar/gateway/config-agents#agentsdefaultssandbox>)
  * [بيئة العزل مقابل سياسة الأدوات مقابل الامتيازات المرتفعة](</ar/gateway/sandbox-vs-tool-policy-vs-elevated>) — تصحيح أخطاء "لماذا تم حظر هذا؟"
  * [العزل](</ar/gateway/sandboxing>) — مرجع بيئة العزل الكامل (الأوضاع، النطاقات، الخلفيات، الصور)
  * [إدارة الجلسات](</ar/concepts/session>)


Was this useful?YesNo