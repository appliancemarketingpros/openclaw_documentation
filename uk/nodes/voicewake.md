---
title: Голосове пробудження
source_url: https://docs.openclaw.ai/uk/nodes/voicewake
scraped_at: 2026-05-25
---

OpenClaw розглядає **слова пробудження як єдиний глобальний список** , яким володіє **Gateway**.

  * **Немає користувацьких слів пробудження для окремих вузлів**.
  * **Будь-який інтерфейс вузла/застосунку може редагувати** список; зміни зберігаються Gateway і транслюються всім.
  * macOS та iOS зберігають локальні перемикачі **увімкнення/вимкнення голосового пробудження** (локальний UX і дозволи відрізняються).
  * Android зараз тримає голосове пробудження вимкненим і використовує ручний мікрофонний потік у вкладці Voice.


## Сховище (хост Gateway)

Слова пробудження зберігаються на машині шлюзу за адресою:

  * `~/.openclaw/settings/voicewake.json`


Форма:

jsonCopy code
[code]
    { "triggers": ["openclaw", "claude", "computer"], "updatedAtMs": 1730000000000 }
[/code]

## Протокол

### Методи

  * `voicewake.get` → `{ triggers: string[] }`
  * `voicewake.set` з параметрами `{ triggers: string[] }` → `{ triggers: string[] }`


Примітки:

  * Тригери нормалізуються (обрізаються пробіли, порожні значення відкидаються). Порожні списки повертаються до значень за замовчуванням.
  * Для безпеки застосовуються обмеження (ліміти кількості/довжини).


### Методи маршрутизації (тригер → ціль)

  * `voicewake.routing.get` → `{ config: VoiceWakeRoutingConfig }`
  * `voicewake.routing.set` з параметрами `{ config: VoiceWakeRoutingConfig }` → `{ config: VoiceWakeRoutingConfig }`


Форма `VoiceWakeRoutingConfig`:

jsonCopy code
[code]
    {  "version": 1,  "defaultTarget": { "mode": "current" },  "routes": [{ "trigger": "robot wake", "target": { "sessionKey": "agent:main:main" } }],  "updatedAtMs": 1730000000000}
[/code]

Цілі маршрутів підтримують рівно один із варіантів:

  * `{ "mode": "current" }`
  * `{ "agentId": "main" }`
  * `{ "sessionKey": "agent:main:main" }`


### Події

  * корисне навантаження `voicewake.changed` `{ triggers: string[] }`
  * корисне навантаження `voicewake.routing.changed` `{ config: VoiceWakeRoutingConfig }`


Хто отримує:

  * Усі клієнти WebSocket (застосунок macOS, WebChat тощо)
  * Усі підключені вузли (iOS/Android), а також під час підключення вузла як початкове надсилання "поточного стану".


## Поведінка клієнтів

### Застосунок macOS

  * Використовує глобальний список для фільтрації тригерів `VoiceWakeRuntime`.
  * Редагування "Слова-тригери" в налаштуваннях голосового пробудження викликає `voicewake.set`, а потім покладається на трансляцію, щоб інші клієнти залишалися синхронізованими.


### Вузол iOS

  * Використовує глобальний список для виявлення тригерів `VoiceWakeManager`.
  * Редагування слів пробудження в налаштуваннях викликає `voicewake.set` (через Gateway WS), а також підтримує локальне виявлення слів пробудження чутливим до змін.


### Вузол Android

  * Голосове пробудження зараз вимкнене в середовищі виконання/налаштуваннях Android.
  * Голос в Android використовує ручне захоплення мікрофона у вкладці Voice замість тригерів за словами пробудження.


## Пов’язане

  * [Режим розмови](</uk/nodes/talk>)
  * [Аудіо та голосові нотатки](</uk/nodes/audio>)
  * [Розуміння медіа](</uk/nodes/media-understanding>)


Was this useful?YesNo