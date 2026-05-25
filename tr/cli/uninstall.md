---
title: Kaldırma
source_url: https://docs.openclaw.ai/tr/cli/uninstall
scraped_at: 2026-05-25
---

# `openclaw uninstall`

Gateway hizmetini + yerel verileri kaldırın (CLI kalır).

Seçenekler:

  * `--service`: Gateway hizmetini kaldır
  * `--state`: durumu ve yapılandırmayı kaldır
  * `--workspace`: çalışma alanı dizinlerini kaldır
  * `--app`: macOS uygulamasını kaldır
  * `--all`: hizmeti, durumu, çalışma alanını ve uygulamayı kaldır
  * `--yes`: onay istemlerini atla
  * `--non-interactive`: istemleri devre dışı bırakır; `--yes` gerektirir
  * `--dry-run`: dosyaları kaldırmadan eylemleri yazdır


Örnekler:

bashCopy code
[code]
    openclaw backup createopenclaw uninstallopenclaw uninstall --service --yes --non-interactiveopenclaw uninstall --state --workspace --yes --non-interactiveopenclaw uninstall --all --yesopenclaw uninstall --dry-run
[/code]

Notlar:

  * Durumu veya çalışma alanlarını kaldırmadan önce geri yüklenebilir bir anlık görüntü istiyorsanız önce `openclaw backup create` çalıştırın.
  * `--all`, hizmeti, durumu, çalışma alanını ve uygulamayı birlikte kaldırmanın kısa yoludur.
  * `--non-interactive`, `--yes` gerektirir.


## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Kaldırma](</tr/install/uninstall>)


Was this useful?YesNo