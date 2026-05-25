---
title: apply_patch-Tool
source_url: https://docs.openclaw.ai/de/tools/apply-patch
scraped_at: 2026-05-25
---

Wenden Sie Dateiänderungen mit einem strukturierten Patch-Format an. Dies ist ideal für Bearbeitungen über mehrere Dateien oder mehrere Hunks hinweg, bei denen ein einzelner `edit`-Aufruf brüchig wäre.

Das Tool akzeptiert einen einzelnen `input`-String, der eine oder mehrere Dateioperationen umschließt:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Parameter

  * `input` (erforderlich): Vollständiger Patch-Inhalt einschließlich `*** Begin Patch` und `*** End Patch`.


## Hinweise

  * Patch-Pfade unterstützen relative Pfade (ausgehend vom Workspace-Verzeichnis) und absolute Pfade.
  * `tools.exec.applyPatch.workspaceOnly` ist standardmäßig `true` (auf den Workspace beschränkt). Setzen Sie es nur dann auf `false`, wenn Sie ausdrücklich möchten, dass `apply_patch` außerhalb des Workspace-Verzeichnisses schreibt/löscht.
  * Verwenden Sie `*** Move to:` innerhalb eines `*** Update File:`-Hunks, um Dateien umzubenennen.
  * `*** End of File` markiert bei Bedarf eine reine EOF-Einfügung.
  * Standardmäßig für OpenAI- und OpenAI Codex-Modelle verfügbar. Setzen Sie `tools.exec.applyPatch.enabled: false`, um es zu deaktivieren.
  * Optional können Sie per Modell über `tools.exec.applyPatch.allowModels` einschränken.
  * Die Konfiguration befindet sich nur unter `tools.exec`.


## Beispiel

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## Verwandt

[**Diffs** Schreibgeschützter Diff-Viewer für die Änderungspräsentation. ](</de/tools/diffs>) [**Exec tool** Ausführung von Shell-Befehlen durch den Agenten. ](</de/tools/exec>) [**Code execution** Sandbox-gestützte entfernte Python-Analyse mit xAI. ](</de/tools/code-execution>)

Was this useful?YesNo