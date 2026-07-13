---
title: مراجع أسرار الخزنة
source_url: https://docs.openclaw.ai/ar/plugins/vault
scraped_at: 2026-07-13
---

CapabilitiesPlugin guides

# مراجع الأسرار في Vault

يتيح Plugin ‏Vault المضمّن لـ OpenClaw تحليل مراجع الأسرار `exec` من HashiCorp Vault عند بدء تشغيل Gateway وعند إعادة التحميل. يخزّن OpenClaw مراجع Vault في الإعدادات، ويحتفظ بالقيم المحلولة في لقطة الأسرار داخل الذاكرة، ولا يعيد كتابة مفاتيح API المحلولة إلى `openclaw.json`.

استخدم هذا عندما تكون قد شغّلت Vault بالفعل أو تريد إبقاء مفاتيح موفّري النماذج خارج ملفات إعدادات OpenClaw. للاطلاع على نموذج وقت تشغيل مراجع الأسرار، راجع [إدارة الأسرار](</ar/gateway/secrets>).

## قبل البدء

تحتاج إلى:

  * OpenClaw مع توفّر Plugin ‏`vault` المضمّن
  * خادم Vault يمكن الوصول إليه
  * مصادقة Vault يمكنها إصدار رمز عميل مميّز يملك صلاحية قراءة مسارات الأسرار التي ينبغي لـ OpenClaw تحليلها
  * يجب أن تتضمن البيئة التي تبدأ تشغيل Gateway المتغير `VAULT_ADDR`، وأحد الخيارات التالية: `VAULT_TOKEN`، أو `OPENCLAW_VAULT_AUTH_METHOD=token_file` مع `VAULT_TOKEN_FILE`، أو تسجيل دخول JWT/Kubernetes مُعدّ


يتصل المحلّل بـ Vault عبر HTTP من Node. لا يحتاج Gateway إلى CLI الخاص بـ Vault لتحليل مراجع الأسرار.

فعّل Plugin المضمّن قبل تشغيل أوامر `openclaw vault`:

bashCopy code
[code]
    openclaw plugins enable vault
[/code]

## تخزين مفتاح موفّر في Vault

يستخدم OpenClaw افتراضيًا KV v2 المثبّت عند `secret`، بما يتوافق مع أمثلة خادم تطوير Vault. بالنسبة إلى Vault في بيئة الإنتاج، عيّن `OPENCLAW_VAULT_KV_MOUNT` إلى مسار تثبيت KV الفعلي قبل إنشاء معرّفات مراجع الأسرار. باستخدام إعدادات OpenClaw الافتراضية، يقرأ معرّف مرجع السر هذا:

textCopy code
[code]
    providers/openrouter/apiKey
[/code]

حقل Vault التالي:

textCopy code
[code]
    secret/data/providers/openrouter -> apiKey
[/code]

إحدى طرق إنشائه باستخدام CLI الخاص بـ Vault هي:

bashCopy code
[code]
    export OPENROUTER_API_KEY=<openrouter-api-key>vault kv put secret/providers/openrouter apiKey="$OPENROUTER_API_KEY"
[/code]

استخدم رمز عميل مميّزًا مقيّد النطاق لـ OpenClaw، وليس رمز الجذر المميّز. بالنسبة إلى تخطيط KV v2 الافتراضي، تبدو سياسة دنيا لمفاتيح موفّري النماذج كما يلي:

hclCopy code
[code]
    path "secret/data/providers/*" {  capabilities = ["read"]}
[/code]

## إتاحة Vault لـ Gateway

بالنسبة إلى Gateway محلي غير موضوع في حاوية، صدّر إعدادات Vault في الصدفة نفسها التي تبدأ تشغيل OpenClaw. تقرأ طريقة المصادقة الافتراضية رمز عميل Vault المميّز من `VAULT_TOKEN`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport VAULT_TOKEN=<vault-client-token>
[/code]

إذا كتب Vault Agent رمزًا مميّزًا في ملف إخراج، فاستخدم المصادقة بملف الرمز المميّز:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=token_fileexport VAULT_TOKEN_FILE=/vault/secrets/token
[/code]

بالنسبة إلى خادم Vault موقّع بواسطة مرجع مصدّق خاص، ثبّت هذا المرجع المصدّق في مخزن ثقة المضيف وفعّل ثقة النظام في Node:

bashCopy code
[code]
    export NODE_USE_SYSTEM_CA=1
[/code]

أو وفّر حزمة PEM مباشرةً:

bashCopy code
[code]
    export NODE_EXTRA_CA_CERTS=/path/to/vault-ca.pem
[/code]

يجب أن تكون هذه المتغيرات موجودة عند بدء تشغيل OpenClaw. يمرّرها Plugin ‏Vault إلى عملية المحلّل الخاصة به.

للمصادقة غير التفاعلية باستخدام JWT، استخدم ملف JWT لحمل العمل ودورًا في Vault من النوع `jwt`:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=jwtexport OPENCLAW_VAULT_AUTH_MOUNT=jwtexport OPENCLAW_VAULT_AUTH_ROLE=openclawexport OPENCLAW_VAULT_JWT_FILE=/var/run/secrets/tokens/vault
[/code]

يجب أن يكون ملف JWT رمز حمل عمل مميّزًا مُسقطًا، مثل رمز حساب خدمة Kubernetes مميّز ذي جمهور يقبله دور Vault. يُعد تسجيل دخول OIDC التفاعلي عبر المتصفح مفيدًا للمستخدمين، لكن وقت تشغيل Gateway يحتاج إلى تسجيل دخول JWT غير تفاعلي أو ملف رمز مميّز.

بالنسبة إلى طريقة مصادقة Kubernetes في Vault، استخدم `kubernetes`. وهي مخصّصة لبوابات Gateway التي تعمل بوصفها Pods؛ ويكون التثبيت الافتراضي هو `kubernetes`، وملف JWT الافتراضي هو مسار رمز حساب الخدمة المميّز القياسي:

bashCopy code
[code]
    export VAULT_ADDR=https://vault.example.comexport OPENCLAW_VAULT_AUTH_METHOD=kubernetesexport OPENCLAW_VAULT_AUTH_ROLE=openclaw
[/code]

عيّن `OPENCLAW_VAULT_AUTH_MOUNT` فقط عندما تكون مصادقة Kubernetes في Vault مثبّتة في موضع آخر غير `auth/kubernetes`. وعيّن `OPENCLAW_VAULT_JWT_FILE` فقط عندما يكون رمز حساب الخدمة المميّز مُسقطًا في مسار مخصّص.

إعدادات اختيارية:

bashCopy code
[code]
    export VAULT_NAMESPACE=<namespace-name>export OPENCLAW_VAULT_KV_MOUNT=secretexport OPENCLAW_VAULT_KV_VERSION=2
[/code]

تحقق مما تستطيع الصدفة الحالية رؤيته:

bashCopy code
[code]
    openclaw vault status
[/code]

عند إعداد أكثر من موفّر أسرار واحد مدعوم من Vault، اختر أحدها بالاسم المستعار:

bashCopy code
[code]
    openclaw vault status --provider-alias corp-vault
[/code]

لا يطبع `openclaw vault status` المتغير `VAULT_TOKEN` مطلقًا؛ بل يبلّغ فقط عما إذا كان الرمز المميّز وملف الرمز المميّز وملف JWT معيّنة أم لا.

## إنشاء خطة لمراجع الأسرار وتطبيقها

أنشئ خطة تربط مفتاح API لموفّر نماذج OpenRouter بـ Vault:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openrouter-id providers/openrouter/apiKey
[/code]

طبّق الخطة وتحقق منها:

bashCopy code
[code]
    openclaw secrets apply --from ./vault-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from ./vault-secrets-plan.json --allow-execopenclaw secrets audit --check --allow-execopenclaw secrets reload
[/code]

استخدم `--allow-exec` لأن Plugin ‏Vault ينفّذ التحليل عبر موفّر مراجع أسرار `exec` يديره OpenClaw.

إذا لم يكن Gateway قيد التشغيل بعد، فابدأ تشغيله بالطريقة المعتادة بعد تطبيق الخطة بدلًا من تشغيل `openclaw secrets reload`.

## إعداد المزيد من مفاتيح الموفّرين

اختصارات مضمّنة:

bashCopy code
[code]
    openclaw vault setup --openai-id providers/openai/apiKeyopenclaw vault setup --anthropic-id providers/anthropic/apiKeyopenclaw vault setup --openrouter-id providers/openrouter/apiKey
[/code]

مفاتيح موفّرين متعددة في خطة واحدة:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --openai-id providers/openai/apiKey \  --anthropic-id providers/anthropic/apiKey \  --openrouter-id providers/openrouter/apiKey
[/code]

بالنسبة إلى الموفّرين المضمّنين الذين لا يملكون اختصارات، أو موفّري النماذج المخصّصين والمتوافقين مع OpenAI والمُعدّين مسبقًا، استخدم `--provider-key`:

bashCopy code
[code]
    openclaw vault setup \  --plan-out ./vault-secrets-plan.json \  --provider-key local-openai=providers/local-openai/apiKey \  --provider-key groq=providers/groq/apiKey
[/code]

يكتب كل `--provider-key <provider=id>` مرجع سر في `models.providers.<provider>.apiKey`. بالنسبة إلى الموفّرين المخصّصين، لا ينشئ هذا الخيار إعدادات الموفّر `baseUrl` أو `api` أو `models`؛ أعدّها أولًا.

استخدم `--target <path=id>` لأي مسار هدف معروف لمرجع سر:

bashCopy code
[code]
    openclaw vault setup \  --target channels.telegram.botToken=channels/telegram/botToken \  --target models.providers.openai.headers.x-api-key=providers/openai/proxyKey \  --target auth-profiles:main:profiles.openai.key=providers/openai/apiKey
[/code]

تنطبق مسارات الأهداف المجرّدة على `openclaw.json`. استخدم `auth-profiles:<agentId>:<path>` لأهداف `auth-profiles.json` الموجودة. يجب أن يكون مسار الهدف هدفًا مسجّلًا لمراجع أسرار OpenClaw. لا ينشئ أمر الإعداد أسرارًا اعتباطية مسمّاة في OpenClaw؛ إذ يظل Vault مخزن الأسرار، ولا يخزّن OpenClaw مراجع الأسرار إلا في حقول الإعدادات المدعومة.

## تنسيق معرّف مرجع السر

تستخدم معرّفات مراجع أسرار Vault الاصطلاح التالي:

textCopy code
[code]
    <vault-secret-path>/<field>
[/code]

أمثلة:

معرّف مرجع السر | قراءة Vault الافتراضية باستخدام KV v2 | الحقل المُعاد  
---|---|---  
`providers/openrouter/apiKey` | `secret/data/providers/openrouter` | `apiKey`  
`providers/openai/apiKey` | `secret/data/providers/openai` | `apiKey`  
`teams/agent-prod/openrouter` | `secret/data/teams/agent-prod` | `openrouter`  
  
يجب أن يكون حقل Vault المُعاد سلسلة نصية.

بالنسبة إلى KV v1، عيّن:

bashCopy code
[code]
    export OPENCLAW_VAULT_KV_VERSION=1
[/code]

عندئذٍ يقرأ `providers/openrouter/apiKey`:

textCopy code
[code]
    secret/providers/openrouter -> apiKey
[/code]

## ما يخزّنه OpenClaw

يؤدي تطبيق خطة إعداد Vault إلى تخزين موفّر يديره Plugin:

jsonCopy code
[code]
    {  "source": "exec",  "pluginIntegration": {    "pluginId": "vault",    "integrationId": "vault"  }}
[/code]

تشير حقول بيانات الاعتماد إلى ذلك الموفّر:

jsonCopy code
[code]
    { "source": "exec", "provider": "vault", "id": "providers/openrouter/apiKey" }
[/code]

توجد القيمة المحلولة فقط في لقطة أسرار وقت التشغيل النشطة.

## الحاويات وعمليات النشر المُدارة

تستخدم بوابات Gateway الموضوعة في حاويات إعدادات Plugin ومراجع الأسرار نفسها. يجب أن تتلقى الحاوية:

  * `VAULT_ADDR`
  * مصدر مصادقة واحدًا: 
    * `VAULT_TOKEN`
    * `OPENCLAW_VAULT_AUTH_METHOD=token_file` بالإضافة إلى `VAULT_TOKEN_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=jwt` بالإضافة إلى `OPENCLAW_VAULT_AUTH_MOUNT` و`OPENCLAW_VAULT_AUTH_ROLE` و`OPENCLAW_VAULT_JWT_FILE`
    * `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` بالإضافة إلى `OPENCLAW_VAULT_AUTH_ROLE`؛ ويمكن اختياريًا تجاوز `OPENCLAW_VAULT_AUTH_MOUNT` أو `OPENCLAW_VAULT_JWT_FILE`
  * اختياريًا: `VAULT_NAMESPACE` و`OPENCLAW_VAULT_KV_MOUNT` و`OPENCLAW_VAULT_KV_VERSION`


عند استخدام Kubernetes، فضّل `OPENCLAW_VAULT_AUTH_METHOD=kubernetes` عندما تكون مصادقة Kubernetes في Vault مُعدّة للعنقود. استخدم `OPENCLAW_VAULT_AUTH_METHOD=jwt` فقط عندما يكون Vault مُعدًّا للتعامل مع العنقود بوصفه جهة إصدار JWT/OIDC عامة. كلا الخيارين أفضل من رمز Vault مميّز طويل الأجل داخل سر Kubernetes. ويمكن لعمليات النشر التي تستخدم Vault Agent كحاوية جانبية أو أداة حقن استخدام `token_file` بدلًا من ذلك.

بالنسبة إلى إعدادات Vault متعددة المستأجرين، احتفظ بتوجيه المستأجرين ضمن سياسة Vault وإعدادات النشر. لا يتطلب OpenClaw تثبيتًا أو دورًا أو مسارًا ثابتًا؛ إذ يمكن لكل بيئة Gateway تعيين قيمها الخاصة لـ `OPENCLAW_VAULT_KV_MOUNT` و`OPENCLAW_VAULT_AUTH_ROLE` ومعرّفات مراجع الأسرار. إذا كان لا بد من أن يحل Gateway مشترك واحد أسرار مستخدمي Vault مختلفين في الوقت نفسه، فاستخدم موفّري `exec` مُعدّين يدويًا يغلّفون بيئات مصادقة منفصلة، أو وزّع المستأجرين على بيئات Gateway ذات بيئات Vault منفصلة.

## ذو صلة

  * [إدارة الأسرار](</ar/gateway/secrets>)
  * [`openclaw secrets`](</ar/cli/secrets>)
  * [قائمة Plugins](</ar/plugins/plugin-inventory>)


Was this useful?YesNo

Open issue