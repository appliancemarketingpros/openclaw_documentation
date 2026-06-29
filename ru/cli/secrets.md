---
title: Секреты
source_url: https://docs.openclaw.ai/ru/cli/secrets
scraped_at: 2026-06-29
---

ReferenceCLI commands

# `openclaw secrets`

Используйте `openclaw secrets` для управления SecretRefs и поддержания активного снимка среды выполнения в исправном состоянии.

Роли команд:

  * `reload`: RPC Gateway (`secrets.reload`), который заново разрешает ссылки и заменяет снимок среды выполнения только при полном успехе (без записи конфигурации).
  * `audit`: сканирование только для чтения хранилищ конфигурации, аутентификации и сгенерированных моделей, а также устаревших остатков на наличие открытого текста, неразрешенных ссылок и расхождений приоритета (exec-ссылки пропускаются, если не задан `--allow-exec`).
  * `configure`: интерактивный планировщик для настройки провайдера, сопоставления целей и предварительной проверки (требуется TTY).
  * `apply`: выполнение сохраненного плана (`--dry-run` только для валидации; пробный запуск по умолчанию пропускает exec-проверки, а режим записи отклоняет планы с exec, если не задан `--allow-exec`), затем очистка целевых остатков открытого текста.


Рекомендуемый цикл оператора:

bashCopy code
[code]
    openclaw secrets audit --checkopenclaw secrets configureopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-runopenclaw secrets apply --from /tmp/openclaw-secrets-plan.jsonopenclaw secrets audit --checkopenclaw secrets reload
[/code]

Если ваш план включает SecretRefs/провайдеры `exec`, передайте `--allow-exec` и для пробного запуска, и для команд применения с записью.

Примечание о кодах выхода для CI/шлюзов:

  * `audit --check` возвращает `1` при находках.
  * неразрешенные ссылки возвращают `2`.


Связанные материалы:

  * Руководство по секретам: [Управление секретами](</ru/gateway/secrets>)
  * Поверхность учетных данных: [Поверхность учетных данных SecretRef](</ru/reference/secretref-credential-surface>)
  * Руководство по безопасности: [Безопасность](</ru/gateway/security>)


## Перезагрузка снимка среды выполнения

Заново разрешить ссылки на секреты и атомарно заменить снимок среды выполнения.

bashCopy code
[code]
    openclaw secrets reloadopenclaw secrets reload --jsonopenclaw secrets reload --url ws://127.0.0.1:18789 --token <token>
[/code]

Примечания:

  * Использует RPC-метод Gateway `secrets.reload`.
  * Если разрешение завершается ошибкой, Gateway сохраняет последний заведомо исправный снимок и возвращает ошибку (без частичной активации).
  * JSON-ответ включает `warningCount`.


Параметры:

  * `--url <url>`
  * `--token <token>`
  * `--timeout <ms>`
  * `--json`


## Аудит

Сканировать состояние OpenClaw на наличие:

  * хранения секретов в открытом тексте
  * неразрешенных ссылок
  * расхождений приоритета (учетные данные `auth-profiles.json` затеняют ссылки `openclaw.json`)
  * остатков сгенерированных `agents/*/agent/models.json` (значения `apiKey` провайдера и чувствительные заголовки провайдера)
  * устаревших остатков (записи устаревшего хранилища аутентификации, напоминания OAuth)


Примечание об остатках заголовков:

  * Обнаружение чувствительных заголовков провайдера основано на эвристике имен (распространенные имена и фрагменты заголовков аутентификации/учетных данных, такие как `authorization`, `x-api-key`, `token`, `secret`, `password` и `credential`).

bashCopy code
[code]
    openclaw secrets auditopenclaw secrets audit --checkopenclaw secrets audit --jsonopenclaw secrets audit --allow-exec
[/code]

Поведение выхода:

  * `--check` завершается с ненулевым кодом при находках.
  * неразрешенные ссылки завершаются с ненулевым кодом более высокого приоритета.


Основные элементы формы отчета:

  * `status`: `clean | findings | unresolved`
  * `resolution`: `refsChecked`, `skippedExecRefs`, `resolvabilityComplete`
  * `summary`: `plaintextCount`, `unresolvedRefCount`, `shadowedRefCount`, `legacyResidueCount`
  * коды находок: 
    * `PLAINTEXT_FOUND`
    * `REF_UNRESOLVED`
    * `REF_SHADOWED`
    * `LEGACY_RESIDUE`


## Настройка (интерактивный помощник)

Интерактивно сформировать изменения провайдеров и SecretRef, выполнить предварительную проверку и при необходимости применить:

bashCopy code
[code]
    openclaw secrets configureopenclaw secrets configure --plan-out /tmp/openclaw-secrets-plan.jsonopenclaw secrets configure --apply --yesopenclaw secrets configure --providers-onlyopenclaw secrets configure --skip-provider-setupopenclaw secrets configure --agent opsopenclaw secrets configure --json
[/code]

Поток:

  * Сначала настройка провайдера (`add/edit/remove` для псевдонимов `secrets.providers`).
  * Затем сопоставление учетных данных (выбор полей и назначение ссылок `{source, provider, id}`).
  * В конце предварительная проверка и необязательное применение.


Флаги:

  * `--providers-only`: настроить только `secrets.providers`, пропустить сопоставление учетных данных.
  * `--skip-provider-setup`: пропустить настройку провайдера и сопоставить учетные данные с существующими провайдерами.
  * `--agent <id>`: ограничить обнаружение целей и записи `auth-profiles.json` одним хранилищем агента.
  * `--allow-exec`: разрешить проверки exec SecretRef во время предварительной проверки/применения (может выполнять команды провайдера).


Примечания:

  * Требует интерактивный TTY.
  * Нельзя сочетать `--providers-only` с `--skip-provider-setup`.
  * `configure` выбирает целями поля с секретами в `openclaw.json`, а также `auth-profiles.json` для выбранной области агента.
  * `configure` поддерживает создание новых сопоставлений `auth-profiles.json` прямо в потоке выбора.
  * Каноническая поддерживаемая поверхность: [Поверхность учетных данных SecretRef](</ru/reference/secretref-credential-surface>).
  * Перед применением выполняется предварительное разрешение.
  * Если предварительная проверка/применение включает exec-ссылки, оставьте `--allow-exec` включенным для обоих шагов.
  * Сгенерированные планы по умолчанию используют параметры очистки (`scrubEnv`, `scrubAuthProfilesForProviderTargets`, `scrubLegacyAuthJson` все включены).
  * Путь применения необратим для очищенных значений открытого текста.
  * Без `--apply` CLI все равно запрашивает `Apply this plan now?` после предварительной проверки.
  * С `--apply` (и без `--yes`) CLI запрашивает дополнительное необратимое подтверждение.
  * `--json` печатает план и отчет предварительной проверки, но команда все равно требует интерактивный TTY.


Примечание о безопасности exec-провайдера:

  * Установки Homebrew часто предоставляют бинарные файлы через символические ссылки в `/opt/homebrew/bin/*`.
  * Устанавливайте `allowSymlinkCommand: true` только когда это необходимо для доверенных путей менеджера пакетов, и сочетайте его с `trustedDirs` (например, `["/opt/homebrew"]`).
  * В Windows, если проверка ACL недоступна для пути провайдера, OpenClaw отказывает безопасно. Только для доверенных путей установите `allowInsecurePath: true` для этого провайдера, чтобы обойти проверки безопасности пути.


## Применение сохраненного плана

Применить или предварительно проверить ранее сгенерированный план:

bashCopy code
[code]
    openclaw secrets apply --from /tmp/openclaw-secrets-plan.jsonopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-runopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --dry-run --allow-execopenclaw secrets apply --from /tmp/openclaw-secrets-plan.json --json
[/code]

Поведение exec:

  * `--dry-run` валидирует предварительную проверку без записи файлов.
  * проверки exec SecretRef по умолчанию пропускаются при пробном запуске.
  * режим записи отклоняет планы, содержащие exec SecretRefs/провайдеры, если не задан `--allow-exec`.
  * Используйте `--allow-exec`, чтобы явно включить проверки/выполнение exec-провайдера в любом режиме.


Подробности контракта плана (разрешенные целевые пути, правила валидации и семантика ошибок):

  * [Контракт плана применения секретов](</ru/gateway/secrets-plan-contract>)


Что может обновлять `apply`:

  * `openclaw.json` (цели SecretRef + добавление/обновление и удаление провайдеров)
  * `auth-profiles.json` (очистка целевых провайдеров)
  * устаревшие остатки `auth.json`
  * известные ключи секретов `~/.openclaw/.env`, значения которых были мигрированы


## Почему нет резервных копий для отката

`secrets apply` намеренно не записывает резервные копии для отката, содержащие старые значения открытого текста.

Безопасность обеспечивается строгой предварительной проверкой и почти атомарным применением с попыткой восстановления в памяти при ошибке.

## Пример

bashCopy code
[code]
    openclaw secrets audit --checkopenclaw secrets configureopenclaw secrets audit --check
[/code]

Если `audit --check` все еще сообщает находки открытого текста, обновите оставшиеся указанные целевые пути и повторно запустите аудит.

## Связанные материалы

  * [Справочник CLI](</ru/cli>)
  * [Управление секретами](</ru/gateway/secrets>)


Was this useful?YesNo

Open issue