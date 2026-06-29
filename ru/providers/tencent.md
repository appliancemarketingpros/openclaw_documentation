---
title: Tencent Cloud (TokenHub)
source_url: https://docs.openclaw.ai/ru/providers/tencent
scraped_at: 2026-06-29
---

ModelsProviders

Установите официальный Plugin поставщика Tencent Cloud, чтобы получать доступ к Tencent Hy3 preview через конечную точку TokenHub (`tencent-tokenhub`) с помощью OpenAI-совместимого API.

Свойство | Значение  
---|---  
Идентификатор поставщика | `tencent-tokenhub`  
Пакет | `@openclaw/tencent-provider`  
Переменная окружения для аутентификации | `TOKENHUB_API_KEY`  
Флаг адаптации | `--auth-choice tokenhub-api-key`  
Прямой флаг CLI | `--tokenhub-api-key <key>`  
API | OpenAI-совместимый (`openai-completions`)  
Базовый URL по умолчанию | `https://tokenhub.tencentmaas.com/v1`  
Глобальный базовый URL | `https://tokenhub-intl.tencentmaas.com/v1` (переопределение)  
Модель по умолчанию | `tencent-tokenhub/hy3-preview`  
  
## Быстрый старт

* ### Установите Plugin

bashCopy code
[code]
    openclaw plugins install @openclaw/tencent-provider
[/code]

* ### Создайте API-ключ TokenHub

Создайте API-ключ в Tencent Cloud TokenHub. Если вы выбираете ограниченную область доступа для ключа, включите **Hy3 preview** в разрешенные модели.

* ### Запустите адаптацию

АдаптацияCopy code
[code]
    openclaw onboard --auth-choice tokenhub-api-key
[/code]

Прямой флагCopy code
[code]
    openclaw onboard --non-interactive \--auth-choice tokenhub-api-key \--tokenhub-api-key "$TOKENHUB_API_KEY"
[/code]

Только envCopy code
[code]
    export TOKENHUB_API_KEY=...
[/code]

* ### Проверьте модель

bashCopy code
[code]
    openclaw models list --provider tencent-tokenhub
[/code]

## Неинтерактивная настройка

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice tokenhub-api-key \  --tokenhub-api-key "$TOKENHUB_API_KEY" \  --skip-health \  --accept-risk
[/code]

## Встроенный каталог

Ссылка на модель | Название | Ввод | Контекст | Макс. вывод | Примечания  
---|---|---|---|---|---  
`tencent-tokenhub/hy3-preview` | Hy3 preview (TokenHub) | text | 256,000 | 64,000 | По умолчанию; с reasoning  
  
Hy3 preview — это большая языковая MoE-модель Tencent Hunyuan для reasoning, следования инструкциям с длинным контекстом, кода и агентных рабочих процессов. OpenAI-совместимые примеры Tencent используют `hy3-preview` как идентификатор модели и поддерживают стандартные вызовы инструментов chat-completions, а также `reasoning_effort`.

## Многоуровневые цены

Каталог поставщика включает многоуровневые метаданные стоимости, которые масштабируются в зависимости от длины входного окна, поэтому оценки стоимости заполняются без ручных переопределений.

Диапазон входных токенов | Тариф ввода | Тариф вывода | Чтение из кэша  
---|---|---|---  
0 - 16,000 | 0.176 | 0.587 | 0.059  
16,000 - 32,000 | 0.235 | 0.939 | 0.088  
32,000+ | 0.293 | 1.173 | 0.117  
  
Тарифы указаны за миллион токенов в долларах США, как заявлено Tencent. Переопределяйте цены в `models.providers.tencent-tokenhub` только если вам нужна другая поверхность.

## Расширенная конфигурация

Переопределение конечной точки

OpenClaw по умолчанию использует конечную точку Tencent Cloud `https://tokenhub.tencentmaas.com/v1`. Tencent также документирует международную конечную точку TokenHub:

bashCopy code
[code]
    openclaw config set models.providers.tencent-tokenhub.baseUrl "https://tokenhub-intl.tencentmaas.com/v1"
[/code]

Переопределяйте конечную точку только если этого требует ваша учетная запись или регион TokenHub.

Доступность окружения для демона

Если Gateway работает как управляемый сервис (launchd, systemd, Docker), `TOKENHUB_API_KEY` должен быть виден этому процессу. Задайте его в `~/.openclaw/.env` или через `env.shellEnv`, чтобы среды выполнения launchd, systemd или Docker могли его прочитать.

## Связанные материалы

[**Поставщики моделей** Выбор поставщиков, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Справочник по конфигурации** Полная схема конфигурации, включая настройки поставщиков. ](</ru/gateway/configuration>) [**Tencent TokenHub** Страница продукта TokenHub от Tencent Cloud. ](<https://cloud.tencent.com/product/tokenhub>) [**Карточка модели Hy3 preview** Сведения и бенчмарки Tencent Hunyuan Hy3 preview. ](<https://huggingface.co/tencent/Hy3-preview>)

Was this useful?YesNo

Open issue