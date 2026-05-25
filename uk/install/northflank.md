---
title: Northflank
source_url: https://docs.openclaw.ai/uk/install/northflank
scraped_at: 2026-05-25
---

# Northflank

Розгорніть OpenClaw на Northflank за допомогою шаблону one-click і отримайте доступ через вебінтерфейс Control UI. Це найпростіший шлях "без термінала на сервері": Northflank запускає Gateway за вас.

## Як почати

  1. Натисніть [Deploy OpenClaw](<https://northflank.com/stacks/deploy-openclaw>), щоб відкрити шаблон.
  2. Створіть [обліковий запис на Northflank](<https://app.northflank.com/signup>), якщо у вас його ще немає.
  3. Натисніть **Deploy OpenClaw now**.
  4. Задайте обов’язкову змінну середовища: `OPENCLAW_GATEWAY_TOKEN` (використайте надійне випадкове значення).
  5. Натисніть **Deploy stack** , щоб зібрати і запустити шаблон OpenClaw.
  6. Дочекайтеся завершення розгортання, потім натисніть **View resources**.
  7. Відкрийте сервіс OpenClaw.
  8. Відкрийте публічний URL OpenClaw за адресою `/openclaw` і підключіться, використовуючи налаштований спільний секрет. Цей шаблон типово використовує `OPENCLAW_GATEWAY_TOKEN`; якщо ви заміните його на автентифікацію за паролем, використовуйте натомість цей пароль.


## Що ви отримуєте

  * Розміщений OpenClaw Gateway + Control UI
  * Постійне сховище через Northflank Volume (`/data`), тож `openclaw.json`, `auth-profiles.json` для кожного агента, стан каналу/провайдера, сесії та робочий простір зберігаються після повторних розгортань


## Підключення каналу

Використовуйте Control UI за адресою `/openclaw` або запустіть `openclaw onboard` через SSH, щоб отримати інструкції з налаштування каналу:

  * [Telegram](</uk/channels/telegram>) (найшвидше — потрібен лише токен бота)
  * [Discord](</uk/channels/discord>)
  * [All channels](</uk/channels>)


## Подальші кроки

  * Налаштуйте канали обміну повідомленнями: [Channels](</uk/channels>)
  * Налаштуйте Gateway: [Gateway configuration](</uk/gateway/configuration>)
  * Підтримуйте OpenClaw в актуальному стані: [Updating](</uk/install/updating>)


Was this useful?YesNo