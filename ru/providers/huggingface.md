---
title: Hugging Face (инференс)
source_url: https://docs.openclaw.ai/ru/providers/huggingface
scraped_at: 2026-06-29
---

ModelsProviders

[Поставщики инференса Hugging Face](<https://huggingface.co/docs/inference-providers>) предлагают OpenAI-совместимые чат-завершения через единый API маршрутизатора. Вы получаете доступ ко множеству моделей (DeepSeek, Llama и другим) с одним токеном. OpenClaw использует **OpenAI-совместимую конечную точку** (только чат-завершения); для генерации изображений из текста, эмбеддингов или речи используйте [клиенты HF inference](<https://huggingface.co/docs/api-inference/quicktour>) напрямую.

  * Поставщик: `huggingface`
  * Аутентификация: `HUGGINGFACE_HUB_TOKEN` или `HF_TOKEN` (тонко настроенный токен с **Make calls to Inference Providers**)
  * API: OpenAI-совместимый (`https://router.huggingface.co/v1`)
  * Оплата: единый токен HF; [цены](<https://huggingface.co/docs/inference-providers/pricing>) следуют тарифам поставщика и включают бесплатный уровень.


## Начало работы

* ### Create a fine-grained token

Перейдите в [Hugging Face Settings Tokens](<https://huggingface.co/settings/tokens/new?ownUserPermissions=inference.serverless.write&tokenType=fineGrained>) и создайте новый тонко настроенный токен.

* ### Run onboarding

Выберите **Hugging Face** в раскрывающемся списке поставщиков, затем введите свой API-ключ при запросе:

bashCopy code
[code]
    openclaw onboard --auth-choice huggingface-api-key
[/code]

* ### Select a default model

В раскрывающемся списке **Default Hugging Face model** выберите нужную модель. Список загружается из Inference API при наличии действительного токена; иначе показывается встроенный список. Ваш выбор сохраняется как модель по умолчанию.

Вы также можете задать или изменить модель по умолчанию позже в конфигурации:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/deepseek-ai/DeepSeek-R1" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider huggingface
[/code]

### Неинтерактивная настройка

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice huggingface-api-key \  --huggingface-api-key "$HF_TOKEN"
[/code]

Это задаст `huggingface/deepseek-ai/DeepSeek-R1` как модель по умолчанию.

## Идентификаторы моделей

Ссылки на модели используют форму `huggingface/<org>/<model>` (идентификаторы в стиле Hub). Список ниже получен из **GET** `https://router.huggingface.co/v1/models`; ваш каталог может включать больше моделей.

Модель | Ref (с префиксом `huggingface/`)  
---|---  
DeepSeek R1 | `deepseek-ai/DeepSeek-R1`  
DeepSeek V3.2 | `deepseek-ai/DeepSeek-V3.2`  
Qwen3 8B | `Qwen/Qwen3-8B`  
Qwen2.5 7B Instruct | `Qwen/Qwen2.5-7B-Instruct`  
Qwen3 32B | `Qwen/Qwen3-32B`  
Llama 3.3 70B Instruct | `meta-llama/Llama-3.3-70B-Instruct`  
Llama 3.1 8B Instruct | `meta-llama/Llama-3.1-8B-Instruct`  
GPT-OSS 120B | `openai/gpt-oss-120b`  
GLM 4.7 | `zai-org/GLM-4.7`  
Kimi K2.5 | `moonshotai/Kimi-K2.5`  
  
## Расширенная конфигурация

Model discovery and onboarding dropdown

OpenClaw обнаруживает модели, вызывая **конечную точку Inference напрямую** :

bashCopy code
[code]
    GET https://router.huggingface.co/v1/models
[/code]

(Необязательно: отправьте `Authorization: Bearer $HUGGINGFACE_HUB_TOKEN` или `$HF_TOKEN` для полного списка; некоторые конечные точки возвращают подмножество без аутентификации.) Ответ имеет OpenAI-стиль: `{ "object": "list", "data": [ { "id": "Qwen/Qwen3-8B", "owned_by": "Qwen", ... }, ... ] }`.

Когда вы настраиваете API-ключ Hugging Face (через онбординг, `HUGGINGFACE_HUB_TOKEN` или `HF_TOKEN`), OpenClaw использует этот GET-запрос для обнаружения доступных моделей чат-завершений. Во время **интерактивной настройки** после ввода токена вы видите раскрывающийся список **Default Hugging Face model** , заполненный из этого списка (или из встроенного каталога, если запрос не удался). Во время выполнения (например, при запуске Gateway), когда ключ присутствует, OpenClaw снова вызывает **GET** `https://router.huggingface.co/v1/models`, чтобы обновить каталог. Список объединяется со встроенным каталогом (для метаданных, таких как контекстное окно и стоимость). Если запрос завершается неудачно или ключ не задан, используется только встроенный каталог.

Model names, aliases, and policy suffixes

  * **Имя из API:** отображаемое имя модели **заполняется из GET /v1/models** , когда API возвращает `name`, `title` или `display_name`; иначе оно выводится из идентификатора модели (например, `deepseek-ai/DeepSeek-R1` становится "DeepSeek R1").
  * **Переопределение отображаемого имени:** вы можете задать пользовательскую метку для каждой модели в конфигурации, чтобы она отображалась в CLI и UI так, как вам нужно:

json5Copy code
[code]
    {  agents: {    defaults: {      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1 (fast)" },        "huggingface/deepseek-ai/DeepSeek-R1:cheapest": { alias: "DeepSeek R1 (cheap)" },      },    },  },}
[/code]

  * **Суффиксы политики:** встроенная документация и вспомогательные средства OpenClaw для Hugging Face сейчас рассматривают эти два суффикса как встроенные варианты политики:

    * **`:fastest`** — максимальная пропускная способность.
    * **`:cheapest`** — минимальная стоимость за выходной токен.

Вы можете добавить их как отдельные записи в `models.providers.huggingface.models` или задать `model.primary` с суффиксом. Вы также можете задать порядок поставщиков по умолчанию в [настройках Inference Provider](<https://hf.co/settings/inference-providers>) (без суффикса = использовать этот порядок).

  * **Слияние конфигурации:** существующие записи в `models.providers.huggingface.models` (например, в `models.json`) сохраняются при слиянии конфигурации. Поэтому любые пользовательские `name`, `alias` или параметры модели, заданные там, сохраняются.


Environment and daemon setup

Если Gateway работает как демон (launchd/systemd), убедитесь, что `HUGGINGFACE_HUB_TOKEN` или `HF_TOKEN` доступен этому процессу (например, в `~/.openclaw/.env` или через `env.shellEnv`).

Config: DeepSeek R1 with Qwen fallback json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-R1",        fallbacks: ["huggingface/Qwen/Qwen3-8B"],      },      models: {        "huggingface/deepseek-ai/DeepSeek-R1": { alias: "DeepSeek R1" },        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },      },    },  },}
[/code]

Config: Qwen with cheapest and fastest variants json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen3-8B" },      models: {        "huggingface/Qwen/Qwen3-8B": { alias: "Qwen3 8B" },        "huggingface/Qwen/Qwen3-8B:cheapest": { alias: "Qwen3 8B (cheapest)" },        "huggingface/Qwen/Qwen3-8B:fastest": { alias: "Qwen3 8B (fastest)" },      },    },  },}
[/code]

Config: DeepSeek + Llama + GPT-OSS with aliases json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "huggingface/deepseek-ai/DeepSeek-V3.2",        fallbacks: [          "huggingface/meta-llama/Llama-3.3-70B-Instruct",          "huggingface/openai/gpt-oss-120b",        ],      },      models: {        "huggingface/deepseek-ai/DeepSeek-V3.2": { alias: "DeepSeek V3.2" },        "huggingface/meta-llama/Llama-3.3-70B-Instruct": { alias: "Llama 3.3 70B" },        "huggingface/openai/gpt-oss-120b": { alias: "GPT-OSS 120B" },      },    },  },}
[/code]

Config: Multiple Qwen and DeepSeek with policy suffixes json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest" },      models: {        "huggingface/Qwen/Qwen2.5-7B-Instruct": { alias: "Qwen2.5 7B" },        "huggingface/Qwen/Qwen2.5-7B-Instruct:cheapest": { alias: "Qwen2.5 7B (cheap)" },        "huggingface/deepseek-ai/DeepSeek-R1:fastest": { alias: "DeepSeek R1 (fast)" },        "huggingface/meta-llama/Llama-3.1-8B-Instruct": { alias: "Llama 3.1 8B" },      },    },  },}
[/code]

## Связанные материалы

[**Model selection** Обзор всех поставщиков, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Model selection** Как выбирать и настраивать модели. ](</ru/concepts/models>) [**Inference Providers docs** Официальная документация Hugging Face Inference Providers. ](<https://huggingface.co/docs/inference-providers>) [**Configuration** Полный справочник конфигурации. ](</ru/gateway/configuration>)

Was this useful?YesNo

Open issue