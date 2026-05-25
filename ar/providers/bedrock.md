---
title: Amazon Bedrock
source_url: https://docs.openclaw.ai/ar/providers/bedrock
scraped_at: 2026-05-25
---

يمكن لـ OpenClaw استخدام نماذج **Amazon Bedrock** عبر مزوّد البث **Bedrock Converse** من pi-ai. تستخدم مصادقة Bedrock **سلسلة بيانات الاعتماد الافتراضية في AWS SDK** ، وليس مفتاح API.

الخاصية | القيمة  
---|---  
المزوّد | `amazon-bedrock`  
API | `bedrock-converse-stream`  
المصادقة | بيانات اعتماد AWS (متغيرات البيئة، التكوين المشترك، أو دور المثيل)  
المنطقة | `AWS_REGION` أو `AWS_DEFAULT_REGION` (الافتراضي: `us-east-1`)  
  
## بدء الاستخدام

اختر طريقة المصادقة المفضلة لديك واتبع خطوات الإعداد.

### Access keys / env vars

**الأفضل لـ:** أجهزة المطورين، وCI، أو المضيفين حيث تدير بيانات اعتماد AWS مباشرة.

* ### Set AWS credentials on the gateway host

bashCopy code
[code]
    export AWS_ACCESS_KEY_ID="AKIA..."export AWS_SECRET_ACCESS_KEY="..."export AWS_REGION="us-east-1"# Optional:export AWS_SESSION_TOKEN="..."export AWS_PROFILE="your-profile"# Optional (Bedrock API key/bearer token):export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

* ### Add a Bedrock provider and model to your config

لا يلزم وجود `apiKey`. اضبط المزوّد باستخدام `auth: "aws-sdk"`:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock": {        baseUrl: "https://bedrock-runtime.us-east-1.amazonaws.com",        api: "bedrock-converse-stream",        auth: "aws-sdk",        models: [          {            id: "us.anthropic.claude-opus-4-6-v1:0",            name: "Claude Opus 4.6 (Bedrock)",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "amazon-bedrock/us.anthropic.claude-opus-4-6-v1:0" },    },  },}
[/code]

* ### Verify models are available

bashCopy code
[code]
    openclaw models list
[/code]

### EC2 instance roles (IMDS)

**الأفضل لـ:** مثيلات EC2 التي لديها دور IAM مرفق، باستخدام خدمة بيانات تعريف المثيل للمصادقة.

* ### Enable discovery explicitly

عند استخدام IMDS، لا يستطيع OpenClaw اكتشاف مصادقة AWS من علامات البيئة وحدها، لذلك يجب أن تشترك صراحة:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1
[/code]

* ### Optionally add an env marker for auto mode

إذا كنت تريد أيضاً أن يعمل مسار الاكتشاف التلقائي عبر علامة البيئة (على سبيل المثال، لأسطح `openclaw status`):

bashCopy code
[code]
    export AWS_PROFILE=defaultexport AWS_REGION=us-east-1
[/code]

لا تحتاج إلى مفتاح API مزيف.

* ### Verify models are discovered

bashCopy code
[code]
    openclaw models list
[/code]

## الاكتشاف التلقائي للنماذج

يمكن لـ OpenClaw اكتشاف نماذج Bedrock التي تدعم **البث** و**إخراج النص** تلقائياً. يستخدم الاكتشاف `bedrock:ListFoundationModels` و `bedrock:ListInferenceProfiles`، وتُخزّن النتائج مؤقتاً (الافتراضي: ساعة واحدة).

كيفية تفعيل المزوّد الضمني:

  * إذا كانت `plugins.entries.amazon-bedrock.config.discovery.enabled` تساوي `true`، فسيحاول OpenClaw الاكتشاف حتى عند عدم وجود علامة بيئة AWS.
  * إذا كانت `plugins.entries.amazon-bedrock.config.discovery.enabled` غير مضبوطة، يضيف OpenClaw تلقائياً مزوّد Bedrock الضمني فقط عندما يرى إحدى علامات مصادقة AWS هذه: `AWS_BEARER_TOKEN_BEDROCK`، أو `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`، أو `AWS_PROFILE`.
  * لا يزال مسار مصادقة وقت تشغيل Bedrock الفعلي يستخدم سلسلة AWS SDK الافتراضية، لذلك يمكن للتكوين المشترك وSSO ومصادقة دور مثيل IMDS أن تعمل حتى عندما احتاج الاكتشاف إلى `enabled: true` للاشتراك.


Discovery config options

توجد خيارات التكوين ضمن `plugins.entries.amazon-bedrock.config.discovery`:

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          discovery: {            enabled: true,            region: "us-east-1",            providerFilter: ["anthropic", "amazon"],            refreshInterval: 3600,            defaultContextWindow: 32000,            defaultMaxTokens: 4096,          },        },      },    },  },}
[/code]

الخيار | الافتراضي | الوصف  
---|---|---  
`enabled` | auto | في الوضع التلقائي، يفعّل OpenClaw مزوّد Bedrock الضمني فقط عندما يرى علامة بيئة AWS مدعومة. اضبطه على `true` لفرض الاكتشاف.  
`region` | `AWS_REGION` / `AWS_DEFAULT_REGION` / `us-east-1` | منطقة AWS المستخدمة لاستدعاءات API الخاصة بالاكتشاف.  
`providerFilter` | (الكل) | يطابق أسماء مزوّدي Bedrock (على سبيل المثال `anthropic`، `amazon`).  
`refreshInterval` | `3600` | مدة التخزين المؤقت بالثواني. اضبطها على `0` لتعطيل التخزين المؤقت.  
`defaultContextWindow` | `32000` | نافذة السياق المستخدمة للنماذج المكتشفة (تجاوزها إذا كنت تعرف حدود نموذجك).  
`defaultMaxTokens` | `4096` | الحد الأقصى لرموز الإخراج المستخدمة للنماذج المكتشفة (تجاوزها إذا كنت تعرف حدود نموذجك).  
  
## إعداد سريع (مسار AWS)

تنشئ هذه الجولة الإرشادية دور IAM، وتُرفق أذونات Bedrock، وتربط ملف تعريف المثيل، وتفعّل اكتشاف OpenClaw على مضيف EC2.

bashCopy code
[code]
    # 1. Create IAM role and instance profileaws iam create-role --role-name EC2-Bedrock-Access \  --assume-role-policy-document '{    "Version": "2012-10-17",    "Statement": [{      "Effect": "Allow",      "Principal": {"Service": "ec2.amazonaws.com"},      "Action": "sts:AssumeRole"    }]  }' aws iam attach-role-policy --role-name EC2-Bedrock-Access \  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess aws iam create-instance-profile --instance-profile-name EC2-Bedrock-Accessaws iam add-role-to-instance-profile \  --instance-profile-name EC2-Bedrock-Access \  --role-name EC2-Bedrock-Access # 2. Attach to your EC2 instanceaws ec2 associate-iam-instance-profile \  --instance-id i-xxxxx \  --iam-instance-profile Name=EC2-Bedrock-Access # 3. On the EC2 instance, enable discovery explicitlyopenclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1 # 4. Optional: add an env marker if you want auto mode without explicit enableecho 'export AWS_PROFILE=default' >> ~/.bashrcecho 'export AWS_REGION=us-east-1' >> ~/.bashrcsource ~/.bashrc # 5. Verify models are discoveredopenclaw models list
[/code]

## التكوين المتقدم

Inference profiles

يكتشف OpenClaw **ملفات تعريف الاستدلال الإقليمية والعالمية** إلى جانب نماذج الأساس. عندما يشير ملف تعريف إلى نموذج أساس معروف، يرث ملف التعريف قدرات ذلك النموذج (نافذة السياق، والحد الأقصى للرموز، والاستدلال، والرؤية)، وتُحقن منطقة طلب Bedrock الصحيحة تلقائياً. يعني ذلك أن ملفات تعريف Claude العابرة للمناطق تعمل دون تجاوزات يدوية للمزوّد.

تبدو معرّفات ملفات تعريف الاستدلال مثل `us.anthropic.claude-opus-4-6-v1:0` (إقليمي) أو `anthropic.claude-opus-4-6-v1:0` (عالمي). إذا كان النموذج الداعم موجوداً بالفعل في نتائج الاكتشاف، يرث ملف التعريف مجموعة قدراته الكاملة؛ وإلا فتُطبق افتراضيات آمنة.

لا يلزم أي تكوين إضافي. ما دام الاكتشاف مفعلاً وكان لدى كيان IAM الأساسي `bedrock:ListInferenceProfiles`، تظهر ملفات التعريف إلى جانب نماذج الأساس في `openclaw models list`.

Service tier

تدعم بعض نماذج Bedrock معامل `service_tier` لتحسين التكلفة أو زمن الاستجابة. تتوفر المستويات التالية:

المستوى | الوصف  
---|---  
`default` | مستوى Bedrock القياسي  
`flex` | معالجة مخفضة التكلفة لأعباء العمل التي يمكنها تحمل زمن استجابة أطول  
`priority` | معالجة ذات أولوية لأعباء العمل الحساسة لزمن الاستجابة  
`reserved` | سعة محجوزة لأعباء العمل المستقرة  
  
اضبط `serviceTier` (أو `service_tier`) عبر `agents.defaults.params` لطلبات نماذج Bedrock، أو لكل نموذج في `agents.defaults.models["<model-key>"].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      params: {        serviceTier: "flex", // applies to all models      },      models: {        "amazon-bedrock/mistral.mistral-large-3-675b-instruct": {          params: {            serviceTier: "priority", // per-model override          },        },      },    },  },}
[/code]

القيم الصالحة هي `default` و`flex` و`priority` و`reserved`. لا تدعم كل النماذج جميع المستويات — إذا طُلب مستوى غير مدعوم، فستُرجع Bedrock خطأ تحقق. ملاحظة: رسالة الخطأ مضللة إلى حد ما؛ قد تقول "The provided model identifier is invalid" بدلاً من الإشارة إلى مستوى خدمة غير مدعوم. إذا رأيت هذا الخطأ، فتحقق مما إذا كان النموذج يدعم المستوى المطلوب.

Claude Opus 4.7 temperature

ترفض Bedrock معامل `temperature` لـ Claude Opus 4.7. يحذف OpenClaw `temperature` تلقائياً لأي مرجع Bedrock خاص بـ Opus 4.7، بما في ذلك معرّفات نماذج الأساس، وملفات تعريف الاستدلال المسماة، وملفات تعريف استدلال التطبيقات التي يُحل نموذجها الأساسي إلى Opus 4.7 عبر `bedrock:GetInferenceProfile`، ومتغيرات `opus-4.7` المنقطة ذات بادئات المناطق الاختيارية (`us.`، `eu.`، `ap.`، `apac.`، `au.`، `jp.`، `global.`). لا يلزم مقبض تكوين، وينطبق الحذف على كل من كائن خيارات الطلب وحقل الحمولة `inferenceConfig`.

حواجز الحماية

يمكنك تطبيق [حواجز حماية Amazon Bedrock](<https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>) على جميع استدعاءات نماذج Bedrock بإضافة كائن `guardrail` إلى إعدادات Plugin `amazon-bedrock`. تتيح لك حواجز الحماية فرض ترشيح المحتوى، ورفض الموضوعات، ومرشحات الكلمات، ومرشحات المعلومات الحساسة، وفحوصات الارتكاز السياقي.

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          guardrail: {            guardrailIdentifier: "abc123", // guardrail ID or full ARN            guardrailVersion: "1", // version number or "DRAFT"            streamProcessingMode: "sync", // optional: "sync" or "async"            trace: "enabled", // optional: "enabled", "disabled", or "enabled_full"          },        },      },    },  },}
[/code]

الخيار | مطلوب | الوصف  
---|---|---  
`guardrailIdentifier` | نعم | معرّف حاجز الحماية (مثل `abc123`) أو ARN الكامل (مثل `arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123`).  
`guardrailVersion` | نعم | رقم الإصدار المنشور، أو `"DRAFT"` لمسودة العمل.  
`streamProcessingMode` | لا | `"sync"` أو `"async"` لتقييم حاجز الحماية أثناء البث. إذا حُذف، يستخدم Bedrock الإعداد الافتراضي الخاص به.  
`trace` | لا | `"enabled"` أو `"enabled_full"` لأغراض التصحيح؛ احذفه أو عيّنه إلى `"disabled"` للإنتاج.  
التضمينات للبحث في الذاكرة

يمكن أن يعمل Bedrock أيضًا بوصفه مزوّد التضمينات لـ [البحث في الذاكرة](</ar/concepts/memory-search>). يُضبط هذا بشكل منفصل عن مزوّد الاستدلال -- عيّن `agents.defaults.memorySearch.provider` إلى `"bedrock"`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0", // default      },    },  },}
[/code]

تستخدم تضمينات Bedrock سلسلة بيانات اعتماد AWS SDK نفسها التي يستخدمها الاستدلال (أدوار المثيلات، وSSO، ومفاتيح الوصول، والإعدادات المشتركة، وهوية الويب). لا حاجة إلى مفتاح API. عندما تكون قيمة `provider` هي `"auto"`، يُكتشف Bedrock تلقائيًا إذا تم حلّ سلسلة بيانات الاعتماد تلك بنجاح.

تشمل نماذج التضمين المدعومة Amazon Titan Embed (v1, v2)، وAmazon Nova Embed، وCohere Embed (v3, v4)، وTwelveLabs Marengo. راجع [مرجع إعدادات الذاكرة -- Bedrock](</ar/reference/memory-config#bedrock-embedding-config>) للاطلاع على قائمة النماذج الكاملة وخيارات الأبعاد.

ملاحظات ومحاذير

  * يتطلب Bedrock تفعيل **الوصول إلى النماذج** في حساب/منطقة AWS لديك.
  * يحتاج الاكتشاف التلقائي إلى صلاحيتي `bedrock:ListFoundationModels` و `bedrock:ListInferenceProfiles`.
  * إذا كنت تعتمد على الوضع التلقائي، فعيّن إحدى علامات بيئة مصادقة AWS المدعومة على مضيف Gateway. إذا كنت تفضّل مصادقة IMDS/الإعدادات المشتركة من دون علامات بيئة، فعيّن `plugins.entries.amazon-bedrock.config.discovery.enabled: true`.
  * يعرض OpenClaw مصدر بيانات الاعتماد بهذا الترتيب: `AWS_BEARER_TOKEN_BEDROCK`, ثم `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`، ثم `AWS_PROFILE`، ثم سلسلة AWS SDK الافتراضية.
  * يعتمد دعم الاستدلال على النموذج؛ راجع بطاقة نموذج Bedrock لمعرفة القدرات الحالية.
  * إذا كنت تفضّل تدفق مفتاح مُدارًا، يمكنك أيضًا وضع وكيل متوافق مع OpenAI أمام Bedrock وإعداده بوصفه مزوّد OpenAI بدلًا من ذلك.


## ذو صلة

[**اختيار النموذج** اختيار المزوّدين، ومراجع النماذج، وسلوك تجاوز الفشل. ](</ar/concepts/model-providers>) [**البحث في الذاكرة** تضمينات Bedrock لإعداد البحث في الذاكرة. ](</ar/concepts/memory-search>) [**مرجع إعدادات الذاكرة** قائمة نماذج تضمين Bedrock الكاملة وخيارات الأبعاد. ](</ar/reference/memory-config#bedrock-embedding-config>) [**استكشاف الأخطاء وإصلاحها** استكشاف الأخطاء وإصلاحها العام والأسئلة الشائعة. ](</ar/help/troubleshooting>)

Was this useful?YesNo