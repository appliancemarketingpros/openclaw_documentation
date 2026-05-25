---
title: التكوين
source_url: https://docs.openclaw.ai/ar/cli/config
scraped_at: 2026-05-25
---

مساعدات الإعداد للتعديلات غير التفاعلية في `openclaw.json`: الحصول على القيم/تعيينها/تصحيحها/إلغاء تعيينها/الملف/المخطط/التحقق منها حسب المسار وطباعة ملف الإعداد النشط. شغّل الأمر بدون أمر فرعي لفتح معالج الإعداد (مثل `openclaw configure`).

## خيارات الجذر

OPENCLAW_DOCS_MARKER:paramOpen:IHBhdGg9Ii0tc2VjdGlvbiA8c2VjdGlvbg " type="string"> مرشح قسم الإعداد الموجّه القابل للتكرار عند تشغيل `openclaw config` بدون أمر فرعي.

الأقسام الموجّهة المدعومة: `workspace`، `model`، `web`، `gateway`، `daemon`، `channels`، `plugins`، `skills`، `health`.

## أمثلة

bashCopy code
[code]
    openclaw config fileopenclaw config --section modelopenclaw config --section gateway --section daemonopenclaw config schemaopenclaw config get browser.executablePathopenclaw config set browser.executablePath "/usr/bin/google-chrome"openclaw config set browser.profiles.work.executablePath "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"openclaw config set agents.defaults.heartbeat.every "2h"openclaw config set agents.list[0].tools.exec.node "node-id-or-name"openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKENopenclaw config set secrets.providers.vaultfile --provider-source file --provider-path /etc/openclaw/secrets.json --provider-mode jsonopenclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config unset plugins.entries.brave.config.webSearch.apiKeyopenclaw config set channels.discord.token --ref-provider default --ref-source env --ref-id DISCORD_BOT_TOKEN --dry-runopenclaw config validateopenclaw config validate --json
[/code]

### `config schema`

يطبع مخطط JSON المُولَّد لـ `openclaw.json` إلى stdout بصيغة JSON.

ما يتضمنه

  * مخطط إعداد الجذر الحالي، بالإضافة إلى حقل سلسلة جذرية `$schema` لأدوات التحرير.
  * بيانات تعريف الوثائق `title` و`description` للحقول المستخدمة في Control UI.
  * ترث عُقد الكائنات المتداخلة، وحرف البدل (`*`)، وعناصر المصفوفة (`[]`) بيانات تعريف `title` / `description` نفسها عند وجود توثيق حقل مطابق.
  * ترث فروع `anyOf` / `oneOf` / `allOf` بيانات تعريف الوثائق نفسها أيضاً عند وجود توثيق حقل مطابق.
  * بيانات تعريف مخطط Plugin والقناة المباشرة بأفضل جهد عند إمكانية تحميل بيانات manifest وقت التشغيل.
  * مخطط احتياطي نظيف حتى عندما يكون الإعداد الحالي غير صالح.

RPC وقت التشغيل المرتبط

يعيد `config.schema.lookup` مسار إعداد واحداً مطبّعاً مع عقدة مخطط سطحية (`title`، `description`، `type`، `enum`، `const`، والحدود الشائعة)، وبيانات تعريف تلميحات واجهة المستخدم المطابقة، وملخصات الأبناء المباشرين. استخدمه للتنقيب محدود المسار في Control UI أو العملاء المخصصين.

bashCopy code
[code]
    openclaw config schema
[/code]

مرّره إلى ملف عندما تريد فحصه أو التحقق منه باستخدام أدوات أخرى:

bashCopy code
[code]
    openclaw config schema > openclaw.schema.json
[/code]

### المسارات

تستخدم المسارات ترميز النقاط أو الأقواس:

bashCopy code
[code]
    openclaw config get agents.defaults.workspaceopenclaw config get agents.list[0].id
[/code]

استخدم فهرس قائمة الوكلاء لاستهداف وكيل محدد:

bashCopy code
[code]
    openclaw config get agents.listopenclaw config set agents.list[1].tools.exec.node "node-id-or-name"
[/code]

## القيم

تُحلَّل القيم كـ JSON5 عند الإمكان؛ وإلا فتُعامل كسلاسل نصية. استخدم `--strict-json` لاشتراط تحليل JSON5. يظل `--json` مدعوماً كاسم مستعار قديم.

bashCopy code
[code]
    openclaw config set agents.defaults.heartbeat.every "0m"openclaw config set gateway.port 19001 --strict-jsonopenclaw config set channels.whatsapp.groups '["*"]' --strict-json
[/code]

يطبع `config get <path> --json` القيمة الخام بصيغة JSON بدلاً من نص منسق للطرفية.

استخدم `--merge` عند إضافة إدخالات إلى تلك الخرائط:

bashCopy code
[code]
    openclaw config set agents.defaults.models '{"openai/gpt-5.4":{}}' --strict-json --mergeopenclaw config set models.providers.ollama.models '[{"id":"llama3.2","name":"Llama 3.2"}]' --strict-json --merge
[/code]

استخدم `--replace` فقط عندما تريد عمداً أن تصبح القيمة المقدمة هي القيمة الكاملة للهدف.

## أوضاع `config set`

يدعم `openclaw config set` أربعة أنماط للإسناد:

### وضع القيمة

bashCopy code
[code]
    openclaw config set <path> <value>
[/code]

### وضع بناء SecretRef

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN
[/code]

### وضع بناء المزوّد

يستهدف وضع بناء المزوّد مسارات `secrets.providers.<alias>` فقط:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-timeout-ms 5000
[/code]

### وضع الدُفعات

bashCopy code
[code]
    openclaw config set --batch-json '[  {    "path": "secrets.providers.default",    "provider": { "source": "env" }  },  {    "path": "channels.discord.token",    "ref": { "source": "env", "provider": "default", "id": "DISCORD_BOT_TOKEN" }  }]'
[/code]

bashCopy code
[code]
    openclaw config set --batch-file ./config-set.batch.json --dry-run
[/code]

يستخدم تحليل الدُفعات دائماً حمولة الدُفعة (`--batch-json`/`--batch-file`) كمصدر للحقيقة. لا يغيّر `--strict-json` / `--json` سلوك تحليل الدُفعات.

## `config patch`

استخدم `config patch` عندما تريد لصق أو تمرير تصحيح بشكل إعداد بدلاً من تشغيل العديد من أوامر `config set` القائمة على المسارات. الإدخال كائن JSON5. تُدمج الكائنات تكرارياً، وتستبدل المصفوفات والقيم العددية القيمة الهدف، وتحذف `null` المسار الهدف.

bashCopy code
[code]
    openclaw config patch --file ./openclaw.patch.json5 --dry-runopenclaw config patch --file ./openclaw.patch.json5
[/code]

يمكنك أيضاً تمرير تصحيح عبر stdin، وهذا مفيد لبرامج إعداد الخوادم البعيدة:

bashCopy code
[code]
    ssh openclaw-host 'openclaw config patch --stdin --dry-run' < ./openclaw.patch.json5ssh openclaw-host 'openclaw config patch --stdin' < ./openclaw.patch.json5
[/code]

مثال على تصحيح:

json5Copy code
[code]
    {  channels: {    slack: {      enabled: true,      mode: "socket",      botToken: { source: "env", provider: "default", id: "SLACK_BOT_TOKEN" },      appToken: { source: "env", provider: "default", id: "SLACK_APP_TOKEN" },      groupPolicy: "open",      requireMention: false,    },    discord: {      enabled: true,      token: { source: "env", provider: "default", id: "DISCORD_BOT_TOKEN" },      dmPolicy: "disabled",      dm: { enabled: false },      groupPolicy: "allowlist",    },  },  agents: {    defaults: {      model: { primary: "openai/gpt-5.5" },      models: {        "openai/gpt-5.5": { params: { fastMode: true } },      },    },  },}
[/code]

استخدم `--replace-path <path>` عندما يجب أن يصبح كائن أو مصفوفة واحد بالضبط القيمة المقدمة بدلاً من تصحيحه تكرارياً:

bashCopy code
[code]
    openclaw config patch --file ./discord.patch.json5 --replace-path 'channels.discord.guilds["123"].channels'
[/code]

يشغّل `--dry-run` فحوصات المخطط وقابلية حل SecretRef بدون كتابة. تُتخطى SecretRefs المدعومة بـ exec افتراضياً أثناء التشغيل التجريبي؛ أضف `--allow-exec` عندما تريد عمداً أن ينفّذ التشغيل التجريبي أوامر المزوّد.

يظل وضع مسار/قيمة JSON مدعوماً لكل من SecretRefs والمزوّدين:

bashCopy code
[code]
    openclaw config set channels.discord.token \  '{"source":"env","provider":"default","id":"DISCORD_BOT_TOKEN"}' \  --strict-json openclaw config set secrets.providers.vaultfile \  '{"source":"file","path":"/etc/openclaw/secrets.json","mode":"json"}' \  --strict-json
[/code]

## أعلام بناء المزوّد

يجب أن تستخدم أهداف بناء المزوّد `secrets.providers.<alias>` كمسار.

الأعلام الشائعة

  * `--provider-source <env|file|exec>`
  * `--provider-timeout-ms <ms>` (`file`, `exec`)

مزوّد Env (--provider-source env)

  * `--provider-allowlist &lt;ENV_VAR&gt;` (قابل للتكرار)

مزوّد File (--provider-source file)

  * `--provider-path <path>` (مطلوب)
  * `--provider-mode <singleValue|json>`
  * `--provider-max-bytes <bytes>`
  * `--provider-allow-insecure-path`

مزوّد Exec (--provider-source exec)

  * `--provider-command <path>` (مطلوب)
  * `--provider-arg <arg>` (قابل للتكرار)
  * `--provider-no-output-timeout-ms <ms>`
  * `--provider-max-output-bytes <bytes>`
  * `--provider-json-only`
  * `--provider-env &lt;KEY=VALUE&gt;` (قابل للتكرار)
  * `--provider-pass-env &lt;ENV_VAR&gt;` (قابل للتكرار)
  * `--provider-trusted-dir <path>` (قابل للتكرار)
  * `--provider-allow-insecure-path`
  * `--provider-allow-symlink-command`


مثال على مزوّد exec مقوّى:

bashCopy code
[code]
    openclaw config set secrets.providers.vault \  --provider-source exec \  --provider-command /usr/local/bin/openclaw-vault \  --provider-arg read \  --provider-arg openai/api-key \  --provider-json-only \  --provider-pass-env VAULT_TOKEN \  --provider-trusted-dir /usr/local/bin \  --provider-timeout-ms 5000
[/code]

## التشغيل التجريبي

استخدم `--dry-run` للتحقق من التغييرات بدون كتابة `openclaw.json`.

bashCopy code
[code]
    openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run openclaw config set channels.discord.token \  --ref-provider default \  --ref-source env \  --ref-id DISCORD_BOT_TOKEN \  --dry-run \  --json openclaw config set channels.discord.token \  --ref-provider vault \  --ref-source exec \  --ref-id discord/token \  --dry-run \  --allow-exec
[/code]

سلوك التشغيل التجريبي

  * وضع البناء: يشغّل فحوصات قابلية حل SecretRef للمراجع/المزوّدين المتغيرين.
  * وضع JSON (`--strict-json`، `--json`، أو وضع الدُفعات): يشغّل التحقق من المخطط بالإضافة إلى فحوصات قابلية حل SecretRef.
  * يعمل التحقق من السياسة أيضاً للأسطح الهدف المعروفة غير المدعومة لـ SecretRef.
  * تقيّم فحوصات السياسة الإعداد الكامل بعد التغيير، لذلك لا يمكن لكتابات الكائن الأب (مثل تعيين `hooks` ككائن) تجاوز التحقق من الأسطح غير المدعومة.
  * تُتخطى فحوصات SecretRef من نوع Exec افتراضياً أثناء التشغيل التجريبي لتجنب الآثار الجانبية للأوامر.
  * استخدم `--allow-exec` مع `--dry-run` للاشتراك في فحوصات SecretRef من نوع exec (قد ينفّذ هذا أوامر المزوّد).
  * `--allow-exec` مخصص للتشغيل التجريبي فقط ويُنتج خطأ إذا استُخدم بدون `--dry-run`.

حقول --dry-run --json

يطبع `--dry-run --json` تقريراً قابلاً للقراءة آلياً:

  * `ok`: ما إذا كان التشغيل التجريبي قد نجح
  * `operations`: عدد التعيينات التي تم تقييمها
  * `checks`: ما إذا كانت فحوصات المخطط/إمكانية الحل قد شُغّلت
  * `checks.resolvabilityComplete`: ما إذا كانت فحوصات إمكانية الحل قد اكتملت (تكون false عند تخطي مراجع exec)
  * `refsChecked`: عدد المراجع التي حُلّت فعليًا أثناء التشغيل التجريبي
  * `skippedExecRefs`: عدد مراجع exec التي تم تخطيها لأن `--allow-exec` لم يكن مضبوطًا
  * `errors`: إخفاقات منظمة في المخطط/إمكانية الحل عندما تكون `ok=false`


### شكل مخرجات JSON

json5Copy code
[code]
    {  ok: boolean,  operations: number,  configPath: string,  inputModes: ["value" | "json" | "builder", ...],  checks: {    schema: boolean,    resolvability: boolean,    resolvabilityComplete: boolean,  },  refsChecked: number,  skippedExecRefs: number,  errors?: [    {      kind: "schema" | "resolvability",      message: string,      ref?: string, // present for resolvability errors    },  ],}
[/code]

### Success example

jsonCopy code
[code]
    {  "ok": true,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0}
[/code]

### Failure example

jsonCopy code
[code]
    {  "ok": false,  "operations": 1,  "configPath": "~/.openclaw/openclaw.json",  "inputModes": ["builder"],  "checks": {    "schema": false,    "resolvability": true,    "resolvabilityComplete": true  },  "refsChecked": 1,  "skippedExecRefs": 0,  "errors": [    {      "kind": "resolvability",      "message": "Error: Environment variable \"MISSING_TEST_SECRET\" is not set.",      "ref": "env:default:MISSING_TEST_SECRET"    }  ]}
[/code]

If dry-run fails

  * `config schema validation failed`: شكل الإعدادات بعد التغيير غير صالح؛ أصلح المسار/القيمة أو شكل كائن المزود/ref.
  * `Config policy validation failed: unsupported SecretRef usage`: انقل بيانات الاعتماد تلك مرة أخرى إلى إدخال نص عادي/سلسلة نصية، وأبقِ SecretRefs على الأسطح المدعومة فقط.
  * `SecretRef assignment(s) could not be resolved`: لا يمكن حاليًا حل المزود/ref المشار إليه (متغير بيئة مفقود، مؤشر ملف غير صالح، فشل مزود exec، أو عدم تطابق المزود/المصدر).
  * `Dry run note: skipped <n> exec SecretRef resolvability check(s)`: تخطى التشغيل التجريبي مراجع exec؛ أعد التشغيل باستخدام `--allow-exec` إذا كنت تحتاج إلى التحقق من إمكانية حل exec.
  * في وضع الدُفعات، أصلح الإدخالات الفاشلة وأعد تشغيل `--dry-run` قبل الكتابة.


## أمان الكتابة

يتحقق `openclaw config set` وغيره من كتّاب الإعدادات المملوكين لـ OpenClaw من الإعدادات الكاملة بعد التغيير قبل تثبيتها على القرص. إذا فشل الحمولة الجديدة في تحقق المخطط أو بدت كاستبدال تدميري، تُترك الإعدادات النشطة كما هي وتُحفظ الحمولة المرفوضة بجانبها باسم `openclaw.json.rejected.*`.

فضّل الكتابة عبر CLI للتعديلات الصغيرة:

bashCopy code
[code]
    openclaw config set gateway.reload.mode hybrid --dry-runopenclaw config set gateway.reload.mode hybridopenclaw config validate
[/code]

إذا رُفضت كتابة، افحص الحمولة المحفوظة وأصلح شكل الإعدادات الكامل:

bashCopy code
[code]
    CONFIG="$(openclaw config file)"ls -lt "$CONFIG".rejected.* 2>/dev/null | headopenclaw config validate
[/code]

ما تزال الكتابة المباشرة بالمحرر مسموحة، لكن Gateway الجاري يعاملها كغير موثوقة حتى تنجح في التحقق. تؤدي التعديلات المباشرة غير الصالحة إلى فشل بدء التشغيل أو يتم تخطيها بواسطة إعادة التحميل الساخنة؛ لا يعيد Gateway كتابة `openclaw.json`. شغّل `openclaw doctor --fix` لإصلاح الإعدادات ذات البادئات/المستبدلة أو لاستعادة آخر نسخة سليمة معروفة. راجع [استكشاف أخطاء Gateway وإصلاحها](</ar/gateway/troubleshooting#gateway-rejected-invalid-config>).

استرداد الملف الكامل مخصص لإصلاح doctor. تبقى تغييرات مخطط Plugin أو انحراف `minHostVersion` واضحة بدلًا من التراجع عن إعدادات المستخدم غير المرتبطة مثل النماذج، والمزودين، وملفات تعريف المصادقة، والقنوات، وتعريض Gateway، والأدوات، والذاكرة، والمتصفح، أو إعدادات cron.

## الأوامر الفرعية

  * `config file`: اطبع مسار ملف الإعدادات النشط (المحلول من `OPENCLAW_CONFIG_PATH` أو الموقع الافتراضي). ينبغي أن يحدد المسار ملفًا عاديًا، لا رابطًا رمزيًا.


أعد تشغيل Gateway بعد التعديلات.

## التحقق

تحقق من الإعدادات الحالية مقابل المخطط النشط دون بدء Gateway.

bashCopy code
[code]
    openclaw config validateopenclaw config validate --json
[/code]

بعد نجاح `openclaw config validate`، يمكنك استخدام TUI المحلي لجعل وكيل مضمّن يقارن الإعدادات النشطة بالوثائق أثناء تحققك من كل تغيير من الطرفية نفسها:

bashCopy code
[code]
    openclaw chat
[/code]

ثم داخل TUI:

textCopy code
[code]
    !openclaw config file!openclaw docs gateway auth token secretref!openclaw config validate!openclaw doctor
[/code]

حلقة الإصلاح المعتادة:

* ### Compare with docs

اطلب من الوكيل مقارنة إعداداتك الحالية بصفحة الوثائق ذات الصلة واقتراح أصغر إصلاح.

* ### Apply targeted edits

طبّق تعديلات مستهدفة باستخدام `openclaw config set` أو `openclaw configure`.

* ### Re-validate

أعد تشغيل `openclaw config validate` بعد كل تغيير.

* ### Doctor for runtime issues

إذا نجح التحقق لكن وقت التشغيل ما يزال غير سليم، فشغّل `openclaw doctor` أو `openclaw doctor --fix` للحصول على مساعدة في الترحيل والإصلاح.

## ذات صلة

  * [مرجع CLI](</ar/cli>)
  * [الإعدادات](</ar/gateway/configuration>)


Was this useful?YesNo