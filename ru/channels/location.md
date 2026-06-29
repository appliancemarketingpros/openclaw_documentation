---
title: Разбор местоположения канала
source_url: https://docs.openclaw.ai/ru/channels/location
scraped_at: 2026-06-29
---

ChannelsConfiguration

OpenClaw нормализует общие местоположения из каналов чата в:

  * краткий текст с координатами, добавляемый к входящему телу сообщения, и
  * структурированные поля в полезной нагрузке контекста автоматического ответа. Предоставленные каналом метки, адреса и подписи/комментарии отображаются в prompt через общий JSON-блок недоверенных метаданных, а не встроенно в тело сообщения пользователя.


Сейчас поддерживаются:

  * **Telegram** (метки местоположения + места + live-местоположения)
  * **WhatsApp** (locationMessage + liveLocationMessage)
  * **Matrix** (`m.location` с `geo_uri`)


## Форматирование текста

Местоположения отображаются как понятные строки без скобок:

  * Метка: 
    * `📍 48.858844, 2.294351 ±12m`
  * Именованное место: 
    * `📍 48.858844, 2.294351 ±12m`
  * Live-геопозиция: 
    * `🛰 Live location: 48.858844, 2.294351 ±12m`


Если канал включает метку, адрес или подпись/комментарий, они сохраняются в полезной нагрузке контекста и появляются в prompt как огражденный недоверенный JSON:

textCopy code
[code]
    Location (untrusted metadata):```json{  "latitude": 48.858844,  "longitude": 2.294351,  "name": "Eiffel Tower",  "address": "Champ de Mars, Paris",  "caption": "Meet here"}```
[/code]

## Поля контекста

Когда местоположение присутствует, эти поля добавляются в `ctx`:

  * `LocationLat` (число)
  * `LocationLon` (число)
  * `LocationAccuracy` (число, метры; необязательно)
  * `LocationName` (строка; необязательно)
  * `LocationAddress` (строка; необязательно)
  * `LocationSource` (`pin | place | live`)
  * `LocationIsLive` (логическое значение)
  * `LocationCaption` (строка; необязательно)


Рендерер prompt обрабатывает `LocationName`, `LocationAddress` и `LocationCaption` как недоверенные метаданные и сериализует их через тот же ограниченный JSON-путь, который используется для другого контекста канала.

## Примечания по каналам

  * **Telegram** : места сопоставляются с `LocationName/LocationAddress`; live-местоположения используют `live_period`.
  * **WhatsApp** : `locationMessage.comment` и `liveLocationMessage.caption` заполняют `LocationCaption`.
  * **Matrix** : `geo_uri` разбирается как местоположение-метка; высота игнорируется, а `LocationIsLive` всегда false.


## Связанные материалы

  * [Команда местоположения (узлы)](</ru/nodes/location-command>)
  * [Съемка с камеры](</ru/nodes/camera>)
  * [Понимание медиа](</ru/nodes/media-understanding>)


Was this useful?YesNo

Open issue