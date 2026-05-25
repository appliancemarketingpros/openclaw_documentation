---
title: إعداد Gateway عن بُعد
source_url: https://docs.openclaw.ai/ar/gateway/remote-gateway-readme
scraped_at: 2026-05-25
---

> دُمج هذا المحتوى في [الوصول عن بُعد](</ar/gateway/remote#macos-persistent-ssh-tunnel-via-launchagent>). راجع تلك الصفحة للاطلاع على الدليل الحالي.

# تشغيل OpenClaw.app باستخدام Gateway بعيد

يستخدم OpenClaw.app نفق SSH للاتصال بـ Gateway بعيد. يوضح لك هذا الدليل كيفية إعداده.

## نظرة عامة
[code] 
    flowchart TB
        subgraph Client["Client Machine"]
            direction TB
            A["OpenClaw.app"]
            B["ws://127.0.0.1:18789\n(local port)"]
            T["SSH Tunnel"]
    
            A --> B
            B --> T
        end
        subgraph Remote["Remote Machine"]
            direction TB
            C["Gateway WebSocket"]
            D["ws://127.0.0.1:18789"]
    
            C --> D
        end
        T --> C
[/code]

## الإعداد السريع

### الخطوة 1: إضافة إعداد SSH

حرّر `~/.ssh/config` وأضف:

sshCopy code
[code]
    Host remote-gateway    HostName &lt;REMOTE_IP&gt;          # e.g., 172.27.187.184    User &lt;REMOTE_USER&gt;            # e.g., jefferson    LocalForward 18789 127.0.0.1:18789    IdentityFile ~/.ssh/id_rsa
[/code]

استبدل `&lt;REMOTE_IP&gt;` و`&lt;REMOTE_USER&gt;` بالقيم الخاصة بك.

### الخطوة 2: نسخ مفتاح SSH

انسخ مفتاحك العام إلى الجهاز البعيد (أدخل كلمة المرور مرة واحدة):

bashCopy code
[code]
    ssh-copy-id -i ~/.ssh/id_rsa &lt;REMOTE_USER&gt;@&lt;REMOTE_IP&gt;
[/code]

### الخطوة 3: إعداد مصادقة Gateway البعيد

bashCopy code
[code]
    openclaw config set gateway.remote.token "<your-token>"
[/code]

استخدم `gateway.remote.password` بدلاً من ذلك إذا كان Gateway البعيد لديك يستخدم مصادقة بكلمة مرور. لا يزال `OPENCLAW_GATEWAY_TOKEN` صالحاً كتجاوز على مستوى الصدفة، لكن إعداد العميل البعيد الدائم هو `gateway.remote.token` / `gateway.remote.password`.

### الخطوة 4: بدء نفق SSH

bashCopy code
[code]
    ssh -N remote-gateway &
[/code]

### الخطوة 5: إعادة تشغيل OpenClaw.app

bashCopy code
[code]
    # Quit OpenClaw.app (⌘Q), then reopen:open /path/to/OpenClaw.app
[/code]

سيتصل التطبيق الآن بـ Gateway البعيد عبر نفق SSH.

* * *

## بدء النفق تلقائياً عند تسجيل الدخول

لجعل نفق SSH يبدأ تلقائياً عند تسجيل الدخول، أنشئ Launch Agent.

### إنشاء ملف PLIST

احفظ هذا باسم `~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist`:

xmlCopy code
[code]
    <?xml version="1.0" encoding="UTF-8"?><!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd"><plist version="1.0"><dict>    <key>Label</key>    <string>ai.openclaw.ssh-tunnel</string>    <key>ProgramArguments</key>    <array>        <string>/usr/bin/ssh</string>        <string>-N</string>        <string>remote-gateway</string>    </array>    <key>KeepAlive</key>    <true/>    <key>RunAtLoad</key>    <true/></dict></plist>
[/code]

### تحميل Launch Agent

bashCopy code
[code]
    launchctl bootstrap gui/$UID ~/Library/LaunchAgents/ai.openclaw.ssh-tunnel.plist
[/code]

سيقوم النفق الآن بما يلي:

  * البدء تلقائياً عند تسجيل الدخول
  * إعادة التشغيل إذا تعطل
  * الاستمرار في العمل في الخلفية


ملاحظة قديمة: أزل أي LaunchAgent متبقٍ باسم `com.openclaw.ssh-tunnel` إن وُجد.

* * *

## استكشاف الأخطاء وإصلاحها

**تحقق مما إذا كان النفق قيد التشغيل:**

bashCopy code
[code]
    ps aux | grep "ssh -N remote-gateway" | grep -v greplsof -i :18789
[/code]

**إعادة تشغيل النفق:**

bashCopy code
[code]
    launchctl kickstart -k gui/$UID/ai.openclaw.ssh-tunnel
[/code]

**إيقاف النفق:**

bashCopy code
[code]
    launchctl bootout gui/$UID/ai.openclaw.ssh-tunnel
[/code]

* * *

## كيف يعمل

المكوّن | ما يفعله  
---|---  
`LocalForward 18789 127.0.0.1:18789` | يوجّه المنفذ المحلي 18789 إلى المنفذ البعيد 18789  
`ssh -N` | SSH من دون تنفيذ أوامر بعيدة (فقط توجيه المنافذ)  
`KeepAlive` | يعيد تشغيل النفق تلقائياً إذا تعطل  
`RunAtLoad` | يبدأ النفق عند تحميل الوكيل  
  
يتصل OpenClaw.app بـ `ws://127.0.0.1:18789` على جهاز العميل لديك. يوجّه نفق SSH ذلك الاتصال إلى المنفذ 18789 على الجهاز البعيد حيث يعمل Gateway.

## ذو صلة

  * [الوصول عن بُعد](</ar/gateway/remote>)
  * [Tailscale](</ar/gateway/tailscale>)


Was this useful?YesNo