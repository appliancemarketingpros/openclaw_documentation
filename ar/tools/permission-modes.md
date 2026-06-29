---
title: أوضاع الأذونات
source_url: https://docs.openclaw.ai/ar/tools/permission-modes
scraped_at: 2026-06-29
---

CapabilitiesTools

تحدد أوضاع الأذونات مقدار الصلاحية التي يمتلكها الوكيل قبل أن يتمكن من تشغيل أوامر المضيف، أو كتابة الملفات، أو طلب وصول إضافي من حزمة خلفية. ابدأ بـ `tools.exec.mode: "auto"` عندما تريد أن يستخدم OpenClaw قوائم السماح أولًا، ثم المراجعة التلقائية الأصلية في Codex أو مسار موافقة بشري عند عدم التطابق.

## الإعداد الافتراضي الموصى به

استخدم `auto` لوكلاء البرمجة الذين يحتاجون إلى وصول مفيد إلى المضيف من دون تحويل كل عدم تطابق إلى طلب بشري:

bashCopy code
[code]
    openclaw config set tools.exec.mode autoopenclaw approvals getopenclaw gateway restart
[/code]

ثم تحقق من السياسة الفعلية:

bashCopy code
[code]
    openclaw exec-policy show
[/code]

في وضع `auto`، يشغل OpenClaw مطابقات قائمة السماح الحتمية مباشرة. تمر حالات عدم تطابق الموافقة أولًا عبر المراجع التلقائي الأصلي في OpenClaw، ثم تعود إلى مسار الموافقة البشري المكوّن عند الحاجة.

## أوضاع تنفيذ المضيف في OpenClaw

`tools.exec.mode` هو سطح السياسة الموحّد لتنفيذ `exec` على المضيف.

الوضع | السلوك | استخدمه عندما  
---|---|---  
`deny` | حظر تنفيذ المضيف. | لا يُسمح بأي أوامر على المضيف.  
`allowlist` | تشغيل الأوامر المدرجة في قائمة السماح فقط. | لديك مجموعة أوامر معروفة بأنها آمنة.  
`ask` | تشغيل مطابقات قائمة السماح والسؤال عند عدم التطابق. | يجب أن يراجع إنسان الأوامر الجديدة.  
`auto` | تشغيل مطابقات قائمة السماح، ثم استخدام المراجعة التلقائية. | تحتاج جلسات البرمجة إلى وصول عملي ومحروس.  
`full` | تشغيل تنفيذ المضيف من دون مطالبات. | يجب أن يتجاوز هذا المضيف/هذه الجلسة الموثوقة بوابات الموافقة.  
  
للاطلاع على سياسة تنفيذ المضيف الكاملة، وملف الموافقات المحلي، ومخطط قائمة السماح، والثنائيات الآمنة، وسلوك التمرير، راجع [موافقات التنفيذ](</ar/tools/exec-approvals>).

## ربط Codex Guardian

بالنسبة إلى جلسات خادم التطبيق الأصلية في Codex، يُربط `tools.exec.mode: "auto"` بموافقات يراجعها Codex Guardian عندما تسمح متطلبات Codex المحلية بذلك. يرسل OpenClaw عادةً:

حقل Codex | القيمة النموذجية  
---|---  
`approvalPolicy` | `on-request`  
`approvalsReviewer` | `auto_review`  
`sandbox` | `workspace-write`  
  
في وضع `auto`، لا يحتفظ OpenClaw بتجاوزات Codex القديمة غير الآمنة مثل `approvalPolicy: "never"` أو `sandbox: "danger-full-access"`. استخدم `tools.exec.mode: "full"` فقط عندما تريد عمدًا وضعًا بلا موافقات.

لإعداد خادم التطبيق، وترتيب المصادقة، وتفاصيل وقت تشغيل Codex الأصلي، راجع [حزمة Codex](</ar/plugins/codex-harness>).

## أذونات حزمة ACPX

جلسات ACPX غير تفاعلية، لذلك لا يمكنها النقر على مطالبة أذونات TTY. يستخدم ACPX إعدادات منفصلة على مستوى الحزمة ضمن `plugins.entries.acpx.config`:

الإعداد | القيمة الشائعة | المعنى  
---|---|---  
`permissionMode` | `approve-reads` | الموافقة التلقائية على القراءات فقط.  
`permissionMode` | `approve-all` | الموافقة التلقائية على الكتابات وأوامر الصدفة.  
`permissionMode` | `deny-all` | رفض كل مطالبات الأذونات.  
`nonInteractivePermissions` | `fail` | الإيقاف عندما تكون المطالبة مطلوبة.  
`nonInteractivePermissions` | `deny` | رفض المطالبة والمتابعة عندما يكون ذلك ممكنًا.  
  
اضبط أذونات ACPX بشكل منفصل عن موافقات التنفيذ في OpenClaw:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions failopenclaw gateway restart
[/code]

استخدم `approve-all` بوصفه مكافئ الطوارئ في ACPX لجلسة حزمة بلا مطالبات. للحصول على تفاصيل الإعداد وأنماط الفشل، راجع [إعداد وكلاء ACP](</ar/tools/acp-agents-setup#permission-configuration>).

## اختيار وضع

الهدف | التكوين  
---|---  
حظر أوامر المضيف بالكامل | `tools.exec.mode: "deny"`  
السماح بتشغيل الأوامر المعروفة بأنها آمنة فقط | `tools.exec.mode: "allowlist"`  
سؤال إنسان عن كل شكل أمر جديد | `tools.exec.mode: "ask"`  
استخدام المراجعة التلقائية في Codex/OpenClaw قبل البشر | `tools.exec.mode: "auto"`  
تخطي موافقات تنفيذ المضيف بالكامل | `tools.exec.mode: "full"` بالإضافة إلى ملف موافقات مضيف مطابق  
جعل جلسات ACPX غير التفاعلية تكتب/تنفذ | `plugins.entries.acpx.config.permissionMode: "approve-all"`  
  
إذا ظل الأمر يعرض مطالبة أو يفشل بعد تغيير الوضع، فتحقق من الطبقتين:

bashCopy code
[code]
    openclaw approvals getopenclaw exec-policy show
[/code]

يستخدم تنفيذ المضيف النتيجة الأكثر صرامة بين إعدادات OpenClaw وملف الموافقات المحلي على المضيف. لا تخفف أذونات حزمة ACPX من موافقات تنفيذ المضيف، ولا تخفف موافقات تنفيذ المضيف من مطالبات حزمة ACPX.

## ذات صلة

  * [موافقات التنفيذ](</ar/tools/exec-approvals>)
  * [موافقات التنفيذ - متقدم](</ar/tools/exec-approvals-advanced>)
  * [حزمة Codex](</ar/plugins/codex-harness>)
  * [إعداد وكلاء ACP](</ar/tools/acp-agents-setup#permission-configuration>)


Was this useful?YesNo

Open issue