---
title: Переопределения установки Plugin
source_url: https://docs.openclaw.ai/ru/plugins/install-overrides
scraped_at: 2026-06-29
---

ReferencePlugin reference

Переопределения установки Plugin позволяют сопровождающим тестировать установки плагинов на этапе настройки с использованием конкретного npm-пакета или локального tarball, созданного `npm pack`. Они предназначены только для E2E и проверки пакетов. Обычным пользователям следует устанавливать плагины с помощью [`openclaw plugins install`](</ru/cli/plugins>).

## Окружение

Переопределения отключены, если не заданы обе переменные:

bashCopy code
[code]
    export OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1export OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{  "codex": "npm-pack:/tmp/openclaw-codex-2026.5.8.tgz",  "openclaw-web-search": "npm:@openclaw/web-search@2026.5.8"}'
[/code]

Карта переопределений — это JSON с ключами по id плагинов. Значения поддерживают:

  * `npm:<registry-spec>` для пакетов из реестра и точных версий или тегов
  * `npm-pack:<path.tgz>` для локальных tarball, созданных `npm pack`


Относительные пути `npm-pack:` разрешаются относительно текущего рабочего каталога.

## Поведение

Когда поток на этапе настройки запрашивает установку плагина, id которого присутствует в карте, OpenClaw использует источник переопределения вместо каталога, встроенного или стандартного npm-источника. Это применяется к онбордингу и другим потокам, использующим общий установщик плагинов на этапе настройки.

Переопределения по-прежнему проверяют ожидаемый id плагина. Tarball, сопоставленный с `codex`, должен установить плагин, чей id в манифесте равен `codex`.

Переопределения не наследуют официальный статус доверенного источника. Даже когда запись каталога обычно представляет пакет, принадлежащий OpenClaw, переопределение считается тестовым вводом, предоставленным оператором.

Файлы `.env` рабочей области не могут включать переопределения установки. Задавайте эти переменные в доверенной оболочке, задании CI или удаленной тестовой команде, запускающей OpenClaw.

## E2E пакета

Используйте изолированный каталог состояния, чтобы установки пакетов и записи об установке не затрагивали ваше обычное состояние OpenClaw:

bashCopy code
[code]
    npm pack extensions/codex --pack-destination /tmp OPENCLAW_STATE_DIR="$(mktemp -d)" \OPENCLAW_ALLOW_PLUGIN_INSTALL_OVERRIDES=1 \OPENCLAW_PLUGIN_INSTALL_OVERRIDES='{"codex":"npm-pack:/tmp/openclaw-codex-2026.5.8.tgz"}' \pnpm openclaw onboard --mode local
[/code]

Проверьте установленный пакет в каталоге состояния:

bashCopy code
[code]
    find "$OPENCLAW_STATE_DIR/npm/projects" -path '*/node_modules/@openclaw/codex/package.json' -printgrep -R '"@openclaw/codex"' "$OPENCLAW_STATE_DIR/npm/projects"/*/package-lock.json
[/code]

Для E2E с реальным провайдером загрузите настоящий API-ключ из доверенной оболочки или секрета CI перед запуском тестовой команды. Не выводите ключи; сообщайте только источник и наличие ключа.

Was this useful?YesNo

Open issue