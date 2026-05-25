---
title: Together AI
source_url: https://docs.openclaw.ai/uk/providers/together
scraped_at: 2026-05-25
---

[Together AI](<https://together.ai>) надає доступ до провідних моделей із відкритим кодом, зокрема Llama, DeepSeek, Kimi та інших, через уніфікований API.

Властивість | Значення  
---|---  
Постачальник | `together`  
Автентифікація | `TOGETHER_API_KEY`  
API | сумісний з OpenAI  
Базова URL-адреса | `https://api.together.xyz/v1`  
  
## Початок роботи

* ### Отримайте API-ключ

Створіть API-ключ на [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Запустіть початкове налаштування

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Установіть модель за замовчуванням

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "together/moonshotai/Kimi-K2.5" },    },  },}
[/code]

### Неінтерактивний приклад

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Вбудований каталог

OpenClaw постачається з таким вбудованим каталогом Together:

Посилання на модель | Назва | Вхідні дані | Контекст | Примітки  
---|---|---|---|---  
`together/moonshotai/Kimi-K2.5` | Kimi K2.5 | текст, зображення | 262,144 | Модель за замовчуванням; reasoning увімкнено  
`together/zai-org/GLM-4.7` | GLM 4.7 Fp8 | текст | 202,752 | Текстова модель загального призначення  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | текст | 131,072 | Швидка інструкційна модель  
`together/meta-llama/Llama-4-Scout-17B-16E-Instruct` | Llama 4 Scout 17B 16E Instruct | текст, зображення | 10,000,000 | Мультимодальна  
`together/meta-llama/Llama-4-Maverick-17B-128E-Instruct-FP8` | Llama 4 Maverick 17B 128E Instruct FP8 | текст, зображення | 20,000,000 | Мультимодальна  
`together/deepseek-ai/DeepSeek-V3.1` | DeepSeek V3.1 | текст | 131,072 | Загальна текстова модель  
`together/deepseek-ai/DeepSeek-R1` | DeepSeek R1 | текст | 131,072 | Модель reasoning  
`together/moonshotai/Kimi-K2-Instruct-0905` | Kimi K2-Instruct 0905 | текст | 262,144 | Додаткова текстова модель Kimi  
  
## Генерація відео

Вбудований Plugin `together` також реєструє генерацію відео через спільний інструмент `video_generate`.

Властивість | Значення  
---|---  
Модель відео за замовчуванням | `together/Wan-AI/Wan2.2-T2V-A14B`  
Режими | текст-у-відео, референс із одного зображення  
Підтримувані параметри | `aspectRatio`, `resolution`  
  
Щоб використовувати Together як постачальника відео за замовчуванням:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Примітка щодо середовища

Якщо Gateway працює як демон (launchd/systemd), переконайтеся, що `TOGETHER_API_KEY` доступний цьому процесу (наприклад, у `~/.openclaw/.env` або через `env.shellEnv`).

Усунення несправностей

  * Перевірте, що ваш ключ працює: `openclaw models list --provider together`
  * Якщо моделі не відображаються, підтвердьте, що API-ключ установлено в правильному середовищі для вашого процесу Gateway.
  * Посилання на моделі мають форму `together/<model-id>`.


## Пов’язане

[**Вибір моделі** Правила постачальників, посилання на моделі та поведінка failover. ](</uk/concepts/model-providers>) [**Генерація відео** Спільні параметри інструмента генерації відео та вибір постачальника. ](</uk/tools/video-generation>) [**Довідник конфігурації** Повна схема конфігурації, включно з налаштуваннями постачальників. ](</uk/gateway/configuration-reference>) [**Together AI** Панель керування Together AI, документація API та ціни. ](<https://together.ai>)

Was this useful?YesNo