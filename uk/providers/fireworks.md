---
title: Феєрверки
source_url: https://docs.openclaw.ai/uk/providers/fireworks
scraped_at: 2026-05-25
---

[Fireworks](<https://fireworks.ai>) надає моделі з відкритими вагами та маршрутизовані моделі через API, сумісний з OpenAI. OpenClaw містить вбудований Plugin постачальника Fireworks, який постачається з двома попередньо каталогізованими моделями Kimi та приймає будь-яку модель або ідентифікатор маршрутизатора Fireworks під час виконання.

Властивість | Значення  
---|---  
Ідентифікатор постачальника | `fireworks` (псевдонім: `fireworks-ai`)  
Plugin | вбудований, `enabledByDefault: true`  
Змінна середовища автентифікації | `FIREWORKS_API_KEY`  
Прапорець онбордингу | `--auth-choice fireworks-api-key`  
Прямий прапорець CLI | `--fireworks-api-key <key>`  
API | сумісний з OpenAI (`openai-completions`)  
Базова URL-адреса | `https://api.fireworks.ai/inference/v1`  
Модель за замовчуванням | `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`  
Псевдонім за замовчуванням | `Kimi K2.5 Turbo`  
  
## Початок роботи

* ### Задайте API-ключ Fireworks

ОнбордингCopy code
[code]
    openclaw onboard --auth-choice fireworks-api-key
[/code]

Прямий прапорецьCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice fireworks-api-key \--fireworks-api-key "$FIREWORKS_API_KEY"
[/code]

Лише середовищеCopy code
[code]
    export FIREWORKS_API_KEY=fw-...
[/code]

Онбординг зберігає ключ для постачальника `fireworks` у ваших профілях автентифікації та задає маршрутизатор **Fire Pass** Kimi K2.5 Turbo як модель за замовчуванням.

* ### Перевірте, що модель доступна

bashCopy code
[code]
    openclaw models list --provider fireworks
[/code]

Список має містити `Kimi K2.6` і `Kimi K2.5 Turbo (Fire Pass)`. Якщо `FIREWORKS_API_KEY` не розв’язано, `openclaw models status --json` повідомляє про відсутні облікові дані в `auth.unusableProfiles`.

## Неінтерактивне налаштування

Для скриптових або CI-встановлень передайте все в командному рядку:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice fireworks-api-key \  --fireworks-api-key "$FIREWORKS_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Вбудований каталог

Посилання на модель | Назва | Вхідні дані | Контекст | Максимальний вивід | Мислення  
---|---|---|---|---|---  
`fireworks/accounts/fireworks/models/kimi-k2p6` | Kimi K2.6 | текст + зображення | 262,144 | 262,144 | Примусово вимкнено  
`fireworks/accounts/fireworks/routers/kimi-k2p5-turbo` | Kimi K2.5 Turbo (Fire Pass) | текст + зображення | 256,000 | 256,000 | Примусово вимкнено (за замовчуванням)  
  
## Власні ідентифікатори моделей Fireworks

OpenClaw приймає будь-яку модель або ідентифікатор маршрутизатора Fireworks під час виконання. Використовуйте точний ідентифікатор, показаний Fireworks, і додайте до нього префікс `fireworks/`. Динамічне розв’язання клонує шаблон Fire Pass (введення тексту + зображення, API, сумісний з OpenAI, вартість за замовчуванням нульова) і автоматично вимикає мислення, коли ідентифікатор відповідає шаблону Kimi.

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "fireworks/accounts/fireworks/models/<your-model-id>",      },    },  },}
[/code]

Як працює префіксування ідентифікаторів моделей

Кожне посилання на модель Fireworks в OpenClaw починається з `fireworks/`, після якого йде точний ідентифікатор або шлях маршрутизатора з платформи Fireworks. Наприклад:

  * Модель маршрутизатора: `fireworks/accounts/fireworks/routers/kimi-k2p5-turbo`
  * Пряма модель: `fireworks/accounts/fireworks/models/<model-name>`


OpenClaw прибирає префікс `fireworks/` під час створення API-запиту та надсилає решту шляху до кінцевої точки Fireworks як сумісне з OpenAI поле `model`.

Чому мислення для Kimi примусово вимкнене

Fireworks K2.6 повертає 400, якщо запит містить параметри `reasoning_*`, хоча Kimi підтримує мислення через власний API Moonshot. Вбудована політика (`extensions/fireworks/thinking-policy.ts`) оголошує для ідентифікаторів моделей Kimi лише рівень мислення `off`, тому ручні перемикачі `/think` і поверхні політик постачальника залишаються узгодженими з контрактом часу виконання.

Щоб використовувати міркування Kimi повністю від початку до кінця, налаштуйте [постачальника Moonshot](</uk/providers/moonshot>) і маршрутизуйте ту саму модель через нього.

Доступність середовища для демона

Якщо Gateway працює як керована служба (launchd, systemd, Docker), ключ Fireworks має бути видимим для цього процесу, а не лише для вашої інтерактивної оболонки.

На macOS `openclaw gateway install` вже під’єднує `~/.openclaw/.env` до файла середовища LaunchAgent. Після ротації ключа повторно запустіть встановлення (або `openclaw doctor --fix`).

## Пов’язане

[**Постачальники моделей** Вибір постачальників, посилань на моделі та поведінки відмовостійкого перемикання. ](</uk/concepts/model-providers>) [**Режими мислення** Рівні `/think`, політики постачальників і маршрутизація моделей, здатних до міркування. ](</uk/tools/thinking>) [**Moonshot** Запускайте Kimi з нативним виводом мислення через власний API Moonshot. ](</uk/providers/moonshot>) [**Усунення несправностей** Загальне усунення несправностей і поширені запитання. ](</uk/help/troubleshooting>)

Was this useful?YesNo