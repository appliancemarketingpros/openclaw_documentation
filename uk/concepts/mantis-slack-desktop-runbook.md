---
title: Операційний посібник для настільного клієнта Mantis Slack
source_url: https://docs.openclaw.ai/uk/concepts/mantis-slack-desktop-runbook
scraped_at: 2026-05-25
---

Mantis Slack desktop QA — це смуга з реальним UI для помилок класу Slack, які потребують Linux desktop, аварійного доступу VNC, Slack Web, справжнього OpenClaw Gateway, знімків екрана, відео та коментаря з доказами в PR.

Використовуйте її, коли модульні тести або headless Slack live lane не можуть довести помилку.

## Модель зберігання

Mantis використовує три різні рівні зберігання:

  * Образ провайдера: належить Crabbox і зберігається в обліковому записі хмарного провайдера. Він містить можливості машини, як-от Chrome/Chromium, ffmpeg, scrot, Node/corepack/pnpm, нативні інструменти складання та порожні каталоги кешу.
  * Стан теплого lease: належить поточній сесії оператора. Він може містити профіль браузера з виконаним входом, `/var/cache/crabbox/pnpm` і підготовлений вихідний checkout, доки lease активний.
  * Артефакти Mantis: належать запуску OpenClaw. Вони розміщуються в `.artifacts/qa-e2e/mantis/...`, потім GitHub Actions завантажує їх, а Mantis GitHub App коментує inline-докази в PR.


Ніколи не додавайте секрети, cookies браузера, стан входу Slack, checkout-и репозиторію, `node_modules` або `dist/` у попередньо запечений образ провайдера.

## GitHub dispatch

Запустіть workflow з `main`:

bashCopy code
[code]
    gh workflow run mantis-slack-desktop-smoke.yml \  --ref main \  -f candidate_ref=<trusted-ref-or-sha> \  -f pr_number=<pr-number> \  -f scenario_id=slack-canary \  -f crabbox_provider=aws \  -f keep_vm=false \  -f hydrate_mode=source
[/code]

Дозволені значення `candidate_ref` навмисно вузькі, оскільки workflow використовує живі облікові дані: поточна історія `main`, release tags або head відкритого PR з `openclaw/openclaw`.

Workflow записує:

  * завантажений артефакт: `mantis-slack-desktop-smoke-<run-id>-<attempt>`;
  * inline-коментар PR від Mantis GitHub App;
  * `slack-desktop-smoke.png`;
  * `slack-desktop-smoke.mp4`;
  * `slack-desktop-smoke-preview.gif`;
  * `slack-desktop-smoke-change.mp4`;
  * `mantis-slack-desktop-smoke-summary.json`;
  * `mantis-slack-desktop-smoke-report.md`;
  * віддалені журнали, як-от `slack-desktop-command.log`, `openclaw-gateway.log`, `chrome.log` і `ffmpeg.log`.


Коментар PR оновлюється на місці за прихованим маркером `<!-- mantis-slack-desktop-smoke -->`.

## Локальний CLI

Холодне доведення з source:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --credential-source convex \  --credential-role maintainer \  --provider-mode live-frontier \  --model openai/gpt-5.4 \  --alt-model openai/gpt-5.4 \  --scenario slack-canary \  --hydrate-mode source
[/code]

Залиште VM для аварійного доступу VNC:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --scenario slack-canary \  --keep-lease
[/code]

Відкрити VNC:

bashCopy code
[code]
    crabbox vnc --provider aws --id <cbx_id> --open
[/code]

Повторно використати теплий lease:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --lease-id <cbx_id-or-slug> \  --gateway-setup \  --scenario slack-canary \  --hydrate-mode source
[/code]

Використовуйте `--hydrate-mode prehydrated` лише тоді, коли повторно використаний віддалений workspace уже має `node_modules` і зібраний `dist/`. Mantis завершується закрито, якщо вони відсутні.

## Режими hydrate

Режим | Коли використовувати | Віддалена поведінка | Компроміс  
---|---|---|---  
`source` | Звичайне доведення PR, холодні машини, CI | Запускає `pnpm install --frozen-lockfile --prefer-offline` і `pnpm build` всередині VM | Найповільніше, найсильніше доведення з source-checkout  
`prehydrated` | Ви навмисно підготували повторний lease | Вимагає наявних `node_modules` і `dist/`; пропускає install/build | Швидко, але чинно лише для контрольованих оператором теплих lease  
  
GitHub Actions завжди готує checkout кандидата перед запуском VM. Його pnpm store кешується за OS, версією Node і lockfile. Запуск source у VM також використовує `/var/cache/crabbox/pnpm`, коли він наявний.

## Інтерпретація таймінгів

`mantis-slack-desktop-smoke-report.md` містить таймінги фаз:

  * `crabbox.warmup`: запуск хмарного провайдера, готовність desktop/browser і SSH.
  * `crabbox.inspect`: пошук метаданих lease.
  * `credentials.prepare`: отримання lease облікових даних Convex.
  * `crabbox.remote_run`: синхронізація, запуск браузера, install/build OpenClaw або перевірка hydrate, запуск Gateway, знімок екрана та захоплення відео.
  * `artifacts.copy`: rsync назад із VM.


`crabbox.remote_run` може бути позначено як `accepted`, коли Crabbox повертає ненульовий віддалений статус після того, як Mantis скопіював метадані, що доводять, що OpenClaw Gateway живий і setup завершено. Вважайте `accepted` проходженням із поясненням, а не проваленим сценарієм.

Якщо запуск повільний:

  * домінує warmup: prebake або просуньте кращий образ провайдера Crabbox;
  * домінує remote_run у `source`: використайте теплий lease, поліпшіть повторне використання pnpm store або перенесіть передумови машини в образ провайдера;
  * домінує remote_run у `prehydrated`: віддалений workspace насправді не був готовий або setup Gateway/browser/Slack повільний;
  * домінує копіювання артефактів: перевірте розмір відео та вміст каталогу артефактів.


## Контрольний список доказів

Якісний коментар PR має показувати:

  * id сценарію та SHA кандидата;
  * URL запуску GitHub Actions;
  * URL артефакту;
  * inline-знімок екрана;
  * inline-анімований preview, коли доступний;
  * посилання на повне MP4 і обрізане MP4;
  * статус pass/fail;
  * підсумок таймінгів у прикріпленому звіті.


Не commit-іть знімки екрана чи відео в репозиторій. Зберігайте їх в артефактах GitHub Actions або коментарі PR.

## Обробка збоїв

Якщо workflow падає до запуску VM, спершу перевірте job Actions. Типові причини — недовірений `candidate_ref`, відсутні секрети середовища або збій install/build кандидата.

Якщо запуск VM падає, але знімки екрана були скопійовані назад, перевірте:

bashCopy code
[code]
    cat mantis-slack-desktop-smoke-report.mdcat mantis-slack-desktop-smoke-summary.jsoncat slack-desktop-command.logcat openclaw-gateway.logcat chrome.logcat ffmpeg.log
[/code]

Якщо запуск залишив lease, відкрийте VNC командою `crabbox vnc ...` зі звіту. Зупиніть lease після завершення:

bashCopy code
[code]
    crabbox stop --provider aws <cbx_id-or-slug>
[/code]

Якщо вхід Slack протермінувався, відремонтуйте його у VNC на збереженому lease і повторно запустіть із `--lease-id`. Не запікайте цей профіль браузера в образ провайдера.

## Пов’язане

  * [Огляд QA](</uk/concepts/qa-e2e-automation>)
  * [Канал Slack](</uk/channels/slack>)
  * [Тестування](</uk/help/testing>)


Was this useful?YesNo