---
title: API OpenResponses
source_url: https://docs.openclaw.ai/ru/gateway/openresponses-http-api
scraped_at: 2026-06-29
---

Gateway & OpsGateway

OpenClaw Gateway может предоставлять совместимую с OpenResponses конечную точку `POST /v1/responses`.

Эта конечная точка **по умолчанию отключена**. Сначала включите ее в конфигурации.

  * `POST /v1/responses`
  * Тот же порт, что и у Gateway (мультиплексирование WS + HTTP): `http://<gateway-host>:<port>/v1/responses`


Под капотом запросы выполняются как обычный запуск агента Gateway (тот же путь кода, что и `openclaw agent`), поэтому маршрутизация, разрешения и конфигурация соответствуют вашему Gateway.

## Аутентификация, безопасность и маршрутизация

Операционное поведение соответствует [OpenAI Chat Completions](</ru/gateway/openai-http-api>):

  * используйте соответствующий путь HTTP-аутентификации Gateway: 
    * аутентификация с общим секретом (`gateway.auth.mode="token"` или `"password"`): `Authorization: Bearer <token-or-password>`
    * аутентификация через доверенный прокси (`gateway.auth.mode="trusted-proxy"`): прокси-заголовки с учетом идентичности от настроенного доверенного источника прокси; прокси same-host loopback требуют явного `gateway.auth.trustedProxy.allowLoopback = true`
    * локальный прямой резервный вариант для доверенного прокси: вызывающие на том же хосте без заголовков `Forwarded`, `X-Forwarded-*` или `X-Real-IP` могут использовать `gateway.auth.password` / `OPENCLAW_GATEWAY_PASSWORD`
    * открытая аутентификация для приватного входящего трафика (`gateway.auth.mode="none"`): без заголовка аутентификации
  * рассматривайте конечную точку как полный операторский доступ к экземпляру gateway
  * для режимов аутентификации с общим секретом (`token` и `password`) игнорируйте более узкие значения `x-openclaw-scopes`, объявленные bearer-токеном, и восстанавливайте обычные полные операторские значения по умолчанию
  * для доверенных HTTP-режимов с идентичностью (например, аутентификация через доверенный прокси или `gateway.auth.mode="none"`) учитывайте `x-openclaw-scopes`, когда они присутствуют, иначе возвращайтесь к обычному набору операторских областей по умолчанию
  * выбирайте агентов с `model: "openclaw"`, `model: "openclaw/default"`, `model: "openclaw/<agentId>"` или `x-openclaw-agent-id`
  * используйте `x-openclaw-model`, когда хотите переопределить backend-модель выбранного агента
  * используйте `x-openclaw-session-key` для явной маршрутизации сессии
  * используйте `x-openclaw-message-channel`, когда нужен нестандартный синтетический контекст входящего канала


Матрица аутентификации:

  * `gateway.auth.mode="token"` или `"password"` \+ `Authorization: Bearer ...`
    * подтверждает владение общим операторским секретом gateway
    * игнорирует более узкие `x-openclaw-scopes`
    * восстанавливает полный операторский набор областей по умолчанию: `operator.admin`, `operator.approvals`, `operator.pairing`, `operator.read`, `operator.talk.secrets`, `operator.write`
    * рассматривает ходы чата на этой конечной точке как ходы отправителя-владельца
  * доверенные HTTP-режимы с идентичностью (например, аутентификация через доверенный прокси или `gateway.auth.mode="none"` для приватного входящего трафика) 
    * учитывают `x-openclaw-scopes`, когда заголовок присутствует
    * возвращаются к обычному операторскому набору областей по умолчанию, когда заголовок отсутствует
    * теряют семантику владельца только тогда, когда вызывающий явно сужает области и опускает `operator.admin`


Включите или отключите эту конечную точку с помощью `gateway.http.endpoints.responses.enabled`.

Та же поверхность совместимости также включает:

  * `GET /v1/models`
  * `GET /v1/models/{id}`
  * `POST /v1/embeddings`
  * `POST /v1/chat/completions`


Каноническое объяснение того, как agent-target модели, `openclaw/default`, сквозная передача embeddings и переопределения backend-моделей сочетаются между собой, см. в [OpenAI Chat Completions](</ru/gateway/openai-http-api#agent-first-model-contract>) и [Список моделей и маршрутизация агентов](</ru/gateway/openai-http-api#model-list-and-agent-routing>).

## Поведение сессии

По умолчанию конечная точка **не сохраняет состояние между запросами** (при каждом вызове генерируется новый ключ сессии).

Если запрос включает строку OpenResponses `user`, Gateway выводит из нее стабильный ключ сессии, чтобы повторные вызовы могли совместно использовать сессию агента.

## Форма запроса (поддерживается)

Запрос следует API OpenResponses с item-based input. Текущая поддержка:

  * `input`: строка или массив объектов элементов.
  * `instructions`: объединяется с системным prompt.
  * `tools`: определения клиентских инструментов (function tools).
  * `tool_choice`: `"auto"`, `"none"`, `"required"` или `{ "type": "function", "name": "..." }` для фильтрации или обязательного использования клиентских инструментов.
  * `stream`: включает потоковую передачу SSE.
  * `max_output_tokens`: best-effort ограничение вывода (зависит от provider).
  * `temperature`: best-effort температура сэмплирования, передаваемая provider. Игнорируется backend Codex Responses на основе ChatGPT, который использует фиксированное серверное сэмплирование.
  * `top_p`: best-effort nucleus sampling, передаваемый provider. То же предупреждение Codex Responses, что и для `temperature`.
  * `user`: стабильная маршрутизация сессии.


Принимаются, но **в настоящее время игнорируются** :

  * `max_tool_calls`
  * `reasoning`
  * `metadata`
  * `store`
  * `truncation`


Поддерживается:

  * `previous_response_id`: OpenClaw повторно использует более раннюю сессию ответа, когда запрос остается в пределах той же области агента/пользователя/запрошенной сессии.


## Элементы (`input`)

### `message`

Роли: `system`, `developer`, `user`, `assistant`.

  * `system` и `developer` добавляются к системному prompt.
  * Самый последний элемент `user` или `function_call_output` становится «текущим сообщением».
  * Более ранние сообщения пользователя/ассистента включаются как история для контекста.


### `function_call_output` (инструменты на основе хода)

Отправляйте результаты инструмента обратно модели:

jsonCopy code
[code]
    {  "type": "function_call_output",  "call_id": "call_123",  "output": "{\"temperature\": \"72F\"}"}
[/code]

### `reasoning` и `item_reference`

Принимаются для совместимости схемы, но игнорируются при построении prompt.

## Инструменты (клиентские function tools)

Предоставляйте инструменты с `tools: [{ type: "function", name, description?, parameters? }]`.

Если агент решает вызвать инструмент, ответ возвращает выходной элемент `function_call`. Затем отправьте последующий запрос с `function_call_output`, чтобы продолжить ход.

Для `tool_choice: "required"` и закрепленного за функцией `tool_choice` конечная точка сужает открытый набор клиентских function-tool, инструктирует runtime вызвать клиентский инструмент перед ответом и отклоняет ход, если он не включает соответствующий структурированный вызов клиентского инструмента. Этот контракт применяется к переданному вызывающим списку HTTP `tools`, а не ко всем внутренним инструментам агента OpenClaw. Непотоковые запросы возвращают `502` с `api_error`; потоковые запросы отправляют событие `response.failed`. Это соответствует контракту `/v1/chat/completions`.

## Изображения (`input_image`)

Поддерживает источники base64 или URL:

jsonCopy code
[code]
    {  "type": "input_image",  "source": { "type": "url", "url": "https://example.com/image.png" }}
[/code]

Разрешенные MIME-типы (текущие): `image/jpeg`, `image/png`, `image/gif`, `image/webp`, `image/heic`, `image/heif`. Максимальный размер (текущий): 10MB.

## Файлы (`input_file`)

Поддерживает источники base64 или URL:

jsonCopy code
[code]
    {  "type": "input_file",  "source": {    "type": "base64",    "media_type": "text/plain",    "data": "SGVsbG8gV29ybGQh",    "filename": "hello.txt"  }}
[/code]

Разрешенные MIME-типы (текущие): `text/plain`, `text/markdown`, `text/html`, `text/csv`, `application/json`, `application/pdf`.

Максимальный размер (текущий): 5MB.

Текущее поведение:

  * Содержимое файла декодируется и добавляется в **системный prompt** , а не в сообщение пользователя, поэтому оно остается эфемерным (не сохраняется в истории сессии).
  * Декодированный текст файла оборачивается как **недоверенное внешнее содержимое** перед добавлением, поэтому байты файла рассматриваются как данные, а не как доверенные инструкции.
  * Вставленный блок использует явные маркеры границ, такие как `<<&lt;EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>` / `<<&lt;END_EXTERNAL_UNTRUSTED_CONTENT id=&quot;...&quot;&gt;>>`, и включает строку метаданных `Source: External`.
  * Этот путь ввода файлов намеренно опускает длинный баннер `SECURITY NOTICE:`, чтобы сохранить бюджет prompt; маркеры границ и метаданные при этом остаются на месте.
  * PDF сначала разбираются на текст. Если текста найдено мало, первые страницы растеризуются в изображения и передаются модели, а вставленный файловый блок использует placeholder `[PDF content rendered to images]`.


Разбор PDF обеспечивается встроенным Plugin `document-extract`, который использует `clawpdf` и его упакованный runtime PDFium WebAssembly для извлечения текста и рендеринга страниц.

Настройки URL-fetch по умолчанию:

  * `files.allowUrl`: `true`
  * `images.allowUrl`: `true`
  * `maxUrlParts`: `8` (всего частей на основе URL `input_file` \+ `input_image` на запрос)
  * Запросы защищены (разрешение DNS, блокировка приватных IP, ограничения перенаправлений, таймауты).
  * Поддерживаются необязательные списки разрешенных имен хостов для каждого типа ввода (`files.urlAllowlist`, `images.urlAllowlist`). 
    * Точный хост: `"cdn.example.com"`
    * Подстановочные поддомены: `"*.assets.example.com"` (не совпадает с apex)
    * Пустые или опущенные списки разрешений означают отсутствие ограничения по списку разрешенных хостов.
  * Чтобы полностью отключить fetch на основе URL, задайте `files.allowUrl: false` и/или `images.allowUrl: false`.


## Ограничения файлов и изображений (конфигурация)

Значения по умолчанию можно настроить в `gateway.http.endpoints.responses`:

json5Copy code
[code]
    {  gateway: {    http: {      endpoints: {        responses: {          enabled: true,          maxBodyBytes: 20000000,          maxUrlParts: 8,          files: {            allowUrl: true,            urlAllowlist: ["cdn.example.com", "*.assets.example.com"],            allowedMimes: [              "text/plain",              "text/markdown",              "text/html",              "text/csv",              "application/json",              "application/pdf",            ],            maxBytes: 5242880,            maxChars: 200000,            maxRedirects: 3,            timeoutMs: 10000,            pdf: {              maxPages: 4,              maxPixels: 4000000,              minTextChars: 200,            },          },          images: {            allowUrl: true,            urlAllowlist: ["images.example.com"],            allowedMimes: [              "image/jpeg",              "image/png",              "image/gif",              "image/webp",              "image/heic",              "image/heif",            ],            maxBytes: 10485760,            maxRedirects: 3,            timeoutMs: 10000,          },        },      },    },  },}
[/code]

Значения по умолчанию, если опущены:

  * `maxBodyBytes`: 20MB
  * `maxUrlParts`: 8
  * `files.maxBytes`: 5MB
  * `files.maxChars`: 200k
  * `files.maxRedirects`: 3
  * `files.timeoutMs`: 10s
  * `files.pdf.maxPages`: 4
  * `files.pdf.maxPixels`: 4,000,000
  * `files.pdf.minTextChars`: 200
  * `images.maxBytes`: 10MB
  * `images.maxRedirects`: 3
  * `images.timeoutMs`: 10s
  * Источники HEIC/HEIF `input_image` принимаются, когда доступен системный конвертер, и нормализуются в JPEG перед доставкой provider. Поддерживаемые конвертеры: macOS `sips`, ImageMagick, GraphicsMagick или ffmpeg.


Примечание по безопасности:

  * Списки разрешенных URL применяются перед fetch и на шагах перенаправления.
  * Внесение имени хоста в список разрешенных не обходит блокировку приватных/внутренних IP.
  * Для gateway, доступных из интернета, применяйте сетевые ограничения исходящего трафика в дополнение к защитам на уровне приложения. См. [Безопасность](</ru/gateway/security>).


## Потоковая передача (SSE)

Задайте `stream: true`, чтобы получать Server-Sent Events (SSE):

  * `Content-Type: text/event-stream`
  * Каждая строка события имеет вид `event: <type>` и `data: <json>`
  * Поток завершается `data: [DONE]`


Типы событий, отправляемые в настоящее время:

  * `response.created`
  * `response.in_progress`
  * `response.output_item.added`
  * `response.content_part.added`
  * `response.output_text.delta`
  * `response.output_text.done`
  * `response.content_part.done`
  * `response.output_item.done`
  * `response.completed`
  * `response.failed` (при ошибке)


## Использование

`usage` заполняется, когда базовый provider сообщает счетчики токенов. OpenClaw нормализует распространенные псевдонимы в стиле OpenAI до того, как эти счетчики попадут в последующие поверхности статуса/сессии, включая `input_tokens` / `output_tokens` и `prompt_tokens` / `completion_tokens`.

## Ошибки

Ошибки используют JSON-объект вида:

jsonCopy code
[code]
    { "error": { "message": "...", "type": "invalid_request_error" } }
[/code]

Распространенные случаи:

  * `401` отсутствует/недействительна аутентификация
  * `400` недействительное тело запроса
  * `405` неправильный метод


## Примеры

Без потоковой передачи:

bashCopy code
[code]
    curl -sS http://127.0.0.1:18789/v1/responses \  -H 'Authorization: Bearer YOUR_TOKEN' \  -H 'Content-Type: application/json' \  -H 'x-openclaw-agent-id: main' \  -d '{    "model": "openclaw",    "input": "hi"  }'
[/code]

Потоковая передача:

bashCopy code
[code]
    curl -N http://127.0.0.1:18789/v1/responses \  -H 'Authorization: Bearer YOUR_TOKEN' \  -H 'Content-Type: application/json' \  -H 'x-openclaw-agent-id: main' \  -d '{    "model": "openclaw",    "stream": true,    "input": "hi"  }'
[/code]

## Связанные материалы

  * [завершения чатов OpenAI](</ru/gateway/openai-http-api>)
  * [OpenAI](</ru/providers/openai>)


Was this useful?YesNo

Open issue