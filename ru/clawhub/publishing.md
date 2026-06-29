---
title: Публикация
source_url: https://docs.openclaw.ai/ru/clawhub/publishing
scraped_at: 2026-06-29
---

Get started

# Публикация

Публикация отправляет папку Skills или пакет Plugin в ClawHub от имени выбранного владельца. ClawHub проверяет, что ваш токен может публиковать от этого владельца, проверяет метаданные, имя, версию, файлы и сведения об исходном коде, затем сохраняет релиз и запускает автоматические проверки безопасности.

Если проверка завершается ошибкой, ничего не публикуется. Новые релизы также могут не попадать в обычные поверхности установки и скачивания, пока не завершится проверка.

## Skills

Самый простой путь публикации — CLI. Войдите в систему, затем опубликуйте локальную папку Skills:

bashCopy code
[code]
    clawhub loginclawhub skill publish ./my-skill \  --slug my-skill \  --name "My Skill" \  --owner <owner>
[/code]

Используйте `--owner <handle>` при публикации от владельца-организации. Опустите его, чтобы опубликовать от имени аутентифицированного пользователя. Публикация пропускает неизмененное содержимое. Новый Skill начинается с `1.0.0`, а последующие изменения автоматически публикуют следующую патч-версию. Передавайте `--version` только когда нужна явная версия.

Для репозиториев каталога используйте переиспользуемый workflow ClawHub [`skill-publish.yml`](<https://github.com/openclaw/clawhub/blob/main/.github/workflows/skill-publish.yml>). Он вызывает `skill publish` для каждой непосредственной папки Skills в `root` (по умолчанию: `skills`) или только для папки, переданной как `skill_path`.

yamlCopy code
[code]
    jobs:  publish:    uses: openclaw/clawhub/.github/workflows/skill-publish.yml@main    with:      owner: <owner>      dry_run: false    secrets:      clawhub_token: ${{ secrets.CLAWHUB_TOKEN }}
[/code]

Используйте `dry_run: true`, чтобы предварительно просмотреть новые и измененные Skills без публикации.

## Plugins

Plugins используют имена пакетов в стиле npm. Имена пакетов со scope включают владельца в первой части имени:

textCopy code
[code]
    @owner/package-name
[/code]

Scope должен соответствовать выбранному владельцу публикации. Если ваш пакет называется `@openclaw/dronzer`, его можно опубликовать только как `@openclaw`. Если вы публикуете как `@vintageayu`, переименуйте пакет в `@vintageayu/dronzer`.

Это не позволяет пакету заявлять namespace организации, которым издатель не управляет.

Если вы являетесь законным владельцем организации, бренда, scope пакета, handle владельца или namespace, который уже занят или зарезервирован в ClawHub, откройте [issue для заявки на организацию / namespace](<https://github.com/openclaw/clawhub/issues/new?template=org-namespace-claim.yml>) с публичным, неконфиденциальным доказательством. См. [Заявки на организации и namespace](</ru/clawhub/namespace-claims>), чтобы узнать, что включать и что не следует публиковать в публичных issue.

### Перед публикацией Plugin

  * Выберите владельца, который соответствует scope пакета.
  * Включите `openclaw.plugin.json`. Plugins с кодом также требуют `package.json` с `openclaw.compat.pluginApi` и `openclaw.build.openclawVersion`.
  * Чтобы показать пользовательскую иконку карточки Plugin, добавьте `icon` в `openclaw.plugin.json` с любым HTTPS URL изображения.
  * Включите репозиторий исходного кода и метаданные точного коммита либо используйте CLI из checkout, связанного с GitHub, чтобы он мог их обнаружить.
  * Запустите `clawhub package validate <source>` перед публикацией. Для находок по пакету, манифесту, импорту SDK или артефакту см. [Исправления проверки Plugin](</ru/clawhub/plugin-validation-fixes>).
  * Запустите `clawhub package publish <source> --dry-run` перед созданием релиза.
  * Ожидайте, что новые релизы не попадут в публичные поверхности установки, пока не завершатся автоматические проверки безопасности и верификация.


### Доверенная публикация для пакетов

Доверенная публикация пакета настраивается в два шага:

  1. Один раз опубликуйте пакет через обычную ручную или аутентифицированную токеном команду `clawhub package publish`. Это создает строку пакета и устанавливает менеджеров пакета, которые могут менять его конфигурацию доверенного издателя.
  2. Менеджер пакета задает конфигурацию доверенного издателя GitHub Actions:

bashCopy code
[code]
    clawhub package trusted-publisher set @owner/package-name \  --repository owner/repo \  --workflow-filename package-publish.yml
[/code]

После настройки будущие поддерживаемые публикации GitHub Actions могут использовать OIDC/доверенную публикацию без хранения долгоживущего токена ClawHub в репозитории. Настроенные репозиторий и имя workflow должны соответствовать claim OIDC GitHub Actions. Если вы также передаете `--environment <name>`, claim среды GitHub Actions должен точно соответствовать этому имени.

ClawHub проверяет настроенный репозиторий GitHub при задании конфигурации доверенного издателя. Публичные репозитории можно проверить через публичные метаданные GitHub. Для приватных репозиториев ClawHub должен иметь доступ GitHub к этому репозиторию, например через будущую установку GitHub App ClawHub или другую авторизованную интеграцию GitHub.

Текущий переиспользуемый workflow публикации пакетов поддерживает доверенную публикацию без секретов для публикаций `workflow_dispatch`, когда доступно `id-token: write`. Реальные публикации по push тега все еще требуют `clawhub_token`, поэтому оставьте `CLAWHUB_TOKEN` доступным для релизов по тегам, первых публикаций, недоверенных пакетов или аварийных публикаций.

Просмотрите или удалите конфигурацию с помощью:

bashCopy code
[code]
    clawhub package trusted-publisher get @owner/package-nameclawhub package trusted-publisher delete @owner/package-name
[/code]

Удаление конфигурации доверенного издателя — это путь отката. Оно отключает будущий выпуск токенов для доверенной публикации, пока менеджер пакета снова не задаст конфигурацию.

## FAQ

### Scope пакета должен соответствовать выбранному владельцу

Если scope пакета и выбранный владелец не совпадают, ClawHub отклоняет публикацию:

textCopy code
[code]
    Package scope "@openclaw" must match selected owner "@vintageayu".Publish as "@openclaw" or rename this package to "@vintageayu/dronzer".
[/code]

Чтобы исправить это, выберите владельца, указанного scope пакета, либо переименуйте пакет так, чтобы scope соответствовал владельцу, от имени которого вы можете публиковать.

Если имя пакета уже имеет правильный scope, но пакет принадлежит неправильному издателю, вместо этого передайте владение:

shCopy code
[code]
    clawhub package transfer @opik/opik-openclaw --to opik
[/code]

Используйте передачу пакета или Skills только когда у вас есть администраторский доступ и к текущему владельцу, и к целевому издателю. Передача пакета не позволяет публиковать в scope, которым вы не можете управлять.

Если у вас нет доступа к текущему владельцу, но вы считаете, что ваша организация, проект или бренд является законным владельцем namespace, откройте [issue для заявки на организацию / namespace](<https://github.com/openclaw/clawhub/issues/new?template=org-namespace-claim.yml>) с публичным, неконфиденциальным доказательством для проверки сотрудниками. Перед подачей см. [Заявки на организации и namespace](</ru/clawhub/namespace-claims>).

Это защищает namespace организаций. Пакет с именем `@openclaw/dronzer` заявляет namespace `@openclaw`, поэтому публиковать его могут только издатели с доступом к владельцу `@openclaw`.

Was this useful?YesNo

Open issue