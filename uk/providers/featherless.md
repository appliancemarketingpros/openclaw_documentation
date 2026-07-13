---
title: Featherless AI
source_url: https://docs.openclaw.ai/uk/providers/featherless
scraped_at: 2026-07-13
---

ModelsProviders

[Featherless AI](<https://featherless.ai>) надає відкриті моделі через API, сумісний з OpenAI. OpenClaw установлює Featherless як офіційний зовнішній Plugin постачальника й зберігає вбудований каталог невеликим, водночас приймаючи точні ідентифікатори моделей Featherless під час виконання.

Властивість | Значення  
---|---  
Ідентифікатор постачальника | `featherless`  
Пакет | `@openclaw/featherless-provider`  
Змінна середовища автентифікації | `FEATHERLESS_API_KEY`  
Прапорець початкового налаштування | `--auth-choice featherless-api-key`  
Прямий прапорець CLI | `--featherless-api-key <key>`  
API | Сумісний з OpenAI (`openai-completions`)  
Базова URL-адреса | `https://api.featherless.ai/v1`  
Модель за замовчуванням | `featherless/Qwen/Qwen3-32B`  
  
## Налаштування

Установіть Plugin і перезапустіть Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/featherless-provideropenclaw gateway restart
[/code]

Запустіть початкове налаштування:

bashCopy code
[code]
    openclaw onboard --auth-choice featherless-api-key
[/code]

Для неінтерактивного налаштування:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice featherless-api-key \  --featherless-api-key "$FEATHERLESS_API_KEY"
[/code]

Або надайте ключ процесу Gateway:

bashCopy code
[code]
    export FEATHERLESS_API_KEY="<your-featherless-api-key>" # pragma: allowlist secret
[/code]

Перевірте постачальника:

bashCopy code
[code]
    openclaw models list --provider featherless
[/code]

## Модель за замовчуванням

Plugin використовує `Qwen/Qwen3-32B` як модель за замовчуванням під час налаштування, оскільки Featherless документує нативний виклик інструментів для сімейства Qwen 3. OpenClaw налаштовує для неї контекстне вікно на 32 768 токенів, консервативне обмеження виведення на 4 096 токенів і засоби керування міркуванням у шаблоні чату Qwen.

Поля вартості в каталозі мають нульові значення, оскільки Featherless підтримує кілька моделей оплати, а OpenClaw не вбудовує тарифи конкретного плану облікового запису чи вартість запитів.

## Інші моделі Featherless

Використовуйте точний ідентифікатор моделі Featherless після префікса постачальника `featherless/`:

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "featherless/moonshotai/Kimi-K2-Instruct",      },    },  },}
[/code]

OpenClaw навмисно не копіює повний загальнодоступний індекс моделей Featherless до засобу вибору. Індекс великий і не надає достатньо структурованих метаданих можливостей, щоб безпечно класифікувати кожну текстову, візуальну, векторну модель і модель міркування. Тому невідомі ідентифікатори отримують консервативні значення за замовчуванням: лише текст без міркування, контекстне вікно на 4 096 токенів і обмеження виведення на 1 024 токени.

Додайте явний запис моделі постачальника, якщо моделі потрібні інші метадані:

json5Copy code
[code]
    {  models: {    mode: "merge",    providers: {      featherless: {        baseUrl: "https://api.featherless.ai/v1",        apiKey: "${FEATHERLESS_API_KEY}",        api: "openai-completions",        models: [          {            id: "google/gemma-3-27b-it",            name: "Gemma 3 27B",            input: ["text", "image"],            reasoning: false,            contextWindow: 32768,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

Перш ніж додавати власні метадані, перевірте в каталозі моделей Featherless поточну доступність моделей і теги можливостей.

## Усунення несправностей

  * `401` або `403`: переконайтеся, що `FEATHERLESS_API_KEY` доступна процесу Gateway, або знову виконайте початкове налаштування.
  * Невідома модель: використовуйте після префікса `featherless/` точний ідентифікатор із Featherless з урахуванням регістру.
  * Виклики інструментів повертаються як текст: виберіть сімейство моделей, для якого Featherless документує нативний виклик функцій, наприклад Qwen 3.
  * Керований Gateway не бачить ключ: додайте його до `~/.openclaw/.env` або іншого джерела середовища, яке завантажує служба, а потім перезапустіть Gateway.


## Пов’язані матеріали

  * [Постачальники моделей](</uk/concepts/model-providers>)
  * [Усі постачальники](</uk/providers>)
  * [Режими міркування](</uk/tools/thinking>)


Was this useful?YesNo

Open issue