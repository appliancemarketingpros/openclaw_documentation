---
title: Nix
source_url: https://docs.openclaw.ai/ru/install/nix
scraped_at: 2026-06-29
---

InstallContainers

Устанавливайте OpenClaw декларативно с **[nix-openclaw](<https://github.com/openclaw/nix-openclaw>)** \- официальным модулем Home Manager с полным набором возможностей.

## Что вы получаете

  * Gateway + приложение macOS + инструменты (whisper, spotify, cameras) -- все с закрепленными версиями
  * Сервис launchd, который сохраняется после перезагрузок
  * Система Plugin с декларативной конфигурацией
  * Мгновенный откат: `home-manager switch --rollback`


## Быстрый старт

* ### Установите Determinate Nix

Если Nix еще не установлен, следуйте инструкциям [установщика Determinate Nix](<https://github.com/DeterminateSystems/nix-installer>).

* ### Создайте локальный flake

Используйте шаблон agent-first из репозитория nix-openclaw:

bashCopy code
[code]
    mkdir -p ~/code/openclaw-local# Copy templates/agent-first/flake.nix from the nix-openclaw repo
[/code]

* ### Настройте секреты

Настройте токен бота для обмена сообщениями и API-ключ поставщика модели. Обычные файлы в `~/.secrets/` вполне подходят.

* ### Заполните заполнители шаблона и переключитесь

bashCopy code
[code]
    home-manager switch
[/code]

* ### Проверьте

Убедитесь, что сервис launchd запущен и ваш бот отвечает на сообщения.

Полные параметры модуля и примеры см. в [README nix-openclaw](<https://github.com/openclaw/nix-openclaw>).

## Поведение среды выполнения в режиме Nix

Когда задано `OPENCLAW_NIX_MODE=1` (автоматически с nix-openclaw), OpenClaw переходит в детерминированный режим для установок, управляемых Nix. Другие пакеты Nix могут задавать тот же режим; nix-openclaw является официальным эталоном.

Его также можно задать вручную:

bashCopy code
[code]
    export OPENCLAW_NIX_MODE=1
[/code]

В macOS приложение с графическим интерфейсом не наследует переменные окружения оболочки автоматически. Вместо этого включите режим Nix через defaults:

bashCopy code
[code]
    defaults write ai.openclaw.mac openclaw.nixMode -bool true
[/code]

### Что меняется в режиме Nix

  * Потоки автоустановки и самоизменения отключены
  * `openclaw.json` рассматривается как неизменяемый. Значения по умолчанию, полученные при запуске, остаются только в среде выполнения, а средства записи конфигурации, такие как настройка, onboarding, изменяющий `openclaw update`, установка/обновление/удаление/включение Plugin, `doctor --fix`, `doctor --generate-gateway-token` и `openclaw config set`, отказываются редактировать файл.
  * Вместо этого агенты должны редактировать исходный код Nix. Для nix-openclaw используйте agent-first [Быстрый старт](<https://github.com/openclaw/nix-openclaw#quick-start>) и задавайте конфигурацию в `programs.openclaw.config` или `instances.<name>.config`.
  * Отсутствующие зависимости выводят сообщения по исправлению, специфичные для Nix
  * UI показывает баннер режима Nix только для чтения


### Пути конфигурации и состояния

OpenClaw читает конфигурацию JSON5 из `OPENCLAW_CONFIG_PATH` и хранит изменяемые данные в `OPENCLAW_STATE_DIR`. При запуске под Nix задавайте их явно в расположения, управляемые Nix, чтобы состояние среды выполнения и конфигурация оставались вне неизменяемого хранилища.

Переменная | Значение по умолчанию  
---|---  
`OPENCLAW_HOME` | `HOME` / `USERPROFILE` / `os.homedir()`  
`OPENCLAW_STATE_DIR` | `~/.openclaw`  
`OPENCLAW_CONFIG_PATH` | `$OPENCLAW_STATE_DIR/openclaw.json`  
  
### Обнаружение PATH сервиса

Сервис gateway launchd/systemd автоматически обнаруживает бинарные файлы Nix-профиля, чтобы plugins и инструменты, запускающие исполняемые файлы, установленные через `nix`, работали без ручной настройки PATH:

  * Когда задан `NIX_PROFILES`, каждая запись добавляется в PATH сервиса с приоритетом справа налево (соответствует приоритету оболочки Nix - самая правая запись побеждает).
  * Когда `NIX_PROFILES` не задан, `~/.nix-profile/bin` добавляется как fallback.


Это относится как к окружениям сервиса launchd в macOS, так и systemd в Linux.

## Связанное

[**nix-openclaw** Модуль Home Manager, являющийся источником истины, и полное руководство по настройке. ](<https://github.com/openclaw/nix-openclaw>) [**Мастер настройки** Пошаговая настройка CLI без Nix. ](</ru/start/wizard>) [**Docker** Контейнеризованная настройка как альтернатива без Nix. ](</ru/install/docker>) [**Обновление** Обновление установок, управляемых Home Manager, вместе с пакетом. ](</ru/install/updating>)

Was this useful?YesNo

Open issue