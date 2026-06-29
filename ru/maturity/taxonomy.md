---
title: Таксономия зрелости
source_url: https://docs.openclaw.ai/ru/maturity/taxonomy
scraped_at: 2026-06-29
---

ReferenceRelease and CI

# Таксономия зрелости

модель, лежащая в основе оценочной таблицы

Поверхности > категории > возможности > доказательства.

50 поверхностей, сгруппированных в 4 семейства, где каждая категория связана с каноническими документами и идентификаторами покрытия QA.

Просмотреть области продукта / Открыть подробную таксономию / [Посмотреть оценки](</ru/maturity/scorecard>)

## Как читать эту страницу

Поверхность — это область продукта, такая как среда выполнения Gateway, Discord или приложение для macOS. Каждая поверхность содержит категории, а каждая категория содержит проверки на уровне возможностей, которые покрывают QA-сценарии. Используйте оценочную таблицу для оценки на уровне релиза; используйте эту страницу, чтобы изучить модель, лежащую под ней.

## Уровни зрелости

M0ЗапланированоНаправление известно, но поддерживаемого пользовательского пути еще нет.Повышение: существуют задача на проектирование, владелец и целевая поверхность.

M1ЭкспериментальноРеализовано с оговорками, флагами, сборками из исходного кода или потоками только для сопровождающих.Повышение: сопровождающий может запустить сценарий из текущей main.

M2АльфаРеальные пользователи могут это попробовать, но ожидаются ломающие изменения и неполный UX.Повышение: документированная настройка, базовые тесты, известные оговорки и как минимум одно доказательство в реальной среде.

M3БетаПубличный путь существует, и основной рабочий процесс можно использовать с ограниченными оговорками.Повышение: документация по установке/обновлению, регрессионные тесты, инструкция для поддержки и успешное доказательство сценария в ожидаемой среде.

M4СтабильныйРекомендуемый путь для обычных пользователей. Сбои рассматриваются как регрессии.Повышение: релизный контроль, путь doctor/устранения неполадок, широкая документация и повторяемые доказательства из реального использования.

M5ClawesomeОтполировано, приятно в использовании, хорошо инструментировано и конкурентоспособно с лучшим сопоставимым рабочим процессом.Повышение: Stable плюс успешная пользовательская оценочная таблица на репрезентативных пользователях.

## Области продукта

### Ядро

CLI M4Стабильный7 областей - завершено на 90% Среда выполнения Gateway M4Стабильный13 областей - завершено на 89% Среда выполнения агента M3Бета9 областей - завершено на 79% Сессия, память и движок контекста M3Бета9 областей - завершено на 79% Фреймворк каналов M3Бета8 областей - завершено на 79% Наблюдаемость M3Бета5 областей - завершено на 79% Веб-приложение Gateway M3Бета6 областей - завершено на 79% Plugins M3Бета9 областей - выполнено 79% Безопасность, аутентификация, сопряжение и секреты M3Бета6 областей - выполнено 79% Автоматизация: Cron, хуки, задачи, опрос M3Бета6 областей - выполнено 79% Понимание медиа и генерация медиа M2Альфа6 областей - выполнено 68% Голос и общение в реальном времени M2Альфа6 областей - выполнено 68% TUI M2Альфа5 областей - выполнено 66% ClawHub M2Альфа4 области - выполнено 62% OpenClaw App SDK M2Альфа6 областей - выполнено 53%

### Платформа

Хост Linux Gateway M4Стабильная версия5 областей - выполнено 89% Хост macOS Gateway M4Стабильная версия7 областей - выполнено 88% Хостинг Docker и Podman M3Бета4 области - выполнено 79% Windows через WSL2 M3Бета6 областей - выполнено 79% Raspberry Pi и небольшие устройства Linux M3Бета4 области - выполнено 79% Сопутствующее приложение macOS M3Бета8 областей - выполнено 78% Приложение Android M2Альфа7 областей - выполнено 66% Нативный Windows M2Альфа4 области - выполнено 66% Хостинг Kubernetes M2Альфа4 области - выполнено 61% Приложение iOS M1Экспериментальный8 областей - выполнено 44% Путь установки Nix M1Экспериментальный5 областей - выполнено 44% Сопутствующие поверхности watchOS M1Экспериментальный5 областей - выполнено 44% Сопутствующее приложение Linux M0Запланировано5 областей - выполнено 21% Нативное сопутствующее приложение Windows M0Запланировано5 областей - выполнено 21%

### Канал

Discord M4Стабильный6 областей - выполнено 87% Telegram M3Бета5 областей - выполнено 78% Slack M3Бета5 областей - выполнено 78% iMessage и BlueBubbles M3Бета5 областей - выполнено 78% WhatsApp M3Бета5 областей - выполнено 78% Matrix M2Альфа6 областей - выполнено 67% Google Chat M2Альфа5 областей - выполнено 66% Microsoft Teams M2Альфа5 областей - выполнено 66% Signal M2Альфа5 областей - выполнено 66% Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, региональные каналы M2Альфа4 области - выполнено 58% Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat M2Альфа4 области - выполнено 54% Канал голосовых вызовов M1Экспериментальный5 областей - выполнено 44%

### Провайдер и инструмент

Автоматизация браузера, exec и инструменты песочницы M3Бета3 области - выполнено 79% Путь провайдера OpenAI и Codex M3Бета5 областей - выполнено 79% Инструменты веб-поиска M3Бета4 области - выполнено 79% Путь провайдера Anthropic M3Бета5 областей - выполнено 78% Путь провайдера Google M3Бета5 областей - выполнено 78% Путь провайдера OpenRouter M3Бета4 области - выполнено 78% Инструменты генерации изображений, видео и музыки M2Альфа5 областей - выполнено 68% Локальные провайдеры моделей: Ollama, vLLM, SGLang, LM Studio M2Альфа5 областей - выполнено 68% Нишевые хостинговые провайдеры M2Альфа3 области - выполнено 68%

## Подробности

### Ядро

CLI - M4 Стабильный - 7 областей

Обычные пути настройки и восстановления документированы в руководствах по установке, CLI и Gateway. Платформенно-специфичные пути Windows отслеживаются в строках Windows через WSL2 и нативного Windows.

Покрытие экспериментальное - 4%Качество стабильное - 83%Полнота стабильная - 90%Частично - 6

Настройка CLI 6 возможностей / поддерживается LTS

Экспериментально17%

Стабильно89%

Стабильно90%

[Индекс](</ru/install>), [Установщик](</ru/install/installer>), [Node](</ru/install/node>), [Обновление](</ru/install/updating>)

Онбординг и настройка аутентификации 5 возможностей / поддерживается LTS

Экспериментально0%

Бета75%

Стабильно89%

[Onboard](</ru/cli/onboard>), [Настройка](</ru/cli/configure>), [Обзор онбординга](</ru/start/onboarding-overview>)

Настройка Plugin и канала 5 возможностей

Экспериментально0%

Бета75%

Стабильно89%

[Onboard](</ru/cli/onboard>), [Plugins](</ru/cli/plugins>), [Каналы](</ru/cli/channels>)

Управление службой Gateway 5 возможностей / поддерживается LTS

Экспериментально14%

Стабильно87%

Стабильно90%

[Gateway](</ru/cli/gateway>), [Обновление](</ru/install/updating>), [Устранение неполадок](</ru/gateway/troubleshooting>)

Наблюдаемость CLI 5 возможностей / поддерживается LTS

Экспериментально0%

Стабильно89%

Стабильно90%

[Статус](</ru/cli/status>), [Работоспособность](</ru/cli/health>), [Журналы](</ru/cli/logs>), [Диагностика](</ru/gateway/diagnostics>)

Doctor 10 возможностей / поддерживается LTS

Экспериментально0%

Стабильно89%

Стабильно90%

[Doctor](</ru/cli/doctor>), [Doctor](</ru/gateway/doctor>), [Секреты](</ru/gateway/secrets>), [Устранение неполадок](</ru/gateway/troubleshooting>)

Обновления и апгрейды 5 возможностей / поддерживается LTS

Экспериментально0%

Бета75%

Стабильно89%

[Обновление](</ru/install/updating>), [Обновить](</ru/cli/update>), [Устранение неполадок](</ru/gateway/troubleshooting>)

Среда выполнения Gateway - M4 Stable - 13 областей

Основная архитектура, аутентификация, сопряжение, документация по протоколу, документация по демону и CLI-инструкции по эксплуатации широкие и актуальные.

Покрытие Экспериментально - 6%Качество Стабильно - 81%Полнота Стабильно - 89%Частично - 12

Подтверждения и удаленное выполнение 6 возможностей / с поддержкой LTS

Экспериментально0%

Бета75%

Стабильно89%

[Протокол](</ru/gateway/protocol>), [Индекс](</ru/gateway/security>)

HTTP API 4 возможности / с поддержкой LTS

Экспериментально25%

Стабильно90%

Стабильно90%

[Индекс](</ru/gateway>), [Openai HTTP API](</ru/gateway/openai-http-api>), [Openresponses HTTP API](</ru/gateway/openresponses-http-api>), [HTTP API вызова инструментов](</ru/gateway/tools-invoke-http-api>), [Хуки](</ru/automation/hooks>), [Индекс](</ru/web>)

Размещенная веб-поверхность 4 возможности / с поддержкой LTS

Экспериментально0%

Стабильно89%

Стабильно90%

[Индекс](</ru/gateway>), [Архитектура](</ru/concepts/architecture>), [UI управления](</ru/web/control-ui>), [Веб-чат](</ru/web/webchat>), [Холст](</ru/refactor/canvas>)

RPC API и события Gateway 20 возможностей / с поддержкой LTS

Экспериментально9%

Стабильно90%

Стабильно90%

[Протокол](</ru/gateway/protocol>), [Индекс](</ru/gateway>), [Архитектура](</ru/concepts/architecture>)

Аутентификация и сопряжение устройств 10 возможностей / с поддержкой LTS

Экспериментально0%

Бета75%

Стабильно89%

[Протокол](</ru/gateway/protocol>), [Сопряжение](</ru/gateway/pairing>), [Индекс](</ru/gateway/security>)

Сетевой доступ и обнаружение 6 возможностей / с поддержкой LTS

Экспериментально0%

Бета75%

Стабильно89%

[Индекс](</ru/gateway>), [Обнаружение](</ru/gateway/discovery>), [Протокол](</ru/gateway/protocol>)

Узлы и удаленные возможности 8 возможностей

Экспериментально0%

Бета75%

Стабильно89%

[Протокол](</ru/gateway/protocol>), [Архитектура](</ru/concepts/architecture>), [Индекс](</ru/nodes>)

Работоспособность, диагностика и восстановление 7 возможностей / с поддержкой LTS

Экспериментально0%

Бета75%

Стабильно89%

[Указатель](</ru/gateway>), [Диагностика](</ru/gateway/diagnostics>), [Doctor](</ru/gateway/doctor>)

Совместимость протокола 7 возможностей / с поддержкой LTS

Экспериментальная0%

Бета75%

Стабильная89%

[Протокол](</ru/gateway/protocol>), [Архитектура](</ru/concepts/architecture>), [Typebox](</ru/concepts/typebox>), [Мостовой протокол](</ru/gateway/bridge-protocol>)

Роли и разрешения 5 возможностей / с поддержкой LTS

Экспериментальная0%

Бета75%

Стабильная89%

[Протокол](</ru/gateway/protocol>), [Указатель](</ru/gateway/security>)

Жизненный цикл Gateway 7 возможностей / с поддержкой LTS

Экспериментальная33%

Стабильная90%

Стабильная90%

[Указатель](</ru/gateway>), [Архитектура](</ru/concepts/architecture>)

Средства контроля безопасности 6 возможностей / с поддержкой LTS

Экспериментальная0%

Бета75%

Стабильная89%

[Указатель](</ru/gateway/security>), [Протокол](</ru/gateway/protocol>), [Обнаружение](</ru/gateway/discovery>)

Подключение WebSocket 8 возможностей / с поддержкой LTS

Экспериментальная13%

Стабильная90%

Стабильная90%

[Протокол](</ru/gateway/protocol>), [Архитектура](</ru/concepts/architecture>)

Agent Runtime - M3 Beta - 9 areas

Основной цикл, модели, маршрутизация провайдеров и потоковая передача инструментов являются первоклассными возможностями, но поведение провайдеров меняется еженедельно и требует сценарного подтверждения для каждого выпуска.

Покрытие экспериментальное - 33%Качество бета - 78%Полнота бета - 79%Частично - 6

Выполнение хода агента 3 возможности / с поддержкой LTS

Экспериментальная29%

Бета79%

Бета79%

[Цикл агента](</ru/concepts/agent-loop>), [Агент](</ru/cli/agent>), [Среды выполнения агентов](</ru/concepts/agent-runtimes>)

Внешние среды выполнения и субагенты 4 возможности

Экспериментальная30%

Бета79%

Бета79%

[Среды выполнения агентов](</ru/concepts/agent-runtimes>), [Anthropic](</ru/providers/anthropic>), [Google](</ru/providers/google>), [Субагенты](</ru/tools/subagents>)

Выполнение через размещенных провайдеров 5 возможностей / с поддержкой LTS

Экспериментальная20%

Бета79%

Бета79%

[Openai](</ru/providers/openai>), [Anthropic](</ru/providers/anthropic>), [Google](</ru/providers/google>), [Модели](</ru/concepts/models>)

Локальные и самостоятельно размещенные провайдеры 5 возможностей

Экспериментальная0%

Альфа68%

Бета79%

[Ollama](</ru/providers/ollama>), [Модели](</ru/concepts/models>), [Агент](</ru/cli/agent>)

Выбор модели и среды выполнения 4 возможности / с поддержкой LTS

Экспериментальная25%

Бета79%

Бета79%

[Модели](</ru/concepts/models>), [Модели](</ru/cli/models>), [Openai](</ru/providers/openai>), [Среды выполнения агентов](</ru/concepts/agent-runtimes>)

Аутентификация провайдера 10 возможностей / с поддержкой LTS

Экспериментальная24%

Бета79%

Бета79%

[Модели](</ru/concepts/models>), [Агент](</ru/cli/agent>), [Модели](</ru/cli/models>), [Openai](</ru/providers/openai>), [Anthropic](</ru/providers/anthropic>), [Google](</ru/providers/google>), [Субагенты](</ru/tools/subagents>)

Потоковая передача и ход выполнения 2 возможности

Альфа56%

Бета79%

Бета79%

[Потоковая передача](</ru/concepts/streaming>), [Цикл агента](</ru/concepts/agent-loop>)

Вызовы инструментов и обработка ответов 3 возможности / с поддержкой LTS

Альфа65%

Бета79%

Бета79%

[Цикл агента](</ru/concepts/agent-loop>), [Ollama](</ru/providers/ollama>)

Средства управления выполнением инструментов 6 возможностей / поддерживается LTS

Альфа50%

Бета79%

Бета79%

[Песочница, политика инструментов и повышенные привилегии](</ru/gateway/sandbox-vs-tool-policy-vs-elevated>), [Цикл агента](</ru/concepts/agent-loop>), [Субагенты](</ru/tools/subagents>)

Сеанс, память и движок контекста - M3 Beta - 9 областей

Сильная документация и активная реализация. Зрелость зависит от долговечности транскриптов, качества Compaction и паритета между клиентами.

Покрытие экспериментальное - 30%Качество Beta - 77%Полнота Beta - 79%Частично - 6

Управление сеансами CLI и транскриптами 2 возможности / с поддержкой LTS

Экспериментальная0%

Альфа68%

Бета79%

[Сеанс](</ru/concepts/session>), [Управление сеансами Compaction](</ru/reference/session-management-compaction>), [Сеансы](</ru/cli/sessions>)

Управление токенами 3 возможности / с поддержкой LTS

Экспериментальная20%

Бета79%

Бета79%

[Compaction](</ru/concepts/compaction>), [Контекст](</ru/concepts/context>), [Управление сеансами Compaction](</ru/reference/session-management-compaction>)

Механизм контекста 2 возможности / с поддержкой LTS

Альфа57%

Бета79%

Бета79%

[Контекст](</ru/concepts/context>), [Механизм контекста](</ru/concepts/context-engine>), [Оснастка механизма контекста Codex](</ru/plan/codex-context-engine-harness>)

Кросс-клиентская история и паритет сеансов 2 возможности

Экспериментальная40%

Бета79%

Бета79%

[Веб-чат](</ru/web/webchat>), [Android](</ru/platforms/android>), [Маршрутизация каналов](</ru/channels/channel-routing>)

Диагностика, обслуживание и восстановление 3 возможности

Экспериментальная40%

Бета79%

Бета79%

[Диагностика](</ru/gateway/diagnostics>), [Управление сеансами Compaction](</ru/reference/session-management-compaction>), [Флаги](</ru/diagnostics/flags>)

Основные подсказки и контекст 2 возможности / с поддержкой LTS

Экспериментальная38%

Бета79%

Бета79%

[Контекст](</ru/concepts/context>), [Гигиена транскрипта](</ru/reference/transcript-hygiene>), [Discord](</ru/channels/discord>)

Память 5 возможностей

Экспериментальная46%

Бета79%

Бета79%

[Конфигурация памяти](</ru/reference/memory-config>), [Memory Qmd](</ru/concepts/memory-qmd>), [Память](</ru/concepts/memory>), [Discord](</ru/channels/discord>)

Маршрутизация сеансов 2 возможности / с поддержкой LTS

Экспериментальная25%

Бета79%

Бета79%

[Сеанс](</ru/concepts/session>), [Маршрутизация каналов](</ru/channels/channel-routing>), [Discord](</ru/channels/discord>)

Сохранение транскриптов 2 возможности / поддерживается LTS

Экспериментальный0%

Альфа68%

Бета79%

[Управление сессиями Compaction](</ru/reference/session-management-compaction>), [Гигиена транскриптов](</ru/reference/transcript-hygiene>)

Фреймворк каналов - M3 бета - 8 областей

Многие каналы используют общие контракты доставки и маршрутизации Gateway, но поведение каналов зависит от ограничений вышестоящего API и политики учетной записи.

Покрытие экспериментальное - 13%Качество бета - 76%Полнота бета - 79%Частично - 5

Действия, команды и подтверждения канала 5 возможностей

Экспериментальный0%

Бета79%

Бета79%

[Группы](</ru/channels/groups>), [Discord](</ru/channels/discord>), [Google Chat](</ru/channels/googlechat>), [Signal](</ru/channels/signal>), [Matrix](</ru/channels/matrix>)

Настройка каналов 5 возможностей / с поддержкой LTS

Экспериментальный14%

Бета79%

Бета79%

[Указатель](</ru/channels>), [Сопряжение](</ru/channels/pairing>), [Устранение неполадок](</ru/channels/troubleshooting>), [SDK Plugin каналов](</ru/plugins/sdk-channel-plugins>)

Поведение групповых потоков и фоновых комнат 5 возможностей

Экспериментальный36%

Бета79%

Бета79%

[Группы](</ru/channels/groups>), [Групповые сообщения](</ru/channels/group-messages>), [События фоновых комнат](</ru/channels/ambient-room-events>), [Группы рассылки](</ru/channels/broadcast-groups>), [Discord](</ru/channels/discord>)

Входящий доступ и проверки идентичности 5 возможностей / с поддержкой LTS

Экспериментальный0%

Альфа68%

Бета79%

[Группы доступа](</ru/channels/access-groups>), [Группы](</ru/channels/groups>), [Discord](</ru/channels/discord>), [LINE](</ru/channels/line>)

Медиавложения и расширенные данные каналов 4 возможности

Экспериментальный0%

Альфа68%

Бета79%

[LINE](</ru/channels/line>), [Signal](</ru/channels/signal>), [Google Chat](</ru/channels/googlechat>), [Matrix](</ru/channels/matrix>), [Discord](</ru/channels/discord>)

Исходящая доставка и конвейер ответов 4 возможности / с поддержкой LTS

Экспериментальный38%

Бета79%

Бета79%

[Группы](</ru/channels/groups>), [События фоновых комнат](</ru/channels/ambient-room-events>), [Discord](</ru/channels/discord>), [Matrix](</ru/channels/matrix>), [Каналы конфигурации](</ru/gateway/config-channels>)

Маршрутизация и доставка разговоров 10 возможностей / с поддержкой LTS

Экспериментальный19%

Бета79%

Бета79%

[Маршрутизация каналов](</ru/channels/channel-routing>), [Группы](</ru/channels/groups>), [Discord](</ru/channels/discord>), [Matrix](</ru/channels/matrix>), [Устранение неполадок](</ru/channels/troubleshooting>), [Справочник по конфигурации](</ru/gateway/configuration-reference>)

Состояние работоспособности и элементы управления оператора 4 возможности / с поддержкой LTS

Экспериментальный0%

Бета79%

Бета79%

[Состояние](</ru/gateway/health>), [Справочник по конфигурации](</ru/gateway/configuration-reference>), [Устранение неполадок](</ru/channels/troubleshooting>), [Discord](</ru/channels/discord>)

Наблюдаемость - M3 Beta - 5 областей

Существуют документы по OTel, Prometheus, ведению журналов и диагностике. Требуется публичная доработка уровня зрелости в формате «на что операторам смотреть в первую очередь».

Покрытие Experimental - 18%Качество Beta - 75%Полнота Beta - 79%Частично - 3

Состояние и восстановление 12 возможностей / с поддержкой LTS

Experimental28%

Beta79%

Beta79%

[Состояние](</ru/gateway/health>), [Telegram](</ru/channels/telegram>), [Doctor](</ru/cli/doctor>), [Doctor](</ru/gateway/doctor>), [Подпути SDK](</ru/plugins/sdk-subpaths>), [Состояние](</ru/cli/health>), [Протокол](</ru/gateway/protocol>)

Журналирование 5 возможностей / с поддержкой LTS

Experimental0%

Alpha68%

Beta79%

[Журналирование](</ru/logging>), [Журналирование](</ru/gateway/logging>), [Журналы](</ru/cli/logs>)

Сбор диагностики 8 возможностей

Experimental30%

Beta79%

Beta79%

[Диагностика](</ru/gateway/diagnostics>), [Состояние](</ru/gateway/health>), [Codex Harness](</ru/plugins/codex-harness>), [Протокол](</ru/gateway/protocol>)

Экспорт телеметрии 13 возможностей

Experimental33%

Beta79%

Beta79%

[Хуки](</ru/plugins/hooks>), [Opentelemetry](</ru/gateway/opentelemetry>), [Журналирование](</ru/logging>), [Подпути SDK](</ru/plugins/sdk-subpaths>), [Диагностика Otel](</ru/plugins/reference/diagnostics-otel>), [Prometheus](</ru/gateway/prometheus>), [Диагностика Prometheus](</ru/plugins/reference/diagnostics-prometheus>)

Диагностика сеансов 4 возможности / с поддержкой LTS

Experimental0%

Alpha68%

Beta79%

[Opentelemetry](</ru/gateway/opentelemetry>), [Prometheus](</ru/gateway/prometheus>), [Диагностика](</ru/gateway/diagnostics>), [Протокол](</ru/gateway/protocol>)

Веб-приложение Gateway - M3 Beta - 6 областей

Веб-интерфейс документирован с потоками сопряжения, чата, PWA, Talk, push-уведомлений и удаленного Gateway. Повышайте статус после оценочных листов по кроссбраузерности и мобильному PWA.

Покрытие Experimental - 4%Качество Beta - 74%Полнота Beta - 79%Нет

Разговор в браузере в реальном времени 5 возможностей

Экспериментально0%

Альфа68%

Бета79%

[Интерфейс управления](</ru/web/control-ui>), [Протокол](</ru/gateway/protocol>), [Разговор](</ru/nodes/talk>)

Доступ из браузера и доверие 5 возможностей

Экспериментально0%

Альфа68%

Бета79%

[Интерфейс управления](</ru/web/control-ui>), [Панель мониторинга](</ru/web/dashboard>), [Tailscale](</ru/gateway/tailscale>), [Удаленный доступ](</ru/gateway/remote>)

Конфигурация 5 возможностей

Экспериментально0%

Альфа68%

Бета79%

[Интерфейс управления](</ru/web/control-ui>), [Конфигурация](</ru/gateway/configuration>)

Интерфейс браузера 10 возможностей

Экспериментально8%

Бета79%

Бета79%

[Интерфейс управления](</ru/web/control-ui>), [Индекс](</ru/web>), [Панель мониторинга](</ru/web/dashboard>), [Протокол](</ru/gateway/protocol>)

Беседы в веб-чате 15 возможностей

Экспериментально10%

Бета79%

Бета79%

[Интерфейс управления](</ru/web/control-ui>), [Веб-чат](</ru/web/webchat>), [Начало работы](</ru/start/getting-started>), [Маршрутизация каналов](</ru/channels/channel-routing>), [Безопасные файловые операции](</ru/gateway/security/secure-file-operations>)

Консоль оператора 10 возможностей

Экспериментально8%

Бета79%

Бета79%

[Интерфейс управления](</ru/web/control-ui>), [Работоспособность](</ru/gateway/health>), [Протокол](</ru/gateway/protocol>), [Панель мониторинга](</ru/web/dashboard>)

Плагины - M3 Бета - 9 областей

Широкая документация и убедительные внутренние доказательства работы среды выполнения существуют для манифестов, обнаружения, загрузки, архитектуры провайдеров и инструментов, а также границ утверждения. Оставьте строку на уровне бета, пока публичный API SDK, подпути и доказательства внешней дистрибуции не станут сильнее.

Покрытие: экспериментально - 12%Качество: бета - 72%Завершенность: бета - 79%Частично - 7

Создание и упаковка Plugin 8 возможностей / поддерживается LTS

Экспериментальный0%

Альфа68%

Бета79%

[Создание Plugin](</ru/plugins/building-plugins>), [Обзор SDK](</ru/plugins/sdk-overview>), [Точки входа SDK](</ru/plugins/sdk-entrypoints>), [Подпути SDK](</ru/plugins/sdk-subpaths>), [Манифест](</ru/plugins/manifest>), [Справочник](</ru/plugins/reference>)

Встроенные Plugin 5 возможностей / поддерживается LTS

Экспериментальный0%

Альфа68%

Бета79%

[Инвентарь Plugin](</ru/plugins/plugin-inventory>), [Plugin](</ru/cli/plugins>), [Внутренняя архитектура](</ru/plugins/architecture-internals>)

Canvas Plugin 6 возможностей

Экспериментальный0%

Альфа68%

Бета79%

[Canvas](</ru/plugins/reference/canvas>), [Canvas](</ru/refactor/canvas>), [Справочник по конфигурации](</ru/gateway/configuration-reference>)

Установка и запуск Plugin 6 возможностей / поддерживается LTS

Экспериментальный35%

Бета79%

Бета79%

[Архитектура](</ru/plugins/architecture>), [Внутренняя архитектура](</ru/plugins/architecture-internals>), [Plugin](</ru/cli/plugins>)

Канальные Plugin 5 возможностей / поддерживается LTS

Экспериментальный0%

Альфа68%

Бета79%

[Канальные Plugin SDK](</ru/plugins/sdk-channel-plugins>), [Входящие каналы SDK](</ru/plugins/sdk-channel-inbound>), [Исходящие каналы SDK](</ru/plugins/sdk-channel-outbound>)

Provider и инструментальные Plugin 6 возможностей / поддерживается LTS

Экспериментальный43%

Бета79%

Бета79%

[Provider Plugin SDK](</ru/plugins/sdk-provider-plugins>), [Инструментальные Plugin](</ru/plugins/tool-plugins>), [Добавление возможностей](</ru/plugins/adding-capabilities>)

Одобрения Plugin 6 возможностей / поддерживается LTS

Экспериментальный0%

Альфа68%

Бета79%

[Запросы разрешений Plugin](</ru/plugins/plugin-permission-requests>), [Одобрения exec](</ru/tools/exec-approvals>), [Канальные Plugin SDK](</ru/plugins/sdk-channel-plugins>)

Публикация Plugin 6 возможностей / поддерживается LTS

Экспериментальный0%

Альфа68%

Beta79%

[Plugins](</ru/cli/plugins>), [Совместимость](</ru/plugins/compatibility>), [Публикация](</ru/clawhub/publishing>)

Тестирование plugins 6 возможностей

Экспериментально27%

Beta79%

Beta79%

[Тестирование Sdk](</ru/plugins/sdk-testing>), [Настройка Sdk](</ru/plugins/sdk-setup>), [Codex Harness](</ru/plugins/codex-harness>)

Безопасность, аутентификация, сопряжение и секреты - M3 Beta - 6 областей

Хорошая документация и поверхности усиления защиты уже есть. Продвигайте после того, как регулярные сценарии обновления и безопасности докажут отсутствие регрессий настройки.

Покрытие Experimental - 16%Качество Beta - 72%Полнота Beta - 79%Частично - 5

Политика утверждений и защитные меры инструментов 2 возможности / с поддержкой LTS

Alpha50%

Beta79%

Beta79%

[Утверждения Exec](</ru/tools/exec-approvals>), [Утверждения](</ru/cli/approvals>), [Запросы разрешений Plugin](</ru/plugins/plugin-permission-requests>), [Проверки аудита](</ru/gateway/security/audit-checks>)

Аутентификация Gateway и удаленный доступ 9 возможностей / с поддержкой LTS

Experimental0%

Alpha68%

Beta79%

[Индекс](</ru/gateway/security>), [Инструкция по экспозиции](</ru/gateway/security/exposure-runbook>), [Аутентификация доверенного прокси](</ru/gateway/trusted-proxy-auth>), [Tailscale](</ru/gateway/tailscale>), [Удаленный доступ](</ru/gateway/remote>), [Справочник конфигурации](</ru/gateway/configuration-reference>), [Gateway](</ru/cli/gateway>), [Doctor](</ru/cli/doctor>), [Control Ui](</ru/web/control-ui>), [Управление браузером](</ru/tools/browser-control>), [Проверки аудита](</ru/gateway/security/audit-checks>)

Контроль доступа к каналам 3 возможности / с поддержкой LTS

Experimental0%

Alpha68%

Beta79%

[Сопряжение](</ru/channels/pairing>), [Telegram](</ru/channels/telegram>), [Группы доступа](</ru/channels/access-groups>), [Проверки аудита](</ru/gateway/security/audit-checks>)

Сопряжение устройств и Node 11 возможностей / с поддержкой LTS

Experimental0%

Alpha68%

Beta79%

[Протокол](</ru/gateway/protocol>), [Устройства](</ru/cli/devices>), [Сопряжение](</ru/channels/pairing>), [Сопряжение](</ru/gateway/pairing>), [Области оператора](</ru/gateway/operator-scopes>), [Control Ui](</ru/web/control-ui>), [Webchat](</ru/web/webchat>), [Утверждения](</ru/cli/approvals>)

Доверие к Plugin 2 возможности

Experimental0%

Alpha68%

Beta79%

[Манифест](</ru/plugins/manifest>), [Запросы разрешений Plugin](</ru/plugins/plugin-permission-requests>), [Управление Plugin](</ru/plugins/manage-plugins>), [Проверки аудита](</ru/gateway/security/audit-checks>)

Гигиена учетных данных и секретов 5 возможностей / с поддержкой LTS

Experimental46%

Beta79%

Beta79%

[Аутентификация](</ru/gateway/authentication>), [Модели](</ru/cli/models>), [Openai](</ru/providers/openai>), [Oauth](</ru/concepts/oauth>), [Секреты](</ru/gateway/secrets>), [Секреты](</ru/cli/secrets>), [Поверхность учетных данных Secretref](</ru/reference/secretref-credential-surface>), [Проверки аудита](</ru/gateway/security/audit-checks>)

Автоматизация: Cron, хуки, задачи, опрос - M3 Beta - 6 областей

Задокументировано и пригодно к использованию, но сценарные проверки должны охватывать автоматическую доставку, повторные попытки и видимость сбоев.

Покрытие Experimental - 2%Качество Beta - 72%Полнота Beta - 79%Нет

Задания Cron 15 возможностей

Экспериментально0%

Бета79%

Бета79%

[Задания Cron](</ru/automation/cron-jobs>), [Cron](</ru/cli/cron>), [Протокол](</ru/gateway/protocol>), [Задачи](</ru/automation/tasks>), [Discord](</ru/channels/discord>)

Входящие события 15 возможностей

Экспериментально0%

Альфа68%

Бета79%

[Telegram](</ru/channels/telegram>), [Zalo](</ru/channels/zalo>), [Устранение неполадок](</ru/channels/troubleshooting>), [iMessage из BlueBubbles](</ru/channels/imessage-from-bluebubbles>), [Интеграция Gmail Pubsub](</ru/automation/cron-jobs#gmail-pubsub-integration>), [Gmail Pubsub](</ru/automation/cron-jobs>), [Webhook](</ru/cli/webhooks>), [Webhook](</ru/automation/cron-jobs#webhooks>), [Webhook](</ru/automation/cron-jobs>)

Хуки автоматизации 11 возможностей

Экспериментально0%

Альфа68%

Бета79%

[Хуки](</ru/automation/hooks>), [Хуки](</ru/cli/hooks>), [Хуки](</ru/plugins/hooks>), [Запросы разрешений Plugin](</ru/plugins/plugin-permission-requests>), [Подпути SDK](</ru/plugins/sdk-subpaths>)

Фоновые задачи и потоки 10 возможностей

Экспериментально0%

Альфа68%

Бета79%

[Задачи](</ru/automation/tasks>), [Индекс](</ru/automation>), [Задачи](</ru/cli/tasks>), [TaskFlow](</ru/automation/taskflow>), [Среда выполнения SDK](</ru/plugins/sdk-runtime>)

Heartbeat 5 возможностей

Экспериментально14%

Бета79%

Бета79%

[Индекс](</ru/automation>), [Heartbeat](</ru/gateway/heartbeat>), [Обязательства](</ru/concepts/commitments>)

Управление опросом 10 возможностей

Экспериментально0%

Альфа68%

Бета79%

[Опрос](</ru/cli/message>), [Сообщение](</ru/cli/message>), [Telegram](</ru/channels/telegram>), [Microsoft Teams](</ru/channels/msteams>), [Фоновый процесс](</ru/gateway/background-process>)

Понимание медиа и генерация медиа — M2 Альфа — 6 областей

Широкая поверхность возможностей существует, но различия между провайдерами, ограничения файлов и паритет Node/приложений пока не делают ее стабильной.

Покрытие: экспериментально — 2%Качество: альфа — 64%Полнота: альфа — 68%Нет

Прием и доступ к медиа 8 возможностей

Экспериментально0%

Alpha61%

Alpha68%

[Обзор медиа](</ru/tools/media-overview>), [Понимание медиа](</ru/nodes/media-understanding>), [Безопасные файловые операции](</ru/gateway/security/secure-file-operations>), [Pdf](</ru/tools/pdf>), [Генерация изображений](</ru/tools/image-generation>), [Qr](</ru/cli/qr>), [Line](</ru/channels/line>), [Whatsapp](</ru/channels/whatsapp>)

Обработка медиа в каналах 5 возможностей

Экспериментально0%

Alpha61%

Alpha68%

[Изображения](</ru/nodes/images>), [Обзор медиа](</ru/tools/media-overview>), [Discord](</ru/channels/discord>)

Конфигурация медиа 1 возможность

Экспериментально0%

Alpha61%

Alpha68%

[Обзор медиа](</ru/tools/media-overview>), [Генерация изображений](</ru/tools/image-generation>), [Манифест](</ru/plugins/manifest>), [Оснастка Codex](</ru/plugins/codex-harness>)

Доставка преобразования текста в речь 2 возможности

Экспериментально0%

Alpha61%

Alpha68%

[Tts](</ru/tools/tts>), [Обзор медиа](</ru/tools/media-overview>), [Discord](</ru/channels/discord>)

Понимание медиа 12 возможностей

Экспериментально7%

Alpha69%

Alpha69%

[Аудио](</ru/nodes/audio>), [Понимание медиа](</ru/nodes/media-understanding>), [Обзор медиа](</ru/tools/media-overview>), [Whatsapp](</ru/channels/whatsapp>), [Изображения](</ru/nodes/images>), [Infer](</ru/cli/infer>), [Pdf](</ru/tools/pdf>)

Генерация медиа 17 возможностей

Экспериментально5%

Alpha69%

Alpha69%

[Генерация изображений](</ru/tools/image-generation>), [Обзор медиа](</ru/tools/media-overview>), [Skills](</ru/tools/skills>), [Генерация музыки](</ru/tools/music-generation>), [Генерация видео](</ru/tools/video-generation>)

Голос и разговоры в реальном времени - M2 Alpha - 6 областей

Несколько реализаций существуют в Control UI, приложениях и провайдерах. Перед бета-версией нужны оценочные карты задержки, режимов отказа и настройки.

Покрытие: экспериментально - 0%Качество: Alpha - 61%Полнота: Alpha - 68%Нет

Провайдеры голосового общения 7 возможностей

Экспериментальная0%

Альфа61%

Альфа68%

[Openai](</ru/providers/openai>), [Google](</ru/providers/google>), [Plugin провайдера SDK](</ru/plugins/sdk-provider-plugins>), [Голосовое общение](</ru/nodes/talk>), [Интерфейс управления](</ru/web/control-ui>)

Сеансы голосового общения в реальном времени 11 возможностей

Экспериментальная0%

Альфа61%

Альфа68%

[Голосовое общение](</ru/nodes/talk>), [Интерфейс управления](</ru/web/control-ui>)

Речь и транскрибация 5 возможностей

Экспериментальная0%

Альфа61%

Альфа68%

[Голосовое общение](</ru/nodes/talk>), [Openai](</ru/providers/openai>), [Google](</ru/providers/google>)

Голосовое общение в нативном приложении 4 возможности

Экспериментальная0%

Альфа61%

Альфа68%

[Голосовое общение](</ru/nodes/talk>), [Voicewake](</ru/platforms/mac/voicewake>)

Голосовая активация и маршрутизация 4 возможности

Экспериментальная0%

Альфа61%

Альфа68%

[Voicewake](</ru/nodes/voicewake>), [Voicewake](</ru/platforms/mac/voicewake>), [Голосовой оверлей](</ru/platforms/mac/voice-overlay>)

Наблюдаемость голосового общения 5 возможностей

Экспериментальная0%

Альфа61%

Альфа68%

[Интерфейс управления](</ru/web/control-ui>), [Голосовой оверлей](</ru/platforms/mac/voice-overlay>), [Голосовое общение](</ru/nodes/talk>)

TUI - M2 Альфа - 5 областей

Присутствует в документации и исходном коде, но менее заметен как основной пользовательский рабочий процесс. Требует явного определения сценариев.

Покрытие: экспериментальная - 0%Качество: альфа - 59%Полнота: альфа - 66%Нет

Режимы выполнения 14 возможностей

Экспериментально0%

Альфа59%

Альфа66%

[TUI](</ru/cli/tui>), [TUI](</ru/web/tui>), [Индекс](</ru/cli>)

Ввод и команды 8 возможностей

Экспериментально0%

Альфа59%

Альфа66%

[TUI](</ru/web/tui>)

Управление сеансами 3 возможности

Экспериментально0%

Альфа59%

Альфа66%

[TUI](</ru/web/tui>), [Сеансы](</ru/cli/sessions>)

Локальное выполнение shell-команд 4 возможности

Экспериментально0%

Альфа59%

Альфа66%

[TUI](</ru/web/tui>), [TUI](</ru/cli/tui>)

Рендеринг и безопасность вывода 4 возможности

Экспериментально0%

Альфа59%

Альфа66%

[TUI](</ru/web/tui>), [QR](</ru/cli/qr>), [Журналы](</ru/cli/logs>), [Автодополнение](</ru/cli/completion>)

ClawHub - M2 Альфа - 4 области

Публичная документация и концепция экосистемы существуют. Нужны оценочные таблицы установки, доверия, обновления, отката и совместимости.

Покрытие: экспериментально - 0%Качество: альфа - 58%Полнота: альфа - 62%Нет

Публикация 7 возможностей

Экспериментальный0%

Alpha54%

Alpha55%

[Публикация](</ru/clawhub/publishing>), [Создание Skills](</ru/tools/creating-skills>), [Сообщество](</ru/plugins/community>)

Обнаружение каталога 5 возможностей

Экспериментальный0%

Alpha61%

Alpha68%

[Plugin](</ru/tools/plugin>), [Plugins](</ru/cli/plugins>), [Skills](</ru/cli/skills>), [Skills](</ru/tools/skills>), [Сообщество](</ru/plugins/community>)

Совместимость и доверие 12 возможностей

Экспериментальный0%

Alpha55%

Alpha56%

[Plugin](</ru/tools/plugin>), [Plugins](</ru/cli/plugins>), [Совместимость](</ru/plugins/compatibility>), [Инвентаризация Plugin](</ru/plugins/plugin-inventory>), [Публикация](</ru/clawhub/publishing>), [Skills](</ru/tools/skills>), [Конфигурация Skills](</ru/tools/skills-config>)

Жизненный цикл и состояние Plugin 26 возможностей

Экспериментальный0%

Alpha61%

Alpha68%

[Plugin](</ru/tools/plugin>), [Plugins](</ru/cli/plugins>), [Skills](</ru/cli/skills>), [Skills](</ru/tools/skills>), [Протокол](</ru/gateway/protocol>), [Пакеты](</ru/plugins/bundles>), [Разрешение зависимостей](</ru/plugins/dependency-resolution>)

OpenClaw App SDK - M2 Alpha - 6 областей

OpenClaw App SDK — отдельный контракт внешнего приложения, независимый от среды выполнения Gateway и Plugin SDK. Текущая оценка показывает реальный путь `@openclaw/sdk` с пробелами в публичной упаковке, автообнаружении, утверждениях, вспомогательных средствах и совместимости.

Покрытие: экспериментальный - 3%Качество: Alpha - 54%Полнота: Alpha - 53%Нет

API клиента 4 возможности

Экспериментальный0%

Альфа51%

Альфа50%

[Openclaw Sdk](</ru/gateway/external-apps>), [Проектирование API Openclaw Sdk](</ru/gateway/external-apps>)

Доступ к Gateway 5 возможностей

Экспериментальный0%

Альфа53%

Альфа54%

[Openclaw Sdk](</ru/gateway/external-apps>), [Проектирование API Openclaw Sdk](</ru/gateway/external-apps>), [Протокол](</ru/gateway/protocol>), [Индекс](</ru/gateway/security>)

Беседы агентов 6 возможностей

Экспериментальный0%

Альфа52%

Альфа52%

[Openclaw Sdk](</ru/gateway/external-apps>), [Проектирование API Openclaw Sdk](</ru/gateway/external-apps>), [Протокол](</ru/gateway/protocol>)

События и утверждения 5 возможностей

Экспериментальный0%

Альфа52%

Альфа52%

[Openclaw Sdk](</ru/gateway/external-apps>), [Проектирование API Openclaw Sdk](</ru/gateway/external-apps>), [Протокол](</ru/gateway/protocol>)

Помощники ресурсов 5 возможностей

Экспериментальный17%

Альфа62%

Альфа53%

[Openclaw Sdk](</ru/gateway/external-apps>), [Проектирование API Openclaw Sdk](</ru/gateway/external-apps>)

Совместимость 5 возможностей

Экспериментальный0%

Альфа54%

Альфа55%

[Проектирование API Openclaw Sdk](</ru/gateway/external-apps>), [Typebox](</ru/concepts/typebox>), [Протокол](</ru/gateway/protocol>)

### Платформа

Хост Linux Gateway - M4 Stable - 5 областей

Рекомендуется среда выполнения Node, документирован пользовательский сервис systemd, а руководство по VPS/контейнерам охватывает широкий круг сценариев.

Покрытие: экспериментальное - 0%Качество: бета - 75%Полнота: стабильная - 89%Частично - 4

Настройка хоста и обновления 4 возможности / с поддержкой LTS

Экспериментальная0%

Бета75%

Стабильная89%

[Индекс](</ru/install>), [Обновление](</ru/install/updating>), [Linux](</ru/platforms/linux>), [Индекс](</ru/platforms>)

Среда выполнения Gateway и управление службой 6 возможностей / с поддержкой LTS

Экспериментальная0%

Бета75%

Стабильная89%

[Индекс](</ru/gateway>), [Gateway](</ru/cli/gateway>), [Linux](</ru/platforms/linux>), [Vps](</ru/vps>)

Удаленный доступ и безопасность 6 возможностей / с поддержкой LTS

Экспериментальная0%

Бета75%

Стабильная89%

[Удаленный доступ](</ru/gateway/remote>), [Tailscale](</ru/gateway/tailscale>), [Регламент действий при раскрытии доступа](</ru/gateway/security/exposure-runbook>), [Аутентификация](</ru/gateway/authentication>), [Секреты](</ru/gateway/secrets>)

Диагностика и восстановление 4 возможности / с поддержкой LTS

Экспериментальная0%

Бета75%

Стабильная89%

[Статус](</ru/cli/status>), [Журналы](</ru/cli/logs>), [Doctor](</ru/cli/doctor>), [Диагностика](</ru/gateway/diagnostics>), [Индекс](</ru/gateway>)

Цели развертывания 3 возможности

Экспериментальная0%

Бета75%

Стабильная89%

[Vps](</ru/vps>), [Docker](</ru/install/docker>), [Hetzner](</ru/install/hetzner>), [Digitalocean](</ru/install/digitalocean>), [Kubernetes](</ru/install/kubernetes>), [Podman](</ru/install/podman>)

Хост macOS Gateway - M4 Стабильный - 7 областей

Путь службы LaunchAgent, локальный/удаленный режимы Gateway, установка CLI и интеграция приложения задокументированы.

Охват Экспериментальная - 0%Качество Бета - 74%Полнота Стабильная - 88%Нет

Настройка CLI 4 возможности

Экспериментальный0%

Бета74%

Стабильный88%

[Macos](</ru/platforms/macos>), [Встроенный Gateway](</ru/platforms/mac/bundled-gateway>), [Установщик](</ru/install/installer>), [Node](</ru/install/node>)

Интеграция локального Gateway 9 возможностей

Экспериментальный0%

Бета74%

Стабильный88%

[Macos](</ru/platforms/macos>), [Встроенный Gateway](</ru/platforms/mac/bundled-gateway>), [Удаленный режим](</ru/platforms/mac/remote>), [Индекс](</ru/gateway>), [Gateway](</ru/cli/gateway>), [Bonjour](</ru/gateway/bonjour>)

Режим удаленного Gateway 5 возможностей

Экспериментальный0%

Бета74%

Стабильный88%

[Удаленный режим](</ru/platforms/mac/remote>), [Удаленный режим](</ru/gateway/remote>), [Tailscale](</ru/gateway/tailscale>)

Жизненный цикл службы Gateway 10 возможностей

Экспериментальный0%

Бета74%

Стабильный88%

[Macos](</ru/platforms/macos>), [Встроенный Gateway](</ru/platforms/mac/bundled-gateway>), [Gateway](</ru/cli/gateway>), [Индекс](</ru/gateway>), [Обновление](</ru/cli/update>), [Обновление](</ru/install/updating>), [Удаление](</ru/install/uninstall>), [Устранение неполадок](</ru/gateway/troubleshooting>)

Диагностика и наблюдаемость 4 возможности

Экспериментальный0%

Бета74%

Стабильный88%

[Встроенный Gateway](</ru/platforms/mac/bundled-gateway>), [Macos](</ru/platforms/macos>), [Gateway](</ru/cli/gateway>), [Doctor](</ru/gateway/doctor>), [Устранение неполадок](</ru/gateway/troubleshooting>)

Разрешения и нативные возможности 4 возможности

Экспериментальный0%

Бета74%

Стабильный88%

[Macos](</ru/platforms/macos>), [Удаленный режим](</ru/platforms/mac/remote>)

Профили и изоляция 5 возможностей

Экспериментальный0%

Бета74%

Стабильный88%

[Несколько Gateway](</ru/gateway/multiple-gateways>), [Индекс](</ru/gateway>), [Gateway](</ru/cli/gateway>)

Хостинг Docker и Podman — M3 Бета — 4 области

Документация по установке существует, и это распространенные пути развертывания. Продвиньте после того, как регулярный release smoke будет фиксировать поведение обновления и томов.

Покрытие: экспериментальный — 7%Качество: бета — 71%Полнота: бета — 79%Нет

Настройка контейнеров 6 возможностей

Экспериментальный0%

Альфа68%

Бета79%

[Docker](</ru/install/docker>), [Podman](</ru/install/podman>)

Операции с контейнерами 11 возможностей

Экспериментальный0%

Альфа68%

Бета79%

[Podman](</ru/install/podman>), [Среда выполнения Docker VM](</ru/install/docker-vm-runtime>), [Docker](</ru/install/docker>), [Hetzner](</ru/install/hetzner>), [Hostinger](</ru/install/hostinger>)

Выпуск и проверка образов 5 возможностей

Экспериментальный29%

Бета79%

Бета79%

[Docker](</ru/install/docker>), [Среда выполнения Docker VM](</ru/install/docker-vm-runtime>), [Полная проверка выпуска](</ru/reference/full-release-validation>)

Песочница и инструменты агента 3 возможности

Экспериментальный0%

Альфа68%

Бета79%

[Docker](</ru/install/docker>), [Среда выполнения Docker VM](</ru/install/docker-vm-runtime>)

Windows через WSL2 - M3 Beta - 6 областей

Рекомендуемый путь для Windows с руководством по systemd/user-service и документацией по цепочке загрузки. Продвигайте после повторных оценочных карт установки/обновления.

Покрытие Экспериментальный - 6%Качество Альфа - 69%Полнота Бета - 79%Частично - 5

Настройка WSL 6 возможностей / с поддержкой LTS

Экспериментально0%

Альфа67%

Бета79%

[Windows](</ru/platforms/windows>), [Начало работы](</ru/start/getting-started>)

CLI 8 возможностей / с поддержкой LTS

Экспериментально0%

Альфа67%

Бета79%

[Windows](</ru/platforms/windows>), [Начало работы](</ru/start/getting-started>), [Обновление](</ru/install/updating>), [Onboard](</ru/cli/onboard>), [Doctor](</ru/cli/doctor>), [Статус](</ru/cli/status>), [Журналы](</ru/cli/logs>)

Жизненный цикл службы Gateway 10 возможностей / с поддержкой LTS

Экспериментально0%

Альфа67%

Бета79%

[Windows](</ru/platforms/windows>), [Указатель](</ru/gateway>), [Doctor](</ru/gateway/doctor>)

Доступ к Gateway и экспонирование 11 возможностей / с поддержкой LTS

Экспериментально0%

Альфа67%

Бета79%

[Аутентификация](</ru/gateway/authentication>), [Секреты](</ru/gateway/secrets>), [Удаленный доступ](</ru/gateway/remote>), [Регламент экспонирования](</ru/gateway/security/exposure-runbook>), [Windows](</ru/platforms/windows>)

Диагностика и восстановление 6 возможностей / с поддержкой LTS

Экспериментально38%

Бета79%

Бета79%

[Windows](</ru/platforms/windows>), [Статус](</ru/cli/status>), [Журналы](</ru/cli/logs>), [Doctor](</ru/cli/doctor>), [Doctor](</ru/gateway/doctor>)

Браузер и интерфейс управления 6 возможностей

Экспериментально0%

Альфа67%

Бета79%

[Устранение неполадок удаленного CDP браузера в WSL2 Windows](</ru/tools/browser-wsl2-windows-remote-cdp-troubleshooting>), [Браузер](</ru/tools/browser>), [Интерфейс управления](</ru/web/control-ui>)

Raspberry Pi и малые устройства Linux - M3 Бета - 4 области

Документация платформы существует, а путь Gateway основан на Linux. Для перехода выше требуется аппаратно-специфическое smoke-подтверждение выпуска.

Покрытие: экспериментально - 0%Качество: альфа - 67%Полнота: бета - 79%Нет

Настройка и совместимость 12 возможностей

Экспериментальный0%

Альфа67%

Бета79%

[Raspberry Pi](</ru/install/raspberry-pi>), [Индекс](</ru/install>), [FAQ первого запуска](</ru/help/faq-first-run>), [FAQ](</ru/help/faq>), [Linux](</ru/platforms/linux>), [Установщик](</ru/install/installer>)

Удаленный доступ и аутентификация 9 возможностей

Экспериментальный0%

Альфа67%

Бета79%

[Raspberry Pi](</ru/install/raspberry-pi>), [Аутентификация](</ru/gateway/authentication>), [Секреты](</ru/gateway/secrets>), [Сопряжение](</ru/gateway/pairing>), [Устройства](</ru/cli/devices>), [Удаленный доступ](</ru/gateway/remote>), [Tailscale](</ru/gateway/tailscale>)

Среда выполнения Gateway 10 возможностей

Экспериментальный0%

Альфа67%

Бета79%

[Индекс](</ru/gateway>), [Gateway](</ru/cli/gateway>), [Raspberry Pi](</ru/install/raspberry-pi>), [Linux](</ru/platforms/linux>), [VPS](</ru/vps>)

Производительность и диагностика 5 возможностей

Экспериментальный0%

Альфа67%

Бета79%

[Raspberry Pi](</ru/install/raspberry-pi>), [Linux](</ru/platforms/linux>), [Состояние](</ru/gateway/health>), [Диагностика](</ru/gateway/diagnostics>)

Приложение-компаньон для macOS - M3 Бета - 8 областей

Доступны развитое приложение в строке меню, разрешения, режим Node, Canvas, голосовая активация, WebChat и удаленный режим. Все еще развивается достаточно быстро, чтобы не считать его стабильным.

Покрытие: экспериментальный уровень - 0%Качество: альфа - 66%Завершенность: бета - 78%Нет

Холст 4 возможности

Экспериментальный0%

Альфа66%

Бета78%

[Холст](</ru/platforms/mac/canvas>), [Macos](</ru/platforms/macos>), [Webchat](</ru/web/webchat>)

Локальная настройка 7 возможностей

Экспериментальный0%

Альфа66%

Бета78%

[Встроенный Gateway](</ru/platforms/mac/bundled-gateway>), [Macos](</ru/platforms/macos>), [Дочерний процесс](</ru/platforms/mac/child-process>), [Настройка разработки](</ru/platforms/mac/dev-setup>)

Состояние и настройки 5 возможностей

Экспериментальный0%

Альфа66%

Бета78%

[Строка меню](</ru/platforms/mac/menu-bar>), [Значок](</ru/platforms/mac/icon>), [Macos](</ru/platforms/macos>), [Состояние](</ru/platforms/mac/health>), [Журналирование](</ru/platforms/mac/logging>), [Удаленный доступ](</ru/platforms/mac/remote>)

Нативные возможности 5 возможностей

Экспериментальный0%

Альфа66%

Бета78%

[Macos](</ru/platforms/macos>), [Xpc](</ru/platforms/mac/xpc>), [Разрешения](</ru/platforms/mac/permissions>), [Подписание](</ru/platforms/mac/signing>), [Peekaboo](</ru/platforms/mac/peekaboo>)

Удаленные подключения 3 возможности

Экспериментальный0%

Альфа66%

Бета78%

[Удаленный доступ](</ru/platforms/mac/remote>), [Macos](</ru/platforms/macos>), [Удаленный доступ](</ru/gateway/remote>)

Голос и Talk 3 возможности

Экспериментальный0%

Альфа66%

Бета78%

[Voicewake](</ru/platforms/mac/voicewake>), [Голосовое наложение](</ru/platforms/mac/voice-overlay>), [Talk](</ru/nodes/talk>), [Macos](</ru/platforms/macos>)

WebChat 3 возможности

Экспериментальный0%

Альфа66%

Бета78%

[Webchat](</ru/platforms/mac/webchat>), [Macos](</ru/platforms/macos>), [Webchat](</ru/web/webchat>)

Удаленный WebChat 5 возможностей

Экспериментальный0%

Альфа66%

Бета78%

[Webchat](</ru/platforms/mac/webchat>), [Удаленный доступ](</ru/gateway/remote>), [Удаленный доступ](</ru/platforms/mac/remote>)

Android-приложение - M2 Альфа - 7 областей

Публичный путь Google Play существует, но документация приложения все еще описывает переработку как крайне раннюю альфа-версию и отдельно указывает работу по усилению релизной готовности.

Покрытие экспериментальное - 0%Качество альфа - 59%Завершенность альфа - 66%Нет

Захват медиа 1 возможность

Экспериментальный0%

Альфа59%

Альфа66%

[Android](</ru/platforms/android>), [Камера](</ru/nodes/camera>)

Мобильный чат 1 возможность

Экспериментальный0%

Альфа59%

Альфа66%

[Android](</ru/platforms/android>)

Настройка подключения 1 возможность

Экспериментальный0%

Альфа59%

Альфа66%

[Android](</ru/platforms/android>), [Bonjour](</ru/gateway/bonjour>), [Сопряжение](</ru/gateway/pairing>)

Распространение 3 возможности

Экспериментальный0%

Альфа59%

Альфа66%

[Android](</ru/platforms/android>)

Настройки 1 возможность

Экспериментальный0%

Альфа59%

Альфа66%

[Android](</ru/platforms/android>)

Голос 1 возможность

Экспериментальный0%

Альфа59%

Альфа66%

[Android](</ru/platforms/android>), [Разговор](</ru/nodes/talk>)

Среда выполнения устройства 2 возможности

Экспериментальный0%

Альфа59%

Альфа66%

[Android](</ru/platforms/android>), [Устранение неполадок](</ru/nodes/troubleshooting>), [Протокол](</ru/gateway/protocol>)

Нативная Windows - M2 Alpha - 4 области

Основные потоки CLI/Gateway работают, но документация по-прежнему рекомендует WSL2 для полноценного опыта и перечисляет ограничения нативной версии.

Покрытие Экспериментальный - 0%Качество Альфа - 58%Полнота Альфа - 66%Частично - 1

CLI 9 возможностей / с поддержкой LTS

Экспериментальный0%

Альфа54%

Альфа64%

[Индекс](</ru/install>), [Установщик](</ru/install/installer>), [Windows](</ru/platforms/windows>), [Начало работы](</ru/start/getting-started>), [Onboard](</ru/cli/onboard>)

Управление Gateway 11 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Windows](</ru/platforms/windows>), [Индекс](</ru/gateway>), [Gateway](</ru/cli/gateway>), [Doctor](</ru/cli/doctor>)

Сеть 4 возможности

Экспериментальный0%

Альфа59%

Альфа66%

[Windows](</ru/platforms/windows>), [Индекс](</ru/gateway>), [Gateway](</ru/cli/gateway>)

Обновления 4 возможности

Экспериментальный0%

Альфа59%

Альфа66%

[Обновление](</ru/install/updating>), [CI](</ru/ci>)

Kubernetes hosting - M2 Alpha - 4 areas

Хостинг Kubernetes — это отдельный путь развертывания кластера на основе Kustomize. Текущая оценка показывает реальный минимальный путь развертывания с пробелами в Kubernetes-специфичной CI, упаковке ingress/TLS/NetworkPolicy, резервном копировании и восстановлении, а также усилении защиты для production-доступа.

Покрытие Experimental - 0%Качество Alpha - 55%Полнота Alpha - 61%Нет

Настройка развертывания 5 возможностей

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</ru/install/kubernetes>), [Индекс](</ru/install>)

Конфигурация и секреты 5 возможностей

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</ru/install/kubernetes>), [Секреты](</ru/gateway/secrets>), [Окружение](</ru/help/environment>)

Доступ и экспонирование 5 возможностей

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</ru/install/kubernetes>), [Аутентификация](</ru/gateway/authentication>), [Удаленный доступ](</ru/gateway/remote>), [Инструкция по экспонированию](</ru/gateway/security/exposure-runbook>)

Жизненный цикл кластера 5 возможностей

Experimental0%

Alpha55%

Alpha61%

[Kubernetes](</ru/install/kubernetes>), [Индекс](</ru/gateway>)

Приложение iOS - M1 Experimental - 8 областей

Внутреннее превью / супер-альфа. Потоки TestFlight и push-уведомлений на основе ретранслятора существуют, но публичной дистрибуции пока нет.

Покрытие Экспериментальное - 0%Качество Экспериментальное - 41%Полнота Экспериментальная - 44%Нет

Медиа и общий доступ 1 возможность

Экспериментальное0%

Экспериментальное41%

Экспериментальное44%

[Ios](</ru/platforms/ios>), [Камера](</ru/nodes/camera>)

Canvas и экран 1 возможность

Экспериментальное0%

Экспериментальное41%

Экспериментальное44%

[Ios](</ru/platforms/ios>), [Canvas](</ru/plugins/reference/canvas>)

Чат и сеансы 1 возможность

Экспериментальное0%

Экспериментальное41%

Экспериментальное44%

[Ios](</ru/platforms/ios>), [Веб-чат](</ru/web/webchat>), [Протокол](</ru/gateway/protocol>)

Настройка и диагностика Gateway 7 возможностей

Экспериментальное0%

Экспериментальное41%

Экспериментальное44%

[Ios](</ru/platforms/ios>), [Сопряжение](</ru/channels/pairing>)

Распространение 1 возможность

Экспериментальное0%

Экспериментальное41%

Экспериментальное44%

[Ios](</ru/platforms/ios>)

Команды устройства 2 возможности

Экспериментальное0%

Экспериментальное41%

Экспериментальное44%

[Ios](</ru/platforms/ios>), [Протокол](</ru/gateway/protocol>)

Уведомления и фоновый режим 1 возможность

Экспериментальное0%

Экспериментальное41%

Экспериментальное44%

[Ios](</ru/platforms/ios>), [Конфигурация](</ru/gateway/configuration>)

Голос 1 возможность

Экспериментальное0%

Экспериментальное41%

Экспериментальное44%

[Ios](</ru/platforms/ios>), [Разговор](</ru/nodes/talk>)

Nix install path - M1 Experimental - 5 areas

Необязательный процесс установки. Требуется более четкое обещание поддержки перед продвижением в статус альфа-/бета-версии.

Покрытие: экспериментальное - 0%Качество: экспериментальное - 41%Полнота: экспериментальное - 44%Нет

Передача установки 4 возможности

Экспериментальный0%

Экспериментальный41%

Экспериментальный44%

[Nix](</ru/install/nix>), [Индекс](</ru/install>), [Каталог документации](</ru/start/docs-directory>)

Жизненный цикл Plugin 4 возможности

Экспериментальный0%

Экспериментальный41%

Экспериментальный44%

[Управление плагинами](</ru/plugins/manage-plugins>), [Plugin](</ru/tools/plugin>), [Nix](</ru/install/nix>)

Активация и UX приложения 7 возможностей

Экспериментальный0%

Экспериментальный41%

Экспериментальный44%

[Nix](</ru/install/nix>)

Конфигурация и состояние 7 возможностей

Экспериментальный0%

Экспериментальный41%

Экспериментальный44%

[Nix](</ru/install/nix>), [Настройка](</ru/cli/setup>), [Среда](</ru/help/environment>)

Среда выполнения сервиса и защитные проверки 8 возможностей

Экспериментальный0%

Экспериментальный41%

Экспериментальный44%

[Nix](</ru/install/nix>), [Настройка](</ru/cli/setup>), [Диагностика](</ru/cli/doctor>), [Обновление](</ru/cli/update>)

сопутствующие поверхности watchOS - M1 Экспериментальный - 5 областей

В исходном коде есть поверхности приложения/расширения Watch; публичная документация пока не представляет это как пользовательскую функцию.

Покрытие: экспериментальное - 0%Качество: экспериментальное - 41%Полнота: экспериментальная - 44%Нет

Доставка и восстановление 7 возможностей

Экспериментальный0%

Экспериментальный41%

Экспериментальный44%

[iOS](</ru/platforms/ios>)

Утверждения выполнения 3 возможности

Экспериментальный0%

Экспериментальный41%

Экспериментальный44%

[Утверждения выполнения](</ru/tools/exec-approvals>), [iOS](</ru/platforms/ios>)

Распространение и поддержка 6 возможностей

Экспериментальный0%

Экспериментальный41%

Экспериментальный44%

[iOS](</ru/platforms/ios>)

Уведомления и ответы 7 возможностей

Экспериментальный0%

Экспериментальный41%

Экспериментальный44%

[iOS](</ru/platforms/ios>)

Интерфейс приложения для часов 3 возможности

Экспериментальный0%

Экспериментальный41%

Экспериментальный44%

[iOS](</ru/platforms/ios>)

Сопутствующее приложение для Linux - M0 Запланировано - 5 областей

В документации сказано, что нативные сопутствующие приложения для Linux запланированы; Gateway сегодня является поддерживаемым способом работы с Linux.

Покрытие Экспериментальный - 0%Качество Экспериментальный - 19%Завершенность Экспериментальный - 21%Нет

Распространение приложения 3 возможности

Экспериментальное0%

Экспериментальное19%

Экспериментальное21%

[Linux](</ru/platforms/linux>), [Указатель](</ru/platforms>), [Указатель](</ru/install>)

Подключение Gateway 4 возможности

Экспериментальное0%

Экспериментальное19%

Экспериментальное21%

[Linux](</ru/platforms/linux>), [Указатель](</ru/gateway>), [Сопряжение](</ru/gateway/pairing>), [Удаленный доступ](</ru/gateway/remote>)

Чат и сеансы 3 возможности

Экспериментальное0%

Экспериментальное19%

Экспериментальное21%

[Linux](</ru/platforms/linux>), [Протокол](</ru/gateway/protocol>), [Webchat](</ru/web/webchat>)

Возможности рабочего стола 9 возможностей

Экспериментальное0%

Экспериментальное19%

Экспериментальное21%

[Linux](</ru/platforms/linux>), [Подтверждения Exec](</ru/tools/exec-approvals>), [Секреты](</ru/gateway/secrets>), [Указатель](</ru/nodes>), [Exec](</ru/tools/exec>), [Разговор](</ru/nodes/talk>), [Камера](</ru/nodes/camera>)

Состояние и диагностика 7 возможностей

Экспериментальное0%

Экспериментальное19%

Экспериментальное21%

[Linux](</ru/platforms/linux>), [Openclaw](</ru/start/openclaw>), [Doctor](</ru/gateway/doctor>)

Нативное сопутствующее приложение для Windows - M0 запланировано - 5 областей

Только запланировано.

Покрытие экспериментальное - 0%Качество экспериментальное - 19%Полнота экспериментальная - 21%Нет

Установка и обновления 4 возможности

Экспериментальный0%

Экспериментальный19%

Экспериментальный21%

[Windows](</ru/platforms/windows>), [Индекс](</ru/install>)

Подключение к Gateway 3 возможности

Экспериментальный0%

Экспериментальный19%

Экспериментальный21%

[Windows](</ru/platforms/windows>), [Индекс](</ru/gateway>), [Сопряжение](</ru/gateway/pairing>), [Удаленный доступ](</ru/gateway/remote>)

Сеансы чата 2 возможности

Экспериментальный0%

Экспериментальный19%

Экспериментальный21%

[Windows](</ru/platforms/windows>), [Протокол](</ru/gateway/protocol>)

Состояние и восстановление 5 возможностей

Экспериментальный0%

Экспериментальный19%

Экспериментальный21%

[Windows](</ru/platforms/windows>), [Doctor](</ru/gateway/doctor>), [Индекс](</ru/gateway>)

Инструменты рабочего стола и разрешения 10 возможностей

Экспериментальный0%

Экспериментальный19%

Экспериментальный21%

[Windows](</ru/platforms/windows>), [Индекс](</ru/nodes>), [Exec](</ru/tools/exec>), [Подтверждения Exec](</ru/tools/exec-approvals>), [Индекс](</ru/gateway/security>)

### Канал

Discord - M4 Стабильный - 6 областей

Подробная документация и широкое покрытие функций. Пути голосовых функций и делегирования следует оценивать отдельно как бета/альфа.

Покрытие Экспериментальный - 0%Качество Бета - 73%Полнота Стабильный - 87%Частично - 4

Настройка и эксплуатация каналов 10 возможностей / с поддержкой LTS

Экспериментальный0%

Бета73%

Стабильный87%

[Discord](</ru/channels/discord>), [Discord](</ru/plugins/reference/discord>), [Fly](</ru/install/fly>), [Слеш-команды](</ru/tools/slash-commands>), [Состояние](</ru/gateway/health>), [Каналы](</ru/cli/channels>), [Каналы конфигурации](</ru/gateway/config-channels>)

Доступ и идентификация 6 возможностей / с поддержкой LTS

Экспериментальный0%

Бета73%

Стабильный87%

[Discord](</ru/channels/discord>), [Сопряжение](</ru/channels/pairing>), [Группы доступа](</ru/channels/access-groups>), [Группы](</ru/channels/groups>)

Маршрутизация и доставка разговоров 12 возможностей / с поддержкой LTS

Экспериментальный0%

Бета73%

Стабильный87%

[Discord](</ru/channels/discord>), [Маршрутизация каналов](</ru/channels/channel-routing>), [Группы](</ru/channels/groups>), [Группы доступа](</ru/channels/access-groups>), [ACP-агенты](</ru/tools/acp-agents>), [Субагенты](</ru/tools/subagents>)

Медиа и расширенный контент 1 возможность / с поддержкой LTS

Экспериментальный0%

Бета73%

Стабильный87%

[Discord](</ru/channels/discord>)

Нативные элементы управления и подтверждения 5 возможностей

Экспериментальный0%

Бета73%

Стабильный87%

[Discord](</ru/channels/discord>), [Слеш-команды](</ru/tools/slash-commands>)

Голос в реальном времени и звонки 5 возможностей

Экспериментальный0%

Бета73%

Стабильный87%

[Discord](</ru/channels/discord>), [Openai](</ru/providers/openai>), [Elevenlabs](</ru/providers/elevenlabs>), [QA E2E-автоматизация](</ru/concepts/qa-e2e-automation>), [Каналы конфигурации](</ru/gateway/config-channels>)

Telegram - M3 Бета - 5 областей

Основной канал достаточно зрелый для регулярного использования, но UX с высокой вариативностью и пограничные случаи с медиа требуют регулярного подтверждения сценариями.

Покрытие: экспериментальный - 0%Качество: альфа - 68%Полнота: бета - 78%Полное - 5

Настройка и эксплуатация каналов 10 возможностей / с поддержкой LTS

Экспериментальный0%

Альфа66%

Бета78%

[Telegram](</ru/channels/telegram>), [Каналы конфигурации](</ru/gateway/config-channels>), [Каналы](</ru/cli/channels>)

Доступ и идентификация 10 возможностей / с поддержкой LTS

Экспериментальный0%

Альфа66%

Бета78%

[Telegram](</ru/channels/telegram>), [Сопряжение](</ru/channels/pairing>), [Группы доступа](</ru/channels/access-groups>), [Группы](</ru/channels/groups>), [Несколько агентов](</ru/concepts/multi-agent>)

Маршрутизация и доставка бесед 1 возможность / с поддержкой LTS

Экспериментальный0%

Альфа66%

Бета78%

[Telegram](</ru/channels/telegram>), [Группы](</ru/channels/groups>), [Несколько агентов](</ru/concepts/multi-agent>)

Медиа и расширенный контент 1 возможность / с поддержкой LTS

Экспериментальный0%

Альфа66%

Бета78%

[Telegram](</ru/channels/telegram>), [Геопозиция](</ru/channels/location>)

Нативные элементы управления и подтверждения 9 возможностей / с поддержкой LTS

Экспериментальный0%

Бета77%

Бета79%

[Telegram](</ru/channels/telegram>), [Подтверждения Exec](</ru/tools/exec-approvals>), [Реакции](</ru/tools/reactions>)

Slack - M3 Бета - 5 областей

Полноценная документация канала и поверхность маршрутизации. Требуются оценочные таблицы для сценариев установки в рабочее пространство и администрирования.

Покрытие: экспериментальный - 0%Качество: альфа - 66%Полнота: бета - 78%Полное - 5

Настройка каналов и операции 10 возможностей / с поддержкой LTS

Экспериментальный0%

Альфа66%

Бета78%

[Slack](</ru/channels/slack>), [Slack](</ru/plugins/reference/slack>), [Секреты](</ru/gateway/secrets>), [Автоматизация QA E2E](</ru/concepts/qa-e2e-automation>), [Устранение неполадок](</ru/channels/troubleshooting>)

Доступ и идентификация 1 возможность / с поддержкой LTS

Экспериментальный0%

Альфа66%

Бета78%

[Slack](</ru/channels/slack>), [Сопряжение](</ru/channels/pairing>)

Маршрутизация и доставка разговоров 5 возможностей / с поддержкой LTS

Экспериментальный0%

Альфа66%

Бета78%

[Slack](</ru/channels/slack>), [Защита от циклов бота](</ru/channels/bot-loop-protection>), [Сопряжение](</ru/channels/pairing>)

Медиа и расширенный контент 1 возможность / с поддержкой LTS

Экспериментальный0%

Альфа66%

Бета78%

[Slack](</ru/channels/slack>), [Автоматизация QA E2E](</ru/concepts/qa-e2e-automation>)

Нативные элементы управления и подтверждения 8 возможностей / с поддержкой LTS

Экспериментальный0%

Альфа66%

Бета78%

[Slack](</ru/channels/slack>), [Slash-команды](</ru/tools/slash-commands>), [Подтверждения выполнения команд](</ru/tools/exec-approvals>)

iMessage и BlueBubbles - M3 Бета - 5 областей

Поддерживаемый iMessage работает через imsg на хосте macOS Messages с выполненным входом; устаревшие конфигурации BlueBubbles требуют миграции. Держите явно видимыми разрешения macOS, SSH-обертку, SIP/private API и оговорки по миграции.

Покрытие: экспериментальный - 0%Качество: альфа - 66%Завершенность: бета - 78%Нет

Настройка и эксплуатация каналов 11 возможностей

Экспериментальный0%

Alpha66%

Beta78%

[Bluebubbles Imessage](</ru/announcements/bluebubbles-imessage>), [Imessage From Bluebubbles](</ru/channels/imessage-from-bluebubbles>), [Настройка каналов](</ru/gateway/config-channels>), [Imessage](</ru/channels/imessage>)

Доступ и идентификация 6 возможностей

Экспериментальный0%

Alpha66%

Beta78%

[Imessage](</ru/channels/imessage>), [Imessage From Bluebubbles](</ru/channels/imessage-from-bluebubbles>), [Настройка каналов](</ru/gateway/config-channels>)

Маршрутизация и доставка разговоров 4 возможности

Экспериментальный0%

Alpha66%

Beta78%

[Imessage](</ru/channels/imessage>)

Медиа и расширенное содержимое 7 возможностей

Экспериментальный0%

Alpha66%

Beta78%

[Imessage](</ru/channels/imessage>), [Imessage From Bluebubbles](</ru/channels/imessage-from-bluebubbles>), [Настройка каналов](</ru/gateway/config-channels>)

Нативные элементы управления и подтверждения 3 возможности

Экспериментальный0%

Alpha66%

Beta78%

[Imessage](</ru/channels/imessage>)

WhatsApp - M3 Beta - 5 областей

Основной путь важен и документирован; нестабильность upstream Baileys/сессий удерживает его ниже Stable.

Покрытие Experimental - 0%Качество Alpha - 66%Полнота Beta - 78%Нет

Настройка каналов и операции 5 возможностей

Экспериментальный0%

Альфа66%

Бета78%

[WhatsApp](</ru/channels/whatsapp>), [Настройка каналов](</ru/gateway/config-channels>), [WhatsApp](</ru/plugins/reference/whatsapp>), [Автоматизация QA E2E](</ru/concepts/qa-e2e-automation>), [Диагностика](</ru/gateway/doctor>)

Доступ и идентификация 7 возможностей

Экспериментальный0%

Альфа66%

Бета78%

[WhatsApp](</ru/channels/whatsapp>), [Настройка каналов](</ru/gateway/config-channels>), [Автоматизация QA E2E](</ru/concepts/qa-e2e-automation>), [Сопряжение](</ru/channels/pairing>)

Маршрутизация и доставка разговоров 4 возможности

Экспериментальный0%

Альфа66%

Бета78%

[WhatsApp](</ru/channels/whatsapp>), [Групповые сообщения](</ru/channels/group-messages>)

Медиа и расширенный контент 2 возможности

Экспериментальный0%

Альфа66%

Бета78%

[WhatsApp](</ru/channels/whatsapp>)

Нативные элементы управления и подтверждения 2 возможности

Экспериментальный0%

Альфа66%

Бета78%

[WhatsApp](</ru/channels/whatsapp>)

Matrix - M2 Alpha - 6 areas

Поддерживается через встроенный Plugin. Нужны оценочные карты моста, аутентификации и жизненного цикла комнат.

Покрытие: экспериментальное - 0%Качество: альфа - 60%Полнота: альфа - 67%Нет

Настройка и эксплуатация каналов 5 возможностей

Экспериментально0%

Альфа60%

Альфа67%

[Matrix](</ru/channels/matrix>), [Миграция Matrix](</ru/channels/matrix-migration>)

Доступ и идентификация 7 возможностей

Экспериментально0%

Альфа60%

Альфа67%

[Matrix](</ru/channels/matrix>), [Группы](</ru/channels/groups>), [Защита от зацикливания ботов](</ru/channels/bot-loop-protection>)

Маршрутизация и доставка разговоров 1 возможность

Экспериментально0%

Альфа60%

Альфа67%

[Matrix](</ru/channels/matrix>)

Медиа и расширенное содержимое 1 возможность

Экспериментально0%

Альфа60%

Альфа67%

[Matrix](</ru/channels/matrix>)

Нативные элементы управления и подтверждения 6 возможностей

Экспериментально0%

Альфа60%

Альфа67%

[Matrix](</ru/channels/matrix>)

Шифрование и проверка 3 возможности

Экспериментально0%

Альфа60%

Альфа67%

[Matrix](</ru/channels/matrix>), [Миграция Matrix](</ru/channels/matrix-migration>)

Google Chat - M2 Альфа - 5 областей

Документированный канал, но корпоративная/административная настройка повышает риск зрелости.

Покрытие Экспериментально - 0%Качество Альфа - 59%Полнота Альфа - 66%Нет

Настройка и эксплуатация каналов 16 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Googlechat](</ru/channels/googlechat>), [Googlechat](</ru/plugins/reference/googlechat>), [Настройка каналов](</ru/gateway/config-channels>), [Справочник Wizard CLI](</ru/start/wizard-cli-reference>), [Секреты](</ru/gateway/secrets>), [Поверхность учетных данных Secretref](</ru/reference/secretref-credential-surface>), [Состояние](</ru/gateway/health>), [Инвентарь Plugin](</ru/plugins/plugin-inventory>), [Индекс](</ru/channels>)

Доступ и идентификация 11 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Googlechat](</ru/channels/googlechat>), [Сопряжение](</ru/channels/pairing>), [Группы доступа](</ru/channels/access-groups>), [Настройка каналов](</ru/gateway/config-channels>), [Защита от циклов ботов](</ru/channels/bot-loop-protection>), [Маршрутизация каналов](</ru/channels/channel-routing>)

Маршрутизация и доставка бесед 1 возможность

Экспериментальный0%

Альфа59%

Альфа66%

[Googlechat](</ru/channels/googlechat>), [Защита от циклов ботов](</ru/channels/bot-loop-protection>), [Группы доступа](</ru/channels/access-groups>), [Маршрутизация каналов](</ru/channels/channel-routing>)

Медиа и расширенный контент 1 возможность

Экспериментальный0%

Альфа59%

Альфа66%

[Googlechat](</ru/channels/googlechat>), [Сообщение](</ru/cli/message>), [Понимание медиа](</ru/nodes/media-understanding>), [Поверхность учетных данных Secretref](</ru/reference/secretref-credential-surface>)

Нативные элементы управления и подтверждения 16 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Googlechat](</ru/channels/googlechat>), [Сообщение](</ru/cli/message>), [Понимание медиа](</ru/nodes/media-understanding>), [Поверхность учетных данных Secretref](</ru/reference/secretref-credential-surface>), [Реакции](</ru/tools/reactions>), [Слэш-команды](</ru/tools/slash-commands>), [Настройка агентов](</ru/gateway/config-agents>), [Рефакторинг жизненного цикла сообщений](</ru/concepts/message-lifecycle-refactor>)

Microsoft Teams - M2 Alpha - 5 областей

Корпоративные потоки аутентификации и администрирования требуют явного подтверждения сценариями.

Покрытие Экспериментальный - 0%Качество Альфа - 59%Полнота Альфа - 66%Нет

Настройка и эксплуатация канала 9 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Msteams](</ru/channels/msteams>), [Msteams](</ru/plugins/reference/msteams>), [Каналы конфигурации](</ru/gateway/config-channels>), [Работоспособность](</ru/gateway/health>)

Доступ и идентификация 9 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Msteams](</ru/channels/msteams>), [Сопряжение](</ru/channels/pairing>), [Группы доступа](</ru/channels/access-groups>)

Маршрутизация и доставка разговоров 5 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Msteams](</ru/channels/msteams>), [Группы](</ru/channels/groups>), [Маршрутизация каналов](</ru/channels/channel-routing>)

Медиа и расширенный контент 5 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Msteams](</ru/channels/msteams>)

Нативные элементы управления и подтверждения 5 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Msteams](</ru/channels/msteams>), [Расширенные подтверждения Exec](</ru/tools/exec-approvals-advanced>)

Signal - M2 Альфа - 5 областей

Документация по поддерживаемому каналу существует; нужны более убедительные подтверждения установки и переподключения.

Покрытие Экспериментальный - 0%Качество Альфа - 59%Полнота Альфа - 66%Нет

Настройка и эксплуатация каналов 7 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Signal](</ru/channels/signal>), [Signal](</ru/plugins/reference/signal>)

Доступ и идентификация 6 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Signal](</ru/channels/signal>)

Маршрутизация и доставка бесед 1 возможность

Экспериментальный0%

Альфа59%

Альфа66%

[Signal](</ru/channels/signal>)

Медиа и насыщенный контент 7 возможностей

Экспериментальный0%

Альфа59%

Альфа66%

[Signal](</ru/channels/signal>)

Нативные элементы управления и подтверждения 3 возможности

Экспериментальный0%

Альфа59%

Альфа66%

[Signal](</ru/channels/signal>)

Feishu, QQ Bot, WeChat, Yuanbao, Zalo, Zalo Personal, региональные каналы - M2 Альфа - 4 области

Важное региональное покрытие, но уровень публичной поддержки следует выверять для каждого типа учетной записи, одобрения upstream и подтверждений от мейнтейнеров.

Покрытие Экспериментальный - 0%Качество Альфа - 55%Полнота Альфа - 58%Нет

Настройка и эксплуатация каналов 6 возможностей

Экспериментальный0%

Alpha61%

Alpha68%

[Индекс](</ru/channels>), [Сопряжение](</ru/channels/pairing>), [Feishu](</ru/plugins/reference/feishu>), [Внутренняя архитектура](</ru/plugins/architecture-internals>)

Доступ и идентификация 1 возможность

Экспериментальный0%

Alpha53%

Alpha54%

Нет связанных документов

Маршрутизация и доставка бесед 1 возможность

Экспериментальный0%

Alpha53%

Alpha54%

Нет связанных документов

Медиа и расширенное содержимое 1 возможность

Экспериментальный0%

Alpha53%

Alpha54%

Нет связанных документов

Mattermost, LINE, IRC, Nextcloud Talk, Nostr, Twitch, Tlon, Synology Chat - M2 Alpha - 4 области

Поддерживаемые поверхности существуют, но зрелость, вероятно, зависит от покрытия со стороны upstream и сопровождающих. Оцените по отдельности позже.

Охват Экспериментальный - 0%Качество Alpha - 53%Полнота Alpha - 54%Нет

Настройка и эксплуатация каналов 1 возможность

Экспериментальный0%

Альфа53%

Альфа54%

Нет связанных документов

Доступ и идентификация 1 возможность

Экспериментальный0%

Альфа53%

Альфа54%

Нет связанных документов

Маршрутизация и доставка разговоров 1 возможность

Экспериментальный0%

Альфа53%

Альфа54%

Нет связанных документов

Медиа и расширенный контент 1 возможность

Экспериментальный0%

Альфа53%

Альфа54%

Нет связанных документов

Канал голосовых вызовов - M1 Экспериментальный - 5 областей

Опциональный путь/путь Plugin со сложным поведением в реальном времени. Требуется карта оценки сценариев перед публичной бета-версией.

Охват: экспериментальный - 0%Качество: экспериментальный - 41%Полнота: экспериментальный - 44%Нет

Настройка и эксплуатация каналов 2 возможности

Экспериментально0%

Экспериментально41%

Экспериментально44%

[Voicecall](</ru/cli/voicecall>), [Голосовой вызов](</ru/plugins/voice-call>), [Протокол](</ru/gateway/protocol>)

Доступ и идентификация 1 возможность

Экспериментально0%

Экспериментально41%

Экспериментально44%

[Голосовой вызов](</ru/plugins/voice-call>), [Voicecall](</ru/cli/voicecall>)

Маршрутизация и доставка разговоров 1 возможность

Экспериментально0%

Экспериментально41%

Экспериментально44%

[Голосовой вызов](</ru/plugins/voice-call>)

Медиа и форматированный контент 2 возможности

Экспериментально0%

Экспериментально41%

Экспериментально44%

[Голосовой вызов](</ru/plugins/voice-call>), [Инвентаризация Plugin](</ru/plugins/plugin-inventory>)

Голос и вызовы в реальном времени 2 возможности

Экспериментально0%

Экспериментально41%

Экспериментально44%

[Голосовой вызов](</ru/plugins/voice-call>)

### Провайдер и инструмент

Автоматизация браузера, exec и инструменты sandbox - M3 Beta - 3 области

Основные инструменты задокументированы, но безопасность хоста и UX разрешений должны оставаться под активной проверкой в scorecard.

Покрытие: экспериментально - 21%Качество: Beta - 75%Полнота: Beta - 79%Частично - 2

Автоматизация браузера 8 возможностей

Экспериментальный13%

Бета79%

Бета79%

[Управление браузером](</ru/tools/browser-control>), [Тестирование](</ru/help/testing>), [Браузер](</ru/tools/browser>), [Индекс](</ru/gateway/security>), [Проверки аудита](</ru/gateway/security/audit-checks>)

Вызов и выполнение инструментов 6 возможностей / с поддержкой LTS

Альфа50%

Бета79%

Бета79%

[Exec](</ru/tools/exec>), [Фоновый процесс](</ru/gateway/background-process>), [HTTP API вызова инструментов](</ru/gateway/tools-invoke-http-api>), [Области действия оператора](</ru/gateway/operator-scopes>), [Протокол](</ru/gateway/protocol>), [Подтверждения Exec](</ru/tools/exec-approvals>), [Расширенные подтверждения Exec](</ru/tools/exec-approvals-advanced>), [Повышенные права](</ru/tools/elevated>)

Песочница и политика инструментов 6 возможностей / с поддержкой LTS

Экспериментальный0%

Альфа68%

Бета79%

[Песочница](</ru/gateway/sandboxing>), [Песочница, политика инструментов и повышенные права](</ru/gateway/sandbox-vs-tool-policy-vs-elevated>), [Инструменты песочницы для нескольких агентов](</ru/tools/multi-agent-sandbox-tools>), [Справочник по среде Codex](</ru/plugins/codex-harness-reference>), [Инструменты конфигурации](</ru/gateway/config-tools>)

Путь провайдера OpenAI и Codex - M3 Бета - 5 областей

Подробная документация, путь OAuth/подписки, голос в реальном времени, изображения и поведение совместимости. Изменчивость провайдера не позволяет перевести это в стабильный статус без подтверждения по оценочной карте релиза.

Покрытие: экспериментальный - 26%Качество: бета - 74%Полнота: бета - 79%Частично - 3

Модель и аутентификация 6 возможностей / с поддержкой LTS

Экспериментально44%

Бета79%

Бета79%

[Openai](</ru/providers/openai>), [Codex Harness](</ru/plugins/codex-harness>), [Модели](</ru/concepts/models>), [Oauth](</ru/concepts/oauth>), [Справочник Codex Harness](</ru/plugins/codex-harness-reference>), [Мониторинг аутентификации](</ru/gateway/authentication>)

Совместимость ответов и инструментов 4 возможности / с поддержкой LTS

Экспериментально40%

Бета79%

Бета79%

[Openai](</ru/providers/openai>), [HTTP API OpenResponses](</ru/gateway/openresponses-http-api>), [HTTP API OpenAI](</ru/gateway/openai-http-api>), [Нативные Plugin Codex](</ru/plugins/codex-native-plugins>)

Нативный Codex Harness 2 возможности / с поддержкой LTS

Экспериментально44%

Бета79%

Бета79%

[Codex Harness](</ru/plugins/codex-harness>), [Среда выполнения Codex Harness](</ru/plugins/codex-harness-runtime>), [Справочник Codex Harness](</ru/plugins/codex-harness-reference>), [Нативные Plugin Codex](</ru/plugins/codex-native-plugins>)

Изображения и мультимодальный ввод 2 возможности

Экспериментально0%

Альфа67%

Бета79%

[Openai](</ru/providers/openai>), [Генерация изображений](</ru/tools/image-generation>), [Изображения](</ru/nodes/images>)

Голос и аудио в реальном времени 2 возможности

Экспериментально0%

Альфа67%

Бета79%

[Openai](</ru/providers/openai>), [Discord](</ru/channels/discord>), [Голосовой вызов](</ru/plugins/voice-call>)

Инструменты веб-поиска - M3 Бета - 4 области

Существует несколько провайдеров и документов. Требуется подтверждение квот, ошибок и SSRF для каждого семейства провайдеров.

Покрытие Экспериментально - 9%Качество Бета - 74%Полнота Бета - 79%Нет

Провайдеры поиска 19 возможностей

Экспериментально11%

Бета79%

Бета79%

[Web](</ru/tools/web>), [Brave Search](</ru/tools/brave-search>), [Tavily](</ru/tools/tavily>), [Exa Search](</ru/tools/exa-search>), [Firecrawl](</ru/tools/firecrawl>), [Perplexity Search](</ru/tools/perplexity-search>), [Duckduckgo Search](</ru/tools/duckduckgo-search>), [Searxng Search](</ru/tools/searxng-search>), [Gemini Search](</ru/tools/gemini-search>), [Grok Search](</ru/tools/grok-search>), [Kimi Search](</ru/tools/kimi-search>), [Minimax Search](</ru/tools/minimax-search>), [Ollama Search](</ru/tools/ollama-search>), [Подпути SDK](</ru/plugins/sdk-subpaths>), [Обзор SDK](</ru/plugins/sdk-overview>), [Манифест](</ru/plugins/manifest>)

Настройка и диагностика 9 возможностей

Экспериментально0%

Альфа68%

Бета79%

[Web](</ru/tools/web>), [Web Fetch](</ru/tools/web-fetch>), [FAQ](</ru/help/faq>), [Затраты на использование API](</ru/reference/api-usage-costs>), [Brave Search](</ru/tools/brave-search>), [Perplexity Search](</ru/tools/perplexity-search>), [Tavily](</ru/tools/tavily>), [Firecrawl](</ru/tools/firecrawl>)

Сетевая безопасность 4 возможности

Экспериментально0%

Альфа68%

Бета79%

[Web](</ru/tools/web>), [Web Fetch](</ru/tools/web-fetch>), [Firecrawl](</ru/tools/firecrawl>), [Searxng Search](</ru/tools/searxng-search>)

Доступность инструментов и получение данных 11 возможностей

Экспериментально25%

Бета79%

Бета79%

[Инструменты конфигурации](</ru/gateway/config-tools>), [Web Fetch](</ru/tools/web-fetch>), [Web](</ru/tools/web>), [FAQ](</ru/help/faq>)

Путь провайдера Anthropic - M3 Beta - 5 областей

Полноправный провайдер моделей. Требуется регулярное подтверждение сценариев аутентификации, каталога и вызовов инструментов.

Покрытие: экспериментально - 0%Качество: бета - 71%Полнота: бета - 78%Нет

Аутентификация и восстановление провайдера 9 возможностей

Экспериментальный0%

Альфа66%

Бета78%

[Anthropic](</ru/providers/anthropic>), [Doctor](</ru/gateway/doctor>), [Примеры конфигурации](</ru/gateway/configuration-examples>), [Устранение неполадок](</ru/gateway/troubleshooting>), [Кэширование промптов](</ru/reference/prompt-caching>)

Выбор модели и среды выполнения 10 возможностей

Экспериментальный0%

Бета78%

Бета79%

[Anthropic](</ru/providers/anthropic>), [Агенты конфигурации](</ru/gateway/config-agents>), [Модели](</ru/concepts/models>), [Бэкенды CLI](</ru/gateway/cli-backends>)

Транспорт запросов и семантика ходов 10 возможностей

Экспериментальный0%

Бета77%

Бета79%

[Anthropic](</ru/providers/anthropic>), [Кэширование промптов](</ru/reference/prompt-caching>), [Устранение неполадок](</ru/gateway/troubleshooting>), [Бэкенды CLI](</ru/gateway/cli-backends>), [Провайдеры моделей](</ru/concepts/model-providers>)

Кэш промптов и контекст 5 возможностей

Экспериментальный0%

Альфа66%

Бета78%

[Anthropic](</ru/providers/anthropic>), [Кэширование промптов](</ru/reference/prompt-caching>), [Устранение неполадок](</ru/gateway/troubleshooting>), [Heartbeat](</ru/gateway/heartbeat>)

Медиа-вводы 4 возможности

Экспериментальный0%

Альфа66%

Бета78%

[Anthropic](</ru/providers/anthropic>), [Агенты конфигурации](</ru/gateway/config-agents>)

Путь провайдера Google - M3 Бета - 5 областей

Полноправный провайдер с поверхностями моделей и реального времени. Требует отдельной оценки Live/Talk.

Покрытие: экспериментальное - 0%Качество: альфа - 66%Полнота: бета - 78%Нет

Настройка провайдера и учетные данные 10 возможностей

Экспериментально0%

Альфа66%

Бета78%

[Google](</ru/providers/google>), [Провайдеры моделей](</ru/concepts/model-providers>)

Маршрутизация моделей и конечные точки 10 возможностей

Экспериментально0%

Альфа66%

Бета78%

[Google](</ru/providers/google>), [Провайдеры моделей](</ru/concepts/model-providers>), [Google](</ru/plugins/reference/google>), [Поиск Gemini](</ru/tools/gemini-search>)

Прямой рантайм Gemini 9 возможностей

Экспериментально0%

Альфа66%

Бета78%

[Google](</ru/providers/google>), [Провайдеры моделей](</ru/concepts/model-providers>), [Частые вопросы о моделях](</ru/help/faq-models>), [Тестирование live](</ru/help/testing-live>)

Медиа, поиск и режим реального времени 10 возможностей

Экспериментально0%

Альфа66%

Бета78%

[Google](</ru/plugins/reference/google>), [Google](</ru/providers/google>)

Кэширование промптов 5 возможностей

Экспериментально0%

Альфа66%

Бета78%

[Кэширование промптов](</ru/reference/prompt-caching>), [Google](</ru/providers/google>), [Провайдеры моделей](</ru/concepts/model-providers>), [Использование токенов](</ru/reference/token-use>)

Путь провайдера OpenRouter - M3 Бета - 4 области

Унифицированный путь провайдера задокументирован и полезен, но поведение отдельных моделей различается.

Покрытие Экспериментально - 0%Качество Альфа - 66%Полнота Бета - 78%Нет

Настройка поставщиков и аутентификация 14 возможностей

Экспериментально0%

Альфа66%

Бета78%

[Openrouter](</ru/providers/openrouter>), [Поставщики моделей](</ru/concepts/model-providers>), [Настройка](</ru/cli/configure>), [Аутентификация](</ru/gateway/authentication>), [Среда](</ru/help/environment>), [Модели](</ru/cli/models>), [Модели](</ru/concepts/models>)

Среда выполнения чата и нормализация 15 возможностей

Экспериментально0%

Альфа66%

Бета78%

[Openrouter](</ru/providers/openrouter>), [Поставщики моделей](</ru/concepts/model-providers>), [Кэширование промптов](</ru/reference/prompt-caching>)

Восстановление поставщиков и диагностика 5 возможностей

Экспериментально0%

Альфа66%

Бета78%

[Отказоустойчивое переключение моделей](</ru/concepts/model-failover>), [Openrouter](</ru/providers/openrouter>), [Модели](</ru/cli/models>)

Генерация медиа и речь 7 возможностей

Экспериментально0%

Альфа66%

Бета78%

[Openrouter](</ru/providers/openrouter>), [Генерация изображений](</ru/tools/image-generation>), [Генерация музыки](</ru/tools/music-generation>), [Обзор медиа](</ru/tools/media-overview>), [Генерация видео](</ru/tools/video-generation>), [TTS](</ru/tools/tts>)

Инструменты генерации изображений, видео и музыки — M2 Альфа — 5 областей

Возможность существует у разных поставщиков, но качество, задержка и совместимость параметров слишком сильно различаются для бета-статуса без подтверждения по каждому поставщику.

Покрытие: экспериментально — 0%Качество: альфа — 61%Полнота: альфа — 68%Нет

Маршрутизация и обнаружение медиа 4 возможности

Экспериментально0%

Альфа61%

Альфа68%

[Агенты конфигурации](</ru/gateway/config-agents>), [Генерация изображений](</ru/tools/image-generation>), [Генерация видео](</ru/tools/video-generation>), [Генерация музыки](</ru/tools/music-generation>)

Жизненный цикл и доставка задач 12 возможностей

Экспериментально0%

Альфа61%

Альфа68%

[Обзор медиа](</ru/tools/media-overview>), [Генерация изображений](</ru/tools/image-generation>), [Генерация видео](</ru/tools/video-generation>), [Генерация музыки](</ru/tools/music-generation>)

Генерация изображений 9 возможностей

Экспериментально0%

Альфа61%

Альфа68%

[Генерация изображений](</ru/tools/image-generation>), [Infer](</ru/cli/infer>), [Обзор медиа](</ru/tools/media-overview>)

Генерация видео 11 возможностей

Экспериментально0%

Альфа61%

Альфа68%

[Генерация видео](</ru/tools/video-generation>), [Runway](</ru/providers/runway>), [Pixverse](</ru/providers/pixverse>), [Fal](</ru/providers/fal>), [Openrouter](</ru/providers/openrouter>)

Генерация музыки 6 возможностей

Экспериментально0%

Альфа61%

Альфа68%

[Генерация музыки](</ru/tools/music-generation>)

Поставщики локальных моделей: Ollama, vLLM, SGLang, LM Studio - M2 Альфа - 5 областей

Полезно и документировано, но разброс окружений велик.

Покрытие: экспериментально - 0%Качество: альфа - 61%Полнота: альфа - 68%Нет

Настройка, жизненный цикл и диагностика провайдеров 12 возможностей

Экспериментально0%

Альфа61%

Альфа68%

[Локальные модели](</ru/gateway/local-models>), [Lmstudio](</ru/providers/lmstudio>), [Ollama](</ru/providers/ollama>), [Vllm](</ru/providers/vllm>), [Сервисы локальных моделей](</ru/gateway/local-model-services>), [Настройка агентов](</ru/gateway/config-agents>), [Устранение неполадок](</ru/gateway/troubleshooting>), [Doctor](</ru/gateway/doctor>)

Нативные Plugin провайдеров 10 возможностей

Экспериментально0%

Альфа61%

Альфа68%

[Ollama](</ru/providers/ollama>), [Lmstudio](</ru/providers/lmstudio>)

Совместимость среды выполнения, совместимой с OpenAI 8 возможностей

Экспериментально0%

Альфа61%

Альфа68%

[Vllm](</ru/providers/vllm>), [Sglang](</ru/providers/sglang>), [Локальные модели](</ru/gateway/local-models>), [Lmstudio](</ru/providers/lmstudio>)

Локальная память и эмбеддинги 5 возможностей

Экспериментально0%

Альфа61%

Альфа68%

[Память](</ru/concepts/memory>), [Doctor](</ru/gateway/doctor>)

Сетевая безопасность и управление промптами 2 возможности

Экспериментально0%

Альфа61%

Альфа68%

[Индекс](</ru/gateway/security>), [Настройка инструментов](</ru/gateway/config-tools>), [Локальные модели](</ru/gateway/local-models>)

Длинный хвост размещенных провайдеров — M2 Альфа — 3 области

Существует много страниц документации и справочника; оценку следует генерировать из метаданных провайдеров плюс покрытие live smoke-проверками.

Покрытие Экспериментальное - 0%Качество Альфа - 61%Полнота Альфа - 68%Нет

Размещенные провайдеры LLM 12 возможностей

Экспериментальное0%

Альфа61%

Альфа68%

[Индекс](</ru/providers>), [Провайдеры моделей](</ru/concepts/model-providers>), [Live-тестирование](</ru/help/testing-live>), [Первичная настройка](</ru/cli/onboard>)

Размещенные медиапровайдеры 8 возможностей

Экспериментальное0%

Альфа61%

Альфа68%

[Манифест](</ru/plugins/manifest>), [Live-тестирование](</ru/help/testing-live>), [Индекс](</ru/providers>)

Операции провайдеров 12 возможностей

Экспериментальное0%

Альфа61%

Альфа68%

[Индекс](</ru/providers>), [Провайдеры моделей](</ru/concepts/model-providers>), [Манифест](</ru/plugins/manifest>), [Live-тестирование](</ru/help/testing-live>), [Модели](</ru/cli/models>)

Was this useful?YesNo

Open issue