---
title: Таксономія зрілості
source_url: https://docs.openclaw.ai/uk/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Таксономія зрілості

модель, що лежить в основі картки оцінювання

Поверхні > категорії > можливості > докази.

50 поверхонь, згрупованих у 4 сімейства, де кожна категорія пов’язана з канонічною документацією та ідентифікаторами покриття QA.

Переглянути продуктові області / Відкрити детальну таксономію / [Переглянути оцінки](</uk/maturity/scorecard>)

## Як читати цю сторінку

Поверхня — це продуктова область, як-от середовище виконання Gateway, Discord або застосунок macOS. Кожна поверхня містить категорії, а кожна категорія містить перевірки на рівні можливостей, які покривають сценарії QA. Використовуйте картку оцінювання для судження на рівні релізу; використовуйте цю сторінку, щоб переглянути модель, що лежить під нею.

## Рівні зрілості

M0ЗапланованоНапрям відомий, але підтримуваного користувацького шляху ще немає.Підвищення: існують дизайн-issue, власник і цільова поверхня.

M1ЕкспериментальнийРеалізовано з застереженнями, прапорцями, збірками з вихідного коду або потоками лише для мейнтейнерів.Підвищення: мейнтейнер може запустити сценарій із поточного main.

M2АльфаРеальні користувачі можуть спробувати це, але очікуються критичні зміни та неповний UX.Підвищення: задокументоване налаштування, базові тести, відомі застереження та принаймні один доказ у реальному середовищі.

M3БетаПублічний шлях існує, а основний робочий процес придатний до використання з обмеженими застереженнями.Підвищення: документація встановлення/оновлення, регресійні тести, runbook підтримки та успішний доказ сценарію в очікуваному середовищі.

M4СтабільнийРекомендований шлях для звичайних користувачів. Збої вважаються регресіями.Підвищення: релізний gate, шлях doctor/усунення несправностей, широка документація та повторювані докази з реального використання.

M5ClawesomeВідшліфований, приємний, добре інструментований і конкурентний із найкращим порівнянним робочим процесом.Підвищення: стабільність плюс проходження користувацької картки оцінювання серед репрезентативних користувачів.

## Продуктові області

### Ядро

CLI M4Стабільний7 областей - завершено на 90% Середовище виконання Gateway M4Стабільний13 областей - завершено на 89% Середовище виконання агента M3Бета9 областей - завершено на 79% Сесія, пам’ять і рушій контексту M3Бета9 областей - завершено на 79% Фреймворк каналів M3Бета8 областей - завершено на 79% Спостережуваність M3Бета5 областей - завершено на 79% Вебзастосунок Gateway M3Бета6 областей - завершено на 79% Плагіни M3Бета9 областей - 79% завершено Безпека, автентифікація, спарювання та секрети M3Бета6 областей - 79% завершено Автоматизація: Cron, хуки, завдання, опитування M3Бета6 областей - 79% завершено Розуміння медіа та генерація медіа M2Альфа6 областей - 68% завершено Голос і розмова в реальному часі M2Альфа6 областей - 68% завершено TUI M2Альфа5 областей - 66% завершено ClawHub M2Альфа4 області - 62% завершено OpenClaw App SDK M2Альфа6 областей - 53% завершено

### Платформа

Хост Linux Gateway M4Стабільна5 областей - 89% завершено Хост macOS Gateway M4Стабільна7 областей - 88% завершено Хостинг Docker і Podman M3Бета4 області - 79% завершено Windows через WSL2 M3Бета6 областей - 79% завершено Raspberry Pi та малі пристрої Linux M3Бета4 області - 79% завершено Супутній застосунок macOS M3Бета8 областей - 78% завершено Застосунок Android M2Альфа7 областей - 66% завершено Нативна Windows M2Альфа4 області - завершено 66% хостинг Kubernetes M2Альфа4 області - завершено 61% застосунок iOS M1Експериментальний8 областей - завершено 44% шлях встановлення Nix M1Експериментальний5 областей - завершено 44% супутні поверхні watchOS M1Експериментальний5 областей - завершено 44% супутній застосунок Linux M0Заплановано5 областей - завершено 21% супутній застосунок для нативної Windows M0Заплановано5 областей - завершено 21%

### Канал

Discord M4Стабільний6 областей - завершено 87% Telegram M3Бета5 областей - завершено 78% Slack M3Бета5 областей - завершено 78% iMessage і BlueBubbles M3Бета5 областей - завершено 78% WhatsApp M3Бета5 областей - завершено 78% Matrix M2Альфа6 областей - завершено 67% Google Chat M2Альфа5 областей - завершено 66% Microsoft Teams M2Альфа5 областей - завершено 66% Signal M2Альфа5 областей - завершено 66% Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, регіональні канали M2Альфа4 області - завершено 58% Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Альфа4 області - завершено 54% канал голосових викликів M1Експериментальний5 областей - завершено 44%

### Провайдер та інструмент

Автоматизація браузера, exec та інструменти пісочниці M3Бета3 області - завершено 79% шлях провайдера OpenAI і Codex M3Бета5 областей - завершено 79% інструменти вебпошуку M3Бета4 області - завершено 79% шлях провайдера Anthropic M3Бета5 областей - завершено 78% шлях провайдера Google M3Бета5 областей - завершено 78% шлях провайдера OpenRouter M3Бета4 області - завершено 78% інструменти генерації зображень, відео та музики M2Альфа5 областей - завершено 68% локальні провайдери моделей: Ollama, vLLM, SGLang, LM Studio M2Альфа5 областей - завершено 68% нішеві хостингові провайдери M2Альфа3 області - завершено 68%

## Докладно

### Ядро

CLI - M4 Стабільний - 7 областей

Звичайні шляхи налаштування та відновлення задокументовано в документації зі встановлення, CLI та Gateway. Специфічні для платформи шляхи Windows відстежуються в рядках Windows через WSL2 і нативної Windows.

Покриття експериментальне - 4%Якість стабільна - 83%Повнота стабільна - 90%Частково - 6

Налаштування CLI 6 можливостей / з підтримкою LTS

Експериментально17%

Стабільно89%

Стабільно90%

[Індекс](</uk/install>), [Інсталятор](</uk/install/installer>), [Node](</uk/install/node>), [Оновлення](</uk/install/updating>)

Налаштування онбордингу й автентифікації 5 можливостей / з підтримкою LTS

Експериментально0%

Бета75%

Стабільно89%

[Онбординг](</uk/cli/onboard>), [Налаштування](</uk/cli/configure>), [Огляд онбордингу](</uk/start/onboarding-overview>)

Налаштування Plugin і каналів 5 можливостей

Експериментально0%

Бета75%

Стабільно89%

[Онбординг](</uk/cli/onboard>), [Plugins](</uk/cli/plugins>), [Канали](</uk/cli/channels>)

Керування сервісом Gateway 5 можливостей / з підтримкою LTS

Експериментально14%

Стабільно87%

Стабільно90%

[Gateway](</uk/cli/gateway>), [Оновлення](</uk/install/updating>), [Усунення несправностей](</uk/gateway/troubleshooting>)

Спостережуваність CLI 5 можливостей / з підтримкою LTS

Експериментально0%

Стабільно89%

Стабільно90%

[Статус](</uk/cli/status>), [Справність](</uk/cli/health>), [Журнали](</uk/cli/logs>), [Діагностика](</uk/gateway/diagnostics>)

Doctor 10 можливостей / з підтримкою LTS

Експериментально0%

Стабільно89%

Стабільно90%

[Doctor](</uk/cli/doctor>), [Doctor](</uk/gateway/doctor>), [Секрети](</uk/gateway/secrets>), [Усунення несправностей](</uk/gateway/troubleshooting>)

Оновлення та підвищення версії 5 можливостей / з підтримкою LTS

Експериментально0%

Бета75%

Стабільно89%

[Оновлення](</uk/install/updating>), [Оновити](</uk/cli/update>), [Усунення несправностей](</uk/gateway/troubleshooting>)

Середовище виконання Gateway - M4 Стабільно - 13 областей

Основна архітектура, автентифікація, сполучення, документація протоколу, документація демона та runbook-и CLI широкі й актуальні.

Покриття: експериментально - 6%Якість: стабільно - 81%Повнота: стабільно - 89%Частково - 12

Затвердження та віддалене виконання 6 можливостей / з підтримкою LTS

Експериментальний0%

Бета75%

Стабільний89%

[Протокол](</uk/gateway/protocol>), [Індекс](</uk/gateway/security>)

HTTP API 4 можливості / з підтримкою LTS

Експериментальний25%

Стабільний90%

Стабільний90%

[Індекс](</uk/gateway>), [OpenAI HTTP API](</uk/gateway/openai-http-api>), [OpenResponses HTTP API](</uk/gateway/openresponses-http-api>), [HTTP API виклику інструментів](</uk/gateway/tools-invoke-http-api>), [Хуки](</uk/automation/hooks>), [Індекс](</uk/web>)

Розміщена вебповерхня 4 можливості / з підтримкою LTS

Експериментальний0%

Стабільний89%

Стабільний90%

[Індекс](</uk/gateway>), [Архітектура](</uk/concepts/architecture>), [Інтерфейс керування](</uk/web/control-ui>), [Вебчат](</uk/web/webchat>), [Полотно](</uk/refactor/canvas>)

RPC API та події Gateway 20 можливостей / з підтримкою LTS

Експериментальний9%

Стабільний90%

Стабільний90%

[Протокол](</uk/gateway/protocol>), [Індекс](</uk/gateway>), [Архітектура](</uk/concepts/architecture>)

Автентифікація та сполучення пристроїв 10 можливостей / з підтримкою LTS

Експериментальний0%

Бета75%

Стабільний89%

[Протокол](</uk/gateway/protocol>), [Сполучення](</uk/gateway/pairing>), [Індекс](</uk/gateway/security>)

Доступ до мережі та виявлення 6 можливостей / з підтримкою LTS

Експериментальний0%

Бета75%

Стабільний89%

[Індекс](</uk/gateway>), [Виявлення](</uk/gateway/discovery>), [Протокол](</uk/gateway/protocol>)

Вузли та віддалені можливості 8 можливостей

Експериментальний0%

Бета75%

Стабільний89%

[Протокол](</uk/gateway/protocol>), [Архітектура](</uk/concepts/architecture>), [Індекс](</uk/nodes>)

Стан, діагностика та відновлення 7 можливостей / з підтримкою LTS

Експериментальний0%

Бета75%

Стабільний89%

[Покажчик](</uk/gateway>), [Діагностика](</uk/gateway/diagnostics>), [Лікар](</uk/gateway/doctor>)

Сумісність протоколу 7 можливостей / з підтримкою LTS

Експериментальний0%

Бета75%

Стабільний89%

[Протокол](</uk/gateway/protocol>), [Архітектура](</uk/concepts/architecture>), [Typebox](</uk/concepts/typebox>), [Протокол Bridge](</uk/gateway/bridge-protocol>)

Ролі та дозволи 5 можливостей / з підтримкою LTS

Експериментальний0%

Бета75%

Стабільний89%

[Протокол](</uk/gateway/protocol>), [Покажчик](</uk/gateway/security>)

Життєвий цикл Gateway 7 можливостей / з підтримкою LTS

Експериментальний33%

Стабільний90%

Стабільний90%

[Покажчик](</uk/gateway>), [Архітектура](</uk/concepts/architecture>)

Засоби контролю безпеки 6 можливостей / з підтримкою LTS

Експериментальний0%

Бета75%

Стабільний89%

[Покажчик](</uk/gateway/security>), [Протокол](</uk/gateway/protocol>), [Виявлення](</uk/gateway/discovery>)

Підключення WebSocket 8 можливостей / з підтримкою LTS

Експериментальний13%

Стабільний90%

Стабільний90%

[Протокол](</uk/gateway/protocol>), [Архітектура](</uk/concepts/architecture>)

Середовище виконання агента - M3 Beta - 9 сфер

Основний цикл, моделі, маршрутизація постачальників і потокова передача інструментів є першокласними можливостями, але поведінка постачальників змінюється щотижня й потребує сценарного підтвердження для кожного випуску.

Покриття експериментальне - 33%Якість Beta - 78%Повнота Beta - 79%Частково - 6

Виконання ходу агента 3 можливості / підтримується LTS

Експериментально29%

Бета79%

Бета79%

[Цикл агента](</uk/concepts/agent-loop>), [Агент](</uk/cli/agent>), [Середовища виконання агента](</uk/concepts/agent-runtimes>)

Зовнішні середовища виконання та субагенти 4 можливості

Експериментально30%

Бета79%

Бета79%

[Середовища виконання агента](</uk/concepts/agent-runtimes>), [Anthropic](</uk/providers/anthropic>), [Google](</uk/providers/google>), [Субагенти](</uk/tools/subagents>)

Виконання через розміщених провайдерів 5 можливостей / підтримується LTS

Експериментально20%

Бета79%

Бета79%

[Openai](</uk/providers/openai>), [Anthropic](</uk/providers/anthropic>), [Google](</uk/providers/google>), [Моделі](</uk/concepts/models>)

Локальні та самостійно розміщені провайдери 5 можливостей

Експериментально0%

Альфа68%

Бета79%

[Ollama](</uk/providers/ollama>), [Моделі](</uk/concepts/models>), [Агент](</uk/cli/agent>)

Вибір моделі та середовища виконання 4 можливості / підтримується LTS

Експериментально25%

Бета79%

Бета79%

[Моделі](</uk/concepts/models>), [Моделі](</uk/cli/models>), [Openai](</uk/providers/openai>), [Середовища виконання агента](</uk/concepts/agent-runtimes>)

Автентифікація провайдера 10 можливостей / підтримується LTS

Експериментально24%

Бета79%

Бета79%

[Моделі](</uk/concepts/models>), [Агент](</uk/cli/agent>), [Моделі](</uk/cli/models>), [Openai](</uk/providers/openai>), [Anthropic](</uk/providers/anthropic>), [Google](</uk/providers/google>), [Субагенти](</uk/tools/subagents>)

Потокове передавання та прогрес 2 можливості

Альфа56%

Бета79%

Бета79%

[Потокове передавання](</uk/concepts/streaming>), [Цикл агента](</uk/concepts/agent-loop>)

Виклики інструментів і обробка відповідей 3 можливості / підтримується LTS

Альфа65%

Бета79%

Бета79%

[Цикл агента](</uk/concepts/agent-loop>), [Ollama](</uk/providers/ollama>)

Засоби керування виконанням інструментів 6 можливостей / підтримується LTS

Alpha50%

Beta79%

Beta79%

[Пісочниця, політика інструментів і підвищені права](</uk/gateway/sandbox-vs-tool-policy-vs-elevated>), [Цикл агента](</uk/concepts/agent-loop>), [Підагенти](</uk/tools/subagents>)

Сесія, памʼять і рушій контексту - M3 Beta - 9 областей

Сильна документація й активна реалізація. Зрілість залежить від надійності збереження транскриптів, якості Compaction і паритету між клієнтами.

Покриття Experimental - 30%Якість Beta - 77%Завершеність Beta - 79%Частково - 6

Керування сеансами CLI і транскриптами 2 можливості / з підтримкою LTS

Експериментально0%

Альфа68%

Бета79%

[Сеанс](</uk/concepts/session>), [Compaction для керування сеансами](</uk/reference/session-management-compaction>), [Сеанси](</uk/cli/sessions>)

Керування токенами 3 можливості / з підтримкою LTS

Експериментально20%

Бета79%

Бета79%

[Compaction](</uk/concepts/compaction>), [Контекст](</uk/concepts/context>), [Compaction для керування сеансами](</uk/reference/session-management-compaction>)

Рушій контексту 2 можливості / з підтримкою LTS

Альфа57%

Бета79%

Бета79%

[Контекст](</uk/concepts/context>), [Рушій контексту](</uk/concepts/context-engine>), [Стенд рушія контексту Codex](</uk/plan/codex-context-engine-harness>)

Кросклієнтська історія та паритет сеансів 2 можливості

Експериментально40%

Бета79%

Бета79%

[Вебчат](</uk/web/webchat>), [Android](</uk/platforms/android>), [Маршрутизація каналів](</uk/channels/channel-routing>)

Діагностика, обслуговування та відновлення 3 можливості

Експериментально40%

Бета79%

Бета79%

[Діагностика](</uk/gateway/diagnostics>), [Compaction для керування сеансами](</uk/reference/session-management-compaction>), [Прапорці](</uk/diagnostics/flags>)

Основні промпти та контекст 2 можливості / з підтримкою LTS

Експериментально38%

Бета79%

Бета79%

[Контекст](</uk/concepts/context>), [Гігієна транскриптів](</uk/reference/transcript-hygiene>), [Discord](</uk/channels/discord>)

Пам’ять 5 можливостей

Експериментально46%

Бета79%

Бета79%

[Конфігурація пам’яті](</uk/reference/memory-config>), [Пам’ять Qmd](</uk/concepts/memory-qmd>), [Пам’ять](</uk/concepts/memory>), [Discord](</uk/channels/discord>)

Маршрутизація сеансів 2 можливості / з підтримкою LTS

Експериментально25%

Бета79%

Бета79%

[Сеанс](</uk/concepts/session>), [Маршрутизація каналів](</uk/channels/channel-routing>), [Discord](</uk/channels/discord>)

Збереження транскриптів 2 можливості / з підтримкою LTS

Експериментальний0%

Alpha68%

Beta79%

[Compaction керування сеансами](</uk/reference/session-management-compaction>), [Гігієна транскриптів](</uk/reference/transcript-hygiene>)

Фреймворк каналів - M3 Beta - 8 областей

Багато каналів спільно використовують контракти доставки та маршрутизації Gateway, але поведінка каналів відрізняється залежно від upstream API та обмежень політики облікового запису.

Покриття Experimental - 13%Якість Beta - 76%Повнота Beta - 79%Частково - 5

Команди дій каналу та схвалення 5 можливостей

Експериментальний0%

Бета79%

Бета79%

[Групи](</uk/channels/groups>), [Discord](</uk/channels/discord>), [Googlechat](</uk/channels/googlechat>), [Signal](</uk/channels/signal>), [Matrix](</uk/channels/matrix>)

Налаштування каналу 5 можливостей / підтримується LTS

Експериментальний14%

Бета79%

Бета79%

[Індекс](</uk/channels>), [Сполучення](</uk/channels/pairing>), [Усунення несправностей](</uk/channels/troubleshooting>), [Plugin-и каналів SDK](</uk/plugins/sdk-channel-plugins>)

Поведінка групових потоків і фонових кімнат 5 можливостей

Експериментальний36%

Бета79%

Бета79%

[Групи](</uk/channels/groups>), [Групові повідомлення](</uk/channels/group-messages>), [Події фонових кімнат](</uk/channels/ambient-room-events>), [Групи трансляції](</uk/channels/broadcast-groups>), [Discord](</uk/channels/discord>)

Вхідний доступ і перевірки ідентичності 5 можливостей / підтримується LTS

Експериментальний0%

Альфа68%

Бета79%

[Групи доступу](</uk/channels/access-groups>), [Групи](</uk/channels/groups>), [Discord](</uk/channels/discord>), [Line](</uk/channels/line>)

Медіавкладення та розширені дані каналів 4 можливості

Експериментальний0%

Альфа68%

Бета79%

[Line](</uk/channels/line>), [Signal](</uk/channels/signal>), [Googlechat](</uk/channels/googlechat>), [Matrix](</uk/channels/matrix>), [Discord](</uk/channels/discord>)

Вихідна доставка та конвеєр відповідей 4 можливості / підтримується LTS

Експериментальний38%

Бета79%

Бета79%

[Групи](</uk/channels/groups>), [Події фонових кімнат](</uk/channels/ambient-room-events>), [Discord](</uk/channels/discord>), [Matrix](</uk/channels/matrix>), [Канали конфігурації](</uk/gateway/config-channels>)

Маршрутизація і доставка розмов 10 можливостей / підтримується LTS

Експериментальний19%

Бета79%

Бета79%

[Маршрутизація каналів](</uk/channels/channel-routing>), [Групи](</uk/channels/groups>), [Discord](</uk/channels/discord>), [Matrix](</uk/channels/matrix>), [Усунення несправностей](</uk/channels/troubleshooting>), [Довідник конфігурації](</uk/gateway/configuration-reference>)

Стан працездатності та засоби керування оператора 4 можливості / підтримується LTS

Експериментальний0%

Бета79%

Бета79%

[Стан](</uk/gateway/health>), [Довідник із конфігурації](</uk/gateway/configuration-reference>), [Усунення неполадок](</uk/channels/troubleshooting>), [Discord](</uk/channels/discord>)

Спостережуваність - M3 Beta - 5 областей

Документація для OTel, Prometheus, журналювання та діагностики існує. Потребує публічного перегляду зрілості щодо того, "на що операторам слід дивитися насамперед".

Покриття Experimental - 18%Якість Beta - 75%Повнота Beta - 79%Частково - 3

Стан і відновлення 12 можливостей / з підтримкою LTS

Experimental28%

Beta79%

Beta79%

[Стан](</uk/gateway/health>), [Telegram](</uk/channels/telegram>), [Doctor](</uk/cli/doctor>), [Doctor](</uk/gateway/doctor>), [Підшляхи SDK](</uk/plugins/sdk-subpaths>), [Стан](</uk/cli/health>), [Протокол](</uk/gateway/protocol>)

Журналювання 5 можливостей / з підтримкою LTS

Experimental0%

Alpha68%

Beta79%

[Журналювання](</uk/logging>), [Журналювання](</uk/gateway/logging>), [Журнали](</uk/cli/logs>)

Збір діагностики 8 можливостей

Experimental30%

Beta79%

Beta79%

[Діагностика](</uk/gateway/diagnostics>), [Стан](</uk/gateway/health>), [Codex Harness](</uk/plugins/codex-harness>), [Протокол](</uk/gateway/protocol>)

Експорт телеметрії 13 можливостей

Experimental33%

Beta79%

Beta79%

[Хуки](</uk/plugins/hooks>), [Opentelemetry](</uk/gateway/opentelemetry>), [Журналювання](</uk/logging>), [Підшляхи SDK](</uk/plugins/sdk-subpaths>), [Diagnostics Otel](</uk/plugins/reference/diagnostics-otel>), [Prometheus](</uk/gateway/prometheus>), [Diagnostics Prometheus](</uk/plugins/reference/diagnostics-prometheus>)

Діагностика сеансу 4 можливості / з підтримкою LTS

Experimental0%

Alpha68%

Beta79%

[Opentelemetry](</uk/gateway/opentelemetry>), [Prometheus](</uk/gateway/prometheus>), [Діагностика](</uk/gateway/diagnostics>), [Протокол](</uk/gateway/protocol>)

Вебзастосунок Gateway - M3 Beta - 6 областей

Вебінтерфейс задокументовано з потоками сполучення, чату, PWA, Talk, push і віддаленого Gateway. Просувайте після оцінок за картками показників для різних браузерів і мобільних PWA.

Покриття Experimental - 4%Якість Beta - 74%Повнота Beta - 79%Немає

Розмова в реальному часі в браузері 5 можливостей

Експериментально0%

Альфа68%

Бета79%

[Інтерфейс керування](</uk/web/control-ui>), [Протокол](</uk/gateway/protocol>), [Розмова](</uk/nodes/talk>)

Доступ і довіра в браузері 5 можливостей

Експериментально0%

Альфа68%

Бета79%

[Інтерфейс керування](</uk/web/control-ui>), [Панель керування](</uk/web/dashboard>), [Tailscale](</uk/gateway/tailscale>), [Віддалений доступ](</uk/gateway/remote>)

Конфігурація 5 можливостей

Експериментально0%

Альфа68%

Бета79%

[Інтерфейс керування](</uk/web/control-ui>), [Конфігурація](</uk/gateway/configuration>)

Браузерний UI 10 можливостей

Експериментально8%

Бета79%

Бета79%

[Інтерфейс керування](</uk/web/control-ui>), [Індекс](</uk/web>), [Панель керування](</uk/web/dashboard>), [Протокол](</uk/gateway/protocol>)

Розмови WebChat 15 можливостей

Експериментально10%

Бета79%

Бета79%

[Інтерфейс керування](</uk/web/control-ui>), [Webchat](</uk/web/webchat>), [Початок роботи](</uk/start/getting-started>), [Маршрутизація каналів](</uk/channels/channel-routing>), [Безпечні файлові операції](</uk/gateway/security/secure-file-operations>)

Консоль оператора 10 можливостей

Експериментально8%

Бета79%

Бета79%

[Інтерфейс керування](</uk/web/control-ui>), [Стан](</uk/gateway/health>), [Протокол](</uk/gateway/protocol>), [Панель керування](</uk/web/dashboard>)

Plugins - M3 Beta - 9 areas

Широка документація та переконливі внутрішні докази роботи середовища виконання існують для маніфестів, виявлення, завантаження, архітектури провайдерів/інструментів і меж схвалення. Залишайте рядок на рівні бета, доки докази щодо публічних API/підшляхів SDK і зовнішнього розповсюдження не стануть сильнішими.

Покриття експериментальне - 12%Якість бета - 72%Повнота бета - 79%Частково - 7

Створення та пакування plugins 8 можливостей / підтримується LTS

Експериментальний0%

Альфа68%

Бета79%

[Створення Plugins](</uk/plugins/building-plugins>), [Огляд Sdk](</uk/plugins/sdk-overview>), [Точки входу Sdk](</uk/plugins/sdk-entrypoints>), [Підшляхи Sdk](</uk/plugins/sdk-subpaths>), [Маніфест](</uk/plugins/manifest>), [Довідник](</uk/plugins/reference>)

Вбудовані plugins 5 можливостей / підтримується LTS

Експериментальний0%

Альфа68%

Бета79%

[Інвентаризація Plugin](</uk/plugins/plugin-inventory>), [Plugins](</uk/cli/plugins>), [Внутрішня архітектура](</uk/plugins/architecture-internals>)

Canvas plugin 6 можливостей

Експериментальний0%

Альфа68%

Бета79%

[Canvas](</uk/plugins/reference/canvas>), [Canvas](</uk/refactor/canvas>), [Довідник конфігурації](</uk/gateway/configuration-reference>)

Установлення та запуск plugins 6 можливостей / підтримується LTS

Експериментальний35%

Бета79%

Бета79%

[Архітектура](</uk/plugins/architecture>), [Внутрішня архітектура](</uk/plugins/architecture-internals>), [Plugins](</uk/cli/plugins>)

Канальні plugins 5 можливостей / підтримується LTS

Експериментальний0%

Альфа68%

Бета79%

[Канальні Plugins Sdk](</uk/plugins/sdk-channel-plugins>), [Вхідні канали Sdk](</uk/plugins/sdk-channel-inbound>), [Вихідні канали Sdk](</uk/plugins/sdk-channel-outbound>)

Plugins провайдерів та інструментів 6 можливостей / підтримується LTS

Експериментальний43%

Бета79%

Бета79%

[Plugins провайдерів Sdk](</uk/plugins/sdk-provider-plugins>), [Інструментальні Plugins](</uk/plugins/tool-plugins>), [Додавання можливостей](</uk/plugins/adding-capabilities>)

Схвалення Plugin 6 можливостей / підтримується LTS

Експериментальний0%

Альфа68%

Бета79%

[Запити дозволів Plugin](</uk/plugins/plugin-permission-requests>), [Схвалення Exec](</uk/tools/exec-approvals>), [Канальні Plugins Sdk](</uk/plugins/sdk-channel-plugins>)

Публікація plugins 6 можливостей / підтримується LTS

Експериментальний0%

Альфа68%

Бета79%

[Плагіни](</uk/cli/plugins>), [Сумісність](</uk/plugins/compatibility>), [Публікація](</uk/clawhub/publishing>)

Тестування плагінів 6 можливостей

Експериментальний27%

Бета79%

Бета79%

[Тестування Sdk](</uk/plugins/sdk-testing>), [Налаштування Sdk](</uk/plugins/sdk-setup>), [Codex Harness](</uk/plugins/codex-harness>)

Безпека, автентифікація, сполучення та секрети - M3 Beta - 6 сфер

Існують якісні документація та поверхні посилення безпеки. Просувайте після того, як регулярні запуски сценаріїв оновлення й безпеки доведуть відсутність регресій налаштування.

Покриття Experimental - 16%Якість Beta - 72%Повнота Beta - 79%Частково - 5

Політика схвалень і захисні механізми інструментів 2 можливості / підтримується LTS

Alpha50%

Beta79%

Beta79%

[Схвалення Exec](</uk/tools/exec-approvals>), [Схвалення](</uk/cli/approvals>), [Запити дозволів Plugin](</uk/plugins/plugin-permission-requests>), [Аудиторські перевірки](</uk/gateway/security/audit-checks>)

Автентифікація Gateway і віддалений доступ 9 можливостей / підтримується LTS

Experimental0%

Alpha68%

Beta79%

[Індекс](</uk/gateway/security>), [Runbook експонування](</uk/gateway/security/exposure-runbook>), [Автентифікація довіреного проксі](</uk/gateway/trusted-proxy-auth>), [Tailscale](</uk/gateway/tailscale>), [Віддалено](</uk/gateway/remote>), [Довідник конфігурації](</uk/gateway/configuration-reference>), [Gateway](</uk/cli/gateway>), [Doctor](</uk/cli/doctor>), [UI керування](</uk/web/control-ui>), [Керування браузером](</uk/tools/browser-control>), [Аудиторські перевірки](</uk/gateway/security/audit-checks>)

Контроль доступу каналів 3 можливості / підтримується LTS

Experimental0%

Alpha68%

Beta79%

[Сполучення](</uk/channels/pairing>), [Telegram](</uk/channels/telegram>), [Групи доступу](</uk/channels/access-groups>), [Аудиторські перевірки](</uk/gateway/security/audit-checks>)

Сполучення пристроїв і Node 11 можливостей / підтримується LTS

Experimental0%

Alpha68%

Beta79%

[Протокол](</uk/gateway/protocol>), [Пристрої](</uk/cli/devices>), [Сполучення](</uk/channels/pairing>), [Сполучення](</uk/gateway/pairing>), [Області оператора](</uk/gateway/operator-scopes>), [UI керування](</uk/web/control-ui>), [Webchat](</uk/web/webchat>), [Схвалення](</uk/cli/approvals>)

Довіра до Plugin 2 можливості

Experimental0%

Alpha68%

Beta79%

[Маніфест](</uk/plugins/manifest>), [Запити дозволів Plugin](</uk/plugins/plugin-permission-requests>), [Керування Plugins](</uk/plugins/manage-plugins>), [Аудиторські перевірки](</uk/gateway/security/audit-checks>)

Гігієна облікових даних і секретів 5 можливостей / підтримується LTS

Experimental46%

Beta79%

Beta79%

[Автентифікація](</uk/gateway/authentication>), [Моделі](</uk/cli/models>), [Openai](</uk/providers/openai>), [Oauth](</uk/concepts/oauth>), [Секрети](</uk/gateway/secrets>), [Секрети](</uk/cli/secrets>), [Поверхня облікових даних Secretref](</uk/reference/secretref-credential-surface>), [Аудиторські перевірки](</uk/gateway/security/audit-checks>)

Автоматизація: Cron, хуки, завдання, опитування - M3 Beta - 6 сфер

Задокументовано й придатно до використання, але підтвердження сценаріями має охоплювати доставку без нагляду, повторні спроби та видимість збоїв.

Покриття Experimental - 2%Якість Beta - 72%Повнота Beta - 79%Немає

Завдання Cron 15 можливостей

Експериментально0%

Бета79%

Бета79%

[Завдання Cron](</uk/automation/cron-jobs>), [Cron](</uk/cli/cron>), [Протокол](</uk/gateway/protocol>), [Завдання](</uk/automation/tasks>), [Discord](</uk/channels/discord>)

Надходження подій 15 можливостей

Експериментально0%

Альфа68%

Бета79%

[Telegram](</uk/channels/telegram>), [Zalo](</uk/channels/zalo>), [Усунення несправностей](</uk/channels/troubleshooting>), [iMessage із BlueBubbles](</uk/channels/imessage-from-bluebubbles>), [Інтеграція Gmail Pub/Sub](</uk/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pub/Sub](</uk/automation/cron-jobs>), [Webhooks](</uk/cli/webhooks>), [Webhooks](</uk/automation/cron-jobs#webhooks>), [Webhook](</uk/automation/cron-jobs>)

Хуки автоматизації 11 можливостей

Експериментально0%

Альфа68%

Бета79%

[Хуки](</uk/automation/hooks>), [Хуки](</uk/cli/hooks>), [Хуки](</uk/plugins/hooks>), [Запити дозволів Plugin](</uk/plugins/plugin-permission-requests>), [Підшляхи SDK](</uk/plugins/sdk-subpaths>)

Фонові завдання та потоки 10 можливостей

Експериментально0%

Альфа68%

Бета79%

[Завдання](</uk/automation/tasks>), [Покажчик](</uk/automation>), [Завдання](</uk/cli/tasks>), [TaskFlow](</uk/automation/taskflow>), [Середовище виконання SDK](</uk/plugins/sdk-runtime>)

Heartbeat 5 можливостей

Експериментально14%

Бета79%

Бета79%

[Покажчик](</uk/automation>), [Heartbeat](</uk/gateway/heartbeat>), [Зобов’язання](</uk/concepts/commitments>)

Керування опитуванням 10 можливостей

Експериментально0%

Альфа68%

Бета79%

[Опитування](</uk/cli/message>), [Повідомлення](</uk/cli/message>), [Telegram](</uk/channels/telegram>), [Msteams](</uk/channels/msteams>), [Фоновий процес](</uk/gateway/background-process>)

Розуміння медіа та генерування медіа - M2 Альфа - 6 областей

Існує широка поверхня можливостей, але відмінності між провайдерами, обмеження файлів і паритет між Node та застосунком роблять її ще нестабільною.

Покриття: експериментально - 2%Якість: альфа - 64%Завершеність: альфа - 68%Немає

Приймання медіа та доступ 8 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Огляд медіа](</uk/tools/media-overview>), [Розуміння медіа](</uk/nodes/media-understanding>), [Безпечні файлові операції](</uk/gateway/security/secure-file-operations>), [PDF](</uk/tools/pdf>), [Генерація зображень](</uk/tools/image-generation>), [QR](</uk/cli/qr>), [LINE](</uk/channels/line>), [WhatsApp](</uk/channels/whatsapp>)

Обробка медіа в каналах 5 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Зображення](</uk/nodes/images>), [Огляд медіа](</uk/tools/media-overview>), [Discord](</uk/channels/discord>)

Конфігурація медіа 1 можливість

Експериментальний0%

Альфа61%

Альфа68%

[Огляд медіа](</uk/tools/media-overview>), [Генерація зображень](</uk/tools/image-generation>), [Маніфест](</uk/plugins/manifest>), [Обв'язка Codex](</uk/plugins/codex-harness>)

Доставка тексту мовленням 2 можливості

Експериментальний0%

Альфа61%

Альфа68%

[TTS](</uk/tools/tts>), [Огляд медіа](</uk/tools/media-overview>), [Discord](</uk/channels/discord>)

Розуміння медіа 12 можливостей

Експериментальний7%

Альфа69%

Альфа69%

[Аудіо](</uk/nodes/audio>), [Розуміння медіа](</uk/nodes/media-understanding>), [Огляд медіа](</uk/tools/media-overview>), [WhatsApp](</uk/channels/whatsapp>), [Зображення](</uk/nodes/images>), [Infer](</uk/cli/infer>), [PDF](</uk/tools/pdf>)

Генерація медіа 17 можливостей

Експериментальний5%

Альфа69%

Альфа69%

[Генерація зображень](</uk/tools/image-generation>), [Огляд медіа](</uk/tools/media-overview>), [Skills](</uk/tools/skills>), [Генерація музики](</uk/tools/music-generation>), [Генерація відео](</uk/tools/video-generation>)

Голос і розмова в реальному часі - M2 Альфа - 6 областей

Існує кілька реалізацій у Control UI, застосунках і провайдерах. Перед бета-версією потрібні оцінювальні карти для затримки, режимів відмови та налаштування.

Покриття Експериментальний - 0%Якість Альфа - 61%Повнота Альфа - 68%Немає

Постачальники розмови 7 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Openai](</uk/providers/openai>), [Google](</uk/providers/google>), [Плагіни постачальників SDK](</uk/plugins/sdk-provider-plugins>), [Розмова](</uk/nodes/talk>), [Інтерфейс керування](</uk/web/control-ui>)

Сеанси розмови в реальному часі 11 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Розмова](</uk/nodes/talk>), [Інтерфейс керування](</uk/web/control-ui>)

Мовлення та транскрибування 5 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Розмова](</uk/nodes/talk>), [Openai](</uk/providers/openai>), [Google](</uk/providers/google>)

Розмова в нативному застосунку 4 можливості

Експериментальний0%

Альфа61%

Альфа68%

[Розмова](</uk/nodes/talk>), [Voicewake](</uk/platforms/mac/voicewake>)

Голосове пробудження та маршрутизація 4 можливості

Експериментальний0%

Альфа61%

Альфа68%

[Voicewake](</uk/nodes/voicewake>), [Voicewake](</uk/platforms/mac/voicewake>), [Голосове накладання](</uk/platforms/mac/voice-overlay>)

Спостережуваність розмови 5 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Інтерфейс керування](</uk/web/control-ui>), [Голосове накладання](</uk/platforms/mac/voice-overlay>), [Розмова](</uk/nodes/talk>)

TUI - M2 Альфа - 5 областей

Присутній у документації та вихідному коді, але менш помітний як основний користувацький робочий процес. Потребує явного визначення сценарію.

Покриття: експериментальний - 0%Якість: альфа - 59%Повнота: альфа - 66%Немає

Режими виконання 14 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[TUI](</uk/cli/tui>), [TUI](</uk/web/tui>), [Індекс](</uk/cli>)

Введення та команди 8 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[TUI](</uk/web/tui>)

Керування сеансами 3 можливості

Експериментальний0%

Альфа59%

Альфа66%

[TUI](</uk/web/tui>), [Сеанси](</uk/cli/sessions>)

Локальне виконання в оболонці 4 можливості

Експериментальний0%

Альфа59%

Альфа66%

[TUI](</uk/web/tui>), [TUI](</uk/cli/tui>)

Рендеринг і безпека виводу 4 можливості

Експериментальний0%

Альфа59%

Альфа66%

[TUI](</uk/web/tui>), [Qr](</uk/cli/qr>), [Журнали](</uk/cli/logs>), [Завершення](</uk/cli/completion>)

ClawHub - M2 Альфа - 4 сфери

Публічна документація та концепція екосистеми існують. Потрібні таблиці оцінки встановлення, довіри, оновлення, відкоту та сумісності.

Покриття Експериментальний - 0%Якість Альфа - 58%Повнота Альфа - 62%Немає

Публікація 7 можливостей

Експериментальний0%

Альфа54%

Альфа55%

[Публікація](</uk/clawhub/publishing>), [Створення Skills](</uk/tools/creating-skills>), [Спільнота](</uk/plugins/community>)

Виявлення каталогу 5 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Plugin](</uk/tools/plugin>), [Plugins](</uk/cli/plugins>), [Skills](</uk/cli/skills>), [Skills](</uk/tools/skills>), [Спільнота](</uk/plugins/community>)

Сумісність і довіра 12 можливостей

Експериментальний0%

Альфа55%

Альфа56%

[Plugin](</uk/tools/plugin>), [Plugins](</uk/cli/plugins>), [Сумісність](</uk/plugins/compatibility>), [Інвентаризація Plugin](</uk/plugins/plugin-inventory>), [Публікація](</uk/clawhub/publishing>), [Skills](</uk/tools/skills>), [Конфігурація Skills](</uk/tools/skills-config>)

Життєвий цикл і стан Plugin 26 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Plugin](</uk/tools/plugin>), [Plugins](</uk/cli/plugins>), [Skills](</uk/cli/skills>), [Skills](</uk/tools/skills>), [Протокол](</uk/gateway/protocol>), [Пакети](</uk/plugins/bundles>), [Розв’язання залежностей](</uk/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Альфа - 6 областей

OpenClaw App SDK — це окремий контракт зовнішнього застосунку, відмінний від середовища виконання Gateway і Plugin SDK. Поточне оцінювання показує реальний шлях `@openclaw/sdk` із прогалинами щодо публічного пакування, автоматичного виявлення, затверджень, допоміжних засобів і сумісності.

Покриття Експериментальне - 3%Якість Альфа - 54%Повнота Альфа - 53%Немає

API клієнта 4 можливості

Експериментальний0%

Альфа51%

Альфа50%

[OpenClaw SDK](</uk/gateway/external-apps>), [Дизайн API OpenClaw SDK](</uk/gateway/external-apps>)

Доступ до Gateway 5 можливостей

Експериментальний0%

Альфа53%

Альфа54%

[OpenClaw SDK](</uk/gateway/external-apps>), [Дизайн API OpenClaw SDK](</uk/gateway/external-apps>), [Протокол](</uk/gateway/protocol>), [Покажчик](</uk/gateway/security>)

Розмови з агентом 6 можливостей

Експериментальний0%

Альфа52%

Альфа52%

[OpenClaw SDK](</uk/gateway/external-apps>), [Дизайн API OpenClaw SDK](</uk/gateway/external-apps>), [Протокол](</uk/gateway/protocol>)

Події та схвалення 5 можливостей

Експериментальний0%

Альфа52%

Альфа52%

[OpenClaw SDK](</uk/gateway/external-apps>), [Дизайн API OpenClaw SDK](</uk/gateway/external-apps>), [Протокол](</uk/gateway/protocol>)

Помічники ресурсів 5 можливостей

Експериментальний17%

Альфа62%

Альфа53%

[OpenClaw SDK](</uk/gateway/external-apps>), [Дизайн API OpenClaw SDK](</uk/gateway/external-apps>)

Сумісність 5 можливостей

Експериментальний0%

Альфа54%

Альфа55%

[Дизайн API OpenClaw SDK](</uk/gateway/external-apps>), [Typebox](</uk/concepts/typebox>), [Протокол](</uk/gateway/protocol>)

### Платформа

Хост Linux Gateway - M4 стабільний - 5 областей

Рекомендовано середовище виконання Node, задокументовано користувацький сервіс systemd, а настанови для VPS/контейнерів є широкими.

Покриття: експериментальне - 0%Якість: бета - 75%Повнота: стабільна - 89%Частково - 4

Налаштування та оновлення хоста 4 можливості / з підтримкою LTS

Експериментально0%

Бета75%

Стабільно89%

[Індекс](</uk/install>), [Оновлення](</uk/install/updating>), [Linux](</uk/platforms/linux>), [Індекс](</uk/platforms>)

Середовище виконання Gateway та керування сервісом 6 можливостей / з підтримкою LTS

Експериментально0%

Бета75%

Стабільно89%

[Індекс](</uk/gateway>), [Gateway](</uk/cli/gateway>), [Linux](</uk/platforms/linux>), [Vps](</uk/vps>)

Віддалений доступ і безпека 6 можливостей / з підтримкою LTS

Експериментально0%

Бета75%

Стабільно89%

[Віддалений доступ](</uk/gateway/remote>), [Tailscale](</uk/gateway/tailscale>), [Інструкція з експонування](</uk/gateway/security/exposure-runbook>), [Автентифікація](</uk/gateway/authentication>), [Секрети](</uk/gateway/secrets>)

Діагностика та відновлення 4 можливості / з підтримкою LTS

Експериментально0%

Бета75%

Стабільно89%

[Стан](</uk/cli/status>), [Журнали](</uk/cli/logs>), [Doctor](</uk/cli/doctor>), [Діагностика](</uk/gateway/diagnostics>), [Індекс](</uk/gateway>)

Цілі розгортання 3 можливості

Експериментально0%

Бета75%

Стабільно89%

[Vps](</uk/vps>), [Docker](</uk/install/docker>), [Hetzner](</uk/install/hetzner>), [Digitalocean](</uk/install/digitalocean>), [Kubernetes](</uk/install/kubernetes>), [Podman](</uk/install/podman>)

Хост macOS Gateway — M4 Stable — 7 областей

Документовано шлях сервісу LaunchAgent, локальні/віддалені режими Gateway, встановлення CLI та інтеграцію з застосунком.

Покриття: експериментально — 0%Якість: бета — 74%Повнота: стабільно — 88%Немає

Налаштування CLI 4 можливості

Експериментальний0%

Бета74%

Стабільний88%

[Macos](</uk/platforms/macos>), [Вбудований Gateway](</uk/platforms/mac/bundled-gateway>), [Інсталятор](</uk/install/installer>), [Node](</uk/install/node>)

Інтеграція з локальним Gateway 9 можливостей

Експериментальний0%

Бета74%

Стабільний88%

[Macos](</uk/platforms/macos>), [Вбудований Gateway](</uk/platforms/mac/bundled-gateway>), [Віддалений доступ](</uk/platforms/mac/remote>), [Індекс](</uk/gateway>), [Gateway](</uk/cli/gateway>), [Bonjour](</uk/gateway/bonjour>)

Віддалений режим Gateway 5 можливостей

Експериментальний0%

Бета74%

Стабільний88%

[Віддалений доступ](</uk/platforms/mac/remote>), [Віддалений доступ](</uk/gateway/remote>), [Tailscale](</uk/gateway/tailscale>)

Життєвий цикл служби Gateway 10 можливостей

Експериментальний0%

Бета74%

Стабільний88%

[Macos](</uk/platforms/macos>), [Вбудований Gateway](</uk/platforms/mac/bundled-gateway>), [Gateway](</uk/cli/gateway>), [Індекс](</uk/gateway>), [Оновлення](</uk/cli/update>), [Оновлення](</uk/install/updating>), [Видалення](</uk/install/uninstall>), [Усунення несправностей](</uk/gateway/troubleshooting>)

Діагностика та спостережуваність 4 можливості

Експериментальний0%

Бета74%

Стабільний88%

[Вбудований Gateway](</uk/platforms/mac/bundled-gateway>), [Macos](</uk/platforms/macos>), [Gateway](</uk/cli/gateway>), [Doctor](</uk/gateway/doctor>), [Усунення несправностей](</uk/gateway/troubleshooting>)

Дозволи та нативні можливості 4 можливості

Експериментальний0%

Бета74%

Стабільний88%

[Macos](</uk/platforms/macos>), [Віддалений доступ](</uk/platforms/mac/remote>)

Профілі та ізоляція 5 можливостей

Експериментальний0%

Бета74%

Стабільний88%

[Кілька Gateway](</uk/gateway/multiple-gateways>), [Індекс](</uk/gateway>), [Gateway](</uk/cli/gateway>)

Хостинг Docker і Podman - M3 Бета - 4 області

Документація зі встановлення існує й охоплює поширені шляхи розгортання. Підвищуйте рівень після того, як регулярні перевірки релізів зафіксують поведінку оновлення та томів.

Покриття Експериментальний - 7%Якість Бета - 71%Повнота Бета - 79%Немає

Налаштування контейнерів 6 можливостей

Експериментальний0%

Альфа68%

Бета79%

[Docker](</uk/install/docker>), [Podman](</uk/install/podman>)

Операції з контейнерами 11 можливостей

Експериментальний0%

Альфа68%

Бета79%

[Podman](</uk/install/podman>), [Docker Vm Runtime](</uk/install/docker-vm-runtime>), [Docker](</uk/install/docker>), [Hetzner](</uk/install/hetzner>), [Hostinger](</uk/install/hostinger>)

Випуск і валідація образів 5 можливостей

Експериментальний29%

Бета79%

Бета79%

[Docker](</uk/install/docker>), [Docker Vm Runtime](</uk/install/docker-vm-runtime>), [Повна валідація випуску](</uk/reference/full-release-validation>)

Пісочниця агента та інструменти 3 можливості

Експериментальний0%

Альфа68%

Бета79%

[Docker](</uk/install/docker>), [Docker Vm Runtime](</uk/install/docker-vm-runtime>)

Windows через WSL2 - M3 Бета - 6 областей

Рекомендований шлях Windows із настановами щодо systemd/служби користувача та документацією ланцюжка завантаження. Просувайте після повторних scorecards встановлення/оновлення.

Покриття Експериментальний - 6%Якість Альфа - 69%Повнота Бета - 79%Частково - 5

Налаштування WSL 6 можливостей / з підтримкою LTS

Експериментальний0%

Альфа67%

Бета79%

[Windows](</uk/platforms/windows>), [Початок роботи](</uk/start/getting-started>)

CLI 8 можливостей / з підтримкою LTS

Експериментальний0%

Альфа67%

Бета79%

[Windows](</uk/platforms/windows>), [Початок роботи](</uk/start/getting-started>), [Оновлення](</uk/install/updating>), [Onboard](</uk/cli/onboard>), [Doctor](</uk/cli/doctor>), [Статус](</uk/cli/status>), [Журнали](</uk/cli/logs>)

Життєвий цикл служби Gateway 10 можливостей / з підтримкою LTS

Експериментальний0%

Альфа67%

Бета79%

[Windows](</uk/platforms/windows>), [Індекс](</uk/gateway>), [Doctor](</uk/gateway/doctor>)

Доступ до Gateway і відкриття доступу назовні 11 можливостей / з підтримкою LTS

Експериментальний0%

Альфа67%

Бета79%

[Автентифікація](</uk/gateway/authentication>), [Секрети](</uk/gateway/secrets>), [Віддалений доступ](</uk/gateway/remote>), [Інструкція з відкриття доступу назовні](</uk/gateway/security/exposure-runbook>), [Windows](</uk/platforms/windows>)

Діагностика та відновлення 6 можливостей / з підтримкою LTS

Експериментальний38%

Бета79%

Бета79%

[Windows](</uk/platforms/windows>), [Статус](</uk/cli/status>), [Журнали](</uk/cli/logs>), [Doctor](</uk/cli/doctor>), [Doctor](</uk/gateway/doctor>)

Браузер і інтерфейс керування 6 можливостей

Експериментальний0%

Альфа67%

Бета79%

[Усунення несправностей Browser Wsl2 Windows Remote Cdp](</uk/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Браузер](</uk/tools/browser>), [Інтерфейс керування](</uk/web/control-ui>)

Raspberry Pi і малі пристрої Linux - M3 Бета - 4 області

Документація платформи існує, а шлях Gateway базується на Linux. Потрібне апаратно-специфічне smoke-підтвердження випуску, щоб перейти вище.

Покриття Експериментальний - 0%Якість Альфа - 67%Повнота Бета - 79%Немає

Налаштування та сумісність 12 можливостей

Експериментальний0%

Альфа67%

Бета79%

[Raspberry Pi](</uk/install/raspberry-pi>), [Індекс](</uk/install>), [Поширені запитання щодо першого запуску](</uk/help/faq-first-run>), [Поширені запитання](</uk/help/faq>), [Linux](</uk/platforms/linux>), [Інсталятор](</uk/install/installer>)

Віддалений доступ і автентифікація 9 можливостей

Експериментальний0%

Альфа67%

Бета79%

[Raspberry Pi](</uk/install/raspberry-pi>), [Автентифікація](</uk/gateway/authentication>), [Секрети](</uk/gateway/secrets>), [Сполучення](</uk/gateway/pairing>), [Пристрої](</uk/cli/devices>), [Віддалений доступ](</uk/gateway/remote>), [Tailscale](</uk/gateway/tailscale>)

Середовище виконання Gateway 10 можливостей

Експериментальний0%

Альфа67%

Бета79%

[Індекс](</uk/gateway>), [Gateway](</uk/cli/gateway>), [Raspberry Pi](</uk/install/raspberry-pi>), [Linux](</uk/platforms/linux>), [VPS](</uk/vps>)

Продуктивність і діагностика 5 можливостей

Експериментальний0%

Альфа67%

Бета79%

[Raspberry Pi](</uk/install/raspberry-pi>), [Linux](</uk/platforms/linux>), [Стан](</uk/gateway/health>), [Діагностика](</uk/gateway/diagnostics>)

Супутній застосунок macOS - M3 Бета - 8 сфер

Багатофункціональний застосунок рядка меню, дозволи, режим Node, Canvas, голосова активація, WebChat і віддалений режим уже існують. Він усе ще розвивається достатньо швидко, щоб уникати стабільного рівня.

Покриття Експериментальний - 0%Якість Альфа - 66%Повнота Бета - 78%Немає

Полотно 4 можливості

Експериментальний0%

Альфа66%

Бета78%

[Полотно](</uk/platforms/mac/canvas>), [macOS](</uk/platforms/macos>), [Вебчат](</uk/web/webchat>)

Локальне налаштування 7 можливостей

Експериментальний0%

Альфа66%

Бета78%

[Вбудований Gateway](</uk/platforms/mac/bundled-gateway>), [macOS](</uk/platforms/macos>), [Дочірній процес](</uk/platforms/mac/child-process>), [Налаштування розробки](</uk/platforms/mac/dev-setup>)

Стан і налаштування 5 можливостей

Експериментальний0%

Альфа66%

Бета78%

[Рядок меню](</uk/platforms/mac/menu-bar>), [Піктограма](</uk/platforms/mac/icon>), [macOS](</uk/platforms/macos>), [Справність](</uk/platforms/mac/health>), [Журналювання](</uk/platforms/mac/logging>), [Віддалений доступ](</uk/platforms/mac/remote>)

Нативні можливості 5 можливостей

Експериментальний0%

Альфа66%

Бета78%

[macOS](</uk/platforms/macos>), [XPC](</uk/platforms/mac/xpc>), [Дозволи](</uk/platforms/mac/permissions>), [Підписування](</uk/platforms/mac/signing>), [Peekaboo](</uk/platforms/mac/peekaboo>)

Віддалені підключення 3 можливості

Експериментальний0%

Альфа66%

Бета78%

[Віддалений доступ](</uk/platforms/mac/remote>), [macOS](</uk/platforms/macos>), [Віддалений доступ](</uk/gateway/remote>)

Голос і розмова 3 можливості

Експериментальний0%

Альфа66%

Бета78%

[Voicewake](</uk/platforms/mac/voicewake>), [Голосовий оверлей](</uk/platforms/mac/voice-overlay>), [Розмова](</uk/nodes/talk>), [macOS](</uk/platforms/macos>)

Вебчат 3 можливості

Експериментальний0%

Альфа66%

Бета78%

[Вебчат](</uk/platforms/mac/webchat>), [macOS](</uk/platforms/macos>), [Вебчат](</uk/web/webchat>)

Віддалений вебчат 5 можливостей

Експериментальний0%

Альфа66%

Бета78%

[Вебчат](</uk/platforms/mac/webchat>), [Віддалений доступ](</uk/gateway/remote>), [Віддалений доступ](</uk/platforms/mac/remote>)

Android-застосунок - M2 Alpha - 7 областей

Публічний шлях Google Play існує, але документація застосунку досі описує перезбірку як вкрай альфа-версію та зазначає роботу з посилення релізу.

Покриття експериментальне - 0%Якість альфа - 59%Повнота альфа - 66%Немає

Захоплення медіа 1 можливість

Експериментально0%

Альфа59%

Альфа66%

[Android](</uk/platforms/android>), [Камера](</uk/nodes/camera>)

Мобільний чат 1 можливість

Експериментально0%

Альфа59%

Альфа66%

[Android](</uk/platforms/android>)

Налаштування підключення 1 можливість

Експериментально0%

Альфа59%

Альфа66%

[Android](</uk/platforms/android>), [Bonjour](</uk/gateway/bonjour>), [Сполучення](</uk/gateway/pairing>)

Розповсюдження 3 можливості

Експериментально0%

Альфа59%

Альфа66%

[Android](</uk/platforms/android>)

Налаштування 1 можливість

Експериментально0%

Альфа59%

Альфа66%

[Android](</uk/platforms/android>)

Голос 1 можливість

Експериментально0%

Альфа59%

Альфа66%

[Android](</uk/platforms/android>), [Розмова](</uk/nodes/talk>)

Середовище виконання пристрою 2 можливості

Експериментально0%

Альфа59%

Альфа66%

[Android](</uk/platforms/android>), [Усунення неполадок](</uk/nodes/troubleshooting>), [Протокол](</uk/gateway/protocol>)

Нативний Windows - M2 Альфа - 4 області

Основні потоки CLI/Gateway працюють, але документація досі рекомендує WSL2 для повного досвіду та перелічує застереження щодо нативного запуску.

Покриття Експериментально - 0%Якість Альфа - 58%Повнота Альфа - 66%Частково - 1

CLI 9 можливостей / з підтримкою LTS

Експериментальний0%

Альфа54%

Альфа64%

[Індекс](</uk/install>), [Інсталятор](</uk/install/installer>), [Windows](</uk/platforms/windows>), [Початок роботи](</uk/start/getting-started>), [Onboard](</uk/cli/onboard>)

Керування Gateway 11 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Windows](</uk/platforms/windows>), [Індекс](</uk/gateway>), [Gateway](</uk/cli/gateway>), [Doctor](</uk/cli/doctor>)

Мережа 4 можливості

Експериментальний0%

Альфа59%

Альфа66%

[Windows](</uk/platforms/windows>), [Індекс](</uk/gateway>), [Gateway](</uk/cli/gateway>)

Оновлення 4 можливості

Експериментальний0%

Альфа59%

Альфа66%

[Оновлення](</uk/install/updating>), [CI](</uk/ci>)

Хостинг Kubernetes - M2 Альфа - 4 області

Хостинг Kubernetes — це окремий шлях розгортання кластера на основі Kustomize. Поточна оцінка показує реальний мінімальний шлях розгортання з прогалинами щодо специфічного для Kubernetes CI, пакування ingress/TLS/NetworkPolicy, резервного копіювання й відновлення, а також посилення захисту виробничого доступу.

Покриття Експериментальне - 0%Якість Альфа - 55%Повнота Альфа - 61%Немає

Налаштування розгортання 5 можливостей

Експериментальне0%

Альфа55%

Альфа61%

[Kubernetes](</uk/install/kubernetes>), [Індекс](</uk/install>)

Конфігурація та секрети 5 можливостей

Експериментальне0%

Альфа55%

Альфа61%

[Kubernetes](</uk/install/kubernetes>), [Секрети](</uk/gateway/secrets>), [Середовище](</uk/help/environment>)

Доступ і експонування 5 можливостей

Експериментальне0%

Альфа55%

Альфа61%

[Kubernetes](</uk/install/kubernetes>), [Автентифікація](</uk/gateway/authentication>), [Віддалений доступ](</uk/gateway/remote>), [Регламент експонування](</uk/gateway/security/exposure-runbook>)

Життєвий цикл кластера 5 можливостей

Експериментальне0%

Альфа55%

Альфа61%

[Kubernetes](</uk/install/kubernetes>), [Індекс](</uk/gateway>)

застосунок iOS - M1 Експериментальний - 8 областей

Внутрішній попередній перегляд / супер-альфа. Потоки push-сповіщень TestFlight і через ретранслятор існують, але публічного розповсюдження ще немає.

Покриття Експериментальне - 0%Якість Експериментальна - 41%Повнота Експериментальна - 44%Немає

Медіа та поширення 1 можливість

Експериментальне0%

Експериментальне41%

Експериментальне44%

[Ios](</uk/platforms/ios>), [Камера](</uk/nodes/camera>)

Полотно й екран 1 можливість

Експериментальне0%

Експериментальне41%

Експериментальне44%

[Ios](</uk/platforms/ios>), [Canvas](</uk/plugins/reference/canvas>)

Чат і сеанси 1 можливість

Експериментальне0%

Експериментальне41%

Експериментальне44%

[Ios](</uk/platforms/ios>), [Webchat](</uk/web/webchat>), [Протокол](</uk/gateway/protocol>)

Налаштування та діагностика Gateway 7 можливостей

Експериментальне0%

Експериментальне41%

Експериментальне44%

[Ios](</uk/platforms/ios>), [Сполучення](</uk/channels/pairing>)

Розповсюдження 1 можливість

Експериментальне0%

Експериментальне41%

Експериментальне44%

[Ios](</uk/platforms/ios>)

Команди пристрою 2 можливості

Експериментальне0%

Експериментальне41%

Експериментальне44%

[Ios](</uk/platforms/ios>), [Протокол](</uk/gateway/protocol>)

Сповіщення та фоновий режим 1 можливість

Експериментальне0%

Експериментальне41%

Експериментальне44%

[Ios](</uk/platforms/ios>), [Конфігурація](</uk/gateway/configuration>)

Голос 1 можливість

Експериментальне0%

Експериментальне41%

Експериментальне44%

[Ios](</uk/platforms/ios>), [Розмова](</uk/nodes/talk>)

Nix install path - M1 Experimental - 5 areas

Необов’язковий процес встановлення. Потребує чіткішої гарантії підтримки перед просуванням до alpha/beta.

Покриття експериментальне - 0%Якість експериментальна - 41%Повнота експериментальна - 44%Немає

Передавання встановлення 4 можливості

Експериментально0%

Експериментально41%

Експериментально44%

[Nix](</uk/install/nix>), [Індекс](</uk/install>), [Каталог документації](</uk/start/docs-directory>)

Життєвий цикл Plugin 4 можливості

Експериментально0%

Експериментально41%

Експериментально44%

[Керування Plugins](</uk/plugins/manage-plugins>), [Plugin](</uk/tools/plugin>), [Nix](</uk/install/nix>)

Активація та UX застосунку 7 можливостей

Експериментально0%

Експериментально41%

Експериментально44%

[Nix](</uk/install/nix>)

Конфігурація та стан 7 можливостей

Експериментально0%

Експериментально41%

Експериментально44%

[Nix](</uk/install/nix>), [Налаштування](</uk/cli/setup>), [Середовище](</uk/help/environment>)

Середовище виконання служби та захисти 8 можливостей

Експериментально0%

Експериментально41%

Експериментально44%

[Nix](</uk/install/nix>), [Налаштування](</uk/cli/setup>), [Doctor](</uk/cli/doctor>), [Оновлення](</uk/cli/update>)

супровідні поверхні watchOS - M1 Експериментально - 5 областей

Джерело містить поверхні застосунку/розширення Watch; публічна документація ще не подає це як користувацьку функцію.

Покриття Експериментально - 0%Якість Експериментально - 41%Повнота Експериментально - 44%Немає

Доставка та відновлення 7 можливостей

Експериментально0%

Експериментально41%

Експериментально44%

[iOS](</uk/platforms/ios>)

Схвалення виконання 3 можливості

Експериментально0%

Експериментально41%

Експериментально44%

[Схвалення виконання](</uk/tools/exec-approvals>), [iOS](</uk/platforms/ios>)

Розповсюдження та підтримка 6 можливостей

Експериментально0%

Експериментально41%

Експериментально44%

[iOS](</uk/platforms/ios>)

Сповіщення та відповіді 7 можливостей

Експериментально0%

Експериментально41%

Експериментально44%

[iOS](</uk/platforms/ios>)

Інтерфейс застосунку для годинника 3 можливості

Експериментально0%

Експериментально41%

Експериментально44%

[iOS](</uk/platforms/ios>)

Супровідний застосунок Linux - M0 заплановано - 5 областей

У документації зазначено, що нативні супровідні застосунки Linux заплановано; Gateway є підтримуваним шляхом Linux на сьогодні.

Покриття експериментальне - 0%Якість експериментальна - 19%Завершеність експериментальна - 21%Немає

Розповсюдження застосунку 3 можливості

Експериментально0%

Експериментально19%

Експериментально21%

[Linux](</uk/platforms/linux>), [Індекс](</uk/platforms>), [Індекс](</uk/install>)

Підключення Gateway 4 можливості

Експериментально0%

Експериментально19%

Експериментально21%

[Linux](</uk/platforms/linux>), [Індекс](</uk/gateway>), [Сполучення](</uk/gateway/pairing>), [Віддалений доступ](</uk/gateway/remote>)

Чат і сеанси 3 можливості

Експериментально0%

Експериментально19%

Експериментально21%

[Linux](</uk/platforms/linux>), [Протокол](</uk/gateway/protocol>), [Вебчат](</uk/web/webchat>)

Можливості настільного середовища 9 можливостей

Експериментально0%

Експериментально19%

Експериментально21%

[Linux](</uk/platforms/linux>), [Підтвердження Exec](</uk/tools/exec-approvals>), [Секрети](</uk/gateway/secrets>), [Індекс](</uk/nodes>), [Exec](</uk/tools/exec>), [Розмова](</uk/nodes/talk>), [Камера](</uk/nodes/camera>)

Стан і діагностика 7 можливостей

Експериментально0%

Експериментально19%

Експериментально21%

[Linux](</uk/platforms/linux>), [OpenClaw](</uk/start/openclaw>), [Doctor](</uk/gateway/doctor>)

Нативний супровідний застосунок для Windows - M0 Заплановано - 5 областей

Лише заплановано.

Покриття експериментальне - 0%Якість експериментальна - 19%Завершеність експериментальна - 21%Немає

Встановлення й оновлення 4 можливості

Експериментальний0%

Експериментальний19%

Експериментальний21%

[Windows](</uk/platforms/windows>), [Індекс](</uk/install>)

Підключення Gateway 3 можливості

Експериментальний0%

Експериментальний19%

Експериментальний21%

[Windows](</uk/platforms/windows>), [Індекс](</uk/gateway>), [Спарювання](</uk/gateway/pairing>), [Віддалений доступ](</uk/gateway/remote>)

Сеанси чату 2 можливості

Експериментальний0%

Експериментальний19%

Експериментальний21%

[Windows](</uk/platforms/windows>), [Протокол](</uk/gateway/protocol>)

Стан і відновлення 5 можливостей

Експериментальний0%

Експериментальний19%

Експериментальний21%

[Windows](</uk/platforms/windows>), [Doctor](</uk/gateway/doctor>), [Індекс](</uk/gateway>)

Інструменти робочого стола й дозволи 10 можливостей

Експериментальний0%

Експериментальний19%

Експериментальний21%

[Windows](</uk/platforms/windows>), [Індекс](</uk/nodes>), [Exec](</uk/tools/exec>), [Затвердження Exec](</uk/tools/exec-approvals>), [Індекс](</uk/gateway/security>)

### Канал

Discord - M4 стабільний - 6 областей

Докладна документація та широке покриття функцій. Шляхи голосу/делегування мають і надалі оцінюватися окремо як beta/alpha.

Покриття експериментальне - 0%Якість Beta - 73%Повнота стабільна - 87%Частково - 4

Налаштування та операції каналу 10 можливостей / підтримується LTS

Експериментальний0%

Бета73%

Стабільний87%

[Discord](</uk/channels/discord>), [Discord](</uk/plugins/reference/discord>), [Fly](</uk/install/fly>), [Slash-команди](</uk/tools/slash-commands>), [Стан справності](</uk/gateway/health>), [Канали](</uk/cli/channels>), [Канали конфігурації](</uk/gateway/config-channels>)

Доступ та ідентичність 6 можливостей / підтримується LTS

Експериментальний0%

Бета73%

Стабільний87%

[Discord](</uk/channels/discord>), [Сполучення](</uk/channels/pairing>), [Групи доступу](</uk/channels/access-groups>), [Групи](</uk/channels/groups>)

Маршрутизація та доставлення розмов 12 можливостей / підтримується LTS

Експериментальний0%

Бета73%

Стабільний87%

[Discord](</uk/channels/discord>), [Маршрутизація каналів](</uk/channels/channel-routing>), [Групи](</uk/channels/groups>), [Групи доступу](</uk/channels/access-groups>), [Агенти ACP](</uk/tools/acp-agents>), [Субагенти](</uk/tools/subagents>)

Медіа та розширений вміст 1 можливість / підтримується LTS

Експериментальний0%

Бета73%

Стабільний87%

[Discord](</uk/channels/discord>)

Нативні елементи керування та схвалення 5 можливостей

Експериментальний0%

Бета73%

Стабільний87%

[Discord](</uk/channels/discord>), [Slash-команди](</uk/tools/slash-commands>)

Голос і виклики в реальному часі 5 можливостей

Експериментальний0%

Бета73%

Стабільний87%

[Discord](</uk/channels/discord>), [Openai](</uk/providers/openai>), [Elevenlabs](</uk/providers/elevenlabs>), [QA E2E-автоматизація](</uk/concepts/qa-e2e-automation>), [Канали конфігурації](</uk/gateway/config-channels>)

Telegram - M3 Бета - 5 областей

Основний канал достатньо зрілий для регулярного використання, але UX із високою варіативністю та граничні випадки з медіа потребують регулярного підтвердження сценаріями.

Покриття Експериментальний - 0%Якість Альфа - 68%Повнота Бета - 78%Повне - 5

Налаштування та експлуатація каналів 10 можливостей / з підтримкою LTS

Експериментальний0%

Альфа66%

Бета78%

[Telegram](</uk/channels/telegram>), [Налаштування каналів](</uk/gateway/config-channels>), [Канали](</uk/cli/channels>)

Доступ та ідентичність 10 можливостей / з підтримкою LTS

Експериментальний0%

Альфа66%

Бета78%

[Telegram](</uk/channels/telegram>), [Сполучення](</uk/channels/pairing>), [Групи доступу](</uk/channels/access-groups>), [Групи](</uk/channels/groups>), [Кілька агентів](</uk/concepts/multi-agent>)

Маршрутизація та доставлення розмов 1 можливість / з підтримкою LTS

Експериментальний0%

Альфа66%

Бета78%

[Telegram](</uk/channels/telegram>), [Групи](</uk/channels/groups>), [Кілька агентів](</uk/concepts/multi-agent>)

Медіа та розширений вміст 1 можливість / з підтримкою LTS

Експериментальний0%

Альфа66%

Бета78%

[Telegram](</uk/channels/telegram>), [Місцеперебування](</uk/channels/location>)

Нативні елементи керування та затвердження 9 можливостей / з підтримкою LTS

Експериментальний0%

Бета77%

Бета79%

[Telegram](</uk/channels/telegram>), [Затвердження виконання](</uk/tools/exec-approvals>), [Реакції](</uk/tools/reactions>)

Slack - M3 Бета - 5 сфер

Повноцінна документація каналу та поверхня маршрутизації. Потрібні оціночні карти сценаріїв встановлення робочого простору й адміністрування.

Покриття Експериментальний - 0%Якість Альфа - 66%Повнота Бета - 78%Повне - 5

Налаштування та експлуатація каналів 10 можливостей / з підтримкою LTS

Експериментальний0%

Альфа66%

Бета78%

[Slack](</uk/channels/slack>), [Slack](</uk/plugins/reference/slack>), [Секрети](</uk/gateway/secrets>), [Автоматизація QA E2E](</uk/concepts/qa-e2e-automation>), [Усунення несправностей](</uk/channels/troubleshooting>)

Доступ та ідентифікація 1 можливість / з підтримкою LTS

Експериментальний0%

Альфа66%

Бета78%

[Slack](</uk/channels/slack>), [Сполучення](</uk/channels/pairing>)

Маршрутизація та доставка розмов 5 можливостей / з підтримкою LTS

Експериментальний0%

Альфа66%

Бета78%

[Slack](</uk/channels/slack>), [Захист від циклів ботів](</uk/channels/bot-loop-protection>), [Сполучення](</uk/channels/pairing>)

Медіа та розширений вміст 1 можливість / з підтримкою LTS

Експериментальний0%

Альфа66%

Бета78%

[Slack](</uk/channels/slack>), [Автоматизація QA E2E](</uk/concepts/qa-e2e-automation>)

Нативні елементи керування та затвердження 8 можливостей / з підтримкою LTS

Експериментальний0%

Альфа66%

Бета78%

[Slack](</uk/channels/slack>), [Слеш-команди](</uk/tools/slash-commands>), [Затвердження виконання](</uk/tools/exec-approvals>)

iMessage and BlueBubbles - M3 Beta - 5 areas

Підтримуваний iMessage працює через imsg на хості macOS Messages із виконаним входом; застарілі конфігурації BlueBubbles потребують міграції. Залишайте видимими дозволи macOS, SSH-обгортку, SIP/приватний API та застереження щодо міграції.

Покриття Експериментальний - 0%Якість Альфа - 66%Повнота Бета - 78%Немає

Налаштування та операції каналу 11 можливостей

Експериментальний0%

Alpha66%

Beta78%

[Bluebubbles Imessage](</uk/announcements/bluebubbles-imessage>), [Imessage From Bluebubbles](</uk/channels/imessage-from-bluebubbles>), [Налаштування каналів](</uk/gateway/config-channels>), [Imessage](</uk/channels/imessage>)

Доступ та ідентичність 6 можливостей

Експериментальний0%

Alpha66%

Beta78%

[Imessage](</uk/channels/imessage>), [Imessage From Bluebubbles](</uk/channels/imessage-from-bluebubbles>), [Налаштування каналів](</uk/gateway/config-channels>)

Маршрутизація та доставлення розмов 4 можливості

Експериментальний0%

Alpha66%

Beta78%

[Imessage](</uk/channels/imessage>)

Медіа та розширений вміст 7 можливостей

Експериментальний0%

Alpha66%

Beta78%

[Imessage](</uk/channels/imessage>), [Imessage From Bluebubbles](</uk/channels/imessage-from-bluebubbles>), [Налаштування каналів](</uk/gateway/config-channels>)

Нативні елементи керування та підтвердження 3 можливості

Експериментальний0%

Alpha66%

Beta78%

[Imessage](</uk/channels/imessage>)

WhatsApp - M3 Beta - 5 областей

Основний шлях важливий і задокументований; нестабільність upstream Baileys/сесій утримує його нижче за Stable.

Покриття: Експериментальний - 0%Якість Alpha - 66%Повнота Beta - 78%Немає

Налаштування та експлуатація каналів 5 можливостей

Експериментальний0%

Alpha66%

Beta78%

[Whatsapp](</uk/channels/whatsapp>), [Канали конфігурації](</uk/gateway/config-channels>), [Whatsapp](</uk/plugins/reference/whatsapp>), [Автоматизація QA E2E](</uk/concepts/qa-e2e-automation>), [Doctor](</uk/gateway/doctor>)

Доступ та ідентичність 7 можливостей

Експериментальний0%

Alpha66%

Beta78%

[Whatsapp](</uk/channels/whatsapp>), [Канали конфігурації](</uk/gateway/config-channels>), [Автоматизація QA E2E](</uk/concepts/qa-e2e-automation>), [Сполучення](</uk/channels/pairing>)

Маршрутизація та доставлення розмов 4 можливості

Експериментальний0%

Alpha66%

Beta78%

[Whatsapp](</uk/channels/whatsapp>), [Групові повідомлення](</uk/channels/group-messages>)

Медіа та розширений вміст 2 можливості

Експериментальний0%

Alpha66%

Beta78%

[Whatsapp](</uk/channels/whatsapp>)

Нативні елементи керування та схвалення 2 можливості

Експериментальний0%

Alpha66%

Beta78%

[Whatsapp](</uk/channels/whatsapp>)

Matrix - M2 Alpha - 6 областей

Підтримується через вбудований plugin. Потрібні міст, автентифікація та scorecard-и життєвого циклу кімнат.

Покриття Експериментальний - 0%Якість Alpha - 60%Повнота Alpha - 67%Немає

Налаштування та експлуатація каналів 5 можливостей

Експериментальний0%

Альфа60%

Альфа67%

[Matrix](</uk/channels/matrix>), [Міграція Matrix](</uk/channels/matrix-migration>)

Доступ та ідентичність 7 можливостей

Експериментальний0%

Альфа60%

Альфа67%

[Matrix](</uk/channels/matrix>), [Групи](</uk/channels/groups>), [Захист від циклу ботів](</uk/channels/bot-loop-protection>)

Маршрутизація та доставка розмов 1 можливість

Експериментальний0%

Альфа60%

Альфа67%

[Matrix](</uk/channels/matrix>)

Медіа та насичений контент 1 можливість

Експериментальний0%

Альфа60%

Альфа67%

[Matrix](</uk/channels/matrix>)

Нативні елементи керування та затвердження 6 можливостей

Експериментальний0%

Альфа60%

Альфа67%

[Matrix](</uk/channels/matrix>)

Шифрування та перевірка 3 можливості

Експериментальний0%

Альфа60%

Альфа67%

[Matrix](</uk/channels/matrix>), [Міграція Matrix](</uk/channels/matrix-migration>)

Google Chat - M2 Alpha - 5 областей

Задокументований канал, але корпоративне/адміністративне налаштування підвищує ризик зрілості.

Покриття Експериментальний - 0%Якість Альфа - 59%Завершеність Альфа - 66%Немає

Налаштування та експлуатація каналів 16 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Googlechat](</uk/channels/googlechat>), [Googlechat](</uk/plugins/reference/googlechat>), [Канали конфігурації](</uk/gateway/config-channels>), [Довідник CLI майстра](</uk/start/wizard-cli-reference>), [Секрети](</uk/gateway/secrets>), [Поверхня облікових даних Secretref](</uk/reference/secretref-credential-surface>), [Справність](</uk/gateway/health>), [Інвентар Plugin](</uk/plugins/plugin-inventory>), [Покажчик](</uk/channels>)

Доступ та ідентичність 11 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Googlechat](</uk/channels/googlechat>), [Сполучення](</uk/channels/pairing>), [Групи доступу](</uk/channels/access-groups>), [Канали конфігурації](</uk/gateway/config-channels>), [Захист від циклу ботів](</uk/channels/bot-loop-protection>), [Маршрутизація каналів](</uk/channels/channel-routing>)

Маршрутизація розмов і доставка 1 можливість

Експериментальний0%

Альфа59%

Альфа66%

[Googlechat](</uk/channels/googlechat>), [Захист від циклу ботів](</uk/channels/bot-loop-protection>), [Групи доступу](</uk/channels/access-groups>), [Маршрутизація каналів](</uk/channels/channel-routing>)

Медіа та розширений вміст 1 можливість

Експериментальний0%

Альфа59%

Альфа66%

[Googlechat](</uk/channels/googlechat>), [Повідомлення](</uk/cli/message>), [Розуміння медіа](</uk/nodes/media-understanding>), [Поверхня облікових даних Secretref](</uk/reference/secretref-credential-surface>)

Нативні елементи керування та схвалення 16 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Googlechat](</uk/channels/googlechat>), [Повідомлення](</uk/cli/message>), [Розуміння медіа](</uk/nodes/media-understanding>), [Поверхня облікових даних Secretref](</uk/reference/secretref-credential-surface>), [Реакції](</uk/tools/reactions>), [Slash-команди](</uk/tools/slash-commands>), [Конфігурація агентів](</uk/gateway/config-agents>), [Рефакторинг життєвого циклу повідомлень](</uk/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Альфа - 5 областей

Потоки корпоративної автентифікації та адміністрування потребують явного підтвердження сценаріями.

Покриття експериментальне - 0%Якість Альфа - 59%Повнота Альфа - 66%Немає

Налаштування та експлуатація каналу 9 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Msteams](</uk/channels/msteams>), [Msteams](</uk/plugins/reference/msteams>), [Налаштування каналів](</uk/gateway/config-channels>), [Стан справності](</uk/gateway/health>)

Доступ та ідентичність 9 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Msteams](</uk/channels/msteams>), [Сполучення](</uk/channels/pairing>), [Групи доступу](</uk/channels/access-groups>)

Маршрутизація та доставка розмов 5 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Msteams](</uk/channels/msteams>), [Групи](</uk/channels/groups>), [Маршрутизація каналів](</uk/channels/channel-routing>)

Медіа та розширений вміст 5 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Msteams](</uk/channels/msteams>)

Нативні елементи керування та затвердження 5 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Msteams](</uk/channels/msteams>), [Розширені затвердження Exec](</uk/tools/exec-approvals-advanced>)

Signal - M2 Альфа - 5 областей

Документація підтримуваного каналу існує; потрібні переконливіші докази встановлення та повторного підключення.

Покриття Експериментальний - 0%Якість Альфа - 59%Повнота Альфа - 66%Немає

Налаштування та експлуатація каналів 7 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Signal](</uk/channels/signal>), [Signal](</uk/plugins/reference/signal>)

Доступ та ідентичність 6 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Signal](</uk/channels/signal>)

Маршрутизація та доставка розмов 1 можливість

Експериментальний0%

Альфа59%

Альфа66%

[Signal](</uk/channels/signal>)

Медіа та насичений вміст 7 можливостей

Експериментальний0%

Альфа59%

Альфа66%

[Signal](</uk/channels/signal>)

Нативні елементи керування та затвердження 3 можливості

Експериментальний0%

Альфа59%

Альфа66%

[Signal](</uk/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, регіональні канали - M2 Альфа - 4 області

Важливе регіональне покриття, але рівень публічної підтримки слід калібрувати за типом облікового запису, затвердженням upstream і підтвердженням від супровідників.

Покриття Експериментальний - 0%Якість Альфа - 55%Повнота Альфа - 58%Немає

Налаштування й експлуатація каналів 6 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Індекс](</uk/channels>), [Сполучення](</uk/channels/pairing>), [Feishu](</uk/plugins/reference/feishu>), [Внутрішня архітектура](</uk/plugins/architecture-internals>)

Доступ та ідентичність 1 можливість

Експериментальний0%

Альфа53%

Альфа54%

Немає пов’язаної документації

Маршрутизація та доставлення розмов 1 можливість

Експериментальний0%

Альфа53%

Альфа54%

Немає пов’язаної документації

Медіа та насичений вміст 1 можливість

Експериментальний0%

Альфа53%

Альфа54%

Немає пов’язаної документації

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Альфа - 4 області

Підтримувані поверхні існують, але зрілість, імовірно, залежить від покриття upstream і супровідників. Оцініть окремо пізніше.

Покриття Експериментальний - 0%Якість Альфа - 53%Повнота Альфа - 54%Немає

Налаштування каналу та операції 1 можливість

Експериментальний0%

Альфа53%

Альфа54%

Немає пов’язаної документації

Доступ та ідентичність 1 можливість

Експериментальний0%

Альфа53%

Альфа54%

Немає пов’язаної документації

Маршрутизація та доставка розмов 1 можливість

Експериментальний0%

Альфа53%

Альфа54%

Немає пов’язаної документації

Медіа та насичений вміст 1 можливість

Експериментальний0%

Альфа53%

Альфа54%

Немає пов’язаної документації

Канал голосових викликів - M1 Експериментальний - 5 областей

Необов’язковий шлях/шлях Plugin зі складною поведінкою в реальному часі. Потребує картки оцінювання сценаріїв перед публічною бета-версією.

Покриття: експериментальний - 0%Якість: експериментальний - 41%Повнота: експериментальний - 44%Немає

Налаштування й операції каналів 2 можливості

Експериментальний0%

Експериментальний41%

Експериментальний44%

[Голосовий виклик](</uk/cli/voicecall>), [Голосовий виклик](</uk/plugins/voice-call>), [Протокол](</uk/gateway/protocol>)

Доступ та ідентичність 1 можливість

Експериментальний0%

Експериментальний41%

Експериментальний44%

[Голосовий виклик](</uk/plugins/voice-call>), [Голосовий виклик](</uk/cli/voicecall>)

Маршрутизація та доставка розмов 1 можливість

Експериментальний0%

Експериментальний41%

Експериментальний44%

[Голосовий виклик](</uk/plugins/voice-call>)

Медіа та розширений вміст 2 можливості

Експериментальний0%

Експериментальний41%

Експериментальний44%

[Голосовий виклик](</uk/plugins/voice-call>), [Інвентар Plugin](</uk/plugins/plugin-inventory>)

Голос і виклики в реальному часі 2 можливості

Експериментальний0%

Експериментальний41%

Експериментальний44%

[Голосовий виклик](</uk/plugins/voice-call>)

### Провайдер та інструмент

Автоматизація браузера, exec та інструменти пісочниці - M3 Бета - 3 області

Основні інструменти задокументовано, але безпека хоста та UX дозволів мають залишатися під активним переглядом у системі оцінювання.

Покриття Експериментальне - 21%Якість Бета - 75%Повнота Бета - 79%Частково - 2

Автоматизація браузера 8 можливостей

Експериментально13%

Бета79%

Бета79%

[Керування браузером](</uk/tools/browser-control>), [Тестування](</uk/help/testing>), [Браузер](</uk/tools/browser>), [Індекс](</uk/gateway/security>), [Аудиторські перевірки](</uk/gateway/security/audit-checks>)

Виклик і виконання інструментів 6 можливостей / підтримується LTS

Альфа50%

Бета79%

Бета79%

[Виконання](</uk/tools/exec>), [Фоновий процес](</uk/gateway/background-process>), [HTTP API виклику інструментів](</uk/gateway/tools-invoke-http-api>), [Області дії оператора](</uk/gateway/operator-scopes>), [Протокол](</uk/gateway/protocol>), [Схвалення виконання](</uk/tools/exec-approvals>), [Розширені схвалення виконання](</uk/tools/exec-approvals-advanced>), [Підвищені права](</uk/tools/elevated>)

Пісочниця та політика інструментів 6 можливостей / підтримується LTS

Експериментально0%

Альфа68%

Бета79%

[Ізоляція в пісочниці](</uk/gateway/sandboxing>), [Пісочниця проти політики інструментів проти підвищених прав](</uk/gateway/sandbox-vs-tool-policy-vs-elevated>), [Інструменти пісочниці для кількох агентів](</uk/tools/multi-agent-sandbox-tools>), [Довідник обв’язки Codex](</uk/plugins/codex-harness-reference>), [Інструменти конфігурації](</uk/gateway/config-tools>)

Шлях провайдера OpenAI і Codex - M3 Бета - 5 областей

Поглиблена документація, шлях OAuth/підписки, голос у реальному часі, зображення та поведінка сумісності. Змінність провайдера не дає цьому перейти до стабільного рівня без доказу з релізної оцінювальної таблиці.

Покриття експериментальне - 26%Якість бета - 74%Повнота бета - 79%Частково - 3

Модель і автентифікація 6 можливостей / підтримується LTS

Експериментальний44%

Бета79%

Бета79%

[Openai](</uk/providers/openai>), [Середовище Codex](</uk/plugins/codex-harness>), [Моделі](</uk/concepts/models>), [Oauth](</uk/concepts/oauth>), [Довідник середовища Codex](</uk/plugins/codex-harness-reference>), [Моніторинг автентифікації](</uk/gateway/authentication>)

Сумісність відповідей та інструментів 4 можливості / підтримується LTS

Експериментальний40%

Бета79%

Бета79%

[Openai](</uk/providers/openai>), [HTTP API Openresponses](</uk/gateway/openresponses-http-api>), [HTTP API Openai](</uk/gateway/openai-http-api>), [Нативні Plugin для Codex](</uk/plugins/codex-native-plugins>)

Нативне середовище Codex 2 можливості / підтримується LTS

Експериментальний44%

Бета79%

Бета79%

[Середовище Codex](</uk/plugins/codex-harness>), [Середовище виконання Codex](</uk/plugins/codex-harness-runtime>), [Довідник середовища Codex](</uk/plugins/codex-harness-reference>), [Нативні Plugin для Codex](</uk/plugins/codex-native-plugins>)

Зображення та мультимодальне введення 2 можливості

Експериментальний0%

Альфа67%

Бета79%

[Openai](</uk/providers/openai>), [Генерація зображень](</uk/tools/image-generation>), [Зображення](</uk/nodes/images>)

Голос і аудіо в реальному часі 2 можливості

Експериментальний0%

Альфа67%

Бета79%

[Openai](</uk/providers/openai>), [Discord](</uk/channels/discord>), [Голосовий виклик](</uk/plugins/voice-call>)

Інструменти вебпошуку - M3 Бета - 4 області

Існують кілька провайдерів і документація. Потрібне підтвердження квот, помилок і SSRF для кожної родини провайдерів.

Покриття експериментальне - 9%Якість бета - 74%Повнота бета - 79%Немає

Постачальники пошуку 19 можливостей

Експериментальний11%

Бета79%

Бета79%

[Веб](</uk/tools/web>), [Пошук Brave](</uk/tools/brave-search>), [Tavily](</uk/tools/tavily>), [Пошук Exa](</uk/tools/exa-search>), [Firecrawl](</uk/tools/firecrawl>), [Пошук Perplexity](</uk/tools/perplexity-search>), [Пошук Duckduckgo](</uk/tools/duckduckgo-search>), [Пошук Searxng](</uk/tools/searxng-search>), [Пошук Gemini](</uk/tools/gemini-search>), [Пошук Grok](</uk/tools/grok-search>), [Пошук Kimi](</uk/tools/kimi-search>), [Пошук Minimax](</uk/tools/minimax-search>), [Пошук Ollama](</uk/tools/ollama-search>), [Підшляхи SDK](</uk/plugins/sdk-subpaths>), [Огляд SDK](</uk/plugins/sdk-overview>), [Маніфест](</uk/plugins/manifest>)

Налаштування й діагностика 9 можливостей

Експериментальний0%

Альфа68%

Бета79%

[Веб](</uk/tools/web>), [Отримання вебвмісту](</uk/tools/web-fetch>), [Поширені запитання](</uk/help/faq>), [Витрати на використання API](</uk/reference/api-usage-costs>), [Пошук Brave](</uk/tools/brave-search>), [Пошук Perplexity](</uk/tools/perplexity-search>), [Tavily](</uk/tools/tavily>), [Firecrawl](</uk/tools/firecrawl>)

Безпека мережі 4 можливості

Експериментальний0%

Альфа68%

Бета79%

[Веб](</uk/tools/web>), [Отримання вебвмісту](</uk/tools/web-fetch>), [Firecrawl](</uk/tools/firecrawl>), [Пошук Searxng](</uk/tools/searxng-search>)

Доступність інструментів і отримання даних 11 можливостей

Експериментальний25%

Бета79%

Бета79%

[Інструменти конфігурації](</uk/gateway/config-tools>), [Отримання вебвмісту](</uk/tools/web-fetch>), [Веб](</uk/tools/web>), [Поширені запитання](</uk/help/faq>)

Шлях постачальника Anthropic - M3 Бета - 5 сфер

Повноцінний постачальник моделей. Потребує регулярного підтвердження сценаріїв автентифікації, каталогу та виклику інструментів.

Покриття Експериментальний - 0%Якість Бета - 71%Повнота Бета - 78%Немає

Автентифікація й відновлення провайдера 9 можливостей

Експериментально0%

Альфа66%

Бета78%

[Anthropic](</uk/providers/anthropic>), [Doctor](</uk/gateway/doctor>), [Приклади конфігурації](</uk/gateway/configuration-examples>), [Усунення несправностей](</uk/gateway/troubleshooting>), [Кешування промптів](</uk/reference/prompt-caching>)

Вибір моделі й середовища виконання 10 можливостей

Експериментально0%

Бета78%

Бета79%

[Anthropic](</uk/providers/anthropic>), [Налаштування агентів](</uk/gateway/config-agents>), [Моделі](</uk/concepts/models>), [CLI-бекенди](</uk/gateway/cli-backends>)

Транспорт запитів і семантика ходів 10 можливостей

Експериментально0%

Бета77%

Бета79%

[Anthropic](</uk/providers/anthropic>), [Кешування промптів](</uk/reference/prompt-caching>), [Усунення несправностей](</uk/gateway/troubleshooting>), [CLI-бекенди](</uk/gateway/cli-backends>), [Провайдери моделей](</uk/concepts/model-providers>)

Кеш промптів і контекст 5 можливостей

Експериментально0%

Альфа66%

Бета78%

[Anthropic](</uk/providers/anthropic>), [Кешування промптів](</uk/reference/prompt-caching>), [Усунення несправностей](</uk/gateway/troubleshooting>), [Heartbeat](</uk/gateway/heartbeat>)

Медіавхідні дані 4 можливості

Експериментально0%

Альфа66%

Бета78%

[Anthropic](</uk/providers/anthropic>), [Налаштування агентів](</uk/gateway/config-agents>)

Шлях провайдера Google - M3 Бета - 5 сфер

Повноцінний провайдер із поверхнями моделей і реального часу. Потребує окремого оцінювання Live/Talk.

Покриття Експериментально - 0%Якість Альфа - 66%Повнота Бета - 78%Немає

Налаштування провайдера та облікові дані 10 можливостей

Експериментальний0%

Alpha66%

Beta78%

[Google](</uk/providers/google>), [Провайдери моделей](</uk/concepts/model-providers>)

Маршрутизація моделей і кінцеві точки 10 можливостей

Експериментальний0%

Alpha66%

Beta78%

[Google](</uk/providers/google>), [Провайдери моделей](</uk/concepts/model-providers>), [Google](</uk/plugins/reference/google>), [Пошук Gemini](</uk/tools/gemini-search>)

Безпосередній runtime Gemini 9 можливостей

Експериментальний0%

Alpha66%

Beta78%

[Google](</uk/providers/google>), [Провайдери моделей](</uk/concepts/model-providers>), [Поширені запитання про моделі](</uk/help/faq-models>), [Тестування наживо](</uk/help/testing-live>)

Медіа, пошук і реальний час 10 можливостей

Експериментальний0%

Alpha66%

Beta78%

[Google](</uk/plugins/reference/google>), [Google](</uk/providers/google>)

Кешування промптів 5 можливостей

Експериментальний0%

Alpha66%

Beta78%

[Кешування промптів](</uk/reference/prompt-caching>), [Google](</uk/providers/google>), [Провайдери моделей](</uk/concepts/model-providers>), [Використання токенів](</uk/reference/token-use>)

Шлях провайдера OpenRouter - M3 Beta - 4 області

Уніфікований шлях провайдера задокументований і цінний, але поведінка залежить від конкретної моделі.

Покриття Експериментальний - 0%Якість Alpha - 66%Завершеність Beta - 78%Немає

Налаштування провайдера та автентифікація 14 можливостей

Експериментальний0%

Альфа66%

Бета78%

[Openrouter](</uk/providers/openrouter>), [Провайдери моделей](</uk/concepts/model-providers>), [Налаштування](</uk/cli/configure>), [Автентифікація](</uk/gateway/authentication>), [Середовище](</uk/help/environment>), [Моделі](</uk/cli/models>), [Моделі](</uk/concepts/models>)

Середовище виконання чату та нормалізація 15 можливостей

Експериментальний0%

Альфа66%

Бета78%

[Openrouter](</uk/providers/openrouter>), [Провайдери моделей](</uk/concepts/model-providers>), [Кешування промптів](</uk/reference/prompt-caching>)

Відновлення провайдера та діагностика 5 можливостей

Експериментальний0%

Альфа66%

Бета78%

[Відмовостійке перемикання моделей](</uk/concepts/model-failover>), [Openrouter](</uk/providers/openrouter>), [Моделі](</uk/cli/models>)

Генерація медіа та мовлення 7 можливостей

Експериментальний0%

Альфа66%

Бета78%

[Openrouter](</uk/providers/openrouter>), [Генерація зображень](</uk/tools/image-generation>), [Генерація музики](</uk/tools/music-generation>), [Огляд медіа](</uk/tools/media-overview>), [Генерація відео](</uk/tools/video-generation>), [TTS](</uk/tools/tts>)

Інструменти генерації зображень, відео та музики - M2 Альфа - 5 областей

Можливість існує в різних провайдерів, але якість, затримка та сумісність параметрів надто різняться для бета-версії без підтвердження для кожного провайдера.

Покриття Експериментальний - 0%Якість Альфа - 61%Повнота Альфа - 68%Немає

Маршрутизація та виявлення медіа 4 можливості

Експериментально0%

Альфа61%

Альфа68%

[Агенти конфігурації](</uk/gateway/config-agents>), [Генерація зображень](</uk/tools/image-generation>), [Генерація відео](</uk/tools/video-generation>), [Генерація музики](</uk/tools/music-generation>)

Життєвий цикл і доставка завдань 12 можливостей

Експериментально0%

Альфа61%

Альфа68%

[Огляд медіа](</uk/tools/media-overview>), [Генерація зображень](</uk/tools/image-generation>), [Генерація відео](</uk/tools/video-generation>), [Генерація музики](</uk/tools/music-generation>)

Генерація зображень 9 можливостей

Експериментально0%

Альфа61%

Альфа68%

[Генерація зображень](</uk/tools/image-generation>), [Infer](</uk/cli/infer>), [Огляд медіа](</uk/tools/media-overview>)

Генерація відео 11 можливостей

Експериментально0%

Альфа61%

Альфа68%

[Генерація відео](</uk/tools/video-generation>), [Runway](</uk/providers/runway>), [Pixverse](</uk/providers/pixverse>), [Fal](</uk/providers/fal>), [Openrouter](</uk/providers/openrouter>)

Генерація музики 6 можливостей

Експериментально0%

Альфа61%

Альфа68%

[Генерація музики](</uk/tools/music-generation>)

Постачальники локальних моделей: Ollama, vLLM, SGLang, LM Studio - M2 Альфа - 5 областей

Корисно й задокументовано, але варіативність середовищ висока.

Покриття Експериментально - 0%Якість Альфа - 61%Повнота Альфа - 68%Немає

Налаштування, життєвий цикл і діагностика провайдерів 12 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Локальні моделі](</uk/gateway/local-models>), [Lmstudio](</uk/providers/lmstudio>), [Ollama](</uk/providers/ollama>), [Vllm](</uk/providers/vllm>), [Локальні сервіси моделей](</uk/gateway/local-model-services>), [Агенти конфігурації](</uk/gateway/config-agents>), [Усунення несправностей](</uk/gateway/troubleshooting>), [Діагностика](</uk/gateway/doctor>)

Нативні Plugin-и провайдерів 10 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Ollama](</uk/providers/ollama>), [Lmstudio](</uk/providers/lmstudio>)

Сумісність середовища виконання з OpenAI 8 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Vllm](</uk/providers/vllm>), [Sglang](</uk/providers/sglang>), [Локальні моделі](</uk/gateway/local-models>), [Lmstudio](</uk/providers/lmstudio>)

Локальна пам’ять і ембеддинги 5 можливостей

Експериментальний0%

Альфа61%

Альфа68%

[Пам’ять](</uk/concepts/memory>), [Діагностика](</uk/gateway/doctor>)

Мережева безпека та засоби керування підказками 2 можливості

Експериментальний0%

Альфа61%

Альфа68%

[Індекс](</uk/gateway/security>), [Інструменти конфігурації](</uk/gateway/config-tools>), [Локальні моделі](</uk/gateway/local-models>)

Довгохвості хостингові провайдери - M2 Альфа - 3 області

Існує багато сторінок документації/довідника; оцінку слід генерувати з метаданих провайдера та покриття оперативних smoke-перевірок.

Покриття Експериментальне - 0%Якість Альфа - 61%Повнота Альфа - 68%Немає

Хостингові постачальники LLM 12 можливостей

Експериментальне0%

Альфа61%

Альфа68%

[Індекс](</uk/providers>), [Постачальники моделей](</uk/concepts/model-providers>), [Живе тестування](</uk/help/testing-live>), [Онбординг](</uk/cli/onboard>)

Хостингові постачальники медіа 8 можливостей

Експериментальне0%

Альфа61%

Альфа68%

[Маніфест](</uk/plugins/manifest>), [Живе тестування](</uk/help/testing-live>), [Індекс](</uk/providers>)

Операції постачальників 12 можливостей

Експериментальне0%

Альфа61%

Альфа68%

[Індекс](</uk/providers>), [Постачальники моделей](</uk/concepts/model-providers>), [Маніфест](</uk/plugins/manifest>), [Живе тестування](</uk/help/testing-live>), [Моделі](</uk/cli/models>)

Was this useful?YesNo

Open issue