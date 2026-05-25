---
title: گروه‌های پخش
source_url: https://docs.openclaw.ai/fa/channels/broadcast-groups
scraped_at: 2026-05-25
---

## نمای کلی

گروه‌های پخش به چند عامل امکان می‌دهند یک پیام واحد را هم‌زمان پردازش کنند و به آن پاسخ دهند. این قابلیت به شما اجازه می‌دهد تیم‌هایی از عامل‌های تخصصی بسازید که در یک گروه WhatsApp یا پیام مستقیم واحد با هم کار می‌کنند — همه با استفاده از یک شماره تلفن.

دامنه فعلی: **فقط WhatsApp** (کانال وب).

گروه‌های پخش پس از فهرست‌های مجاز کانال و قواعد فعال‌سازی گروه ارزیابی می‌شوند. در گروه‌های WhatsApp، این یعنی پخش‌ها زمانی انجام می‌شوند که OpenClaw در حالت عادی پاسخ می‌داد (برای مثال: هنگام اشاره، بسته به تنظیمات گروه شما).

## موارد استفاده

1\. Specialized agent teams

چند عامل را با مسئولیت‌های اتمیک و متمرکز مستقر کنید:

CodeCopy code
[code]
    Group: "Development Team"Agents:  - CodeReviewer (reviews code snippets)  - DocumentationBot (generates docs)  - SecurityAuditor (checks for vulnerabilities)  - TestGenerator (suggests test cases)
[/code]

هر عامل همان پیام را پردازش می‌کند و دیدگاه تخصصی خود را ارائه می‌دهد.

2\. Multi-language support CodeCopy code
[code]
    Group: "International Support"Agents:  - Agent_EN (responds in English)  - Agent_DE (responds in German)  - Agent_ES (responds in Spanish)
[/code]

3\. Quality assurance workflows CodeCopy code
[code]
    Group: "Customer Support"Agents:  - SupportAgent (provides answer)  - QAAgent (reviews quality, only responds if issues found)
[/code]

4\. Task automation CodeCopy code
[code]
    Group: "Project Management"Agents:  - TaskTracker (updates task database)  - TimeLogger (logs time spent)  - ReportGenerator (creates summaries)
[/code]

## پیکربندی

### راه‌اندازی پایه

یک بخش سطح‌بالای `broadcast` اضافه کنید (کنار `bindings`). کلیدها شناسه‌های همتای WhatsApp هستند:

  * گپ‌های گروهی: JID گروه (مثلاً `120363403215116621@g.us`)
  * پیام‌های مستقیم: شماره تلفن E.164 (مثلاً `+15551234567`)

jsonCopy code
[code]
    {  "broadcast": {    "120363403215116621@g.us": ["alfred", "baerbel", "assistant3"]  }}
[/code]

**نتیجه:** وقتی OpenClaw در این گپ پاسخ می‌داد، هر سه عامل را اجرا می‌کند.

### راهبرد پردازش

نحوه پردازش پیام‌ها توسط عامل‌ها را کنترل کنید:

### parallel (default)

همه عامل‌ها هم‌زمان پردازش می‌کنند:

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### sequential

عامل‌ها به‌ترتیب پردازش می‌کنند (هرکدام منتظر پایان عامل قبلی می‌ماند):

jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "120363403215116621@g.us": ["alfred", "baerbel"]  }}
[/code]

### مثال کامل

jsonCopy code
[code]
    {  "agents": {    "list": [      {        "id": "code-reviewer",        "name": "Code Reviewer",        "workspace": "/path/to/code-reviewer",        "sandbox": { "mode": "all" }      },      {        "id": "security-auditor",        "name": "Security Auditor",        "workspace": "/path/to/security-auditor",        "sandbox": { "mode": "all" }      },      {        "id": "docs-generator",        "name": "Documentation Generator",        "workspace": "/path/to/docs-generator",        "sandbox": { "mode": "all" }      }    ]  },  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": ["code-reviewer", "security-auditor", "docs-generator"],    "120363424282127706@g.us": ["support-en", "support-de"],    "+15555550123": ["assistant", "logger"]  }}
[/code]

## نحوه کارکرد

### جریان پیام

* ### Incoming message arrives

یک پیام گروهی یا پیام مستقیم WhatsApp می‌رسد.

* ### Broadcast check

سیستم بررسی می‌کند که آیا شناسه همتا در `broadcast` وجود دارد یا نه.

* ### If in broadcast list

  * همه عامل‌های فهرست‌شده پیام را پردازش می‌کنند.
  * هر عامل کلید جلسه و زمینه جداگانه خودش را دارد.
  * عامل‌ها به‌صورت موازی (پیش‌فرض) یا ترتیبی پردازش می‌کنند.


* ### If not in broadcast list

مسیریابی عادی اعمال می‌شود (اولین binding منطبق).

### جداسازی جلسه

هر عامل در یک گروه پخش موارد زیر را کاملاً جداگانه نگه می‌دارد:

  * **کلیدهای جلسه** (`agent:alfred:whatsapp:group:120363...` در برابر `agent:baerbel:whatsapp:group:120363...`)
  * **تاریخچه گفتگو** (عامل پیام‌های عامل‌های دیگر را نمی‌بیند)
  * **فضای کاری** (sandboxهای جداگانه در صورت پیکربندی)
  * **دسترسی ابزار** (فهرست‌های مجاز/ممنوع متفاوت)
  * **حافظه/زمینه** (`IDENTITY.md`، `SOUL.md` و غیره جداگانه)
  * **بافر زمینه گروه** (پیام‌های اخیر گروه که برای زمینه استفاده می‌شوند) برای هر همتا مشترک است، بنابراین همه عامل‌های پخش هنگام فعال‌شدن همان زمینه را می‌بینند


این به هر عامل امکان می‌دهد موارد زیر را داشته باشد:

  * شخصیت‌های متفاوت
  * دسترسی ابزار متفاوت (مثلاً فقط‌خواندنی در برابر خواندنی-نوشتنی)
  * مدل‌های متفاوت (مثلاً opus در برابر sonnet)
  * Skills نصب‌شده متفاوت


### مثال: جلسه‌های جداشده

در گروه `120363403215116621@g.us` با عامل‌های `["alfred", "baerbel"]`:

### Alfred's context

CodeCopy code
[code]
    Session: agent:alfred:whatsapp:group:120363403215116621@g.usHistory: [user message, alfred's previous responses]Workspace: /Users/user/openclaw-alfred/Tools: read, write, exec
[/code]

### Bärbel's context

CodeCopy code
[code]
    Session: agent:baerbel:whatsapp:group:120363403215116621@g.usHistory: [user message, baerbel's previous responses]Workspace: /Users/user/openclaw-baerbel/Tools: read only
[/code]

## بهترین شیوه‌ها

1\. Keep agents focused

هر عامل را با یک مسئولیت واحد و روشن طراحی کنید:

jsonCopy code
[code]
    {  "broadcast": {    "DEV_GROUP": ["formatter", "linter", "tester"]  }}
[/code]

✅ **خوب:** هر عامل یک کار دارد. ❌ **بد:** یک عامل عمومی "dev-helper".

2\. Use descriptive names

روشن کنید هر عامل چه کاری انجام می‌دهد:

jsonCopy code
[code]
    {  "agents": {    "security-scanner": { "name": "Security Scanner" },    "code-formatter": { "name": "Code Formatter" },    "test-generator": { "name": "Test Generator" }  }}
[/code]

3\. Configure different tool access

فقط ابزارهایی را که عامل‌ها نیاز دارند به آن‌ها بدهید:

jsonCopy code
[code]
    {  "agents": {    "reviewer": {      "tools": { "allow": ["read", "exec"] }    },    "fixer": {      "tools": { "allow": ["read", "write", "edit", "exec"] }    }  }}
[/code]

`reviewer` فقط‌خواندنی است. `fixer` می‌تواند بخواند و بنویسد.

4\. Monitor performance

با تعداد زیادی عامل، موارد زیر را در نظر بگیرید:

  * استفاده از `"strategy": "parallel"` (پیش‌فرض) برای سرعت
  * محدودکردن گروه‌های پخش به ۵ تا ۱۰ عامل
  * استفاده از مدل‌های سریع‌تر برای عامل‌های ساده‌تر

5\. Handle failures gracefully

عامل‌ها مستقل از هم شکست می‌خورند. خطای یک عامل، دیگران را مسدود نمی‌کند:

CodeCopy code
[code]
    Message → [Agent A ✓, Agent B ✗ error, Agent C ✓]Result: Agent A and C respond, Agent B logs error
[/code]

## سازگاری

### ارائه‌دهنده‌ها

گروه‌های پخش در حال حاضر با موارد زیر کار می‌کنند:

  * ✅ WhatsApp (پیاده‌سازی‌شده)
  * 🚧 Telegram (برنامه‌ریزی‌شده)
  * 🚧 Discord (برنامه‌ریزی‌شده)
  * 🚧 Slack (برنامه‌ریزی‌شده)


### مسیریابی

گروه‌های پخش در کنار مسیریابی موجود کار می‌کنند:

jsonCopy code
[code]
    {  "bindings": [    {      "match": { "channel": "whatsapp", "peer": { "kind": "group", "id": "GROUP_A" } },      "agentId": "alfred"    }  ],  "broadcast": {    "GROUP_B": ["agent1", "agent2"]  }}
[/code]

  * `GROUP_A`: فقط alfred پاسخ می‌دهد (مسیریابی عادی).
  * `GROUP_B`: agent1 و agent2 پاسخ می‌دهند (پخش).


## عیب‌یابی

Agents not responding

**بررسی کنید:**

  1. شناسه‌های عامل در `agents.list` وجود داشته باشند.
  2. قالب شناسه همتا درست باشد (مثلاً `120363403215116621@g.us`).
  3. عامل‌ها در فهرست‌های ممنوع نباشند.


**اشکال‌زدایی:**

bashCopy code
[code]
    tail -f ~/.openclaw/logs/gateway.log | grep broadcast
[/code]

Only one agent responding

**علت:** شناسه همتا ممکن است در `bindings` باشد اما در `broadcast` نباشد.

**رفع:** آن را به پیکربندی پخش اضافه کنید یا از bindings حذف کنید.

Performance issues

اگر با تعداد زیادی عامل کند است:

  * تعداد عامل‌ها در هر گروه را کاهش دهید.
  * از مدل‌های سبک‌تر استفاده کنید (sonnet به‌جای opus).
  * زمان راه‌اندازی sandbox را بررسی کنید.


## مثال‌ها

Example 1: Code review team jsonCopy code
[code]
    {  "broadcast": {    "strategy": "parallel",    "120363403215116621@g.us": [      "code-formatter",      "security-scanner",      "test-coverage",      "docs-checker"    ]  },  "agents": {    "list": [      {        "id": "code-formatter",        "workspace": "~/agents/formatter",        "tools": { "allow": ["read", "write"] }      },      {        "id": "security-scanner",        "workspace": "~/agents/security",        "tools": { "allow": ["read", "exec"] }      },      {        "id": "test-coverage",        "workspace": "~/agents/testing",        "tools": { "allow": ["read", "exec"] }      },      { "id": "docs-checker", "workspace": "~/agents/docs", "tools": { "allow": ["read"] } }    ]  }}
[/code]

**کاربر ارسال می‌کند:** قطعه کد.

**پاسخ‌ها:**

  * code-formatter: "تورفتگی را اصلاح کردم و اشاره‌های نوع را اضافه کردم"
  * security-scanner: "⚠️ آسیب‌پذیری تزریق SQL در خط 12"
  * test-coverage: "پوشش 45٪ است، آزمون‌ها برای حالت‌های خطا وجود ندارند"
  * docs-checker: "docstring برای تابع `process_data` وجود ندارد"

Example 2: Multi-language support jsonCopy code
[code]
    {  "broadcast": {    "strategy": "sequential",    "+15555550123": ["detect-language", "translator-en", "translator-de"]  },  "agents": {    "list": [      { "id": "detect-language", "workspace": "~/agents/lang-detect" },      { "id": "translator-en", "workspace": "~/agents/translate-en" },      { "id": "translator-de", "workspace": "~/agents/translate-de" }    ]  }}
[/code]

## مرجع API

### طرح‌واره پیکربندی

typescriptCopy code
[code]
    interface OpenClawConfig {  broadcast?: {    strategy?: "parallel" | "sequential";    [peerId: string]: string[];  };}
[/code]

### فیلدها

نحوه پردازش عامل‌ها. `parallel` همه عامل‌ها را هم‌زمان اجرا می‌کند؛ `sequential` آن‌ها را به‌ترتیب آرایه اجرا می‌کند.

JID گروه WhatsApp، شماره E.164، یا شناسه همتای دیگر. مقدار، آرایه‌ای از شناسه‌های عامل‌هایی است که باید پیام‌ها را پردازش کنند.

## محدودیت‌ها

  1. **حداکثر عامل‌ها:** حد سختی وجود ندارد، اما بیش از ۱۰ عامل ممکن است کند باشد.
  2. **زمینه مشترک:** عامل‌ها پاسخ‌های یکدیگر را نمی‌بینند (طبق طراحی).
  3. **ترتیب پیام‌ها:** پاسخ‌های موازی ممکن است با هر ترتیبی برسند.
  4. **محدودیت‌های نرخ:** همه عامل‌ها در محدودیت‌های نرخ WhatsApp حساب می‌شوند.


## بهبودهای آینده

ویژگی‌های برنامه‌ریزی‌شده:

  * [ ] حالت زمینه مشترک (عامل‌ها پاسخ‌های یکدیگر را می‌بینند)
  * [ ] هماهنگی عامل‌ها (عامل‌ها می‌توانند به یکدیگر سیگنال دهند)
  * [ ] انتخاب پویای عامل (انتخاب عامل‌ها بر اساس محتوای پیام)
  * [ ] اولویت‌های عامل (برخی عامل‌ها پیش از دیگران پاسخ می‌دهند)


## مرتبط

  * [مسیریابی کانال](</fa/channels/channel-routing>)
  * [گروه‌ها](</fa/channels/groups>)
  * [ابزارهای محیط ایزوله چندعاملی](</fa/tools/multi-agent-sandbox-tools>)
  * [جفت‌سازی](</fa/channels/pairing>)
  * [مدیریت نشست](</fa/concepts/session>)


Was this useful?YesNo