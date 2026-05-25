---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/uk/providers/tencent
scraped_at: 2026-05-25
---

Tencent Cloud постачається як вбудований Plugin постачальника в OpenClaw. Він надає доступ до Tencent Hy3 preview через кінцеву точку TokenHub (`tencent-tokenhub`) з використанням API, сумісного з OpenAI.

Властивість | Значення  
---|---  
Ідентифікатор постачальника | `tencent-tokenhub`  
Plugin | вбудований, `enabledByDefault: true`  
Змінна середовища автентифікації | `TOKENHUB_API_KEY`  
Прапорець онбордингу | `--auth-choice tokenhub-api-key`  
Прямий прапорець CLI | `--tokenhub-api-key <key>`  
API | сумісний з OpenAI (`openai-completions`)  
Базовий URL за замовчуванням | `https://tokenhub.tencentmaas.com/v1`  
Глобальний базовий URL | `https://tokenhub-intl.tencentmaas.com/v1` (перевизначення)  
Модель за замовчуванням | `tencent-tokenhub/hy3-preview`  
  
## Швидкий старт

* ### Створіть API-ключ TokenHub

Створіть API-ключ у Tencent Cloud TokenHub. Якщо ви вибираєте обмежену область доступу для ключа, додайте **Hy3 preview** до дозволених моделей.

* ### Запустіть онбординг

OnboardingCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Direct flagCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Env onlyCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Перевірте модель

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Неінтерактивне налаштування

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Вбудований каталог

Посилання на модель | Назва | Вхідні дані | Контекст | Максимальний вихід | Примітки  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | text | 256,000 | 64,000 | За замовчуванням; підтримує reasoning  
  
Hy3 preview — це велика MoE-мовна модель Tencent Hunyuan для reasoning, виконання інструкцій із довгим контекстом, коду та агентних робочих процесів. Приклади Tencent, сумісні з OpenAI, використовують `hy3-preview` як ідентифікатор моделі та підтримують стандартні chat-completions tool calling, а також `reasoning_effort`.

## Багаторівневе ціноутворення

Вбудований каталог постачається з багаторівневими метаданими вартості, що масштабуються залежно від довжини вхідного вікна, тому оцінки вартості заповнюються без ручних перевизначень.

Діапазон вхідних токенів | Вхідний тариф | Вихідний тариф | Читання з кешу  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
Тарифи наведено за мільйон токенів у доларах США, як заявляє Tencent. Перевизначайте ціни в `models.providers.tencent-tokenhub` лише тоді, коли вам потрібна інша поверхня.

## Розширена конфігурація

Перевизначення кінцевої точки

OpenClaw за замовчуванням використовує кінцеву точку Tencent Cloud `https://tokenhub.tencentmaas.com/v1`. Tencent також документує міжнародну кінцеву точку TokenHub:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

Перевизначайте кінцеву точку лише тоді, коли цього вимагає ваш обліковий запис або регіон TokenHub.

Доступність середовища для демона

Якщо Gateway працює як керована служба (launchd, systemd, Docker), `TOKENHUB_API_KEY` має бути видимим для цього процесу. Задайте його в `~/.openclaw/.env` або через `env.shellEnv`, щоб середовища launchd, systemd або Docker exec могли його прочитати.

## Пов’язане

[**Постачальники моделей** Вибір постачальників, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Довідник конфігурації** Повна схема конфігурації, включно з налаштуваннями постачальників. ](</uk/gateway/configuration>) [**Tencent TokenHub** Сторінка продукту TokenHub від Tencent Cloud. ](<https://cloud.tencent.com/product/tokenhub>) [**Картка моделі Hy3 preview** Відомості та бенчмарки Tencent Hunyuan Hy3 preview. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo