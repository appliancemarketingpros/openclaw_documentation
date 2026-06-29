---
title: Konvensi Placeholder Rahasia
source_url: https://docs.openclaw.ai/id/reference/secret-placeholder-conventions
scraped_at: 2026-06-29
---

Get started

# Konvensi placeholder rahasia

Gunakan placeholder yang mudah dibaca manusia tetapi tidak menyerupai rahasia sungguhan.

## Gaya yang disarankan

  * Utamakan nilai deskriptif seperti `example-openai-key-not-real` atau `example-discord-bot-token`.
  * Untuk cuplikan shell, utamakan `${OPENAI_API_KEY}` daripada string inline yang menyerupai token.
  * Pastikan contoh jelas palsu dan dibatasi sesuai tujuan (penyedia, saluran, jenis autentikasi).


## Hindari pola ini dalam dokumentasi

  * Teks header atau footer kunci privat PEM literal.
  * Prefiks yang menyerupai kredensial aktif, misalnya `sk-...`, `xoxb-...`, `AKIA...`.
  * Token bearer yang tampak realistis dan disalin dari log runtime.


## Contoh

bashCopy code
[code]
    # Goodexport OPENAI_API_KEY="example-openai-key-not-real" # Better (when the doc is about env wiring)export OPENAI_API_KEY="${OPENAI_API_KEY}"
[/code]

Was this useful?YesNo

Open issue