---
title: Рабочий процесс среды выполнения агента OpenClaw
source_url: https://docs.openclaw.ai/ru/openclaw-agent-runtime
scraped_at: 2026-06-29
---

InstallAdvanced setup

Нормальный рабочий процесс для работы над средой выполнения агента OpenClaw в OpenClaw.

## Проверка типов и линтинг

  * Локальная проверка по умолчанию: `pnpm check`
  * Проверка сборки: `pnpm build`, когда изменение может повлиять на вывод сборки, упаковку или границы отложенной загрузки/модулей
  * Полная проверка перед слиянием для изменений среды выполнения агента: `pnpm check && pnpm test`


## Запуск тестов среды выполнения агента

Запустите набор тестов среды выполнения агента напрямую через Vitest:

bashCopy code
[code]
    pnpm test \  "src/agents/agent-*.test.ts" \  "src/agents/embedded-agent-*.test.ts" \  "src/agents/agent-tools*.test.ts" \  "src/agents/agent-settings.test.ts" \  "src/agents/agent-tool-definition-adapter*.test.ts" \  "src/agents/agent-hooks/**/*.test.ts"
[/code]

Чтобы включить проверку с live-провайдером:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/embedded-agent-runner-extraparams.live.test.ts
[/code]

Это покрывает основные модульные наборы тестов среды выполнения агента:

  * `src/agents/agent-*.test.ts`
  * `src/agents/embedded-agent-*.test.ts`
  * `src/agents/agent-tools*.test.ts`
  * `src/agents/agent-settings.test.ts`
  * `src/agents/agent-tool-definition-adapter.test.ts`
  * `src/agents/agent-hooks/*.test.ts`


## Ручное тестирование

Рекомендуемый процесс:

  * Запустите Gateway в режиме разработки: 
    * `pnpm gateway:dev`
  * Запустите агента напрямую: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Используйте TUI для интерактивной отладки: 
    * `pnpm tui`


Для поведения вызовов инструментов запросите действие `read` или `exec`, чтобы увидеть потоковую передачу инструмента и обработку полезной нагрузки.

## Сброс до чистого состояния

Состояние хранится в каталоге состояния OpenClaw. По умолчанию это `~/.openclaw`. Если задан `OPENCLAW_STATE_DIR`, используйте вместо него этот каталог.

Чтобы сбросить все:

  * `openclaw.json` для конфигурации
  * `agents/<agentId>/agent/auth-profiles.json` для профилей аутентификации модели (ключи API + OAuth)
  * `credentials/` для состояния провайдеров/каналов, которое все еще хранится вне хранилища профилей аутентификации
  * `agents/<agentId>/sessions/` для истории сеансов агента
  * `agents/<agentId>/sessions/sessions.json` для индекса сеансов
  * `sessions/`, если существуют устаревшие пути
  * `workspace/`, если вам нужна пустая рабочая область


Если вы хотите сбросить только сеансы, удалите `agents/<agentId>/sessions/` для этого агента. Если вы хотите сохранить аутентификацию, оставьте `agents/<agentId>/agent/auth-profiles.json` и любое состояние провайдера в `credentials/` на месте.

## Справочные материалы

  * [Тестирование](</ru/help/testing>)
  * [Начало работы](</ru/start/getting-started>)


## См. также

  * [Архитектура среды выполнения агента OpenClaw](</ru/agent-runtime-architecture>)


Was this useful?YesNo

Open issue