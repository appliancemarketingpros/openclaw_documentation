---
title: Повна валідація релізу
source_url: https://docs.openclaw.ai/uk/reference/full-release-validation
scraped_at: 2026-05-25
---

`Full Release Validation` — це парасольковий процес релізу. Це єдина ручна точка входу для передрелізного підтвердження, але більшість роботи виконується в дочірніх робочих процесах, щоб збій окремого середовища можна було перезапустити без повторного запуску всього релізу.

Запускайте його з довіреного посилання на робочий процес, зазвичай `main`, і передавайте релізну гілку, тег або повний SHA коміту як `ref`:

bashCopy code
[code]
    gh workflow run full-release-validation.yml \  --ref main \  -f ref=release/YYYY.M.D \  -f provider=openai \  -f mode=both \  -f release_profile=stable
[/code]

Дочірні робочі процеси використовують довірене посилання на робочий процес для тестового стенда, а вхідний параметр `ref` — для кандидата, який перевіряється. Це дає змогу мати нову логіку валідації під час перевірки старішої релізної гілки або тегу.

За замовчуванням `release_profile=stable` запускає блокувальні для релізу лінії та пропускає вичерпний live/Docker soak. Передайте `run_release_soak=true`, щоб включити soak-лінії у стабільному запуску. `release_profile=full` завжди вмикає soak-лінії, щоб широкий консультаційний профіль ніколи непомітно не втрачав покриття.

Package Acceptance зазвичай збирає tarball кандидата з розв’язаного `ref`, включно із запусками за повним SHA, ініційованими через `pnpm ci:full-release`. Після публікації beta передайте `release_package_spec=openclaw@YYYY.M.D-beta.N`, щоб повторно використати відправлений npm-пакет у перевірках релізу, Package Acceptance, cross-OS, release-path Docker і package Telegram. Використовуйте `package_acceptance_package_spec` лише тоді, коли Package Acceptance має навмисно підтвердити інший пакет.

## Етапи верхнього рівня

Етап | Подробиці  
---|---  
Розв’язання цілі | **Завдання:** `Resolve target ref`  
**Дочірній робочий процес:** немає |   
**Підтверджує:** розв’язує релізну гілку, тег або повний SHA коміту й записує вибрані вхідні параметри. |   
**Повторний запуск:** перезапустіть парасольковий процес, якщо це завершується з помилкою. |   
Vitest і звичайний CI | **Завдання:** `Run normal full CI`  
**Дочірній робочий процес:** `CI` |   
**Підтверджує:** ручний повний граф CI для цільового ref, включно з лініями Linux Node, шардами вбудованих Plugin, контрактами каналів, сумісністю Node 22, `check`, `check-additional`, build smoke, перевірками документації, Python skills, Windows, macOS, Control UI i18n і Android через парасольковий процес. |   
**Повторний запуск:** `rerun_group=ci`. |   
Передреліз Plugin | **Завдання:** `Run plugin prerelease validation`  
**Дочірній робочий процес:** `Plugin Prerelease` |   
**Підтверджує:** статичні перевірки Plugin лише для релізу, агентне покриття Plugin, повні шарди пакетів розширень, передрелізні Docker-лінії Plugin і неблокувальний артефакт `plugin-inspector-advisory` для тріажу сумісності. |   
**Повторний запуск:** `rerun_group=plugin-prerelease`. |   
Перевірки релізу | **Завдання:** `Run release/live/Docker/QA validation`  
**Дочірній робочий процес:** `OpenClaw Release Checks` |   
**Підтверджує:** install smoke, перевірки пакета cross-OS, Package Acceptance, паритет QA Lab, live Matrix і live Telegram. З `run_release_soak=true` або `release_profile=full` також запускає вичерпні live/E2E набори та release-path фрагменти Docker. |   
**Повторний запуск:** `rerun_group=release-checks` або вужчий дескриптор release-checks. |   
Артефакт пакета | **Завдання:** `Prepare release package artifact`  
**Дочірній робочий процес:** немає |   
**Підтверджує:** створює батьківський tarball `release-package-under-test` достатньо рано для перевірок, орієнтованих на пакет, яким не потрібно чекати на `OpenClaw Release Checks`. |   
**Повторний запуск:** перезапустіть парасольковий процес або надайте `release_package_spec` для повторних запусків опублікованого пакета. |   
Package Telegram | **Завдання:** `Run package Telegram E2E`  
**Дочірній робочий процес:** `NPM Telegram Beta E2E` |   
**Підтверджує:** підтвердження пакета Telegram на основі батьківського артефакта для `rerun_group=all` з `release_profile=full` або підтвердження Telegram для опублікованого пакета, коли задано `release_package_spec` чи `npm_telegram_package_spec`. |   
**Повторний запуск:** `rerun_group=npm-telegram` з `release_package_spec` або `npm_telegram_package_spec`. |   
Верифікатор парасолькового процесу | **Завдання:** `Verify full validation`  
**Дочірній робочий процес:** немає |   
**Підтверджує:** повторно перевіряє записані висновки дочірніх запусків і додає таблиці найповільніших завдань із дочірніх робочих процесів. |   
**Повторний запуск:** перезапустіть лише це завдання після повторного запуску невдалого дочірнього процесу до зеленого стану. |   
  
Для `ref=main` і `rerun_group=all` новіший парасольковий процес замінює старіший. Коли батьківський процес скасовано, його монітор скасовує всі дочірні робочі процеси, які він уже запустив. Запуски валідації релізних гілок і тегів за замовчуванням не скасовують один одного.

## Етапи перевірок релізу

`OpenClaw Release Checks` — найбільший дочірній робочий процес. Він один раз розв’язує ціль і готує спільний артефакт `release-package-under-test`, коли він потрібен етапам, орієнтованим на пакет або Docker.

Етап | Подробиці  
---|---  
Ціль релізу | **Завдання:** `Resolve target ref`  
**Базовий workflow:** немає |   
**Тести:** вибраний ref, необов’язковий очікуваний SHA, профіль, група повторного запуску та фокусований фільтр live-набору. |   
**Повторний запуск:** `rerun_group=release-checks`. |   
Артефакт пакета | **Завдання:** `Prepare release package artifact`  
**Базовий workflow:** немає |   
**Тести:** пакує або знаходить один кандидатний tarball і завантажує `release-package-under-test` для подальших перевірок, що працюють із пакетом. |   
**Повторний запуск:** відповідний пакет, cross-OS або група live/E2E. |   
Install smoke | **Завдання:** `Run install smoke`  
**Базовий workflow:** `Install Smoke` |   
**Тести:** повний шлях встановлення з повторним використанням smoke-образу кореневого Dockerfile, встановлення QR-пакета, root і gateway Docker smoke, Docker-тести інсталятора, Bun global install image-provider smoke, а також швидкий bundled-plugin install/uninstall E2E. |   
**Повторний запуск:** `rerun_group=install-smoke`. |   
Cross-OS | **Завдання:** `cross_os_release_checks`  
**Базовий workflow:** `OpenClaw Cross-OS Release Checks (Reusable)` |   
**Тести:** гілки свіжого встановлення та оновлення на Linux, Windows і macOS для вибраного провайдера й режиму, з використанням кандидатного tarball і базового пакета. |   
**Повторний запуск:** `rerun_group=cross-os`. |   
Репозиторій і live E2E | **Завдання:** `Run repo/live E2E validation`  
**Базовий workflow:** `OpenClaw Live And E2E Checks (Reusable)` |   
**Тести:** repository E2E, live cache, OpenAI websocket streaming, native live provider і Plugin shards, а також Docker-backed live model/backend/gateway harnesses, вибрані через `release_profile`. |   
**Запуски:** `run_release_soak=true`, `release_profile=full` або фокусований `rerun_group=live-e2e`. |   
**Повторний запуск:** `rerun_group=live-e2e`, необов’язково з `live_suite_filter`. |   
Docker release path | **Завдання:** `Run Docker release-path validation`  
**Базовий workflow:** `OpenClaw Live And E2E Checks (Reusable)` |   
**Тести:** release-path Docker chunks для спільного артефакта пакета. |   
**Запуски:** `run_release_soak=true`, `release_profile=full` або фокусований `rerun_group=live-e2e`. |   
**Повторний запуск:** `rerun_group=live-e2e`. |   
Package Acceptance | **Завдання:** `Run package acceptance`  
**Базовий workflow:** `Package Acceptance` |   
**Тести:** offline Plugin package fixtures, оновлення Plugin, mock-OpenAI Telegram package acceptance і перевірки published-upgrade survivor для того самого tarball. Блокувальні перевірки релізу використовують типову останню опубліковану baseline; soak-перевірки розширюються до кожного stable npm-релізу від `2026.4.23` включно плюс fixtures для повідомлених проблем. |   
**Повторний запуск:** `rerun_group=package`. |   
Паритет QA | **Завдання:** `Run QA Lab parity lane` і `Run QA Lab parity report`  
**Базовий workflow:** прямі завдання |   
**Тести:** кандидатні та базові agentic parity packs, потім звіт про паритет. |   
**Повторний запуск:** `rerun_group=qa-parity` або `rerun_group=qa`. |   
QA live Matrix | **Завдання:** `Run QA Lab live Matrix lane`  
**Базовий workflow:** пряме завдання |   
**Тести:** швидкий live Matrix QA profile в середовищі `qa-live-shared`. |   
**Повторний запуск:** `rerun_group=qa-live` або `rerun_group=qa`. |   
QA live Telegram | **Завдання:** `Run QA Lab live Telegram lane`  
**Базовий workflow:** пряме завдання |   
**Тести:** live Telegram QA з Convex CI credential leases. |   
**Повторний запуск:** `rerun_group=qa-live` або `rerun_group=qa`. |   
Перевіряльник релізу | **Завдання:** `Verify release checks`  
**Базовий workflow:** немає |   
**Тести:** обов’язкові release-check jobs для вибраної групи повторного запуску. |   
**Повторний запуск:** повторіть після успішного проходження фокусованих дочірніх завдань. |   
  
## Частини Docker release-path

Етап Docker release-path запускає ці частини, коли `live_suite_filter` порожній:

Частина | Покриття  
---|---  
`core` | Core Docker release-path smoke lanes.  
`package-update-openai` | Поведінка встановлення/оновлення пакета OpenAI, встановлення Codex на вимогу та виклики інструментів Chat Completions.  
`package-update-anthropic` | Поведінка встановлення й оновлення пакета Anthropic.  
`package-update-core` | Нейтральна до провайдера поведінка пакета й оновлення.  
`plugins-runtime-plugins` | Runtime-гілки Plugin, які перевіряють поведінку Plugin.  
`plugins-runtime-services` | Service-backed і live runtime-гілки Plugin; включає OpenWebUI за запитом.  
`plugins-runtime-install-a` through `plugins-runtime-install-h` | Пакети встановлення/runtime Plugin, розділені для паралельної валідації релізу.  
  
Використовуйте цільовий `docker_lanes=<lane[,lane]>` у reusable live/E2E workflow, коли збій стався лише в одній Docker-гілці. Артефакти релізу містять команди повторного запуску для кожної гілки з артефактом пакета та вхідними даними повторного використання образу, коли вони доступні.

## Профілі релізу

`release_profile` здебільшого керує широтою live/provider усередині перевірок релізу. Він не прибирає звичайний full CI, Plugin Prerelease, install smoke, package acceptance або QA Lab. Для `stable` вичерпні repo/live E2E та Docker release-path chunks є soak-покриттям і запускаються, коли `run_release_soak=true`. `full` примусово вмикає soak-покриття, а також змушує umbrella-запуск виконувати package Telegram E2E для батьківського артефакта релізного пакета, коли `rerun_group=all`, тож повний кандидат перед публікацією не пропустить цю Telegram package lane непомітно.

Профіль | Призначене використання | Включене live/provider покриття  
---|---|---  
`minimum` | Найшвидший критичний для релізу smoke. | OpenAI/core live path, Docker live models для OpenAI, native gateway core, native OpenAI gateway profile, native OpenAI Plugin і Docker live gateway OpenAI.  
`stable` | Типовий профіль схвалення релізу. | `minimum` плюс Anthropic smoke, Google, MiniMax, backend, native live test harness, Docker live CLI backend, Docker ACP bind, Docker Codex harness і OpenCode Go smoke shard.  
`full` | Широкий advisory sweep. | `stable` плюс advisory providers, Plugin live shards і media live shards.  
  
## Додавання лише для full

Ці набори пропускаються в `stable` і включаються в `full`:

Область | Покриття лише для full  
---|---  
Docker live models | OpenCode Go, OpenRouter, xAI, [Z.ai](<http://Z.ai>) і Fireworks.  
Docker live gateway | Advisory providers, розділені на DeepSeek/Fireworks, OpenCode Go/OpenRouter і xAI/Z.ai shards.  
Native gateway provider profiles | Full Anthropic Opus і Sonnet/Haiku shards, Fireworks, DeepSeek, full OpenCode Go model shards, OpenRouter, xAI і [Z.ai](<http://Z.ai>).  
Native Plugin live shards | Plugins A-K, L-N, O-Z other, Moonshot і xAI.  
Native media live shards | Audio, Google music, MiniMax music і video groups A-D.  
  
`stable` включає `native-live-src-gateway-profiles-anthropic-smoke` і `native-live-src-gateway-profiles-opencode-go-smoke`; `full` натомість використовує ширші Anthropic і OpenCode Go model shards. Фокусовані повторні запуски все ще можуть використовувати агреговані handles `native-live-src-gateway-profiles-anthropic` або `native-live-src-gateway-profiles-opencode-go`.

## Фокусовані повторні запуски

Використовуйте `rerun_group`, щоб не повторювати непов’язані release boxes:

Дескриптор | Область застосування  
---|---  
`all` | Усі етапи повної валідації релізу.  
`ci` | Лише дочірній ручний повний CI.  
`plugin-prerelease` | Лише дочірній prerelease Plugin.  
`release-checks` | Усі етапи перевірок релізу OpenClaw.  
`install-smoke` | Install Smoke через перевірки релізу.  
`cross-os` | Міжплатформні перевірки релізу.  
`live-e2e` | Валідація репозиторію/live E2E і Docker release-path.  
`package` | Приймання пакета.  
`qa` | Паритет QA плюс live-гілки QA.  
`qa-parity` | Лише гілки паритету QA та звіт.  
`qa-live` | Лише live Matrix і Telegram для QA.  
`npm-telegram` | E2E Telegram для опублікованого пакета; потребує `release_package_spec` або `npm_telegram_package_spec`.  
  
Використовуйте `live_suite_filter` з `rerun_group=live-e2e`, коли один live-набір не пройшов. Допустимі ідентифікатори фільтрів визначені в повторно використовуваному workflow live/E2E, зокрема `docker-live-models`, `live-gateway-docker`, `live-gateway-anthropic-docker`, `live-gateway-google-docker`, `live-gateway-minimax-docker`, `live-gateway-advisory-docker`, `live-cli-backend-docker`, `live-acp-bind-docker` і `live-codex-harness-docker`.

Дескриптор `live-gateway-advisory-docker` є агрегованим дескриптором повторного запуску для своїх трьох provider-шардів, тому він усе одно розгортається на всі advisory Docker Gateway-завдання.

Використовуйте `cross_os_suite_filter` з `rerun_group=cross-os`, коли одна міжплатформна гілка не пройшла. Фільтр приймає ідентифікатор OS, ідентифікатор набору або пару OS/набір, наприклад `windows/packaged-upgrade`, `windows` або `packaged-fresh`. Міжплатформні зведення містять таймінги за фазами для гілок оновлення пакетованої версії, а довготривалі команди друкують рядки Heartbeat, щоб зависле оновлення Windows було видно до завершення завдання за таймаутом.

Гілки перевірок релізу QA є рекомендаційними. Збій лише в QA повідомляється як попередження і не блокує верифікатор перевірок релізу; повторно запустіть `rerun_group=qa`, `qa-parity` або `qa-live`, коли потрібні свіжі докази QA.

## Докази, які слід зберегти

Зберігайте зведення `Full Release Validation` як індекс рівня релізу. Воно містить посилання на ідентифікатори дочірніх запусків і таблиці найповільніших завдань. У разі збоїв спочатку перевірте дочірній workflow, а потім повторно запустіть найменший відповідний дескриптор вище.

Корисні артефакти:

  * `release-package-under-test` з батьківського workflow повної валідації релізу та `OpenClaw Release Checks`
  * Артефакти Docker release-path у `.artifacts/docker-tests/`
  * `package-under-test` приймання пакета й артефакти приймання Docker
  * Артефакти міжплатформних перевірок релізу для кожної OS і набору
  * Артефакти паритету QA, Matrix і Telegram


## Файли workflow

  * `.github/workflows/full-release-validation.yml`
  * `.github/workflows/openclaw-release-checks.yml`
  * `.github/workflows/openclaw-live-and-e2e-checks-reusable.yml`
  * `.github/workflows/plugin-prerelease.yml`
  * `.github/workflows/install-smoke.yml`
  * `.github/workflows/openclaw-cross-os-release-checks-reusable.yml`
  * `.github/workflows/package-acceptance.yml`


Was this useful?YesNo