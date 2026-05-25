---
title: `openclaw tasks`
source_url: https://docs.openclaw.ai/uk/cli/tasks
scraped_at: 2026-05-25
---

Переглядайте довговічні фонові завдання та стан Task Flow. Без підкоманди `openclaw tasks` еквівалентна `openclaw tasks list`.

Див. [Фонові завдання](</uk/automation/tasks>), щоб дізнатися про життєвий цикл і модель доставки.

## Використання

bashCopy code
[code]
    openclaw tasksopenclaw tasks listopenclaw tasks list --runtime acpopenclaw tasks list --status runningopenclaw tasks show <lookup>openclaw tasks notify <lookup> state_changesopenclaw tasks cancel <lookup>openclaw tasks auditopenclaw tasks maintenanceopenclaw tasks maintenance --applyopenclaw tasks flow listopenclaw tasks flow show <lookup>openclaw tasks flow cancel <lookup>
[/code]

## Кореневі параметри

  * `--json`: вивести JSON.
  * `--runtime <name>`: фільтрувати за типом: `subagent`, `acp`, `cron` або `cli`.
  * `--status <name>`: фільтрувати за статусом: `queued`, `running`, `succeeded`, `failed`, `timed_out`, `cancelled` або `lost`.


## Підкоманди

### `list`

bashCopy code
[code]
    openclaw tasks list [--runtime <name>] [--status <name>] [--json]
[/code]

Виводить відстежувані фонові завдання, починаючи з найновіших.

### `show`

bashCopy code
[code]
    openclaw tasks show <lookup> [--json]
[/code]

Показує одне завдання за ID завдання, ID запуску або ключем сеансу.

### `notify`

bashCopy code
[code]
    openclaw tasks notify <lookup> <done_only|state_changes|silent>
[/code]

Змінює політику сповіщень для завдання, що виконується.

### `cancel`

bashCopy code
[code]
    openclaw tasks cancel <lookup>
[/code]

Скасовує фонове завдання, що виконується.

### `audit`

bashCopy code
[code]
    openclaw tasks audit [--severity <warn|error>] [--code <name>] [--limit <n>] [--json]
[/code]

Виявляє застарілі, втрачені, з помилкою доставки або іншим чином неузгоджені записи завдань і Task Flow. Втрачені завдання, збережені до `cleanupAfter`, є попередженнями; прострочені або втрачені завдання без мітки часу є помилками.

### `maintenance`

bashCopy code
[code]
    openclaw tasks maintenance [--apply] [--json]
[/code]

Попередньо показує або застосовує узгодження завдань і Task Flow, проставлення міток очищення, обрізання та очищення реєстру сеансів застарілих запусків Cron. Для завдань Cron узгодження використовує збережені журнали запусків/стан завдання перед тим, як позначити старе активне завдання як `lost`, тож завершені запуски Cron не стають хибними помилками аудиту лише тому, що стан середовища виконання Gateway у пам’яті зник. Офлайн-аудит CLI не є авторитетним для локального для процесу набору активних завдань Cron у Gateway. Завдання CLI з ID запуску/ID джерела позначаються як `lost`, коли їхній живий контекст запуску Gateway зник, навіть якщо старий рядок дочірнього сеансу залишається. Під час застосування maintenance також обрізає рядки реєстру сеансів `cron:<jobId>:run:<uuid>`, старші за 7 днів, зберігаючи поточні завдання Cron, що виконуються, і залишаючи рядки сеансів, не пов’язані з Cron, без змін.

### `flow`

bashCopy code
[code]
    openclaw tasks flow list [--status <name>] [--json]openclaw tasks flow show <lookup> [--json]openclaw tasks flow cancel <lookup>
[/code]

Переглядає або скасовує довговічний стан Task Flow у реєстрі завдань.

## Пов’язане

  * [Довідник CLI](</uk/cli>)
  * [Фонові завдання](</uk/automation/tasks>)


Was this useful?YesNo