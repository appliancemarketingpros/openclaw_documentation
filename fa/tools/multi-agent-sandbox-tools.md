---
title: محیط ایزوله و ابزارهای چندعاملی
source_url: https://docs.openclaw.ai/fa/tools/multi-agent-sandbox-tools
scraped_at: 2026-05-25
---

هر عامل در یک چیدمان چندعامله می‌تواند Sandbox و سیاست ابزار سراسری را بازنویسی کند. این صفحه پیکربندی به‌ازای هر عامل، قواعد تقدم، و نمونه‌ها را پوشش می‌دهد.

[**Sandboxing** بک‌اندها و حالت‌ها — مرجع کامل Sandbox. ](</fa/gateway/sandboxing>) [**Sandbox در برابر سیاست ابزار در برابر elevated** اشکال‌زدایی «چرا این مسدود شده است؟» ](</fa/gateway/sandbox-vs-tool-policy-vs-elevated>) [**حالت elevated** اجرای elevated برای فرستندگان مورد اعتماد. ](</fa/tools/elevated>)

* * *

## نمونه‌های پیکربندی

نمونه ۱: عامل شخصی + عامل خانوادگی محدود jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "name": "Personal Assistant",        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      },      {        "id": "family",        "name": "Family Bot",        "workspace": "~/.openclaw/workspace-family",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read", "message"],          "deny": ["exec", "write", "edit", "apply_patch", "process", "browser"],          "message": {            "crossContext": {              "allowWithinProvider": false,              "allowAcrossProviders": false            }          }        }      }    ]  },  "bindings": [    {      "agentId": "family",      "match": {        "provider": "whatsapp",        "accountId": "*",        "peer": {          "kind": "group",          "id": "120363424282127706@g.us"        }      }    }  ]}
[/code]

**نتیجه:**

  * عامل `main`: روی میزبان اجرا می‌شود و دسترسی کامل به ابزارها دارد.
  * عامل `family`: در Docker اجرا می‌شود (یک کانتینر برای هر عامل)، فقط `read` و ارسال پیام در گفت‌وگوی فعلی.

نمونه ۲: عامل کاری با Sandbox مشترک jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "personal",        "workspace": "~/.openclaw/workspace-personal",        "sandbox": { "mode": "off" }      },      {        "id": "work",        "workspace": "~/.openclaw/workspace-work",        "sandbox": {          "mode": "all",          "scope": "shared",          "workspaceRoot": "/tmp/work-sandboxes"        },        "tools": {          "allow": ["read", "write", "apply_patch", "exec"],          "deny": ["browser", "gateway", "discord"]        }      }    ]  }}
[/code]

نمونه ۲ب: پروفایل کدنویسی سراسری + عامل فقط پیام‌رسانی jsonCopy code
[code]
    {  "tools": { "profile": "coding" },  "agents": {    "list": [      {        "id": "support",        "tools": { "profile": "messaging", "allow": ["slack"] }      }    ]  }}
[/code]

**نتیجه:**

  * عامل‌های پیش‌فرض ابزارهای کدنویسی را دریافت می‌کنند.
  * عامل `support` فقط پیام‌رسانی است (+ ابزار Slack).

نمونه ۳: حالت‌های Sandbox متفاوت برای هر عامل jsonCopy code
[code]
    {  "agents": {    "defaults": {      "sandbox": {        "mode": "non-main",        "scope": "session"      }    },    "list": [      {        "id": "main",        "workspace": "~/.openclaw/workspace",        "sandbox": {          "mode": "off"        }      },      {        "id": "public",        "workspace": "~/.openclaw/workspace-public",        "sandbox": {          "mode": "all",          "scope": "agent"        },        "tools": {          "allow": ["read"],          "deny": ["exec", "write", "edit", "apply_patch"]        }      }    ]  }}
[/code]

* * *

## تقدم پیکربندی

وقتی هم پیکربندی سراسری (`agents.defaults.*`) و هم پیکربندی ویژه عامل (`agents.list[].*`) وجود داشته باشد:

### پیکربندی Sandbox

تنظیمات ویژه عامل، تنظیمات سراسری را بازنویسی می‌کنند:

CodeCopy code
[code]
    agents.list[].sandbox.mode > agents.defaults.sandbox.modeagents.list[].sandbox.scope > agents.defaults.sandbox.scopeagents.list[].sandbox.workspaceRoot > agents.defaults.sandbox.workspaceRootagents.list[].sandbox.workspaceAccess > agents.defaults.sandbox.workspaceAccessagents.list[].sandbox.docker.* > agents.defaults.sandbox.docker.*agents.list[].sandbox.browser.* > agents.defaults.sandbox.browser.*agents.list[].sandbox.prune.* > agents.defaults.sandbox.prune.*
[/code]

### محدودیت‌های ابزار

ترتیب فیلتر کردن این است:

* ### پروفایل ابزار

`tools.profile` یا `agents.list[].tools.profile`.

* ### پروفایل ابزار ارائه‌دهنده

`tools.byProvider[provider].profile` یا `agents.list[].tools.byProvider[provider].profile`.

* ### سیاست ابزار سراسری

`tools.allow` / `tools.deny`.

* ### سیاست ابزار ارائه‌دهنده

`tools.byProvider[provider].allow/deny`.

* ### سیاست ابزار ویژه عامل

`agents.list[].tools.allow/deny`.

* ### سیاست ارائه‌دهنده عامل

`agents.list[].tools.byProvider[provider].allow/deny`.

* ### سیاست ابزار Sandbox

`tools.sandbox.tools` یا `agents.list[].tools.sandbox.tools`.

* ### سیاست ابزار عامل فرعی

`tools.subagents.tools`، اگر قابل اعمال باشد.

قواعد تقدم

  * هر سطح می‌تواند ابزارها را بیشتر محدود کند، اما نمی‌تواند ابزارهایی را که در سطوح قبلی رد شده‌اند دوباره مجاز کند.
  * اگر `agents.list[].tools.sandbox.tools` تنظیم شده باشد، برای آن عامل جایگزین `tools.sandbox.tools` می‌شود.
  * اگر `agents.list[].tools.profile` تنظیم شده باشد، برای آن عامل `tools.profile` را بازنویسی می‌کند.
  * کلیدهای ابزار ارائه‌دهنده می‌توانند یا `provider` (مثلاً `google-antigravity`) یا `provider/model` (مثلاً `openai/gpt-5.4`) باشند.

رفتار فهرست مجاز خالی

اگر هر فهرست مجاز صریحی در آن زنجیره اجرا را بدون هیچ ابزار قابل‌فراخوانی باقی بگذارد، OpenClaw پیش از ارسال پرامپت به مدل متوقف می‌شود. این عمدی است: عاملی که با یک ابزار مفقود مانند `agents.list[].tools.allow: ["query_db"]` پیکربندی شده است باید تا زمانی که Plugin ثبت‌کننده `query_db` فعال شود با خطای آشکار متوقف شود، نه اینکه به‌عنوان عامل فقط متنی ادامه دهد.

سیاست‌های ابزار از میان‌برهای `group:*` پشتیبانی می‌کنند که به چند ابزار گسترش می‌یابند. برای فهرست کامل، [گروه‌های ابزار](</fa/gateway/sandbox-vs-tool-policy-vs-elevated#tool-groups-shorthands>) را ببینید.

بازنویسی‌های elevated به‌ازای هر عامل (`agents.list[].tools.elevated`) می‌توانند اجرای elevated را برای عامل‌های مشخص بیشتر محدود کنند. برای جزئیات، [حالت elevated](</fa/tools/elevated>) را ببینید.

* * *

## مهاجرت از عامل تک‌عاملی

### قبل (عامل تک‌عاملی)

jsonCopy code
[code]
    {  "agents": {    "defaults": {      "workspace": "~/.openclaw/workspace",      "sandbox": {        "mode": "non-main"      }    }  },  "tools": {    "sandbox": {      "tools": {        "allow": ["read", "write", "apply_patch", "exec"],        "deny": []      }    }  }}
[/code]

### بعد (چندعاملی)

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "main",        "default": true,        "workspace": "~/.openclaw/workspace",        "sandbox": { "mode": "off" }      }    ]  }}
[/code]

* * *

## نمونه‌های محدودسازی ابزار

### عامل فقط‌خواندنی

jsonCopy code
[code]
    {  "tools": {    "allow": ["read"],    "deny": ["exec", "write", "edit", "apply_patch", "process"]  }}
[/code]

### اجرای shell با ابزارهای فایل‌سیستم غیرفعال

jsonCopy code
[code]
    {  "tools": {    "allow": ["read", "exec", "process"],    "deny": ["write", "edit", "apply_patch", "browser", "gateway"]  }}
[/code]

### فقط ارتباطات

jsonCopy code
[code]
    {  "tools": {    "sessions": { "visibility": "tree" },    "allow": ["sessions_list", "sessions_send", "sessions_history", "session_status"],    "deny": ["exec", "write", "edit", "apply_patch", "read", "browser"]  }}
[/code]

`sessions_history` در این پروفایل همچنان به‌جای dump خام رونوشت، یک نمای یادآوری محدود و پاک‌سازی‌شده برمی‌گرداند. یادآوری دستیار برچسب‌های تفکر، داربست `<relevant-memories>`، payloadهای XML فراخوانی ابزار به‌صورت متن ساده (از جمله `<tool_call>...</tool_call>`، `<function_call>...</function_call>`، `<tool_calls>...</tool_calls>`، `<function_calls>...</function_calls>` و بلوک‌های کوتاه‌شده فراخوانی ابزار)، داربست فراخوانی ابزار تنزل‌یافته، توکن‌های کنترلی مدل نشت‌کرده ASCII/تمام‌عرض، و XML بدشکل فراخوانی ابزار MiniMax را پیش از پوشاندن/کوتاه‌سازی حذف می‌کند.

* * *

## خطای رایج: "non-main"

* * *

## آزمایش

پس از پیکربندی sandbox و ابزارهای چندعاملی:

* ### بررسی تفکیک عامل

bashCopy code
[code]
    openclaw agents list --bindings
[/code]

* ### تأیید کانتینرهای sandbox

bashCopy code
[code]
    docker ps --filter "name=openclaw-sbx-"
[/code]

* ### آزمایش محدودیت‌های ابزار

  * پیامی ارسال کنید که به ابزارهای محدودشده نیاز داشته باشد.
  * تأیید کنید که عامل نمی‌تواند از ابزارهای ردشده استفاده کند.


* ### پایش گزارش‌ها

bashCopy code
[code]
    tail -f "${OPENCLAW_STATE_DIR:-$HOME/.openclaw}/logs/gateway.log" | grep -E "routing|sandbox|tools"
[/code]

* * *

## عیب‌یابی

عامل با وجود `mode: 'all'` در sandbox نیست

  * بررسی کنید آیا یک `agents.defaults.sandbox.mode` سراسری وجود دارد که آن را override می‌کند.
  * پیکربندی اختصاصی عامل اولویت دارد، بنابراین `agents.list[].sandbox.mode: "all"` را تنظیم کنید.

ابزارها با وجود فهرست deny همچنان در دسترس هستند

  * ترتیب فیلترکردن ابزارها را بررسی کنید: سراسری → عامل → sandbox → زیرعامل.
  * هر سطح فقط می‌تواند بیشتر محدود کند، نه اینکه دوباره مجوز بدهد.
  * با گزارش‌ها تأیید کنید: `[tools] filtering tools for agent:${agentId}`.

کانتینر برای هر عامل ایزوله نیست

  * در پیکربندی sandbox اختصاصی عامل، `scope: "agent"` را تنظیم کنید.
  * پیش‌فرض `"session"` است که برای هر نشست یک کانتینر ایجاد می‌کند.


* * *

## مرتبط

  * [حالت ارتقایافته](</fa/tools/elevated>)
  * [مسیریابی چندعاملی](</fa/concepts/multi-agent>)
  * [پیکربندی سندباکس](</fa/gateway/config-agents#agentsdefaultssandbox>)
  * [سندباکس در برابر سیاست ابزار در برابر ارتقایافته](</fa/gateway/sandbox-vs-tool-policy-vs-elevated>) — اشکال‌زدایی «چرا این مسدود شده است؟»
  * [سندباکسینگ](</fa/gateway/sandboxing>) — مرجع کامل سندباکس (حالت‌ها، دامنه‌ها، بک‌اندها، ایمیج‌ها)
  * [مدیریت نشست](</fa/concepts/session>)


Was this useful?YesNo