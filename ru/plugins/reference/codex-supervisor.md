---
title: Plugin супервизора Codex
source_url: https://docs.openclaw.ai/ru/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin супервайзера Codex

Контролируйте сеансы app-server Codex из OpenClaw.

## Распространение

  * Пакет: `@openclaw/codex-supervisor`
  * Маршрут установки: включено в OpenClaw


## Интерфейс

contracts: tools

## Список сеансов

`codex_sessions_list` по умолчанию показывает только загруженные сеансы Codex. Установите `include_stored`, чтобы включить сохраненную историю; Plugin использует путь получения списка только из БД состояния app-server Codex и по умолчанию ограничивает сохраненные результаты 200. Передайте `max_stored_sessions`, чтобы уменьшить или увеличить этот лимит, вплоть до 1000.

Was this useful?YesNo

Open issue