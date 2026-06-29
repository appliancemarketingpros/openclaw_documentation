---
title: Plugin Codex Supervisor
source_url: https://docs.openclaw.ai/uk/plugins/reference/codex-supervisor
scraped_at: 2026-06-29
---

Get started

# Plugin Codex Supervisor

Наглядайте за сеансами сервера застосунку Codex з OpenClaw.

## Розповсюдження

  * Пакет: `@openclaw/codex-supervisor`
  * Маршрут встановлення: включено в OpenClaw


## Інтерфейс

контракти: інструменти

## Список сеансів

`codex_sessions_list` за замовчуванням показує лише завантажені сеанси Codex. Установіть `include_stored`, щоб включити збережену історію; Plugin використовує шлях переліку сервера застосунку Codex лише з БД стану та за замовчуванням обмежує збережені результати до 200. Передайте `max_stored_sessions`, щоб зменшити або збільшити це обмеження, аж до 1000.

Was this useful?YesNo

Open issue