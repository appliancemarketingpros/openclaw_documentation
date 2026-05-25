---
title: إرسال الوكيل
source_url: https://docs.openclaw.ai/ar/tools/agent-send
scraped_at: 2026-05-25
---

يشغّل `openclaw agent` دورة وكيل واحدة من سطر الأوامر دون الحاجة إلى رسالة دردشة واردة. استخدمه لسير العمل النصية، والاختبار، والتسليم البرمجي.

## البدء السريع

* ### تشغيل دورة وكيل بسيطة

bashCopy code
[code]
    openclaw agent --message "What is the weather today?"
[/code]

يرسل هذا الرسالة عبر Gateway ويطبع الرد.

* ### استهداف وكيل أو جلسة محددة

bashCopy code
[code]
    # Target a specific agentopenclaw agent --agent ops --message "Summarize logs" # Target a phone number (derives session key)openclaw agent --to +15555550123 --message "Status update" # Reuse an existing sessionopenclaw agent --session-id abc123 --message "Continue the task"
[/code]

* ### تسليم الرد إلى قناة

bashCopy code
[code]
    # Deliver to WhatsApp (default channel)openclaw agent --to +15555550123 --message "Report ready" --deliver # Deliver to Slackopenclaw agent --agent ops --message "Generate report" \  --deliver --reply-channel slack --reply-to "#reports"
[/code]

## العلامات

العلامة | الوصف  
---|---  
`--message \<text\>` | الرسالة المراد إرسالها (مطلوبة)  
`--to \<dest\>` | اشتقاق مفتاح الجلسة من هدف (هاتف، معرّف دردشة)  
`--agent \<id\>` | استهداف وكيل مُعدّ (يستخدم جلسة `main` الخاصة به)  
`--session-id \<id\>` | إعادة استخدام جلسة موجودة حسب المعرّف  
`--local` | فرض وقت التشغيل المضمّن المحلي (تجاوز Gateway)  
`--deliver` | إرسال الرد إلى قناة دردشة  
`--channel \<name\>` | قناة التسليم (whatsapp، telegram، discord، slack، إلخ)  
`--reply-to \<target\>` | تجاوز هدف التسليم  
`--reply-channel \<name\>` | تجاوز قناة التسليم  
`--reply-account \<id\>` | تجاوز معرّف حساب التسليم  
`--thinking \<level\>` | ضبط مستوى التفكير لملف تعريف النموذج المحدد  
`--verbose \<on|full|off\>` | ضبط مستوى الإسهاب  
`--timeout \<seconds\>` | تجاوز مهلة الوكيل  
`--json` | إخراج JSON منظّم  
  
## السلوك

  * افتراضيًا، تمر CLI **عبر Gateway**. أضف `--local` لفرض وقت التشغيل المضمّن على الجهاز الحالي.
  * إذا تعذّر الوصول إلى Gateway، **تعود** CLI إلى التشغيل المضمّن المحلي.
  * اختيار الجلسة: يشتق `--to` مفتاح الجلسة (تحافظ أهداف المجموعة/القناة على العزل؛ وتُدمج الدردشات المباشرة في `main`).
  * تستمر علامات التفكير والإسهاب في مخزن الجلسات.
  * الإخراج: نص عادي افتراضيًا، أو `--json` لحمولة منظّمة + بيانات وصفية.
  * مع `--json --deliver`، يتضمن JSON حالة التسليم للرسائل المرسلة، والمكبوتة، والجزئية، والفاشلة. راجع [حالة تسليم JSON](</ar/cli/agent#json-delivery-status>).


## أمثلة

bashCopy code
[code]
    # Simple turn with JSON outputopenclaw agent --to +15555550123 --message "Trace logs" --verbose on --json # Turn with thinking levelopenclaw agent --session-id 1234 --message "Summarize inbox" --thinking medium # Deliver to a different channel than the sessionopenclaw agent --agent ops --message "Alert" --deliver --reply-channel telegram --reply-to "@admin"
[/code]

## ذات صلة

[**مرجع CLI للوكيل** مرجع كامل لعلامات وخيارات `openclaw agent`. ](</ar/cli/agent>) [**الوكلاء الفرعيون** إنشاء وكلاء فرعيين في الخلفية. ](</ar/tools/subagents>) [**الجلسات** كيف تعمل مفاتيح الجلسات وكيف يحلّ `--to` و`--agent` و`--session-id` إليها. ](</ar/concepts/session>) [**أوامر الشرطة المائلة** كتالوج الأوامر الأصلي المستخدم داخل جلسات الوكيل. ](</ar/tools/slash-commands>)

Was this useful?YesNo