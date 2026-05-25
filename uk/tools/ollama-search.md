---
title: вебпошук Ollama
source_url: https://docs.openclaw.ai/uk/tools/ollama-search
scraped_at: 2026-05-25
---

OpenClaw підтримує **вебпошук Ollama** як вбудований постачальник `web_search`. Він використовує API вебпошуку Ollama і повертає структуровані результати із заголовками, URL-адресами та фрагментами.

Для локального або самостійно розміщеного Ollama це налаштування типово не потребує API-ключа. Однак потрібні:

  * хост Ollama, до якого OpenClaw може підключитися
  * `ollama signin`


Для прямого розміщеного пошуку встановіть базову URL-адресу постачальника Ollama як `https://ollama.com` і вкажіть справжній `OLLAMA_API_KEY`.

## Налаштування

* ### Запустіть Ollama

Переконайтеся, що Ollama встановлено та запущено.

* ### Увійдіть

Виконайте:

bashCopy code
[code]
    ollama signin
[/code]

* ### Виберіть вебпошук Ollama

Виконайте:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Потім виберіть **вебпошук Ollama** як постачальника.

Якщо ви вже використовуєте Ollama для моделей, вебпошук Ollama повторно використовує той самий налаштований хост.

## Конфігурація

json5Copy code
[code]
    {  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

Необов’язкове перевизначення хоста Ollama:

json5Copy code
[code]
    {  plugins: {    entries: {      ollama: {        config: {          webSearch: {            baseUrl: "http://ollama-host:11434",          },        },      },    },  },}
[/code]

Якщо ви вже налаштовуєте Ollama як постачальника моделей, постачальник вебпошуку може повторно використовувати цей хост:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "http://ollama-host:11434",      },    },  },}
[/code]

Постачальник моделей Ollama використовує `baseUrl` як канонічний ключ. Постачальник вебпошуку також підтримує `baseURL` у `models.providers.ollama` для сумісності з прикладами конфігурації в стилі OpenAI SDK.

Якщо явну базову URL-адресу Ollama не задано, OpenClaw використовує `http://127.0.0.1:11434`.

Якщо ваш хост Ollama очікує bearer-автентифікацію, OpenClaw повторно використовує `models.providers.ollama.apiKey` (або відповідну автентифікацію постачальника, підкріплену змінними середовища) для запитів до цього налаштованого хоста.

Прямий розміщений вебпошук Ollama:

json5Copy code
[code]
    {  models: {    providers: {      ollama: {        baseUrl: "https://ollama.com",        apiKey: "OLLAMA_API_KEY",      },    },  },  tools: {    web: {      search: {        provider: "ollama",      },    },  },}
[/code]

## Примітки

  * Для цього постачальника не потрібне окреме поле API-ключа саме для вебпошуку.
  * Якщо хост Ollama захищено автентифікацією, OpenClaw повторно використовує звичайний API-ключ постачальника Ollama, якщо його задано.
  * Якщо `baseUrl` дорівнює `https://ollama.com`, OpenClaw викликає `https://ollama.com/api/web_search` напряму й надсилає налаштований API-ключ Ollama як bearer-автентифікацію.
  * Якщо налаштований хост не надає вебпошук і встановлено `OLLAMA_API_KEY`, OpenClaw може повернутися до `https://ollama.com/api/web_search`, не надсилаючи цей ключ змінної середовища на локальний хост.
  * Під час налаштування OpenClaw попереджає, якщо Ollama недоступний або не виконано вхід, але це не блокує вибір.
  * Автовизначення під час виконання може повернутися до вебпошуку Ollama, якщо не налаштовано жодного постачальника з вищим пріоритетом і обліковими даними.
  * Локальні хости демона Ollama використовують локальну проксі-кінцеву точку `/api/experimental/web_search`, яка підписує та пересилає запити в Ollama Cloud.
  * Хости `https://ollama.com` використовують публічну розміщену кінцеву точку `/api/web_search` напряму з bearer-автентифікацією API-ключем.


## Пов’язане

  * [Огляд вебпошуку](</uk/tools/web>) \-- усі постачальники та автовизначення
  * [Ollama](</uk/providers/ollama>) \-- налаштування моделі Ollama та хмарні/локальні режими


Was this useful?YesNo