---
title: Fly.io
source_url: https://docs.openclaw.ai/ar/install/fly
scraped_at: 2026-05-25
---

**الهدف:** تشغيل OpenClaw Gateway على جهاز [Fly.io](<https://fly.io>) مع تخزين دائم وHTTPS تلقائي وإمكانية وصول Discord/القنوات.

## ما تحتاج إليه

  * تثبيت [flyctl CLI](<https://fly.io/docs/hands-on/install-flyctl/>)
  * حساب [Fly.io](<http://Fly.io>) (تعمل الطبقة المجانية)
  * مصادقة النموذج: مفتاح API لمزوّد النموذج الذي تختاره
  * بيانات اعتماد القناة: رمز بوت Discord، رمز Telegram، وما إلى ذلك.


## المسار السريع للمبتدئين

  1. استنسخ المستودع ← خصّص `fly.toml`
  2. أنشئ التطبيق + وحدة التخزين ← عيّن الأسرار
  3. انشر باستخدام `fly deploy`
  4. ادخل عبر SSH لإنشاء الإعدادات أو استخدم واجهة التحكم


* ### إنشاء تطبيق Fly

bashCopy code
[code]
    # Clone the repogit clone https://github.com/openclaw/openclaw.gitcd openclaw # Create a new Fly app (pick your own name)fly apps create my-openclaw # Create a persistent volume (1GB is usually enough)fly volumes create openclaw_data --size 1 --region iad
[/code]

**نصيحة:** اختر منطقة قريبة منك. خيارات شائعة: `lhr` (لندن)، `iad` (فرجينيا)، `sjc` (سان خوسيه).

* ### تهيئة fly.toml

عدّل `fly.toml` ليتوافق مع اسم تطبيقك ومتطلباتك.

**ملاحظة أمنية:** تعرض الإعدادات الافتراضية عنوان URL عامًا. لنشر محصّن بلا IP عام، راجع النشر الخاص أو استخدم `deploy/fly.private.toml`.

tomlCopy code
[code]
    app = "my-openclaw"  # Your app nameprimary_region = "iad" [build]  dockerfile = "Dockerfile" [env]  NODE_ENV = "production"  OPENCLAW_PREFER_PNPM = "1"  OPENCLAW_STATE_DIR = "/data"  NODE_OPTIONS = "--max-old-space-size=1536" [processes]  app = "node dist/index.js gateway --allow-unconfigured --port 3000 --bind lan" [http_service]  internal_port = 3000  force_https = true  auto_stop_machines = false  auto_start_machines = true  min_machines_running = 1  processes = ["app"] [[vm]]  size = "shared-cpu-2x"  memory = "2048mb" [mounts]  source = "openclaw_data"  destination = "/data"
[/code]

تستخدم صورة Docker الخاصة بـ OpenClaw `tini` كنقطة دخول. تستبدل أوامر عمليات Fly قيمة Docker `CMD` من دون استبدال `ENTRYPOINT`، لذلك تظل العملية تعمل تحت `tini`.

**الإعدادات الأساسية:**

الإعداد | السبب  
---|---  
`--bind lan` | يربط بـ `0.0.0.0` حتى يتمكن وكيل Fly من الوصول إلى Gateway  
`--allow-unconfigured` | يبدأ من دون ملف إعدادات (ستنشيئه لاحقًا)  
`internal_port = 3000` | يجب أن يطابق `--port 3000` (أو `OPENCLAW_GATEWAY_PORT`) لفحوصات صحة Fly  
`memory = "2048mb"` | 512MB صغيرة جدًا؛ يُوصى بـ 2GB  
`OPENCLAW_STATE_DIR = "/data"` | يحافظ على الحالة في وحدة التخزين  
* ### تعيين الأسرار

bashCopy code
[code]
    # Required: Gateway token (for non-loopback binding)fly secrets set OPENCLAW_GATEWAY_TOKEN=$(openssl rand -hex 32) # Model provider API keysfly secrets set ANTHROPIC_API_KEY=sk-ant-... # Optional: Other providersfly secrets set OPENAI_API_KEY=sk-...fly secrets set GOOGLE_API_KEY=... # Channel tokensfly secrets set DISCORD_BOT_TOKEN=MTQ...
[/code]

**ملاحظات:**

  * تتطلب عمليات الربط غير الاسترجاعية (`--bind lan`) مسار مصادقة صالحًا لـ Gateway. يستخدم مثال [Fly.io](<http://Fly.io>) هذا `OPENCLAW_GATEWAY_TOKEN`، لكن `gateway.auth.password` أو نشر `trusted-proxy` غير استرجاعي مهيأ بشكل صحيح يفيان بالمتطلب أيضًا.
  * تعامل مع هذه الرموز مثل كلمات المرور.
  * **فضّل متغيرات البيئة على ملف الإعدادات** لكل مفاتيح API والرموز. هذا يُبقي الأسرار خارج `openclaw.json` حيث قد تُكشف أو تُسجّل عن طريق الخطأ.


* ### النشر

bashCopy code
[code]
    fly deploy
[/code]

ينشئ النشر الأول صورة Docker (نحو 2-3 دقائق). عمليات النشر اللاحقة أسرع.

بعد النشر، تحقّق:

bashCopy code
[code]
    fly statusfly logs
[/code]

يجب أن ترى:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:3000 (PID xxx)[discord] logged in to discord as xxx
[/code]

* ### إنشاء ملف الإعدادات

ادخل إلى الجهاز عبر SSH لإنشاء إعدادات مناسبة:

bashCopy code
[code]
    fly ssh console
[/code]

أنشئ دليل الإعدادات والملف:

bashCopy code
[code]
    mkdir -p /datacat > /data/openclaw.json << 'EOF'{  "agents": {    "defaults": {      "model": {        "primary": "anthropic/claude-opus-4-6",        "fallbacks": ["anthropic/claude-sonnet-4-6", "openai/gpt-5.4"]      },      "maxConcurrent": 4    },    "list": [      {        "id": "main",        "default": true      }    ]  },  "auth": {    "profiles": {      "anthropic:default": { "mode": "token", "provider": "anthropic" },      "openai:default": { "mode": "token", "provider": "openai" }    }  },  "bindings": [    {      "agentId": "main",      "match": { "channel": "discord" }    }  ],  "channels": {    "discord": {      "enabled": true,      "groupPolicy": "allowlist",      "guilds": {        "YOUR_GUILD_ID": {          "channels": { "general": { "allow": true } },          "requireMention": false        }      }    }  },  "gateway": {    "mode": "local",    "bind": "auto",    "controlUi": {      "allowedOrigins": [        "https://my-openclaw.fly.dev",        "http://localhost:3000",        "http://127.0.0.1:3000"      ]    }  },  "meta": {}}EOF
[/code]

**ملاحظة:** مع `OPENCLAW_STATE_DIR=/data`، يكون مسار الإعدادات هو `/data/openclaw.json`.

**ملاحظة:** استبدل `https://my-openclaw.fly.dev` بمنشأ تطبيق Fly الحقيقي لديك. يزرع بدء تشغيل Gateway مناشئ واجهة التحكم المحلية من قيم وقت التشغيل `--bind` و`--port` حتى يمكن للإقلاع الأول أن يستمر قبل وجود الإعدادات، لكن الوصول عبر المتصفح من خلال Fly لا يزال يحتاج إلى إدراج منشأ HTTPS الدقيق في `gateway.controlUi.allowedOrigins`.

**ملاحظة:** يمكن أن يأتي رمز Discord من أي مما يلي:

  * متغير البيئة: `DISCORD_BOT_TOKEN` (موصى به للأسرار)
  * ملف الإعدادات: `channels.discord.token`


إذا كنت تستخدم متغير البيئة، فلا حاجة إلى إضافة الرمز إلى الإعدادات. يقرأ Gateway `DISCORD_BOT_TOKEN` تلقائيًا.

أعد التشغيل للتطبيق:

bashCopy code
[code]
    exitfly machine restart <machine-id>
[/code]

* ### الوصول إلى Gateway

### واجهة التحكم

افتح في المتصفح:

bashCopy code
[code]
    fly open
[/code]

أو زر `https://my-openclaw.fly.dev/`

صادِق باستخدام السر المشترك المهيأ. يستخدم هذا الدليل رمز Gateway من `OPENCLAW_GATEWAY_TOKEN`؛ إذا بدّلت إلى مصادقة كلمة المرور، فاستخدم تلك كلمة المرور بدلًا من ذلك.

### السجلات

bashCopy code
[code]
    fly logs              # Live logsfly logs --no-tail    # Recent logs
[/code]

### وحدة تحكم SSH

bashCopy code
[code]
    fly ssh console
[/code]

## استكشاف الأخطاء وإصلاحها

### "التطبيق لا يستمع على العنوان المتوقع"

يرتبط Gateway بـ `127.0.0.1` بدلًا من `0.0.0.0`.

**الإصلاح:** أضف `--bind lan` إلى أمر العملية في `fly.toml`.

### فشل فحوصات الصحة / رفض الاتصال

لا يستطيع Fly الوصول إلى Gateway على المنفذ المهيأ.

**الإصلاح:** تأكد من أن `internal_port` يطابق منفذ Gateway (عيّن `--port 3000` أو `OPENCLAW_GATEWAY_PORT=3000`).

### نفاد الذاكرة / مشكلات الذاكرة

تستمر الحاوية في إعادة التشغيل أو تُنهى. العلامات: `SIGABRT`، أو `v8::internal::Runtime_AllocateInYoungGeneration`، أو عمليات إعادة تشغيل صامتة.

**الإصلاح:** زد الذاكرة في `fly.toml`:

tomlCopy code
[code]
    [[vm]]  memory = "2048mb"
[/code]

أو حدّث جهازًا موجودًا:

bashCopy code
[code]
    fly machine update <machine-id> --vm-memory 2048 -y
[/code]

**ملاحظة:** 512MB صغيرة جدًا. قد تعمل 1GB لكنها قد تنفد من الذاكرة تحت الحمل أو مع التسجيل المفصل. **يُوصى بـ 2GB.**

### مشكلات قفل Gateway

يرفض Gateway البدء مع أخطاء "قيد التشغيل بالفعل".

يحدث هذا عندما تعاد تشغيل الحاوية لكن ملف قفل PID يبقى على وحدة التخزين.

**الإصلاح:** احذف ملف القفل:

bashCopy code
[code]
    fly ssh console --command "rm -f /data/gateway.*.lock"fly machine restart <machine-id>
[/code]

يوجد ملف القفل في `/data/gateway.*.lock` (وليس في دليل فرعي).

### عدم قراءة الإعدادات

يتجاوز `--allow-unconfigured` حارس بدء التشغيل فقط. لا ينشئ أو يصلح `/data/openclaw.json`، لذا تأكد من وجود إعداداتك الحقيقية وأنها تتضمن `gateway.mode="local"` عندما تريد بدء Gateway محلي عادي.

تحقّق من وجود الإعدادات:

bashCopy code
[code]
    fly ssh console --command "cat /data/openclaw.json"
[/code]

### كتابة الإعدادات عبر SSH

لا يدعم الأمر `fly ssh console -C` إعادة توجيه الصدفة. لكتابة ملف إعدادات:

bashCopy code
[code]
    # Use echo + tee (pipe from local to remote)echo '{"your":"config"}' | fly ssh console -C "tee /data/openclaw.json" # Or use sftpfly sftp shell> put /local/path/config.json /data/openclaw.json
[/code]

**ملاحظة:** قد يفشل `fly sftp` إذا كان الملف موجودًا بالفعل. احذفه أولًا:

bashCopy code
[code]
    fly ssh console --command "rm /data/openclaw.json"
[/code]

### عدم بقاء الحالة

إذا فقدت ملفات تعريف المصادقة، أو حالة القنوات/المزوّدين، أو الجلسات بعد إعادة التشغيل، فإن دليل الحالة يكتب إلى نظام ملفات الحاوية.

**الإصلاح:** تأكد من تعيين `OPENCLAW_STATE_DIR=/data` في `fly.toml` ثم أعد النشر.

## التحديثات

bashCopy code
[code]
    # Pull latest changesgit pull # Redeployfly deploy # Check healthfly statusfly logs
[/code]

### تحديث أمر الجهاز

إذا احتجت إلى تغيير أمر بدء التشغيل من دون إعادة نشر كاملة:

bashCopy code
[code]
    # Get machine IDfly machines list # Update commandfly machine update <machine-id> --command "node dist/index.js gateway --port 3000 --bind lan" -y # Or with memory increasefly machine update <machine-id> --vm-memory 2048 --command "node dist/index.js gateway --port 3000 --bind lan" -y
[/code]

**ملاحظة:** بعد `fly deploy`، قد يُعاد ضبط أمر الجهاز إلى ما هو موجود في `fly.toml`. إذا أجريت تغييرات يدوية، فأعد تطبيقها بعد النشر.

## النشر الخاص (محصّن)

افتراضيًا، يخصص Fly عناوين IP عامة، ما يجعل Gateway لديك متاحًا على `https://your-app.fly.dev`. هذا ملائم لكنه يعني أن نشرك قابل للاكتشاف بواسطة ماسحات الإنترنت (Shodan، Censys، وما إلى ذلك).

لنشر محصّن مع **عدم وجود تعرّض عام** ، استخدم القالب الخاص.

### متى تستخدم النشر الخاص

  * أنت تجري فقط مكالمات/رسائل **صادرة** (لا توجد Webhook واردة)
  * تستخدم أنفاق **ngrok أو Tailscale** لأي استدعاءات Webhook راجعة
  * تصل إلى Gateway عبر **SSH أو وكيل أو WireGuard** بدلًا من المتصفح
  * تريد أن يكون النشر **مخفيًا عن ماسحات الإنترنت**


### الإعداد

استخدم `deploy/fly.private.toml` بدلًا من الإعدادات القياسية:

bashCopy code
[code]
    # Deploy with private configfly deploy -c deploy/fly.private.toml
[/code]

أو حوّل نشرًا موجودًا:

bashCopy code
[code]
    # List current IPsfly ips list -a my-openclaw # Release public IPsfly ips release <public-ipv4> -a my-openclawfly ips release <public-ipv6> -a my-openclaw # Switch to private config so future deploys don't re-allocate public IPs# (remove [http_service] or deploy with the private template)fly deploy -c deploy/fly.private.toml # Allocate private-only IPv6fly ips allocate-v6 --private -a my-openclaw
[/code]

بعد ذلك، يجب أن يعرض `fly ips list` عنوان IP واحدًا فقط من النوع `private`:

CodeCopy code
[code]
    VERSION  IP                   TYPE             REGIONv6       fdaa:x:x:x:x::x      private          global
[/code]

### الوصول إلى نشر خاص

نظرًا لعدم وجود عنوان URL عام، استخدم إحدى هذه الطرق:

**الخيار 1: وكيل محلي (الأبسط)**

bashCopy code
[code]
    # Forward local port 3000 to the appfly proxy 3000:3000 -a my-openclaw # Then open http://localhost:3000 in browser
[/code]

**الخيار 2: WireGuard VPN**

bashCopy code
[code]
    # Create WireGuard config (one-time)fly wireguard create # Import to WireGuard client, then access via internal IPv6# Example: http://[fdaa:x:x:x:x::x]:3000
[/code]

**الخيار 3: SSH فقط**

bashCopy code
[code]
    fly ssh console -a my-openclaw
[/code]

### Webhook مع النشر الخاص

إذا كنت تحتاج إلى استدعاءات Webhook الراجعة (Twilio وTelnyx وغيرهما) من دون تعريض عام:

  1. **نفق ngrok** \- شغّل ngrok داخل الحاوية أو كحاوية جانبية
  2. **Tailscale Funnel** \- اعرض مسارات محددة عبر Tailscale
  3. **الصادر فقط** \- يعمل بعض المزوّدين (Twilio) جيدًا للمكالمات الصادرة من دون Webhook


مثال على إعداد مكالمات الصوت مع ngrok:

json5Copy code
[code]
    {  plugins: {    entries: {      "voice-call": {        enabled: true,        config: {          provider: "twilio",          tunnel: { provider: "ngrok" },          webhookSecurity: {            allowedHosts: ["example.ngrok.app"],          },        },      },    },  },}
[/code]

يعمل نفق ngrok داخل الحاوية ويوفر عنوان URL عامًا لـ Webhook من دون كشف تطبيق Fly نفسه. اضبط `webhookSecurity.allowedHosts` على اسم مضيف النفق العام حتى يتم قبول ترويسات المضيف المُمرَّرة.

### مزايا الأمان

الجانب | عام | خاص  
---|---|---  
ماسحات الإنترنت | قابل للاكتشاف | مخفي  
الهجمات المباشرة | ممكنة | محظورة  
وصول واجهة التحكم | المتصفح | وكيل/VPN  
تسليم Webhook | مباشر | عبر نفق  
  
## ملاحظات

  * يستخدم [Fly.io](<http://Fly.io>) **معمارية x86** (وليس ARM)
  * ملف Dockerfile متوافق مع كلتا المعماريتين
  * لتهيئة WhatsApp/Telegram، استخدم `fly ssh console`
  * توجد البيانات الدائمة على وحدة التخزين في `/data`
  * يتطلب Signal Java + signal-cli؛ استخدم صورة مخصصة وأبقِ الذاكرة عند 2GB أو أكثر.


## التكلفة

مع الإعداد الموصى به (`shared-cpu-2x`، وذاكرة RAM بسعة 2GB):

  * حوالي 10-15 دولارًا شهريًا حسب الاستخدام
  * تتضمن الطبقة المجانية بعض الحصة


راجع [أسعار Fly.io](<https://fly.io/docs/about/pricing/>) لمعرفة التفاصيل.

## الخطوات التالية

  * إعداد قنوات المراسلة: [القنوات](</ar/channels>)
  * تهيئة Gateway: [إعدادات Gateway](</ar/gateway/configuration>)
  * إبقاء OpenClaw محدّثًا: [التحديث](</ar/install/updating>)


## ذات صلة

  * [نظرة عامة على التثبيت](</ar/install>)
  * [Hetzner](</ar/install/hetzner>)
  * [Docker](</ar/install/docker>)
  * [استضافة VPS](</ar/vps>)


Was this useful?YesNo