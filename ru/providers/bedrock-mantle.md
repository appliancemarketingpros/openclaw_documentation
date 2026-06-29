---
title: Amazon Bedrock Mantle
source_url: https://docs.openclaw.ai/ru/providers/bedrock-mantle
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw включает встроенный провайдер **Amazon Bedrock Mantle** , который подключается к OpenAI-совместимой конечной точке Mantle. Mantle размещает модели с открытым исходным кодом и сторонние модели (GPT-OSS, Qwen, Kimi, GLM и похожие) через стандартную поверхность `/v1/chat/completions` на базе инфраструктуры Bedrock.

Свойство | Значение  
---|---  
ID провайдера | `amazon-bedrock-mantle`  
API | `openai-completions` (OpenAI-совместимый) или `anthropic-messages` (маршрут Anthropic Messages)  
Аутентификация | Явный `AWS_BEARER_TOKEN_BEDROCK` или генерация bearer-токена через цепочку учетных данных IAM  
Регион по умолчанию | `us-east-1` (переопределяется через `AWS_REGION` или `AWS_DEFAULT_REGION`)  
  
## Начало работы

Выберите предпочтительный способ аутентификации и выполните шаги настройки.

### Явный bearer-токен

**Лучше всего для:** сред, где у вас уже есть bearer-токен Mantle.

* ### Установите bearer-токен на хосте Gateway

bashCopy code
[code]
    export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

При необходимости задайте регион (по умолчанию `us-east-1`):

bashCopy code
[code]
    export AWS_REGION="us-west-2"
[/code]

* ### Включите передачу данных провайдеру для Claude Fable 5

Claude Fable 5 и модели Bedrock класса Claude Mythos требуют режим Mantle Data Retention API `provider_data_share` перед вызовом. Это явное согласие позволяет Bedrock передавать промпты и завершения в Anthropic и хранить их до 30 дней для проверки доверия и безопасности.

bashCopy code
[code]
    AWS_REGION="${AWS_REGION:-us-east-1}"curl -X PUT "https://bedrock-mantle.${AWS_REGION}.api.aws/v1/data_retention" \  -H "Authorization: Bearer $AWS_BEARER_TOKEN_BEDROCK" \  -H "Content-Type: application/json" \  -d '{ "mode": "provider_data_share" }'
[/code]

Используйте другую модель Bedrock в конфигурации, если вы не можете принять этот режим хранения.

* ### Проверьте, что модели обнаруживаются

bashCopy code
[code]
    openclaw models list
[/code]

Обнаруженные модели появляются в провайдере `amazon-bedrock-mantle`. Дополнительная конфигурация не требуется, если вы не хотите переопределить значения по умолчанию.

### Учетные данные IAM

**Лучше всего для:** использования учетных данных, совместимых с AWS SDK (общая конфигурация, SSO, web identity, роли инстанса или задачи).

* ### Настройте учетные данные AWS на хосте Gateway

Подходит любой источник аутентификации, совместимый с AWS SDK:

bashCopy code
[code]
    export AWS_PROFILE="default"export AWS_REGION="us-west-2"
[/code]

* ### Проверьте, что модели обнаруживаются

bashCopy code
[code]
    openclaw models list
[/code]

OpenClaw автоматически генерирует bearer-токен Mantle из цепочки учетных данных.

## Автоматическое обнаружение моделей

Когда `AWS_BEARER_TOKEN_BEDROCK` задан, OpenClaw использует его напрямую. В противном случае OpenClaw пытается сгенерировать bearer-токен Mantle из стандартной цепочки учетных данных AWS. Затем он обнаруживает доступные модели Mantle, запрашивая региональную конечную точку `/v1/models`.

Поведение | Подробности  
---|---  
Кэш обнаружения | Результаты кэшируются на 1 час  
Обновление токена IAM | Ежечасно  
  
Чтобы оставить Plugin Mantle включенным, но отключить автоматическое обнаружение и генерацию bearer-токена IAM, отключите принадлежащий Plugin переключатель обнаружения:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock-mantle.config.discovery.enabled false
[/code]

### Поддерживаемые регионы

`us-east-1`, `us-east-2`, `us-west-2`, `ap-northeast-1`, `ap-south-1`, `ap-southeast-3`, `eu-central-1`, `eu-west-1`, `eu-west-2`, `eu-south-1`, `eu-north-1`, `sa-east-1`.

## Ручная конфигурация

Если вы предпочитаете явную конфигурацию вместо автообнаружения:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        baseUrl: "https://bedrock-mantle.us-east-1.api.aws/v1",        api: "openai-completions",        auth: "api-key",        apiKey: "env:AWS_BEARER_TOKEN_BEDROCK",        models: [          {            id: "gpt-oss-120b",            name: "GPT-OSS 120B",            reasoning: true,            input: ["text"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 32000,            maxTokens: 4096,          },        ],      },    },  },}
[/code]

## Расширенная конфигурация

Поддержка рассуждений

Поддержка рассуждений выводится из ID моделей, содержащих шаблоны вроде `thinking`, `reasoner` или `gpt-oss-120b`. OpenClaw автоматически устанавливает `reasoning: true` для подходящих моделей во время обнаружения.

Недоступность конечной точки

Если конечная точка Mantle недоступна или не возвращает моделей, провайдер тихо пропускается. OpenClaw не выдает ошибку; другие настроенные провайдеры продолжают работать как обычно.

Claude Opus 4.7 через маршрут Anthropic Messages

Mantle также предоставляет маршрут Anthropic Messages, который передает модели Claude через тот же потоковый путь с bearer-аутентификацией. Claude Opus 4.7 (`amazon-bedrock-mantle/claude-opus-4.7`) можно вызывать через этот маршрут с потоковой передачей, принадлежащей провайдеру, поэтому bearer-токены AWS не обрабатываются как API-ключи Anthropic.

Когда вы закрепляете модель Anthropic Messages за провайдером Mantle, OpenClaw использует поверхность API `anthropic-messages` вместо `openai-completions` для этой модели. Аутентификация по-прежнему берется из `AWS_BEARER_TOKEN_BEDROCK` (или выпущенного bearer-токена IAM).

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock-mantle": {        models: [          {            id: "claude-opus-4.7",            name: "Claude Opus 4.7",            api: "anthropic-messages",            reasoning: true,            input: ["text", "image"],            contextWindow: 1000000,            maxTokens: 32000,          },        ],      },    },  },}
[/code]

Связь с провайдером Amazon Bedrock

Bedrock Mantle — это отдельный провайдер относительно стандартного провайдера [Amazon Bedrock](</ru/providers/bedrock>). Mantle использует OpenAI-совместимую поверхность `/v1`, а стандартный провайдер Bedrock использует нативный API Bedrock.

Оба провайдера используют одни и те же учетные данные `AWS_BEARER_TOKEN_BEDROCK`, когда они присутствуют.

## Связанное

[**Amazon Bedrock** Нативный провайдер Bedrock для Anthropic Claude, Titan и других моделей. ](</ru/providers/bedrock>) [**Выбор модели** Выбор провайдеров, ссылок на модели и поведения при переключении после сбоя. ](</ru/concepts/model-providers>) [**OAuth и аутентификация** Подробности аутентификации и правила повторного использования учетных данных. ](</ru/gateway/authentication>) [**Устранение неполадок** Распространенные проблемы и способы их решения. ](</ru/help/troubleshooting>)

Was this useful?YesNo

Open issue