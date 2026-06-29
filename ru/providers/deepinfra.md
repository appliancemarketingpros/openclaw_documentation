---
title: DeepInfra
source_url: https://docs.openclaw.ai/ru/providers/deepinfra
scraped_at: 2026-06-29
---

ModelsProviders

DeepInfra предоставляет **унифицированный API** , который направляет запросы к самым популярным open source и frontier-моделям через одну конечную точку и ключ API. Он совместим с OpenAI, поэтому большинство SDK OpenAI работают после смены базового URL.

## Установка Plugin

Установите официальный Plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/deepinfra-provideropenclaw gateway restart
[/code]

## Получение ключа API

  1. Перейдите на <https://deepinfra.com/>
  2. Войдите или создайте учетную запись
  3. Перейдите в Панель управления / Ключи и создайте новый ключ API или используйте автоматически созданный


## Настройка CLI

bashCopy code
[code]
    openclaw onboard --deepinfra-api-key <key>
[/code]

Или задайте переменную окружения:

bashCopy code
[code]
    export DEEPINFRA_API_KEY="<your-deepinfra-api-key>" # pragma: allowlist secret
[/code]

## Фрагмент конфигурации

json5Copy code
[code]
    {  env: { DEEPINFRA_API_KEY: "<your-deepinfra-api-key>" }, // pragma: allowlist secret  agents: {    defaults: {      model: { primary: "deepinfra/deepseek-ai/DeepSeek-V4-Flash" },    },  },}
[/code]

## Поддерживаемые поверхности OpenClaw

Plugin регистрирует все поверхности DeepInfra, которые соответствуют текущим контрактам провайдера OpenClaw. Чат, генерация изображений и генерация видео обновляют свои каталоги моделей в реальном времени из `/v1/openai/models?sort_by=openclaw&filter=with_meta`, когда настроен `DEEPINFRA_API_KEY`; остальные поверхности используют отобранные статические значения по умолчанию ниже.

Поверхность | Модель по умолчанию | Конфигурация/инструмент OpenClaw  
---|---|---  
Чат / провайдер моделей | первая запись с тегом чата из живого каталога (резерв из манифеста `deepseek-ai/DeepSeek-V4-Flash`) | `agents.defaults.model`  
Генерация/редактирование изображений | первая запись с тегом `image-gen` из живого каталога (статический резерв `black-forest-labs/FLUX-1-schnell`) | `image_generate`, `agents.defaults.imageGenerationModel`  
Понимание медиа | `moonshotai/Kimi-K2.5` для изображений | понимание входящих изображений  
Распознавание речи в текст | `openai/whisper-large-v3-turbo` | транскрипция входящего аудио  
Синтез речи из текста | `hexgrad/Kokoro-82M` | `messages.tts.provider: "deepinfra"`  
Генерация видео | первая запись с тегом `video-gen` из живого каталога (статический резерв `Pixverse/Pixverse-T2V`) | `video_generate`, `agents.defaults.videoGenerationModel`  
Эмбеддинги памяти | `BAAI/bge-m3` | `agents.defaults.memorySearch.provider: "deepinfra"`  
  
DeepInfra также предоставляет reranking, классификацию, обнаружение объектов и другие нативные типы моделей. В OpenClaw сейчас нет полноценных контрактов провайдера для этих категорий, поэтому этот Plugin пока их не регистрирует.

## Доступные модели

OpenClaw динамически обнаруживает доступные модели DeepInfra при запуске. Используйте `/models deepinfra`, чтобы увидеть полный список доступных моделей.

Любую модель, доступную на [DeepInfra.com](<https://deepinfra.com/>), можно использовать с префиксом `deepinfra/`:

CodeCopy code
[code]
    deepinfra/deepseek-ai/DeepSeek-V4-Flashdeepinfra/deepseek-ai/DeepSeek-V3.2deepinfra/MiniMaxAI/MiniMax-M2.5deepinfra/moonshotai/Kimi-K2.5deepinfra/nvidia/NVIDIA-Nemotron-3-Super-120B-A12Bdeepinfra/zai-org/GLM-5.1...and many more
[/code]

## Примечания

  * Ссылки на модели имеют формат `deepinfra/<provider>/<model>` (например, `deepinfra/Qwen/Qwen3-Max`).
  * Модель по умолчанию: `deepinfra/deepseek-ai/DeepSeek-V4-Flash`
  * Базовый URL: `https://api.deepinfra.com/v1/openai`
  * Нативная генерация видео использует `https://api.deepinfra.com/v1/inference/<model>`.


## Связанные материалы

  * [Провайдеры моделей](</ru/concepts/model-providers>)
  * [Все провайдеры](</ru/providers>)


Was this useful?YesNo

Open issue