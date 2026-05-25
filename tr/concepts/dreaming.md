---
title: Dreaming
source_url: https://docs.openclaw.ai/tr/concepts/dreaming
scraped_at: 2026-05-25
---

Dreaming, `memory-core` içindeki arka plan bellek pekiştirme sistemidir. OpenClaw’ın güçlü kısa vadeli sinyalleri kalıcı belleğe taşımasına yardımcı olurken süreci açıklanabilir ve incelenebilir tutar.

## Dreaming ne yazar

Dreaming iki tür çıktı tutar:

  * `memory/.dreams/` içinde **makine durumu** (geri çağırma deposu, faz sinyalleri, içe alma kontrol noktaları, kilitler).
  * `DREAMS.md` içinde (veya mevcut `dreams.md`) **insan tarafından okunabilir çıktı** ve isteğe bağlı olarak `memory/dreaming/<phase>/YYYY-MM-DD.md` altında faz raporu dosyaları.


Uzun vadeli yükseltme hâlâ yalnızca `MEMORY.md` dosyasına yazar.

## Faz modeli

Dreaming üç işbirlikçi faz kullanır:

Faz | Amaç | Kalıcı yazma  
---|---|---  
Light | Son kısa vadeli malzemeyi sıralayıp hazırlar | Hayır  
Deep | Kalıcı adayları puanlayıp yükseltir | Evet (`MEMORY.md`)  
REM | Temalar ve yinelenen fikirler üzerine düşünür | Hayır  
  
Bu fazlar ayrı kullanıcı yapılandırmalı "modlar" değil, dahili uygulama ayrıntılarıdır.

Light fazı

Light fazı son günlük bellek sinyallerini ve geri çağırma izlerini içe alır, tekilleştirir ve aday satırları hazırlar.

  * Kısa vadeli geri çağırma durumundan, son günlük bellek dosyalarından ve mevcut olduğunda düzeltilmiş oturum dökümlerinden okur.
  * Depolama satır içi çıktı içerdiğinde yönetilen bir `## Light Sleep` bloğu yazar.
  * Daha sonraki deep sıralaması için pekiştirme sinyallerini kaydeder.
  * `MEMORY.md` dosyasına asla yazmaz.

Deep fazı

Deep fazı neyin uzun vadeli bellek olacağına karar verir.

  * Adayları ağırlıklı puanlama ve eşik kapıları kullanarak sıralar.
  * Geçmek için `minScore`, `minRecallCount` ve `minUniqueQueries` gerektirir.
  * Yazmadan önce canlı günlük dosyalardan parçacıkları yeniden canlandırır, bu nedenle eski/silinmiş parçacıklar atlanır.
  * Yükseltilen girdileri `MEMORY.md` dosyasına ekler.
  * `DREAMS.md` içine bir `## Deep Sleep` özeti yazar ve isteğe bağlı olarak `memory/dreaming/deep/YYYY-MM-DD.md` yazar.

REM fazı

REM fazı örüntüleri ve yansıtıcı sinyalleri çıkarır.

  * Son kısa vadeli izlerden tema ve yansıma özetleri oluşturur.
  * Depolama satır içi çıktı içerdiğinde yönetilen bir `## REM Sleep` bloğu yazar.
  * Deep sıralaması tarafından kullanılan REM pekiştirme sinyallerini kaydeder.
  * `MEMORY.md` dosyasına asla yazmaz.


## Oturum dökümü içe alma

Dreaming, düzeltilmiş oturum dökümlerini Dreaming derlemine içe alabilir. Dökümler mevcut olduğunda, günlük bellek sinyalleri ve geri çağırma izleriyle birlikte light fazına beslenir. Kişisel ve hassas içerik içe almadan önce düzeltilir.

## Dream Diary

Dreaming ayrıca `DREAMS.md` içinde anlatı biçiminde bir **Dream Diary** tutar. Her faz yeterli malzemeye sahip olduktan sonra, `memory-core` en iyi çaba yaklaşımıyla arka planda bir alt ajan turu çalıştırır ve kısa bir günlük girdisi ekler. `dreaming.model` yapılandırılmadıkça varsayılan çalışma zamanı modelini kullanır. Yapılandırılan model kullanılamıyorsa Dream Diary oturumun varsayılan modeliyle bir kez yeniden dener.

İnceleme ve kurtarma çalışmaları için temellendirilmiş bir geçmiş geri doldurma hattı da vardır:

Geri doldurma komutları

  * `memory rem-harness --path ... --grounded`, geçmiş `YYYY-MM-DD.md` notlarından temellendirilmiş günlük çıktısını önizler.
  * `memory rem-backfill --path ...`, geri alınabilir temellendirilmiş günlük girdilerini `DREAMS.md` içine yazar.
  * `memory rem-backfill --path ... --stage-short-term`, temellendirilmiş kalıcı adayları normal deep fazının zaten kullandığı aynı kısa vadeli kanıt deposuna hazırlar.
  * `memory rem-backfill --rollback` ve `--rollback-short-term`, sıradan günlük girdilerine veya canlı kısa vadeli geri çağırmaya dokunmadan bu hazırlanmış geri doldurma yapıtlarını kaldırır.


Control UI aynı günlük geri doldurma/sıfırlama akışını sunar; böylece temellendirilmiş adayların yükseltmeyi hak edip etmediğine karar vermeden önce sonuçları Dreams sahnesinde inceleyebilirsiniz. Scene ayrıca ayrı bir temellendirilmiş hat gösterir; böylece hangi hazırlanmış kısa vadeli girdilerin geçmiş yeniden oynatmadan geldiğini, hangi yükseltilmiş öğelerin temellendirme öncüllü olduğunu görebilir ve sıradan canlı kısa vadeli duruma dokunmadan yalnızca temellendirilmiş hazırlanmış girdileri temizleyebilirsiniz.

## Deep sıralama sinyalleri

Deep sıralama altı ağırlıklı temel sinyal ve faz pekiştirmesi kullanır:

Sinyal | Ağırlık | Açıklama  
---|---|---  
Sıklık | 0.24 | Girdinin biriktirdiği kısa vadeli sinyal sayısı  
Alaka düzeyi | 0.30 | Girdi için ortalama getirme kalitesi  
Sorgu çeşitliliği | 0.15 | Onu ortaya çıkaran farklı sorgu/gün bağlamları  
Güncellik | 0.15 | Zamana göre azalan tazelik puanı  
Pekiştirme | 0.10 | Çok günlük yinelenme gücü  
Kavramsal zenginlik | 0.06 | Parçacık/yoldan kavram etiketi yoğunluğu  
  
Light ve REM fazı isabetleri `memory/.dreams/phase-signals.json` içinden küçük, güncelliğe göre azalan bir destek ekler.

## Zamanlama

Etkinleştirildiğinde `memory-core`, tam Dreaming taraması için bir Cron işini otomatik yönetir. Her tarama fazları sırayla çalıştırır: light → REM → deep.

Tarama, birincil çalışma zamanı çalışma alanını ve yapılandırılmış ajan çalışma alanlarını içerir; bunlar yola göre tekilleştirilir. Böylece alt ajan çalışma alanı yayılımı ana ajanın `DREAMS.md` dosyasını ve bellek durumunu dışarıda bırakmaz.

Varsayılan tempo davranışı:

Ayar | Varsayılan  
---|---  
`dreaming.frequency` | `0 3 * * *`  
`dreaming.model` | varsayılan model  
  
## Hızlı başlangıç

### Dreaming’i etkinleştir

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true          }        }      }    }  }}
[/code]

### Özel tarama temposu

jsonCopy code
[code]
    {  "plugins": {    "entries": {      "memory-core": {        "config": {          "dreaming": {            "enabled": true,            "timezone": "America/Los_Angeles",            "frequency": "0 */6 * * *"          }        }      }    }  }}
[/code]

## Eğik çizgi komutu

CodeCopy code
[code]
    /dreaming status/dreaming on/dreaming off/dreaming help
[/code]

## CLI iş akışı

### Yükseltme önizlemesi / uygulama

bashCopy code
[code]
    openclaw memory promoteopenclaw memory promote --applyopenclaw memory promote --limit 5openclaw memory status --deep
[/code]

Elle `memory promote`, CLI bayraklarıyla geçersiz kılınmadıkça varsayılan olarak deep fazı eşiklerini kullanır.

### Yükseltmeyi açıkla

Belirli bir adayın neden yükseltilip yükseltilmeyeceğini açıklayın:

bashCopy code
[code]
    openclaw memory promote-explain "router vlan"openclaw memory promote-explain "router vlan" --json
[/code]

### REM harness önizlemesi

Hiçbir şey yazmadan REM yansımalarını, aday doğruları ve deep yükseltme çıktısını önizleyin:

bashCopy code
[code]
    openclaw memory rem-harnessopenclaw memory rem-harness --json
[/code]

## Temel varsayılanlar

Tüm ayarlar `plugins.entries.memory-core.config.dreaming` altında bulunur.

Dreaming taramasını etkinleştirin veya devre dışı bırakın.

Tam Dreaming taraması için Cron temposu.

İsteğe bağlı Dream Diary alt ajan modeli geçersiz kılması. Alt ajan `allowedModels` izin listesini de ayarlarken kurallı bir `provider/model` değeri kullanın.

## Dreams UI

Etkinleştirildiğinde Gateway **Dreams** sekmesi şunları gösterir:

  * geçerli Dreaming etkin durumu
  * faz düzeyi durumu ve yönetilen tarama varlığı
  * kısa vadeli, temellendirilmiş, sinyal ve bugün yükseltilen sayıları
  * bir sonraki zamanlanmış çalıştırma zamanı
  * hazırlanmış geçmiş yeniden oynatma girdileri için ayrı bir temellendirilmiş Scene hattı
  * `doctor.memory.dreamDiary` tarafından desteklenen genişletilebilir Dream Diary okuyucusu


## Dreaming asla çalışmıyor: durum engellendi gösteriyor

`openclaw memory status`, `Dreaming status: blocked` bildirirse yönetilen Cron vardır ancak varsayılan ajan Heartbeat tetiklenmiyordur. Varsayılan ajan için Heartbeat’in etkin olduğunu ve hedefinin `none` olmadığını kontrol edin, ardından bir sonraki Heartbeat aralığından sonra `openclaw memory status --deep` komutunu yeniden çalıştırın.

## İlgili

  * [Bellek](</tr/concepts/memory>)
  * [Bellek CLI](</tr/cli/memory>)
  * [Bellek yapılandırma başvurusu](</tr/reference/memory-config>)
  * [Bellek arama](</tr/concepts/memory-search>)


Was this useful?YesNo