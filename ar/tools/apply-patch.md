---
title: أداة apply_patch
source_url: https://docs.openclaw.ai/ar/tools/apply-patch
scraped_at: 2026-05-25
---

طبّق تغييرات الملفات باستخدام صيغة تصحيح منظّمة. يُعدّ هذا مثاليًا للتعديلات متعددة الملفات أو متعددة المقاطع حيث يكون استدعاء `edit` واحد هشًا.

تقبل الأداة سلسلة `input` واحدة تغلّف عملية ملف واحدة أو أكثر:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## المعاملات

  * `input` (مطلوب): محتويات التصحيح كاملة بما في ذلك `*** Begin Patch` و `*** End Patch`.


## ملاحظات

  * تدعم مسارات التصحيح المسارات النسبية (من دليل مساحة العمل) والمسارات المطلقة.
  * القيمة الافتراضية لـ `tools.exec.applyPatch.workspaceOnly` هي `true` (محصورة ضمن مساحة العمل). عيّنها إلى `false` فقط إذا كنت تريد عمدًا أن يكتب `apply_patch` أو يحذف خارج دليل مساحة العمل.
  * استخدم `*** Move to:` ضمن مقطع `*** Update File:` لإعادة تسمية الملفات.
  * يضع `*** End of File` علامة على إدراج خاص بنهاية الملف فقط عند الحاجة.
  * متاحة افتراضيًا لنماذج OpenAI و OpenAI Codex. عيّن `tools.exec.applyPatch.enabled: false` لتعطيلها.
  * يمكن اختياريًا تقييدها حسب النموذج عبر `tools.exec.applyPatch.allowModels`.
  * الإعدادات موجودة فقط ضمن `tools.exec`.


## مثال

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## ذات صلة

[**Diffs** عارض فروق للقراءة فقط لعرض التغييرات. ](</ar/tools/diffs>) [**Exec tool** تنفيذ أوامر Shell من الوكيل. ](</ar/tools/exec>) [**Code execution** تحليل Python بعيد ضمن صندوق عزل باستخدام xAI. ](</ar/tools/code-execution>)

Was this useful?YesNo