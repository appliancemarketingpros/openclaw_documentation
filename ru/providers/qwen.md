---
title: Qwen
source_url: https://docs.openclaw.ai/ru/providers/qwen
scraped_at: 2026-06-29
---

ModelsProviders

OpenClaw теперь рассматривает Qwen как полноправный Plugin провайдера с каноническим идентификатором `qwen`. Plugin провайдера нацелен на конечные точки Qwen Cloud / Alibaba DashScope и Coding Plan, сохраняет работоспособность устаревших идентификаторов `modelstudio` как совместимого псевдонима, а также предоставляет поток токенов Qwen Portal как провайдер `qwen-oauth`.

  * Провайдер: `qwen`
  * Провайдер Portal: [`qwen-oauth`](</ru/providers/qwen-oauth>)
  * Предпочтительная переменная окружения: `QWEN_API_KEY`
  * Также принимаются для совместимости: `MODELSTUDIO_API_KEY`, `DASHSCOPE_API_KEY`
  * Стиль API: совместимый с OpenAI


## Установите Plugin

Установите официальный Plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/qwen-provideropenclaw gateway restart
[/code]

## Начало работы

Выберите тип плана и выполните шаги настройки.

### Coding Plan (subscription)

**Лучше всего подходит для:** доступа по подписке через Qwen Coding Plan.

* ### Get your API key

Создайте или скопируйте API-ключ на [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>).

* ### Run onboarding

Для конечной точки **Global** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key
[/code]

Для конечной точки **China** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

### Standard (pay-as-you-go)

**Лучше всего подходит для:** доступа с оплатой по мере использования через конечную точку Standard Model Studio, включая модели вроде `qwen3.6-plus`, которые могут быть недоступны в Coding Plan.

* ### Get your API key

Создайте или скопируйте API-ключ на [home.qwencloud.com/api-keys](<https://home.qwencloud.com/api-keys>).

* ### Run onboarding

Для конечной точки **Global** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key
[/code]

Для конечной точки **China** :

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-standard-api-key-cn
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen/qwen3.5-plus" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qwen
[/code]

### Qwen OAuth / Portal

**Лучше всего подходит для:** токена Qwen Portal для `https://portal.qwen.ai/v1`.

См. [Qwen OAuth / Portal](</ru/providers/qwen-oauth>) для отдельной страницы провайдера и заметок о миграции.

* ### Provide your portal token

bashCopy code
[code]
    openclaw onboard --auth-choice qwen-oauth
[/code]

* ### Set a default model

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "qwen-oauth/qwen3.5-plus" },    },  },}
[/code]

* ### Verify the model is available

bashCopy code
[code]
    openclaw models list --provider qwen-oauth
[/code]

## Типы планов и конечные точки

План | Регион | Вариант аутентификации | Конечная точка  
---|---|---|---  
Standard (pay-as-you-go) | Китай | `qwen-standard-api-key-cn` | `dashscope.aliyuncs.com/compatible-mode/v1`  
Standard (pay-as-you-go) | Global | `qwen-standard-api-key` | `dashscope-intl.aliyuncs.com/compatible-mode/v1`  
Coding Plan (subscription) | Китай | `qwen-api-key-cn` | `coding.dashscope.aliyuncs.com/v1`  
Coding Plan (subscription) | Global | `qwen-api-key` | `coding-intl.dashscope.aliyuncs.com/v1`  
Qwen Portal | Global | `qwen-oauth` | `portal.qwen.ai/v1`  
  
Провайдер автоматически выбирает конечную точку на основе выбранного варианта аутентификации. Канонические варианты используют семейство `qwen-*`; `modelstudio-*` остается только для совместимости. Вы можете переопределить это пользовательским `baseUrl` в конфигурации.

## Встроенный каталог

В настоящее время OpenClaw поставляется с этим статическим каталогом Qwen. Настроенный каталог учитывает конечную точку: конфигурации Coding Plan исключают модели, о которых известно, что они работают только на конечной точке Standard.

Model ref | Ввод | Контекст | Примечания  
---|---|---|---  
`qwen/qwen3.5-plus` | текст, изображение | 1,000,000 | Модель по умолчанию  
`qwen/qwen3.6-plus` | текст, изображение | 1,000,000 | Предпочитайте конечные точки Standard, когда нужна эта модель  
`qwen/qwen3-max-2026-01-23` | текст | 262,144 | Линейка Qwen Max  
`qwen/qwen3-coder-next` | текст | 262,144 | Кодирование  
`qwen/qwen3-coder-plus` | текст | 1,000,000 | Кодирование  
`qwen/MiniMax-M2.5` | текст | 1,000,000 | Рассуждение включено  
`qwen/glm-5` | текст | 202,752 | GLM  
`qwen/glm-4.7` | текст | 202,752 | GLM  
`qwen/kimi-k2.5` | текст, изображение | 262,144 | Moonshot AI через Alibaba  
`qwen-oauth/qwen3.5-plus` | текст, изображение | 1,000,000 | Значение по умолчанию для Qwen Portal  
  
## Элементы управления мышлением

Для моделей Qwen Cloud с поддержкой рассуждения провайдер сопоставляет уровни мышления OpenClaw с флагом запроса верхнего уровня DashScope `enable_thinking`. Отключённое мышление отправляет `enable_thinking: false`; остальные уровни мышления отправляют `enable_thinking: true`.

## Мультимодальные дополнения

Plugin `qwen` также предоставляет мультимодальные возможности на конечных точках DashScope **Standard** (не на конечных точках Coding Plan):

  * **Понимание видео** через `qwen-vl-max-latest`
  * **Генерация видео Wan** через `wan2.6-t2v` (по умолчанию), `wan2.6-i2v`, `wan2.6-r2v`, `wan2.6-r2v-flash`, `wan2.7-r2v`


Чтобы использовать Qwen как видеопровайдера по умолчанию:

json5Copy code
[code]
    {  agents: {    defaults: {      videoGenerationModel: { primary: "qwen/wan2.6-t2v" },    },  },}
[/code]

## Расширенная конфигурация

Понимание изображений и видео

Plugin Qwen регистрирует понимание медиа для изображений и видео на конечных точках DashScope **Standard** (не на конечных точках Coding Plan).

Свойство | Значение  
---|---  
Модель | `qwen-vl-max-latest`  
Поддерживаемый ввод | Изображения, видео  
  
Понимание медиа автоматически определяется из настроенной авторизации Qwen — дополнительная конфигурация не нужна. Убедитесь, что вы используете конечную точку Standard (с оплатой по мере использования) для поддержки понимания медиа.

Доступность Qwen 3.6 Plus

`qwen3.6-plus` доступна на конечных точках Model Studio Standard (с оплатой по мере использования):

  * Китай: `dashscope.aliyuncs.com/compatible-mode/v1`
  * Global: `dashscope-intl.aliyuncs.com/compatible-mode/v1`


Если конечные точки Coding Plan возвращают ошибку "unsupported model" для `qwen3.6-plus`, переключитесь на Standard (с оплатой по мере использования) вместо пары конечной точки/ключа Coding Plan.

Статический каталог Qwen в OpenClaw не публикует `qwen3.6-plus` на конечных точках Coding Plan, но явно настроенные записи `qwen/qwen3.6-plus` в `models.providers.qwen.models` учитываются для baseUrls Coding Plan, поэтому вы можете подключить эту модель, если Aliyun включит её для вашей подписки. Вышестоящий API всё равно решает, будет ли вызов успешным.

План возможностей

Plugin `qwen` позиционируется как основное место поставщика для всей поверхности Qwen Cloud, а не только для моделей кодирования/текста.

  * **Текстовые/чат-модели:** доступны через Plugin
  * **Вызов инструментов, структурированный вывод, мышление:** наследуются от OpenAI-совместимого транспорта
  * **Генерация изображений:** запланирована на уровне provider-Plugin
  * **Понимание изображений/видео:** доступно через Plugin на конечной точке Standard
  * **Речь/аудио:** запланировано на уровне provider-Plugin
  * **Эмбеддинги памяти/переранжирование:** запланированы через поверхность адаптера эмбеддингов
  * **Генерация видео:** доступна через Plugin с помощью общей возможности генерации видео

Подробности генерации видео

Для генерации видео OpenClaw сопоставляет настроенный регион Qwen с соответствующим хостом DashScope AIGC перед отправкой задания:

  * Global/Intl: `https://dashscope-intl.aliyuncs.com`
  * Китай: `https://dashscope.aliyuncs.com`


Это означает, что обычный `models.providers.qwen.baseUrl`, указывающий либо на хосты Coding Plan, либо на хосты Standard Qwen, всё равно сохраняет генерацию видео на правильной региональной видеоконечной точке DashScope.

Текущие ограничения генерации видео Qwen:

  * До **1** выходного видео на запрос
  * До **1** входного изображения
  * До **4** входных видео
  * Длительность до **10 секунд**
  * Поддерживает `size`, `aspectRatio`, `resolution`, `audio` и `watermark`
  * Режим эталонного изображения/видео в настоящее время требует **удалённые URL-адреса http(s)**. Локальные пути к файлам отклоняются заранее, потому что видеоконечная точка DashScope не принимает загруженные локальные буферы для таких эталонов.

Совместимость использования потоковой передачи

Нативные конечные точки Model Studio заявляют о совместимости использования потоковой передачи на общем транспорте `openai-completions`. Теперь OpenClaw определяет это по возможностям конечной точки, поэтому пользовательские идентификаторы провайдеров, совместимые с DashScope и нацеленные на те же нативные хосты, наследуют то же поведение использования потоковой передачи, вместо того чтобы требовать именно встроенный идентификатор провайдера `qwen`.

Совместимость использования нативной потоковой передачи применяется как к хостам Coding Plan, так и к стандартным хостам, совместимым с DashScope:

  * `https://coding.dashscope.aliyuncs.com/v1`
  * `https://coding-intl.dashscope.aliyuncs.com/v1`
  * `https://dashscope.aliyuncs.com/compatible-mode/v1`
  * `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`

Регионы мультимодальных конечных точек

Мультимодальные поверхности (понимание видео и генерация видео Wan) используют **стандартные** конечные точки DashScope, а не конечные точки Coding Plan:

  * Глобальный/международный стандартный базовый URL: `https://dashscope-intl.aliyuncs.com/compatible-mode/v1`
  * Китайский стандартный базовый URL: `https://dashscope.aliyuncs.com/compatible-mode/v1`

Настройка окружения и демона

Если Gateway работает как демон (launchd/systemd), убедитесь, что `QWEN_API_KEY` доступен этому процессу (например, в `~/.openclaw/.env` или через `env.shellEnv`).

## Связанные материалы

[**Выбор модели** Выбор провайдеров, ссылок на модели и поведения при отказе. ](</ru/concepts/model-providers>) [**Генерация видео** Общие параметры инструмента видео и выбор провайдера. ](</ru/tools/video-generation>) [**Alibaba (ModelStudio)** Устаревший провайдер ModelStudio и примечания по миграции. ](</ru/providers/alibaba>) [**Устранение неполадок** Общее устранение неполадок и FAQ. ](</ru/help/troubleshooting>)

Was this useful?YesNo

Open issue