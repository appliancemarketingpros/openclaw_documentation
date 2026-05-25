---
title: Початок роботи
source_url: https://docs.openclaw.ai/uk/cli/onboard
scraped_at: 2026-05-25
---

# `openclaw onboard`

Повний керований онбординг для налаштування локального або віддаленого Gateway. Використовуйте це, коли хочете, щоб OpenClaw провів через автентифікацію моделі, робочий простір, Gateway, канали, Skills і перевірку справності в одному потоці.

## Пов’язані посібники

[**Центр онбордингу CLI** Покроковий опис інтерактивного потоку CLI. ](</uk/start/wizard>) [**Огляд онбордингу** Як онбординг OpenClaw поєднується в єдине ціле. ](</uk/start/onboarding-overview>) [**Довідник налаштування CLI** Вивід, внутрішня логіка та поведінка кожного кроку. ](</uk/start/wizard-cli-reference>) [**Автоматизація CLI** Неінтерактивні прапорці та скриптові налаштування. ](</uk/start/wizard-cli-automation>) [**Онбординг застосунку macOS** Потік онбордингу для застосунку в рядку меню macOS. ](</uk/start/onboarding>)

## Приклади

bashCopy code
[code]
    openclaw onboardopenclaw onboard --modernopenclaw onboard --flow quickstartopenclaw onboard --flow manualopenclaw onboard --flow importopenclaw onboard --import-from hermes --import-source ~/.hermesopenclaw onboard --skip-bootstrapopenclaw onboard --mode remote --remote-url wss://gateway-host:18789
[/code]

`--flow import` використовує постачальники міграції, що належать плагінам, наприклад Hermes. Він запускається лише для нового налаштування OpenClaw; якщо вже наявні конфігурація, облікові дані, сеанси або файли пам’яті/ідентичності робочого простору, перед імпортом скиньте їх або виберіть нове налаштування.

`--modern` запускає попередню версію розмовного онбордингу Crestodian. Без `--modern` команда `openclaw onboard` зберігає класичний потік онбордингу.

Для plaintext-цілей `ws://` у приватній мережі (лише довірені мережі) задайте `OPENCLAW_ALLOW_INSECURE_PRIVATE_WS=1` у середовищі процесу онбордингу. Еквівалента в `openclaw.json` для цього аварійного обходу клієнтського транспорту немає.

Неінтерактивний користувацький постачальник:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice custom-api-key \  --custom-base-url "https://llm.example.com/v1" \  --custom-model-id "foo-large" \  --custom-api-key "$CUSTOM_API_KEY" \  --secret-input-mode plaintext \  --custom-compatibility openai \  --custom-image-input
[/code]

`--custom-api-key` є необов’язковим у неінтерактивному режимі. Якщо його пропущено, онбординг перевіряє `CUSTOM_API_KEY`. OpenClaw автоматично позначає поширені ідентифікатори моделей зору як такі, що підтримують зображення. Передайте `--custom-image-input` для невідомих користувацьких ідентифікаторів моделей зору або `--custom-text-input`, щоб примусово задати метадані лише для тексту.

LM Studio також підтримує прапорець ключа, специфічний для постачальника, у неінтерактивному режимі:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice lmstudio \  --custom-base-url "http://localhost:1234/v1" \  --custom-model-id "qwen/qwen3.5-9b" \  --lmstudio-api-key "$LM_API_TOKEN" \  --accept-risk
[/code]

Неінтерактивний Ollama:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice ollama \  --custom-base-url "http://ollama-host:11434" \  --custom-model-id "qwen3.5:27b" \  --accept-risk
[/code]

`--custom-base-url` за замовчуванням має значення `http://127.0.0.1:11434`. `--custom-model-id` є необов’язковим; якщо його пропущено, онбординг використовує рекомендовані Ollama значення за замовчуванням. Тут також працюють ідентифікатори хмарних моделей, наприклад `kimi-k2.5:cloud`.

Зберігайте ключі постачальника як посилання замість plaintext:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice openai-api-key \  --secret-input-mode ref \  --accept-risk
[/code]

З `--secret-input-mode ref` онбординг записує посилання на основі змінних середовища замість plaintext-значень ключів. Для постачальників на основі auth-profile це записує записи `keyRef`; для користувацьких постачальників це записує `models.providers.<id>.apiKey` як env-посилання (наприклад `{ source: "env", provider: "default", id: "CUSTOM_API_KEY" }`).

Контракт неінтерактивного режиму `ref`:

  * Задайте змінну середовища постачальника в середовищі процесу онбордингу (наприклад `OPENAI_API_KEY`).
  * Не передавайте inline-прапорці ключів (наприклад `--openai-api-key`), якщо ця змінна середовища також не задана.
  * Якщо inline-прапорець ключа передано без потрібної змінної середовища, онбординг швидко завершується помилкою з підказками.


Параметри токена Gateway у неінтерактивному режимі:

  * `--gateway-auth token --gateway-token <token>` зберігає plaintext-токен.
  * `--gateway-auth token --gateway-token-ref-env <name>` зберігає `gateway.auth.token` як env SecretRef.
  * `--gateway-token` і `--gateway-token-ref-env` взаємовиключні.
  * `--gateway-token-ref-env` вимагає непорожню змінну середовища в середовищі процесу онбордингу.
  * З `--install-daemon`, коли автентифікація токеном вимагає токен, токени Gateway, керовані SecretRef, перевіряються, але не зберігаються як розв’язаний plaintext у метаданих середовища служби супервізора.
  * З `--install-daemon`, якщо режим токена вимагає токен, а налаштований SecretRef токена не розв’язується, онбординг завершується відмовою із вказівками для виправлення.
  * З `--install-daemon`, якщо налаштовано і `gateway.auth.token`, і `gateway.auth.password`, а `gateway.auth.mode` не задано, онбординг блокує встановлення, доки режим не буде задано явно.
  * Локальний онбординг записує `gateway.mode="local"` у конфігурацію. Якщо в пізнішому файлі конфігурації відсутній `gateway.mode`, розглядайте це як пошкодження конфігурації або незавершене ручне редагування, а не як коректний скорочений шлях локального режиму.
  * Локальний онбординг встановлює вибрані завантажувані плагіни, коли вибраний шлях налаштування цього потребує.
  * Віддалений онбординг записує лише відомості про підключення до віддаленого Gateway і не встановлює локальні пакети плагінів.
  * `--allow-unconfigured` є окремим аварійним механізмом часу виконання Gateway. Він не означає, що онбординг може пропустити `gateway.mode`.


Приклад:

bashCopy code
[code]
    export OPENCLAW_GATEWAY_TOKEN="your-token"openclaw onboard --non-interactive \  --mode local \  --auth-choice skip \  --gateway-auth token \  --gateway-token-ref-env OPENCLAW_GATEWAY_TOKEN \  --accept-risk
[/code]

Неінтерактивна перевірка справності локального Gateway:

  * Якщо ви не передаєте `--skip-health`, онбординг чекає, доки локальний Gateway стане доступним, перш ніж успішно завершитися.
  * `--install-daemon` спочатку запускає шлях встановлення керованого Gateway. Без нього локальний Gateway має вже бути запущений, наприклад `openclaw gateway run`.
  * Якщо в автоматизації вам потрібні лише записи конфігурації/робочого простору/bootstrap, використовуйте `--skip-health`.
  * Якщо ви самостійно керуєте файлами робочого простору, передайте `--skip-bootstrap`, щоб задати `agents.defaults.skipBootstrap: true` і пропустити створення `AGENTS.md`, `SOUL.md`, `TOOLS.md`, `IDENTITY.md`, `USER.md`, `HEARTBEAT.md` і `BOOTSTRAP.md`.
  * У нативній Windows `--install-daemon` спочатку пробує Scheduled Tasks і, якщо створення завдання заборонено, повертається до login item у Startup-folder для поточного користувача.


Поведінка інтерактивного онбордингу в режимі посилань:

  * Виберіть **Використати secret reference** , коли з’явиться запит.
  * Потім виберіть одне з: 
    * Змінна середовища
    * Налаштований постачальник секретів (`file` або `exec`)
  * Онбординг виконує швидку попередню перевірку перед збереженням посилання. 
    * Якщо перевірка не проходить, онбординг показує помилку й дає змогу повторити спробу.


### Неінтерактивний вибір кінцевих точок [Z.AI](<http://Z.AI>)

bashCopy code
[code]
    # Promptless endpoint selectionopenclaw onboard --non-interactive \  --auth-choice zai-coding-global \  --zai-api-key "$ZAI_API_KEY" # Other Z.AI endpoint choices:# --auth-choice zai-coding-cn# --auth-choice zai-global# --auth-choice zai-cn
[/code]

Неінтерактивний приклад Mistral:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice mistral-api-key \  --mistral-api-key "$MISTRAL_API_KEY"
[/code]

## Примітки до потоку

Типи потоків

  * `quickstart`: мінімальні запити, автоматично генерує токен Gateway.
  * `manual`: повні запити для порту, bind і автентифікації (псевдонім `advanced`).
  * `import`: запускає виявленого постачальника міграції, попередньо показує план, а потім застосовує його після підтвердження.

Попередня фільтрація постачальників

Коли вибір автентифікації передбачає бажаного постачальника, онбординг попередньо фільтрує вибірники моделі за замовчуванням і allowlist до цього постачальника. Для Volcengine і BytePlus це також зіставляє варіанти coding-plan (`volcengine-plan/*`, `byteplus-plan/*`).

Якщо фільтр бажаного постачальника ще не дає завантажених моделей, онбординг повертається до нефільтрованого каталогу замість того, щоб залишати вибірник порожнім.

Подальші запити web-search

Деякі постачальники web-search запускають подальші запити, специфічні для постачальника:

  * **Grok** може запропонувати необов’язкове налаштування `x_search` з тим самим `XAI_API_KEY` і вибором моделі `x_search`.
  * **Kimi** може попросити регіон Moonshot API (`api.moonshot.ai` або `api.moonshot.cn`) і модель Kimi web-search за замовчуванням.

Інша поведінка

  * Поведінка DM-області локального онбордингу: [довідник налаштування CLI](</uk/start/wizard-cli-reference#outputs-and-internals>).
  * Найшвидший перший чат: `openclaw dashboard` (інтерфейс керування, без налаштування каналу).
  * Користувацький постачальник: підключіть будь-яку кінцеву точку, сумісну з OpenAI або Anthropic, включно з розміщеними постачальниками, яких немає в списку. Використовуйте Unknown для автоматичного виявлення.
  * Якщо виявлено стан Hermes, онбординг пропонує потік міграції. Використовуйте [Migrate](</uk/cli/migrate>) для планів dry-run, режиму перезапису, звітів і точних зіставлень.


## Поширені наступні команди

bashCopy code
[code]
    openclaw channels addopenclaw configureopenclaw agents add <name>
[/code]

Натомість використовуйте `openclaw setup`, коли вам потрібна лише базова конфігурація/робочий простір. Використовуйте `openclaw configure` пізніше для цільових змін і `openclaw channels add` для налаштування лише каналів.

Was this useful?YesNo