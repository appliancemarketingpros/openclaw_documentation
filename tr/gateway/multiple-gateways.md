---
title: Birden fazla Gateway
source_url: https://docs.openclaw.ai/tr/gateway/multiple-gateways
scraped_at: 2026-05-25
---

Çoğu kurulum tek bir Gateway kullanmalıdır çünkü tek bir Gateway birden fazla mesajlaşma bağlantısını ve agent'ı yönetebilir. Daha güçlü izolasyon veya yedeklilik gerekiyorsa (ör. bir kurtarma botu), izole profiller/portlarla ayrı Gateway'ler çalıştırın.

## En çok önerilen kurulum

Çoğu kullanıcı için en basit kurtarma botu kurulumu şudur:

  * ana botu varsayılan profilde tutun
  * kurtarma botunu `--profile rescue` ile çalıştırın
  * kurtarma hesabı için tamamen ayrı bir Telegram botu kullanın
  * kurtarma botunu `19789` gibi farklı bir taban portta tutun


Bu, kurtarma botunu ana bottan izole tutar; böylece birincil bot kapalıysa hata ayıklayabilir veya yapılandırma değişiklikleri uygulayabilir. Türetilmiş tarayıcı/canvas/CDP portlarının asla çakışmaması için taban portlar arasında en az 20 port bırakın.

## Kurtarma Botu Hızlı Başlangıç

Başka bir şey yapmak için güçlü bir nedeniniz yoksa bunu varsayılan yol olarak kullanın:

bashCopy code
[code]
    # Rescue bot (separate Telegram bot, separate profile, port 19789)openclaw --profile rescue onboardopenclaw --profile rescue gateway install --port 19789
[/code]

Ana botunuz zaten çalışıyorsa, genellikle ihtiyacınız olan tek şey budur.

`openclaw --profile rescue onboard` sırasında:

  * ayrı Telegram bot token'ını kullanın
  * `rescue` profilini koruyun
  * ana bottan en az 20 daha yüksek bir taban port kullanın
  * zaten kendiniz yönetmiyorsanız varsayılan kurtarma çalışma alanını kabul edin


Onboarding kurtarma hizmetini sizin için zaten kurduysa, son `gateway install` gerekli değildir.

## Bu neden çalışır?

Kurtarma botu bağımsız kalır çünkü kendine ait şunları vardır:

  * profil/yapılandırma
  * durum dizini
  * çalışma alanı
  * taban port (artı türetilmiş portlar)
  * Telegram bot token'ı


Çoğu kurulum için kurtarma profili adına tamamen ayrı bir Telegram botu kullanın:

  * yalnızca operatörlere özel tutması kolaydır
  * ayrı bot token'ı ve kimliği
  * ana botun kanal/uygulama kurulumundan bağımsızdır
  * ana bot bozulduğunda basit DM tabanlı kurtarma yolu sunar


## `--profile rescue onboard` Neleri Değiştirir?

`openclaw --profile rescue onboard` normal onboarding akışını kullanır, ancak her şeyi ayrı bir profile yazar.

Pratikte bu, kurtarma botunun kendine ait şunları aldığı anlamına gelir:

  * yapılandırma dosyası
  * durum dizini
  * çalışma alanı (varsayılan olarak `~/.openclaw/workspace-rescue`)
  * yönetilen hizmet adı


İstemler bunun dışında normal onboarding ile aynıdır.

## Genel çoklu Gateway kurulumu

Yukarıdaki kurtarma botu düzeni en kolay varsayılandır, ancak aynı izolasyon modeli tek bir makinedeki herhangi bir Gateway çifti veya grubu için çalışır.

Daha genel bir kurulum için her ek Gateway'e kendi adlandırılmış profilini ve kendi taban portunu verin:

bashCopy code
[code]
    # main (default profile)openclaw setupopenclaw gateway --port 18789 # extra gatewayopenclaw --profile ops setupopenclaw --profile ops gateway --port 19789
[/code]

Her iki Gateway'in de adlandırılmış profiller kullanmasını istiyorsanız bu da çalışır:

bashCopy code
[code]
    openclaw --profile main setupopenclaw --profile main gateway --port 18789 openclaw --profile ops setupopenclaw --profile ops gateway --port 19789
[/code]

Hizmetler de aynı kalıbı izler:

bashCopy code
[code]
    openclaw gateway installopenclaw --profile ops gateway install --port 19789
[/code]

Bir yedek operatör hattı istediğinizde kurtarma botu hızlı başlangıcını kullanın. Farklı kanallar, kiracılar, çalışma alanları veya operasyonel roller için uzun ömürlü birden fazla Gateway istediğinizde genel profil kalıbını kullanın.

## İzolasyon kontrol listesi

Bunları her Gateway örneği için benzersiz tutun:

  * `OPENCLAW_CONFIG_PATH` — örnek başına yapılandırma dosyası
  * `OPENCLAW_STATE_DIR` — örnek başına oturumlar, kimlik bilgileri, önbellekler
  * `agents.defaults.workspace` — örnek başına çalışma alanı kökü
  * `gateway.port` (veya `--port`) — örnek başına benzersiz
  * türetilmiş tarayıcı/canvas/CDP portları


Bunlar paylaşılırsa yapılandırma yarışları ve port çakışmaları yaşarsınız.

## Port eşlemesi (türetilmiş)

Taban port = `gateway.port` (veya `OPENCLAW_GATEWAY_PORT` / `--port`).

  * tarayıcı kontrol hizmeti portu = taban + 2 (yalnızca local loopback)
  * canvas host'u Gateway HTTP sunucusunda sunulur (`gateway.port` ile aynı port)
  * Tarayıcı profili CDP portları `browser.controlPort + 9 .. + 108` aralığından otomatik ayrılır


Bunlardan herhangi birini yapılandırmada veya ortam değişkenlerinde geçersiz kılarsanız, her örnek için benzersiz tutmanız gerekir.

## Tarayıcı/CDP notları (yaygın hata kaynağı)

  * `browser.cdpUrl` değerini birden fazla örnekte aynı değerlere **sabitlemeyin**.
  * Her örneğin kendi tarayıcı kontrol portuna ve CDP aralığına ihtiyacı vardır (gateway portundan türetilir).
  * Açık CDP portlarına ihtiyacınız varsa, örnek başına `browser.profiles.<name>.cdpPort` değerini ayarlayın.
  * Uzak Chrome: `browser.profiles.<name>.cdpUrl` kullanın (profil başına, örnek başına).


## Manuel env örneği

bashCopy code
[code]
    OPENCLAW_CONFIG_PATH=~/.openclaw/main.json \OPENCLAW_STATE_DIR=~/.openclaw \openclaw gateway --port 18789 OPENCLAW_CONFIG_PATH=~/.openclaw/rescue.json \OPENCLAW_STATE_DIR=~/.openclaw-rescue \openclaw gateway --port 19789
[/code]

## Hızlı kontroller

bashCopy code
[code]
    openclaw gateway status --deepopenclaw --profile rescue gateway status --deepopenclaw --profile rescue gateway probeopenclaw statusopenclaw --profile rescue statusopenclaw --profile rescue browser status
[/code]

Yorumlama:

  * `gateway status --deep`, eski kurulumlardan kalma bayat launchd/systemd/schtasks hizmetlerini yakalamaya yardımcı olur.
  * `multiple reachable gateways detected` gibi `gateway probe` uyarı metni yalnızca bilerek birden fazla izole gateway çalıştırdığınızda beklenir.


## İlgili

  * [Gateway runbook](</tr/gateway>)
  * [Gateway kilidi](</tr/gateway/gateway-lock>)
  * [Yapılandırma](</tr/gateway/configuration>)


Was this useful?YesNo