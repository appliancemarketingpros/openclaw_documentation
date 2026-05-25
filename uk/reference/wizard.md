---
title: Довідник з онбордингу
source_url: https://docs.openclaw.ai/uk/reference/wizard
scraped_at: 2026-05-25
---

Це повний довідник для `openclaw onboard`. Для загального огляду див. [Онбординг (CLI)](</uk/start/wizard>).

## Деталі потоку (локальний режим)

* ### Виявлення наявної конфігурації

  * Якщо `~/.openclaw/openclaw.json` існує, виберіть **Зберегти поточні значення** , **Переглянути й оновити** або **Скинути перед налаштуванням**.
  * Повторний запуск онбордингу **не** видаляє нічого, якщо ви явно не виберете **Скинути** (або не передасте `--reset`).
  * CLI `--reset` типово скидає `config+creds+sessions`; використайте `--reset-scope full`, щоб також видалити робочу область.
  * Якщо конфігурація недійсна або містить застарілі ключі, майстер зупиняється й просить запустити `openclaw doctor`, перш ніж продовжити.
  * Скидання використовує `trash` (ніколи `rm`) і пропонує області: 
    * Лише конфігурація
    * Конфігурація + облікові дані + сеанси
    * Повне скидання (також видаляє робочу область)


* ### Модель/автентифікація

  * **Ключ API Anthropic** : використовує `ANTHROPIC_API_KEY`, якщо він наявний, або запитує ключ, а потім зберігає його для використання демоном.
  * **Ключ API Anthropic** : бажаний вибір асистента Anthropic в онбордингу/налаштуванні.
  * **Setup-token Anthropic** : усе ще доступний в онбордингу/налаштуванні, хоча OpenClaw тепер віддає перевагу повторному використанню Claude CLI, коли це можливо.
  * **Підписка OpenAI Code (Codex) (OAuth)** : браузерний потік; вставте `code#state`. 
    * Встановлює `agents.defaults.model` у `openai/gpt-5.5` через середовище виконання Codex, коли модель не задана або вже належить до сімейства OpenAI.
  * **Підписка OpenAI Code (Codex) (сполучення пристрою)** : браузерний потік сполучення з короткочасним кодом пристрою. 
    * Встановлює `agents.defaults.model` у `openai/gpt-5.5` через середовище виконання Codex, коли модель не задана або вже належить до сімейства OpenAI.
  * **Ключ API OpenAI** : використовує `OPENAI_API_KEY`, якщо він наявний, або запитує ключ, а потім зберігає його в профілях автентифікації. 
    * Встановлює `agents.defaults.model` у `openai/gpt-5.5`, коли модель не задана, `openai/*` або `openai-codex/*`.
  * **Ключ API xAI (Grok)** : запитує `XAI_API_KEY` і налаштовує xAI як постачальника моделей.
  * **OpenCode** : запитує `OPENCODE_API_KEY` (або `OPENCODE_ZEN_API_KEY`, отримайте його на <https://opencode.ai/auth>) і дає змогу вибрати каталог Zen або Go.
  * **Ollama** : спочатку пропонує **Хмара + локально** , **Лише хмара** або **Лише локально**. `Cloud only` запитує `OLLAMA_API_KEY` і використовує `https://ollama.com`; режими, що спираються на хост, запитують базову URL-адресу Ollama, виявляють доступні моделі та автоматично завантажують вибрану локальну модель за потреби; `Cloud + Local` також перевіряє, чи цей хост Ollama ввійшов у систему для хмарного доступу.
  * Докладніше: [Ollama](</uk/providers/ollama>)
  * **Ключ API** : зберігає ключ для вас.
  * **Vercel AI Gateway (мультимодельний проксі)** : запитує `AI_GATEWAY_API_KEY`.
  * Докладніше: [Vercel AI Gateway](</uk/providers/vercel-ai-gateway>)
  * **Cloudflare AI Gateway** : запитує Account ID, Gateway ID і `CLOUDFLARE_AI_GATEWAY_API_KEY`.
  * Докладніше: [Cloudflare AI Gateway](</uk/providers/cloudflare-ai-gateway>)
  * **MiniMax** : конфігурація записується автоматично; розміщене типове значення — `MiniMax-M2.7`. Налаштування ключа API використовує `minimax/...`, а налаштування OAuth використовує `minimax-portal/...`.
  * Докладніше: [MiniMax](</uk/providers/minimax>)
  * **StepFun** : конфігурація автоматично записується для StepFun standard або Step Plan на китайських чи глобальних кінцевих точках.
  * Standard наразі містить `step-3.5-flash`, а Step Plan також містить `step-3.5-flash-2603`.
  * Докладніше: [StepFun](</uk/providers/stepfun>)
  * **Synthetic (сумісний з Anthropic)** : запитує `SYNTHETIC_API_KEY`.
  * Докладніше: [Synthetic](</uk/providers/synthetic>)
  * **Moonshot (Kimi K2)** : конфігурація записується автоматично.
  * **Kimi Coding** : конфігурація записується автоматично.
  * Докладніше: [Moonshot AI (Kimi + Kimi Coding)](</uk/providers/moonshot>)
  * **Пропустити** : автентифікацію ще не налаштовано.
  * Виберіть типову модель із виявлених варіантів (або введіть постачальника/модель вручну). Для найкращої якості та нижчого ризику ін’єкції промптів виберіть найпотужнішу модель останнього покоління, доступну у вашому стеку постачальників.
  * Онбординг запускає перевірку моделі й попереджає, якщо налаштована модель невідома або бракує автентифікації.
  * Режим зберігання ключа API типово використовує відкритий текст у значеннях профілю автентифікації. Використайте `--secret-input-mode ref`, щоб натомість зберігати посилання, підтримані env (наприклад `keyRef: { source: "env", provider: "default", id: "OPENAI_API_KEY" }`).
  * Профілі автентифікації розміщено в `~/.openclaw/agents/<agentId>/agent/auth-profiles.json` (ключі API + OAuth). `~/.openclaw/credentials/oauth.json` є лише застарілим джерелом імпорту.
  * Докладніше: [/concepts/oauth](</uk/concepts/oauth>)


* ### Робоча область

  * Типово `~/.openclaw/workspace` (можна налаштувати).
  * Створює початкові файли робочої області, потрібні для bootstrap-ритуалу агента.
  * Повна структура робочої області + посібник із резервного копіювання: [Робоча область агента](</uk/concepts/agent-workspace>)


* ### Gateway

  * Порт, прив’язка, режим автентифікації, доступ через tailscale.
  * Рекомендація щодо автентифікації: залишайте **Token** навіть для loopback, щоб локальні клієнти WS мусили автентифікуватися.
  * У режимі token інтерактивне налаштування пропонує: 
    * **Згенерувати/зберегти plaintext token** (типово)
    * **Використати SecretRef** (за явним вибором)
    * Quickstart повторно використовує наявні SecretRef `gateway.auth.token` у постачальниках `env`, `file` і `exec` для проби онбордингу/початкового запуску dashboard.
    * Якщо цей SecretRef налаштований, але його неможливо розв’язати, онбординг завершується рано з чітким повідомленням про виправлення замість тихого погіршення runtime-автентифікації.
  * У режимі пароля інтерактивне налаштування також підтримує зберігання у plaintext або SecretRef.
  * Неінтерактивний шлях token SecretRef: `--gateway-token-ref-env &lt;ENV_VAR&gt;`. 
    * Потребує непорожньої env-змінної в середовищі процесу онбордингу.
    * Не можна поєднувати з `--gateway-token`.
  * Вимикайте автентифікацію лише якщо повністю довіряєте кожному локальному процесу.
  * Прив’язки не до loopback усе одно потребують автентифікації.


* ### Канали

  * [WhatsApp](</uk/channels/whatsapp>): необов’язковий вхід через QR.
  * [Telegram](</uk/channels/telegram>): token бота.
  * [Discord](</uk/channels/discord>): token бота.
  * [Google Chat](</uk/channels/googlechat>): JSON службового облікового запису + аудиторія webhook.
  * [Mattermost](</uk/channels/mattermost>) (Plugin): token бота + базова URL-адреса.
  * [Signal](</uk/channels/signal>): необов’язкове встановлення `signal-cli` \+ конфігурація облікового запису.
  * [iMessage](</uk/channels/imessage>): шлях до CLI `imsg` \+ доступ до БД Messages; використовуйте SSH-обгортку, коли Gateway працює не на Mac.
  * Безпека DM: типово використовується сполучення. Перший DM надсилає код; підтвердьте через `openclaw pairing approve <channel> <code>` або використайте allowlists.


* ### Вебпошук

  * Виберіть підтримуваного постачальника, як-от Brave, DuckDuckGo, Exa, Firecrawl, Gemini, Grok, Kimi, MiniMax Search, Ollama Web Search, Perplexity, SearXNG або Tavily (або пропустіть).
  * Постачальники з API можуть використовувати env-змінні або наявну конфігурацію для швидкого налаштування; постачальники без ключів натомість використовують власні передумови.
  * Пропустіть за допомогою `--skip-search`.
  * Налаштувати пізніше: `openclaw configure --section web`.


* ### Встановлення демона

  * macOS: LaunchAgent 
    * Потребує сеансу користувача, що ввійшов у систему; для headless використовуйте власний LaunchDaemon (не постачається).
  * Linux (і Windows через WSL2): systemd user unit 
    * Онбординг намагається увімкнути lingering через `loginctl enable-linger <user>`, щоб Gateway залишався запущеним після виходу.
    * Може запросити sudo (записує `/var/lib/systemd/linger`); спершу намагається без sudo.
  * **Вибір runtime:** Node (рекомендовано; потрібно для WhatsApp/Telegram). Bun **не рекомендовано**.
  * Якщо token-автентифікація потребує token і `gateway.auth.token` керується SecretRef, встановлення демона перевіряє його, але не зберігає розв’язані plaintext-значення token у метаданих середовища supervisor-сервісу.
  * Якщо token-автентифікація потребує token, а налаштований token SecretRef не розв’язано, встановлення демона блокується з практичними вказівками.
  * Якщо налаштовано і `gateway.auth.token`, і `gateway.auth.password`, а `gateway.auth.mode` не задано, встановлення демона блокується, доки режим не буде задано явно.


* ### Перевірка справності

  * Запускає Gateway (за потреби) і виконує `openclaw health`.
  * Порада: `openclaw status --deep` додає live health probe gateway до виводу status, зокрема probes каналів, коли вони підтримуються (потрібен доступний gateway).


* ### Skills (рекомендовано)

  * Зчитує доступні Skills і перевіряє вимоги.
  * Дає змогу вибрати менеджер node: **npm / pnpm** (bun не рекомендовано).
  * Встановлює необов’язкові залежності (деякі використовують Homebrew на macOS).


* ### Завершення

  * Підсумок + наступні кроки, зокрема запит **Як ви хочете вилупити свого агента?** для Terminal, Browser або пізніше.


## Неінтерактивний режим

Використайте `--non-interactive`, щоб автоматизувати або скриптувати онбординг:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice apiKey \  --anthropic-api-key "$ANTHROPIC_API_KEY" \  --gateway-port 18789 \  --gateway-bind loopback \  --install-daemon \  --daemon-runtime node \  --skip-skills
[/code]

Додайте `--json` для машинозчитуваного підсумку.

Gateway token SecretRef у неінтерактивному режимі:

bashCopy code
[code]
    export OPENCLAW_GATEWAY_TOKEN="your-token"openclaw onboard --non-interactive \  --mode local \  --auth-choice skip \  --gateway-auth token \  --gateway-token-ref-env OPENCLAW_GATEWAY_TOKEN
[/code]

`--gateway-token` і `--gateway-token-ref-env` є взаємовиключними.

Приклади команд для конкретних постачальників наведено в [Автоматизації CLI](</uk/start/wizard-cli-automation#provider-specific-examples>). Використовуйте цю довідкову сторінку для семантики прапорців і порядку кроків.

### Додати агента (неінтерактивно)

bashCopy code
[code]
    openclaw agents add work \  --workspace ~/.openclaw/workspace-work \  --model openai/gpt-5.5 \  --bind whatsapp:biz \  --non-interactive \  --json
[/code]

## RPC майстра Gateway

Gateway надає потік онбордингу через RPC (`wizard.start`, `wizard.next`, `wizard.cancel`, `wizard.status`). Клієнти (застосунок macOS, Control UI) можуть рендерити кроки без повторної реалізації логіки онбордингу.

## Налаштування Signal (signal-cli)

Онбординг може встановити `signal-cli` з GitHub releases:

  * Завантажує відповідний release asset.
  * Зберігає його в `~/.openclaw/tools/signal-cli/<version>/`.
  * Записує `channels.signal.cliPath` у вашу конфігурацію.


Примітки:

  * JVM-збірки потребують **Java 21**.
  * Native-збірки використовуються, коли доступні.
  * Windows використовує WSL2; встановлення signal-cli відбувається за Linux-потоком усередині WSL.


## Що записує майстер

Типові поля в `~/.openclaw/openclaw.json`:

  * `agents.defaults.workspace`
  * `agents.defaults.model` / `models.providers` (якщо вибрано Minimax)
  * `tools.profile` (локальне початкове налаштування за замовчуванням використовує `"coding"`, якщо не задано; наявні явні значення зберігаються)
  * `gateway.*` (mode, bind, auth, tailscale)
  * `session.dmScope` (деталі поведінки: [Довідник із налаштування CLI](</uk/start/wizard-cli-reference#outputs-and-internals>))
  * `channels.telegram.botToken`, `channels.discord.token`, `channels.matrix.*`, `channels.signal.*`, `channels.imessage.*`
  * Списки дозволених каналів (Slack/Discord/Matrix/Microsoft Teams), коли ви погоджуєтеся під час підказок (імена за можливості перетворюються на ID).
  * `skills.install.nodeManager`
    * `setup --node-manager` приймає `npm`, `pnpm` або `bun`.
    * Ручна конфігурація все ще може використовувати `yarn`, якщо задати `skills.install.nodeManager` напряму.
  * `wizard.lastRunAt`
  * `wizard.lastRunVersion`
  * `wizard.lastRunCommit`
  * `wizard.lastRunCommand`
  * `wizard.lastRunMode`


`openclaw agents add` записує `agents.list[]` і необов’язкові `bindings`.

Облікові дані WhatsApp розміщуються в `~/.openclaw/credentials/whatsapp/<accountId>/`. Сеанси зберігаються в `~/.openclaw/agents/<agentId>/sessions/`.

Деякі канали постачаються як plugins. Коли ви вибираєте один із них під час налаштування, onboarding запропонує встановити його (npm або локальний шлях), перш ніж його можна буде налаштувати.

## Пов’язані документи

  * Огляд початкового налаштування: [Початкове налаштування (CLI)](</uk/start/wizard>)
  * Початкове налаштування застосунку macOS: [Початкове налаштування](</uk/start/onboarding>)
  * Довідник конфігурації: [Конфігурація Gateway](</uk/gateway/configuration>)
  * Провайдери: [WhatsApp](</uk/channels/whatsapp>), [Telegram](</uk/channels/telegram>), [Discord](</uk/channels/discord>), [Google Chat](</uk/channels/googlechat>), [Signal](</uk/channels/signal>), [iMessage](</uk/channels/imessage>)
  * Skills: [Skills](</uk/tools/skills>), [Конфігурація Skills](</uk/tools/skills-config>)


Was this useful?YesNo