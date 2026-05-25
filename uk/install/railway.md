---
title: Railway
source_url: https://docs.openclaw.ai/uk/install/railway
scraped_at: 2026-05-25
---

# Railway

Розгорніть OpenClaw на Railway за допомогою шаблону one-click і отримайте доступ до нього через вебінтерфейс Control UI. Це найпростіший шлях «без термінала на сервері»: Railway запускає Gateway за вас.

## Швидкий контрольний список (для нових користувачів)

  1. Натисніть **Deploy on Railway** (нижче).
  2. Додайте **Volume** , змонтований у `/data`.
  3. Задайте потрібні **Variables** (щонайменше `OPENCLAW_GATEWAY_PORT` і `OPENCLAW_GATEWAY_TOKEN`).
  4. Увімкніть **HTTP Proxy** на порті `8080`.
  5. Відкрийте `https://<your-railway-domain>/openclaw` і підключіться, використовуючи налаштований спільний секрет. Цей шаблон типово використовує `OPENCLAW_GATEWAY_TOKEN`; якщо ви заміните його на автентифікацію паролем, використовуйте натомість цей пароль.


## Розгортання one-click

[ Deploy on Railway ](<https://railway.com/deploy/clawdbot-railway-template>)

Після розгортання знайдіть свій публічний URL у **Railway → your service → Settings → Domains**.

Railway або:

  * надасть вам згенерований домен (часто `https://<something>.up.railway.app`), або
  * використовуватиме ваш власний домен, якщо ви його підключили.


Потім відкрийте:

  * `https://<your-railway-domain>/openclaw` — Control UI


## Що ви отримаєте

  * Хостинговий Gateway OpenClaw + Control UI
  * Постійне сховище через Railway Volume (`/data`), щоб `openclaw.json`, `auth-profiles.json` для кожного агента, стан каналів/провайдерів, сесії та робочий простір зберігалися після повторних розгортань


## Обов’язкові налаштування Railway

### Публічна мережа

Увімкніть **HTTP Proxy** для сервісу.

  * Порт: `8080`


### Volume (обов’язково)

Підключіть volume, змонтований у:

  * `/data`


### Variables

Задайте ці variables для сервісу:

  * `OPENCLAW_GATEWAY_PORT=8080` (обов’язково — має збігатися з портом у Public Networking)
  * `OPENCLAW_GATEWAY_TOKEN` (обов’язково; розглядайте як секрет адміністратора)
  * `OPENCLAW_STATE_DIR=/data/.openclaw` (рекомендовано)
  * `OPENCLAW_WORKSPACE_DIR=/data/workspace` (рекомендовано)


## Підключення каналу

Скористайтеся Control UI за адресою `/openclaw` або запустіть `openclaw onboard` через shell Railway, щоб отримати інструкції з налаштування каналу:

  * [Telegram](</uk/channels/telegram>) (найшвидше — потрібен лише токен бота)
  * [Discord](</uk/channels/discord>)
  * [Усі канали](</uk/channels>)


## Резервні копії та міграція

Експортуйте свій стан, конфігурацію, auth profiles і робочий простір:

bashCopy code
[code]
    openclaw backup create
[/code]

Це створить переносний архів резервної копії зі станом OpenClaw і будь-яким налаштованим робочим простором. Докладніше див. у [Backup](</uk/cli/backup>).

## Наступні кроки

  * Налаштуйте канали обміну повідомленнями: [Channels](</uk/channels>)
  * Налаштуйте Gateway: [Конфігурація Gateway](</uk/gateway/configuration>)
  * Підтримуйте OpenClaw в актуальному стані: [Оновлення](</uk/install/updating>)


Was this useful?YesNo