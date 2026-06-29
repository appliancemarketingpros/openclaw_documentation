---
title: Умовні позначення заповнювачів секретів
source_url: https://docs.openclaw.ai/uk/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Умовні позначення заповнювачів для секретів

Використовуйте заповнювачі, які зрозумілі людині, але не схожі на справжні секрети.

## Рекомендований стиль

  * Надавайте перевагу описовим значенням, як-от `example-openai-key-not-real` або `example-discord-bot-token`.
  * Для фрагментів shell надавайте перевагу `${OPENAI_API_KEY}` замість вбудованих рядків, схожих на токени.
  * Залишайте приклади очевидно фальшивими й обмеженими конкретною метою (провайдер, канал, тип автентифікації).


## Уникайте цих шаблонів у документації

  * Буквальний текст заголовка або нижнього колонтитула приватного ключа PEM.
  * Префікси, схожі на реальні облікові дані, наприклад `sk-...`, `xoxb-...`, `AKIA...`.
  * Bearer-токени реалістичного вигляду, скопійовані з runtime-журналів.


## Приклад

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue