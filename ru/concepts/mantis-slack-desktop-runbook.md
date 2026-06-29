---
title: Операционное руководство Mantis для настольного клиента Slack
source_url: https://docs.openclaw.ai/ru/concepts/mantis-slack-desktop-runbook
scraped_at: 2026-06-29
---

Get started

Mantis Slack desktop QA — это канал реального UI для ошибок класса Slack, которым нужны рабочий стол Linux, аварийный доступ через VNC, Slack Web, настоящий OpenClaw gateway, скриншоты, видео и комментарий с доказательствами в PR.

Используйте его, когда модульные тесты или headless live-канал Slack не могут доказать ошибку.

## Модель хранения

Mantis использует три разных уровня хранения:

  * Образ провайдера: принадлежит Crabbox и хранится в учетной записи облачного провайдера. Он содержит возможности машины, такие как Chrome/Chromium, ffmpeg, scrot, Node/corepack/pnpm, нативные инструменты сборки и пустые каталоги кеша.
  * Состояние теплой аренды: принадлежит текущей операторской сессии. Оно может содержать профиль браузера с выполненным входом, `/var/cache/crabbox/pnpm` и подготовленный checkout исходного кода, пока аренда активна.
  * Артефакты Mantis: принадлежат запуску OpenClaw. Они находятся в `.artifacts/qa-e2e/mantis/...`, затем GitHub Actions загружает их, а Mantis GitHub App комментирует встроенные доказательства в PR.


Никогда не помещайте секреты, cookie браузера, состояние входа в Slack, checkout репозитория, `node_modules` или `dist/` в заранее собранный образ провайдера.

## GitHub dispatch

Запустите workflow из `main`:

bashCopy code
[code]
    gh workflow run mantis-slack-desktop-smoke.yml \  --ref main \  -f candidate_ref=<trusted-ref-or-sha> \  -f pr_number=<pr-number> \  -f scenario_id=slack-canary \  -f crabbox_provider=aws \  -f keep_vm=false \  -f hydrate_mode=source
[/code]

Разрешенные значения `candidate_ref` намеренно узкие, потому что workflow использует реальные учетные данные: текущая история `main`, release-теги или head открытого PR из `openclaw/openclaw`.

Workflow записывает:

  * загруженный артефакт: `mantis-slack-desktop-smoke-<run-id>-<attempt>`;
  * встроенный комментарий PR от Mantis GitHub App;
  * `slack-desktop-smoke.png`;
  * `slack-desktop-smoke.mp4`;
  * `slack-desktop-smoke-preview.gif`;
  * `slack-desktop-smoke-change.mp4`;
  * `mantis-slack-desktop-smoke-summary.json`;
  * `mantis-slack-desktop-smoke-report.md`;
  * удаленные логи, такие как `slack-desktop-command.log`, `openclaw-gateway.log`, `chrome.log` и `ffmpeg.log`.


Комментарий PR обновляется на месте через скрытый `<!-- mantis-slack-desktop-smoke -->` marker.

## Локальный CLI

Холодное доказательство из исходного кода:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --credential-source convex \  --credential-role maintainer \  --provider-mode live-frontier \  --model openai/gpt-5.4 \  --alt-model openai/gpt-5.4 \  --scenario slack-canary \  --hydrate-mode source
[/code]

Оставить VM для аварийного доступа через VNC:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --gateway-setup \  --scenario slack-canary \  --keep-lease
[/code]

Открыть VNC:

bashCopy code
[code]
    crabbox vnc --provider aws --id <cbx_id> --open
[/code]

Повторно использовать теплую аренду:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --lease-id <cbx_id-or-slug> \  --gateway-setup \  --scenario slack-canary \  --hydrate-mode source
[/code]

Используйте `--hydrate-mode prehydrated` только когда в повторно используемом удаленном рабочем пространстве уже есть `node_modules` и собранный `dist/`. Mantis завершается закрыто, если они отсутствуют.

Доказать нативный UI одобрения Slack:

bashCopy code
[code]
    pnpm openclaw qa mantis slack-desktop-smoke \  --provider aws \  --class standard \  --approval-checkpoints \  --credential-source convex \  --credential-role maintainer \  --hydrate-mode source
[/code]

Режим контрольных точек одобрения взаимоисключается с `--gateway-setup`. Он запускает opt-in сценарии `slack-approval-exec-native` и `slack-approval-plugin-native`, если вы не передали явные флаги `--scenario` для контрольных точек одобрения; другие сценарии Slack отклоняются до запуска VM. Slack QA runner записывает каждый JSON-файл контрольной точки из реального сообщения Slack API, которое он наблюдал, затем удаленный watcher рендерит этот снимок сообщения в `approval-checkpoints/<scenario>-pending.png` и `approval-checkpoints/<scenario>-resolved.png`. Запуск завершается ошибкой, если какой-либо JSON контрольной точки, доказательство сообщения, ack JSON или отрендеренный скриншот отсутствует или пуст.

Холодные аренды GitHub Actions не имеют cookie Slack Web, поэтому их захват браузера может попасть на страницу входа Slack. Для доказательства контрольных точек одобрения доверяйте отрендеренным изображениям контрольных точек и артефактам Slack QA, а не `slack-desktop-smoke.png`. Используйте сохраненную теплую аренду с вручную выполненным входом в профиль Slack Web только когда сам скриншот браузера должен показывать Slack Web.

## Режимы hydrate

Режим | Когда использовать | Удаленное поведение | Компромисс  
---|---|---|---  
`source` | Обычное доказательство PR, холодные машины, CI | Запускает `pnpm install --frozen-lockfile --prefer-offline` и `pnpm build` внутри VM | Самое медленное, самое сильное доказательство checkout исходного кода  
`prehydrated` | Вы намеренно подготовили повторно используемую аренду | Требует существующие `node_modules` и `dist/`; пропускает install/build | Быстро, но допустимо только для контролируемых оператором теплых аренд  
  
GitHub Actions всегда готовит checkout кандидата перед запуском VM. Его pnpm store кешируется по ОС, версии Node и lockfile. Запуск VM из исходного кода также использует `/var/cache/crabbox/pnpm`, когда он присутствует.

## Интерпретация времени

`mantis-slack-desktop-smoke-report.md` включает время фаз:

  * `crabbox.warmup`: загрузка облачного провайдера, готовность рабочего стола/браузера и SSH.
  * `crabbox.inspect`: поиск metadata аренды.
  * `credentials.prepare`: получение аренды учетных данных Convex.
  * `crabbox.remote_run`: синхронизация, запуск браузера, установка/сборка OpenClaw или проверка hydrate, запуск gateway, скриншот и запись видео.
  * `artifacts.copy`: rsync обратно из VM.


`crabbox.remote_run` может быть помечен как `accepted`, когда Crabbox возвращает ненулевой удаленный status после того, как Mantis скопировал metadata, доказывающие, что либо настройка OpenClaw gateway завершилась, либо сама команда Slack QA успешно завершилась. Считайте `accepted` прохождением с объяснением, а не проваленным сценарием.

Если запуск медленный:

  * доминирует warmup: заранее соберите или продвиньте более подходящий образ провайдера Crabbox;
  * `remote_run` доминирует в `source`: используйте теплую аренду, улучшите повторное использование pnpm store или перенесите предварительные требования машины в образ провайдера;
  * `remote_run` доминирует в `prehydrated`: удаленное рабочее пространство на самом деле не было готово, или настройка gateway/browser/Slack медленная;
  * доминирует копирование артефактов: проверьте размер видео и содержимое каталога артефактов.


## Чеклист доказательств

Хороший комментарий PR должен показывать:

  * id сценария и SHA кандидата;
  * URL запуска GitHub Actions;
  * URL артефакта;
  * встроенный скриншот контрольной точки одобрения или скриншот Slack Web из теплой аренды с выполненным входом;
  * встроенный анимированный preview, когда доступен;
  * ссылки на полный MP4 и обрезанный MP4;
  * status pass/fail;
  * сводку времени в приложенном отчете.


Не коммитьте скриншоты или видео в репозиторий. Храните их в артефактах GitHub Actions или комментарии PR.

## Обработка сбоев

Если workflow завершается ошибкой до запуска VM, сначала проверьте job Actions. Типичные причины — недоверенный `candidate_ref`, отсутствующие environment secrets или сбой install/build кандидата.

Если запуск VM завершается ошибкой, но скриншоты были скопированы обратно, проверьте:

bashCopy code
[code]
    cat mantis-slack-desktop-smoke-report.mdcat mantis-slack-desktop-smoke-summary.jsoncat slack-desktop-command.logcat openclaw-gateway.logcat chrome.logcat ffmpeg.log
[/code]

Если запуск сохранил аренду, откройте VNC командой `crabbox vnc ...` из отчета. Остановите аренду, когда закончите:

bashCopy code
[code]
    crabbox stop --provider aws <cbx_id-or-slug>
[/code]

Если срок входа в Slack истек, исправьте его в VNC на сохраненной аренде и перезапустите с `--lease-id`. Не запекайте этот профиль браузера в образ провайдера.

## Связанные материалы

  * [Обзор QA](</ru/concepts/qa-e2e-automation>)
  * [Канал Slack](</ru/channels/slack>)
  * [Тестирование](</ru/help/testing>)


Was this useful?YesNo

Open issue