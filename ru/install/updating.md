---
title: Обновление
source_url: https://docs.openclaw.ai/ru/install/updating
scraped_at: 2026-06-29
---

InstallMaintenance

Поддерживайте OpenClaw в актуальном состоянии.

## Рекомендуется: `openclaw update`

Самый быстрый способ обновления. Он определяет тип вашей установки (npm или git), получает последнюю версию, запускает `openclaw doctor` и перезапускает Gateway.

bashCopy code
[code]
    openclaw update
[/code]

Чтобы переключить каналы или выбрать конкретную версию:

bashCopy code
[code]
    openclaw update --channel betaopenclaw update --channel devopenclaw update --dry-run   # preview without applying
[/code]

`openclaw update` не принимает `--verbose`. Для диагностики обновления используйте `--dry-run`, чтобы предварительно посмотреть запланированные действия, `--json` для структурированных результатов или `openclaw update status --json`, чтобы проверить состояние канала и доступности. У установщика есть собственный флаг `--verbose`, но этот флаг не является частью `openclaw update`.

`--channel beta` предпочитает beta, но runtime откатывается к stable/latest, когда тег beta отсутствует или старше последнего стабильного выпуска. Используйте `--tag beta`, если вам нужен исходный npm dist-tag beta для разового обновления пакета.

Используйте `--channel dev` для постоянного движущегося checkout ветки GitHub `main`. Для обновлений пакетов `--tag main` сопоставляется с `github:openclaw/openclaw#main` для одного запуска, а спецификации источников GitHub/git упаковываются во временный tarball перед staged npm install.

Для управляемых плагинов fallback beta-канала является предупреждением: обновление ядра все равно может успешно завершиться, пока плагин использует свой записанный default/latest выпуск, потому что beta-версия плагина недоступна.

См. [Каналы разработки](</ru/install/development-channels>), чтобы узнать семантику каналов.

## Переключение между установками npm и git

Используйте каналы, когда хотите изменить тип установки. Средство обновления сохраняет ваши состояние, конфигурацию, учетные данные и рабочую область в `~/.openclaw`; оно изменяет только то, какую установку кода OpenClaw используют CLI и Gateway.

bashCopy code
[code]
    # npm package install -> editable git checkoutopenclaw update --channel dev # git checkout -> npm package installopenclaw update --channel stable
[/code]

Сначала запустите с `--dry-run`, чтобы предварительно посмотреть точное переключение режима установки:

bashCopy code
[code]
    openclaw update --channel dev --dry-runopenclaw update --channel stable --dry-run
[/code]

Канал `dev` обеспечивает git checkout, собирает его и устанавливает глобальный CLI из этого checkout. Каналы `stable` и `beta` используют установки пакетов. Если Gateway уже установлен, `openclaw update` обновляет метаданные службы и перезапускает ее, если вы не передали `--no-restart`.

Для установок пакетов с управляемой службой Gateway `openclaw update` нацеливается на корень пакета, используемый этой службой. Если shell-команда `openclaw` приходит из другой установки, средство обновления выводит оба корня и путь Node управляемой службы. Обновление пакета использует менеджер пакетов, которому принадлежит корень службы, и проверяет Node управляемой службы относительно engine целевого выпуска перед заменой пакета.

## Альтернатива: повторно запустить установщик

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash
[/code]

Добавьте `--no-onboard`, чтобы пропустить onboarding. Чтобы принудительно выбрать конкретный тип установки через установщик, передайте `--install-method git --no-onboard` или `--install-method npm --no-onboard`.

Если `openclaw update` завершается ошибкой после этапа установки npm-пакета, повторно запустите установщик. Установщик не вызывает старое средство обновления; он напрямую запускает установку глобального пакета и может восстановить частично обновленную npm-установку.

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm
[/code]

Чтобы закрепить восстановление за конкретной версией или dist-tag, добавьте `--version`:

bashCopy code
[code]
    curl -fsSL https://openclaw.ai/install.sh | bash -s -- --install-method npm --version <version-or-dist-tag>
[/code]

## Альтернатива: ручной npm, pnpm или bun

bashCopy code
[code]
    npm i -g openclaw@latest
[/code]

Предпочитайте `openclaw update` для supervised-установок, потому что он может согласовать замену пакета с работающей службой Gateway. Если вы обновляете supervised-установку вручную, остановите управляемый Gateway до запуска менеджера пакетов. Менеджеры пакетов заменяют файлы на месте, и работающий Gateway иначе может попытаться загрузить файлы ядра или плагинов, пока дерево пакета временно заменено лишь частично. Перезапустите Gateway после завершения работы менеджера пакетов, чтобы служба подхватила новую установку.

Для root-owned глобальной установки Linux на уровне системы, если `openclaw update` завершается ошибкой с `EACCES` и вы восстанавливаете установку через системный npm, держите Gateway остановленным на протяжении ручной замены пакета. Используйте те же флаги профиля `openclaw` или окружение, которые вы обычно используете для этого Gateway. Замените `/usr/bin/npm` на системный npm, которому принадлежит root-owned глобальный prefix на вашем хосте:

bashCopy code
[code]
    openclaw gateway stopsudo /usr/bin/npm i -g openclaw@latestopenclaw gateway install --forceopenclaw gateway restart
[/code]

Затем проверьте службу:

bashCopy code
[code]
    openclaw --versioncurl -fsS http://127.0.0.1:18789/readyzopenclaw plugins list --jsonopenclaw gateway status --deep --jsonopenclaw doctor --lint --json
[/code]

Когда `openclaw update` управляет глобальной npm-установкой, он сначала устанавливает целевую версию во временный npm prefix, проверяет инвентарь упакованного `dist`, затем заменяет чистое дерево пакета в реальном глобальном prefix. Это предотвращает наложение npm нового пакета поверх устаревших файлов из старого пакета. Если команда установки завершается ошибкой, OpenClaw повторяет попытку один раз с `--omit=optional`. Эта повторная попытка помогает хостам, где native optional-зависимости не могут скомпилироваться, при этом сохраняя видимой исходную ошибку, если fallback тоже завершается ошибкой.

Команды обновления npm и обновления плагинов, управляемые OpenClaw, также очищают quarantine npm `min-release-age` для дочернего процесса npm. npm может сообщать эту политику как производный cutoff `before`; оба полезны для общих политик supply-chain quarantine, но явное обновление OpenClaw означает: «установить выбранный выпуск OpenClaw сейчас».

bashCopy code
[code]
    pnpm add -g openclaw@latest
[/code]

bashCopy code
[code]
    bun add -g openclaw@latest
[/code]

### Расширенные темы установки npm

Read-only package tree

OpenClaw рассматривает упакованные глобальные установки как доступные только для чтения во время выполнения, даже если каталог глобального пакета доступен текущему пользователю для записи. Установки пакетов Plugin находятся в принадлежащих OpenClaw корнях npm/git в каталоге пользовательской конфигурации, а запуск Gateway не изменяет дерево пакета OpenClaw.

Некоторые конфигурации npm в Linux устанавливают глобальные пакеты в каталоги, принадлежащие root, например `/usr/lib/node_modules/openclaw`. OpenClaw поддерживает такую структуру, потому что команды установки/обновления Plugin записывают данные за пределами этого каталога глобального пакета.

Hardened systemd units

Предоставьте OpenClaw доступ на запись к его корням конфигурации/состояния, чтобы явные установки Plugin, обновления Plugin и очистка doctor могли сохранять свои изменения:

iniCopy code
[code]
    ReadWritePaths=/var/lib/openclaw /home/openclaw/.openclaw /tmp
[/code]

Disk-space preflight

Перед обновлениями пакетов и явными установками Plugin OpenClaw пытается выполнить максимально возможную проверку свободного места на целевом томе. При нехватке места выводится предупреждение с проверенным путем, но обновление не блокируется, потому что квоты файловой системы, снимки и сетевые тома могут измениться после проверки. Фактическая установка через менеджер пакетов и проверка после установки остаются авторитетными.

## Автообновление

Автообновление по умолчанию выключено. Включите его в `~/.openclaw/openclaw.json`:

json5Copy code
[code]
    {  update: {    channel: "stable",    auto: {      enabled: true,      stableDelayHours: 6,      stableJitterHours: 12,      betaCheckIntervalHours: 1,    },  },}
[/code]

Канал | Поведение  
---|---  
`stable` | Ожидает `stableDelayHours`, затем применяет обновление с детерминированным джиттером в пределах `stableJitterHours` (постепенное развертывание).  
`beta` | Проверяет каждые `betaCheckIntervalHours` (по умолчанию: каждый час) и применяет сразу.  
`dev` | Автоматическое применение отсутствует. Используйте `openclaw update` вручную.  
  
Gateway также записывает подсказку об обновлении при запуске (отключается через `update.checkOnStart: false`). Для отката версии или восстановления после инцидента задайте `OPENCLAW_NO_AUTO_UPDATE=1` в окружении Gateway, чтобы блокировать автоматическое применение даже при настроенном `update.auto.enabled`. Подсказки об обновлении при запуске все еще могут выполняться, если также не отключен `update.checkOnStart`.

Обновления через менеджер пакетов, запрошенные через обработчик live control-plane Gateway, не заменяют дерево пакета внутри запущенного процесса Gateway. В управляемых сервисных установках Gateway запускает отсоединенную передачу управления, завершает работу и позволяет обычному пути CLI `openclaw update --yes --json` остановить сервис, заменить пакет, обновить метаданные сервиса, перезапустить, проверить версию Gateway и доступность, а также по возможности восстановить установленный, но не загруженный macOS LaunchAgent. Если Gateway не может безопасно выполнить такую передачу управления, `update.run` сообщает безопасную shell-команду вместо запуска менеджера пакетов внутри процесса.

## После обновления

### Запустите doctor

bashCopy code
[code]
    openclaw doctor
[/code]

Мигрирует конфигурацию, проверяет политики DM и проверяет состояние Gateway. Подробности: [Doctor](</ru/gateway/doctor>)

### Перезапустите Gateway

bashCopy code
[code]
    openclaw gateway restart
[/code]

### Проверьте

bashCopy code
[code]
    openclaw health
[/code]

## Откат

### Закрепите версию (npm)

bashCopy code
[code]
    npm i -g openclaw@<version>openclaw doctoropenclaw gateway restart
[/code]

### Закрепите коммит (исходный код)

bashCopy code
[code]
    git fetch origingit checkout "$(git rev-list -n 1 --before=\"2026-01-01\" origin/main)"pnpm install && pnpm buildopenclaw gateway restart
[/code]

Чтобы вернуться к последней версии: `git checkout main && git pull`.

## Если вы застряли

  * Снова запустите `openclaw doctor` и внимательно прочитайте вывод.
  * Для `openclaw update --channel dev` в checkout исходного кода средство обновления автоматически подготавливает `pnpm` при необходимости. Если вы видите ошибку начальной подготовки pnpm/corepack, установите `pnpm` вручную (или снова включите `corepack`) и повторно запустите обновление.
  * Проверьте: [Устранение неполадок](</ru/gateway/troubleshooting>)
  * Спросите в Discord: <https://discord.gg/clawd>


## Связанные материалы

  * [Обзор установки](</ru/install>): все способы установки.
  * [Doctor](</ru/gateway/doctor>): проверки состояния после обновлений.
  * [Миграция](</ru/install/migrating>): руководства по миграции между основными версиями.


Was this useful?YesNo

Open issue