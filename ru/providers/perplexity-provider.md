---
title: Perplexity
source_url: https://docs.openclaw.ai/ru/providers/perplexity-provider
scraped_at: 2026-06-29
---

ModelsProviders

Plugin Perplexity предоставляет возможности веб-поиска через Perplexity Search API или Perplexity Sonar через OpenRouter.

Свойство | Значение  
---|---  
Тип | Поставщик веб-поиска (не поставщик моделей)  
Аутентификация | `PERPLEXITY_API_KEY` (напрямую) или `OPENROUTER_API_KEY` (через OpenRouter)  
Путь конфигурации | `plugins.entries.perplexity.config.webSearch.apiKey`  
  
## Установка Plugin

Установите официальный Plugin, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/perplexity-pluginopenclaw gateway restart
[/code]

## Начало работы

* ### Задайте ключ API

Запустите интерактивный поток настройки веб-поиска:

bashCopy code
[code]
    openclaw configure --section web
[/code]

Или задайте ключ напрямую:

bashCopy code
[code]
    openclaw config set plugins.entries.perplexity.config.webSearch.apiKey "pplx-xxxxxxxxxxxx"
[/code]

* ### Начните поиск

Агент будет автоматически использовать Perplexity для веб-поиска после настройки ключа. Дополнительные действия не требуются.

## Режимы поиска

Plugin автоматически выбирает транспорт на основе префикса ключа API:

### Нативный API Perplexity (pplx-)

Если ваш ключ начинается с `pplx-`, OpenClaw использует нативный Perplexity Search API. Этот транспорт возвращает структурированные результаты и поддерживает фильтры по домену, языку и дате (см. параметры фильтрации ниже).

### OpenRouter / Sonar (sk-or-)

Если ваш ключ начинается с `sk-or-`, OpenClaw выполняет маршрутизацию через OpenRouter с использованием модели Perplexity Sonar. Этот транспорт возвращает ответы, синтезированные ИИ, с цитатами.

Префикс ключа | Транспорт | Возможности  
---|---|---  
`pplx-` | Нативный Perplexity Search API | Структурированные результаты, фильтры по домену/языку/дате  
`sk-or-` | OpenRouter (Sonar) | Ответы, синтезированные ИИ, с цитатами  
  
## Фильтрация в нативном API

При использовании нативного API Perplexity поиск поддерживает следующие фильтры:

Фильтр | Описание | Пример  
---|---|---  
Страна | Двухбуквенный код страны | `us`, `de`, `jp`  
Язык | Код языка ISO 639-1 | `en`, `fr`, `zh`  
Диапазон дат | Окно давности | `day`, `week`, `month`, `year`  
Фильтры доменов | Список разрешенных или запрещенных доменов (макс. 20 доменов) | `example.com`  
Бюджет содержимого | Лимиты токенов на ответ / на страницу | `max_tokens`, `max_tokens_per_page`  
  
## Расширенная конфигурация

Переменная окружения для процессов-демонов

Если OpenClaw Gateway работает как демон (launchd/systemd), убедитесь, что `PERPLEXITY_API_KEY` доступен этому процессу.

Настройка прокси OpenRouter

Если вы предпочитаете направлять поисковые запросы Perplexity через OpenRouter, задайте `OPENROUTER_API_KEY` (префикс `sk-or-`) вместо нативного ключа Perplexity. OpenClaw определит префикс и автоматически переключится на транспорт Sonar.

## Связанные материалы

[**Инструмент поиска Perplexity** Как агент вызывает поиски Perplexity и интерпретирует результаты. ](</ru/tools/perplexity-search>) [**Справочник по конфигурации** Полный справочник по конфигурации, включая записи Plugin. ](</ru/gateway/configuration-reference>)

Was this useful?YesNo

Open issue