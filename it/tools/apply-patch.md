---
title: strumento apply_patch
source_url: https://docs.openclaw.ai/it/tools/apply-patch
scraped_at: 2026-05-25
---

Applica modifiche ai file usando un formato di patch strutturato. È ideale per modifiche su più file o con più blocchi, dove una singola chiamata `edit` sarebbe fragile.

Lo strumento accetta una singola stringa `input` che racchiude una o più operazioni sui file:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Parametri

  * `input` (obbligatorio): contenuto completo della patch, inclusi `*** Begin Patch` e `*** End Patch`.


## Note

  * I percorsi delle patch supportano percorsi relativi (dalla directory dell'area di lavoro) e percorsi assoluti.
  * `tools.exec.applyPatch.workspaceOnly` ha valore predefinito `true` (limitato all'area di lavoro). Impostalo su `false` solo se vuoi intenzionalmente che `apply_patch` scriva/eliminini file al di fuori della directory dell'area di lavoro.
  * Usa `*** Move to:` all'interno di un blocco `*** Update File:` per rinominare i file.
  * `*** End of File` indica un inserimento solo EOF quando necessario.
  * Disponibile per impostazione predefinita per i modelli OpenAI e OpenAI Codex. Imposta `tools.exec.applyPatch.enabled: false` per disabilitarlo.
  * Facoltativamente, limita per modello tramite `tools.exec.applyPatch.allowModels`.
  * La configurazione si trova solo sotto `tools.exec`.


## Esempio

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## Correlati

[**Diffs** Visualizzatore diff in sola lettura per la presentazione delle modifiche. ](</it/tools/diffs>) [**Exec tool** Esecuzione di comandi shell dall'agente. ](</it/tools/exec>) [**Code execution** Analisi Python remota in sandbox con xAI. ](</it/tools/code-execution>)

Was this useful?YesNo