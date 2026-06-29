---
title: EasyRunner
source_url: https://docs.openclaw.ai/ar/platforms/easyrunner
scraped_at: 2026-06-29
---

PlatformsPlatforms overview

يمكن لـ EasyRunner استضافة OpenClaw Gateway كتطبيق صغير ضمن حاوية خلف وكيل Caddy. يفترض هذا الدليل وجود مضيف EasyRunner يشغّل تطبيقات Compose متوافقة مع Podman ويعرّض HTTPS عبر Caddy.

## قبل أن تبدأ

  * خادم EasyRunner مع نطاق موجّه إليه.
  * صورة حاوية OpenClaw مبنية أو منشورة.
  * مجلد تهيئة دائم لـ `/home/node/.openclaw`.
  * مجلد مساحة عمل دائم لـ `/workspace`.
  * رمز أو كلمة مرور قوية لـ Gateway.


أبقِ مصادقة الجهاز مفعّلة عندما يكون ذلك ممكنًا. إذا كان نشر الوكيل العكسي لديك لا ينقل هوية الجهاز بشكل صحيح، فأصلح إعدادات الوكيل الموثوق أولًا؛ ولا تستخدم تجاوزات المصادقة الخطرة إلا لشبكة خاصة بالكامل وتحت تحكم المشغّل.

## تطبيق Compose

أنشئ تطبيق EasyRunner بملف Compose على الشكل التالي:

yamlCopy code
[code]
    services:  openclaw:    image: ghcr.io/openclaw/openclaw:latest    restart: unless-stopped    environment:      OPENCLAW_GATEWAY_TOKEN: ${OPENCLAW_GATEWAY_TOKEN}      OPENCLAW_HOME: /home/node      OPENCLAW_STATE_DIR: /home/node/.openclaw      OPENCLAW_CONFIG_PATH: /home/node/.openclaw/openclaw.json      OPENCLAW_WORKSPACE_DIR: /workspace    volumes:      - openclaw-config:/home/node/.openclaw      - openclaw-workspace:/workspace    labels:      caddy: openclaw.example.com      caddy.reverse_proxy: "{{upstreams 1455}}"    command: ["openclaw", "gateway", "--bind", "lan", "--port", "1455"] volumes:  openclaw-config:  openclaw-workspace:
[/code]

استبدل `openclaw.example.com` باسم مضيف Gateway لديك. خزّن `OPENCLAW_GATEWAY_TOKEN` في مدير الأسرار/البيئة في EasyRunner بدلًا من تثبيته في تعريف التطبيق.

## تهيئة OpenClaw

داخل مجلد التهيئة الدائم، اجعل Gateway قابلًا للوصول فقط عبر الوكيل واطلب المصادقة:

json5Copy code
[code]
    {  gateway: {    bind: "lan",    port: 1455,    auth: {      token: "${OPENCLAW_GATEWAY_TOKEN}",    },  },}
[/code]

إذا كان Caddy ينهي TLS لـ Gateway، فاضبط إعدادات الوكيل الموثوق لمسار الوكيل الدقيق بدلًا من تعطيل فحوصات المصادقة عالميًا. راجع [مصادقة الوكيل الموثوق](</ar/gateway/trusted-proxy-auth>).

## التحقق

من محطة العمل لديك:

bashCopy code
[code]
    openclaw gateway probe --url https://openclaw.example.com --token <token>openclaw gateway status --url https://openclaw.example.com --token <token>
[/code]

من مضيف EasyRunner، افحص سجلات التطبيق للتأكد من وجود Gateway يستمع وعدم وجود إخفاقات عند بدء التشغيل في SecretRef أو Plugin أو مصادقة القنوات.

## التحديثات والنسخ الاحتياطية

  * اسحب أو ابنِ صورة OpenClaw الجديدة، ثم أعد نشر تطبيق EasyRunner.
  * انسخ مجلد `openclaw-config` احتياطيًا قبل التحديثات.
  * انسخ `openclaw-workspace` احتياطيًا إذا كان الوكلاء يكتبون بيانات مشاريع دائمة هناك.
  * شغّل `openclaw doctor` بعد التحديثات الكبرى لاكتشاف ترحيلات التهيئة وتحذيرات الخدمة.


## استكشاف الأخطاء وإصلاحها

  * يتعذر على `gateway probe` الاتصال: تأكد من أن اسم مضيف Caddy يشير إلى التطبيق وأن الحاوية تستمع على `0.0.0.0:1455`.
  * فشل المصادقة: بدّل الرمز في أسرار EasyRunner وأمر العميل المحلي معًا.
  * أصبحت الملفات مملوكة للمستخدم root بعد الاستعادة: أصلح المجلدات المثبتة بحيث يستطيع مستخدم الحاوية الكتابة إلى `/home/node/.openclaw` و`/workspace`.
  * فشل المتصفح أو Plugins القنوات: تحقق مما إذا كانت الملفات التنفيذية الخارجية المطلوبة، والخروج إلى الشبكة، وبيانات الاعتماد المثبتة متاحة داخل الحاوية.


Was this useful?YesNo

Open issue