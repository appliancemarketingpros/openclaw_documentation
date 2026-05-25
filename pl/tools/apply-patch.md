---
title: narzędzie apply_patch
source_url: https://docs.openclaw.ai/pl/tools/apply-patch
scraped_at: 2026-05-25
---

Zastosuj zmiany w plikach przy użyciu ustrukturyzowanego formatu łaty. Jest to idealne w przypadku edycji obejmujących wiele plików lub wiele fragmentów, gdzie pojedyncze wywołanie `edit` byłoby kruche.

Narzędzie przyjmuje pojedynczy ciąg `input`, który obejmuje jedną lub więcej operacji na plikach:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Parametry

  * `input` (wymagane): Pełna zawartość łaty, w tym `*** Begin Patch` i `*** End Patch`.


## Uwagi

  * Ścieżki łaty obsługują ścieżki względne (z katalogu obszaru roboczego) i ścieżki bezwzględne.
  * `tools.exec.applyPatch.workspaceOnly` domyślnie ma wartość `true` (ograniczone do obszaru roboczego). Ustaw ją na `false` tylko wtedy, gdy celowo chcesz, aby `apply_patch` zapisywało/usuwało poza katalogiem obszaru roboczego.
  * Użyj `*** Move to:` w fragmencie `*** Update File:`, aby zmieniać nazwy plików.
  * `*** End of File` oznacza wstawienie wyłącznie na końcu pliku, gdy jest potrzebne.
  * Domyślnie dostępne dla modeli OpenAI i OpenAI Codex. Ustaw `tools.exec.applyPatch.enabled: false`, aby je wyłączyć.
  * Opcjonalnie ogranicz według modelu za pomocą `tools.exec.applyPatch.allowModels`.
  * Konfiguracja znajduje się tylko w `tools.exec`.


## Przykład

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## Powiązane

[**Diffs** Przeglądarka różnic tylko do odczytu służąca do prezentacji zmian. ](</pl/tools/diffs>) [**Exec tool** Wykonywanie poleceń powłoki przez agenta. ](</pl/tools/exec>) [**Code execution** Izolowana zdalna analiza w Pythonie z xAI. ](</pl/tools/code-execution>)

Was this useful?YesNo