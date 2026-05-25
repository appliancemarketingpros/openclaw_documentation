---
title: Bun (експериментально)
source_url: https://docs.openclaw.ai/uk/install/bun
scraped_at: 2026-05-25
---

Bun — необов’язкове локальне середовище виконання для прямого запуску TypeScript (`bun run ...`, `bun --watch ...`). Типовим менеджером пакетів залишається `pnpm`, який повністю підтримується й використовується інструментами документації. Bun не може використовувати `pnpm-lock.yaml` і ігноруватиме його.

## Встановлення

* ### Встановіть залежності

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` ігноруються Git, тому в репозиторії не виникає зайвих змін. Щоб повністю пропустити записування lockfile:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Зберіть і протестуйте

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Скрипти життєвого циклу

Bun блокує скрипти життєвого циклу залежностей, якщо їм явно не надано довіру. Для цього репозиторію скрипти, які зазвичай блокуються, не потрібні:

  * `baileys` `preinstall` \-- перевіряє, що основна версія Node >= 20 (OpenClaw за замовчуванням використовує Node 24 і все ще підтримує Node 22 LTS, наразі `22.16+`)
  * `protobufjs` `postinstall` \-- виводить попередження про несумісні схеми версій (без артефактів збірки)


Якщо ви зіткнетеся з проблемою під час виконання, яка потребує цих скриптів, явно надайте їм довіру:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Застереження

Деякі скрипти досі жорстко прив’язані до pnpm (наприклад, `docs:build`, `ui:*`, `protocol:check`). Поки що запускайте їх через pnpm.

## Пов’язане

  * [Огляд встановлення](</uk/install>)
  * [Node.js](</uk/install/node>)
  * [Оновлення](</uk/install/updating>)


Was this useful?YesNo