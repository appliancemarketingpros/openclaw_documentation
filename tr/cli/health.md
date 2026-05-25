---
title: Sağlık
source_url: https://docs.openclaw.ai/tr/cli/health
scraped_at: 2026-05-25
---

# `openclaw health`

Çalışan Gateway'den sağlık durumunu getirir.

## Seçenekler

Bayrak | Varsayılan | Açıklama  
---|---|---  
`--json` | `false` | Metin yerine makine tarafından okunabilir JSON yazdırır.  
`--timeout <ms>` | `10000` | Milisaniye cinsinden bağlantı zaman aşımı.  
`--verbose` | `false` | Ayrıntılı günlükleme. Canlı bir yoklamayı zorunlu kılar ve ajan başına çıktıyı genişletir.  
`--debug` | `false` | `--verbose` için takma ad.  
  
Örnekler:

bashCopy code
[code]
    openclaw healthopenclaw health --jsonopenclaw health --timeout 2500openclaw health --verboseopenclaw health --debug
[/code]

Notlar:

  * Varsayılan `openclaw health`, çalışan Gateway'den sağlık anlık görüntüsünü ister. Gateway'in zaten taze ve önbelleğe alınmış bir anlık görüntüsü varsa, bu önbelleğe alınmış yükü döndürebilir ve arka planda yenileyebilir.
  * `--verbose` canlı bir yoklamayı zorunlu kılar, Gateway bağlantı ayrıntılarını yazdırır ve insan tarafından okunabilir çıktıyı yapılandırılmış tüm hesaplar ve ajanlar genelinde genişletir.
  * Birden fazla ajan yapılandırıldığında çıktı, ajan başına oturum depolarını içerir.


## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Gateway sağlık durumu](</tr/gateway/health>)


Was this useful?YesNo