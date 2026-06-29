---
title: Робочий процес середовища виконання агента OpenClaw
source_url: https://docs.openclaw.ai/uk/openclaw-agent-runtime
scraped_at: 2026-06-29
---

InstallAdvanced setup

Раціональний робочий процес для роботи над середовищем виконання агента OpenClaw в OpenClaw.

## Перевірка типів і лінтинг

  * Типовий локальний контроль: `pnpm check`
  * Контроль збірки: `pnpm build`, коли зміна може вплинути на результат збірки, пакування або межі lazy-loading/модулів
  * Повний контроль перед злиттям для змін середовища виконання агента: `pnpm check && pnpm test`


## Запуск тестів середовища виконання агента

Запустіть набір тестів середовища виконання агента напряму через Vitest:

bashCopy code
[code]
    pnpm test \  "src/agents/agent-*.test.ts" \  "src/agents/embedded-agent-*.test.ts" \  "src/agents/agent-tools*.test.ts" \  "src/agents/agent-settings.test.ts" \  "src/agents/agent-tool-definition-adapter*.test.ts" \  "src/agents/agent-hooks/**/*.test.ts"
[/code]

Щоб включити перевірку з live-провайдером:

bashCopy code
[code]
    OPENCLAW_LIVE_TEST=1 pnpm test src/agents/embedded-agent-runner-extraparams.live.test.ts
[/code]

Це покриває основні модульні набори тестів середовища виконання агента:

  * `src/agents/agent-*.test.ts`
  * `src/agents/embedded-agent-*.test.ts`
  * `src/agents/agent-tools*.test.ts`
  * `src/agents/agent-settings.test.ts`
  * `src/agents/agent-tool-definition-adapter.test.ts`
  * `src/agents/agent-hooks/*.test.ts`


## Ручне тестування

Рекомендований потік:

  * Запустіть Gateway у режимі розробки: 
    * `pnpm gateway:dev`
  * Запустіть агента напряму: 
    * `pnpm openclaw agent --message "Hello" --thinking low`
  * Використовуйте TUI для інтерактивного налагодження: 
    * `pnpm tui`


Для поведінки викликів інструментів попросіть дію `read` або `exec`, щоб побачити потокове передавання даних інструмента й обробку payload.

## Скидання до чистого стану

Стан зберігається в каталозі стану OpenClaw. Типове значення — `~/.openclaw`. Якщо встановлено `OPENCLAW_STATE_DIR`, натомість використовуйте цей каталог.

Щоб скинути все:

  * `openclaw.json` для конфігурації
  * `agents/<agentId>/agent/auth-profiles.json` для профілів автентифікації моделей (ключі API + OAuth)
  * `credentials/` для стану провайдера/каналу, який досі зберігається поза сховищем профілів автентифікації
  * `agents/<agentId>/sessions/` для історії сесій агента
  * `agents/<agentId>/sessions/sessions.json` для індексу сесій
  * `sessions/`, якщо існують застарілі шляхи
  * `workspace/`, якщо потрібен порожній робочий простір


Якщо потрібно скинути лише сесії, видаліть `agents/<agentId>/sessions/` для цього агента. Якщо потрібно зберегти автентифікацію, залиште `agents/<agentId>/agent/auth-profiles.json` і будь-який стан провайдера в `credentials/` на місці.

## Довідкові матеріали

  * [Тестування](</uk/help/testing>)
  * [Початок роботи](</uk/start/getting-started>)


## Пов’язане

  * [Архітектура середовища виконання агента OpenClaw](</uk/agent-runtime-architecture>)


Was this useful?YesNo

Open issue