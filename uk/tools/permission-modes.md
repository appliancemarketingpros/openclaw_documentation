---
title: Режими дозволів
source_url: https://docs.openclaw.ai/uk/tools/permission-modes
scraped_at: 2026-06-29
---

CapabilitiesTools

Режими дозволів визначають, скільки повноважень має агент, перш ніж він зможе запускати команди хоста, записувати файли або просити бекенд-обвʼязку про додатковий доступ. Починайте з `tools.exec.mode: "auto"`, коли хочете, щоб OpenClaw спершу використовував списки дозволеного, а потім нативну автоматичну перевірку Codex або маршрут схвалення людиною для промахів.

## Рекомендоване значення за замовчуванням

Використовуйте `auto` для агентів кодування, яким потрібен корисний доступ до хоста без перетворення кожного промаху на запит до людини:

bashCopy code
[code]
    openclaw config set tools.exec.mode autoopenclaw approvals getopenclaw gateway restart
[/code]

Потім перевірте ефективну політику:

bashCopy code
[code]
    openclaw exec-policy show
[/code]

У режимі `auto` OpenClaw напряму запускає детерміновані збіги зі списком дозволеного. Промахи схвалення спершу проходять через нативного автоматичного рецензента OpenClaw, а потім за потреби переходять до налаштованого маршруту схвалення людиною.

## Режими виконання команд хоста OpenClaw

`tools.exec.mode` є нормалізованою поверхнею політики для хостового `exec`.

Режим | Поведінка | Коли використовувати  
---|---|---  
`deny` | Блокувати виконання команд хоста. | Команди хоста не дозволені.  
`allowlist` | Запускати лише команди зі списку дозволеного. | У вас є відомий безпечний набір команд.  
`ask` | Запускати збіги зі списком дозволеного й питати при промахах. | Людина має перевіряти нові форми команд.  
`auto` | Запускати збіги зі списком дозволеного, потім використовувати автоматичну перевірку. | Сеансам кодування потрібен практичний захищений доступ.  
`full` | Запускати команди хоста без запитів. | Цей довірений хост/сеанс має пропускати шлюзи схвалення.  
  
Повну політику виконання команд хоста, локальний файл схвалень, схему списку дозволеного, безпечні бінарні файли та поведінку переспрямування див. у [Схваленнях exec](</uk/tools/exec-approvals>).

## Зіставлення Codex Guardian

Для нативних сеансів сервера застосунку Codex `tools.exec.mode: "auto"` зіставляється зі схваленнями, перевіреними Codex Guardian, коли локальні вимоги Codex це дозволяють. OpenClaw зазвичай надсилає:

Поле Codex | Типове значення  
---|---  
`approvalPolicy` | `on-request`  
`approvalsReviewer` | `auto_review`  
`sandbox` | `workspace-write`  
  
У режимі `auto` OpenClaw не зберігає застарілі небезпечні перевизначення Codex, як-от `approvalPolicy: "never"` або `sandbox: "danger-full-access"`. Використовуйте `tools.exec.mode: "full"` лише тоді, коли навмисно потрібна позиція без схвалень.

Налаштування сервера застосунку, порядок автентифікації та деталі нативного середовища виконання Codex див. у [обвʼязці Codex](</uk/plugins/codex-harness>).

## Дозволи обвʼязки ACPX

Сеанси ACPX неінтерактивні, тому вони не можуть натиснути запит дозволу в TTY. ACPX використовує окремі налаштування рівня обвʼязки в `plugins.entries.acpx.config`:

Налаштування | Типове значення | Значення  
---|---|---  
`permissionMode` | `approve-reads` | Автоматично схвалювати лише читання.  
`permissionMode` | `approve-all` | Автоматично схвалювати записи та команди оболонки.  
`permissionMode` | `deny-all` | Відхиляти всі запити дозволів.  
`nonInteractivePermissions` | `fail` | Переривати, коли потрібен запит.  
`nonInteractivePermissions` | `deny` | Відхиляти запит і продовжувати, коли можливо.  
  
Налаштовуйте дозволи ACPX окремо від схвалень exec OpenClaw:

bashCopy code
[code]
    openclaw config set plugins.entries.acpx.config.permissionMode approve-allopenclaw config set plugins.entries.acpx.config.nonInteractivePermissions failopenclaw gateway restart
[/code]

Використовуйте `approve-all` як аварійний еквівалент сеансу обвʼязки без запитів для ACPX. Деталі налаштування та режими відмов див. у [налаштуванні агентів ACP](</uk/tools/acp-agents-setup#permission-configuration>).

## Вибір режиму

Мета | Налаштування  
---|---  
Повністю заблокувати команди хоста | `tools.exec.mode: "deny"`  
Дозволити запуск лише відомих безпечних команд | `tools.exec.mode: "allowlist"`  
Питати людину про кожну нову форму команди | `tools.exec.mode: "ask"`  
Використовувати автоматичну перевірку Codex/OpenClaw перед людьми | `tools.exec.mode: "auto"`  
Повністю пропустити схвалення exec на хості | `tools.exec.mode: "full"` плюс відповідний файл схвалень хоста  
Дозволити неінтерактивним сеансам ACPX запис/exec | `plugins.entries.acpx.config.permissionMode: "approve-all"`  
  
Якщо команда все ще показує запит або завершується помилкою після зміни режиму, перевірте обидва рівні:

bashCopy code
[code]
    openclaw approvals getopenclaw exec-policy show
[/code]

Виконання команд хоста використовує суворіший результат із конфігурації OpenClaw і локального для хоста файлу схвалень. Дозволи обвʼязки ACPX не послаблюють схвалення exec на хості, а схвалення exec на хості не послаблюють запити обвʼязки ACPX.

## Повʼязане

  * [Схвалення exec](</uk/tools/exec-approvals>)
  * [Схвалення exec - розширені](</uk/tools/exec-approvals-advanced>)
  * [Обвʼязка Codex](</uk/plugins/codex-harness>)
  * [Налаштування агентів ACP](</uk/tools/acp-agents-setup#permission-configuration>)


Was this useful?YesNo

Open issue