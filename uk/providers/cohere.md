---
title: Cohere
source_url: https://docs.openclaw.ai/uk/providers/cohere
scraped_at: 2026-06-29
---

ModelsProviders

[Cohere](<https://cohere.com>) надає OpenAI-сумісний інференс через свій Compatibility API. OpenClaw постачає провайдер Cohere під час переходу до екстерналізації, а також публікує його як офіційний зовнішній Plugin з каталогом моделей Command A.

Властивість | Значення  
---|---  
ID провайдера | `cohere`  
Plugin | вбудований під час переходу; офіційний зовнішній пакет  
Змінна середовища автентифікації | `COHERE_API_KEY`  
Прапорець онбордингу | `--auth-choice cohere-api-key`  
Прямий прапорець CLI | `--cohere-api-key <key>`  
API | OpenAI-сумісний (`openai-completions`)  
Базова URL-адреса | `https://api.cohere.ai/compatibility/v1`  
Модель за замовчуванням | `cohere/command-a-03-2025`  
  
## Початок роботи

  1. Cohere включено до поточних пакетів OpenClaw. Якщо він недоступний, установіть зовнішній пакет і перезапустіть Gateway:

bashCopy code
[code]
    openclaw plugins install @openclaw/cohere-provideropenclaw gateway restart
[/code]

  2. Створіть API-ключ Cohere.
  3. Запустіть онбординг:

bashCopy code
[code]
    openclaw onboard --non-interactive \  --auth-choice cohere-api-key \  --cohere-api-key "$COHERE_API_KEY"
[/code]

  4. Підтвердьте, що каталог доступний:

bashCopy code
[code]
    openclaw models list --provider cohere
[/code]

Модель за замовчуванням установлюється лише тоді, коли основну модель ще не налаштовано.

## Налаштування лише через середовище

Зробіть `COHERE_API_KEY` доступною для процесу Gateway, а потім виберіть модель Cohere:

json5Copy code
[code]
    {  agents: {    defaults: {      model: { primary: "cohere/command-a-03-2025" },    },  },}
[/code]

## Пов’язано

  * [Провайдери моделей](</uk/concepts/model-providers>)
  * [CLI моделей](</uk/cli/models>)
  * [Каталог провайдерів](</uk/providers>)


Was this useful?YesNo

Open issue