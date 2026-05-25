---
title: інструмент apply_patch
source_url: https://docs.openclaw.ai/uk/tools/apply-patch
scraped_at: 2026-05-25
---

Застосовуйте зміни до файлів за допомогою структурованого формату патча. Це ідеально підходить для багатофайлових або багатофрагментних редагувань, коли один виклик `edit` був би крихким.

Інструмент приймає один рядок `input`, який обгортає одну або кілька файлових операцій:

CodeCopy code
[code]
    *** Begin Patch*** Add File: path/to/file.txt+line 1+line 2*** Update File: src/app.ts@@-old line+new line*** Delete File: obsolete.txt*** End Patch
[/code]

## Параметри

  * `input` (обов’язковий): повний вміст патча, включно з `*** Begin Patch` і `*** End Patch`.


## Примітки

  * Шляхи патча підтримують відносні шляхи (від каталогу робочого простору) й абсолютні шляхи.
  * `tools.exec.applyPatch.workspaceOnly` за замовчуванням має значення `true` (у межах робочого простору). Установлюйте його в `false` лише якщо ви навмисно хочете, щоб `apply_patch` записував або видаляв файли поза каталогом робочого простору.
  * Використовуйте `*** Move to:` всередині фрагмента `*** Update File:`, щоб перейменовувати файли.
  * `*** End of File` позначає вставлення лише в EOF, коли це потрібно.
  * Доступний за замовчуванням для моделей OpenAI та OpenAI Codex. Установіть `tools.exec.applyPatch.enabled: false`, щоб вимкнути його.
  * За потреби обмежуйте за моделлю через `tools.exec.applyPatch.allowModels`.
  * Конфігурація є лише в `tools.exec`.


## Приклад

jsonCopy code
[code]
    {  "tool": "apply_patch",  "input": "*** Begin Patch\n*** Update File: src/index.ts\n@@\n-const foo = 1\n+const foo = 2\n*** End Patch"}
[/code]

## Пов’язане

[**Diffs** Засіб перегляду diff лише для читання для представлення змін. ](</uk/tools/diffs>) [**Exec tool** Виконання команд shell з агента. ](</uk/tools/exec>) [**Code execution** Ізольований віддалений аналіз Python з xAI. ](</uk/tools/code-execution>)

Was this useful?YesNo