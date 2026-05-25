---
title: Kontrol Paneli
source_url: https://docs.openclaw.ai/tr/cli/dashboard
scraped_at: 2026-05-25
---

# `openclaw dashboard`

Geçerli kimlik doğrulamanızı kullanarak Kontrol UI'sını açın.

bashCopy code
[code]
    openclaw dashboardopenclaw dashboard --no-open
[/code]

Notlar:

  * `dashboard`, mümkün olduğunda yapılandırılmış `gateway.auth.token` SecretRef'lerini çözer.
  * `dashboard`, `gateway.tls.enabled` ayarını izler: TLS etkin Gateway'ler `https://` Kontrol UI URL'lerini yazdırır/açar ve `wss://` üzerinden bağlanır.
  * Belirteçle kimliği doğrulanmış bir dashboard URL'si için pano/tarayıcı iletimi başarısız olursa, `dashboard`, belirteç değerini yazdırmadan `OPENCLAW_GATEWAY_TOKEN`, `gateway.auth.token` ve parça anahtarı `token` adlarını içeren güvenli bir manuel kimlik doğrulama ipucu kaydeder.
  * SecretRef tarafından yönetilen belirteçler için (çözülmüş veya çözülmemiş), `dashboard` dış sırların terminal çıktısında, pano geçmişinde veya tarayıcı başlatma argümanlarında açığa çıkmasını önlemek için belirteçsiz bir URL yazdırır/kopyalar/açar.
  * `gateway.auth.token` SecretRef tarafından yönetiliyorsa ancak bu komut yolunda çözülemiyorsa, komut geçersiz bir belirteç yer tutucusu gömmek yerine belirteçsiz bir URL ve açık düzeltme rehberliği yazdırır.


## İlgili

  * [CLI başvurusu](</tr/cli>)
  * [Dashboard](</tr/web/dashboard>)


Was this useful?YesNo