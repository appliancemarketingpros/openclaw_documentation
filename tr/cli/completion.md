---
title: Tamamlama
source_url: https://docs.openclaw.ai/tr/cli/completion
scraped_at: 2026-05-25
---

# `openclaw completion`

Kabuk tamamlama betiklerini oluşturun ve isteğe bağlı olarak bunları kabuk profilinize yükleyin.

## Kullanım

bashCopy code
[code]
    openclaw completionopenclaw completion --shell zshopenclaw completion --installopenclaw completion --shell fish --installopenclaw completion --write-stateopenclaw completion --shell bash --write-state
[/code]

## Seçenekler

  * `-s, --shell <shell>`: kabuk hedefi (`zsh`, `bash`, `powershell`, `fish`; varsayılan: `zsh`)
  * `-i, --install`: kabuk profilinize bir source satırı ekleyerek tamamlamayı yükle
  * `--write-state`: tamamlama betiklerini stdout'a yazdırmadan `$OPENCLAW_STATE_DIR/completions` içine yaz
  * `-y, --yes`: yükleme onay istemlerini atla


## Notlar

  * `--install`, kabuk profilinize küçük bir "OpenClaw Completion" bloğu yazar ve bunu önbelleğe alınmış betiğe yönlendirir.
  * `--install` veya `--write-state` olmadan komut betiği stdout'a yazdırır.
  * Tamamlama oluşturma, iç içe alt komutların dahil edilmesi için komut ağaçlarını eager olarak yükler.


## İlgili

  * [CLI başvurusu](</tr/cli>)


Was this useful?YesNo