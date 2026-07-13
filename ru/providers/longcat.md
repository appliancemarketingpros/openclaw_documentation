---
title: LongCat
source_url: https://docs.openclaw.ai/ru/providers/longcat
scraped_at: 2026-07-13
---

ModelsProviders

[LongCat](<https://longcat.ai>) предоставляет размещаемый API для LongCat-2.0 — модели с поддержкой рассуждений, созданной для программирования и агентных рабочих нагрузок. OpenClaw предоставляет официальный плагин `longcat` для совместимой с OpenAI конечной точки LongCat.

Свойство | Значение  
---|---  
Поставщик | `longcat`  
Аутентификация | `LONGCAT_API_KEY`  
API | Совместимый с OpenAI Chat Completions API  
Базовый URL | `https://api.longcat.chat/openai`  
Модель | `longcat/LongCat-2.0`  
Контекст | 1 048 576 токенов  
Макс. вывод | 131 072 токена  
Входные данные | Текст  
  
## Установка плагина

Установите официальный пакет, затем перезапустите Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/longcat-provideropenclaw gateway restart
[/code]

## Начало работы

* ### Создание ключа API

Войдите на [платформу LongCat API](<https://longcat.chat/platform/>) и создайте ключ на странице [API Keys](<https://longcat.chat/platform/api_keys>).

* ### Запуск первоначальной настройки

bashCopy code
[code]
    openclaw onboard --auth-choice longcat-api-key
[/code]

* ### Проверка модели

bashCopy code
[code]
    openclaw models list --provider longcat
[/code]

Первоначальная настройка добавляет размещаемый каталог и выбирает `longcat/LongCat-2.0`, если основная модель ещё не настроена.

### Неинтерактивная настройка

bashCopy code
[code]
    openclaw onboard --non-interactive \  --mode local \  --auth-choice longcat-api-key \  --longcat-api-key "$LONGCAT_API_KEY"
[/code]

## Поведение рассуждений

LongCat предоставляет двоичное управление размышлениями. OpenClaw сопоставляет включённые уровни размышлений с `thinking: { type: "enabled" }`, а `/think off` — с `thinking: { type: "disabled" }`. В настоящее время LongCat не документирует `reasoning_effort`, поэтому OpenClaw не отправляет этот параметр.

LongCat возвращает рассуждения в поле `reasoning_content`. OpenClaw сохраняет это поле при повторном воспроизведении ходов ассистента с вызовами инструментов, чтобы в многоходовых агентных сеансах сохранялась ожидаемая поставщиком структура сообщений.

## Цены

Встроенный каталог использует стандартные цены LongCat с оплатой по мере использования в долларах США за миллион токенов: $0.75 за некэшированные входные токены, $0.015 за кэшированные входные токены и $2.95 за выходные токены. LongCat может предлагать временные скидки; актуальными источниками являются [страница с ценами](<https://longcat.chat/platform/docs/Pricing/LongCat-2.0.html>) и ваши платёжные записи.

## Самостоятельное размещение LongCat-2.0

Поставщик `longcat` предназначен для размещаемого API LongCat. Чтобы использовать модель с открытыми весами из [Hugging Face](<https://huggingface.co/meituan-longcat/LongCat-2.0>), запустите её через совместимую с OpenAI среду выполнения и вместо этого используйте существующего поставщика OpenClaw [vLLM](</ru/providers/vllm>) или [SGLang](</ru/providers/sglang>).

Сохраните точный идентификатор модели среды выполнения в каталоге самостоятельно размещаемого поставщика; не направляйте локальное развёртывание через `longcat/LongCat-2.0`.

## Устранение неполадок

Ключ работает в оболочке, но не в Gateway

Управляемые демоном процессы Gateway наследуют не все переменные интерактивной оболочки. Поместите `LONGCAT_API_KEY` в `~/.openclaw/.env`, настройте его при первоначальной настройке или используйте разрешённую ссылку на секрет.

Запросы завершаются ошибкой 402 или 429

`402` означает, что у учётной записи недостаточно квоты токенов. `429` означает, что ключ API достиг ограничения частоты запросов. Проверьте [использование LongCat](<https://longcat.chat/platform/usage>) и повторите запросы с ограниченной частотой после завершения заданного поставщиком периода ожидания.

Модель не отображается

Выполните `openclaw plugins list` и убедитесь, что плагин `longcat` включён, затем выполните `openclaw models list --provider longcat`.

## Связанные материалы

[**Поставщики моделей** Настройка поставщиков, ссылки на модели и поведение при переключении после сбоя. ](</ru/concepts/model-providers>) [**Документация LongCat API** Конечные точки размещаемого API, аутентификация, ограничения и примеры. ](<https://longcat.chat/platform/docs/>) [**Карточка модели LongCat-2.0** Архитектура, рекомендации по развёртыванию и сведения о модели. ](<https://huggingface.co/meituan-longcat/LongCat-2.0>) [**Секреты** Хранение учётных данных поставщика без добавления открытого текста в конфигурацию. ](</ru/gateway/secrets>)

Was this useful?YesNo

Open issue