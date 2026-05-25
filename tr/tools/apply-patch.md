---
title: apply_patch aracı
source_url: https://docs.openclaw.ai/tr/tools/apply-patch
scraped_at: 2026-05-25
---

Yapılandırılmış bir yama formatı kullanarak dosya değişiklikleri uygulayın. Bu, tek bir `edit` çağrısının kırılgan olacağı çok dosyalı veya çok hunk'lı düzenlemeler için idealdir.

Araç, bir veya daha fazla dosya işlemini saran tek bir `input` dizesi kabul eder:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Parametreler

  * `input` (gerekli): `*** Begin Patch` ve `*** End Patch` dahil tam yama içeriği.


## Notlar

  * Yama yolları göreli yolları (çalışma alanı dizininden) ve mutlak yolları destekler.
  * `tools.exec.applyPatch.workspaceOnly` varsayılan olarak `true` değerindedir (çalışma alanıyla sınırlı). Yalnızca `apply_patch` aracının çalışma alanı dizini dışında yazmasını/silmesini özellikle istiyorsanız bunu `false` olarak ayarlayın.
  * Dosyaları yeniden adlandırmak için bir `*** Update File:` hunk'ı içinde `*** Move to:` kullanın.
  * `*** End of File`, gerektiğinde yalnızca EOF eklemesini işaretler.
  * OpenAI ve OpenAI Codex modelleri için varsayılan olarak kullanılabilir. Devre dışı bırakmak için `tools.exec.applyPatch.enabled: false` ayarlayın.
  * İsteğe bağlı olarak model bazında şu yapılandırmayla sınırlayın: `tools.exec.applyPatch.allowModels`.
  * Yapılandırma yalnızca `tools.exec` altındadır.


## Örnek

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## İlgili

[**Diffs** Değişiklik sunumu için salt okunur diff görüntüleyici. ](</tr/tools/diffs>) [**Exec tool** Agent tarafından shell komutu yürütme. ](</tr/tools/exec>) [**Code execution** xAI ile sandbox içinde uzak Python analizi. ](</tr/tools/code-execution>)

Was this useful?YesNo