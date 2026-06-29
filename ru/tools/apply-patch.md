---
title: инструмент apply_patch
source_url: https://docs.openclaw.ai/ru/tools/apply-patch
scraped_at: 2026-06-29
---

CapabilitiesTools

Применяйте изменения файлов с помощью структурированного формата патчей. Это идеально подходит для многофайловых или многофрагментных правок, когда один вызов `edit` был бы ненадежным.

Инструмент принимает одну строку `input`, которая оборачивает одну или несколько файловых операций:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Параметры

  * `input` (обязательно): Полное содержимое патча, включая `*** Begin Patch` и `*** End Patch`.


## Примечания

  * Пути в патче поддерживают относительные пути (от каталога рабочей области) и абсолютные пути.
  * `tools.exec.applyPatch.workspaceOnly` по умолчанию имеет значение `true` (в пределах рабочей области). Устанавливайте `false` только если намеренно хотите, чтобы `apply_patch` записывал/удалял файлы за пределами каталога рабочей области.
  * Используйте `*** Move to:` внутри фрагмента `*** Update File:`, чтобы переименовывать файлы.
  * `*** End of File` при необходимости помечает вставку только в конец файла.
  * Доступно по умолчанию для моделей OpenAI и OpenAI Codex. Установите `tools.exec.applyPatch.enabled: false`, чтобы отключить это.
  * При необходимости ограничьте по модели через `tools.exec.applyPatch.allowModels`.
  * Конфигурация находится только в `tools.exec`.


## Пример

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## Связанное

[**Различия** Средство просмотра различий только для чтения для представления изменений. ](</ru/tools/diffs>) [**Инструмент Exec** Выполнение команд оболочки из агента. ](</ru/tools/exec>) [**Выполнение кода** Изолированный удаленный анализ Python с xAI. ](</ru/tools/code-execution>)

Was this useful?YesNo

Open issue