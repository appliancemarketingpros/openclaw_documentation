---
title: Полотно
source_url: https://docs.openclaw.ai/uk/platforms/mac/canvas
scraped_at: 2026-05-25
---

Застосунок macOS вбудовує керовану агентом **панель Canvas** за допомогою `WKWebView`. Це легка візуальна робоча область для HTML/CSS/JS, A2UI та невеликих інтерактивних поверхонь інтерфейсу.

## Де розміщено Canvas

Стан Canvas зберігається в Application Support:

  * `~/Library/Application Support/OpenClaw/canvas/<session>/...`


Панель Canvas обслуговує ці файли через **власну URL-схему** :

  * `openclaw-canvas://<session>/<path>`


Приклади:

  * `openclaw-canvas://main/` → `<canvasRoot>/main/index.html`
  * `openclaw-canvas://main/assets/app.css` → `<canvasRoot>/main/assets/app.css`
  * `openclaw-canvas://main/widgets/todo/` → `<canvasRoot>/main/widgets/todo/index.html`


Якщо в корені немає `index.html`, застосунок показує **вбудовану сторінку-заготовку**.

## Поведінка панелі

  * Безрамкова панель зі змінним розміром, прив’язана біля рядка меню (або курсора миші).
  * Запам’ятовує розмір і позицію для кожної сесії.
  * Автоматично перезавантажується, коли локальні файли Canvas змінюються.
  * Одночасно видима лише одна панель Canvas (сесія перемикається за потреби).


Canvas можна вимкнути в Налаштування → **Дозволити Canvas**. Коли його вимкнено, команди вузлів canvas повертають `CANVAS_DISABLED`.

## Поверхня API агента

Canvas доступний через **Gateway WebSocket** , тому агент може:

  * показувати/приховувати панель
  * переходити до шляху або URL
  * виконувати JavaScript
  * захоплювати зображення знімка


Приклади CLI:

bashCopy code
[code]
    openclaw nodes canvas present --node <id>openclaw nodes canvas navigate --node <id> --url "/"openclaw nodes canvas eval --node <id> --js "document.title"openclaw nodes canvas snapshot --node <id>
[/code]

Примітки:

  * `canvas.navigate` приймає **локальні шляхи Canvas** , URL `http(s)` і URL `file://`.
  * Якщо передати `"/"`, Canvas показує локальну заготовку або `index.html`.


## A2UI у Canvas

A2UI розміщується хостом canvas у Gateway і відтворюється всередині панелі Canvas. Коли Gateway оголошує хост Canvas, застосунок macOS автоматично переходить на сторінку хоста A2UI під час першого відкриття.

Стандартний URL хоста A2UI:

CodeCopy code
[code]
    http://<gateway-host>:18789/__openclaw__/a2ui/
[/code]

### Команди A2UI (v0.8)

Зараз Canvas приймає повідомлення сервер→клієнт **A2UI v0.8** :

  * `beginRendering`
  * `surfaceUpdate`
  * `dataModelUpdate`
  * `deleteSurface`


`createSurface` (v0.9) не підтримується.

Приклад CLI:

bashCopy code
[code]
    cat > /tmp/a2ui-v0.8.jsonl <<'EOFA2'{"surfaceUpdate":{"surfaceId":"main","components":[{"id":"root","component":{"Column":{"children":{"explicitList":["title","content"]}}}},{"id":"title","component":{"Text":{"text":{"literalString":"Canvas (A2UI v0.8)"},"usageHint":"h1"}}},{"id":"content","component":{"Text":{"text":{"literalString":"If you can read this, A2UI push works."},"usageHint":"body"}}}]}}{"beginRendering":{"surfaceId":"main","root":"root"}}EOFA2 openclaw nodes canvas a2ui push --jsonl /tmp/a2ui-v0.8.jsonl --node <id>
[/code]

Швидка перевірка:

bashCopy code
[code]
    openclaw nodes canvas a2ui push --node <id> --text "Hello from A2UI"
[/code]

## Запуск виконань агента з Canvas

Canvas може запускати нові виконання агента через глибокі посилання:

  * `openclaw://agent?...`


Приклад (у JS):

jsCopy code
[code]
    window.location.href = "openclaw://agent?message=Review%20this%20design";
[/code]

Застосунок просить підтвердження, якщо не надано дійсний ключ.

## Примітки щодо безпеки

  * Схема Canvas блокує обхід каталогів; файли мають бути розміщені в корені сесії.
  * Локальний вміст Canvas використовує власну схему (loopback-сервер не потрібен).
  * Зовнішні URL `http(s)` дозволені лише після явного переходу.


## Пов’язане

  * [застосунок macOS](</uk/platforms/macos>)
  * [WebChat](</uk/web/webchat>)


Was this useful?YesNo