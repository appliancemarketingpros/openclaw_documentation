---
title: Bun (экспериментально)
source_url: https://docs.openclaw.ai/ru/install/bun
scraped_at: 2026-06-29
---

InstallContainers

Bun — необязательная локальная среда выполнения для прямого запуска TypeScript (`bun run ...`, `bun --watch ...`). Пакетным менеджером по умолчанию остается `pnpm`, который полностью поддерживается и используется инструментами документации. Bun не может использовать `pnpm-lock.yaml` и будет игнорировать его.

## Установка

* ### Install dependencies

shCopy code
[code]
    bun install
[/code]

`bun.lock` / `bun.lockb` игнорируются Git, поэтому в репозитории не возникает лишних изменений. Чтобы полностью пропустить запись lock-файла:

shCopy code
[code]
    bun install --no-save
[/code]

* ### Build and test

shCopy code
[code]
    bun run buildbun run vitest run
[/code]

## Скрипты жизненного цикла

Bun блокирует скрипты жизненного цикла зависимостей, если они явно не доверены. Для этого репозитория обычно блокируемые скрипты не требуются:

  * `baileys` `preinstall` \-- проверяет, что основная версия Node >= 20 (OpenClaw по умолчанию использует Node 24 и по-прежнему поддерживает Node 22 LTS, сейчас `22.19+`)
  * `protobufjs` `postinstall` \-- выводит предупреждения о несовместимых схемах версий (без артефактов сборки)


Если вы столкнулись с проблемой во время выполнения, для которой нужны эти скрипты, явно доверьте их:

shCopy code
[code]
    bun pm trust baileys protobufjs
[/code]

## Ограничения

В некоторых скриптах пока жестко задан pnpm (например, `check:docs`, `ui:*`, `protocol:check`). Пока запускайте их через pnpm.

## См. также

  * [Обзор установки](</ru/install>)
  * [Node.js](</ru/install/node>)
  * [Обновление](</ru/install/updating>)


Was this useful?YesNo

Open issue