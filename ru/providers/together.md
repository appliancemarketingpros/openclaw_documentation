---
title: Together AI
source_url: https://docs.openclaw.ai/ru/providers/together
scraped_at: 2026-06-29
---

ModelsProviders

[Together AI](<https://together.ai>) предоставляет доступ к ведущим open-source моделям, включая Llama, DeepSeek, Kimi и другие, через единый API.

Свойство | Значение  
---|---  
Провайдер | `together`  
Аутентификация | `TOGETHER_API_KEY`  
API | Совместимо с OpenAI  
Базовый URL | `https://api.together.xyz/v1`  
  
## Начало работы

* ### Получите ключ API

Создайте ключ API на [api.together.ai/settings/api-keys](<https://api.together.ai/settings/api-keys>).

* ### Запустите настройку

bashCopy code
[code]
    openclaw onboard --auth-choice together-api-key
[/code]

* ### Задайте модель по умолчанию

json5Copy code
[code]
    {  agents: {    defaults: {      model: {        primary: "together/meta-llama/Llama-3.3-70B-Instruct-Turbo",      },    },  },}
[/code]

### Неинтерактивный пример

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice together-api-key \  --together-api-key "$TOGETHER_API_KEY"
[/code]

## Встроенный каталог

OpenClaw поставляется со следующим встроенным каталогом Together:

Ссылка на модель | Название | Ввод | Контекст | Примечания  
---|---|---|---|---  
`together/meta-llama/Llama-3.3-70B-Instruct-Turbo` | Llama 3.3 70B Instruct Turbo | текст | 131,072 | Модель по умолчанию  
`together/moonshotai/Kimi-K2.6` | Kimi K2.6 FP4 | текст, изображение | 262,144 | Модель Kimi для рассуждений  
`together/deepseek-ai/DeepSeek-V4-Pro` | DeepSeek V4 Pro | текст | 512,000 | Текстовая модель для рассуждений  
`together/Qwen/Qwen2.5-7B-Instruct-Turbo` | Qwen2.5 7B Instruct Turbo | текст | 32,768 | Быстрая текстовая модель  
`together/zai-org/GLM-5.1` | GLM 5.1 FP4 | текст | 202,752 | Текстовая модель для рассуждений  
  
## Генерация видео

Встроенный Plugin `together` также регистрирует генерацию видео через общий инструмент `video_generate`.

Свойство | Значение  
---|---  
Модель видео по умолчанию | `together/Wan-AI/Wan2.2-T2V-A14B`  
Режимы | text-to-video; только референс по одному изображению с `Wan-AI/Wan2.2-I2V-A14B`  
Поддерживаемые параметры | `aspectRatio`, `resolution`  
  
Чтобы использовать Together как провайдера видео по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: {        primary: "together/Wan-AI/Wan2.2-T2V-A14B",      },    },  },}
[/code]

Примечание об окружении

Если Gateway работает как daemon (launchd/systemd), убедитесь, что `TOGETHER_API_KEY` доступен этому процессу (например, в `~/.openclaw/.env` или через `env.shellEnv`).

Устранение неполадок

  * Проверьте, что ваш ключ работает: `openclaw models list --provider together`
  * Если модели не отображаются, подтвердите, что ключ API задан в правильном окружении для вашего процесса Gateway.
  * Ссылки на модели используют форму `together/<model-id>`.


## Связанные материалы

[**Выбор модели** Правила провайдеров, ссылки на модели и поведение failover. ](</ru/concepts/model-providers>) [**Генерация видео** Общие параметры инструмента генерации видео и выбор провайдера. ](</ru/tools/video-generation>) [**Справочник конфигурации** Полная схема конфигурации, включая настройки провайдеров. ](</ru/gateway/configuration-reference>) [**Together AI** Панель управления Together AI, документация API и цены. ](<https://together.ai>)

Was this useful?YesNo

Open issue