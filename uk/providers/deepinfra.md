---
title: DeepInfra
source_url: https://docs.openclaw.ai/uk/providers/deepinfra
scraped_at: 2026-05-25
---

DeepInfra надає **уніфікований API** , який спрямовує запити до найпопулярніших моделей з відкритим кодом і frontier-моделей через один endpoint і API-ключ. Він сумісний з OpenAI, тому більшість OpenAI SDK працюють після зміни базового URL.

## Отримання API-ключа

  1. Перейдіть на <https://deepinfra.com/>
  2. Увійдіть або створіть обліковий запис
  3. Перейдіть до Dashboard / Keys і згенеруйте новий API-ключ або використайте автоматично створений


## Налаштування CLI

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

Або задайте змінну середовища:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Фрагмент конфігурації

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V3.2" },    },  },}
[/code]

## Підтримувані поверхні OpenClaw

Вбудований plugin реєструє всі поверхні DeepInfra, які відповідають поточним контрактам постачальників OpenClaw:

Поверхня | Модель за замовчуванням | Конфігурація/інструмент OpenClaw  
---|---|---  
Чат / постачальник моделей | `deepseek-ai/DeepSeek-V3.2` | `agents.defaults.model`  
Генерація/редагування зображень | `black-forest-labs/FLUX-1-schnell` | `image_generate`, `agents.defaults.imageGenerationModel`  
Розуміння медіа | `moonshotai/Kimi-K2.5` для зображень | розуміння вхідних зображень  
Мовлення в текст | `openai/whisper-large-v3-turbo` | транскрибування вхідного аудіо  
Текст у мовлення | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
Генерація відео | `Pixverse/Pixverse-T2V` | `video_generate`, `agents.defaults.videoGenerationModel`  
Векторні представлення пам’яті | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra також надає reranking, класифікацію, виявлення об’єктів та інші нативні типи моделей. OpenClaw наразі не має повноцінних контрактів постачальників для цих категорій, тому цей plugin поки їх не реєструє.

## Доступні моделі

OpenClaw динамічно виявляє доступні моделі DeepInfra під час запуску. Використайте `/models deepinfra`, щоб переглянути повний список доступних моделей.

Будь-яку модель, доступну на [DeepInfra.com](<https://deepinfra.com/>), можна використовувати з префіксом `deepinfra/`:

CodeCopy code
[code]
    deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/moonshotai/Kimi-K2.5deepinfra/zai-org/GLM-5.1...і багато інших
[/code]

## Примітки

  * Посилання на моделі мають формат `deepinfra/<provider>/<model>` (наприклад, `deepinfra/Qwen/Qwen3-Max`).
  * Модель за замовчуванням: `deepinfra/deepseek-ai/DeepSeek-V3.2`
  * Базовий URL: `https://api.deepinfra.com/v1/openai`
  * Нативна генерація відео використовує `https://api.deepinfra.com/v1/inference/<model>`.


## Пов’язане

  * [Постачальники моделей](</uk/concepts/model-providers>)
  * [Усі постачальники](</uk/providers>)


Was this useful?YesNo