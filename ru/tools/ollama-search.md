---
title: Веб-поиск Ollama
source_url: https://docs.openclaw.ai/ru/tools/ollama-search
scraped_at: 2026-06-29
---

CapabilitiesTools

OpenClaw поддерживает **Ollama Web Search** как встроенный провайдер `web_search`. Он использует API веб-поиска Ollama и возвращает структурированные результаты с заголовками, URL и фрагментами.

Для локальной или самостоятельно размещенной Ollama эта настройка по умолчанию не требует API-ключа. Для нее требуется:

  * хост Ollama, доступный из OpenClaw
  * `ollama signin`


Для прямого размещенного поиска задайте базовый URL провайдера Ollama как `https://ollama.com` и укажите настоящий `OLLAMA_API_KEY`.

## Настройка

* ### Запустите Ollama

Убедитесь, что Ollama установлена и запущена.

* ### Войдите

Выполните:

bashCopy code
[code]
    ollama signin
[/code]

* ### Выберите Ollama Web Search

Выполните:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Затем выберите **Ollama Web Search** в качестве провайдера.

Если вы уже используете Ollama для моделей, Ollama Web Search повторно использует тот же настроенный хост.

## Конфигурация

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

Необязательное переопределение хоста Ollama:

json5Copy code
[code]
    {  plugins: {    entries: {      ollama: {        config: {          webSearch: {            baseUrl: "http://ollama-host:11434",          },        },      },    },  },}
[/code]

Если вы уже настраиваете Ollama как провайдера моделей, провайдер веб-поиска может вместо этого повторно использовать этот хост:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",      },    },  },}
[/code]

Провайдер моделей Ollama использует `baseUrl` как канонический ключ. Провайдер веб-поиска также учитывает `baseURL` в `models.providers.ollama` для совместимости с примерами конфигурации в стиле OpenAI SDK.

Если явный базовый URL Ollama не задан, OpenClaw использует `http://127.0.0.1:11434`.

Если ваш хост Ollama ожидает bearer-аутентификацию, OpenClaw повторно использует `models.providers.ollama.apiKey` (или соответствующую аутентификацию провайдера на основе env) для запросов к этому настроенному хосту.

Прямой размещенный Ollama Web Search:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",      },    },  },  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

## Примечания

  * Для этого провайдера не требуется отдельное поле API-ключа для веб-поиска.
  * Если хост Ollama защищен аутентификацией, OpenClaw повторно использует обычный API-ключ провайдера Ollama, когда он присутствует.
  * Если `baseUrl` равно `https://ollama.com`, OpenClaw напрямую вызывает `https://ollama.com/api/web_search` и отправляет настроенный API-ключ Ollama как bearer-аутентификацию.
  * Если настроенный хост не предоставляет веб-поиск и задан `OLLAMA_API_KEY`, OpenClaw может вернуться к `https://ollama.com/api/web_search` без отправки этого env-ключа на локальный хост.
  * OpenClaw предупреждает во время настройки, если Ollama недоступна или вход не выполнен, но не блокирует выбор.
  * OpenClaw не выбирает Ollama Web Search автоматически, когда не настроен провайдер с учетными данными с более высоким приоритетом; выберите его явно через `tools.web.search.provider: "ollama"`.
  * Хосты локального демона Ollama используют локальную прокси-точку `/api/experimental/web_search`, которая подписывает запросы и пересылает их в Ollama Cloud.
  * Хосты `https://ollama.com` используют публичную размещенную точку `/api/web_search` напрямую с bearer-аутентификацией по API-ключу.


## Связанные материалы

  * [Обзор Web Search](</ru/tools/web>) \-- все провайдеры и автообнаружение
  * [Ollama](</ru/providers/ollama>) \-- настройка моделей Ollama и облачный/локальный режимы


Was this useful?YesNo

Open issue