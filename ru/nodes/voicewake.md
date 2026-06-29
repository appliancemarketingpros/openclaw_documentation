---
title: Голосовое пробуждение
source_url: https://docs.openclaw.ai/ru/nodes/voicewake
scraped_at: 2026-06-29
---

Gateway & OpsNodes and media

OpenClaw рассматривает **слова пробуждения как единый глобальный список** , принадлежащий **Gateway**.

  * **Пользовательских слов пробуждения для отдельных узлов нет**.
  * **Любой интерфейс узла/приложения может редактировать** список; изменения сохраняются Gateway и рассылаются всем.
  * macOS и iOS сохраняют локальные переключатели **Голосового пробуждения включено/выключено** (локальный UX и разрешения отличаются).
  * На Android Голосовое пробуждение сейчас отключено, а на вкладке «Голос» используется ручной сценарий микрофона.


## Хранилище (хост Gateway)

Слова пробуждения и правила маршрутизации хранятся в базе данных состояния Gateway:

  * `~/.openclaw/state/openclaw.sqlite`


Активные таблицы:

  * `voicewake_triggers`
  * `voicewake_routing_config`
  * `voicewake_routing_routes`


Устаревшие файлы `settings/voicewake.json` и `settings/voicewake-routing.json` являются только входными данными для миграции doctor; во время выполнения чтение и запись выполняются в таблицы SQLite.

## Протокол

### Методы

  * `voicewake.get` → `{ triggers: string[] }`
  * `voicewake.set` с параметрами `{ triggers: string[] }` → `{ triggers: string[] }`


Примечания:

  * Триггеры нормализуются (обрезаются пробелы, пустые значения отбрасываются). Пустые списки откатываются к значениям по умолчанию.
  * Для безопасности применяются ограничения (лимиты количества и длины).


### Методы маршрутизации (триггер → цель)

  * `voicewake.routing.get` → `{ config: VoiceWakeRoutingConfig }`
  * `voicewake.routing.set` с параметрами `{ config: VoiceWakeRoutingConfig }` → `{ config: VoiceWakeRoutingConfig }`


Форма `VoiceWakeRoutingConfig`:

jsonCopy code
[code]
    {  "version": 1,  "defaultTarget": { "mode": "current" },  "routes": [{ "trigger": "robot wake", "target": { "sessionKey": "agent:main:main" } }],  "updatedAtMs": 1730000000000}
[/code]

Цели маршрутов поддерживают ровно один из вариантов:

  * `{ "mode": "current" }`
  * `{ "agentId": "main" }`
  * `{ "sessionKey": "agent:main:main" }`


### События

  * полезная нагрузка `voicewake.changed` `{ triggers: string[] }`
  * полезная нагрузка `voicewake.routing.changed` `{ config: VoiceWakeRoutingConfig }`


Кто получает это:

  * Все клиенты WebSocket (приложение macOS, WebChat и т. д.)
  * Все подключенные узлы (iOS/Android), а также при подключении узла как начальная отправка «текущего состояния».


## Поведение клиента

### Приложение macOS

  * Использует глобальный список для допуска триггеров `VoiceWakeRuntime`.
  * Редактирование «Слов-триггеров» в настройках Голосового пробуждения вызывает `voicewake.set`, а затем полагается на рассылку, чтобы поддерживать синхронизацию других клиентов.


### Узел iOS

  * Использует глобальный список для обнаружения триггеров `VoiceWakeManager`.
  * Редактирование слов пробуждения в настройках вызывает `voicewake.set` (через Gateway WS), а также сохраняет отзывчивость локального обнаружения слов пробуждения.


### Узел Android

  * Голосовое пробуждение сейчас отключено в среде выполнения/настройках Android.
  * Голос на Android использует ручной захват микрофона на вкладке «Голос» вместо триггеров по словам пробуждения.


## Связано

  * [Режим разговора](</ru/nodes/talk>)
  * [Аудио и голосовые заметки](</ru/nodes/audio>)
  * [Понимание медиа](</ru/nodes/media-understanding>)


Was this useful?YesNo

Open issue