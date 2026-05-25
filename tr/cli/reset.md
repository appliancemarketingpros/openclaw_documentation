---
title: Sıfırla
source_url: https://docs.openclaw.ai/tr/cli/reset
scraped_at: 2026-05-25
---

# `openclaw reset`

Yerel config/durumu sıfırlayın (CLI kurulu kalır).

Seçenekler:

  * `--scope <scope>`: `config`, `config+creds+sessions` veya `full`
  * `--yes`: onay istemlerini atla
  * `--non-interactive`: istemleri devre dışı bırak; `--scope` ve `--yes` gerektirir
  * `--dry-run`: dosyaları kaldırmadan eylemleri yazdır


Örnekler:

bashCopy code
[code]
    openclaw backup createopenclaw resetopenclaw reset --dry-runopenclaw reset --scope config --yes --non-interactiveopenclaw reset --scope config+creds+sessions --yes --non-interactiveopenclaw reset --scope full --yes --non-interactive
[/code]

Notlar:

  * Yerel durumu kaldırmadan önce geri yüklenebilir bir anlık görüntü istiyorsanız önce `openclaw backup create` çalıştırın.
  * `--scope` değerini atlayırsanız, `openclaw reset` neyin kaldırılacağını seçmek için etkileşimli bir istem kullanır.
  * `--non-interactive` yalnızca hem `--scope` hem de `--yes` ayarlı olduğunda geçerlidir.


## İlgili

  * [CLI reference](</tr/cli>)


Was this useful?YesNo