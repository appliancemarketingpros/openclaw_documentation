---
title: MCP
source_url: https://docs.openclaw.ai/ar/cli/mcp
scraped_at: 2026-05-25
---

`openclaw mcp` له مهمتان:

  * تشغيل OpenClaw كخادم MCP باستخدام `openclaw mcp serve`
  * إدارة تعريفات خوادم MCP الصادرة المملوكة لـ OpenClaw باستخدام `list` و`show` و`set` و`unset`


بعبارة أخرى:

  * `serve` يعني أن OpenClaw يعمل كخادم MCP
  * `list` / `show` / `set` / `unset` تعني أن OpenClaw يعمل كسجل من جهة عميل MCP لخوادم MCP أخرى قد تستهلكها بيئات التشغيل الخاصة به لاحقًا


استخدم [`openclaw acp`](</ar/cli/acp>) عندما ينبغي لـ OpenClaw استضافة جلسة حاضنة ترميز بنفسه وتوجيه بيئة التشغيل تلك عبر ACP.

## OpenClaw كخادم MCP

هذا هو مسار `openclaw mcp serve`.

### متى تستخدم `serve`

استخدم `openclaw mcp serve` عندما:

  * ينبغي لـ Codex أو Claude Code أو عميل MCP آخر التحدث مباشرة إلى محادثات القنوات المدعومة من OpenClaw
  * لديك بالفعل Gateway محلي أو بعيد لـ OpenClaw مع جلسات موجهة
  * تريد خادم MCP واحدًا يعمل عبر خلفيات قنوات OpenClaw بدلًا من تشغيل جسور منفصلة لكل قناة


استخدم [`openclaw acp`](</ar/cli/acp>) بدلًا من ذلك عندما ينبغي لـ OpenClaw استضافة بيئة تشغيل الترميز بنفسه وإبقاء جلسة الوكيل داخل OpenClaw.

### آلية العمل

يبدأ `openclaw mcp serve` خادم MCP عبر stdio. يملك عميل MCP تلك العملية. ما دام العميل يبقي جلسة stdio مفتوحة، يتصل الجسر بـ Gateway محلي أو بعيد لـ OpenClaw عبر WebSocket ويعرض محادثات القنوات الموجهة عبر MCP.

* ### ينشئ العميل الجسر

ينشئ عميل MCP العملية `openclaw mcp serve`.

* ### يتصل الجسر بـ Gateway

يتصل الجسر بـ OpenClaw Gateway عبر WebSocket.

* ### تصبح الجلسات محادثات MCP

تصبح الجلسات الموجهة محادثات MCP وأدوات نصوص/سجل.

* ### تصطف الأحداث الحية في طابور

تُضاف الأحداث الحية إلى طابور في الذاكرة أثناء اتصال الجسر.

* ### دفع Claude اختياري

إذا كان وضع قناة Claude مفعّلًا، يمكن للجلسة نفسها أيضًا تلقي إشعارات دفع خاصة بـ Claude.

سلوك مهم

  * تبدأ حالة الطابور الحي عند اتصال الجسر
  * يُقرأ سجل النصوص الأقدم باستخدام `messages_read`
  * لا توجد إشعارات دفع Claude إلا أثناء بقاء جلسة MCP نشطة
  * عند قطع اتصال العميل، يخرج الجسر ويختفي الطابور الحي
  * نقاط دخول الوكيل أحادية التشغيل مثل `openclaw agent` و`openclaw infer model run` تنهي أي بيئات تشغيل MCP مضمّنة تفتحها عند اكتمال الرد، لذلك لا تتراكم عمليات stdio MCP الفرعية عند التشغيل النصي المتكرر
  * تُفكك خوادم stdio MCP التي يشغلها OpenClaw (المضمّنة أو المكوّنة من المستخدم) كشجرة عمليات عند الإيقاف، لذلك لا تبقى العمليات الفرعية التي يبدأها الخادم بعد خروج عميل stdio الأب
  * حذف جلسة أو إعادة تعيينها يتخلص من عملاء MCP لتلك الجلسة عبر مسار التنظيف المشترك لبيئة التشغيل، لذلك لا تبقى اتصالات stdio عالقة مرتبطة بجلسة محذوفة


### اختر وضع عميل

استخدم الجسر نفسه بطريقتين مختلفتين:

### عملاء MCP عامون

أدوات MCP القياسية فقط. استخدم `conversations_list` و`messages_read` و`events_poll` و`events_wait` و`messages_send` وأدوات الموافقة.

### Claude Code

أدوات MCP القياسية إضافة إلى محول قناة Claude الخاص. فعّل `--claude-channel-mode on` أو اترك القيمة الافتراضية `auto`.

### ما يعرضه `serve`

يستخدم الجسر بيانات وصف مسارات جلسات Gateway الموجودة لعرض المحادثات المدعومة بالقنوات. تظهر محادثة عندما يكون لدى OpenClaw بالفعل حالة جلسة ذات مسار معروف مثل:

  * `channel`
  * بيانات وصف المستلم أو الوجهة
  * `accountId` اختياري
  * `threadId` اختياري


يوفر ذلك لعملاء MCP مكانًا واحدًا من أجل:

  * سرد المحادثات الموجهة الحديثة
  * قراءة سجل النصوص الحديث
  * انتظار أحداث واردة جديدة
  * إرسال رد عبر المسار نفسه
  * رؤية طلبات الموافقة التي تصل أثناء اتصال الجسر


### الاستخدام

### Gateway محلي

bashCopy code
[code]
    openclaw mcp serve
[/code]

### Gateway بعيد (رمز)

bashCopy code
[code]
    openclaw mcp serve --url wss://gateway-host:18789 --token-file ~/.openclaw/gateway.token
[/code]

### Gateway بعيد (كلمة مرور)

bashCopy code
[code]
    openclaw mcp serve --url wss://gateway-host:18789 --password-file ~/.openclaw/gateway.password
[/code]

### تفصيلي / إيقاف Claude

bashCopy code
[code]
    openclaw mcp serve --verboseopenclaw mcp serve --claude-channel-mode off
[/code]

### أدوات الجسر

يعرض الجسر الحالي أدوات MCP التالية:

conversations_list

يسرد المحادثات الحديثة المدعومة بجلسات والتي لديها بالفعل بيانات وصف للمسار في حالة جلسة Gateway.

عوامل تصفية مفيدة:

  * `limit`
  * `search`
  * `channel`
  * `includeDerivedTitles`
  * `includeLastMessage`

conversation_get

يعيد محادثة واحدة حسب `session_key` باستخدام بحث مباشر عن جلسة Gateway.

messages_read

يقرأ رسائل النصوص الحديثة لمحادثة واحدة مدعومة بجلسة.

attachments_fetch

يستخرج كتل محتوى الرسائل غير النصية من رسالة نصية واحدة. هذه طريقة عرض بيانات وصفية فوق محتوى النصوص، وليست مخزنًا مستقلًا ودائمًا لكائنات المرفقات.

events_poll

يقرأ الأحداث الحية الموضوعة في الطابور منذ مؤشر رقمي.

events_wait

يجري استقصاءً طويلًا حتى يصل الحدث التالي المطابق في الطابور أو تنتهي المهلة.

استخدم هذا عندما يحتاج عميل MCP عام إلى تسليم قريب من الوقت الفعلي دون بروتوكول دفع خاص بـ Claude.

messages_send

يرسل النص عبر المسار نفسه المسجل بالفعل في الجلسة.

السلوك الحالي:

  * يتطلب مسار محادثة موجودًا
  * يستخدم قناة الجلسة والمستلم ومعرف الحساب ومعرف السلسلة
  * يرسل نصًا فقط

permissions_list_open

يسرد طلبات الموافقة المعلقة على exec/Plugin التي لاحظها الجسر منذ اتصاله بـ Gateway.

permissions_respond

يحل طلب موافقة معلقًا واحدًا على exec/Plugin باستخدام:

  * `allow-once`
  * `allow-always`
  * `deny`


### نموذج الأحداث

يحتفظ الجسر بطابور أحداث في الذاكرة أثناء اتصاله.

أنواع الأحداث الحالية:

  * `message`
  * `exec_approval_requested`
  * `exec_approval_resolved`
  * `plugin_approval_requested`
  * `plugin_approval_resolved`
  * `claude_permission_request`


### إشعارات قناة Claude

يمكن للجسر أيضًا عرض إشعارات قناة خاصة بـ Claude. هذا هو مكافئ OpenClaw لمحول قناة Claude Code: تبقى أدوات MCP القياسية متاحة، لكن يمكن أن تصل الرسائل الواردة الحية أيضًا كإشعارات MCP خاصة بـ Claude.

### off

`--claude-channel-mode off`: أدوات MCP القياسية فقط.

### on

`--claude-channel-mode on`: تفعيل إشعارات قناة Claude.

### auto (الافتراضي)

`--claude-channel-mode auto`: القيمة الافتراضية الحالية؛ سلوك الجسر نفسه مثل `on`.

عند تفعيل وضع قناة Claude، يعلن الخادم عن قدرات Claude التجريبية ويمكنه إصدار:

  * `notifications/claude/channel`
  * `notifications/claude/channel/permission`


سلوك الجسر الحالي:

  * تُمرّر رسائل نصوص `user` الواردة كـ `notifications/claude/channel`
  * تُتبع طلبات إذن Claude المستلمة عبر MCP في الذاكرة
  * إذا أرسلت المحادثة المرتبطة لاحقًا `yes abcde` أو `no abcde`، يحول الجسر ذلك إلى `notifications/claude/channel/permission`
  * هذه الإشعارات خاصة بالجلسة الحية فقط؛ إذا قطع عميل MCP الاتصال، فلا يوجد هدف دفع


هذا مخصص للعميل عمدًا. ينبغي لعملاء MCP العامين الاعتماد على أدوات الاستقصاء القياسية.

### تكوين عميل MCP

مثال على تكوين عميل stdio:

jsonCopy code
[code]
    {  "mcpServers": {    "openclaw": {      "command": "openclaw",      "args": [        "mcp",        "serve",        "--url",        "wss://gateway-host:18789",        "--token-file",        "/path/to/gateway.token"      ]    }  }}
[/code]

بالنسبة إلى معظم عملاء MCP العامين، ابدأ بسطح الأدوات القياسي وتجاهل وضع Claude. شغّل وضع Claude فقط للعملاء الذين يفهمون فعليًا أساليب الإشعارات الخاصة بـ Claude.

### الخيارات

يدعم `openclaw mcp serve` ما يلي:

عنوان URL لـ Gateway WebSocket.

رمز Gateway.

قراءة الرمز من ملف.

كلمة مرور Gateway.

قراءة كلمة المرور من ملف.

وضع إشعارات Claude.

سجلات تفصيلية على stderr.

### الأمان وحدود الثقة

لا يخترع الجسر التوجيه. إنه يعرض فقط المحادثات التي يعرف Gateway بالفعل كيفية توجيهها.

هذا يعني:

  * قوائم السماح للمرسلين والاقتران والثقة على مستوى القناة لا تزال تابعة لتكوين قناة OpenClaw الأساسية
  * لا يمكن لـ `messages_send` الرد إلا عبر مسار مخزن موجود
  * حالة الموافقة حية/في الذاكرة فقط لجلسة الجسر الحالية
  * ينبغي لمصادقة الجسر استخدام عناصر تحكم رمز Gateway أو كلمة المرور نفسها التي تثق بها لأي عميل Gateway بعيد آخر


إذا كانت محادثة مفقودة من `conversations_list`، فغالبًا ليس السبب تكوين MCP. السبب هو فقدان بيانات وصف المسار أو عدم اكتمالها في جلسة Gateway الأساسية.

### الاختبار

يوفر OpenClaw اختبار دخان Docker حتميًا لهذا الجسر:

bashCopy code
[code]
    pnpm test:docker:mcp-channels
[/code]

اختبار الدخان هذا:

  * يبدأ حاوية Gateway مزروعة مسبقًا
  * يبدأ حاوية ثانية تنشئ `openclaw mcp serve`
  * يتحقق من اكتشاف المحادثات وقراءات النصوص وقراءات بيانات وصف المرفقات وسلوك طابور الأحداث الحية وتوجيه الإرسال الصادر
  * يتحقق من إشعارات القناة والأذونات بأسلوب Claude عبر جسر stdio MCP الحقيقي


هذه أسرع طريقة لإثبات أن الجسر يعمل دون توصيل حساب Telegram أو Discord أو iMessage حقيقي بتشغيل الاختبار.

لسياق اختبار أوسع، راجع [الاختبار](</ar/help/testing>).

### استكشاف الأخطاء وإصلاحها

لم تُرجع أي محادثات

يعني ذلك عادةً أن جلسة Gateway ليست قابلة للتوجيه بالفعل. تأكد من أن الجلسة الأساسية لديها بيانات وصف لمسار القناة/الموفر والمستلم والحساب/السلسلة الاختياريين.

يفوّت events_poll أو events_wait الرسائل الأقدم

متوقع. يبدأ الطابور الحي عندما يتصل الجسر. اقرأ سجل النصوص الأقدم باستخدام `messages_read`.

لا تظهر إشعارات Claude

تحقق من كل ما يلي:

  * أبقى العميل جلسة stdio MCP مفتوحة
  * `--claude-channel-mode` مضبوط على `on` أو `auto`
  * العميل يفهم فعليًا أساليب الإشعارات الخاصة بـ Claude
  * حدثت الرسالة الواردة بعد اتصال الجسر

الموافقات مفقودة

يعرض `permissions_list_open` فقط طلبات الموافقة التي لوحظت أثناء اتصال الجسر. إنه ليس واجهة API دائمة لسجل الموافقات.

## OpenClaw كسجل عميل MCP

هذا هو مسار `openclaw mcp list` و`show` و`set` و`unset`.

لا تعرض هذه الأوامر OpenClaw عبر MCP. إنها تدير تعريفات خادم MCP المملوكة لـ OpenClaw ضمن `mcp.servers` في إعدادات OpenClaw.

هذه التعريفات المحفوظة مخصصة لبيئات التشغيل التي يشغلها OpenClaw أو يهيئها لاحقا، مثل Pi المضمن ومحولات التشغيل الأخرى. يخزن OpenClaw التعريفات مركزيا حتى لا تحتاج بيئات التشغيل هذه إلى الاحتفاظ بقوائم خوادم MCP مكررة خاصة بها.

سلوك مهم

  * هذه الأوامر تقرأ إعدادات OpenClaw أو تكتبها فقط
  * لا تتصل بخادم MCP الهدف
  * لا تتحقق مما إذا كان الأمر أو عنوان URL أو النقل البعيد قابلا للوصول الآن
  * تقرر محولات التشغيل أشكال النقل التي تدعمها فعليا وقت التنفيذ
  * يعرض Pi المضمن أدوات MCP المهيأة في ملفات تعريف الأدوات العادية `coding` و`messaging`؛ لا يزال `minimal` يخفيها، ويعطلها `tools.deny: ["bundle-mcp"]` صراحة
  * تتم إزالة بيئات تشغيل MCP المضمنة محددة النطاق للجلسة بعد `mcp.sessionIdleTtlMs` مللي ثانية من وقت الخمول (الافتراضي 10 دقائق؛ اضبطها على `0` للتعطيل)، وتنظفها عمليات التشغيل المضمنة أحادية التنفيذ عند نهاية التشغيل


قد تطبع محولات التشغيل هذا السجل المشترك بالشكل الذي يتوقعه العميل اللاحق. على سبيل المثال، يستهلك Pi المضمن قيم `transport` في OpenClaw مباشرة، بينما يتلقى Claude Code وGemini قيم `type` الأصلية للـ CLI مثل `http` أو`sse` أو`stdio`.

### تعريفات خادم MCP المحفوظة

يخزن OpenClaw أيضا سجل خادم MCP خفيفا في الإعدادات للواجهات التي تريد تعريفات MCP مدارة من OpenClaw.

الأوامر:

  * `openclaw mcp list`
  * `openclaw mcp show [name]`
  * `openclaw mcp set <name> <json>`
  * `openclaw mcp unset <name>`


ملاحظات:

  * يرتب `list` أسماء الخوادم.
  * يطبع `show`، دون اسم، كائن خادم MCP المهيأ كاملا.
  * يتوقع `set` قيمة كائن JSON واحدة في سطر الأوامر.
  * استخدم `transport: "streamable-http"` لخوادم MCP عبر Streamable HTTP. يطبع `openclaw mcp set` أيضا `type: "http"` الأصلي للـ CLI إلى شكل الإعدادات القياسي نفسه للتوافق.
  * يفشل `unset` إذا لم يكن الخادم المسمى موجودا.


أمثلة:

bashCopy code
[code]
    openclaw mcp listopenclaw mcp show context7 --jsonopenclaw mcp set context7 '{"command":"uvx","args":["context7-mcp"]}'openclaw mcp set docs '{"url":"https://mcp.example.com","transport":"streamable-http"}'openclaw mcp unset context7
[/code]

مثال على شكل الإعدادات:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "context7": {        "command": "uvx",        "args": ["context7-mcp"]      },      "docs": {        "url": "https://mcp.example.com",        "transport": "streamable-http"      }    }  }}
[/code]

### نقل Stdio

يشغل عملية فرعية محلية ويتواصل عبر stdin/stdout.

الحقل | الوصف  
---|---  
`command` | الملف التنفيذي المراد تشغيله (مطلوب)  
`args` | مصفوفة من وسيطات سطر الأوامر  
`env` | متغيرات بيئة إضافية  
`cwd` / `workingDirectory` | دليل العمل للعملية  
  
### نقل SSE / HTTP

يتصل بخادم MCP بعيد عبر HTTP Server-Sent Events.

الحقل | الوصف  
---|---  
`url` | عنوان URL عبر HTTP أو HTTPS للخادم البعيد (مطلوب)  
`headers` | خريطة اختيارية من مفاتيح وقيم لترويسات HTTP (مثل رموز المصادقة)  
`connectionTimeoutMs` | مهلة اتصال لكل خادم بالمللي ثانية (اختياري)  
  
مثال:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "remote-tools": {        "url": "https://mcp.example.com",        "headers": {          "Authorization": "Bearer <token>"        }      }    }  }}
[/code]

تتم تنقيح القيم الحساسة في `url` (userinfo) و`headers` في السجلات ومخرجات الحالة.

### نقل Streamable HTTP

`streamable-http` هو خيار نقل إضافي إلى جانب `sse` و`stdio`. يستخدم بث HTTP للتواصل ثنائي الاتجاه مع خوادم MCP البعيدة.

الحقل | الوصف  
---|---  
`url` | عنوان URL عبر HTTP أو HTTPS للخادم البعيد (مطلوب)  
`transport` | اضبطه على `"streamable-http"` لاختيار هذا النقل؛ عند حذفه، يستخدم OpenClaw `sse`  
`headers` | خريطة اختيارية من مفاتيح وقيم لترويسات HTTP (مثل رموز المصادقة)  
`connectionTimeoutMs` | مهلة اتصال لكل خادم بالمللي ثانية (اختياري)  
  
تستخدم إعدادات OpenClaw `transport: "streamable-http"` كالتهجئة القياسية. يتم قبول قيم MCP الأصلية للـ CLI مثل `type: "http"` عند حفظها عبر `openclaw mcp set` وإصلاحها بواسطة `openclaw doctor --fix` في الإعدادات الحالية، لكن `transport` هو ما يستهلكه Pi المضمن مباشرة.

مثال:

jsonCopy code
[code]
    {  "mcp": {    "servers": {      "streaming-tools": {        "url": "https://mcp.example.com/stream",        "transport": "streamable-http",        "connectionTimeoutMs": 10000,        "headers": {          "Authorization": "Bearer <token>"        }      }    }  }}
[/code]

## الحدود الحالية

توثق هذه الصفحة الجسر كما هو مشحون اليوم.

الحدود الحالية:

  * يعتمد اكتشاف المحادثات على بيانات تعريف مسار جلسة Gateway الحالية
  * لا يوجد بروتوكول دفع عام يتجاوز المحول الخاص بـ Claude
  * لا توجد أدوات تعديل الرسائل أو التفاعل معها بعد
  * يتصل نقل HTTP/SSE/streamable-http بخادم بعيد واحد؛ لا توجد واجهة صاعدة متعددة الإرسال بعد
  * لا يتضمن `permissions_list_open` إلا الموافقات المرصودة أثناء اتصال الجسر


## ذو صلة

  * [مرجع CLI](</ar/cli>)
  * [Plugins](</ar/cli/plugins>)


Was this useful?YesNo