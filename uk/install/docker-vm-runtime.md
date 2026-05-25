---
title: Середовище виконання віртуальної машини Docker
source_url: https://docs.openclaw.ai/uk/install/docker-vm-runtime
scraped_at: 2026-05-25
---

Спільні кроки середовища виконання для встановлень Docker на основі віртуальних машин, таких як GCP, Hetzner та подібні постачальники VPS.

## Вбудуйте потрібні бінарні файли в образ

Встановлення бінарних файлів усередині запущеного контейнера — пастка. Усе, що встановлено під час виконання, буде втрачено після перезапуску.

Усі зовнішні бінарні файли, потрібні для Skills, мають бути встановлені під час збирання образу.

Наведені нижче приклади показують лише три поширені бінарні файли:

  * `gog` (з `gogcli`) для доступу до Gmail
  * `goplaces` для Google Places
  * `wacli` для WhatsApp


Це приклади, а не повний список. Ви можете встановити стільки бінарних файлів, скільки потрібно, використовуючи той самий шаблон.

Якщо згодом ви додасте нові Skills, які залежать від додаткових бінарних файлів, потрібно:

  1. Оновити Dockerfile
  2. Перезібрати образ
  3. Перезапустити контейнери


**Приклад Dockerfile**

dockerfileCopy code
[code]
    FROM node:24-bookworm RUN apt-get update && apt-get install -y socat && rm -rf /var/lib/apt/lists/* # Example binary 1: Gmail CLI (gogcli — installs as `gog`)# Copy the current Linux asset URL from https://github.com/steipete/gogcli/releasesRUN curl -L https://github.com/steipete/gogcli/releases/latest/download/gogcli_linux_amd64.tar.gz \  | tar -xzO gog > /usr/local/bin/gog; \  chmod +x /usr/local/bin/gog # Example binary 2: Google Places CLI# Copy the current Linux asset URL from https://github.com/steipete/goplaces/releasesRUN curl -L https://github.com/steipete/goplaces/releases/latest/download/goplaces_linux_amd64.tar.gz \  | tar -xzO goplaces > /usr/local/bin/goplaces; \  chmod +x /usr/local/bin/goplaces # Example binary 3: WhatsApp CLI# Copy the current Linux asset URL from https://github.com/steipete/wacli/releasesRUN curl -L https://github.com/steipete/wacli/releases/latest/download/wacli-linux-amd64.tar.gz \  | tar -xzO wacli > /usr/local/bin/wacli; \  chmod +x /usr/local/bin/wacli # Add more binaries below using the same pattern WORKDIR /appCOPY package.json pnpm-lock.yaml pnpm-workspace.yaml .npmrc ./COPY ui/package.json ./ui/package.jsonCOPY scripts ./scripts RUN corepack enableRUN pnpm install --frozen-lockfile COPY . .RUN pnpm buildRUN pnpm ui:installRUN pnpm ui:build ENV NODE_ENV=production CMD ["node","dist/index.js"]
[/code]

## Збирання та запуск

bashCopy code
[code]
    docker compose builddocker compose up -d openclaw-gateway
[/code]

Якщо збирання завершується помилкою `Killed` або `exit code 137` під час `pnpm install --frozen-lockfile`, на віртуальній машині бракує пам’яті. Перед повторною спробою використайте більший клас машини.

Перевірте бінарні файли:

bashCopy code
[code]
    docker compose exec openclaw-gateway which gogdocker compose exec openclaw-gateway which goplacesdocker compose exec openclaw-gateway which wacli
[/code]

Очікуваний вивід:

CodeCopy code
[code]
    /usr/local/bin/gog/usr/local/bin/goplaces/usr/local/bin/wacli
[/code]

Перевірте Gateway:

bashCopy code
[code]
    docker compose logs -f openclaw-gateway
[/code]

Очікуваний вивід:

CodeCopy code
[code]
    [gateway] listening on ws://0.0.0.0:18789
[/code]

## Що де зберігається

OpenClaw працює в Docker, але Docker не є джерелом істини. Увесь довготривалий стан має переживати перезапуски, перезбирання та перезавантаження.

Компонент | Розташування | Механізм збереження | Примітки  
---|---|---|---  
Конфігурація Gateway | `/home/node/.openclaw/` | Монтування тому хоста | Містить `openclaw.json`, `.env`  
Профілі автентифікації моделей | `/home/node/.openclaw/agents/` | Монтування тому хоста | `agents/<agentId>/agent/auth-profiles.json` (OAuth, ключі API)  
Ключ профілю автентифікації | `/home/node/.config/openclaw/` | Монтування тому хоста | Локальний ключ шифрування для матеріалу токенів профілю автентифікації OAuth  
Конфігурації Skills | `/home/node/.openclaw/skills/` | Монтування тому хоста | Стан на рівні Skill  
Робочий простір агента | `/home/node/.openclaw/workspace/` | Монтування тому хоста | Код і артефакти агента  
Сесія WhatsApp | `/home/node/.openclaw/` | Монтування тому хоста | Зберігає вхід через QR  
Сховище ключів Gmail | `/home/node/.openclaw/` | Том хоста + пароль | Потребує `GOG_KEYRING_PASSWORD`  
Пакети Plugin | `/home/node/.openclaw/npm`, `/home/node/.openclaw/git` | Монтування тому хоста | Корені завантажуваних пакетів Plugin  
Зовнішні бінарні файли | `/usr/local/bin/` | Образ Docker | Мають бути вбудовані під час збирання  
Середовище виконання Node | Файлова система контейнера | Образ Docker | Перезбирається під час кожного збирання образу  
Пакети ОС | Файлова система контейнера | Образ Docker | Не встановлюйте під час виконання  
Контейнер Docker | Тимчасовий | Можна перезапустити | Безпечно знищувати  
  
## Оновлення

Щоб оновити OpenClaw на віртуальній машині:

bashCopy code
[code]
    git pulldocker compose builddocker compose up -d
[/code]

## Пов’язане

  * [Docker](</uk/install/docker>)
  * [Podman](</uk/install/podman>)
  * [ClawDock](</uk/install/clawdock>)


Was this useful?YesNo