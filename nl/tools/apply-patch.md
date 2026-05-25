---
title: apply_patch-tool
source_url: https://docs.openclaw.ai/nl/tools/apply-patch
scraped_at: 2026-05-25
---

Pas bestandswijzigingen toe met een gestructureerde patchindeling. Dit is ideaal voor bewerkingen met meerdere bestanden of meerdere hunks waarbij één enkele `edit`-aanroep kwetsbaar zou zijn.

De tool accepteert één `input`-tekenreeks die één of meer bestandsbewerkingen omvat:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Parameters

  * `input` (required): Volledige patchinhoud inclusief `*** Begin Patch` en `*** End Patch`.


## Opmerkingen

  * Patchpaden ondersteunen relatieve paden (vanaf de werkruimtemap) en absolute paden.
  * `tools.exec.applyPatch.workspaceOnly` is standaard `true` (binnen de werkruimte). Stel dit alleen in op `false` als je bewust wilt dat `apply_patch` buiten de werkruimtemap schrijft/verwijdert.
  * Gebruik `*** Move to:` binnen een `*** Update File:`-hunk om bestanden te hernoemen.
  * `*** End of File` markeert indien nodig een invoeging die alleen EOF betreft.
  * Standaard beschikbaar voor OpenAI- en OpenAI Codex-modellen. Stel `tools.exec.applyPatch.enabled: false` in om dit uit te schakelen.
  * Optioneel per model beperken via `tools.exec.applyPatch.allowModels`.
  * Configuratie staat alleen onder `tools.exec`.


## Voorbeeld

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## Gerelateerd

[**Diffs** Alleen-lezen diffviewer voor wijzigingspresentatie. ](</nl/tools/diffs>) [**Exec-tool** Uitvoering van shellopdrachten vanuit de agent. ](</nl/tools/exec>) [**Code-uitvoering** Gesandboxte externe Python-analyse met xAI. ](</nl/tools/code-execution>)

Was this useful?YesNo