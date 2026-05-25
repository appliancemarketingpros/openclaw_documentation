---
title: إعداد Plugin وتكوينه
source_url: https://docs.openclaw.ai/ar/plugins/sdk-setup
scraped_at: 2026-05-25
---

مرجع لتحزيم Plugin (بيانات `package.json` الوصفية)، والبيانات التعريفية (`openclaw.plugin.json`)، وإدخالات الإعداد، ومخططات التهيئة.

## بيانات الحزمة الوصفية

يحتاج `package.json` لديك إلى حقل `openclaw` يوضّح لنظام Plugin ما يوفّره Plugin لديك:

### Channel plugin

jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-channel",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "channel": {      "id": "my-channel",      "label": "My Channel",      "blurb": "Short description of the channel."    }  }}
[/code]

### Provider plugin / ClawHub baseline

openclaw-clawhub-package.jsonCopy code
[code]
    {  "name": "@myorg/openclaw-my-plugin",  "version": "1.0.0",  "type": "module",  "openclaw": {    "extensions": ["./index.ts"],    "compat": {      "pluginApi": ">=2026.3.24-beta.2",      "minGatewayVersion": "2026.3.24-beta.2"    },    "build": {      "openclawVersion": "2026.3.24-beta.2",      "pluginSdkVersion": "2026.3.24-beta.2"    }  }}
[/code]

### حقول `openclaw`

ملفات نقطة الدخول (نسبية إلى جذر الحزمة).

إدخال خفيف خاص بالإعداد فقط (اختياري).

بيانات وصفية لفهرس القنوات لواجهات الإعداد، والاختيار، والبدء السريع، والحالة.

معرّفات المزوّدين التي يسجلها هذا Plugin.

تلميحات التثبيت: `npmSpec`، و`localPath`، و`defaultChoice`، و`minHostVersion`، و`expectedIntegrity`، و`allowInvalidConfigRecovery`.

أعلام سلوك بدء التشغيل.

### `openclaw.channel`

`openclaw.channel` هو بيانات وصفية خفيفة للحزمة لاكتشاف القنوات وواجهات الإعداد قبل تحميل وقت التشغيل.

الحقل | النوع | معناه  
---|---|---  
`id` | `string` | معرّف القناة المعتمد.  
`label` | `string` | تسمية القناة الرئيسية.  
`selectionLabel` | `string` | تسمية أداة الاختيار/الإعداد عندما ينبغي أن تختلف عن `label`.  
`detailLabel` | `string` | تسمية تفاصيل ثانوية لفهارس القنوات الأكثر ثراءً وواجهات الحالة.  
`docsPath` | `string` | مسار الوثائق لروابط الإعداد والاختيار.  
`docsLabel` | `string` | تسمية بديلة تُستخدم لروابط الوثائق عندما ينبغي أن تختلف عن معرّف القناة.  
`blurb` | `string` | وصف قصير للتعريف/الفهرس.  
`order` | `number` | ترتيب الفرز في فهارس القنوات.  
`aliases` | `string[]` | أسماء مستعارة إضافية للبحث عند اختيار القناة.  
`preferOver` | `string[]` | معرّفات Plugins/قنوات ذات أولوية أدنى ينبغي أن تتقدم هذه القناة عليها.  
`systemImage` | `string` | اسم اختياري لأيقونة/صورة نظام لفهارس واجهة مستخدم القنوات.  
`selectionDocsPrefix` | `string` | نص بادئة قبل روابط الوثائق في واجهات الاختيار.  
`selectionDocsOmitLabel` | `boolean` | عرض مسار الوثائق مباشرة بدلًا من رابط وثائق ذي تسمية في نص الاختيار.  
`selectionExtras` | `string[]` | سلاسل قصيرة إضافية تُلحق بنص الاختيار.  
`markdownCapable` | `boolean` | يعلّم القناة على أنها تدعم Markdown لقرارات التنسيق الصادر.  
`exposure` | `object` | عناصر التحكم في ظهور القناة لواجهات الإعداد، والقوائم المهيأة، والوثائق.  
`quickstartAllowFrom` | `boolean` | يضم هذه القناة إلى مسار إعداد البدء السريع القياسي `allowFrom`.  
`forceAccountBinding` | `boolean` | يتطلب ربط الحساب صراحة حتى عند وجود حساب واحد فقط.  
`preferSessionLookupForAnnounceTarget` | `boolean` | يفضّل البحث عن الجلسة عند حل أهداف الإعلان لهذه القناة.  
  
مثال:

jsonCopy code
[code]
    {  "openclaw": {    "channel": {      "id": "my-channel",      "label": "My Channel",      "selectionLabel": "My Channel (self-hosted)",      "detailLabel": "My Channel Bot",      "docsPath": "/channels/my-channel",      "docsLabel": "my-channel",      "blurb": "Webhook-based self-hosted chat integration.",      "order": 80,      "aliases": ["mc"],      "preferOver": ["my-channel-legacy"],      "selectionDocsPrefix": "Guide:",      "selectionExtras": ["Markdown"],      "markdownCapable": true,      "exposure": {        "configured": true,        "setup": true,        "docs": true      },      "quickstartAllowFrom": true    }  }}
[/code]

يدعم `exposure` ما يلي:

  * `configured`: تضمين القناة في واجهات القوائم المهيأة/ذات نمط الحالة
  * `setup`: تضمين القناة في أدوات اختيار الإعداد/التهيئة التفاعلية
  * `docs`: تعليم القناة على أنها عامة الظهور في واجهات الوثائق/التنقل


### `openclaw.install`

`openclaw.install` هو بيانات وصفية للحزمة، وليس بيانات وصفية للبيان التعريفي.

الحقل | النوع | معناه  
---|---|---  
`clawhubSpec` | `string` | مواصفة ClawHub المعتمدة لمسارات التثبيت/التحديث وتثبيت التعريف عند الطلب.  
`npmSpec` | `string` | مواصفة npm المعتمدة لمسارات التثبيت/التحديث الاحتياطية.  
`localPath` | `string` | مسار التطوير المحلي أو التثبيت المضمّن.  
`defaultChoice` | `"clawhub"` | `"npm"` | `"local"` | مصدر التثبيت المفضل عند توفر عدة مصادر.  
`minHostVersion` | `string` | أدنى إصدار OpenClaw مدعوم بالصيغة `>=x.y.z` أو `>=x.y.z-prerelease`.  
`expectedIntegrity` | `string` | سلسلة سلامة توزيعة npm المتوقعة، عادةً `sha512-...`، للتثبيتات المثبتة بإصدار محدد.  
`allowInvalidConfigRecovery` | `boolean` | يتيح لمسارات إعادة تثبيت Plugin المضمّن التعافي من إخفاقات محددة في تهيئة قديمة.  
  
Onboarding behavior

يستخدم التعريف التفاعلي أيضًا `openclaw.install` لواجهات التثبيت عند الطلب. إذا كان Plugin لديك يعرض خيارات مصادقة المزوّد أو بيانات وصفية لإعداد/فهرس القنوات قبل تحميل وقت التشغيل، يمكن للتعريف عرض ذلك الخيار، والمطالبة بتثبيت ClawHub أو npm أو تثبيت محلي، ثم تثبيت Plugin أو تمكينه، ثم متابعة المسار المحدد. تستخدم خيارات تعريف ClawHub `clawhubSpec` وتُفضّل عند وجودها؛ وتتطلب خيارات npm بيانات وصفية موثوقة للفهرس مع `npmSpec` للسجل؛ وتكون الإصدارات الدقيقة و`expectedIntegrity` اختيارية كتثبيتات npm مثبتة. إذا كان `expectedIntegrity` موجودًا، تفرضه مسارات التثبيت/التحديث لـ npm. أبقِ بيانات "ما الذي يجب عرضه" الوصفية في `openclaw.plugin.json` وبيانات "كيفية تثبيته" الوصفية في `package.json`.

minHostVersion enforcement

إذا تم تعيين `minHostVersion`، فإن كلًا من التثبيت وتحميل سجل البيانات التعريفية غير المضمّن يفرضان ذلك. تتخطى المضيفات الأقدم Plugins الخارجية؛ وتُرفض سلاسل الإصدارات غير الصالحة. يُفترض أن Plugins المصدر المضمّنة متوافقة الإصدار مع نسخة عمل المضيف.

Pinned npm installs

بالنسبة إلى تثبيتات npm المثبتة بإصدار محدد، احتفظ بالإصدار الدقيق في `npmSpec` وأضف سلامة الأثر المتوقعة:

jsonCopy code
[code]
    {  "openclaw": {    "install": {      "npmSpec": "@wecom/wecom-openclaw-plugin@1.2.3",      "expectedIntegrity": "sha512-REPLACE_WITH_NPM_DIST_INTEGRITY",      "defaultChoice": "npm"    }  }}
[/code]

allowInvalidConfigRecovery scope

لا يُعد `allowInvalidConfigRecovery` تجاوزًا عامًا للتهيئات المعطلة. إنه مخصص فقط لاسترداد Plugin المضمّن ضمن نطاق ضيق، بحيث يمكن لإعادة التثبيت/الإعداد إصلاح بقايا ترقية معروفة مثل مسار Plugin مضمّن مفقود أو إدخال `channels.<id>` قديم لذلك Plugin نفسه. إذا كانت التهيئة معطلة لأسباب غير ذات صلة، يظل التثبيت يفشل بإغلاق آمن ويطلب من المشغّل تشغيل `openclaw doctor --fix`.

### التحميل الكامل المؤجل

يمكن لـ Plugins القنوات اختيار التحميل المؤجل باستخدام:

jsonCopy code
[code]
    {  "openclaw": {    "extensions": ["./index.ts"],    "setupEntry": "./setup-entry.ts",    "startup": {      "deferConfiguredChannelFullLoadUntilAfterListen": true    }  }}
[/code]

عند التمكين، يحمّل OpenClaw فقط `setupEntry` أثناء مرحلة بدء التشغيل السابقة للاستماع، حتى للقنوات المهيأة مسبقًا. يتم تحميل الإدخال الكامل بعد أن يبدأ Gateway بالاستماع.

إذا كان إدخال الإعداد/الإدخال الكامل لديك يسجّل طرق RPC في Gateway، فأبقها ضمن بادئة خاصة بـ Plugin. تظل مساحات أسماء الإدارة الأساسية المحجوزة (`config.*`، و`exec.approvals.*`، و`wizard.*`، و`update.*`) مملوكة للنواة وتُحل دائمًا إلى `operator.admin`.

## البيان التعريفي لـ Plugin

يجب أن يشحن كل Plugin أصلي ملف `openclaw.plugin.json` في جذر الحزمة. يستخدم OpenClaw هذا الملف للتحقق من التهيئة دون تنفيذ كود Plugin.

jsonCopy code
[code]
    {  "id": "my-plugin",  "name": "My Plugin",  "description": "Adds My Plugin capabilities to OpenClaw",  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {      "webhookSecret": {        "type": "string",        "description": "Webhook verification secret"      }    }  }}
[/code]

بالنسبة إلى Plugins القنوات، أضف `kind` و`channels`:

jsonCopy code
[code]
    {  "id": "my-channel",  "kind": "channel",  "channels": ["my-channel"],  "configSchema": {    "type": "object",    "additionalProperties": false,    "properties": {}  }}
[/code]

حتى Plugins التي لا تحتوي على تهيئة يجب أن تشحن مخططًا. المخطط الفارغ صالح:

jsonCopy code
[code]
    {  "id": "my-plugin",  "configSchema": {    "type": "object",    "additionalProperties": false  }}
[/code]

راجع [البيان التعريفي لـ Plugin](</ar/plugins/manifest>) للاطلاع على مرجع المخطط الكامل.

## النشر على ClawHub

بالنسبة إلى حزم Plugin، استخدم أمر ClawHub الخاص بالحزمة:

bashCopy code
[code]
    clawhub package publish your-org/your-plugin --dry-runclawhub package publish your-org/your-plugin
[/code]

## إدخال الإعداد

ملف `setup-entry.ts` هو بديل خفيف لـ `index.ts` يحمّله OpenClaw عندما يحتاج فقط إلى أسطح الإعداد (التهيئة الأولية، إصلاح الإعدادات، فحص القناة المعطّلة).

typescriptCopy code
[code]
    // setup-entry.ts  export default defineSetupPluginEntry(myChannelPlugin);
[/code]

يتجنب هذا تحميل كود وقت التشغيل الثقيل (مكتبات التشفير، تسجيلات CLI، خدمات الخلفية) أثناء تدفقات الإعداد.

يمكن لقنوات مساحة العمل المضمّنة التي تحتفظ بتصديرات آمنة للإعداد في وحدات جانبية استخدام `defineBundledChannelSetupEntry(...)` من `openclaw/plugin-sdk/channel-entry-contract` بدلًا من `defineSetupPluginEntry(...)`. يدعم ذلك العقد المضمّن أيضًا تصدير `runtime` اختياريًا بحيث تبقى وصلات وقت التشغيل أثناء الإعداد خفيفة وصريحة.

متى يستخدم OpenClaw setupEntry بدلًا من الإدخال الكامل

  * تكون القناة معطّلة لكنها تحتاج إلى أسطح الإعداد/التهيئة الأولية.
  * تكون القناة مفعّلة لكنها غير مهيأة.
  * يكون التحميل المؤجل مفعّلًا (`deferConfiguredChannelFullLoadUntilAfterListen`).

ما الذي يجب أن يسجله setupEntry

  * كائن Channel Plugin (عبر `defineSetupPluginEntry`).
  * أي مسارات HTTP مطلوبة قبل استماع Gateway.
  * أي أساليب Gateway مطلوبة أثناء بدء التشغيل.


يجب أن تتجنب أساليب Gateway عند بدء التشغيل هذه أيضًا مساحات أسماء الإدارة الأساسية المحجوزة مثل `config.*` أو `update.*`.

ما الذي ينبغي ألا يتضمنه setupEntry

  * تسجيلات CLI.
  * خدمات الخلفية.
  * استيرادات وقت التشغيل الثقيلة (التشفير، SDKs).
  * أساليب Gateway التي لا تكون مطلوبة إلا بعد بدء التشغيل.


### استيرادات مساعدي الإعداد الضيقة

بالنسبة للمسارات الساخنة الخاصة بالإعداد فقط، فضّل منافذ مساعدي الإعداد الضيقة على مظلة `plugin-sdk/setup` الأوسع عندما لا تحتاج إلا إلى جزء من سطح الإعداد:

مسار الاستيراد | استخدمه من أجل | التصديرات الرئيسية  
---|---|---  
`plugin-sdk/setup-runtime` | مساعدو وقت التشغيل أثناء الإعداد الذين يبقون متاحين في `setupEntry` / بدء تشغيل القناة المؤجل | `createPatchedAccountSetupAdapter`, `createEnvPatchedAccountSetupAdapter`, `createSetupInputPresenceValidator`, `noteChannelLookupFailure`, `noteChannelLookupSummary`, `promptResolvedAllowFrom`, `splitSetupEntries`, `createAllowlistSetupWizardProxy`, `createDelegatedSetupWizardProxy`  
`plugin-sdk/setup-adapter-runtime` | اسم مستعار متوافق مهجور؛ استخدم `plugin-sdk/setup-runtime` | `createEnvPatchedAccountSetupAdapter`  
`plugin-sdk/setup-tools` | مساعدو CLI/الأرشيف/المستندات للإعداد/التثبيت | `formatCliCommand`, `detectBinary`, `extractArchive`, `resolveBrewExecutable`, `formatDocsLink`, `CONFIG_DIR`  
  
استخدم منفذ `plugin-sdk/setup` الأوسع عندما تريد صندوق أدوات الإعداد المشترك الكامل، بما في ذلك مساعدو تصحيح الإعدادات مثل `moveSingleAccountChannelSectionToDefaultAccount(...)`.

تبقى محولات تصحيح الإعداد آمنة للمسارات الساخنة عند الاستيراد. يكون البحث في سطح عقد ترقية الحساب الواحد المضمّن كسولًا، لذلك لا يؤدي استيراد `plugin-sdk/setup-runtime` إلى تحميل اكتشاف سطح العقد المضمّن مسبقًا قبل استخدام المحول فعليًا.

### ترقية الحساب الواحد المملوكة للقناة

عندما ترقّي قناة إعدادًا علويًا ذا حساب واحد إلى `channels.<id>.accounts.*`، يكون السلوك المشترك الافتراضي هو نقل القيم المرقّاة ذات نطاق الحساب إلى `accounts.default`.

يمكن للقنوات المضمّنة تضييق تلك الترقية أو تجاوزها عبر سطح عقد الإعداد الخاص بها:

  * `singleAccountKeysToMove`: مفاتيح علوية إضافية ينبغي نقلها إلى الحساب المرقّى
  * `namedAccountPromotionKeys`: عندما تكون الحسابات المسماة موجودة بالفعل، تُنقل هذه المفاتيح فقط إلى الحساب المرقّى؛ وتبقى مفاتيح السياسة/التسليم المشتركة في جذر القناة
  * `resolveSingleAccountPromotionTarget(...)`: اختيار الحساب الحالي الذي يتلقى القيم المرقّاة


## مخطط الإعدادات

يُتحقق من إعدادات Plugin مقابل JSON Schema في البيان الخاص بك. يهيئ المستخدمون Plugins عبر:

json5Copy code
[code]
    {  plugins: {    entries: {      "my-plugin": {        config: {          webhookSecret: "abc123",        },      },    },  },}
[/code]

يتلقى Plugin هذا الإعداد باسم `api.pluginConfig` أثناء التسجيل.

بالنسبة للإعداد الخاص بالقناة، استخدم قسم إعداد القناة بدلًا من ذلك:

json5Copy code
[code]
    {  channels: {    "my-channel": {      token: "bot-token",      allowFrom: ["user1", "user2"],    },  },}
[/code]

### بناء مخططات إعداد القناة

استخدم `buildChannelConfigSchema` لتحويل مخطط Zod إلى غلاف `ChannelConfigSchema` المستخدم بواسطة عناصر الإعدادات المملوكة لـ Plugin:

typescriptCopy code
[code]
      const accountSchema = z.object({  token: z.string().optional(),  allowFrom: z.array(z.string()).optional(),  accounts: z.object({}).catchall(z.any()).optional(),  defaultAccount: z.string().optional(),}); const configSchema = buildChannelConfigSchema(accountSchema);
[/code]

إذا كنت تؤلف العقد بالفعل بوصفه JSON Schema أو TypeBox، فاستخدم المساعد المباشر حتى يتمكن OpenClaw من تخطي تحويل Zod إلى JSON-Schema في مسارات البيانات الوصفية:

typescriptCopy code
[code]
      const configSchema = buildJsonChannelConfigSchema(  Type.Object({    token: Type.Optional(Type.String()),    allowFrom: Type.Optional(Type.Array(Type.String())),  }),);
[/code]

بالنسبة لـ Plugins التابعة لأطراف ثالثة، يظل عقد المسار البارد هو بيان Plugin: انسخ JSON Schema المُنشأ إلى `openclaw.plugin.json#channelConfigs` بحيث يمكن لأسطح مخطط الإعدادات، والإعداد، والواجهة فحص `channels.<id>` دون تحميل كود وقت التشغيل.

## معالجات الإعداد

يمكن لـ Channel Plugins توفير معالجات إعداد تفاعلية لـ `openclaw onboard`. المعالج هو كائن `ChannelSetupWizard` على `ChannelPlugin`:

typescriptCopy code
[code]
     const setupWizard: ChannelSetupWizard = {  channel: "my-channel",  status: {    configuredLabel: "Connected",    unconfiguredLabel: "Not configured",    resolveConfigured: ({ cfg }) => Boolean((cfg.channels as any)?.["my-channel"]?.token),  },  credentials: [    {      inputKey: "token",      providerHint: "my-channel",      credentialLabel: "Bot token",      preferredEnvVar: "MY_CHANNEL_BOT_TOKEN",      envPrompt: "Use MY_CHANNEL_BOT_TOKEN from environment?",      keepPrompt: "Keep current token?",      inputPrompt: "Enter your bot token:",      inspect: ({ cfg, accountId }) => {        const token = (cfg.channels as any)?.["my-channel"]?.token;        return {          accountConfigured: Boolean(token),          hasConfiguredValue: Boolean(token),        };      },    },  ],};
[/code]

يدعم نوع `ChannelSetupWizard` كلًا من `credentials` و`textInputs` و`dmPolicy` و`allowFrom` و`groupAccess` و`prepare` و`finalize` والمزيد. راجع حزم Plugin المضمّنة (على سبيل المثال Plugin الخاص بـ Discord في `src/channel.setup.ts`) للحصول على أمثلة كاملة.

مطالبات allowFrom المشتركة

بالنسبة لمطالبات قائمة السماح في الرسائل المباشرة التي لا تحتاج إلا إلى التدفق القياسي `note -> prompt -> parse -> merge -> patch`، فضّل مساعدي الإعداد المشتركين من `openclaw/plugin-sdk/setup`: `createPromptParsedAllowFromForAccount(...)`، و`createTopLevelChannelParsedAllowFromPrompt(...)`، و`createNestedChannelParsedAllowFromPrompt(...)`.

حالة إعداد القناة القياسية

بالنسبة لكتل حالة إعداد القناة التي لا تختلف إلا بالملصقات والدرجات والسطور الإضافية الاختيارية، فضّل `createStandardChannelSetupStatus(...)` من `openclaw/plugin-sdk/setup` بدلًا من إنشاء كائن `status` نفسه يدويًا في كل Plugin.

سطح إعداد القناة الاختياري

بالنسبة لأسطح الإعداد الاختيارية التي ينبغي أن تظهر فقط في سياقات معينة، استخدم `createOptionalChannelSetupSurface` من `openclaw/plugin-sdk/channel-setup`:

typescriptCopy code
[code]
    import { createOptionalChannelSetupSurface } from "openclaw/plugin-sdk/channel-setup"; const setupSurface = createOptionalChannelSetupSurface({  channel: "my-channel",  label: "My Channel",  npmSpec: "@myorg/openclaw-my-channel",  docsPath: "/channels/my-channel",});// Returns { setupAdapter, setupWizard }
[/code]

يعرّض `plugin-sdk/channel-setup` أيضًا بنّاءي المستوى الأدنى `createOptionalChannelSetupAdapter(...)` و`createOptionalChannelSetupWizard(...)` عندما لا تحتاج إلا إلى نصف واحد من سطح التثبيت الاختياري ذلك.

يفشل المحول/المعالج الاختياري المُنشأ بإغلاق عند عمليات كتابة الإعدادات الحقيقية. يعيدان استخدام رسالة واحدة تفيد بأن التثبيت مطلوب عبر `validateInput` و`applyAccountConfig` و`finalize`، ويضيفان رابط مستندات عندما يكون `docsPath` مضبوطًا.

مساعدو الإعداد المدعومون بملفات تنفيذية

بالنسبة لواجهات إعداد مدعومة بملفات تنفيذية، فضّل المساعدين المشتركين المفوضين بدلًا من نسخ غراء الملف التنفيذي/الحالة نفسه إلى كل قناة:

  * `createDetectedBinaryStatus(...)` لكتل الحالة التي لا تختلف إلا بالملصقات والتلميحات والدرجات واكتشاف الملف التنفيذي
  * `createCliPathTextInput(...)` لمدخلات النص المدعومة بمسار
  * `createDelegatedSetupWizardStatusResolvers(...)`، و`createDelegatedPrepare(...)`، و`createDelegatedFinalize(...)`، و`createDelegatedResolveConfigured(...)` عندما يحتاج `setupEntry` إلى التمرير إلى معالج كامل أثقل بشكل كسول
  * `createDelegatedTextInputShouldPrompt(...)` عندما يحتاج `setupEntry` فقط إلى تفويض قرار `textInputs[*].shouldPrompt`


## النشر والتثبيت

**Plugins الخارجية:** انشر إلى [ClawHub](</ar/clawhub>)، ثم ثبّت:

### npm

bashCopy code
[code]
    openclaw plugins install @myorg/openclaw-my-plugin
[/code]

تُثبَّت مواصفات الحزم المجردة من npm أثناء انتقال الإطلاق.

### ClawHub فقط

bashCopy code
[code]
    openclaw plugins install clawhub:@myorg/openclaw-my-plugin
[/code]

### مواصفة حزمة npm

استخدم npm عندما لا تكون الحزمة قد انتقلت إلى ClawHub بعد، أو عندما تحتاج إلى مسار تثبيت npm مباشر أثناء الترحيل:

bashCopy code
[code]
    openclaw plugins install npm:@myorg/openclaw-my-plugin
[/code]

**Plugins داخل المستودع:** ضعها ضمن شجرة مساحة عمل Plugin المضمّنة، وسيتم اكتشافها تلقائيًا أثناء البناء.

**يمكن للمستخدمين التثبيت:**

bashCopy code
[code]
    openclaw plugins install <package-name>
[/code]

بيانات تعريف الحزمة المضمّنة صريحة، وليست مستنتجة من JavaScript المبني عند بدء تشغيل Gateway. تبعيات وقت التشغيل تنتمي إلى حزمة Plugin التي تملكها؛ ولا يقوم بدء تشغيل OpenClaw المعبأ أبدًا بإصلاح تبعيات Plugin أو نسخها.

## ذات صلة

  * [بناء Plugins](</ar/plugins/building-plugins>) — دليل بدء خطوة بخطوة
  * [بيان Plugin](</ar/plugins/manifest>) — مرجع مخطط البيان الكامل
  * [نقاط دخول SDK](</ar/plugins/sdk-entrypoints>) — `definePluginEntry` و `defineChannelPluginEntry`


Was this useful?YesNo