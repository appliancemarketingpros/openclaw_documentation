---
title: Amazon Bedrock
source_url: https://docs.openclaw.ai/uk/providers/bedrock
scraped_at: 2026-05-25
---

OpenClaw може використовувати моделі **Amazon Bedrock** через потокового постачальника **Bedrock Converse** від pi-ai. Автентифікація Bedrock використовує **типовий ланцюжок облікових даних AWS SDK** , а не API-ключ.

Властивість | Значення  
---|---  
Постачальник | `amazon-bedrock`  
API | `bedrock-converse-stream`  
Автентифікація | облікові дані AWS (змінні середовища, спільна конфігурація або роль екземпляра)  
Регіон | `AWS_REGION` або `AWS_DEFAULT_REGION` (типово: `us-east-1`)  
  
## Початок роботи

Виберіть бажаний метод автентифікації та виконайте кроки налаштування.

### Ключі доступу / змінні середовища

**Найкраще для:** машин розробників, CI або хостів, де ви керуєте обліковими даними AWS напряму.

* ### Установіть облікові дані AWS на хості Gateway

bashCopy code
[code]
    export AWS_ACCESS_KEY_ID="AKIA..."export AWS_SECRET_ACCESS_KEY="..."export AWS_REGION="us-east-1"# Optional:export AWS_SESSION_TOKEN="..."export AWS_PROFILE="your-profile"# Optional (Bedrock API key/bearer token):export AWS_BEARER_TOKEN_BEDROCK="..."
[/code]

* ### Додайте постачальника Bedrock і модель до своєї конфігурації

`apiKey` не потрібен. Налаштуйте постачальника з `auth: "aws-sdk"`:

json5Copy code
[code]
    {  models: {    providers: {      "amazon-bedrock": {        baseUrl: "https://bedrock-runtime.us-east-1.amazonaws.com",        api: "bedrock-converse-stream",        auth: "aws-sdk",        models: [          {            id: "us.anthropic.claude-opus-4-6-v1:0",            name: "Claude Opus 4.6 (Bedrock)",            reasoning: true,            input: ["text", "image"],            cost: { input: 0, output: 0, cacheRead: 0, cacheWrite: 0 },            contextWindow: 200000,            maxTokens: 8192,          },        ],      },    },  },  agents: {    defaults: {      model: { primary: "amazon-bedrock/us.anthropic.claude-opus-4-6-v1:0" },    },  },}
[/code]

* ### Перевірте, що моделі доступні

bashCopy code
[code]
    openclaw models list
[/code]

### Ролі екземплярів EC2 (IMDS)

**Найкраще для:** екземплярів EC2 із прикріпленою роллю IAM, які використовують службу метаданих екземпляра для автентифікації.

* ### Увімкніть виявлення явно

Під час використання IMDS OpenClaw не може виявити автентифікацію AWS лише за маркерами середовища, тому потрібно явно погодитися:

bashCopy code
[code]
    openclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1
[/code]

* ### За бажанням додайте маркер середовища для автоматичного режиму

Якщо ви також хочете, щоб шлях автоматичного виявлення за маркером середовища працював (наприклад, для поверхонь `openclaw status`):

bashCopy code
[code]
    export AWS_PROFILE=defaultexport AWS_REGION=us-east-1
[/code]

Вам **не** потрібен фіктивний API-ключ.

* ### Перевірте, що моделі виявлено

bashCopy code
[code]
    openclaw models list
[/code]

## Автоматичне виявлення моделей

OpenClaw може автоматично виявляти моделі Bedrock, які підтримують **потокове передавання** та **текстовий вивід**. Виявлення використовує `bedrock:ListFoundationModels` і `bedrock:ListInferenceProfiles`, а результати кешуються (типово: 1 година).

Як увімкнено неявного провайдера:

  * Якщо `plugins.entries.amazon-bedrock.config.discovery.enabled` має значення `true`, OpenClaw спробує виконати виявлення, навіть якщо маркер середовища AWS відсутній.
  * Якщо `plugins.entries.amazon-bedrock.config.discovery.enabled` не задано, OpenClaw автоматично додає неявного провайдера Bedrock лише тоді, коли бачить один із цих маркерів автентифікації AWS: `AWS_BEARER_TOKEN_BEDROCK`, `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY` або `AWS_PROFILE`.
  * Фактичний шлях автентифікації середовища виконання Bedrock усе ще використовує типовий ланцюжок AWS SDK, тому спільна конфігурація, SSO й автентифікація ролі інстансу IMDS можуть працювати навіть тоді, коли для виявлення потрібно було `enabled: true` для явного ввімкнення.


Параметри конфігурації виявлення

Параметри конфігурації розташовані в `plugins.entries.amazon-bedrock.config.discovery`:

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          discovery: {            enabled: true,            region: "us-east-1",            providerFilter: ["anthropic", "amazon"],            refreshInterval: 3600,            defaultContextWindow: 32000,            defaultMaxTokens: 4096,          },        },      },    },  },}
[/code]

Параметр | Типове значення | Опис  
---|---|---  
`enabled` | auto | В автоматичному режимі OpenClaw вмикає неявного провайдера Bedrock лише тоді, коли бачить підтримуваний маркер середовища AWS. Установіть `true`, щоб примусово ввімкнути виявлення.  
`region` | `AWS_REGION` / `AWS_DEFAULT_REGION` / `us-east-1` | Регіон AWS, що використовується для викликів API виявлення.  
`providerFilter` | (усі) | Зіставляє імена провайдерів Bedrock (наприклад, `anthropic`, `amazon`).  
`refreshInterval` | `3600` | Тривалість кешування в секундах. Установіть `0`, щоб вимкнути кешування.  
`defaultContextWindow` | `32000` | Контекстне вікно, що використовується для виявлених моделей (перевизначте, якщо знаєте обмеження своєї моделі).  
`defaultMaxTokens` | `4096` | Максимальна кількість вихідних токенів, що використовується для виявлених моделей (перевизначте, якщо знаєте обмеження своєї моделі).  
  
## Швидке налаштування (шлях AWS)

Цей покроковий приклад створює роль IAM, додає дозволи Bedrock, пов’язує профіль інстансу та вмикає виявлення OpenClaw на хості EC2.

bashCopy code
[code]
    # 1. Create IAM role and instance profileaws iam create-role --role-name EC2-Bedrock-Access \  --assume-role-policy-document '{    "Version": "2012-10-17",    "Statement": [{      "Effect": "Allow",      "Principal": {"Service": "ec2.amazonaws.com"},      "Action": "sts:AssumeRole"    }]  }' aws iam attach-role-policy --role-name EC2-Bedrock-Access \  --policy-arn arn:aws:iam::aws:policy/AmazonBedrockFullAccess aws iam create-instance-profile --instance-profile-name EC2-Bedrock-Accessaws iam add-role-to-instance-profile \  --instance-profile-name EC2-Bedrock-Access \  --role-name EC2-Bedrock-Access # 2. Attach to your EC2 instanceaws ec2 associate-iam-instance-profile \  --instance-id i-xxxxx \  --iam-instance-profile Name=EC2-Bedrock-Access # 3. On the EC2 instance, enable discovery explicitlyopenclaw config set plugins.entries.amazon-bedrock.config.discovery.enabled trueopenclaw config set plugins.entries.amazon-bedrock.config.discovery.region us-east-1 # 4. Optional: add an env marker if you want auto mode without explicit enableecho 'export AWS_PROFILE=default' >> ~/.bashrcecho 'export AWS_REGION=us-east-1' >> ~/.bashrcsource ~/.bashrc # 5. Verify models are discoveredopenclaw models list
[/code]

## Розширена конфігурація

Профілі інференсу

OpenClaw виявляє **регіональні та глобальні профілі інференсу** разом із базовими моделями. Коли профіль зіставляється з відомою базовою моделлю, профіль успадковує можливості цієї моделі (контекстне вікно, максимальні токени, reasoning, vision), а правильний регіон запиту Bedrock підставляється автоматично. Це означає, що міжрегіональні профілі Claude працюють без ручних перевизначень провайдера.

ID профілів інференсу мають вигляд `us.anthropic.claude-opus-4-6-v1:0` (регіональний) або `anthropic.claude-opus-4-6-v1:0` (глобальний). Якщо базова модель уже є в результатах виявлення, профіль успадковує повний набір її можливостей; інакше застосовуються безпечні типові значення.

Додаткова конфігурація не потрібна. Поки виявлення ввімкнено, а принципал IAM має `bedrock:ListInferenceProfiles`, профілі з’являються поряд із базовими моделями в `openclaw models list`.

Рівень сервісу

Деякі моделі Bedrock підтримують параметр `service_tier` для оптимізації за вартістю або затримкою. Доступні такі рівні:

Рівень | Опис  
---|---  
`default` | Стандартний рівень Bedrock  
`flex` | Обробка зі знижкою для навантажень, які можуть витримувати більшу затримку  
`priority` | Пріоритетна обробка для навантажень, чутливих до затримки  
`reserved` | Зарезервована потужність для стабільних навантажень  
  
Установіть `serviceTier` (або `service_tier`) через `agents.defaults.params` для запитів до моделей Bedrock або для окремої моделі в `agents.defaults.models["<model-key>"].params`:

json5Copy code
[code]
    {  agents: {    defaults: {      params: {        serviceTier: "flex", // applies to all models      },      models: {        "amazon-bedrock/mistral.mistral-large-3-675b-instruct": {          params: {            serviceTier: "priority", // per-model override          },        },      },    },  },}
[/code]

Допустимі значення: `default`, `flex`, `priority` і `reserved`. Не всі моделі підтримують усі рівні — якщо запитано непідтримуваний рівень, Bedrock поверне помилку валідації. Примітка: повідомлення про помилку дещо вводить в оману; воно може сказати "The provided model identifier is invalid" замість вказівки на непідтримуваний рівень сервісу. Якщо бачите цю помилку, перевірте, чи модель підтримує запитаний рівень.

Температура Claude Opus 4.7

Bedrock відхиляє параметр `temperature` для Claude Opus 4.7. OpenClaw автоматично пропускає `temperature` для будь-якого посилання Bedrock на Opus 4.7, зокрема ID базових моделей, іменованих профілів інференсу, прикладних профілів інференсу, базова модель яких визначається як Opus 4.7 через `bedrock:GetInferenceProfile`, а також варіантів із крапками `opus-4.7` з необов’язковими префіксами регіонів (`us.`, `eu.`, `ap.`, `apac.`, `au.`, `jp.`, `global.`). Ручка конфігурації не потрібна, а пропуск застосовується як до об’єкта параметрів запиту, так і до поля payload `inferenceConfig`.

Захисні обмеження

Ви можете застосувати [Amazon Bedrock Guardrails](<https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html>) до всіх викликів моделей Bedrock, додавши об’єкт `guardrail` до конфігурації Plugin `amazon-bedrock`. Захисні обмеження дають змогу застосовувати фільтрацію контенту, заборону тем, фільтри слів, фільтри чутливої інформації та перевірки контекстного обґрунтування.

json5Copy code
[code]
    {  plugins: {    entries: {      "amazon-bedrock": {        config: {          guardrail: {            guardrailIdentifier: "abc123", // guardrail ID or full ARN            guardrailVersion: "1", // version number or "DRAFT"            streamProcessingMode: "sync", // optional: "sync" or "async"            trace: "enabled", // optional: "enabled", "disabled", or "enabled_full"          },        },      },    },  },}
[/code]

Параметр | Обов’язково | Опис  
---|---|---  
`guardrailIdentifier` | Так | Ідентифікатор захисного обмеження (наприклад, `abc123`) або повний ARN (наприклад, `arn:aws:bedrock:us-east-1:123456789012:guardrail/abc123`).  
`guardrailVersion` | Так | Номер опублікованої версії або `"DRAFT"` для робочого чернеткового варіанта.  
`streamProcessingMode` | Ні | `"sync"` або `"async"` для оцінювання захисного обмеження під час потокового передавання. Якщо пропущено, Bedrock використовує своє стандартне значення.  
`trace` | Ні | `"enabled"` або `"enabled_full"` для налагодження; пропустіть або встановіть `"disabled"` для продакшну.  
Ембеддинги для пошуку в пам’яті

Bedrock також може бути постачальником ембеддингів для [пошуку в пам’яті](</uk/concepts/memory-search>). Це налаштовується окремо від постачальника інференсу -- встановіть `agents.defaults.memorySearch.provider` у `"bedrock"`:

json5Copy code
[code]
    {  agents: {    defaults: {      memorySearch: {        provider: "bedrock",        model: "amazon.titan-embed-text-v2:0", // default      },    },  },}
[/code]

Ембеддинги Bedrock використовують той самий ланцюжок облікових даних AWS SDK, що й інференс (ролі екземплярів, SSO, ключі доступу, спільну конфігурацію та web identity). API-ключ не потрібен. Коли `provider` дорівнює `"auto"`, Bedrock автоматично виявляється, якщо цей ланцюжок облікових даних успішно розв’язується.

Підтримувані моделі ембеддингів включають Amazon Titan Embed (v1, v2), Amazon Nova Embed, Cohere Embed (v3, v4) і TwelveLabs Marengo. Див. [довідник конфігурації пам’яті -- Bedrock](</uk/reference/memory-config#bedrock-embedding-config>) для повного списку моделей і параметрів розмірності.

Примітки та застереження

  * Bedrock вимагає ввімкненого **доступу до моделей** у вашому обліковому записі/регіоні AWS.
  * Для автоматичного виявлення потрібні дозволи `bedrock:ListFoundationModels` і `bedrock:ListInferenceProfiles`.
  * Якщо ви покладаєтеся на автоматичний режим, задайте один із підтримуваних маркерів середовища автентифікації AWS на хості Gateway. Якщо ви віддаєте перевагу автентифікації IMDS/спільної конфігурації без маркерів середовища, встановіть `plugins.entries.amazon-bedrock.config.discovery.enabled: true`.
  * OpenClaw показує джерело облікових даних у такому порядку: `AWS_BEARER_TOKEN_BEDROCK`, потім `AWS_ACCESS_KEY_ID` \+ `AWS_SECRET_ACCESS_KEY`, потім `AWS_PROFILE`, потім стандартний ланцюжок AWS SDK.
  * Підтримка reasoning залежить від моделі; перевірте картку моделі Bedrock щодо поточних можливостей.
  * Якщо ви віддаєте перевагу керованому потоку ключів, ви також можете розмістити OpenAI-сумісний proxy перед Bedrock і натомість налаштувати його як постачальника OpenAI.


## Пов’язане

[**Вибір моделі** Вибір постачальників, посилань на моделі та поведінки failover. ](</uk/concepts/model-providers>) [**Пошук у пам’яті** Ембеддинги Bedrock для конфігурації пошуку в пам’яті. ](</uk/concepts/memory-search>) [**Довідник конфігурації пам’яті** Повний список моделей ембеддингів Bedrock і параметри розмірності. ](</uk/reference/memory-config#bedrock-embedding-config>) [**Усунення несправностей** Загальне усунення несправностей і FAQ. ](</uk/help/troubleshooting>)

Was this useful?YesNo