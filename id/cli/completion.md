---
title: Completion
source_url: https://docs.openclaw.ai/id/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

Buat skrip shell completion dan opsional pasang ke profil shell Anda.

## Penggunaan

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Opsi

  * `-s, --shell <shell>`: target shell (`zsh`, `bash`, `powershell`, `fish`; default: `zsh`)
  * `-i, --install`: pasang completion dengan menambahkan baris source ke profil shell Anda
  * `--write-state`: tulis skrip completion ke `$OPENCLAW_STATE_DIR/completions` tanpa mencetak ke stdout
  * `-y, --yes`: lewati prompt konfirmasi pemasangan


## Catatan

  * `--install` menulis blok kecil "OpenClaw Completion" ke dalam profil shell Anda dan mengarahkannya ke skrip cache.
  * Tanpa `--install` atau `--write-state`, perintah mencetak skrip ke stdout.
  * Pembuatan completion memuat pohon perintah secara eager sehingga subperintah bertingkat disertakan.


## Terkait

  * [Referensi CLI](</id/cli>)


Was this useful?YesNo