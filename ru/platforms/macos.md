---
title: приложение macOS
source_url: https://docs.openclaw.ai/ru/platforms/macos
scraped_at: 2026-06-29
---

PlatformsPlatforms overview

Приложение для macOS — это **спутник в строке меню** OpenClaw. Используйте его, когда вам нужен нативный интерфейс в трее, запросы разрешений macOS, уведомления, WebChat, голосовой ввод, Canvas или инструменты узла, размещенные на Mac, например `system.run`.

Если вам нужны только CLI и Gateway, начните с раздела [Начало работы](</ru/start/getting-started>).

## Загрузка

Загрузите сборки приложения для macOS из [релизов OpenClaw на GitHub](<https://github.com/openclaw/openclaw/releases>). Если релиз включает ресурсы приложения для macOS, ищите:

  * `OpenClaw-<version>.dmg` (предпочтительно)
  * `OpenClaw-<version>.zip`


Некоторые релизы включают только CLI, материалы подтверждения или ресурсы Windows. Если в самом новом релизе нет ресурса приложения для macOS, используйте самый новый релиз, в котором он есть, или соберите приложение из исходного кода с помощью [настройки среды разработки macOS](</ru/platforms/mac/dev-setup>).

## Первый запуск

  1. Установите и запустите **OpenClaw.app**.
  2. Выполните контрольный список разрешений macOS.
  3. Выберите режим **Локальный** или **Удаленный**.
  4. Установите CLI `openclaw`, если приложение попросит это сделать.
  5. Откройте WebChat из строки меню и отправьте тестовое сообщение.


Для пути настройки CLI/Gateway используйте [Начало работы](</ru/start/getting-started>). Для восстановления разрешений используйте [Разрешения macOS](</ru/platforms/mac/permissions>).

## Выбор режима Gateway

Режим | Когда использовать | Страница с подробностями  
---|---|---  
Локальный | Этот Mac должен запускать Gateway и поддерживать его работу через launchd. | [Gateway на macOS](</ru/platforms/mac/bundled-gateway>)  
Удаленный | Другой хост запускает Gateway, а этот Mac должен управлять им через SSH, LAN или Tailnet. | [Удаленное управление](</ru/platforms/mac/remote>)  
  
Для локального режима требуется установленный CLI `openclaw`. Приложение может установить его, или вы можете следовать инструкции [Gateway на macOS](</ru/platforms/mac/bundled-gateway>).

## За что отвечает приложение

  * Статус в строке меню, уведомления, состояние работоспособности и WebChat.
  * Запросы разрешений macOS для экрана, микрофона, речи, автоматизации и специальных возможностей.
  * Локальные инструменты узла, такие как Canvas, захват камеры/экрана, уведомления и `system.run`.
  * Запросы подтверждения Exec для команд, размещенных на Mac.
  * SSH-туннели в удаленном режиме или прямые подключения к Gateway.


Приложение **не** заменяет Gateway OpenClaw или общую документацию CLI. Основная конфигурация Gateway, провайдеры, plugins, каналы, инструменты и безопасность описаны в собственной документации.

## Подробные страницы macOS

Задача | Читать  
---|---  
Установить или отладить службу CLI/Gateway | [Gateway на macOS](</ru/platforms/mac/bundled-gateway>)  
Не хранить состояние в папках с облачной синхронизацией | [Gateway на macOS](</ru/platforms/mac/bundled-gateway#state-directory-on-macos>)  
Отладить обнаружение приложения и подключение | [Gateway на macOS](</ru/platforms/mac/bundled-gateway#debug-app-connectivity>)  
Понять поведение launchd | [Жизненный цикл Gateway](</ru/platforms/mac/child-process>)  
Исправить разрешения или проблемы подписи/TCC | [Разрешения macOS](</ru/platforms/mac/permissions>)  
Подключиться к удаленному Gateway | [Удаленное управление](</ru/platforms/mac/remote>)  
Читать статус строки меню и проверки работоспособности | [Строка меню](</ru/platforms/mac/menu-bar>), [Проверки работоспособности](</ru/platforms/mac/health>)  
Использовать встроенный интерфейс чата | [WebChat](</ru/platforms/mac/webchat>)  
Использовать голосовое пробуждение или push-to-talk | [Голосовое пробуждение](</ru/platforms/mac/voicewake>)  
Использовать Canvas и глубокие ссылки Canvas | [Canvas](</ru/platforms/mac/canvas>)  
Разместить PeekabooBridge для автоматизации UI | [Мост Peekaboo](</ru/platforms/mac/peekaboo>)  
Настроить подтверждения команд | [Подтверждения Exec](</ru/tools/exec-approvals>), [расширенные сведения](</ru/tools/exec-approvals-advanced>)  
Проверить команды узла Mac и IPC приложения | [IPC macOS](</ru/platforms/mac/xpc>)  
Собирать журналы | [Журналирование macOS](</ru/platforms/mac/logging>)  
Собрать из исходного кода | [Настройка среды разработки macOS](</ru/platforms/mac/dev-setup>)  
  
## Связанные разделы

  * [Платформы](</ru/platforms>)
  * [Начало работы](</ru/start/getting-started>)
  * [Gateway](</ru/gateway>)
  * [Подтверждения Exec](</ru/tools/exec-approvals>)


Was this useful?YesNo

Open issue