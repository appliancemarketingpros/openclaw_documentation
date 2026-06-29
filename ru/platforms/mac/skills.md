---
title: Skills (macOS)
source_url: https://docs.openclaw.ai/ru/platforms/mac/skills
scraped_at: 2026-06-29
---

PlatformsmacOS companion app

Приложение для macOS отображает OpenClaw Skills через Gateway; оно не разбирает Skills локально.

## Источник данных

  * `skills.status` (Gateway) возвращает все Skills, а также сведения о допустимости и недостающих требованиях (включая блокировки allowlist для встроенных Skills).
  * Требования выводятся из `metadata.openclaw.requires` в каждом `SKILL.md`.


## Действия установки

  * `metadata.openclaw.install` определяет варианты установки (brew/node/go/uv).
  * Приложение вызывает `skills.install`, чтобы запустить установщики на хосте Gateway.
  * Управляемая оператором `security.installPolicy` может блокировать установки Skills через Gateway до запуска метаданных установщика. Встроенная блокировка опасного кода во время установки не является частью потока установки Skills.
  * Если каждый вариант установки равен `download`, Gateway отображает все варианты загрузки.
  * В противном случае Gateway выбирает один предпочтительный установщик с учетом текущих предпочтений установки и бинарных файлов на хосте: сначала Homebrew, когда `skills.install.preferBrew` включен и `brew` существует, затем `uv`, затем настроенный менеджер Node из `skills.install.nodeManager`, затем более поздние резервные варианты, такие как `go` или `download`.
  * Метки установки Node отражают настроенный менеджер Node, включая `yarn`.


## Ключи окружения/API

  * Приложение хранит ключи в `~/.openclaw/openclaw.json` в `skills.entries.<skillKey>`.
  * `skills.update` исправляет `enabled`, `apiKey` и `env`.


## Удаленный режим

  * Установка и обновления конфигурации выполняются на хосте Gateway (не на локальном Mac).


## См. также

  * [Skills](</ru/tools/skills>)
  * [приложение macOS](</ru/platforms/macos>)


Was this useful?YesNo

Open issue